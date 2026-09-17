# CreateListingByIdResponseItems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_title** | **str** |  | 
**effective_images** | **[str]** |  | 
**effective_color** | **[str]** |  | 
**effective_tags** | **[str]** |  | 
**platform_listings** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | 
**id** | **str** |  | 
**user_id** | **str** |  | 
**status** | **str** |  | 
**color** | **[str]** |  | 
**tags** | **[str]** |  | 
**quantity** | **float** |  | 
**quantity_available** | **float** |  | 
**is_bundle** | **bool** |  | 
**automation_assigned_rule_ids** | **[str]** | Per-listing automation overrides. See migration 0098.     automationAssignedRuleIds  — force-include for these rules   automationBlockedRuleIds   — exempt from these rules   automationAssignedChainIds — force-include for these workflow chains   automationBlockedChainIds  — exempt from these workflow chains | 
**automation_blocked_rule_ids** | **[str]** |  | 
**automation_assigned_chain_ids** | **[str]** |  | 
**automation_blocked_chain_ids** | **[str]** |  | 
**floor_is_net** | **bool** | When true the floor is a TAKE-HOME target, converted to a per-platform  gross at reprice time. A gross floor is four different promises across  four platforms; this is the one number a seller actually cares about. | 
**source** | **str** | Mirrors inventory_items.source. &#39;manual&#39; for every seller-created  listing; external-stub.ts sets &#39;external_sale&#39; on the synthetic  listing it fabricates for a sale detected on a platform id Crossly  never listed — those rows have no real photos/description of their  own (everything is lifted from the platform&#39;s sale payload) and are  otherwise indistinguishable from a real listing in the UI. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**effective_price** | **str, none_type** |  | [optional] 
**effective_description** | **str, none_type** |  | [optional] 
**effective_brand** | **str, none_type** |  | [optional] 
**effective_condition** | **str, none_type** |  | [optional] 
**effective_size** | **str, none_type** |  | [optional] 
**effective_sku** | **str, none_type** |  | [optional] 
**inventory_item_id** | **str, none_type** |  | [optional] 
**name** | **str, none_type** |  | [optional] 
**title** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**description_html** | **str, none_type** |  | [optional] 
**price** | **str, none_type** |  | [optional] 
**images** | **[str], none_type** |  | [optional] 
**video_url** | **str, none_type** | Optional single product video (R2/CDN URL). Shown on the Crossly buyer page. | [optional] 
**condition** | **str, none_type** |  | [optional] 
**grade_key** | **str, none_type** | Third-party grading, when the item is slabbed. Migration 0277.    Separate from &#x60;condition&#x60; on purpose and never derived from it: a grade  is a claim about what a GRADING COMPANY certified, and inferring \&quot;PSA 10\&quot;  from a coarse condition would be a false authenticity claim. It is also  never filled from our own AI estimate (&#x60;bulk_market_items.grade&#x60;), which  carries an explicit \&quot;not a professional grade\&quot; disclaimer.    &#x60;gradeKey&#x60; is the canonical form from &#x60;gradeKey()&#x60; in  shared/constants/graders.ts; &#x60;grading&#x60; holds the full GradingInfo  including the cert number and whether a cert lookup verified it. | [optional] 
**grading** | [**ListListingsItemGrading**](ListListingsItemGrading.md) |  | [optional] 
**brand** | **str, none_type** |  | [optional] 
**size** | **str, none_type** |  | [optional] 
**material** | **str, none_type** | Migration 0179 — see the matching fields on inventory_items above. | [optional] 
**style** | **str, none_type** |  | [optional] 
**pattern** | **str, none_type** |  | [optional] 
**department** | **str, none_type** |  | [optional] 
**gender** | **str, none_type** |  | [optional] 
**item_type** | **str, none_type** |  | [optional] 
**size_system** | **str, none_type** |  | [optional] 
**sku** | **str, none_type** |  | [optional] 
**weight_lb** | **str, none_type** |  | [optional] 
**weight_oz** | **str, none_type** |  | [optional] 
**dimension_lin** | **str, none_type** |  | [optional] 
**dimension_win** | **str, none_type** |  | [optional] 
**dimension_hin** | **str, none_type** |  | [optional] 
**publish_at** | **datetime, none_type** | Scheduled go-live time. When set on a draft, the listing-scheduler  worker waits until this passes then dispatches the crosspost to  scheduledPlatforms and flips status from &#39;draft&#39; to &#39;active&#39;. | [optional] 
**scheduled_platforms** | **[str], none_type** | Which platforms to publish to when publishAt fires. JSON array of  platform ids. Null/empty &#x3D; scheduler skips (listing won&#39;t auto-  publish, even after publishAt — gives the seller an escape hatch). | [optional] 
**parent_listing_id** | **str, none_type** | Parent listing when this row is a CHILD in a listing chain. Null &#x3D;  standalone. What being a child means depends on the parent&#39;s  &#x60;groupKind&#x60; — see it. | [optional] 
**hs_code** | **str, none_type** | Harmonised System customs code — international shipping declarations. | [optional] 
**country_of_origin** | **str, none_type** | Customs country of origin. Distinct from the seller&#39;s location. | [optional] 
**price_floor_cents** | **float, none_type** | Never let a repricing rule go below this. On the ITEM because it is a  fact about the thing owned, not about any one rule — \&quot;this jacket never  goes below $45\&quot; should apply to every rule, and before this it was  expressible only as one rule per jacket. Listings inherit when null. | [optional] 
**delisted_at** | **datetime, none_type** |  | [optional] 
**sold_at** | **datetime, none_type** |  | [optional] 
**duplicate_of_listing_id** | **str, none_type** | Set when import&#39;s bin-packing (see _import-one.ts) created THIS  listing to hold a same-platform straggler it couldn&#39;t fit onto an  existing candidate listing for the same physical item — points at  the primary/first candidate. Purely informational: this listing  is a real, independently listable/delistable row, not a shadow.  Null for every ordinarily-created listing. | [optional] 
**client_draft_id** | **str, none_type** | UUID minted on a seller&#39;s machine for a draft written offline.    The idempotency key for desktop sync. The failure it guards is a POST  that succeeds server-side whose reply is lost — the client cannot tell  that from a failure, retries, and one item becomes two live listings  against one piece of stock. Unique per user (partial index, migration  0268); null for every listing that did not come from an offline draft. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


