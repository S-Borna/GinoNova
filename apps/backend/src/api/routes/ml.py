"""
Phase 27 - Machine Learning Foundation & Intelligence Pipeline API routes.
"""
from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Query, Response

from ..schemas.ml import (
    MLStatus,
    Feature,
    FeatureType,
    FeatureVector,
    FeatureSnapshot,
    DatasetInfo,
    DatasetType,
    DatasetPreview,
    ModelInfo,
    ModelStatus,
    TrainingLog,
    UserInsight,
    InsightCategory,
    PipelineJob,
    PipelineStatus,
    MLStorageInfo,
)

ml_router = APIRouter(prefix="/ml", tags=["Machine Learning"])


def add_phase_header(response: Response):
    response.headers["X-Phase"] = "27-ml"


# ============ Status Endpoints ============

@ml_router.get("/status", response_model=MLStatus)
def get_ml_status(response: Response) -> MLStatus:
    """
    Get ML system status.
    """
    add_phase_header(response)
    
    return MLStatus(
        status="operational",
        version="27.0",
        features_count=15,
        datasets_count=3,
        models_count=2,
        insights_generated_today=450,
        pipeline_status="idle",
        storage_used_mb=125.5
    )


# ============ Feature Endpoints ============

@ml_router.get("/features")
def list_features(response: Response) -> list[Feature]:
    """
    List available ML features.
    """
    add_phase_header(response)
    
    return [
        Feature(
            name="study_velocity",
            feature_type=FeatureType.numeric,
            description="Tasks completed per hour",
            source="studyflow",
            importance=0.85
        ),
        Feature(
            name="module_complexity_score",
            feature_type=FeatureType.numeric,
            description="Average complexity of completed modules",
            source="modules",
            importance=0.72
        ),
        Feature(
            name="task_difficulty_calibration",
            feature_type=FeatureType.numeric,
            description="User's actual vs expected difficulty performance",
            source="tasks",
            importance=0.68
        ),
        Feature(
            name="ai_usage_style",
            feature_type=FeatureType.categorical,
            description="Pattern of AI assistance usage",
            source="ai_engine",
            importance=0.55
        ),
        Feature(
            name="retry_count_avg",
            feature_type=FeatureType.numeric,
            description="Average retries per task",
            source="progress",
            importance=0.62
        ),
        Feature(
            name="confusion_indicator",
            feature_type=FeatureType.numeric,
            description="Score indicating user confusion",
            source="analytics",
            importance=0.75
        ),
        Feature(
            name="streak_stability",
            feature_type=FeatureType.numeric,
            description="Consistency of study streaks",
            source="studyflow",
            importance=0.58
        ),
        Feature(
            name="active_passive_ratio",
            feature_type=FeatureType.numeric,
            description="Active vs passive learning ratio",
            source="behavior",
            importance=0.65
        ),
        Feature(
            name="time_of_day_preference",
            feature_type=FeatureType.categorical,
            description="Preferred study time",
            source="studyflow",
            importance=0.45
        ),
        Feature(
            name="module_transition_prob",
            feature_type=FeatureType.numeric,
            description="Probability of completing next module",
            source="progress",
            importance=0.78
        ),
    ]


@ml_router.get("/features/{user_id}", response_model=FeatureVector)
def get_user_features(user_id: str, response: Response) -> FeatureVector:
    """
    Get feature vector for a user.
    """
    add_phase_header(response)
    
    return FeatureVector(
        user_id=user_id,
        features={
            "study_velocity": 2.5,
            "module_complexity_score": 0.68,
            "task_difficulty_calibration": 1.15,
            "ai_usage_style": "moderate",
            "retry_count_avg": 1.3,
            "confusion_indicator": 0.25,
            "streak_stability": 0.85,
            "active_passive_ratio": 0.72,
            "time_of_day_preference": "evening",
            "module_transition_prob": 0.88
        },
        created_at=datetime.utcnow()
    )


@ml_router.get("/features/{user_id}/snapshots")
def list_feature_snapshots(
    user_id: str,
    response: Response,
    limit: int = Query(10, le=50),
) -> list[FeatureSnapshot]:
    """
    List feature snapshots for a user.
    """
    add_phase_header(response)
    
    return [
        FeatureSnapshot(
            id=str(uuid4()),
            user_id=user_id,
            feature_vector={
                "study_velocity": 2.5 - i * 0.1,
                "module_complexity_score": 0.68 + i * 0.02,
                "confusion_indicator": 0.25 + i * 0.05,
            },
            version=i + 1,
            created_at=datetime.utcnow() - timedelta(days=i)
        )
        for i in range(min(limit, 7))
    ]


# ============ Dataset Endpoints ============

@ml_router.get("/datasets")
def list_datasets(response: Response) -> list[DatasetInfo]:
    """
    List available datasets.
    """
    add_phase_header(response)
    
    return [
        DatasetInfo(
            id="ds-1",
            name="user_skill_dataset",
            dataset_type=DatasetType.user_skill,
            description="User skill progression features",
            rows=15000,
            columns=12,
            size_mb=25.5,
            path="ml/datasets/user_skill_v1.parquet",
            created_at=datetime.utcnow() - timedelta(days=7),
            last_updated=datetime.utcnow() - timedelta(hours=6)
        ),
        DatasetInfo(
            id="ds-2",
            name="task_difficulty_dataset",
            dataset_type=DatasetType.task_difficulty,
            description="Task difficulty calibration data",
            rows=8500,
            columns=8,
            size_mb=12.3,
            path="ml/datasets/task_difficulty_v1.parquet",
            created_at=datetime.utcnow() - timedelta(days=14),
            last_updated=datetime.utcnow() - timedelta(hours=6)
        ),
        DatasetInfo(
            id="ds-3",
            name="prediction_ready_dataset",
            dataset_type=DatasetType.prediction_ready,
            description="Combined features for prediction",
            rows=12000,
            columns=20,
            size_mb=45.8,
            path="ml/datasets/prediction_ready_v1.parquet",
            created_at=datetime.utcnow() - timedelta(days=3),
            last_updated=datetime.utcnow() - timedelta(hours=6)
        ),
    ]


@ml_router.get("/datasets/{dataset_id}/preview", response_model=DatasetPreview)
def preview_dataset(dataset_id: str, response: Response) -> DatasetPreview:
    """
    Preview a dataset.
    """
    add_phase_header(response)
    
    return DatasetPreview(
        id=dataset_id,
        name="user_skill_dataset",
        columns=["user_id", "study_velocity", "tasks_completed", "difficulty_score", "ai_usage"],
        sample_rows=[
            {"user_id": "u1", "study_velocity": 2.5, "tasks_completed": 45, "difficulty_score": 0.68, "ai_usage": 15},
            {"user_id": "u2", "study_velocity": 1.8, "tasks_completed": 32, "difficulty_score": 0.55, "ai_usage": 28},
            {"user_id": "u3", "study_velocity": 3.2, "tasks_completed": 68, "difficulty_score": 0.82, "ai_usage": 5},
        ],
        total_rows=15000
    )


# ============ Model Endpoints ============

@ml_router.get("/models")
def list_models(response: Response) -> list[ModelInfo]:
    """
    List ML models.
    """
    add_phase_header(response)
    
    return [
        ModelInfo(
            id="model-1",
            name="task_difficulty_predictor",
            version="1.0.0",
            description="Predicts task difficulty based on user features",
            status=ModelStatus.deployed,
            accuracy=0.85,
            path="ml/models/task_difficulty_v1.pkl",
            metadata={"algorithm": "random_forest", "features": 12},
            created_at=datetime.utcnow() - timedelta(days=30),
            deployed_at=datetime.utcnow() - timedelta(days=7)
        ),
        ModelInfo(
            id="model-2",
            name="next_task_recommender",
            version="0.9.0",
            description="Recommends next best task",
            status=ModelStatus.completed,
            accuracy=0.78,
            path="ml/models/next_task_v0.pkl",
            metadata={"algorithm": "gradient_boosting", "features": 15},
            created_at=datetime.utcnow() - timedelta(days=14)
        ),
    ]


@ml_router.get("/models/{model_id}/training-logs")
def get_training_logs(
    model_id: str,
    response: Response,
    limit: int = Query(10, le=50),
) -> list[TrainingLog]:
    """
    Get training logs for a model.
    """
    add_phase_header(response)
    
    return [
        TrainingLog(
            id=str(uuid4()),
            model_id=model_id,
            dataset="user_skill_dataset",
            status=ModelStatus.completed,
            accuracy=0.85 - i * 0.02,
            loss=0.15 + i * 0.01,
            epochs=100,
            duration_seconds=3600 + i * 300,
            notes=f"Training run {i + 1}",
            started_at=datetime.utcnow() - timedelta(days=i * 7),
            completed_at=datetime.utcnow() - timedelta(days=i * 7) + timedelta(hours=1)
        )
        for i in range(min(limit, 5))
    ]


# ============ Insight Endpoints ============

@ml_router.get("/insights/{user_id}")
def get_user_insights(
    user_id: str,
    response: Response,
    limit: int = Query(10, le=50),
) -> list[UserInsight]:
    """
    Get AI-generated insights for a user.
    """
    add_phase_header(response)
    
    insights = [
        UserInsight(
            id=str(uuid4()),
            user_id=user_id,
            insight_type="learning_pattern",
            title="Kvällsstudier mest effektiva",
            message="Du presterar 23% bättre under kvällstid (18-22). Överväg att schemalägga svårare uppgifter då.",
            confidence=0.87,
            data={"peak_hours": [18, 19, 20, 21], "improvement": 0.23},
            created_at=datetime.utcnow() - timedelta(hours=2)
        ),
        UserInsight(
            id=str(uuid4()),
            user_id=user_id,
            insight_type="difficulty_prediction",
            title="Modul 4 kan bli utmanande",
            message="Baserat på din progression pekar data på att modul 4 (Terraform) kan ta 40% längre tid än genomsnittet.",
            confidence=0.72,
            data={"predicted_duration": 1.4, "avg_duration": 1.0},
            created_at=datetime.utcnow() - timedelta(hours=6)
        ),
        UserInsight(
            id=str(uuid4()),
            user_id=user_id,
            insight_type="skill_gap",
            title="Regex-mönster behöver mer övning",
            message="Du fastnar 37% mer än snittet på regex-uppgifter. Rekommenderar extra övning.",
            confidence=0.82,
            data={"topic": "regex", "deviation": 0.37},
            created_at=datetime.utcnow() - timedelta(days=1)
        ),
    ]
    
    return insights[:limit]


@ml_router.get("/insights/categories")
def list_insight_categories(response: Response) -> list[InsightCategory]:
    """
    List insight categories.
    """
    add_phase_header(response)
    
    return [
        InsightCategory(name="learning_pattern", count=150, description="Patterns in study behavior"),
        InsightCategory(name="difficulty_prediction", count=85, description="Task/module difficulty predictions"),
        InsightCategory(name="skill_gap", count=120, description="Identified skill gaps"),
        InsightCategory(name="recommendation", count=95, description="Personalized recommendations"),
    ]


# ============ Pipeline Endpoints ============

@ml_router.get("/pipeline/status", response_model=PipelineStatus)
def get_pipeline_status(response: Response) -> PipelineStatus:
    """
    Get ML pipeline status.
    """
    add_phase_header(response)
    
    return PipelineStatus(
        feature_pipeline="idle",
        dataset_builder="idle",
        last_run=datetime.utcnow() - timedelta(hours=6),
        next_run=datetime.utcnow() + timedelta(hours=18),
        jobs_today=4
    )


@ml_router.get("/pipeline/jobs")
def list_pipeline_jobs(
    response: Response,
    limit: int = Query(10, le=50),
) -> list[PipelineJob]:
    """
    List recent pipeline jobs.
    """
    add_phase_header(response)
    
    return [
        PipelineJob(
            id=str(uuid4()),
            name="feature_extraction",
            status="completed",
            started_at=datetime.utcnow() - timedelta(hours=6),
            completed_at=datetime.utcnow() - timedelta(hours=5, minutes=45),
            records_processed=15000,
            errors=0
        ),
        PipelineJob(
            id=str(uuid4()),
            name="dataset_build",
            status="completed",
            started_at=datetime.utcnow() - timedelta(hours=5, minutes=45),
            completed_at=datetime.utcnow() - timedelta(hours=5, minutes=30),
            records_processed=12000,
            errors=2
        ),
    ]


@ml_router.post("/pipeline/trigger")
def trigger_pipeline(response: Response) -> PipelineJob:
    """
    Trigger ML pipeline manually.
    """
    add_phase_header(response)
    
    return PipelineJob(
        id=str(uuid4()),
        name="full_pipeline",
        status="started",
        started_at=datetime.utcnow(),
        records_processed=0,
        errors=0
    )


# ============ Storage Endpoints ============

@ml_router.get("/storage", response_model=MLStorageInfo)
def get_storage_info(response: Response) -> MLStorageInfo:
    """
    Get ML storage information.
    """
    add_phase_header(response)
    
    return MLStorageInfo(
        total_mb=125.5,
        raw_mb=35.2,
        features_mb=22.8,
        datasets_mb=45.5,
        models_mb=15.0,
        logs_mb=7.0
    )
