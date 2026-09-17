# crossly.BillingApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_upgrade**](BillingApi.md#create_billing_upgrade) | **POST** /v1/billing/upgrade | Start an upgrade to a higher plan.


# **create_billing_upgrade**
> CreateBillingUpgradeResponse create_billing_upgrade(inline_object)

Start an upgrade to a higher plan.

Returns a Stripe Checkout URL. Nothing is charged by this call — a person completes the payment. Downgrades and cancellation are not available to a token at all; they stay with the account owner.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import billing_api
from crossly.model.create_billing_upgrade_response import CreateBillingUpgradeResponse
from crossly.model.error import Error
from crossly.model.inline_object import InlineObject
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
    api_instance = billing_api.BillingApi(api_client)
    inline_object = InlineObject(
        tier="starter",
        interval="monthly",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Start an upgrade to a higher plan.
        api_response = api_instance.create_billing_upgrade(inline_object)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BillingApi->create_billing_upgrade: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

[**CreateBillingUpgradeResponse**](CreateBillingUpgradeResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
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

