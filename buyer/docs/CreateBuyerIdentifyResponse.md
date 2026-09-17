# CreateBuyerIdentifyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **str** |  | 
**confidence** | **float** |  | 
**vision_quota_exhausted** | **bool** | Surfaced rather than hidden: \&quot;we could not look harder\&quot; and \&quot;we looked and found nothing\&quot; are different answers, and a client that cannot tell them apart shows the wrong message on both. | 
**visual_matches** | [**[CreateBuyerIdentifyResponseVisualMatches]**](CreateBuyerIdentifyResponseVisualMatches.md) |  | 
**verdict** | **str** |  | 
**alternates** | [**[GetBuyerAnywhereResponseAlternates]**](GetBuyerAnywhereResponseAlternates.md) |  | 
**shipping_unknown** | **bool** |  | 
**hud** | [**CreateBuyerIdentifyResponseHud**](CreateBuyerIdentifyResponseHud.md) |  | 
**identifier** | [**CreateBuyerIdentifyResponseIdentifier**](CreateBuyerIdentifyResponseIdentifier.md) |  | [optional] 
**vision_label** | **str, none_type** |  | [optional] 
**crossly** | [**GetBuyerAnywhereResponseCrossly**](GetBuyerAnywhereResponseCrossly.md) |  | [optional] 
**offsite** | [**GetBuyerAnywhereResponseOffsite**](GetBuyerAnywhereResponseOffsite.md) |  | [optional] 
**saving_cents** | **float, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


