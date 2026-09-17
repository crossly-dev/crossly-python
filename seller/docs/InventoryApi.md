# crossly.InventoryApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inventory**](InventoryApi.md#create_inventory) | **POST** /v1/inventory | Create a new inventory item.
[**create_inventory_bulk_archive**](InventoryApi.md#create_inventory_bulk_archive) | **POST** /v1/inventory/bulk-archive | Bulk archive inventory items (soft).
[**create_inventory_bulk_delete**](InventoryApi.md#create_inventory_bulk_delete) | **POST** /v1/inventory/bulk-delete | Bulk delete inventory items (delinks listings).
[**create_inventory_bulk_label**](InventoryApi.md#create_inventory_bulk_label) | **POST** /v1/inventory/bulk-labels | Bulk add/remove labels on inventory items.
[**create_inventory_bulk_quantity**](InventoryApi.md#create_inventory_bulk_quantity) | **POST** /v1/inventory/bulk-quantity | Set / add / subtract stock across many items, syncing live listings.
[**create_inventory_csv_export**](InventoryApi.md#create_inventory_csv_export) | **POST** /v1/inventory/csv/export | Export inventory as CSV. Round-trips back through csv/import.
[**create_inventory_csv_import**](InventoryApi.md#create_inventory_csv_import) | **POST** /v1/inventory/csv/import | Import a CSV. Rows whose sku matches an existing item update it; others are added. Pass dryRun to preview.
[**create_inventory_label_rename**](InventoryApi.md#create_inventory_label_rename) | **POST** /v1/inventory/labels/rename | Rename a label across every inventory item.
[**create_inventory_unit_identifier**](InventoryApi.md#create_inventory_unit_identifier) | **POST** /v1/inventory/{id}/units/identifiers | Record a serial, IMEI, or licence key against an inventory item.
[**create_inventory_unit_lookup**](InventoryApi.md#create_inventory_unit_lookup) | **POST** /v1/inventory/units/lookup | Find a unit by identifier.
[**delete_inventory**](InventoryApi.md#delete_inventory) | **DELETE** /v1/inventory/{id} | Soft-archive an inventory item.
[**get_inventory**](InventoryApi.md#get_inventory) | **GET** /v1/inventory/{id} | Get one inventory item with platform listings.
[**get_inventory_facet**](InventoryApi.md#get_inventory_facet) | **GET** /v1/inventory/facets | Distinct brands + categories across this user&#39;s inventory.
[**get_inventory_label**](InventoryApi.md#get_inventory_label) | **GET** /v1/inventory/labels | List every distinct label across this user&#39;s inventory.
[**get_inventory_label_stat**](InventoryApi.md#get_inventory_label_stat) | **GET** /v1/inventory/labels/stats | List distinct labels with usage counts + colors.
[**get_inventory_sku_exist**](InventoryApi.md#get_inventory_sku_exist) | **GET** /v1/inventory/sku-exists | Check whether a SKU is already in use on this user&#39;s inventory.
[**get_spatial_public**](InventoryApi.md#get_spatial_public) | **GET** /v1/spatial/public/{slug} | A shared room, as a visitor sees it.
[**get_spatial_scene**](InventoryApi.md#get_spatial_scene) | **GET** /v1/spatial/scenes/{id} | A solved room: every item, where it sits, and why.
[**list_inventory**](InventoryApi.md#list_inventory) | **GET** /v1/inventory | List inventory items.
[**list_inventory_activity**](InventoryApi.md#list_inventory_activity) | **GET** /v1/inventory/{id}/activity | Activity log for an inventory item (created/sold/edited/etc.).
[**list_inventory_ids**](InventoryApi.md#list_inventory_ids) | **GET** /v1/inventory/ids | Filter inventory → return matching id list.
[**list_inventory_units**](InventoryApi.md#list_inventory_units) | **GET** /v1/inventory/{id}/units | List the individually identified units of an inventory item.
[**list_spatial_public**](InventoryApi.md#list_spatial_public) | **GET** /v1/spatial/public | Public rooms anyone can walk into.
[**list_spatial_public_offers**](InventoryApi.md#list_spatial_public_offers) | **GET** /v1/spatial/public/{slug}/offers | What is for sale in a shared room.
[**list_spatial_scene_movements**](InventoryApi.md#list_spatial_scene_movements) | **GET** /v1/spatial/scenes/{id}/movements | Stock movements in a room over a time window.
[**list_spatial_scenes**](InventoryApi.md#list_spatial_scenes) | **GET** /v1/spatial/scenes | The rooms this account has.
[**update_inventory**](InventoryApi.md#update_inventory) | **PATCH** /v1/inventory/{id} | Update an inventory item (partial).


# **create_inventory**
> CreateInventoryResponse create_inventory()

Create a new inventory item.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.create_inventory_response import CreateInventoryResponse
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a new inventory item.
        api_response = api_instance.create_inventory()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->create_inventory: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInventoryResponse**](CreateInventoryResponse.md)

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

# **create_inventory_bulk_archive**
> CreateInventoryBulkArchiveResponse create_inventory_bulk_archive()

Bulk archive inventory items (soft).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.create_inventory_bulk_archive_response import CreateInventoryBulkArchiveResponse
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk archive inventory items (soft).
        api_response = api_instance.create_inventory_bulk_archive()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->create_inventory_bulk_archive: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInventoryBulkArchiveResponse**](CreateInventoryBulkArchiveResponse.md)

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

# **create_inventory_bulk_delete**
> CreateInventoryBulkDeleteResponse create_inventory_bulk_delete()

Bulk delete inventory items (delinks listings).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.create_inventory_bulk_delete_response import CreateInventoryBulkDeleteResponse
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk delete inventory items (delinks listings).
        api_response = api_instance.create_inventory_bulk_delete()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->create_inventory_bulk_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInventoryBulkDeleteResponse**](CreateInventoryBulkDeleteResponse.md)

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

# **create_inventory_bulk_label**
> CreateInventoryBulkLabelResponse create_inventory_bulk_label()

Bulk add/remove labels on inventory items.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.create_inventory_bulk_label_response import CreateInventoryBulkLabelResponse
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk add/remove labels on inventory items.
        api_response = api_instance.create_inventory_bulk_label()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->create_inventory_bulk_label: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInventoryBulkLabelResponse**](CreateInventoryBulkLabelResponse.md)

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

# **create_inventory_bulk_quantity**
> CreateInventoryBulkQuantityResponse create_inventory_bulk_quantity()

Set / add / subtract stock across many items, syncing live listings.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.create_inventory_bulk_quantity_response import CreateInventoryBulkQuantityResponse
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Set / add / subtract stock across many items, syncing live listings.
        api_response = api_instance.create_inventory_bulk_quantity()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->create_inventory_bulk_quantity: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInventoryBulkQuantityResponse**](CreateInventoryBulkQuantityResponse.md)

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

# **create_inventory_csv_export**
> str create_inventory_csv_export()

Export inventory as CSV. Round-trips back through csv/import.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Export inventory as CSV. Round-trips back through csv/import.
        api_response = api_instance.create_inventory_csv_export()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->create_inventory_csv_export: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **create_inventory_csv_import**
> CreateInventoryCsvImportResponse create_inventory_csv_import()

Import a CSV. Rows whose sku matches an existing item update it; others are added. Pass dryRun to preview.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.create_inventory_csv_import_response import CreateInventoryCsvImportResponse
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Import a CSV. Rows whose sku matches an existing item update it; others are added. Pass dryRun to preview.
        api_response = api_instance.create_inventory_csv_import()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->create_inventory_csv_import: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInventoryCsvImportResponse**](CreateInventoryCsvImportResponse.md)

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

# **create_inventory_label_rename**
> CreateInventoryLabelRenameResponse create_inventory_label_rename()

Rename a label across every inventory item.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.create_inventory_label_rename_response import CreateInventoryLabelRenameResponse
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Rename a label across every inventory item.
        api_response = api_instance.create_inventory_label_rename()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->create_inventory_label_rename: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInventoryLabelRenameResponse**](CreateInventoryLabelRenameResponse.md)

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

# **create_inventory_unit_identifier**
> CreateInventoryUnitIdentifierResponse create_inventory_unit_identifier(id)

Record a serial, IMEI, or licence key against an inventory item.

Creates the unit lazily if no `unitId` is given. Recording BEFORE the item sells is what makes the identifier usable as evidence on a return — one first recorded after a dispute opens is graded `weak` and says so.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.create_inventory_unit_identifier_response import CreateInventoryUnitIdentifierResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Record a serial, IMEI, or licence key against an inventory item.
        api_response = api_instance.create_inventory_unit_identifier(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->create_inventory_unit_identifier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**CreateInventoryUnitIdentifierResponse**](CreateInventoryUnitIdentifierResponse.md)

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

# **create_inventory_unit_lookup**
> CreateInventoryUnitLookupResponse create_inventory_unit_lookup()

Find a unit by identifier.

\"Have I ever seen this serial?\" — for when something arrives back and nobody knows which order it belongs to. Scoped to the caller, so it can never be used to probe another seller's stock.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.create_inventory_unit_lookup_response import CreateInventoryUnitLookupResponse
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find a unit by identifier.
        api_response = api_instance.create_inventory_unit_lookup()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->create_inventory_unit_lookup: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInventoryUnitLookupResponse**](CreateInventoryUnitLookupResponse.md)

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

# **delete_inventory**
> DeleteInventoryResponse delete_inventory(id)

Soft-archive an inventory item.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.delete_inventory_response import DeleteInventoryResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Soft-archive an inventory item.
        api_response = api_instance.delete_inventory(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->delete_inventory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DeleteInventoryResponse**](DeleteInventoryResponse.md)

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

# **get_inventory**
> GetInventoryResponse get_inventory(id)

Get one inventory item with platform listings.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.get_inventory_response import GetInventoryResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get one inventory item with platform listings.
        api_response = api_instance.get_inventory(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->get_inventory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**GetInventoryResponse**](GetInventoryResponse.md)

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

# **get_inventory_facet**
> GetInventoryFacetResponse get_inventory_facet()

Distinct brands + categories across this user's inventory.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.get_inventory_facet_response import GetInventoryFacetResponse
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Distinct brands + categories across this user's inventory.
        api_response = api_instance.get_inventory_facet()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->get_inventory_facet: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInventoryFacetResponse**](GetInventoryFacetResponse.md)

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

# **get_inventory_label**
> GetInventoryLabelResponse get_inventory_label()

List every distinct label across this user's inventory.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.get_inventory_label_response import GetInventoryLabelResponse
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List every distinct label across this user's inventory.
        api_response = api_instance.get_inventory_label()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->get_inventory_label: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInventoryLabelResponse**](GetInventoryLabelResponse.md)

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

# **get_inventory_label_stat**
> GetInventoryLabelStatResponse get_inventory_label_stat()

List distinct labels with usage counts + colors.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.get_inventory_label_stat_response import GetInventoryLabelStatResponse
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List distinct labels with usage counts + colors.
        api_response = api_instance.get_inventory_label_stat()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->get_inventory_label_stat: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInventoryLabelStatResponse**](GetInventoryLabelStatResponse.md)

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

# **get_inventory_sku_exist**
> GetInventorySkuExistResponse get_inventory_sku_exist(sku)

Check whether a SKU is already in use on this user's inventory.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.get_inventory_sku_exist_response import GetInventorySkuExistResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    sku = "sku_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Check whether a SKU is already in use on this user's inventory.
        api_response = api_instance.get_inventory_sku_exist(sku)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->get_inventory_sku_exist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  |

### Return type

[**GetInventorySkuExistResponse**](GetInventorySkuExistResponse.md)

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

# **get_spatial_public**
> GetSpatialPublicResponse get_spatial_public(slug)

A shared room, as a visitor sees it.

The room behind a share link: container geometry in METRES matching the real physical object, the solved arrangement, and one row per object on the shelves. REDACTED relative to the owner's view — no cost, no storage location, no listing status — so do not expect the fields /v1/spatial/scenes/{id} returns. Each placement carries `pinned`: true means a HUMAN put it there and it will not move; false means a layout SOLVER chose, and it may choose differently once the stock changes, so an unpinned placement is never a statement about where something physically is. `solved.overflow` lists what did not fit — a non-empty array means the room is INCOMPLETE and `stats.itemCount` exceeds what is on screen. Resolves rooms shared as `unlisted` as well as `public`: holding the link is the permission.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.get_spatial_public_response import GetSpatialPublicResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A shared room, as a visitor sees it.
        api_response = api_instance.get_spatial_public(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->get_spatial_public: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

[**GetSpatialPublicResponse**](GetSpatialPublicResponse.md)

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

# **get_spatial_scene**
> GetSpatialSceneResponse get_spatial_scene(id)

A solved room: every item, where it sits, and why.

Returns the space profile (container geometry in METRES, matching the real physical object), the solved placements, and the items. Placements carry a `pinned` flag: true means a human put it there and the layout solver will not move it; false means the solver chose, and it may choose differently once the stock changes. `overflow` lists anything that did not fit — it is reported, never silently dropped.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.get_spatial_scene_response import GetSpatialSceneResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A solved room: every item, where it sits, and why.
        api_response = api_instance.get_spatial_scene(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->get_spatial_scene: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**GetSpatialSceneResponse**](GetSpatialSceneResponse.md)

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

# **list_inventory**
> bool, date, datetime, dict, float, int, list, str, none_type list_inventory()

List inventory items.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.list_inventory_item import ListInventoryItem
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
    api_instance = inventory_api.InventoryApi(api_client)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    limit = 25 # int |  (optional) if omitted the server will use the default value of 25
    search = "search_example" # str |  (optional)
    status = "status_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List inventory items.
        api_response = api_instance.list_inventory(page=page, limit=limit, search=search, status=status)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->list_inventory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 25
 **search** | **str**|  | [optional]
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

# **list_inventory_activity**
> bool, date, datetime, dict, float, int, list, str, none_type list_inventory_activity(id)

Activity log for an inventory item (created/sold/edited/etc.).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.list_inventory_activity_item import ListInventoryActivityItem
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
    api_instance = inventory_api.InventoryApi(api_client)
    id = "id_example" # str | 
    limit = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Activity log for an inventory item (created/sold/edited/etc.).
        api_response = api_instance.list_inventory_activity(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->list_inventory_activity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Activity log for an inventory item (created/sold/edited/etc.).
        api_response = api_instance.list_inventory_activity(id, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->list_inventory_activity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 50

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

# **list_inventory_ids**
> bool, date, datetime, dict, float, int, list, str, none_type list_inventory_ids()

Filter inventory → return matching id list.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Filter inventory → return matching id list.
        api_response = api_instance.list_inventory_ids()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->list_inventory_ids: %s\n" % e)
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

# **list_inventory_units**
> bool, date, datetime, dict, float, int, list, str, none_type list_inventory_units(id)

List the individually identified units of an inventory item.

Each identifier carries a `strength` describing what it proves: `strong` was recorded before the item sold, `good` at packing, `weak` only after it shipped. The grade is derived from when it was recorded, never from the value itself.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.list_inventory_units_item import ListInventoryUnitsItem
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
    api_instance = inventory_api.InventoryApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List the individually identified units of an inventory item.
        api_response = api_instance.list_inventory_units(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->list_inventory_units: %s\n" % e)
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

# **list_spatial_public**
> bool, date, datetime, dict, float, int, list, str, none_type list_spatial_public()

Public rooms anyone can walk into.

The directory behind world-hopping. A room becomes public when its owner shares it; this lists those, newest first, with enough to draw a doorway AND enough to choose one — name, slug, category, itemCount, up to four previewImages, forSaleCount, a priceFromCents/priceToCents band and updatedAt. The band is the cheapest and dearest thing for sale in the room, never a quote for one object: /api/public/spatial/{slug}/offers is the authority on that. Fetch the room itself from /api/public/spatial/{slug}. Rooms with no items are omitted: an empty room is not a destination.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.list_spatial_public_item import ListSpatialPublicItem
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Public rooms anyone can walk into.
        api_response = api_instance.list_spatial_public()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->list_spatial_public: %s\n" % e)
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

# **list_spatial_public_offers**
> bool, date, datetime, dict, float, int, list, str, none_type list_spatial_public_offers(slug)

What is for sale in a shared room.

Price, stock, condition and grade for everything in the room its owner is actually selling. Correlate to the room by `itemId`, which is the SAME id the scene payload publishes per item — never by title. An item in the room with no row here is not for sale; an empty array means the owner is showing the collection rather than selling it, which is a different answer from a 404 (no such shared room). SEPARATE CALL ON PURPOSE: the room's geometry is stable for minutes, a price is not — it changes whenever the seller edits a listing. Re-read this before quoting, and do not cache a price alongside a cached room. `priceCents` is CENTS. `available` is remaining stock, or null when the listing declares none; null is unknown, not zero. Where an item sits inside more than one active listing, the offer quoted is the one for that item alone rather than a bundle it belongs to.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.list_spatial_public_offers_item import ListSpatialPublicOffersItem
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
    api_instance = inventory_api.InventoryApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # What is for sale in a shared room.
        api_response = api_instance.list_spatial_public_offers(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->list_spatial_public_offers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

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

# **list_spatial_scene_movements**
> bool, date, datetime, dict, float, int, list, str, none_type list_spatial_scene_movements(id)

Stock movements in a room over a time window.

One row per physical transition: which item, from which node, to which node, when, and of what kind (placed/moved/picked/shipped/received/removed). Nodes are referenced by id; the `fromCode`/`toCode` strings are display snapshots of the location code AT THE TIME and are not stable identifiers — correlate on the node ids. `since`/`until` are ISO timestamps, defaulting to the last seven days and clamped to 90. Movements are NOT attributed to individual team members on this surface: a token has no team role, so there is no honest way to decide whether its holder may see who did the work.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.list_spatial_scene_movements_item import ListSpatialSceneMovementsItem
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
    api_instance = inventory_api.InventoryApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Stock movements in a room over a time window.
        api_response = api_instance.list_spatial_scene_movements(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->list_spatial_scene_movements: %s\n" % e)
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

# **list_spatial_scenes**
> bool, date, datetime, dict, float, int, list, str, none_type list_spatial_scenes()

The rooms this account has.

One per market category the seller holds catalog-resolved stock in, plus a warehouse. Rooms are created on first read rather than requiring setup, so this call is safe to treat as the entry point.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.list_spatial_scenes_item import ListSpatialScenesItem
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
    api_instance = inventory_api.InventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The rooms this account has.
        api_response = api_instance.list_spatial_scenes()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->list_spatial_scenes: %s\n" % e)
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

# **update_inventory**
> UpdateInventoryResponse update_inventory(id)

Update an inventory item (partial).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inventory_api
from crossly.model.error import Error
from crossly.model.update_inventory_response import UpdateInventoryResponse
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
    api_instance = inventory_api.InventoryApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update an inventory item (partial).
        api_response = api_instance.update_inventory(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InventoryApi->update_inventory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UpdateInventoryResponse**](UpdateInventoryResponse.md)

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

