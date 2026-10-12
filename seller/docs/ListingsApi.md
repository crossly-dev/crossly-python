# crossly.ListingsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ai_detection_dispute**](ListingsApi.md#create_ai_detection_dispute) | **POST** /v1/ai-detections/{id}/dispute | Dispute an AI-image detection on your photo (sends it to Crossly review).
[**create_listing**](ListingsApi.md#create_listing) | **POST** /v1/listings | Create a listing and fan out crosspost jobs across platforms.
[**create_listing_bulk_check_status**](ListingsApi.md#create_listing_bulk_check_status) | **POST** /v1/listings/bulk-check-status | Check listing status on platforms
[**create_listing_bulk_crosspost**](ListingsApi.md#create_listing_bulk_crosspost) | **POST** /v1/listings/bulk-crosspost | Bulk crosspost (no delist phase)
[**create_listing_bulk_delete**](ListingsApi.md#create_listing_bulk_delete) | **POST** /v1/listings/bulk-delete | Bulk archive + delist
[**create_listing_bulk_delist**](ListingsApi.md#create_listing_bulk_delist) | **POST** /v1/listings/bulk-delist | Bulk delist from platforms
[**create_listing_bulk_delist_preview**](ListingsApi.md#create_listing_bulk_delist_preview) | **POST** /v1/listings/bulk-delist-preview | Preview which marketplaces a delist would touch
[**create_listing_bulk_hard_delete**](ListingsApi.md#create_listing_bulk_hard_delete) | **POST** /v1/listings/bulk-hard-delete | Permanently delete listings (live ones need allowLive)
[**create_listing_bulk_relist**](ListingsApi.md#create_listing_bulk_relist) | **POST** /v1/listings/bulk-relist | Bulk relist across platforms
[**create_listing_bulk_update**](ListingsApi.md#create_listing_bulk_update) | **POST** /v1/listings/bulk-update | Bulk update listing fields
[**create_listing_by_id**](ListingsApi.md#create_listing_by_id) | **POST** /v1/listings/by-ids | Fetch hydrated listings by ID
[**create_listing_check_duplicate**](ListingsApi.md#create_listing_check_duplicate) | **POST** /v1/listings/check-duplicates | Check whether the seller already owns something matching this title/photo, and what to do about it.
[**create_listing_combine**](ListingsApi.md#create_listing_combine) | **POST** /v1/listings/combine | Combine duplicate listings into one: sums their stock, delists and archives the rest.
[**create_listing_discrepancy_resolve**](ListingsApi.md#create_listing_discrepancy_resolve) | **POST** /v1/listings/{id}/discrepancies/{discrepancyId}/resolve | Resolve a detected marketplace-drift discrepancy: accept the platform value, push ours back, relist to apply it, or dismiss.
[**create_listing_import_by_url**](ListingsApi.md#create_listing_import_by_url) | **POST** /v1/listings/{id}/import-by-url | Attach a real platform listing to this listing by pasting its live URL.
[**create_listing_magic_fill**](ListingsApi.md#create_listing_magic_fill) | **POST** /v1/listings/{id}/magic-fill | Auto-fill empty fields on one platform tab from the master listing + AI/deterministic taxonomy resolution.
[**create_listing_merge**](ListingsApi.md#create_listing_merge) | **POST** /v1/listings/merge | Merge the same item listed on different marketplaces into one listing; all stay live.
[**create_live_stream_pin_launch**](ListingsApi.md#create_live_stream_pin_launch) | **POST** /v1/live-streams/{id}/pin-launch | Pin one of your live NFT launches on your live show; viewers mint it from the stream. Returns &#x60;{ ok }&#x60;.
[**create_passport**](ListingsApi.md#create_passport) | **POST** /v1/passports | Register a product passport for a Crossly listing you sell, optionally bound to an NFC tag UID (hex). Returns the URL to write to the NFC tag or print as a QR; ownership then follows the item’s paid sales.
[**create_passport_revoke**](ListingsApi.md#create_passport_revoke) | **POST** /v1/passports/{id}/revoke | Revoke a passport (a lost or misprinted tag). Refused once the item has sold — the passport is then part of its history.
[**create_passport_tag**](ListingsApi.md#create_passport_tag) | **POST** /v1/passports/{id}/tag | Bind (or re-bind) a passport to the NFC tag you wrote its nfcUrl to: the tag UID (hex), and whether you locked the tag read-only. Refused once the item has sold, for a locked tag, or a tag already on another item.
[**create_variation_group**](ListingsApi.md#create_variation_group) | **POST** /v1/variation-groups | Group listings you already have: a variation (one product, an axis such as Size) or a purchase-rule group (\&quot;buy any 3\&quot;).
[**create_variation_group_generate**](ListingsApi.md#create_variation_group_generate) | **POST** /v1/variation-groups/generate | Turn one listing into a variation group: each new value becomes its own listing (a copy, with its own price, quantity and SKU) and all of them one group.
[**create_variation_group_publish**](ListingsApi.md#create_variation_group_publish) | **POST** /v1/variation-groups/{id}/publish | Publish a variation group per platform: one listing with a variation picker where the platform supports it (eBay, Shopify, Etsy), one per option elsewhere. Each platform reports its own outcome.
[**delete_listing**](ListingsApi.md#delete_listing) | **DELETE** /v1/listings/{id} | Delist a listing (optionally narrowed to specific platforms via ?platforms&#x3D;).
[**delete_live_stream_pin_launch**](ListingsApi.md#delete_live_stream_pin_launch) | **DELETE** /v1/live-streams/{id}/pin-launch | Unpin the launch from your live show. Returns &#x60;{ ok }&#x60;.
[**delete_rental_offer**](ListingsApi.md#delete_rental_offer) | **DELETE** /v1/rentals/offers/{platformListingId} | Stop offering a listing for rent (existing bookings stand).
[**delete_variation_group**](ListingsApi.md#delete_variation_group) | **DELETE** /v1/variation-groups/{id} | Dissolve a group. Its options stay as ordinary listings.
[**get_listing**](ListingsApi.md#get_listing) | **GET** /v1/listings/{id} | Get one listing with its platform rows.
[**get_listing_facet**](ListingsApi.md#get_listing_facet) | **GET** /v1/listings/facets | Distinct brands + categories across listings + inventory.
[**get_listing_sku_exist**](ListingsApi.md#get_listing_sku_exist) | **GET** /v1/listings/sku-exists | Check whether a SKU is already used by one of this user&#39;s items.
[**get_pricing_setting**](ListingsApi.md#get_pricing_setting) | **GET** /v1/pricing/settings | Selling options: own-price match (Crossly sells your items at your own lower price for the same item on another marketplace; dollar-priced copies only) and layaway (buyers may put items on layaway). Both on by default.
[**get_pricing_sold_comp**](ListingsApi.md#get_pricing_sold_comp) | **GET** /v1/pricing/sold-comps | What one catalog product (market_sku_id, in one condition) actually sold for across Crossly in the last 180 days: median, p25/p75, p10/p90 (null under 10 sales), sale count, last sold, and days from listing to sale (median, p25, p75). Pass marketSkuId (+ optional condition) or one of your listingIds. comps is null until there are 3+ sales from 2+ sellers; holdCode says why there is nothing (no_market_sku, mixed_inventory, below_privacy_floor) — the same reasons a sold_median reprice rule holds.
[**list_listing_ai_detections**](ListingsApi.md#list_listing_ai_detections) | **GET** /v1/listings/{id}/ai-detections | Crossly&#39;s AI-image detections for a listing&#39;s photos.
[**list_listing_discrepancies**](ListingsApi.md#list_listing_discrepancies) | **GET** /v1/listings/{id}/discrepancies | List detected marketplace-drift discrepancies for a listing.
[**list_listing_ids**](ListingsApi.md#list_listing_ids) | **GET** /v1/listings/ids | Filter listings → return matching id list (no pagination).
[**list_listings**](ListingsApi.md#list_listings) | **GET** /v1/listings | List active platform listings.
[**list_passports**](ListingsApi.md#list_passports) | **GET** /v1/passports | Product passports you registered (optionally for one Crossly listing): the code and URL each tag carries.
[**list_rental_offers**](ListingsApi.md#list_rental_offers) | **GET** /v1/rentals/offers | What you offer for rent.
[**update_hotspot**](ListingsApi.md#update_hotspot) | **PUT** /v1/hotspots | Tag your listings at points on a story or lookbook photo (shop the look). Replaces that photo’s tags; at most 12.
[**update_listing**](ListingsApi.md#update_listing) | **PATCH** /v1/listings/{id} | Edit a listing and fan out update jobs to existing platform listings.
[**update_listing_custom**](ListingsApi.md#update_listing_custom) | **PUT** /v1/listings/{id}/customs | Set a listing’s customs: HS code (6–10 digits), country of origin, and countries this item must not ship to on Crossly. Omitted fields are left alone; null (or [] for restrictedCountries) clears.
[**update_listing_platform_listing**](ListingsApi.md#update_listing_platform_listing) | **PATCH** /v1/listings/{id}/platform-listings/{plId} | Set one marketplace copy&#39;s price (e.g. the ebay.com copy of a listing also live on ebay.co.uk), in that copy&#39;s own currency.
[**update_live_stream_lineup**](ListingsApi.md#update_live_stream_lineup) | **PUT** /v1/live-streams/{id}/lineup | Set a live show’s lineup: your Crossly listings, in the order you will sell them. Buyers see it before they join; a sale of a lineup item while the show is live is recorded at its replay moment.
[**update_pricing_setting**](ListingsApi.md#update_pricing_setting) | **PUT** /v1/pricing/settings | Turn own-price match and/or layaway on or off.
[**update_rental_offer**](ListingsApi.md#update_rental_offer) | **PUT** /v1/rentals/offers/{platformListingId} | Offer a Crossly listing for rent: day rate, optional week rate, deposit, min/max days, turnaround buffer, and rent-only (off sale while offered). Needs a ship-from address.
[**update_variation_group**](ListingsApi.md#update_variation_group) | **PATCH** /v1/variation-groups/{id} | Retitle a group, rename its axis, or change a group&#39;s purchase rule (written into every member&#39;s description).


# **create_ai_detection_dispute**
> CreateAiDetectionDisputeResponse create_ai_detection_dispute(id)

Dispute an AI-image detection on your photo (sends it to Crossly review).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.ai.create_ai_detection_dispute_response import CreateAiDetectionDisputeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Dispute an AI-image detection on your photo (sends it to Crossly review).
        api_response = api_instance.create_ai_detection_dispute(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_ai_detection_dispute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateAiDetectionDisputeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing**
> CreateListingResponse create_listing()

Create a listing and fan out crosspost jobs across platforms.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.listing.create_listing_response import CreateListingResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a listing and fan out crosspost jobs across platforms.
        api_response = api_instance.create_listing()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_bulk_check_status**
> CreateListingBulkDeleteResponse create_listing_bulk_check_status()

Check listing status on platforms

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.create_listing_bulk_delete_response import CreateListingBulkDeleteResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Check listing status on platforms
        api_response = api_instance.create_listing_bulk_check_status()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_bulk_check_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingBulkDeleteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_bulk_crosspost**
> CreateListingBulkDeleteResponse create_listing_bulk_crosspost()

Bulk crosspost (no delist phase)

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.create_listing_bulk_delete_response import CreateListingBulkDeleteResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk crosspost (no delist phase)
        api_response = api_instance.create_listing_bulk_crosspost()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_bulk_crosspost: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingBulkDeleteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_bulk_delete**
> CreateListingBulkDeleteResponse create_listing_bulk_delete()

Bulk archive + delist

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.create_listing_bulk_delete_response import CreateListingBulkDeleteResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk archive + delist
        api_response = api_instance.create_listing_bulk_delete()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_bulk_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingBulkDeleteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_bulk_delist**
> CreateListingBulkDeleteResponse create_listing_bulk_delist()

Bulk delist from platforms

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.create_listing_bulk_delete_response import CreateListingBulkDeleteResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk delist from platforms
        api_response = api_instance.create_listing_bulk_delist()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_bulk_delist: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingBulkDeleteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_bulk_delist_preview**
> CreateListingBulkDelistPreviewResponse create_listing_bulk_delist_preview()

Preview which marketplaces a delist would touch

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.create_listing_bulk_delist_preview_response import CreateListingBulkDelistPreviewResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Preview which marketplaces a delist would touch
        api_response = api_instance.create_listing_bulk_delist_preview()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_bulk_delist_preview: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingBulkDelistPreviewResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_bulk_hard_delete**
> CreateListingBulkHardDeleteResponse create_listing_bulk_hard_delete()

Permanently delete listings (live ones need allowLive)

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.listing.create_listing_bulk_hard_delete_response import CreateListingBulkHardDeleteResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Permanently delete listings (live ones need allowLive)
        api_response = api_instance.create_listing_bulk_hard_delete()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_bulk_hard_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingBulkHardDeleteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_bulk_relist**
> CreateListingBulkDeleteResponse create_listing_bulk_relist()

Bulk relist across platforms

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.create_listing_bulk_delete_response import CreateListingBulkDeleteResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk relist across platforms
        api_response = api_instance.create_listing_bulk_relist()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_bulk_relist: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingBulkDeleteResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_bulk_update**
> CreateListingBulkUpdateResponse create_listing_bulk_update()

Bulk update listing fields

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.listing.create_listing_bulk_update_response import CreateListingBulkUpdateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk update listing fields
        api_response = api_instance.create_listing_bulk_update()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_bulk_update: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingBulkUpdateResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_by_id**
> CreateListingByIdResponse create_listing_by_id()

Fetch hydrated listings by ID

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.create_listing_by_id_response import CreateListingByIdResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch hydrated listings by ID
        api_response = api_instance.create_listing_by_id()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_by_id: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingByIdResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_check_duplicate**
> CreateListingCheckDuplicateResponse create_listing_check_duplicate()

Check whether the seller already owns something matching this title/photo, and what to do about it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.listing.create_listing_check_duplicate_response import CreateListingCheckDuplicateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Check whether the seller already owns something matching this title/photo, and what to do about it.
        api_response = api_instance.create_listing_check_duplicate()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_check_duplicate: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingCheckDuplicateResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_combine**
> CreateListingCombineResponse create_listing_combine()

Combine duplicate listings into one: sums their stock, delists and archives the rest.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.listing.create_listing_combine_response import CreateListingCombineResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Combine duplicate listings into one: sums their stock, delists and archives the rest.
        api_response = api_instance.create_listing_combine()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_combine: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingCombineResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_discrepancy_resolve**
> CreateListingDiscrepancyResolveResponse create_listing_discrepancy_resolve(id, discrepancy_id)

Resolve a detected marketplace-drift discrepancy: accept the platform value, push ours back, relist to apply it, or dismiss.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.create_listing_discrepancy_resolve_response import CreateListingDiscrepancyResolveResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 
    discrepancy_id = "discrepancyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Resolve a detected marketplace-drift discrepancy: accept the platform value, push ours back, relist to apply it, or dismiss.
        api_response = api_instance.create_listing_discrepancy_resolve(id, discrepancy_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_discrepancy_resolve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **discrepancy_id** | **str**|  |

### Return type

**CreateListingDiscrepancyResolveResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_import_by_url**
> CreateListingImportByUrlResponse create_listing_import_by_url(id)

Attach a real platform listing to this listing by pasting its live URL.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.listing.create_listing_import_by_url_response import CreateListingImportByUrlResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Attach a real platform listing to this listing by pasting its live URL.
        api_response = api_instance.create_listing_import_by_url(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_import_by_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateListingImportByUrlResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_magic_fill**
> CreateListingMagicFillResponse create_listing_magic_fill(id)

Auto-fill empty fields on one platform tab from the master listing + AI/deterministic taxonomy resolution.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.create_listing_magic_fill_response import CreateListingMagicFillResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Auto-fill empty fields on one platform tab from the master listing + AI/deterministic taxonomy resolution.
        api_response = api_instance.create_listing_magic_fill(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_magic_fill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateListingMagicFillResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_listing_merge**
> CreateListingMergeResponse create_listing_merge()

Merge the same item listed on different marketplaces into one listing; all stay live.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.listing.create_listing_merge_response import CreateListingMergeResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Merge the same item listed on different marketplaces into one listing; all stay live.
        api_response = api_instance.create_listing_merge()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_merge: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateListingMergeResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_live_stream_pin_launch**
> OkResponse create_live_stream_pin_launch(id)

Pin one of your live NFT launches on your live show; viewers mint it from the stream. Returns `{ ok }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.ok_response import OkResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Pin one of your live NFT launches on your live show; viewers mint it from the stream. Returns `{ ok }`.
        api_response = api_instance.create_live_stream_pin_launch(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_live_stream_pin_launch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**OkResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_passport**
> PassportResponse create_passport()

Register a product passport for a Crossly listing you sell, optionally bound to an NFC tag UID (hex). Returns the URL to write to the NFC tag or print as a QR; ownership then follows the item’s paid sales.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.passport_response import PassportResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Register a product passport for a Crossly listing you sell, optionally bound to an NFC tag UID (hex). Returns the URL to write to the NFC tag or print as a QR; ownership then follows the item’s paid sales.
        api_response = api_instance.create_passport()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_passport: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**PassportResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_passport_revoke**
> PassportResponse create_passport_revoke(id)

Revoke a passport (a lost or misprinted tag). Refused once the item has sold — the passport is then part of its history.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.passport_response import PassportResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke a passport (a lost or misprinted tag). Refused once the item has sold — the passport is then part of its history.
        api_response = api_instance.create_passport_revoke(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_passport_revoke: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**PassportResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_passport_tag**
> PassportResponse create_passport_tag(id)

Bind (or re-bind) a passport to the NFC tag you wrote its nfcUrl to: the tag UID (hex), and whether you locked the tag read-only. Refused once the item has sold, for a locked tag, or a tag already on another item.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.passport_response import PassportResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Bind (or re-bind) a passport to the NFC tag you wrote its nfcUrl to: the tag UID (hex), and whether you locked the tag read-only. Refused once the item has sold, for a locked tag, or a tag already on another item.
        api_response = api_instance.create_passport_tag(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_passport_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**PassportResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_variation_group**
> CreateVariationGroupResponse create_variation_group()

Group listings you already have: a variation (one product, an axis such as Size) or a purchase-rule group (\"buy any 3\").

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.variation.create_variation_group_response import CreateVariationGroupResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Group listings you already have: a variation (one product, an axis such as Size) or a purchase-rule group (\"buy any 3\").
        api_response = api_instance.create_variation_group()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_variation_group: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateVariationGroupResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_variation_group_generate**
> CreateVariationGroupGenerateResponse create_variation_group_generate()

Turn one listing into a variation group: each new value becomes its own listing (a copy, with its own price, quantity and SKU) and all of them one group.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.variation.create_variation_group_generate_response import CreateVariationGroupGenerateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Turn one listing into a variation group: each new value becomes its own listing (a copy, with its own price, quantity and SKU) and all of them one group.
        api_response = api_instance.create_variation_group_generate()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_variation_group_generate: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateVariationGroupGenerateResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_variation_group_publish**
> CreateVariationGroupPublishResponse create_variation_group_publish(id)

Publish a variation group per platform: one listing with a variation picker where the platform supports it (eBay, Shopify, Etsy), one per option elsewhere. Each platform reports its own outcome.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.variation.create_variation_group_publish_response import CreateVariationGroupPublishResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Publish a variation group per platform: one listing with a variation picker where the platform supports it (eBay, Shopify, Etsy), one per option elsewhere. Each platform reports its own outcome.
        api_response = api_instance.create_variation_group_publish(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_variation_group_publish: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateVariationGroupPublishResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_listing**
> DeleteListingResponse delete_listing(id)

Delist a listing (optionally narrowed to specific platforms via ?platforms=).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.listing.delete_listing_response import DeleteListingResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 
    platforms = "platforms_example" # str | Comma-separated platform slugs to limit the delist fan-out. (optional)
    platform_listing_ids = "platformListingIds_example" # str | Comma-separated platform listing ids — end only those copies (e.g. one eBay site's copy). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delist a listing (optionally narrowed to specific platforms via ?platforms=).
        api_response = api_instance.delete_listing(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->delete_listing: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delist a listing (optionally narrowed to specific platforms via ?platforms=).
        api_response = api_instance.delete_listing(id, platforms=platforms, platform_listing_ids=platform_listing_ids)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->delete_listing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **platforms** | **str**| Comma-separated platform slugs to limit the delist fan-out. | [optional]
 **platform_listing_ids** | **str**| Comma-separated platform listing ids — end only those copies (e.g. one eBay site&#39;s copy). | [optional]

### Return type

**DeleteListingResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_live_stream_pin_launch**
> OkResponse delete_live_stream_pin_launch(id)

Unpin the launch from your live show. Returns `{ ok }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.ok_response import OkResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unpin the launch from your live show. Returns `{ ok }`.
        api_response = api_instance.delete_live_stream_pin_launch(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->delete_live_stream_pin_launch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**OkResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_rental_offer**
> CreateBreakCancelResponse delete_rental_offer(platform_listing_id)

Stop offering a listing for rent (existing bookings stand).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.breaks.create_break_cancel_response import CreateBreakCancelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    platform_listing_id = "platformListingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Stop offering a listing for rent (existing bookings stand).
        api_response = api_instance.delete_rental_offer(platform_listing_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->delete_rental_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_listing_id** | **str**|  |

### Return type

**CreateBreakCancelResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_variation_group**
> CreateBreakCancelResponse delete_variation_group(id)

Dissolve a group. Its options stay as ordinary listings.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.breaks.create_break_cancel_response import CreateBreakCancelResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Dissolve a group. Its options stay as ordinary listings.
        api_response = api_instance.delete_variation_group(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->delete_variation_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateBreakCancelResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_listing**
> GetListingResponse get_listing(id)

Get one listing with its platform rows.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.get_listing_response import GetListingResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get one listing with its platform rows.
        api_response = api_instance.get_listing(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->get_listing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetListingResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_listing_facet**
> GetListingFacetResponse get_listing_facet()

Distinct brands + categories across listings + inventory.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.get_listing_facet_response import GetListingFacetResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Distinct brands + categories across listings + inventory.
        api_response = api_instance.get_listing_facet()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->get_listing_facet: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetListingFacetResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_listing_sku_exist**
> GetListingSkuExistResponse get_listing_sku_exist(sku)

Check whether a SKU is already used by one of this user's items.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.get_listing_sku_exist_response import GetListingSkuExistResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    sku = "sku_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Check whether a SKU is already used by one of this user's items.
        api_response = api_instance.get_listing_sku_exist(sku)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->get_listing_sku_exist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  |

### Return type

**GetListingSkuExistResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_pricing_setting**
> GetPricingSettingResponse get_pricing_setting()

Selling options: own-price match (Crossly sells your items at your own lower price for the same item on another marketplace; dollar-priced copies only) and layaway (buyers may put items on layaway). Both on by default.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.get_pricing_setting_response import GetPricingSettingResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Selling options: own-price match (Crossly sells your items at your own lower price for the same item on another marketplace; dollar-priced copies only) and layaway (buyers may put items on layaway). Both on by default.
        api_response = api_instance.get_pricing_setting()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->get_pricing_setting: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetPricingSettingResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_pricing_sold_comp**
> GetPricingSoldCompResponse get_pricing_sold_comp()

What one catalog product (market_sku_id, in one condition) actually sold for across Crossly in the last 180 days: median, p25/p75, p10/p90 (null under 10 sales), sale count, last sold, and days from listing to sale (median, p25, p75). Pass marketSkuId (+ optional condition) or one of your listingIds. comps is null until there are 3+ sales from 2+ sellers; holdCode says why there is nothing (no_market_sku, mixed_inventory, below_privacy_floor) — the same reasons a sold_median reprice rule holds.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.common.get_pricing_sold_comp_response import GetPricingSoldCompResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What one catalog product (market_sku_id, in one condition) actually sold for across Crossly in the last 180 days: median, p25/p75, p10/p90 (null under 10 sales), sale count, last sold, and days from listing to sale (median, p25, p75). Pass marketSkuId (+ optional condition) or one of your listingIds. comps is null until there are 3+ sales from 2+ sellers; holdCode says why there is nothing (no_market_sku, mixed_inventory, below_privacy_floor) — the same reasons a sold_median reprice rule holds.
        api_response = api_instance.get_pricing_sold_comp()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->get_pricing_sold_comp: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetPricingSoldCompResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_listing_ai_detections**
> ListListingAiDetectionsResponse list_listing_ai_detections(id)

Crossly's AI-image detections for a listing's photos.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.listing.list_listing_ai_detections_response import ListListingAiDetectionsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Crossly's AI-image detections for a listing's photos.
        api_response = api_instance.list_listing_ai_detections(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->list_listing_ai_detections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListListingAiDetectionsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_listing_discrepancies**
> ListListingDiscrepanciesResponse list_listing_discrepancies(id)

List detected marketplace-drift discrepancies for a listing.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.listing.list_listing_discrepancies_response import ListListingDiscrepanciesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List detected marketplace-drift discrepancies for a listing.
        api_response = api_instance.list_listing_discrepancies(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->list_listing_discrepancies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListListingDiscrepanciesResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_listing_ids**
> ListListingIdsResponse list_listing_ids()

Filter listings → return matching id list (no pagination).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.listing.list_listing_ids_response import ListListingIdsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Filter listings → return matching id list (no pagination).
        api_response = api_instance.list_listing_ids()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->list_listing_ids: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListListingIdsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_listings**
> ListListingsResponse list_listings()

List active platform listings.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.list_listings_response import ListListingsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    limit = 25 # int |  (optional) if omitted the server will use the default value of 25
    platform = "platform_example" # str |  (optional)
    status = "status_example" # str |  (optional)
    kind = "physical" # str | Physical goods or Web3 assets (NFT listings). Omit for both. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List active platform listings.
        api_response = api_instance.list_listings(page=page, limit=limit, platform=platform, status=status, kind=kind)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->list_listings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 25
 **platform** | **str**|  | [optional]
 **status** | **str**|  | [optional]
 **kind** | **str**| Physical goods or Web3 assets (NFT listings). Omit for both. | [optional]

### Return type

**ListListingsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_passports**
> ListPassportsResponse list_passports()

Product passports you registered (optionally for one Crossly listing): the code and URL each tag carries.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.list_passports_response import ListPassportsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Product passports you registered (optionally for one Crossly listing): the code and URL each tag carries.
        api_response = api_instance.list_passports()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->list_passports: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListPassportsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_rental_offers**
> ListRentalOffersResponse list_rental_offers()

What you offer for rent.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.rental.list_rental_offers_response import ListRentalOffersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What you offer for rent.
        api_response = api_instance.list_rental_offers()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->list_rental_offers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListRentalOffersResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_hotspot**
> UpdateHotspotResponse update_hotspot()

Tag your listings at points on a story or lookbook photo (shop the look). Replaces that photo’s tags; at most 12.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.common.update_hotspot_response import UpdateHotspotResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Tag your listings at points on a story or lookbook photo (shop the look). Replaces that photo’s tags; at most 12.
        api_response = api_instance.update_hotspot()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->update_hotspot: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**UpdateHotspotResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_listing**
> UpdateListingResponse update_listing(id)

Edit a listing and fan out update jobs to existing platform listings.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.update_listing_response import UpdateListingResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Edit a listing and fan out update jobs to existing platform listings.
        api_response = api_instance.update_listing(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->update_listing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateListingResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_listing_custom**
> UpdateListingCustomResponse update_listing_custom(id)

Set a listing’s customs: HS code (6–10 digits), country of origin, and countries this item must not ship to on Crossly. Omitted fields are left alone; null (or [] for restrictedCountries) clears.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.update_listing_custom_response import UpdateListingCustomResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set a listing’s customs: HS code (6–10 digits), country of origin, and countries this item must not ship to on Crossly. Omitted fields are left alone; null (or [] for restrictedCountries) clears.
        api_response = api_instance.update_listing_custom(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->update_listing_custom: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateListingCustomResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_listing_platform_listing**
> UpdateListingPlatformListingResponse update_listing_platform_listing(id, pl_id)

Set one marketplace copy's price (e.g. the ebay.com copy of a listing also live on ebay.co.uk), in that copy's own currency.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.listing.update_listing_platform_listing_response import UpdateListingPlatformListingResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 
    pl_id = "plId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set one marketplace copy's price (e.g. the ebay.com copy of a listing also live on ebay.co.uk), in that copy's own currency.
        api_response = api_instance.update_listing_platform_listing(id, pl_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->update_listing_platform_listing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **pl_id** | **str**|  |

### Return type

**UpdateListingPlatformListingResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_live_stream_lineup**
> UpdateLiveStreamLineupResponse update_live_stream_lineup(id)

Set a live show’s lineup: your Crossly listings, in the order you will sell them. Buyers see it before they join; a sale of a lineup item while the show is live is recorded at its replay moment.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.live.update_live_stream_lineup_response import UpdateLiveStreamLineupResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set a live show’s lineup: your Crossly listings, in the order you will sell them. Buyers see it before they join; a sale of a lineup item while the show is live is recorded at its replay moment.
        api_response = api_instance.update_live_stream_lineup(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->update_live_stream_lineup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateLiveStreamLineupResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_pricing_setting**
> GetPricingSettingResponse update_pricing_setting()

Turn own-price match and/or layaway on or off.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.get_pricing_setting_response import GetPricingSettingResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Turn own-price match and/or layaway on or off.
        api_response = api_instance.update_pricing_setting()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->update_pricing_setting: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetPricingSettingResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_rental_offer**
> UpdateRentalOfferResponse update_rental_offer(platform_listing_id)

Offer a Crossly listing for rent: day rate, optional week rate, deposit, min/max days, turnaround buffer, and rent-only (off sale while offered). Needs a ship-from address.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.rental.update_rental_offer_response import UpdateRentalOfferResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    platform_listing_id = "platformListingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Offer a Crossly listing for rent: day rate, optional week rate, deposit, min/max days, turnaround buffer, and rent-only (off sale while offered). Needs a ship-from address.
        api_response = api_instance.update_rental_offer(platform_listing_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->update_rental_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_listing_id** | **str**|  |

### Return type

**UpdateRentalOfferResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_variation_group**
> CreateVariationGroupResponse update_variation_group(id)

Retitle a group, rename its axis, or change a group's purchase rule (written into every member's description).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.common.error import Error
from crossly.model.variation.create_variation_group_response import CreateVariationGroupResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listings_api.ListingsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retitle a group, rename its axis, or change a group's purchase rule (written into every member's description).
        api_response = api_instance.update_variation_group(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->update_variation_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateVariationGroupResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

