
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.ai_api import AIApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from crossly.api.ai_api import AIApi
from crossly.api.account_api import AccountApi
from crossly.api.accounts_api import AccountsApi
from crossly.api.activity_api import ActivityApi
from crossly.api.ads_api import AdsApi
from crossly.api.analytics_api import AnalyticsApi
from crossly.api.automation_api import AutomationApi
from crossly.api.billing_api import BillingApi
from crossly.api.cbx_api import CBXApi
from crossly.api.catalog_api import CatalogApi
from crossly.api.comp_watchlists_api import CompWatchlistsApi
from crossly.api.connections_api import ConnectionsApi
from crossly.api.customers_api import CustomersApi
from crossly.api.embeds_api import EmbedsApi
from crossly.api.imports_api import ImportsApi
from crossly.api.inbox_api import InboxApi
from crossly.api.integrations_api import IntegrationsApi
from crossly.api.inventory_api import InventoryApi
from crossly.api.listings_api import ListingsApi
from crossly.api.magic_api import MagicApi
from crossly.api.mobile_api import MobileApi
from crossly.api.network_api import NetworkApi
from crossly.api.offers_api import OffersApi
from crossly.api.orders_api import OrdersApi
from crossly.api.pat_api import PATApi
from crossly.api.payout_api import PayoutApi
from crossly.api.policy_presets_api import PolicyPresetsApi
from crossly.api.profile_api import ProfileApi
from crossly.api.reference_api import ReferenceApi
from crossly.api.restock_prompts_api import RestockPromptsApi
from crossly.api.returns_api import ReturnsApi
from crossly.api.sales_api import SalesApi
from crossly.api.saved_views_api import SavedViewsApi
from crossly.api.sourcing_api import SourcingApi
from crossly.api.tax_api import TaxApi
from crossly.api.taxonomy_api import TaxonomyApi
from crossly.api.team_api import TeamApi
from crossly.api.templates_api import TemplatesApi
from crossly.api.webhooks_api import WebhooksApi
from crossly.api.workflows_api import WorkflowsApi
from crossly.api.default_api import DefaultApi
