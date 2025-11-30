"""
Phase 28 - Public API, Webhooks & Integration Layer schemas.
"""
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any, List
from pydantic import BaseModel


class APIKeyPermission(str, Enum):
    """API key permissions"""
    read_modules = "read:modules"
    read_tasks = "read:tasks"
    write_progress = "write:progress"
    read_ai = "read:ai"
    write_ai = "write:ai"
    read_analytics = "read:analytics"
    write_webhooks = "write:webhooks"
    admin_org = "admin:org"


class WebhookEvent(str, Enum):
    """Webhook event types"""
    user_created = "user.created"
    user_login = "user.login"
    task_completed = "task.completed"
    module_completed = "module.completed"
    studyflow_minute = "studyflow.minute"
    ai_recommendation = "ai.recommendation"
    ai_cost = "ai.cost"
    cost_event = "cost.event"
    security_alert = "security.alert"
    org_invite = "org.invite"


class DeliveryStatus(str, Enum):
    """Webhook delivery status"""
    pending = "pending"
    delivered = "delivered"
    failed = "failed"
    retrying = "retrying"


# ============ API Key Schemas ============

class APIKey(BaseModel):
    """API key"""
    id: str
    name: str
    key_prefix: str  # First 8 chars only shown
    user_id: str
    org_id: Optional[str] = None
    permissions: List[APIKeyPermission]
    rate_limit: int
    active: bool
    last_used_at: Optional[datetime] = None
    created_at: datetime
    expires_at: Optional[datetime] = None


class APIKeyCreate(BaseModel):
    """Create API key request"""
    name: str
    permissions: List[APIKeyPermission]
    expires_days: Optional[int] = None


class APIKeyCreated(BaseModel):
    """API key creation response (includes full key, shown only once)"""
    id: str
    name: str
    key: str  # Full key - show only on creation
    permissions: List[APIKeyPermission]
    created_at: datetime


class APIKeyUsage(BaseModel):
    """API key usage statistics"""
    key_id: str
    requests_today: int
    requests_this_month: int
    rate_limit: int
    rate_limit_remaining: int
    last_request_at: Optional[datetime] = None


# ============ Webhook Schemas ============

class WebhookEndpoint(BaseModel):
    """Webhook endpoint configuration"""
    id: str
    org_id: Optional[str] = None
    url: str
    description: Optional[str] = None
    event_types: List[WebhookEvent]
    active: bool
    secret_prefix: str  # First 8 chars only
    created_at: datetime


class WebhookEndpointCreate(BaseModel):
    """Create webhook endpoint request"""
    url: str
    description: Optional[str] = None
    event_types: List[WebhookEvent]


class WebhookEndpointCreated(BaseModel):
    """Webhook endpoint creation response (includes secret)"""
    id: str
    url: str
    event_types: List[WebhookEvent]
    secret: str  # Full secret - show only on creation
    created_at: datetime


class WebhookDelivery(BaseModel):
    """Webhook delivery record"""
    id: str
    endpoint_id: str
    event_type: WebhookEvent
    payload: Dict[str, Any]
    status: DeliveryStatus
    http_status: Optional[int] = None
    attempts: int
    next_retry_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    created_at: datetime


class WebhookPayload(BaseModel):
    """Webhook payload format"""
    event: WebhookEvent
    timestamp: datetime
    payload: Dict[str, Any]


# ============ Rate Limit Schemas ============

class RateLimitInfo(BaseModel):
    """Rate limit information"""
    requests_per_minute: int
    writes_per_minute: int
    ai_calls_per_day: int
    remaining_requests: int
    remaining_writes: int
    remaining_ai_calls: int
    reset_at: datetime


# ============ Public API Status Schema ============

class PublicAPIStatus(BaseModel):
    """Public API status"""
    status: str
    version: str = "28.0"
    api_version: str = "v1"
    base_url: str
    documentation_url: str
    total_api_keys: int
    total_webhooks: int
    requests_today: int


# ============ Validation Schemas ============

class APIKeyValidation(BaseModel):
    """API key validation result"""
    valid: bool
    key_id: Optional[str] = None
    user_id: Optional[str] = None
    org_id: Optional[str] = None
    permissions: List[APIKeyPermission] = []
    rate_limit_remaining: int = 0
