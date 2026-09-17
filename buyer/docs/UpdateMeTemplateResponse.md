# UpdateMeTemplateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**scope** | **str** |  | 
**name** | **str** |  | 
**is_default** | **bool** |  | 
**sort_order** | **float** | Snippet ordering — kept for scope&#x3D;&#39;description&#39; back-compat with  the description_templates.sort_order behavior. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**notes** | **str, none_type** | Optional short blurb the seller can attach to remember what it&#39;s for. | [optional] 
**description** | **str, none_type** | Primary description body. For scope&#x3D;&#39;description&#39; this is the  snippet body; for scope&#x3D;&#39;listing&#39; this is the default description  the seller wants pre-filled. | [optional] 
**description_variants** | **[str], none_type** | A/B variants for description. Populated for scope&#x3D;&#39;listing&#39;;  typically null for scope&#x3D;&#39;description&#39; (a snippet is one string). | [optional] 
**title** | **str, none_type** |  | [optional] 
**title_variants** | **[str], none_type** |  | [optional] 
**brand** | **str, none_type** |  | [optional] 
**condition** | **str, none_type** | Master condition enum — new/like_new/good/fair/poor. | [optional] 
**color** | **str, none_type** |  | [optional] 
**material** | **str, none_type** |  | [optional] 
**size** | **str, none_type** |  | [optional] 
**size_system** | **str, none_type** |  | [optional] 
**weight_oz** | **float, none_type** |  | [optional] 
**department** | **str, none_type** |  | [optional] 
**gender** | **str, none_type** |  | [optional] 
**style** | **str, none_type** |  | [optional] 
**pattern** | **str, none_type** |  | [optional] 
**item_type** | **str, none_type** |  | [optional] 
**tags** | **[str], none_type** |  | [optional] 
**default_for_category** | **str, none_type** | When set, form&#39;s category picker prompts \&quot;Use your default for  this category\&quot; on match. | [optional] 
**share_token** | **str, none_type** | URL-safe random token. Populated by POST /me/templates/:id/share;  the /public/templates/:token route surfaces a read-only view any  visitor can browse + import. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


