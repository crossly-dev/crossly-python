# GetConnectionHealthResponseLiveness


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_browser_push_ago** | **str** |  | 
**last_used_ago** | **str** |  | 
**auth_failure_streak** | **float** |  | 
**last_browser_push_at** | **str, none_type** | The clean \&quot;the browser pushed cookies\&quot; signal. | [optional] 
**last_synced_at** | **str, none_type** | Also stamped by the executor on any successful server-side call, so it is NOT evidence the extension is alive. Exposed for debugging only. | [optional] 
**last_used_at** | **str, none_type** | Last server-exec attempt, success or fail. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


