# ListSpatialPublicItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**public_slug** | **str** |  | 
**category_slug** | **str** |  | 
**item_count** | **float** | Unsold stock that lands in this room. The same predicate the room uses. | 
**for_sale_count** | **float** | How many of those a visitor could buy right now. | 
**preview_images** | **[str]** | Up to PREVIEW_IMAGES item images. Catalog art first, seller photo else. | 
**price_from_cents** | **float, none_type** | The cheapest and dearest thing for sale, in cents.  A BAND, deliberately, and never a quote: &#x60;listPublicSceneOffers&#x60; is the only authority on what a given object costs. Null when nothing is for sale — zero would read as free. | [optional] 
**price_to_cents** | **float, none_type** |  | [optional] 
**updated_at** | **str, none_type** | Last time the room itself changed. ISO, or null if the row has no date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


