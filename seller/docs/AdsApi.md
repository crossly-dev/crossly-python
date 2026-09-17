# crossly.AdsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ad_offsite_campaign**](AdsApi.md#create_ad_offsite_campaign) | **POST** /v1/ads/offsite/campaigns | Launch an offsite campaign for an item.
[**create_ad_offsite_resume**](AdsApi.md#create_ad_offsite_resume) | **POST** /v1/ads/offsite/resume | Clear an auto-pause and resume offsite spend.
[**get_ad_offsite**](AdsApi.md#get_ad_offsite) | **GET** /v1/ads/offsite | Your offsite-ads opt-in and its terms.
[**get_ad_offsite_eligibility**](AdsApi.md#get_ad_offsite_eligibility) | **GET** /v1/ads/offsite/eligibility | Whether an item can run offsite, and why not.
[**get_ad_offsite_report**](AdsApi.md#get_ad_offsite_report) | **GET** /v1/ads/offsite/report | What your offsite budget bought — including the misses.
[**update_ad_offsite**](AdsApi.md#update_ad_offsite) | **PUT** /v1/ads/offsite | Turn offsite ads on or off. Yours alone to set.


# **create_ad_offsite_campaign**
> CreateAdOffsiteCampaignResponse create_ad_offsite_campaign()

Launch an offsite campaign for an item.

Creative is built from the structured fields you pass — title, condition as you recorded it, price, image. We generate no prose and invent no claims about condition or authenticity: an ad saying \"mint\" or \"authenticated\" when your listing says neither is a misrepresentation we authored and YOU would take the dispute for. Refuses with 403 when no ad network is wired, rather than returning a campaign that does not exist — a campaign row marked live with nothing behind it would read as spending your money when it is not.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ads_api
from crossly.model.error import Error
from crossly.model.create_ad_offsite_campaign_response import CreateAdOffsiteCampaignResponse
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
    api_instance = ads_api.AdsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Launch an offsite campaign for an item.
        api_response = api_instance.create_ad_offsite_campaign()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AdsApi->create_ad_offsite_campaign: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAdOffsiteCampaignResponse**](CreateAdOffsiteCampaignResponse.md)

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

# **create_ad_offsite_resume**
> CreateAdOffsiteResumeResponse create_ad_offsite_resume()

Clear an auto-pause and resume offsite spend.

Returns 409 when you are not actually paused. The pause reason is worth reading first — resuming without changing anything will usually just trip the floor again over the next window.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ads_api
from crossly.model.create_ad_offsite_resume_response import CreateAdOffsiteResumeResponse
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
    api_instance = ads_api.AdsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Clear an auto-pause and resume offsite spend.
        api_response = api_instance.create_ad_offsite_resume()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AdsApi->create_ad_offsite_resume: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAdOffsiteResumeResponse**](CreateAdOffsiteResumeResponse.md)

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

# **get_ad_offsite**
> GetAdOffsiteResponse get_ad_offsite()

Your offsite-ads opt-in and its terms.

Offsite ads spend your CBX advertising budget on external networks — Google, Meta and similar — at our discretion. Your item gets promoted, and the traffic lands on Crossly. OFF unless you turn it on, and there is no path that enables it on your behalf. Media is passed through AT COST with a separate, disclosed management fee, so you can always see how much of your budget reached the auction. `minReturnBps` is a STOP, not a guarantee: below it, offsite spend auto-pauses and the rest of your budget reverts to on-platform placement. Nobody can honestly promise ad performance; what we can promise is that it stops.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ads_api
from crossly.model.get_ad_offsite_response import GetAdOffsiteResponse
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
    api_instance = ads_api.AdsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your offsite-ads opt-in and its terms.
        api_response = api_instance.get_ad_offsite()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AdsApi->get_ad_offsite: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAdOffsiteResponse**](GetAdOffsiteResponse.md)

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

# **get_ad_offsite_eligibility**
> GetAdOffsiteEligibilityResponse get_ad_offsite_eligibility()

Whether an item can run offsite, and why not.

Reasons: `not_opted_in`, `auto_paused`, `network_not_allowed`, `category_not_allowlisted`, `no_adapter`, `no_budget`. The category check is an ALLOWLIST, so an unclassified category is not eligible. That is not bureaucracy: ad networks suspend the ACCOUNT over a prohibited item, and the account is one shared resource across every merchant using this — so one listing could take offsite ads away from all of them. A blocklist would fail open on the first category nobody thought of.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ads_api
from crossly.model.get_ad_offsite_eligibility_response import GetAdOffsiteEligibilityResponse
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
    api_instance = ads_api.AdsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Whether an item can run offsite, and why not.
        api_response = api_instance.get_ad_offsite_eligibility()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AdsApi->get_ad_offsite_eligibility: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAdOffsiteEligibilityResponse**](GetAdOffsiteEligibilityResponse.md)

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

# **get_ad_offsite_report**
> GetAdOffsiteReportResponse get_ad_offsite_report()

What your offsite budget bought — including the misses.

Spend, impressions and clicks are reported whether or not anything converted. A report showing only conversions is a report nobody can audit, and this is a feature where you handed over discretion over your money. `mediaCostCents` versus `managementFeeCents` answers \"how much of my budget reached the auction\" — the two are recorded separately so the answer survives. `spilloverConversions` is sales your ads produced on OTHER sellers' items. Reported so you can see whether offsite traffic is reaching buyers who want your item — a high spillover rate is the signal to turn it off. `returnBps` is attributed revenue as bps of spend; compare it with your `minReturnBps` floor.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ads_api
from crossly.model.get_ad_offsite_report_response import GetAdOffsiteReportResponse
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
    api_instance = ads_api.AdsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What your offsite budget bought — including the misses.
        api_response = api_instance.get_ad_offsite_report()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AdsApi->get_ad_offsite_report: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAdOffsiteReportResponse**](GetAdOffsiteReportResponse.md)

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

# **update_ad_offsite**
> UpdateAdOffsiteResponse update_ad_offsite()

Turn offsite ads on or off. Yours alone to set.

The toggle. Nothing else in the system sets `enabled` — no onboarding default, no bulk enable, no admin override. `maxOffsiteShareBps` caps how much of your budget may leave the platform, so opting in does not mean discovering the whole thing went to Google. `minReturnBps` sets the floor below which offsite spend auto-pauses: 20000 means we must return $2 of attributed revenue per $1 spent over the window. Toggling either way clears any existing auto-pause, so turning it back on later does not inherit a pause from months ago. When one of your ads brings a buyer who purchases somebody ELSE's item, that is reported to you as spillover so you can judge whether offsite traffic is reaching buyers who want YOUR item, and switch it off if not. It is not credited back — you bought clicks, which is how every ad market works.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ads_api
from crossly.model.update_ad_offsite_response import UpdateAdOffsiteResponse
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
    api_instance = ads_api.AdsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Turn offsite ads on or off. Yours alone to set.
        api_response = api_instance.update_ad_offsite()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AdsApi->update_ad_offsite: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UpdateAdOffsiteResponse**](UpdateAdOffsiteResponse.md)

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

