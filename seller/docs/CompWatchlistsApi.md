# crossly.CompWatchlistsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comp_watchlist**](CompWatchlistsApi.md#create_comp_watchlist) | **POST** /v1/comp-watchlists | Create a sold-comp watchlist.
[**create_comp_watchlist_scrape**](CompWatchlistsApi.md#create_comp_watchlist_scrape) | **POST** /v1/comp-watchlists/{id}/scrape | Manually trigger a watchlist scrape.
[**delete_comp_watchlist**](CompWatchlistsApi.md#delete_comp_watchlist) | **DELETE** /v1/comp-watchlists/{id} | Delete a sold-comp watchlist.
[**list_comp_watchlist_recent**](CompWatchlistsApi.md#list_comp_watchlist_recent) | **GET** /v1/comp-watchlists/{id}/recent | Recent external sold comps matching this watchlist.
[**list_comp_watchlists**](CompWatchlistsApi.md#list_comp_watchlists) | **GET** /v1/comp-watchlists | List the seller&#39;s sold-comp watchlists.


# **create_comp_watchlist**
> ListCompWatchlistsItem create_comp_watchlist()

Create a sold-comp watchlist.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import comp_watchlists_api
from crossly.model.common.error import Error
from crossly.model.common.list_comp_watchlists_item import ListCompWatchlistsItem
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
    api_instance = comp_watchlists_api.CompWatchlistsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a sold-comp watchlist.
        api_response = api_instance.create_comp_watchlist()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CompWatchlistsApi->create_comp_watchlist: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCompWatchlistsItem**

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

# **create_comp_watchlist_scrape**
> CreateCompWatchlistScrapeResponse create_comp_watchlist_scrape(id)

Manually trigger a watchlist scrape.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import comp_watchlists_api
from crossly.model.common.create_comp_watchlist_scrape_response import CreateCompWatchlistScrapeResponse
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
    api_instance = comp_watchlists_api.CompWatchlistsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Manually trigger a watchlist scrape.
        api_response = api_instance.create_comp_watchlist_scrape(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CompWatchlistsApi->create_comp_watchlist_scrape: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateCompWatchlistScrapeResponse**

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

# **delete_comp_watchlist**
> OkResponse delete_comp_watchlist(id)

Delete a sold-comp watchlist.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import comp_watchlists_api
from crossly.model.common.ok_response import OkResponse
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
    api_instance = comp_watchlists_api.CompWatchlistsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a sold-comp watchlist.
        api_response = api_instance.delete_comp_watchlist(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CompWatchlistsApi->delete_comp_watchlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**OkResponse**

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

# **list_comp_watchlist_recent**
> ListCompWatchlistRecentResponse list_comp_watchlist_recent(id)

Recent external sold comps matching this watchlist.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import comp_watchlists_api
from crossly.model.common.list_comp_watchlist_recent_response import ListCompWatchlistRecentResponse
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
    api_instance = comp_watchlists_api.CompWatchlistsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Recent external sold comps matching this watchlist.
        api_response = api_instance.list_comp_watchlist_recent(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CompWatchlistsApi->list_comp_watchlist_recent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListCompWatchlistRecentResponse**

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

# **list_comp_watchlists**
> ListCompWatchlistsResponse list_comp_watchlists()

List the seller's sold-comp watchlists.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import comp_watchlists_api
from crossly.model.common.error import Error
from crossly.model.common.list_comp_watchlists_response import ListCompWatchlistsResponse
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
    api_instance = comp_watchlists_api.CompWatchlistsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the seller's sold-comp watchlists.
        api_response = api_instance.list_comp_watchlists()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CompWatchlistsApi->list_comp_watchlists: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCompWatchlistsResponse**

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

