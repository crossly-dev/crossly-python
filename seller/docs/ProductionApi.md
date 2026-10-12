# crossly.ProductionApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_production_candidate_accept**](ProductionApi.md#create_production_candidate_accept) | **POST** /v1/production/candidates/{id}/accept | Accept a graduated design&#39;s production terms (edition size, cost, holder access).
[**create_production_candidate_po**](ProductionApi.md#create_production_candidate_po) | **POST** /v1/production/candidates/{id}/po | Ops: open a purchase order for a candidate. Admin PAT only.
[**create_production_candidate_vote**](ProductionApi.md#create_production_candidate_vote) | **POST** /v1/production/candidates/{id}/vote | Back (support: true) or un-back a design on the production ballot. One vote per person per design; voters must have bought on Crossly.
[**create_production_design_brief**](ProductionApi.md#create_production_design_brief) | **POST** /v1/production/designs/{cosmeticId}/brief | Set a design&#39;s production brief (materials, finish, box, reference images).
[**create_production_design_consent**](ProductionApi.md#create_production_design_consent) | **POST** /v1/production/designs/{cosmeticId}/consent | Opt a design in or out of physical production.
[**create_production_design_spec**](ProductionApi.md#create_production_design_spec) | **POST** /v1/production/designs/{cosmeticId}/spec | Set a design&#39;s production spec (category, materials, complexity, packaging).
[**create_production_estimate**](ProductionApi.md#create_production_estimate) | **POST** /v1/production/estimate | Estimate a run&#39;s landed cost from a spec + edition size (overshoots for safety).
[**create_production_run_purchase**](ProductionApi.md#create_production_run_purchase) | **POST** /v1/production/runs/{id}/purchase | Buy a limited-edition unit of a physical run (holder pricing applies).
[**create_receipt_relist**](ProductionApi.md#create_receipt_relist) | **POST** /v1/receipts/{id}/relist | Sell it again: a draft listing of something you bought on Crossly, carrying its purchase receipt so the next buyer inherits its provenance.
[**get_production_ballot**](ProductionApi.md#get_production_ballot) | **GET** /v1/production/ballot | The ballot: designs waiting for a physical run, most backed first, and whether you may vote.
[**get_production_candidate**](ProductionApi.md#get_production_candidate) | **GET** /v1/production/candidates | Your designs that have graduated toward a physical run.
[**get_production_design_pref**](ProductionApi.md#get_production_design_pref) | **GET** /v1/production/designs/{cosmeticId}/prefs | Read a design&#39;s production preferences (spec, brief, opt-out).
[**get_production_drop**](ProductionApi.md#get_production_drop) | **GET** /v1/production/drops | Limited-edition units you own, with fulfillment status.
[**get_production_earning**](ProductionApi.md#get_production_earning) | **GET** /v1/production/earnings | Your CBX earnings from physical production (royalties + balance + lines).
[**get_production_line**](ProductionApi.md#get_production_line) | **GET** /v1/production/lines | Your production lines dashboard (candidate + run + inventory).
[**get_production_po**](ProductionApi.md#get_production_po) | **GET** /v1/production/pos | Ops: list purchase orders (optionally for one candidate). Admin PAT only.
[**get_production_po_reconcile**](ProductionApi.md#get_production_po_reconcile) | **GET** /v1/production/pos/{poId}/reconcile | Ops: reconcile a PO&#39;s actuals against the estimate. Admin PAT only.
[**get_production_run**](ProductionApi.md#get_production_run) | **GET** /v1/production/runs | Browse open limited-edition physical runs (graduated designs).
[**get_shop_listing_provenance**](ProductionApi.md#get_shop_listing_provenance) | **GET** /v1/shop/listings/{slug}/provenance | Crossly provenance behind a shop listing: owners on Crossly and since when (never who or for how much). Null when not bought here.
[**update_production_po**](ProductionApi.md#update_production_po) | **PATCH** /v1/production/pos/{poId} | Ops: update a PO (supplier, freight, actuals, QC, status). Admin PAT only.


# **create_production_candidate_accept**
> CreateProductionCandidateAcceptResponse create_production_candidate_accept(id)

Accept a graduated design's production terms (edition size, cost, holder access).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.production.create_production_candidate_accept_response import CreateProductionCandidateAcceptResponse
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
    api_instance = production_api.ProductionApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Accept a graduated design's production terms (edition size, cost, holder access).
        api_response = api_instance.create_production_candidate_accept(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->create_production_candidate_accept: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateProductionCandidateAcceptResponse**

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

# **create_production_candidate_po**
> UpdateProductionPoResponse create_production_candidate_po(id)

Ops: open a purchase order for a candidate. Admin PAT only.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.update_production_po_response import UpdateProductionPoResponse
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
    api_instance = production_api.ProductionApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Ops: open a purchase order for a candidate. Admin PAT only.
        api_response = api_instance.create_production_candidate_po(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->create_production_candidate_po: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateProductionPoResponse**

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

# **create_production_candidate_vote**
> CreateProductionCandidateVoteResponse create_production_candidate_vote(id)

Back (support: true) or un-back a design on the production ballot. One vote per person per design; voters must have bought on Crossly.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.create_production_candidate_vote_response import CreateProductionCandidateVoteResponse
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
    api_instance = production_api.ProductionApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Back (support: true) or un-back a design on the production ballot. One vote per person per design; voters must have bought on Crossly.
        api_response = api_instance.create_production_candidate_vote(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->create_production_candidate_vote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateProductionCandidateVoteResponse**

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

# **create_production_design_brief**
> CreateProductionDesignSpecResponse create_production_design_brief(cosmetic_id)

Set a design's production brief (materials, finish, box, reference images).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.create_production_design_spec_response import CreateProductionDesignSpecResponse
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
    api_instance = production_api.ProductionApi(api_client)
    cosmetic_id = "cosmeticId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set a design's production brief (materials, finish, box, reference images).
        api_response = api_instance.create_production_design_brief(cosmetic_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->create_production_design_brief: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosmetic_id** | **str**|  |

### Return type

**CreateProductionDesignSpecResponse**

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

# **create_production_design_consent**
> CreateProductionDesignSpecResponse create_production_design_consent(cosmetic_id)

Opt a design in or out of physical production.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.create_production_design_spec_response import CreateProductionDesignSpecResponse
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
    api_instance = production_api.ProductionApi(api_client)
    cosmetic_id = "cosmeticId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Opt a design in or out of physical production.
        api_response = api_instance.create_production_design_consent(cosmetic_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->create_production_design_consent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosmetic_id** | **str**|  |

### Return type

**CreateProductionDesignSpecResponse**

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

# **create_production_design_spec**
> CreateProductionDesignSpecResponse create_production_design_spec(cosmetic_id)

Set a design's production spec (category, materials, complexity, packaging).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.create_production_design_spec_response import CreateProductionDesignSpecResponse
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
    api_instance = production_api.ProductionApi(api_client)
    cosmetic_id = "cosmeticId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set a design's production spec (category, materials, complexity, packaging).
        api_response = api_instance.create_production_design_spec(cosmetic_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->create_production_design_spec: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosmetic_id** | **str**|  |

### Return type

**CreateProductionDesignSpecResponse**

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

# **create_production_estimate**
> CreateProductionEstimateResponse create_production_estimate()

Estimate a run's landed cost from a spec + edition size (overshoots for safety).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.create_production_estimate_response import CreateProductionEstimateResponse
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
    api_instance = production_api.ProductionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Estimate a run's landed cost from a spec + edition size (overshoots for safety).
        api_response = api_instance.create_production_estimate()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->create_production_estimate: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateProductionEstimateResponse**

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

# **create_production_run_purchase**
> CreateProductionRunPurchaseResponse create_production_run_purchase(id)

Buy a limited-edition unit of a physical run (holder pricing applies).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.create_production_run_purchase_response import CreateProductionRunPurchaseResponse
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
    api_instance = production_api.ProductionApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Buy a limited-edition unit of a physical run (holder pricing applies).
        api_response = api_instance.create_production_run_purchase(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->create_production_run_purchase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateProductionRunPurchaseResponse**

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

# **create_receipt_relist**
> CreateReceiptRelistResponse create_receipt_relist(id)

Sell it again: a draft listing of something you bought on Crossly, carrying its purchase receipt so the next buyer inherits its provenance.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.common.create_receipt_relist_response import CreateReceiptRelistResponse
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
    api_instance = production_api.ProductionApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Sell it again: a draft listing of something you bought on Crossly, carrying its purchase receipt so the next buyer inherits its provenance.
        api_response = api_instance.create_receipt_relist(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->create_receipt_relist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateReceiptRelistResponse**

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

# **get_production_ballot**
> GetProductionBallotResponse get_production_ballot()

The ballot: designs waiting for a physical run, most backed first, and whether you may vote.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.production.get_production_ballot_response import GetProductionBallotResponse
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
    api_instance = production_api.ProductionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The ballot: designs waiting for a physical run, most backed first, and whether you may vote.
        api_response = api_instance.get_production_ballot()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->get_production_ballot: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetProductionBallotResponse**

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

# **get_production_candidate**
> GetProductionCandidateResponse get_production_candidate()

Your designs that have graduated toward a physical run.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.production.get_production_candidate_response import GetProductionCandidateResponse
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
    api_instance = production_api.ProductionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your designs that have graduated toward a physical run.
        api_response = api_instance.get_production_candidate()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->get_production_candidate: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetProductionCandidateResponse**

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

# **get_production_design_pref**
> GetProductionDesignPrefResponse get_production_design_pref(cosmetic_id)

Read a design's production preferences (spec, brief, opt-out).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.get_production_design_pref_response import GetProductionDesignPrefResponse
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
    api_instance = production_api.ProductionApi(api_client)
    cosmetic_id = "cosmeticId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Read a design's production preferences (spec, brief, opt-out).
        api_response = api_instance.get_production_design_pref(cosmetic_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->get_production_design_pref: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosmetic_id** | **str**|  |

### Return type

**GetProductionDesignPrefResponse**

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

# **get_production_drop**
> GetProductionDropResponse get_production_drop()

Limited-edition units you own, with fulfillment status.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.production.get_production_drop_response import GetProductionDropResponse
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
    api_instance = production_api.ProductionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Limited-edition units you own, with fulfillment status.
        api_response = api_instance.get_production_drop()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->get_production_drop: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetProductionDropResponse**

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

# **get_production_earning**
> GetProductionEarningResponse get_production_earning()

Your CBX earnings from physical production (royalties + balance + lines).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.get_production_earning_response import GetProductionEarningResponse
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
    api_instance = production_api.ProductionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your CBX earnings from physical production (royalties + balance + lines).
        api_response = api_instance.get_production_earning()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->get_production_earning: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetProductionEarningResponse**

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

# **get_production_line**
> GetProductionLineResponse get_production_line()

Your production lines dashboard (candidate + run + inventory).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.get_production_line_response import GetProductionLineResponse
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
    api_instance = production_api.ProductionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your production lines dashboard (candidate + run + inventory).
        api_response = api_instance.get_production_line()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->get_production_line: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetProductionLineResponse**

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

# **get_production_po**
> GetProductionPoResponse get_production_po()

Ops: list purchase orders (optionally for one candidate). Admin PAT only.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.production.get_production_po_response import GetProductionPoResponse
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
    api_instance = production_api.ProductionApi(api_client)
    candidate_id = "candidateId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ops: list purchase orders (optionally for one candidate). Admin PAT only.
        api_response = api_instance.get_production_po(candidate_id=candidate_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->get_production_po: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candidate_id** | **str**|  | [optional]

### Return type

**GetProductionPoResponse**

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

# **get_production_po_reconcile**
> GetProductionPoReconcileResponse get_production_po_reconcile(po_id)

Ops: reconcile a PO's actuals against the estimate. Admin PAT only.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.production.get_production_po_reconcile_response import GetProductionPoReconcileResponse
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
    api_instance = production_api.ProductionApi(api_client)
    po_id = "poId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Ops: reconcile a PO's actuals against the estimate. Admin PAT only.
        api_response = api_instance.get_production_po_reconcile(po_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->get_production_po_reconcile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **po_id** | **str**|  |

### Return type

**GetProductionPoReconcileResponse**

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

# **get_production_run**
> GetProductionRunResponse get_production_run()

Browse open limited-edition physical runs (graduated designs).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.get_production_run_response import GetProductionRunResponse
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
    api_instance = production_api.ProductionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Browse open limited-edition physical runs (graduated designs).
        api_response = api_instance.get_production_run()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->get_production_run: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetProductionRunResponse**

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

# **get_shop_listing_provenance**
> GetShopListingProvenanceResponse get_shop_listing_provenance(slug)

Crossly provenance behind a shop listing: owners on Crossly and since when (never who or for how much). Null when not bought here.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.common.get_shop_listing_provenance_response import GetShopListingProvenanceResponse
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
    api_instance = production_api.ProductionApi(api_client)
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Crossly provenance behind a shop listing: owners on Crossly and since when (never who or for how much). Null when not bought here.
        api_response = api_instance.get_shop_listing_provenance(slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->get_shop_listing_provenance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  |

### Return type

**GetShopListingProvenanceResponse**

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

# **update_production_po**
> UpdateProductionPoResponse update_production_po(po_id)

Ops: update a PO (supplier, freight, actuals, QC, status). Admin PAT only.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import production_api
from crossly.model.common.error import Error
from crossly.model.production.update_production_po_response import UpdateProductionPoResponse
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
    api_instance = production_api.ProductionApi(api_client)
    po_id = "poId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Ops: update a PO (supplier, freight, actuals, QC, status). Admin PAT only.
        api_response = api_instance.update_production_po(po_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProductionApi->update_production_po: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **po_id** | **str**|  |

### Return type

**UpdateProductionPoResponse**

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

