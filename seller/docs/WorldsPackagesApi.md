# crossly.WorldsPackagesApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_world_experience_place_package**](WorldsPackagesApi.md#create_world_experience_place_package) | **POST** /v1/worlds/experiences/{experienceId}/places/{placeId}/packages | Insert a copy of a package (default: the newest version, auto-update on).
[**create_world_experience_place_package_update**](WorldsPackagesApi.md#create_world_experience_place_package_update) | **POST** /v1/worlds/experiences/{experienceId}/places/{placeId}/packages/{nodeId}/update | Update a copy to a version (default newest). A copy edited in the place needs force: true (its edits are replaced).
[**create_world_package**](WorldsPackagesApi.md#create_world_package) | **POST** /v1/worlds/packages | Create a package (v1) from one node (place JSON) or from a node in a place — which then becomes copy v1, auto-updating.
[**create_world_package_toolbox**](WorldsPackagesApi.md#create_world_package_toolbox) | **POST** /v1/worlds/packages/{packageId}/toolbox | List the latest version in the Toolbox as an asset of kind package (Toolbox review and pricing rules apply).
[**create_world_package_version**](WorldsPackagesApi.md#create_world_package_version) | **POST** /v1/worlds/packages/{packageId}/versions | Publish a new version; every auto-updating, unmodified copy in your places is updated through its co-editing session. Returns what happened per place.
[**delete_world_package**](WorldsPackagesApi.md#delete_world_package) | **DELETE** /v1/worlds/packages/{packageId} | Archive a package. Copies in places keep working; they just stop receiving updates.
[**get_world_package**](WorldsPackagesApi.md#get_world_package) | **GET** /v1/worlds/packages/{packageId} | A package with its versions.
[**get_world_package_version**](WorldsPackagesApi.md#get_world_package_version) | **GET** /v1/worlds/packages/{packageId}/versions/{number} | One version, with its payload (one root node in place JSON).
[**list_world_experience_place_packages**](WorldsPackagesApi.md#list_world_experience_place_packages) | **GET** /v1/worlds/experiences/{experienceId}/places/{placeId}/packages | Package copies in a place: version, newest version, modified, auto-update.
[**list_world_packages**](WorldsPackagesApi.md#list_world_packages) | **GET** /v1/worlds/packages | Your package library: reusable models and modules, newest first, with how many places hold copies.
[**update_world_experience_place_package**](WorldsPackagesApi.md#update_world_experience_place_package) | **PATCH** /v1/worlds/experiences/{experienceId}/places/{placeId}/packages/{nodeId} | Turn auto-update on or off for one copy.
[**update_world_package**](WorldsPackagesApi.md#update_world_package) | **PATCH** /v1/worlds/packages/{packageId} | Rename a package or change its description.


# **create_world_experience_place_package**
> CreateWorldExperiencePlacePackageResponse create_world_experience_place_package(experience_id, place_id)

Insert a copy of a package (default: the newest version, auto-update on).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.world.create_world_experience_place_package_response import CreateWorldExperiencePlacePackageResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)
    experience_id = "experienceId_example" # str | 
    place_id = "placeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Insert a copy of a package (default: the newest version, auto-update on).
        api_response = api_instance.create_world_experience_place_package(experience_id, place_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->create_world_experience_place_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **place_id** | **str**|  |

### Return type

**CreateWorldExperiencePlacePackageResponse**

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

# **create_world_experience_place_package_update**
> CreateWorldExperiencePlacePackageUpdateResponse create_world_experience_place_package_update(experience_id, place_id, node_id)

Update a copy to a version (default newest). A copy edited in the place needs force: true (its edits are replaced).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.world.create_world_experience_place_package_update_response import CreateWorldExperiencePlacePackageUpdateResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)
    experience_id = "experienceId_example" # str | 
    place_id = "placeId_example" # str | 
    node_id = "nodeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update a copy to a version (default newest). A copy edited in the place needs force: true (its edits are replaced).
        api_response = api_instance.create_world_experience_place_package_update(experience_id, place_id, node_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->create_world_experience_place_package_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **place_id** | **str**|  |
 **node_id** | **str**|  |

### Return type

**CreateWorldExperiencePlacePackageUpdateResponse**

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

# **create_world_package**
> GetWorldPackageResponse create_world_package()

Create a package (v1) from one node (place JSON) or from a node in a place — which then becomes copy v1, auto-updating.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_package_response import GetWorldPackageResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a package (v1) from one node (place JSON) or from a node in a place — which then becomes copy v1, auto-updating.
        api_response = api_instance.create_world_package()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->create_world_package: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorldPackageResponse**

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

# **create_world_package_toolbox**
> CreateWorldPackageToolboxResponse create_world_package_toolbox(package_id)

List the latest version in the Toolbox as an asset of kind package (Toolbox review and pricing rules apply).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_package_toolbox_response import CreateWorldPackageToolboxResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)
    package_id = "packageId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List the latest version in the Toolbox as an asset of kind package (Toolbox review and pricing rules apply).
        api_response = api_instance.create_world_package_toolbox(package_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->create_world_package_toolbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**|  |

### Return type

**CreateWorldPackageToolboxResponse**

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

# **create_world_package_version**
> CreateWorldPackageVersionResponse create_world_package_version(package_id)

Publish a new version; every auto-updating, unmodified copy in your places is updated through its co-editing session. Returns what happened per place.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_package_version_response import CreateWorldPackageVersionResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)
    package_id = "packageId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Publish a new version; every auto-updating, unmodified copy in your places is updated through its co-editing session. Returns what happened per place.
        api_response = api_instance.create_world_package_version(package_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->create_world_package_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**|  |

### Return type

**CreateWorldPackageVersionResponse**

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

# **delete_world_package**
> DeleteWorldPackageResponse delete_world_package(package_id)

Archive a package. Copies in places keep working; they just stop receiving updates.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.common.error import Error
from crossly.model.world.delete_world_package_response import DeleteWorldPackageResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)
    package_id = "packageId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Archive a package. Copies in places keep working; they just stop receiving updates.
        api_response = api_instance.delete_world_package(package_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->delete_world_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**|  |

### Return type

**DeleteWorldPackageResponse**

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

# **get_world_package**
> GetWorldPackageResponse get_world_package(package_id)

A package with its versions.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_package_response import GetWorldPackageResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)
    package_id = "packageId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A package with its versions.
        api_response = api_instance.get_world_package(package_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->get_world_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**|  |

### Return type

**GetWorldPackageResponse**

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

# **get_world_package_version**
> GetWorldPackageVersionResponse get_world_package_version(package_id, number)

One version, with its payload (one root node in place JSON).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.world.get_world_package_version_response import GetWorldPackageVersionResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)
    package_id = "packageId_example" # str | 
    number = "number_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One version, with its payload (one root node in place JSON).
        api_response = api_instance.get_world_package_version(package_id, number)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->get_world_package_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**|  |
 **number** | **str**|  |

### Return type

**GetWorldPackageVersionResponse**

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

# **list_world_experience_place_packages**
> ListWorldExperiencePlacePackagesResponse list_world_experience_place_packages(experience_id, place_id)

Package copies in a place: version, newest version, modified, auto-update.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.world.list_world_experience_place_packages_response import ListWorldExperiencePlacePackagesResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)
    experience_id = "experienceId_example" # str | 
    place_id = "placeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Package copies in a place: version, newest version, modified, auto-update.
        api_response = api_instance.list_world_experience_place_packages(experience_id, place_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->list_world_experience_place_packages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **place_id** | **str**|  |

### Return type

**ListWorldExperiencePlacePackagesResponse**

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

# **list_world_packages**
> ListWorldPackagesResponse list_world_packages()

Your package library: reusable models and modules, newest first, with how many places hold copies.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_packages_response import ListWorldPackagesResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your package library: reusable models and modules, newest first, with how many places hold copies.
        api_response = api_instance.list_world_packages()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->list_world_packages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorldPackagesResponse**

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

# **update_world_experience_place_package**
> UpdateWorldExperiencePlacePackageResponse update_world_experience_place_package(experience_id, place_id, node_id)

Turn auto-update on or off for one copy.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.world.update_world_experience_place_package_response import UpdateWorldExperiencePlacePackageResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)
    experience_id = "experienceId_example" # str | 
    place_id = "placeId_example" # str | 
    node_id = "nodeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Turn auto-update on or off for one copy.
        api_response = api_instance.update_world_experience_place_package(experience_id, place_id, node_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->update_world_experience_place_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **place_id** | **str**|  |
 **node_id** | **str**|  |

### Return type

**UpdateWorldExperiencePlacePackageResponse**

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

# **update_world_package**
> DeleteWorldPackageResponse update_world_package(package_id)

Rename a package or change its description.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_packages_api
from crossly.model.common.error import Error
from crossly.model.world.delete_world_package_response import DeleteWorldPackageResponse
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
    api_instance = worlds_packages_api.WorldsPackagesApi(api_client)
    package_id = "packageId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Rename a package or change its description.
        api_response = api_instance.update_world_package(package_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsPackagesApi->update_world_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**|  |

### Return type

**DeleteWorldPackageResponse**

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

