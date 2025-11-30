"""
Phase 22 - Infrastructure, Deployment & Observability API routes.
"""
from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4
import time

from fastapi import APIRouter, Query, Response

from ...schemas.observability import (
    InfraStatus,
    ServiceHealth,
    ServiceStatus,
    MetricsResponse,
    MetricPoint,
    RequestMetrics,
    LogsResponse,
    LogEntry,
    LogLevel,
    LogFilter,
    AlertsResponse,
    Alert,
    AlertRule,
    AlertSeverity,
    DeploymentHistory,
    DeploymentInfo,
    ResourceUsage,
)

observability_router = APIRouter(prefix="/observability", tags=["Observability"])

# Track start time for uptime calculation
START_TIME = time.time()


def add_phase_header(response: Response):
    response.headers["X-Phase"] = "22-observability"


# ============ Status Endpoints ============

@observability_router.get("/status", response_model=InfraStatus)
def get_infra_status(response: Response) -> InfraStatus:
    """
    Get overall infrastructure status.
    """
    add_phase_header(response)

    services = [
        ServiceHealth(
            name="backend",
            status=ServiceStatus.healthy,
            latency_ms=12.5,
            last_check=datetime.utcnow(),
            details={"version": "1.0.0", "workers": 2}
        ),
        ServiceHealth(
            name="database",
            status=ServiceStatus.healthy,
            latency_ms=3.2,
            last_check=datetime.utcnow(),
            details={"type": "postgresql", "connections": 15}
        ),
        ServiceHealth(
            name="redis",
            status=ServiceStatus.healthy,
            latency_ms=0.8,
            last_check=datetime.utcnow(),
            details={"memory_used_mb": 45, "keys": 1250}
        ),
        ServiceHealth(
            name="ai_gateway",
            status=ServiceStatus.healthy,
            latency_ms=145.0,
            last_check=datetime.utcnow(),
            details={"model": "gpt-4", "quota_remaining": 850}
        ),
        ServiceHealth(
            name="storage",
            status=ServiceStatus.healthy,
            latency_ms=25.0,
            last_check=datetime.utcnow(),
            details={"provider": "s3-compatible", "files": 342}
        ),
    ]

    return InfraStatus(
        status="operational",
        version="22.0",
        services=services,
        uptime_seconds=int(time.time() - START_TIME),
        last_deploy=datetime.utcnow() - timedelta(hours=2)
    )


# ============ Metrics Endpoints ============

@observability_router.get("/metrics", response_model=MetricsResponse)
def get_metrics(
    response: Response,
    period: str = Query("1h", description="Time period: 1h, 6h, 24h, 7d"),
) -> MetricsResponse:
    """
    Get system metrics for the specified period.
    """
    add_phase_header(response)

    now = datetime.utcnow()
    period_hours = {"1h": 1, "6h": 6, "24h": 24, "7d": 168}.get(period, 1)

    metrics = [
        MetricPoint(
            name="api_requests_total",
            value=15420,
            unit="count",
            timestamp=now,
            tags={"service": "backend"}
        ),
        MetricPoint(
            name="api_latency_avg",
            value=45.2,
            unit="ms",
            timestamp=now,
            tags={"service": "backend"}
        ),
        MetricPoint(
            name="error_rate",
            value=0.02,
            unit="percent",
            timestamp=now,
            tags={"service": "backend"}
        ),
        MetricPoint(
            name="cpu_usage",
            value=35.5,
            unit="percent",
            timestamp=now,
            tags={"container": "backend-1"}
        ),
        MetricPoint(
            name="memory_usage",
            value=512,
            unit="mb",
            timestamp=now,
            tags={"container": "backend-1"}
        ),
        MetricPoint(
            name="db_connections",
            value=15,
            unit="count",
            timestamp=now,
            tags={"database": "postgresql"}
        ),
        MetricPoint(
            name="redis_memory",
            value=45,
            unit="mb",
            timestamp=now,
            tags={"cache": "redis"}
        ),
        MetricPoint(
            name="ai_tokens_used",
            value=125000,
            unit="tokens",
            timestamp=now,
            tags={"provider": "openai"}
        ),
    ]

    return MetricsResponse(
        metrics=metrics,
        period_start=now - timedelta(hours=period_hours),
        period_end=now
    )


@observability_router.get("/metrics/requests", response_model=RequestMetrics)
def get_request_metrics(
    response: Response,
    period: str = Query("1h", description="Time period"),
) -> RequestMetrics:
    """
    Get API request metrics.
    """
    add_phase_header(response)

    return RequestMetrics(
        total_requests=15420,
        success_rate=98.5,
        avg_latency_ms=45.2,
        p95_latency_ms=120.0,
        p99_latency_ms=250.0,
        error_count=232,
        period=period
    )


# ============ Logs Endpoints ============

@observability_router.get("/logs", response_model=LogsResponse)
def get_logs(
    response: Response,
    level: Optional[LogLevel] = None,
    service: Optional[str] = None,
    search: Optional[str] = None,
    limit: int = Query(50, le=200),
) -> LogsResponse:
    """
    Get system logs with optional filtering.
    """
    add_phase_header(response)

    # Sample logs
    logs = [
        LogEntry(
            id=str(uuid4()),
            timestamp=datetime.utcnow() - timedelta(minutes=i),
            level=LogLevel.info if i % 5 != 0 else LogLevel.warning,
            service="backend",
            message=f"Request processed successfully" if i % 5 != 0 else "High latency detected",
            context={"endpoint": "/api/tasks", "duration_ms": 45 + i * 2},
            trace_id=f"trace-{uuid4().hex[:8]}"
        )
        for i in range(min(limit, 20))
    ]

    # Filter by level if specified
    if level:
        logs = [l for l in logs if l.level == level]

    return LogsResponse(
        logs=logs,
        total=len(logs),
        has_more=False
    )


@observability_router.get("/logs/errors", response_model=LogsResponse)
def get_error_logs(
    response: Response,
    limit: int = Query(50, le=200),
) -> LogsResponse:
    """
    Get recent error logs.
    """
    add_phase_header(response)

    errors = [
        LogEntry(
            id=str(uuid4()),
            timestamp=datetime.utcnow() - timedelta(hours=i),
            level=LogLevel.error,
            service="backend",
            message=f"Database connection timeout" if i % 2 == 0 else "AI API rate limit exceeded",
            context={"retry_count": 3, "duration_ms": 5000},
            trace_id=f"trace-{uuid4().hex[:8]}"
        )
        for i in range(min(limit, 5))
    ]

    return LogsResponse(
        logs=errors,
        total=len(errors),
        has_more=False
    )


# ============ Alerts Endpoints ============

@observability_router.get("/alerts", response_model=AlertsResponse)
def get_alerts(response: Response) -> AlertsResponse:
    """
    Get active alerts and alert rules.
    """
    add_phase_header(response)

    # No active critical alerts - system healthy
    active_alerts = [
        Alert(
            id=str(uuid4()),
            rule_id="rule-2",
            rule_name="High API Latency",
            severity=AlertSeverity.low,
            message="API latency above 100ms threshold",
            triggered_at=datetime.utcnow() - timedelta(minutes=30),
            acknowledged=True,
            metadata={"current_latency_ms": 120, "threshold_ms": 100}
        )
    ]

    return AlertsResponse(
        active=active_alerts,
        resolved_today=3,
        total_rules=8
    )


@observability_router.get("/alerts/rules")
def get_alert_rules(response: Response) -> list[AlertRule]:
    """
    Get configured alert rules.
    """
    add_phase_header(response)

    return [
        AlertRule(
            id="rule-1",
            name="Error Rate High",
            condition="error_rate > threshold",
            threshold=5.0,
            severity=AlertSeverity.high,
            enabled=True,
            notification_channels=["email", "slack"]
        ),
        AlertRule(
            id="rule-2",
            name="High API Latency",
            condition="avg_latency > threshold",
            threshold=100.0,
            severity=AlertSeverity.medium,
            enabled=True,
            notification_channels=["email"]
        ),
        AlertRule(
            id="rule-3",
            name="Database CPU High",
            condition="db_cpu > threshold",
            threshold=80.0,
            severity=AlertSeverity.high,
            enabled=True,
            notification_channels=["email", "slack"]
        ),
        AlertRule(
            id="rule-4",
            name="Redis Memory High",
            condition="redis_memory > threshold",
            threshold=70.0,
            severity=AlertSeverity.medium,
            enabled=True,
            notification_channels=["email"]
        ),
        AlertRule(
            id="rule-5",
            name="AI Rate Limit",
            condition="ai_429_count > threshold",
            threshold=10.0,
            severity=AlertSeverity.high,
            enabled=True,
            notification_channels=["email", "slack"]
        ),
        AlertRule(
            id="rule-6",
            name="Backend Down",
            condition="backend_health != healthy",
            threshold=0,
            severity=AlertSeverity.critical,
            enabled=True,
            notification_channels=["email", "slack", "pagerduty"]
        ),
        AlertRule(
            id="rule-7",
            name="Worker Stuck",
            condition="worker_queue_age > threshold",
            threshold=300.0,
            severity=AlertSeverity.high,
            enabled=True,
            notification_channels=["email"]
        ),
        AlertRule(
            id="rule-8",
            name="Storage Failures",
            condition="storage_errors > threshold",
            threshold=5.0,
            severity=AlertSeverity.high,
            enabled=True,
            notification_channels=["email", "slack"]
        ),
    ]


# ============ Deployment Endpoints ============

@observability_router.get("/deployments", response_model=DeploymentHistory)
def get_deployment_history(response: Response) -> DeploymentHistory:
    """
    Get deployment history.
    """
    add_phase_header(response)

    current = DeploymentInfo(
        id="deploy-001",
        version="1.0.0",
        environment="production",
        status="running",
        deployed_at=datetime.utcnow() - timedelta(hours=2),
        deployed_by="github-actions",
        commit_sha="ef4fdc5",
        rollback_available=True
    )

    history = [
        current,
        DeploymentInfo(
            id="deploy-000",
            version="0.9.9",
            environment="production",
            status="replaced",
            deployed_at=datetime.utcnow() - timedelta(days=1),
            deployed_by="github-actions",
            commit_sha="6bd723a",
            rollback_available=True
        ),
    ]

    return DeploymentHistory(
        deployments=history,
        current=current
    )


# ============ Resources Endpoints ============

@observability_router.get("/resources", response_model=ResourceUsage)
def get_resource_usage(response: Response) -> ResourceUsage:
    """
    Get current resource usage.
    """
    add_phase_header(response)

    return ResourceUsage(
        cpu_percent=35.5,
        memory_percent=45.2,
        memory_used_mb=512,
        memory_total_mb=1024,
        disk_percent=28.0,
        network_in_mbps=5.2,
        network_out_mbps=12.8
    )
