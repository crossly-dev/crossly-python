# crossly.WorldsRewardsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_world_experience_reward_close**](WorldsRewardsApi.md#create_world_experience_reward_close) | **POST** /v1/worlds/experiences/{experienceId}/rewards/close | Close the pool: the unspent balance returns to your Crossly Carnival earnings. Free rewards keep working.
[**create_world_experience_reward_definition**](WorldsRewardsApi.md#create_world_experience_reward_definition) | **POST** /v1/worlds/experiences/{experienceId}/rewards/definitions | Add a reward scripts can grant: pin, emote, decor, item (your own COSM design), cosm or cbx (with an amount).
[**create_world_experience_reward_deposit**](WorldsRewardsApi.md#create_world_experience_reward_deposit) | **POST** /v1/worlds/experiences/{experienceId}/rewards/deposits | Move available Crossly Carnival earnings into the pool ($1-$10,000). Owner only; idempotent on idempotencyKey.
[**create_world_experience_reward_topup**](WorldsRewardsApi.md#create_world_experience_reward_topup) | **POST** /v1/worlds/experiences/{experienceId}/rewards/topups | Open a card top-up ($5-$10,000 into the pool; the 2.9% + 30¢ card fee is added on top). Returns checkoutUrl, where the owner pays with Crossly checkout; the pool is credited once when the payment lands. Owner only.
[**create_world_reward_topup_cancel**](WorldsRewardsApi.md#create_world_reward_topup_cancel) | **POST** /v1/worlds/rewards/topups/{topupId}/cancel | Cancel an unpaid top-up sheet.
[**get_world_experience_reward**](WorldsRewardsApi.md#get_world_experience_reward) | **GET** /v1/worlds/experiences/{experienceId}/rewards | The funded reward pool: balance, reserved (owed) value, caps, today&#39;s grants, the reward catalogue and the published rates.
[**get_world_reward_topup**](WorldsRewardsApi.md#get_world_reward_topup) | **GET** /v1/worlds/rewards/topups/{topupId} | One card top-up: its status (open, paying, paid, cancelled, expired, refused), amounts and the pool it funds.
[**list_world_experience_reward_grants**](WorldsRewardsApi.md#list_world_experience_reward_grants) | **GET** /v1/worlds/experiences/{experienceId}/rewards/grants | Every grant, newest first: reward, player sub, amount, cost, status. Cursor-paged; ?sub&#x3D; for one player.
[**list_world_experience_reward_ledger**](WorldsRewardsApi.md#list_world_experience_reward_ledger) | **GET** /v1/worlds/experiences/{experienceId}/rewards/ledger | The pool&#39;s own ledger: deposits, grant draw-downs, refunds. Cursor-paged.
[**list_world_experience_reward_topups**](WorldsRewardsApi.md#list_world_experience_reward_topups) | **GET** /v1/worlds/experiences/{experienceId}/rewards/topups | Card top-ups of the reward pool, newest first: amount into the pool, card fee, status, what went back to the card.
[**update_world_experience_reward_definition**](WorldsRewardsApi.md#update_world_experience_reward_definition) | **PATCH** /v1/worlds/experiences/{experienceId}/rewards/definitions/{rewardId} | Edit a reward: name, description, image, amount, per-player daily cap, on/off. Key and kind never change.
[**update_world_experience_reward_pool**](WorldsRewardsApi.md#update_world_experience_reward_pool) | **PATCH** /v1/worlds/experiences/{experienceId}/rewards/pool | Set the pool&#39;s daily caps: total value per day, value and grant count per player per day.


# **create_world_experience_reward_close**
> CreateWorldExperienceRewardCloseResponse create_world_experience_reward_close(experience_id)

Close the pool: the unspent balance returns to your Crossly Carnival earnings. Free rewards keep working.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.world.create_world_experience_reward_close_response import CreateWorldExperienceRewardCloseResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Close the pool: the unspent balance returns to your Crossly Carnival earnings. Free rewards keep working.
        api_response = api_instance.create_world_experience_reward_close(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->create_world_experience_reward_close: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**CreateWorldExperienceRewardCloseResponse**

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

# **create_world_experience_reward_definition**
> CreateWorldExperienceRewardDefinitionResponse create_world_experience_reward_definition(experience_id)

Add a reward scripts can grant: pin, emote, decor, item (your own COSM design), cosm or cbx (with an amount).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.world.create_world_experience_reward_definition_response import CreateWorldExperienceRewardDefinitionResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Add a reward scripts can grant: pin, emote, decor, item (your own COSM design), cosm or cbx (with an amount).
        api_response = api_instance.create_world_experience_reward_definition(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->create_world_experience_reward_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**CreateWorldExperienceRewardDefinitionResponse**

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

# **create_world_experience_reward_deposit**
> CreateWorldExperienceRewardDepositResponse create_world_experience_reward_deposit(experience_id)

Move available Crossly Carnival earnings into the pool ($1-$10,000). Owner only; idempotent on idempotencyKey.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_experience_reward_deposit_response import CreateWorldExperienceRewardDepositResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Move available Crossly Carnival earnings into the pool ($1-$10,000). Owner only; idempotent on idempotencyKey.
        api_response = api_instance.create_world_experience_reward_deposit(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->create_world_experience_reward_deposit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**CreateWorldExperienceRewardDepositResponse**

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

# **create_world_experience_reward_topup**
> CreateWorldExperienceRewardTopupResponse create_world_experience_reward_topup(experience_id)

Open a card top-up ($5-$10,000 into the pool; the 2.9% + 30¢ card fee is added on top). Returns checkoutUrl, where the owner pays with Crossly checkout; the pool is credited once when the payment lands. Owner only.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_experience_reward_topup_response import CreateWorldExperienceRewardTopupResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Open a card top-up ($5-$10,000 into the pool; the 2.9% + 30¢ card fee is added on top). Returns checkoutUrl, where the owner pays with Crossly checkout; the pool is credited once when the payment lands. Owner only.
        api_response = api_instance.create_world_experience_reward_topup(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->create_world_experience_reward_topup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**CreateWorldExperienceRewardTopupResponse**

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

# **create_world_reward_topup_cancel**
> CreateWorldSpaceJoinResponse create_world_reward_topup_cancel(topup_id)

Cancel an unpaid top-up sheet.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.world.create_world_space_join_response import CreateWorldSpaceJoinResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    topup_id = "topupId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Cancel an unpaid top-up sheet.
        api_response = api_instance.create_world_reward_topup_cancel(topup_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->create_world_reward_topup_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topup_id** | **str**|  |

### Return type

**CreateWorldSpaceJoinResponse**

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

# **get_world_experience_reward**
> GetWorldExperienceRewardResponse get_world_experience_reward(experience_id)

The funded reward pool: balance, reserved (owed) value, caps, today's grants, the reward catalogue and the published rates.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.world.get_world_experience_reward_response import GetWorldExperienceRewardResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The funded reward pool: balance, reserved (owed) value, caps, today's grants, the reward catalogue and the published rates.
        api_response = api_instance.get_world_experience_reward(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->get_world_experience_reward: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**GetWorldExperienceRewardResponse**

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

# **get_world_reward_topup**
> GetWorldRewardTopupResponse get_world_reward_topup(topup_id)

One card top-up: its status (open, paying, paid, cancelled, expired, refused), amounts and the pool it funds.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_reward_topup_response import GetWorldRewardTopupResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    topup_id = "topupId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One card top-up: its status (open, paying, paid, cancelled, expired, refused), amounts and the pool it funds.
        api_response = api_instance.get_world_reward_topup(topup_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->get_world_reward_topup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topup_id** | **str**|  |

### Return type

**GetWorldRewardTopupResponse**

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

# **list_world_experience_reward_grants**
> ListWorldExperienceRewardGrantsResponse list_world_experience_reward_grants(experience_id)

Every grant, newest first: reward, player sub, amount, cost, status. Cursor-paged; ?sub= for one player.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.world.list_world_experience_reward_grants_response import ListWorldExperienceRewardGrantsResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Every grant, newest first: reward, player sub, amount, cost, status. Cursor-paged; ?sub= for one player.
        api_response = api_instance.list_world_experience_reward_grants(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->list_world_experience_reward_grants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**ListWorldExperienceRewardGrantsResponse**

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

# **list_world_experience_reward_ledger**
> ListWorldExperienceRewardLedgerResponse list_world_experience_reward_ledger(experience_id)

The pool's own ledger: deposits, grant draw-downs, refunds. Cursor-paged.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_experience_reward_ledger_response import ListWorldExperienceRewardLedgerResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The pool's own ledger: deposits, grant draw-downs, refunds. Cursor-paged.
        api_response = api_instance.list_world_experience_reward_ledger(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->list_world_experience_reward_ledger: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**ListWorldExperienceRewardLedgerResponse**

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

# **list_world_experience_reward_topups**
> ListWorldExperienceRewardTopupsResponse list_world_experience_reward_topups(experience_id)

Card top-ups of the reward pool, newest first: amount into the pool, card fee, status, what went back to the card.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_experience_reward_topups_response import ListWorldExperienceRewardTopupsResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Card top-ups of the reward pool, newest first: amount into the pool, card fee, status, what went back to the card.
        api_response = api_instance.list_world_experience_reward_topups(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->list_world_experience_reward_topups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**ListWorldExperienceRewardTopupsResponse**

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

# **update_world_experience_reward_definition**
> CreateWorldExperienceRewardDefinitionResponse update_world_experience_reward_definition(experience_id, reward_id)

Edit a reward: name, description, image, amount, per-player daily cap, on/off. Key and kind never change.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.world.create_world_experience_reward_definition_response import CreateWorldExperienceRewardDefinitionResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    experience_id = "experienceId_example" # str | 
    reward_id = "rewardId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Edit a reward: name, description, image, amount, per-player daily cap, on/off. Key and kind never change.
        api_response = api_instance.update_world_experience_reward_definition(experience_id, reward_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->update_world_experience_reward_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **reward_id** | **str**|  |

### Return type

**CreateWorldExperienceRewardDefinitionResponse**

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

# **update_world_experience_reward_pool**
> UpdateWorldExperienceRewardPoolResponse update_world_experience_reward_pool(experience_id)

Set the pool's daily caps: total value per day, value and grant count per player per day.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_rewards_api
from crossly.model.common.error import Error
from crossly.model.world.update_world_experience_reward_pool_response import UpdateWorldExperienceRewardPoolResponse
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
    api_instance = worlds_rewards_api.WorldsRewardsApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set the pool's daily caps: total value per day, value and grant count per player per day.
        api_response = api_instance.update_world_experience_reward_pool(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsRewardsApi->update_world_experience_reward_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**UpdateWorldExperienceRewardPoolResponse**

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

