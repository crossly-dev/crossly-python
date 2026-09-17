# crossly.AccountsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](AccountsApi.md#create_account) | **POST** /v1/accounts | Connect a new platform account (kicks off OAuth or extension handshake).
[**create_connection_email_imap**](AccountsApi.md#create_connection_email_imap) | **POST** /v1/connections/email/imap | Add an IMAP mailbox connection.
[**create_connection_email_imap_test**](AccountsApi.md#create_connection_email_imap_test) | **POST** /v1/connections/email/imap/test | Validate IMAP credentials without persisting.
[**create_connection_request**](AccountsApi.md#create_connection_request) | **POST** /v1/connections/{platform}/request | Express interest in a request_only platform.
[**create_platform_account_connect**](AccountsApi.md#create_platform_account_connect) | **POST** /v1/platform-accounts/{platform}/connect | Revive or initiate connection for a cookie platform.
[**create_platform_account_disconnect**](AccountsApi.md#create_platform_account_disconnect) | **POST** /v1/platform-accounts/{platform}/disconnect | Archive every active account row for a platform.
[**create_platform_account_history_import**](AccountsApi.md#create_platform_account_history_import) | **POST** /v1/platform-accounts/{platform}/history-import | Set how far back to backfill order history + active listings for a platform, and run it now.
[**create_platform_account_refresh_status**](AccountsApi.md#create_platform_account_refresh_status) | **POST** /v1/platform-accounts/refresh-status | Run on-demand healthchecks across cookie accounts.
[**delete_account**](AccountsApi.md#delete_account) | **DELETE** /v1/accounts/{id} | Disconnect a platform account.
[**delete_connection_by_id**](AccountsApi.md#delete_connection_by_id) | **DELETE** /v1/connections/by-id/{id} | Disconnect a specific OAuth connection by id.
[**delete_connection_email_imap**](AccountsApi.md#delete_connection_email_imap) | **DELETE** /v1/connections/email/imap/{id} | Remove an IMAP mailbox connection.
[**get_connection_email**](AccountsApi.md#get_connection_email) | **GET** /v1/connections/email | List IMAP and email-OAuth connections.
[**get_connection_extension_online**](AccountsApi.md#get_connection_extension_online) | **GET** /v1/connections/extension-online | Check if the browser extension is online.
[**get_oauth_init**](AccountsApi.md#get_oauth_init) | **GET** /v1/oauth/{platform}/init | Return the OAuth authorize URL for an API-track platform.
[**get_platform_limit**](AccountsApi.md#get_platform_limit) | **GET** /v1/platforms/limits | eBay free-tier + Etsy fees aggregate.
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /v1/accounts | List your connected platform accounts.
[**list_connections**](AccountsApi.md#list_connections) | **GET** /v1/connections | List OAuth-connected API platforms.
[**update_connection_email_imap**](AccountsApi.md#update_connection_email_imap) | **PATCH** /v1/connections/email/imap/{id} | Edit an IMAP mailbox connection.
[**update_platform_preference**](AccountsApi.md#update_platform_preference) | **PATCH** /v1/platforms/{platform}/preferences | Update per-platform connection preferences.


# **create_account**
> CreateAccountResponse create_account()

Connect a new platform account (kicks off OAuth or extension handshake).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.create_account_response import CreateAccountResponse
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
    api_instance = accounts_api.AccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Connect a new platform account (kicks off OAuth or extension handshake).
        api_response = api_instance.create_account()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->create_account: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAccountResponse**](CreateAccountResponse.md)

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

# **create_connection_email_imap**
> CreateConnectionEmailImapResponse create_connection_email_imap()

Add an IMAP mailbox connection.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.create_connection_email_imap_response import CreateConnectionEmailImapResponse
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
    api_instance = accounts_api.AccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Add an IMAP mailbox connection.
        api_response = api_instance.create_connection_email_imap()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->create_connection_email_imap: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateConnectionEmailImapResponse**](CreateConnectionEmailImapResponse.md)

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

# **create_connection_email_imap_test**
> CreateConnectionEmailImapTestResponse create_connection_email_imap_test()

Validate IMAP credentials without persisting.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.create_connection_email_imap_test_response import CreateConnectionEmailImapTestResponse
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
    api_instance = accounts_api.AccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Validate IMAP credentials without persisting.
        api_response = api_instance.create_connection_email_imap_test()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->create_connection_email_imap_test: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateConnectionEmailImapTestResponse**](CreateConnectionEmailImapTestResponse.md)

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

# **create_connection_request**
> CreateConnectionRequestResponse create_connection_request(platform)

Express interest in a request_only platform.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.create_connection_request_response import CreateConnectionRequestResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    platform = "platform_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Express interest in a request_only platform.
        api_response = api_instance.create_connection_request(platform)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->create_connection_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |

### Return type

[**CreateConnectionRequestResponse**](CreateConnectionRequestResponse.md)

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

# **create_platform_account_connect**
> CreatePlatformAccountConnectResponse create_platform_account_connect(platform)

Revive or initiate connection for a cookie platform.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.create_platform_account_connect_response import CreatePlatformAccountConnectResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    platform = "platform_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Revive or initiate connection for a cookie platform.
        api_response = api_instance.create_platform_account_connect(platform)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->create_platform_account_connect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |

### Return type

[**CreatePlatformAccountConnectResponse**](CreatePlatformAccountConnectResponse.md)

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

# **create_platform_account_disconnect**
> CreatePlatformAccountDisconnectResponse create_platform_account_disconnect(platform)

Archive every active account row for a platform.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.create_platform_account_disconnect_response import CreatePlatformAccountDisconnectResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    platform = "platform_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Archive every active account row for a platform.
        api_response = api_instance.create_platform_account_disconnect(platform)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->create_platform_account_disconnect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |

### Return type

[**CreatePlatformAccountDisconnectResponse**](CreatePlatformAccountDisconnectResponse.md)

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

# **create_platform_account_history_import**
> CreatePlatformAccountHistoryImportResponse create_platform_account_history_import(platform, inline_object1)

Set how far back to backfill order history + active listings for a platform, and run it now.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.inline_object1 import InlineObject1
from crossly.model.create_platform_account_history_import_response import CreatePlatformAccountHistoryImportResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    platform = "platform_example" # str | 
    inline_object1 = InlineObject1(
        days=None,
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Set how far back to backfill order history + active listings for a platform, and run it now.
        api_response = api_instance.create_platform_account_history_import(platform, inline_object1)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->create_platform_account_history_import: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

### Return type

[**CreatePlatformAccountHistoryImportResponse**](CreatePlatformAccountHistoryImportResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_platform_account_refresh_status**
> CreatePlatformAccountRefreshStatusResponse create_platform_account_refresh_status()

Run on-demand healthchecks across cookie accounts.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.create_platform_account_refresh_status_response import CreatePlatformAccountRefreshStatusResponse
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
    api_instance = accounts_api.AccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Run on-demand healthchecks across cookie accounts.
        api_response = api_instance.create_platform_account_refresh_status()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->create_platform_account_refresh_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreatePlatformAccountRefreshStatusResponse**](CreatePlatformAccountRefreshStatusResponse.md)

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

# **delete_account**
> DeleteAccountResponse delete_account(id)

Disconnect a platform account.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.delete_account_response import DeleteAccountResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Disconnect a platform account.
        api_response = api_instance.delete_account(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->delete_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DeleteAccountResponse**](DeleteAccountResponse.md)

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

# **delete_connection_by_id**
> DeleteConnectionByIdResponse delete_connection_by_id(id)

Disconnect a specific OAuth connection by id.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.delete_connection_by_id_response import DeleteConnectionByIdResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Disconnect a specific OAuth connection by id.
        api_response = api_instance.delete_connection_by_id(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->delete_connection_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DeleteConnectionByIdResponse**](DeleteConnectionByIdResponse.md)

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

# **delete_connection_email_imap**
> DeleteConnectionEmailImapResponse delete_connection_email_imap(id)

Remove an IMAP mailbox connection.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.delete_connection_email_imap_response import DeleteConnectionEmailImapResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove an IMAP mailbox connection.
        api_response = api_instance.delete_connection_email_imap(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->delete_connection_email_imap: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DeleteConnectionEmailImapResponse**](DeleteConnectionEmailImapResponse.md)

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

# **get_connection_email**
> GetConnectionEmailResponse get_connection_email()

List IMAP and email-OAuth connections.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.get_connection_email_response import GetConnectionEmailResponse
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
    api_instance = accounts_api.AccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List IMAP and email-OAuth connections.
        api_response = api_instance.get_connection_email()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->get_connection_email: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetConnectionEmailResponse**](GetConnectionEmailResponse.md)

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

# **get_connection_extension_online**
> GetConnectionExtensionOnlineResponse get_connection_extension_online()

Check if the browser extension is online.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.get_connection_extension_online_response import GetConnectionExtensionOnlineResponse
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
    api_instance = accounts_api.AccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Check if the browser extension is online.
        api_response = api_instance.get_connection_extension_online()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->get_connection_extension_online: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetConnectionExtensionOnlineResponse**](GetConnectionExtensionOnlineResponse.md)

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

# **get_oauth_init**
> GetOauthInitResponse get_oauth_init(platform)

Return the OAuth authorize URL for an API-track platform.

Most platforms return `{ url }`. Etsy adds `{ correlationId }` (PKCE verifier stashed in Redis). Bonanza adds `{ oneShot: true }`. WooCommerce requires `?siteUrl=...`. Walmart returns `{ status: \"request_only\", requestUrl, message }` instead of a URL because per-seller OAuth needs Solution Provider approval.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.get_oauth_init_response import GetOauthInitResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    platform = "platform_example" # str | 
    shop = "shop_example" # str |  (optional)
    region = "region_example" # str |  (optional)
    site_url = "siteUrl_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return the OAuth authorize URL for an API-track platform.
        api_response = api_instance.get_oauth_init(platform)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->get_oauth_init: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return the OAuth authorize URL for an API-track platform.
        api_response = api_instance.get_oauth_init(platform, shop=shop, region=region, site_url=site_url)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->get_oauth_init: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |
 **shop** | **str**|  | [optional]
 **region** | **str**|  | [optional]
 **site_url** | **str**|  | [optional]

### Return type

[**GetOauthInitResponse**](GetOauthInitResponse.md)

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

# **get_platform_limit**
> GetPlatformLimitResponse get_platform_limit()

eBay free-tier + Etsy fees aggregate.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.get_platform_limit_response import GetPlatformLimitResponse
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
    api_instance = accounts_api.AccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # eBay free-tier + Etsy fees aggregate.
        api_response = api_instance.get_platform_limit()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->get_platform_limit: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPlatformLimitResponse**](GetPlatformLimitResponse.md)

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

# **list_accounts**
> bool, date, datetime, dict, float, int, list, str, none_type list_accounts()

List your connected platform accounts.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.list_accounts_item import ListAccountsItem
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
    api_instance = accounts_api.AccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List your connected platform accounts.
        api_response = api_instance.list_accounts()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
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

# **list_connections**
> bool, date, datetime, dict, float, int, list, str, none_type list_connections()

List OAuth-connected API platforms.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.list_connections_item import ListConnectionsItem
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
    api_instance = accounts_api.AccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List OAuth-connected API platforms.
        api_response = api_instance.list_connections()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->list_connections: %s\n" % e)
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

# **update_connection_email_imap**
> UpdateConnectionEmailImapResponse update_connection_email_imap(id)

Edit an IMAP mailbox connection.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.error import Error
from crossly.model.update_connection_email_imap_response import UpdateConnectionEmailImapResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an IMAP mailbox connection.
        api_response = api_instance.update_connection_email_imap(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->update_connection_email_imap: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UpdateConnectionEmailImapResponse**](UpdateConnectionEmailImapResponse.md)

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

# **update_platform_preference**
> UpdatePlatformPreferenceResponse update_platform_preference(platform)

Update per-platform connection preferences.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import accounts_api
from crossly.model.update_platform_preference_response import UpdatePlatformPreferenceResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    platform = "platform_example" # str | 
    connection_id = "connection_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update per-platform connection preferences.
        api_response = api_instance.update_platform_preference(platform)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->update_platform_preference: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update per-platform connection preferences.
        api_response = api_instance.update_platform_preference(platform, connection_id=connection_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AccountsApi->update_platform_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |
 **connection_id** | **str**|  | [optional]

### Return type

[**UpdatePlatformPreferenceResponse**](UpdatePlatformPreferenceResponse.md)

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

