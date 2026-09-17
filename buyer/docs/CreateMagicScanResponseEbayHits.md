# CreateMagicScanResponseEbayHits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | 
**title** | **str** |  | 
**item_url** | **str** |  | 
**legacy_item_id** | **str, none_type** |  | [optional] 
**brand** | **str, none_type** |  | [optional] 
**price_cents** | **float, none_type** | Normalized cents. eBay returns string + currency on &#x60;price.value&#x60;. | [optional] 
**currency** | **str, none_type** |  | [optional] 
**condition** | **str, none_type** |  | [optional] 
**category_id** | **str, none_type** | Top-level category eBay assigned to the match (id + path). | [optional] 
**category_path** | **str, none_type** |  | [optional] 
**thumbnail_url** | **str, none_type** |  | [optional] 
**aspects** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Loosely-typed aspect bag — Brand, Color, Material, etc. when eBay inlines them. Always inspected defensively by the synthesizer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


