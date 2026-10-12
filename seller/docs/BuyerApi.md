# crossly.BuyerApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_spatial_auction_room_bid**](BuyerApi.md#create_spatial_auction_room_bid) | **POST** /v1/spatial/auction/rooms/{sceneId}/bid | Bid on the lot currently up in a room.


# **create_spatial_auction_room_bid**
> CreateSpatialAuctionRoomBidResponse create_spatial_auction_room_bid(scene_id)

Bid on the lot currently up in a room.

Bids on whatever the auctioneer has up RIGHT NOW. Pass `lotId` to say which lot you believe that is: it is checked against the rostrum rather than used in its place, and a mismatch answers 409 with the lot that is actually up, so a stale catalogue cannot buy you something you never looked at. `amountCents` is CENTS and must be at least the room state's `minimumNextBidCents` — do not compute that yourself, because the opening bid on a lot is floored at the START price rather than start + step. Below it you get 400 `bid_too_low` carrying `details.minimumNextBidCents`, which is the figure the transaction itself used; raise to that and retry. THIS AUCTION HOUSE SELLS DIGITAL GOODS ONLY. A physical lot is refused 403 `forbidden` with `details.reason: \"physical_lot\"`, checked against the listing on every single bid rather than once when the room was set up. Bids by one person on one lot are throttled to a few per second — 429 `bidding_too_fast` carries `retryInSeconds`. A hammered or skipped lot answers 409 `lot_closed`. A room you may not enter answers 404, the same as one that does not exist. Success is the bid RECORDED, not the lot won: the reply names the topic the price moves on, and somebody may outbid you on the next frame.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import buyer_api
from crossly.model.spatial.create_spatial_auction_room_bid_response import CreateSpatialAuctionRoomBidResponse
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
    api_instance = buyer_api.BuyerApi(api_client)
    scene_id = "sceneId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Bid on the lot currently up in a room.
        api_response = api_instance.create_spatial_auction_room_bid(scene_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling BuyerApi->create_spatial_auction_room_bid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **str**|  |

### Return type

**CreateSpatialAuctionRoomBidResponse**

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

