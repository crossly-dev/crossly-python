# GetConnectionHealthResponseAnchors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected** | **[str]** | What we were looking for. Empty ⇒ this platform is unmonitored. | 
**observations** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | 
**present** | **[str]** | Name found carrying a non-empty value — the only honest \&quot;logged in\&quot;. | 
**empty** | **[str]** | Name found, value is the empty string. The Whatnot class. | 
**missing** | **[str]** | Name not in the jar at all. | 
**cookie_count** | **float** |  | 
**observed_cookie_names** | **[str]** | Cookie names actually in the jar, truncated. This is the payload that turns \&quot;anchors missing\&quot; into a diagnosis: if the jar holds 30 cookies and none are ours, a rename is the likely story; if it holds three device cookies, the browser is signed out. NAMES ONLY — never values. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


