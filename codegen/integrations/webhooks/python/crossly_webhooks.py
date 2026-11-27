"""Verify a Crossly webhook.

    Crossly-Signature: t=<unix seconds>,v1=<hex HMAC-SHA256>

signed over ``f"{t}.{raw_body}"`` with the endpoint's signing secret.

Three ways to get this wrong, all of them silent:

1. Verifying a re-serialised body. ``json.loads`` then ``json.dumps`` does not
   round-trip byte for byte — key order and float formatting both drift — so
   genuine payloads fail and the usual fix somebody reaches for is to stop
   verifying. Pass the raw bytes.
2. Comparing with ``==``. Python's string compare returns early on the first
   differing byte; ``hmac.compare_digest`` does not.
3. Ignoring the timestamp. Without it a captured request replays forever and
   "the signature was valid" is true every time. The timestamp is INSIDE the
   signed message, so it cannot be edited to look fresh.

No third-party dependencies — stdlib only.
"""

from __future__ import annotations

import hmac
import json
import time
from dataclasses import dataclass
from hashlib import sha256
from typing import Any

__all__ = ["verify_webhook", "WebhookVerificationError", "WebhookEvent"]

DEFAULT_TOLERANCE_SECONDS = 300


class WebhookVerificationError(Exception):
    """Raised when a webhook does not verify.

    Carries a machine-readable ``reason`` so a caller can tell a forged request
    from a clock problem — those want different responses and different alerts.
    """

    def __init__(self, reason: str, message: str) -> None:
        super().__init__(message)
        self.reason = reason


@dataclass(frozen=True)
class WebhookEvent:
    id: str
    type: str
    created: str
    data: Any


def _parse_signature_header(header: str) -> tuple[int, str] | None:
    """Pull ``t`` and ``v1`` out of the header.

    Parsed field-wise rather than with one regex so that a future ``v2=``
    alongside ``v1=`` does not break existing verifiers — which is the entire
    reason the scheme carries a version.
    """
    t: int | None = None
    v1: str | None = None

    for part in header.split(","):
        key, sep, value = part.partition("=")
        if not sep:
            continue
        key = key.strip()
        value = value.strip()
        if key == "t":
            try:
                t = int(value)
            except ValueError:
                return None
        elif key == "v1":
            v1 = value

    if t is None or not v1:
        return None
    return t, v1


def verify_webhook(
    raw_body: str | bytes,
    signature_header: str | None,
    secret: str,
    *,
    tolerance_seconds: int = DEFAULT_TOLERANCE_SECONDS,
    now: int | None = None,
) -> WebhookEvent:
    """Verify a webhook and return the parsed event.

    :param raw_body: The EXACT bytes received. In Flask use ``request.get_data()``;
        in Django ``request.body``; in FastAPI ``await request.body()``. Never
        ``json.dumps(request.json)``.
    :param signature_header: The ``Crossly-Signature`` header, verbatim.
    :param secret: The endpoint's signing secret, from Settings → Webhooks.
    :raises WebhookVerificationError: on anything that does not verify. It
        raises rather than returning ``False`` so a caller who forgets to check
        a return value does not silently accept forged events.
    """
    if not secret:
        raise WebhookVerificationError(
            "missing_secret", "A webhook signing secret is required."
        )
    if not signature_header:
        raise WebhookVerificationError(
            "malformed_header", "No Crossly-Signature header on the request."
        )

    parsed = _parse_signature_header(signature_header)
    if parsed is None:
        raise WebhookVerificationError(
            "malformed_header",
            'Could not parse Crossly-Signature: expected "t=<unix>,v1=<hex>", '
            f'got "{signature_header[:60]}".',
        )
    timestamp, provided = parsed

    body = raw_body.decode("utf-8") if isinstance(raw_body, bytes) else raw_body
    expected = hmac.new(
        secret.encode("utf-8"), f"{timestamp}.{body}".encode("utf-8"), sha256
    ).hexdigest()

    # compare_digest, not ==. It also handles the length mismatch of a
    # truncated signature without leaking where the difference is.
    if not hmac.compare_digest(expected, provided):
        raise WebhookVerificationError(
            "bad_signature",
            "Signature did not match. If genuine payloads are failing, you are almost "
            "certainly verifying a re-serialised body — pass the raw bytes, not "
            "json.dumps(request.json).",
        )

    # Freshness is checked AFTER the signature so an attacker cannot learn
    # anything about timestamps without already holding a valid signature.
    current = int(time.time()) if now is None else now
    drift = abs(current - timestamp)
    if drift > tolerance_seconds:
        raise WebhookVerificationError(
            "timestamp_out_of_tolerance",
            f"Timestamp is {drift}s away from now (tolerance {tolerance_seconds}s). "
            "This is a replay guard — if it fires on live traffic, check your server clock.",
        )

    payload = json.loads(body)
    return WebhookEvent(
        id=payload["id"],
        type=payload["type"],
        created=payload["created"],
        data=payload.get("data"),
    )
