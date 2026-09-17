# Pagination

Present only when the endpoint pages. Absent — not null — when it returns everything.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | 1-indexed page number. | 
**limit** | **int** | Rows per page. | 
**total** | **int** | Total matching rows, when the endpoint counts them. | [optional] 
**total_pages** | **int** | Derived from total and limit. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


