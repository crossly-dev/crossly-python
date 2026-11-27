# crossly.SandboxApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sandbox_reset**](SandboxApi.md#create_sandbox_reset) | **POST** /v1/sandbox/reset | Restore the sandbox seller to its seed. Your grant and webhook subscriptions are kept.
[**create_sandbox_simulate_inventory**](SandboxApi.md#create_sandbox_simulate_inventory) | **POST** /v1/sandbox/simulate/inventory | Change stock (set, increase or decrease); the new quantity is pushed to every channel.
[**create_sandbox_simulate_listing_sold_out**](SandboxApi.md#create_sandbox_simulate_listing_sold_out) | **POST** /v1/sandbox/simulate/listing.sold_out | A listing sells out on a marketplace with no order (stock moves, other channels delist).
[**create_sandbox_simulate_order**](SandboxApi.md#create_sandbox_simulate_order) | **POST** /v1/sandbox/simulate/order | Simulate a sale through the real sale pipeline (order.created, sale.detected, stock and cross-channel updates).
[**create_sandbox_simulate_order_address**](SandboxApi.md#create_sandbox_simulate_order_address) | **POST** /v1/sandbox/simulate/order.address | The buyer address of an order simulated with address \&quot;delayed\&quot; arrives now (order.address_available).
[**create_sandbox_simulate_order_cancelled**](SandboxApi.md#create_sandbox_simulate_order_cancelled) | **POST** /v1/sandbox/simulate/order.cancelled | The buyer or the marketplace cancels an order (order.cancelled).
[**create_sandbox_simulate_order_delivered**](SandboxApi.md#create_sandbox_simulate_order_delivered) | **POST** /v1/sandbox/simulate/order.delivered | The carrier delivers a shipped order (order.delivered).
[**create_sandbox_simulate_refund**](SandboxApi.md#create_sandbox_simulate_refund) | **POST** /v1/sandbox/simulate/refund | Refund an order in full or in part (refund.issued).
[**get_sandbox**](SandboxApi.md#get_sandbox) | **GET** /v1/sandbox | The sandbox seller this token acts on, its simulated channels and the failure modes.
[**list_sandbox_events**](SandboxApi.md#list_sandbox_events) | **GET** /v1/sandbox/events | The simulated marketplaces&#39; call log: verb, channel, outcome, latency.


# **create_sandbox_reset**
> CreateSandboxResetResponse create_sandbox_reset()

Restore the sandbox seller to its seed. Your grant and webhook subscriptions are kept.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sandbox_api
from crossly.model.common.error import Error
from crossly.model.sandbox.create_sandbox_reset_response import CreateSandboxResetResponse
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
    api_instance = sandbox_api.SandboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Restore the sandbox seller to its seed. Your grant and webhook subscriptions are kept.
        api_response = api_instance.create_sandbox_reset()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SandboxApi->create_sandbox_reset: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateSandboxResetResponse**

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

# **create_sandbox_simulate_inventory**
> CreateInboxConversationBulkResponse create_sandbox_simulate_inventory()

Change stock (set, increase or decrease); the new quantity is pushed to every channel.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sandbox_api
from crossly.model.inbox.create_inbox_conversation_bulk_response import CreateInboxConversationBulkResponse
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
    api_instance = sandbox_api.SandboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Change stock (set, increase or decrease); the new quantity is pushed to every channel.
        api_response = api_instance.create_sandbox_simulate_inventory()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SandboxApi->create_sandbox_simulate_inventory: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateInboxConversationBulkResponse**

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

# **create_sandbox_simulate_listing_sold_out**
> CreateSandboxSimulateListingSoldOutResponse create_sandbox_simulate_listing_sold_out()

A listing sells out on a marketplace with no order (stock moves, other channels delist).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sandbox_api
from crossly.model.common.error import Error
from crossly.model.sandbox.create_sandbox_simulate_listing_sold_out_response import CreateSandboxSimulateListingSoldOutResponse
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
    api_instance = sandbox_api.SandboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # A listing sells out on a marketplace with no order (stock moves, other channels delist).
        api_response = api_instance.create_sandbox_simulate_listing_sold_out()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SandboxApi->create_sandbox_simulate_listing_sold_out: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateSandboxSimulateListingSoldOutResponse**

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

# **create_sandbox_simulate_order**
> CreateSandboxSimulateOrderResponse create_sandbox_simulate_order()

Simulate a sale through the real sale pipeline (order.created, sale.detected, stock and cross-channel updates).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sandbox_api
from crossly.model.common.error import Error
from crossly.model.sandbox.create_sandbox_simulate_order_response import CreateSandboxSimulateOrderResponse
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
    api_instance = sandbox_api.SandboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Simulate a sale through the real sale pipeline (order.created, sale.detected, stock and cross-channel updates).
        api_response = api_instance.create_sandbox_simulate_order()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SandboxApi->create_sandbox_simulate_order: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateSandboxSimulateOrderResponse**

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

# **create_sandbox_simulate_order_address**
> CreateSandboxSimulateOrderAddressResponse create_sandbox_simulate_order_address()

The buyer address of an order simulated with address \"delayed\" arrives now (order.address_available).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sandbox_api
from crossly.model.common.error import Error
from crossly.model.sandbox.create_sandbox_simulate_order_address_response import CreateSandboxSimulateOrderAddressResponse
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
    api_instance = sandbox_api.SandboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The buyer address of an order simulated with address \"delayed\" arrives now (order.address_available).
        api_response = api_instance.create_sandbox_simulate_order_address()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SandboxApi->create_sandbox_simulate_order_address: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateSandboxSimulateOrderAddressResponse**

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

# **create_sandbox_simulate_order_cancelled**
> CreateSandboxSimulateOrderCancelledResponse create_sandbox_simulate_order_cancelled()

The buyer or the marketplace cancels an order (order.cancelled).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sandbox_api
from crossly.model.sandbox.create_sandbox_simulate_order_cancelled_response import CreateSandboxSimulateOrderCancelledResponse
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
    api_instance = sandbox_api.SandboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The buyer or the marketplace cancels an order (order.cancelled).
        api_response = api_instance.create_sandbox_simulate_order_cancelled()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SandboxApi->create_sandbox_simulate_order_cancelled: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateSandboxSimulateOrderCancelledResponse**

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

# **create_sandbox_simulate_order_delivered**
> CreateSandboxSimulateOrderDeliveredResponse create_sandbox_simulate_order_delivered()

The carrier delivers a shipped order (order.delivered).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sandbox_api
from crossly.model.common.error import Error
from crossly.model.sandbox.create_sandbox_simulate_order_delivered_response import CreateSandboxSimulateOrderDeliveredResponse
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
    api_instance = sandbox_api.SandboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The carrier delivers a shipped order (order.delivered).
        api_response = api_instance.create_sandbox_simulate_order_delivered()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SandboxApi->create_sandbox_simulate_order_delivered: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateSandboxSimulateOrderDeliveredResponse**

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

# **create_sandbox_simulate_refund**
> CreateSandboxSimulateRefundResponse create_sandbox_simulate_refund()

Refund an order in full or in part (refund.issued).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sandbox_api
from crossly.model.sandbox.create_sandbox_simulate_refund_response import CreateSandboxSimulateRefundResponse
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
    api_instance = sandbox_api.SandboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Refund an order in full or in part (refund.issued).
        api_response = api_instance.create_sandbox_simulate_refund()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SandboxApi->create_sandbox_simulate_refund: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateSandboxSimulateRefundResponse**

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

# **get_sandbox**
> GetSandboxResponse get_sandbox()

The sandbox seller this token acts on, its simulated channels and the failure modes.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sandbox_api
from crossly.model.sandbox.get_sandbox_response import GetSandboxResponse
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
    api_instance = sandbox_api.SandboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The sandbox seller this token acts on, its simulated channels and the failure modes.
        api_response = api_instance.get_sandbox()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SandboxApi->get_sandbox: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetSandboxResponse**

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

# **list_sandbox_events**
> ListSandboxEventsResponse list_sandbox_events()

The simulated marketplaces' call log: verb, channel, outcome, latency.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sandbox_api
from crossly.model.common.error import Error
from crossly.model.sandbox.list_sandbox_events_response import ListSandboxEventsResponse
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
    api_instance = sandbox_api.SandboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The simulated marketplaces' call log: verb, channel, outcome, latency.
        api_response = api_instance.list_sandbox_events()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SandboxApi->list_sandbox_events: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListSandboxEventsResponse**

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

