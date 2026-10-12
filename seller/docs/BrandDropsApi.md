# crossly.BrandDropsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_brand_drop**](BrandDropsApi.md#create_brand_drop) | **POST** /v1/brand-drops | Create a brand drop as a draft (name, dropAt in the future, optional description, cover image and Crossly platform-listing ids). Approved partners only (403 drop_partner_required); counts against your monthly allowance (403 drop_quota_exhausted).
[**get_brand_drop**](BrandDropsApi.md#get_brand_drop) | **GET** /v1/brand-drops/{id} | One of your brand drops, with its status and any note from Crossly’s review.
[**get_brand_drop_partner**](BrandDropsApi.md#get_brand_drop_partner) | **GET** /v1/brand-drops/partner | Your drop-partner terms (fee, promotion tier, monthly allowance, whether you may schedule without review) and how many drops you have created this month. partner is null when you are not an approved partner — apply at crossly.net/drops/apply.
[**list_brand_drop_listings**](BrandDropsApi.md#list_brand_drop_listings) | **GET** /v1/brand-drops/{id}/listings | The listings a brand drop releases when it goes live.
[**list_brand_drops**](BrandDropsApi.md#list_brand_drops) | **GET** /v1/brand-drops | Your brand drops, newest start time first. Filter with ?status&#x3D;draft|pending_review|scheduled|live|sold_out|ended|cancelled. Empty when you are not a partner.
[**update_brand_drop**](BrandDropsApi.md#update_brand_drop) | **PATCH** /v1/brand-drops/{id} | Edit a brand drop and/or change its status: draft (withdraw / unschedule), pending_review (submit for review), scheduled (only with canSelfPublish — 403 drop_review_required otherwise), cancelled. Editing name, time or description of a reviewed drop sends it back to review. Live and finished drops cannot be changed.
[**update_brand_drop_listing**](BrandDropsApi.md#update_brand_drop_listing) | **PUT** /v1/brand-drops/{id}/listings | Replace the listings a brand drop releases, by master listing id (up to 100). Each must already be listed on Crossly — otherwise 400 listing_not_on_crossly naming them. Not allowed once the drop is live or finished.


# **create_brand_drop**
> BrandDropResponse create_brand_drop()

Create a brand drop as a draft (name, dropAt in the future, optional description, cover image and Crossly platform-listing ids). Approved partners only (403 drop_partner_required); counts against your monthly allowance (403 drop_quota_exhausted).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import brand_drops_api
from crossly.model.common.brand_drop_response import BrandDropResponse
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
    api_instance = brand_drops_api.BrandDropsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a brand drop as a draft (name, dropAt in the future, optional description, cover image and Crossly platform-listing ids). Approved partners only (403 drop_partner_required); counts against your monthly allowance (403 drop_quota_exhausted).
        api_response = api_instance.create_brand_drop()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BrandDropsApi->create_brand_drop: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**BrandDropResponse**

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

# **get_brand_drop**
> BrandDropResponse get_brand_drop(id)

One of your brand drops, with its status and any note from Crossly’s review.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import brand_drops_api
from crossly.model.common.brand_drop_response import BrandDropResponse
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
    api_instance = brand_drops_api.BrandDropsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One of your brand drops, with its status and any note from Crossly’s review.
        api_response = api_instance.get_brand_drop(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BrandDropsApi->get_brand_drop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**BrandDropResponse**

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

# **get_brand_drop_partner**
> GetBrandDropPartnerResponse get_brand_drop_partner()

Your drop-partner terms (fee, promotion tier, monthly allowance, whether you may schedule without review) and how many drops you have created this month. partner is null when you are not an approved partner — apply at crossly.net/drops/apply.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import brand_drops_api
from crossly.model.brand.get_brand_drop_partner_response import GetBrandDropPartnerResponse
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
    api_instance = brand_drops_api.BrandDropsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your drop-partner terms (fee, promotion tier, monthly allowance, whether you may schedule without review) and how many drops you have created this month. partner is null when you are not an approved partner — apply at crossly.net/drops/apply.
        api_response = api_instance.get_brand_drop_partner()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BrandDropsApi->get_brand_drop_partner: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetBrandDropPartnerResponse**

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

# **list_brand_drop_listings**
> ListBrandDropListingsResponse list_brand_drop_listings(id)

The listings a brand drop releases when it goes live.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import brand_drops_api
from crossly.model.brand.list_brand_drop_listings_response import ListBrandDropListingsResponse
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
    api_instance = brand_drops_api.BrandDropsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The listings a brand drop releases when it goes live.
        api_response = api_instance.list_brand_drop_listings(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BrandDropsApi->list_brand_drop_listings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListBrandDropListingsResponse**

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

# **list_brand_drops**
> ListBrandDropsResponse list_brand_drops()

Your brand drops, newest start time first. Filter with ?status=draft|pending_review|scheduled|live|sold_out|ended|cancelled. Empty when you are not a partner.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import brand_drops_api
from crossly.model.common.error import Error
from crossly.model.brand.list_brand_drops_response import ListBrandDropsResponse
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
    api_instance = brand_drops_api.BrandDropsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your brand drops, newest start time first. Filter with ?status=draft|pending_review|scheduled|live|sold_out|ended|cancelled. Empty when you are not a partner.
        api_response = api_instance.list_brand_drops()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BrandDropsApi->list_brand_drops: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListBrandDropsResponse**

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

# **update_brand_drop**
> BrandDropResponse update_brand_drop(id)

Edit a brand drop and/or change its status: draft (withdraw / unschedule), pending_review (submit for review), scheduled (only with canSelfPublish — 403 drop_review_required otherwise), cancelled. Editing name, time or description of a reviewed drop sends it back to review. Live and finished drops cannot be changed.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import brand_drops_api
from crossly.model.common.brand_drop_response import BrandDropResponse
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
    api_instance = brand_drops_api.BrandDropsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Edit a brand drop and/or change its status: draft (withdraw / unschedule), pending_review (submit for review), scheduled (only with canSelfPublish — 403 drop_review_required otherwise), cancelled. Editing name, time or description of a reviewed drop sends it back to review. Live and finished drops cannot be changed.
        api_response = api_instance.update_brand_drop(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BrandDropsApi->update_brand_drop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**BrandDropResponse**

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

# **update_brand_drop_listing**
> ListBrandDropListingsResponse update_brand_drop_listing(id)

Replace the listings a brand drop releases, by master listing id (up to 100). Each must already be listed on Crossly — otherwise 400 listing_not_on_crossly naming them. Not allowed once the drop is live or finished.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import brand_drops_api
from crossly.model.brand.list_brand_drop_listings_response import ListBrandDropListingsResponse
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
    api_instance = brand_drops_api.BrandDropsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Replace the listings a brand drop releases, by master listing id (up to 100). Each must already be listed on Crossly — otherwise 400 listing_not_on_crossly naming them. Not allowed once the drop is live or finished.
        api_response = api_instance.update_brand_drop_listing(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BrandDropsApi->update_brand_drop_listing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListBrandDropListingsResponse**

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

