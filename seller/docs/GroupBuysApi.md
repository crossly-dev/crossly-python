# crossly.GroupBuysApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_buy**](GroupBuysApi.md#create_group_buy) | **POST** /v1/group-buys | Run a group buy on a listing with stock: price tiers by buyer count, a minimum, up to 6 days. Below the minimum nobody pays.


# **create_group_buy**
> CreateBreakResponse create_group_buy()

Run a group buy on a listing with stock: price tiers by buyer count, a minimum, up to 6 days. Below the minimum nobody pays.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import group_buys_api
from crossly.model.common.error import Error
from crossly.model.breaks.create_break_response import CreateBreakResponse
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
    api_instance = group_buys_api.GroupBuysApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Run a group buy on a listing with stock: price tiers by buyer count, a minimum, up to 6 days. Below the minimum nobody pays.
        api_response = api_instance.create_group_buy()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling GroupBuysApi->create_group_buy: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateBreakResponse**

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

