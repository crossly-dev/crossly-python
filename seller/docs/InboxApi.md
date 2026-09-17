# crossly.InboxApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inbox_ai_suggest**](InboxApi.md#create_inbox_ai_suggest) | **POST** /v1/inbox/ai-suggest | AI reply suggestion for a conversation.
[**create_inbox_canned_respons**](InboxApi.md#create_inbox_canned_respons) | **POST** /v1/inbox/canned-responses | Create a canned response.
[**create_inbox_conversation_bulk**](InboxApi.md#create_inbox_conversation_bulk) | **POST** /v1/inbox/conversations/bulk | Bulk mark read / mark unread / soft-delete conversations.
[**create_inbox_conversation_bulk_ai_respond**](InboxApi.md#create_inbox_conversation_bulk_ai_respond) | **POST** /v1/inbox/conversations/bulk-ai-respond | AI reply suggestion for multiple conversations — draft or send.
[**create_inbox_conversation_offer_action**](InboxApi.md#create_inbox_conversation_offer_action) | **POST** /v1/inbox/conversations/{id}/offer-action | Accept / counter / decline an active offer on a conversation.
[**create_inbox_message_triage**](InboxApi.md#create_inbox_message_triage) | **POST** /v1/inbox/messages/{id}/triage | Manually re-triage a buyer message.
[**create_inbox_offer**](InboxApi.md#create_inbox_offer) | **POST** /v1/inbox/{id}/offer | Accept, counter, or decline an offer on a conversation.
[**create_inbox_reply**](InboxApi.md#create_inbox_reply) | **POST** /v1/inbox/{id}/reply | Send a reply to a conversation thread.
[**delete_inbox_canned_respons**](InboxApi.md#delete_inbox_canned_respons) | **DELETE** /v1/inbox/canned-responses/{id} | Delete a canned response.
[**get_inbox**](InboxApi.md#get_inbox) | **GET** /v1/inbox/{id} | Get one conversation with its messages.
[**get_inbox_canned_respons**](InboxApi.md#get_inbox_canned_respons) | **GET** /v1/inbox/canned-responses | List canned responses.
[**get_inbox_conversation_message**](InboxApi.md#get_inbox_conversation_message) | **GET** /v1/inbox/conversations/{id}/messages | Paginated messages for a conversation.
[**get_inbox_conversation_unread_count**](InboxApi.md#get_inbox_conversation_unread_count) | **GET** /v1/inbox/conversations/unread-count | Sidebar badge: unread conversation count.
[**list_inbox**](InboxApi.md#list_inbox) | **GET** /v1/inbox | List conversations.
[**update_inbox_canned_respons**](InboxApi.md#update_inbox_canned_respons) | **PUT** /v1/inbox/canned-responses/{id} | Update a canned response.
[**update_inbox_conversation**](InboxApi.md#update_inbox_conversation) | **PATCH** /v1/inbox/conversations/{id} | Mark read / change status / close conversation.


# **create_inbox_ai_suggest**
> CreateInboxAiSuggestResponse create_inbox_ai_suggest()

AI reply suggestion for a conversation.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.error import Error
from crossly.model.create_inbox_ai_suggest_response import CreateInboxAiSuggestResponse
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
    api_instance = inbox_api.InboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # AI reply suggestion for a conversation.
        api_response = api_instance.create_inbox_ai_suggest()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->create_inbox_ai_suggest: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInboxAiSuggestResponse**](CreateInboxAiSuggestResponse.md)

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

# **create_inbox_canned_respons**
> CreateInboxCannedResponsResponse create_inbox_canned_respons()

Create a canned response.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.create_inbox_canned_respons_response import CreateInboxCannedResponsResponse
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
    api_instance = inbox_api.InboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a canned response.
        api_response = api_instance.create_inbox_canned_respons()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->create_inbox_canned_respons: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInboxCannedResponsResponse**](CreateInboxCannedResponsResponse.md)

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

# **create_inbox_conversation_bulk**
> CreateInboxConversationBulkResponse create_inbox_conversation_bulk()

Bulk mark read / mark unread / soft-delete conversations.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.create_inbox_conversation_bulk_response import CreateInboxConversationBulkResponse
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
    api_instance = inbox_api.InboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk mark read / mark unread / soft-delete conversations.
        api_response = api_instance.create_inbox_conversation_bulk()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->create_inbox_conversation_bulk: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInboxConversationBulkResponse**](CreateInboxConversationBulkResponse.md)

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

# **create_inbox_conversation_bulk_ai_respond**
> CreateInboxConversationBulkAiRespondResponse create_inbox_conversation_bulk_ai_respond()

AI reply suggestion for multiple conversations — draft or send.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.create_inbox_conversation_bulk_ai_respond_response import CreateInboxConversationBulkAiRespondResponse
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
    api_instance = inbox_api.InboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # AI reply suggestion for multiple conversations — draft or send.
        api_response = api_instance.create_inbox_conversation_bulk_ai_respond()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->create_inbox_conversation_bulk_ai_respond: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateInboxConversationBulkAiRespondResponse**](CreateInboxConversationBulkAiRespondResponse.md)

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

# **create_inbox_conversation_offer_action**
> CreateInboxConversationOfferActionResponse create_inbox_conversation_offer_action(id)

Accept / counter / decline an active offer on a conversation.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.error import Error
from crossly.model.create_inbox_conversation_offer_action_response import CreateInboxConversationOfferActionResponse
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
    api_instance = inbox_api.InboxApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Accept / counter / decline an active offer on a conversation.
        api_response = api_instance.create_inbox_conversation_offer_action(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->create_inbox_conversation_offer_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**CreateInboxConversationOfferActionResponse**](CreateInboxConversationOfferActionResponse.md)

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

# **create_inbox_message_triage**
> CreateInboxMessageTriageResponse create_inbox_message_triage(id)

Manually re-triage a buyer message.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.create_inbox_message_triage_response import CreateInboxMessageTriageResponse
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
    api_instance = inbox_api.InboxApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Manually re-triage a buyer message.
        api_response = api_instance.create_inbox_message_triage(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->create_inbox_message_triage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**CreateInboxMessageTriageResponse**](CreateInboxMessageTriageResponse.md)

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

# **create_inbox_offer**
> CreateInboxOfferResponse create_inbox_offer(id)

Accept, counter, or decline an offer on a conversation.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.create_inbox_offer_response import CreateInboxOfferResponse
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
    api_instance = inbox_api.InboxApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Accept, counter, or decline an offer on a conversation.
        api_response = api_instance.create_inbox_offer(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->create_inbox_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**CreateInboxOfferResponse**](CreateInboxOfferResponse.md)

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

# **create_inbox_reply**
> CreateInboxReplyResponse create_inbox_reply(id)

Send a reply to a conversation thread.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.error import Error
from crossly.model.create_inbox_reply_response import CreateInboxReplyResponse
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
    api_instance = inbox_api.InboxApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Send a reply to a conversation thread.
        api_response = api_instance.create_inbox_reply(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->create_inbox_reply: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**CreateInboxReplyResponse**](CreateInboxReplyResponse.md)

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

# **delete_inbox_canned_respons**
> DeleteInboxCannedResponsResponse delete_inbox_canned_respons(id)

Delete a canned response.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.delete_inbox_canned_respons_response import DeleteInboxCannedResponsResponse
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
    api_instance = inbox_api.InboxApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a canned response.
        api_response = api_instance.delete_inbox_canned_respons(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->delete_inbox_canned_respons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DeleteInboxCannedResponsResponse**](DeleteInboxCannedResponsResponse.md)

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

# **get_inbox**
> GetInboxResponse get_inbox(id)

Get one conversation with its messages.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.error import Error
from crossly.model.get_inbox_response import GetInboxResponse
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
    api_instance = inbox_api.InboxApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get one conversation with its messages.
        api_response = api_instance.get_inbox(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->get_inbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**GetInboxResponse**](GetInboxResponse.md)

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

# **get_inbox_canned_respons**
> GetInboxCannedResponsResponse get_inbox_canned_respons()

List canned responses.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.error import Error
from crossly.model.get_inbox_canned_respons_response import GetInboxCannedResponsResponse
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
    api_instance = inbox_api.InboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List canned responses.
        api_response = api_instance.get_inbox_canned_respons()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->get_inbox_canned_respons: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInboxCannedResponsResponse**](GetInboxCannedResponsResponse.md)

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

# **get_inbox_conversation_message**
> GetInboxConversationMessageResponse get_inbox_conversation_message(id)

Paginated messages for a conversation.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.error import Error
from crossly.model.get_inbox_conversation_message_response import GetInboxConversationMessageResponse
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
    api_instance = inbox_api.InboxApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Paginated messages for a conversation.
        api_response = api_instance.get_inbox_conversation_message(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->get_inbox_conversation_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**GetInboxConversationMessageResponse**](GetInboxConversationMessageResponse.md)

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

# **get_inbox_conversation_unread_count**
> GetInboxConversationUnreadCountResponse get_inbox_conversation_unread_count()

Sidebar badge: unread conversation count.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.error import Error
from crossly.model.get_inbox_conversation_unread_count_response import GetInboxConversationUnreadCountResponse
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
    api_instance = inbox_api.InboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Sidebar badge: unread conversation count.
        api_response = api_instance.get_inbox_conversation_unread_count()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->get_inbox_conversation_unread_count: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInboxConversationUnreadCountResponse**](GetInboxConversationUnreadCountResponse.md)

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

# **list_inbox**
> bool, date, datetime, dict, float, int, list, str, none_type list_inbox()

List conversations.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.error import Error
from crossly.model.list_inbox_item import ListInboxItem
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
    api_instance = inbox_api.InboxApi(api_client)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    limit = 25 # int |  (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List conversations.
        api_response = api_instance.list_inbox(page=page, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->list_inbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 25

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

# **update_inbox_canned_respons**
> UpdateInboxCannedResponsResponse update_inbox_canned_respons(id)

Update a canned response.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.update_inbox_canned_respons_response import UpdateInboxCannedResponsResponse
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
    api_instance = inbox_api.InboxApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update a canned response.
        api_response = api_instance.update_inbox_canned_respons(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->update_inbox_canned_respons: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UpdateInboxCannedResponsResponse**](UpdateInboxCannedResponsResponse.md)

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

# **update_inbox_conversation**
> UpdateInboxConversationResponse update_inbox_conversation(id)

Mark read / change status / close conversation.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import inbox_api
from crossly.model.error import Error
from crossly.model.update_inbox_conversation_response import UpdateInboxConversationResponse
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
    api_instance = inbox_api.InboxApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Mark read / change status / close conversation.
        api_response = api_instance.update_inbox_conversation(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling InboxApi->update_inbox_conversation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UpdateInboxConversationResponse**](UpdateInboxConversationResponse.md)

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

