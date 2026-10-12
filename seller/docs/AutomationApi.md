# crossly.AutomationApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_automation_rule**](AutomationApi.md#create_automation_rule) | **POST** /v1/automation/rules | Create an automation rule.
[**create_automation_rule_import**](AutomationApi.md#create_automation_rule_import) | **POST** /v1/automation/rules/import | Import one or more rules from recipe JSON (single or bundle).
[**create_automation_rule_run_now**](AutomationApi.md#create_automation_rule_run_now) | **POST** /v1/automation/rules/{id}/run-now | Fire an automation rule immediately.
[**create_automation_rule_toggle**](AutomationApi.md#create_automation_rule_toggle) | **POST** /v1/automation/rules/{id}/toggle | Flip an automation rule between active and inactive.
[**create_automation_rule_validate_recipe**](AutomationApi.md#create_automation_rule_validate_recipe) | **POST** /v1/automation/rules/validate-recipe | Dry-run validate one or more recipes against the live catalog.
[**create_reprice_event_approve**](AutomationApi.md#create_reprice_event_approve) | **POST** /v1/reprice-events/{id}/approve | Apply a pending reprice proposal: the recorded price goes to the recorded platform listing. Proposals older than three days expire instead.
[**create_reprice_event_skip**](AutomationApi.md#create_reprice_event_skip) | **POST** /v1/reprice-events/{id}/skip | Skip a pending reprice proposal; the price stays as it is.
[**delete_automation_rule**](AutomationApi.md#delete_automation_rule) | **DELETE** /v1/automation/rules/{id} | Delete an automation rule.
[**get_automation_catalog**](AutomationApi.md#get_automation_catalog) | **GET** /v1/automation/catalog | Supported triggerType / actionType / conditionType values for automation rules.
[**get_automation_rule**](AutomationApi.md#get_automation_rule) | **GET** /v1/automation/rules/{id} | Get a single automation rule.
[**get_automation_rule_export**](AutomationApi.md#get_automation_rule_export) | **GET** /v1/automation/rules/export | Export the user&#39;s full rule library as a portable recipe bundle.
[**get_automation_rule_export_by_id**](AutomationApi.md#get_automation_rule_export_by_id) | **GET** /v1/automation/rules/{id}/export | Export a single automation rule as a portable recipe.
[**list_automation_rules**](AutomationApi.md#list_automation_rules) | **GET** /v1/automation/rules | List automation rules.
[**list_automation_runs**](AutomationApi.md#list_automation_runs) | **GET** /v1/automation/runs | Per-fire history for automation rules and workflow chain runs.
[**list_reprice_events**](AutomationApi.md#list_reprice_events) | **GET** /v1/reprice-events | Reprice decisions, newest first: applied, held at a floor, or pending approval (pending&#x3D;true for only those waiting).
[**update_automation_rule**](AutomationApi.md#update_automation_rule) | **PUT** /v1/automation/rules/{id} | Update an automation rule (full replace).


# **create_automation_rule**
> ListAutomationRulesItem create_automation_rule()

Create an automation rule.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.automation.list_automation_rules_item import ListAutomationRulesItem
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
    api_instance = automation_api.AutomationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create an automation rule.
        api_response = api_instance.create_automation_rule()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->create_automation_rule: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListAutomationRulesItem**

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

# **create_automation_rule_import**
> CreateAutomationRuleImportResponse create_automation_rule_import()

Import one or more rules from recipe JSON (single or bundle).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.common.error import Error
from crossly.model.automation.create_automation_rule_import_response import CreateAutomationRuleImportResponse
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
    api_instance = automation_api.AutomationApi(api_client)
    activate = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import one or more rules from recipe JSON (single or bundle).
        api_response = api_instance.create_automation_rule_import(activate=activate)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->create_automation_rule_import: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

**CreateAutomationRuleImportResponse**

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

# **create_automation_rule_run_now**
> CreateAutomationRuleRunNowResponse create_automation_rule_run_now(id)

Fire an automation rule immediately.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.automation.create_automation_rule_run_now_response import CreateAutomationRuleRunNowResponse
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
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fire an automation rule immediately.
        api_response = api_instance.create_automation_rule_run_now(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->create_automation_rule_run_now: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateAutomationRuleRunNowResponse**

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

# **create_automation_rule_toggle**
> UpdateAutomationRuleResponse create_automation_rule_toggle(id)

Flip an automation rule between active and inactive.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.automation.update_automation_rule_response import UpdateAutomationRuleResponse
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
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Flip an automation rule between active and inactive.
        api_response = api_instance.create_automation_rule_toggle(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->create_automation_rule_toggle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateAutomationRuleResponse**

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

# **create_automation_rule_validate_recipe**
> CreateAutomationRuleValidateRecipeResponse create_automation_rule_validate_recipe()

Dry-run validate one or more recipes against the live catalog.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.automation.create_automation_rule_validate_recipe_response import CreateAutomationRuleValidateRecipeResponse
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
    api_instance = automation_api.AutomationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Dry-run validate one or more recipes against the live catalog.
        api_response = api_instance.create_automation_rule_validate_recipe()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->create_automation_rule_validate_recipe: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateAutomationRuleValidateRecipeResponse**

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

# **create_reprice_event_approve**
> CreateRepriceEventSkipResponse create_reprice_event_approve(id)

Apply a pending reprice proposal: the recorded price goes to the recorded platform listing. Proposals older than three days expire instead.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.common.create_reprice_event_skip_response import CreateRepriceEventSkipResponse
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
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Apply a pending reprice proposal: the recorded price goes to the recorded platform listing. Proposals older than three days expire instead.
        api_response = api_instance.create_reprice_event_approve(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->create_reprice_event_approve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateRepriceEventSkipResponse**

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

# **create_reprice_event_skip**
> CreateRepriceEventSkipResponse create_reprice_event_skip(id)

Skip a pending reprice proposal; the price stays as it is.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.common.create_reprice_event_skip_response import CreateRepriceEventSkipResponse
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
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Skip a pending reprice proposal; the price stays as it is.
        api_response = api_instance.create_reprice_event_skip(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->create_reprice_event_skip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateRepriceEventSkipResponse**

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

# **delete_automation_rule**
> OkResponse delete_automation_rule(id)

Delete an automation rule.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
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
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an automation rule.
        api_response = api_instance.delete_automation_rule(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->delete_automation_rule: %s\n" % e)
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

# **get_automation_catalog**
> GetAutomationCatalogResponse get_automation_catalog()

Supported triggerType / actionType / conditionType values for automation rules.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.common.error import Error
from crossly.model.automation.get_automation_catalog_response import GetAutomationCatalogResponse
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
    api_instance = automation_api.AutomationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Supported triggerType / actionType / conditionType values for automation rules.
        api_response = api_instance.get_automation_catalog()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->get_automation_catalog: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetAutomationCatalogResponse**

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

# **get_automation_rule**
> GetAutomationRuleResponse get_automation_rule(id)

Get a single automation rule.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.common.error import Error
from crossly.model.automation.get_automation_rule_response import GetAutomationRuleResponse
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
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a single automation rule.
        api_response = api_instance.get_automation_rule(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->get_automation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetAutomationRuleResponse**

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

# **get_automation_rule_export**
> GetAutomationRuleExportResponse get_automation_rule_export()

Export the user's full rule library as a portable recipe bundle.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.common.error import Error
from crossly.model.automation.get_automation_rule_export_response import GetAutomationRuleExportResponse
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
    api_instance = automation_api.AutomationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Export the user's full rule library as a portable recipe bundle.
        api_response = api_instance.get_automation_rule_export()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->get_automation_rule_export: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetAutomationRuleExportResponse**

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

# **get_automation_rule_export_by_id**
> GetAutomationRuleExportByIdResponse get_automation_rule_export_by_id(id)

Export a single automation rule as a portable recipe.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.common.error import Error
from crossly.model.automation.get_automation_rule_export_by_id_response import GetAutomationRuleExportByIdResponse
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
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Export a single automation rule as a portable recipe.
        api_response = api_instance.get_automation_rule_export_by_id(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->get_automation_rule_export_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetAutomationRuleExportByIdResponse**

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

# **list_automation_rules**
> ListAutomationRulesResponse list_automation_rules()

List automation rules.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.common.error import Error
from crossly.model.automation.list_automation_rules_response import ListAutomationRulesResponse
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
    api_instance = automation_api.AutomationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List automation rules.
        api_response = api_instance.list_automation_rules()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->list_automation_rules: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListAutomationRulesResponse**

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

# **list_automation_runs**
> ListAutomationRunsResponse list_automation_runs()

Per-fire history for automation rules and workflow chain runs.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.automation.list_automation_runs_response import ListAutomationRunsResponse
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
    api_instance = automation_api.AutomationApi(api_client)
    rule_id = "ruleId_example" # str |  (optional)
    chain_id = "chainId_example" # str |  (optional)
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Per-fire history for automation rules and workflow chain runs.
        api_response = api_instance.list_automation_runs(rule_id=rule_id, chain_id=chain_id, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->list_automation_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | [optional]
 **chain_id** | **str**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

**ListAutomationRunsResponse**

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

# **list_reprice_events**
> ListRepriceEventsResponse list_reprice_events()

Reprice decisions, newest first: applied, held at a floor, or pending approval (pending=true for only those waiting).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.common.list_reprice_events_response import ListRepriceEventsResponse
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
    api_instance = automation_api.AutomationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Reprice decisions, newest first: applied, held at a floor, or pending approval (pending=true for only those waiting).
        api_response = api_instance.list_reprice_events()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->list_reprice_events: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListRepriceEventsResponse**

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

# **update_automation_rule**
> UpdateAutomationRuleResponse update_automation_rule(id)

Update an automation rule (full replace).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import automation_api
from crossly.model.automation.update_automation_rule_response import UpdateAutomationRuleResponse
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
    api_instance = automation_api.AutomationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update an automation rule (full replace).
        api_response = api_instance.update_automation_rule(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AutomationApi->update_automation_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateAutomationRuleResponse**

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

