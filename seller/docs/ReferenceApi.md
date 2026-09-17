# crossly.ReferenceApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_brand**](ReferenceApi.md#get_brand) | **GET** /v1/brands | Search the Crossly brand index. Returns up to 50 matches.
[**get_category**](ReferenceApi.md#get_category) | **GET** /v1/categories | List Crossly&#39;s canonical category tree.
[**get_department**](ReferenceApi.md#get_department) | **GET** /v1/departments | Search the eBay-sourced \&quot;Department\&quot; item-specific values.
[**get_gender**](ReferenceApi.md#get_gender) | **GET** /v1/genders | Search the eBay-sourced \&quot;Gender\&quot; item-specific values.
[**get_pattern**](ReferenceApi.md#get_pattern) | **GET** /v1/patterns | Search the eBay-sourced \&quot;Pattern\&quot; item-specific values.
[**get_size_system**](ReferenceApi.md#get_size_system) | **GET** /v1/size-systems | Search the Poshmark + Vestiaire size-system union (US/UK/EU/AU/FR/KR).
[**get_style**](ReferenceApi.md#get_style) | **GET** /v1/styles | Search the eBay-sourced \&quot;Style\&quot; item-specific values.
[**get_type**](ReferenceApi.md#get_type) | **GET** /v1/types | Search the eBay-sourced \&quot;Type\&quot; item-specific values.


# **get_brand**
> GetBrandResponse get_brand()

Search the Crossly brand index. Returns up to 50 matches.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import reference_api
from crossly.model.error import Error
from crossly.model.get_brand_response import GetBrandResponse
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
    api_instance = reference_api.ReferenceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Search the Crossly brand index. Returns up to 50 matches.
        api_response = api_instance.get_brand()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReferenceApi->get_brand: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBrandResponse**](GetBrandResponse.md)

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

# **get_category**
> GetCategoryResponse get_category()

List Crossly's canonical category tree.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import reference_api
from crossly.model.get_category_response import GetCategoryResponse
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
    api_instance = reference_api.ReferenceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Crossly's canonical category tree.
        api_response = api_instance.get_category()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReferenceApi->get_category: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCategoryResponse**](GetCategoryResponse.md)

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

# **get_department**
> GetDepartmentResponse get_department()

Search the eBay-sourced \"Department\" item-specific values.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import reference_api
from crossly.model.get_department_response import GetDepartmentResponse
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
    api_instance = reference_api.ReferenceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Search the eBay-sourced \"Department\" item-specific values.
        api_response = api_instance.get_department()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReferenceApi->get_department: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDepartmentResponse**](GetDepartmentResponse.md)

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

# **get_gender**
> GetGenderResponse get_gender()

Search the eBay-sourced \"Gender\" item-specific values.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import reference_api
from crossly.model.get_gender_response import GetGenderResponse
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
    api_instance = reference_api.ReferenceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Search the eBay-sourced \"Gender\" item-specific values.
        api_response = api_instance.get_gender()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReferenceApi->get_gender: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetGenderResponse**](GetGenderResponse.md)

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

# **get_pattern**
> GetPatternResponse get_pattern()

Search the eBay-sourced \"Pattern\" item-specific values.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import reference_api
from crossly.model.get_pattern_response import GetPatternResponse
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
    api_instance = reference_api.ReferenceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Search the eBay-sourced \"Pattern\" item-specific values.
        api_response = api_instance.get_pattern()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReferenceApi->get_pattern: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPatternResponse**](GetPatternResponse.md)

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

# **get_size_system**
> GetSizeSystemResponse get_size_system()

Search the Poshmark + Vestiaire size-system union (US/UK/EU/AU/FR/KR).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import reference_api
from crossly.model.get_size_system_response import GetSizeSystemResponse
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
    api_instance = reference_api.ReferenceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Search the Poshmark + Vestiaire size-system union (US/UK/EU/AU/FR/KR).
        api_response = api_instance.get_size_system()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReferenceApi->get_size_system: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSizeSystemResponse**](GetSizeSystemResponse.md)

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

# **get_style**
> GetStyleResponse get_style()

Search the eBay-sourced \"Style\" item-specific values.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import reference_api
from crossly.model.error import Error
from crossly.model.get_style_response import GetStyleResponse
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
    api_instance = reference_api.ReferenceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Search the eBay-sourced \"Style\" item-specific values.
        api_response = api_instance.get_style()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReferenceApi->get_style: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetStyleResponse**](GetStyleResponse.md)

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

# **get_type**
> GetTypeResponse get_type()

Search the eBay-sourced \"Type\" item-specific values.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import reference_api
from crossly.model.error import Error
from crossly.model.get_type_response import GetTypeResponse
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
    api_instance = reference_api.ReferenceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Search the eBay-sourced \"Type\" item-specific values.
        api_response = api_instance.get_type()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ReferenceApi->get_type: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetTypeResponse**](GetTypeResponse.md)

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

