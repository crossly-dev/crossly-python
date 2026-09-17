# crossly.AIApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ai_categorize**](AIApi.md#create_ai_categorize) | **POST** /v1/ai/categorize | Taxonomy guess from a single image URL.
[**create_ai_categorize_from_image**](AIApi.md#create_ai_categorize_from_image) | **POST** /v1/ai/categorize-from-image | Taxonomy guess from a single base64 image.
[**create_ai_enhance_description**](AIApi.md#create_ai_enhance_description) | **POST** /v1/ai/enhance-description | SEO-rewrite a listing description.
[**create_ai_enhance_listing**](AIApi.md#create_ai_enhance_listing) | **POST** /v1/ai/enhance-listing | Rewrite title + description + tags in one call.
[**create_ai_enhance_title**](AIApi.md#create_ai_enhance_title) | **POST** /v1/ai/enhance-title | SEO-rewrite a listing title.
[**create_ai_extract_receipt**](AIApi.md#create_ai_extract_receipt) | **POST** /v1/ai/extract-receipt | Structured data extraction from a receipt photo.
[**create_ai_generate_listing**](AIApi.md#create_ai_generate_listing) | **POST** /v1/ai/generate-listing | Generate full listing fields from up to 4 image URLs.
[**create_ai_help**](AIApi.md#create_ai_help) | **POST** /v1/ai/help | In-app help Q&amp;A grounded in supplied docs.
[**create_ai_magic_listing**](AIApi.md#create_ai_magic_listing) | **POST** /v1/ai/magic-listing | Generate full listing fields from base64 photos.
[**create_ai_test_key**](AIApi.md#create_ai_test_key) | **POST** /v1/ai/test-key | Live-ping a candidate BYO-key.
[**delete_ai_key**](AIApi.md#delete_ai_key) | **DELETE** /v1/ai/key | Remove the BYO-key for a provider.
[**get_ai_provider**](AIApi.md#get_ai_provider) | **GET** /v1/ai/providers | Static catalog of supported AI providers.
[**get_ai_status**](AIApi.md#get_ai_status) | **GET** /v1/ai/status | BYO-key state for the calling user.
[**update_ai_key**](AIApi.md#update_ai_key) | **PUT** /v1/ai/key | Save an encrypted BYO-key for an AI provider.


# **create_ai_categorize**
> CreateAiCategorizeResponse create_ai_categorize()

Taxonomy guess from a single image URL.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.create_ai_categorize_response import CreateAiCategorizeResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Taxonomy guess from a single image URL.
        api_response = api_instance.create_ai_categorize()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->create_ai_categorize: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAiCategorizeResponse**](CreateAiCategorizeResponse.md)

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

# **create_ai_categorize_from_image**
> CreateAiCategorizeFromImageResponse create_ai_categorize_from_image()

Taxonomy guess from a single base64 image.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.create_ai_categorize_from_image_response import CreateAiCategorizeFromImageResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Taxonomy guess from a single base64 image.
        api_response = api_instance.create_ai_categorize_from_image()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->create_ai_categorize_from_image: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAiCategorizeFromImageResponse**](CreateAiCategorizeFromImageResponse.md)

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

# **create_ai_enhance_description**
> CreateAiEnhanceDescriptionResponse create_ai_enhance_description()

SEO-rewrite a listing description.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.create_ai_enhance_description_response import CreateAiEnhanceDescriptionResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # SEO-rewrite a listing description.
        api_response = api_instance.create_ai_enhance_description()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->create_ai_enhance_description: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAiEnhanceDescriptionResponse**](CreateAiEnhanceDescriptionResponse.md)

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

# **create_ai_enhance_listing**
> CreateAiEnhanceListingResponse create_ai_enhance_listing()

Rewrite title + description + tags in one call.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.create_ai_enhance_listing_response import CreateAiEnhanceListingResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Rewrite title + description + tags in one call.
        api_response = api_instance.create_ai_enhance_listing()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->create_ai_enhance_listing: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAiEnhanceListingResponse**](CreateAiEnhanceListingResponse.md)

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

# **create_ai_enhance_title**
> CreateAiEnhanceTitleResponse create_ai_enhance_title()

SEO-rewrite a listing title.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.create_ai_enhance_title_response import CreateAiEnhanceTitleResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # SEO-rewrite a listing title.
        api_response = api_instance.create_ai_enhance_title()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->create_ai_enhance_title: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAiEnhanceTitleResponse**](CreateAiEnhanceTitleResponse.md)

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

# **create_ai_extract_receipt**
> CreateAiExtractReceiptResponse create_ai_extract_receipt()

Structured data extraction from a receipt photo.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.create_ai_extract_receipt_response import CreateAiExtractReceiptResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Structured data extraction from a receipt photo.
        api_response = api_instance.create_ai_extract_receipt()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->create_ai_extract_receipt: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAiExtractReceiptResponse**](CreateAiExtractReceiptResponse.md)

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

# **create_ai_generate_listing**
> CreateAiGenerateListingResponse create_ai_generate_listing()

Generate full listing fields from up to 4 image URLs.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.create_ai_generate_listing_response import CreateAiGenerateListingResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Generate full listing fields from up to 4 image URLs.
        api_response = api_instance.create_ai_generate_listing()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->create_ai_generate_listing: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAiGenerateListingResponse**](CreateAiGenerateListingResponse.md)

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

# **create_ai_help**
> CreateAiHelpResponse create_ai_help()

In-app help Q&A grounded in supplied docs.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.create_ai_help_response import CreateAiHelpResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # In-app help Q&A grounded in supplied docs.
        api_response = api_instance.create_ai_help()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->create_ai_help: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAiHelpResponse**](CreateAiHelpResponse.md)

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

# **create_ai_magic_listing**
> CreateAiMagicListingResponse create_ai_magic_listing()

Generate full listing fields from base64 photos.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.create_ai_magic_listing_response import CreateAiMagicListingResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Generate full listing fields from base64 photos.
        api_response = api_instance.create_ai_magic_listing()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->create_ai_magic_listing: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAiMagicListingResponse**](CreateAiMagicListingResponse.md)

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

# **create_ai_test_key**
> CreateAiTestKeyResponse create_ai_test_key()

Live-ping a candidate BYO-key.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.create_ai_test_key_response import CreateAiTestKeyResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Live-ping a candidate BYO-key.
        api_response = api_instance.create_ai_test_key()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->create_ai_test_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAiTestKeyResponse**](CreateAiTestKeyResponse.md)

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

# **delete_ai_key**
> DeleteAiKeyResponse delete_ai_key()

Remove the BYO-key for a provider.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.delete_ai_key_response import DeleteAiKeyResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Remove the BYO-key for a provider.
        api_response = api_instance.delete_ai_key()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->delete_ai_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DeleteAiKeyResponse**](DeleteAiKeyResponse.md)

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

# **get_ai_provider**
> GetAiProviderResponse get_ai_provider()

Static catalog of supported AI providers.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.get_ai_provider_response import GetAiProviderResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Static catalog of supported AI providers.
        api_response = api_instance.get_ai_provider()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->get_ai_provider: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAiProviderResponse**](GetAiProviderResponse.md)

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

# **get_ai_status**
> GetAiStatusResponse get_ai_status()

BYO-key state for the calling user.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.error import Error
from crossly.model.get_ai_status_response import GetAiStatusResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # BYO-key state for the calling user.
        api_response = api_instance.get_ai_status()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->get_ai_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAiStatusResponse**](GetAiStatusResponse.md)

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

# **update_ai_key**
> UpdateAiKeyResponse update_ai_key()

Save an encrypted BYO-key for an AI provider.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import ai_api
from crossly.model.update_ai_key_response import UpdateAiKeyResponse
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
    api_instance = ai_api.AIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Save an encrypted BYO-key for an AI provider.
        api_response = api_instance.update_ai_key()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling AIApi->update_ai_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UpdateAiKeyResponse**](UpdateAiKeyResponse.md)

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

