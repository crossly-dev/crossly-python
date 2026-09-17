# crossly.ProfileApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_me**](ProfileApi.md#update_me) | **PATCH** /v1/me | Update the authenticated user&#39;s profile (display name, etc).


# **update_me**
> UpdateMeResponse update_me()

Update the authenticated user's profile (display name, etc).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import profile_api
from crossly.model.update_me_response import UpdateMeResponse
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
    api_instance = profile_api.ProfileApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update the authenticated user's profile (display name, etc).
        api_response = api_instance.update_me()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ProfileApi->update_me: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UpdateMeResponse**](UpdateMeResponse.md)

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

