# crossly.PolicyPresetsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_preset**](PolicyPresetsApi.md#create_policy_preset) | **POST** /v1/policy-presets | Create a return / shipping / payment policy preset.
[**delete_policy_preset**](PolicyPresetsApi.md#delete_policy_preset) | **DELETE** /v1/policy-presets/{id} | Delete a policy preset.
[**list_policy_presets**](PolicyPresetsApi.md#list_policy_presets) | **GET** /v1/policy-presets | List the seller&#39;s return / shipping / payment policy presets.
[**update_policy_preset**](PolicyPresetsApi.md#update_policy_preset) | **PATCH** /v1/policy-presets/{id} | Update a policy preset.


# **create_policy_preset**
> CreatePolicyPresetResponse create_policy_preset()

Create a return / shipping / payment policy preset.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import policy_presets_api
from crossly.model.create_policy_preset_response import CreatePolicyPresetResponse
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
    api_instance = policy_presets_api.PolicyPresetsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a return / shipping / payment policy preset.
        api_response = api_instance.create_policy_preset()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PolicyPresetsApi->create_policy_preset: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreatePolicyPresetResponse**](CreatePolicyPresetResponse.md)

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

# **delete_policy_preset**
> DeletePolicyPresetResponse delete_policy_preset(id)

Delete a policy preset.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import policy_presets_api
from crossly.model.delete_policy_preset_response import DeletePolicyPresetResponse
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
    api_instance = policy_presets_api.PolicyPresetsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a policy preset.
        api_response = api_instance.delete_policy_preset(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PolicyPresetsApi->delete_policy_preset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DeletePolicyPresetResponse**](DeletePolicyPresetResponse.md)

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

# **list_policy_presets**
> bool, date, datetime, dict, float, int, list, str, none_type list_policy_presets()

List the seller's return / shipping / payment policy presets.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import policy_presets_api
from crossly.model.error import Error
from crossly.model.list_policy_presets_item import ListPolicyPresetsItem
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
    api_instance = policy_presets_api.PolicyPresetsApi(api_client)
    kind = "return" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the seller's return / shipping / payment policy presets.
        api_response = api_instance.list_policy_presets(kind=kind)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PolicyPresetsApi->list_policy_presets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**|  | [optional]

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

# **update_policy_preset**
> UpdatePolicyPresetResponse update_policy_preset(id)

Update a policy preset.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import policy_presets_api
from crossly.model.error import Error
from crossly.model.update_policy_preset_response import UpdatePolicyPresetResponse
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
    api_instance = policy_presets_api.PolicyPresetsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update a policy preset.
        api_response = api_instance.update_policy_preset(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling PolicyPresetsApi->update_policy_preset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UpdatePolicyPresetResponse**](UpdatePolicyPresetResponse.md)

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

