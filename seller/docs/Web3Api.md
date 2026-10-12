# crossly.Web3Api

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_web3_alert**](Web3Api.md#create_web3_alert) | **POST** /v1/web3/alerts | Set a price alert on a token, or on a whole collection without tokenId: you are notified when one is listed at or below &#x60;price&#x60; (the chain&#39;s native coin). Setting it again moves the price.
[**create_web3_auction**](Web3Api.md#create_web3_auction) | **POST** /v1/web3/auctions | Start an English auction on a token in your linked wallet: &#x60;reserve&#x60; is the opening bid in the chain&#39;s native coin, &#x60;hours&#x60; its length (1–720). Bids must rise 5%; a late bid extends the end by 10 minutes.
[**create_web3_auction_cancel**](Web3Api.md#create_web3_auction_cancel) | **POST** /v1/web3/auctions/{id}/cancel | Call off your auction while it has no bids.
[**create_web3_creator_claim**](Web3Api.md#create_web3_creator_claim) | **POST** /v1/web3/creator/claims | Claim an EVM collection as its creator: its owner() must be one of your verified wallets. Returns &#x60;{ chain, contract }&#x60;.
[**create_web3_crosslist**](Web3Api.md#create_web3_crosslist) | **POST** /v1/web3/crosslist | Submit signed Seaport listings for several marketplaces at once (crossly, opensea); results per marketplace.
[**create_web3_drop_remind**](Web3Api.md#create_web3_drop_remind) | **POST** /v1/web3/drops/{id}/remind | Turn the 15-minute reminder for a drop on, or off if it already is. Returns &#x60;{ remindMe }&#x60;.
[**create_web3_favorite**](Web3Api.md#create_web3_favorite) | **POST** /v1/web3/favorites | Favourite an NFT, or unfavourite it if it already is. Returns &#x60;{ favorited }&#x60;.
[**create_web3_launch**](Web3Api.md#create_web3_launch) | **POST** /v1/web3/launches | Draft a launchpad collection: name, symbol, supply, mint price (wei of the chain’s native currency), schedule, optional holder phase and royalty. Crossly takes 5% of each mint inside the contract.
[**create_web3_launch_airdrop**](Web3Api.md#create_web3_launch_airdrop) | **POST** /v1/web3/launches/{id}/airdrop | Plan an airdrop (one free NFT each, up to 500) to &#x60;addresses&#x60; and/or the holders of &#x60;holdersOf&#x60;. Returns the transactions for the owner wallet; no payment moves.
[**create_web3_launch_art**](Web3Api.md#create_web3_launch_art) | **POST** /v1/web3/launches/{id}/art | Append per-token art (image URL, name, traits), up to the supply, before the reveal. Returns &#x60;{ count }&#x60;.
[**create_web3_launch_confirm_deploy**](Web3Api.md#create_web3_launch_confirm_deploy) | **POST** /v1/web3/launches/{id}/confirm-deploy | Confirm a sent deploy transaction: the contract must be the Crossly launch contract with this draft’s settings; it then goes live.
[**create_web3_launch_follow_creator**](Web3Api.md#create_web3_launch_follow_creator) | **POST** /v1/web3/launches/{id}/follow-creator | Follow the creator of a launch: their launches are announced to you, and again when each opens. Returns &#x60;{ following }&#x60;.
[**create_web3_launch_reveal**](Web3Api.md#create_web3_launch_reveal) | **POST** /v1/web3/launches/{id}/reveal | Reveal the art: one random offset maps every token to its asset for good. Returns &#x60;{ revealedAt }&#x60;.
[**create_web3_order**](Web3Api.md#create_web3_order) | **POST** /v1/web3/orders | Place a signed Seaport 1.6 order (listing, offer or collection offer) in the Crossly book.
[**create_web3_order_cancel**](Web3Api.md#create_web3_order_cancel) | **POST** /v1/web3/orders/{chain}/{hash}/cancel | Take one of your orders out of the Crossly book.
[**create_web3_order_fulfillment_batch**](Web3Api.md#create_web3_order_fulfillment_batch) | **POST** /v1/web3/orders/fulfillment-batch | Fulfilments for sweeping several listings in one Seaport transaction; unfillable ones are skipped with a reason.
[**create_web3_phygital**](Web3Api.md#create_web3_phygital) | **POST** /v1/web3/phygitals | Make an NFT you hold redeemable for one of your physical inventory items.
[**create_web3_phygital_redeem**](Web3Api.md#create_web3_phygital_redeem) | **POST** /v1/web3/phygitals/{id}/redeem | Redeem a phygital you hold (checked on-chain) for its physical item, with a shipping address. Once per phygital.
[**create_web3_phygital_redemption_ship**](Web3Api.md#create_web3_phygital_redemption_ship) | **POST** /v1/web3/phygitals/redemptions/{id}/ship | Mark a redemption shipped with its carrier and tracking number; the redeemer is notified.
[**create_web3_rarible_draft**](Web3Api.md#create_web3_rarible_draft) | **POST** /v1/web3/rarible/draft | Draft a Rarible V2 listing for an NFT in your linked wallet: the EIP-712 order to sign and whether Rarible&#39;s transfer proxy is approved.
[**create_web3_rarible_listing**](Web3Api.md#create_web3_rarible_listing) | **POST** /v1/web3/rarible/listings | Submit a signed Rarible V2 listing: the signature is verified, then the order is posted to Rarible and recorded.
[**create_web3_solana_list_tx**](Web3Api.md#create_web3_solana_list_tx) | **POST** /v1/web3/solana/{marketplace}/list-tx | Build an unsigned listing transaction on the Crossly book, Tensor or Magic Eden for a Solana NFT in your linked wallet.
[**create_web3_solana_listing**](Web3Api.md#create_web3_solana_listing) | **POST** /v1/web3/solana/{marketplace}/listings | Record a Crossly-book, Tensor or Magic Eden listing your wallet sent (read back from the chain first).
[**create_web3_solana_offer**](Web3Api.md#create_web3_solana_offer) | **POST** /v1/web3/solana/offers | Record a sent bid; it is recorded only once its trade state exists on chain.
[**create_web3_solana_offer_accept_tx**](Web3Api.md#create_web3_solana_offer_accept_tx) | **POST** /v1/web3/solana/offers/{hash}/accept-tx | Build the sale into a bid from your linked wallet that holds the NFT (sell + execute_sale, one transaction).
[**create_web3_solana_offer_cancel_tx**](Web3Api.md#create_web3_solana_offer_cancel_tx) | **POST** /v1/web3/solana/offers/{hash}/cancel-tx | Build the cancel of your bid: the SOL your other bids do not need comes back.
[**create_web3_solana_offer_confirm**](Web3Api.md#create_web3_solana_offer_confirm) | **POST** /v1/web3/solana/offers/{hash}/confirm | Apply a sent accept or cancel once the chain shows the bid closed.
[**create_web3_solana_offer_tx**](Web3Api.md#create_web3_solana_offer_tx) | **POST** /v1/web3/solana/offers/tx | Build a bid on a Solana NFT on Crossly&#39;s book for your linked wallet to sign; the SOL goes into your Auction House escrow.
[**create_web3_solana_order_buy_tx**](Web3Api.md#create_web3_solana_order_buy_tx) | **POST** /v1/web3/solana/orders/{hash}/buy-tx | Build the unsigned transaction that buys a Solana listing (price capped at the listed price).
[**create_web3_solana_order_confirm**](Web3Api.md#create_web3_solana_order_confirm) | **POST** /v1/web3/solana/orders/{hash}/confirm | Apply a sent Solana buy or delist to the book (the transaction is read back from the chain).
[**create_web3_solana_order_delist_tx**](Web3Api.md#create_web3_solana_order_delist_tx) | **POST** /v1/web3/solana/orders/{hash}/delist-tx | Build the unsigned transaction that takes your Solana listing down.
[**create_web3_solana_tensor_bid_accept_tx**](Web3Api.md#create_web3_solana_tensor_bid_accept_tx) | **POST** /v1/web3/solana/tensor-bids/accept-tx | Build the transaction that sells your NFT into a Tensor bid, never below &#x60;minLamports&#x60;.
[**create_web3_solana_tensor_bid_cancel_tx**](Web3Api.md#create_web3_solana_tensor_bid_cancel_tx) | **POST** /v1/web3/solana/tensor-bids/cancel-tx | Build the transaction that cancels your Tensor bid.
[**create_web3_solana_tensor_bid_place_tx**](Web3Api.md#create_web3_solana_tensor_bid_place_tx) | **POST** /v1/web3/solana/tensor-bids/place-tx | Build a Tensor collection bid (or trait bid with &#x60;trait&#x60;) for your Solana wallet to sign. Price in lamports.
[**create_web3_token_refresh**](Web3Api.md#create_web3_token_refresh) | **POST** /v1/web3/tokens/{chain}/{contract}/{tokenId}/refresh | Re-read a token&#39;s metadata from the chain&#39;s provider (name, traits, image — a new image is copied to Crossly&#39;s CDN). Once per token per 10 minutes.
[**create_web3_transaction**](Web3Api.md#create_web3_transaction) | **POST** /v1/web3/transactions | Apply a Seaport transaction&#39;s fills and cancels to the Crossly book (read from the receipt).
[**create_web3_wallet_challenge**](Web3Api.md#create_web3_wallet_challenge) | **POST** /v1/web3/wallets/challenge | Start linking a wallet: returns the message the wallet must sign.
[**create_web3_wallet_sync**](Web3Api.md#create_web3_wallet_sync) | **POST** /v1/web3/wallets/{id}/sync | Import a linked wallet&#39;s NFTs into inventory; archives ones that have left the wallet.
[**create_web3_wallet_verify**](Web3Api.md#create_web3_wallet_verify) | **POST** /v1/web3/wallets/verify | Finish linking a wallet with its signature over the challenge message.
[**delete_web3_alert**](Web3Api.md#delete_web3_alert) | **DELETE** /v1/web3/alerts/{id} | Delete a price alert.
[**delete_web3_holder_perk**](Web3Api.md#delete_web3_holder_perk) | **DELETE** /v1/web3/holder-perks/{id} | Remove a holder perk. Returns &#x60;{ ok }&#x60;.
[**delete_web3_launch**](Web3Api.md#delete_web3_launch) | **DELETE** /v1/web3/launches/{id} | Delete a launch draft that never went live. Returns &#x60;{ ok }&#x60;.
[**delete_web3_launch_follow_creator**](Web3Api.md#delete_web3_launch_follow_creator) | **DELETE** /v1/web3/launches/{id}/follow-creator | Stop following the creator of a launch. Returns &#x60;{ following }&#x60;.
[**delete_web3_marketplace_key**](Web3Api.md#delete_web3_marketplace_key) | **DELETE** /v1/web3/marketplace-keys/{marketplace} | Remove your own key for a marketplace; Crossly&#39;s key is used again.
[**delete_web3_wallet**](Web3Api.md#delete_web3_wallet) | **DELETE** /v1/web3/wallets/{id} | Unlink a wallet. Its NFTs stay in inventory but stop syncing.
[**get_web3_auction**](Web3Api.md#get_web3_auction) | **GET** /v1/web3/auctions/{chain}/{contract}/{tokenId} | A token&#39;s live (or latest) auction: reserve, end, top bid, bid count and the minimum next bid.
[**get_web3_browse**](Web3Api.md#get_web3_browse) | **GET** /v1/web3/browse | The Web3 directory&#39;s categories and chains, with how many collections each holds.
[**get_web3_collection**](Web3Api.md#get_web3_collection) | **GET** /v1/web3/collections/{chain}/{contract} | A collection: metadata and Crossly stats (floor, listed, volume, best collection offer).
[**get_web3_collection_depth**](Web3Api.md#get_web3_collection_depth) | **GET** /v1/web3/collections/{chain}/{contract}/depth | A collection&#39;s Crossly order book by price level — asks cheapest first, bids dearest first, with running totals — and the floor of every trait value.
[**get_web3_collection_insight**](Web3Api.md#get_web3_collection_insight) | **GET** /v1/web3/collections/{chain}/{contract}/insights | On-chain insights for a collection: holders, trait counts across the whole collection, recent transfers and a 30-day activity series.
[**get_web3_collection_item**](Web3Api.md#get_web3_collection_item) | **GET** /v1/web3/collections/{chain}/{contract}/items | A collection&#39;s NFTs: filter by traits (repeat trait&#x3D;Type:Value; OR within a type, AND across), search by name or token id, sort by id, rarity or Crossly price. Whole-collection once indexed.
[**get_web3_collection_trait**](Web3Api.md#get_web3_collection_trait) | **GET** /v1/web3/collections/{chain}/{contract}/traits | Every trait type and value in a collection, with how many tokens have each.
[**get_web3_collection_trait_token**](Web3Api.md#get_web3_collection_trait_token) | **GET** /v1/web3/collections/{chain}/{contract}/trait-tokens | Token ids in a collection with one trait — what a trait offer commits to.
[**get_web3_collector**](Web3Api.md#get_web3_collector) | **GET** /v1/web3/collector | Your collector perks: how many different NFTs you bought through Crossly, your Collector pin tier, relist rewards paid, and each NFT you still hold with the Bought on Crossly mark.
[**get_web3_creator**](Web3Api.md#get_web3_creator) | **GET** /v1/web3/creator/{chain}/{contract} | A collection’s creator dashboard: sales by marketplace and day, estimated royalties, holders, and for a launch the mint revenue and what is waiting to be withdrawn (wei of the chain’s native currency).
[**get_web3_crosslist_quote**](Web3Api.md#get_web3_crosslist_quote) | **GET** /v1/web3/crosslist/quote | Each marketplace&#39;s terms for listing a token: Crossly fee, OpenSea required fees and zone, Tensor availability.
[**get_web3_featured**](Web3Api.md#get_web3_featured) | **GET** /v1/web3/featured | The NFT home&#39;s featured collections: chosen by Crossly, else the hottest.
[**get_web3_inventory**](Web3Api.md#get_web3_inventory) | **GET** /v1/web3/inventory/{itemId} | The NFT behind an inventory item: its token, wallet, and open listings on every marketplace (null if it is not an NFT).
[**get_web3_launch_allowlist_root_tx**](Web3Api.md#get_web3_launch_allowlist_root_tx) | **GET** /v1/web3/launches/{id}/allowlist/root-tx | The setAllowlistRoot transaction for the allowlist Crossly holds (EVM, live): &#x60;{ chain, from, to, data }&#x60;.
[**get_web3_launch_deploy_tx**](Web3Api.md#get_web3_launch_deploy_tx) | **GET** /v1/web3/launches/{id}/deploy-tx | The contract-creation transaction for the draft: send it from the owner wallet, then confirm it. Returns &#x60;{ chain, from, data }&#x60;.
[**get_web3_launch_tool**](Web3Api.md#get_web3_launch_tool) | **GET** /v1/web3/launches/{id}/tools | A launch’s creator tools: allowlist size and root (and whether the contract has it yet), uploaded art and reveal, supply minted.
[**get_web3_order_fulfillment**](Web3Api.md#get_web3_order_fulfillment) | **GET** /v1/web3/orders/{chain}/{hash}/fulfillment | The signed order a taker passes to Seaport, after re-checking it can still fill.
[**get_web3_phygital**](Web3Api.md#get_web3_phygital) | **GET** /v1/web3/phygitals/{chain}/{contract}/{tokenId} | A token&#39;s phygital: the physical item it can be redeemed for, and whether it has been.
[**get_web3_phygital2**](Web3Api.md#get_web3_phygital2) | **GET** /v1/web3/phygitals | Phygitals you linked (with each redemption and its shipping address) and ones you redeemed.
[**get_web3_portfolio**](Web3Api.md#get_web3_portfolio) | **GET** /v1/web3/portfolio | Your NFTs with value (Crossly floor, else recent sales) and cost (what a linked wallet paid), realised sales, and USD totals at each day’s coin price.
[**get_web3_portfolio_tax**](Web3Api.md#get_web3_portfolio_tax) | **GET** /v1/web3/portfolio/tax | One calendar year of NFT disposals from your linked wallets as CSV text: acquired, sold, proceeds, cost basis, gain (coin and USD).
[**get_web3_profile**](Web3Api.md#get_web3_profile) | **GET** /v1/web3/profiles/{address} | A wallet&#39;s public profile: NFTs held, open Crossly listings, and activity.
[**get_web3_resolve**](Web3Api.md#get_web3_resolve) | **GET** /v1/web3/resolve/{chain}/{slug} | A collection&#39;s chain and contract from its readable URL slug (e.g. eth / boredapeyachtclub).
[**get_web3_solana_collection_tensor_bid**](Web3Api.md#get_web3_solana_collection_tensor_bid) | **GET** /v1/web3/solana/collections/{collection}/tensor-bids | A Solana collection’s Tensor bids (collection-wide and by trait), best first; price in lamports. Needs your Tensor key.
[**get_web3_token**](Web3Api.md#get_web3_token) | **GET** /v1/web3/tokens/{chain}/{contract}/{tokenId} | One NFT: metadata, traits, owner, open listings and offers, activity.
[**list_web3_activity**](Web3Api.md#list_web3_activity) | **GET** /v1/web3/activity | Listings, offers, sales and cancels in the Crossly book, newest first.
[**list_web3_alerts**](Web3Api.md#list_web3_alerts) | **GET** /v1/web3/alerts | Your NFT price alerts, with the cheapest open Crossly listing each one covers now.
[**list_web3_approvals**](Web3Api.md#list_web3_approvals) | **GET** /v1/web3/approvals | Your collections the OpenSea conduit is approved to move, per linked wallet.
[**list_web3_auctions**](Web3Api.md#list_web3_auctions) | **GET** /v1/web3/auctions | Live English auctions on the Crossly book, ending soonest first, each with its top bid and the least the next bid can be.
[**list_web3_browse_collections**](Web3Api.md#list_web3_browse_collections) | **GET** /v1/web3/browse/collections | Browse NFT collections by chain, category and name; sort hot (Crossly sales, listings, favourites), new, volume, floor or name.
[**list_web3_browse_tokens**](Web3Api.md#list_web3_browse_tokens) | **GET** /v1/web3/browse/tokens | Hot NFTs: what is for sale on Crossly first, then tokens from the hottest collections.
[**list_web3_bundles**](Web3Api.md#list_web3_bundles) | **GET** /v1/web3/bundles | Open bundle listings (2–30 NFTs for one price), newest first, by chain or by a contract any item is from.
[**list_web3_collection_history**](Web3Api.md#list_web3_collection_history) | **GET** /v1/web3/collections/{chain}/{contract}/history | Daily floor, sales, volume, holders and listed count for a collection, oldest first (up to 365 days).
[**list_web3_collections**](Web3Api.md#list_web3_collections) | **GET** /v1/web3/collections | Collections ranked by 30-day Crossly volume, with floor and listed count.
[**list_web3_creator_collections**](Web3Api.md#list_web3_creator_collections) | **GET** /v1/web3/creator/collections | Collections you are the creator of: your launches, and contracts you claimed by owning them.
[**list_web3_drops**](Web3Api.md#list_web3_drops) | **GET** /v1/web3/drops | Upcoming and live NFT drops (curated mints on the creator&#39;s own page), soonest first, with whether you asked to be reminded.
[**list_web3_holder_perks**](Web3Api.md#list_web3_holder_perks) | **GET** /v1/web3/holder-perks | Your holder perks: percent off your Crossly shop for holders of an NFT collection, best first.
[**list_web3_launches**](Web3Api.md#list_web3_launches) | **GET** /v1/web3/launches | Your launchpad collections (drafts and live), newest first, with minted count and phase.
[**list_web3_listings**](Web3Api.md#list_web3_listings) | **GET** /v1/web3/listings | Open NFT listings in the Crossly book — the cheapest per token.
[**list_web3_marketplace_keys**](Web3Api.md#list_web3_marketplace_keys) | **GET** /v1/web3/marketplace-keys | Your own marketplace API keys (last four characters only) and whether Crossly&#39;s key covers each marketplace.
[**list_web3_nfts**](Web3Api.md#list_web3_nfts) | **GET** /v1/web3/nfts | List the NFTs in your inventory, imported from your linked wallets.
[**list_web3_orders**](Web3Api.md#list_web3_orders) | **GET** /v1/web3/orders | Your orders in the Crossly book (listings and offers), any status.
[**list_web3_purchases**](Web3Api.md#list_web3_purchases) | **GET** /v1/web3/purchases | NFTs your linked wallets bought — on Crossly or any marketplace the chain feed saw — newest first, with price and whether you still hold each.
[**list_web3_rankings**](Web3Api.md#list_web3_rankings) | **GET** /v1/web3/rankings | Collections by sales volume over 24h, 7d or 30d, in one coin: the ETH chains together, or Polygon / Solana on their own.
[**list_web3_reserved**](Web3Api.md#list_web3_reserved) | **GET** /v1/web3/reserved | Private listings reserved for one of your linked wallets — only you can see or buy them.
[**list_web3_sales**](Web3Api.md#list_web3_sales) | **GET** /v1/web3/sales | The latest NFT sales across the directory, from the chain (Seaport and Blur) and the Crossly book, newest first; page with &#x60;before&#x60;.
[**list_web3_search**](Web3Api.md#list_web3_search) | **GET** /v1/web3/search | Find collections by contract address (every chain) or by name.
[**list_web3_search_tokens**](Web3Api.md#list_web3_search_tokens) | **GET** /v1/web3/search/tokens | Find tokens by collection name and number: &#39;pudgy 42&#39;, &#39;Bored Ape #1234&#39;.
[**list_web3_wallets**](Web3Api.md#list_web3_wallets) | **GET** /v1/web3/wallets | List your verified, linked wallets (EVM and Solana).
[**list_web3_watchlist**](Web3Api.md#list_web3_watchlist) | **GET** /v1/web3/watchlist | Your favourited NFTs, with the cheapest open Crossly listing and the last sale of each.
[**update_web3_holder_perk**](Web3Api.md#update_web3_holder_perk) | **PUT** /v1/web3/holder-perks | Set the percent off (100–5000 bps) holders of a collection get across your Crossly shop; one perk per collection.
[**update_web3_launch_allowlist**](Web3Api.md#update_web3_launch_allowlist) | **PUT** /v1/web3/launches/{id}/allowlist | Replace the early-phase allowlist (up to 10,000 wallets). EVM live launches get back &#x60;rootTx&#x60;, the setAllowlistRoot transaction for the owner wallet.
[**update_web3_marketplace_key**](Web3Api.md#update_web3_marketplace_key) | **PUT** /v1/web3/marketplace-keys/{marketplace} | Save your own API key for a marketplace (checked against the marketplace first where it can be); stored encrypted.


# **create_web3_alert**
> IdResponse create_web3_alert()

Set a price alert on a token, or on a whole collection without tokenId: you are notified when one is listed at or below `price` (the chain's native coin). Setting it again moves the price.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.id_response import IdResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Set a price alert on a token, or on a whole collection without tokenId: you are notified when one is listed at or below `price` (the chain's native coin). Setting it again moves the price.
        api_response = api_instance.create_web3_alert()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_alert: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**IdResponse**

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

# **create_web3_auction**
> CreateWeb3AuctionResponse create_web3_auction()

Start an English auction on a token in your linked wallet: `reserve` is the opening bid in the chain's native coin, `hours` its length (1–720). Bids must rise 5%; a late bid extends the end by 10 minutes.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_auction_response import CreateWeb3AuctionResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Start an English auction on a token in your linked wallet: `reserve` is the opening bid in the chain's native coin, `hours` its length (1–720). Bids must rise 5%; a late bid extends the end by 10 minutes.
        api_response = api_instance.create_web3_auction()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_auction: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3AuctionResponse**

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

# **create_web3_auction_cancel**
> OkResponse create_web3_auction_cancel(id)

Call off your auction while it has no bids.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.ok_response import OkResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Call off your auction while it has no bids.
        api_response = api_instance.create_web3_auction_cancel(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_auction_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**OkResponse**

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

# **create_web3_creator_claim**
> CreateWeb3CreatorClaimResponse create_web3_creator_claim()

Claim an EVM collection as its creator: its owner() must be one of your verified wallets. Returns `{ chain, contract }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_creator_claim_response import CreateWeb3CreatorClaimResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Claim an EVM collection as its creator: its owner() must be one of your verified wallets. Returns `{ chain, contract }`.
        api_response = api_instance.create_web3_creator_claim()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_creator_claim: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3CreatorClaimResponse**

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

# **create_web3_crosslist**
> CreateWeb3CrosslistResponse create_web3_crosslist()

Submit signed Seaport listings for several marketplaces at once (crossly, opensea); results per marketplace.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.create_web3_crosslist_response import CreateWeb3CrosslistResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Submit signed Seaport listings for several marketplaces at once (crossly, opensea); results per marketplace.
        api_response = api_instance.create_web3_crosslist()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_crosslist: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3CrosslistResponse**

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

# **create_web3_drop_remind**
> CreateWeb3DropRemindResponse create_web3_drop_remind(id)

Turn the 15-minute reminder for a drop on, or off if it already is. Returns `{ remindMe }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_drop_remind_response import CreateWeb3DropRemindResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Turn the 15-minute reminder for a drop on, or off if it already is. Returns `{ remindMe }`.
        api_response = api_instance.create_web3_drop_remind(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_drop_remind: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWeb3DropRemindResponse**

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

# **create_web3_favorite**
> CreateWeb3FavoriteResponse create_web3_favorite()

Favourite an NFT, or unfavourite it if it already is. Returns `{ favorited }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.create_web3_favorite_response import CreateWeb3FavoriteResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Favourite an NFT, or unfavourite it if it already is. Returns `{ favorited }`.
        api_response = api_instance.create_web3_favorite()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_favorite: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3FavoriteResponse**

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

# **create_web3_launch**
> ListWeb3LaunchesItem create_web3_launch()

Draft a launchpad collection: name, symbol, supply, mint price (wei of the chain’s native currency), schedule, optional holder phase and royalty. Crossly takes 5% of each mint inside the contract.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_launches_item import ListWeb3LaunchesItem
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Draft a launchpad collection: name, symbol, supply, mint price (wei of the chain’s native currency), schedule, optional holder phase and royalty. Crossly takes 5% of each mint inside the contract.
        api_response = api_instance.create_web3_launch()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_launch: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3LaunchesItem**

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

# **create_web3_launch_airdrop**
> CreateWeb3LaunchAirdropResponse create_web3_launch_airdrop(id)

Plan an airdrop (one free NFT each, up to 500) to `addresses` and/or the holders of `holdersOf`. Returns the transactions for the owner wallet; no payment moves.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_launch_airdrop_response import CreateWeb3LaunchAirdropResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Plan an airdrop (one free NFT each, up to 500) to `addresses` and/or the holders of `holdersOf`. Returns the transactions for the owner wallet; no payment moves.
        api_response = api_instance.create_web3_launch_airdrop(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_launch_airdrop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWeb3LaunchAirdropResponse**

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

# **create_web3_launch_art**
> CreateWeb3LaunchArtResponse create_web3_launch_art(id)

Append per-token art (image URL, name, traits), up to the supply, before the reveal. Returns `{ count }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_launch_art_response import CreateWeb3LaunchArtResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Append per-token art (image URL, name, traits), up to the supply, before the reveal. Returns `{ count }`.
        api_response = api_instance.create_web3_launch_art(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_launch_art: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWeb3LaunchArtResponse**

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

# **create_web3_launch_confirm_deploy**
> ListWeb3LaunchesItem create_web3_launch_confirm_deploy(id)

Confirm a sent deploy transaction: the contract must be the Crossly launch contract with this draft’s settings; it then goes live.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_launches_item import ListWeb3LaunchesItem
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Confirm a sent deploy transaction: the contract must be the Crossly launch contract with this draft’s settings; it then goes live.
        api_response = api_instance.create_web3_launch_confirm_deploy(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_launch_confirm_deploy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListWeb3LaunchesItem**

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

# **create_web3_launch_follow_creator**
> CreateWeb3LaunchFollowCreatorResponse create_web3_launch_follow_creator(id)

Follow the creator of a launch: their launches are announced to you, and again when each opens. Returns `{ following }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_launch_follow_creator_response import CreateWeb3LaunchFollowCreatorResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Follow the creator of a launch: their launches are announced to you, and again when each opens. Returns `{ following }`.
        api_response = api_instance.create_web3_launch_follow_creator(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_launch_follow_creator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWeb3LaunchFollowCreatorResponse**

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

# **create_web3_launch_reveal**
> CreateWeb3LaunchRevealResponse create_web3_launch_reveal(id)

Reveal the art: one random offset maps every token to its asset for good. Returns `{ revealedAt }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.create_web3_launch_reveal_response import CreateWeb3LaunchRevealResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Reveal the art: one random offset maps every token to its asset for good. Returns `{ revealedAt }`.
        api_response = api_instance.create_web3_launch_reveal(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_launch_reveal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWeb3LaunchRevealResponse**

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

# **create_web3_order**
> CreateWeb3OrderResponse create_web3_order()

Place a signed Seaport 1.6 order (listing, offer or collection offer) in the Crossly book.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_order_response import CreateWeb3OrderResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Place a signed Seaport 1.6 order (listing, offer or collection offer) in the Crossly book.
        api_response = api_instance.create_web3_order()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_order: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3OrderResponse**

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

# **create_web3_order_cancel**
> OkResponse create_web3_order_cancel(chain, hash)

Take one of your orders out of the Crossly book.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.ok_response import OkResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    hash = "hash_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Take one of your orders out of the Crossly book.
        api_response = api_instance.create_web3_order_cancel(chain, hash)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_order_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **hash** | **str**|  |

### Return type

**OkResponse**

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

# **create_web3_order_fulfillment_batch**
> CreateWeb3OrderFulfillmentBatchResponse create_web3_order_fulfillment_batch()

Fulfilments for sweeping several listings in one Seaport transaction; unfillable ones are skipped with a reason.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_order_fulfillment_batch_response import CreateWeb3OrderFulfillmentBatchResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fulfilments for sweeping several listings in one Seaport transaction; unfillable ones are skipped with a reason.
        api_response = api_instance.create_web3_order_fulfillment_batch()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_order_fulfillment_batch: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3OrderFulfillmentBatchResponse**

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

# **create_web3_phygital**
> CreateWeb3PhygitalResponse create_web3_phygital()

Make an NFT you hold redeemable for one of your physical inventory items.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_phygital_response import CreateWeb3PhygitalResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Make an NFT you hold redeemable for one of your physical inventory items.
        api_response = api_instance.create_web3_phygital()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_phygital: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3PhygitalResponse**

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

# **create_web3_phygital_redeem**
> CreateWeb3PhygitalRedeemResponse create_web3_phygital_redeem(id)

Redeem a phygital you hold (checked on-chain) for its physical item, with a shipping address. Once per phygital.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.create_web3_phygital_redeem_response import CreateWeb3PhygitalRedeemResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Redeem a phygital you hold (checked on-chain) for its physical item, with a shipping address. Once per phygital.
        api_response = api_instance.create_web3_phygital_redeem(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_phygital_redeem: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWeb3PhygitalRedeemResponse**

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

# **create_web3_phygital_redemption_ship**
> OkResponse create_web3_phygital_redemption_ship(id)

Mark a redemption shipped with its carrier and tracking number; the redeemer is notified.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.ok_response import OkResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Mark a redemption shipped with its carrier and tracking number; the redeemer is notified.
        api_response = api_instance.create_web3_phygital_redemption_ship(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_phygital_redemption_ship: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**OkResponse**

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

# **create_web3_rarible_draft**
> CreateWeb3RaribleDraftResponse create_web3_rarible_draft()

Draft a Rarible V2 listing for an NFT in your linked wallet: the EIP-712 order to sign and whether Rarible's transfer proxy is approved.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_rarible_draft_response import CreateWeb3RaribleDraftResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Draft a Rarible V2 listing for an NFT in your linked wallet: the EIP-712 order to sign and whether Rarible's transfer proxy is approved.
        api_response = api_instance.create_web3_rarible_draft()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_rarible_draft: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3RaribleDraftResponse**

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

# **create_web3_rarible_listing**
> OrderHashResponse create_web3_rarible_listing()

Submit a signed Rarible V2 listing: the signature is verified, then the order is posted to Rarible and recorded.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.common.order_hash_response import OrderHashResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Submit a signed Rarible V2 listing: the signature is verified, then the order is posted to Rarible and recorded.
        api_response = api_instance.create_web3_rarible_listing()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_rarible_listing: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**OrderHashResponse**

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

# **create_web3_solana_list_tx**
> CreateWeb3SolanaListTxResponse create_web3_solana_list_tx(marketplace)

Build an unsigned listing transaction on the Crossly book, Tensor or Magic Eden for a Solana NFT in your linked wallet.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.create_web3_solana_list_tx_response import CreateWeb3SolanaListTxResponse
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
    api_instance = web3_api.Web3Api(api_client)
    marketplace = "crossly" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Build an unsigned listing transaction on the Crossly book, Tensor or Magic Eden for a Solana NFT in your linked wallet.
        api_response = api_instance.create_web3_solana_list_tx(marketplace)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_list_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace** | **str**|  |

### Return type

**CreateWeb3SolanaListTxResponse**

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

# **create_web3_solana_listing**
> OrderHashResponse create_web3_solana_listing(marketplace)

Record a Crossly-book, Tensor or Magic Eden listing your wallet sent (read back from the chain first).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.common.order_hash_response import OrderHashResponse
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
    api_instance = web3_api.Web3Api(api_client)
    marketplace = "crossly" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Record a Crossly-book, Tensor or Magic Eden listing your wallet sent (read back from the chain first).
        api_response = api_instance.create_web3_solana_listing(marketplace)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_listing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace** | **str**|  |

### Return type

**OrderHashResponse**

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

# **create_web3_solana_offer**
> OrderHashResponse create_web3_solana_offer()

Record a sent bid; it is recorded only once its trade state exists on chain.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.common.order_hash_response import OrderHashResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Record a sent bid; it is recorded only once its trade state exists on chain.
        api_response = api_instance.create_web3_solana_offer()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_offer: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**OrderHashResponse**

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

# **create_web3_solana_offer_accept_tx**
> CreateWeb3SolanaListTxResponse create_web3_solana_offer_accept_tx(hash)

Build the sale into a bid from your linked wallet that holds the NFT (sell + execute_sale, one transaction).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.create_web3_solana_list_tx_response import CreateWeb3SolanaListTxResponse
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
    api_instance = web3_api.Web3Api(api_client)
    hash = "hash_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Build the sale into a bid from your linked wallet that holds the NFT (sell + execute_sale, one transaction).
        api_response = api_instance.create_web3_solana_offer_accept_tx(hash)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_offer_accept_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**|  |

### Return type

**CreateWeb3SolanaListTxResponse**

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

# **create_web3_solana_offer_cancel_tx**
> CreateWeb3SolanaListTxResponse create_web3_solana_offer_cancel_tx(hash)

Build the cancel of your bid: the SOL your other bids do not need comes back.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.create_web3_solana_list_tx_response import CreateWeb3SolanaListTxResponse
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
    api_instance = web3_api.Web3Api(api_client)
    hash = "hash_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Build the cancel of your bid: the SOL your other bids do not need comes back.
        api_response = api_instance.create_web3_solana_offer_cancel_tx(hash)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_offer_cancel_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**|  |

### Return type

**CreateWeb3SolanaListTxResponse**

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

# **create_web3_solana_offer_confirm**
> CreateWeb3SolanaOfferConfirmResponse create_web3_solana_offer_confirm(hash)

Apply a sent accept or cancel once the chain shows the bid closed.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.create_web3_solana_offer_confirm_response import CreateWeb3SolanaOfferConfirmResponse
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
    api_instance = web3_api.Web3Api(api_client)
    hash = "hash_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Apply a sent accept or cancel once the chain shows the bid closed.
        api_response = api_instance.create_web3_solana_offer_confirm(hash)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_offer_confirm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**|  |

### Return type

**CreateWeb3SolanaOfferConfirmResponse**

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

# **create_web3_solana_offer_tx**
> CreateWeb3SolanaOfferTxResponse create_web3_solana_offer_tx()

Build a bid on a Solana NFT on Crossly's book for your linked wallet to sign; the SOL goes into your Auction House escrow.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_solana_offer_tx_response import CreateWeb3SolanaOfferTxResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Build a bid on a Solana NFT on Crossly's book for your linked wallet to sign; the SOL goes into your Auction House escrow.
        api_response = api_instance.create_web3_solana_offer_tx()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_offer_tx: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3SolanaOfferTxResponse**

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

# **create_web3_solana_order_buy_tx**
> CreateWeb3SolanaOrderBuyTxResponse create_web3_solana_order_buy_tx(hash)

Build the unsigned transaction that buys a Solana listing (price capped at the listed price).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_solana_order_buy_tx_response import CreateWeb3SolanaOrderBuyTxResponse
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
    api_instance = web3_api.Web3Api(api_client)
    hash = "hash_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Build the unsigned transaction that buys a Solana listing (price capped at the listed price).
        api_response = api_instance.create_web3_solana_order_buy_tx(hash)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_order_buy_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**|  |

### Return type

**CreateWeb3SolanaOrderBuyTxResponse**

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

# **create_web3_solana_order_confirm**
> CreateWeb3SolanaOfferConfirmResponse create_web3_solana_order_confirm(hash)

Apply a sent Solana buy or delist to the book (the transaction is read back from the chain).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.create_web3_solana_offer_confirm_response import CreateWeb3SolanaOfferConfirmResponse
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
    api_instance = web3_api.Web3Api(api_client)
    hash = "hash_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Apply a sent Solana buy or delist to the book (the transaction is read back from the chain).
        api_response = api_instance.create_web3_solana_order_confirm(hash)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_order_confirm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**|  |

### Return type

**CreateWeb3SolanaOfferConfirmResponse**

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

# **create_web3_solana_order_delist_tx**
> CreateWeb3SolanaListTxResponse create_web3_solana_order_delist_tx(hash)

Build the unsigned transaction that takes your Solana listing down.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.create_web3_solana_list_tx_response import CreateWeb3SolanaListTxResponse
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
    api_instance = web3_api.Web3Api(api_client)
    hash = "hash_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Build the unsigned transaction that takes your Solana listing down.
        api_response = api_instance.create_web3_solana_order_delist_tx(hash)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_order_delist_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**|  |

### Return type

**CreateWeb3SolanaListTxResponse**

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

# **create_web3_solana_tensor_bid_accept_tx**
> CreateWeb3SolanaTensorBidPlaceTxResponse create_web3_solana_tensor_bid_accept_tx()

Build the transaction that sells your NFT into a Tensor bid, never below `minLamports`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_solana_tensor_bid_place_tx_response import CreateWeb3SolanaTensorBidPlaceTxResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Build the transaction that sells your NFT into a Tensor bid, never below `minLamports`.
        api_response = api_instance.create_web3_solana_tensor_bid_accept_tx()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_tensor_bid_accept_tx: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3SolanaTensorBidPlaceTxResponse**

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

# **create_web3_solana_tensor_bid_cancel_tx**
> CreateWeb3SolanaTensorBidPlaceTxResponse create_web3_solana_tensor_bid_cancel_tx()

Build the transaction that cancels your Tensor bid.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_solana_tensor_bid_place_tx_response import CreateWeb3SolanaTensorBidPlaceTxResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Build the transaction that cancels your Tensor bid.
        api_response = api_instance.create_web3_solana_tensor_bid_cancel_tx()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_tensor_bid_cancel_tx: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3SolanaTensorBidPlaceTxResponse**

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

# **create_web3_solana_tensor_bid_place_tx**
> CreateWeb3SolanaTensorBidPlaceTxResponse create_web3_solana_tensor_bid_place_tx()

Build a Tensor collection bid (or trait bid with `trait`) for your Solana wallet to sign. Price in lamports.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_solana_tensor_bid_place_tx_response import CreateWeb3SolanaTensorBidPlaceTxResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Build a Tensor collection bid (or trait bid with `trait`) for your Solana wallet to sign. Price in lamports.
        api_response = api_instance.create_web3_solana_tensor_bid_place_tx()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_solana_tensor_bid_place_tx: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3SolanaTensorBidPlaceTxResponse**

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

# **create_web3_token_refresh**
> CreateWeb3TokenRefreshResponse create_web3_token_refresh(chain, contract, token_id)

Re-read a token's metadata from the chain's provider (name, traits, image — a new image is copied to Crossly's CDN). Once per token per 10 minutes.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_token_refresh_response import CreateWeb3TokenRefreshResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 
    token_id = "tokenId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Re-read a token's metadata from the chain's provider (name, traits, image — a new image is copied to Crossly's CDN). Once per token per 10 minutes.
        api_response = api_instance.create_web3_token_refresh(chain, contract, token_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_token_refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |
 **token_id** | **str**|  |

### Return type

**CreateWeb3TokenRefreshResponse**

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

# **create_web3_transaction**
> CreateWeb3TransactionResponse create_web3_transaction()

Apply a Seaport transaction's fills and cancels to the Crossly book (read from the receipt).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_transaction_response import CreateWeb3TransactionResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Apply a Seaport transaction's fills and cancels to the Crossly book (read from the receipt).
        api_response = api_instance.create_web3_transaction()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_transaction: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3TransactionResponse**

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

# **create_web3_wallet_challenge**
> CreateWeb3WalletChallengeResponse create_web3_wallet_challenge()

Start linking a wallet: returns the message the wallet must sign.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.create_web3_wallet_challenge_response import CreateWeb3WalletChallengeResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Start linking a wallet: returns the message the wallet must sign.
        api_response = api_instance.create_web3_wallet_challenge()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_wallet_challenge: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3WalletChallengeResponse**

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

# **create_web3_wallet_sync**
> CreateWeb3WalletSyncResponse create_web3_wallet_sync(id)

Import a linked wallet's NFTs into inventory; archives ones that have left the wallet.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_wallet_sync_response import CreateWeb3WalletSyncResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Import a linked wallet's NFTs into inventory; archives ones that have left the wallet.
        api_response = api_instance.create_web3_wallet_sync(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_wallet_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWeb3WalletSyncResponse**

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

# **create_web3_wallet_verify**
> CreateWeb3WalletVerifyResponse create_web3_wallet_verify()

Finish linking a wallet with its signature over the challenge message.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_wallet_verify_response import CreateWeb3WalletVerifyResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Finish linking a wallet with its signature over the challenge message.
        api_response = api_instance.create_web3_wallet_verify()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->create_web3_wallet_verify: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**CreateWeb3WalletVerifyResponse**

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

# **delete_web3_alert**
> OkResponse delete_web3_alert(id)

Delete a price alert.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.ok_response import OkResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a price alert.
        api_response = api_instance.delete_web3_alert(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->delete_web3_alert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**OkResponse**

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

# **delete_web3_holder_perk**
> OkResponse delete_web3_holder_perk(id)

Remove a holder perk. Returns `{ ok }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.ok_response import OkResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove a holder perk. Returns `{ ok }`.
        api_response = api_instance.delete_web3_holder_perk(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->delete_web3_holder_perk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**OkResponse**

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

# **delete_web3_launch**
> OkResponse delete_web3_launch(id)

Delete a launch draft that never went live. Returns `{ ok }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.ok_response import OkResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a launch draft that never went live. Returns `{ ok }`.
        api_response = api_instance.delete_web3_launch(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->delete_web3_launch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**OkResponse**

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

# **delete_web3_launch_follow_creator**
> CreateWeb3LaunchFollowCreatorResponse delete_web3_launch_follow_creator(id)

Stop following the creator of a launch. Returns `{ following }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.create_web3_launch_follow_creator_response import CreateWeb3LaunchFollowCreatorResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Stop following the creator of a launch. Returns `{ following }`.
        api_response = api_instance.delete_web3_launch_follow_creator(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->delete_web3_launch_follow_creator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWeb3LaunchFollowCreatorResponse**

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

# **delete_web3_marketplace_key**
> delete_web3_marketplace_key(marketplace)

Remove your own key for a marketplace; Crossly's key is used again.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
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
    api_instance = web3_api.Web3Api(api_client)
    marketplace = "opensea" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove your own key for a marketplace; Crossly's key is used again.
        api_instance.delete_web3_marketplace_key(marketplace)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->delete_web3_marketplace_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace** | **str**|  |

### Return type

void (empty response body)

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content — the request succeeded and there is no body. |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_web3_wallet**
> OkResponse delete_web3_wallet(id)

Unlink a wallet. Its NFTs stay in inventory but stop syncing.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.ok_response import OkResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink a wallet. Its NFTs stay in inventory but stop syncing.
        api_response = api_instance.delete_web3_wallet(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->delete_web3_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**OkResponse**

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

# **get_web3_auction**
> GetWeb3AuctionResponse get_web3_auction(chain, contract, token_id)

A token's live (or latest) auction: reserve, end, top bid, bid count and the minimum next bid.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_auction_response import GetWeb3AuctionResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 
    token_id = "tokenId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A token's live (or latest) auction: reserve, end, top bid, bid count and the minimum next bid.
        api_response = api_instance.get_web3_auction(chain, contract, token_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_auction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |
 **token_id** | **str**|  |

### Return type

**GetWeb3AuctionResponse**

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

# **get_web3_browse**
> GetWeb3BrowseResponse get_web3_browse()

The Web3 directory's categories and chains, with how many collections each holds.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_browse_response import GetWeb3BrowseResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The Web3 directory's categories and chains, with how many collections each holds.
        api_response = api_instance.get_web3_browse()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_browse: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWeb3BrowseResponse**

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

# **get_web3_collection**
> GetWeb3CollectionResponse get_web3_collection(chain, contract)

A collection: metadata and Crossly stats (floor, listed, volume, best collection offer).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_collection_response import GetWeb3CollectionResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A collection: metadata and Crossly stats (floor, listed, volume, best collection offer).
        api_response = api_instance.get_web3_collection(chain, contract)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |

### Return type

**GetWeb3CollectionResponse**

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

# **get_web3_collection_depth**
> GetWeb3CollectionDepthResponse get_web3_collection_depth(chain, contract)

A collection's Crossly order book by price level — asks cheapest first, bids dearest first, with running totals — and the floor of every trait value.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_collection_depth_response import GetWeb3CollectionDepthResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A collection's Crossly order book by price level — asks cheapest first, bids dearest first, with running totals — and the floor of every trait value.
        api_response = api_instance.get_web3_collection_depth(chain, contract)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_collection_depth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |

### Return type

**GetWeb3CollectionDepthResponse**

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

# **get_web3_collection_insight**
> GetWeb3CollectionInsightResponse get_web3_collection_insight(chain, contract)

On-chain insights for a collection: holders, trait counts across the whole collection, recent transfers and a 30-day activity series.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_collection_insight_response import GetWeb3CollectionInsightResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # On-chain insights for a collection: holders, trait counts across the whole collection, recent transfers and a 30-day activity series.
        api_response = api_instance.get_web3_collection_insight(chain, contract)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_collection_insight: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |

### Return type

**GetWeb3CollectionInsightResponse**

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

# **get_web3_collection_item**
> GetWeb3CollectionItemResponse get_web3_collection_item(chain, contract)

A collection's NFTs: filter by traits (repeat trait=Type:Value; OR within a type, AND across), search by name or token id, sort by id, rarity or Crossly price. Whole-collection once indexed.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_collection_item_response import GetWeb3CollectionItemResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A collection's NFTs: filter by traits (repeat trait=Type:Value; OR within a type, AND across), search by name or token id, sort by id, rarity or Crossly price. Whole-collection once indexed.
        api_response = api_instance.get_web3_collection_item(chain, contract)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_collection_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |

### Return type

**GetWeb3CollectionItemResponse**

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

# **get_web3_collection_trait**
> GetWeb3CollectionTraitResponse get_web3_collection_trait(chain, contract)

Every trait type and value in a collection, with how many tokens have each.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_collection_trait_response import GetWeb3CollectionTraitResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Every trait type and value in a collection, with how many tokens have each.
        api_response = api_instance.get_web3_collection_trait(chain, contract)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_collection_trait: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |

### Return type

**GetWeb3CollectionTraitResponse**

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

# **get_web3_collection_trait_token**
> GetWeb3CollectionTraitTokenResponse get_web3_collection_trait_token(chain, contract)

Token ids in a collection with one trait — what a trait offer commits to.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_collection_trait_token_response import GetWeb3CollectionTraitTokenResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Token ids in a collection with one trait — what a trait offer commits to.
        api_response = api_instance.get_web3_collection_trait_token(chain, contract)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_collection_trait_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |

### Return type

**GetWeb3CollectionTraitTokenResponse**

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

# **get_web3_collector**
> GetWeb3CollectorResponse get_web3_collector()

Your collector perks: how many different NFTs you bought through Crossly, your Collector pin tier, relist rewards paid, and each NFT you still hold with the Bought on Crossly mark.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_collector_response import GetWeb3CollectorResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your collector perks: how many different NFTs you bought through Crossly, your Collector pin tier, relist rewards paid, and each NFT you still hold with the Bought on Crossly mark.
        api_response = api_instance.get_web3_collector()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_collector: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWeb3CollectorResponse**

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

# **get_web3_creator**
> GetWeb3CreatorResponse get_web3_creator(chain, contract)

A collection’s creator dashboard: sales by marketplace and day, estimated royalties, holders, and for a launch the mint revenue and what is waiting to be withdrawn (wei of the chain’s native currency).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_creator_response import GetWeb3CreatorResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A collection’s creator dashboard: sales by marketplace and day, estimated royalties, holders, and for a launch the mint revenue and what is waiting to be withdrawn (wei of the chain’s native currency).
        api_response = api_instance.get_web3_creator(chain, contract)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_creator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |

### Return type

**GetWeb3CreatorResponse**

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

# **get_web3_crosslist_quote**
> GetWeb3CrosslistQuoteResponse get_web3_crosslist_quote()

Each marketplace's terms for listing a token: Crossly fee, OpenSea required fees and zone, Tensor availability.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_crosslist_quote_response import GetWeb3CrosslistQuoteResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Each marketplace's terms for listing a token: Crossly fee, OpenSea required fees and zone, Tensor availability.
        api_response = api_instance.get_web3_crosslist_quote()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_crosslist_quote: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWeb3CrosslistQuoteResponse**

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

# **get_web3_featured**
> GetWeb3FeaturedResponse get_web3_featured()

The NFT home's featured collections: chosen by Crossly, else the hottest.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_featured_response import GetWeb3FeaturedResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The NFT home's featured collections: chosen by Crossly, else the hottest.
        api_response = api_instance.get_web3_featured()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_featured: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWeb3FeaturedResponse**

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

# **get_web3_inventory**
> GetWeb3InventoryResponse get_web3_inventory(item_id)

The NFT behind an inventory item: its token, wallet, and open listings on every marketplace (null if it is not an NFT).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_inventory_response import GetWeb3InventoryResponse
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
    api_instance = web3_api.Web3Api(api_client)
    item_id = "itemId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The NFT behind an inventory item: its token, wallet, and open listings on every marketplace (null if it is not an NFT).
        api_response = api_instance.get_web3_inventory(item_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_inventory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |

### Return type

**GetWeb3InventoryResponse**

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

# **get_web3_launch_allowlist_root_tx**
> GetWeb3LaunchAllowlistRootTxResponse get_web3_launch_allowlist_root_tx(id)

The setAllowlistRoot transaction for the allowlist Crossly holds (EVM, live): `{ chain, from, to, data }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_launch_allowlist_root_tx_response import GetWeb3LaunchAllowlistRootTxResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The setAllowlistRoot transaction for the allowlist Crossly holds (EVM, live): `{ chain, from, to, data }`.
        api_response = api_instance.get_web3_launch_allowlist_root_tx(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_launch_allowlist_root_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetWeb3LaunchAllowlistRootTxResponse**

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

# **get_web3_launch_deploy_tx**
> GetWeb3LaunchDeployTxResponse get_web3_launch_deploy_tx(id)

The contract-creation transaction for the draft: send it from the owner wallet, then confirm it. Returns `{ chain, from, data }`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_launch_deploy_tx_response import GetWeb3LaunchDeployTxResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The contract-creation transaction for the draft: send it from the owner wallet, then confirm it. Returns `{ chain, from, data }`.
        api_response = api_instance.get_web3_launch_deploy_tx(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_launch_deploy_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetWeb3LaunchDeployTxResponse**

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

# **get_web3_launch_tool**
> GetWeb3LaunchToolResponse get_web3_launch_tool(id)

A launch’s creator tools: allowlist size and root (and whether the contract has it yet), uploaded art and reveal, supply minted.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_launch_tool_response import GetWeb3LaunchToolResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A launch’s creator tools: allowlist size and root (and whether the contract has it yet), uploaded art and reveal, supply minted.
        api_response = api_instance.get_web3_launch_tool(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_launch_tool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetWeb3LaunchToolResponse**

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

# **get_web3_order_fulfillment**
> GetWeb3OrderFulfillmentResponse get_web3_order_fulfillment(chain, hash)

The signed order a taker passes to Seaport, after re-checking it can still fill.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_order_fulfillment_response import GetWeb3OrderFulfillmentResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    hash = "hash_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The signed order a taker passes to Seaport, after re-checking it can still fill.
        api_response = api_instance.get_web3_order_fulfillment(chain, hash)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_order_fulfillment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **hash** | **str**|  |

### Return type

**GetWeb3OrderFulfillmentResponse**

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

# **get_web3_phygital**
> GetWeb3PhygitalResponse get_web3_phygital(chain, contract, token_id)

A token's phygital: the physical item it can be redeemed for, and whether it has been.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_phygital_response import GetWeb3PhygitalResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 
    token_id = "tokenId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A token's phygital: the physical item it can be redeemed for, and whether it has been.
        api_response = api_instance.get_web3_phygital(chain, contract, token_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_phygital: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |
 **token_id** | **str**|  |

### Return type

**GetWeb3PhygitalResponse**

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

# **get_web3_phygital2**
> GetWeb3Phygital2Response get_web3_phygital2()

Phygitals you linked (with each redemption and its shipping address) and ones you redeemed.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_phygital2_response import GetWeb3Phygital2Response
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Phygitals you linked (with each redemption and its shipping address) and ones you redeemed.
        api_response = api_instance.get_web3_phygital2()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_phygital2: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWeb3Phygital2Response**

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

# **get_web3_portfolio**
> GetWeb3PortfolioResponse get_web3_portfolio()

Your NFTs with value (Crossly floor, else recent sales) and cost (what a linked wallet paid), realised sales, and USD totals at each day’s coin price.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_portfolio_response import GetWeb3PortfolioResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your NFTs with value (Crossly floor, else recent sales) and cost (what a linked wallet paid), realised sales, and USD totals at each day’s coin price.
        api_response = api_instance.get_web3_portfolio()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_portfolio: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWeb3PortfolioResponse**

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

# **get_web3_portfolio_tax**
> GetWeb3PortfolioTaxResponse get_web3_portfolio_tax()

One calendar year of NFT disposals from your linked wallets as CSV text: acquired, sold, proceeds, cost basis, gain (coin and USD).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_portfolio_tax_response import GetWeb3PortfolioTaxResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # One calendar year of NFT disposals from your linked wallets as CSV text: acquired, sold, proceeds, cost basis, gain (coin and USD).
        api_response = api_instance.get_web3_portfolio_tax()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_portfolio_tax: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWeb3PortfolioTaxResponse**

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

# **get_web3_profile**
> GetWeb3ProfileResponse get_web3_profile(address)

A wallet's public profile: NFTs held, open Crossly listings, and activity.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_profile_response import GetWeb3ProfileResponse
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
    api_instance = web3_api.Web3Api(api_client)
    address = "address_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A wallet's public profile: NFTs held, open Crossly listings, and activity.
        api_response = api_instance.get_web3_profile(address)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  |

### Return type

**GetWeb3ProfileResponse**

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

# **get_web3_resolve**
> GetWeb3ResolveResponse get_web3_resolve(chain, slug)

A collection's chain and contract from its readable URL slug (e.g. eth / boredapeyachtclub).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_resolve_response import GetWeb3ResolveResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    slug = "slug_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A collection's chain and contract from its readable URL slug (e.g. eth / boredapeyachtclub).
        api_response = api_instance.get_web3_resolve(chain, slug)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_resolve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **slug** | **str**|  |

### Return type

**GetWeb3ResolveResponse**

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

# **get_web3_solana_collection_tensor_bid**
> GetWeb3SolanaCollectionTensorBidResponse get_web3_solana_collection_tensor_bid(collection)

A Solana collection’s Tensor bids (collection-wide and by trait), best first; price in lamports. Needs your Tensor key.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.get_web3_solana_collection_tensor_bid_response import GetWeb3SolanaCollectionTensorBidResponse
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
    api_instance = web3_api.Web3Api(api_client)
    collection = "collection_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # A Solana collection’s Tensor bids (collection-wide and by trait), best first; price in lamports. Needs your Tensor key.
        api_response = api_instance.get_web3_solana_collection_tensor_bid(collection)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_solana_collection_tensor_bid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**|  |

### Return type

**GetWeb3SolanaCollectionTensorBidResponse**

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

# **get_web3_token**
> GetWeb3TokenResponse get_web3_token(chain, contract, token_id)

One NFT: metadata, traits, owner, open listings and offers, activity.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.get_web3_token_response import GetWeb3TokenResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 
    token_id = "tokenId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One NFT: metadata, traits, owner, open listings and offers, activity.
        api_response = api_instance.get_web3_token(chain, contract, token_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->get_web3_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |
 **token_id** | **str**|  |

### Return type

**GetWeb3TokenResponse**

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

# **list_web3_activity**
> ListWeb3ActivityResponse list_web3_activity()

Listings, offers, sales and cancels in the Crossly book, newest first.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_activity_response import ListWeb3ActivityResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Listings, offers, sales and cancels in the Crossly book, newest first.
        api_response = api_instance.list_web3_activity()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_activity: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3ActivityResponse**

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

# **list_web3_alerts**
> ListWeb3AlertsResponse list_web3_alerts()

Your NFT price alerts, with the cheapest open Crossly listing each one covers now.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_alerts_response import ListWeb3AlertsResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your NFT price alerts, with the cheapest open Crossly listing each one covers now.
        api_response = api_instance.list_web3_alerts()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_alerts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3AlertsResponse**

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

# **list_web3_approvals**
> ListWeb3ApprovalsResponse list_web3_approvals()

Your collections the OpenSea conduit is approved to move, per linked wallet.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_approvals_response import ListWeb3ApprovalsResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your collections the OpenSea conduit is approved to move, per linked wallet.
        api_response = api_instance.list_web3_approvals()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_approvals: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3ApprovalsResponse**

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

# **list_web3_auctions**
> ListWeb3AuctionsResponse list_web3_auctions()

Live English auctions on the Crossly book, ending soonest first, each with its top bid and the least the next bid can be.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_auctions_response import ListWeb3AuctionsResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Live English auctions on the Crossly book, ending soonest first, each with its top bid and the least the next bid can be.
        api_response = api_instance.list_web3_auctions()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_auctions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3AuctionsResponse**

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

# **list_web3_browse_collections**
> ListWeb3BrowseCollectionsResponse list_web3_browse_collections()

Browse NFT collections by chain, category and name; sort hot (Crossly sales, listings, favourites), new, volume, floor or name.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_browse_collections_response import ListWeb3BrowseCollectionsResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Browse NFT collections by chain, category and name; sort hot (Crossly sales, listings, favourites), new, volume, floor or name.
        api_response = api_instance.list_web3_browse_collections()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_browse_collections: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3BrowseCollectionsResponse**

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

# **list_web3_browse_tokens**
> ListWeb3BrowseTokensResponse list_web3_browse_tokens()

Hot NFTs: what is for sale on Crossly first, then tokens from the hottest collections.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_browse_tokens_response import ListWeb3BrowseTokensResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Hot NFTs: what is for sale on Crossly first, then tokens from the hottest collections.
        api_response = api_instance.list_web3_browse_tokens()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_browse_tokens: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3BrowseTokensResponse**

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

# **list_web3_bundles**
> ListWeb3BundlesResponse list_web3_bundles()

Open bundle listings (2–30 NFTs for one price), newest first, by chain or by a contract any item is from.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_bundles_response import ListWeb3BundlesResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Open bundle listings (2–30 NFTs for one price), newest first, by chain or by a contract any item is from.
        api_response = api_instance.list_web3_bundles()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_bundles: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3BundlesResponse**

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

# **list_web3_collection_history**
> ListWeb3CollectionHistoryResponse list_web3_collection_history(chain, contract)

Daily floor, sales, volume, holders and listed count for a collection, oldest first (up to 365 days).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_collection_history_response import ListWeb3CollectionHistoryResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "chain_example" # str | 
    contract = "contract_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Daily floor, sales, volume, holders and listed count for a collection, oldest first (up to 365 days).
        api_response = api_instance.list_web3_collection_history(chain, contract)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_collection_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  |
 **contract** | **str**|  |

### Return type

**ListWeb3CollectionHistoryResponse**

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

# **list_web3_collections**
> ListWeb3CollectionsResponse list_web3_collections()

Collections ranked by 30-day Crossly volume, with floor and listed count.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_collections_response import ListWeb3CollectionsResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Collections ranked by 30-day Crossly volume, with floor and listed count.
        api_response = api_instance.list_web3_collections()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_collections: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3CollectionsResponse**

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

# **list_web3_creator_collections**
> ListWeb3CreatorCollectionsResponse list_web3_creator_collections()

Collections you are the creator of: your launches, and contracts you claimed by owning them.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_creator_collections_response import ListWeb3CreatorCollectionsResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Collections you are the creator of: your launches, and contracts you claimed by owning them.
        api_response = api_instance.list_web3_creator_collections()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_creator_collections: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3CreatorCollectionsResponse**

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

# **list_web3_drops**
> ListWeb3DropsResponse list_web3_drops()

Upcoming and live NFT drops (curated mints on the creator's own page), soonest first, with whether you asked to be reminded.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_drops_response import ListWeb3DropsResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Upcoming and live NFT drops (curated mints on the creator's own page), soonest first, with whether you asked to be reminded.
        api_response = api_instance.list_web3_drops()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_drops: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3DropsResponse**

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

# **list_web3_holder_perks**
> ListWeb3HolderPerksResponse list_web3_holder_perks()

Your holder perks: percent off your Crossly shop for holders of an NFT collection, best first.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_holder_perks_response import ListWeb3HolderPerksResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your holder perks: percent off your Crossly shop for holders of an NFT collection, best first.
        api_response = api_instance.list_web3_holder_perks()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_holder_perks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3HolderPerksResponse**

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

# **list_web3_launches**
> ListWeb3LaunchesResponse list_web3_launches()

Your launchpad collections (drafts and live), newest first, with minted count and phase.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_launches_response import ListWeb3LaunchesResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your launchpad collections (drafts and live), newest first, with minted count and phase.
        api_response = api_instance.list_web3_launches()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_launches: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3LaunchesResponse**

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

# **list_web3_listings**
> ListWeb3ListingsResponse list_web3_listings()

Open NFT listings in the Crossly book — the cheapest per token.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_listings_response import ListWeb3ListingsResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Open NFT listings in the Crossly book — the cheapest per token.
        api_response = api_instance.list_web3_listings()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_listings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3ListingsResponse**

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

# **list_web3_marketplace_keys**
> ListWeb3MarketplaceKeysResponse list_web3_marketplace_keys()

Your own marketplace API keys (last four characters only) and whether Crossly's key covers each marketplace.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_marketplace_keys_response import ListWeb3MarketplaceKeysResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your own marketplace API keys (last four characters only) and whether Crossly's key covers each marketplace.
        api_response = api_instance.list_web3_marketplace_keys()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_marketplace_keys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3MarketplaceKeysResponse**

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

# **list_web3_nfts**
> ListWeb3NftsResponse list_web3_nfts()

List the NFTs in your inventory, imported from your linked wallets.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_nfts_response import ListWeb3NftsResponse
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
    api_instance = web3_api.Web3Api(api_client)
    chain = "ethereum" # str |  (optional)
    wallet_id = "walletId_example" # str |  (optional)
    page = 1 # int |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the NFTs in your inventory, imported from your linked wallets.
        api_response = api_instance.list_web3_nfts(chain=chain, wallet_id=wallet_id, page=page, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_nfts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**|  | [optional]
 **wallet_id** | **str**|  | [optional]
 **page** | **int**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

**ListWeb3NftsResponse**

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

# **list_web3_orders**
> ListWeb3OrdersResponse list_web3_orders()

Your orders in the Crossly book (listings and offers), any status.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_orders_response import ListWeb3OrdersResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your orders in the Crossly book (listings and offers), any status.
        api_response = api_instance.list_web3_orders()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_orders: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3OrdersResponse**

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

# **list_web3_purchases**
> ListWeb3PurchasesResponse list_web3_purchases()

NFTs your linked wallets bought — on Crossly or any marketplace the chain feed saw — newest first, with price and whether you still hold each.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_purchases_response import ListWeb3PurchasesResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # NFTs your linked wallets bought — on Crossly or any marketplace the chain feed saw — newest first, with price and whether you still hold each.
        api_response = api_instance.list_web3_purchases()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_purchases: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3PurchasesResponse**

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

# **list_web3_rankings**
> ListWeb3RankingsResponse list_web3_rankings()

Collections by sales volume over 24h, 7d or 30d, in one coin: the ETH chains together, or Polygon / Solana on their own.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_rankings_response import ListWeb3RankingsResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Collections by sales volume over 24h, 7d or 30d, in one coin: the ETH chains together, or Polygon / Solana on their own.
        api_response = api_instance.list_web3_rankings()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_rankings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3RankingsResponse**

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

# **list_web3_reserved**
> ListWeb3BundlesResponse list_web3_reserved()

Private listings reserved for one of your linked wallets — only you can see or buy them.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_bundles_response import ListWeb3BundlesResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Private listings reserved for one of your linked wallets — only you can see or buy them.
        api_response = api_instance.list_web3_reserved()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_reserved: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3BundlesResponse**

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

# **list_web3_sales**
> ListWeb3SalesResponse list_web3_sales()

The latest NFT sales across the directory, from the chain (Seaport and Blur) and the Crossly book, newest first; page with `before`.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_sales_response import ListWeb3SalesResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The latest NFT sales across the directory, from the chain (Seaport and Blur) and the Crossly book, newest first; page with `before`.
        api_response = api_instance.list_web3_sales()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_sales: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3SalesResponse**

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

# **list_web3_search**
> ListWeb3SearchResponse list_web3_search()

Find collections by contract address (every chain) or by name.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_search_response import ListWeb3SearchResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find collections by contract address (every chain) or by name.
        api_response = api_instance.list_web3_search()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_search: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3SearchResponse**

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

# **list_web3_search_tokens**
> ListWeb3SearchTokensResponse list_web3_search_tokens()

Find tokens by collection name and number: 'pudgy 42', 'Bored Ape #1234'.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_search_tokens_response import ListWeb3SearchTokensResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find tokens by collection name and number: 'pudgy 42', 'Bored Ape #1234'.
        api_response = api_instance.list_web3_search_tokens()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_search_tokens: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3SearchTokensResponse**

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

# **list_web3_wallets**
> ListWeb3WalletsResponse list_web3_wallets()

List your verified, linked wallets (EVM and Solana).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_wallets_response import ListWeb3WalletsResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List your verified, linked wallets (EVM and Solana).
        api_response = api_instance.list_web3_wallets()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_wallets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3WalletsResponse**

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

# **list_web3_watchlist**
> ListWeb3WatchlistResponse list_web3_watchlist()

Your favourited NFTs, with the cheapest open Crossly listing and the last sale of each.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_watchlist_response import ListWeb3WatchlistResponse
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Your favourited NFTs, with the cheapest open Crossly listing and the last sale of each.
        api_response = api_instance.list_web3_watchlist()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->list_web3_watchlist: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3WatchlistResponse**

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

# **update_web3_holder_perk**
> ListWeb3HolderPerksItem update_web3_holder_perk()

Set the percent off (100–5000 bps) holders of a collection get across your Crossly shop; one perk per collection.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.web3.list_web3_holder_perks_item import ListWeb3HolderPerksItem
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
    api_instance = web3_api.Web3Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Set the percent off (100–5000 bps) holders of a collection get across your Crossly shop; one perk per collection.
        api_response = api_instance.update_web3_holder_perk()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->update_web3_holder_perk: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWeb3HolderPerksItem**

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

# **update_web3_launch_allowlist**
> UpdateWeb3LaunchAllowlistResponse update_web3_launch_allowlist(id)

Replace the early-phase allowlist (up to 10,000 wallets). EVM live launches get back `rootTx`, the setAllowlistRoot transaction for the owner wallet.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.update_web3_launch_allowlist_response import UpdateWeb3LaunchAllowlistResponse
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
    api_instance = web3_api.Web3Api(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Replace the early-phase allowlist (up to 10,000 wallets). EVM live launches get back `rootTx`, the setAllowlistRoot transaction for the owner wallet.
        api_response = api_instance.update_web3_launch_allowlist(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->update_web3_launch_allowlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**UpdateWeb3LaunchAllowlistResponse**

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

# **update_web3_marketplace_key**
> ListWeb3MarketplaceKeysItem update_web3_marketplace_key(marketplace)

Save your own API key for a marketplace (checked against the marketplace first where it can be); stored encrypted.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import web3_api
from crossly.model.common.error import Error
from crossly.model.web3.list_web3_marketplace_keys_item import ListWeb3MarketplaceKeysItem
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
    api_instance = web3_api.Web3Api(api_client)
    marketplace = "opensea" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Save your own API key for a marketplace (checked against the marketplace first where it can be); stored encrypted.
        api_response = api_instance.update_web3_marketplace_key(marketplace)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling Web3Api->update_web3_marketplace_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace** | **str**|  |

### Return type

**ListWeb3MarketplaceKeysItem**

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

