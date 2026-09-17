# GetTaxonomyCategoryAspectResponseAspects


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**required** | **bool** |  | 
**data_type** | **str** | &#39;STRING&#39; | &#39;NUMBER&#39; | &#39;DATE&#39; — eBay&#39;s dataType per aspect. | 
**has_enum_values** | **bool** | True when the aspect is selection-only (no free-text). | 
**cardinality** | **str** | Cardinality — SINGLE_VALUE / MULTIPLE_VALUES. | 
**enum_values** | **[str], none_type** |  | [optional] 
**max_length** | **float, none_type** | Helpful for client validation — max length when supplied. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


