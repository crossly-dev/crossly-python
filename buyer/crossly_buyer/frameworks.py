"""Crossly webhook verification for Flask, Django, FastAPI and any ASGI app (Starlette, Quart, …).

Each helper verifies ``Crossly-Signature`` over the exact bytes received, before anything parses them, and hands
the view the verified :class:`WebhookEvent`. A request that does not verify gets 400 with the stable reason
(``bad_signature``, ``timestamp_out_of_tolerance``, ``malformed_header``); a missing secret is a server
misconfiguration and gets 500. The secret defaults to the ``CROSSLY_WEBHOOK_SECRET`` environment variable.

No framework is a dependency: each one is imported only when its helper is used.

Flask::

    from crossly.frameworks import flask_webhook

    @app.post("/webhooks/crossly")
    @flask_webhook()
    def crossly_webhook(event):
        print(event.type, event.data)
        return "", 204

Django (CSRF-exempt, since the signature is the authentication)::

    from crossly.frameworks import django_webhook

    @django_webhook()
    def crossly_webhook(request, event):
        return HttpResponse(status=204)

FastAPI::

    from fastapi import Depends
    from crossly.frameworks import fastapi_webhook

    @app.post("/webhooks/crossly", status_code=204)
    async def crossly_webhook(event=Depends(fastapi_webhook())):
        ...

Any ASGI app (the event lands in ``scope["state"]["crossly_event"]``, i.e. ``request.state.crossly_event``)::

    app.add_middleware(CrosslyWebhookMiddleware, path="/webhooks/crossly")      # Starlette / FastAPI

Hand-written (tools/sdk-repo/extras/python in the Crossly monorepo) and vendored into the package on every release.
"""

import functools
import os

from .webhooks import DEFAULT_TOLERANCE_SECONDS, WebhookVerificationError, verify_webhook

__all__ = ["flask_webhook", "django_webhook", "fastapi_webhook", "CrosslyWebhookMiddleware"]

SIGNATURE_HEADER = "Crossly-Signature"


def _secret(secret):
    return secret if secret is not None else os.environ.get("CROSSLY_WEBHOOK_SECRET", "")


def _status(error):
    return 500 if error.reason == "missing_secret" else 400


def flask_webhook(secret=None, tolerance_seconds=DEFAULT_TOLERANCE_SECONDS):
    """Decorate a Flask view; it is called as ``view(event, **url_params)``."""

    def decorator(view):
        @functools.wraps(view)
        def wrapper(*args, **kwargs):
            from flask import Response, request

            try:
                event = verify_webhook(
                    request.get_data(cache=True), request.headers.get(SIGNATURE_HEADER), _secret(secret),
                    tolerance_seconds=tolerance_seconds,
                )
            except WebhookVerificationError as e:
                return Response(e.reason, status=_status(e), mimetype="text/plain")
            return view(event, *args, **kwargs)

        return wrapper

    return decorator


def django_webhook(secret=None, tolerance_seconds=DEFAULT_TOLERANCE_SECONDS):
    """Decorate a Django function view; it is called as ``view(request, event, *args, **kwargs)``. CSRF-exempt."""

    def decorator(view):
        from django.http import HttpResponse
        from django.views.decorators.csrf import csrf_exempt
        from django.views.decorators.http import require_POST

        @functools.wraps(view)
        def wrapper(request, *args, **kwargs):
            try:
                event = verify_webhook(
                    request.body, request.META.get("HTTP_CROSSLY_SIGNATURE"), _secret(secret),
                    tolerance_seconds=tolerance_seconds,
                )
            except WebhookVerificationError as e:
                return HttpResponse(e.reason, status=_status(e), content_type="text/plain")
            return view(request, event, *args, **kwargs)

        return csrf_exempt(require_POST(wrapper))

    return decorator


def fastapi_webhook(secret=None, tolerance_seconds=DEFAULT_TOLERANCE_SECONDS):
    """A FastAPI dependency returning the verified event: ``event = Depends(fastapi_webhook())``."""
    from fastapi import HTTPException, Request

    async def crossly_webhook_event(request: Request):
        raw = await request.body()
        try:
            return verify_webhook(
                raw, request.headers.get(SIGNATURE_HEADER), _secret(secret), tolerance_seconds=tolerance_seconds
            )
        except WebhookVerificationError as e:
            raise HTTPException(status_code=_status(e), detail=e.reason)

    return crossly_webhook_event


class CrosslyWebhookMiddleware:
    """Pure ASGI middleware: verifies requests to ``path`` and stores the event in ``scope["state"]``.

    The body is buffered (up to ``max_body_bytes``, else 413), verified, then replayed to the app, which can read it
    again as usual.
    """

    def __init__(self, app, path, secret=None, tolerance_seconds=DEFAULT_TOLERANCE_SECONDS, max_body_bytes=1 << 20):
        self.app = app
        self.path = path
        self.secret = secret
        self.tolerance_seconds = tolerance_seconds
        self.max_body_bytes = max_body_bytes

    async def __call__(self, scope, receive, send):
        if scope.get("type") != "http" or scope.get("path") != self.path:
            await self.app(scope, receive, send)
            return
        chunks = []
        size = 0
        more = True
        while more:
            message = await receive()
            if message["type"] == "http.disconnect":
                return
            chunk = message.get("body", b"")
            size += len(chunk)
            if size > self.max_body_bytes:
                await self._reply(send, 413, "payload_too_large")
                return
            chunks.append(chunk)
            more = message.get("more_body", False)
        raw = b"".join(chunks)
        header = None
        for key, value in scope.get("headers") or []:
            if key.lower() == b"crossly-signature":
                header = value.decode("latin-1")
                break
        try:
            event = verify_webhook(raw, header, _secret(self.secret), tolerance_seconds=self.tolerance_seconds)
        except WebhookVerificationError as e:
            await self._reply(send, _status(e), e.reason)
            return

        scope = dict(scope)
        state = dict(scope.get("state") or {})
        state["crossly_event"] = event
        scope["state"] = state
        replayed = False

        async def replay():
            nonlocal replayed
            if not replayed:
                replayed = True
                return {"type": "http.request", "body": raw, "more_body": False}
            return await receive()

        await self.app(scope, replay, send)

    @staticmethod
    async def _reply(send, status, text):
        body = text.encode("utf-8")
        await send({
            "type": "http.response.start",
            "status": status,
            "headers": [(b"content-type", b"text/plain; charset=utf-8"), (b"content-length", str(len(body)).encode())],
        })
        await send({"type": "http.response.body", "body": body})
