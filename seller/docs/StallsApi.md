# crossly.StallsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stall_book**](StallsApi.md#create_stall_book) | **POST** /v1/stalls/book | Book and pay for a pop-up stall: { street, spotIndex, rail, unit: \&quot;day\&quot;, startDate, days } or { ..., unit: \&quot;event\&quot;, eventIds }, optional booth { canopy, pattern, lights, counter, piece } (premium values need holding; checked before paying). Paid up front; full-access token and Idempotency-Key required.
[**create_stall_booking_cancel**](StallsApi.md#create_stall_booking_cancel) | **POST** /v1/stalls/bookings/{id}/cancel | Cancel a stall before it opens: a full refund on the rail it was paid on. Final once it has opened.
[**get_stall_quote**](StallsApi.md#get_stall_quote) | **GET** /v1/stalls/quote | Quote a stall: street, spot, and either unit&#x3D;day with start (YYYY-MM-DD) and days, or unit&#x3D;event with events (comma-separated event ids). Returns the line items in cents, the rails the spot accepts and whether it is bookable.
[**list_stall_mine**](StallsApi.md#list_stall_mine) | **GET** /v1/stalls/mine | Your stall bookings, newest first, with visits, offers and sales while the stall was up.
[**list_street_events**](StallsApi.md#list_street_events) | **GET** /v1/streets/{slug}/events | Current and upcoming street events (Night Market, Swap Meet) on a street, soonest first.
[**list_street_stalls**](StallsApi.md#list_street_stalls) | **GET** /v1/streets/{slug}/stalls | Today&#39;s pop-up stalls on a street (each with its live listings, awning, sign and seller), plus the spots still free today. meta carries the street, the phase (day / night_market / swap_meet) and the free spots.
[**update_stall_booking**](StallsApi.md#update_stall_booking) | **PATCH** /v1/stalls/bookings/{id} | Change a booked stall before or while it is up: listingIds (up to 6 of your live listings), awning { colour, pattern }, booth { canopy, pattern, lights, counter, piece } (premium values need holding), sign, attendant.


# **create_stall_book**
> CreateStallBookResponse create_stall_book()

Book and pay for a pop-up stall: { street, spotIndex, rail, unit: \"day\", startDate, days } or { ..., unit: \"event\", eventIds }, optional booth { canopy, pattern, lights, counter, piece } (premium values need holding; checked before paying). Paid up front; full-access token and Idempotency-Key required.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import stalls_api
from crossly.model.common.error import Error
from crossly.model.stall.create_stall_book_response import CreateStallBookResponse
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
    api_instance = stalls_api.StallsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Book and pay for a pop-up stall: { street, spotIndex, rail, unit: \"day\", startDate, days } or { ..., unit: \"event\", eventIds }, optional booth { canopy, pattern, lights, counter, piece } (premium values need holding; checked before paying). Paid up front; full-access token and Idempotency-Key required.
        api_response = api_instance.create_stall_book()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling StallsApi->create_stall_book: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateStallBookResponse**

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

# **create_stall_booking_cancel**
> CreateStallBookingCancelResponse create_stall_booking_cancel(id)

Cancel a stall before it opens: a full refund on the rail it was paid on. Final once it has opened.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import stalls_api
from crossly.model.stall.create_stall_booking_cancel_response import CreateStallBookingCancelResponse
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
    api_instance = stalls_api.StallsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Cancel a stall before it opens: a full refund on the rail it was paid on. Final once it has opened.
        api_response = api_instance.create_stall_booking_cancel(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling StallsApi->create_stall_booking_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateStallBookingCancelResponse**

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

# **get_stall_quote**
> GetStallQuoteResponse get_stall_quote(street, spot)

Quote a stall: street, spot, and either unit=day with start (YYYY-MM-DD) and days, or unit=event with events (comma-separated event ids). Returns the line items in cents, the rails the spot accepts and whether it is bookable.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import stalls_api
from crossly.model.common.error import Error
from crossly.model.stall.get_stall_quote_response import GetStallQuoteResponse
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
    api_instance = stalls_api.StallsApi(api_client)
    street = "street_example" # str | 
    spot = 1 # int | 
    unit = "day" # str |  (optional)
    start = "start_example" # str | YYYY-MM-DD (unit=day). (optional)
    days = 1 # int | How many days (unit=day). (optional)
    events = "events_example" # str | Comma-separated street event ids (unit=event). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Quote a stall: street, spot, and either unit=day with start (YYYY-MM-DD) and days, or unit=event with events (comma-separated event ids). Returns the line items in cents, the rails the spot accepts and whether it is bookable.
        api_response = api_instance.get_stall_quote(street, spot)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling StallsApi->get_stall_quote: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Quote a stall: street, spot, and either unit=day with start (YYYY-MM-DD) and days, or unit=event with events (comma-separated event ids). Returns the line items in cents, the rails the spot accepts and whether it is bookable.
        api_response = api_instance.get_stall_quote(street, spot, unit=unit, start=start, days=days, events=events)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling StallsApi->get_stall_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **street** | **str**|  |
 **spot** | **int**|  |
 **unit** | **str**|  | [optional]
 **start** | **str**| YYYY-MM-DD (unit&#x3D;day). | [optional]
 **days** | **int**| How many days (unit&#x3D;day). | [optional]
 **events** | **str**| Comma-separated street event ids (unit&#x3D;event). | [optional]

### Return type

**GetStallQuoteResponse**

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

# **list_stall_mine**
> ListStallMineResponse list_stall_mine()

Your stall bookings, newest first, with visits, offers and sales while the stall was up.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import stalls_api
from crossly.model.stall.list_stall_mine_response import ListStallMineResponse
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
    api_instance = stalls_api.StallsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your stall bookings, newest first, with visits, offers and sales while the stall was up.
        api_response = api_instance.list_stall_mine()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling StallsApi->list_stall_mine: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListStallMineResponse**

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

# **list_street_events**
> ListStreetEventsResponse list_street_events(slug)

Current and upcoming street events (Night Market, Swap Meet) on a street, soonest first.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import stalls_api
from crossly.model.common.error import Error
from crossly.model.street.list_street_events_response import ListStreetEventsResponse
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
    api_instance = stalls_api.StallsApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Current and upcoming street events (Night Market, Swap Meet) on a street, soonest first.
        api_response = api_instance.list_street_events(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling StallsApi->list_street_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListStreetEventsResponse**

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

# **list_street_stalls**
> ListStreetStallsResponse list_street_stalls(slug)

Today's pop-up stalls on a street (each with its live listings, awning, sign and seller), plus the spots still free today. meta carries the street, the phase (day / night_market / swap_meet) and the free spots.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import stalls_api
from crossly.model.street.list_street_stalls_response import ListStreetStallsResponse
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
    api_instance = stalls_api.StallsApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Today's pop-up stalls on a street (each with its live listings, awning, sign and seller), plus the spots still free today. meta carries the street, the phase (day / night_market / swap_meet) and the free spots.
        api_response = api_instance.list_street_stalls(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling StallsApi->list_street_stalls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListStreetStallsResponse**

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

# **update_stall_booking**
> CreateStallBookResponse update_stall_booking(id)

Change a booked stall before or while it is up: listingIds (up to 6 of your live listings), awning { colour, pattern }, booth { canopy, pattern, lights, counter, piece } (premium values need holding), sign, attendant.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import stalls_api
from crossly.model.common.error import Error
from crossly.model.stall.create_stall_book_response import CreateStallBookResponse
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
    api_instance = stalls_api.StallsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Change a booked stall before or while it is up: listingIds (up to 6 of your live listings), awning { colour, pattern }, booth { canopy, pattern, lights, counter, piece } (premium values need holding), sign, attendant.
        api_response = api_instance.update_stall_booking(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling StallsApi->update_stall_booking: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateStallBookResponse**

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

