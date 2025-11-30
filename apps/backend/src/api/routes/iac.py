"""
Phase 23 - Infrastructure as Code (IaC) API routes.
"""
from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Query, Response, HTTPException

from ..schemas.iac import (
    IaCStatus,
    Environment,
    ResourceType,
    TerraformState,
    TerraformModule,
    ModuleStatus,
    StateFile,
    StateLock,
    TerraformPlan,
    TerraformApply,
    ResourceChange,
    EnvironmentConfig,
    EnvironmentStatus,
    ScalingRule,
    ScalingConfig,
)

iac_router = APIRouter(prefix="/iac", tags=["Infrastructure as Code"])


def add_phase_header(response: Response):
    response.headers["X-Phase"] = "23-iac"


# ============ Status Endpoints ============

@iac_router.get("/status", response_model=IaCStatus)
def get_iac_status(response: Response) -> IaCStatus:
    """
    Get IaC system status.
    """
    add_phase_header(response)
    
    return IaCStatus(
        status="operational",
        version="23.0",
        terraform_version="1.6.0",
        environments=[Environment.staging, Environment.production],
        modules_count=7,
        last_plan=datetime.utcnow() - timedelta(hours=1),
        last_apply=datetime.utcnow() - timedelta(hours=2),
        state_backend="s3"
    )


# ============ Modules Endpoints ============

@iac_router.get("/modules")
def list_modules(response: Response) -> list[TerraformModule]:
    """
    List all Terraform modules.
    """
    add_phase_header(response)
    
    return [
        TerraformModule(
            name="backend",
            resource_type=ResourceType.backend,
            version="1.0.0",
            path="infra/modules/backend",
            description="FastAPI backend service on Railway",
            variables={"replicas": 2, "cpu": "1", "memory": "1Gi"},
            outputs=["service_url", "health_endpoint"]
        ),
        TerraformModule(
            name="worker",
            resource_type=ResourceType.worker,
            version="1.0.0",
            path="infra/modules/worker",
            description="Background worker service",
            variables={"replicas": 1, "queue_name": "default"},
            outputs=["worker_id"]
        ),
        TerraformModule(
            name="database",
            resource_type=ResourceType.database,
            version="1.0.0",
            path="infra/modules/database",
            description="PostgreSQL database on Railway",
            variables={"size": "medium", "backup_retention": 7},
            outputs=["database_url", "host", "port"]
        ),
        TerraformModule(
            name="redis",
            resource_type=ResourceType.redis,
            version="1.0.0",
            path="infra/modules/redis",
            description="Redis cache on Railway",
            variables={"max_memory": "256mb", "eviction_policy": "allkeys-lru"},
            outputs=["redis_url"]
        ),
        TerraformModule(
            name="storage",
            resource_type=ResourceType.storage,
            version="1.0.0",
            path="infra/modules/storage",
            description="S3-compatible object storage",
            variables={"bucket_name": "devopshub-storage", "region": "us-east-1"},
            outputs=["bucket_url", "access_key_id"]
        ),
        TerraformModule(
            name="network",
            resource_type=ResourceType.network,
            version="1.0.0",
            path="infra/modules/network",
            description="Network configuration and secrets",
            variables={"enable_tls": True, "allowed_origins": ["*.netlify.app"]},
            outputs=["network_id"]
        ),
        TerraformModule(
            name="observability",
            resource_type=ResourceType.observability,
            version="1.0.0",
            path="infra/modules/observability",
            description="Grafana dashboards and alerts",
            variables={"retention_days": 30, "alert_email": "ops@devopshub.io"},
            outputs=["grafana_url", "dashboard_ids"]
        ),
    ]


@iac_router.get("/modules/{name}/status", response_model=ModuleStatus)
def get_module_status(
    name: str,
    response: Response,
    environment: Environment = Query(Environment.production),
) -> ModuleStatus:
    """
    Get status of a specific module.
    """
    add_phase_header(response)
    
    modules = {
        "backend": ModuleStatus(
            name="backend",
            resource_type=ResourceType.backend,
            environment=environment,
            status="deployed",
            last_applied=datetime.utcnow() - timedelta(hours=2),
            drift_detected=False,
            resources_count=3
        ),
        "database": ModuleStatus(
            name="database",
            resource_type=ResourceType.database,
            environment=environment,
            status="deployed",
            last_applied=datetime.utcnow() - timedelta(days=1),
            drift_detected=False,
            resources_count=2
        ),
    }
    
    if name not in modules:
        return ModuleStatus(
            name=name,
            resource_type=ResourceType.backend,
            environment=environment,
            status="deployed",
            last_applied=datetime.utcnow() - timedelta(hours=3),
            drift_detected=False,
            resources_count=1
        )
    
    return modules[name]


# ============ State Endpoints ============

@iac_router.get("/state")
def list_state_files(response: Response) -> list[StateFile]:
    """
    List Terraform state files.
    """
    add_phase_header(response)
    
    return [
        StateFile(
            environment=Environment.production,
            version=1,
            serial=42,
            last_modified=datetime.utcnow() - timedelta(hours=2),
            resources_count=15,
            locked=False
        ),
        StateFile(
            environment=Environment.staging,
            version=1,
            serial=38,
            last_modified=datetime.utcnow() - timedelta(hours=6),
            resources_count=12,
            locked=False
        ),
    ]


@iac_router.get("/state/{environment}", response_model=StateFile)
def get_state(environment: Environment, response: Response) -> StateFile:
    """
    Get state file for an environment.
    """
    add_phase_header(response)
    
    return StateFile(
        environment=environment,
        version=1,
        serial=42 if environment == Environment.production else 38,
        last_modified=datetime.utcnow() - timedelta(hours=2),
        resources_count=15 if environment == Environment.production else 12,
        locked=False
    )


# ============ Plan/Apply Endpoints ============

@iac_router.get("/plans")
def list_plans(
    response: Response,
    environment: Optional[Environment] = None,
    limit: int = Query(10, le=50),
) -> list[TerraformPlan]:
    """
    List recent Terraform plans.
    """
    add_phase_header(response)
    
    plans = [
        TerraformPlan(
            id=f"plan-{uuid4().hex[:8]}",
            environment=Environment.production,
            status=TerraformState.completed,
            created_at=datetime.utcnow() - timedelta(hours=i),
            created_by="github-actions",
            changes=[],
            resources_to_add=0,
            resources_to_change=1 if i == 0 else 0,
            resources_to_destroy=0
        )
        for i in range(min(limit, 5))
    ]
    
    if environment:
        plans = [p for p in plans if p.environment == environment]
    
    return plans


@iac_router.post("/plan", response_model=TerraformPlan)
def create_plan(
    response: Response,
    environment: Environment = Query(Environment.staging),
) -> TerraformPlan:
    """
    Create a new Terraform plan.
    """
    add_phase_header(response)
    
    return TerraformPlan(
        id=f"plan-{uuid4().hex[:8]}",
        environment=environment,
        status=TerraformState.completed,
        created_at=datetime.utcnow(),
        created_by="api",
        changes=[
            ResourceChange(
                address="module.backend.railway_service.main",
                action="update",
                resource_type="railway_service",
                name="main",
                before={"replicas": 1},
                after={"replicas": 2}
            )
        ],
        resources_to_add=0,
        resources_to_change=1,
        resources_to_destroy=0
    )


@iac_router.get("/applies")
def list_applies(
    response: Response,
    environment: Optional[Environment] = None,
    limit: int = Query(10, le=50),
) -> list[TerraformApply]:
    """
    List recent Terraform applies.
    """
    add_phase_header(response)
    
    applies = [
        TerraformApply(
            id=f"apply-{uuid4().hex[:8]}",
            plan_id=f"plan-{uuid4().hex[:8]}",
            environment=Environment.production,
            status=TerraformState.completed,
            started_at=datetime.utcnow() - timedelta(hours=i + 1),
            completed_at=datetime.utcnow() - timedelta(hours=i),
            applied_by="github-actions",
            resources_created=0,
            resources_updated=1,
            resources_destroyed=0
        )
        for i in range(min(limit, 5))
    ]
    
    if environment:
        applies = [a for a in applies if a.environment == environment]
    
    return applies


# ============ Environment Endpoints ============

@iac_router.get("/environments")
def list_environments(response: Response) -> list[EnvironmentConfig]:
    """
    List environment configurations.
    """
    add_phase_header(response)
    
    return [
        EnvironmentConfig(
            name=Environment.production,
            backend_replicas=2,
            worker_replicas=1,
            database_size="medium",
            redis_size="256mb",
            storage_bucket="devopshub-prod",
            auto_deploy=True,
            branch="main"
        ),
        EnvironmentConfig(
            name=Environment.staging,
            backend_replicas=1,
            worker_replicas=1,
            database_size="small",
            redis_size="128mb",
            storage_bucket="devopshub-staging",
            auto_deploy=True,
            branch="develop"
        ),
    ]


@iac_router.get("/environments/{environment}/status", response_model=EnvironmentStatus)
def get_environment_status(environment: Environment, response: Response) -> EnvironmentStatus:
    """
    Get detailed environment status.
    """
    add_phase_header(response)
    
    modules = [
        ModuleStatus(
            name=name,
            resource_type=rt,
            environment=environment,
            status="deployed",
            last_applied=datetime.utcnow() - timedelta(hours=2),
            drift_detected=False,
            resources_count=2
        )
        for name, rt in [
            ("backend", ResourceType.backend),
            ("worker", ResourceType.worker),
            ("database", ResourceType.database),
            ("redis", ResourceType.redis),
            ("storage", ResourceType.storage),
        ]
    ]
    
    return EnvironmentStatus(
        name=environment,
        status="healthy",
        modules=modules,
        last_apply=datetime.utcnow() - timedelta(hours=2),
        drift_detected=False
    )


# ============ Scaling Endpoints ============

@iac_router.get("/scaling/{environment}", response_model=ScalingConfig)
def get_scaling_config(environment: Environment, response: Response) -> ScalingConfig:
    """
    Get auto-scaling configuration for an environment.
    """
    add_phase_header(response)
    
    rules = [
        ScalingRule(
            resource="backend",
            metric="cpu_percent",
            threshold=70.0,
            min_replicas=1 if environment == Environment.staging else 2,
            max_replicas=3 if environment == Environment.staging else 5,
            cooldown_seconds=300
        ),
        ScalingRule(
            resource="worker",
            metric="queue_depth",
            threshold=50.0,
            min_replicas=1,
            max_replicas=3 if environment == Environment.staging else 5,
            cooldown_seconds=180
        ),
    ]
    
    return ScalingConfig(
        environment=environment,
        rules=rules
    )
