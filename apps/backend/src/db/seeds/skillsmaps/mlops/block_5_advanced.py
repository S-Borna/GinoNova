"""
MLOps SkillsMap - Block 5: Advanced MLOps
Nodes 17-20: Monitoring, AutoML, Production Best Practices, Platform Engineering
"""

BLOCK_5_NODES = [
    # Node 17: Model Monitoring
    {
        "id": "mlops-monitoring",
        "slug": "model-monitoring",
        "title": "Model Monitoring & Observability",
        "order_index": 17,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["mlops-containers"],
        "content": '''# Model Monitoring & Observability

## Varför Model Monitoring?

```
┌─────────────────────────────────────────────────────────────────────┐
│                     Model Decay Over Time                            │
│                                                                      │
│  Accuracy                                                            │
│    ↑                                                                 │
│  95├─────╮                                                          │
│    │      ╲                                                         │
│  90├       ╲─────╮                                                  │
│    │              ╲                                                 │
│  85├               ╲────────╮                                       │
│    │                         ╲         ← Data Drift                 │
│  80├                          ╲                                     │
│    │                           ╲────── ← Concept Drift              │
│  75├                                                                │
│    └────────┴────────┴────────┴────────→ Time                       │
│           Week 1    Week 4    Week 8   Week 12                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Types of Monitoring

### 1. Data Drift Detection

```python
from evidently import ColumnDriftMetric, DataDriftPreset
from evidently.report import Report
from evidently.test_suite import TestSuite
from evidently.tests import TestColumnDrift
import pandas as pd

def detect_data_drift(
    reference_data: pd.DataFrame,
    current_data: pd.DataFrame,
    threshold: float = 0.1
) -> dict:
    """Detect data drift using Evidently"""

    report = Report(metrics=[
        DataDriftPreset(),
    ])

    report.run(
        reference_data=reference_data,
        current_data=current_data,
    )

    # Get drift results
    result = report.as_dict()

    drift_summary = {
        "dataset_drift": result["metrics"][0]["result"]["dataset_drift"],
        "drift_share": result["metrics"][0]["result"]["drift_share"],
        "drifted_columns": [],
    }

    # Find drifted columns
    for col_name, col_data in result["metrics"][0]["result"]["drift_by_columns"].items():
        if col_data["drift_detected"]:
            drift_summary["drifted_columns"].append({
                "column": col_name,
                "statistic": col_data["stattest_name"],
                "p_value": col_data["p_value"],
            })

    return drift_summary

# Population Stability Index (PSI)
def calculate_psi(
    expected: pd.Series,
    actual: pd.Series,
    buckets: int = 10
) -> float:
    """Calculate PSI for a feature"""

    def scale_range(series, min_val, max_val, buckets):
        return np.floor((series - min_val) / (max_val - min_val) * buckets)

    breakpoints = np.linspace(
        min(expected.min(), actual.min()),
        max(expected.max(), actual.max()),
        buckets + 1
    )

    expected_counts = np.histogram(expected, bins=breakpoints)[0]
    actual_counts = np.histogram(actual, bins=breakpoints)[0]

    expected_percents = expected_counts / len(expected)
    actual_percents = actual_counts / len(actual)

    # Avoid division by zero
    expected_percents = np.where(expected_percents == 0, 0.001, expected_percents)
    actual_percents = np.where(actual_percents == 0, 0.001, actual_percents)

    psi_values = (actual_percents - expected_percents) * np.log(actual_percents / expected_percents)

    return np.sum(psi_values)

# PSI Thresholds:
# < 0.1: No significant change
# 0.1 - 0.2: Moderate change, investigation needed
# > 0.2: Significant change, action required
```

### 2. Model Performance Monitoring

```python
from prometheus_client import Counter, Histogram, Gauge
import time

# Metrics
PREDICTIONS = Counter(
    'model_predictions_total',
    'Total predictions',
    ['model_version', 'result']
)

LATENCY = Histogram(
    'model_inference_latency_seconds',
    'Inference latency',
    ['model_version'],
    buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0]
)

FEATURE_VALUES = Histogram(
    'model_feature_value',
    'Feature value distribution',
    ['feature_name'],
    buckets=[-10, -5, -2, -1, 0, 1, 2, 5, 10, 50, 100]
)

PREDICTION_CONFIDENCE = Histogram(
    'model_prediction_confidence',
    'Prediction confidence distribution',
    buckets=[0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
)

MODEL_ACCURACY = Gauge(
    'model_accuracy',
    'Rolling accuracy based on ground truth',
    ['model_version']
)

class InferenceMonitor:
    def __init__(self, model_version: str):
        self.model_version = model_version

    def record_prediction(
        self,
        features: dict,
        prediction: int,
        confidence: float,
        latency: float,
    ):
        # Record metrics
        PREDICTIONS.labels(
            model_version=self.model_version,
            result="fraud" if prediction == 1 else "legitimate"
        ).inc()

        LATENCY.labels(
            model_version=self.model_version
        ).observe(latency)

        PREDICTION_CONFIDENCE.observe(confidence)

        # Track feature distributions
        for feature_name, value in features.items():
            if isinstance(value, (int, float)):
                FEATURE_VALUES.labels(feature_name=feature_name).observe(value)

    def update_accuracy(self, predictions: list, ground_truth: list):
        """Update accuracy based on delayed ground truth"""
        accuracy = sum(p == g for p, g in zip(predictions, ground_truth)) / len(predictions)
        MODEL_ACCURACY.labels(model_version=self.model_version).set(accuracy)
```

### 3. Alerting

```python
from dataclasses import dataclass
from typing import List
import httpx

@dataclass
class Alert:
    severity: str  # critical, warning, info
    title: str
    description: str
    model_name: str
    metric_value: float
    threshold: float

class AlertManager:
    def __init__(self, slack_webhook: str, pagerduty_key: str):
        self.slack_webhook = slack_webhook
        self.pagerduty_key = pagerduty_key

    def check_thresholds(self, metrics: dict) -> List[Alert]:
        """Check metrics against thresholds"""
        alerts = []

        thresholds = {
            "accuracy": {"warning": 0.90, "critical": 0.85},
            "latency_p99": {"warning": 100, "critical": 200},
            "drift_score": {"warning": 0.1, "critical": 0.2},
            "error_rate": {"warning": 0.01, "critical": 0.05},
        }

        for metric_name, value in metrics.items():
            if metric_name in thresholds:
                t = thresholds[metric_name]

                if metric_name in ["accuracy"]:
                    # Lower is worse
                    if value < t["critical"]:
                        alerts.append(Alert("critical", f"{metric_name} critical",
                            f"{metric_name} is {value:.2f}", "fraud-detector", value, t["critical"]))
                    elif value < t["warning"]:
                        alerts.append(Alert("warning", f"{metric_name} warning",
                            f"{metric_name} is {value:.2f}", "fraud-detector", value, t["warning"]))
                else:
                    # Higher is worse
                    if value > t["critical"]:
                        alerts.append(Alert("critical", f"{metric_name} critical",
                            f"{metric_name} is {value:.2f}", "fraud-detector", value, t["critical"]))
                    elif value > t["warning"]:
                        alerts.append(Alert("warning", f"{metric_name} warning",
                            f"{metric_name} is {value:.2f}", "fraud-detector", value, t["warning"]))

        return alerts

    async def send_slack_alert(self, alert: Alert):
        """Send alert to Slack"""
        color = "#FF0000" if alert.severity == "critical" else "#FFA500"

        payload = {
            "attachments": [{
                "color": color,
                "title": alert.title,
                "text": alert.description,
                "fields": [
                    {"title": "Model", "value": alert.model_name, "short": True},
                    {"title": "Severity", "value": alert.severity, "short": True},
                    {"title": "Value", "value": f"{alert.metric_value:.4f}", "short": True},
                    {"title": "Threshold", "value": f"{alert.threshold:.4f}", "short": True},
                ]
            }]
        }

        async with httpx.AsyncClient() as client:
            await client.post(self.slack_webhook, json=payload)
```

## Grafana Dashboard

```json
{
  "dashboard": {
    "title": "ML Model Monitoring",
    "panels": [
      {
        "title": "Predictions per Second",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(model_predictions_total[5m])",
            "legendFormat": "{{result}}"
          }
        ]
      },
      {
        "title": "Inference Latency P99",
        "type": "stat",
        "targets": [
          {
            "expr": "histogram_quantile(0.99, rate(model_inference_latency_seconds_bucket[5m]))"
          }
        ],
        "thresholds": {
          "mode": "absolute",
          "steps": [
            {"value": null, "color": "green"},
            {"value": 0.1, "color": "yellow"},
            {"value": 0.2, "color": "red"}
          ]
        }
      },
      {
        "title": "Model Accuracy (Rolling 24h)",
        "type": "gauge",
        "targets": [
          {
            "expr": "model_accuracy"
          }
        ],
        "thresholds": {
          "steps": [
            {"value": 0, "color": "red"},
            {"value": 0.85, "color": "yellow"},
            {"value": 0.90, "color": "green"}
          ]
        }
      },
      {
        "title": "Prediction Confidence Distribution",
        "type": "heatmap",
        "targets": [
          {
            "expr": "sum(rate(model_prediction_confidence_bucket[1h])) by (le)"
          }
        ]
      }
    ]
  }
}
```

## Best Practices

1. **Log everything** - predictions, features, latency
2. **Delayed ground truth** - track accuracy over time
3. **Alert tuning** - avoid alert fatigue
4. **Dashboards** - visualize trends
5. **Runbooks** - documented response procedures
'''
    },

    # Node 18: Feature Stores
    {
        "id": "mlops-feature-store",
        "slug": "feature-stores",
        "title": "Feature Stores",
        "order_index": 18,
        "estimated_minutes": 35,
        "xp_reward": 100,
        "difficulty": "hard",
        "node_type": "concept",
        "prerequisites": ["mlops-monitoring"],
        "content": '''# Feature Stores

## Vad är en Feature Store?

```
┌────────────────────────────────────────────────────────────────────┐
│                       Feature Store                                 │
│                                                                     │
│  ┌─────────────┐    ┌─────────────────┐    ┌─────────────┐        │
│  │   Raw Data  │    │   Feature       │    │  Training   │        │
│  │  Sources    │───→│   Engineering   │───→│    Data     │        │
│  └─────────────┘    │   Pipelines     │    └─────────────┘        │
│                     └─────────────────┘            │               │
│                            │                       ▼               │
│                            ▼               ┌─────────────┐        │
│                     ┌─────────────┐        │   Offline   │        │
│                     │   Feature   │        │   Store     │        │
│                     │   Registry  │        │  (Batch)    │        │
│                     └─────────────┘        └─────────────┘        │
│                            │                       │               │
│                            ▼                       ▼               │
│                     ┌─────────────┐        ┌─────────────┐        │
│                     │   Online    │←───────│    Sync     │        │
│                     │   Store     │        │   Process   │        │
│                     │  (Real-time)│        └─────────────┘        │
│                     └─────────────┘                                │
│                            │                                       │
│                            ▼                                       │
│                     ┌─────────────┐                                │
│                     │   Serving   │                                │
│                     │    API      │                                │
│                     └─────────────┘                                │
└────────────────────────────────────────────────────────────────────┘
```

## Feast

### Setup
```python
# feature_store.yaml
project: fraud_detection
registry: data/registry.db
provider: local
online_store:
  type: redis
  connection_string: redis://localhost:6379
offline_store:
  type: file
entity_key_serialization_version: 2
```

### Define Features
```python
from feast import Entity, Feature, FeatureView, FileSource, ValueType
from feast.types import Float32, Int64, String
from datetime import timedelta

# Entity definition
user = Entity(
    name="user_id",
    value_type=ValueType.STRING,
    description="User identifier",
)

merchant = Entity(
    name="merchant_id",
    value_type=ValueType.STRING,
    description="Merchant identifier",
)

# Feature source (offline)
user_stats_source = FileSource(
    name="user_stats_source",
    path="data/user_stats.parquet",
    timestamp_field="event_timestamp",
)

# Feature view
user_stats_fv = FeatureView(
    name="user_stats",
    entities=[user],
    ttl=timedelta(days=1),
    schema=[
        Feature(name="total_transactions_7d", dtype=Int64),
        Feature(name="avg_transaction_amount_7d", dtype=Float32),
        Feature(name="fraud_rate_30d", dtype=Float32),
        Feature(name="account_age_days", dtype=Int64),
        Feature(name="distinct_merchants_7d", dtype=Int64),
    ],
    source=user_stats_source,
    online=True,  # Enable online serving
)

merchant_stats_fv = FeatureView(
    name="merchant_stats",
    entities=[merchant],
    ttl=timedelta(days=1),
    schema=[
        Feature(name="transaction_volume_24h", dtype=Int64),
        Feature(name="avg_ticket_size", dtype=Float32),
        Feature(name="chargeback_rate_30d", dtype=Float32),
        Feature(name="merchant_category", dtype=String),
    ],
    source=merchant_stats_source,
    online=True,
)
```

### Materialize Features
```python
from feast import FeatureStore
from datetime import datetime

store = FeatureStore(repo_path=".")

# Materialize features to online store
store.materialize(
    start_date=datetime(2024, 1, 1),
    end_date=datetime.now(),
)

# Incremental materialization
store.materialize_incremental(end_date=datetime.now())
```

### Get Training Data
```python
from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path=".")

# Training entity dataframe
entity_df = pd.DataFrame({
    "user_id": ["user_1", "user_2", "user_3"],
    "merchant_id": ["merchant_a", "merchant_b", "merchant_c"],
    "event_timestamp": pd.to_datetime([
        "2024-01-15 10:00:00",
        "2024-01-15 11:00:00",
        "2024-01-15 12:00:00",
    ]),
})

# Get historical features (point-in-time correct)
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "user_stats:total_transactions_7d",
        "user_stats:avg_transaction_amount_7d",
        "user_stats:fraud_rate_30d",
        "merchant_stats:chargeback_rate_30d",
        "merchant_stats:avg_ticket_size",
    ],
).to_df()

print(training_df)
```

### Online Serving
```python
from feast import FeatureStore

store = FeatureStore(repo_path=".")

# Real-time feature retrieval
features = store.get_online_features(
    features=[
        "user_stats:total_transactions_7d",
        "user_stats:avg_transaction_amount_7d",
        "user_stats:fraud_rate_30d",
        "merchant_stats:chargeback_rate_30d",
    ],
    entity_rows=[
        {"user_id": "user_123", "merchant_id": "merchant_abc"},
    ],
).to_dict()

print(features)
# {'user_id': ['user_123'],
#  'total_transactions_7d': [42],
#  'avg_transaction_amount_7d': [150.50], ...}
```

## On-Demand Features

```python
from feast import on_demand_feature_view, Field
from feast.types import Float32
import pandas as pd

@on_demand_feature_view(
    sources=[user_stats_fv],
    schema=[
        Field(name="transaction_velocity", dtype=Float32),
        Field(name="risk_score", dtype=Float32),
    ],
)
def user_risk_features(inputs: pd.DataFrame) -> pd.DataFrame:
    """Compute features on-demand at serving time"""

    df = pd.DataFrame()

    # Transaction velocity (transactions per day)
    df["transaction_velocity"] = inputs["total_transactions_7d"] / 7.0

    # Simple risk score
    df["risk_score"] = (
        inputs["fraud_rate_30d"] * 0.5 +
        (inputs["total_transactions_7d"] / 100) * 0.3 +
        (inputs["avg_transaction_amount_7d"] / 1000) * 0.2
    )

    return df
```

## Feature Engineering Patterns

```python
import pandas as pd
from typing import List

class FeatureEngineer:
    """Reusable feature engineering patterns"""

    @staticmethod
    def rolling_aggregates(
        df: pd.DataFrame,
        group_col: str,
        value_col: str,
        windows: List[int],
        timestamp_col: str = "timestamp"
    ) -> pd.DataFrame:
        """Create rolling aggregate features"""

        df = df.sort_values([group_col, timestamp_col])

        for window in windows:
            df[f"{value_col}_sum_{window}d"] = df.groupby(group_col)[value_col].transform(
                lambda x: x.rolling(f'{window}D', on=timestamp_col).sum()
            )
            df[f"{value_col}_mean_{window}d"] = df.groupby(group_col)[value_col].transform(
                lambda x: x.rolling(f'{window}D', on=timestamp_col).mean()
            )
            df[f"{value_col}_std_{window}d"] = df.groupby(group_col)[value_col].transform(
                lambda x: x.rolling(f'{window}D', on=timestamp_col).std()
            )

        return df

    @staticmethod
    def count_encoding(
        df: pd.DataFrame,
        categorical_cols: List[str]
    ) -> pd.DataFrame:
        """Count encoding for categorical features"""

        for col in categorical_cols:
            counts = df[col].value_counts().to_dict()
            df[f"{col}_count"] = df[col].map(counts)

        return df

    @staticmethod
    def target_encoding(
        df: pd.DataFrame,
        categorical_col: str,
        target_col: str,
        smoothing: float = 10.0
    ) -> pd.DataFrame:
        """Target encoding with smoothing"""

        global_mean = df[target_col].mean()

        agg = df.groupby(categorical_col)[target_col].agg(['mean', 'count'])

        # Smoothing to avoid overfitting
        smoothed = (
            agg['count'] * agg['mean'] + smoothing * global_mean
        ) / (agg['count'] + smoothing)

        df[f"{categorical_col}_target_encoded"] = df[categorical_col].map(smoothed)

        return df
```

## Best Practices

1. **Point-in-time correctness** - undvik data leakage
2. **Feature versioning** - spåra feature ändringar
3. **Feature documentation** - metadata och linage
4. **Feature sharing** - återanvänd mellan modeller
5. **Monitoring** - feature drift detection
'''
    },

    # Node 19: AutoML
    {
        "id": "mlops-automl",
        "slug": "automl",
        "title": "AutoML & Neural Architecture Search",
        "order_index": 19,
        "estimated_minutes": 30,
        "xp_reward": 100,
        "difficulty": "hard",
        "node_type": "concept",
        "prerequisites": ["mlops-feature-store"],
        "content": '''# AutoML & Neural Architecture Search

## AutoML Landscape

```
┌─────────────────────────────────────────────────────────────────────┐
│                        AutoML Stack                                  │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                  End-to-End AutoML                           │   │
│  │  (AutoGluon, H2O AutoML, Google AutoML, Azure AutoML)       │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│          ┌───────────────────┼───────────────────┐                  │
│          ▼                   ▼                   ▼                  │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐           │
│  │   Feature     │  │    Model      │  │  Hyperparams  │           │
│  │ Engineering   │  │  Selection    │  │    Tuning     │           │
│  │ (AutoFeat,    │  │ (TPOT, auto-  │  │ (Optuna, Ray  │           │
│  │  Featuretools)│  │  sklearn)     │  │  Tune, Hyperopt│          │
│  └───────────────┘  └───────────────┘  └───────────────┘           │
│                              │                                      │
│                              ▼                                      │
│                     ┌───────────────┐                               │
│                     │Neural Arch    │                               │
│                     │Search (NAS)   │                               │
│                     │(AutoKeras,    │                               │
│                     │ Neural-Net    │                               │
│                     │ Intelligence) │                               │
│                     └───────────────┘                               │
└─────────────────────────────────────────────────────────────────────┘
```

## AutoGluon

```python
from autogluon.tabular import TabularDataset, TabularPredictor

# Load data
train_data = TabularDataset('data/train.csv')
test_data = TabularDataset('data/test.csv')

# Train AutoML
predictor = TabularPredictor(
    label='is_fraud',
    problem_type='binary',
    eval_metric='f1',
    path='autogluon_models/'
).fit(
    train_data,
    time_limit=3600,  # 1 hour
    presets='best_quality',
    excluded_model_types=['NN'],  # Skip neural nets
)

# Evaluate
leaderboard = predictor.leaderboard(test_data)
print(leaderboard)

# Feature importance
importance = predictor.feature_importance(test_data)
print(importance)

# Predictions
predictions = predictor.predict(test_data)
probabilities = predictor.predict_proba(test_data)
```

## H2O AutoML

```python
import h2o
from h2o.automl import H2OAutoML

# Start H2O
h2o.init()

# Load data
train = h2o.import_file("data/train.csv")
test = h2o.import_file("data/test.csv")

# Specify target and features
target = "is_fraud"
features = train.columns
features.remove(target)

# Convert target to factor for classification
train[target] = train[target].asfactor()
test[target] = test[target].asfactor()

# Train AutoML
aml = H2OAutoML(
    max_runtime_secs=3600,
    max_models=20,
    seed=42,
    balance_classes=True,
    stopping_metric="AUC",
    sort_metric="AUC",
)

aml.train(x=features, y=target, training_frame=train)

# Leaderboard
lb = aml.leaderboard
print(lb.head(10))

# Best model
best_model = aml.leader
print(best_model)

# Evaluate on test
performance = best_model.model_performance(test)
print(performance)

# Save model
h2o.save_model(best_model, path="models/")
```

## TPOT (Tree-based Pipeline Optimization)

```python
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Load data
df = pd.read_csv('data/train.csv')
X = df.drop('is_fraud', axis=1)
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Run TPOT
tpot = TPOTClassifier(
    generations=10,
    population_size=50,
    cv=5,
    scoring='f1',
    random_state=42,
    verbosity=2,
    n_jobs=-1,
    early_stop=5,
)

tpot.fit(X_train, y_train)

# Evaluate
print(f"Test score: {tpot.score(X_test, y_test)}")

# Export best pipeline
tpot.export('best_pipeline.py')
```

## AutoKeras (Neural Architecture Search)

```python
import autokeras as ak
import tensorflow as tf

# Structured Data Classifier
clf = ak.StructuredDataClassifier(
    max_trials=20,
    overwrite=True,
    objective='val_f1_score',
)

# Train
clf.fit(
    X_train,
    y_train,
    validation_split=0.15,
    epochs=100,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(patience=10),
    ]
)

# Get best model
best_model = clf.export_model()
best_model.summary()

# Predictions
predictions = clf.predict(X_test)

# Image Classification
image_clf = ak.ImageClassifier(
    max_trials=25,
    overwrite=True,
)

image_clf.fit(
    X_train_images,
    y_train_labels,
    epochs=50,
)

# Text Classification
text_clf = ak.TextClassifier(
    max_trials=10,
    overwrite=True,
)

text_clf.fit(
    X_train_texts,
    y_train_labels,
    epochs=20,
)
```

## Feature Engineering Automation

```python
import featuretools as ft

# Create entity set
es = ft.EntitySet(id="fraud_detection")

# Add entities
es = es.add_dataframe(
    dataframe_name="transactions",
    dataframe=transactions_df,
    index="transaction_id",
    time_index="timestamp",
)

es = es.add_dataframe(
    dataframe_name="users",
    dataframe=users_df,
    index="user_id",
)

# Add relationship
es = es.add_relationship("users", "user_id", "transactions", "user_id")

# Deep Feature Synthesis
feature_matrix, feature_defs = ft.dfs(
    entityset=es,
    target_dataframe_name="transactions",
    max_depth=2,
    agg_primitives=["mean", "sum", "count", "std", "max", "min"],
    trans_primitives=["day", "month", "weekday", "hour"],
    verbose=True,
)

print(f"Generated {len(feature_defs)} features")
print(feature_matrix.head())
```

## Best Practices

1. **Set time limits** - AutoML kan ta lång tid
2. **Holdout set** - validera utanför AutoML
3. **Interpretability** - förstå vad AutoML väljer
4. **Production readiness** - validera edge cases
5. **Cost awareness** - cloud AutoML kan bli dyrt
'''
    },

    # Node 20: Production Best Practices
    {
        "id": "mlops-production",
        "slug": "production-best-practices",
        "title": "Production MLOps Best Practices",
        "order_index": 20,
        "estimated_minutes": 40,
        "xp_reward": 120,
        "difficulty": "hard",
        "node_type": "challenge",
        "prerequisites": ["mlops-automl"],
        "content": '''# Production MLOps Best Practices

## MLOps Maturity Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MLOps Maturity Levels                             │
│                                                                      │
│  Level 0: Manual                                                     │
│  ├── Manual training in notebooks                                   │
│  ├── No pipeline automation                                         │
│  └── Manual deployment                                               │
│                                                                      │
│  Level 1: ML Pipeline Automation                                     │
│  ├── Automated training pipelines                                   │
│  ├── Experiment tracking                                            │
│  └── Continuous training                                             │
│                                                                      │
│  Level 2: CI/CD Pipeline Automation                                  │
│  ├── Automated testing                                               │
│  ├── Automated deployment                                           │
│  └── Model monitoring                                                │
│                                                                      │
│  Level 3: Full MLOps                                                 │
│  ├── A/B testing                                                     │
│  ├── Feature stores                                                  │
│  ├── Automated retraining triggers                                  │
│  └── Full observability                                              │
└─────────────────────────────────────────────────────────────────────┘
```

## Production Checklist

```python
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class CheckStatus(Enum):
    PASSED = "passed"
    FAILED = "failed"
    WARNING = "warning"
    SKIPPED = "skipped"

@dataclass
class ProductionReadinessCheck:
    name: str
    description: str
    status: CheckStatus
    details: str

@dataclass
class ProductionChecklist:
    model_name: str
    version: str
    checks: List[ProductionReadinessCheck] = field(default_factory=list)

    def add_check(self, check: ProductionReadinessCheck):
        self.checks.append(check)

    def is_production_ready(self) -> bool:
        return all(
            check.status in [CheckStatus.PASSED, CheckStatus.WARNING, CheckStatus.SKIPPED]
            for check in self.checks
        )

    def generate_report(self) -> str:
        report = f"# Production Readiness Report\\n"
        report += f"## Model: {self.model_name} v{self.version}\\n\\n"

        for check in self.checks:
            emoji = {
                CheckStatus.PASSED: "✅",
                CheckStatus.FAILED: "❌",
                CheckStatus.WARNING: "⚠️",
                CheckStatus.SKIPPED: "⏭️",
            }[check.status]

            report += f"### {emoji} {check.name}\\n"
            report += f"{check.description}\\n"
            report += f"**Details:** {check.details}\\n\\n"

        return report

def run_production_checks(model_path: str, test_data_path: str) -> ProductionChecklist:
    """Run all production readiness checks"""

    checklist = ProductionChecklist(
        model_name="fraud-detector",
        version="1.2.0"
    )

    # 1. Model Performance Check
    accuracy = evaluate_model(model_path, test_data_path)
    checklist.add_check(ProductionReadinessCheck(
        name="Model Performance",
        description="Model meets minimum accuracy threshold",
        status=CheckStatus.PASSED if accuracy > 0.90 else CheckStatus.FAILED,
        details=f"Accuracy: {accuracy:.4f} (threshold: 0.90)"
    ))

    # 2. Latency Check
    latency_p99 = measure_latency(model_path)
    checklist.add_check(ProductionReadinessCheck(
        name="Inference Latency",
        description="P99 latency under 100ms",
        status=CheckStatus.PASSED if latency_p99 < 100 else CheckStatus.WARNING,
        details=f"P99 latency: {latency_p99:.1f}ms"
    ))

    # 3. Model Size Check
    model_size_mb = get_model_size(model_path)
    checklist.add_check(ProductionReadinessCheck(
        name="Model Size",
        description="Model size suitable for deployment",
        status=CheckStatus.PASSED if model_size_mb < 500 else CheckStatus.WARNING,
        details=f"Model size: {model_size_mb:.1f}MB"
    ))

    # 4. Data Schema Validation
    schema_valid = validate_input_schema(model_path)
    checklist.add_check(ProductionReadinessCheck(
        name="Input Schema",
        description="Input schema is documented and validated",
        status=CheckStatus.PASSED if schema_valid else CheckStatus.FAILED,
        details="Schema validation passed" if schema_valid else "Missing schema definition"
    ))

    # 5. Bias/Fairness Check
    fairness_metrics = run_fairness_audit(model_path, test_data_path)
    checklist.add_check(ProductionReadinessCheck(
        name="Fairness Audit",
        description="Model passes fairness checks",
        status=CheckStatus.PASSED if fairness_metrics['demographic_parity'] > 0.8 else CheckStatus.WARNING,
        details=f"Demographic parity: {fairness_metrics['demographic_parity']:.2f}"
    ))

    # 6. Documentation Check
    has_docs = check_documentation(model_path)
    checklist.add_check(ProductionReadinessCheck(
        name="Documentation",
        description="Model card and API docs exist",
        status=CheckStatus.PASSED if has_docs else CheckStatus.WARNING,
        details="Documentation found" if has_docs else "Missing model card"
    ))

    return checklist
```

## Canary Deployment Strategy

```python
from dataclasses import dataclass
from typing import Dict
import random

@dataclass
class CanaryConfig:
    canary_percentage: float = 5.0
    promotion_threshold: float = 95.0  # Accuracy
    rollback_threshold: float = 85.0
    evaluation_period_minutes: int = 60
    auto_promotion: bool = True

class CanaryDeployer:
    def __init__(self, config: CanaryConfig):
        self.config = config
        self.models = {}
        self.metrics = {"stable": [], "canary": []}

    def deploy_canary(self, canary_model, stable_model):
        """Deploy canary alongside stable model"""
        self.models = {
            "stable": stable_model,
            "canary": canary_model,
        }

    def route_request(self, request) -> str:
        """Route request to appropriate model"""
        if random.random() < self.config.canary_percentage / 100:
            return "canary"
        return "stable"

    def predict(self, request):
        model_version = self.route_request(request)
        model = self.models[model_version]

        prediction = model.predict(request)

        return {
            "prediction": prediction,
            "model_version": model_version,
        }

    def record_feedback(self, model_version: str, correct: bool):
        """Record ground truth feedback"""
        self.metrics[model_version].append(correct)

    def evaluate_canary(self) -> str:
        """Evaluate canary performance"""
        if len(self.metrics["canary"]) < 100:
            return "insufficient_data"

        canary_accuracy = sum(self.metrics["canary"]) / len(self.metrics["canary"])
        stable_accuracy = sum(self.metrics["stable"]) / len(self.metrics["stable"])

        if canary_accuracy < self.config.rollback_threshold / 100:
            return "rollback"

        if canary_accuracy >= self.config.promotion_threshold / 100:
            if canary_accuracy >= stable_accuracy:
                return "promote"

        return "continue"

    def increase_canary_traffic(self, step: float = 10.0):
        """Gradually increase canary traffic"""
        self.config.canary_percentage = min(
            100.0,
            self.config.canary_percentage + step
        )

    def promote_canary(self):
        """Promote canary to stable"""
        self.models["stable"] = self.models["canary"]
        self.config.canary_percentage = 0.0
        self.metrics = {"stable": [], "canary": []}

    def rollback(self):
        """Rollback to stable"""
        del self.models["canary"]
        self.config.canary_percentage = 0.0
        self.metrics["canary"] = []
```

## Incident Response

```python
from enum import Enum
from datetime import datetime
from typing import Optional

class IncidentSeverity(Enum):
    P1 = "critical"  # Full outage
    P2 = "high"      # Major degradation
    P3 = "medium"    # Minor impact
    P4 = "low"       # Cosmetic issues

@dataclass
class MLIncident:
    id: str
    title: str
    severity: IncidentSeverity
    description: str
    detected_at: datetime
    model_name: str
    model_version: str

    # Root cause
    root_cause: Optional[str] = None

    # Resolution
    resolved_at: Optional[datetime] = None
    resolution: Optional[str] = None

    # Post-mortem
    lessons_learned: Optional[str] = None
    action_items: Optional[list] = None

class IncidentRunbook:
    """ML-specific incident response runbook"""

    @staticmethod
    def model_accuracy_drop():
        return """
        ## Runbook: Model Accuracy Drop

        1. **Verify** the drop using multiple metrics sources
        2. **Check** for data drift in recent predictions
        3. **Compare** feature distributions to training data
        4. **Review** recent deployments or changes
        5. **If severe**, trigger automatic rollback

        ### Immediate Actions:
        - [ ] Switch to shadow mode (log predictions, don't serve)
        - [ ] Route traffic to fallback model
        - [ ] Alert on-call ML engineer

        ### Investigation:
        - [ ] Query prediction logs for anomalies
        - [ ] Check upstream data sources
        - [ ] Review feature store for issues
        """

    @staticmethod
    def high_latency():
        return """
        ## Runbook: High Model Latency

        1. **Check** model server resource utilization
        2. **Review** recent traffic patterns
        3. **Inspect** feature retrieval times
        4. **Verify** model size and complexity

        ### Immediate Actions:
        - [ ] Scale up model server instances
        - [ ] Enable request batching
        - [ ] Check for memory leaks

        ### Resolution Options:
        - Reduce model complexity
        - Optimize feature pipeline
        - Add caching layer
        """
```

## Complete MLOps Architecture

```yaml
# mlops-platform.yaml (Kubernetes)
apiVersion: v1
kind: ConfigMap
metadata:
  name: mlops-config
data:
  MLFLOW_TRACKING_URI: "http://mlflow:5000"
  FEAST_ONLINE_STORE: "redis://redis:6379"
  PROMETHEUS_URL: "http://prometheus:9090"
---
# Core services
# - MLflow for experiment tracking & model registry
# - Feast for feature store
# - Airflow for pipeline orchestration
# - Prometheus + Grafana for monitoring
# - Kubeflow for ML pipelines on K8s
```

## Summary

```
Production MLOps =
  Automated Training Pipelines +
  CI/CD for ML +
  Feature Store +
  Model Registry +
  Serving Infrastructure +
  Monitoring & Alerting +
  Incident Response
```

Grattis! Du har slutfört MLOps SkillsMap! 🎉
'''
    },
]
