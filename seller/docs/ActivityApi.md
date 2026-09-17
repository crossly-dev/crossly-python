# crossly.ActivityApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_log**](ActivityApi.md#get_action_log) | **GET** /v1/action-log/{id} | Get one action-log event by id (ownership-checked).
[**get_action_log_facet**](ActivityApi.md#get_action_log_facet) | **GET** /v1/action-log/facets | Distinct platforms / actions / categories present in the caller&#39;s action log (last 90 days) — powers filter dropdowns before you query.
[**list_action_log**](ActivityApi.md#list_action_log) | **GET** /v1/action-log | List action-log events — the semantic \&quot;what happened\&quot; record of every user + platform action. Filter by platform / action / category / status / source / target, and a since/until created_at window.
[**list_action_log_calls**](ActivityApi.md#list_action_log_calls) | **GET** /v1/action-log/{id}/calls | The outbound platform HTTP calls under an event (oldest first) — url, method, status, latency, redacted request/response bodies, proxy + recipe/hash. Answers \&quot;what was sent / what went wrong\&quot;.


# **get_action_log**
> GetActionLogResponse get_action_log(id)

Get one action-log event by id (ownership-checked).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.error import Error
from crossly.model.get_action_log_response import GetActionLogResponse
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
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get one action-log event by id (ownership-checked).
        api_response = api_instance.get_action_log(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->get_action_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**GetActionLogResponse**](GetActionLogResponse.md)

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

# **get_action_log_facet**
> GetActionLogFacetResponse get_action_log_facet()

Distinct platforms / actions / categories present in the caller's action log (last 90 days) — powers filter dropdowns before you query.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.error import Error
from crossly.model.get_action_log_facet_response import GetActionLogFacetResponse
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
    api_instance = activity_api.ActivityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Distinct platforms / actions / categories present in the caller's action log (last 90 days) — powers filter dropdowns before you query.
        api_response = api_instance.get_action_log_facet()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->get_action_log_facet: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetActionLogFacetResponse**](GetActionLogFacetResponse.md)

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

# **list_action_log**
> bool, date, datetime, dict, float, int, list, str, none_type list_action_log()

List action-log events — the semantic \"what happened\" record of every user + platform action. Filter by platform / action / category / status / source / target, and a since/until created_at window.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.list_action_log_item import ListActionLogItem
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
    api_instance = activity_api.ActivityApi(api_client)
    platform = "platform_example" # str |  (optional)
    action = "action_example" # str |  (optional)
    category = "category_example" # str |  (optional)
    status = "status_example" # str |  (optional)
    source = "source_example" # str |  (optional)
    target_type = "targetType_example" # str |  (optional)
    target_id = "targetId_example" # str |  (optional)
    since = "since_example" # str | ISO lower bound (inclusive) on created_at. (optional)
    until = "until_example" # str | ISO upper bound (exclusive) on created_at. (optional)
    limit = 50 # int |  (optional) if omitted the server will use the default value of 50
    offset = 0 # int |  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List action-log events — the semantic \"what happened\" record of every user + platform action. Filter by platform / action / category / status / source / target, and a since/until created_at window.
        api_response = api_instance.list_action_log(platform=platform, action=action, category=category, status=status, source=source, target_type=target_type, target_id=target_id, since=since, until=until, limit=limit, offset=offset)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->list_action_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  | [optional]
 **action** | **str**|  | [optional]
 **category** | **str**|  | [optional]
 **status** | **str**|  | [optional]
 **source** | **str**|  | [optional]
 **target_type** | **str**|  | [optional]
 **target_id** | **str**|  | [optional]
 **since** | **str**| ISO lower bound (inclusive) on created_at. | [optional]
 **until** | **str**| ISO upper bound (exclusive) on created_at. | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 50
 **offset** | **int**|  | [optional] if omitted the server will use the default value of 0

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

# **list_action_log_calls**
> bool, date, datetime, dict, float, int, list, str, none_type list_action_log_calls(id)

The outbound platform HTTP calls under an event (oldest first) — url, method, status, latency, redacted request/response bodies, proxy + recipe/hash. Answers \"what was sent / what went wrong\".

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.list_action_log_calls_item import ListActionLogCallsItem
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
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The outbound platform HTTP calls under an event (oldest first) — url, method, status, latency, redacted request/response bodies, proxy + recipe/hash. Answers \"what was sent / what went wrong\".
        api_response = api_instance.list_action_log_calls(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->list_action_log_calls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

