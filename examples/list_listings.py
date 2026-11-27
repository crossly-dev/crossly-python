"""Print every listing in your Crossly store, following pagination.

    pip install crossly
    CROSSLY_TOKEN=crossly_pat_... python list_listings.py
"""
import os
import sys

from crossly.client import Crossly, CrosslyError

with Crossly(os.environ["CROSSLY_TOKEN"]) as crossly:
    try:
        for item in crossly.iter_items(crossly.listings.list_listings):
            print(f"{item.id}  {item.status:<10}  {item.title}")
    except CrosslyError as e:
        # code and correlation_id are what support needs.
        sys.exit(f"failed: {e.status} {e.code} {e.message} (correlationId {e.correlation_id})")
