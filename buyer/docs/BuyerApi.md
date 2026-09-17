# crossly_buyer.BuyerApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_buyer_activity**](BuyerApi.md#create_buyer_activity) | **POST** /v1/buyer/activity | Report an item your user is looking at, and get our answer.
[**create_buyer_cart_item**](BuyerApi.md#create_buyer_cart_item) | **POST** /v1/buyer/cart/items | Add a listing to your cart.
[**create_buyer_cart_quote**](BuyerApi.md#create_buyer_cart_quote) | **POST** /v1/buyer/cart/quote | Price the cart, delivered — item, shipping, tax, total.
[**create_buyer_offer**](BuyerApi.md#create_buyer_offer) | **POST** /v1/buyer/offers | Offer a price on a listing.
[**create_buyer_wishlist**](BuyerApi.md#create_buyer_wishlist) | **POST** /v1/buyer/wishlists | Create a wishlist.
[**create_buyer_wishlist_item**](BuyerApi.md#create_buyer_wishlist_item) | **POST** /v1/buyer/wishlists/{id}/items | Add a listing to a wishlist.
[**delete_buyer_cart_item**](BuyerApi.md#delete_buyer_cart_item) | **DELETE** /v1/buyer/cart/items/{id} | Remove a line from your cart.
[**get_buyer_preference**](BuyerApi.md#get_buyer_preference) | **GET** /v1/buyer/preferences | The shopping profile derived from that activity.
[**get_buyer_profile**](BuyerApi.md#get_buyer_profile) | **GET** /v1/buyer/profile | Your Crossly shopping profile — name, email, saved address, Bucks balance.
[**list_buyer_activity**](BuyerApi.md#list_buyer_activity) | **GET** /v1/buyer/activity | What this buyer has compared lately.
[**list_buyer_cart**](BuyerApi.md#list_buyer_cart) | **GET** /v1/buyer/cart | What is in your Crossly cart.
[**list_buyer_cashback**](BuyerApi.md#list_buyer_cashback) | **GET** /v1/buyer/cashback | Your Scout cashback — pending, confirmed, paid.
[**list_buyer_orders**](BuyerApi.md#list_buyer_orders) | **GET** /v1/buyer/orders | What you have bought on Crossly, newest first.
[**list_buyer_wishlist_items**](BuyerApi.md#list_buyer_wishlist_items) | **GET** /v1/buyer/wishlists/{id}/items | What is on one wishlist.
[**list_buyer_wishlists**](BuyerApi.md#list_buyer_wishlists) | **GET** /v1/buyer/wishlists | Your wishlists.


# **create_buyer_activity**
> CreateBuyerActivityResponse create_buyer_activity(inline_object4)

Report an item your user is looking at, and get our answer.

Records the look and returns whether Crossly has the item and at what price. Send an identifier and a store DOMAIN — a full URL is refused. Nothing about the page itself is stored.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.inline_object4 import InlineObject4
from crossly_buyer.model.create_buyer_activity_response import CreateBuyerActivityResponse
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)
    inline_object4 = InlineObject4(
        namespace="gtin",
        value="value_example",
        retail_host="retail_host_example",
        page_price_cents=0,
        page_currency="page_currency_example",
    ) # InlineObject4 | 

    # example passing only required values which don't have defaults set
    try:
        # Report an item your user is looking at, and get our answer.
        api_response = api_instance.create_buyer_activity(inline_object4)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->create_buyer_activity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  |

### Return type

[**CreateBuyerActivityResponse**](CreateBuyerActivityResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **create_buyer_cart_item**
> CreateBuyerCartItemResponse create_buyer_cart_item(inline_object2)

Add a listing to your cart.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.create_buyer_cart_item_response import CreateBuyerCartItemResponse
from crossly_buyer.model.inline_object2 import InlineObject2
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)
    inline_object2 = InlineObject2(
        listing_slug="listing_slug_example",
        quantity=1,
    ) # InlineObject2 | 

    # example passing only required values which don't have defaults set
    try:
        # Add a listing to your cart.
        api_response = api_instance.create_buyer_cart_item(inline_object2)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->create_buyer_cart_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  |

### Return type

[**CreateBuyerCartItemResponse**](CreateBuyerCartItemResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **create_buyer_cart_quote**
> CreateBuyerCartQuoteResponse create_buyer_cart_quote()

Price the cart, delivered — item, shipping, tax, total.

Runs the real checkout cascade and returns the totals instead of charging. Nothing is purchased. `taxComplete: false` means there is no saved delivery address, so the total is a floor rather than a final figure.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.create_buyer_cart_quote_response import CreateBuyerCartQuoteResponse
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Price the cart, delivered — item, shipping, tax, total.
        api_response = api_instance.create_buyer_cart_quote()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->create_buyer_cart_quote: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateBuyerCartQuoteResponse**](CreateBuyerCartQuoteResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_buyer_offer**
> CreateBuyerOfferResponse create_buyer_offer(inline_object3)

Offer a price on a listing.

Sends an offer to the seller. Spends nothing — a seller accepting still leaves you to complete checkout. Offers at or above the asking price are refused; buy it instead.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.create_buyer_offer_response import CreateBuyerOfferResponse
from crossly_buyer.model.inline_object3 import InlineObject3
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)
    inline_object3 = InlineObject3(
        listing_slug="listing_slug_example",
        amount_cents=100,
        message="message_example",
    ) # InlineObject3 | 

    # example passing only required values which don't have defaults set
    try:
        # Offer a price on a listing.
        api_response = api_instance.create_buyer_offer(inline_object3)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->create_buyer_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  |

### Return type

[**CreateBuyerOfferResponse**](CreateBuyerOfferResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **create_buyer_wishlist**
> CreateBuyerWishlistResponse create_buyer_wishlist(inline_object)

Create a wishlist.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.inline_object import InlineObject
from crossly_buyer.model.create_buyer_wishlist_response import CreateBuyerWishlistResponse
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)
    inline_object = InlineObject(
        name="name_example",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Create a wishlist.
        api_response = api_instance.create_buyer_wishlist(inline_object)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->create_buyer_wishlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

[**CreateBuyerWishlistResponse**](CreateBuyerWishlistResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **create_buyer_wishlist_item**
> CreateBuyerWishlistItemResponse create_buyer_wishlist_item(id, inline_object1)

Add a listing to a wishlist.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.inline_object1 import InlineObject1
from crossly_buyer.model.create_buyer_wishlist_item_response import CreateBuyerWishlistItemResponse
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)
    id = "id_example" # str | 
    inline_object1 = InlineObject1(
        listing_slug="listing_slug_example",
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Add a listing to a wishlist.
        api_response = api_instance.create_buyer_wishlist_item(id, inline_object1)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->create_buyer_wishlist_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

### Return type

[**CreateBuyerWishlistItemResponse**](CreateBuyerWishlistItemResponse.md)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

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

# **delete_buyer_cart_item**
> delete_buyer_cart_item(id)

Remove a line from your cart.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove a line from your cart.
        api_instance.delete_buyer_cart_item(id)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->delete_buyer_cart_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[BuyerOAuth](../README.md#BuyerOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content — the request succeeded and there is no body. |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buyer_preference**
> GetBuyerPreferenceResponse get_buyer_preference()

The shopping profile derived from that activity.

Derived, never declared — there is no preferences form anywhere. `matchRate` is the share of this person's searches Crossly could answer; a low number is an inventory problem, not a personalisation one, which is why it is here.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.error import Error
from crossly_buyer.model.get_buyer_preference_response import GetBuyerPreferenceResponse
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
    api_instance = buyer_api.BuyerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The shopping profile derived from that activity.
        api_response = api_instance.get_buyer_preference()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->get_buyer_preference: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBuyerPreferenceResponse**](GetBuyerPreferenceResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buyer_profile**
> GetBuyerProfileResponse get_buyer_profile()

Your Crossly shopping profile — name, email, saved address, Bucks balance.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.get_buyer_profile_response import GetBuyerProfileResponse
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your Crossly shopping profile — name, email, saved address, Bucks balance.
        api_response = api_instance.get_buyer_profile()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->get_buyer_profile: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBuyerProfileResponse**](GetBuyerProfileResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_activity**
> bool, date, datetime, dict, float, int, list, str, none_type list_buyer_activity()

What this buyer has compared lately.

Newest first, and only as far back as the retention window — the link between a person and a comparison is dropped after 180 days, so this thins out rather than growing forever.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.list_buyer_activity_item import ListBuyerActivityItem
from crossly_buyer.model.v1_list import V1List
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What this buyer has compared lately.
        api_response = api_instance.list_buyer_activity()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->list_buyer_activity: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_cart**
> bool, date, datetime, dict, float, int, list, str, none_type list_buyer_cart()

What is in your Crossly cart.

Line items with the price captured when each was added. This is NOT a quote — shipping, tax and any discounts are computed at checkout against a delivery address, and the sum of these lines is not what you will be charged.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.list_buyer_cart_item import ListBuyerCartItem
from crossly_buyer.model.v1_list import V1List
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What is in your Crossly cart.
        api_response = api_instance.list_buyer_cart()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->list_buyer_cart: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_cashback**
> bool, date, datetime, dict, float, int, list, str, none_type list_buyer_cashback()

Your Scout cashback — pending, confirmed, paid.

Newest first. `pending` means an order was reported and the retailer's return window has not closed; nothing is paid until it does. `expired` means a click was never reported as converting, which is the ordinary outcome for most clicks.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.list_buyer_cashback_item import ListBuyerCashbackItem
from crossly_buyer.model.v1_list import V1List
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)
    status = "pending" # str |  (optional)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    limit = 25 # int |  (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Your Scout cashback — pending, confirmed, paid.
        api_response = api_instance.list_buyer_cashback(status=status, page=page, limit=limit)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->list_buyer_cashback: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 25

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_orders**
> bool, date, datetime, dict, float, int, list, str, none_type list_buyer_orders()

What you have bought on Crossly, newest first.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.list_buyer_orders_item import ListBuyerOrdersItem
from crossly_buyer.model.v1_list import V1List
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    limit = 25 # int |  (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # What you have bought on Crossly, newest first.
        api_response = api_instance.list_buyer_orders(page=page, limit=limit)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->list_buyer_orders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 25

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_wishlist_items**
> bool, date, datetime, dict, float, int, list, str, none_type list_buyer_wishlist_items(id)

What is on one wishlist.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.list_buyer_wishlist_items_item import ListBuyerWishlistItemsItem
from crossly_buyer.model.v1_list import V1List
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # What is on one wishlist.
        api_response = api_instance.list_buyer_wishlist_items(id)
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->list_buyer_wishlist_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buyer_wishlists**
> bool, date, datetime, dict, float, int, list, str, none_type list_buyer_wishlists()

Your wishlists.

### Example

* Bearer Authentication (BuyerOAuth):

```python
import time
import crossly_buyer
from crossly_buyer.api import buyer_api
from crossly_buyer.model.list_buyer_wishlists_item import ListBuyerWishlistsItem
from crossly_buyer.model.v1_list import V1List
from crossly_buyer.model.error import Error
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
    api_instance = buyer_api.BuyerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your wishlists.
        api_response = api_instance.list_buyer_wishlists()
        pprint(api_response)
    except crossly_buyer.ApiException as e:
        print("Exception when calling BuyerApi->list_buyer_wishlists: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

