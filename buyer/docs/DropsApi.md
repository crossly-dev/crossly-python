# crossly_buyer.DropsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_buyer_drop_join**](DropsApi.md#create_buyer_drop_join) | **POST** /v1/buyer/drops/{id}/join | Join a drop&#39;s line while it is open: one entry per account, the same odds as joining in the world. Repeating it returns the same entry.
[**delete_buyer_drop_join**](DropsApi.md#delete_buyer_drop_join) | **DELETE** /v1/buyer/drops/{id}/join | Leave a drop&#39;s line before the draw.
[**get_buyer_drop_me**](DropsApi.md#get_buyer_drop_me) | **GET** /v1/buyer/drops/{id}/me | Your entry in a drop: in line or not, your draw rank and outcome, and the checkout path while your 15-minute hold is live.


# **create_buyer_drop_join**
> CreateBuyerDropJoinResponse create_buyer_drop_join(id)

Join a drop's line while it is open: one entry per account, the same odds as joining in the world. Repeating it returns the same entry.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import drops_api
from crossly_buyer.model.common.create_buyer_drop_join_response import CreateBuyerDropJoinResponse
from crossly_buyer.model.common.error import Error
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
    api_instance = drops_api.DropsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Join a drop's line while it is open: one entry per account, the same odds as joining in the world. Repeating it returns the same entry.
        api_response = api_instance.create_buyer_drop_join(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling DropsApi->create_buyer_drop_join: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateBuyerDropJoinResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_buyer_drop_join**
> DeleteBuyerDropJoinResponse delete_buyer_drop_join(id)

Leave a drop's line before the draw.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import drops_api
from crossly_buyer.model.common.error import Error
from crossly_buyer.model.common.delete_buyer_drop_join_response import DeleteBuyerDropJoinResponse
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
    api_instance = drops_api.DropsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Leave a drop's line before the draw.
        api_response = api_instance.delete_buyer_drop_join(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling DropsApi->delete_buyer_drop_join: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteBuyerDropJoinResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_buyer_drop_me**
> GetBuyerDropMeResponse get_buyer_drop_me(id)

Your entry in a drop: in line or not, your draw rank and outcome, and the checkout path while your 15-minute hold is live.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import drops_api
from crossly_buyer.model.common.error import Error
from crossly_buyer.model.common.get_buyer_drop_me_response import GetBuyerDropMeResponse
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
    api_instance = drops_api.DropsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your entry in a drop: in line or not, your draw rank and outcome, and the checkout path while your 15-minute hold is live.
        api_response = api_instance.get_buyer_drop_me(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling DropsApi->get_buyer_drop_me: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetBuyerDropMeResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

