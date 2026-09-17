# CreateBuyerLockonConfirmResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lockon_id** | **str** |  | 
**status** | **str** |  | 
**candidates** | [**[CreateBuyerLockonObserveResponseCandidates]**](CreateBuyerLockonObserveResponseCandidates.md) | Present when we could not settle it alone. Show them; a pinch on one is the cheapest, strongest disambiguation available. | 
**observation_count** | **float** |  | 
**vision_calls** | **float** |  | 
**vision_quota_exhausted** | **bool** |  | 
**verdict** | **str** |  | 
**alternates** | [**[GetBuyerAnywhereResponseAlternates]**](GetBuyerAnywhereResponseAlternates.md) |  | 
**shipping_unknown** | **bool** |  | 
**hud** | [**CreateBuyerIdentifyResponseHud**](CreateBuyerIdentifyResponseHud.md) |  | 
**identifier** | [**CreateBuyerIdentifyResponseIdentifier**](CreateBuyerIdentifyResponseIdentifier.md) |  | [optional] 
**crossly** | [**GetBuyerAnywhereResponseCrossly**](GetBuyerAnywhereResponseCrossly.md) |  | [optional] 
**offsite** | [**GetBuyerAnywhereResponseOffsite**](GetBuyerAnywhereResponseOffsite.md) |  | [optional] 
**saving_cents** | **float, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


