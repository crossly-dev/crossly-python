# crossly.MobileApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mobile_push_test**](MobileApi.md#create_mobile_push_test) | **POST** /v1/mobile/push-test | Fire a no-op test push to this user&#39;s devices.
[**create_mobile_push_token**](MobileApi.md#create_mobile_push_token) | **POST** /v1/mobile/push-token | Register an Expo push token for this user.
[**delete_mobile_push_token**](MobileApi.md#delete_mobile_push_token) | **DELETE** /v1/mobile/push-tokens | Clear ALL registered push tokens for this user.
[**list_mobile_push_tokens**](MobileApi.md#list_mobile_push_tokens) | **GET** /v1/mobile/push-tokens | List registered Expo push tokens (masked).


# **create_mobile_push_test**
> CreateMobilePushTestResponse create_mobile_push_test()

Fire a no-op test push to this user's devices.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import mobile_api
from crossly.model.error import Error
from crossly.model.create_mobile_push_test_response import CreateMobilePushTestResponse
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
    api_instance = mobile_api.MobileApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fire a no-op test push to this user's devices.
        api_response = api_instance.create_mobile_push_test()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MobileApi->create_mobile_push_test: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateMobilePushTestResponse**](CreateMobilePushTestResponse.md)

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

# **create_mobile_push_token**
> CreateMobilePushTokenResponse create_mobile_push_token()

Register an Expo push token for this user.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import mobile_api
from crossly.model.create_mobile_push_token_response import CreateMobilePushTokenResponse
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
    api_instance = mobile_api.MobileApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Register an Expo push token for this user.
        api_response = api_instance.create_mobile_push_token()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MobileApi->create_mobile_push_token: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateMobilePushTokenResponse**](CreateMobilePushTokenResponse.md)

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

# **delete_mobile_push_token**
> DeleteMobilePushTokenResponse delete_mobile_push_token()

Clear ALL registered push tokens for this user.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import mobile_api
from crossly.model.error import Error
from crossly.model.delete_mobile_push_token_response import DeleteMobilePushTokenResponse
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
    api_instance = mobile_api.MobileApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Clear ALL registered push tokens for this user.
        api_response = api_instance.delete_mobile_push_token()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MobileApi->delete_mobile_push_token: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DeleteMobilePushTokenResponse**](DeleteMobilePushTokenResponse.md)

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

# **list_mobile_push_tokens**
> bool, date, datetime, dict, float, int, list, str, none_type list_mobile_push_tokens()

List registered Expo push tokens (masked).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import mobile_api
from crossly.model.list_mobile_push_tokens_item import ListMobilePushTokensItem
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
    api_instance = mobile_api.MobileApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List registered Expo push tokens (masked).
        api_response = api_instance.list_mobile_push_tokens()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling MobileApi->list_mobile_push_tokens: %s\n" % e)
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

