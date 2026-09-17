# crossly.CustomersApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_bulk_delete**](CustomersApi.md#create_customer_bulk_delete) | **POST** /v1/customers/bulk-delete | Bulk blocklist customer handles.
[**create_customer_bulk_export**](CustomersApi.md#create_customer_bulk_export) | **POST** /v1/customers/bulk-export | Bulk export aggregated customers as CSV.
[**get_customer**](CustomersApi.md#get_customer) | **GET** /v1/customers/{handle} | Get one customer with their recent 50 orders.
[**list_customers**](CustomersApi.md#list_customers) | **GET** /v1/customers | List aggregated customers (group-by lower(buyer_username)).


# **create_customer_bulk_delete**
> CreateCustomerBulkDeleteResponse create_customer_bulk_delete()

Bulk blocklist customer handles.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
from crossly.model.error import Error
from crossly.model.create_customer_bulk_delete_response import CreateCustomerBulkDeleteResponse
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
    api_instance = customers_api.CustomersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk blocklist customer handles.
        api_response = api_instance.create_customer_bulk_delete()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->create_customer_bulk_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateCustomerBulkDeleteResponse**](CreateCustomerBulkDeleteResponse.md)

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

# **create_customer_bulk_export**
> str create_customer_bulk_export()

Bulk export aggregated customers as CSV.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
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
    api_instance = customers_api.CustomersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk export aggregated customers as CSV.
        api_response = api_instance.create_customer_bulk_export()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->create_customer_bulk_export: %s\n" % e)
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

# **get_customer**
> GetCustomerResponse get_customer(handle)

Get one customer with their recent 50 orders.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
from crossly.model.error import Error
from crossly.model.get_customer_response import GetCustomerResponse
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
    api_instance = customers_api.CustomersApi(api_client)
    handle = "handle_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get one customer with their recent 50 orders.
        api_response = api_instance.get_customer(handle)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->get_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**|  |

### Return type

[**GetCustomerResponse**](GetCustomerResponse.md)

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

# **list_customers**
> bool, date, datetime, dict, float, int, list, str, none_type list_customers()

List aggregated customers (group-by lower(buyer_username)).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
from crossly.model.error import Error
from crossly.model.list_customers_item import ListCustomersItem
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
    api_instance = customers_api.CustomersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List aggregated customers (group-by lower(buyer_username)).
        api_response = api_instance.list_customers()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->list_customers: %s\n" % e)
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

