# crossly.COSMApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cosm_attestation_anchor**](COSMApi.md#create_cosm_attestation_anchor) | **POST** /v1/cosm/attestations/{id}/anchor | Record a signature for a commitment anchored BY HAND.
[**create_cosm_auction**](COSMApi.md#create_cosm_auction) | **POST** /v1/cosm/auction | List an owned cosmetic for COSM.
[**create_cosm_auction_buy**](COSMApi.md#create_cosm_auction_buy) | **POST** /v1/cosm/auction/{id}/buy | Buy an open listing.
[**create_cosm_cosmetic_buy**](COSMApi.md#create_cosm_cosmetic_buy) | **POST** /v1/cosm/cosmetics/{id}/buy | Buy an earned-tier cosmetic. The COSM is DESTROYED.
[**create_cosm_cosmetic_buy_cbx**](COSMApi.md#create_cosm_cosmetic_buy_cbx) | **POST** /v1/cosm/cosmetics/{id}/buy-cbx | Buy a dollar-priced cosmetic, paying in CBX.
[**create_cosm_cosmetic_claim**](COSMApi.md#create_cosm_cosmetic_claim) | **POST** /v1/cosm/cosmetics/{id}/claim | Claim a stake-exclusive cosmetic once tenure qualifies.
[**create_cosm_fusion**](COSMApi.md#create_cosm_fusion) | **POST** /v1/cosm/fusion/{recipeId} | Fuse two cosmetics plus COSM into a rarer one.
[**create_cosm_handle**](COSMApi.md#create_cosm_handle) | **POST** /v1/cosm/handles | Claim a vanity handle, burning COSM.
[**create_cosm_withdrawal**](COSMApi.md#create_cosm_withdrawal) | **POST** /v1/cosm/withdrawals | Request a withdrawal to your own proven wallet. REFUSES today.
[**delete_cosm_handle**](COSMApi.md#delete_cosm_handle) | **DELETE** /v1/cosm/handles | Release a handle. NOTHING IS REFUNDED.
[**delete_cosm_peg**](COSMApi.md#delete_cosm_peg) | **DELETE** /v1/cosm/pegs/{listingId} | Stop repricing. The current ask stays where it is.
[**get_cosm_attestation_proof**](COSMApi.md#get_cosm_attestation_proof) | **GET** /v1/cosm/attestations/{id}/proof | A Merkle inclusion proof for one subject, against a published root.
[**get_cosm_auction_quote**](COSMApi.md#get_cosm_auction_quote) | **GET** /v1/cosm/auction/quote | What an auction listing would cost in fees.
[**get_cosm_balance**](COSMApi.md#get_cosm_balance) | **GET** /v1/cosm/balance | A subject&#39;s COSM balance and the earn rate in force.
[**get_cosm_employee_fee_quote**](COSMApi.md#get_cosm_employee_fee_quote) | **GET** /v1/cosm/employee/fee-quote | What one shop-employee conversation will cost, in COSM.
[**get_cosm_handle**](COSMApi.md#get_cosm_handle) | **GET** /v1/cosm/handles/{handle} | Is this handle available, and what does it cost?
[**get_cosm_stake_tenure**](COSMApi.md#get_cosm_stake_tenure) | **GET** /v1/cosm/stake-tenure | How long a subject has held a stake continuously, in days.
[**get_cosm_supply**](COSMApi.md#get_cosm_supply) | **GET** /v1/cosm/supply | Total supply — minted, burned, circulating.
[**list_cosm_attestations**](COSMApi.md#list_cosm_attestations) | **GET** /v1/cosm/attestations | Published Merkle commitments. What you can check instead of trusting us.
[**list_cosm_auction**](COSMApi.md#list_cosm_auction) | **GET** /v1/cosm/auction | Open auction listings, priced in COSM.
[**list_cosm_cosmetics**](COSMApi.md#list_cosm_cosmetics) | **GET** /v1/cosm/cosmetics | The cosmetics catalogue.
[**list_cosm_goals**](COSMApi.md#list_cosm_goals) | **GET** /v1/cosm/goals | Community burn goal progress.
[**list_cosm_inventory**](COSMApi.md#list_cosm_inventory) | **GET** /v1/cosm/inventory | Cosmetics a subject holds.
[**list_cosm_pegs**](COSMApi.md#list_cosm_pegs) | **GET** /v1/cosm/pegs | CBX-pegged listings and why each last moved.
[**list_cosm_supply_epochs**](COSMApi.md#list_cosm_supply_epochs) | **GET** /v1/cosm/supply/epochs | Per-epoch emission against the backstop.
[**list_cosm_supply_schedule**](COSMApi.md#list_cosm_supply_schedule) | **GET** /v1/cosm/supply/schedule | The published emission taper. Fixed years ahead.
[**list_cosm_unlocks**](COSMApi.md#list_cosm_unlocks) | **GET** /v1/cosm/unlocks | Which spatial cosmetic values this subject may apply.
[**list_cosm_withdrawals**](COSMApi.md#list_cosm_withdrawals) | **GET** /v1/cosm/withdrawals | Withdrawal history, and whether withdrawals are open at all.
[**update_cosm_cosmetic_unlock**](COSMApi.md#update_cosm_cosmetic_unlock) | **PUT** /v1/cosm/cosmetics/{id}/unlock | Set (or clear) what a cosmetic unlocks spatially.
[**update_cosm_peg**](COSMApi.md#update_cosm_peg) | **PUT** /v1/cosm/pegs | Set or update a CBX price peg. OFF unless you turn it on.


# **create_cosm_attestation_anchor**
> CreateCosmAttestationAnchorResponse create_cosm_attestation_anchor(id)

Record a signature for a commitment anchored BY HAND.

An ops tool, not a trust boundary. Automated anchoring needs an RPC and a dedicated key; until those are wired, `attestationMemo()` emits exactly the bytes to publish, and this records the resulting signature so the verifiable story is available before the automation is. IT VERIFIES NOTHING beyond the signature’s shape — there is no RPC here to confirm the transaction exists or that its memo matches. A wrong signature recorded here produces a commitment that LOOKS anchored and is not, which is worse than unanchored. Refuses to overwrite an existing anchor.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.create_cosm_attestation_anchor_response import CreateCosmAttestationAnchorResponse
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
    api_instance = cosm_api.COSMApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Record a signature for a commitment anchored BY HAND.
        api_response = api_instance.create_cosm_attestation_anchor(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->create_cosm_attestation_anchor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateCosmAttestationAnchorResponse**

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

# **create_cosm_auction**
> CreateCosmAuctionResponse create_cosm_auction()

List an owned cosmetic for COSM.

Refuses a BOUND item with 403. The bound flag is CHECK-derived from how the item was acquired, so the refusal cannot be bypassed by writing a different flag. One open listing per item, enforced by a unique index — otherwise the same cosmetic could be listed twice and sold to two buyers. `askBaseUnits` is a STRING of base units and must exceed 1.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.create_cosm_auction_response import CreateCosmAuctionResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List an owned cosmetic for COSM.
        api_response = api_instance.create_cosm_auction()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->create_cosm_auction: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateCosmAuctionResponse**

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

# **create_cosm_auction_buy**
> CreateCosmFusionResponse create_cosm_auction_buy(id)

Buy an open listing.

Three ledger rows: the buyer is debited the ask, the seller is credited it, and the fee burns against the seller. Net supply falls by exactly the fee. The listing is claimed out of `open` BEFORE any COSM moves, so the loser of a race is refused rather than debited. Buying your own listing is refused by a database CHECK: it would burn the fee for nothing and is the obvious way to fake a market price.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.create_cosm_fusion_response import CreateCosmFusionResponse
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
    api_instance = cosm_api.COSMApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Buy an open listing.
        api_response = api_instance.create_cosm_auction_buy(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->create_cosm_auction_buy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateCosmFusionResponse**

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

# **create_cosm_cosmetic_buy**
> CreateCosmCosmeticBuyResponse create_cosm_cosmetic_buy(id)

Buy an earned-tier cosmetic. The COSM is DESTROYED.

Not credited to a treasury. Keeping it would make cosmetics a round trip rather than a sink, and the epoch backstop is computed FROM the burn — recycling would quietly uncouple emission from consumption. Refuses a premium or stake-exclusive SKU: those are not sold for COSM. Also counts toward any open community burn goal.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.cosm.create_cosm_cosmetic_buy_response import CreateCosmCosmeticBuyResponse
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
    api_instance = cosm_api.COSMApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Buy an earned-tier cosmetic. The COSM is DESTROYED.
        api_response = api_instance.create_cosm_cosmetic_buy(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->create_cosm_cosmetic_buy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateCosmCosmeticBuyResponse**

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

# **create_cosm_cosmetic_buy_cbx**
> CreateCosmCosmeticBuyCbxResponse create_cosm_cosmetic_buy_cbx(id)

Buy a dollar-priced cosmetic, paying in CBX.

The SKU's `priceCents` is paid from the subject's EARNED CBX at spot. `requestKey` (8-64 chars, one per purchase attempt) makes a retry the same purchase. If the grant fails after payment — sold out, already held — the CBX spend is reversed. Refuses an earned (COSM) or stake-exclusive SKU.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.create_cosm_cosmetic_buy_cbx_response import CreateCosmCosmeticBuyCbxResponse
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
    api_instance = cosm_api.COSMApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Buy a dollar-priced cosmetic, paying in CBX.
        api_response = api_instance.create_cosm_cosmetic_buy_cbx(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->create_cosm_cosmetic_buy_cbx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateCosmCosmeticBuyCbxResponse**

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

# **create_cosm_cosmetic_claim**
> CreateCosmCosmeticClaimResponse create_cosm_cosmetic_claim(id)

Claim a stake-exclusive cosmetic once tenure qualifies.

Bound forever, and purchasable by nobody at any price in any currency. What people buy in cosmetics is STATUS, and anything purchasable is by definition available to anyone with money — an item money cannot buy is strictly rarer than an expensive one. Tenure is the LONGEST CONTINUOUS active stake, not time since first staking: somebody who staked, unstaked and staked again has not held continuously, and that is the whole claim the item makes. A cooling stake does not count, because the commitment is already being withdrawn. Returns `granted: false` with the tenure and the requirement when it is short — that is the normal answer, not an error. Idempotent: claiming twice while the first copy is held is a no-op.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.create_cosm_cosmetic_claim_response import CreateCosmCosmeticClaimResponse
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
    api_instance = cosm_api.COSMApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Claim a stake-exclusive cosmetic once tenure qualifies.
        api_response = api_instance.create_cosm_cosmetic_claim(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->create_cosm_cosmetic_claim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateCosmCosmeticClaimResponse**

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

# **create_cosm_fusion**
> CreateCosmFusionResponse create_cosm_fusion(recipe_id)

Fuse two cosmetics plus COSM into a rarer one.

The deepest sink available: it destroys on three axes at once — both input items AND the COSM cost — while producing something whose scarcity is real, because a recipe is the only route to it. Inputs must be owned, live, UNBOUND and flagged `fusable`. Stake-exclusive items can never be consumed: there is no way to reissue one without falsifying its scarcity, so the loss would be unrecoverable. An open listing on a consumed input is cancelled, since the owner has just chosen fusion over selling.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.create_cosm_fusion_response import CreateCosmFusionResponse
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
    api_instance = cosm_api.COSMApi(api_client)
    recipe_id = "recipeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fuse two cosmetics plus COSM into a rarer one.
        api_response = api_instance.create_cosm_fusion(recipe_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->create_cosm_fusion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe_id** | **str**|  |

### Return type

**CreateCosmFusionResponse**

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

# **create_cosm_handle**
> CreateCosmHandleResponse create_cosm_handle()

Claim a vanity handle, burning COSM.

One live handle per subject, enforced by a unique index. Collecting handles is a land grab that makes the good names unavailable, not a sink. A handle is released rather than deleted when given up, so the record of who held it survives — a handle that silently changed owner is the same impersonation problem from the other direction. There is no refund on release: the COSM was burned, and refunding would mean minting.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.cosm.create_cosm_handle_response import CreateCosmHandleResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Claim a vanity handle, burning COSM.
        api_response = api_instance.create_cosm_handle()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->create_cosm_handle: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateCosmHandleResponse**

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

# **create_cosm_withdrawal**
> CreateCosmWithdrawalResponse create_cosm_withdrawal()

Request a withdrawal to your own proven wallet. REFUSES today.

Returns 409 with the outstanding preconditions until COSM is transferable. Built and switched off deliberately: a withdrawal rail written in a hurry the week it is cleared is the one that ships with mistakes. THE DESTINATION IS NOT A PARAMETER. It resolves to this subject’s own VERIFIED connected wallet, because a per-request destination is how a compromised session drains a balance to somebody else’s address. Idempotent on `externalId`. The debit lands before anything is minted, so a crash leaves a recoverable state rather than tokens in a wallet with no debit behind them.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.cosm.create_cosm_withdrawal_response import CreateCosmWithdrawalResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Request a withdrawal to your own proven wallet. REFUSES today.
        api_response = api_instance.create_cosm_withdrawal()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->create_cosm_withdrawal: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateCosmWithdrawalResponse**

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

# **delete_cosm_handle**
> DeleteCosmHandleResponse delete_cosm_handle()

Release a handle. NOTHING IS REFUNDED.

The COSM paid for a handle was BURNED, so there is nothing to give back — refunding would mean minting, which no support flow should be able to do. Say that in the UI before calling this; a user who expects a refund will read silence as a bug. The handle returns to the pool and can be claimed by anyone, including somebody else, so releasing is not a way to park one. Returns `released: false` when the subject held none.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.delete_cosm_handle_response import DeleteCosmHandleResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Release a handle. NOTHING IS REFUNDED.
        api_response = api_instance.delete_cosm_handle()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->delete_cosm_handle: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**DeleteCosmHandleResponse**

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

# **delete_cosm_peg**
> DeleteCosmPegResponse delete_cosm_peg(listing_id)

Stop repricing. The current ask stays where it is.

Disabling means “stop moving it”, not “revert to something the buyer never saw”. The terms are kept, so re-enabling later does not mean re-entering them.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.delete_cosm_peg_response import DeleteCosmPegResponse
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
    api_instance = cosm_api.COSMApi(api_client)
    listing_id = "listingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Stop repricing. The current ask stays where it is.
        api_response = api_instance.delete_cosm_peg(listing_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->delete_cosm_peg: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **str**|  |

### Return type

**DeleteCosmPegResponse**

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

# **get_cosm_attestation_proof**
> GetCosmAttestationProofResponse get_cosm_attestation_proof(id)

A Merkle inclusion proof for one subject, against a published root.

Returns `canonicalLeaf`, a `proof` of sibling hashes, and the `root`. VERIFY IT YOURSELF rather than trusting `verified`: hash the leaf with a 0x00 prefix, then fold each proof step with a 0x01 prefix, ordering the two hashes lexicographically at each step, and compare to the root. That is sixteen lines in any language and needs nothing from us. The prefixes are not decoration — without them an internal node is indistinguishable from a leaf and membership of uncommitted data can be forged. Returns 409 if the underlying data no longer reproduces the published root. That is a disclosure event, not a retryable error: the published root stands and a proof against a rebuilt one would be worthless.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.cosm.get_cosm_attestation_proof_response import GetCosmAttestationProofResponse
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
    api_instance = cosm_api.COSMApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A Merkle inclusion proof for one subject, against a published root.
        api_response = api_instance.get_cosm_attestation_proof(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->get_cosm_attestation_proof: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetCosmAttestationProofResponse**

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

# **get_cosm_auction_quote**
> GetCosmAuctionQuoteResponse get_cosm_auction_quote()

What an auction listing would cost in fees.

Quote before committing. The fee is 8% of the ask, rounded UP so a small listing can never pay nothing — a zero-fee listing would be a free transfer channel, which is the one thing the design forbids outright. The seller always nets something, and a database CHECK asserts the same bound.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.get_cosm_auction_quote_response import GetCosmAuctionQuoteResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What an auction listing would cost in fees.
        api_response = api_instance.get_cosm_auction_quote()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->get_cosm_auction_quote: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetCosmAuctionQuoteResponse**

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

# **get_cosm_balance**
> GetCosmBalanceResponse get_cosm_balance()

A subject's COSM balance and the earn rate in force.

Balances are STRINGS of base units, and COSM has six decimals — divide by 1e6 to display. They are strings because a JSON number loses precision past 2^53, which is only about nine billion COSM: it would work in testing and corrupt balances at scale. `taper` is the emission step currently in force, which depends on lifetime supply rather than on anything about this subject — two sellers earning the same week always see the same taper.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.cosm.get_cosm_balance_response import GetCosmBalanceResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # A subject's COSM balance and the earn rate in force.
        api_response = api_instance.get_cosm_balance()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->get_cosm_balance: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetCosmBalanceResponse**

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

# **get_cosm_employee_fee_quote**
> GetCosmEmployeeFeeQuoteResponse get_cosm_employee_fee_quote()

What one shop-employee conversation will cost, in COSM.

A quote, priced with the SAME functions the charge uses, so the figure shown is the figure taken. Half of the fee BURNS and half moves to the market pool as a tax; the two always sum to the total exactly, because the split is applied in cents and the remainder is handed to the pool rather than derived from the complementary basis points. A pure burn would make the employee a deflation lever and nothing else; a pure transfer would make it a tax with no sink. Reads nothing and charges nothing — safe to call on every keystroke.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.get_cosm_employee_fee_quote_response import GetCosmEmployeeFeeQuoteResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # What one shop-employee conversation will cost, in COSM.
        api_response = api_instance.get_cosm_employee_fee_quote()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->get_cosm_employee_fee_quote: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetCosmEmployeeFeeQuoteResponse**

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

# **get_cosm_handle**
> GetCosmHandleResponse get_cosm_handle(handle)

Is this handle available, and what does it cost?

Reasons for unavailability: `invalid_shape`, `reserved`, `taken`. Handles are lowercased and constrained to a narrow character class, because anything that can be made to LOOK like another handle is an impersonation vector rather than an expressive option. Priced by length: short names are scarcer. Uniqueness is platform-wide, not per merchant — it is a URL namespace.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.cosm.get_cosm_handle_response import GetCosmHandleResponse
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
    api_instance = cosm_api.COSMApi(api_client)
    handle = "handle_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Is this handle available, and what does it cost?
        api_response = api_instance.get_cosm_handle(handle)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->get_cosm_handle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**|  |

### Return type

**GetCosmHandleResponse**

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

# **get_cosm_stake_tenure**
> GetCosmStakeTenureResponse get_cosm_stake_tenure()

How long a subject has held a stake continuously, in days.

The figure every stake-exclusive grant is decided on, readable on its own so a UI can show progress rather than only reporting failure at claim time. LONGEST CONTINUOUS active stake — a gap resets it, and a cooling stake does not count.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.get_cosm_stake_tenure_response import GetCosmStakeTenureResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # How long a subject has held a stake continuously, in days.
        api_response = api_instance.get_cosm_stake_tenure()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->get_cosm_stake_tenure: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetCosmStakeTenureResponse**

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

# **get_cosm_supply**
> GetCosmSupplyResponse get_cosm_supply()

Total supply — minted, burned, circulating.

The one question a holder of an emitted currency cannot answer for themselves. Every figure is derived from the ledger rather than a cached counter, so it cannot drift from the rows it summarises. `reconciles` is the check you can run against us: minted minus burned minus reversed must equal the sum of every balance, and the auction debit/credit pair must cancel exactly. False means a bug on our side, not stale data. Once COSM is transferable the on-chain `total_minted` emitted by `cosm-minter` is the authoritative figure and this becomes the convenient one.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.cosm.get_cosm_supply_response import GetCosmSupplyResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Total supply — minted, burned, circulating.
        api_response = api_instance.get_cosm_supply()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->get_cosm_supply: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetCosmSupplyResponse**

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

# **list_cosm_attestations**
> ListCosmAttestationsResponse list_cosm_attestations()

Published Merkle commitments. What you can check instead of trusting us.

Two claims become verifiable here. `cosm_emission` commits an epoch’s activity claims, so anybody can confirm emission never exceeded the sum of committed real activity — and every input is in the leaf, so the payout arithmetic can be rechecked, not just membership. `cbx_liability` commits every balance, which is the half of proof-of-reserve usually hand-waved. READ `anchoredAt` BEFORE RELYING ON A ROOT. Null means the commitment is computed and stored but NOT yet on chain — which makes it a row we could edit, so it proves nothing to somebody who does not already trust us. `totalBaseUnits` lets you check the sum without rebuilding the tree.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.list_cosm_attestations_response import ListCosmAttestationsResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Published Merkle commitments. What you can check instead of trusting us.
        api_response = api_instance.list_cosm_attestations()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->list_cosm_attestations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCosmAttestationsResponse**

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

# **list_cosm_auction**
> ListCosmAuctionResponse list_cosm_auction()

Open auction listings, priced in COSM.

A COSM-denominated peer market: buyers pay COSM, sellers receive COSM, and the 8% fee BURNS. It is not a cash market — a cash resale market for COSM-bought items would reintroduce the arbitrage between a fixed COSM price and a floating market price. `feeBaseUnits` was quoted when the listing was created and is held, because a fee recomputed at sale time is a quote nobody can rely on.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.list_cosm_auction_response import ListCosmAuctionResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Open auction listings, priced in COSM.
        api_response = api_instance.list_cosm_auction()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->list_cosm_auction: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCosmAuctionResponse**

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

# **list_cosm_cosmetics**
> ListCosmCosmeticsResponse list_cosm_cosmetics()

The cosmetics catalogue.

Tiers are DISJOINT and no SKU carries two prices: `premium` is cash only, `earned` is COSM only, `stake_exclusive` cannot be bought at any price in any currency. That is not a presentation choice — pricing one SKU in both currencies would expose a fixed COSM price to a floating market price, which is free money in the gap and hands limited editions to whoever automates it. `priceCents` is set only on premium, `priceBaseUnits` only on earned.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.list_cosm_cosmetics_response import ListCosmCosmeticsResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The cosmetics catalogue.
        api_response = api_instance.list_cosm_cosmetics()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->list_cosm_cosmetics: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCosmCosmeticsResponse**

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

# **list_cosm_goals**
> ListCosmGoalsResponse list_cosm_goals()

Community burn goal progress.

Aggregate burn crossing a threshold unlocks a cosmetic for everyone who contributed — scoped to contributors, because a goal that rewarded non-participants makes contributing irrational. Only burns inside the window count; a goal counting all history would complete the moment it was created. `progressBps` is capped at 10000: the total is snapshotted on completion so a bar never reads over 100%.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.list_cosm_goals_response import ListCosmGoalsResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Community burn goal progress.
        api_response = api_instance.list_cosm_goals()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->list_cosm_goals: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCosmGoalsResponse**

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

# **list_cosm_inventory**
> ListCosmInventoryResponse list_cosm_inventory()

Cosmetics a subject holds.

`bound` is derived from how it was acquired and is enforced by a database CHECK, not set by hand: a stake-exclusive grant and a make-good are bound forever, everything else trades. Bound items cannot be listed on the auction house or used as a fusion input. `editionNumber` identifies the ITEM and travels with it through a sale, because a reissued #7 would falsify every scarcity claim a market has priced.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.list_cosm_inventory_response import ListCosmInventoryResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Cosmetics a subject holds.
        api_response = api_instance.list_cosm_inventory()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->list_cosm_inventory: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCosmInventoryResponse**

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

# **list_cosm_pegs**
> ListCosmPegsResponse list_cosm_pegs()

CBX-pegged listings and why each last moved.

A peg holds a CBX ask at a dollar target. `lastReason` says what the last cycle did: repriced, no_rate, below_threshold, clamped_floor, clamped_ceiling or clamped_change. A seller asking why their price has not moved deserves an answer that is not “it should have”. The repricer reads a 24h MINIMUM rate, never spot — tracking spot would let somebody pump CBX, watch the ask drop, and pay with cheaply bought tokens.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.list_cosm_pegs_response import ListCosmPegsResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # CBX-pegged listings and why each last moved.
        api_response = api_instance.list_cosm_pegs()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->list_cosm_pegs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCosmPegsResponse**

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

# **list_cosm_supply_epochs**
> ListCosmSupplyEpochsResponse list_cosm_supply_epochs()

Per-epoch emission against the backstop.

`demanded` is what activity would have earned at full rate; `emitted` is what was actually credited. Both are reported because storing only the second would make a refusal indistinguishable from a quiet rate cut. `ceilingBound` should be rare — the governor is the emission rate itself, which is a share of transaction value, so the ceiling binding means an anomaly rather than a busy week.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.cosm.list_cosm_supply_epochs_response import ListCosmSupplyEpochsResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Per-epoch emission against the backstop.
        api_response = api_instance.list_cosm_supply_epochs()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->list_cosm_supply_epochs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCosmSupplyEpochsResponse**

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

# **list_cosm_supply_schedule**
> ListCosmSupplyScheduleResponse list_cosm_supply_schedule()

The published emission taper. Fixed years ahead.

Indexed on CUMULATIVE MINTED, which is monotonic and which nothing anybody does can move backwards. Net circulating supply would be self-correcting against a healthy sink and would also be reflexive — burning to hold the taper back would become a strategy. A schedule nobody can game beats a clever loop. The final step is a floor, not zero: a terminating schedule is a loyalty programme with an expiry date, where the last cohort to join earns nothing.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.list_cosm_supply_schedule_response import ListCosmSupplyScheduleResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The published emission taper. Fixed years ahead.
        api_response = api_instance.list_cosm_supply_schedule()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->list_cosm_supply_schedule: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCosmSupplyScheduleResponse**

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

# **list_cosm_unlocks**
> ListCosmUnlocksResponse list_cosm_unlocks()

Which spatial cosmetic values this subject may apply.

Owning a cosmetic is what permits setting the room value it claims. Values no SKU claims — the stock walls, floors and themes — are free and are not listed here. Paint a picker from this rather than discovering a refusal on submit: the redecorate endpoint returns the locked items by name so a swatch can be greyed out instead.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.cosm.list_cosm_unlocks_response import ListCosmUnlocksResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Which spatial cosmetic values this subject may apply.
        api_response = api_instance.list_cosm_unlocks()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->list_cosm_unlocks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCosmUnlocksResponse**

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

# **list_cosm_withdrawals**
> ListCosmWithdrawalsResponse list_cosm_withdrawals()

Withdrawal history, and whether withdrawals are open at all.

COSM does not leave the platform yet. `open` is false and `outstanding` lists the preconditions still to be met: an audited minter, a securities opinion, a money-transmission review, and the emission invariant proven under real volume. None of them has a date, so do not present one. The endpoint exists so a client can show that state honestly rather than hiding the feature and surprising somebody later.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.cosm.list_cosm_withdrawals_response import ListCosmWithdrawalsResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Withdrawal history, and whether withdrawals are open at all.
        api_response = api_instance.list_cosm_withdrawals()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->list_cosm_withdrawals: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListCosmWithdrawalsResponse**

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

# **update_cosm_cosmetic_unlock**
> UpdateCosmCosmeticUnlockResponse update_cosm_cosmetic_unlock(id)

Set (or clear) what a cosmetic unlocks spatially.

A cosmetic can gate a spatial control — a theme, a prop, a room feature — by naming a key/value pair the scene reads. Both or neither: a key with no value would claim EVERY value of that key and silently gate the whole control, so passing one without the other clears both. Pass two nulls to remove the gate entirely, which makes the control free for everyone. Treasury scope — this changes what every holder can reach, not one subject.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.common.error import Error
from crossly.model.cosm.update_cosm_cosmetic_unlock_response import UpdateCosmCosmeticUnlockResponse
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
    api_instance = cosm_api.COSMApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set (or clear) what a cosmetic unlocks spatially.
        api_response = api_instance.update_cosm_cosmetic_unlock(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->update_cosm_cosmetic_unlock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateCosmCosmeticUnlockResponse**

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

# **update_cosm_peg**
> UpdateCosmPegResponse update_cosm_peg()

Set or update a CBX price peg. OFF unless you turn it on.

Holds a CBX ask at a dollar target, repriced hourly against a 24h MINIMUM rate. Three bounds, each for a different failure: `maxChangeBps` stops one bad reading posting an absurd ask (it converges over cycles instead), `floorBaseUnits` and `ceilingBaseUnits` are YOUR limits so a sustained real move never posts a price you did not consider, and `minChangeBps` stops the ask being rewritten for a fraction of a percent. Accepting CBX means holding CBX. The peg protects the dollar value of the ASK; it cannot protect the value of tokens once you have them.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import cosm_api
from crossly.model.cosm.update_cosm_peg_response import UpdateCosmPegResponse
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
    api_instance = cosm_api.COSMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Set or update a CBX price peg. OFF unless you turn it on.
        api_response = api_instance.update_cosm_peg()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling COSMApi->update_cosm_peg: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**UpdateCosmPegResponse**

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

