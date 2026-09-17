# V1List

The canonical collection envelope. The array is ALWAYS under `data`, never under the noun — so one accessor works for every list endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | The rows. | 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**meta** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Endpoint-specific extras that are NOT pagination — e.g. &#x60;pendingCents&#x60;, &#x60;basis&#x60;. Omitted when empty. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


