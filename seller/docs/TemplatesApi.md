# crossly.TemplatesApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_me_template**](TemplatesApi.md#create_me_template) | **POST** /v1/me/templates | Create a template.
[**create_me_template_import**](TemplatesApi.md#create_me_template_import) | **POST** /v1/me/templates/import | Bulk-create templates from an exported payload.
[**create_me_template_render**](TemplatesApi.md#create_me_template_render) | **POST** /v1/me/templates/{id}/render | Render a template&#39;s title + description against a context.
[**create_me_template_share**](TemplatesApi.md#create_me_template_share) | **POST** /v1/me/templates/{id}/share | Mint or return an existing share token for a template.
[**delete_me_template**](TemplatesApi.md#delete_me_template) | **DELETE** /v1/me/templates/{id} | Delete a template.
[**delete_me_template_share**](TemplatesApi.md#delete_me_template_share) | **DELETE** /v1/me/templates/{id}/share | Revoke a template share link.
[**get_me_template**](TemplatesApi.md#get_me_template) | **GET** /v1/me/templates/{id} | Fetch one template in full.
[**get_me_template_suggest**](TemplatesApi.md#get_me_template_suggest) | **GET** /v1/me/templates/suggest | The seller&#39;s default template for a category.
[**list_me_templates**](TemplatesApi.md#list_me_templates) | **GET** /v1/me/templates | List the seller&#39;s templates.
[**update_me_template**](TemplatesApi.md#update_me_template) | **PATCH** /v1/me/templates/{id} | Patch a template.


# **create_me_template**
> CreateMeTemplateResponse create_me_template()

Create a template.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import templates_api
from crossly.model.error import Error
from crossly.model.create_me_template_response import CreateMeTemplateResponse
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
    api_instance = templates_api.TemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a template.
        api_response = api_instance.create_me_template()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TemplatesApi->create_me_template: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateMeTemplateResponse**](CreateMeTemplateResponse.md)

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

# **create_me_template_import**
> CreateMeTemplateImportResponse create_me_template_import()

Bulk-create templates from an exported payload.

Accepts one template object or an array of them. Entries that fail validation are SKIPPED rather than failing the batch — an import is usually someone else's export, and rejecting fifty good templates over one bad row helps nobody. The response reports how many landed, so a short count is visible rather than silent.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import templates_api
from crossly.model.error import Error
from crossly.model.create_me_template_import_response import CreateMeTemplateImportResponse
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
    api_instance = templates_api.TemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk-create templates from an exported payload.
        api_response = api_instance.create_me_template_import()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TemplatesApi->create_me_template_import: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateMeTemplateImportResponse**](CreateMeTemplateImportResponse.md)

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

# **create_me_template_render**
> CreateMeTemplateRenderResponse create_me_template_render(id)

Render a template's title + description against a context.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import templates_api
from crossly.model.error import Error
from crossly.model.create_me_template_render_response import CreateMeTemplateRenderResponse
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Render a template's title + description against a context.
        api_response = api_instance.create_me_template_render(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TemplatesApi->create_me_template_render: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**CreateMeTemplateRenderResponse**](CreateMeTemplateRenderResponse.md)

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

# **create_me_template_share**
> CreateMeTemplateShareResponse create_me_template_share(id)

Mint or return an existing share token for a template.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import templates_api
from crossly.model.create_me_template_share_response import CreateMeTemplateShareResponse
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Mint or return an existing share token for a template.
        api_response = api_instance.create_me_template_share(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TemplatesApi->create_me_template_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**CreateMeTemplateShareResponse**](CreateMeTemplateShareResponse.md)

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

# **delete_me_template**
> DeleteMeTemplateResponse delete_me_template(id)

Delete a template.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import templates_api
from crossly.model.delete_me_template_response import DeleteMeTemplateResponse
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a template.
        api_response = api_instance.delete_me_template(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TemplatesApi->delete_me_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DeleteMeTemplateResponse**](DeleteMeTemplateResponse.md)

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

# **delete_me_template_share**
> DeleteMeTemplateShareResponse delete_me_template_share(id)

Revoke a template share link.

Clears the share token, so the public link stops resolving. The template itself is untouched. Sharing again mints a NEW token — the old link is dead for good, which is the point of revoking.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import templates_api
from crossly.model.error import Error
from crossly.model.delete_me_template_share_response import DeleteMeTemplateShareResponse
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke a template share link.
        api_response = api_instance.delete_me_template_share(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TemplatesApi->delete_me_template_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DeleteMeTemplateShareResponse**](DeleteMeTemplateShareResponse.md)

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

# **get_me_template**
> GetMeTemplateResponse get_me_template(id)

Fetch one template in full.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import templates_api
from crossly.model.error import Error
from crossly.model.get_me_template_response import GetMeTemplateResponse
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch one template in full.
        api_response = api_instance.get_me_template(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TemplatesApi->get_me_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**GetMeTemplateResponse**](GetMeTemplateResponse.md)

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

# **get_me_template_suggest**
> GetMeTemplateSuggestResponse get_me_template_suggest()

The seller's default template for a category.

Returns { template: null } rather than 404 when the seller has no default for that category — \"no default\" is a normal answer, not an error, and callers hydrate a form from it.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import templates_api
from crossly.model.error import Error
from crossly.model.get_me_template_suggest_response import GetMeTemplateSuggestResponse
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
    api_instance = templates_api.TemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The seller's default template for a category.
        api_response = api_instance.get_me_template_suggest()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TemplatesApi->get_me_template_suggest: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMeTemplateSuggestResponse**](GetMeTemplateSuggestResponse.md)

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

# **list_me_templates**
> bool, date, datetime, dict, float, int, list, str, none_type list_me_templates()

List the seller's templates.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import templates_api
from crossly.model.error import Error
from crossly.model.list_me_templates_item import ListMeTemplatesItem
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
    api_instance = templates_api.TemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List the seller's templates.
        api_response = api_instance.list_me_templates()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TemplatesApi->list_me_templates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **update_me_template**
> UpdateMeTemplateResponse update_me_template(id)

Patch a template.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import templates_api
from crossly.model.error import Error
from crossly.model.update_me_template_response import UpdateMeTemplateResponse
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Patch a template.
        api_response = api_instance.update_me_template(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling TemplatesApi->update_me_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**UpdateMeTemplateResponse**](UpdateMeTemplateResponse.md)

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

