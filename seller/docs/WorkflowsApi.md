# crossly.WorkflowsApi

All URIs are relative to *https://crossly.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](WorkflowsApi.md#create_workflow) | **POST** /v1/workflows | Create a workflow: from blank ({ name, graph? }), from a template ({ from: \&quot;template\&quot;, templateId, setup?, activate? }) or from an export document ({ from: \&quot;import\&quot;, document }). New workflows start paused; activate one with POST /v1/workflows/{id}/activate. Returns the workflow and its validation issues.
[**create_workflow_activate**](WorkflowsApi.md#create_workflow_activate) | **POST** /v1/workflows/{id}/activate | Activate a workflow: its triggers start firing. A graph with blocking issues is refused (422, details.issues).
[**create_workflow_approval_decide**](WorkflowsApi.md#create_workflow_approval_decide) | **POST** /v1/workflow-approvals/{id}/decide | Approve or reject a pending flow.approval request: the waiting run resumes down the approved or rejected port. 409 when it was already decided (another device, Telegram, or the timeout).
[**create_workflow_chain**](WorkflowsApi.md#create_workflow_chain) | **POST** /v1/workflow-chains | Create a multi-step workflow chain.
[**create_workflow_chain_run_now**](WorkflowsApi.md#create_workflow_chain_run_now) | **POST** /v1/workflow-chains/{id}/run-now | Enqueue an ad-hoc run of a workflow chain.
[**create_workflow_chain_toggle**](WorkflowsApi.md#create_workflow_chain_toggle) | **POST** /v1/workflow-chains/{id}/toggle | Flip a workflow chain between active and inactive.
[**create_workflow_deactivate**](WorkflowsApi.md#create_workflow_deactivate) | **POST** /v1/workflows/{id}/deactivate | Pause a workflow: its triggers stop firing. Runs already started finish.
[**create_workflow_duplicate**](WorkflowsApi.md#create_workflow_duplicate) | **POST** /v1/workflows/{id}/duplicate | Copy a workflow (graph, description, tags) into a new paused workflow.
[**create_workflow_expression_preview**](WorkflowsApi.md#create_workflow_expression_preview) | **POST** /v1/workflows/expressions/preview | Resolve one param value (\&quot;{{ $json.priceCents * 0.9 }}\&quot;) with the engine&#39;s evaluator against an item, the trigger item, earlier nodes&#39; items or a stored run. A bad expression is an answer (ok&#x3D;false with the message), not an HTTP error. Changes nothing.
[**create_workflow_import**](WorkflowsApi.md#create_workflow_import) | **POST** /v1/workflows/import | Import a crossly.workflow export document (or { document, name }) as a new, paused workflow. Integration and workflow references are cleared (they belong to the exporting account) and listed in stripped.
[**create_workflow_run**](WorkflowsApi.md#create_workflow_run) | **POST** /v1/workflows/{id}/run | Run a workflow (active or paused) live now, on items you pass or on selected listings / orders / inventory items (one kind per call, up to 1,000). The graph must validate (422 with issues otherwise).
[**create_workflow_run_cancel**](WorkflowsApi.md#create_workflow_run_cancel) | **POST** /v1/workflow-runs/{runId}/cancel | Cancel a queued, running or waiting run. 409 when it already finished.
[**create_workflow_run_on**](WorkflowsApi.md#create_workflow_run_on) | **POST** /v1/workflows/run-on | \&quot;Run workflow on…\&quot;: the same as POST /v1/workflows/{id}/run with the workflow named in the body.
[**create_workflow_run_retry**](WorkflowsApi.md#create_workflow_run_retry) | **POST** /v1/workflow-runs/{runId}/retry | Retry a failed run from the node that failed: a new run (retryOfRunId) seeded from the failed run&#39;s checkpoint, so nodes that succeeded are not repeated. 409 unless the run failed.
[**create_workflow_sale_end**](WorkflowsApi.md#create_workflow_sale_end) | **POST** /v1/workflows/sales/{saleEventId}/end | End a sale now. A sale that has not started is cancelled; a live one closes and every discounted price is put back now (reverted &#x3D; how many listings were restored). 404 for a sale that is not yours.
[**create_workflow_template_use**](WorkflowsApi.md#create_workflow_template_use) | **POST** /v1/workflows/templates/{id}/use | Create a workflow from a template, filling its setup fields; activate&#x3D;true activates it when it validates.
[**create_workflow_test**](WorkflowsApi.md#create_workflow_test) | **POST** /v1/workflows/{id}/test | Test a workflow (the saved graph, or a draft graph you pass). mode&#x3D;test runs it for real, using pinned data where a node has it; mode&#x3D;dry is a safe test: write, destructive and money nodes report what they would do and change nothing. Trigger items: the ones you pass, else pinned, else the last real ones, else the trigger sample.
[**create_workflow_validate**](WorkflowsApi.md#create_workflow_validate) | **POST** /v1/workflows/validate | Validate a graph without saving it: unknown node types, missing required params, bad ports, cycles, expression errors. blocking&#x3D;true means activation would be refused.
[**create_workflow_version_restore**](WorkflowsApi.md#create_workflow_version_restore) | **POST** /v1/workflows/{id}/versions/{v}/restore | Restore an earlier version&#39;s graph as a new version. Pass version (the current one you read) to refuse the restore when someone saved meanwhile (409). Body optional: { version?: integer }.
[**create_workflow_webhook_rotate**](WorkflowsApi.md#create_workflow_webhook_rotate) | **POST** /v1/workflows/{id}/webhooks/{nodeId}/rotate | Issue a new inbound URL for an on.webhook trigger node (the old one stops working). The URL, and the signing secret when withSecret&#x3D;true, are returned ONCE: store them now.
[**delete_workflow**](WorkflowsApi.md#delete_workflow) | **DELETE** /v1/workflows/{id} | Delete (archive) a workflow: its triggers stop, open runs are cancelled, run history stays readable.
[**delete_workflow_chain**](WorkflowsApi.md#delete_workflow_chain) | **DELETE** /v1/workflow-chains/{id} | Delete a workflow chain (cascades steps + runs).
[**get_workflow**](WorkflowsApi.md#get_workflow) | **GET** /v1/workflows/{id} | Get one workflow with its full graph and current version.
[**get_workflow_catalog**](WorkflowsApi.md#get_workflow_catalog) | **GET** /v1/workflows/catalog | Everything needed to build a workflow: every node type (params, ports, output fields, risk, platforms capability), which platforms each capability covers and which of those you have connected, the expression helpers and bindings ({{ $json.listingId }}…) and the condition operators. Read this before composing a graph rather than guessing node types or param keys.
[**get_workflow_chain**](WorkflowsApi.md#get_workflow_chain) | **GET** /v1/workflow-chains/{id} | Get one workflow chain with its steps.
[**get_workflow_export**](WorkflowsApi.md#get_workflow_export) | **GET** /v1/workflows/{id}/export | Export a workflow as a portable document (format crossly.workflow) that POST /v1/workflows/import accepts. Credentials and account handles are stripped; pinned test data only with pinnedData&#x3D;true.
[**get_workflow_run**](WorkflowsApi.md#get_workflow_run) | **GET** /v1/workflow-runs/{runId} | One run: its summary, the graph version it ran, and every node execution (status, item counts per port, timing, errors). Item data per node: GET …/nodes/{nodeId}.
[**get_workflow_run_node**](WorkflowsApi.md#get_workflow_run_node) | **GET** /v1/workflow-runs/{runId}/nodes/{nodeId} | Every execution of one node in a run with its input and output items (each port keeps the first 50 items, 16 KB per item; truncated&#x3D;true when cut). Data older than the retention window, or not kept by settings.saveSuccessData&#x3D;false, is pruned: that execution has input/output null and pruned&#x3D;true, and when every execution is pruned the response is { data: null, meta: { pruned: true } } (never an empty list).
[**list_workflow_approvals**](WorkflowsApi.md#list_workflow_approvals) | **GET** /v1/workflow-approvals | Approval requests from flow.approval nodes, newest first (pending only unless status says otherwise). Decide one with POST /v1/workflow-approvals/{id}/decide.
[**list_workflow_chains**](WorkflowsApi.md#list_workflow_chains) | **GET** /v1/workflow-chains | List workflow chains with their step graph.
[**list_workflow_runs**](WorkflowsApi.md#list_workflow_runs) | **GET** /v1/workflows/{id}/runs | Run history of one workflow, newest first, with per-node status and item counts.
[**list_workflow_runs2**](WorkflowsApi.md#list_workflow_runs2) | **GET** /v1/workflow-runs | Runs of every workflow, newest first. Filter by workflow, status, mode and time.
[**list_workflow_sale_active**](WorkflowsApi.md#list_workflow_sale_active) | **GET** /v1/workflows/sales/active | Every live or upcoming sale (a sales event started by a sale.start node) with the workflow that runs it: percent off, window, and how many listings it applies to.
[**list_workflow_templates**](WorkflowsApi.md#list_workflow_templates) | **GET** /v1/workflows/templates | Ready-made workflows (weekend sale, stale-listing markdowns, offer responder, ship-by alerts…), each a complete graph plus the setup fields its \&quot;use\&quot; call asks for.
[**list_workflow_versions**](WorkflowsApi.md#list_workflow_versions) | **GET** /v1/workflows/{id}/versions | The saved versions of a workflow, newest first (restore one with POST …/versions/{v}/restore).
[**list_workflows**](WorkflowsApi.md#list_workflows) | **GET** /v1/workflows | List workflows, newest change first. A workflow is a graph of nodes: one or more triggers, then actions, lookups and flow nodes (if, switch, wait, approval…). Each row carries its trigger and node types and a 7-day run sparkline, not the graph (GET /v1/workflows/{id} has it).
[**update_workflow**](WorkflowsApi.md#update_workflow) | **PUT** /v1/workflows/{id} | Save a workflow. Pass the version you edited: a save over a newer version is 409 version_conflict (re-read and merge). Saving an active workflow validates it like activation does (422 with issues).
[**update_workflow_chain**](WorkflowsApi.md#update_workflow_chain) | **PUT** /v1/workflow-chains/{id} | Replace a workflow chain wholesale.


# **create_workflow**
> CreateWorkflowResponse create_workflow(create_workflow_request)

Create a workflow: from blank ({ name, graph? }), from a template ({ from: \"template\", templateId, setup?, activate? }) or from an export document ({ from: \"import\", document }). New workflows start paused; activate one with POST /v1/workflows/{id}/activate. Returns the workflow and its validation issues.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.create_workflow_request import CreateWorkflowRequest
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_response import CreateWorkflowResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    create_workflow_request = CreateWorkflowRequest(
        _from="blank",
        name="name_example",
        description="description_example",
        tags=[
            "tags_example",
        ],
        graph={
            "key": None,
        },
        timezone="timezone_example",
        template_id="template_id_example",
        setup={
            "key": None,
        },
        activate=True,
        document={
            "key": None,
        },
    ) # CreateWorkflowRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a workflow: from blank ({ name, graph? }), from a template ({ from: \"template\", templateId, setup?, activate? }) or from an export document ({ from: \"import\", document }). New workflows start paused; activate one with POST /v1/workflows/{id}/activate. Returns the workflow and its validation issues.
        api_response = api_instance.create_workflow(create_workflow_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workflow_request** | **CreateWorkflowRequest**|  |

### Return type

**CreateWorkflowResponse**

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

# **create_workflow_activate**
> WorkflowResponse create_workflow_activate(id)

Activate a workflow: its triggers start firing. A graph with blocking issues is refused (422, details.issues).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.workflow_response import WorkflowResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.

    # example passing only required values which don't have defaults set
    try:
        # Activate a workflow: its triggers start firing. A graph with blocking issues is refused (422, details.issues).
        api_response = api_instance.create_workflow_activate(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_activate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |

### Return type

**WorkflowResponse**

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

# **create_workflow_approval_decide**
> CreateWorkflowApprovalDecideResponse create_workflow_approval_decide(id, create_workflow_approval_decide_request)

Approve or reject a pending flow.approval request: the waiting run resumes down the approved or rejected port. 409 when it was already decided (another device, Telegram, or the timeout).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_approval_decide_response import CreateWorkflowApprovalDecideResponse
from crossly.model.workflow.create_workflow_approval_decide_request import CreateWorkflowApprovalDecideRequest
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Approval id from GET /v1/workflow-approvals.
    create_workflow_approval_decide_request = CreateWorkflowApprovalDecideRequest(
        decision="approved",
        note="note_example",
    ) # CreateWorkflowApprovalDecideRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Approve or reject a pending flow.approval request: the waiting run resumes down the approved or rejected port. 409 when it was already decided (another device, Telegram, or the timeout).
        api_response = api_instance.create_workflow_approval_decide(id, create_workflow_approval_decide_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_approval_decide: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Approval id from GET /v1/workflow-approvals. |
 **create_workflow_approval_decide_request** | **CreateWorkflowApprovalDecideRequest**|  |

### Return type

**CreateWorkflowApprovalDecideResponse**

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

# **create_workflow_chain**
> IdResponse create_workflow_chain()

Create a multi-step workflow chain.

Deprecated: workflow chains are workflows now. Use /v1/workflows.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.id_response import IdResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a multi-step workflow chain.
        api_response = api_instance.create_workflow_chain()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_chain: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**IdResponse**

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

# **create_workflow_chain_run_now**
> CreateWorkflowChainRunNowResponse create_workflow_chain_run_now(id)

Enqueue an ad-hoc run of a workflow chain.

Deprecated: workflow chains are workflows now. Use /v1/workflows.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_chain_run_now_response import CreateWorkflowChainRunNowResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Enqueue an ad-hoc run of a workflow chain.
        api_response = api_instance.create_workflow_chain_run_now(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_chain_run_now: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorkflowChainRunNowResponse**

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

# **create_workflow_chain_toggle**
> CreateWorkflowChainToggleResponse create_workflow_chain_toggle(id)

Flip a workflow chain between active and inactive.

Deprecated: workflow chains are workflows now. Use /v1/workflows.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_chain_toggle_response import CreateWorkflowChainToggleResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Flip a workflow chain between active and inactive.
        api_response = api_instance.create_workflow_chain_toggle(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_chain_toggle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**CreateWorkflowChainToggleResponse**

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

# **create_workflow_deactivate**
> WorkflowResponse create_workflow_deactivate(id)

Pause a workflow: its triggers stop firing. Runs already started finish.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.workflow_response import WorkflowResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.

    # example passing only required values which don't have defaults set
    try:
        # Pause a workflow: its triggers stop firing. Runs already started finish.
        api_response = api_instance.create_workflow_deactivate(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_deactivate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |

### Return type

**WorkflowResponse**

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

# **create_workflow_duplicate**
> CreateWorkflowDuplicateResponse create_workflow_duplicate(id, create_workflow_duplicate_request)

Copy a workflow (graph, description, tags) into a new paused workflow.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.create_workflow_duplicate_request import CreateWorkflowDuplicateRequest
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_duplicate_response import CreateWorkflowDuplicateResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.
    create_workflow_duplicate_request = CreateWorkflowDuplicateRequest(
        name="name_example",
    ) # CreateWorkflowDuplicateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Copy a workflow (graph, description, tags) into a new paused workflow.
        api_response = api_instance.create_workflow_duplicate(id, create_workflow_duplicate_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_duplicate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |
 **create_workflow_duplicate_request** | **CreateWorkflowDuplicateRequest**|  |

### Return type

**CreateWorkflowDuplicateResponse**

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

# **create_workflow_expression_preview**
> CreateWorkflowExpressionPreviewResponse create_workflow_expression_preview(create_workflow_expression_preview_request)

Resolve one param value (\"{{ $json.priceCents * 0.9 }}\") with the engine's evaluator against an item, the trigger item, earlier nodes' items or a stored run. A bad expression is an answer (ok=false with the message), not an HTTP error. Changes nothing.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.create_workflow_expression_preview_request import CreateWorkflowExpressionPreviewRequest
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_expression_preview_response import CreateWorkflowExpressionPreviewResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    create_workflow_expression_preview_request = CreateWorkflowExpressionPreviewRequest(
        value=None,
        item={
            "key": None,
        },
        trigger={
            "key": None,
        },
        nodes={
            "key": None,
        },
        run_id="run_id_example",
        workflow_id="workflow_id_example",
        item_index=0,
        vars={
            "key": None,
        },
        timezone="timezone_example",
    ) # CreateWorkflowExpressionPreviewRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Resolve one param value (\"{{ $json.priceCents * 0.9 }}\") with the engine's evaluator against an item, the trigger item, earlier nodes' items or a stored run. A bad expression is an answer (ok=false with the message), not an HTTP error. Changes nothing.
        api_response = api_instance.create_workflow_expression_preview(create_workflow_expression_preview_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_expression_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workflow_expression_preview_request** | **CreateWorkflowExpressionPreviewRequest**|  |

### Return type

**CreateWorkflowExpressionPreviewResponse**

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

# **create_workflow_import**
> CreateWorkflowImportResponse create_workflow_import(request_body)

Import a crossly.workflow export document (or { document, name }) as a new, paused workflow. Integration and workflow references are cleared (they belong to the exporting account) and listed in stripped.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.create_workflow_import_response import CreateWorkflowImportResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    request_body = {
        "key": None,
    } # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        # Import a crossly.workflow export document (or { document, name }) as a new, paused workflow. Integration and workflow references are cleared (they belong to the exporting account) and listed in stripped.
        api_response = api_instance.create_workflow_import(request_body)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_import: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

**CreateWorkflowImportResponse**

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

# **create_workflow_run**
> CreateWorkflowRunResponse create_workflow_run(id, create_workflow_run_request)

Run a workflow (active or paused) live now, on items you pass or on selected listings / orders / inventory items (one kind per call, up to 1,000). The graph must validate (422 with issues otherwise).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.create_workflow_run_response import CreateWorkflowRunResponse
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_run_request import CreateWorkflowRunRequest
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.
    create_workflow_run_request = CreateWorkflowRunRequest(
        items=[
            CreateWorkflowRunOnRequestItems(
                json={
                    "key": None,
                },
            ),
        ],
        listing_ids=[
            "listing_ids_example",
        ],
        order_ids=[
            "order_ids_example",
        ],
        inventory_item_ids=[
            "inventory_item_ids_example",
        ],
        trigger_node_id="trigger_node_id_example",
    ) # CreateWorkflowRunRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Run a workflow (active or paused) live now, on items you pass or on selected listings / orders / inventory items (one kind per call, up to 1,000). The graph must validate (422 with issues otherwise).
        api_response = api_instance.create_workflow_run(id, create_workflow_run_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |
 **create_workflow_run_request** | **CreateWorkflowRunRequest**|  |

### Return type

**CreateWorkflowRunResponse**

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

# **create_workflow_run_cancel**
> CreateWorkflowRunCancelResponse create_workflow_run_cancel(run_id)

Cancel a queued, running or waiting run. 409 when it already finished.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.create_workflow_run_cancel_response import CreateWorkflowRunCancelResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    run_id = "runId_example" # str | Workflow run id.

    # example passing only required values which don't have defaults set
    try:
        # Cancel a queued, running or waiting run. 409 when it already finished.
        api_response = api_instance.create_workflow_run_cancel(run_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_run_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Workflow run id. |

### Return type

**CreateWorkflowRunCancelResponse**

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

# **create_workflow_run_on**
> CreateWorkflowRunOnResponse create_workflow_run_on(create_workflow_run_on_request)

\"Run workflow on…\": the same as POST /v1/workflows/{id}/run with the workflow named in the body.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.create_workflow_run_on_response import CreateWorkflowRunOnResponse
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_run_on_request import CreateWorkflowRunOnRequest
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    create_workflow_run_on_request = CreateWorkflowRunOnRequest(
        workflow_id="workflow_id_example",
        items=[
            CreateWorkflowRunOnRequestItems(
                json={
                    "key": None,
                },
            ),
        ],
        listing_ids=[
            "listing_ids_example",
        ],
        order_ids=[
            "order_ids_example",
        ],
        inventory_item_ids=[
            "inventory_item_ids_example",
        ],
        trigger_node_id="trigger_node_id_example",
    ) # CreateWorkflowRunOnRequest | 

    # example passing only required values which don't have defaults set
    try:
        # \"Run workflow on…\": the same as POST /v1/workflows/{id}/run with the workflow named in the body.
        api_response = api_instance.create_workflow_run_on(create_workflow_run_on_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_run_on: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workflow_run_on_request** | **CreateWorkflowRunOnRequest**|  |

### Return type

**CreateWorkflowRunOnResponse**

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

# **create_workflow_run_retry**
> CreateWorkflowRunRetryResponse create_workflow_run_retry(run_id)

Retry a failed run from the node that failed: a new run (retryOfRunId) seeded from the failed run's checkpoint, so nodes that succeeded are not repeated. 409 unless the run failed.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_run_retry_response import CreateWorkflowRunRetryResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    run_id = "runId_example" # str | Workflow run id.

    # example passing only required values which don't have defaults set
    try:
        # Retry a failed run from the node that failed: a new run (retryOfRunId) seeded from the failed run's checkpoint, so nodes that succeeded are not repeated. 409 unless the run failed.
        api_response = api_instance.create_workflow_run_retry(run_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_run_retry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Workflow run id. |

### Return type

**CreateWorkflowRunRetryResponse**

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

# **create_workflow_sale_end**
> CreateWorkflowSaleEndResponse create_workflow_sale_end(sale_event_id)

End a sale now. A sale that has not started is cancelled; a live one closes and every discounted price is put back now (reverted = how many listings were restored). 404 for a sale that is not yours.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_sale_end_response import CreateWorkflowSaleEndResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    sale_event_id = "saleEventId_example" # str | Sale id from GET /v1/workflows/sales/active.

    # example passing only required values which don't have defaults set
    try:
        # End a sale now. A sale that has not started is cancelled; a live one closes and every discounted price is put back now (reverted = how many listings were restored). 404 for a sale that is not yours.
        api_response = api_instance.create_workflow_sale_end(sale_event_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_sale_end: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sale_event_id** | **str**| Sale id from GET /v1/workflows/sales/active. |

### Return type

**CreateWorkflowSaleEndResponse**

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

# **create_workflow_template_use**
> CreateWorkflowResponse create_workflow_template_use(id, create_workflow_template_use_request)

Create a workflow from a template, filling its setup fields; activate=true activates it when it validates.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_response import CreateWorkflowResponse
from crossly.model.workflow.create_workflow_template_use_request import CreateWorkflowTemplateUseRequest
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Template id from GET /v1/workflows/templates.
    create_workflow_template_use_request = CreateWorkflowTemplateUseRequest(
        setup={
            "key": None,
        },
        name="name_example",
        activate=True,
    ) # CreateWorkflowTemplateUseRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a workflow from a template, filling its setup fields; activate=true activates it when it validates.
        api_response = api_instance.create_workflow_template_use(id, create_workflow_template_use_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_template_use: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id from GET /v1/workflows/templates. |
 **create_workflow_template_use_request** | **CreateWorkflowTemplateUseRequest**|  |

### Return type

**CreateWorkflowResponse**

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

# **create_workflow_test**
> CreateWorkflowTestResponse create_workflow_test(id, create_workflow_test_request)

Test a workflow (the saved graph, or a draft graph you pass). mode=test runs it for real, using pinned data where a node has it; mode=dry is a safe test: write, destructive and money nodes report what they would do and change nothing. Trigger items: the ones you pass, else pinned, else the last real ones, else the trigger sample.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.create_workflow_test_response import CreateWorkflowTestResponse
from crossly.model.workflow.create_workflow_test_request import CreateWorkflowTestRequest
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.
    create_workflow_test_request = CreateWorkflowTestRequest(
        graph={
            "key": None,
        },
        mode="test",
        trigger_node_id="trigger_node_id_example",
        start_node_id="start_node_id_example",
        stop_after_node_id="stop_after_node_id_example",
        trigger_items=[
            CreateWorkflowRunOnRequestItems(
                json={
                    "key": None,
                },
            ),
        ],
    ) # CreateWorkflowTestRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Test a workflow (the saved graph, or a draft graph you pass). mode=test runs it for real, using pinned data where a node has it; mode=dry is a safe test: write, destructive and money nodes report what they would do and change nothing. Trigger items: the ones you pass, else pinned, else the last real ones, else the trigger sample.
        api_response = api_instance.create_workflow_test(id, create_workflow_test_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |
 **create_workflow_test_request** | **CreateWorkflowTestRequest**|  |

### Return type

**CreateWorkflowTestResponse**

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

# **create_workflow_validate**
> CreateWorkflowValidateResponse create_workflow_validate(create_workflow_validate_request)

Validate a graph without saving it: unknown node types, missing required params, bad ports, cycles, expression errors. blocking=true means activation would be refused.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_validate_request import CreateWorkflowValidateRequest
from crossly.model.workflow.create_workflow_validate_response import CreateWorkflowValidateResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    create_workflow_validate_request = CreateWorkflowValidateRequest(
        graph={
            "key": None,
        },
    ) # CreateWorkflowValidateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Validate a graph without saving it: unknown node types, missing required params, bad ports, cycles, expression errors. blocking=true means activation would be refused.
        api_response = api_instance.create_workflow_validate(create_workflow_validate_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_validate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workflow_validate_request** | **CreateWorkflowValidateRequest**|  |

### Return type

**CreateWorkflowValidateResponse**

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

# **create_workflow_version_restore**
> WorkflowResponse create_workflow_version_restore(id, v)

Restore an earlier version's graph as a new version. Pass version (the current one you read) to refuse the restore when someone saved meanwhile (409). Body optional: { version?: integer }.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.workflow_response import WorkflowResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.
    v = 1 # int | The version number to restore.

    # example passing only required values which don't have defaults set
    try:
        # Restore an earlier version's graph as a new version. Pass version (the current one you read) to refuse the restore when someone saved meanwhile (409). Body optional: { version?: integer }.
        api_response = api_instance.create_workflow_version_restore(id, v)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_version_restore: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |
 **v** | **int**| The version number to restore. |

### Return type

**WorkflowResponse**

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

# **create_workflow_webhook_rotate**
> CreateWorkflowWebhookRotateResponse create_workflow_webhook_rotate(id, node_id, create_workflow_webhook_rotate_request)

Issue a new inbound URL for an on.webhook trigger node (the old one stops working). The URL, and the signing secret when withSecret=true, are returned ONCE: store them now.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.create_workflow_webhook_rotate_response import CreateWorkflowWebhookRotateResponse
from crossly.model.common.error import Error
from crossly.model.workflow.create_workflow_webhook_rotate_request import CreateWorkflowWebhookRotateRequest
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.
    node_id = "nodeId_example" # str | The on.webhook trigger node id.
    create_workflow_webhook_rotate_request = CreateWorkflowWebhookRotateRequest(
        with_secret=False,
    ) # CreateWorkflowWebhookRotateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Issue a new inbound URL for an on.webhook trigger node (the old one stops working). The URL, and the signing secret when withSecret=true, are returned ONCE: store them now.
        api_response = api_instance.create_workflow_webhook_rotate(id, node_id, create_workflow_webhook_rotate_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->create_workflow_webhook_rotate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |
 **node_id** | **str**| The on.webhook trigger node id. |
 **create_workflow_webhook_rotate_request** | **CreateWorkflowWebhookRotateRequest**|  |

### Return type

**CreateWorkflowWebhookRotateResponse**

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

# **delete_workflow**
> DeleteWorkflowResponse delete_workflow(id)

Delete (archive) a workflow: its triggers stop, open runs are cancelled, run history stays readable.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.delete_workflow_response import DeleteWorkflowResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.

    # example passing only required values which don't have defaults set
    try:
        # Delete (archive) a workflow: its triggers stop, open runs are cancelled, run history stays readable.
        api_response = api_instance.delete_workflow(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->delete_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |

### Return type

**DeleteWorkflowResponse**

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

# **delete_workflow_chain**
> OkResponse delete_workflow_chain(id)

Delete a workflow chain (cascades steps + runs).

Deprecated: workflow chains are workflows now. Use /v1/workflows.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.ok_response import OkResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a workflow chain (cascades steps + runs).
        api_response = api_instance.delete_workflow_chain(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->delete_workflow_chain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**OkResponse**

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

# **get_workflow**
> GetWorkflowResponse get_workflow(id)

Get one workflow with its full graph and current version.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.get_workflow_response import GetWorkflowResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.

    # example passing only required values which don't have defaults set
    try:
        # Get one workflow with its full graph and current version.
        api_response = api_instance.get_workflow(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |

### Return type

**GetWorkflowResponse**

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

# **get_workflow_catalog**
> GetWorkflowCatalogResponse get_workflow_catalog()

Everything needed to build a workflow: every node type (params, ports, output fields, risk, platforms capability), which platforms each capability covers and which of those you have connected, the expression helpers and bindings ({{ $json.listingId }}…) and the condition operators. Read this before composing a graph rather than guessing node types or param keys.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.get_workflow_catalog_response import GetWorkflowCatalogResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Everything needed to build a workflow: every node type (params, ports, output fields, risk, platforms capability), which platforms each capability covers and which of those you have connected, the expression helpers and bindings ({{ $json.listingId }}…) and the condition operators. Read this before composing a graph rather than guessing node types or param keys.
        api_response = api_instance.get_workflow_catalog()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow_catalog: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**GetWorkflowCatalogResponse**

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

# **get_workflow_chain**
> GetWorkflowChainResponse get_workflow_chain(id)

Get one workflow chain with its steps.

Deprecated: workflow chains are workflows now. Use /v1/workflows.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.get_workflow_chain_response import GetWorkflowChainResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get one workflow chain with its steps.
        api_response = api_instance.get_workflow_chain(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow_chain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**GetWorkflowChainResponse**

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

# **get_workflow_export**
> GetWorkflowExportResponse get_workflow_export(id)

Export a workflow as a portable document (format crossly.workflow) that POST /v1/workflows/import accepts. Credentials and account handles are stripped; pinned test data only with pinnedData=true.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.get_workflow_export_response import GetWorkflowExportResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.
    pinned_data = "true" # str | Keep the nodes' pinned test data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export a workflow as a portable document (format crossly.workflow) that POST /v1/workflows/import accepts. Credentials and account handles are stripped; pinned test data only with pinnedData=true.
        api_response = api_instance.get_workflow_export(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow_export: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export a workflow as a portable document (format crossly.workflow) that POST /v1/workflows/import accepts. Credentials and account handles are stripped; pinned test data only with pinnedData=true.
        api_response = api_instance.get_workflow_export(id, pinned_data=pinned_data)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |
 **pinned_data** | **str**| Keep the nodes&#39; pinned test data. | [optional]

### Return type

**GetWorkflowExportResponse**

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

# **get_workflow_run**
> GetWorkflowRunResponse get_workflow_run(run_id)

One run: its summary, the graph version it ran, and every node execution (status, item counts per port, timing, errors). Item data per node: GET …/nodes/{nodeId}.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.get_workflow_run_response import GetWorkflowRunResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    run_id = "runId_example" # str | Workflow run id.

    # example passing only required values which don't have defaults set
    try:
        # One run: its summary, the graph version it ran, and every node execution (status, item counts per port, timing, errors). Item data per node: GET …/nodes/{nodeId}.
        api_response = api_instance.get_workflow_run(run_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Workflow run id. |

### Return type

**GetWorkflowRunResponse**

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

# **get_workflow_run_node**
> GetWorkflowRunNodeResponse get_workflow_run_node(run_id, node_id)

Every execution of one node in a run with its input and output items (each port keeps the first 50 items, 16 KB per item; truncated=true when cut). Data older than the retention window, or not kept by settings.saveSuccessData=false, is pruned: that execution has input/output null and pruned=true, and when every execution is pruned the response is { data: null, meta: { pruned: true } } (never an empty list).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.get_workflow_run_node_response import GetWorkflowRunNodeResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    run_id = "runId_example" # str | Workflow run id.
    node_id = "nodeId_example" # str | Node id within the run's graph.

    # example passing only required values which don't have defaults set
    try:
        # Every execution of one node in a run with its input and output items (each port keeps the first 50 items, 16 KB per item; truncated=true when cut). Data older than the retention window, or not kept by settings.saveSuccessData=false, is pruned: that execution has input/output null and pruned=true, and when every execution is pruned the response is { data: null, meta: { pruned: true } } (never an empty list).
        api_response = api_instance.get_workflow_run_node(run_id, node_id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow_run_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Workflow run id. |
 **node_id** | **str**| Node id within the run&#39;s graph. |

### Return type

**GetWorkflowRunNodeResponse**

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

# **list_workflow_approvals**
> ListWorkflowApprovalsResponse list_workflow_approvals()

Approval requests from flow.approval nodes, newest first (pending only unless status says otherwise). Decide one with POST /v1/workflow-approvals/{id}/decide.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.list_workflow_approvals_response import ListWorkflowApprovalsResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    status = "status_example" # str | Comma-separated: pending, approved, rejected, expired. Default pending. (optional)
    workflow_id = "workflowId_example" # str | Only approvals of this workflow. (optional)
    page = 1 # int | 1-indexed page. (optional) if omitted the server will use the default value of 1
    limit = 25 # int | Rows per page (1-100). (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Approval requests from flow.approval nodes, newest first (pending only unless status says otherwise). Decide one with POST /v1/workflow-approvals/{id}/decide.
        api_response = api_instance.list_workflow_approvals(status=status, workflow_id=workflow_id, page=page, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflow_approvals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Comma-separated: pending, approved, rejected, expired. Default pending. | [optional]
 **workflow_id** | **str**| Only approvals of this workflow. | [optional]
 **page** | **int**| 1-indexed page. | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Rows per page (1-100). | [optional] if omitted the server will use the default value of 25

### Return type

**ListWorkflowApprovalsResponse**

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

# **list_workflow_chains**
> ListWorkflowChainsResponse list_workflow_chains()

List workflow chains with their step graph.

Deprecated: workflow chains are workflows now. Use /v1/workflows.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.list_workflow_chains_response import ListWorkflowChainsResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List workflow chains with their step graph.
        api_response = api_instance.list_workflow_chains()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflow_chains: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorkflowChainsResponse**

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

# **list_workflow_runs**
> ListWorkflowRunsResponse list_workflow_runs(id)

Run history of one workflow, newest first, with per-node status and item counts.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.list_workflow_runs_response import ListWorkflowRunsResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.
    status = "status_example" # str | Comma-separated run statuses: queued, running, waiting, succeeded, failed, cancelled. (optional)
    mode = "live" # str | live (triggers), test (editor test run) or dry (safe test: no writes). (optional)
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Runs queued at or after this time (ISO 8601). (optional)
    until = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Runs queued at or before this time (ISO 8601). (optional)
    page = 1 # int | 1-indexed page. (optional) if omitted the server will use the default value of 1
    limit = 25 # int | Rows per page (1-100). (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Run history of one workflow, newest first, with per-node status and item counts.
        api_response = api_instance.list_workflow_runs(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflow_runs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Run history of one workflow, newest first, with per-node status and item counts.
        api_response = api_instance.list_workflow_runs(id, status=status, mode=mode, since=since, until=until, page=page, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflow_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |
 **status** | **str**| Comma-separated run statuses: queued, running, waiting, succeeded, failed, cancelled. | [optional]
 **mode** | **str**| live (triggers), test (editor test run) or dry (safe test: no writes). | [optional]
 **since** | **datetime**| Runs queued at or after this time (ISO 8601). | [optional]
 **until** | **datetime**| Runs queued at or before this time (ISO 8601). | [optional]
 **page** | **int**| 1-indexed page. | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Rows per page (1-100). | [optional] if omitted the server will use the default value of 25

### Return type

**ListWorkflowRunsResponse**

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

# **list_workflow_runs2**
> ListWorkflowRunsResponse list_workflow_runs2()

Runs of every workflow, newest first. Filter by workflow, status, mode and time.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.list_workflow_runs_response import ListWorkflowRunsResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    workflow_id = "workflowId_example" # str | Only runs of this workflow. (optional)
    status = "status_example" # str | Comma-separated run statuses: queued, running, waiting, succeeded, failed, cancelled. (optional)
    mode = "live" # str | live (triggers), test (editor test run) or dry (safe test: no writes). (optional)
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Runs queued at or after this time (ISO 8601). (optional)
    until = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Runs queued at or before this time (ISO 8601). (optional)
    page = 1 # int | 1-indexed page. (optional) if omitted the server will use the default value of 1
    limit = 25 # int | Rows per page (1-100). (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Runs of every workflow, newest first. Filter by workflow, status, mode and time.
        api_response = api_instance.list_workflow_runs2(workflow_id=workflow_id, status=status, mode=mode, since=since, until=until, page=page, limit=limit)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflow_runs2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| Only runs of this workflow. | [optional]
 **status** | **str**| Comma-separated run statuses: queued, running, waiting, succeeded, failed, cancelled. | [optional]
 **mode** | **str**| live (triggers), test (editor test run) or dry (safe test: no writes). | [optional]
 **since** | **datetime**| Runs queued at or after this time (ISO 8601). | [optional]
 **until** | **datetime**| Runs queued at or before this time (ISO 8601). | [optional]
 **page** | **int**| 1-indexed page. | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Rows per page (1-100). | [optional] if omitted the server will use the default value of 25

### Return type

**ListWorkflowRunsResponse**

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

# **list_workflow_sale_active**
> ListWorkflowSaleActiveResponse list_workflow_sale_active()

Every live or upcoming sale (a sales event started by a sale.start node) with the workflow that runs it: percent off, window, and how many listings it applies to.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.list_workflow_sale_active_response import ListWorkflowSaleActiveResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Every live or upcoming sale (a sales event started by a sale.start node) with the workflow that runs it: percent off, window, and how many listings it applies to.
        api_response = api_instance.list_workflow_sale_active()
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflow_sale_active: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**ListWorkflowSaleActiveResponse**

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

# **list_workflow_templates**
> ListWorkflowTemplatesResponse list_workflow_templates()

Ready-made workflows (weekend sale, stale-listing markdowns, offer responder, ship-by alerts…), each a complete graph plus the setup fields its \"use\" call asks for.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.error import Error
from crossly.model.workflow.list_workflow_templates_response import ListWorkflowTemplatesResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    category = "category_example" # str | Exact template category, e.g. \"Sales & markdowns\". (optional)
    q = "q_example" # str | Matches name, description, category or tags. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ready-made workflows (weekend sale, stale-listing markdowns, offer responder, ship-by alerts…), each a complete graph plus the setup fields its \"use\" call asks for.
        api_response = api_instance.list_workflow_templates(category=category, q=q)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflow_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Exact template category, e.g. \&quot;Sales &amp; markdowns\&quot;. | [optional]
 **q** | **str**| Matches name, description, category or tags. | [optional]

### Return type

**ListWorkflowTemplatesResponse**

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

# **list_workflow_versions**
> ListWorkflowVersionsResponse list_workflow_versions(id)

The saved versions of a workflow, newest first (restore one with POST …/versions/{v}/restore).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.list_workflow_versions_response import ListWorkflowVersionsResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.

    # example passing only required values which don't have defaults set
    try:
        # The saved versions of a workflow, newest first (restore one with POST …/versions/{v}/restore).
        api_response = api_instance.list_workflow_versions(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflow_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |

### Return type

**ListWorkflowVersionsResponse**

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

# **list_workflows**
> ListWorkflowsResponse list_workflows()

List workflows, newest change first. A workflow is a graph of nodes: one or more triggers, then actions, lookups and flow nodes (if, switch, wait, approval…). Each row carries its trigger and node types and a 7-day run sparkline, not the graph (GET /v1/workflows/{id} has it).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.workflow.list_workflows_response import ListWorkflowsResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    active = "true" # str | Only active (true) or paused (false) workflows. (optional)
    tag = "tag_example" # str | Only workflows carrying this tag. (optional)
    trigger = "trigger_example" # str | Only workflows started by this trigger node type, e.g. on.listing.sold. (optional)
    q = "q_example" # str | Name contains (case-insensitive). (optional)
    legacy_ref = "legacyRef_example" # str | The workflow an old automation became: rule:<id>, chain:<id> or sale_event:<id>. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List workflows, newest change first. A workflow is a graph of nodes: one or more triggers, then actions, lookups and flow nodes (if, switch, wait, approval…). Each row carries its trigger and node types and a 7-day run sparkline, not the graph (GET /v1/workflows/{id} has it).
        api_response = api_instance.list_workflows(active=active, tag=tag, trigger=trigger, q=q, legacy_ref=legacy_ref)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->list_workflows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **str**| Only active (true) or paused (false) workflows. | [optional]
 **tag** | **str**| Only workflows carrying this tag. | [optional]
 **trigger** | **str**| Only workflows started by this trigger node type, e.g. on.listing.sold. | [optional]
 **q** | **str**| Name contains (case-insensitive). | [optional]
 **legacy_ref** | **str**| The workflow an old automation became: rule:&lt;id&gt;, chain:&lt;id&gt; or sale_event:&lt;id&gt;. | [optional]

### Return type

**ListWorkflowsResponse**

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

# **update_workflow**
> WorkflowResponse update_workflow(id, update_workflow_request)

Save a workflow. Pass the version you edited: a save over a newer version is 409 version_conflict (re-read and merge). Saving an active workflow validates it like activation does (422 with issues).

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.workflow_response import WorkflowResponse
from crossly.model.common.error import Error
from crossly.model.workflow.update_workflow_request import UpdateWorkflowRequest
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | Workflow id.
    update_workflow_request = UpdateWorkflowRequest(
        version=1,
        name="name_example",
        description="description_example",
        tags=[
            "tags_example",
        ],
        graph={
            "key": None,
        },
    ) # UpdateWorkflowRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Save a workflow. Pass the version you edited: a save over a newer version is 409 version_conflict (re-read and merge). Saving an active workflow validates it like activation does (422 with issues).
        api_response = api_instance.update_workflow(id, update_workflow_request)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->update_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workflow id. |
 **update_workflow_request** | **UpdateWorkflowRequest**|  |

### Return type

**WorkflowResponse**

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

# **update_workflow_chain**
> OkResponse update_workflow_chain(id)

Replace a workflow chain wholesale.

Deprecated: workflow chains are workflows now. Use /v1/workflows.

### Example

* Bearer Authentication (PersonalAccessToken):

```python
import time
import crossly
from crossly.api import workflows_api
from crossly.model.common.ok_response import OkResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Replace a workflow chain wholesale.
        api_response = api_instance.update_workflow_chain(id)
        pprint(api_response)
    except crossly.ApiException as e:
        print("Exception when calling WorkflowsApi->update_workflow_chain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**OkResponse**

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

