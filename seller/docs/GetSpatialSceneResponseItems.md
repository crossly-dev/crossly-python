# GetSpatialSceneResponseItems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**status** | **str** |  | 
**market_tagged** | **bool** | True when this row resolved to a catalog product. | 
**unit_id** | **str, none_type** |  | [optional] 
**image_url** | **str, none_type** |  | [optional] 
**thumb_url** | **str, none_type** | A small copy of &#x60;imageUrl&#x60;, when the catalog has one.    The room binds this for everything except the few items you are standing  in front of. A 600x600 original costs 1.83 MiB of VRAM; a 150x150 thumb  costs 0.11 MiB, and at more than a couple of metres they are the same  handful of pixels on screen. Null when the catalog never made one, which  the renderer treats as \&quot;use the original\&quot; rather than as \&quot;draw nothing\&quot;. | [optional] 
**size** | [**GetSpatialSceneResponseSize**](GetSpatialSceneResponseSize.md) |  | [optional] 
**cost_cents** | **float, none_type** | Cents the seller paid. Drives the &#x60;value&#x60; overlay and capital density. | [optional] 
**age_days** | **float, none_type** | Days since first listed anywhere. Drives the &#x60;aging&#x60; overlay. | [optional] 
**location** | **str, none_type** | Free-text or structured location, when the unit has one. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


