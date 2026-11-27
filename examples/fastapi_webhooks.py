"""A Crossly webhook receiver on FastAPI.

    pip install crossly fastapi uvicorn
    CROSSLY_WEBHOOK_SECRET=... uvicorn fastapi_webhooks:app --port 8080
"""
from fastapi import Depends, FastAPI

from crossly.frameworks import fastapi_webhook

app = FastAPI()


@app.post("/webhooks/crossly", status_code=204)
async def crossly_webhook(event=Depends(fastapi_webhook())):
    print(f"{event.type}: {event.data}")
