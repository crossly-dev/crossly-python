# crossly_buyer.BuyerCatalogApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_buyer_identify**](BuyerCatalogApi.md#create_buyer_identify) | **POST** /v1/buyer/identify | Identify a held object and return a HUD-ready answer.
[**create_buyer_lockon**](BuyerCatalogApi.md#create_buyer_lockon) | **POST** /v1/buyer/lockons | Lock on to an object the buyer is holding.
[**create_buyer_lockon_confirm**](BuyerCatalogApi.md#create_buyer_lockon_confirm) | **POST** /v1/buyer/lockons/{id}/confirm | The buyer picked one of the candidates.
[**create_buyer_lockon_observe**](BuyerCatalogApi.md#create_buyer_lockon_observe) | **POST** /v1/buyer/lockons/{id}/observe | Add what this frame revealed, and get the current best answer.
[**create_buyer_scan**](BuyerCatalogApi.md#create_buyer_scan) | **POST** /v1/buyer/scan | Identify a physical item and find the cheapest place to buy it.
[**create_buyer_scan_session**](BuyerCatalogApi.md#create_buyer_scan_session) | **POST** /v1/buyer/scan/sessions | Open a Live Shop session.
[**create_buyer_scan_session_end**](BuyerCatalogApi.md#create_buyer_scan_session_end) | **POST** /v1/buyer/scan/sessions/{id}/end | Close a Live Shop session.
[**get_buyer_anywhere**](BuyerCatalogApi.md#get_buyer_anywhere) | **GET** /v1/buyer/anywhere | Cheapest source for an item — Crossly first, then other retailers.
[**get_buyer_catalog_facet**](BuyerCatalogApi.md#get_buyer_catalog_facet) | **GET** /v1/buyer/catalog/facets | Brands, categories and conditions that currently have stock.
[**get_buyer_catalog_listing**](BuyerCatalogApi.md#get_buyer_catalog_listing) | **GET** /v1/buyer/catalog/listings/{slug} | One listing, in full.
[**get_buyer_catalog_listing_availability**](BuyerCatalogApi.md#get_buyer_catalog_listing_availability) | **GET** /v1/buyer/catalog/listings/{slug}/availability | Is it still buyable, and at what price.
[**get_buyer_scan_session**](BuyerCatalogApi.md#get_buyer_scan_session) | **GET** /v1/buyer/scan/sessions/{id} | One trip and everything it found.
[**list_buyer_catalog_search**](BuyerCatalogApi.md#list_buyer_catalog_search) | **GET** /v1/buyer/catalog/search | Search the Crossly catalogue.
[**list_buyer_scan_sessions**](BuyerCatalogApi.md#list_buyer_scan_sessions) | **GET** /v1/buyer/scan/sessions | Your scanning trips, newest first.


# **create_buyer_identify**
> CreateBuyerIdentifyResponse create_buyer_identify()

Identify a held object and return a HUD-ready answer.

The gesture endpoint for Live Shop. Runs a cost ladder: a decoded BARCODE resolves in ~50ms for nothing; failing that, self-hosted CLIP matches the catalogue; failing that, a vision model names it (the only rung that costs anything, capped per buyer per day). `hud` is pre-formatted for a 600×600 lens — one headline, one subline, up to three fact chips and exactly ONE action, because a pinch cannot choose between buttons. A vision label is WORDS, never an identity: it names the thing so the buyer can search, and never drives a price comparison.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.create_buyer_identify_response import CreateBuyerIdentifyResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Identify a held object and return a HUD-ready answer.
        api_response = api_instance.create_buyer_identify()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->create_buyer_identify: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateBuyerIdentifyResponse**](CreateBuyerIdentifyResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_buyer_lockon**
> CreateBuyerLockonResponse create_buyer_lockon()

Lock on to an object the buyer is holding.

Open this when on-device tracking acquires an object, then post observations to it as the buyer turns the thing over. The answer improves as evidence arrives — the style code inside a shoe settles what the front of it could not.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.create_buyer_lockon_response import CreateBuyerLockonResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Lock on to an object the buyer is holding.
        api_response = api_instance.create_buyer_lockon()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->create_buyer_lockon: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateBuyerLockonResponse**](CreateBuyerLockonResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_buyer_lockon_confirm**
> CreateBuyerLockonConfirmResponse create_buyer_lockon_confirm(id)

The buyer picked one of the candidates.

Promotes a text match to a CONFIRMED identity — the strongest evidence in the system, because a person holding the object said yes. Validated against the candidates we actually offered, so it cannot be claimed about an arbitrary product.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.create_buyer_lockon_confirm_response import CreateBuyerLockonConfirmResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The buyer picked one of the candidates.
        api_response = api_instance.create_buyer_lockon_confirm(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->create_buyer_lockon_confirm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**CreateBuyerLockonConfirmResponse**](CreateBuyerLockonConfirmResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_buyer_lockon_observe**
> CreateBuyerLockonObserveResponse create_buyer_lockon_observe(id)

Add what this frame revealed, and get the current best answer.

Send only what you LEARNED: a decoded barcode, newly-read OCR text, or a frame when neither settled it. Do not post every frame — tracking and decoding happen on-device for free, and this endpoint is for evidence, not video. Evidence is RANKED (confirmed > barcode > ocr > visual), so a late weak reading can never overwrite a strong early one. When text evidence finds several products, `candidates` comes back for the buyer to pick from — a vision label is words, and only a human confirmation turns it into an identity we will price against.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.error import Error
from crossly_buyer.model.create_buyer_lockon_observe_response import CreateBuyerLockonObserveResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Add what this frame revealed, and get the current best answer.
        api_response = api_instance.create_buyer_lockon_observe(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->create_buyer_lockon_observe: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**CreateBuyerLockonObserveResponse**](CreateBuyerLockonObserveResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_buyer_scan**
> CreateBuyerScanResponse create_buyer_scan()

Identify a physical item and find the cheapest place to buy it.

Send a barcode identifier OR a photo. A BARCODE establishes identity, so the response carries a full price verdict across Crossly and other retailers. A PHOTO establishes resemblance only: you get visual matches from the Crossly catalogue, and a price verdict ONLY if the matched listing carries a real identifier. When it does not, `comparable` is false and there is no verdict — a price comparison built on a visual guess is a claim about a different product. Most second-hand items have no identifier by nature, so this is expected rather than a failure.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.create_buyer_scan_response import CreateBuyerScanResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Identify a physical item and find the cheapest place to buy it.
        api_response = api_instance.create_buyer_scan()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->create_buyer_scan: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateBuyerScanResponse**](CreateBuyerScanResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_buyer_scan_session**
> CreateBuyerScanSessionResponse create_buyer_scan_session()

Open a Live Shop session.

Call this when the glasses connect, then pass the returned id as `sessionId` on each scan. Opening a session CLOSES any other live one — a person is in one shop at a time, and two live sessions split a trip across both.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.create_buyer_scan_session_response import CreateBuyerScanSessionResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Open a Live Shop session.
        api_response = api_instance.create_buyer_scan_session()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->create_buyer_scan_session: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateBuyerScanSessionResponse**](CreateBuyerScanSessionResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_buyer_scan_session_end**
> CreateBuyerScanSessionEndResponse create_buyer_scan_session_end(id)

Close a Live Shop session.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.create_buyer_scan_session_end_response import CreateBuyerScanSessionEndResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Close a Live Shop session.
        api_response = api_instance.create_buyer_scan_session_end(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->create_buyer_scan_session_end: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**CreateBuyerScanSessionEndResponse**](CreateBuyerScanSessionEndResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buyer_anywhere**
> GetBuyerAnywhereResponse get_buyer_anywhere()

Cheapest source for an item — Crossly first, then other retailers.

Answers with a VERDICT, not a list: crossly_best, offsite_cheaper, offsite_only or no_match. Offsite offers come from licensed affiliate product feeds, are ranked CHEAPEST-FIRST — commission only ever breaks a sub-$1 tie — and only appear when they beat the price you passed in. `shippingUnknown: true` means a compared price omitted postage, so present the result as \"before postage\" rather than as a delivered total. Crossly wins ties within $1; beyond that the honest answer wins.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.get_buyer_anywhere_response import GetBuyerAnywhereResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Cheapest source for an item — Crossly first, then other retailers.
        api_response = api_instance.get_buyer_anywhere()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->get_buyer_anywhere: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBuyerAnywhereResponse**](GetBuyerAnywhereResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buyer_catalog_facet**
> GetBuyerCatalogFacetResponse get_buyer_catalog_facet()

Brands, categories and conditions that currently have stock.

The vocabulary the search filters accept. Counts are live, so a filter built from this will never return an empty page for a value that has since sold out.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.get_buyer_catalog_facet_response import GetBuyerCatalogFacetResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Brands, categories and conditions that currently have stock.
        api_response = api_instance.get_buyer_catalog_facet()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->get_buyer_catalog_facet: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBuyerCatalogFacetResponse**](GetBuyerCatalogFacetResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buyer_catalog_listing**
> GetBuyerCatalogListingResponse get_buyer_catalog_listing(slug)

One listing, in full.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.get_buyer_catalog_listing_response import GetBuyerCatalogListingResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One listing, in full.
        api_response = api_instance.get_buyer_catalog_listing(slug)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->get_buyer_catalog_listing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

[**GetBuyerCatalogListingResponse**](GetBuyerCatalogListingResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buyer_catalog_listing_availability**
> GetBuyerCatalogListingAvailabilityResponse get_buyer_catalog_listing_availability(slug)

Is it still buyable, and at what price.

The cheapest endpoint here, and the one to poll if you are going to poll — a single indexed row, no joins beyond stock, and an ETag so an unchanged answer is a 304. If you want to be TOLD instead of asking, create a monitor.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.get_buyer_catalog_listing_availability_response import GetBuyerCatalogListingAvailabilityResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Is it still buyable, and at what price.
        api_response = api_instance.get_buyer_catalog_listing_availability(slug)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->get_buyer_catalog_listing_availability: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

[**GetBuyerCatalogListingAvailabilityResponse**](GetBuyerCatalogListingAvailabilityResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buyer_scan_session**
> GetBuyerScanSessionResponse get_buyer_scan_session(id)

One trip and everything it found.

Verdicts are returned EXACTLY as they were given at the time, not re-priced. A history screen that silently refreshes old prices shows a saving that was never actually on offer.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.get_buyer_scan_session_response import GetBuyerScanSessionResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One trip and everything it found.
        api_response = api_instance.get_buyer_scan_session(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->get_buyer_scan_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**GetBuyerScanSessionResponse**](GetBuyerScanSessionResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_catalog_search**
> bool, date, datetime, dict, float, int, list, str, none_type list_buyer_catalog_search()

Search the Crossly catalogue.

Keyset-paginated. Pass the `nextCursor` you were given back as `cursor`; page 500 costs the same as page 1. Cursors are opaque — do not parse them. Responses carry an ETag: send it back as If-None-Match and an unchanged page answers 304, which is free. `sort=popular` is deliberately unavailable, because a cursor into a continuously-reordering list silently skips rows.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.list_buyer_catalog_search_item import ListBuyerCatalogSearchItem
from crossly_buyer.model.v1_list import V1List
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Search the Crossly catalogue.
        api_response = api_instance.list_buyer_catalog_search()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->list_buyer_catalog_search: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_scan_sessions**
> bool, date, datetime, dict, float, int, list, str, none_type list_buyer_scan_sessions()

Your scanning trips, newest first.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_catalog_api
from crossly_buyer.model.list_buyer_scan_sessions_item import ListBuyerScanSessionsItem
from crossly_buyer.model.v1_list import V1List
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_catalog_api.BuyerCatalogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your scanning trips, newest first.
        api_response = api_instance.list_buyer_scan_sessions()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCatalogApi->list_buyer_scan_sessions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

