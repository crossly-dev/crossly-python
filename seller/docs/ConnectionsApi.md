# crossly.ConnectionsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connection_health**](ConnectionsApi.md#get_connection_health) | **GET** /v1/connection-health | Health of each connected marketplace account, with a plain-English diagnosis.
[**list_devices**](ConnectionsApi.md#list_devices) | **GET** /v1/devices | Machines paired to this account, and what each can do.


# **get_connection_health**
> GetConnectionHealthResponse get_connection_health()

Health of each connected marketplace account, with a plain-English diagnosis.

One entry per ACCOUNT, not per platform — a healthy slot 1 must not speak for a dead slot 2. States that were never measured are reported as \"unknown\" rather than as failures.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import connections_api
from crossly.model.get_connection_health_response import GetConnectionHealthResponse
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
    api_instance = connections_api.ConnectionsApi(api_client)
    include_unconnected = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Health of each connected marketplace account, with a plain-English diagnosis.
        api_response = api_instance.get_connection_health(include_unconnected=include_unconnected)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ConnectionsApi->get_connection_health: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_unconnected** | **bool**|  | [optional]

### Return type

[**GetConnectionHealthResponse**](GetConnectionHealthResponse.md)

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

# **list_devices**
> bool, date, datetime, dict, float, int, list, str, none_type list_devices()

Machines paired to this account, and what each can do.

Capabilities are what the machine DECLARED it can do at pairing — print, scan_watch, browser, cookie_jar, proxy_bind, scale. A machine only declares \"scale\" when one actually answered, never on the assumption that one might.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import connections_api
from crossly.model.list_devices_item import ListDevicesItem
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
    api_instance = connections_api.ConnectionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Machines paired to this account, and what each can do.
        api_response = api_instance.list_devices()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ConnectionsApi->list_devices: %s\n" % e)
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

