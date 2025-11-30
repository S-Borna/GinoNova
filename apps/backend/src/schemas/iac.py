"""
Phase 23 - Infrastructure as Code (IaC) schemas.
"""
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any, List
from pydantic import BaseModel


class Environment(str, Enum):
    """Deployment environments"""
    staging = "staging"
    production = "production"


class ResourceType(str, Enum):
    """Terraform resource types"""
    backend = "backend"
    worker = "worker"
    database = "database"
    redis = "redis"
    storage = "storage"
    network = "network"
    observability = "observability"


class TerraformState(str, Enum):
    """Terraform operation states"""
    pending = "pending"
    planning = "planning"
    applying = "applying"
    completed = "completed"
    failed = "failed"


# ============ Module Schemas ============

class TerraformModule(BaseModel):
    """Terraform module definition"""
    name: str
    resource_type: ResourceType
    version: str
    path: str
    description: str
    variables: Dict[str, Any]
    outputs: List[str]


class ModuleStatus(BaseModel):
    """Module deployment status"""
    name: str
    resource_type: ResourceType
    environment: Environment
    status: str
    last_applied: Optional[datetime] = None
    drift_detected: bool = False
    resources_count: int = 0


# ============ State Schemas ============

class StateFile(BaseModel):
    """Terraform state file info"""
    environment: Environment
    version: int
    serial: int
    last_modified: datetime
    resources_count: int
    locked: bool = False
    locked_by: Optional[str] = None


class StateLock(BaseModel):
    """State lock information"""
    id: str
    environment: Environment
    locked_at: datetime
    locked_by: str
    operation: str


# ============ Plan/Apply Schemas ============

class ResourceChange(BaseModel):
    """Individual resource change"""
    address: str
    action: str  # create, update, delete, no-op
    resource_type: str
    name: str
    before: Optional[Dict[str, Any]] = None
    after: Optional[Dict[str, Any]] = None


class TerraformPlan(BaseModel):
    """Terraform plan output"""
    id: str
    environment: Environment
    status: TerraformState
    created_at: datetime
    created_by: str
    changes: List[ResourceChange]
    resources_to_add: int = 0
    resources_to_change: int = 0
    resources_to_destroy: int = 0


class TerraformApply(BaseModel):
    """Terraform apply result"""
    id: str
    plan_id: str
    environment: Environment
    status: TerraformState
    started_at: datetime
    completed_at: Optional[datetime] = None
    applied_by: str
    resources_created: int = 0
    resources_updated: int = 0
    resources_destroyed: int = 0
    error: Optional[str] = None


# ============ Environment Schemas ============

class EnvironmentConfig(BaseModel):
    """Environment configuration"""
    name: Environment
    backend_replicas: int
    worker_replicas: int
    database_size: str
    redis_size: str
    storage_bucket: str
    auto_deploy: bool
    branch: str


class EnvironmentStatus(BaseModel):
    """Environment deployment status"""
    name: Environment
    status: str
    modules: List[ModuleStatus]
    last_apply: Optional[datetime] = None
    drift_detected: bool = False


# ============ IaC Status Schema ============

class IaCStatus(BaseModel):
    """IaC system status"""
    status: str
    version: str = "23.0"
    terraform_version: str
    environments: List[Environment]
    modules_count: int
    last_plan: Optional[datetime] = None
    last_apply: Optional[datetime] = None
    state_backend: str = "s3"


# ============ Scaling Schemas ============

class ScalingRule(BaseModel):
    """Auto-scaling rule"""
    resource: str
    metric: str
    threshold: float
    min_replicas: int
    max_replicas: int
    cooldown_seconds: int


class ScalingConfig(BaseModel):
    """Scaling configuration"""
    environment: Environment
    rules: List[ScalingRule]
