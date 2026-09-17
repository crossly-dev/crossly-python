# CreateListingCheckDuplicateResponseMatches


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggested** | **str** | What we&#39;d offer to do about this match. A suggestion for which button to  feature — never a decision. All three actions stay available. | 
**title** | **str** |  | 
**match_type** | **str** |  | 
**score** | **float** | 0–1 confidence. Image matches report 1; title matches the similarity. | 
**variation_group_id** | **str, none_type** | The variation group to ADD to, when the match already belongs to one.  Null means there is no group yet and choosing &#x60;variation&#x60; creates one from  the match plus the new listing. Without this the UI has to guess, and  guessing wrong means either a second group beside the first or a silent  no-op. | [optional] 
**listing_id** | **str, none_type** | The seller&#39;s existing listing this scan probably duplicates (null if the  match landed only on an inventory item with no listing row). | [optional] 
**inventory_item_id** | **str, none_type** | The inventory item behind that listing, when linked. Drives the  \&quot;View inventory\&quot; button. | [optional] 
**image_url** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


