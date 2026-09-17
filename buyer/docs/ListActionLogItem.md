# ListActionLogItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**status** | **str** |  | 
**source** | **str** |  | 
**action** | **str** |  | 
**category** | **str** |  | 
**correlation_id** | **str** |  | 
**user_id** | **str, none_type** |  | [optional] 
**platform** | **str, none_type** |  | [optional] 
**latency_ms** | **float, none_type** |  | [optional] 
**error_class** | **str, none_type** |  | [optional] 
**error_message** | **str, none_type** |  | [optional] 
**ip_address** | **str, none_type** |  | [optional] 
**user_agent** | **str, none_type** |  | [optional] 
**oauth_app_id** | **str, none_type** |  | [optional] 
**actor_user_id** | **str, none_type** |  | [optional] 
**finished_at** | **datetime, none_type** |  | [optional] 
**track** | **str, none_type** |  | [optional] 
**target_type** | **str, none_type** |  | [optional] 
**target_id** | **str, none_type** |  | [optional] 
**http_status** | **float, none_type** |  | [optional] 
**actor_email** | **str, none_type** | Resolved from actorUserId so the UI can say \&quot;Jane relisted this\&quot; rather than printing a UUID. Null for worker/system actions, which genuinely had no human actor. | [optional] 
**actor_display_name** | **str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


