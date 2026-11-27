# crossly.PayoutApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payout_connect_onboard**](PayoutApi.md#create_payout_connect_onboard) | **POST** /v1/payout/connect/onboard | Start or resume payout-account onboarding; returns a Stripe-hosted URL.
[**create_payout_identity_link**](PayoutApi.md#create_payout_identity_link) | **POST** /v1/payouts/identity/link | Continue with Stripe: a one-time Stripe-hosted link that collects what Stripe needs.
[**create_payout_payout**](PayoutApi.md#create_payout_payout) | **POST** /v1/payout/payouts | Pay out now: instant (fee, minutes, to an eligible card/bank) or standard (free, manual schedule only).
[**get_payout_connect**](PayoutApi.md#get_payout_connect) | **GET** /v1/payout/connect | Your Stripe payout account: status, country, agreement and payout currency.
[**get_payout_estimate**](PayoutApi.md#get_payout_estimate) | **GET** /v1/payout/estimate | What one platform nets at a given price, after fees and shipping.
[**get_payout_gross_for_net**](PayoutApi.md#get_payout_gross_for_net) | **GET** /v1/payout/gross-for-net | The gross price needed to clear a target net on one platform.
[**get_payout_identity**](PayoutApi.md#get_payout_identity) | **GET** /v1/payouts/identity | Stripe&#39;s verification of your payout account: status and what Stripe still needs, in plain words.
[**get_payout_wallet**](PayoutApi.md#get_payout_wallet) | **GET** /v1/payout/wallet | Your payout wallet: balances, schedule, next payout, instant-payout quote, methods, payouts, transactions.
[**list_payout_compare**](PayoutApi.md#list_payout_compare) | **GET** /v1/payout/compare | Rank platforms by what they net at a given price. Defaults to connected ones.
[**update_payout_schedule**](PayoutApi.md#update_payout_schedule) | **PUT** /v1/payout/schedule | Change the automatic payout schedule.


# **create_payout_connect_onboard**
> CreatePayoutConnectOnboardResponse create_payout_connect_onboard(create_payout_connect_onboard_request)

Start or resume payout-account onboarding; returns a Stripe-hosted URL.

country (ISO 3166-1 alpha-2) defaults to the storefront ship-from country, then US. Fixed once the account exists. Nothing is set up until a person completes the link.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.payout.create_payout_connect_onboard_response import CreatePayoutConnectOnboardResponse
from crossly.model.common.error import Error
from crossly.model.payout.create_payout_connect_onboard_request import CreatePayoutConnectOnboardRequest
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
    create_payout_connect_onboard_request = CreatePayoutConnectOnboardRequest(
        country="country_example",
    ) # CreatePayoutConnectOnboardRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start or resume payout-account onboarding; returns a Stripe-hosted URL.
        api_response = api_instance.create_payout_connect_onboard(create_payout_connect_onboard_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PayoutApi->create_payout_connect_onboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payout_connect_onboard_request** | **CreatePayoutConnectOnboardRequest**|  |

### Return type

**CreatePayoutConnectOnboardResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_payout_identity_link**
> CreatePayoutIdentityLinkResponse create_payout_identity_link(create_payout_connect_onboard_request)

Continue with Stripe: a one-time Stripe-hosted link that collects what Stripe needs.

Creates the payout account first when there is none (country: ISO alpha-2, default the ship-from country). type is account_onboarding (Stripe shows only what is outstanding) or account_update. The link expires in minutes; ask for a new one rather than storing it. Nothing changes until a person completes it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.common.error import Error
from crossly.model.payout.create_payout_identity_link_response import CreatePayoutIdentityLinkResponse
from crossly.model.payout.create_payout_connect_onboard_request import CreatePayoutConnectOnboardRequest
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
    create_payout_connect_onboard_request = CreatePayoutConnectOnboardRequest(
        country="country_example",
    ) # CreatePayoutConnectOnboardRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Continue with Stripe: a one-time Stripe-hosted link that collects what Stripe needs.
        api_response = api_instance.create_payout_identity_link(create_payout_connect_onboard_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PayoutApi->create_payout_identity_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payout_connect_onboard_request** | **CreatePayoutConnectOnboardRequest**|  |

### Return type

**CreatePayoutIdentityLinkResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_payout_payout**
> CreatePayoutPayoutResponse create_payout_payout(create_payout_payout_request)

Pay out now: instant (fee, minutes, to an eligible card/bank) or standard (free, manual schedule only).

amountCents defaults to everything eligible. Pass idempotencyKey so a retry is the same payout. Returns { payout, feeCents }. 409 when the account cannot be paid or instant is unavailable.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.payout.create_payout_payout_response import CreatePayoutPayoutResponse
from crossly.model.payout.create_payout_payout_request import CreatePayoutPayoutRequest
from crossly.model.common.error import Error
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
    create_payout_payout_request = CreatePayoutPayoutRequest(
        method="instant",
        amount_cents=1,
        destination="destination_example",
        idempotency_key="idempotency_key_example",
    ) # CreatePayoutPayoutRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Pay out now: instant (fee, minutes, to an eligible card/bank) or standard (free, manual schedule only).
        api_response = api_instance.create_payout_payout(create_payout_payout_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PayoutApi->create_payout_payout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payout_payout_request** | **CreatePayoutPayoutRequest**|  |

### Return type

**CreatePayoutPayoutResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_payout_connect**
> GetPayoutConnectResponse get_payout_connect()

Your Stripe payout account: status, country, agreement and payout currency.

status is not_started (with defaultCountry), pending, active, restricted or payouts_unavailable. Only active can be paid; payouts_unavailable means Stripe offers no payout path to the account's country yet.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.common.error import Error
from crossly.model.payout.get_payout_connect_response import GetPayoutConnectResponse
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
        # Your Stripe payout account: status, country, agreement and payout currency.
        api_response = api_instance.get_payout_connect()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PayoutApi->get_payout_connect: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetPayoutConnectResponse**

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

# **get_payout_estimate**
> GetPayoutEstimateResponse get_payout_estimate()

What one platform nets at a given price, after fees and shipping.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.common.error import Error
from crossly.model.payout.get_payout_estimate_response import GetPayoutEstimateResponse
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

**GetPayoutEstimateResponse**

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

# **get_payout_gross_for_net**
> GetPayoutGrossForNetResponse get_payout_gross_for_net()

The gross price needed to clear a target net on one platform.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.payout.get_payout_gross_for_net_response import GetPayoutGrossForNetResponse
from crossly.model.common.error import Error
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

**GetPayoutGrossForNetResponse**

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

# **get_payout_identity**
> GetPayoutIdentityResponse get_payout_identity()

Stripe's verification of your payout account: status and what Stripe still needs, in plain words.

status is not_started, pending (Stripe is checking), action_required (dueNow lists what to add), verified (payouts on) or restricted (disabledReasonText says why). dueNow / dueLater / inReview are Stripe's requirement keys as plain-words lines ({ keys, label }); errors carry Stripe's reason. Cached up to 60 s; fresh=1 re-reads Stripe. Payouts are gated on payoutsEnabled only.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.common.error import Error
from crossly.model.payout.get_payout_identity_response import GetPayoutIdentityResponse
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
    fresh = "0" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stripe's verification of your payout account: status and what Stripe still needs, in plain words.
        api_response = api_instance.get_payout_identity(fresh=fresh)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PayoutApi->get_payout_identity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fresh** | **str**|  | [optional]

### Return type

**GetPayoutIdentityResponse**

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

# **get_payout_wallet**
> GetPayoutWalletResponse get_payout_wallet()

Your payout wallet: balances, schedule, next payout, instant-payout quote, methods, payouts, transactions.

connected:false (with defaultCountry) before onboarding. balance has availableCents, pendingCents and instantAvailableCents in the account currency. instant.available says whether an instant payout can be made now, with feeCents/netCents for the full instant-available amount and reason when not.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.payout.get_payout_wallet_response import GetPayoutWalletResponse
from crossly.model.common.error import Error
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
        # Your payout wallet: balances, schedule, next payout, instant-payout quote, methods, payouts, transactions.
        api_response = api_instance.get_payout_wallet()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PayoutApi->get_payout_wallet: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetPayoutWalletResponse**

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

# **list_payout_compare**
> ListPayoutCompareResponse list_payout_compare()

Rank platforms by what they net at a given price. Defaults to connected ones.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.payout.list_payout_compare_response import ListPayoutCompareResponse
from crossly.model.common.error import Error
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

**ListPayoutCompareResponse**

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

# **update_payout_schedule**
> UpdatePayoutScheduleResponse update_payout_schedule(update_payout_schedule_request)

Change the automatic payout schedule.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import payout_api
from crossly.model.payout.update_payout_schedule_response import UpdatePayoutScheduleResponse
from crossly.model.common.error import Error
from crossly.model.payout.update_payout_schedule_request import UpdatePayoutScheduleRequest
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
    update_payout_schedule_request = UpdatePayoutScheduleRequest(
        interval="manual",
        weekly_anchor="monday",
        monthly_anchor=1,
    ) # UpdatePayoutScheduleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Change the automatic payout schedule.
        api_response = api_instance.update_payout_schedule(update_payout_schedule_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PayoutApi->update_payout_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_payout_schedule_request** | **UpdatePayoutScheduleRequest**|  |

### Return type

**UpdatePayoutScheduleResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

