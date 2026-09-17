# GetPlatformLimitResponseEbay


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** |  | 
**used** | **float** |  | 
**limit** | **float** |  | 
**remaining** | **float** |  | 
**tier_configured** | **bool** | False if the user hasn&#39;t picked a tier (we default to 250 but flag it so the UI can prompt). | 
**respect_quota** | **bool** |  | 
**period_start** | **str** |  | 
**per_overage_fee_usd** | **float** | Approximate cost if &#x60;used&#x60; overflows &#x60;limit&#x60; — informational. | 
**selling_cap** | [**GetPlatformLimitResponseEbaySellingCap**](GetPlatformLimitResponseEbaySellingCap.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


