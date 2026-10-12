# crossly.DropsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_drop**](DropsApi.md#create_drop) | **POST** /v1/drops | Set up a drop: { title, listingIds (1-10 of your live Crossly listings), units (at most their stock), opensLineAt, releaseAt (ISO), eligibility: \&quot;signed_in\&quot; | \&quot;verified\&quot; }. The line opens at opensLineAt with a published seed commitment; the draw runs at releaseAt.
[**delete_drop**](DropsApi.md#delete_drop) | **DELETE** /v1/drops/{id} | Call a drop off before its line opens.
[**get_drop**](DropsApi.md#get_drop) | **GET** /v1/drops/{id} | A drop: its listings, units, times, eligibility, the sha256 seed commitment and the entry count. After release also the revealed seed, the sorted entry ids and the draw order (recompute it with drawWinners(seed, dropId, entryIds, units)).
[**list_drop_mine**](DropsApi.md#list_drop_mine) | **GET** /v1/drops/mine | Your drops, latest release first, with entries, winners, claims, the waitlist and expired holds.
[**list_street_drops**](DropsApi.md#list_street_drops) | **GET** /v1/streets/{slug}/drops | Upcoming, open and just-released drops on a Crossly World street, one per shop, soonest first, with the plot (or live stall spot) each line forms at.
[**update_drop**](DropsApi.md#update_drop) | **PATCH** /v1/drops/{id} | Change a drop before its line opens (any of the set-up fields).


# **create_drop**
> CreateDropResponse create_drop()

Set up a drop: { title, listingIds (1-10 of your live Crossly listings), units (at most their stock), opensLineAt, releaseAt (ISO), eligibility: \"signed_in\" | \"verified\" }. The line opens at opensLineAt with a published seed commitment; the draw runs at releaseAt.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import drops_api
from crossly.model.drop.create_drop_response import CreateDropResponse
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
    api_instance = drops_api.DropsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Set up a drop: { title, listingIds (1-10 of your live Crossly listings), units (at most their stock), opensLineAt, releaseAt (ISO), eligibility: \"signed_in\" | \"verified\" }. The line opens at opensLineAt with a published seed commitment; the draw runs at releaseAt.
        api_response = api_instance.create_drop()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DropsApi->create_drop: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateDropResponse**

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

# **delete_drop**
> DeleteDropResponse delete_drop(id)

Call a drop off before its line opens.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import drops_api
from crossly.model.common.error import Error
from crossly.model.drop.delete_drop_response import DeleteDropResponse
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
    api_instance = drops_api.DropsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Call a drop off before its line opens.
        api_response = api_instance.delete_drop(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DropsApi->delete_drop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteDropResponse**

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

# **get_drop**
> GetDropResponse get_drop(id)

A drop: its listings, units, times, eligibility, the sha256 seed commitment and the entry count. After release also the revealed seed, the sorted entry ids and the draw order (recompute it with drawWinners(seed, dropId, entryIds, units)).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import drops_api
from crossly.model.drop.get_drop_response import GetDropResponse
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
    api_instance = drops_api.DropsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A drop: its listings, units, times, eligibility, the sha256 seed commitment and the entry count. After release also the revealed seed, the sorted entry ids and the draw order (recompute it with drawWinners(seed, dropId, entryIds, units)).
        api_response = api_instance.get_drop(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DropsApi->get_drop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetDropResponse**

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

# **list_drop_mine**
> ListDropMineResponse list_drop_mine()

Your drops, latest release first, with entries, winners, claims, the waitlist and expired holds.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import drops_api
from crossly.model.drop.list_drop_mine_response import ListDropMineResponse
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
    api_instance = drops_api.DropsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your drops, latest release first, with entries, winners, claims, the waitlist and expired holds.
        api_response = api_instance.list_drop_mine()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DropsApi->list_drop_mine: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListDropMineResponse**

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

# **list_street_drops**
> ListStreetDropsResponse list_street_drops(slug)

Upcoming, open and just-released drops on a Crossly World street, one per shop, soonest first, with the plot (or live stall spot) each line forms at.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import drops_api
from crossly.model.common.error import Error
from crossly.model.street.list_street_drops_response import ListStreetDropsResponse
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
    api_instance = drops_api.DropsApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Upcoming, open and just-released drops on a Crossly World street, one per shop, soonest first, with the plot (or live stall spot) each line forms at.
        api_response = api_instance.list_street_drops(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DropsApi->list_street_drops: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**ListStreetDropsResponse**

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

# **update_drop**
> CreateDropResponse update_drop(id)

Change a drop before its line opens (any of the set-up fields).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import drops_api
from crossly.model.drop.create_drop_response import CreateDropResponse
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
    api_instance = drops_api.DropsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Change a drop before its line opens (any of the set-up fields).
        api_response = api_instance.update_drop(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DropsApi->update_drop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateDropResponse**

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

