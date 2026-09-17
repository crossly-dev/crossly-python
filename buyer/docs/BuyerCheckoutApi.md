# crossly_buyer.BuyerCheckoutApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_buyer_checkout**](BuyerCheckoutApi.md#create_buyer_checkout) | **POST** /v1/buyer/checkout | Buy a listing without being present.
[**get_buyer_checkout_control**](BuyerCheckoutApi.md#get_buyer_checkout_control) | **GET** /v1/buyer/checkout/controls | What this key is allowed to spend.
[**update_buyer_checkout_control**](BuyerCheckoutApi.md#update_buyer_checkout_control) | **PUT** /v1/buyer/checkout/controls | Switch this key on for spending, and set its limits.


# **create_buyer_checkout**
> CreateBuyerCheckoutResponse create_buyer_checkout()

Buy a listing without being present.

An Idempotency-Key header is REQUIRED — this endpoint refuses without one, because a retried request would otherwise buy the item twice and a retry is the most likely thing an automated buyer does. Derive the key from what you are buying and reuse it across retries; a fresh random value per attempt satisfies the check and keeps the bug. The item is QUOTED first and the delivered total is checked against both your maxTotalCents and this key's limits before anything is charged. A card that demands 3-D Secure cannot be charged unattended; that answers 402 with `authentication_required` and the purchase must be finished on Crossly.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_checkout_api
from crossly_buyer.model.create_buyer_checkout_response import CreateBuyerCheckoutResponse
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
    api_instance = buyer_checkout_api.BuyerCheckoutApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Buy a listing without being present.
        api_response = api_instance.create_buyer_checkout()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCheckoutApi->create_buyer_checkout: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateBuyerCheckoutResponse**](CreateBuyerCheckoutResponse.md)

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

# **get_buyer_checkout_control**
> GetBuyerCheckoutControlResponse get_buyer_checkout_control()

What this key is allowed to spend.

Reports the controls for the key making the call — not for your account. Every key has its own switch and its own limits.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_checkout_api
from crossly_buyer.model.get_buyer_checkout_control_response import GetBuyerCheckoutControlResponse
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
    api_instance = buyer_checkout_api.BuyerCheckoutApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What this key is allowed to spend.
        api_response = api_instance.get_buyer_checkout_control()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCheckoutApi->get_buyer_checkout_control: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBuyerCheckoutControlResponse**](GetBuyerCheckoutControlResponse.md)

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

# **update_buyer_checkout_control**
> UpdateBuyerCheckoutControlResponse update_buyer_checkout_control()

Switch this key on for spending, and set its limits.

A key can only ever raise or lower ITS OWN limits, and only if the token already carries buyer:checkout:write. Turning it off takes effect immediately.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_checkout_api
from crossly_buyer.model.update_buyer_checkout_control_response import UpdateBuyerCheckoutControlResponse
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
    api_instance = buyer_checkout_api.BuyerCheckoutApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Switch this key on for spending, and set its limits.
        api_response = api_instance.update_buyer_checkout_control()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerCheckoutApi->update_buyer_checkout_control: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UpdateBuyerCheckoutControlResponse**](UpdateBuyerCheckoutControlResponse.md)

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

