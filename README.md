# Crossly Python SDK

[![ci](https://github.com/crossly-dev/crossly-python/actions/workflows/ci.yml/badge.svg)](https://github.com/crossly-dev/crossly-python/actions/workflows/ci.yml) [![release](https://github.com/crossly-dev/crossly-python/actions/workflows/release.yml/badge.svg)](https://github.com/crossly-dev/crossly-python/actions/workflows/release.yml) [![PyPI](https://img.shields.io/pypi/v/crossly)](https://pypi.org/project/crossly/) [![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

Official Python clients for the [Crossly](https://crossly.net) API: list once and sell across every marketplace, read
orders, manage inventory, and receive signed webhooks. Generated from the public OpenAPI specs and released
automatically when they change, with signed build provenance.

## Install

| client | for | install |
|---|---|---|
| seller | your store: listings, crossposting, orders, analytics | `pip install crossly` |
| buyer | shopping: cart, orders, wishlists, offers, cashback | `pip install crossly-buyer` |

## Two clients, two credentials

| client | credential |
|---|---|
| seller | a Personal Access Token (`crossly_pat_…`, Settings → Developer) or a seller OAuth token |
| buyer | a buyer OAuth token (`crossly_oat_…`) with `buyer:*` scopes |

They are not interchangeable: a seller token is refused by the buyer API and the reverse, even for the same
Crossly account. A 401 from a call that looks right usually means the other client's token.

## First call

```python
import os
import crossly
from crossly.api import listings_api

config = crossly.Configuration(access_token=os.environ["CROSSLY_TOKEN"])  # crossly_pat_…
with crossly.ApiClient(config) as client:
    page = listings_api.ListingsApi(client).list_listings(page=1, limit=25)
    for item in page.data:
        print(item.id, item.title, item.status)
```

List calls return `{ data, pagination }` and page with `page` and `limit`. Money fields named `…_cents` are
integer cents. A failed call raises `crossly.ApiException` with `.status` and `.body`, the API's `{ "error": { "code", "message" } }` plus a `correlationId` support can trace.

## Webhooks

Crossly signs every webhook with `Crossly-Signature: t=<unix>,v1=<hex HMAC-SHA256 of "t.body">`. The verifier
ships in the seller and buyer packages and checks the signature in constant time, rejects a timestamp more than
five minutes old, and returns the parsed event:

```python
from crossly.webhooks import verify_webhook, WebhookVerificationError

# raw_body: the exact bytes received, before any JSON parsing
try:
    event = verify_webhook(raw_body, request.headers["Crossly-Signature"], os.environ["CROSSLY_WEBHOOK_SECRET"])
except WebhookVerificationError:
    return Response(status=400)
```

Verify the raw bytes, not a re-serialised body. `webhooks/` holds the same verifier on its own, with the shared
test vectors every language's port is checked against on each build.

## Where things are

| client | API classes | models | API reference pages |
|---|---|---|---|
| seller | `seller/crossly/api/` | `seller/crossly/model/<area>/` | `seller/docs/` |
| buyer | `buyer/crossly_buyer/api/` | `buyer/crossly_buyer/model/<area>/` | `buyer/docs/` |

One class per API group (`OrdersApi`, `ListingsApi`, …), one model per type, the
models grouped one folder per product area (`vault`, `world`, `order`, …). A type
several endpoints share is ONE model, named after where it first appears
(`GetOrderResponse`, `ListOrdersItem`) or, for small shared shapes such as `{ ok }`,
after its fields (`OkResponse`). Each client README lists every method.

## Versions and changelog

Semantic versioning. While the version is 0.x, a release that removes an operation or a model bumps the minor
version; anything else bumps the patch. Every [CHANGELOG](CHANGELOG.md) entry lists the operations and models
that were added, changed or removed in the specs it was generated from.

## Verifying a release

Every release artifact is built on GitHub-hosted runners by [release.yml](.github/workflows/release.yml) and
carries a signed SLSA provenance attestation:

```sh
gh attestation verify <downloaded-file> --repo crossly-dev/crossly-python
```

PyPI shows the same attestations on each file's page, since the packages are uploaded by trusted publishing.

## Contributing

`seller/`, `buyer/` and `webhooks/` are generated, so a pull request that edits them would be overwritten by the
next release. Open an issue instead: the fix goes into the API spec or the generator, and every language picks it
up. [CONTRIBUTING.md](CONTRIBUTING.md) explains how to regenerate locally.

## More

- API reference and guides: https://crossly.net/docs
- Other languages: https://github.com/crossly-dev
- TypeScript (Node and browsers): [`@crossly/sdk`](https://github.com/crossly-dev/crossly-sdk); command line: [`@crossly/cli`](https://github.com/crossly-dev/crossly-cli); AI agents: [`@crossly/mcp`](https://github.com/crossly-dev/crossly-mcp)

## License

[MIT](LICENSE)
