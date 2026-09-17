# crossly.PATApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pat**](PATApi.md#create_pat) | **POST** /v1/pat | Mint a new PAT. Full token returned ONCE — store it on the client.
[**delete_pat**](PATApi.md#delete_pat) | **DELETE** /v1/pat/{id} | Revoke a PAT by id.
[**get_pat_scope**](PATApi.md#get_pat_scope) | **GET** /v1/pat/scopes | List the canonical scope catalog.
[**list_pat**](PATApi.md#list_pat) | **GET** /v1/pat | List the caller&#39;s PATs (preview only).


# **create_pat**
> CreatePatResponse create_pat()

Mint a new PAT. Full token returned ONCE — store it on the client.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import pat_api
from crossly.model.create_pat_response import CreatePatResponse
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
    api_instance = pat_api.PATApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Mint a new PAT. Full token returned ONCE — store it on the client.
        api_response = api_instance.create_pat()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PATApi->create_pat: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreatePatResponse**](CreatePatResponse.md)

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

# **delete_pat**
> DeletePatResponse delete_pat(id)

Revoke a PAT by id.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import pat_api
from crossly.model.error import Error
from crossly.model.delete_pat_response import DeletePatResponse
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
    api_instance = pat_api.PATApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke a PAT by id.
        api_response = api_instance.delete_pat(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PATApi->delete_pat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DeletePatResponse**](DeletePatResponse.md)

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

# **get_pat_scope**
> GetPatScopeResponse get_pat_scope()

List the canonical scope catalog.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import pat_api
from crossly.model.error import Error
from crossly.model.get_pat_scope_response import GetPatScopeResponse
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
    api_instance = pat_api.PATApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the canonical scope catalog.
        api_response = api_instance.get_pat_scope()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PATApi->get_pat_scope: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPatScopeResponse**](GetPatScopeResponse.md)

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

# **list_pat**
> bool, date, datetime, dict, float, int, list, str, none_type list_pat()

List the caller's PATs (preview only).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import pat_api
from crossly.model.error import Error
from crossly.model.list_pat_item import ListPatItem
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
    api_instance = pat_api.PATApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the caller's PATs (preview only).
        api_response = api_instance.list_pat()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PATApi->list_pat: %s\n" % e)
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

