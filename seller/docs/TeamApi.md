# crossly.TeamApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team_accept**](TeamApi.md#create_team_accept) | **POST** /v1/team/accept | Accept a pending team invitation by raw token.
[**create_team_invite**](TeamApi.md#create_team_invite) | **POST** /v1/team/invite | Mint a team invitation; returns the one-time accept URL.
[**create_team_leave**](TeamApi.md#create_team_leave) | **POST** /v1/team/leave | Leave every team this user is currently a member of.
[**create_team_revoke**](TeamApi.md#create_team_revoke) | **POST** /v1/team/revoke | Revoke a pending invite OR an active team member.
[**get_team**](TeamApi.md#get_team) | **GET** /v1/team | List pending team invitations + active members.
[**update_team**](TeamApi.md#update_team) | **PATCH** /v1/team/{memberId} | Update a team member&#39;s scopes (owner only).


# **create_team_accept**
> CreateTeamAcceptResponse create_team_accept()

Accept a pending team invitation by raw token.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import team_api
from crossly.model.create_team_accept_response import CreateTeamAcceptResponse
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
    api_instance = team_api.TeamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Accept a pending team invitation by raw token.
        api_response = api_instance.create_team_accept()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TeamApi->create_team_accept: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateTeamAcceptResponse**](CreateTeamAcceptResponse.md)

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

# **create_team_invite**
> CreateTeamInviteResponse create_team_invite()

Mint a team invitation; returns the one-time accept URL.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import team_api
from crossly.model.create_team_invite_response import CreateTeamInviteResponse
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
    api_instance = team_api.TeamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Mint a team invitation; returns the one-time accept URL.
        api_response = api_instance.create_team_invite()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TeamApi->create_team_invite: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateTeamInviteResponse**](CreateTeamInviteResponse.md)

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

# **create_team_leave**
> CreateTeamLeaveResponse create_team_leave()

Leave every team this user is currently a member of.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import team_api
from crossly.model.error import Error
from crossly.model.create_team_leave_response import CreateTeamLeaveResponse
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
    api_instance = team_api.TeamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Leave every team this user is currently a member of.
        api_response = api_instance.create_team_leave()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TeamApi->create_team_leave: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateTeamLeaveResponse**](CreateTeamLeaveResponse.md)

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

# **create_team_revoke**
> CreateTeamRevokeResponse create_team_revoke()

Revoke a pending invite OR an active team member.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import team_api
from crossly.model.create_team_revoke_response import CreateTeamRevokeResponse
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
    api_instance = team_api.TeamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Revoke a pending invite OR an active team member.
        api_response = api_instance.create_team_revoke()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TeamApi->create_team_revoke: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateTeamRevokeResponse**](CreateTeamRevokeResponse.md)

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

# **get_team**
> GetTeamResponse get_team()

List pending team invitations + active members.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import team_api
from crossly.model.get_team_response import GetTeamResponse
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
    api_instance = team_api.TeamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List pending team invitations + active members.
        api_response = api_instance.get_team()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TeamApi->get_team: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetTeamResponse**](GetTeamResponse.md)

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

# **update_team**
> UpdateTeamResponse update_team(member_id)

Update a team member's scopes (owner only).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import team_api
from crossly.model.error import Error
from crossly.model.update_team_response import UpdateTeamResponse
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
    api_instance = team_api.TeamApi(api_client)
    member_id = "memberId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update a team member's scopes (owner only).
        api_response = api_instance.update_team(member_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TeamApi->update_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  |

### Return type

[**UpdateTeamResponse**](UpdateTeamResponse.md)

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

