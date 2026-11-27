# crossly.WorldsDataApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_world_experience_datastore_entry_increment**](WorldsDataApi.md#create_world_experience_datastore_entry_increment) | **POST** /v1/worlds/experiences/{experienceId}/datastores/{store}/entries/{key}/increment | Atomically add &#x60;by&#x60; to a numeric key (absent counts as 0).
[**create_world_experience_memory_queue_item**](WorldsDataApi.md#create_world_experience_memory_queue_item) | **POST** /v1/worlds/experiences/{experienceId}/memory/queues/{queue}/items | Add an item to a MemoryStore queue (ttlSeconds ≤ 45 days, priority 0-1000).
[**create_world_experience_memory_queue_read**](WorldsDataApi.md#create_world_experience_memory_queue_read) | **POST** /v1/worlds/experiences/{experienceId}/memory/queues/{queue}/read | Read and hide up to &#x60;count&#x60; queue items for invisibilitySeconds; remove them with the readId.
[**create_world_experience_messaging**](WorldsDataApi.md#create_world_experience_messaging) | **POST** /v1/worlds/experiences/{experienceId}/messaging/{topic} | Publish a message (≤ 1 KB) to every live server of the experience subscribed to the topic.
[**create_world_experience_ordered_entry_increment**](WorldsDataApi.md#create_world_experience_ordered_entry_increment) | **POST** /v1/worlds/experiences/{experienceId}/ordered/{store}/entries/{key}/increment | Atomically add &#x60;by&#x60; to an OrderedStore entry.
[**delete_world_experience_datastore_entry**](WorldsDataApi.md#delete_world_experience_datastore_entry) | **DELETE** /v1/worlds/experiences/{experienceId}/datastores/{store}/entries/{key} | Remove a key (a tombstone version; history stays readable for 30 days). Honours If-Match.
[**delete_world_experience_memory_map**](WorldsDataApi.md#delete_world_experience_memory_map) | **DELETE** /v1/worlds/experiences/{experienceId}/memory/maps/{map}/{key} | Remove a hash map item.
[**delete_world_experience_memory_queue_read**](WorldsDataApi.md#delete_world_experience_memory_queue_read) | **DELETE** /v1/worlds/experiences/{experienceId}/memory/queues/{queue}/reads/{readId} | Remove the items of one read (409 if the read lapsed).
[**delete_world_experience_memory_sorted**](WorldsDataApi.md#delete_world_experience_memory_sorted) | **DELETE** /v1/worlds/experiences/{experienceId}/memory/sorted/{map}/{key} | Remove a sorted map item.
[**delete_world_experience_ordered_entry**](WorldsDataApi.md#delete_world_experience_ordered_entry) | **DELETE** /v1/worlds/experiences/{experienceId}/ordered/{store}/entries/{key} | Remove an OrderedStore entry.
[**get_world_experience_data_usage**](WorldsDataApi.md#get_world_experience_data_usage) | **GET** /v1/worlds/experiences/{experienceId}/data/usage | Live quotas and usage: CCU, request budgets per minute, DataStore storage, MemoryStore memory.
[**get_world_experience_datastore_entry**](WorldsDataApi.md#get_world_experience_datastore_entry) | **GET** /v1/worlds/experiences/{experienceId}/datastores/{store}/entries/{key} | The current value of a key: version (ETag \&quot;v&lt;n&gt;\&quot;), userIds and attributes.
[**get_world_experience_datastore_entry_version**](WorldsDataApi.md#get_world_experience_datastore_entry_version) | **GET** /v1/worlds/experiences/{experienceId}/datastores/{store}/entries/{key}/versions/{version} | One version of a key, including a removed one.
[**get_world_experience_memory_map**](WorldsDataApi.md#get_world_experience_memory_map) | **GET** /v1/worlds/experiences/{experienceId}/memory/maps/{map} | Items of a MemoryStore hash map (cursor-paged, unordered).
[**get_world_experience_memory_map_by_key**](WorldsDataApi.md#get_world_experience_memory_map_by_key) | **GET** /v1/worlds/experiences/{experienceId}/memory/maps/{map}/{key} | One MemoryStore hash map item with its version and expiry.
[**get_world_experience_memory_queue**](WorldsDataApi.md#get_world_experience_memory_queue) | **GET** /v1/worlds/experiences/{experienceId}/memory/queues/{queue} | Queue length (visible, in flight) and the head, without hiding anything.
[**get_world_experience_memory_sorted**](WorldsDataApi.md#get_world_experience_memory_sorted) | **GET** /v1/worlds/experiences/{experienceId}/memory/sorted/{map} | A MemoryStore sorted map in order (sortKey, then key); ?order&#x3D;&amp;cursor&#x3D;&amp;limit&#x3D;.
[**get_world_experience_memory_sorted_by_key**](WorldsDataApi.md#get_world_experience_memory_sorted_by_key) | **GET** /v1/worlds/experiences/{experienceId}/memory/sorted/{map}/{key} | One sorted map item.
[**get_world_experience_ordered**](WorldsDataApi.md#get_world_experience_ordered) | **GET** /v1/worlds/experiences/{experienceId}/ordered/{store} | An OrderedStore page ranked by value; ?order&#x3D;desc|asc&amp;min&#x3D;&amp;max&#x3D;&amp;cursor&#x3D;&amp;limit&#x3D;.
[**get_world_experience_ordered_entry**](WorldsDataApi.md#get_world_experience_ordered_entry) | **GET** /v1/worlds/experiences/{experienceId}/ordered/{store}/entries/{key} | One OrderedStore entry.
[**list_world_experience_datastore_entries**](WorldsDataApi.md#list_world_experience_datastore_entries) | **GET** /v1/worlds/experiences/{experienceId}/datastores/{store}/entries | Keys of a DataStore in key order; ?prefix&#x3D;&amp;scope&#x3D;&amp;cursor&#x3D;&amp;limit&#x3D;.
[**list_world_experience_datastore_entry_versions**](WorldsDataApi.md#list_world_experience_datastore_entry_versions) | **GET** /v1/worlds/experiences/{experienceId}/datastores/{store}/entries/{key}/versions | Versions of a key, newest first (30-day history; the current version is kept).
[**list_world_experience_datastores**](WorldsDataApi.md#list_world_experience_datastores) | **GET** /v1/worlds/experiences/{experienceId}/datastores | The DataStores of an experience, with key counts and bytes.
[**update_world_experience_datastore_entry**](WorldsDataApi.md#update_world_experience_datastore_entry) | **PUT** /v1/worlds/experiences/{experienceId}/datastores/{store}/entries/{key} | Write a new version. If-Match \&quot;v&lt;n&gt;\&quot; (or ifVersion) writes only at that version; If-None-Match: * only if absent. 412 on a mismatch.
[**update_world_experience_memory_map**](WorldsDataApi.md#update_world_experience_memory_map) | **PUT** /v1/worlds/experiences/{experienceId}/memory/maps/{map}/{key} | Set a hash map item (ttlSeconds required; ifVersion for compare-and-set).
[**update_world_experience_memory_sorted**](WorldsDataApi.md#update_world_experience_memory_sorted) | **PUT** /v1/worlds/experiences/{experienceId}/memory/sorted/{map}/{key} | Set a sorted map item (ttlSeconds, optional sortKey and ifVersion).
[**update_world_experience_ordered_entry**](WorldsDataApi.md#update_world_experience_ordered_entry) | **PUT** /v1/worlds/experiences/{experienceId}/ordered/{store}/entries/{key} | Set an OrderedStore entry to a whole number.


# **create_world_experience_datastore_entry_increment**
> CreateWorldExperienceDatastoreEntryIncrementResponse create_world_experience_datastore_entry_increment(experience_id, store, key)

Atomically add `by` to a numeric key (absent counts as 0).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.world.create_world_experience_datastore_entry_increment_response import CreateWorldExperienceDatastoreEntryIncrementResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Atomically add `by` to a numeric key (absent counts as 0).
        api_response = api_instance.create_world_experience_datastore_entry_increment(experience_id, store, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->create_world_experience_datastore_entry_increment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |
 **key** | **str**|  |

### Return type

**CreateWorldExperienceDatastoreEntryIncrementResponse**

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

# **create_world_experience_memory_queue_item**
> CreateWorldPartyInviteResponse create_world_experience_memory_queue_item(experience_id, queue)

Add an item to a MemoryStore queue (ttlSeconds ≤ 45 days, priority 0-1000).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_party_invite_response import CreateWorldPartyInviteResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    queue = "queue_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Add an item to a MemoryStore queue (ttlSeconds ≤ 45 days, priority 0-1000).
        api_response = api_instance.create_world_experience_memory_queue_item(experience_id, queue)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->create_world_experience_memory_queue_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **queue** | **str**|  |

### Return type

**CreateWorldPartyInviteResponse**

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

# **create_world_experience_memory_queue_read**
> CreateWorldExperienceMemoryQueueReadResponse create_world_experience_memory_queue_read(experience_id, queue)

Read and hide up to `count` queue items for invisibilitySeconds; remove them with the readId.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_experience_memory_queue_read_response import CreateWorldExperienceMemoryQueueReadResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    queue = "queue_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Read and hide up to `count` queue items for invisibilitySeconds; remove them with the readId.
        api_response = api_instance.create_world_experience_memory_queue_read(experience_id, queue)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->create_world_experience_memory_queue_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **queue** | **str**|  |

### Return type

**CreateWorldExperienceMemoryQueueReadResponse**

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

# **create_world_experience_messaging**
> CreateWorldExperienceMessagingResponse create_world_experience_messaging(experience_id, topic)

Publish a message (≤ 1 KB) to every live server of the experience subscribed to the topic.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.create_world_experience_messaging_response import CreateWorldExperienceMessagingResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    topic = "topic_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Publish a message (≤ 1 KB) to every live server of the experience subscribed to the topic.
        api_response = api_instance.create_world_experience_messaging(experience_id, topic)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->create_world_experience_messaging: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **topic** | **str**|  |

### Return type

**CreateWorldExperienceMessagingResponse**

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

# **create_world_experience_ordered_entry_increment**
> WorldExperienceOrderedEntryResponse create_world_experience_ordered_entry_increment(experience_id, store, key)

Atomically add `by` to an OrderedStore entry.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.common.world_experience_ordered_entry_response import WorldExperienceOrderedEntryResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Atomically add `by` to an OrderedStore entry.
        api_response = api_instance.create_world_experience_ordered_entry_increment(experience_id, store, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->create_world_experience_ordered_entry_increment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |
 **key** | **str**|  |

### Return type

**WorldExperienceOrderedEntryResponse**

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

# **delete_world_experience_datastore_entry**
> DeleteWorldExperienceDatastoreEntryResponse delete_world_experience_datastore_entry(experience_id, store, key)

Remove a key (a tombstone version; history stays readable for 30 days). Honours If-Match.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.delete_world_experience_datastore_entry_response import DeleteWorldExperienceDatastoreEntryResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove a key (a tombstone version; history stays readable for 30 days). Honours If-Match.
        api_response = api_instance.delete_world_experience_datastore_entry(experience_id, store, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->delete_world_experience_datastore_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |
 **key** | **str**|  |

### Return type

**DeleteWorldExperienceDatastoreEntryResponse**

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

# **delete_world_experience_memory_map**
> DeleteSpatialSceneGrantResponse delete_world_experience_memory_map(experience_id, map, key)

Remove a hash map item.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    map = "map_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove a hash map item.
        api_response = api_instance.delete_world_experience_memory_map(experience_id, map, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->delete_world_experience_memory_map: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **map** | **str**|  |
 **key** | **str**|  |

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

# **delete_world_experience_memory_queue_read**
> DeleteSpatialSceneNodeResponse delete_world_experience_memory_queue_read(experience_id, queue, read_id)

Remove the items of one read (409 if the read lapsed).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.spatial.delete_spatial_scene_node_response import DeleteSpatialSceneNodeResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    queue = "queue_example" # str | 
    read_id = "readId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove the items of one read (409 if the read lapsed).
        api_response = api_instance.delete_world_experience_memory_queue_read(experience_id, queue, read_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->delete_world_experience_memory_queue_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **queue** | **str**|  |
 **read_id** | **str**|  |

### Return type

**DeleteSpatialSceneNodeResponse**

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

# **delete_world_experience_memory_sorted**
> DeleteSpatialSceneGrantResponse delete_world_experience_memory_sorted(experience_id, map, key)

Remove a sorted map item.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    map = "map_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove a sorted map item.
        api_response = api_instance.delete_world_experience_memory_sorted(experience_id, map, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->delete_world_experience_memory_sorted: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **map** | **str**|  |
 **key** | **str**|  |

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

# **delete_world_experience_ordered_entry**
> DeleteWorldExperienceOrderedEntryResponse delete_world_experience_ordered_entry(experience_id, store, key)

Remove an OrderedStore entry.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.delete_world_experience_ordered_entry_response import DeleteWorldExperienceOrderedEntryResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove an OrderedStore entry.
        api_response = api_instance.delete_world_experience_ordered_entry(experience_id, store, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->delete_world_experience_ordered_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |
 **key** | **str**|  |

### Return type

**DeleteWorldExperienceOrderedEntryResponse**

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

# **get_world_experience_data_usage**
> GetWorldExperienceDataUsageResponse get_world_experience_data_usage(experience_id)

Live quotas and usage: CCU, request budgets per minute, DataStore storage, MemoryStore memory.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_experience_data_usage_response import GetWorldExperienceDataUsageResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Live quotas and usage: CCU, request budgets per minute, DataStore storage, MemoryStore memory.
        api_response = api_instance.get_world_experience_data_usage(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->get_world_experience_data_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**GetWorldExperienceDataUsageResponse**

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

# **get_world_experience_datastore_entry**
> GetWorldExperienceDatastoreEntryResponse get_world_experience_datastore_entry(experience_id, store, key)

The current value of a key: version (ETag \"v<n>\"), userIds and attributes.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_experience_datastore_entry_response import GetWorldExperienceDatastoreEntryResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The current value of a key: version (ETag \"v<n>\"), userIds and attributes.
        api_response = api_instance.get_world_experience_datastore_entry(experience_id, store, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->get_world_experience_datastore_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |
 **key** | **str**|  |

### Return type

**GetWorldExperienceDatastoreEntryResponse**

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

# **get_world_experience_datastore_entry_version**
> GetWorldExperienceDatastoreEntryResponse get_world_experience_datastore_entry_version(experience_id, store, key, version)

One version of a key, including a removed one.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_experience_datastore_entry_response import GetWorldExperienceDatastoreEntryResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 
    key = "key_example" # str | 
    version = "version_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One version of a key, including a removed one.
        api_response = api_instance.get_world_experience_datastore_entry_version(experience_id, store, key, version)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->get_world_experience_datastore_entry_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |
 **key** | **str**|  |
 **version** | **str**|  |

### Return type

**GetWorldExperienceDatastoreEntryResponse**

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

# **get_world_experience_memory_map**
> GetWorldExperienceMemoryMapResponse get_world_experience_memory_map(experience_id, map)

Items of a MemoryStore hash map (cursor-paged, unordered).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_experience_memory_map_response import GetWorldExperienceMemoryMapResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    map = "map_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Items of a MemoryStore hash map (cursor-paged, unordered).
        api_response = api_instance.get_world_experience_memory_map(experience_id, map)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->get_world_experience_memory_map: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **map** | **str**|  |

### Return type

**GetWorldExperienceMemoryMapResponse**

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

# **get_world_experience_memory_map_by_key**
> GetWorldExperienceMemoryMapByKeyResponse get_world_experience_memory_map_by_key(experience_id, map, key)

One MemoryStore hash map item with its version and expiry.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_experience_memory_map_by_key_response import GetWorldExperienceMemoryMapByKeyResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    map = "map_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One MemoryStore hash map item with its version and expiry.
        api_response = api_instance.get_world_experience_memory_map_by_key(experience_id, map, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->get_world_experience_memory_map_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **map** | **str**|  |
 **key** | **str**|  |

### Return type

**GetWorldExperienceMemoryMapByKeyResponse**

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

# **get_world_experience_memory_queue**
> GetWorldExperienceMemoryQueueResponse get_world_experience_memory_queue(experience_id, queue)

Queue length (visible, in flight) and the head, without hiding anything.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_experience_memory_queue_response import GetWorldExperienceMemoryQueueResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    queue = "queue_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Queue length (visible, in flight) and the head, without hiding anything.
        api_response = api_instance.get_world_experience_memory_queue(experience_id, queue)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->get_world_experience_memory_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **queue** | **str**|  |

### Return type

**GetWorldExperienceMemoryQueueResponse**

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

# **get_world_experience_memory_sorted**
> GetWorldExperienceMemoryMapResponse get_world_experience_memory_sorted(experience_id, map)

A MemoryStore sorted map in order (sortKey, then key); ?order=&cursor=&limit=.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_experience_memory_map_response import GetWorldExperienceMemoryMapResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    map = "map_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A MemoryStore sorted map in order (sortKey, then key); ?order=&cursor=&limit=.
        api_response = api_instance.get_world_experience_memory_sorted(experience_id, map)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->get_world_experience_memory_sorted: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **map** | **str**|  |

### Return type

**GetWorldExperienceMemoryMapResponse**

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

# **get_world_experience_memory_sorted_by_key**
> GetWorldExperienceMemoryMapByKeyResponse get_world_experience_memory_sorted_by_key(experience_id, map, key)

One sorted map item.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_experience_memory_map_by_key_response import GetWorldExperienceMemoryMapByKeyResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    map = "map_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One sorted map item.
        api_response = api_instance.get_world_experience_memory_sorted_by_key(experience_id, map, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->get_world_experience_memory_sorted_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **map** | **str**|  |
 **key** | **str**|  |

### Return type

**GetWorldExperienceMemoryMapByKeyResponse**

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

# **get_world_experience_ordered**
> GetWorldExperienceOrderedResponse get_world_experience_ordered(experience_id, store)

An OrderedStore page ranked by value; ?order=desc|asc&min=&max=&cursor=&limit=.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.get_world_experience_ordered_response import GetWorldExperienceOrderedResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # An OrderedStore page ranked by value; ?order=desc|asc&min=&max=&cursor=&limit=.
        api_response = api_instance.get_world_experience_ordered(experience_id, store)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->get_world_experience_ordered: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |

### Return type

**GetWorldExperienceOrderedResponse**

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

# **get_world_experience_ordered_entry**
> WorldExperienceOrderedEntryResponse get_world_experience_ordered_entry(experience_id, store, key)

One OrderedStore entry.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.common.world_experience_ordered_entry_response import WorldExperienceOrderedEntryResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One OrderedStore entry.
        api_response = api_instance.get_world_experience_ordered_entry(experience_id, store, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->get_world_experience_ordered_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |
 **key** | **str**|  |

### Return type

**WorldExperienceOrderedEntryResponse**

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

# **list_world_experience_datastore_entries**
> ListWorldExperienceDatastoreEntriesResponse list_world_experience_datastore_entries(experience_id, store)

Keys of a DataStore in key order; ?prefix=&scope=&cursor=&limit=.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_experience_datastore_entries_response import ListWorldExperienceDatastoreEntriesResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Keys of a DataStore in key order; ?prefix=&scope=&cursor=&limit=.
        api_response = api_instance.list_world_experience_datastore_entries(experience_id, store)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->list_world_experience_datastore_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |

### Return type

**ListWorldExperienceDatastoreEntriesResponse**

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

# **list_world_experience_datastore_entry_versions**
> ListWorldExperienceDatastoreEntryVersionsResponse list_world_experience_datastore_entry_versions(experience_id, store, key)

Versions of a key, newest first (30-day history; the current version is kept).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.world.list_world_experience_datastore_entry_versions_response import ListWorldExperienceDatastoreEntryVersionsResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Versions of a key, newest first (30-day history; the current version is kept).
        api_response = api_instance.list_world_experience_datastore_entry_versions(experience_id, store, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->list_world_experience_datastore_entry_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |
 **key** | **str**|  |

### Return type

**ListWorldExperienceDatastoreEntryVersionsResponse**

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

# **list_world_experience_datastores**
> ListWorldExperienceDatastoresResponse list_world_experience_datastores(experience_id)

The DataStores of an experience, with key counts and bytes.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.list_world_experience_datastores_response import ListWorldExperienceDatastoresResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The DataStores of an experience, with key counts and bytes.
        api_response = api_instance.list_world_experience_datastores(experience_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->list_world_experience_datastores: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |

### Return type

**ListWorldExperienceDatastoresResponse**

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

# **update_world_experience_datastore_entry**
> UpdateWorldExperienceDatastoreEntryResponse update_world_experience_datastore_entry(experience_id, store, key)

Write a new version. If-Match \"v<n>\" (or ifVersion) writes only at that version; If-None-Match: * only if absent. 412 on a mismatch.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.update_world_experience_datastore_entry_response import UpdateWorldExperienceDatastoreEntryResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Write a new version. If-Match \"v<n>\" (or ifVersion) writes only at that version; If-None-Match: * only if absent. 412 on a mismatch.
        api_response = api_instance.update_world_experience_datastore_entry(experience_id, store, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->update_world_experience_datastore_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |
 **key** | **str**|  |

### Return type

**UpdateWorldExperienceDatastoreEntryResponse**

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

# **update_world_experience_memory_map**
> UpdateWorldExperienceMemoryMapResponse update_world_experience_memory_map(experience_id, map, key)

Set a hash map item (ttlSeconds required; ifVersion for compare-and-set).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.update_world_experience_memory_map_response import UpdateWorldExperienceMemoryMapResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    map = "map_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set a hash map item (ttlSeconds required; ifVersion for compare-and-set).
        api_response = api_instance.update_world_experience_memory_map(experience_id, map, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->update_world_experience_memory_map: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **map** | **str**|  |
 **key** | **str**|  |

### Return type

**UpdateWorldExperienceMemoryMapResponse**

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

# **update_world_experience_memory_sorted**
> UpdateWorldExperienceMemoryMapResponse update_world_experience_memory_sorted(experience_id, map, key)

Set a sorted map item (ttlSeconds, optional sortKey and ifVersion).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.world.update_world_experience_memory_map_response import UpdateWorldExperienceMemoryMapResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    map = "map_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set a sorted map item (ttlSeconds, optional sortKey and ifVersion).
        api_response = api_instance.update_world_experience_memory_sorted(experience_id, map, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->update_world_experience_memory_sorted: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **map** | **str**|  |
 **key** | **str**|  |

### Return type

**UpdateWorldExperienceMemoryMapResponse**

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

# **update_world_experience_ordered_entry**
> WorldExperienceOrderedEntryResponse update_world_experience_ordered_entry(experience_id, store, key)

Set an OrderedStore entry to a whole number.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import worlds_data_api
from crossly.model.common.error import Error
from crossly.model.common.world_experience_ordered_entry_response import WorldExperienceOrderedEntryResponse
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
    api_instance = worlds_data_api.WorldsDataApi(api_client)
    experience_id = "experienceId_example" # str | 
    store = "store_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set an OrderedStore entry to a whole number.
        api_response = api_instance.update_world_experience_ordered_entry(experience_id, store, key)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorldsDataApi->update_world_experience_ordered_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experience_id** | **str**|  |
 **store** | **str**|  |
 **key** | **str**|  |

### Return type

**WorldExperienceOrderedEntryResponse**

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

