# crossly.AnalyticsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analytic_bookkeeping**](AnalyticsApi.md#get_analytic_bookkeeping) | **GET** /v1/analytics/bookkeeping | Monthly P&amp;L + per-platform breakdown for a calendar year.
[**get_analytic_by_platform**](AnalyticsApi.md#get_analytic_by_platform) | **GET** /v1/analytics/by-platform | Sales + revenue grouped by platform for the last N days.
[**get_analytic_dashboard**](AnalyticsApi.md#get_analytic_dashboard) | **GET** /v1/analytics/dashboard | Composite dashboard: KPIs + breakdowns + recent activity.
[**get_analytic_item**](AnalyticsApi.md#get_analytic_item) | **GET** /v1/analytics/items | Per-item P&amp;L for sold inventory.
[**get_analytic_summary**](AnalyticsApi.md#get_analytic_summary) | **GET** /v1/analytics/summary | Headline KPIs for the last N days.
[**get_analytic_timesery**](AnalyticsApi.md#get_analytic_timesery) | **GET** /v1/analytics/timeseries | Daily sales + revenue series for the last N days.
[**get_analytic_today**](AnalyticsApi.md#get_analytic_today) | **GET** /v1/analytics/today | Today&#39;s checklist + 14-day activity streak.
[**list_insight_by_platform**](AnalyticsApi.md#list_insight_by_platform) | **GET** /v1/insights/by-platform | Platform velocity + margin insight (90-day window).


# **get_analytic_bookkeeping**
> GetAnalyticBookkeepingResponse get_analytic_bookkeeping()

Monthly P&L + per-platform breakdown for a calendar year.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.error import Error
from crossly.model.get_analytic_bookkeeping_response import GetAnalyticBookkeepingResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Monthly P&L + per-platform breakdown for a calendar year.
        api_response = api_instance.get_analytic_bookkeeping()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_bookkeeping: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAnalyticBookkeepingResponse**](GetAnalyticBookkeepingResponse.md)

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

# **get_analytic_by_platform**
> GetAnalyticByPlatformResponse get_analytic_by_platform()

Sales + revenue grouped by platform for the last N days.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.get_analytic_by_platform_response import GetAnalyticByPlatformResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Sales + revenue grouped by platform for the last N days.
        api_response = api_instance.get_analytic_by_platform()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_by_platform: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAnalyticByPlatformResponse**](GetAnalyticByPlatformResponse.md)

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

# **get_analytic_dashboard**
> GetAnalyticDashboardResponse get_analytic_dashboard()

Composite dashboard: KPIs + breakdowns + recent activity.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.get_analytic_dashboard_response import GetAnalyticDashboardResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Composite dashboard: KPIs + breakdowns + recent activity.
        api_response = api_instance.get_analytic_dashboard()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_dashboard: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAnalyticDashboardResponse**](GetAnalyticDashboardResponse.md)

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

# **get_analytic_item**
> GetAnalyticItemResponse get_analytic_item()

Per-item P&L for sold inventory.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.error import Error
from crossly.model.get_analytic_item_response import GetAnalyticItemResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Per-item P&L for sold inventory.
        api_response = api_instance.get_analytic_item()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_item: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAnalyticItemResponse**](GetAnalyticItemResponse.md)

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

# **get_analytic_summary**
> GetAnalyticSummaryResponse get_analytic_summary()

Headline KPIs for the last N days.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.error import Error
from crossly.model.get_analytic_summary_response import GetAnalyticSummaryResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    days = 30 # int |  (optional) if omitted the server will use the default value of 30

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Headline KPIs for the last N days.
        api_response = api_instance.get_analytic_summary(days=days)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | [optional] if omitted the server will use the default value of 30

### Return type

[**GetAnalyticSummaryResponse**](GetAnalyticSummaryResponse.md)

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

# **get_analytic_timesery**
> GetAnalyticTimeseryResponse get_analytic_timesery()

Daily sales + revenue series for the last N days.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.error import Error
from crossly.model.get_analytic_timesery_response import GetAnalyticTimeseryResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Daily sales + revenue series for the last N days.
        api_response = api_instance.get_analytic_timesery()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_timesery: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAnalyticTimeseryResponse**](GetAnalyticTimeseryResponse.md)

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

# **get_analytic_today**
> GetAnalyticTodayResponse get_analytic_today()

Today's checklist + 14-day activity streak.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.error import Error
from crossly.model.get_analytic_today_response import GetAnalyticTodayResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Today's checklist + 14-day activity streak.
        api_response = api_instance.get_analytic_today()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_today: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAnalyticTodayResponse**](GetAnalyticTodayResponse.md)

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

# **list_insight_by_platform**
> bool, date, datetime, dict, float, int, list, str, none_type list_insight_by_platform()

Platform velocity + margin insight (90-day window).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.list_insight_by_platform_item import ListInsightByPlatformItem
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Platform velocity + margin insight (90-day window).
        api_response = api_instance.list_insight_by_platform()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->list_insight_by_platform: %s\n" % e)
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

