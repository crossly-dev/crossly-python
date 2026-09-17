# GetBuyerAnywhereResponseAlternates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** |  | 
**host** | **str** | The retailer&#39;s hostname, e.g. &#x60;rei.com&#x60;. | 
**store_name** | **str** |  | 
**title** | **str** |  | 
**price_cents** | **float** |  | 
**currency** | **str** |  | 
**url** | **str** |  | 
**buyer_cashback_cents** | **float** | What the buyer gets back, in cents, if they buy through us.  Shown because a cashback figure the buyer cannot see is a figure they have no reason to believe. Derived from the store&#39;s rate, never stored per offer — rates change and a copied one goes stale silently. | 
**delivered_cents** | **float** | Item + shipping when known; item alone otherwise. See &#x60;shippingUnknown&#x60;. | 
**shipping_unknown** | **bool** |  | 
**shipping_cents** | **float, none_type** | Null &#x3D; UNKNOWN, never free. | [optional] 
**condition** | **str, none_type** |  | [optional] 
**image_url** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


