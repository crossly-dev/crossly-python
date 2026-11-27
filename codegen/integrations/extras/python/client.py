"""The ergonomic Crossly client: one object over the generated API classes.

    from crossly.client import Crossly

    crossly = Crossly(os.environ["CROSSLY_TOKEN"])          # crossly_pat_… or crossly_oat_…
    page = crossly.listings.list_listings(page=1, limit=25)   # = crossly.api.listings_api.ListingsApi
    for listing in crossly.iter_items(crossly.listings.list_listings):
        print(listing.id)

``crossly.<area>`` is the generated ``crossly.api.<area>_api.<Area>Api`` bound to one shared, configured
``ApiClient``; every call made through it gets:

- the bearer token, a ``crossly-python/<version>`` User-Agent and a default timeout;
- retries with exponential backoff and jitter, honouring ``Retry-After``: on 429 for every method, on 5xx and
  network errors for GET, HEAD, OPTIONS, PUT and DELETE, and for POST and PATCH only with ``retry_writes=True``
  (only some endpoints deduplicate on the Idempotency-Key, so a retried create could create twice);
- an ``Idempotency-Key`` on every POST, PUT, PATCH and DELETE, the same on each retry of that call;
- typed errors: :class:`CrosslyError` (a ``crossly.ApiException``) with ``code``, ``message``, ``details``,
  ``correlation_id`` and ``retry_after``; 401/403/404/429/5xx raise its subclasses, which are also the generated
  ``UnauthorizedException`` / ``ForbiddenException`` / ``NotFoundException`` / ``ServiceException``.

Hand-written (tools/sdk-repo/extras/python in the Crossly monorepo) and vendored into the package on every
release; it changes nothing in the generated code. Standard library only.
"""

import email.utils
import importlib
import json
import random
import time
import uuid

from . import __version__
from .api_client import ApiClient
from .configuration import Configuration
from .exceptions import (
    ApiException,
    ForbiddenException,
    NotFoundException,
    ServiceException,
    UnauthorizedException,
)

__all__ = [
    "Crossly",
    "CrosslyApiClient",
    "CrosslyError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "RateLimitError",
    "ServerError",
]

_PACKAGE = __name__.rsplit(".", 1)[0]
_WRITES = frozenset(("POST", "PUT", "PATCH", "DELETE"))
_UNSAFE = frozenset(("POST", "PATCH"))
_TRANSIENT_5XX = frozenset((500, 502, 503, 504))


def _header(headers, name):
    if not headers:
        return None
    try:
        value = headers.get(name)
    except AttributeError:
        value = None
    if value is not None:
        return value
    lower = name.lower()
    for k, v in dict(headers).items():
        if k.lower() == lower:
            return v
    return None


def parse_retry_after(value):
    """Seconds from a ``Retry-After`` header (delta-seconds or an HTTP date); None when absent or unreadable."""
    if value is None:
        return None
    value = str(value).strip()
    if not value:
        return None
    try:
        return max(0.0, float(value))
    except ValueError:
        pass
    try:
        when = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError, IndexError):
        return None
    if when is None:
        return None
    return max(0.0, when.timestamp() - time.time())


class CrosslyError(ApiException):
    """A failed call, with the API's ``{"error": {"code", "message", "details"}, "correlationId"}`` parsed.

    Still a ``crossly.ApiException``: ``status``, ``reason``, ``body`` and ``headers`` are there as before.
    """

    def __init__(self, status=None, reason=None, http_resp=None):
        super().__init__(status, reason, http_resp)

    def _payload(self):
        body = self.body
        if isinstance(body, (bytes, bytearray)):
            body = body.decode("utf-8", "replace")
        if not body:
            return {}
        try:
            data = json.loads(body)
        except ValueError:
            return {}
        return data if isinstance(data, dict) else {}

    def _error(self):
        err = self._payload().get("error")
        return err if isinstance(err, dict) else {}

    @property
    def code(self):
        """The API's machine-readable ``error.code`` (e.g. ``not_found``, ``rate_limited``), or None."""
        return self._error().get("code")

    @property
    def message(self):
        err = self._payload().get("error")
        if isinstance(err, dict) and err.get("message"):
            return err["message"]
        if isinstance(err, str):
            return err
        return self.reason or "HTTP {}".format(self.status)

    @property
    def details(self):
        return self._error().get("details")

    @property
    def correlation_id(self):
        """Quote this to support: it threads the request back to server logs."""
        return self._payload().get("correlationId") or _header(self.headers, "X-Correlation-Id")

    @property
    def retry_after(self):
        """Seconds the API asked to wait (``Retry-After``), or None."""
        return parse_retry_after(_header(self.headers, "Retry-After"))

    def __str__(self):
        out = "CrosslyError {}".format(self.status)
        if self.code:
            out += " {}".format(self.code)
        out += ": {}".format(self.message)
        if self.correlation_id:
            out += " (correlationId {})".format(self.correlation_id)
        return out


class AuthenticationError(CrosslyError, UnauthorizedException):
    """401: a missing, expired or wrong token (a seller token on the buyer API, or the reverse)."""


class PermissionDeniedError(CrosslyError, ForbiddenException):
    """403: the token lacks the scope, or the resource belongs to someone else."""


class NotFoundError(CrosslyError, NotFoundException):
    """404."""


class RateLimitError(CrosslyError):
    """429 after every retry; ``retry_after`` says how long the API asked to wait."""


class ServerError(CrosslyError, ServiceException):
    """5xx."""


_BY_STATUS = {401: AuthenticationError, 403: PermissionDeniedError, 404: NotFoundError, 429: RateLimitError}


def _typed(e):
    if isinstance(e, CrosslyError):
        return e
    status = e.status or 0
    cls = _BY_STATUS.get(status) or (ServerError if 500 <= status <= 599 else CrosslyError)
    typed = cls(status=e.status, reason=e.reason)
    typed.body = e.body
    typed.headers = e.headers
    return typed


class CrosslyApiClient(ApiClient):
    """The generated ``ApiClient`` with retries, backoff, timeouts, the Idempotency-Key and typed errors."""

    def __init__(
        self,
        configuration=None,
        timeout=30.0,
        max_retries=3,
        backoff=0.5,
        max_backoff=30.0,
        retry_writes=False,
        user_agent=None,
        **kwargs
    ):
        super().__init__(configuration, **kwargs)
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff = backoff
        self.max_backoff = max_backoff
        self.retry_writes = retry_writes
        self.user_agent = user_agent or "crossly-python/{}".format(__version__)

    def _transient(self, status, method):
        if status == 429:
            return True
        if status in _TRANSIENT_5XX:
            return method not in _UNSAFE or self.retry_writes
        return False

    def _delay(self, attempt, retry_after):
        asked = parse_retry_after(retry_after)
        if asked is not None:
            return min(asked, self.max_backoff)
        ceiling = min(self.max_backoff, self.backoff * (2 ** attempt))
        return random.uniform(ceiling / 2, ceiling)

    def request(self, method, url, query_params=None, headers=None, post_params=None, body=None,
                _preload_content=True, _request_timeout=None):
        verb = method.upper()
        headers = dict(headers or {})
        if verb in _WRITES and not any(k.lower() == "idempotency-key" for k in headers):
            headers["Idempotency-Key"] = str(uuid.uuid4())
        if _request_timeout is None:
            _request_timeout = self.timeout
        attempt = 0
        while True:
            try:
                # A fresh headers dict per attempt: the REST layer edits the one it is given.
                return super().request(
                    method, url, query_params=query_params, headers=dict(headers), post_params=post_params,
                    body=body, _preload_content=_preload_content, _request_timeout=_request_timeout,
                )
            except ApiException as e:
                if attempt >= self.max_retries or not self._transient(e.status, verb):
                    raise _typed(e) from None
                delay = self._delay(attempt, _header(e.headers, "Retry-After"))
            except (OSError, _urllib3_errors()) as e:  # connection refused/reset, read timeout
                if attempt >= self.max_retries or (verb in _UNSAFE and not self.retry_writes):
                    raise
                delay = self._delay(attempt, None)
            time.sleep(delay)
            attempt += 1


def _urllib3_errors():
    import urllib3.exceptions

    return urllib3.exceptions.HTTPError


class Crossly:
    """One configured client; ``crossly.<area>`` is the generated ``<Area>Api`` for ``crossly.api.<area>_api``.

    :param token: a Personal Access Token (``crossly_pat_…``) or an OAuth token (``crossly_oat_…``).
    :param base_url: API root; defaults to the spec's (https://crossly.net/api).
    :param timeout: seconds per attempt (a number, or a ``(connect, read)`` pair).
    :param max_retries: retries after the first attempt; 0 turns retrying off.
    :param backoff: first backoff in seconds; doubles per retry, with jitter, up to ``max_backoff``.
    :param retry_writes: also retry POST and PATCH on 5xx and network errors.
    :param user_agent: replaces ``crossly-python/<version>``.
    """

    def __init__(self, token, base_url=None, timeout=30.0, max_retries=3, backoff=0.5, max_backoff=30.0,
                 retry_writes=False, user_agent=None):
        self.configuration = Configuration(host=base_url, access_token=token)
        self.api_client = CrosslyApiClient(
            self.configuration, timeout=timeout, max_retries=max_retries, backoff=backoff,
            max_backoff=max_backoff, retry_writes=retry_writes, user_agent=user_agent,
        )
        self._apis = {}

    def api(self, area):
        """The generated API class for ``crossly.api.<area>_api``, bound to this client (``crossly.api("tax")``)."""
        if area not in self._apis:
            module_name = "{}.api.{}_api".format(_PACKAGE, area)
            try:
                module = importlib.import_module(module_name)
            except ImportError as e:
                if getattr(e, "name", None) == module_name:
                    raise AttributeError("{} has no API area {!r} (no module {})".format(_PACKAGE, area, module_name))
                raise
            classes = [v for k, v in vars(module).items()
                       if isinstance(v, type) and k.endswith("Api") and v.__module__ == module.__name__]
            if not classes:
                raise AttributeError("no API class in {}".format(module_name))
            self._apis[area] = classes[0](self.api_client)
        return self._apis[area]

    def __getattr__(self, name):
        if name.startswith("_"):
            raise AttributeError(name)
        return self.api(name)

    def iter_pages(self, method, limit=100, **params):
        """Yield each page a paged list method returns, following ``page`` until the last.

        Stops at ``pagination.total_pages`` when the API counts, else at the first short page; an endpoint that
        sends no ``pagination`` returned everything in one page.
        """
        page = int(params.pop("page", 1))
        while True:
            result = method(page=page, limit=limit, **params)
            yield result
            rows = getattr(result, "data", None) or []
            pagination = getattr(result, "pagination", None)
            if not rows or pagination is None:
                return
            total = getattr(pagination, "total_pages", None)
            if total is not None:
                if page >= total:
                    return
            elif len(rows) < limit:
                return
            page += 1

    def iter_items(self, method, limit=100, **params):
        """Yield every row (``data`` item) of a paged list method, across all pages."""
        for result in self.iter_pages(method, limit=limit, **params):
            for row in getattr(result, "data", None) or []:
                yield row

    def close(self):
        self.api_client.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
