"""
MLOps SkillsMap - Block 5: Advanced MLOps
Nodes 17-20: Monitoring, A/B Testing, Feature Stores, ML Platform
"""

BLOCK_5_NODES = [
    # Node 17: Model Monitoring
    {
        "id": "mlops-monitoring",
        "slug": "model-monitoring",
        "title": "Model Monitoring och Observability",
        "order_index": 17,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["mlops-containers"],
        "content": '''# Model Monitoring och Observability

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor model monitoring ar viktigt |
|----------|-----------------------------------|
| **Model Drift** | Modellprestanda forsamras over tid |
| **Data Drift** | Indata andras fran traningsdata |
| **Incidents** | Snabb detektion av problem |
| **Compliance** | Spara predictions for audit |

Du maste forsta:

- **Drift detection** - nar modeller forsamras
- **Metrics** - vad man ska overvaka
- **Alerting** - nar och hur man larmar

------------------------------------------------------------

## Monitoring Architecture

```
+---------------------------------------------------------------------+
|                     ML Monitoring Stack                              |
+---------------------------------------------------------------------+
|                                                                      |
|  +--------------+   +--------------+   +--------------+            |
|  |   Model      |   |   Feature    |   |    Ground    |            |
|  | Predictions  |   |   Values     |   |    Truth     |            |
|  +------+-------+   +------+-------+   +------+-------+            |
|         |                  |                  |                     |
|         +------------------+------------------+                     |
|                            |                                        |
|                            ▼                                        |
|                   +----------------+                                |
|                   |  Monitoring    |                                |
|                   |    Service     |                                |
|                   +--------+-------+                                |
|                            |                                        |
|         +------------------+------------------+                     |
|         |                  |                  |                     |
|         ▼                  ▼                  ▼                     |
|  +------------+    +------------+    +------------+                |
|  | Prometheus |    |   Grafana  |    |  PagerDuty |                |
|  |  Metrics   |    | Dashboards |    |   Alerts   |                |
|  +------------+    +------------+    +------------+                |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Drift Detection

```python
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset

def detect_drift(reference_data, current_data):
    """Detect data and prediction drift"""

    column_mapping = ColumnMapping(
        target='fraud',
        prediction='prediction',
        numerical_features=['amount', 'age'],
        categorical_features=['merchant_category']
    )

    report = Report(metrics=[
        DataDriftPreset(),
        TargetDriftPreset(),
    ])

    report.run(
        reference_data=reference_data,
        current_data=current_data,
        column_mapping=column_mapping
    )

    # Check if drift detected
    result = report.as_dict()
    data_drift = result['metrics'][0]['result']['dataset_drift']

    if data_drift:
        alert_team("Data drift detected!")
        trigger_retraining()

    return report
```

------------------------------------------------------------

## Prometheus Metrics

```python
from prometheus_client import Counter, Histogram, Gauge, Summary

# Prediction metrics
PREDICTIONS_TOTAL = Counter(
    'model_predictions_total',
    'Total number of predictions',
    ['model_name', 'model_version', 'result']
)

PREDICTION_LATENCY = Histogram(
    'model_prediction_latency_seconds',
    'Prediction latency in seconds',
    ['model_name'],
    buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0]
)

# Model performance metrics
MODEL_ACCURACY = Gauge(
    'model_accuracy',
    'Current model accuracy',
    ['model_name', 'model_version']
)

FEATURE_DRIFT = Gauge(
    'feature_drift_score',
    'Feature drift score',
    ['model_name', 'feature_name']
)

# Example usage
@app.post("/predict")
async def predict(request: PredictionRequest):
    start_time = time.time()

    prediction = model.predict(request.features)

    # Record metrics
    PREDICTIONS_TOTAL.labels(
        model_name='fraud_detector',
        model_version='v1.2',
        result='fraud' if prediction > 0.5 else 'legitimate'
    ).inc()

    PREDICTION_LATENCY.labels(
        model_name='fraud_detector'
    ).observe(time.time() - start_time)

    return {"prediction": prediction}
```

------------------------------------------------------------

## Snabbreferens

| Metric | Beskrivning |
|--------|-------------|
| **Data Drift** | Forandring i input-distribution |
| **Concept Drift** | Forandring i relationen input-output |
| **Prediction Drift** | Forandring i predictions |
| **Latency** | Tid for inference |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Missed drift | For lag threshold | Justera sensitivity |
| False alerts | For hog sensitivity | Lagg till bekraftelse |
| Missing ground truth | Labels ej tillgangliga | Proxy metrics |
| Metric gaps | Saknade datapunkter | Backfill eller interpolera |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Drift detection** | Kritiskt for produktionsmodeller |
| **Multi-layer monitoring** | Data, modell, och system |
| **Automated alerts** | Snabb respons pa problem |
| **Ground truth** | Viktig for att mata verklig prestanda |

**Kom ihag:**

- Overvaka bade data och modellprestanda
- Ha baseline fran traning
- Automatisera retraining vid drift
- Logga allt for debugging
'''
    },

    # Node 18: A/B Testing & Experimentation
    {
        "id": "mlops-experimentation",
        "slug": "ml-experimentation",
        "title": "A/B Testing och Experimentation",
        "order_index": 18,
        "estimated_minutes": 35,
        "xp_reward": 100,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["mlops-monitoring"],
        "content": '''# A/B Testing och Experimentation

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor A/B testing ar viktigt |
|----------|------------------------------|
| **Model comparison** | Jamfor modellversioner i produktion |
| **Risk mitigation** | Gradvis utrullning av nya modeller |
| **Data-driven decisions** | Beslut baserade pa verklig data |
| **Continuous improvement** | Iterativ forbattring |

Du maste forsta:

- **Experiment design** - hur man satter upp tester
- **Statistical significance** - nar resultat ar tillforlitliga
- **Traffic splitting** - hur man fordelar trafik

------------------------------------------------------------

## Experiment Architecture

```
+---------------------------------------------------------------------+
|                     A/B Testing Flow                                 |
+---------------------------------------------------------------------+
|                                                                      |
|                        +--------------+                             |
|      Request ---------▶|   Router     |                             |
|                        +------+-------+                             |
|                               |                                      |
|              +----------------+----------------+                    |
|              |                |                |                     |
|              ▼                ▼                ▼                     |
|       +----------+     +----------+     +----------+               |
|       | Model A  |     | Model B  |     | Model C  |               |
|       |  (80%)   |     |  (15%)   |     |  (5%)    |               |
|       +----+-----+     +----+-----+     +----+-----+               |
|            |                |                |                       |
|            +----------------+----------------+                      |
|                             |                                        |
|                             ▼                                        |
|                     +--------------+                                |
|                     |  Experiment  |                                |
|                     |   Logger     |                                |
|                     +--------------+                                |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Implementation

```python
import hashlib
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class Experiment:
    name: str
    variants: Dict[str, float]  # variant_name -> traffic_percentage

class ExperimentRouter:
    def __init__(self):
        self.experiments: Dict[str, Experiment] = {}

    def add_experiment(self, experiment: Experiment):
        self.experiments[experiment.name] = experiment

    def get_variant(self, experiment_name: str, user_id: str) -> str:
        """Deterministically assign user to variant"""
        experiment = self.experiments[experiment_name]

        # Hash user_id for consistent assignment
        hash_input = f"{experiment_name}:{user_id}"
        hash_value = int(hashlib.md5(hash_input.encode()).hexdigest(), 16)
        bucket = hash_value % 100

        cumulative = 0
        for variant, percentage in experiment.variants.items():
            cumulative += percentage * 100
            if bucket < cumulative:
                return variant

        return list(experiment.variants.keys())[0]

# Usage
router = ExperimentRouter()
router.add_experiment(Experiment(
    name="fraud_model_v2",
    variants={"control": 0.8, "treatment": 0.2}
))

variant = router.get_variant("fraud_model_v2", user_id="user123")
```

------------------------------------------------------------

## Statistical Analysis

```python
from scipy import stats
import numpy as np

def analyze_experiment(control_metrics, treatment_metrics):
    """Analyze A/B test results"""

    # Calculate means
    control_mean = np.mean(control_metrics)
    treatment_mean = np.mean(treatment_metrics)

    # T-test for statistical significance
    t_stat, p_value = stats.ttest_ind(control_metrics, treatment_metrics)

    # Effect size (Cohen's d)
    pooled_std = np.sqrt(
        (np.std(control_metrics)**2 + np.std(treatment_metrics)**2) / 2
    )
    effect_size = (treatment_mean - control_mean) / pooled_std

    # Confidence interval
    ci = stats.t.interval(
        0.95,
        len(treatment_metrics) - 1,
        loc=treatment_mean - control_mean,
        scale=stats.sem(treatment_metrics - control_metrics)
    )

    return {
        "control_mean": control_mean,
        "treatment_mean": treatment_mean,
        "lift": (treatment_mean - control_mean) / control_mean,
        "p_value": p_value,
        "significant": p_value < 0.05,
        "effect_size": effect_size,
        "confidence_interval": ci
    }
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Control** | Befintlig modell/baseline |
| **Treatment** | Ny modell att testa |
| **p-value** | Sannolikhet att resultatet ar slump |
| **Effect size** | Storlek pa skillnaden |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Not significant | For fa samples | Oka sample size |
| Selection bias | Ej slumpmassigt | Anvand hash-baserad tilldelning |
| Novelty effect | Tidigt beteende | Vanta langre |
| Interaction effects | Multipla experiment | Isolera experiment |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Statistical rigor** | Vanta pa signifikans |
| **Consistent assignment** | Anvandare far alltid samma variant |
| **Proper logging** | Logga allt for analys |
| **Gradual rollout** | Oka trafik gradvis |

**Kom ihag:**

- Definiera hypotes fore testet
- Bestam sample size i forvag
- Kor test tillrackligt lange
- Ha tydliga success metrics
'''
    },

    # Node 19: Feature Stores
    {
        "id": "mlops-feature-store",
        "slug": "feature-stores",
        "title": "Feature Stores",
        "order_index": 19,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["mlops-experimentation"],
        "content": '''# Feature Stores

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor feature stores ar viktigt |
|----------|----------------------------------|
| **Feature reuse** | Dela features mellan modeller |
| **Consistency** | Samma features i training och serving |
| **Point-in-time** | Undvik data leakage |
| **Discoverability** | Hitta befintliga features |

Du maste forsta:

- **Online vs Offline** - olika servingbehov
- **Feature engineering** - transformera radata
- **Time travel** - historiska feature-varden

------------------------------------------------------------

## Feature Store Architecture

```
+---------------------------------------------------------------------+
|                     Feature Store Architecture                       |
+---------------------------------------------------------------------+
|                                                                      |
|  +--------------+                                                   |
|  |  Raw Data    |                                                   |
|  |  Sources     |                                                   |
|  +------+-------+                                                   |
|         |                                                           |
|         ▼                                                           |
|  +----------------------------------------------------------+      |
|  |              Feature Engineering Pipeline                  |      |
|  |  +---------+  +---------+  +---------+  +---------+     |      |
|  |  |Transform|-▶|Aggregate|-▶| Validate|-▶|  Store  |     |      |
|  |  +---------+  +---------+  +---------+  +---------+     |      |
|  +----------------------------------------------------------+      |
|                              |                                       |
|              +---------------+---------------+                      |
|              |               |               |                       |
|              ▼               ▼               ▼                       |
|      +-------------+ +-------------+ +-------------+               |
|      |   Offline   | |   Online    | |  Registry   |               |
|      |    Store    | |   Store     | |  (Metadata) |               |
|      |  (S3/GCS)   | |  (Redis)    | |             |               |
|      +------+------+ +------+------+ +-------------+               |
|             |               |                                        |
|      +------+------+ +------+------+                                |
|      |  Training   | |  Serving    |                                |
|      |   (Batch)   | |  (Online)   |                                |
|      +-------------+ +-------------+                                |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Feast Example

```python
from feast import FeatureStore, Entity, Feature, FeatureView
from feast import FileSource
from datetime import timedelta

# Define entity
user = Entity(
    name="user_id",
    value_type=ValueType.STRING,
    description="User identifier"
)

# Define data source
user_stats_source = FileSource(
    path="data/user_stats.parquet",
    event_timestamp_column="event_timestamp",
)

# Define feature view
user_stats_fv = FeatureView(
    name="user_stats",
    entities=["user_id"],
    ttl=timedelta(days=1),
    features=[
        Feature(name="total_transactions", dtype=ValueType.INT64),
        Feature(name="avg_transaction_amount", dtype=ValueType.FLOAT),
        Feature(name="days_since_first_transaction", dtype=ValueType.INT64),
    ],
    online=True,
    source=user_stats_source,
)

# Initialize store
store = FeatureStore(repo_path=".")

# Get online features (for serving)
features = store.get_online_features(
    features=["user_stats:total_transactions", "user_stats:avg_transaction_amount"],
    entity_rows=[{"user_id": "user123"}]
).to_dict()

# Get historical features (for training)
training_df = store.get_historical_features(
    entity_df=entity_df,  # DataFrame with user_id and timestamps
    features=["user_stats:total_transactions", "user_stats:avg_transaction_amount"],
).to_df()
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Offline Store** | Historiska features for training |
| **Online Store** | Low-latency features for serving |
| **Feature View** | Logisk gruppering av features |
| **TTL** | Time-to-live for cached features |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Training-serving skew | Olika feature logic | Anvand feature store |
| Data leakage | Point-in-time fel | Korrekt timestamp join |
| Stale features | Gammal data i online store | Minska TTL, oka refresh |
| Missing features | Entity ej i store | Handle gracefully |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Consistency** | Samma features i training och serving |
| **Reuse** | Dela features mellan team/modeller |
| **Point-in-time** | Undvik framtida data i training |
| **Discovery** | Katalog over tillgangliga features |

**Kom ihag:**

- Feature stores loser training-serving skew
- Dokumentera features for discoverability
- Overvaka feature freshness
- Ha fallback for missing features
'''
    },

    # Node 20: ML Platform Design
    {
        "id": "mlops-platform",
        "slug": "ml-platform-design",
        "title": "ML Platform Design",
        "order_index": 20,
        "estimated_minutes": 45,
        "xp_reward": 120,
        "difficulty": "hard",
        "node_type": "concept",
        "prerequisites": ["mlops-feature-store"],
        "content": '''# ML Platform Design

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor ML platform ar viktigt |
|----------|------------------------------|
| **Skalning** | Fran 1 till 100+ modeller |
| **Standardisering** | Konsekvent process for alla team |
| **Efficiency** | Reducera tid till produktion |
| **Governance** | Compliance och spårbarhet |

Du maste forsta:

- **Platform components** - vad som behovs
- **Build vs Buy** - nar man bygger sjalv
- **Team structure** - hur man organiserar

------------------------------------------------------------

## Platform Architecture

```
+---------------------------------------------------------------------+
|                     ML PLATFORM OVERVIEW                             |
+---------------------------------------------------------------------+
|                                                                      |
|  +-------------------------------------------------------------+   |
|  |                    Developer Experience                       |   |
|  |  +---------+  +---------+  +---------+  +---------+        |   |
|  |  |Notebooks|  |   CLI   |  |   SDK   |  |   UI    |        |   |
|  |  +---------+  +---------+  +---------+  +---------+        |   |
|  +-------------------------------------------------------------+   |
|                                                                      |
|  +-------------------------------------------------------------+   |
|  |                    Platform Services                          |   |
|  |  +-----------+ +-----------+ +-----------+ +-----------+   |   |
|  |  | Experiment | |  Feature  | |   Model   | |  Serving  |   |   |
|  |  |  Tracking | |   Store   | | Registry  | |  Gateway  |   |   |
|  |  +-----------+ +-----------+ +-----------+ +-----------+   |   |
|  |  +-----------+ +-----------+ +-----------+ +-----------+   |   |
|  |  |  Pipeline | |Monitoring | | Data Catalog| |  Compute  |   |   |
|  |  |Orchestrator| |& Alerting | |           | | Management|   |   |
|  |  +-----------+ +-----------+ +-----------+ +-----------+   |   |
|  +-------------------------------------------------------------+   |
|                                                                      |
|  +-------------------------------------------------------------+   |
|  |                    Infrastructure                             |   |
|  |  +-----------+ +-----------+ +-----------+ +-----------+   |   |
|  |  |Kubernetes | |  Object   | |  Message  | |  Secrets  |   |   |
|  |  |  Cluster  | |  Storage  | |   Queue   | |Management |   |   |
|  |  +-----------+ +-----------+ +-----------+ +-----------+   |   |
|  +-------------------------------------------------------------+   |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Component Selection

| Component | Open Source | Managed |
|-----------|-------------|---------|
| **Experiment Tracking** | MLflow, Aim | Weights & Biases, Neptune |
| **Feature Store** | Feast, Hopsworks | Tecton, Databricks |
| **Pipeline Orchestration** | Airflow, Kubeflow | Vertex AI, SageMaker |
| **Model Registry** | MLflow | Vertex AI, SageMaker |
| **Serving** | KServe, Seldon | SageMaker, Vertex AI |
| **Monitoring** | Evidently, WhyLabs | Arize, Fiddler |

------------------------------------------------------------

## Maturity Model

```
+---------------------------------------------------------------------+
|                     ML MATURITY LEVELS                               |
+---------------------------------------------------------------------+
|                                                                      |
|  Level 0: Manual                                                     |
|  +-- Ad-hoc experiments                                              |
|  +-- Manual deployments                                              |
|  +-- No version control for models                                   |
|                                                                      |
|  Level 1: ML Pipeline Automation                                     |
|  +-- Automated training pipelines                                    |
|  +-- Experiment tracking                                             |
|  +-- Model versioning                                                |
|                                                                      |
|  Level 2: CI/CD for ML                                               |
|  +-- Automated testing (data, model)                                 |
|  +-- Continuous training                                             |
|  +-- Automated deployment                                            |
|                                                                      |
|  Level 3: Full MLOps                                                 |
|  +-- Feature store                                                   |
|  +-- Model monitoring & drift detection                              |
|  +-- Automated retraining                                            |
|  +-- A/B testing & experimentation                                   |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Team Structure

| Team | Ansvar |
|------|--------|
| **ML Platform** | Infrastruktur och verktyg |
| **Data Engineering** | Data pipelines och kvalitet |
| **ML Engineering** | Modeller i produktion |
| **Data Science** | Experiment och utveckling |

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **ML Platform** | Infrastruktur for ML-livscykeln |
| **Golden Path** | Rekommenderad vag till produktion |
| **Self-service** | Team kan deploya sjalva |
| **Guardrails** | Automatiska kvalitetskontroller |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Overengineering | For mycket for tidigt | Borja med basics |
| Tool sprawl | For manga verktyg | Standardisera |
| Adoption issues | For komplex | Fokusera pa UX |
| Silos | Team jobbar isolerat | Gemensam platform |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Start simple** | Bygg pa behov, inte speculation |
| **Developer experience** | Gor det latt att gora ratt |
| **Standardization** | Konsekvent process for alla |
| **Automation** | Automatisera allt som gar |

**Kom ihag:**

- Platform ar en produkt - behandla users som kunder
- Maturity tar tid - iterera gradvis
- Buy vs build - vara realistisk om resurser
- Dokumentation ar kritiskt for adoption
'''
    },
]
