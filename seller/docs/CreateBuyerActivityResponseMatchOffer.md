# CreateBuyerActivityResponseMatchOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**price_cents** | **float** |  | 
**url** | **str** |  | 
**condition** | **str, none_type** | Free-text on listings, an order-book grade (&#39;DS&#39;) on asks. Never null on asks; frequently null on listings, which is itself informative. | [optional] 
**title** | **str, none_type** |  | [optional] 
**image_url** | **str, none_type** |  | [optional] 
**slug** | **str, none_type** | The public slug, when this offer is a marketplace listing.  Present so Scout can buy it without parsing the URL it was given back. Null on an order-book ask, which is deliberate rather than an omission: an ask is a price in a book, not a thing with a checkout, and a Buy button on one would be a promise the market side cannot keep. | [optional] 
**available** | **float, none_type** | How many the seller has. Caps the quantity stepper honestly. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


