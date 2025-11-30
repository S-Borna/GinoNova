"""
Phase 25 - Central Monitoring, Audit Trails & Event Bus API routes.
"""
from datetime import datetime, timedelta
from typing import Optional, List
from uuid import uuid4

from fastapi import APIRouter, Query, Response

from ..schemas.monitoring import (
    MonitoringStatus,
    Event,
    EventType,
    EventStats,
    AuditEntry,
    AuditAction,
    AuditSummary,
    SystemAlert,
    AlertType,
    AlertSeverity,
    AlertsOverview,
    EventConsumer,
    ConsumerStats,
)

monitoring_router = APIRouter(prefix="/monitoring", tags=["Monitoring"])


def add_phase_header(response: Response):
    response.headers["X-Phase"] = "25-monitoring"


# ============ Status Endpoints ============

@monitoring_router.get("/status", response_model=MonitoringStatus)
def get_monitoring_status(response: Response) -> MonitoringStatus:
    """
    Get monitoring system status.
    """
    add_phase_header(response)
    
    return MonitoringStatus(
        status="operational",
        version="25.0",
        event_bus_connected=True,
        events_per_minute=45.2,
        audit_entries_today=1250,
        active_alerts=1,
        consumers_running=6
    )


# ============ Event Bus Endpoints ============

@monitoring_router.get("/events")
def list_events(
    response: Response,
    event_type: Optional[EventType] = None,
    user_id: Optional[str] = None,
    limit: int = Query(50, le=200),
) -> list[Event]:
    """
    List recent events from the event bus.
    """
    add_phase_header(response)
    
    event_types = [
        EventType.task_completed,
        EventType.user_login,
        EventType.ai_request,
        EventType.studyflow_minute,
        EventType.module_completed,
    ]
    
    events = [
        Event(
            id=str(uuid4()),
            event_type=event_types[i % len(event_types)],
            user_id=user_id or f"user-{i % 10}",
            payload={
                "task_id": f"task-{i}",
                "duration": 30 + i * 5,
                "xp_earned": 25
            },
            timestamp=datetime.utcnow() - timedelta(minutes=i * 2),
            trace_id=f"trace-{uuid4().hex[:8]}"
        )
        for i in range(min(limit, 50))
    ]
    
    if event_type:
        events = [e for e in events if e.event_type == event_type]
    
    return events


@monitoring_router.get("/events/stats", response_model=EventStats)
def get_event_stats(
    response: Response,
    hours: int = Query(24, le=168),
) -> EventStats:
    """
    Get event statistics.
    """
    add_phase_header(response)
    
    return EventStats(
        total_events=12500,
        events_per_hour=520.8,
        by_type={
            "task.completed": 3500,
            "user.login": 850,
            "ai.request": 2200,
            "studyflow.minute": 4500,
            "module.completed": 450,
            "other": 1000
        },
        by_user={
            "user-1": 450,
            "user-2": 380,
            "user-3": 320,
            "user-4": 290,
            "user-5": 260
        }
    )


@monitoring_router.post("/events/publish")
def publish_event(
    response: Response,
    event_type: EventType,
    user_id: Optional[str] = None,
) -> Event:
    """
    Publish an event to the event bus (for testing).
    """
    add_phase_header(response)
    
    return Event(
        id=str(uuid4()),
        event_type=event_type,
        user_id=user_id,
        payload={"source": "api", "test": True},
        timestamp=datetime.utcnow(),
        trace_id=f"trace-{uuid4().hex[:8]}"
    )


# ============ Audit Trail Endpoints ============

@monitoring_router.get("/audit")
def list_audit_entries(
    response: Response,
    user_id: Optional[str] = None,
    action: Optional[AuditAction] = None,
    resource_type: Optional[str] = None,
    limit: int = Query(50, le=200),
) -> list[AuditEntry]:
    """
    List audit trail entries.
    """
    add_phase_header(response)
    
    actions = [AuditAction.create, AuditAction.update, AuditAction.read, AuditAction.login]
    resources = ["task", "module", "user", "progress", "studyflow"]
    
    entries = [
        AuditEntry(
            id=str(uuid4()),
            user_id=user_id or f"user-{i % 10}",
            action=actions[i % len(actions)],
            resource_type=resources[i % len(resources)],
            resource_id=f"res-{i}",
            changes={"field": "value", "old": "old_value", "new": "new_value"} if i % 3 == 0 else None,
            ip_address="192.168.1.100",
            user_agent="Mozilla/5.0",
            timestamp=datetime.utcnow() - timedelta(minutes=i * 3)
        )
        for i in range(min(limit, 50))
    ]
    
    if action:
        entries = [e for e in entries if e.action == action]
    if resource_type:
        entries = [e for e in entries if e.resource_type == resource_type]
    
    return entries


@monitoring_router.get("/audit/summary", response_model=AuditSummary)
def get_audit_summary(response: Response) -> AuditSummary:
    """
    Get audit summary.
    """
    add_phase_header(response)
    
    return AuditSummary(
        total_entries=45000,
        by_action={
            "create": 8500,
            "read": 25000,
            "update": 9500,
            "delete": 500,
            "login": 1500
        },
        by_resource={
            "task": 15000,
            "module": 5000,
            "progress": 12000,
            "user": 3000,
            "studyflow": 10000
        },
        recent_admin_actions=25
    )


@monitoring_router.get("/audit/admin")
def list_admin_audit(
    response: Response,
    limit: int = Query(50, le=200),
) -> list[AuditEntry]:
    """
    List admin audit entries.
    """
    add_phase_header(response)
    
    return [
        AuditEntry(
            id=str(uuid4()),
            user_id=f"user-{i}",
            admin_id="admin-1",
            action=AuditAction.admin,
            resource_type="user",
            resource_id=f"user-{i}",
            changes={"is_active": {"old": True, "new": False}},
            ip_address="10.0.0.1",
            timestamp=datetime.utcnow() - timedelta(hours=i)
        )
        for i in range(min(limit, 10))
    ]


# ============ Alerts Endpoints ============

@monitoring_router.get("/alerts")
def list_alerts(
    response: Response,
    alert_type: Optional[AlertType] = None,
    severity: Optional[AlertSeverity] = None,
    active_only: bool = Query(True),
    limit: int = Query(50, le=200),
) -> list[SystemAlert]:
    """
    List system alerts.
    """
    add_phase_header(response)
    
    alerts = [
        SystemAlert(
            id="alert-1",
            alert_type=AlertType.performance,
            severity=AlertSeverity.low,
            title="High API Latency",
            message="Average API latency above 100ms threshold",
            source="observability",
            metadata={"current_latency_ms": 120, "threshold_ms": 100},
            acknowledged=True,
            acknowledged_by="admin-1",
            acknowledged_at=datetime.utcnow() - timedelta(hours=1),
            created_at=datetime.utcnow() - timedelta(hours=2)
        ),
        SystemAlert(
            id="alert-2",
            alert_type=AlertType.cost,
            severity=AlertSeverity.info,
            title="AI Budget Warning",
            message="AI costs approaching 75% of monthly budget",
            source="finops",
            metadata={"current_percent": 72, "threshold_percent": 75},
            resolved=True,
            resolved_at=datetime.utcnow() - timedelta(hours=6),
            created_at=datetime.utcnow() - timedelta(hours=12)
        ),
    ]
    
    if active_only:
        alerts = [a for a in alerts if not a.resolved]
    if alert_type:
        alerts = [a for a in alerts if a.alert_type == alert_type]
    if severity:
        alerts = [a for a in alerts if a.severity == severity]
    
    return alerts


@monitoring_router.get("/alerts/overview", response_model=AlertsOverview)
def get_alerts_overview(response: Response) -> AlertsOverview:
    """
    Get alerts overview.
    """
    add_phase_header(response)
    
    return AlertsOverview(
        active_count=1,
        by_severity={
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 1,
            "info": 0
        },
        by_type={
            "infra": 0,
            "ai": 0,
            "cost": 0,
            "security": 0,
            "performance": 1
        },
        recent_resolved=5
    )


@monitoring_router.post("/alerts/{alert_id}/acknowledge")
def acknowledge_alert(alert_id: str, response: Response) -> SystemAlert:
    """
    Acknowledge an alert.
    """
    add_phase_header(response)
    
    return SystemAlert(
        id=alert_id,
        alert_type=AlertType.performance,
        severity=AlertSeverity.low,
        title="High API Latency",
        message="Average API latency above 100ms threshold",
        source="observability",
        acknowledged=True,
        acknowledged_by="api-user",
        acknowledged_at=datetime.utcnow(),
        created_at=datetime.utcnow() - timedelta(hours=2)
    )


@monitoring_router.post("/alerts/{alert_id}/resolve")
def resolve_alert(alert_id: str, response: Response) -> SystemAlert:
    """
    Resolve an alert.
    """
    add_phase_header(response)
    
    return SystemAlert(
        id=alert_id,
        alert_type=AlertType.performance,
        severity=AlertSeverity.low,
        title="High API Latency",
        message="Average API latency above 100ms threshold",
        source="observability",
        acknowledged=True,
        resolved=True,
        resolved_at=datetime.utcnow(),
        created_at=datetime.utcnow() - timedelta(hours=2)
    )


# ============ Consumer Endpoints ============

@monitoring_router.get("/consumers", response_model=ConsumerStats)
def get_consumer_stats(response: Response) -> ConsumerStats:
    """
    Get event consumer statistics.
    """
    add_phase_header(response)
    
    consumers = [
        EventConsumer(
            name="studyflow_consumer",
            status="running",
            events_processed=45000,
            last_event_at=datetime.utcnow() - timedelta(seconds=5),
            lag=0
        ),
        EventConsumer(
            name="ai_consumer",
            status="running",
            events_processed=22000,
            last_event_at=datetime.utcnow() - timedelta(seconds=10),
            lag=2
        ),
        EventConsumer(
            name="finops_consumer",
            status="running",
            events_processed=12500,
            last_event_at=datetime.utcnow() - timedelta(seconds=30),
            lag=0
        ),
        EventConsumer(
            name="analytics_consumer",
            status="running",
            events_processed=35000,
            last_event_at=datetime.utcnow() - timedelta(seconds=15),
            lag=5
        ),
        EventConsumer(
            name="security_consumer",
            status="running",
            events_processed=8500,
            last_event_at=datetime.utcnow() - timedelta(minutes=1),
            lag=0
        ),
        EventConsumer(
            name="notification_consumer",
            status="running",
            events_processed=15000,
            last_event_at=datetime.utcnow() - timedelta(seconds=45),
            lag=3
        ),
    ]
    
    return ConsumerStats(
        consumers=consumers,
        total_processed=sum(c.events_processed for c in consumers),
        processing_rate=520.8
    )
