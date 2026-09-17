# crossly.AccountApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_cancel_deletion**](AccountApi.md#create_account_cancel_deletion) | **POST** /v1/account/cancel-deletion | Cancel a pending account deletion.
[**create_account_logout_all**](AccountApi.md#create_account_logout_all) | **POST** /v1/account/logout-all | Revoke every browser auth session for this user.
[**create_account_request_deletion**](AccountApi.md#create_account_request_deletion) | **POST** /v1/account/request-deletion | Schedule account deletion after a grace period.
[**delete_auth_session**](AccountApi.md#delete_auth_session) | **DELETE** /v1/auth/sessions | Revoke all active browser sessions.
[**delete_auth_session_by_session_id**](AccountApi.md#delete_auth_session_by_session_id) | **DELETE** /v1/auth/sessions/{sessionId} | Revoke a single browser session by id.
[**delete_connected_app**](AccountApi.md#delete_connected_app) | **DELETE** /v1/connected-apps/{grantId} | Disconnect a third-party app. Its tokens stop working immediately.
[**get_account_deletion_status**](AccountApi.md#get_account_deletion_status) | **GET** /v1/account/deletion-status | Get the currently-pending deletion request, if any.
[**get_me**](AccountApi.md#get_me) | **GET** /v1/me | Identity check — authenticated user + PAT scopes + account state.
[**list_auth_sessions**](AccountApi.md#list_auth_sessions) | **GET** /v1/auth/sessions | List active browser auth sessions.
[**list_connected_apps**](AccountApi.md#list_connected_apps) | **GET** /v1/connected-apps | List third-party OAuth apps with access to this account.


# **create_account_cancel_deletion**
> CreateAccountCancelDeletionResponse create_account_cancel_deletion()

Cancel a pending account deletion.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import account_api
from crossly.model.error import Error
from crossly.model.create_account_cancel_deletion_response import CreateAccountCancelDeletionResponse
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
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Cancel a pending account deletion.
        api_response = api_instance.create_account_cancel_deletion()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountApi->create_account_cancel_deletion: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAccountCancelDeletionResponse**](CreateAccountCancelDeletionResponse.md)

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

# **create_account_logout_all**
> CreateAccountLogoutAllResponse create_account_logout_all()

Revoke every browser auth session for this user.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import account_api
from crossly.model.error import Error
from crossly.model.create_account_logout_all_response import CreateAccountLogoutAllResponse
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
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Revoke every browser auth session for this user.
        api_response = api_instance.create_account_logout_all()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountApi->create_account_logout_all: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAccountLogoutAllResponse**](CreateAccountLogoutAllResponse.md)

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

# **create_account_request_deletion**
> CreateAccountRequestDeletionResponse create_account_request_deletion()

Schedule account deletion after a grace period.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import account_api
from crossly.model.error import Error
from crossly.model.create_account_request_deletion_response import CreateAccountRequestDeletionResponse
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
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Schedule account deletion after a grace period.
        api_response = api_instance.create_account_request_deletion()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountApi->create_account_request_deletion: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAccountRequestDeletionResponse**](CreateAccountRequestDeletionResponse.md)

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

# **delete_auth_session**
> DeleteAuthSessionResponse delete_auth_session()

Revoke all active browser sessions.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import account_api
from crossly.model.delete_auth_session_response import DeleteAuthSessionResponse
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
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Revoke all active browser sessions.
        api_response = api_instance.delete_auth_session()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountApi->delete_auth_session: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DeleteAuthSessionResponse**](DeleteAuthSessionResponse.md)

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

# **delete_auth_session_by_session_id**
> DeleteAuthSessionBySessionIdResponse delete_auth_session_by_session_id(session_id)

Revoke a single browser session by id.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import account_api
from crossly.model.error import Error
from crossly.model.delete_auth_session_by_session_id_response import DeleteAuthSessionBySessionIdResponse
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
    api_instance = account_api.AccountApi(api_client)
    session_id = "sessionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke a single browser session by id.
        api_response = api_instance.delete_auth_session_by_session_id(session_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountApi->delete_auth_session_by_session_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  |

### Return type

[**DeleteAuthSessionBySessionIdResponse**](DeleteAuthSessionBySessionIdResponse.md)

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

# **delete_connected_app**
> DeleteConnectedAppResponse delete_connected_app(grant_id)

Disconnect a third-party app. Its tokens stop working immediately.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import account_api
from crossly.model.delete_connected_app_response import DeleteConnectedAppResponse
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
    api_instance = account_api.AccountApi(api_client)
    grant_id = "grantId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Disconnect a third-party app. Its tokens stop working immediately.
        api_response = api_instance.delete_connected_app(grant_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountApi->delete_connected_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_id** | **str**|  |

### Return type

[**DeleteConnectedAppResponse**](DeleteConnectedAppResponse.md)

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

# **get_account_deletion_status**
> GetAccountDeletionStatusResponse get_account_deletion_status()

Get the currently-pending deletion request, if any.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import account_api
from crossly.model.get_account_deletion_status_response import GetAccountDeletionStatusResponse
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
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the currently-pending deletion request, if any.
        api_response = api_instance.get_account_deletion_status()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountApi->get_account_deletion_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAccountDeletionStatusResponse**](GetAccountDeletionStatusResponse.md)

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

# **get_me**
> InlineResponse200 get_me()

Identity check — authenticated user + PAT scopes + account state.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import account_api
from crossly.model.inline_response200 import InlineResponse200
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
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Identity check — authenticated user + PAT scopes + account state.
        api_response = api_instance.get_me()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountApi->get_me: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auth_sessions**
> bool, date, datetime, dict, float, int, list, str, none_type list_auth_sessions()

List active browser auth sessions.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import account_api
from crossly.model.list_auth_sessions_item import ListAuthSessionsItem
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
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List active browser auth sessions.
        api_response = api_instance.list_auth_sessions()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountApi->list_auth_sessions: %s\n" % e)
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

# **list_connected_apps**
> bool, date, datetime, dict, float, int, list, str, none_type list_connected_apps()

List third-party OAuth apps with access to this account.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import account_api
from crossly.model.list_connected_apps_item import ListConnectedAppsItem
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
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List third-party OAuth apps with access to this account.
        api_response = api_instance.list_connected_apps()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountApi->list_connected_apps: %s\n" % e)
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

