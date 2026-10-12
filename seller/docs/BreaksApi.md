# crossly.BreaksApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_break**](BreaksApi.md#create_break) | **POST** /v1/breaks | Start a break on one of your listings: pick (buyers choose a spot) or random (drawn). The seed is committed now and revealed at the draw.
[**create_break_cancel**](BreaksApi.md#create_break_cancel) | **POST** /v1/breaks/{id}/cancel | Cancel a break before any spot is paid for; after that, refund those orders instead (409).
[**create_break_draw**](BreaksApi.md#create_break_draw) | **POST** /v1/breaks/{id}/draw | Draw a sold-out random break: assigns spots from the committed seed and reveals it.
[**create_break_opened**](BreaksApi.md#create_break_opened) | **POST** /v1/breaks/{id}/opened | Mark the product opened on stream.
[**create_break_spot_hit**](BreaksApi.md#create_break_spot_hit) | **POST** /v1/breaks/{id}/spots/{spotId}/hits | Record what a spot pulled.
[**get_break**](BreaksApi.md#get_break) | **GET** /v1/breaks/{id} | A break’s board with every spot, its buyer and its hits.
[**list_breaks**](BreaksApi.md#list_breaks) | **GET** /v1/breaks | Your card breaks, newest first.


# **create_break**
> CreateBreakResponse create_break()

Start a break on one of your listings: pick (buyers choose a spot) or random (drawn). The seed is committed now and revealed at the draw.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import breaks_api
from crossly.model.common.error import Error
from crossly.model.breaks.create_break_response import CreateBreakResponse
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
    api_instance = breaks_api.BreaksApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Start a break on one of your listings: pick (buyers choose a spot) or random (drawn). The seed is committed now and revealed at the draw.
        api_response = api_instance.create_break()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BreaksApi->create_break: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateBreakResponse**

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

# **create_break_cancel**
> CreateBreakCancelResponse create_break_cancel(id)

Cancel a break before any spot is paid for; after that, refund those orders instead (409).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import breaks_api
from crossly.model.common.error import Error
from crossly.model.breaks.create_break_cancel_response import CreateBreakCancelResponse
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
    api_instance = breaks_api.BreaksApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Cancel a break before any spot is paid for; after that, refund those orders instead (409).
        api_response = api_instance.create_break_cancel(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BreaksApi->create_break_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateBreakCancelResponse**

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

# **create_break_draw**
> CreateBreakDrawResponse create_break_draw(id)

Draw a sold-out random break: assigns spots from the committed seed and reveals it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import breaks_api
from crossly.model.breaks.create_break_draw_response import CreateBreakDrawResponse
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
    api_instance = breaks_api.BreaksApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Draw a sold-out random break: assigns spots from the committed seed and reveals it.
        api_response = api_instance.create_break_draw(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BreaksApi->create_break_draw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateBreakDrawResponse**

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

# **create_break_opened**
> CreateBreakCancelResponse create_break_opened(id)

Mark the product opened on stream.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import breaks_api
from crossly.model.common.error import Error
from crossly.model.breaks.create_break_cancel_response import CreateBreakCancelResponse
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
    api_instance = breaks_api.BreaksApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Mark the product opened on stream.
        api_response = api_instance.create_break_opened(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BreaksApi->create_break_opened: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateBreakCancelResponse**

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

# **create_break_spot_hit**
> CreateBreakCancelResponse create_break_spot_hit(id, spot_id)

Record what a spot pulled.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import breaks_api
from crossly.model.common.error import Error
from crossly.model.breaks.create_break_cancel_response import CreateBreakCancelResponse
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
    api_instance = breaks_api.BreaksApi(api_client)
    id = "id_example" # str | 
    spot_id = "spotId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Record what a spot pulled.
        api_response = api_instance.create_break_spot_hit(id, spot_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BreaksApi->create_break_spot_hit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **spot_id** | **str**|  |

### Return type

**CreateBreakCancelResponse**

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

# **get_break**
> GetBreakResponse get_break(id)

A break’s board with every spot, its buyer and its hits.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import breaks_api
from crossly.model.common.error import Error
from crossly.model.breaks.get_break_response import GetBreakResponse
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
    api_instance = breaks_api.BreaksApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A break’s board with every spot, its buyer and its hits.
        api_response = api_instance.get_break(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BreaksApi->get_break: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetBreakResponse**

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

# **list_breaks**
> ListBreaksResponse list_breaks()

Your card breaks, newest first.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import breaks_api
from crossly.model.breaks.list_breaks_response import ListBreaksResponse
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
    api_instance = breaks_api.BreaksApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your card breaks, newest first.
        api_response = api_instance.list_breaks()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BreaksApi->list_breaks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListBreaksResponse**

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

