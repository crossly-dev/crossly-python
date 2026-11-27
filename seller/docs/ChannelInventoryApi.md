# crossly.ChannelInventoryApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_channel_inventory**](ChannelInventoryApi.md#delete_channel_inventory) | **DELETE** /v1/channel-inventory/{platform}/{slot} | Reset a channel&#39;s inventory controls to the default (no cap, no buffer, sync on, end on sell-out).
[**get_channel_inventory**](ChannelInventoryApi.md#get_channel_inventory) | **GET** /v1/channel-inventory/{platform}/{slot} | Get one channel&#39;s inventory controls.
[**list_channel_inventory**](ChannelInventoryApi.md#list_channel_inventory) | **GET** /v1/channel-inventory | List every sales channel with its inventory controls (cap, buffer, sync, out-of-stock action, exclusions).
[**update_channel_inventory**](ChannelInventoryApi.md#update_channel_inventory) | **PUT** /v1/channel-inventory/{platform}/{slot} | Set a channel&#39;s quantity cap, buffer, sync toggle, out-of-stock action and exclusion lists (merge write).


# **delete_channel_inventory**
> ListChannelInventoryItem delete_channel_inventory(platform, slot)

Reset a channel's inventory controls to the default (no cap, no buffer, sync on, end on sell-out).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import channel_inventory_api
from crossly.model.common.error import Error
from crossly.model.channel.list_channel_inventory_item import ListChannelInventoryItem
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
    api_instance = channel_inventory_api.ChannelInventoryApi(api_client)
    platform = "platform_example" # str | 
    slot = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Reset a channel's inventory controls to the default (no cap, no buffer, sync on, end on sell-out).
        api_response = api_instance.delete_channel_inventory(platform, slot)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ChannelInventoryApi->delete_channel_inventory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |
 **slot** | **int**|  |

### Return type

**ListChannelInventoryItem**

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

# **get_channel_inventory**
> ListChannelInventoryItem get_channel_inventory(platform, slot)

Get one channel's inventory controls.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import channel_inventory_api
from crossly.model.common.error import Error
from crossly.model.channel.list_channel_inventory_item import ListChannelInventoryItem
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
    api_instance = channel_inventory_api.ChannelInventoryApi(api_client)
    platform = "platform_example" # str | 
    slot = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get one channel's inventory controls.
        api_response = api_instance.get_channel_inventory(platform, slot)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ChannelInventoryApi->get_channel_inventory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |
 **slot** | **int**|  |

### Return type

**ListChannelInventoryItem**

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

# **list_channel_inventory**
> ListChannelInventoryResponse list_channel_inventory()

List every sales channel with its inventory controls (cap, buffer, sync, out-of-stock action, exclusions).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import channel_inventory_api
from crossly.model.common.error import Error
from crossly.model.channel.list_channel_inventory_response import ListChannelInventoryResponse
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
    api_instance = channel_inventory_api.ChannelInventoryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List every sales channel with its inventory controls (cap, buffer, sync, out-of-stock action, exclusions).
        api_response = api_instance.list_channel_inventory()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ChannelInventoryApi->list_channel_inventory: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListChannelInventoryResponse**

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

# **update_channel_inventory**
> ListChannelInventoryItem update_channel_inventory(platform, slot)

Set a channel's quantity cap, buffer, sync toggle, out-of-stock action and exclusion lists (merge write).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import channel_inventory_api
from crossly.model.common.error import Error
from crossly.model.channel.list_channel_inventory_item import ListChannelInventoryItem
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
    api_instance = channel_inventory_api.ChannelInventoryApi(api_client)
    platform = "platform_example" # str | 
    slot = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Set a channel's quantity cap, buffer, sync toggle, out-of-stock action and exclusion lists (merge write).
        api_response = api_instance.update_channel_inventory(platform, slot)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ChannelInventoryApi->update_channel_inventory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |
 **slot** | **int**|  |

### Return type

**ListChannelInventoryItem**

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

