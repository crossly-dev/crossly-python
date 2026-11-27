"""A Crossly webhook receiver on Flask.

    pip install crossly flask
    CROSSLY_WEBHOOK_SECRET=... flask --app flask_webhooks run --port 8080
    # then point a webhook endpoint (Settings → Webhooks) at http://<host>:8080/webhooks/crossly
"""
from flask import Flask

from crossly.frameworks import flask_webhook

app = Flask(__name__)


@app.post("/webhooks/crossly")
@flask_webhook()  # reads CROSSLY_WEBHOOK_SECRET; 400 with the reason if the signature does not verify
def crossly_webhook(event):
    print(f"{event.type}: {event.data}")
    # Answer fast; do slow work after replying, or Crossly retries the delivery.
    return "", 204
