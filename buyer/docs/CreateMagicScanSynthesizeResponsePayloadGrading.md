# CreateMagicScanSynthesizeResponsePayloadGrading

Third-party grading read off a slab label, when the item is one.    SEPARATE FROM `condition` and never derived from it. A grade is a claim  about what a grading company certified; inferring \"PSA 10\" from a coarse  condition would be inventing an authenticity claim. It is equally never  filled from our own vision estimate (`bulk_market_items.grade`), which  ships with an explicit \"not a professional grade\" disclaimer.    Feeds eBay's Professional Grader / Grade / Certification Number condition  descriptors (synthesize/condition-descriptors.ts) and, on platforms with  no grading field, the title.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grader_slug** | **str** |  | 
**grade** | **str** | As the grader writes it: &#39;10&#39;, &#39;9.8&#39;, &#39;MS-65&#39;. | 
**grade_key** | **str** | Derived. Never assign by hand — call &#x60;gradeKey()&#x60;. | 
**qualifier** | **str, none_type** |  | [optional] 
**seal_grade** | **str, none_type** | Second axis on a &#x60;dual&#x60; scale — WATA&#39;s seal grade. | [optional] 
**cert_number** | **str, none_type** |  | [optional] 
**verified_at** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


