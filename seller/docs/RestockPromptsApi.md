# crossly.RestockPromptsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_restock_prompt_dismiss**](RestockPromptsApi.md#create_restock_prompt_dismiss) | **POST** /v1/restock-prompts/{id}/dismiss | Dismiss a pending restock prompt.
[**create_restock_prompt_republish**](RestockPromptsApi.md#create_restock_prompt_republish) | **POST** /v1/restock-prompts/{id}/republish | Republish a restock prompt to platforms.
[**get_restock_prompt_setting**](RestockPromptsApi.md#get_restock_prompt_setting) | **GET** /v1/restock-prompts/settings | Whether restocked items are republished automatically.
[**list_restock_prompts**](RestockPromptsApi.md#list_restock_prompts) | **GET** /v1/restock-prompts | List pending restock prompts.
[**update_restock_prompt_setting**](RestockPromptsApi.md#update_restock_prompt_setting) | **PUT** /v1/restock-prompts/settings | Turn automatic republish of restocked items on or off.


# **create_restock_prompt_dismiss**
> OkResponse create_restock_prompt_dismiss(id)

Dismiss a pending restock prompt.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import restock_prompts_api
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
    api_instance = restock_prompts_api.RestockPromptsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Dismiss a pending restock prompt.
        api_response = api_instance.create_restock_prompt_dismiss(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling RestockPromptsApi->create_restock_prompt_dismiss: %s\n" % e)
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

# **create_restock_prompt_republish**
> CreateRestockPromptRepublishResponse create_restock_prompt_republish(id)

Republish a restock prompt to platforms.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import restock_prompts_api
from crossly.model.common.create_restock_prompt_republish_response import CreateRestockPromptRepublishResponse
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
    api_instance = restock_prompts_api.RestockPromptsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Republish a restock prompt to platforms.
        api_response = api_instance.create_restock_prompt_republish(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling RestockPromptsApi->create_restock_prompt_republish: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateRestockPromptRepublishResponse**

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

# **get_restock_prompt_setting**
> GetRestockPromptSettingResponse get_restock_prompt_setting()

Whether restocked items are republished automatically.

autoRepublish (default true): when an item that sold out comes back in stock, Crossly republishes it to the marketplaces it came off without asking. False: a restock prompt is raised instead. A listing the seller ended by hand is never republished automatically.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import restock_prompts_api
from crossly.model.common.error import Error
from crossly.model.common.get_restock_prompt_setting_response import GetRestockPromptSettingResponse
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
    api_instance = restock_prompts_api.RestockPromptsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Whether restocked items are republished automatically.
        api_response = api_instance.get_restock_prompt_setting()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling RestockPromptsApi->get_restock_prompt_setting: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetRestockPromptSettingResponse**

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

# **list_restock_prompts**
> ListRestockPromptsResponse list_restock_prompts()

List pending restock prompts.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import restock_prompts_api
from crossly.model.common.list_restock_prompts_response import ListRestockPromptsResponse
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
    api_instance = restock_prompts_api.RestockPromptsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List pending restock prompts.
        api_response = api_instance.list_restock_prompts()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling RestockPromptsApi->list_restock_prompts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListRestockPromptsResponse**

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

# **update_restock_prompt_setting**
> GetRestockPromptSettingResponse update_restock_prompt_setting(get_restock_prompt_setting_response)

Turn automatic republish of restocked items on or off.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import restock_prompts_api
from crossly.model.common.error import Error
from crossly.model.common.get_restock_prompt_setting_response import GetRestockPromptSettingResponse
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
    api_instance = restock_prompts_api.RestockPromptsApi(api_client)
    get_restock_prompt_setting_response = GetRestockPromptSettingResponse(
        auto_republish=True,
    ) # GetRestockPromptSettingResponse | 

    # example passing only required values which don't have defaults set
    try:
        # Turn automatic republish of restocked items on or off.
        api_response = api_instance.update_restock_prompt_setting(get_restock_prompt_setting_response)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling RestockPromptsApi->update_restock_prompt_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_restock_prompt_setting_response** | **GetRestockPromptSettingResponse**|  |

### Return type

**GetRestockPromptSettingResponse**

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

