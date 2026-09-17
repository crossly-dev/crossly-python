# crossly.SourcingApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sourcing_receipt**](SourcingApi.md#create_sourcing_receipt) | **POST** /v1/sourcing/receipts | Append a parsed receipt to the sourcing ledger.
[**get_sourcing_receipt**](SourcingApi.md#get_sourcing_receipt) | **GET** /v1/sourcing/receipts | List parsed sourcing receipts in this user&#39;s ledger.
[**list_sourcing_demand**](SourcingApi.md#list_sourcing_demand) | **GET** /v1/sourcing/demand | Items buyers looked for on other sites that Crossly did not have.
[**list_sourcing_demand_mine**](SourcingApi.md#list_sourcing_demand_mine) | **GET** /v1/sourcing/demand/mine | Unmet buyer demand for items you hold or have sold before.


# **create_sourcing_receipt**
> CreateSourcingReceiptResponse create_sourcing_receipt()

Append a parsed receipt to the sourcing ledger.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sourcing_api
from crossly.model.error import Error
from crossly.model.create_sourcing_receipt_response import CreateSourcingReceiptResponse
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
    api_instance = sourcing_api.SourcingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Append a parsed receipt to the sourcing ledger.
        api_response = api_instance.create_sourcing_receipt()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SourcingApi->create_sourcing_receipt: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateSourcingReceiptResponse**](CreateSourcingReceiptResponse.md)

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

# **get_sourcing_receipt**
> GetSourcingReceiptResponse get_sourcing_receipt()

List parsed sourcing receipts in this user's ledger.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sourcing_api
from crossly.model.error import Error
from crossly.model.get_sourcing_receipt_response import GetSourcingReceiptResponse
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
    api_instance = sourcing_api.SourcingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List parsed sourcing receipts in this user's ledger.
        api_response = api_instance.get_sourcing_receipt()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SourcingApi->get_sourcing_receipt: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSourcingReceiptResponse**](GetSourcingReceiptResponse.md)

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

# **list_sourcing_demand**
> bool, date, datetime, dict, float, int, list, str, none_type list_sourcing_demand()

Items buyers looked for on other sites that Crossly did not have.

Aggregate demand observed by the Scout extension, ranked by MISSES — the times somebody asked and we had nothing. `medianPageCents` is what the retailers were charging, which is the number to source against. Anonymous in every case; there is no per-buyer view of this.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sourcing_api
from crossly.model.error import Error
from crossly.model.list_sourcing_demand_item import ListSourcingDemandItem
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
    api_instance = sourcing_api.SourcingApi(api_client)
    days = 30 # int |  (optional) if omitted the server will use the default value of 30
    min_looks = 3 # int |  (optional) if omitted the server will use the default value of 3
    limit = 50 # int |  (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Items buyers looked for on other sites that Crossly did not have.
        api_response = api_instance.list_sourcing_demand(days=days, min_looks=min_looks, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SourcingApi->list_sourcing_demand: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | [optional] if omitted the server will use the default value of 30
 **min_looks** | **int**|  | [optional] if omitted the server will use the default value of 3
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 50

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

# **list_sourcing_demand_mine**
> bool, date, datetime, dict, float, int, list, str, none_type list_sourcing_demand_mine()

Unmet buyer demand for items you hold or have sold before.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import sourcing_api
from crossly.model.list_sourcing_demand_mine_item import ListSourcingDemandMineItem
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
    api_instance = sourcing_api.SourcingApi(api_client)
    days = 60 # int |  (optional) if omitted the server will use the default value of 60
    min_lookers = 2 # int |  (optional) if omitted the server will use the default value of 2
    limit = 25 # int |  (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unmet buyer demand for items you hold or have sold before.
        api_response = api_instance.list_sourcing_demand_mine(days=days, min_lookers=min_lookers, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling SourcingApi->list_sourcing_demand_mine: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | [optional] if omitted the server will use the default value of 60
 **min_lookers** | **int**|  | [optional] if omitted the server will use the default value of 2
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 25

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

