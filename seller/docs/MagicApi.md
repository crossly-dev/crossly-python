# crossly.MagicApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_magic_scan**](MagicApi.md#create_magic_scan) | **POST** /v1/magic/scan | Run a Magic List image scan.
[**create_magic_scan_synthesize**](MagicApi.md#create_magic_scan_synthesize) | **POST** /v1/magic/scan/{runId}/synthesize | Synthesize a draft from confirmed matches.
[**get_magic_draft**](MagicApi.md#get_magic_draft) | **GET** /v1/magic/drafts/{draftId} | Get a synthesized Magic List draft.
[**list_magic_recent**](MagicApi.md#list_magic_recent) | **GET** /v1/magic/recent | Recent Magic List scans for this seller.


# **create_magic_scan**
> CreateMagicScanResponse create_magic_scan()

Run a Magic List image scan.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.error import Error
from crossly.model.create_magic_scan_response import CreateMagicScanResponse
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

[**CreateMagicScanResponse**](CreateMagicScanResponse.md)

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

# **create_magic_scan_synthesize**
> CreateMagicScanSynthesizeResponse create_magic_scan_synthesize(run_id)

Synthesize a draft from confirmed matches.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.create_magic_scan_synthesize_response import CreateMagicScanSynthesizeResponse
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

[**CreateMagicScanSynthesizeResponse**](CreateMagicScanSynthesizeResponse.md)

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

# **get_magic_draft**
> GetMagicDraftResponse get_magic_draft(draft_id)

Get a synthesized Magic List draft.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.error import Error
from crossly.model.get_magic_draft_response import GetMagicDraftResponse
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

[**GetMagicDraftResponse**](GetMagicDraftResponse.md)

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

# **list_magic_recent**
> bool, date, datetime, dict, float, int, list, str, none_type list_magic_recent()

Recent Magic List scans for this seller.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import magic_api
from crossly.model.list_magic_recent_item import ListMagicRecentItem
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

