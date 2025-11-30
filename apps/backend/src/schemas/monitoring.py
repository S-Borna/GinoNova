"""
Phase 25 - Central Monitoring, Audit Trails & Event Bus schemas.
"""
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any, List
from pydantic import BaseModel


class EventType(str, Enum):
    """Event types for the event bus"""
    # User events
    user_login = "user.login"
    user_logout = "user.logout"
    user_created = "user.created"
    user_updated = "user.updated"

    # Learning events
    task_started = "task.started"
    task_completed = "task.completed"
    task_failed = "task.failed"
    module_started = "module.started"
    module_completed = "module.completed"

    # Studyflow events
    studyflow_started = "studyflow.started"
    studyflow_paused = "studyflow.paused"
    studyflow_completed = "studyflow.completed"
    studyflow_minute = "studyflow.minute"

    # AI events
    ai_request = "ai.request"
    ai_response = "ai.response"
    ai_error = "ai.error"

    # Admin events
    admin_action = "admin.action"
    admin_user_update = "admin.user_update"

    # System events
    system_alert = "system.alert"
    system_error = "system.error"

    # Billing events
    billing_subscription = "billing.subscription"
    billing_payment = "billing.payment"

    # Security events
    security_login_failed = "security.login_failed"
    security_rate_limit = "security.rate_limit"
    security_suspicious = "security.suspicious"


class AuditAction(str, Enum):
    """Audit action types"""
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"
    login = "login"
    logout = "logout"
    export = "export"
    admin = "admin"


class AlertType(str, Enum):
    """System alert types"""
    infra = "infra"
    ai = "ai"
    cost = "cost"
    security = "security"
    performance = "performance"


class AlertSeverity(str, Enum):
    """Alert severity levels"""
    info = "info"
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


# ============ Event Bus Schemas ============

class Event(BaseModel):
    """Event in the event bus"""
    id: str
    event_type: EventType
    user_id: Optional[str] = None
    tenant_id: Optional[str] = None
    payload: Dict[str, Any]
    timestamp: datetime
    trace_id: Optional[str] = None


class EventFilter(BaseModel):
    """Filter for querying events"""
    event_types: Optional[List[EventType]] = None
    user_id: Optional[str] = None
    tenant_id: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    limit: int = 100


class EventStats(BaseModel):
    """Event statistics"""
    total_events: int
    events_per_hour: float
    by_type: Dict[str, int]
    by_user: Dict[str, int]


# ============ Audit Trail Schemas ============

class AuditEntry(BaseModel):
    """Audit trail entry"""
    id: str
    user_id: str
    admin_id: Optional[str] = None
    action: AuditAction
    resource_type: str
    resource_id: Optional[str] = None
    changes: Optional[Dict[str, Any]] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    timestamp: datetime


class AuditFilter(BaseModel):
    """Filter for querying audit entries"""
    user_id: Optional[str] = None
    admin_id: Optional[str] = None
    action: Optional[AuditAction] = None
    resource_type: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    limit: int = 100


class AuditSummary(BaseModel):
    """Audit summary"""
    total_entries: int
    by_action: Dict[str, int]
    by_resource: Dict[str, int]
    recent_admin_actions: int


# ============ System Alert Schemas ============

class SystemAlert(BaseModel):
    """System alert"""
    id: str
    alert_type: AlertType
    severity: AlertSeverity
    title: str
    message: str
    source: str
    metadata: Optional[Dict[str, Any]] = None
    acknowledged: bool = False
    acknowledged_by: Optional[str] = None
    acknowledged_at: Optional[datetime] = None
    resolved: bool = False
    resolved_at: Optional[datetime] = None
    created_at: datetime


class AlertsOverview(BaseModel):
    """Alerts overview"""
    active_count: int
    by_severity: Dict[str, int]
    by_type: Dict[str, int]
    recent_resolved: int


# ============ Event Log Schemas ============

class EventLog(BaseModel):
    """Persistent event log"""
    id: str
    event_type: str
    payload: Dict[str, Any]
    processed: bool = False
    processed_at: Optional[datetime] = None
    created_at: datetime


# ============ Monitoring Status Schema ============

class MonitoringStatus(BaseModel):
    """Monitoring system status"""
    status: str
    version: str = "25.0"
    event_bus_connected: bool
    events_per_minute: float
    audit_entries_today: int
    active_alerts: int
    consumers_running: int


# ============ Consumer Schemas ============

class EventConsumer(BaseModel):
    """Event consumer status"""
    name: str
    status: str
    events_processed: int
    last_event_at: Optional[datetime] = None
    lag: int = 0


class ConsumerStats(BaseModel):
    """Consumer statistics"""
    consumers: List[EventConsumer]
    total_processed: int
    processing_rate: float
