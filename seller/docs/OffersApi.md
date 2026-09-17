# crossly.OffersApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_offer_respond**](OffersApi.md#create_offer_respond) | **POST** /v1/offers/{id}/respond | Accept, decline, or counter a buyer offer on a Crossly marketplace listing.
[**get_offer**](OffersApi.md#get_offer) | **GET** /v1/offers | List buyer offers on your Crossly marketplace listings, including bundles.


# **create_offer_respond**
> CreateOfferRespondResponse create_offer_respond(id, inline_object2)

Accept, decline, or counter a buyer offer on a Crossly marketplace listing.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import offers_api
from crossly.model.inline_object2 import InlineObject2
from crossly.model.error import Error
from crossly.model.create_offer_respond_response import CreateOfferRespondResponse
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
    api_instance = offers_api.OffersApi(api_client)
    id = "id_example" # str | Offer UUID.
    inline_object2 = InlineObject2(
        action="accept",
        counter_cents=1,
    ) # InlineObject2 | 

    # example passing only required values which don't have defaults set
    try:
        # Accept, decline, or counter a buyer offer on a Crossly marketplace listing.
        api_response = api_instance.create_offer_respond(id, inline_object2)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling OffersApi->create_offer_respond: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Offer UUID. |
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  |

### Return type

[**CreateOfferRespondResponse**](CreateOfferRespondResponse.md)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

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

# **get_offer**
> GetOfferResponse get_offer()

List buyer offers on your Crossly marketplace listings, including bundles.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import offers_api
from crossly.model.error import Error
from crossly.model.get_offer_response import GetOfferResponse
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
    api_instance = offers_api.OffersApi(api_client)
    status = "pending" # str | Filter to one status. Omit for all. (optional)
    limit = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List buyer offers on your Crossly marketplace listings, including bundles.
        api_response = api_instance.get_offer(status=status, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling OffersApi->get_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter to one status. Omit for all. | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

[**GetOfferResponse**](GetOfferResponse.md)

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

