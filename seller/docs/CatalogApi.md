# crossly.CatalogApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_lookup**](CatalogApi.md#get_catalog_lookup) | **GET** /v1/catalog/lookup | Live Crossly offers for a product identifier (barcode, style code, LEGO set…).


# **get_catalog_lookup**
> GetCatalogLookupResponse get_catalog_lookup(namespace, value)

Live Crossly offers for a product identifier (barcode, style code, LEGO set…).

Identifier-first: a GTIN is validated against its GS1 check digit and every length is normalised to 14 digits before lookup, so a UPC-A and its EAN-13 twin resolve to the same product. There is no fuzzy fallback — an identifier we cannot validate returns nothing rather than a guess.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import catalog_api
from crossly.model.error import Error
from crossly.model.get_catalog_lookup_response import GetCatalogLookupResponse
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
    api_instance = catalog_api.CatalogApi(api_client)
    namespace = "gtin" # str | 
    value = "value_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Live Crossly offers for a product identifier (barcode, style code, LEGO set…).
        api_response = api_instance.get_catalog_lookup(namespace, value)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CatalogApi->get_catalog_lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  |
 **value** | **str**|  |

### Return type

[**GetCatalogLookupResponse**](GetCatalogLookupResponse.md)

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

