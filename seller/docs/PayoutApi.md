# crossly.PayoutApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payout_estimate**](PayoutApi.md#get_payout_estimate) | **GET** /v1/payout/estimate | What one platform nets at a given price, after fees and shipping.
[**get_payout_gross_for_net**](PayoutApi.md#get_payout_gross_for_net) | **GET** /v1/payout/gross-for-net | The gross price needed to clear a target net on one platform.
[**list_payout_compare**](PayoutApi.md#list_payout_compare) | **GET** /v1/payout/compare | Rank platforms by what they net at a given price. Defaults to connected ones.


# **get_payout_estimate**
> GetPayoutEstimateResponse get_payout_estimate()

What one platform nets at a given price, after fees and shipping.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.error import Error
from crossly.model.get_payout_estimate_response import GetPayoutEstimateResponse
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
    api_instance = payout_api.PayoutApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What one platform nets at a given price, after fees and shipping.
        api_response = api_instance.get_payout_estimate()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PayoutApi->get_payout_estimate: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPayoutEstimateResponse**](GetPayoutEstimateResponse.md)

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

# **get_payout_gross_for_net**
> GetPayoutGrossForNetResponse get_payout_gross_for_net()

The gross price needed to clear a target net on one platform.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.get_payout_gross_for_net_response import GetPayoutGrossForNetResponse
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
    api_instance = payout_api.PayoutApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The gross price needed to clear a target net on one platform.
        api_response = api_instance.get_payout_gross_for_net()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PayoutApi->get_payout_gross_for_net: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPayoutGrossForNetResponse**](GetPayoutGrossForNetResponse.md)

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

# **list_payout_compare**
> bool, date, datetime, dict, float, int, list, str, none_type list_payout_compare()

Rank platforms by what they net at a given price. Defaults to connected ones.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.error import Error
from crossly.model.list_payout_compare_item import ListPayoutCompareItem
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
    api_instance = payout_api.PayoutApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Rank platforms by what they net at a given price. Defaults to connected ones.
        api_response = api_instance.list_payout_compare()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PayoutApi->list_payout_compare: %s\n" % e)
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

