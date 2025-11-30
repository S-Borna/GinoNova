"""
Phase 24 - FinOps, Cost Governance & Resource Optimization schemas.
"""
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any, List
from uuid import UUID
from pydantic import BaseModel


class CostCategory(str, Enum):
    """Cost categories"""
    compute = "compute"
    database = "database"
    redis = "redis"
    storage = "storage"
    ai = "ai"
    network = "network"


class BudgetStatus(str, Enum):
    """Budget status"""
    ok = "ok"
    warning = "warning"
    exceeded = "exceeded"


# ============ Cost Event Schemas ============

class CostEvent(BaseModel):
    """Individual cost event"""
    id: str
    tenant_id: Optional[str] = None
    category: CostCategory
    amount_usd: float
    description: str
    metadata: Optional[Dict[str, Any]] = None
    created_at: datetime


class CostSummary(BaseModel):
    """Cost summary for a period"""
    period: str
    total_usd: float
    by_category: Dict[str, float]
    change_percent: float
    forecast_usd: float


# ============ Budget Schemas ============

class CostBudget(BaseModel):
    """Budget definition"""
    id: str
    name: str
    tenant_id: Optional[str] = None
    monthly_limit_usd: float
    alert_threshold_percent: float
    current_spend_usd: float
    status: BudgetStatus
    created_at: datetime


class BudgetAlert(BaseModel):
    """Budget alert"""
    id: str
    budget_id: str
    budget_name: str
    threshold_percent: float
    current_percent: float
    message: str
    triggered_at: datetime


# ============ AI Usage Schemas ============

class AIUsageCost(BaseModel):
    """AI usage cost tracking"""
    id: str
    user_id: str
    task_id: Optional[str] = None
    model: str
    tokens_input: int
    tokens_output: int
    cost_usd: float
    request_type: str  # hint, explain, solve, chat
    created_at: datetime


class AIUsageSummary(BaseModel):
    """AI usage summary"""
    period: str
    total_tokens: int
    total_cost_usd: float
    by_model: Dict[str, float]
    by_type: Dict[str, float]
    top_users: List[Dict[str, Any]]


# ============ Resource Usage Schemas ============

class ComputeCost(BaseModel):
    """Compute cost breakdown"""
    backend_hours: float
    backend_cost_usd: float
    worker_hours: float
    worker_cost_usd: float
    total_usd: float


class StorageCost(BaseModel):
    """Storage cost breakdown"""
    total_gb: float
    cost_per_gb: float
    total_usd: float
    by_type: Dict[str, float]  # pdfs, images, logs, etc.


class DatabaseCost(BaseModel):
    """Database cost breakdown"""
    size_gb: float
    backup_gb: float
    compute_hours: float
    total_usd: float


# ============ Forecast Schemas ============

class CostForecast(BaseModel):
    """Cost forecast"""
    period: str
    predicted_usd: float
    confidence: float
    breakdown: Dict[str, float]
    growth_rate: float
    recommendations: List[str]


class CostAnomaly(BaseModel):
    """Cost anomaly detection"""
    id: str
    category: CostCategory
    expected_usd: float
    actual_usd: float
    deviation_percent: float
    severity: str
    message: str
    detected_at: datetime


# ============ Optimization Schemas ============

class OptimizationRecommendation(BaseModel):
    """Cost optimization recommendation"""
    id: str
    category: CostCategory
    title: str
    description: str
    potential_savings_usd: float
    effort: str  # low, medium, high
    impact: str  # low, medium, high


# ============ FinOps Status Schema ============

class FinOpsStatus(BaseModel):
    """FinOps system status"""
    status: str
    version: str = "24.0"
    current_month_spend_usd: float
    monthly_budget_usd: float
    budget_status: BudgetStatus
    active_alerts: int
    anomalies_detected: int


# ============ Dashboard Schemas ============

class FinOpsDashboard(BaseModel):
    """FinOps dashboard data"""
    status: FinOpsStatus
    cost_summary: CostSummary
    ai_summary: AIUsageSummary
    budgets: List[CostBudget]
    anomalies: List[CostAnomaly]
    recommendations: List[OptimizationRecommendation]
