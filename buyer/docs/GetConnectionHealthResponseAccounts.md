# GetConnectionHealthResponseAccounts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_name** | **str** |  | 
**summary** | **str** | Plain-English \&quot;what is true\&quot; + \&quot;what to do\&quot;. Never empty. | 
**action** | **str** |  | 
**liveness** | [**GetConnectionHealthResponseLiveness**](GetConnectionHealthResponseLiveness.md) |  | 
**platform** | **str** |  | 
**state** | **str** |  | 
**severity** | **str** |  | 
**audience** | **str** |  | 
**notes** | **[str]** | Secondary observations that do not change the verdict but change the debugging. Always safe to show; never the only thing shown. | 
**account_id** | **str, none_type** |  | [optional] 
**account_slot** | **float, none_type** |  | [optional] 
**label** | **str, none_type** |  | [optional] 
**platform_username** | **str, none_type** |  | [optional] 
**browser** | [**GetConnectionHealthResponseBrowser**](GetConnectionHealthResponseBrowser.md) |  | [optional] 
**anchors** | [**GetConnectionHealthResponseAnchors**](GetConnectionHealthResponseAnchors.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


