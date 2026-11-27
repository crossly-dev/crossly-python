# crossly.MagicApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_magic_auto_decision_undo**](MagicApi.md#create_magic_auto_decision_undo) | **POST** /v1/magic/auto/decisions/{decisionId}/undo | Undo an automated Magic List decision, deleting its unpublished draft.
[**create_magic_auto_item**](MagicApi.md#create_magic_auto_item) | **POST** /v1/magic/auto/items | Scan one item and match it automatically (drafts only, never publishes).
[**create_magic_auto_run**](MagicApi.md#create_magic_auto_run) | **POST** /v1/magic/auto/runs/{runId} | Score a Magic List run automatically; a confident match in auto mode becomes a draft.
[**create_magic_auto_run_swipe**](MagicApi.md#create_magic_auto_run_swipe) | **POST** /v1/magic/auto/runs/{runId}/swipes | Record a seller swipe session (kept and rejected match keys) for a Magic List run.
[**create_magic_scan**](MagicApi.md#create_magic_scan) | **POST** /v1/magic/scan | Run a Magic List image scan.
[**create_magic_scan_synthesize**](MagicApi.md#create_magic_scan_synthesize) | **POST** /v1/magic/scan/{runId}/synthesize | Synthesize a draft from confirmed matches.
[**get_magic_auto_setting**](MagicApi.md#get_magic_auto_setting) | **GET** /v1/magic/auto/settings | The seller’s Magic List automated-matching mode.
[**get_magic_draft**](MagicApi.md#get_magic_draft) | **GET** /v1/magic/drafts/{draftId} | Get a synthesized Magic List draft.
[**list_magic_auto_run_decisions**](MagicApi.md#list_magic_auto_run_decisions) | **GET** /v1/magic/auto/runs/{runId}/decisions | Every match decision round (automated and seller) for a Magic List run.
[**list_magic_recent**](MagicApi.md#list_magic_recent) | **GET** /v1/magic/recent | Recent Magic List scans for this seller.
[**update_magic_auto_setting**](MagicApi.md#update_magic_auto_setting) | **PUT** /v1/magic/auto/settings | Set the Magic List automated-matching mode (off | auto | review_all).


# **create_magic_auto_decision_undo**
> CreateMagicAutoDecisionUndoResponse create_magic_auto_decision_undo(decision_id)

Undo an automated Magic List decision, deleting its unpublished draft.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.common.error import Error
from crossly.model.magic.create_magic_auto_decision_undo_response import CreateMagicAutoDecisionUndoResponse
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
    api_instance = magic_api.MagicApi(api_client)
    decision_id = "decisionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Undo an automated Magic List decision, deleting its unpublished draft.
        api_response = api_instance.create_magic_auto_decision_undo(decision_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MagicApi->create_magic_auto_decision_undo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **decision_id** | **str**|  |

### Return type

**CreateMagicAutoDecisionUndoResponse**

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

# **create_magic_auto_item**
> CreateMagicAutoItemResponse create_magic_auto_item()

Scan one item and match it automatically (drafts only, never publishes).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.magic.create_magic_auto_item_response import CreateMagicAutoItemResponse
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
    api_instance = magic_api.MagicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Scan one item and match it automatically (drafts only, never publishes).
        api_response = api_instance.create_magic_auto_item()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MagicApi->create_magic_auto_item: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateMagicAutoItemResponse**

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

# **create_magic_auto_run**
> CreateMagicAutoRunResponse create_magic_auto_run(run_id)

Score a Magic List run automatically; a confident match in auto mode becomes a draft.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.magic.create_magic_auto_run_response import CreateMagicAutoRunResponse
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
    api_instance = magic_api.MagicApi(api_client)
    run_id = "runId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Score a Magic List run automatically; a confident match in auto mode becomes a draft.
        api_response = api_instance.create_magic_auto_run(run_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MagicApi->create_magic_auto_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |

### Return type

**CreateMagicAutoRunResponse**

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

# **create_magic_auto_run_swipe**
> CreateMagicAutoRunSwipeResponse create_magic_auto_run_swipe(run_id)

Record a seller swipe session (kept and rejected match keys) for a Magic List run.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.common.error import Error
from crossly.model.magic.create_magic_auto_run_swipe_response import CreateMagicAutoRunSwipeResponse
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
    api_instance = magic_api.MagicApi(api_client)
    run_id = "runId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Record a seller swipe session (kept and rejected match keys) for a Magic List run.
        api_response = api_instance.create_magic_auto_run_swipe(run_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MagicApi->create_magic_auto_run_swipe: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |

### Return type

**CreateMagicAutoRunSwipeResponse**

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

# **create_magic_scan**
> CreateMagicScanResponse create_magic_scan()

Run a Magic List image scan.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.common.error import Error
from crossly.model.magic.create_magic_scan_response import CreateMagicScanResponse
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
    api_instance = magic_api.MagicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Run a Magic List image scan.
        api_response = api_instance.create_magic_scan()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MagicApi->create_magic_scan: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateMagicScanResponse**

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

# **create_magic_scan_synthesize**
> CreateMagicScanSynthesizeResponse create_magic_scan_synthesize(run_id)

Synthesize a draft from confirmed matches.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.magic.create_magic_scan_synthesize_response import CreateMagicScanSynthesizeResponse
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
    api_instance = magic_api.MagicApi(api_client)
    run_id = "runId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Synthesize a draft from confirmed matches.
        api_response = api_instance.create_magic_scan_synthesize(run_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MagicApi->create_magic_scan_synthesize: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |

### Return type

**CreateMagicScanSynthesizeResponse**

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

# **get_magic_auto_setting**
> GetMagicAutoSettingResponse get_magic_auto_setting()

The seller’s Magic List automated-matching mode.

mode: off (every match is swiped by hand), auto (confident matches become DRAFTS on their own, never published, always undoable) or review_all (Crossly pre-marks its picks; the seller confirms). Default review_all.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.common.error import Error
from crossly.model.magic.get_magic_auto_setting_response import GetMagicAutoSettingResponse
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
    api_instance = magic_api.MagicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The seller’s Magic List automated-matching mode.
        api_response = api_instance.get_magic_auto_setting()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MagicApi->get_magic_auto_setting: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetMagicAutoSettingResponse**

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

# **get_magic_draft**
> GetMagicDraftResponse get_magic_draft(draft_id)

Get a synthesized Magic List draft.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.common.error import Error
from crossly.model.magic.get_magic_draft_response import GetMagicDraftResponse
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
    api_instance = magic_api.MagicApi(api_client)
    draft_id = "draftId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a synthesized Magic List draft.
        api_response = api_instance.get_magic_draft(draft_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MagicApi->get_magic_draft: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**|  |

### Return type

**GetMagicDraftResponse**

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

# **list_magic_auto_run_decisions**
> ListMagicAutoRunDecisionsResponse list_magic_auto_run_decisions(run_id)

Every match decision round (automated and seller) for a Magic List run.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.common.error import Error
from crossly.model.magic.list_magic_auto_run_decisions_response import ListMagicAutoRunDecisionsResponse
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
    api_instance = magic_api.MagicApi(api_client)
    run_id = "runId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Every match decision round (automated and seller) for a Magic List run.
        api_response = api_instance.list_magic_auto_run_decisions(run_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MagicApi->list_magic_auto_run_decisions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  |

### Return type

**ListMagicAutoRunDecisionsResponse**

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

# **list_magic_recent**
> ListMagicRecentResponse list_magic_recent()

Recent Magic List scans for this seller.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.common.error import Error
from crossly.model.magic.list_magic_recent_response import ListMagicRecentResponse
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
    api_instance = magic_api.MagicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Recent Magic List scans for this seller.
        api_response = api_instance.list_magic_recent()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MagicApi->list_magic_recent: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListMagicRecentResponse**

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

# **update_magic_auto_setting**
> GetMagicAutoSettingResponse update_magic_auto_setting(update_magic_auto_setting_request)

Set the Magic List automated-matching mode (off | auto | review_all).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.magic.update_magic_auto_setting_request import UpdateMagicAutoSettingRequest
from crossly.model.common.error import Error
from crossly.model.magic.get_magic_auto_setting_response import GetMagicAutoSettingResponse
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
    api_instance = magic_api.MagicApi(api_client)
    update_magic_auto_setting_request = UpdateMagicAutoSettingRequest(
        mode="off",
    ) # UpdateMagicAutoSettingRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set the Magic List automated-matching mode (off | auto | review_all).
        api_response = api_instance.update_magic_auto_setting(update_magic_auto_setting_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MagicApi->update_magic_auto_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_magic_auto_setting_request** | **UpdateMagicAutoSettingRequest**|  |

### Return type

**GetMagicAutoSettingResponse**

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

