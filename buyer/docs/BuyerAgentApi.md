# crossly_buyer.BuyerAgentApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_buyer_agent_session**](BuyerAgentApi.md#create_buyer_agent_session) | **POST** /v1/buyer/agent/sessions | Start a shopping agent conversation.
[**create_buyer_agent_session_act**](BuyerAgentApi.md#create_buyer_agent_session_act) | **POST** /v1/buyer/agent/sessions/{id}/act | Act on an option: save, cart, alert, registry, price (real-sales check), offer (prepare / confirm), or buy (quote — complete with POST /api/v1/buyer/checkout). Needs the action’s own scope too.
[**create_buyer_agent_session_react**](BuyerAgentApi.md#create_buyer_agent_session_react) | **POST** /v1/buyer/agent/sessions/{id}/react | Like or dislike an option; the next search leans toward likes and drops dislikes.
[**create_buyer_agent_session_turn**](BuyerAgentApi.md#create_buyer_agent_session_turn) | **POST** /v1/buyer/agent/sessions/{id}/turns | Say something to the agent: what you want, a critique of the options (\&quot;cheaper\&quot;, \&quot;more like #2\&quot;), or send a photo (imageBase64) to find things like it. Returns its reply and the new numbered options.
[**delete_buyer_agent_session**](BuyerAgentApi.md#delete_buyer_agent_session) | **DELETE** /v1/buyer/agent/sessions/{id} | Delete a conversation.
[**get_buyer_agent_session**](BuyerAgentApi.md#get_buyer_agent_session) | **GET** /v1/buyer/agent/sessions/{id} | A conversation: its brief and turns, with each turn’s options re-read live.
[**list_buyer_agent_sessions**](BuyerAgentApi.md#list_buyer_agent_sessions) | **GET** /v1/buyer/agent/sessions | Your shopping agent conversations, newest first.


# **create_buyer_agent_session**
> CreateBuyerAgentSessionResponse create_buyer_agent_session()

Start a shopping agent conversation.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_agent_api
from crossly_buyer.model.agent.create_buyer_agent_session_response import CreateBuyerAgentSessionResponse
from crossly_buyer.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_agent_api.BuyerAgentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Start a shopping agent conversation.
        api_response = api_instance.create_buyer_agent_session()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerAgentApi->create_buyer_agent_session: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateBuyerAgentSessionResponse**

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **create_buyer_agent_session_act**
> CreateBuyerAgentSessionActResponse create_buyer_agent_session_act(id)

Act on an option: save, cart, alert, registry, price (real-sales check), offer (prepare / confirm), or buy (quote — complete with POST /api/v1/buyer/checkout). Needs the action’s own scope too.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_agent_api
from crossly_buyer.model.agent.create_buyer_agent_session_act_response import CreateBuyerAgentSessionActResponse
from crossly_buyer.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_agent_api.BuyerAgentApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Act on an option: save, cart, alert, registry, price (real-sales check), offer (prepare / confirm), or buy (quote — complete with POST /api/v1/buyer/checkout). Needs the action’s own scope too.
        api_response = api_instance.create_buyer_agent_session_act(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerAgentApi->create_buyer_agent_session_act: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateBuyerAgentSessionActResponse**

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **create_buyer_agent_session_react**
> DeleteBuyerAgentSessionResponse create_buyer_agent_session_react(id)

Like or dislike an option; the next search leans toward likes and drops dislikes.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_agent_api
from crossly_buyer.model.agent.delete_buyer_agent_session_response import DeleteBuyerAgentSessionResponse
from crossly_buyer.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_agent_api.BuyerAgentApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Like or dislike an option; the next search leans toward likes and drops dislikes.
        api_response = api_instance.create_buyer_agent_session_react(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerAgentApi->create_buyer_agent_session_react: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteBuyerAgentSessionResponse**

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **create_buyer_agent_session_turn**
> CreateBuyerAgentSessionTurnResponse create_buyer_agent_session_turn(id)

Say something to the agent: what you want, a critique of the options (\"cheaper\", \"more like #2\"), or send a photo (imageBase64) to find things like it. Returns its reply and the new numbered options.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_agent_api
from crossly_buyer.model.common.error import Error
from crossly_buyer.model.agent.create_buyer_agent_session_turn_response import CreateBuyerAgentSessionTurnResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_agent_api.BuyerAgentApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Say something to the agent: what you want, a critique of the options (\"cheaper\", \"more like #2\"), or send a photo (imageBase64) to find things like it. Returns its reply and the new numbered options.
        api_response = api_instance.create_buyer_agent_session_turn(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerAgentApi->create_buyer_agent_session_turn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateBuyerAgentSessionTurnResponse**

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **delete_buyer_agent_session**
> DeleteBuyerAgentSessionResponse delete_buyer_agent_session(id)

Delete a conversation.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_agent_api
from crossly_buyer.model.agent.delete_buyer_agent_session_response import DeleteBuyerAgentSessionResponse
from crossly_buyer.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_agent_api.BuyerAgentApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a conversation.
        api_response = api_instance.delete_buyer_agent_session(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerAgentApi->delete_buyer_agent_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteBuyerAgentSessionResponse**

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **get_buyer_agent_session**
> GetBuyerAgentSessionResponse get_buyer_agent_session(id)

A conversation: its brief and turns, with each turn’s options re-read live.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_agent_api
from crossly_buyer.model.agent.get_buyer_agent_session_response import GetBuyerAgentSessionResponse
from crossly_buyer.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_agent_api.BuyerAgentApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A conversation: its brief and turns, with each turn’s options re-read live.
        api_response = api_instance.get_buyer_agent_session(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerAgentApi->get_buyer_agent_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetBuyerAgentSessionResponse**

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **list_buyer_agent_sessions**
> ListBuyerAgentSessionsResponse list_buyer_agent_sessions()

Your shopping agent conversations, newest first.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_agent_api
from crossly_buyer.model.common.error import Error
from crossly_buyer.model.agent.list_buyer_agent_sessions_response import ListBuyerAgentSessionsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly_buyer.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BuyerOAuth
configuration = crossly_buyer.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly_buyer.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buyer_agent_api.BuyerAgentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your shopping agent conversations, newest first.
        api_response = api_instance.list_buyer_agent_sessions()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerAgentApi->list_buyer_agent_sessions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListBuyerAgentSessionsResponse**

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

