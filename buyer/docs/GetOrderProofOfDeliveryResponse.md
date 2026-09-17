# GetOrderProofOfDeliveryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | 
**platform** | **str** |  | 
**scans** | [**[GetOrderProofOfDeliveryResponseScans]**](GetOrderProofOfDeliveryResponseScans.md) |  | 
**gaps** | **[str]** | Why this document is weak, stated plainly so the seller isn&#39;t surprised  by the marketplace&#39;s response. | 
**platform_order_id** | **str, none_type** |  | [optional] 
**item_title** | **str, none_type** |  | [optional] 
**buyer_username** | **str, none_type** |  | [optional] 
**ship_to_postal_code** | **str, none_type** | The ZIP we shipped to, for comparison against the delivery scan. | [optional] 
**ship_to_city_state** | **str, none_type** |  | [optional] 
**carrier** | **str, none_type** |  | [optional] 
**tracking_number** | **str, none_type** |  | [optional] 
**tracking_url** | **str, none_type** |  | [optional] 
**shipped_at** | **str, none_type** |  | [optional] 
**delivered_at** | **str, none_type** |  | [optional] 
**delivery_location** | **str, none_type** |  | [optional] 
**signature** | **str, none_type** | Null means the carrier captured none — NOT that delivery is unproven. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


