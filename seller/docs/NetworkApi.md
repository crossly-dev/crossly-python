# crossly.NetworkApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_pool**](NetworkApi.md#create_network_pool) | **POST** /v1/network/pool | Join the Crossly Network reciprocal engagement pool.
[**delete_network_pool**](NetworkApi.md#delete_network_pool) | **DELETE** /v1/network/pool | Leave the Crossly Network pool.
[**get_network_pool**](NetworkApi.md#get_network_pool) | **GET** /v1/network/pool | The seller&#39;s Crossly Network pool membership row.
[**get_network_pool_size**](NetworkApi.md#get_network_pool_size) | **GET** /v1/network/pool/size | Total members in the Crossly Network pool.
[**list_network_pool_log**](NetworkApi.md#list_network_pool_log) | **GET** /v1/network/pool/log | Recent engagement history — both sent and received.
[**update_network_pool**](NetworkApi.md#update_network_pool) | **PATCH** /v1/network/pool | Update per-action toggles + platforms on pool membership.


# **create_network_pool**
> CreateNetworkPoolResponse create_network_pool()

Join the Crossly Network reciprocal engagement pool.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import network_api
from crossly.model.error import Error
from crossly.model.create_network_pool_response import CreateNetworkPoolResponse
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
    api_instance = network_api.NetworkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Join the Crossly Network reciprocal engagement pool.
        api_response = api_instance.create_network_pool()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NetworkApi->create_network_pool: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateNetworkPoolResponse**](CreateNetworkPoolResponse.md)

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

# **delete_network_pool**
> DeleteNetworkPoolResponse delete_network_pool()

Leave the Crossly Network pool.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import network_api
from crossly.model.delete_network_pool_response import DeleteNetworkPoolResponse
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
    api_instance = network_api.NetworkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Leave the Crossly Network pool.
        api_response = api_instance.delete_network_pool()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NetworkApi->delete_network_pool: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DeleteNetworkPoolResponse**](DeleteNetworkPoolResponse.md)

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

# **get_network_pool**
> GetNetworkPoolResponse get_network_pool()

The seller's Crossly Network pool membership row.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import network_api
from crossly.model.error import Error
from crossly.model.get_network_pool_response import GetNetworkPoolResponse
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
    api_instance = network_api.NetworkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The seller's Crossly Network pool membership row.
        api_response = api_instance.get_network_pool()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NetworkApi->get_network_pool: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNetworkPoolResponse**](GetNetworkPoolResponse.md)

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

# **get_network_pool_size**
> GetNetworkPoolSizeResponse get_network_pool_size()

Total members in the Crossly Network pool.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import network_api
from crossly.model.error import Error
from crossly.model.get_network_pool_size_response import GetNetworkPoolSizeResponse
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
    api_instance = network_api.NetworkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Total members in the Crossly Network pool.
        api_response = api_instance.get_network_pool_size()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NetworkApi->get_network_pool_size: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNetworkPoolSizeResponse**](GetNetworkPoolSizeResponse.md)

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

# **list_network_pool_log**
> bool, date, datetime, dict, float, int, list, str, none_type list_network_pool_log()

Recent engagement history — both sent and received.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import network_api
from crossly.model.list_network_pool_log_item import ListNetworkPoolLogItem
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
    api_instance = network_api.NetworkApi(api_client)
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Recent engagement history — both sent and received.
        api_response = api_instance.list_network_pool_log(limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NetworkApi->list_network_pool_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100

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

# **update_network_pool**
> UpdateNetworkPoolResponse update_network_pool()

Update per-action toggles + platforms on pool membership.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import network_api
from crossly.model.update_network_pool_response import UpdateNetworkPoolResponse
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
    api_instance = network_api.NetworkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update per-action toggles + platforms on pool membership.
        api_response = api_instance.update_network_pool()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NetworkApi->update_network_pool: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UpdateNetworkPoolResponse**](UpdateNetworkPoolResponse.md)

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

