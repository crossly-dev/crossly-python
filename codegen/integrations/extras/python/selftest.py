"""Exercise the facade and the framework middleware against the REAL generated clients.

    python codegen/integrations/extras/python/selftest.py

Copies the generated seller/crossly and buyer/crossly_buyer packages to a temp dir, overlays this directory's
client.py and frameworks.py and the webhook verifier exactly as the release vendors them, then checks against a
local stub server: retry on 429 honouring Retry-After, bearer token, User-Agent, timeouts passed down, pagination,
no retry of a POST on 503, the Idempotency-Key, typed errors; and Flask, Django, FastAPI and raw ASGI verification
with real signatures. Run in CI after `pip install flask django fastapi httpx`; exit 1 on any failure.
"""
import hashlib
import hmac
import json
import shutil
import sys
import tempfile
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
VERIFIER = REPO / "codegen" / "integrations" / "webhooks" / "python" / "crossly_webhooks.py"

failures = 0


def check(ok, what):
    global failures
    print("  {} {}".format("ok  " if ok else "FAIL", what))
    if not ok:
        failures += 1


# ── assemble the packages as the release does ────────────────────────────────────────────────────────────────
tmp = Path(tempfile.mkdtemp(prefix="crossly-selftest-"))
for part, pkg in (("seller", "crossly"), ("buyer", "crossly_buyer")):
    shutil.copytree(REPO / part / pkg, tmp / pkg, ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copy(HERE / "client.py", tmp / pkg / "client.py")
    shutil.copy(HERE / "frameworks.py", tmp / pkg / "frameworks.py")
    shutil.copy(VERIFIER, tmp / pkg / "webhooks.py")
sys.path.insert(0, str(tmp))

import crossly  # noqa: E402
from crossly.client import Crossly, CrosslyError, NotFoundError, RateLimitError, ServerError  # noqa: E402
import crossly_buyer.client  # noqa: E402,F401  (the buyer copy imports cleanly too)

# ── stub API ─────────────────────────────────────────────────────────────────────────────────────────────────
seen = []
hits = {"mileage": 0}


def mileage(i):
    return {"id": "m{}".format(i), "date": "2026-01-0{}".format(i), "createdAt": "2026-01-01T00:00:00Z",
            "userId": "u1", "miles": "12.5", "purpose": "sourcing"}


class Stub(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, status, payload, headers=None):
        raw = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(raw)

    def _record(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n:
            self.rfile.read(n)
        seen.append((self.command, self.path, {k.lower(): v for k, v in self.headers.items()}))

    def do_GET(self):
        self._record()
        if self.path.startswith("/api/v1/mileage"):
            hits["mileage"] += 1
            if hits["mileage"] == 1:
                return self._send(429, {"error": {"code": "rate_limited", "message": "slow down"}, "correlationId": "c0"},
                                  {"Retry-After": "0"})
            if "page=2" in self.path:
                return self._send(200, {"data": [mileage(3)], "pagination": {"page": 2, "limit": 2, "totalPages": 2}})
            return self._send(200, {"data": [mileage(1), mileage(2)], "pagination": {"page": 1, "limit": 2, "totalPages": 2}})
        if self.path.startswith("/api/v1/listings/missing"):
            return self._send(404, {"error": {"code": "not_found", "message": "no such listing"}, "correlationId": "c404"})
        return self._send(404, {"error": {"code": "not_found", "message": "?"}})

    def do_POST(self):
        self._record()
        if self.path == "/api/v1/listings/l1/magic-fill":
            return self._send(503, {"error": {"code": "unavailable", "message": "try later", "details": {"x": 1}},
                                    "correlationId": "corr_1"})
        return self._send(404, {"error": {"code": "not_found", "message": "?"}})


server = ThreadingHTTPServer(("127.0.0.1", 0), Stub)
threading.Thread(target=server.serve_forever, daemon=True).start()
base = "http://127.0.0.1:{}/api".format(server.server_address[1])

# ── facade ───────────────────────────────────────────────────────────────────────────────────────────────────
print("facade")
c = Crossly("crossly_pat_test", base_url=base, backoff=0.01, timeout=5)
check(type(c.tax).__name__ == "TaxApi" and type(c.tax).__module__ == "crossly.api.tax_api", "crossly.tax is TaxApi")
check(c.tax.api_client is c.api_client, "the API shares the configured client")

first = c.tax.list_mileage(page=1, limit=2)
check(hits["mileage"] == 2, "429 then 200: retried once (hits={})".format(hits["mileage"]))
check([m.id for m in first.data] == ["m1", "m2"], "decoded the generated ListMileageResponse")
h = seen[-1][2]
check(h.get("authorization") == "Bearer crossly_pat_test", "bearer token sent")
check(h.get("user-agent") == "crossly-python/{}".format(crossly.__version__), "User-Agent {}".format(h.get("user-agent")))
check("idempotency-key" not in h, "no Idempotency-Key on GET")

ids = [m.id for m in c.iter_items(c.tax.list_mileage, limit=2)]
check(ids == ["m1", "m2", "m3"], "iter_items walked totalPages: {}".format(ids))
pages = list(c.iter_pages(c.tax.list_mileage, limit=2))
check(len(pages) == 2, "iter_pages yielded 2 pages")

before = len(seen)
try:
    c.listings.create_listing_magic_fill("l1")
    check(False, "POST 503 should raise")
except ServerError as e:
    check(len(seen) - before == 1, "POST not retried on 503 (attempts={})".format(len(seen) - before))
    check(isinstance(e, crossly.ApiException) and isinstance(e, CrosslyError), "ServerError is a crossly.ApiException")
    check(e.status == 503 and e.code == "unavailable" and e.message == "try later", "status/code/message: {}".format(e))
    check(e.correlation_id == "corr_1" and e.details == {"x": 1}, "correlation_id + details")
key = seen[-1][2].get("idempotency-key", "")
check(len(key) == 36, "Idempotency-Key on POST: {}".format(key))

try:
    c.listings.get_listing("missing")
    check(False, "404 should raise")
except NotFoundError as e:
    from crossly.exceptions import NotFoundException

    check(isinstance(e, NotFoundException), "NotFoundError is the generated NotFoundException too")
    check(e.code == "not_found" and e.correlation_id == "c404", "404 parsed: {}".format(e))
except Exception as e:  # noqa: BLE001
    check(False, "404 raised {!r}".format(e))

r = RateLimitError(status=429, reason="Too Many Requests")
r.headers = {"Retry-After": "7"}
check(r.retry_after == 7.0, "retry_after from Retry-After")

# ── webhooks in each framework ───────────────────────────────────────────────────────────────────────────────
SECRET = "whsec_selftest"
BODY = json.dumps({"id": "evt_1", "type": "listing.sold", "created": "2026-01-01T00:00:00Z", "data": {"x": 1}})


def sign(body, secret=SECRET, t=None):
    t = int(time.time()) if t is None else t
    mac = hmac.new(secret.encode(), "{}.{}".format(t, body).encode(), hashlib.sha256).hexdigest()
    return "t={},v1={}".format(t, mac)


from crossly.frameworks import CrosslyWebhookMiddleware, django_webhook, fastapi_webhook, flask_webhook  # noqa: E402

print("flask")
import flask  # noqa: E402

fapp = flask.Flask("selftest")


@fapp.post("/hook")
@flask_webhook(secret=SECRET)
def fhook(event):
    return event.type, 200


fc = fapp.test_client()
resp = fc.post("/hook", data=BODY, headers={"Crossly-Signature": sign(BODY)})
check(resp.status_code == 200 and resp.data == b"listing.sold", "valid signature reaches the view")
resp = fc.post("/hook", data=BODY + " ", headers={"Crossly-Signature": sign(BODY)})
check(resp.status_code == 400 and resp.data == b"bad_signature", "tampered body: 400 bad_signature")

print("django")
from django.conf import settings  # noqa: E402

settings.configure(DEBUG=True, SECRET_KEY="x", ALLOWED_HOSTS=["*"], ROOT_URLCONF=__name__)
import django  # noqa: E402

django.setup()
from django.http import HttpResponse  # noqa: E402
from django.test import RequestFactory  # noqa: E402


@django_webhook(secret=SECRET)
def dhook(request, event):
    return HttpResponse(event.id)


rf = RequestFactory()
resp = dhook(rf.post("/hook", data=BODY, content_type="application/json", HTTP_CROSSLY_SIGNATURE=sign(BODY)))
check(resp.status_code == 200 and resp.content == b"evt_1", "valid signature reaches the view")
resp = dhook(rf.post("/hook", data=BODY, content_type="application/json",
                     HTTP_CROSSLY_SIGNATURE=sign(BODY, t=int(time.time()) - 3600)))
check(resp.status_code == 400 and resp.content == b"timestamp_out_of_tolerance", "an hour old: 400")
check(getattr(dhook, "csrf_exempt", False) is True, "CSRF-exempt")

print("fastapi")
from fastapi import Depends, FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from starlette.requests import Request as StarletteRequest  # noqa: E402

api = FastAPI()


@api.post("/hook")
async def ahook(event=Depends(fastapi_webhook(secret=SECRET))):
    return {"type": event.type}


@api.post("/raw")
async def raw(request: StarletteRequest):
    return {"state": request.state.crossly_event.id, "body": (await request.body()).decode()}


api.add_middleware(CrosslyWebhookMiddleware, path="/raw", secret=SECRET)
tc = TestClient(api)
resp = tc.post("/hook", content=BODY, headers={"Crossly-Signature": sign(BODY)})
check(resp.status_code == 200 and resp.json() == {"type": "listing.sold"}, "dependency: valid signature")
resp = tc.post("/hook", content=BODY, headers={"Crossly-Signature": "garbage"})
check(resp.status_code == 400 and resp.json().get("detail") == "malformed_header", "dependency: malformed header 400")
resp = tc.post("/raw", content=BODY, headers={"Crossly-Signature": sign(BODY)})
check(resp.status_code == 200 and resp.json() == {"state": "evt_1", "body": BODY}, "ASGI middleware: state + replayed body")
resp = tc.post("/raw", content=BODY, headers={"Crossly-Signature": sign(BODY, secret="other")})
check(resp.status_code == 400 and resp.text == "bad_signature", "ASGI middleware: wrong secret 400")

server.shutdown()
shutil.rmtree(tmp, ignore_errors=True)
print("python facade + frameworks: {}".format("all checks passed" if not failures else "{} FAILED".format(failures)))
sys.exit(1 if failures else 0)
