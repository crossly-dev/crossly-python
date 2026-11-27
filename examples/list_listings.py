"""Print every listing in your Crossly store, page by page.

    pip install crossly
    CROSSLY_TOKEN=crossly_pat_... python list_listings.py
"""
import os

import crossly
from crossly.api import listings_api

config = crossly.Configuration(access_token=os.environ["CROSSLY_TOKEN"])

with crossly.ApiClient(config) as client:
    api = listings_api.ListingsApi(client)
    page = 1
    while True:
        result = api.list_listings(page=page, limit=100)
        for item in result.data:
            print(f"{item.id}  {item.status:<10}  {item.title}")
        if len(result.data) < 100:
            break
        page += 1
