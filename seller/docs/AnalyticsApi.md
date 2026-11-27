# crossly.AnalyticsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_analytic_experiment**](AnalyticsApi.md#create_analytic_experiment) | **POST** /v1/analytics/experiments | Start a listing experiment. split: 2-4 live platform listings observed over the same window; sequential: one platform listing, before vs after changeAt (optionally applying a new price).
[**create_analytic_experiment_declare**](AnalyticsApi.md#create_analytic_experiment_declare) | **POST** /v1/analytics/experiments/{id}/declare | Record the outcome: a winning arm, no difference, or inconclusive. Concludes the experiment.
[**create_analytic_experiment_stop**](AnalyticsApi.md#create_analytic_experiment_stop) | **POST** /v1/analytics/experiments/{id}/stop | Stop an experiment: no more data is counted after now.
[**delete_analytic_experiment**](AnalyticsApi.md#delete_analytic_experiment) | **DELETE** /v1/analytics/experiments/{id} | Delete an experiment. The listings are untouched.
[**get_analytic_bookkeeping**](AnalyticsApi.md#get_analytic_bookkeeping) | **GET** /v1/analytics/bookkeeping | Monthly P&amp;L + per-platform breakdown for a calendar year.
[**get_analytic_by_platform**](AnalyticsApi.md#get_analytic_by_platform) | **GET** /v1/analytics/by-platform | Sales, net sales, fees and net profit by platform for the last N days.
[**get_analytic_compare**](AnalyticsApi.md#get_analytic_compare) | **GET** /v1/analytics/compare | Compare 2-4 of your listings: columns of price, quality, channels, views, favorites, offers and outcome, engagement curves, the fields that differ, and observational tests of favorite rate, view-to-offer rate and views per day.
[**get_analytic_dashboard**](AnalyticsApi.md#get_analytic_dashboard) | **GET** /v1/analytics/dashboard | Composite dashboard: KPIs + breakdowns + recent activity.
[**get_analytic_experiment**](AnalyticsApi.md#get_analytic_experiment) | **GET** /v1/analytics/experiments | Your listing A/B experiments, newest first, with status, days running and the current verdict.
[**get_analytic_experiment_by_id**](AnalyticsApi.md#get_analytic_experiment_by_id) | **GET** /v1/analytics/experiments/{id} | One experiment: arms with their windows, exposure and rates, the primary-metric test per arm against A, guardrail tests, the daily series and what to do next.
[**get_analytic_inventory**](AnalyticsApi.md#get_analytic_inventory) | **GET** /v1/analytics/inventory | Unsold stock: aging buckets with cost, listed value and market value, the 20 listings most in need of attention, shelf value over time, cohort sell-through at the chosen maturity, listed vs sold velocity and data health.
[**get_analytic_item**](AnalyticsApi.md#get_analytic_item) | **GET** /v1/analytics/items | Per-item P&amp;L for sold inventory.
[**get_analytic_item_by_listing_id**](AnalyticsApi.md#get_analytic_item_by_listing_id) | **GET** /v1/analytics/items/{listingId} | One listing in depth: channels with views, favorites and offers, the merged timeline, engagement series, price history, comps, money waterfall, days on market, offers, messages, experiments and suggestions.
[**get_analytic_marketplace**](AnalyticsApi.md#get_analytic_marketplace) | **GET** /v1/analytics/marketplaces | Every marketplace side by side: net sales and profit, units, ASP, take rate, margin, shipping subsidy, days to sell, sell-through, cancel and return rates, offers and engagement; with vs&#x3D;2-3 platforms, a head-to-head over listings live on all of them.
[**get_analytic_marketplace_by_platform**](AnalyticsApi.md#get_analytic_marketplace_by_platform) | **GET** /v1/analytics/marketplaces/{platform} | One marketplace in depth: its row, the money series, fee breakdown, days-to-sell and price-realization histograms, categories, top items, at-risk listings, a day-by-hour sales heatmap and offer stats.
[**get_analytic_overview**](AnalyticsApi.md#get_analytic_overview) | **GET** /v1/analytics/overview | KPIs with deltas (net sales, net profit, units, ASP, margin, sell-through, median days to sell, active listings, take rate), the trend series, by-marketplace split, top categories, brands and items, sell-through cohort, data health and insights.
[**get_analytic_performance**](AnalyticsApi.md#get_analytic_performance) | **GET** /v1/analytics/performance | Per-listing performance: channels, views, favorites, offers and conversations in the period, units sold, net sales and profit, margin, days to sell and a 0-100 health score, paged and sortable.
[**get_analytic_program**](AnalyticsApi.md#get_analytic_program) | **GET** /v1/analytics/programs/{program} | One program&#39;s report over a date range (default the last 30 days, at most 366): KPIs, a daily trend and a breakdown table. Money in integer cents.
[**get_analytic_segment**](AnalyticsApi.md#get_analytic_segment) | **GET** /v1/analytics/segments | Niches along one dimension: listed and active counts, units sold, cohort sell-through, median days to sell, net sales and profit, margin, ROI, ASP and discount from ask; rows under minN are flagged lowSample.
[**get_analytic_segment_by_key**](AnalyticsApi.md#get_analytic_segment_by_key) | **GET** /v1/analytics/segments/{dim}/{key} | One niche in depth: its row, series, by-marketplace split, days-to-sell histogram, price bands, top items and the 10 oldest unsold listings in it.
[**get_analytic_summary**](AnalyticsApi.md#get_analytic_summary) | **GET** /v1/analytics/summary | Headline KPIs for the last N days (the same numbers as the analytics overview).
[**get_analytic_timesery**](AnalyticsApi.md#get_analytic_timesery) | **GET** /v1/analytics/timeseries | Sales and net sales over the last N days, zero-filled, one row per calendar day.
[**get_analytic_today**](AnalyticsApi.md#get_analytic_today) | **GET** /v1/analytics/today | Today&#39;s checklist + 14-day activity streak.
[**list_insight_by_platform**](AnalyticsApi.md#list_insight_by_platform) | **GET** /v1/insights/by-platform | Platform velocity + margin insight (90-day window): units, net sales, median days to sell, ASP and net after the real marketplace fees.
[**update_analytic_experiment**](AnalyticsApi.md#update_analytic_experiment) | **PATCH** /v1/analytics/experiments/{id} | Rename an experiment or change its hypothesis, notes or planned end.


# **create_analytic_experiment**
> AnalyticExperimentResponse create_analytic_experiment()

Start a listing experiment. split: 2-4 live platform listings observed over the same window; sequential: one platform listing, before vs after changeAt (optionally applying a new price).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.common.analytic_experiment_response import AnalyticExperimentResponse
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
        # Start a listing experiment. split: 2-4 live platform listings observed over the same window; sequential: one platform listing, before vs after changeAt (optionally applying a new price).
        api_response = api_instance.create_analytic_experiment()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->create_analytic_experiment: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**AnalyticExperimentResponse**

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

# **create_analytic_experiment_declare**
> AnalyticExperimentResponse create_analytic_experiment_declare(id)

Record the outcome: a winning arm, no difference, or inconclusive. Concludes the experiment.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.common.analytic_experiment_response import AnalyticExperimentResponse
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
    id = "id_example" # str | The experiment id (a uuid; any other id is a 404).

    # example passing only required values which don't have defaults set
    try:
        # Record the outcome: a winning arm, no difference, or inconclusive. Concludes the experiment.
        api_response = api_instance.create_analytic_experiment_declare(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->create_analytic_experiment_declare: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The experiment id (a uuid; any other id is a 404). |

### Return type

**AnalyticExperimentResponse**

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

# **create_analytic_experiment_stop**
> AnalyticExperimentResponse create_analytic_experiment_stop(id)

Stop an experiment: no more data is counted after now.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.common.analytic_experiment_response import AnalyticExperimentResponse
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
    id = "id_example" # str | The experiment id (a uuid; any other id is a 404).

    # example passing only required values which don't have defaults set
    try:
        # Stop an experiment: no more data is counted after now.
        api_response = api_instance.create_analytic_experiment_stop(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->create_analytic_experiment_stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The experiment id (a uuid; any other id is a 404). |

### Return type

**AnalyticExperimentResponse**

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

# **delete_analytic_experiment**
> DeleteStoryResponse delete_analytic_experiment(id)

Delete an experiment. The listings are untouched.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.common.delete_story_response import DeleteStoryResponse
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
    id = "id_example" # str | The experiment id (a uuid; any other id is a 404).

    # example passing only required values which don't have defaults set
    try:
        # Delete an experiment. The listings are untouched.
        api_response = api_instance.delete_analytic_experiment(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->delete_analytic_experiment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The experiment id (a uuid; any other id is a 404). |

### Return type

**DeleteStoryResponse**

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

# **get_analytic_bookkeeping**
> GetAnalyticBookkeepingResponse get_analytic_bookkeeping()

Monthly P&L + per-platform breakdown for a calendar year.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.analytic.get_analytic_bookkeeping_response import GetAnalyticBookkeepingResponse
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

**GetAnalyticBookkeepingResponse**

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

# **get_analytic_by_platform**
> GetAnalyticByPlatformResponse get_analytic_by_platform()

Sales, net sales, fees and net profit by platform for the last N days.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.analytic.get_analytic_by_platform_response import GetAnalyticByPlatformResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    days = 30 # int | Calendar days back, today included. Larger values are clamped to 365. (optional) if omitted the server will use the default value of 30
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sales, net sales, fees and net profit by platform for the last N days.
        api_response = api_instance.get_analytic_by_platform(days=days, tz=tz)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_by_platform: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Calendar days back, today included. Larger values are clamped to 365. | [optional] if omitted the server will use the default value of 30
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. | [optional]

### Return type

**GetAnalyticByPlatformResponse**

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

# **get_analytic_compare**
> GetAnalyticCompareResponse get_analytic_compare(ids)

Compare 2-4 of your listings: columns of price, quality, channels, views, favorites, offers and outcome, engagement curves, the fields that differ, and observational tests of favorite rate, view-to-offer rate and views per day.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.analytic.get_analytic_compare_response import GetAnalyticCompareResponse
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
    ids = "ids_example" # str | Comma-separated listing ids, 2 to 4. The first is arm A.
    align = "age" # str | age = x is days since first listed (default); calendar = x is the date. (optional)
    platform = "platform_example" # str | Restrict engagement to one channel (platform id). (optional)
    tz = "tz_example" # str | IANA time zone. Default UTC. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Compare 2-4 of your listings: columns of price, quality, channels, views, favorites, offers and outcome, engagement curves, the fields that differ, and observational tests of favorite rate, view-to-offer rate and views per day.
        api_response = api_instance.get_analytic_compare(ids)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_compare: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Compare 2-4 of your listings: columns of price, quality, channels, views, favorites, offers and outcome, engagement curves, the fields that differ, and observational tests of favorite rate, view-to-offer rate and views per day.
        api_response = api_instance.get_analytic_compare(ids, align=align, platform=platform, tz=tz)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_compare: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Comma-separated listing ids, 2 to 4. The first is arm A. |
 **align** | **str**| age &#x3D; x is days since first listed (default); calendar &#x3D; x is the date. | [optional]
 **platform** | **str**| Restrict engagement to one channel (platform id). | [optional]
 **tz** | **str**| IANA time zone. Default UTC. | [optional]

### Return type

**GetAnalyticCompareResponse**

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

# **get_analytic_dashboard**
> GetAnalyticDashboardResponse get_analytic_dashboard()

Composite dashboard: KPIs + breakdowns + recent activity.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.analytic.get_analytic_dashboard_response import GetAnalyticDashboardResponse
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

**GetAnalyticDashboardResponse**

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

# **get_analytic_experiment**
> GetAnalyticExperimentResponse get_analytic_experiment()

Your listing A/B experiments, newest first, with status, days running and the current verdict.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.analytic.get_analytic_experiment_response import GetAnalyticExperimentResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    status = "all" # str | Default all. (optional)
    page = 1 # int | 1-indexed page. Default 1. (optional)
    size = 1 # int | Rows per page. Default 20. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Your listing A/B experiments, newest first, with status, days running and the current verdict.
        api_response = api_instance.get_analytic_experiment(status=status, page=page, size=size)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_experiment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Default all. | [optional]
 **page** | **int**| 1-indexed page. Default 1. | [optional]
 **size** | **int**| Rows per page. Default 20. | [optional]

### Return type

**GetAnalyticExperimentResponse**

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

# **get_analytic_experiment_by_id**
> GetAnalyticExperimentByIdResponse get_analytic_experiment_by_id(id)

One experiment: arms with their windows, exposure and rates, the primary-metric test per arm against A, guardrail tests, the daily series and what to do next.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.analytic.get_analytic_experiment_by_id_response import GetAnalyticExperimentByIdResponse
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
    id = "id_example" # str | The experiment id (a uuid).

    # example passing only required values which don't have defaults set
    try:
        # One experiment: arms with their windows, exposure and rates, the primary-metric test per arm against A, guardrail tests, the daily series and what to do next.
        api_response = api_instance.get_analytic_experiment_by_id(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_experiment_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The experiment id (a uuid). |

### Return type

**GetAnalyticExperimentByIdResponse**

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

# **get_analytic_inventory**
> GetAnalyticInventoryResponse get_analytic_inventory()

Unsold stock: aging buckets with cost, listed value and market value, the 20 listings most in need of attention, shelf value over time, cohort sell-through at the chosen maturity, listed vs sold velocity and data health.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.analytic.get_analytic_inventory_response import GetAnalyticInventoryResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    range = "7d" # str | Reporting window. Default 30d. custom needs from and to. (optional)
    _from = "from_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    to = "to_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    compare = "prev" # str | Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). (optional)
    cmp_from = "cmpFrom_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    cmp_to = "cmpTo_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    labels = "labels_example" # str | Comma-separated inventory labels (any of them). (optional)
    platforms = "platforms_example" # str | Comma-separated platform ids. (optional)
    category = "category_example" # str | Canonical main-category key. (optional)
    brand = "brand_example" # str | Brand name. (optional)
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. An invalid name is a 400. (optional)
    maturity = 30 # int | Days an item has to sell within to count as sold in the cohort. Default 30. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unsold stock: aging buckets with cost, listed value and market value, the 20 listings most in need of attention, shelf value over time, cohort sell-through at the chosen maturity, listed vs sold velocity and data health.
        api_response = api_instance.get_analytic_inventory(range=range, _from=_from, to=to, compare=compare, cmp_from=cmp_from, cmp_to=cmp_to, labels=labels, platforms=platforms, category=category, brand=brand, tz=tz, maturity=maturity)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_inventory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**| Reporting window. Default 30d. custom needs from and to. | [optional]
 **_from** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **to** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **compare** | **str**| Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). | [optional]
 **cmp_from** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **cmp_to** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **labels** | **str**| Comma-separated inventory labels (any of them). | [optional]
 **platforms** | **str**| Comma-separated platform ids. | [optional]
 **category** | **str**| Canonical main-category key. | [optional]
 **brand** | **str**| Brand name. | [optional]
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. An invalid name is a 400. | [optional]
 **maturity** | **int**| Days an item has to sell within to count as sold in the cohort. Default 30. | [optional]

### Return type

**GetAnalyticInventoryResponse**

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

# **get_analytic_item**
> GetAnalyticItemResponse get_analytic_item()

Per-item P&L for sold inventory.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.analytic.get_analytic_item_response import GetAnalyticItemResponse
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

**GetAnalyticItemResponse**

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

# **get_analytic_item_by_listing_id**
> GetAnalyticItemByListingIdResponse get_analytic_item_by_listing_id(listing_id)

One listing in depth: channels with views, favorites and offers, the merged timeline, engagement series, price history, comps, money waterfall, days on market, offers, messages, experiments and suggestions.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.analytic.get_analytic_item_by_listing_id_response import GetAnalyticItemByListingIdResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    listing_id = "listingId_example" # str | A listings.id you own (or an inventory item id with by=inventory).
    by = "listing" # str | inventory = the id is an inventory item id; the answer is { redirectListingId }. Default listing. (optional)
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. (optional)

    # example passing only required values which don't have defaults set
    try:
        # One listing in depth: channels with views, favorites and offers, the merged timeline, engagement series, price history, comps, money waterfall, days on market, offers, messages, experiments and suggestions.
        api_response = api_instance.get_analytic_item_by_listing_id(listing_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_item_by_listing_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # One listing in depth: channels with views, favorites and offers, the merged timeline, engagement series, price history, comps, money waterfall, days on market, offers, messages, experiments and suggestions.
        api_response = api_instance.get_analytic_item_by_listing_id(listing_id, by=by, tz=tz)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_item_by_listing_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **str**| A listings.id you own (or an inventory item id with by&#x3D;inventory). |
 **by** | **str**| inventory &#x3D; the id is an inventory item id; the answer is { redirectListingId }. Default listing. | [optional]
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. | [optional]

### Return type

**GetAnalyticItemByListingIdResponse**

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

# **get_analytic_marketplace**
> GetAnalyticMarketplaceResponse get_analytic_marketplace()

Every marketplace side by side: net sales and profit, units, ASP, take rate, margin, shipping subsidy, days to sell, sell-through, cancel and return rates, offers and engagement; with vs=2-3 platforms, a head-to-head over listings live on all of them.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.analytic.get_analytic_marketplace_response import GetAnalyticMarketplaceResponse
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
    range = "7d" # str | Reporting window. Default 30d. custom needs from and to. (optional)
    _from = "from_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    to = "to_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    compare = "prev" # str | Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). (optional)
    cmp_from = "cmpFrom_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    cmp_to = "cmpTo_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    labels = "labels_example" # str | Comma-separated inventory labels (any of them). (optional)
    platforms = "platforms_example" # str | Comma-separated platform ids. (optional)
    category = "category_example" # str | Canonical main-category key. (optional)
    brand = "brand_example" # str | Brand name. (optional)
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. An invalid name is a 400. (optional)
    vs = "vs_example" # str | Comma-separated 2-3 platform ids for the head-to-head. (optional)
    sort = "netSales" # str | Default netSales. (optional)
    dir = "asc" # str | Default desc. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Every marketplace side by side: net sales and profit, units, ASP, take rate, margin, shipping subsidy, days to sell, sell-through, cancel and return rates, offers and engagement; with vs=2-3 platforms, a head-to-head over listings live on all of them.
        api_response = api_instance.get_analytic_marketplace(range=range, _from=_from, to=to, compare=compare, cmp_from=cmp_from, cmp_to=cmp_to, labels=labels, platforms=platforms, category=category, brand=brand, tz=tz, vs=vs, sort=sort, dir=dir)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_marketplace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**| Reporting window. Default 30d. custom needs from and to. | [optional]
 **_from** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **to** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **compare** | **str**| Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). | [optional]
 **cmp_from** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **cmp_to** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **labels** | **str**| Comma-separated inventory labels (any of them). | [optional]
 **platforms** | **str**| Comma-separated platform ids. | [optional]
 **category** | **str**| Canonical main-category key. | [optional]
 **brand** | **str**| Brand name. | [optional]
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. An invalid name is a 400. | [optional]
 **vs** | **str**| Comma-separated 2-3 platform ids for the head-to-head. | [optional]
 **sort** | **str**| Default netSales. | [optional]
 **dir** | **str**| Default desc. | [optional]

### Return type

**GetAnalyticMarketplaceResponse**

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

# **get_analytic_marketplace_by_platform**
> GetAnalyticMarketplaceByPlatformResponse get_analytic_marketplace_by_platform(platform)

One marketplace in depth: its row, the money series, fee breakdown, days-to-sell and price-realization histograms, categories, top items, at-risk listings, a day-by-hour sales heatmap and offer stats.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.analytic.get_analytic_marketplace_by_platform_response import GetAnalyticMarketplaceByPlatformResponse
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
    platform = "platform_example" # str | A platform id, e.g. ebay, poshmark.
    range = "7d" # str | Reporting window. Default 30d. custom needs from and to. (optional)
    _from = "from_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    to = "to_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    compare = "prev" # str | Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). (optional)
    cmp_from = "cmpFrom_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    cmp_to = "cmpTo_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    labels = "labels_example" # str | Comma-separated inventory labels (any of them). (optional)
    platforms = "platforms_example" # str | Comma-separated platform ids. (optional)
    category = "category_example" # str | Canonical main-category key. (optional)
    brand = "brand_example" # str | Brand name. (optional)
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. An invalid name is a 400. (optional)

    # example passing only required values which don't have defaults set
    try:
        # One marketplace in depth: its row, the money series, fee breakdown, days-to-sell and price-realization histograms, categories, top items, at-risk listings, a day-by-hour sales heatmap and offer stats.
        api_response = api_instance.get_analytic_marketplace_by_platform(platform)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_marketplace_by_platform: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # One marketplace in depth: its row, the money series, fee breakdown, days-to-sell and price-realization histograms, categories, top items, at-risk listings, a day-by-hour sales heatmap and offer stats.
        api_response = api_instance.get_analytic_marketplace_by_platform(platform, range=range, _from=_from, to=to, compare=compare, cmp_from=cmp_from, cmp_to=cmp_to, labels=labels, platforms=platforms, category=category, brand=brand, tz=tz)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_marketplace_by_platform: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| A platform id, e.g. ebay, poshmark. |
 **range** | **str**| Reporting window. Default 30d. custom needs from and to. | [optional]
 **_from** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **to** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **compare** | **str**| Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). | [optional]
 **cmp_from** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **cmp_to** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **labels** | **str**| Comma-separated inventory labels (any of them). | [optional]
 **platforms** | **str**| Comma-separated platform ids. | [optional]
 **category** | **str**| Canonical main-category key. | [optional]
 **brand** | **str**| Brand name. | [optional]
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. An invalid name is a 400. | [optional]

### Return type

**GetAnalyticMarketplaceByPlatformResponse**

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

# **get_analytic_overview**
> GetAnalyticOverviewResponse get_analytic_overview()

KPIs with deltas (net sales, net profit, units, ASP, margin, sell-through, median days to sell, active listings, take rate), the trend series, by-marketplace split, top categories, brands and items, sell-through cohort, data health and insights.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.analytic.get_analytic_overview_response import GetAnalyticOverviewResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    range = "7d" # str | Reporting window. Default 30d. custom needs from and to. (optional)
    _from = "from_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    to = "to_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    compare = "prev" # str | Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). (optional)
    cmp_from = "cmpFrom_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    cmp_to = "cmpTo_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    labels = "labels_example" # str | Comma-separated inventory labels (any of them). (optional)
    platforms = "platforms_example" # str | Comma-separated platform ids. (optional)
    category = "category_example" # str | Canonical main-category key. (optional)
    brand = "brand_example" # str | Brand name. (optional)
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. An invalid name is a 400. (optional)
    stores = "stores_example" # str | Comma-separated store ids. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # KPIs with deltas (net sales, net profit, units, ASP, margin, sell-through, median days to sell, active listings, take rate), the trend series, by-marketplace split, top categories, brands and items, sell-through cohort, data health and insights.
        api_response = api_instance.get_analytic_overview(range=range, _from=_from, to=to, compare=compare, cmp_from=cmp_from, cmp_to=cmp_to, labels=labels, platforms=platforms, category=category, brand=brand, tz=tz, stores=stores)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_overview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**| Reporting window. Default 30d. custom needs from and to. | [optional]
 **_from** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **to** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **compare** | **str**| Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). | [optional]
 **cmp_from** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **cmp_to** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **labels** | **str**| Comma-separated inventory labels (any of them). | [optional]
 **platforms** | **str**| Comma-separated platform ids. | [optional]
 **category** | **str**| Canonical main-category key. | [optional]
 **brand** | **str**| Brand name. | [optional]
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. An invalid name is a 400. | [optional]
 **stores** | **str**| Comma-separated store ids. | [optional]

### Return type

**GetAnalyticOverviewResponse**

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

# **get_analytic_performance**
> GetAnalyticPerformanceResponse get_analytic_performance()

Per-listing performance: channels, views, favorites, offers and conversations in the period, units sold, net sales and profit, margin, days to sell and a 0-100 health score, paged and sortable.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.analytic.get_analytic_performance_response import GetAnalyticPerformanceResponse
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
    range = "7d" # str | Reporting window. Default 30d. custom needs from and to. (optional)
    _from = "from_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    to = "to_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    compare = "prev" # str | Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). (optional)
    cmp_from = "cmpFrom_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    cmp_to = "cmpTo_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    labels = "labels_example" # str | Comma-separated inventory labels (any of them). (optional)
    platforms = "platforms_example" # str | Comma-separated platform ids. (optional)
    category = "category_example" # str | Canonical main-category key. (optional)
    brand = "brand_example" # str | Brand name. (optional)
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. An invalid name is a 400. (optional)
    status = "all" # str | unsold = listed at least minDays with no completed sale. (optional)
    q = "q_example" # str | Title, SKU or brand contains. (optional)
    sort = "lastActivity" # str | Default lastActivity. (optional)
    dir = "asc" # str | Default desc. (optional)
    page = 1 # int | 1-indexed page. Default 1. (optional)
    size = 25 # int | Rows per page. Default 50. (optional)
    min_days = 0 # int | Minimum days listed (for status=unsold). Default 0. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Per-listing performance: channels, views, favorites, offers and conversations in the period, units sold, net sales and profit, margin, days to sell and a 0-100 health score, paged and sortable.
        api_response = api_instance.get_analytic_performance(range=range, _from=_from, to=to, compare=compare, cmp_from=cmp_from, cmp_to=cmp_to, labels=labels, platforms=platforms, category=category, brand=brand, tz=tz, status=status, q=q, sort=sort, dir=dir, page=page, size=size, min_days=min_days)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_performance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**| Reporting window. Default 30d. custom needs from and to. | [optional]
 **_from** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **to** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **compare** | **str**| Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). | [optional]
 **cmp_from** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **cmp_to** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **labels** | **str**| Comma-separated inventory labels (any of them). | [optional]
 **platforms** | **str**| Comma-separated platform ids. | [optional]
 **category** | **str**| Canonical main-category key. | [optional]
 **brand** | **str**| Brand name. | [optional]
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. An invalid name is a 400. | [optional]
 **status** | **str**| unsold &#x3D; listed at least minDays with no completed sale. | [optional]
 **q** | **str**| Title, SKU or brand contains. | [optional]
 **sort** | **str**| Default lastActivity. | [optional]
 **dir** | **str**| Default desc. | [optional]
 **page** | **int**| 1-indexed page. Default 1. | [optional]
 **size** | **int**| Rows per page. Default 50. | [optional]
 **min_days** | **int**| Minimum days listed (for status&#x3D;unsold). Default 0. | [optional]

### Return type

**GetAnalyticPerformanceResponse**

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

# **get_analytic_program**
> GetAnalyticProgramResponse get_analytic_program(program)

One program's report over a date range (default the last 30 days, at most 366): KPIs, a daily trend and a breakdown table. Money in integer cents.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.analytic.get_analytic_program_response import GetAnalyticProgramResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    program = "wholesale" # str | 
    _from = dateutil_parser('1970-01-01').date() # date | First UTC day (YYYY-MM-DD), inclusive. (optional)
    to = dateutil_parser('1970-01-01').date() # date | Last UTC day (YYYY-MM-DD), inclusive. Default today. (optional)
    by = "by_example" # str | Breakdown dimension, when the program offers one (worlds: showroom, property, event). (optional)

    # example passing only required values which don't have defaults set
    try:
        # One program's report over a date range (default the last 30 days, at most 366): KPIs, a daily trend and a breakdown table. Money in integer cents.
        api_response = api_instance.get_analytic_program(program)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_program: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # One program's report over a date range (default the last 30 days, at most 366): KPIs, a daily trend and a breakdown table. Money in integer cents.
        api_response = api_instance.get_analytic_program(program, _from=_from, to=to, by=by)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_program: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program** | **str**|  |
 **_from** | **date**| First UTC day (YYYY-MM-DD), inclusive. | [optional]
 **to** | **date**| Last UTC day (YYYY-MM-DD), inclusive. Default today. | [optional]
 **by** | **str**| Breakdown dimension, when the program offers one (worlds: showroom, property, event). | [optional]

### Return type

**GetAnalyticProgramResponse**

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

# **get_analytic_segment**
> GetAnalyticSegmentResponse get_analytic_segment()

Niches along one dimension: listed and active counts, units sold, cohort sell-through, median days to sell, net sales and profit, margin, ROI, ASP and discount from ask; rows under minN are flagged lowSample.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.analytic.get_analytic_segment_response import GetAnalyticSegmentResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    range = "7d" # str | Reporting window. Default 30d. custom needs from and to. (optional)
    _from = "from_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    to = "to_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    compare = "prev" # str | Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). (optional)
    cmp_from = "cmpFrom_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    cmp_to = "cmpTo_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    labels = "labels_example" # str | Comma-separated inventory labels (any of them). (optional)
    platforms = "platforms_example" # str | Comma-separated platform ids. (optional)
    category = "category_example" # str | Canonical main-category key. (optional)
    brand = "brand_example" # str | Brand name. (optional)
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. An invalid name is a 400. (optional)
    dim = "category" # str | category = main category; subcategory = main > sub; brand; condition; size; source = where you acquired it; department; priceBand = ask in <$10, $10-25, $25-50, $50-100, $100-250, $250+; ageBand = days live at sale or now (<7, 7-30, 30-90, 90+). (optional)
    sort = "label" # str | Default netSales. (optional)
    dir = "asc" # str | Default desc. (optional)
    min_n = 1 # int | Minimum sample for a row to count as a winner or loser. Default 3. (optional)
    q = "q_example" # str | Segment label contains. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Niches along one dimension: listed and active counts, units sold, cohort sell-through, median days to sell, net sales and profit, margin, ROI, ASP and discount from ask; rows under minN are flagged lowSample.
        api_response = api_instance.get_analytic_segment(range=range, _from=_from, to=to, compare=compare, cmp_from=cmp_from, cmp_to=cmp_to, labels=labels, platforms=platforms, category=category, brand=brand, tz=tz, dim=dim, sort=sort, dir=dir, min_n=min_n, q=q)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**| Reporting window. Default 30d. custom needs from and to. | [optional]
 **_from** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **to** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **compare** | **str**| Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). | [optional]
 **cmp_from** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **cmp_to** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **labels** | **str**| Comma-separated inventory labels (any of them). | [optional]
 **platforms** | **str**| Comma-separated platform ids. | [optional]
 **category** | **str**| Canonical main-category key. | [optional]
 **brand** | **str**| Brand name. | [optional]
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. An invalid name is a 400. | [optional]
 **dim** | **str**| category &#x3D; main category; subcategory &#x3D; main &gt; sub; brand; condition; size; source &#x3D; where you acquired it; department; priceBand &#x3D; ask in &lt;$10, $10-25, $25-50, $50-100, $100-250, $250+; ageBand &#x3D; days live at sale or now (&lt;7, 7-30, 30-90, 90+). | [optional]
 **sort** | **str**| Default netSales. | [optional]
 **dir** | **str**| Default desc. | [optional]
 **min_n** | **int**| Minimum sample for a row to count as a winner or loser. Default 3. | [optional]
 **q** | **str**| Segment label contains. | [optional]

### Return type

**GetAnalyticSegmentResponse**

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

# **get_analytic_segment_by_key**
> GetAnalyticSegmentByKeyResponse get_analytic_segment_by_key(dim, key)

One niche in depth: its row, series, by-marketplace split, days-to-sell histogram, price bands, top items and the 10 oldest unsold listings in it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.analytic.get_analytic_segment_by_key_response import GetAnalyticSegmentByKeyResponse
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    dim = "dim_example" # str | One of category, subcategory, brand, condition, size, source, department, priceBand, ageBand. category = main category; subcategory = main > sub; brand; condition; size; source = where you acquired it; department; priceBand = ask in <$10, $10-25, $25-50, $50-100, $100-250, $250+; ageBand = days live at sale or now (<7, 7-30, 30-90, 90+).
    key = "key_example" # str | The segment key from a segments row (URL-encoded). A key with no data in scope is a 404.
    range = "7d" # str | Reporting window. Default 30d. custom needs from and to. (optional)
    _from = "from_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    to = "to_example" # str | YYYY-MM-DD, inclusive, in tz. Only with range=custom. (optional)
    compare = "prev" # str | Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). (optional)
    cmp_from = "cmpFrom_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    cmp_to = "cmpTo_example" # str | YYYY-MM-DD. Only with compare=custom. (optional)
    labels = "labels_example" # str | Comma-separated inventory labels (any of them). (optional)
    platforms = "platforms_example" # str | Comma-separated platform ids. (optional)
    category = "category_example" # str | Canonical main-category key. (optional)
    brand = "brand_example" # str | Brand name. (optional)
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. An invalid name is a 400. (optional)

    # example passing only required values which don't have defaults set
    try:
        # One niche in depth: its row, series, by-marketplace split, days-to-sell histogram, price bands, top items and the 10 oldest unsold listings in it.
        api_response = api_instance.get_analytic_segment_by_key(dim, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_segment_by_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # One niche in depth: its row, series, by-marketplace split, days-to-sell histogram, price bands, top items and the 10 oldest unsold listings in it.
        api_response = api_instance.get_analytic_segment_by_key(dim, key, range=range, _from=_from, to=to, compare=compare, cmp_from=cmp_from, cmp_to=cmp_to, labels=labels, platforms=platforms, category=category, brand=brand, tz=tz)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_segment_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dim** | **str**| One of category, subcategory, brand, condition, size, source, department, priceBand, ageBand. category &#x3D; main category; subcategory &#x3D; main &gt; sub; brand; condition; size; source &#x3D; where you acquired it; department; priceBand &#x3D; ask in &lt;$10, $10-25, $25-50, $50-100, $100-250, $250+; ageBand &#x3D; days live at sale or now (&lt;7, 7-30, 30-90, 90+). |
 **key** | **str**| The segment key from a segments row (URL-encoded). A key with no data in scope is a 404. |
 **range** | **str**| Reporting window. Default 30d. custom needs from and to. | [optional]
 **_from** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **to** | **str**| YYYY-MM-DD, inclusive, in tz. Only with range&#x3D;custom. | [optional]
 **compare** | **str**| Comparison window for deltas: prev (same length just before), yoy, none, custom (cmpFrom/cmpTo). | [optional]
 **cmp_from** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **cmp_to** | **str**| YYYY-MM-DD. Only with compare&#x3D;custom. | [optional]
 **labels** | **str**| Comma-separated inventory labels (any of them). | [optional]
 **platforms** | **str**| Comma-separated platform ids. | [optional]
 **category** | **str**| Canonical main-category key. | [optional]
 **brand** | **str**| Brand name. | [optional]
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. An invalid name is a 400. | [optional]

### Return type

**GetAnalyticSegmentByKeyResponse**

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

# **get_analytic_summary**
> GetAnalyticSummaryResponse get_analytic_summary()

Headline KPIs for the last N days (the same numbers as the analytics overview).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.analytic.get_analytic_summary_response import GetAnalyticSummaryResponse
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
    days = 30 # int | Calendar days back, today included. Larger values are clamped to 365. (optional) if omitted the server will use the default value of 30
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Headline KPIs for the last N days (the same numbers as the analytics overview).
        api_response = api_instance.get_analytic_summary(days=days, tz=tz)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Calendar days back, today included. Larger values are clamped to 365. | [optional] if omitted the server will use the default value of 30
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. | [optional]

### Return type

**GetAnalyticSummaryResponse**

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

# **get_analytic_timesery**
> GetAnalyticTimeseryResponse get_analytic_timesery()

Sales and net sales over the last N days, zero-filled, one row per calendar day.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.analytic.get_analytic_timesery_response import GetAnalyticTimeseryResponse
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
    days = 30 # int | Calendar days back, today included. Larger values are clamped to 365. (optional) if omitted the server will use the default value of 30
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sales and net sales over the last N days, zero-filled, one row per calendar day.
        api_response = api_instance.get_analytic_timesery(days=days, tz=tz)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytic_timesery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Calendar days back, today included. Larger values are clamped to 365. | [optional] if omitted the server will use the default value of 30
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. | [optional]

### Return type

**GetAnalyticTimeseryResponse**

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

# **get_analytic_today**
> GetAnalyticTodayResponse get_analytic_today()

Today's checklist + 14-day activity streak.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.analytic.get_analytic_today_response import GetAnalyticTodayResponse
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

**GetAnalyticTodayResponse**

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

# **list_insight_by_platform**
> ListInsightByPlatformResponse list_insight_by_platform()

Platform velocity + margin insight (90-day window): units, net sales, median days to sell, ASP and net after the real marketplace fees.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.common.list_insight_by_platform_response import ListInsightByPlatformResponse
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
    tz = "tz_example" # str | IANA time zone for day boundaries. Default UTC. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Platform velocity + margin insight (90-day window): units, net sales, median days to sell, ASP and net after the real marketplace fees.
        api_response = api_instance.list_insight_by_platform(tz=tz)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->list_insight_by_platform: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tz** | **str**| IANA time zone for day boundaries. Default UTC. | [optional]

### Return type

**ListInsightByPlatformResponse**

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

# **update_analytic_experiment**
> AnalyticExperimentResponse update_analytic_experiment(id)

Rename an experiment or change its hypothesis, notes or planned end.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import analytics_api
from crossly.model.common.error import Error
from crossly.model.common.analytic_experiment_response import AnalyticExperimentResponse
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
    id = "id_example" # str | The experiment id (a uuid; any other id is a 404).

    # example passing only required values which don't have defaults set
    try:
        # Rename an experiment or change its hypothesis, notes or planned end.
        api_response = api_instance.update_analytic_experiment(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AnalyticsApi->update_analytic_experiment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The experiment id (a uuid; any other id is a 404). |

### Return type

**AnalyticExperimentResponse**

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

