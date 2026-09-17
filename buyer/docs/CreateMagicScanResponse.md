# CreateMagicScanResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** |  | 
**top_hits** | [**[CreateMagicScanResponseTopHits]**](CreateMagicScanResponseTopHits.md) | Unified top-10-globally list, ranked by CLIP visual similarity to  the seller&#39;s source photo. Each hit carries its origin platform. | 
**ebay_hits** | [**[CreateMagicScanResponseEbayHits]**](CreateMagicScanResponseEbayHits.md) | Legacy compat — UI&#39;s existing render. ebayHits now &#x3D;&#x3D; visually-  validated eBay subset; otherMatches is re-grouped from topHits. | 
**other_matches** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**image_urls** | **[str]** | Every photo the seller uploaded for this scan, primary first. | 
**vision_aspects** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Vision-LLM aspects extracted across all photos. Populated only  when the seller has magic-list-vision-aspects enabled + a vision  provider configured. Empty otherwise. | 
**possible_duplicates** | [**[CreateMagicScanResponsePossibleDuplicates]**](CreateMagicScanResponsePossibleDuplicates.md) | The seller&#39;s OWN listings/inventory that this scan probably duplicates  (image + fuzzy-title self-dedup). Empty when nothing matched. Drives the  \&quot;you may already have this\&quot; prompt. | 
**cached** | **bool** |  | 
**ebay_match** | [**CreateMagicScanResponseEbayMatch**](CreateMagicScanResponseEbayMatch.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


