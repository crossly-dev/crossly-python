# ListSourcingDemandMineItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_value** | **str** |  | 
**lookers** | **float** | How many distinct shoppers looked, in the window. | 
**misses** | **float** | How many of those looks Crossly could not answer at all. | 
**relation** | **str** | &#39;in_stock&#39; — it is in their inventory. &#39;sold_before&#39; — they have sold one. | 
**median_retail_cents** | **float, none_type** | What the retailers were charging, median of what Scout saw. | [optional] 
**inventory_item_id** | **str, none_type** | Their own row, for the link. | [optional] 
**title** | **str, none_type** |  | [optional] 
**last_sold_cents** | **float, none_type** | What they got for it last time, when they have sold one. | [optional] 
**last_sold_at** | **datetime, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


