"""
Phase 24 - FinOps, Cost Governance & Resource Optimization API routes.
"""
from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Query, Response

from ..schemas.finops import (
    FinOpsStatus,
    BudgetStatus,
    CostCategory,
    CostEvent,
    CostSummary,
    CostBudget,
    BudgetAlert,
    AIUsageCost,
    AIUsageSummary,
    ComputeCost,
    StorageCost,
    DatabaseCost,
    CostForecast,
    CostAnomaly,
    OptimizationRecommendation,
    FinOpsDashboard,
)

finops_router = APIRouter(prefix="/finops", tags=["FinOps"])


def add_phase_header(response: Response):
    response.headers["X-Phase"] = "24-finops"


# ============ Status Endpoints ============

@finops_router.get("/status", response_model=FinOpsStatus)
def get_finops_status(response: Response) -> FinOpsStatus:
    """
    Get FinOps system status.
    """
    add_phase_header(response)
    
    return FinOpsStatus(
        status="operational",
        version="24.0",
        current_month_spend_usd=245.80,
        monthly_budget_usd=500.00,
        budget_status=BudgetStatus.ok,
        active_alerts=0,
        anomalies_detected=1
    )


@finops_router.get("/dashboard", response_model=FinOpsDashboard)
def get_finops_dashboard(response: Response) -> FinOpsDashboard:
    """
    Get complete FinOps dashboard data.
    """
    add_phase_header(response)
    
    status = FinOpsStatus(
        status="operational",
        version="24.0",
        current_month_spend_usd=245.80,
        monthly_budget_usd=500.00,
        budget_status=BudgetStatus.ok,
        active_alerts=0,
        anomalies_detected=1
    )
    
    cost_summary = CostSummary(
        period="2025-11",
        total_usd=245.80,
        by_category={
            "compute": 85.00,
            "database": 45.00,
            "redis": 15.00,
            "storage": 12.50,
            "ai": 88.30
        },
        change_percent=5.2,
        forecast_usd=320.00
    )
    
    ai_summary = AIUsageSummary(
        period="2025-11",
        total_tokens=2500000,
        total_cost_usd=88.30,
        by_model={"gpt-4": 75.00, "gpt-3.5-turbo": 13.30},
        by_type={"chat": 45.00, "hint": 25.00, "explain": 18.30},
        top_users=[
            {"user_id": "user-1", "tokens": 150000, "cost_usd": 5.25},
            {"user_id": "user-2", "tokens": 120000, "cost_usd": 4.20},
        ]
    )
    
    budgets = [
        CostBudget(
            id="budget-1",
            name="Monthly Total",
            monthly_limit_usd=500.00,
            alert_threshold_percent=80.0,
            current_spend_usd=245.80,
            status=BudgetStatus.ok,
            created_at=datetime.utcnow() - timedelta(days=30)
        ),
        CostBudget(
            id="budget-2",
            name="AI Budget",
            monthly_limit_usd=150.00,
            alert_threshold_percent=75.0,
            current_spend_usd=88.30,
            status=BudgetStatus.ok,
            created_at=datetime.utcnow() - timedelta(days=30)
        ),
    ]
    
    anomalies = [
        CostAnomaly(
            id="anomaly-1",
            category=CostCategory.ai,
            expected_usd=60.00,
            actual_usd=88.30,
            deviation_percent=47.0,
            severity="low",
            message="AI costs 47% higher than expected - increased user engagement",
            detected_at=datetime.utcnow() - timedelta(hours=6)
        )
    ]
    
    recommendations = [
        OptimizationRecommendation(
            id="rec-1",
            category=CostCategory.ai,
            title="Use GPT-3.5 for hints",
            description="Switch hint requests to GPT-3.5-turbo to reduce AI costs by 40%",
            potential_savings_usd=30.00,
            effort="low",
            impact="low"
        ),
        OptimizationRecommendation(
            id="rec-2",
            category=CostCategory.compute,
            title="Reduce staging resources",
            description="Scale down staging environment during off-hours",
            potential_savings_usd=15.00,
            effort="medium",
            impact="low"
        ),
    ]
    
    return FinOpsDashboard(
        status=status,
        cost_summary=cost_summary,
        ai_summary=ai_summary,
        budgets=budgets,
        anomalies=anomalies,
        recommendations=recommendations
    )


# ============ Cost Endpoints ============

@finops_router.get("/costs", response_model=CostSummary)
def get_cost_summary(
    response: Response,
    period: str = Query("2025-11", description="Period in YYYY-MM format"),
) -> CostSummary:
    """
    Get cost summary for a period.
    """
    add_phase_header(response)
    
    return CostSummary(
        period=period,
        total_usd=245.80,
        by_category={
            "compute": 85.00,
            "database": 45.00,
            "redis": 15.00,
            "storage": 12.50,
            "ai": 88.30
        },
        change_percent=5.2,
        forecast_usd=320.00
    )


@finops_router.get("/costs/events")
def list_cost_events(
    response: Response,
    category: Optional[CostCategory] = None,
    limit: int = Query(50, le=200),
) -> list[CostEvent]:
    """
    List recent cost events.
    """
    add_phase_header(response)
    
    events = [
        CostEvent(
            id=str(uuid4()),
            category=CostCategory.ai,
            amount_usd=0.05,
            description="AI chat request",
            metadata={"model": "gpt-4", "tokens": 1500},
            created_at=datetime.utcnow() - timedelta(minutes=i * 5)
        )
        for i in range(20)
    ]
    
    if category:
        events = [e for e in events if e.category == category]
    
    return events[:limit]


@finops_router.get("/costs/compute", response_model=ComputeCost)
def get_compute_costs(response: Response) -> ComputeCost:
    """
    Get compute cost breakdown.
    """
    add_phase_header(response)
    
    return ComputeCost(
        backend_hours=720,
        backend_cost_usd=65.00,
        worker_hours=360,
        worker_cost_usd=20.00,
        total_usd=85.00
    )


@finops_router.get("/costs/storage", response_model=StorageCost)
def get_storage_costs(response: Response) -> StorageCost:
    """
    Get storage cost breakdown.
    """
    add_phase_header(response)
    
    return StorageCost(
        total_gb=25.5,
        cost_per_gb=0.49,
        total_usd=12.50,
        by_type={
            "certificates": 2.50,
            "images": 5.00,
            "logs": 3.00,
            "exports": 2.00
        }
    )


@finops_router.get("/costs/database", response_model=DatabaseCost)
def get_database_costs(response: Response) -> DatabaseCost:
    """
    Get database cost breakdown.
    """
    add_phase_header(response)
    
    return DatabaseCost(
        size_gb=5.2,
        backup_gb=15.6,
        compute_hours=720,
        total_usd=45.00
    )


# ============ AI Usage Endpoints ============

@finops_router.get("/ai/usage", response_model=AIUsageSummary)
def get_ai_usage(
    response: Response,
    period: str = Query("2025-11", description="Period in YYYY-MM format"),
) -> AIUsageSummary:
    """
    Get AI usage summary.
    """
    add_phase_header(response)
    
    return AIUsageSummary(
        period=period,
        total_tokens=2500000,
        total_cost_usd=88.30,
        by_model={"gpt-4": 75.00, "gpt-3.5-turbo": 13.30},
        by_type={"chat": 45.00, "hint": 25.00, "explain": 18.30},
        top_users=[
            {"user_id": "user-1", "tokens": 150000, "cost_usd": 5.25},
            {"user_id": "user-2", "tokens": 120000, "cost_usd": 4.20},
            {"user_id": "user-3", "tokens": 95000, "cost_usd": 3.33},
        ]
    )


@finops_router.get("/ai/events")
def list_ai_usage_events(
    response: Response,
    user_id: Optional[str] = None,
    limit: int = Query(50, le=200),
) -> list[AIUsageCost]:
    """
    List AI usage events.
    """
    add_phase_header(response)
    
    events = [
        AIUsageCost(
            id=str(uuid4()),
            user_id=user_id or f"user-{i % 5}",
            model="gpt-4" if i % 3 == 0 else "gpt-3.5-turbo",
            tokens_input=500 + i * 100,
            tokens_output=200 + i * 50,
            cost_usd=0.05 if i % 3 == 0 else 0.01,
            request_type=["chat", "hint", "explain"][i % 3],
            created_at=datetime.utcnow() - timedelta(minutes=i * 10)
        )
        for i in range(30)
    ]
    
    return events[:limit]


# ============ Budget Endpoints ============

@finops_router.get("/budgets")
def list_budgets(response: Response) -> list[CostBudget]:
    """
    List all budgets.
    """
    add_phase_header(response)
    
    return [
        CostBudget(
            id="budget-1",
            name="Monthly Total",
            monthly_limit_usd=500.00,
            alert_threshold_percent=80.0,
            current_spend_usd=245.80,
            status=BudgetStatus.ok,
            created_at=datetime.utcnow() - timedelta(days=30)
        ),
        CostBudget(
            id="budget-2",
            name="AI Budget",
            monthly_limit_usd=150.00,
            alert_threshold_percent=75.0,
            current_spend_usd=88.30,
            status=BudgetStatus.ok,
            created_at=datetime.utcnow() - timedelta(days=30)
        ),
        CostBudget(
            id="budget-3",
            name="Compute Budget",
            monthly_limit_usd=100.00,
            alert_threshold_percent=80.0,
            current_spend_usd=85.00,
            status=BudgetStatus.warning,
            created_at=datetime.utcnow() - timedelta(days=30)
        ),
    ]


@finops_router.get("/budgets/alerts")
def list_budget_alerts(response: Response) -> list[BudgetAlert]:
    """
    List budget alerts.
    """
    add_phase_header(response)
    
    return [
        BudgetAlert(
            id="alert-1",
            budget_id="budget-3",
            budget_name="Compute Budget",
            threshold_percent=80.0,
            current_percent=85.0,
            message="Compute budget at 85% - approaching limit",
            triggered_at=datetime.utcnow() - timedelta(hours=2)
        )
    ]


# ============ Forecast Endpoints ============

@finops_router.get("/forecast", response_model=CostForecast)
def get_cost_forecast(response: Response) -> CostForecast:
    """
    Get cost forecast for next period.
    """
    add_phase_header(response)
    
    return CostForecast(
        period="2025-12",
        predicted_usd=320.00,
        confidence=0.85,
        breakdown={
            "compute": 95.00,
            "database": 50.00,
            "redis": 18.00,
            "storage": 15.00,
            "ai": 142.00
        },
        growth_rate=0.30,
        recommendations=[
            "Consider upgrading to annual billing for 20% savings",
            "AI usage projected to increase - review model selection",
            "Storage growth steady - no action needed"
        ]
    )


# ============ Anomaly Endpoints ============

@finops_router.get("/anomalies")
def list_anomalies(response: Response) -> list[CostAnomaly]:
    """
    List detected cost anomalies.
    """
    add_phase_header(response)
    
    return [
        CostAnomaly(
            id="anomaly-1",
            category=CostCategory.ai,
            expected_usd=60.00,
            actual_usd=88.30,
            deviation_percent=47.0,
            severity="low",
            message="AI costs 47% higher than expected - increased user engagement",
            detected_at=datetime.utcnow() - timedelta(hours=6)
        )
    ]


# ============ Optimization Endpoints ============

@finops_router.get("/recommendations")
def list_recommendations(response: Response) -> list[OptimizationRecommendation]:
    """
    List cost optimization recommendations.
    """
    add_phase_header(response)
    
    return [
        OptimizationRecommendation(
            id="rec-1",
            category=CostCategory.ai,
            title="Use GPT-3.5 for hints",
            description="Switch hint requests to GPT-3.5-turbo to reduce AI costs by 40%",
            potential_savings_usd=30.00,
            effort="low",
            impact="low"
        ),
        OptimizationRecommendation(
            id="rec-2",
            category=CostCategory.compute,
            title="Reduce staging resources",
            description="Scale down staging environment during off-hours",
            potential_savings_usd=15.00,
            effort="medium",
            impact="low"
        ),
        OptimizationRecommendation(
            id="rec-3",
            category=CostCategory.storage,
            title="Enable log compression",
            description="Compress older logs to reduce storage costs",
            potential_savings_usd=5.00,
            effort="low",
            impact="low"
        ),
        OptimizationRecommendation(
            id="rec-4",
            category=CostCategory.database,
            title="Schedule backups off-peak",
            description="Move backup window to off-peak hours for lower costs",
            potential_savings_usd=8.00,
            effort="low",
            impact="low"
        ),
    ]
