# crossly.CrosslyWalletApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tcg_nft_reconcile**](CrosslyWalletApi.md#create_tcg_nft_reconcile) | **POST** /v1/tcg/nfts/reconcile | Re-read your wallets on chain so your card counts follow what you hold (cards you moved away leave; cards you received join).
[**create_wallet_crossly**](CrosslyWalletApi.md#create_wallet_crossly) | **POST** /v1/wallet/crossly | Create your Crossly wallet now (it is otherwise created for you in the background). Idempotent.
[**get_wallet_crossly**](CrosslyWalletApi.md#get_wallet_crossly) | **GET** /v1/wallet/crossly | Your Crossly wallet (self-custody Solana): status, address, whether it is configured, and your card NFT counts by status.
[**list_tcg_nfts**](CrosslyWalletApi.md#list_tcg_nfts) | **GET** /v1/tcg/{game}/nfts | Your card NFTs for a Crossly TCG game: each copy, its mint status, asset id and whether it is soulbound (starter).


# **create_tcg_nft_reconcile**
> CreateTcgNftReconcileResponse create_tcg_nft_reconcile()

Re-read your wallets on chain so your card counts follow what you hold (cards you moved away leave; cards you received join).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import crossly_wallet_api
from crossly.model.tcg.create_tcg_nft_reconcile_response import CreateTcgNftReconcileResponse
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
    api_instance = crossly_wallet_api.CrosslyWalletApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Re-read your wallets on chain so your card counts follow what you hold (cards you moved away leave; cards you received join).
        api_response = api_instance.create_tcg_nft_reconcile()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CrosslyWalletApi->create_tcg_nft_reconcile: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateTcgNftReconcileResponse**

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

# **create_wallet_crossly**
> GetWalletCrosslyResponse create_wallet_crossly()

Create your Crossly wallet now (it is otherwise created for you in the background). Idempotent.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import crossly_wallet_api
from crossly.model.common.error import Error
from crossly.model.wallet.get_wallet_crossly_response import GetWalletCrosslyResponse
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
    api_instance = crossly_wallet_api.CrosslyWalletApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create your Crossly wallet now (it is otherwise created for you in the background). Idempotent.
        api_response = api_instance.create_wallet_crossly()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CrosslyWalletApi->create_wallet_crossly: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWalletCrosslyResponse**

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

# **get_wallet_crossly**
> GetWalletCrosslyResponse get_wallet_crossly()

Your Crossly wallet (self-custody Solana): status, address, whether it is configured, and your card NFT counts by status.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import crossly_wallet_api
from crossly.model.common.error import Error
from crossly.model.wallet.get_wallet_crossly_response import GetWalletCrosslyResponse
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
    api_instance = crossly_wallet_api.CrosslyWalletApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your Crossly wallet (self-custody Solana): status, address, whether it is configured, and your card NFT counts by status.
        api_response = api_instance.get_wallet_crossly()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CrosslyWalletApi->get_wallet_crossly: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWalletCrosslyResponse**

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

# **list_tcg_nfts**
> ListTcgNftsResponse list_tcg_nfts(game)

Your card NFTs for a Crossly TCG game: each copy, its mint status, asset id and whether it is soulbound (starter).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import crossly_wallet_api
from crossly.model.tcg.list_tcg_nfts_response import ListTcgNftsResponse
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
    api_instance = crossly_wallet_api.CrosslyWalletApi(api_client)
    game = "game_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Your card NFTs for a Crossly TCG game: each copy, its mint status, asset id and whether it is soulbound (starter).
        api_response = api_instance.list_tcg_nfts(game)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CrosslyWalletApi->list_tcg_nfts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**|  |

### Return type

**ListTcgNftsResponse**

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

