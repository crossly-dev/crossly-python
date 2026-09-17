# GetOrderEvidenceResponseSeal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessment** | [**GetOrderEvidenceResponseSealAssessment**](GetOrderEvidenceResponseSealAssessment.md) |  | 
**has_dispatch** | **bool** |  | 
**has_arrival** | **bool** |  | 
**has_courier_photo** | **bool** | A courier photo exists, even if the seal was not legible in it. | 
**dispatch_searched_frames** | **float, none_type** | How many packing frames were searched to find the dispatch frame shot closest to the arrival angle. Null when the dispatch reading was simply the frame the recorder ended on.  Surfaced rather than kept internal: \&quot;the best of eighteen frames matched\&quot; is a weaker claim than \&quot;the frame we took matched\&quot;, and a reviewer has to be able to tell them apart. See frame-match.ts. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


