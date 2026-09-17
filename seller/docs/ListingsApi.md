# crossly.ListingsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_listing**](ListingsApi.md#create_listing) | **POST** /v1/listings | Create a listing and fan out crosspost jobs across platforms.
[**create_listing_bulk_check_status**](ListingsApi.md#create_listing_bulk_check_status) | **POST** /v1/listings/bulk-check-status | Check listing status on platforms
[**create_listing_bulk_crosspost**](ListingsApi.md#create_listing_bulk_crosspost) | **POST** /v1/listings/bulk-crosspost | Bulk crosspost (no delist phase)
[**create_listing_bulk_delete**](ListingsApi.md#create_listing_bulk_delete) | **POST** /v1/listings/bulk-delete | Bulk archive + delist
[**create_listing_bulk_delist**](ListingsApi.md#create_listing_bulk_delist) | **POST** /v1/listings/bulk-delist | Bulk delist from platforms
[**create_listing_bulk_delist_preview**](ListingsApi.md#create_listing_bulk_delist_preview) | **POST** /v1/listings/bulk-delist-preview | Preview which marketplaces a delist would touch
[**create_listing_bulk_hard_delete**](ListingsApi.md#create_listing_bulk_hard_delete) | **POST** /v1/listings/bulk-hard-delete | Permanently delete archived listings
[**create_listing_bulk_relist**](ListingsApi.md#create_listing_bulk_relist) | **POST** /v1/listings/bulk-relist | Bulk relist across platforms
[**create_listing_bulk_update**](ListingsApi.md#create_listing_bulk_update) | **POST** /v1/listings/bulk-update | Bulk update listing fields
[**create_listing_by_id**](ListingsApi.md#create_listing_by_id) | **POST** /v1/listings/by-ids | Fetch hydrated listings by ID
[**create_listing_check_duplicate**](ListingsApi.md#create_listing_check_duplicate) | **POST** /v1/listings/check-duplicates | Check whether the seller already owns something matching this title/photo, and what to do about it.
[**create_listing_combine**](ListingsApi.md#create_listing_combine) | **POST** /v1/listings/combine | Combine duplicate listings into one: sums their stock, delists and archives the rest.
[**create_listing_discrepancy_resolve**](ListingsApi.md#create_listing_discrepancy_resolve) | **POST** /v1/listings/{id}/discrepancies/{discrepancyId}/resolve | Resolve a detected marketplace-drift discrepancy: accept the platform value, push ours back, relist to apply it, or dismiss.
[**create_listing_import_by_url**](ListingsApi.md#create_listing_import_by_url) | **POST** /v1/listings/{id}/import-by-url | Attach a real platform listing to this listing by pasting its live URL.
[**create_listing_magic_fill**](ListingsApi.md#create_listing_magic_fill) | **POST** /v1/listings/{id}/magic-fill | Auto-fill empty fields on one platform tab from the master listing + AI/deterministic taxonomy resolution.
[**delete_listing**](ListingsApi.md#delete_listing) | **DELETE** /v1/listings/{id} | Delist a listing (optionally narrowed to specific platforms via ?platforms&#x3D;).
[**get_listing**](ListingsApi.md#get_listing) | **GET** /v1/listings/{id} | Get one listing with its platform rows.
[**get_listing_facet**](ListingsApi.md#get_listing_facet) | **GET** /v1/listings/facets | Distinct brands + categories across listings + inventory.
[**get_listing_sku_exist**](ListingsApi.md#get_listing_sku_exist) | **GET** /v1/listings/sku-exists | Check whether a SKU is already used by one of this user&#39;s items.
[**list_listing_discrepancies**](ListingsApi.md#list_listing_discrepancies) | **GET** /v1/listings/{id}/discrepancies | List detected marketplace-drift discrepancies for a listing.
[**list_listing_ids**](ListingsApi.md#list_listing_ids) | **GET** /v1/listings/ids | Filter listings → return matching id list (no pagination).
[**list_listings**](ListingsApi.md#list_listings) | **GET** /v1/listings | List active platform listings.
[**update_listing**](ListingsApi.md#update_listing) | **PATCH** /v1/listings/{id} | Edit a listing and fan out update jobs to existing platform listings.


# **create_listing**
> CreateListingResponse create_listing()

Create a listing and fan out crosspost jobs across platforms.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.create_listing_response import CreateListingResponse
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

[**CreateListingResponse**](CreateListingResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_bulk_check_status**
> CreateListingBulkCheckStatusResponse create_listing_bulk_check_status()

Check listing status on platforms

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.create_listing_bulk_check_status_response import CreateListingBulkCheckStatusResponse
from crossly.model.error import Error
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

[**CreateListingBulkCheckStatusResponse**](CreateListingBulkCheckStatusResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_bulk_crosspost**
> CreateListingBulkCrosspostResponse create_listing_bulk_crosspost()

Bulk crosspost (no delist phase)

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.create_listing_bulk_crosspost_response import CreateListingBulkCrosspostResponse
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

[**CreateListingBulkCrosspostResponse**](CreateListingBulkCrosspostResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_bulk_delete**
> CreateListingBulkDeleteResponse create_listing_bulk_delete()

Bulk archive + delist

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.create_listing_bulk_delete_response import CreateListingBulkDeleteResponse
from crossly.model.error import Error
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

[**CreateListingBulkDeleteResponse**](CreateListingBulkDeleteResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_bulk_delist**
> CreateListingBulkDelistResponse create_listing_bulk_delist()

Bulk delist from platforms

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.create_listing_bulk_delist_response import CreateListingBulkDelistResponse
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

[**CreateListingBulkDelistResponse**](CreateListingBulkDelistResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_bulk_delist_preview**
> CreateListingBulkDelistPreviewResponse create_listing_bulk_delist_preview()

Preview which marketplaces a delist would touch

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.create_listing_bulk_delist_preview_response import CreateListingBulkDelistPreviewResponse
from crossly.model.error import Error
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

[**CreateListingBulkDelistPreviewResponse**](CreateListingBulkDelistPreviewResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_bulk_hard_delete**
> CreateListingBulkHardDeleteResponse create_listing_bulk_hard_delete()

Permanently delete archived listings

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.create_listing_bulk_hard_delete_response import CreateListingBulkHardDeleteResponse
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
        # Permanently delete archived listings
        api_response = api_instance.create_listing_bulk_hard_delete()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->create_listing_bulk_hard_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateListingBulkHardDeleteResponse**](CreateListingBulkHardDeleteResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_bulk_relist**
> CreateListingBulkRelistResponse create_listing_bulk_relist()

Bulk relist across platforms

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.create_listing_bulk_relist_response import CreateListingBulkRelistResponse
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

[**CreateListingBulkRelistResponse**](CreateListingBulkRelistResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_bulk_update**
> CreateListingBulkUpdateResponse create_listing_bulk_update()

Bulk update listing fields

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.create_listing_bulk_update_response import CreateListingBulkUpdateResponse
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

[**CreateListingBulkUpdateResponse**](CreateListingBulkUpdateResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_by_id**
> CreateListingByIdResponse create_listing_by_id()

Fetch hydrated listings by ID

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.create_listing_by_id_response import CreateListingByIdResponse
from crossly.model.error import Error
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

[**CreateListingByIdResponse**](CreateListingByIdResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_check_duplicate**
> CreateListingCheckDuplicateResponse create_listing_check_duplicate()

Check whether the seller already owns something matching this title/photo, and what to do about it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.create_listing_check_duplicate_response import CreateListingCheckDuplicateResponse
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

[**CreateListingCheckDuplicateResponse**](CreateListingCheckDuplicateResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_combine**
> CreateListingCombineResponse create_listing_combine()

Combine duplicate listings into one: sums their stock, delists and archives the rest.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.create_listing_combine_response import CreateListingCombineResponse
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

[**CreateListingCombineResponse**](CreateListingCombineResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_discrepancy_resolve**
> CreateListingDiscrepancyResolveResponse create_listing_discrepancy_resolve(id, discrepancy_id)

Resolve a detected marketplace-drift discrepancy: accept the platform value, push ours back, relist to apply it, or dismiss.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.create_listing_discrepancy_resolve_response import CreateListingDiscrepancyResolveResponse
from crossly.model.error import Error
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

[**CreateListingDiscrepancyResolveResponse**](CreateListingDiscrepancyResolveResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_import_by_url**
> CreateListingImportByUrlResponse create_listing_import_by_url(id)

Attach a real platform listing to this listing by pasting its live URL.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.create_listing_import_by_url_response import CreateListingImportByUrlResponse
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

[**CreateListingImportByUrlResponse**](CreateListingImportByUrlResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_listing_magic_fill**
> CreateListingMagicFillResponse create_listing_magic_fill(id)

Auto-fill empty fields on one platform tab from the master listing + AI/deterministic taxonomy resolution.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.create_listing_magic_fill_response import CreateListingMagicFillResponse
from crossly.model.error import Error
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

[**CreateListingMagicFillResponse**](CreateListingMagicFillResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_listing**
> DeleteListingResponse delete_listing(id)

Delist a listing (optionally narrowed to specific platforms via ?platforms=).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.delete_listing_response import DeleteListingResponse
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
        api_response = api_instance.delete_listing(id, platforms=platforms)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ListingsApi->delete_listing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **platforms** | **str**| Comma-separated platform slugs to limit the delist fan-out. | [optional]

### Return type

[**DeleteListingResponse**](DeleteListingResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing**
> GetListingResponse get_listing(id)

Get one listing with its platform rows.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.get_listing_response import GetListingResponse
from crossly.model.error import Error
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

[**GetListingResponse**](GetListingResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_facet**
> GetListingFacetResponse get_listing_facet()

Distinct brands + categories across listings + inventory.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.get_listing_facet_response import GetListingFacetResponse
from crossly.model.error import Error
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

[**GetListingFacetResponse**](GetListingFacetResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_sku_exist**
> GetListingSkuExistResponse get_listing_sku_exist(sku)

Check whether a SKU is already used by one of this user's items.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.get_listing_sku_exist_response import GetListingSkuExistResponse
from crossly.model.error import Error
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

[**GetListingSkuExistResponse**](GetListingSkuExistResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_listing_discrepancies**
> bool, date, datetime, dict, float, int, list, str, none_type list_listing_discrepancies(id)

List detected marketplace-drift discrepancies for a listing.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.list_listing_discrepancies_item import ListListingDiscrepanciesItem
from crossly.model.error import Error
from crossly.model.v1_list import V1List
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

**bool, date, datetime, dict, float, int, list, str, none_type**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_listing_ids**
> bool, date, datetime, dict, float, int, list, str, none_type list_listing_ids()

Filter listings → return matching id list (no pagination).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.v1_list import V1List
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

**bool, date, datetime, dict, float, int, list, str, none_type**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_listings**
> bool, date, datetime, dict, float, int, list, str, none_type list_listings()

List active platform listings.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.error import Error
from crossly.model.list_listings_item import ListListingsItem
from crossly.model.v1_list import V1List
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List active platform listings.
        api_response = api_instance.list_listings(page=page, limit=limit, platform=platform, status=status)
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

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_listing**
> UpdateListingResponse update_listing(id)

Edit a listing and fan out update jobs to existing platform listings.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import listings_api
from crossly.model.update_listing_response import UpdateListingResponse
from crossly.model.error import Error
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

[**UpdateListingResponse**](UpdateListingResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

