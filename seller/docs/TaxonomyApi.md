# crossly.TaxonomyApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_taxonomy_category**](TaxonomyApi.md#get_taxonomy_category) | **GET** /v1/taxonomy/{platform}/categories | Categories for a platform. Default is top-level; pass &#x60;?parent&#x3D;&lt;categoryId&gt;&#x60; to drill down one level (supported on cookie platforms whose recipe returns flat parent_id-linked rows).
[**get_taxonomy_category_aspect**](TaxonomyApi.md#get_taxonomy_category_aspect) | **GET** /v1/taxonomy/{platform}/categories/{id}/aspects | Item-specific aspects (eBay) / properties (Etsy) / hard-coded enums (cookie platforms) for a category.
[**get_taxonomy_category_children**](TaxonomyApi.md#get_taxonomy_category_children) | **GET** /v1/taxonomy/{platform}/categories/{id}/children | Direct children of a category node.
[**get_taxonomy_required_field**](TaxonomyApi.md#get_taxonomy_required_field) | **GET** /v1/taxonomy/{platform}/required-fields | Normalized field schema the seller needs to fill before crossposting to this platform. Combines master fields (title/description/price/condition) with platform-specific overrides.
[**list_taxonomy_suggest**](TaxonomyApi.md#list_taxonomy_suggest) | **GET** /v1/taxonomy/{platform}/suggest | Reverse lookup — suggest categories matching a search phrase. eBay-only today.


# **get_taxonomy_category**
> GetTaxonomyCategoryResponse get_taxonomy_category(platform)

Categories for a platform. Default is top-level; pass `?parent=<categoryId>` to drill down one level (supported on cookie platforms whose recipe returns flat parent_id-linked rows).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.get_taxonomy_category_response import GetTaxonomyCategoryResponse
from crossly.model.error import Error
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

[**GetTaxonomyCategoryResponse**](GetTaxonomyCategoryResponse.md)

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

# **get_taxonomy_category_aspect**
> GetTaxonomyCategoryAspectResponse get_taxonomy_category_aspect(platform, id)

Item-specific aspects (eBay) / properties (Etsy) / hard-coded enums (cookie platforms) for a category.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.get_taxonomy_category_aspect_response import GetTaxonomyCategoryAspectResponse
from crossly.model.error import Error
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

[**GetTaxonomyCategoryAspectResponse**](GetTaxonomyCategoryAspectResponse.md)

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

# **get_taxonomy_category_children**
> GetTaxonomyCategoryChildrenResponse get_taxonomy_category_children(platform, id)

Direct children of a category node.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.get_taxonomy_category_children_response import GetTaxonomyCategoryChildrenResponse
from crossly.model.error import Error
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

[**GetTaxonomyCategoryChildrenResponse**](GetTaxonomyCategoryChildrenResponse.md)

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

# **get_taxonomy_required_field**
> GetTaxonomyRequiredFieldResponse get_taxonomy_required_field(platform)

Normalized field schema the seller needs to fill before crossposting to this platform. Combines master fields (title/description/price/condition) with platform-specific overrides.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.error import Error
from crossly.model.get_taxonomy_required_field_response import GetTaxonomyRequiredFieldResponse
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

[**GetTaxonomyRequiredFieldResponse**](GetTaxonomyRequiredFieldResponse.md)

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

# **list_taxonomy_suggest**
> bool, date, datetime, dict, float, int, list, str, none_type list_taxonomy_suggest(platform)

Reverse lookup — suggest categories matching a search phrase. eBay-only today.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import taxonomy_api
from crossly.model.list_taxonomy_suggest_item import ListTaxonomySuggestItem
from crossly.model.error import Error
from crossly.model.v1_list import V1List
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
        # Reverse lookup — suggest categories matching a search phrase. eBay-only today.
        api_response = api_instance.list_taxonomy_suggest(platform)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TaxonomyApi->list_taxonomy_suggest: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reverse lookup — suggest categories matching a search phrase. eBay-only today.
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

**bool, date, datetime, dict, float, int, list, str, none_type**

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

