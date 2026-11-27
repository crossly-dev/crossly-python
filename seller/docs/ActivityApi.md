# crossly.ActivityApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_action_log_export**](ActivityApi.md#create_action_log_export) | **POST** /v1/action-log/exports | Queue an export of the Activity Log: every event (csv, ndjson, pdf) or a summary report (pdf, ndjson). Poll GET /api/v1/action-log/exports/{exportId}, then download it. Exports never contain IP addresses.
[**create_action_log_search_translate**](ActivityApi.md#create_action_log_search_translate) | **POST** /v1/action-log/search/translate | Turn a question in words (\&quot;failed delists on Mercari last week\&quot;) into an Activity Log search: pass the returned &#x60;q&#x60; to GET /api/v1/action-log (or the histogram and csv/ndjson exports). Nothing is run. A 404 with details.code &#x60;not_enabled&#x60; means natural-language search is off for this account.
[**create_detected_event_event_confirm**](ActivityApi.md#create_detected_event_event_confirm) | **POST** /v1/detected-events/events/{id}/confirm | Answer an open ask (canConfirm true): optionally which item it is (itemId, one of the match candidates) and which actions to run instead of the ask&#39;s preselected ones. Returns the event. 409 ask_not_open when the event is not waiting.
[**create_detected_event_event_undo**](ActivityApi.md#create_detected_event_event_undo) | **POST** /v1/detected-events/events/{id}/undo | Undo what Crossly did for an event (canUndo true): every executed action&#39;s stored inverse runs, newest first (restore stock, relist, unlink…). Returns the event. 409 nothing_to_undo when nothing is reversible.
[**create_detected_event_rule**](ActivityApi.md#create_detected_event_rule) | **POST** /v1/detected-events/rules | Create a detection rule: which detected events it applies to (filter + optional condition over any event axis) and what Crossly does then (and else). Without order it is placed most-specific-first, above the default set. Returns the stored rule with its id.
[**create_detected_event_rule_place**](ActivityApi.md#create_detected_event_rule_place) | **POST** /v1/detected-events/rules/place | Save one rule and the whole evaluation order in one transaction: rule.id is an existing id (replace) or any new client id (create); ids is every rule id top-down, naming the rule by that id. Returns the stored rule and the list.
[**create_detected_event_rule_reorder**](ActivityApi.md#create_detected_event_rule_reorder) | **POST** /v1/detected-events/rules/reorder | Set the evaluation order: ids top-down, defaults included (ids from the rules list). Rules are re-numbered 10, 20, 30…; a default moved above one of your rules is stored as your edit. Returns the list.
[**create_detected_event_rule_reset_default**](ActivityApi.md#create_detected_event_rule_reset_default) | **POST** /v1/detected-events/rules/reset-defaults | Drop your edits of the shipped default rules (keys, or all when omitted). Returns the list.
[**create_detected_event_simulate**](ActivityApi.md#create_detected_event_simulate) | **POST** /v1/detected-events/simulate | Run one event through the rules without acting: the winning rule, rules it shadowed, the trace, the guards that held actions back and the plan per target with how it would run (direct / relay / ask / skip). event needs only kind; every axis left out takes its default. rules &#x3D; an unsaved draft list.
[**create_detected_event_simulate_impact**](ActivityApi.md#create_detected_event_simulate_impact) | **POST** /v1/detected-events/simulate/impact | What a rule edit would change: your detected events of the last days (default 30, at most 500) re-resolved against the draft rules and against the stored ones. Per event: winning rule and actions before and after, and whether it changed. Nothing runs.
[**create_email_event_confirm**](ActivityApi.md#create_email_event_confirm) | **POST** /v1/email-events/{id}/confirm | Confirm an email-detected event: re-run it as certain (a possible sale records the sale and delists the item elsewhere). When several listings could be meant, pass platformListingDbId to choose one.
[**create_email_event_dismiss**](ActivityApi.md#create_email_event_dismiss) | **POST** /v1/email-events/{id}/dismiss | Dismiss an email-detected event (\&quot;not a sale\&quot;): closes the card without acting.
[**create_event_policy_decision_confirm**](ActivityApi.md#create_event_policy_decision_confirm) | **POST** /v1/event-policies/decisions/{id}/confirm | Confirm a review decision from a webhook, order poller or app relay (canConfirm true): the event runs again with the seller confirmed, so a review rule runs the strongest allowed non-review action for that cell. Returns the new decision. 409 when the decision was already confirmed or is not confirmable (email review decisions are confirmed on their review card).
[**delete_detected_event_rule**](ActivityApi.md#delete_detected_event_rule) | **DELETE** /v1/detected-events/rules/{id} | Delete a detection rule. Deleting your edit of a default (its id, or default:&lt;key&gt;) brings the shipped default back; deleting a translated event-policy rule deletes that policy rule too.
[**delete_event_policy_rule**](ActivityApi.md#delete_event_policy_rule) | **DELETE** /v1/event-policies/rules/{id} | Delete a rule: its cell falls back to the next scope (platform → global → the built-in default).
[**get_action_log**](ActivityApi.md#get_action_log) | **GET** /v1/action-log/{id} | One Activity Log event by id, with &#x60;view&#x60; including its steps and, for bulk jobs, its children.
[**get_action_log_export**](ActivityApi.md#get_action_log_export) | **GET** /v1/action-log/exports/{exportId} | The state of one Activity Log export.
[**get_action_log_export_download**](ActivityApi.md#get_action_log_export_download) | **GET** /v1/action-log/exports/{exportId}/download | Download a finished Activity Log export (for 24 hours after it completes).
[**get_action_log_facet**](ActivityApi.md#get_action_log_facet) | **GET** /v1/action-log/facets | Filter options of the caller&#39;s Activity Log (last 90 days): areas with their actions and counts, the team members who acted, platforms and outcomes.
[**get_detected_event_event**](ActivityApi.md#get_detected_event_event) | **GET** /v1/detected-events/events/{id} | One detected event with every report of it (first + corroborations, with correlation and contradiction), the guards that held actions back, the plan and each executed action&#39;s outcome and reversibility.
[**get_event_policy**](ActivityApi.md#get_event_policy) | **GET** /v1/event-policies | What Crossly does with each detected marketplace event (sale, listing ended, offer, cancellation, label, shipped, delivered, refund, return, payout, message), per who owns the item (crossly, imported, app_managed, other_tool, untracked). Each matrix cell lists the allowed actions and the effective one, with the scope it comes from (app &gt; platform &gt; global &gt; default). Pass platform (or appId) to see the matrix as that platform&#39;s (or app&#39;s) items see it. Also returns the rules, platforms and connected apps.
[**list_action_log**](ActivityApi.md#list_action_log) | **GET** /v1/action-log | List Activity Log events, newest first. Each event carries &#x60;view&#x60; (title, sentence, fields, failure advice, who did it) and typed &#x60;detail&#x60;. Page with &#x60;cursor&#x60;; &#x60;pagination.total&#x60; counts matches.
[**list_action_log_calls**](ActivityApi.md#list_action_log_calls) | **GET** /v1/action-log/{id}/calls | The outbound platform HTTP calls under an event (oldest first) — platform, operation, method, host, status, latency, error class/message, proxy + recipe id. Answers \&quot;what was sent / what went wrong\&quot;. The URL path, request/response bodies and persisted-query hash are never returned.
[**list_action_log_histogram**](ActivityApi.md#list_action_log_histogram) | **GET** /v1/action-log/histogram | Events per UTC day for the list filters (default: the last 30 days; at most 366).
[**list_detected_event_events**](ActivityApi.md#list_detected_event_events) | **GET** /v1/detected-events/events | Every event Crossly detected (sales, order changes, listing changes, offers, messages, account notices), newest first: all its axes, the rule that decided it, its corroborating reports, the plan per target and how each action went, with canConfirm (an open ask) and canUndo. Cursor-paged; filter by kinds, platforms statuses and accounts (comma-separated) and since (ISO time).
[**list_detected_event_rules**](ActivityApi.md#list_detected_event_rules) | **GET** /v1/detected-events/rules | The seller&#39;s detection rules, top-down in the order they are evaluated (first match wins unless a rule says continue): the seller&#39;s own rules, translations of their event-policy rules (source legacy), then the shipped default set (source default, ids default:&lt;key&gt;; a stored edit of a default replaces it). Each rule has a filter (event kinds, platforms, accounts, apps, tags, items), an optional condition over any event axis, the actions it runs (then / else) and its guard loosenings.
[**list_email_events**](ActivityApi.md#list_email_events) | **GET** /v1/email-events | List email-detected events waiting for the seller (status&#x3D;needs_review): a possible sale, ended listing, cancellation or other event an email reported that was not certain enough to act on automatically.
[**list_event_policy_decisions**](ActivityApi.md#list_event_policy_decisions) | **GET** /v1/event-policies/decisions | The decision log, newest first: for each detected event, what the rule or default asked for, what was done (after capability fallback and the email confidence ceiling), the rule that decided it, and the outcome (done / skipped / failed / review). Cursor-paged; filter by event, ownership, platform or outcome (outcome&#x3D;review: still waiting for the seller). Kept 90 days.
[**update_detected_event_rule**](ActivityApi.md#update_detected_event_rule) | **PUT** /v1/detected-events/rules/{id} | Replace a detection rule. An id default:&lt;key&gt; stores your edit of that shipped default (delete it, or reset-defaults, to go back to the shipped one).
[**update_event_policy_rule**](ActivityApi.md#update_event_policy_rule) | **PUT** /v1/event-policies/rules | Set what Crossly does with one kind of detected event for one kind of item: scope global (scopeValue null), platform (scopeValue &#x3D; platform id) or app (scopeValue &#x3D; OAuth app id, app_managed items only). Replaces the rule for the same cell and scope. The action must be one the matrix allows for that cell; import actions exist only for untracked items.


# **create_action_log_export**
> GetActionLogExportResponse create_action_log_export(create_action_log_export_request)

Queue an export of the Activity Log: every event (csv, ndjson, pdf) or a summary report (pdf, ndjson). Poll GET /api/v1/action-log/exports/{exportId}, then download it. Exports never contain IP addresses.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.action.get_action_log_export_response import GetActionLogExportResponse
from crossly.model.common.error import Error
from crossly.model.action.create_action_log_export_request import CreateActionLogExportRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    create_action_log_export_request = CreateActionLogExportRequest(
        format="csv",
        report="events",
        filters=CreateActionLogExportRequestFilters(
            action="action_example",
            actor_user_id="actor_user_id_example",
            status="success",
            target_type="target_type_example",
            target_id="target_id_example",
            area="listings",
            platform="platform_example",
            category="category_example",
            source="source_example",
            q="q_example",
            since=dateutil_parser('1970-01-01T00:00:00.00Z'),
            until=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # CreateActionLogExportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Queue an export of the Activity Log: every event (csv, ndjson, pdf) or a summary report (pdf, ndjson). Poll GET /api/v1/action-log/exports/{exportId}, then download it. Exports never contain IP addresses.
        api_response = api_instance.create_action_log_export(create_action_log_export_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_action_log_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_action_log_export_request** | **CreateActionLogExportRequest**|  |

### Return type

**GetActionLogExportResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_action_log_search_translate**
> CreateActionLogSearchTranslateResponse create_action_log_search_translate(create_action_log_search_translate_request)

Turn a question in words (\"failed delists on Mercari last week\") into an Activity Log search: pass the returned `q` to GET /api/v1/action-log (or the histogram and csv/ndjson exports). Nothing is run. A 404 with details.code `not_enabled` means natural-language search is off for this account.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.action.create_action_log_search_translate_response import CreateActionLogSearchTranslateResponse
from crossly.model.common.error import Error
from crossly.model.action.create_action_log_search_translate_request import CreateActionLogSearchTranslateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    create_action_log_search_translate_request = CreateActionLogSearchTranslateRequest(
        text="text_example",
    ) # CreateActionLogSearchTranslateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Turn a question in words (\"failed delists on Mercari last week\") into an Activity Log search: pass the returned `q` to GET /api/v1/action-log (or the histogram and csv/ndjson exports). Nothing is run. A 404 with details.code `not_enabled` means natural-language search is off for this account.
        api_response = api_instance.create_action_log_search_translate(create_action_log_search_translate_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_action_log_search_translate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_action_log_search_translate_request** | **CreateActionLogSearchTranslateRequest**|  |

### Return type

**CreateActionLogSearchTranslateResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_detected_event_event_confirm**
> CreateDetectedEventEventUndoResponse create_detected_event_event_confirm(id, create_detected_event_event_confirm_request)

Answer an open ask (canConfirm true): optionally which item it is (itemId, one of the match candidates) and which actions to run instead of the ask's preselected ones. Returns the event. 409 ask_not_open when the event is not waiting.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.detected.create_detected_event_event_confirm_request import CreateDetectedEventEventConfirmRequest
from crossly.model.common.error import Error
from crossly.model.detected.create_detected_event_event_undo_response import CreateDetectedEventEventUndoResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 
    create_detected_event_event_confirm_request = CreateDetectedEventEventConfirmRequest(
        item_id="item_id_example",
        actions=[
            {
                "key": None,
            },
        ],
    ) # CreateDetectedEventEventConfirmRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Answer an open ask (canConfirm true): optionally which item it is (itemId, one of the match candidates) and which actions to run instead of the ask's preselected ones. Returns the event. 409 ask_not_open when the event is not waiting.
        api_response = api_instance.create_detected_event_event_confirm(id, create_detected_event_event_confirm_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_detected_event_event_confirm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **create_detected_event_event_confirm_request** | **CreateDetectedEventEventConfirmRequest**|  |

### Return type

**CreateDetectedEventEventUndoResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_detected_event_event_undo**
> CreateDetectedEventEventUndoResponse create_detected_event_event_undo(id)

Undo what Crossly did for an event (canUndo true): every executed action's stored inverse runs, newest first (restore stock, relist, unlink…). Returns the event. 409 nothing_to_undo when nothing is reversible.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.detected.create_detected_event_event_undo_response import CreateDetectedEventEventUndoResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Undo what Crossly did for an event (canUndo true): every executed action's stored inverse runs, newest first (restore stock, relist, unlink…). Returns the event. 409 nothing_to_undo when nothing is reversible.
        api_response = api_instance.create_detected_event_event_undo(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_detected_event_event_undo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateDetectedEventEventUndoResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_detected_event_rule**
> CreateDetectedEventRuleResponse create_detected_event_rule(create_detected_event_rule_request)

Create a detection rule: which detected events it applies to (filter + optional condition over any event axis) and what Crossly does then (and else). Without order it is placed most-specific-first, above the default set. Returns the stored rule with its id.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.detected.create_detected_event_rule_request import CreateDetectedEventRuleRequest
from crossly.model.detected.create_detected_event_rule_response import CreateDetectedEventRuleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    create_detected_event_rule_request = CreateDetectedEventRuleRequest(
        name="name_example",
        enabled=True,
        order=1,
        filter={
            "key": None,
        },
        when={
            "key": None,
        },
        then=[
            {
                "key": None,
            },
        ],
        _else=[
            {
                "key": None,
            },
        ],
        _continue=True,
        allow_weak_evidence=True,
        loosen={
            "key": None,
        },
        target={
            "key": None,
        },
        candidate_pool={
            "key": None,
        },
        meta={
            "key": None,
        },
    ) # CreateDetectedEventRuleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a detection rule: which detected events it applies to (filter + optional condition over any event axis) and what Crossly does then (and else). Without order it is placed most-specific-first, above the default set. Returns the stored rule with its id.
        api_response = api_instance.create_detected_event_rule(create_detected_event_rule_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_detected_event_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_detected_event_rule_request** | **CreateDetectedEventRuleRequest**|  |

### Return type

**CreateDetectedEventRuleResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_detected_event_rule_place**
> CreateDetectedEventRulePlaceResponse create_detected_event_rule_place(create_detected_event_rule_place_request)

Save one rule and the whole evaluation order in one transaction: rule.id is an existing id (replace) or any new client id (create); ids is every rule id top-down, naming the rule by that id. Returns the stored rule and the list.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.detected.create_detected_event_rule_place_response import CreateDetectedEventRulePlaceResponse
from crossly.model.detected.create_detected_event_rule_place_request import CreateDetectedEventRulePlaceRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    create_detected_event_rule_place_request = CreateDetectedEventRulePlaceRequest(
        rule=CreateDetectedEventRuleRequest(
            name="name_example",
            enabled=True,
            order=1,
            filter={
                "key": None,
            },
            when={
                "key": None,
            },
            then=[
                {
                    "key": None,
                },
            ],
            _else=[
                {
                    "key": None,
                },
            ],
            _continue=True,
            allow_weak_evidence=True,
            loosen={
                "key": None,
            },
            target={
                "key": None,
            },
            candidate_pool={
                "key": None,
            },
            meta={
                "key": None,
            },
        ),
        ids=[
            "ids_example",
        ],
    ) # CreateDetectedEventRulePlaceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Save one rule and the whole evaluation order in one transaction: rule.id is an existing id (replace) or any new client id (create); ids is every rule id top-down, naming the rule by that id. Returns the stored rule and the list.
        api_response = api_instance.create_detected_event_rule_place(create_detected_event_rule_place_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_detected_event_rule_place: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_detected_event_rule_place_request** | **CreateDetectedEventRulePlaceRequest**|  |

### Return type

**CreateDetectedEventRulePlaceResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_detected_event_rule_reorder**
> CreateDetectedEventRuleReorderResponse create_detected_event_rule_reorder(create_detected_event_rule_reorder_request)

Set the evaluation order: ids top-down, defaults included (ids from the rules list). Rules are re-numbered 10, 20, 30…; a default moved above one of your rules is stored as your edit. Returns the list.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.detected.create_detected_event_rule_reorder_response import CreateDetectedEventRuleReorderResponse
from crossly.model.detected.create_detected_event_rule_reorder_request import CreateDetectedEventRuleReorderRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    create_detected_event_rule_reorder_request = CreateDetectedEventRuleReorderRequest(
        ids=[
            "ids_example",
        ],
    ) # CreateDetectedEventRuleReorderRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set the evaluation order: ids top-down, defaults included (ids from the rules list). Rules are re-numbered 10, 20, 30…; a default moved above one of your rules is stored as your edit. Returns the list.
        api_response = api_instance.create_detected_event_rule_reorder(create_detected_event_rule_reorder_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_detected_event_rule_reorder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_detected_event_rule_reorder_request** | **CreateDetectedEventRuleReorderRequest**|  |

### Return type

**CreateDetectedEventRuleReorderResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_detected_event_rule_reset_default**
> CreateDetectedEventRuleReorderResponse create_detected_event_rule_reset_default(create_detected_event_rule_reset_default_request)

Drop your edits of the shipped default rules (keys, or all when omitted). Returns the list.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.detected.create_detected_event_rule_reset_default_request import CreateDetectedEventRuleResetDefaultRequest
from crossly.model.common.error import Error
from crossly.model.detected.create_detected_event_rule_reorder_response import CreateDetectedEventRuleReorderResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    create_detected_event_rule_reset_default_request = CreateDetectedEventRuleResetDefaultRequest(
        keys=[
            "keys_example",
        ],
    ) # CreateDetectedEventRuleResetDefaultRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Drop your edits of the shipped default rules (keys, or all when omitted). Returns the list.
        api_response = api_instance.create_detected_event_rule_reset_default(create_detected_event_rule_reset_default_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_detected_event_rule_reset_default: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_detected_event_rule_reset_default_request** | **CreateDetectedEventRuleResetDefaultRequest**|  |

### Return type

**CreateDetectedEventRuleReorderResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_detected_event_simulate**
> CreateDetectedEventSimulateResponse create_detected_event_simulate(create_detected_event_simulate_request)

Run one event through the rules without acting: the winning rule, rules it shadowed, the trace, the guards that held actions back and the plan per target with how it would run (direct / relay / ask / skip). event needs only kind; every axis left out takes its default. rules = an unsaved draft list.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.detected.create_detected_event_simulate_response import CreateDetectedEventSimulateResponse
from crossly.model.detected.create_detected_event_simulate_request import CreateDetectedEventSimulateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    create_detected_event_simulate_request = CreateDetectedEventSimulateRequest(
        event={
            "key": None,
        },
        rules=[
            {
                "key": None,
            },
        ],
    ) # CreateDetectedEventSimulateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Run one event through the rules without acting: the winning rule, rules it shadowed, the trace, the guards that held actions back and the plan per target with how it would run (direct / relay / ask / skip). event needs only kind; every axis left out takes its default. rules = an unsaved draft list.
        api_response = api_instance.create_detected_event_simulate(create_detected_event_simulate_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_detected_event_simulate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_detected_event_simulate_request** | **CreateDetectedEventSimulateRequest**|  |

### Return type

**CreateDetectedEventSimulateResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_detected_event_simulate_impact**
> CreateDetectedEventSimulateImpactResponse create_detected_event_simulate_impact(create_detected_event_simulate_impact_request)

What a rule edit would change: your detected events of the last days (default 30, at most 500) re-resolved against the draft rules and against the stored ones. Per event: winning rule and actions before and after, and whether it changed. Nothing runs.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.detected.create_detected_event_simulate_impact_response import CreateDetectedEventSimulateImpactResponse
from crossly.model.detected.create_detected_event_simulate_impact_request import CreateDetectedEventSimulateImpactRequest
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    create_detected_event_simulate_impact_request = CreateDetectedEventSimulateImpactRequest(
        rules=[
            {
                "key": None,
            },
        ],
        days=1,
    ) # CreateDetectedEventSimulateImpactRequest | 

    # example passing only required values which don't have defaults set
    try:
        # What a rule edit would change: your detected events of the last days (default 30, at most 500) re-resolved against the draft rules and against the stored ones. Per event: winning rule and actions before and after, and whether it changed. Nothing runs.
        api_response = api_instance.create_detected_event_simulate_impact(create_detected_event_simulate_impact_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_detected_event_simulate_impact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_detected_event_simulate_impact_request** | **CreateDetectedEventSimulateImpactRequest**|  |

### Return type

**CreateDetectedEventSimulateImpactResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_email_event_confirm**
> CreateEmailEventConfirmResponse create_email_event_confirm(id, create_email_event_confirm_request)

Confirm an email-detected event: re-run it as certain (a possible sale records the sale and delists the item elsewhere). When several listings could be meant, pass platformListingDbId to choose one.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.email.create_email_event_confirm_request import CreateEmailEventConfirmRequest
from crossly.model.common.error import Error
from crossly.model.email.create_email_event_confirm_response import CreateEmailEventConfirmResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 
    create_email_event_confirm_request = CreateEmailEventConfirmRequest(
        platform_listing_db_id="platform_listing_db_id_example",
    ) # CreateEmailEventConfirmRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Confirm an email-detected event: re-run it as certain (a possible sale records the sale and delists the item elsewhere). When several listings could be meant, pass platformListingDbId to choose one.
        api_response = api_instance.create_email_event_confirm(id, create_email_event_confirm_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_email_event_confirm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **create_email_event_confirm_request** | **CreateEmailEventConfirmRequest**|  |

### Return type

**CreateEmailEventConfirmResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_email_event_dismiss**
> IdStatusResponse create_email_event_dismiss(id)

Dismiss an email-detected event (\"not a sale\"): closes the card without acting.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.id_status_response import IdStatusResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Dismiss an email-detected event (\"not a sale\"): closes the card without acting.
        api_response = api_instance.create_email_event_dismiss(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_email_event_dismiss: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**IdStatusResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_event_policy_decision_confirm**
> CreateEventPolicyDecisionConfirmResponse create_event_policy_decision_confirm(id)

Confirm a review decision from a webhook, order poller or app relay (canConfirm true): the event runs again with the seller confirmed, so a review rule runs the strongest allowed non-review action for that cell. Returns the new decision. 409 when the decision was already confirmed or is not confirmable (email review decisions are confirmed on their review card).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.event.create_event_policy_decision_confirm_response import CreateEventPolicyDecisionConfirmResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Confirm a review decision from a webhook, order poller or app relay (canConfirm true): the event runs again with the seller confirmed, so a review rule runs the strongest allowed non-review action for that cell. Returns the new decision. 409 when the decision was already confirmed or is not confirmable (email review decisions are confirmed on their review card).
        api_response = api_instance.create_event_policy_decision_confirm(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->create_event_policy_decision_confirm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateEventPolicyDecisionConfirmResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_detected_event_rule**
> DeleteStoryResponse delete_detected_event_rule(id)

Delete a detection rule. Deleting your edit of a default (its id, or default:<key>) brings the shipped default back; deleting a translated event-policy rule deletes that policy rule too.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.common.delete_story_response import DeleteStoryResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a detection rule. Deleting your edit of a default (its id, or default:<key>) brings the shipped default back; deleting a translated event-policy rule deletes that policy rule too.
        api_response = api_instance.delete_detected_event_rule(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->delete_detected_event_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteStoryResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_event_policy_rule**
> DeleteStoryResponse delete_event_policy_rule(id)

Delete a rule: its cell falls back to the next scope (platform → global → the built-in default).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.common.delete_story_response import DeleteStoryResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a rule: its cell falls back to the next scope (platform → global → the built-in default).
        api_response = api_instance.delete_event_policy_rule(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->delete_event_policy_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**DeleteStoryResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_action_log**
> ListActionLogItem get_action_log(id)

One Activity Log event by id, with `view` including its steps and, for bulk jobs, its children.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.action.list_action_log_item import ListActionLogItem
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One Activity Log event by id, with `view` including its steps and, for bulk jobs, its children.
        api_response = api_instance.get_action_log(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->get_action_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListActionLogItem**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_action_log_export**
> GetActionLogExportResponse get_action_log_export(export_id)

The state of one Activity Log export.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.action.get_action_log_export_response import GetActionLogExportResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    export_id = "exportId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The state of one Activity Log export.
        api_response = api_instance.get_action_log_export(export_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->get_action_log_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**|  |

### Return type

**GetActionLogExportResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_action_log_export_download**
> GetActionLogExportDownloadResponse get_action_log_export_download(export_id)

Download a finished Activity Log export (for 24 hours after it completes).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.action.get_action_log_export_download_response import GetActionLogExportDownloadResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    export_id = "exportId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Download a finished Activity Log export (for 24 hours after it completes).
        api_response = api_instance.get_action_log_export_download(export_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->get_action_log_export_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**|  |

### Return type

**GetActionLogExportDownloadResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_action_log_facet**
> GetActionLogFacetResponse get_action_log_facet()

Filter options of the caller's Activity Log (last 90 days): areas with their actions and counts, the team members who acted, platforms and outcomes.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.action.get_action_log_facet_response import GetActionLogFacetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Filter options of the caller's Activity Log (last 90 days): areas with their actions and counts, the team members who acted, platforms and outcomes.
        api_response = api_instance.get_action_log_facet()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->get_action_log_facet: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetActionLogFacetResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_detected_event_event**
> GetDetectedEventEventResponse get_detected_event_event(id)

One detected event with every report of it (first + corroborations, with correlation and contradiction), the guards that held actions back, the plan and each executed action's outcome and reversibility.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.detected.get_detected_event_event_response import GetDetectedEventEventResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # One detected event with every report of it (first + corroborations, with correlation and contradiction), the guards that held actions back, the plan and each executed action's outcome and reversibility.
        api_response = api_instance.get_detected_event_event(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->get_detected_event_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetDetectedEventEventResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_event_policy**
> GetEventPolicyResponse get_event_policy()

What Crossly does with each detected marketplace event (sale, listing ended, offer, cancellation, label, shipped, delivered, refund, return, payout, message), per who owns the item (crossly, imported, app_managed, other_tool, untracked). Each matrix cell lists the allowed actions and the effective one, with the scope it comes from (app > platform > global > default). Pass platform (or appId) to see the matrix as that platform's (or app's) items see it. Also returns the rules, platforms and connected apps.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.event.get_event_policy_response import GetEventPolicyResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    platform = "platform_example" # str |  (optional)
    app_id = "appId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # What Crossly does with each detected marketplace event (sale, listing ended, offer, cancellation, label, shipped, delivered, refund, return, payout, message), per who owns the item (crossly, imported, app_managed, other_tool, untracked). Each matrix cell lists the allowed actions and the effective one, with the scope it comes from (app > platform > global > default). Pass platform (or appId) to see the matrix as that platform's (or app's) items see it. Also returns the rules, platforms and connected apps.
        api_response = api_instance.get_event_policy(platform=platform, app_id=app_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->get_event_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**|  | [optional]
 **app_id** | **str**|  | [optional]

### Return type

**GetEventPolicyResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_action_log**
> ListActionLogResponse list_action_log()

List Activity Log events, newest first. Each event carries `view` (title, sentence, fields, failure advice, who did it) and typed `detail`. Page with `cursor`; `pagination.total` counts matches.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.action.list_action_log_response import ListActionLogResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    platform = "platform_example" # str | Platform id (`ebay`, `poshmark`, ...). (optional)
    action = "action_example" # str | A canonical action key (`listing.delist`, see the public action catalog) or a legacy action word. (optional)
    category = "category_example" # str |  (optional)
    area = "listings" # str | A seller area: every action of that area (the grouped filter of the dashboard). (optional)
    status = "pending" # str |  (optional)
    source = "source_example" # str |  (optional)
    target_type = "targetType_example" # str | With targetId: events about that object (any of their targets). (optional)
    target_id = "targetId_example" # str |  (optional)
    actor_user_id = "actorUserId_example" # str | Only what one team member did. (optional)
    q = "q_example" # str | A search in the activity query language (`action:listing.* -outcome:failure \"free text\"`), ANDed with the other filters. POST /api/v1/action-log/search/translate turns a question in words into one. (optional)
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Inclusive lower bound on when the action happened. (optional)
    until = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Exclusive upper bound. (optional)
    at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Jump to a time: the page starts at the newest event at or before it. (optional)
    cursor = "cursor_example" # str | `pagination.nextCursor` of the previous page. (optional)
    limit = 50 # int |  (optional) if omitted the server will use the default value of 50
    offset = 0 # int | Deprecated: use cursor. offset + limit may reach at most 1000 events. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Activity Log events, newest first. Each event carries `view` (title, sentence, fields, failure advice, who did it) and typed `detail`. Page with `cursor`; `pagination.total` counts matches.
        api_response = api_instance.list_action_log(platform=platform, action=action, category=category, area=area, status=status, source=source, target_type=target_type, target_id=target_id, actor_user_id=actor_user_id, q=q, since=since, until=until, at=at, cursor=cursor, limit=limit, offset=offset)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->list_action_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Platform id (&#x60;ebay&#x60;, &#x60;poshmark&#x60;, ...). | [optional]
 **action** | **str**| A canonical action key (&#x60;listing.delist&#x60;, see the public action catalog) or a legacy action word. | [optional]
 **category** | **str**|  | [optional]
 **area** | **str**| A seller area: every action of that area (the grouped filter of the dashboard). | [optional]
 **status** | **str**|  | [optional]
 **source** | **str**|  | [optional]
 **target_type** | **str**| With targetId: events about that object (any of their targets). | [optional]
 **target_id** | **str**|  | [optional]
 **actor_user_id** | **str**| Only what one team member did. | [optional]
 **q** | **str**| A search in the activity query language (&#x60;action:listing.* -outcome:failure \&quot;free text\&quot;&#x60;), ANDed with the other filters. POST /api/v1/action-log/search/translate turns a question in words into one. | [optional]
 **since** | **datetime**| Inclusive lower bound on when the action happened. | [optional]
 **until** | **datetime**| Exclusive upper bound. | [optional]
 **at** | **datetime**| Jump to a time: the page starts at the newest event at or before it. | [optional]
 **cursor** | **str**| &#x60;pagination.nextCursor&#x60; of the previous page. | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| Deprecated: use cursor. offset + limit may reach at most 1000 events. | [optional]

### Return type

**ListActionLogResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_action_log_calls**
> ListActionLogCallsResponse list_action_log_calls(id)

The outbound platform HTTP calls under an event (oldest first) — platform, operation, method, host, status, latency, error class/message, proxy + recipe id. Answers \"what was sent / what went wrong\". The URL path, request/response bodies and persisted-query hash are never returned.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.action.list_action_log_calls_response import ListActionLogCallsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The outbound platform HTTP calls under an event (oldest first) — platform, operation, method, host, status, latency, error class/message, proxy + recipe id. Answers \"what was sent / what went wrong\". The URL path, request/response bodies and persisted-query hash are never returned.
        api_response = api_instance.list_action_log_calls(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->list_action_log_calls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**ListActionLogCallsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_action_log_histogram**
> ListActionLogHistogramResponse list_action_log_histogram()

Events per UTC day for the list filters (default: the last 30 days; at most 366).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.action.list_action_log_histogram_response import ListActionLogHistogramResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    platform = "platform_example" # str | Platform id (`ebay`, `poshmark`, ...). (optional)
    action = "action_example" # str | A canonical action key (`listing.delist`, see the public action catalog) or a legacy action word. (optional)
    category = "category_example" # str |  (optional)
    area = "listings" # str | A seller area: every action of that area (the grouped filter of the dashboard). (optional)
    status = "pending" # str |  (optional)
    source = "source_example" # str |  (optional)
    target_type = "targetType_example" # str | With targetId: events about that object (any of their targets). (optional)
    target_id = "targetId_example" # str |  (optional)
    actor_user_id = "actorUserId_example" # str | Only what one team member did. (optional)
    q = "q_example" # str | A search in the activity query language (`action:listing.* -outcome:failure \"free text\"`), ANDed with the other filters. POST /api/v1/action-log/search/translate turns a question in words into one. (optional)
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Inclusive lower bound on when the action happened. (optional)
    until = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Exclusive upper bound. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Events per UTC day for the list filters (default: the last 30 days; at most 366).
        api_response = api_instance.list_action_log_histogram(platform=platform, action=action, category=category, area=area, status=status, source=source, target_type=target_type, target_id=target_id, actor_user_id=actor_user_id, q=q, since=since, until=until)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->list_action_log_histogram: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Platform id (&#x60;ebay&#x60;, &#x60;poshmark&#x60;, ...). | [optional]
 **action** | **str**| A canonical action key (&#x60;listing.delist&#x60;, see the public action catalog) or a legacy action word. | [optional]
 **category** | **str**|  | [optional]
 **area** | **str**| A seller area: every action of that area (the grouped filter of the dashboard). | [optional]
 **status** | **str**|  | [optional]
 **source** | **str**|  | [optional]
 **target_type** | **str**| With targetId: events about that object (any of their targets). | [optional]
 **target_id** | **str**|  | [optional]
 **actor_user_id** | **str**| Only what one team member did. | [optional]
 **q** | **str**| A search in the activity query language (&#x60;action:listing.* -outcome:failure \&quot;free text\&quot;&#x60;), ANDed with the other filters. POST /api/v1/action-log/search/translate turns a question in words into one. | [optional]
 **since** | **datetime**| Inclusive lower bound on when the action happened. | [optional]
 **until** | **datetime**| Exclusive upper bound. | [optional]

### Return type

**ListActionLogHistogramResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_detected_event_events**
> ListDetectedEventEventsResponse list_detected_event_events()

Every event Crossly detected (sales, order changes, listing changes, offers, messages, account notices), newest first: all its axes, the rule that decided it, its corroborating reports, the plan per target and how each action went, with canConfirm (an open ask) and canUndo. Cursor-paged; filter by kinds, platforms statuses and accounts (comma-separated) and since (ISO time).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.detected.list_detected_event_events_response import ListDetectedEventEventsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    kinds = "kinds_example" # str |  (optional)
    platforms = "platforms_example" # str |  (optional)
    accounts = "accounts_example" # str | Comma-separated platform account ids (scope.account). (optional)
    statuses = "statuses_example" # str | Comma-separated: acted, held, asked, confirmed, ignored, undone, failed, received, corrected (optional)
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    cursor = "cursor_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Every event Crossly detected (sales, order changes, listing changes, offers, messages, account notices), newest first: all its axes, the rule that decided it, its corroborating reports, the plan per target and how each action went, with canConfirm (an open ask) and canUndo. Cursor-paged; filter by kinds, platforms statuses and accounts (comma-separated) and since (ISO time).
        api_response = api_instance.list_detected_event_events(kinds=kinds, platforms=platforms, accounts=accounts, statuses=statuses, since=since, cursor=cursor, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->list_detected_event_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kinds** | **str**|  | [optional]
 **platforms** | **str**|  | [optional]
 **accounts** | **str**| Comma-separated platform account ids (scope.account). | [optional]
 **statuses** | **str**| Comma-separated: acted, held, asked, confirmed, ignored, undone, failed, received, corrected | [optional]
 **since** | **datetime**|  | [optional]
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

**ListDetectedEventEventsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_detected_event_rules**
> ListDetectedEventRulesResponse list_detected_event_rules()

The seller's detection rules, top-down in the order they are evaluated (first match wins unless a rule says continue): the seller's own rules, translations of their event-policy rules (source legacy), then the shipped default set (source default, ids default:<key>; a stored edit of a default replaces it). Each rule has a filter (event kinds, platforms, accounts, apps, tags, items), an optional condition over any event axis, the actions it runs (then / else) and its guard loosenings.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.detected.list_detected_event_rules_response import ListDetectedEventRulesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The seller's detection rules, top-down in the order they are evaluated (first match wins unless a rule says continue): the seller's own rules, translations of their event-policy rules (source legacy), then the shipped default set (source default, ids default:<key>; a stored edit of a default replaces it). Each rule has a filter (event kinds, platforms, accounts, apps, tags, items), an optional condition over any event axis, the actions it runs (then / else) and its guard loosenings.
        api_response = api_instance.list_detected_event_rules()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->list_detected_event_rules: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListDetectedEventRulesResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_email_events**
> ListEmailEventsResponse list_email_events()

List email-detected events waiting for the seller (status=needs_review): a possible sale, ended listing, cancellation or other event an email reported that was not certain enough to act on automatically.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.email.list_email_events_response import ListEmailEventsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    status = "needs_review" # str |  (optional) if omitted the server will use the default value of "needs_review"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List email-detected events waiting for the seller (status=needs_review): a possible sale, ended listing, cancellation or other event an email reported that was not certain enough to act on automatically.
        api_response = api_instance.list_email_events(status=status)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->list_email_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] if omitted the server will use the default value of "needs_review"

### Return type

**ListEmailEventsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **list_event_policy_decisions**
> ListEventPolicyDecisionsResponse list_event_policy_decisions()

The decision log, newest first: for each detected event, what the rule or default asked for, what was done (after capability fallback and the email confidence ceiling), the rule that decided it, and the outcome (done / skipped / failed / review). Cursor-paged; filter by event, ownership, platform or outcome (outcome=review: still waiting for the seller). Kept 90 days.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.event.list_event_policy_decisions_response import ListEventPolicyDecisionsResponse
from crossly.model.common.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    cursor = "cursor_example" # str |  (optional)
    limit = 1 # int |  (optional)
    event = "sale" # str |  (optional)
    ownership = "crossly" # str |  (optional)
    platform = "platform_example" # str |  (optional)
    outcome = "done" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # The decision log, newest first: for each detected event, what the rule or default asked for, what was done (after capability fallback and the email confidence ceiling), the rule that decided it, and the outcome (done / skipped / failed / review). Cursor-paged; filter by event, ownership, platform or outcome (outcome=review: still waiting for the seller). Kept 90 days.
        api_response = api_instance.list_event_policy_decisions(cursor=cursor, limit=limit, event=event, ownership=ownership, platform=platform, outcome=outcome)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->list_event_policy_decisions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **event** | **str**|  | [optional]
 **ownership** | **str**|  | [optional]
 **platform** | **str**|  | [optional]
 **outcome** | **str**|  | [optional]

### Return type

**ListEventPolicyDecisionsResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_detected_event_rule**
> CreateDetectedEventRuleResponse update_detected_event_rule(id, create_detected_event_rule_request)

Replace a detection rule. An id default:<key> stores your edit of that shipped default (delete it, or reset-defaults, to go back to the shipped one).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.detected.create_detected_event_rule_request import CreateDetectedEventRuleRequest
from crossly.model.detected.create_detected_event_rule_response import CreateDetectedEventRuleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    id = "id_example" # str | 
    create_detected_event_rule_request = CreateDetectedEventRuleRequest(
        name="name_example",
        enabled=True,
        order=1,
        filter={
            "key": None,
        },
        when={
            "key": None,
        },
        then=[
            {
                "key": None,
            },
        ],
        _else=[
            {
                "key": None,
            },
        ],
        _continue=True,
        allow_weak_evidence=True,
        loosen={
            "key": None,
        },
        target={
            "key": None,
        },
        candidate_pool={
            "key": None,
        },
        meta={
            "key": None,
        },
    ) # CreateDetectedEventRuleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Replace a detection rule. An id default:<key> stores your edit of that shipped default (delete it, or reset-defaults, to go back to the shipped one).
        api_response = api_instance.update_detected_event_rule(id, create_detected_event_rule_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->update_detected_event_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **create_detected_event_rule_request** | **CreateDetectedEventRuleRequest**|  |

### Return type

**CreateDetectedEventRuleResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_event_policy_rule**
> UpdateEventPolicyRuleResponse update_event_policy_rule(update_event_policy_rule_request)

Set what Crossly does with one kind of detected event for one kind of item: scope global (scopeValue null), platform (scopeValue = platform id) or app (scopeValue = OAuth app id, app_managed items only). Replaces the rule for the same cell and scope. The action must be one the matrix allows for that cell; import actions exist only for untracked items.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import activity_api
from crossly.model.common.error import Error
from crossly.model.event.update_event_policy_rule_request import UpdateEventPolicyRuleRequest
from crossly.model.event.update_event_policy_rule_response import UpdateEventPolicyRuleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://crossly.net/api
# See configuration.py for a list of all supported configuration parameters.
configuration = crossly.Configuration(
    host = "https://crossly.net/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PersonalAccessToken
configuration = crossly.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with crossly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activity_api.ActivityApi(api_client)
    update_event_policy_rule_request = UpdateEventPolicyRuleRequest(
        scope="global",
        scope_value="scope_value_example",
        event="sale",
        ownership="crossly",
        action="ignore",
    ) # UpdateEventPolicyRuleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set what Crossly does with one kind of detected event for one kind of item: scope global (scopeValue null), platform (scopeValue = platform id) or app (scopeValue = OAuth app id, app_managed items only). Replaces the rule for the same cell and scope. The action must be one the matrix allows for that cell; import actions exist only for untracked items.
        api_response = api_instance.update_event_policy_rule(update_event_policy_rule_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling ActivityApi->update_event_policy_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_event_policy_rule_request** | **UpdateEventPolicyRuleRequest**|  |

### Return type

**UpdateEventPolicyRuleResponse**

### Authorization

[PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**403** | Error |  -  |
**404** | Error |  -  |
**429** | Error |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

