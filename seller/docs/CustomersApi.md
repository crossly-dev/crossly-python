# crossly.CustomersApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_bulk_delete**](CustomersApi.md#create_customer_bulk_delete) | **POST** /v1/customers/bulk-delete | Bulk blocklist customer handles.
[**create_customer_bulk_export**](CustomersApi.md#create_customer_bulk_export) | **POST** /v1/customers/bulk-export | Bulk export aggregated customers as CSV.
[**create_customer_refresh_profile**](CustomersApi.md#create_customer_refresh_profile) | **POST** /v1/customers/{handle}/refresh-profile | Queue a fresh read of a customer&#39;s buyer profiles on every platform they ordered on.
[**get_customer**](CustomersApi.md#get_customer) | **GET** /v1/customers/{handle} | Get one customer: recent 50 orders, buyer profiles per platform, and stats over all of their orders.
[**get_loyalty_club**](CustomersApi.md#get_loyalty_club) | **GET** /v1/loyalty/club | Your loyalty club: tiers and how many members are in each.
[**list_customers**](CustomersApi.md#list_customers) | **GET** /v1/customers | List aggregated customers (group-by lower(buyer_username)), each with its best avatar, display name and star rating.
[**list_loyalty_members**](CustomersApi.md#list_loyalty_members) | **GET** /v1/loyalty/members | Your loyalty club’s members, by spend with you.
[**update_loyalty_club**](CustomersApi.md#update_loyalty_club) | **PUT** /v1/loyalty/club | Create or update your loyalty club: name, on/off, and up to 6 spend tiers each with a discount (≤ 30%) and perks.


# **create_customer_bulk_delete**
> CreateCustomerBulkDeleteResponse create_customer_bulk_delete()

Bulk blocklist customer handles.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
from crossly.model.common.error import Error
from crossly.model.customer.create_customer_bulk_delete_response import CreateCustomerBulkDeleteResponse
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
    api_instance = customers_api.CustomersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk blocklist customer handles.
        api_response = api_instance.create_customer_bulk_delete()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->create_customer_bulk_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateCustomerBulkDeleteResponse**

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

# **create_customer_bulk_export**
> str create_customer_bulk_export()

Bulk export aggregated customers as CSV.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
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
    api_instance = customers_api.CustomersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Bulk export aggregated customers as CSV.
        api_response = api_instance.create_customer_bulk_export()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->create_customer_bulk_export: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **create_customer_refresh_profile**
> CreateCustomerRefreshProfileResponse create_customer_refresh_profile(handle)

Queue a fresh read of a customer's buyer profiles on every platform they ordered on.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
from crossly.model.common.error import Error
from crossly.model.customer.create_customer_refresh_profile_response import CreateCustomerRefreshProfileResponse
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
    api_instance = customers_api.CustomersApi(api_client)
    handle = "handle_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Queue a fresh read of a customer's buyer profiles on every platform they ordered on.
        api_response = api_instance.create_customer_refresh_profile(handle)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->create_customer_refresh_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**|  |

### Return type

**CreateCustomerRefreshProfileResponse**

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

# **get_customer**
> GetCustomerResponse get_customer(handle)

Get one customer: recent 50 orders, buyer profiles per platform, and stats over all of their orders.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
from crossly.model.common.error import Error
from crossly.model.customer.get_customer_response import GetCustomerResponse
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
    api_instance = customers_api.CustomersApi(api_client)
    handle = "handle_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get one customer: recent 50 orders, buyer profiles per platform, and stats over all of their orders.
        api_response = api_instance.get_customer(handle)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->get_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**|  |

### Return type

**GetCustomerResponse**

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

# **get_loyalty_club**
> GetLoyaltyClubResponse get_loyalty_club()

Your loyalty club: tiers and how many members are in each.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
from crossly.model.common.error import Error
from crossly.model.common.get_loyalty_club_response import GetLoyaltyClubResponse
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
    api_instance = customers_api.CustomersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your loyalty club: tiers and how many members are in each.
        api_response = api_instance.get_loyalty_club()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->get_loyalty_club: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetLoyaltyClubResponse**

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

# **list_customers**
> ListCustomersResponse list_customers()

List aggregated customers (group-by lower(buyer_username)), each with its best avatar, display name and star rating.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
from crossly.model.common.error import Error
from crossly.model.customer.list_customers_response import ListCustomersResponse
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
    api_instance = customers_api.CustomersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List aggregated customers (group-by lower(buyer_username)), each with its best avatar, display name and star rating.
        api_response = api_instance.list_customers()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->list_customers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCustomersResponse**

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

# **list_loyalty_members**
> ListLoyaltyMembersResponse list_loyalty_members()

Your loyalty club’s members, by spend with you.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
from crossly.model.common.list_loyalty_members_response import ListLoyaltyMembersResponse
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
    api_instance = customers_api.CustomersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your loyalty club’s members, by spend with you.
        api_response = api_instance.list_loyalty_members()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->list_loyalty_members: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListLoyaltyMembersResponse**

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

# **update_loyalty_club**
> GetLoyaltyClubResponse update_loyalty_club()

Create or update your loyalty club: name, on/off, and up to 6 spend tiers each with a discount (≤ 30%) and perks.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import customers_api
from crossly.model.common.error import Error
from crossly.model.common.get_loyalty_club_response import GetLoyaltyClubResponse
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
    api_instance = customers_api.CustomersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create or update your loyalty club: name, on/off, and up to 6 spend tiers each with a discount (≤ 30%) and perks.
        api_response = api_instance.update_loyalty_club()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling CustomersApi->update_loyalty_club: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetLoyaltyClubResponse**

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

