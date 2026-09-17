# crossly_buyer.BuyerMonitorsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_buyer_monitor**](BuyerMonitorsApi.md#create_buyer_monitor) | **POST** /v1/buyer/monitors | Watch a search, and be told when it matches.
[**delete_buyer_monitor**](BuyerMonitorsApi.md#delete_buyer_monitor) | **DELETE** /v1/buyer/monitors/{id} | Delete a monitor.
[**list_buyer_monitor_matches**](BuyerMonitorsApi.md#list_buyer_monitor_matches) | **GET** /v1/buyer/monitors/{id}/matches | What this monitor has matched.
[**list_buyer_monitors**](BuyerMonitorsApi.md#list_buyer_monitors) | **GET** /v1/buyer/monitors | Your monitors.
[**update_buyer_monitor**](BuyerMonitorsApi.md#update_buyer_monitor) | **PATCH** /v1/buyer/monitors/{id} | Pause, resume or rename a monitor.


# **create_buyer_monitor**
> CreateBuyerMonitorResponse create_buyer_monitor()

Watch a search, and be told when it matches.

Works immediately — there is no review step. The signing secret is returned ONCE, here; it is never readable again. The first sweep SEEDS without firing: a restock alert created while the item is already in stock has not observed a restock, and a new-listing monitor would otherwise deliver the entire back catalogue.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_monitors_api
from crossly_buyer.model.create_buyer_monitor_response import CreateBuyerMonitorResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_monitors_api.BuyerMonitorsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Watch a search, and be told when it matches.
        api_response = api_instance.create_buyer_monitor()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerMonitorsApi->create_buyer_monitor: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateBuyerMonitorResponse**](CreateBuyerMonitorResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **delete_buyer_monitor**
> delete_buyer_monitor(id)

Delete a monitor.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_monitors_api
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_monitors_api.BuyerMonitorsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a monitor.
        api_instance.delete_buyer_monitor(id)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerMonitorsApi->delete_buyer_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content — the request succeeded and there is no body. |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_monitor_matches**
> bool, date, datetime, dict, float, int, list, str, none_type list_buyer_monitor_matches(id)

What this monitor has matched.

The read side of a `poll` monitor, and an audit trail for a `webhook` one — so a missed delivery does not mean lost data.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_monitors_api
from crossly_buyer.model.list_buyer_monitor_matches_item import ListBuyerMonitorMatchesItem
from crossly_buyer.model.v1_list import V1List
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_monitors_api.BuyerMonitorsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # What this monitor has matched.
        api_response = api_instance.list_buyer_monitor_matches(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerMonitorsApi->list_buyer_monitor_matches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **list_buyer_monitors**
> bool, date, datetime, dict, float, int, list, str, none_type list_buyer_monitors()

Your monitors.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_monitors_api
from crossly_buyer.model.list_buyer_monitors_item import ListBuyerMonitorsItem
from crossly_buyer.model.v1_list import V1List
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_monitors_api.BuyerMonitorsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your monitors.
        api_response = api_instance.list_buyer_monitors()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerMonitorsApi->list_buyer_monitors: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **update_buyer_monitor**
> UpdateBuyerMonitorResponse update_buyer_monitor(id)

Pause, resume or rename a monitor.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_monitors_api
from crossly_buyer.model.update_buyer_monitor_response import UpdateBuyerMonitorResponse
from crossly_buyer.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_monitors_api.BuyerMonitorsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Pause, resume or rename a monitor.
        api_response = api_instance.update_buyer_monitor(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerMonitorsApi->update_buyer_monitor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UpdateBuyerMonitorResponse**](UpdateBuyerMonitorResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

