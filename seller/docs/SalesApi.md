# crossly.SalesApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sale_bulk_delete**](SalesApi.md#create_sale_bulk_delete) | **POST** /v1/sales/bulk-delete | Bulk soft-delete sales rows.
[**list_sales**](SalesApi.md#list_sales) | **GET** /v1/sales | List sales (each unique sale event).


# **create_sale_bulk_delete**
> CreateSaleBulkDeleteResponse create_sale_bulk_delete()

Bulk soft-delete sales rows.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sales_api
from crossly.model.create_sale_bulk_delete_response import CreateSaleBulkDeleteResponse
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
    api_instance = sales_api.SalesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk soft-delete sales rows.
        api_response = api_instance.create_sale_bulk_delete()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SalesApi->create_sale_bulk_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateSaleBulkDeleteResponse**](CreateSaleBulkDeleteResponse.md)

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

# **list_sales**
> bool, date, datetime, dict, float, int, list, str, none_type list_sales()

List sales (each unique sale event).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sales_api
from crossly.model.list_sales_item import ListSalesItem
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
    api_instance = sales_api.SalesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List sales (each unique sale event).
        api_response = api_instance.list_sales()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SalesApi->list_sales: %s\n" % e)
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

