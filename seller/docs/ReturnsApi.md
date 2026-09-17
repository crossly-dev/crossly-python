# crossly.ReturnsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_return**](ReturnsApi.md#create_return) | **POST** /v1/returns | Open a return record on an order (rejects if another open return exists).
[**get_return**](ReturnsApi.md#get_return) | **GET** /v1/returns/{id} | Get one return record.
[**list_returns**](ReturnsApi.md#list_returns) | **GET** /v1/returns | List returns (physical-return workflow). status&#x3D;open|closed|&lt;exact&gt;.
[**update_return**](ReturnsApi.md#update_return) | **PATCH** /v1/returns/{id} | Transition return status (received/inspected/restocked) and bump inventory on restock.


# **create_return**
> CreateReturnResponse create_return()

Open a return record on an order (rejects if another open return exists).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import returns_api
from crossly.model.error import Error
from crossly.model.create_return_response import CreateReturnResponse
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
    api_instance = returns_api.ReturnsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Open a return record on an order (rejects if another open return exists).
        api_response = api_instance.create_return()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReturnsApi->create_return: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateReturnResponse**](CreateReturnResponse.md)

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

# **get_return**
> GetReturnResponse get_return(id)

Get one return record.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import returns_api
from crossly.model.get_return_response import GetReturnResponse
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
    api_instance = returns_api.ReturnsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get one return record.
        api_response = api_instance.get_return(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReturnsApi->get_return: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**GetReturnResponse**](GetReturnResponse.md)

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

# **list_returns**
> bool, date, datetime, dict, float, int, list, str, none_type list_returns()

List returns (physical-return workflow). status=open|closed|<exact>.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import returns_api
from crossly.model.error import Error
from crossly.model.list_returns_item import ListReturnsItem
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
    api_instance = returns_api.ReturnsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List returns (physical-return workflow). status=open|closed|<exact>.
        api_response = api_instance.list_returns()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReturnsApi->list_returns: %s\n" % e)
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

# **update_return**
> UpdateReturnResponse update_return(id)

Transition return status (received/inspected/restocked) and bump inventory on restock.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import returns_api
from crossly.model.update_return_response import UpdateReturnResponse
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
    api_instance = returns_api.ReturnsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Transition return status (received/inspected/restocked) and bump inventory on restock.
        api_response = api_instance.update_return(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReturnsApi->update_return: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UpdateReturnResponse**](UpdateReturnResponse.md)

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

