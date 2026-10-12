# crossly.DefaultApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cosm_designer_chain_auto_unlock**](DefaultApi.md#create_cosm_designer_chain_auto_unlock) | **POST** /v1/cosm/designer/chain-auto-unlock | 
[**create_cosm_designer_chain_unlock**](DefaultApi.md#create_cosm_designer_chain_unlock) | **POST** /v1/cosm/designer/chain-unlock | 
[**create_cosm_designer_materialise**](DefaultApi.md#create_cosm_designer_materialise) | **POST** /v1/cosm/designer/materialise | 
[**create_cosm_designer_materialise_confirm**](DefaultApi.md#create_cosm_designer_materialise_confirm) | **POST** /v1/cosm/designer/materialise/confirm | 
[**create_cosm_designer_materialise_release**](DefaultApi.md#create_cosm_designer_materialise_release) | **POST** /v1/cosm/designer/materialise/release | 
[**create_cosm_designer_submit_for_review**](DefaultApi.md#create_cosm_designer_submit_for_review) | **POST** /v1/cosm/designer/submit-for-review | 
[**create_cosm_designer_term**](DefaultApi.md#create_cosm_designer_term) | **POST** /v1/cosm/designer/terms | 
[**get_cosm_designer_copy_state**](DefaultApi.md#get_cosm_designer_copy_state) | **GET** /v1/cosm/designer/copy-state | 
[**get_cosm_designer_earning**](DefaultApi.md#get_cosm_designer_earning) | **GET** /v1/cosm/designer/earnings | 
[**get_cosm_designer_term**](DefaultApi.md#get_cosm_designer_term) | **GET** /v1/cosm/designer/terms | 
[**get_listing_variation_group**](DefaultApi.md#get_listing_variation_group) | **GET** /v1/listings/{id}/variation-group | 
[**get_market_metal_spot_history**](DefaultApi.md#get_market_metal_spot_history) | **GET** /v1/market/metals/spot/history | 
[**get_market_product**](DefaultApi.md#get_market_product) | **GET** /v1/market/products/{id} | 
[**get_market_product_related**](DefaultApi.md#get_market_product_related) | **GET** /v1/market/products/{id}/related | 
[**get_market_scrap_quote**](DefaultApi.md#get_market_scrap_quote) | **GET** /v1/market/scrap/quote | 
[**get_market_variant_book**](DefaultApi.md#get_market_variant_book) | **GET** /v1/market/variants/{id}/book | 
[**get_variation_group**](DefaultApi.md#get_variation_group) | **GET** /v1/variation-groups/{id} | 
[**get_variation_group_publish_plan**](DefaultApi.md#get_variation_group_publish_plan) | **GET** /v1/variation-groups/{id}/publish-plan | 
[**list_market_bullion**](DefaultApi.md#list_market_bullion) | **GET** /v1/market/bullion | 
[**list_market_graders**](DefaultApi.md#list_market_graders) | **GET** /v1/market/graders | 
[**list_market_metal_spot**](DefaultApi.md#list_market_metal_spot) | **GET** /v1/market/metals/spot | 
[**list_market_products**](DefaultApi.md#list_market_products) | **GET** /v1/market/products | 
[**list_market_variant_tiers**](DefaultApi.md#list_market_variant_tiers) | **GET** /v1/market/variants/{id}/tiers | 
[**list_variation_groups**](DefaultApi.md#list_variation_groups) | **GET** /v1/variation-groups | 


# **create_cosm_designer_chain_auto_unlock**
> CreateCosmDesignerChainAutoUnlockResponse create_cosm_designer_chain_auto_unlock(request_body)



Opt a design in or out of the free chain unlock a popular limited design earns (on by default). Designer-only. Answers the popularity of the design toward the bar.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.cosm.create_cosm_designer_chain_auto_unlock_response import CreateCosmDesignerChainAutoUnlockResponse
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
    api_instance = default_api.DefaultApi(api_client)
    request_body = {
        "key": None,
    } # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cosm_designer_chain_auto_unlock(request_body)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->create_cosm_designer_chain_auto_unlock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

**CreateCosmDesignerChainAutoUnlockResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_cosm_designer_chain_unlock**
> CreateCosmDesignerChainUnlockResponse create_cosm_designer_chain_unlock(request_body)



Burn COSM to make a design mintable on chain. Designer-only and idempotent: paying twice is impossible, and a second call returns the existing unlock without charging. The fee is DESTROYED rather than collected. Limited editions only. Once unlocked, any holder may take their own copy on chain.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.cosm.create_cosm_designer_chain_unlock_response import CreateCosmDesignerChainUnlockResponse
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
    api_instance = default_api.DefaultApi(api_client)
    request_body = {
        "key": None,
    } # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cosm_designer_chain_unlock(request_body)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->create_cosm_designer_chain_unlock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

**CreateCosmDesignerChainUnlockResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_cosm_designer_materialise**
> CreateCosmDesignerMaterialiseResponse create_cosm_designer_materialise(request_body)



Lock a copy and return an UNSIGNED Metaplex Core mint for the holder to sign. One call: it resolves the designer royalty, locks the copy, publishes immutable content-addressed metadata and builds the transaction — so a lock is never taken without a transaction to go with it, and a failure after the lock releases it. Does NOT void the copy; call confirm once the chain reaches FINALIZED commitment. Every royalty recipient needs a connected wallet first, and the designer must have unlocked the design.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.cosm.create_cosm_designer_materialise_response import CreateCosmDesignerMaterialiseResponse
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
    api_instance = default_api.DefaultApi(api_client)
    request_body = {
        "key": None,
    } # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cosm_designer_materialise(request_body)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->create_cosm_designer_materialise: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

**CreateCosmDesignerMaterialiseResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_cosm_designer_materialise_confirm**
> CreateCosmDesignerMaterialiseConfirmResponse create_cosm_designer_materialise_confirm(request_body)



Record a confirmed mint and void the in-world copy, in one transaction. The caller MUST have verified the transaction at finalized commitment first — an NFT recorded against a transaction that never landed cannot be recalled, and the copy it voided is gone. Idempotent on an already-confirmed request.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.cosm.create_cosm_designer_materialise_confirm_response import CreateCosmDesignerMaterialiseConfirmResponse
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
    api_instance = default_api.DefaultApi(api_client)
    request_body = {
        "key": None,
    } # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cosm_designer_materialise_confirm(request_body)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->create_cosm_designer_materialise_confirm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

**CreateCosmDesignerMaterialiseConfirmResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_cosm_designer_materialise_release**
> CreateWorldJobShiftReleaseResponse create_cosm_designer_materialise_release(request_body)



Release a mint lock that was never signed. The ordinary outcome of somebody closing a wallet prompt, and it leaves the copy exactly as it was. Refuses a request that has already minted, because releasing one would unlock a copy that is on chain.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_job_shift_release_response import CreateWorldJobShiftReleaseResponse
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
    api_instance = default_api.DefaultApi(api_client)
    request_body = {
        "key": None,
    } # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cosm_designer_materialise_release(request_body)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->create_cosm_designer_materialise_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

**CreateWorldJobShiftReleaseResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_cosm_designer_submit_for_review**
> CreateCosmDesignerSubmitForReviewResponse create_cosm_designer_submit_for_review(request_body)



Submit a user-authored design for moderation. Designer-only, and refuses a design with no preview image HERE rather than at approval so the designer learns what is missing while they can still fix it. Submitting twice returns the existing pending review instead of queueing a second one — a moderator facing two reviews of one piece does not know which they are deciding. A design already on sale is refused.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.cosm.create_cosm_designer_submit_for_review_response import CreateCosmDesignerSubmitForReviewResponse
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
    api_instance = default_api.DefaultApi(api_client)
    request_body = {
        "key": None,
    } # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cosm_designer_submit_for_review(request_body)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->create_cosm_designer_submit_for_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

**CreateCosmDesignerSubmitForReviewResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_cosm_designer_term**
> CreateCosmDesignerTermResponse create_cosm_designer_term(request_body)



Publish terms for a design. Never edits: every change is a new version, and a copy sold under an earlier one keeps those terms forever. Only the designer may call it. Collaborator shares are of the ROYALTY rather than the sale price and may total at most 100%, with the remainder staying with the designer; a total above 100% is refused rather than scaled down.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.cosm.create_cosm_designer_term_response import CreateCosmDesignerTermResponse
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
    api_instance = default_api.DefaultApi(api_client)
    request_body = {
        "key": None,
    } # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_cosm_designer_term(request_body)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->create_cosm_designer_term: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

**CreateCosmDesignerTermResponse**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_cosm_designer_copy_state**
> GetCosmDesignerCopyStateResponse get_cosm_designer_copy_state(ownership_id)



Where a copy currently is: held (in-world, wearable, listable for COSM), minting (locked while a mint is in flight) or materialised (an NFT in the holder wallet). A copy is in exactly one of these, never two.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.cosm.get_cosm_designer_copy_state_response import GetCosmDesignerCopyStateResponse
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
    api_instance = default_api.DefaultApi(api_client)
    ownership_id = "ownershipId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cosm_designer_copy_state(ownership_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->get_cosm_designer_copy_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownership_id** | **str**|  |

### Return type

**GetCosmDesignerCopyStateResponse**

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

# **get_cosm_designer_earning**
> GetCosmDesignerEarningResponse get_cosm_designer_earning(subject_id)



What a designer has earned, in both denominations. COSM royalties come from COSM-priced sales; cash earnings come from cash-priced sales and are funded by the buyer payment itself. The two are never converted into one another, and COSM is never cashed out.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.cosm.get_cosm_designer_earning_response import GetCosmDesignerEarningResponse
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
    api_instance = default_api.DefaultApi(api_client)
    subject_id = "subjectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cosm_designer_earning(subject_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->get_cosm_designer_earning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**|  |

### Return type

**GetCosmDesignerEarningResponse**

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

# **get_cosm_designer_term**
> GetCosmDesignerTermResponse get_cosm_designer_term(cosmetic_id)



The published terms for a design: resale, price window, secondary royalty and collaborator splits. Also reports the platform rates a designer does not control, and whether the terms are enforceable on chain — inside Crossly every rule is enforced, but a third-party marketplace honours a royalty voluntarily at best.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.cosm.get_cosm_designer_term_response import GetCosmDesignerTermResponse
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
    api_instance = default_api.DefaultApi(api_client)
    cosmetic_id = "cosmeticId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cosm_designer_term(cosmetic_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->get_cosm_designer_term: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosmetic_id** | **str**|  |

### Return type

**GetCosmDesignerTermResponse**

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

# **get_listing_variation_group**
> GetListingVariationGroupResponse get_listing_variation_group(id)



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.listing.get_listing_variation_group_response import GetListingVariationGroupResponse
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
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_listing_variation_group(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->get_listing_variation_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetListingVariationGroupResponse**

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

# **get_market_metal_spot_history**
> GetMarketMetalSpotHistoryResponse get_market_metal_spot_history()



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.market.get_market_metal_spot_history_response import GetMarketMetalSpotHistoryResponse
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_market_metal_spot_history()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->get_market_metal_spot_history: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetMarketMetalSpotHistoryResponse**

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

# **get_market_product**
> GetMarketProductResponse get_market_product(id)



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.market.get_market_product_response import GetMarketProductResponse
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
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_market_product(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->get_market_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetMarketProductResponse**

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

# **get_market_product_related**
> GetMarketProductRelatedResponse get_market_product_related(id)



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.market.get_market_product_related_response import GetMarketProductRelatedResponse
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
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_market_product_related(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->get_market_product_related: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetMarketProductRelatedResponse**

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

# **get_market_scrap_quote**
> GetMarketScrapQuoteResponse get_market_scrap_quote()



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.market.get_market_scrap_quote_response import GetMarketScrapQuoteResponse
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_market_scrap_quote()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->get_market_scrap_quote: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetMarketScrapQuoteResponse**

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

# **get_market_variant_book**
> GetMarketVariantBookResponse get_market_variant_book(id)



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.market.get_market_variant_book_response import GetMarketVariantBookResponse
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
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_market_variant_book(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->get_market_variant_book: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetMarketVariantBookResponse**

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

# **get_variation_group**
> ListVariationGroupsItem get_variation_group(id)



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.variation.list_variation_groups_item import ListVariationGroupsItem
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
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_variation_group(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->get_variation_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListVariationGroupsItem**

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

# **get_variation_group_publish_plan**
> GetVariationGroupPublishPlanResponse get_variation_group_publish_plan(id)



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.variation.get_variation_group_publish_plan_response import GetVariationGroupPublishPlanResponse
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
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_variation_group_publish_plan(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->get_variation_group_publish_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetVariationGroupPublishPlanResponse**

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

# **list_market_bullion**
> ListMarketBullionResponse list_market_bullion()



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.market.list_market_bullion_response import ListMarketBullionResponse
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_market_bullion()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->list_market_bullion: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListMarketBullionResponse**

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

# **list_market_graders**
> ListMarketGradersResponse list_market_graders()



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.market.list_market_graders_response import ListMarketGradersResponse
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_market_graders()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->list_market_graders: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListMarketGradersResponse**

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

# **list_market_metal_spot**
> ListMarketMetalSpotResponse list_market_metal_spot()



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.market.list_market_metal_spot_response import ListMarketMetalSpotResponse
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_market_metal_spot()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->list_market_metal_spot: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListMarketMetalSpotResponse**

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

# **list_market_products**
> ListMarketProductsResponse list_market_products()



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.market.list_market_products_response import ListMarketProductsResponse
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_market_products()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->list_market_products: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListMarketProductsResponse**

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

# **list_market_variant_tiers**
> ListMarketVariantTiersResponse list_market_variant_tiers(id)



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.market.list_market_variant_tiers_response import ListMarketVariantTiersResponse
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
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_market_variant_tiers(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->list_market_variant_tiers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListMarketVariantTiersResponse**

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

# **list_variation_groups**
> ListVariationGroupsResponse list_variation_groups()



### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import default_api
from crossly.model.common.error import Error
from crossly.model.variation.list_variation_groups_response import ListVariationGroupsResponse
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_variation_groups()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DefaultApi->list_variation_groups: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListVariationGroupsResponse**

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

