# crossly.TradeBlockApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trade_block_evolution_claim**](TradeBlockApi.md#create_trade_block_evolution_claim) | **POST** /v1/trade-block/evolutions/{id}/claim | Burn COSM and mint the evolved (or set-master) NFT for one of your unlocks.
[**create_trade_block_evolution_recipe**](TradeBlockApi.md#create_trade_block_evolution_recipe) | **POST** /v1/trade-block/evolution-recipes | Author a Trade Evolution recipe (a graded item or pair that, when swapped, unlocks a cosmetic you designed). Born unreviewed until ops approves.
[**create_trade_block_offer_respond**](TradeBlockApi.md#create_trade_block_offer_respond) | **POST** /v1/trade-block/offers/{id}/respond | Accept, decline, counter, or withdraw a Trade Block offer.
[**create_trade_block_post_close**](TradeBlockApi.md#create_trade_block_post_close) | **POST** /v1/trade-block/posts/{id}/close | Close one of your posts so it stops taking offers.
[**create_trade_block_post_offer**](TradeBlockApi.md#create_trade_block_post_offer) | **POST** /v1/trade-block/posts/{id}/offers | Respond to a post with a concrete swap: items on each side (0..N), optional cash.
[**create_trade_block_set_recipe**](TradeBlockApi.md#create_trade_block_set_recipe) | **POST** /v1/trade-block/set-recipes | Author a set-completion recipe (a set of items that, once assembled through trading, unlocks a set-master cosmetic you designed). Born unreviewed until ops approves.
[**get_trade_block_evolution**](TradeBlockApi.md#get_trade_block_evolution) | **GET** /v1/trade-block/evolutions | List your Trade Evolution unlocks — completed swaps that unlocked an evolved or set-master NFT you can mint by burning COSM.
[**get_trade_block_post**](TradeBlockApi.md#get_trade_block_post) | **GET** /v1/trade-block/posts | Browse open Trade Block posts (wants + offers) on the Crossly Market.
[**get_trade_block_post_by_id**](TradeBlockApi.md#get_trade_block_post_by_id) | **GET** /v1/trade-block/posts/{id} | Get one Trade Block post with its items and open-offer count.
[**get_trade_block_trade**](TradeBlockApi.md#get_trade_block_trade) | **GET** /v1/trade-block/trades | List the trades you are a party to, newest first.


# **create_trade_block_evolution_claim**
> CreateTradeBlockEvolutionClaimResponse create_trade_block_evolution_claim(id)

Burn COSM and mint the evolved (or set-master) NFT for one of your unlocks.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import trade_block_api
from crossly.model.trade.create_trade_block_evolution_claim_response import CreateTradeBlockEvolutionClaimResponse
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
    api_instance = trade_block_api.TradeBlockApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Burn COSM and mint the evolved (or set-master) NFT for one of your unlocks.
        api_response = api_instance.create_trade_block_evolution_claim(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TradeBlockApi->create_trade_block_evolution_claim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateTradeBlockEvolutionClaimResponse**

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

# **create_trade_block_evolution_recipe**
> CreateTradeBlockEvolutionRecipeResponse create_trade_block_evolution_recipe()

Author a Trade Evolution recipe (a graded item or pair that, when swapped, unlocks a cosmetic you designed). Born unreviewed until ops approves.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import trade_block_api
from crossly.model.trade.create_trade_block_evolution_recipe_response import CreateTradeBlockEvolutionRecipeResponse
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
    api_instance = trade_block_api.TradeBlockApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Author a Trade Evolution recipe (a graded item or pair that, when swapped, unlocks a cosmetic you designed). Born unreviewed until ops approves.
        api_response = api_instance.create_trade_block_evolution_recipe()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TradeBlockApi->create_trade_block_evolution_recipe: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateTradeBlockEvolutionRecipeResponse**

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

# **create_trade_block_offer_respond**
> CreateTradeBlockOfferRespondResponse create_trade_block_offer_respond(id)

Accept, decline, counter, or withdraw a Trade Block offer.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import trade_block_api
from crossly.model.common.error import Error
from crossly.model.trade.create_trade_block_offer_respond_response import CreateTradeBlockOfferRespondResponse
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
    api_instance = trade_block_api.TradeBlockApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Accept, decline, counter, or withdraw a Trade Block offer.
        api_response = api_instance.create_trade_block_offer_respond(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TradeBlockApi->create_trade_block_offer_respond: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateTradeBlockOfferRespondResponse**

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

# **create_trade_block_post_close**
> OkResponse create_trade_block_post_close(id)

Close one of your posts so it stops taking offers.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import trade_block_api
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
    api_instance = trade_block_api.TradeBlockApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Close one of your posts so it stops taking offers.
        api_response = api_instance.create_trade_block_post_close(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TradeBlockApi->create_trade_block_post_close: %s\n" % e)
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

# **create_trade_block_post_offer**
> IdResponse create_trade_block_post_offer(id)

Respond to a post with a concrete swap: items on each side (0..N), optional cash.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import trade_block_api
from crossly.model.common.id_response import IdResponse
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
    api_instance = trade_block_api.TradeBlockApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Respond to a post with a concrete swap: items on each side (0..N), optional cash.
        api_response = api_instance.create_trade_block_post_offer(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TradeBlockApi->create_trade_block_post_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**IdResponse**

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

# **create_trade_block_set_recipe**
> CreateTradeBlockSetRecipeResponse create_trade_block_set_recipe()

Author a set-completion recipe (a set of items that, once assembled through trading, unlocks a set-master cosmetic you designed). Born unreviewed until ops approves.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import trade_block_api
from crossly.model.common.error import Error
from crossly.model.trade.create_trade_block_set_recipe_response import CreateTradeBlockSetRecipeResponse
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
    api_instance = trade_block_api.TradeBlockApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Author a set-completion recipe (a set of items that, once assembled through trading, unlocks a set-master cosmetic you designed). Born unreviewed until ops approves.
        api_response = api_instance.create_trade_block_set_recipe()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TradeBlockApi->create_trade_block_set_recipe: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateTradeBlockSetRecipeResponse**

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

# **get_trade_block_evolution**
> GetTradeBlockEvolutionResponse get_trade_block_evolution()

List your Trade Evolution unlocks — completed swaps that unlocked an evolved or set-master NFT you can mint by burning COSM.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import trade_block_api
from crossly.model.trade.get_trade_block_evolution_response import GetTradeBlockEvolutionResponse
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
    api_instance = trade_block_api.TradeBlockApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List your Trade Evolution unlocks — completed swaps that unlocked an evolved or set-master NFT you can mint by burning COSM.
        api_response = api_instance.get_trade_block_evolution()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TradeBlockApi->get_trade_block_evolution: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetTradeBlockEvolutionResponse**

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

# **get_trade_block_post**
> GetTradeBlockPostResponse get_trade_block_post()

Browse open Trade Block posts (wants + offers) on the Crossly Market.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import trade_block_api
from crossly.model.common.error import Error
from crossly.model.trade.get_trade_block_post_response import GetTradeBlockPostResponse
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
    api_instance = trade_block_api.TradeBlockApi(api_client)
    kind = "want" # str | Filter to wants or offers. (optional)
    category_slug = "categorySlug_example" # str | Filter to a market category. (optional)
    brand = "brand_example" # str | Filter to posts with a product of this brand (case-insensitive). (optional)
    model = "model_example" # str | Filter to posts with a product of this catalogue model (case-insensitive). (optional)
    q = "q_example" # str | Search title + want text. (optional)
    limit = 40 # int |  (optional) if omitted the server will use the default value of 40
    offset = 0 # int |  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Browse open Trade Block posts (wants + offers) on the Crossly Market.
        api_response = api_instance.get_trade_block_post(kind=kind, category_slug=category_slug, brand=brand, model=model, q=q, limit=limit, offset=offset)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TradeBlockApi->get_trade_block_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**| Filter to wants or offers. | [optional]
 **category_slug** | **str**| Filter to a market category. | [optional]
 **brand** | **str**| Filter to posts with a product of this brand (case-insensitive). | [optional]
 **model** | **str**| Filter to posts with a product of this catalogue model (case-insensitive). | [optional]
 **q** | **str**| Search title + want text. | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 40
 **offset** | **int**|  | [optional] if omitted the server will use the default value of 0

### Return type

**GetTradeBlockPostResponse**

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

# **get_trade_block_post_by_id**
> GetTradeBlockPostByIdResponse get_trade_block_post_by_id(id)

Get one Trade Block post with its items and open-offer count.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import trade_block_api
from crossly.model.common.error import Error
from crossly.model.trade.get_trade_block_post_by_id_response import GetTradeBlockPostByIdResponse
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
    api_instance = trade_block_api.TradeBlockApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get one Trade Block post with its items and open-offer count.
        api_response = api_instance.get_trade_block_post_by_id(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TradeBlockApi->get_trade_block_post_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetTradeBlockPostByIdResponse**

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

# **get_trade_block_trade**
> GetTradeBlockTradeResponse get_trade_block_trade()

List the trades you are a party to, newest first.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import trade_block_api
from crossly.model.common.error import Error
from crossly.model.trade.get_trade_block_trade_response import GetTradeBlockTradeResponse
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
    api_instance = trade_block_api.TradeBlockApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the trades you are a party to, newest first.
        api_response = api_instance.get_trade_block_trade()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TradeBlockApi->get_trade_block_trade: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetTradeBlockTradeResponse**

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

