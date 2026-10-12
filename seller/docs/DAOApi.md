# crossly.DAOApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dao_proposal**](DAOApi.md#create_dao_proposal) | **POST** /v1/dao/proposals | Raise a proposal. Starts as a draft.
[**create_dao_proposal_finalise**](DAOApi.md#create_dao_proposal_finalise) | **POST** /v1/dao/proposals/{id}/finalise | Close a proposal whose window has passed and record the outcome.
[**create_dao_proposal_open**](DAOApi.md#create_dao_proposal_open) | **POST** /v1/dao/proposals/{id}/open | Put your draft to a vote. Snapshots voting power.
[**create_dao_proposal_veto**](DAOApi.md#create_dao_proposal_veto) | **POST** /v1/dao/proposals/{id}/veto | Operator block. There is no matching power to PASS.
[**create_dao_proposal_vote**](DAOApi.md#create_dao_proposal_vote) | **POST** /v1/dao/proposals/{id}/vote | Cast or change a vote while the window is open.
[**delete_dao_proposal**](DAOApi.md#delete_dao_proposal) | **DELETE** /v1/dao/proposals/{id} | Withdraw your own DRAFT.
[**get_dao_proposal_tally**](DAOApi.md#get_dao_proposal_tally) | **GET** /v1/dao/proposals/{id}/tally | The live count.
[**list_dao_proposals**](DAOApi.md#list_dao_proposals) | **GET** /v1/dao/proposals | The proposal queue.


# **create_dao_proposal**
> CreateDaoProposalResponse create_dao_proposal()

Raise a proposal. Starts as a draft.

Requires staked CBX above `minProposeWeight`, and one in-flight proposal at a time. The limits bound a denial of ATTENTION rather than of service — attention is the resource a DAO actually runs on. `beneficiaryKind` is a CLOSED set and there is deliberately no stakers, holders, airdrop or distribution option. A proposal whose beneficiaries are the voters would be a self-payment, and a distribution decided by its own recipients is a dividend whatever it is called. The DAO decides WHAT to fund, never WHO gets paid. A `policy` proposal requests no funds and must omit the amount; every other kind must supply one.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import dao_api
from crossly.model.common.error import Error
from crossly.model.dao.create_dao_proposal_response import CreateDaoProposalResponse
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
    api_instance = dao_api.DAOApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Raise a proposal. Starts as a draft.
        api_response = api_instance.create_dao_proposal()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DAOApi->create_dao_proposal: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateDaoProposalResponse**

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

# **create_dao_proposal_finalise**
> CreateDaoProposalFinaliseResponse create_dao_proposal_finalise(id)

Close a proposal whose window has passed and record the outcome.

Normally unnecessary — the hourly sweep does it. Exposed so a result can be published immediately after a window closes rather than waiting for a tick. FINALISING RECORDS AN OUTCOME AND NOTHING ELSE. A passed proposal sets a status; disbursing still requires a campaign with a preview and a human approval, and there is no endpoint here that can move value.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import dao_api
from crossly.model.common.error import Error
from crossly.model.dao.create_dao_proposal_finalise_response import CreateDaoProposalFinaliseResponse
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
    api_instance = dao_api.DAOApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Close a proposal whose window has passed and record the outcome.
        api_response = api_instance.create_dao_proposal_finalise(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DAOApi->create_dao_proposal_finalise: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateDaoProposalFinaliseResponse**

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

# **create_dao_proposal_open**
> CreateDaoProposalOpenResponse create_dao_proposal_open(id)

Put your draft to a vote. Snapshots voting power.

ONLY THE PROPOSER may open their own draft. Opening puts something to a binding vote in somebody's name, and authorship and that decision both belong to them. Opening writes a per-subject voting-power snapshot and freezes the quorum denominator. Nothing recomputes either afterwards, which is what stops acquire-vote-sell. Refuses when nobody holds enough staked CBX to vote — opening then would guarantee a failed quorum, waste a week and read as the feature being broken.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import dao_api
from crossly.model.dao.create_dao_proposal_open_response import CreateDaoProposalOpenResponse
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
    api_instance = dao_api.DAOApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Put your draft to a vote. Snapshots voting power.
        api_response = api_instance.create_dao_proposal_open(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DAOApi->create_dao_proposal_open: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateDaoProposalOpenResponse**

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

# **create_dao_proposal_veto**
> CreateDaoProposalVetoResponse create_dao_proposal_veto(id)

Operator block. There is no matching power to PASS.

DELIBERATELY ASYMMETRIC. A veto exists for the illegal and the ruinous — funding something unlawful, or emptying the pool in a week. A power to pass would make every vote advisory theatre, because the outcome would always be whatever the operator preferred. An operator who can only say no cannot manufacture an outcome. The reason is MANDATORY and stored: an unexplained veto is indistinguishable from disliking the result, which is exactly what would destroy confidence in the mechanism. Expect it to be read.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import dao_api
from crossly.model.dao.create_dao_proposal_veto_response import CreateDaoProposalVetoResponse
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
    api_instance = dao_api.DAOApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Operator block. There is no matching power to PASS.
        api_response = api_instance.create_dao_proposal_veto(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DAOApi->create_dao_proposal_veto: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateDaoProposalVetoResponse**

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

# **create_dao_proposal_vote**
> CreateDaoProposalVoteResponse create_dao_proposal_vote(id)

Cast or change a vote while the window is open.

Weight comes from the snapshot taken when the proposal opened, so staking afterwards grants no vote on it. Changing your mind is an UPDATE, not a second vote — a unique index makes double-counting impossible even if this logic were wrong. ABSTAIN counts toward turnout and not toward approval, which is the whole reason to offer it: it lets you help a proposal clear quorum without taking a side.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import dao_api
from crossly.model.common.error import Error
from crossly.model.dao.create_dao_proposal_vote_response import CreateDaoProposalVoteResponse
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
    api_instance = dao_api.DAOApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Cast or change a vote while the window is open.
        api_response = api_instance.create_dao_proposal_vote(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DAOApi->create_dao_proposal_vote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateDaoProposalVoteResponse**

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

# **delete_dao_proposal**
> DeleteDaoProposalResponse delete_dao_proposal(id)

Withdraw your own DRAFT.

Drafts only. Withdrawing an OPEN proposal would discard votes already cast, which is the proposer overruling the electorate — the thing the whole mechanism exists to prevent. An open proposal runs its window and gets a result. This exists so the one-in-flight limit is not a trap: without it a typo would lock somebody out of governance until the draft expired.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import dao_api
from crossly.model.common.error import Error
from crossly.model.dao.delete_dao_proposal_response import DeleteDaoProposalResponse
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
    api_instance = dao_api.DAOApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Withdraw your own DRAFT.
        api_response = api_instance.delete_dao_proposal(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DAOApi->delete_dao_proposal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteDaoProposalResponse**

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

# **get_dao_proposal_tally**
> GetDaoProposalTallyResponse get_dao_proposal_tally(id)

The live count.

`turnoutBps` is cast power over the frozen total, and counts abstentions. `approvalBps` is FOR over decisive votes, and does not. A proposal that misses quorum reports `expired` rather than `rejected` when finalised — \"nobody turned up\" and \"the room said no\" are different outcomes and a proposer deserves to know which happened.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import dao_api
from crossly.model.dao.get_dao_proposal_tally_response import GetDaoProposalTallyResponse
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
    api_instance = dao_api.DAOApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The live count.
        api_response = api_instance.get_dao_proposal_tally(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DAOApi->get_dao_proposal_tally: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetDaoProposalTallyResponse**

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

# **list_dao_proposals**
> ListDaoProposalsResponse list_dao_proposals()

The proposal queue.

Staked CBX decides what the events pool funds. Voting power is size x tenure — the same weighting the earn multiplier uses — and it is SNAPSHOTTED when a proposal opens, so staking after seeing one grants no vote on it. `totalVotingPower` is the frozen quorum denominator; recomputing it would let somebody move the bar after votes were cast. Amounts are strings of base units.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import dao_api
from crossly.model.common.error import Error
from crossly.model.dao.list_dao_proposals_response import ListDaoProposalsResponse
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
    api_instance = dao_api.DAOApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The proposal queue.
        api_response = api_instance.list_dao_proposals()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling DAOApi->list_dao_proposals: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListDaoProposalsResponse**

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

