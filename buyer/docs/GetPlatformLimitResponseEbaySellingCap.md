# GetPlatformLimitResponseEbaySellingCap

eBay-imposed monthly selling cap (quantity + $$) fetched from Trading API GetMyeBaySelling. These are HARD blocks — past them, `publishOffer` returns an error. Distinct from the free-tier `limit` (which is just a fee threshold). Null when seller has no caps (established accounts) or the Trading call failed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**fetched_at** | **str** | ISO timestamp this was fetched (used for cache freshness display). | 
**amount_limit** | **float, none_type** | Monthly $$ ceiling — null when seller has no $$ cap set. | [optional] 
**amount_used** | **float, none_type** |  | [optional] 
**quantity_limit** | **float, none_type** | Monthly item-count ceiling — null when seller has no qty cap. | [optional] 
**quantity_used** | **float, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


