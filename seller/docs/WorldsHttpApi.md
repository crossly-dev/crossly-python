# crossly.WorldsHttpApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_world_experience_http_domain**](WorldsHttpApi.md#create_world_experience_http_domain) | **POST** /v1/worlds/experiences/{experienceId}/http/domains | Declare a domain server scripts may call (example.com or *.example.com). It is reviewed by a person before it works.
[**delete_world_experience_http_domain**](WorldsHttpApi.md#delete_world_experience_http_domain) | **DELETE** /v1/worlds/experiences/{experienceId}/http/domains/{domainId} | Remove a domain: scripts lose access at once.
[**delete_world_experience_http_secret**](WorldsHttpApi.md#delete_world_experience_http_secret) | **DELETE** /v1/worlds/experiences/{experienceId}/http/secrets/{name} | Delete a secret.
[**get_world_experience_http**](WorldsHttpApi.md#get_world_experience_http) | **GET** /v1/worlds/experiences/{experienceId}/http | Http settings: declared domains with their review state, secret names (never values), limits and rules.
[**update_world_experience_http_secret**](WorldsHttpApi.md#update_world_experience_http_secret) | **PUT** /v1/worlds/experiences/{experienceId}/http/secrets/{name} | Set a secret (UPPER_SNAKE name). Scripts reference it as Http.secret(\&quot;NAME\&quot;); the value is never returned.


# **create_world_experience_http_domain**
> CreateWorldExperienceHttpDomainResponse create_world_experience_http_domain(experience_id)

Declare a domain server scripts may call (example.com or *.example.com). It is reviewed by a person before it works.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_http_api
from crossly.model.world.create_world_experience_http_domain_response import CreateWorldExperienceHttpDomainResponse
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
    api_instance = worlds_http_api.WorldsHttpApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Declare a domain server scripts may call (example.com or *.example.com). It is reviewed by a person before it works.
        api_response = api_instance.create_world_experience_http_domain(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsHttpApi->create_world_experience_http_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**CreateWorldExperienceHttpDomainResponse**

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

# **delete_world_experience_http_domain**
> DeleteSpatialSceneGrantResponse delete_world_experience_http_domain(experience_id, domain_id)

Remove a domain: scripts lose access at once.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_http_api
from crossly.model.common.error import Error
from crossly.model.spatial.delete_spatial_scene_grant_response import DeleteSpatialSceneGrantResponse
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
    api_instance = worlds_http_api.WorldsHttpApi(api_client)
    experience_id = "experienceId_example" # str | 
    domain_id = "domainId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove a domain: scripts lose access at once.
        api_response = api_instance.delete_world_experience_http_domain(experience_id, domain_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsHttpApi->delete_world_experience_http_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **domain_id** | **str**|  |

### Return type

**DeleteSpatialSceneGrantResponse**

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

# **delete_world_experience_http_secret**
> DeleteSpatialSceneGrantResponse delete_world_experience_http_secret(experience_id, name)

Delete a secret.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_http_api
from crossly.model.common.error import Error
from crossly.model.spatial.delete_spatial_scene_grant_response import DeleteSpatialSceneGrantResponse
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
    api_instance = worlds_http_api.WorldsHttpApi(api_client)
    experience_id = "experienceId_example" # str | 
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a secret.
        api_response = api_instance.delete_world_experience_http_secret(experience_id, name)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsHttpApi->delete_world_experience_http_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **name** | **str**|  |

### Return type

**DeleteSpatialSceneGrantResponse**

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

# **get_world_experience_http**
> GetWorldExperienceHttpResponse get_world_experience_http(experience_id)

Http settings: declared domains with their review state, secret names (never values), limits and rules.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_http_api
from crossly.model.world.get_world_experience_http_response import GetWorldExperienceHttpResponse
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
    api_instance = worlds_http_api.WorldsHttpApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Http settings: declared domains with their review state, secret names (never values), limits and rules.
        api_response = api_instance.get_world_experience_http(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsHttpApi->get_world_experience_http: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**GetWorldExperienceHttpResponse**

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

# **update_world_experience_http_secret**
> UpdateWorldExperienceHttpSecretResponse update_world_experience_http_secret(experience_id, name)

Set a secret (UPPER_SNAKE name). Scripts reference it as Http.secret(\"NAME\"); the value is never returned.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_http_api
from crossly.model.world.update_world_experience_http_secret_response import UpdateWorldExperienceHttpSecretResponse
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
    api_instance = worlds_http_api.WorldsHttpApi(api_client)
    experience_id = "experienceId_example" # str | 
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set a secret (UPPER_SNAKE name). Scripts reference it as Http.secret(\"NAME\"); the value is never returned.
        api_response = api_instance.update_world_experience_http_secret(experience_id, name)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsHttpApi->update_world_experience_http_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **name** | **str**|  |

### Return type

**UpdateWorldExperienceHttpSecretResponse**

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

