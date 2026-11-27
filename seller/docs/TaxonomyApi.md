# crossly.TaxonomyApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_category_by_id**](TaxonomyApi.md#get_category_by_id) | **GET** /v1/categories/{id} | One canonical category and the category it maps to on each marketplace.
[**get_taxonomy_category**](TaxonomyApi.md#get_taxonomy_category) | **GET** /v1/taxonomy/{platform}/categories | Categories for a platform. Default is top-level; pass &#x60;?parent&#x3D;&lt;categoryId&gt;&#x60; to drill down one level (supported on cookie platforms whose recipe returns flat parent_id-linked rows).
[**get_taxonomy_category_aspect**](TaxonomyApi.md#get_taxonomy_category_aspect) | **GET** /v1/taxonomy/{platform}/categories/{id}/aspects | Item-specific aspects (eBay) / properties (Etsy) / hard-coded enums (cookie platforms) for a category.
[**get_taxonomy_category_children**](TaxonomyApi.md#get_taxonomy_category_children) | **GET** /v1/taxonomy/{platform}/categories/{id}/children | Direct children of a category node.
[**get_taxonomy_required_field**](TaxonomyApi.md#get_taxonomy_required_field) | **GET** /v1/taxonomy/{platform}/required-fields | Normalized field schema the seller needs to fill before crossposting to this platform. Combines master fields (title/description/price/condition) with platform-specific overrides.
[**list_category_aspects**](TaxonomyApi.md#list_category_aspects) | **GET** /v1/categories/{id}/aspects | Item specifics for a canonical category: required/optional, known values, per-marketplace names.
[**list_category_search**](TaxonomyApi.md#list_category_search) | **GET** /v1/categories/search | Search or browse Crossly&#39;s canonical categories (the ids listings take as categoryId).
[**list_taxonomy_ebay_charities**](TaxonomyApi.md#list_taxonomy_ebay_charities) | **GET** /v1/taxonomy/ebay/charities | Search eBay for Charity organisations (the charityId an eBay listing donates to).
[**list_taxonomy_suggest**](TaxonomyApi.md#list_taxonomy_suggest) | **GET** /v1/taxonomy/{platform}/suggest | Reverse lookup — suggest categories matching a search phrase: eBay live; Poshmark, Mercari, Depop, Grailed, Vinted, Whatnot, Vestiaire, OfferUp, Facebook and Curtsy over their harvested trees. Etsy answers an empty list (browse its tree instead).


# **get_category_by_id**
> GetCategoryByIdResponse get_category_by_id(id)

One canonical category and the category it maps to on each marketplace.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.common.error import Error
from crossly.model.category.get_category_by_id_response import GetCategoryByIdResponse
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
    api_instance = taxonomy_api.TaxonomyApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One canonical category and the category it maps to on each marketplace.
        api_response = api_instance.get_category_by_id(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->get_category_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetCategoryByIdResponse**

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

# **get_taxonomy_category**
> GetTaxonomyCategoryResponse get_taxonomy_category(platform)

Categories for a platform. Default is top-level; pass `?parent=<categoryId>` to drill down one level (supported on cookie platforms whose recipe returns flat parent_id-linked rows).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.taxonomy.get_taxonomy_category_response import GetTaxonomyCategoryResponse
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
    api_instance = taxonomy_api.TaxonomyApi(api_client)
    platform = "platform_example" # str | 
    parent = "parent_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Categories for a platform. Default is top-level; pass `?parent=<categoryId>` to drill down one level (supported on cookie platforms whose recipe returns flat parent_id-linked rows).
        api_response = api_instance.get_taxonomy_category(platform)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->get_taxonomy_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Categories for a platform. Default is top-level; pass `?parent=<categoryId>` to drill down one level (supported on cookie platforms whose recipe returns flat parent_id-linked rows).
        api_response = api_instance.get_taxonomy_category(platform, parent=parent)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->get_taxonomy_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |
 **parent** | **str**|  | [optional]

### Return type

**GetTaxonomyCategoryResponse**

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

# **get_taxonomy_category_aspect**
> GetTaxonomyCategoryAspectResponse get_taxonomy_category_aspect(platform, id)

Item-specific aspects (eBay) / properties (Etsy) / hard-coded enums (cookie platforms) for a category.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.taxonomy.get_taxonomy_category_aspect_response import GetTaxonomyCategoryAspectResponse
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
    api_instance = taxonomy_api.TaxonomyApi(api_client)
    platform = "platform_example" # str | 
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Item-specific aspects (eBay) / properties (Etsy) / hard-coded enums (cookie platforms) for a category.
        api_response = api_instance.get_taxonomy_category_aspect(platform, id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->get_taxonomy_category_aspect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |
 **id** | **str**|  |

### Return type

**GetTaxonomyCategoryAspectResponse**

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

# **get_taxonomy_category_children**
> GetTaxonomyCategoryChildrenResponse get_taxonomy_category_children(platform, id)

Direct children of a category node.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.taxonomy.get_taxonomy_category_children_response import GetTaxonomyCategoryChildrenResponse
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
    api_instance = taxonomy_api.TaxonomyApi(api_client)
    platform = "platform_example" # str | 
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Direct children of a category node.
        api_response = api_instance.get_taxonomy_category_children(platform, id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->get_taxonomy_category_children: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |
 **id** | **str**|  |

### Return type

**GetTaxonomyCategoryChildrenResponse**

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

# **get_taxonomy_required_field**
> GetTaxonomyRequiredFieldResponse get_taxonomy_required_field(platform)

Normalized field schema the seller needs to fill before crossposting to this platform. Combines master fields (title/description/price/condition) with platform-specific overrides.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.common.error import Error
from crossly.model.taxonomy.get_taxonomy_required_field_response import GetTaxonomyRequiredFieldResponse
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
    api_instance = taxonomy_api.TaxonomyApi(api_client)
    platform = "platform_example" # str | 
    category_id = "categoryId_example" # str | Optional — used to inline aspects when present. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Normalized field schema the seller needs to fill before crossposting to this platform. Combines master fields (title/description/price/condition) with platform-specific overrides.
        api_response = api_instance.get_taxonomy_required_field(platform)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->get_taxonomy_required_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Normalized field schema the seller needs to fill before crossposting to this platform. Combines master fields (title/description/price/condition) with platform-specific overrides.
        api_response = api_instance.get_taxonomy_required_field(platform, category_id=category_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->get_taxonomy_required_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |
 **category_id** | **str**| Optional — used to inline aspects when present. | [optional]

### Return type

**GetTaxonomyRequiredFieldResponse**

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

# **list_category_aspects**
> ListCategoryAspectsResponse list_category_aspects(id)

Item specifics for a canonical category: required/optional, known values, per-marketplace names.

Required-ness and cardinality come from the eBay category the concept maps to. `freeText` = any text is accepted; otherwise `values` are the known values (up to `valuesLimit`). `marketplaces` gives the attribute name each marketplace uses for the aspect. Send them as `itemSpecifics` on POST /v1/listings.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.common.error import Error
from crossly.model.category.list_category_aspects_response import ListCategoryAspectsResponse
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
    api_instance = taxonomy_api.TaxonomyApi(api_client)
    id = "id_example" # str | 
    values_limit = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Item specifics for a canonical category: required/optional, known values, per-marketplace names.
        api_response = api_instance.list_category_aspects(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->list_category_aspects: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Item specifics for a canonical category: required/optional, known values, per-marketplace names.
        api_response = api_instance.list_category_aspects(id, values_limit=values_limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->list_category_aspects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **values_limit** | **int**|  | [optional] if omitted the server will use the default value of 50

### Return type

**ListCategoryAspectsResponse**

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

# **list_category_search**
> ListCategorySearchResponse list_category_search()

Search or browse Crossly's canonical categories (the ids listings take as categoryId).

`q` matches the category name and path. `path` (e.g. \"Clothing & Shoes > Men\") limits to one branch. Without `q`, `meta.branches` lists the next level under `path` (the root when omitted) so a client can walk the tree down to a leaf.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.common.error import Error
from crossly.model.category.list_category_search_response import ListCategorySearchResponse
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
    api_instance = taxonomy_api.TaxonomyApi(api_client)
    q = "q_example" # str |  (optional)
    path = "path_example" # str |  (optional)
    limit = 25 # int |  (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search or browse Crossly's canonical categories (the ids listings take as categoryId).
        api_response = api_instance.list_category_search(q=q, path=path, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->list_category_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional]
 **path** | **str**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 25

### Return type

**ListCategorySearchResponse**

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

# **list_taxonomy_ebay_charities**
> ListTaxonomyEbayCharitiesResponse list_taxonomy_ebay_charities()

Search eBay for Charity organisations (the charityId an eBay listing donates to).

Send the chosen `charityOrgId` as `overrides.ebay.charityId` with `overrides.ebay.donationPercentage` (10-100 in steps of 5) on a listing to donate that share of the eBay sale. `q` needs at least 2 characters.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.taxonomy.list_taxonomy_ebay_charities_response import ListTaxonomyEbayCharitiesResponse
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
    api_instance = taxonomy_api.TaxonomyApi(api_client)
    q = "q_example" # str |  (optional)
    limit = 20 # int |  (optional) if omitted the server will use the default value of 20
    marketplace = "EBAY_US" # str |  (optional) if omitted the server will use the default value of "EBAY_US"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search eBay for Charity organisations (the charityId an eBay listing donates to).
        api_response = api_instance.list_taxonomy_ebay_charities(q=q, limit=limit, marketplace=marketplace)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->list_taxonomy_ebay_charities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 20
 **marketplace** | **str**|  | [optional] if omitted the server will use the default value of "EBAY_US"

### Return type

**ListTaxonomyEbayCharitiesResponse**

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

# **list_taxonomy_suggest**
> ListTaxonomySuggestResponse list_taxonomy_suggest(platform)

Reverse lookup — suggest categories matching a search phrase: eBay live; Poshmark, Mercari, Depop, Grailed, Vinted, Whatnot, Vestiaire, OfferUp, Facebook and Curtsy over their harvested trees. Etsy answers an empty list (browse its tree instead).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.taxonomy.list_taxonomy_suggest_response import ListTaxonomySuggestResponse
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
    api_instance = taxonomy_api.TaxonomyApi(api_client)
    platform = "platform_example" # str | 
    q = "q_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reverse lookup — suggest categories matching a search phrase: eBay live; Poshmark, Mercari, Depop, Grailed, Vinted, Whatnot, Vestiaire, OfferUp, Facebook and Curtsy over their harvested trees. Etsy answers an empty list (browse its tree instead).
        api_response = api_instance.list_taxonomy_suggest(platform)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->list_taxonomy_suggest: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reverse lookup — suggest categories matching a search phrase: eBay live; Poshmark, Mercari, Depop, Grailed, Vinted, Whatnot, Vestiaire, OfferUp, Facebook and Curtsy over their harvested trees. Etsy answers an empty list (browse its tree instead).
        api_response = api_instance.list_taxonomy_suggest(platform, q=q)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->list_taxonomy_suggest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  |
 **q** | **str**|  | [optional]

### Return type

**ListTaxonomySuggestResponse**

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

