"""A minimal Crossly webhook receiver, standard library only.

    pip install crossly
    CROSSLY_WEBHOOK_SECRET=... python webhook_server.py
    # then point a webhook endpoint (Settings → Webhooks) at http://<host>:8080/

The signature is checked over the exact bytes received, before anything parses them.
"""
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from crossly.webhooks import WebhookVerificationError, verify_webhook

SECRET = os.environ["CROSSLY_WEBHOOK_SECRET"]


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        raw = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        try:
            event = verify_webhook(raw, self.headers.get("Crossly-Signature"), SECRET)
        except WebhookVerificationError as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(str(e).encode())
            return
        print(f"{event.type}: {event.data}")
        # Answer fast; do slow work after replying, or Crossly retries the delivery.
        self.send_response(204)
        self.end_headers()


HTTPServer(("", 8080), Handler).serve_forever()
