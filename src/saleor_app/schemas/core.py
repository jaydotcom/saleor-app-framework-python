from enum import Enum

from pydantic import BaseModel

DomainName = str
AppToken = str
Url = str


class WebhookData(BaseModel):
    webhook_id: str
    webhook_secret_key: str


class InstallData(BaseModel):
    auth_token: str


class SaleorPermissions(str, Enum):
    MANAGE_APPS = "MANAGE_APPS"
    MANAGE_CHANNELS = "MANAGE_CHANNELS"
    MANAGE_CHECKOUTS = "MANAGE_CHECKOUTS"
    MANAGE_DISCOUNTS = "MANAGE_DISCOUNTS"
    MANAGE_GIFT_CARD = "MANAGE_GIFT_CARD"
    MANAGE_MENUS = "MANAGE_MENUS"
    MANAGE_ORDERS = "MANAGE_ORDERS"
    MANAGE_PAGE_TYPES_AND_ATTRIBUTES = "MANAGE_PAGE_TYPES_AND_ATTRIBUTES"
    MANAGE_PAGES = "MANAGE_PAGES"
    MANAGE_PLUGINS = "MANAGE_PLUGINS"
    MANAGE_PRODUCT_TYPES_AND_ATTRIBUTES = "MANAGE_PRODUCT_TYPES_AND_ATTRIBUTES"
    MANAGE_PRODUCTS = "MANAGE_PRODUCTS"
    MANAGE_SETTINGS = "MANAGE_SETTINGS"
    MANAGE_SHIPPING = "MANAGE_SHIPPING"
    MANAGE_STAFF = "MANAGE_STAFF"
    MANAGE_TRANSLATIONS = "MANAGE_TRANSLATIONS"
    MANAGE_USERS = "MANAGE_USERS"
    HANDLE_PAYMENTS = "HANDLE_PAYMENTS"
