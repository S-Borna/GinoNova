"""
Phase 27 - Machine Learning Foundation & Intelligence Pipeline schemas.
"""
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any, List
from pydantic import BaseModel


class DatasetType(str, Enum):
    """Dataset types"""
    user_skill = "user_skill"
    task_difficulty = "task_difficulty"
    prediction_ready = "prediction_ready"
    user_behavior = "user_behavior"


class FeatureType(str, Enum):
    """Feature types"""
    numeric = "numeric"
    categorical = "categorical"
    embedding = "embedding"
    time_series = "time_series"


class ModelStatus(str, Enum):
    """Model training status"""
    pending = "pending"
    training = "training"
    completed = "completed"
    failed = "failed"
    deployed = "deployed"


# ============ Feature Schemas ============

class Feature(BaseModel):
    """Individual feature definition"""
    name: str
    feature_type: FeatureType
    description: str
    source: str
    importance: Optional[float] = None


class FeatureVector(BaseModel):
    """Feature vector for a user"""
    user_id: str
    features: Dict[str, Any]
    created_at: datetime


class FeatureSnapshot(BaseModel):
    """Feature snapshot"""
    id: str
    user_id: str
    feature_vector: Dict[str, float]
    version: int
    created_at: datetime


# ============ Dataset Schemas ============

class DatasetInfo(BaseModel):
    """Dataset information"""
    id: str
    name: str
    dataset_type: DatasetType
    description: str
    rows: int
    columns: int
    size_mb: float
    path: str
    created_at: datetime
    last_updated: datetime


class DatasetPreview(BaseModel):
    """Dataset preview"""
    id: str
    name: str
    columns: List[str]
    sample_rows: List[Dict[str, Any]]
    total_rows: int


# ============ Model Schemas ============

class ModelInfo(BaseModel):
    """ML model information"""
    id: str
    name: str
    version: str
    description: str
    status: ModelStatus
    accuracy: Optional[float] = None
    path: str
    metadata: Optional[Dict[str, Any]] = None
    created_at: datetime
    deployed_at: Optional[datetime] = None


class TrainingLog(BaseModel):
    """Training log entry"""
    id: str
    model_id: str
    dataset: str
    status: ModelStatus
    accuracy: Optional[float] = None
    loss: Optional[float] = None
    epochs: Optional[int] = None
    duration_seconds: Optional[int] = None
    notes: Optional[str] = None
    started_at: datetime
    completed_at: Optional[datetime] = None


# ============ Insight Schemas ============

class UserInsight(BaseModel):
    """AI-generated user insight"""
    id: str
    user_id: str
    insight_type: str
    title: str
    message: str
    confidence: float
    data: Optional[Dict[str, Any]] = None
    created_at: datetime


class InsightCategory(BaseModel):
    """Insight category"""
    name: str
    count: int
    description: str


# ============ Pipeline Schemas ============

class PipelineJob(BaseModel):
    """Pipeline job"""
    id: str
    name: str
    status: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    records_processed: int = 0
    errors: int = 0


class PipelineStatus(BaseModel):
    """Pipeline status"""
    feature_pipeline: str
    dataset_builder: str
    last_run: Optional[datetime] = None
    next_run: Optional[datetime] = None
    jobs_today: int


# ============ ML Status Schema ============

class MLStatus(BaseModel):
    """ML system status"""
    status: str
    version: str = "27.0"
    features_count: int
    datasets_count: int
    models_count: int
    insights_generated_today: int
    pipeline_status: str
    storage_used_mb: float


# ============ Storage Schemas ============

class MLStorageInfo(BaseModel):
    """ML storage information"""
    total_mb: float
    raw_mb: float
    features_mb: float
    datasets_mb: float
    models_mb: float
    logs_mb: float
