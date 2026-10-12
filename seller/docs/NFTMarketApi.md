# crossly.NFTMarketApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nft_market_external_resale**](NFTMarketApi.md#create_nft_market_external_resale) | **POST** /v1/nft-market/external-resale | Ops: record a Crossly NFT resold on ANY marketplace — maps mint → design and funds the pot. Admin PAT only.
[**create_nft_market_listing**](NFTMarketApi.md#create_nft_market_listing) | **POST** /v1/nft-market/listings | List an NFT you own for resale on the Crossly marketplace.
[**create_nft_market_listing_cancel**](NFTMarketApi.md#create_nft_market_listing_cancel) | **POST** /v1/nft-market/listings/{id}/cancel | Cancel one of your open NFT listings.
[**create_nft_market_listing_confirm_sale**](NFTMarketApi.md#create_nft_market_listing_confirm_sale) | **POST** /v1/nft-market/listings/{id}/confirm-sale | Ops: record a finalized on-Crossly NFT sale (verifies the royalty landed, funds the pot). Admin PAT only.
[**get_nft_market_listing**](NFTMarketApi.md#get_nft_market_listing) | **GET** /v1/nft-market/listings | Browse open on-platform NFT listings (Crossly cosmetics for resale in CBX/SOL).


# **create_nft_market_external_resale**
> CreateNftMarketExternalResaleResponse create_nft_market_external_resale()

Ops: record a Crossly NFT resold on ANY marketplace — maps mint → design and funds the pot. Admin PAT only.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import nft_market_api
from crossly.model.common.create_nft_market_external_resale_response import CreateNftMarketExternalResaleResponse
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
    api_instance = nft_market_api.NFTMarketApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Ops: record a Crossly NFT resold on ANY marketplace — maps mint → design and funds the pot. Admin PAT only.
        api_response = api_instance.create_nft_market_external_resale()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NFTMarketApi->create_nft_market_external_resale: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateNftMarketExternalResaleResponse**

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

# **create_nft_market_listing**
> CreateNftMarketListingResponse create_nft_market_listing()

List an NFT you own for resale on the Crossly marketplace.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import nft_market_api
from crossly.model.common.error import Error
from crossly.model.common.create_nft_market_listing_response import CreateNftMarketListingResponse
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
    api_instance = nft_market_api.NFTMarketApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List an NFT you own for resale on the Crossly marketplace.
        api_response = api_instance.create_nft_market_listing()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NFTMarketApi->create_nft_market_listing: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateNftMarketListingResponse**

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

# **create_nft_market_listing_cancel**
> OkResponse create_nft_market_listing_cancel(id)

Cancel one of your open NFT listings.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import nft_market_api
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
    api_instance = nft_market_api.NFTMarketApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Cancel one of your open NFT listings.
        api_response = api_instance.create_nft_market_listing_cancel(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NFTMarketApi->create_nft_market_listing_cancel: %s\n" % e)
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

# **create_nft_market_listing_confirm_sale**
> OkResponse create_nft_market_listing_confirm_sale(id)

Ops: record a finalized on-Crossly NFT sale (verifies the royalty landed, funds the pot). Admin PAT only.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import nft_market_api
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
    api_instance = nft_market_api.NFTMarketApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Ops: record a finalized on-Crossly NFT sale (verifies the royalty landed, funds the pot). Admin PAT only.
        api_response = api_instance.create_nft_market_listing_confirm_sale(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NFTMarketApi->create_nft_market_listing_confirm_sale: %s\n" % e)
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

# **get_nft_market_listing**
> GetNftMarketListingResponse get_nft_market_listing()

Browse open on-platform NFT listings (Crossly cosmetics for resale in CBX/SOL).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import nft_market_api
from crossly.model.common.error import Error
from crossly.model.common.get_nft_market_listing_response import GetNftMarketListingResponse
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
    api_instance = nft_market_api.NFTMarketApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Browse open on-platform NFT listings (Crossly cosmetics for resale in CBX/SOL).
        api_response = api_instance.get_nft_market_listing()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling NFTMarketApi->get_nft_market_listing: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetNftMarketListingResponse**

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

