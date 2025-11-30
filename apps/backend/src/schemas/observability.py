"""
Phase 22 - Infrastructure, Deployment & Observability schemas.
"""
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any, List
from uuid import UUID
from pydantic import BaseModel


class ServiceStatus(str, Enum):
    """Service health status"""
    healthy = "healthy"
    degraded = "degraded"
    unhealthy = "unhealthy"
    unknown = "unknown"


class AlertSeverity(str, Enum):
    """Alert severity levels"""
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class LogLevel(str, Enum):
    """Log levels"""
    debug = "debug"
    info = "info"
    warning = "warning"
    error = "error"
    critical = "critical"


# ============ Status Schemas ============

class ServiceHealth(BaseModel):
    """Individual service health"""
    name: str
    status: ServiceStatus
    latency_ms: Optional[float] = None
    last_check: datetime
    details: Optional[Dict[str, Any]] = None


class InfraStatus(BaseModel):
    """Infrastructure status response"""
    status: str
    version: str = "22.0"
    services: List[ServiceHealth]
    uptime_seconds: int
    last_deploy: Optional[datetime] = None


# ============ Metrics Schemas ============

class MetricPoint(BaseModel):
    """Single metric data point"""
    name: str
    value: float
    unit: str
    timestamp: datetime
    tags: Optional[Dict[str, str]] = None


class MetricsResponse(BaseModel):
    """Metrics response"""
    metrics: List[MetricPoint]
    period_start: datetime
    period_end: datetime


class RequestMetrics(BaseModel):
    """API request metrics"""
    total_requests: int
    success_rate: float
    avg_latency_ms: float
    p95_latency_ms: float
    p99_latency_ms: float
    error_count: int
    period: str = "1h"


# ============ Log Schemas ============

class LogEntry(BaseModel):
    """Log entry"""
    id: str
    timestamp: datetime
    level: LogLevel
    service: str
    message: str
    context: Optional[Dict[str, Any]] = None
    trace_id: Optional[str] = None


class LogsResponse(BaseModel):
    """Logs response"""
    logs: List[LogEntry]
    total: int
    has_more: bool


class LogFilter(BaseModel):
    """Log filter criteria"""
    level: Optional[LogLevel] = None
    service: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    search: Optional[str] = None
    limit: int = 100


# ============ Alert Schemas ============

class AlertRule(BaseModel):
    """Alert rule definition"""
    id: str
    name: str
    condition: str
    threshold: float
    severity: AlertSeverity
    enabled: bool
    notification_channels: List[str]


class Alert(BaseModel):
    """Active alert"""
    id: str
    rule_id: str
    rule_name: str
    severity: AlertSeverity
    message: str
    triggered_at: datetime
    resolved_at: Optional[datetime] = None
    acknowledged: bool = False
    metadata: Optional[Dict[str, Any]] = None


class AlertsResponse(BaseModel):
    """Alerts response"""
    active: List[Alert]
    resolved_today: int
    total_rules: int


# ============ Deployment Schemas ============

class DeploymentInfo(BaseModel):
    """Deployment information"""
    id: str
    version: str
    environment: str
    status: str
    deployed_at: datetime
    deployed_by: Optional[str] = None
    commit_sha: Optional[str] = None
    rollback_available: bool = False


class DeploymentHistory(BaseModel):
    """Deployment history"""
    deployments: List[DeploymentInfo]
    current: DeploymentInfo


# ============ Resource Schemas ============

class ResourceUsage(BaseModel):
    """Resource usage metrics"""
    cpu_percent: float
    memory_percent: float
    memory_used_mb: int
    memory_total_mb: int
    disk_percent: float
    network_in_mbps: float
    network_out_mbps: float


class ContainerInfo(BaseModel):
    """Container information"""
    id: str
    name: str
    status: str
    image: str
    created_at: datetime
    resource_usage: Optional[ResourceUsage] = None
