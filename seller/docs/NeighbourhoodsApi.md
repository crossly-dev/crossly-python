# crossly.NeighbourhoodsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_neighbourhood**](NeighbourhoodsApi.md#get_neighbourhood) | **GET** /v1/neighbourhoods/{slug} | One neighbourhood street by slug.
[**list_neighbourhoods**](NeighbourhoodsApi.md#list_neighbourhoods) | **GET** /v1/neighbourhoods | Every neighbourhood street (Sneaker Row, Card District, Vintage Alley, Vinyl Lane): open or \&quot;opening soon\&quot; (6 shops + open stalls, or a live street event), shops, stalls today, the next street event and its /c/&lt;slug&gt; URL.


# **get_neighbourhood**
> GetNeighbourhoodResponse get_neighbourhood(slug)

One neighbourhood street by slug.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import neighbourhoods_api
from crossly.model.common.get_neighbourhood_response import GetNeighbourhoodResponse
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
    api_instance = neighbourhoods_api.NeighbourhoodsApi(api_client)
    slug = "sneaker-row" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One neighbourhood street by slug.
        api_response = api_instance.get_neighbourhood(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NeighbourhoodsApi->get_neighbourhood: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**GetNeighbourhoodResponse**

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

# **list_neighbourhoods**
> ListNeighbourhoodsResponse list_neighbourhoods()

Every neighbourhood street (Sneaker Row, Card District, Vintage Alley, Vinyl Lane): open or \"opening soon\" (6 shops + open stalls, or a live street event), shops, stalls today, the next street event and its /c/<slug> URL.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import neighbourhoods_api
from crossly.model.common.list_neighbourhoods_response import ListNeighbourhoodsResponse
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
    api_instance = neighbourhoods_api.NeighbourhoodsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Every neighbourhood street (Sneaker Row, Card District, Vintage Alley, Vinyl Lane): open or \"opening soon\" (6 shops + open stalls, or a live street event), shops, stalls today, the next street event and its /c/<slug> URL.
        api_response = api_instance.list_neighbourhoods()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NeighbourhoodsApi->list_neighbourhoods: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListNeighbourhoodsResponse**

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

