# crossly.ScanApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_scan_captures**](ScanApi.md#list_scan_captures) | **GET** /v1/scan/captures | Your capture sessions and what they produced.
[**list_scan_models**](ScanApi.md#list_scan_models) | **GET** /v1/scan/models | Which items already have a 3D model.


# **list_scan_captures**
> ListScanCapturesResponse list_scan_captures()

Your capture sessions and what they produced.

One row per scan, newest first. `status` is capturing | uploaded | processing | ready | failed | rejected; `rejectReason` says why in the same words the seller was shown. A capture that reports `ready` with no mesh is normal — most items are textured onto a known shape rather than having geometry generated, which is cheaper and looks the same. When an item that WOULD have been generated was not, `generationSkipped` says why: out of monthly allowance, too few distinct angles, or you had already had a model built from this object.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import scan_api
from crossly.model.common.error import Error
from crossly.model.common.list_scan_captures_response import ListScanCapturesResponse
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
    api_instance = scan_api.ScanApi(api_client)
    status = "status_example" # str | Filter to one status. (optional)
    limit = 25 # int |  (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Your capture sessions and what they produced.
        api_response = api_instance.list_scan_captures(status=status, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ScanApi->list_scan_captures: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter to one status. | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 25

### Return type

**ListScanCapturesResponse**

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

# **list_scan_models**
> ListScanModelsResponse list_scan_models()

Which items already have a 3D model.

Ask by CATALOGUE variant (`variantIds`) or by your own inventory rows (`inventoryItemIds`), comma separated, up to 200 of each. At least one is required. Returns only the ones that have a model. The two are different KINDS of answer. A catalogue model belongs to the product and is shared: a hit means your listing gets it with nothing to capture, because somebody else already paid to generate it. An inventory model belongs to one of your rows, because an object with no catalogue identity — a lamp, a one-off — is not a product anyone else can claim. `longestEdgeMm` is present only when a capture MEASURED the item against something of known size; null means the mesh has correct proportions and no real-world scale.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import scan_api
from crossly.model.common.list_scan_models_response import ListScanModelsResponse
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
    api_instance = scan_api.ScanApi(api_client)
    variant_ids = "variantIds_example" # str | Comma-separated catalogue variant ids, max 200. (optional)
    inventory_item_ids = "inventoryItemIds_example" # str | Comma-separated inventory item ids, max 200. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Which items already have a 3D model.
        api_response = api_instance.list_scan_models(variant_ids=variant_ids, inventory_item_ids=inventory_item_ids)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ScanApi->list_scan_models: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variant_ids** | **str**| Comma-separated catalogue variant ids, max 200. | [optional]
 **inventory_item_ids** | **str**| Comma-separated inventory item ids, max 200. | [optional]

### Return type

**ListScanModelsResponse**

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

