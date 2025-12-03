"""
Mlops - Bootcamp v3 Format
Auto-converted from skillsmap format.

Track: advanced-specialty
Tasks: 20
Estimated Hours: 10.0
"""

MODULE_MLOPS = {
    "track_slug": "advanced-specialty",
    "order_index": 100,
    "name": "Mlops",
    "slug": "mlops",
    "description": """Master Mlops from fundamentals to production""",
    "difficulty": "intermediate",
    "estimated_hours": 10.0,
    "prerequisites": [],
    "tasks": [
            {
                "title": "Introduction to MLOps",
                "difficulty": "easy",
                "estimated_minutes": 25,
                "xp_reward": 50,
                "content": r"""# Introduction to MLOps

## Vad är MLOps?

MLOps (Machine Learning Operations) är praktiker och verktyg för att automatisera och effektivisera hela ML-livscykeln - från experiment till produktion.

## Varför MLOps?

### Utan MLOps (ML-skuld)
```
┌─────────────────────────────────────────────────────────┐
│  Data Scientist's Laptop                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │ Notebook    │→ │ model.pkl   │→ │ "It works!" │     │
│  │ experiment  │  │ (local)     │  │             │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│                                                         │
│  Månader senare: "Vilken version? Vilken data?"        │
└─────────────────────────────────────────────────────────┘
```

### Med MLOps
```
┌─────────────────────────────────────────────────────────┐
│                    MLOps Pipeline                        │
│                                                          │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────────┐    │
│  │ Data   │→ │ Train  │→ │ Test   │→ │ Deploy     │    │
│  │ Ingest │  │ Model  │  │ Valid. │  │ Monitor    │    │
│  └────────┘  └────────┘  └────────┘  └────────────┘    │
│       │          │           │             │            │
│       ▼          ▼           ▼             ▼            │
│  ┌─────────────────────────────────────────────────┐   │
│  │        Version Control + Experiment Tracking     │   │
│  │        Model Registry + Feature Store            │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## MLOps Maturity Levels

### Level 0: Manual
- Jupyter notebooks
- Manuell deployment
- Ingen versionshantering av modeller
- Ingen automatiserad testning

### Level 1: ML Pipeline Automation
- Automatiserade tränings-pipelines
- Experiment tracking
- Model registry
- Continuous Training (CT)

### Level 2: CI/CD Pipeline Automation
- Automatiserad CI/CD för ML
- A/B-testning
- Continuous Monitoring
- Automated retraining

## MLOps vs DevOps

| Aspekt | DevOps | MLOps |
|--------|--------|-------|
| **Artefakt** | Code | Code + Data + Model |
| **Testning** | Unit/Integration | + Data validation, Model validation |
| **Deployment** | Application | Model serving |
| **Monitoring** | App metrics | + Data drift, Model drift |
| **Versioning** | Code | Code + Data + Model |

## MLOps Komponenter

```
┌─────────────────────────────────────────────────────────┐
│                     MLOps Stack                          │
├─────────────────────────────────────────────────────────┤
│  Monitoring     │ Prometheus, Grafana, Evidently AI     │
├─────────────────────────────────────────────────────────┤
│  Model Serving  │ TensorFlow Serving, Seldon, KServe    │
├─────────────────────────────────────────────────────────┤
│  Orchestration  │ Airflow, Kubeflow, Prefect, Dagster   │
├─────────────────────────────────────────────────────────┤
│  Experiment     │ MLflow, Weights & Biases, Neptune     │
│  Tracking       │                                       │
├─────────────────────────────────────────────────────────┤
│  Feature Store  │ Feast, Tecton, Hopsworks              │
├─────────────────────────────────────────────────────────┤
│  Data Pipeline  │ Spark, dbt, Airflow, Kafka            │
├─────────────────────────────────────────────────────────┤
│  Infrastructure │ Kubernetes, Docker, Terraform         │
└─────────────────────────────────────────────────────────┘
```

## Karriärvägar i MLOps

1. **ML Engineer** - Fokus på modellträning och optimering
2. **MLOps Engineer** - Fokus på infrastruktur och pipelines
3. **Data Engineer** - Fokus på data pipelines
4. **Platform Engineer** - Bygger ML-plattformar

## Praktisk övning

Identifiera MLOps-mognadsnivån för ett projekt:

```python
def assess_mlops_maturity():
    checklist = {
        "level_0": [
            "Manual model training",
            "No version control for models",
            "Manual deployment",
        ],
        "level_1": [
            "Automated training pipeline",
            "Experiment tracking (MLflow etc)",
            "Model registry",
            "Continuous Training",
        ],
        "level_2": [
            "CI/CD for ML pipelines",
            "Automated testing (data + model)",
            "Continuous monitoring",
            "Automated retraining triggers",
        ],
    }

    # Evaluate your project
    for level, items in checklist.items():
        print(f"\n{level.upper()}:")
        for item in items:
            status = "✅" if check_item(item) else "❌"
            print(f"  {status} {item}")
```

## Nästa steg

I denna SkillsMap kommer du lära dig:
1. **Data Engineering** - Pipelines och Feature Stores
2. **ML Fundamentals** - Träning och experiment tracking
3. **MLOps Core** - CI/CD och orchestration
4. **Production** - Monitoring och scaling
"""
            },
            {
                "title": "Python for Machine Learning",
                "difficulty": "easy",
                "estimated_minutes": 35,
                "xp_reward": 75,
                "content": r"""# Python for Machine Learning

## Förutsättningar

Du bör redan kunna grundläggande Python. Här fokuserar vi på ML-specifika bibliotek och mönster.

## ML Python Stack

```
┌─────────────────────────────────────────────────────────┐
│                    ML Python Ecosystem                   │
├─────────────────────────────────────────────────────────┤
│  Deep Learning  │ PyTorch, TensorFlow, JAX              │
├─────────────────────────────────────────────────────────┤
│  ML Frameworks  │ scikit-learn, XGBoost, LightGBM       │
├─────────────────────────────────────────────────────────┤
│  Data Proc.     │ Pandas, NumPy, Polars, Dask           │
├─────────────────────────────────────────────────────────┤
│  Visualization  │ Matplotlib, Seaborn, Plotly           │
├─────────────────────────────────────────────────────────┤
│  MLOps Tools    │ MLflow, DVC, Hydra, ONNX              │
└─────────────────────────────────────────────────────────┘
```

## Environment Management

### pyproject.toml (Rekommenderat)
```toml
[project]
name = "ml-project"
version = "1.0.0"
requires-python = ">=3.10"

dependencies = [
    "numpy>=1.24.0",
    "pandas>=2.0.0",
    "scikit-learn>=1.3.0",
    "torch>=2.0.0",
    "mlflow>=2.8.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
]

[tool.ruff]
line-length = 100
select = ["E", "F", "I"]
```

### UV (Snabb pakethanterare)
```bash
# Installera UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Skapa virtuell miljö
uv venv

# Installera dependencies
uv pip install -r requirements.txt

# Sync från pyproject.toml
uv pip sync
```

## NumPy Essentials

```python
import numpy as np

# Vektoroperationer (snabbare än Python-loopar)
X = np.random.randn(1000, 10)  # 1000 samples, 10 features
y = np.random.randint(0, 2, 1000)  # Binary labels

# Broadcasting - automatisk dimension-matchning
weights = np.array([0.1, 0.2, 0.3])
data = np.array([[1, 2, 3], [4, 5, 6]])
result = data * weights  # Varje rad multipliceras med weights

# Effektiva operationer
mean = X.mean(axis=0)  # Medelvärde per kolumn
std = X.std(axis=0)    # Standardavvikelse per kolumn
X_normalized = (X - mean) / std  # Normalisering

# Matrix operationer
W = np.random.randn(10, 5)  # Weight matrix
output = X @ W  # Matrix multiplication
```

## Pandas för Data Prep

```python
import pandas as pd

# Ladda och inspektera data
df = pd.read_csv("data/training_data.csv")
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Feature engineering pipeline
def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    '''Reproducerbar feature engineering'''
    df = df.copy()

    # Hantera missing values
    df['age'] = df['age'].fillna(df['age'].median())

    # Skapa nya features
    df['age_bucket'] = pd.cut(df['age'], bins=[0, 18, 35, 50, 100],
                              labels=['young', 'adult', 'middle', 'senior'])

    # One-hot encoding
    df = pd.get_dummies(df, columns=['category'], prefix='cat')

    # Log-transform skewed features
    df['income_log'] = np.log1p(df['income'])

    return df

# Applicera pipeline
df_processed = prepare_features(df)
```

## Scikit-learn Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score

# Definiera features
numeric_features = ['age', 'income', 'credit_score']
categorical_features = ['occupation', 'education']

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# Full pipeline med modell
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Träna och evaluera
pipeline.fit(X_train, y_train)
scores = cross_val_score(pipeline, X_train, y_train, cv=5)
print(f"CV Score: {scores.mean():.3f} (+/- {scores.std():.3f})")

# Spara pipeline
import joblib
joblib.dump(pipeline, 'models/pipeline.joblib')
```

## PyTorch Basics

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

# Device setup
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Enkel neural network
class SimpleNN(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.layers(x)

# Training loop
def train_model(model, train_loader, criterion, optimizer, epochs=10):
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for batch_X, batch_y in train_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)

            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(train_loader)
        print(f"Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.4f}")
```

## Type Hints för ML-kod

```python
from typing import Tuple, Optional
import numpy as np
import pandas as pd
from numpy.typing import NDArray

def prepare_data(
    df: pd.DataFrame,
    target_col: str,
    test_size: float = 0.2
) -> Tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.int64], NDArray[np.int64]]:
    '''Prepare data for ML training with proper type hints'''
    X = df.drop(columns=[target_col]).values
    y = df[target_col].values

    # Split data
    from sklearn.model_selection import train_test_split
    return train_test_split(X, y, test_size=test_size, random_state=42)
```

## Nästa steg

Med solid Python-grund går vi vidare till:
- Git och versionshantering för ML
- Cloud computing för ML-workloads
- Containerisering av ML-modeller
"""
            },
            {
                "title": "Version Control for ML",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 75,
                "content": r"""# Version Control for ML

## Varför är ML-versionshantering speciell?

```
Traditional Software:
  Code → Application

Machine Learning:
  Code + Data + Config + Model → ML System

  Alla måste versionshanteras!
```

## Git för ML-projekt

### Rekommenderad projektstruktur
```
ml-project/
├── .git/
├── .gitignore
├── .dvc/                    # DVC config
├── pyproject.toml
├── README.md
├── configs/                 # Hydra/YAML configs
│   ├── config.yaml
│   ├── model/
│   │   ├── random_forest.yaml
│   │   └── xgboost.yaml
│   └── data/
│       └── preprocessing.yaml
├── data/
│   ├── raw/                 # → Tracked by DVC
│   ├── processed/           # → Tracked by DVC
│   └── .gitkeep
├── models/                  # → Tracked by DVC
│   └── .gitkeep
├── notebooks/               # Exploratory notebooks
│   └── eda.ipynb
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── preprocessing.py
│   ├── features/
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train.py
│   │   └── predict.py
│   └── evaluation/
│       ├── __init__.py
│       └── metrics.py
├── tests/
│   ├── test_data.py
│   └── test_model.py
└── dvc.yaml                 # DVC pipeline
```

### .gitignore för ML
```gitignore
# Data och modeller (hanteras av DVC)
data/raw/
data/processed/
models/*.pkl
models/*.pt
models/*.onnx

# Experiment outputs
outputs/
mlruns/
wandb/

# Notebooks checkpoints
.ipynb_checkpoints/

# Python
__pycache__/
*.py[cod]
.venv/
venv/

# IDE
.vscode/
.idea/

# System
.DS_Store
```

## DVC - Data Version Control

### Installation och setup
```bash
# Installera DVC
pip install dvc dvc-s3  # eller dvc-gcs, dvc-azure

# Initiera i git-repo
dvc init

# Konfigurera remote storage
dvc remote add -d myremote s3://my-bucket/dvc-storage
```

### Versionhantera data och modeller
```bash
# Lägg till data under DVC
dvc add data/raw/training_data.csv
# Skapar: data/raw/training_data.csv.dvc

# Git-committa .dvc-filen (inte datan!)
git add data/raw/training_data.csv.dvc data/raw/.gitignore
git commit -m "Add training data v1"

# Pusha data till remote
dvc push

# Andra kan hämta datan
git pull
dvc pull
```

### DVC Pipeline
```yaml
# dvc.yaml
stages:
  prepare:
    cmd: python src/data/preprocessing.py
    deps:
      - src/data/preprocessing.py
      - data/raw/training_data.csv
    outs:
      - data/processed/train.csv
      - data/processed/test.csv
    params:
      - preprocessing.test_size
      - preprocessing.random_state

  train:
    cmd: python src/models/train.py
    deps:
      - src/models/train.py
      - data/processed/train.csv
    outs:
      - models/model.pkl
    params:
      - model.type
      - model.hyperparameters
    metrics:
      - metrics/train_metrics.json:
          cache: false

  evaluate:
    cmd: python src/evaluation/evaluate.py
    deps:
      - src/evaluation/evaluate.py
      - models/model.pkl
      - data/processed/test.csv
    metrics:
      - metrics/test_metrics.json:
          cache: false
    plots:
      - plots/confusion_matrix.png
```

### Kör pipeline
```bash
# Kör hela pipelinen
dvc repro

# Se DAG
dvc dag

# Jämför metrics mellan branches
dvc metrics diff

# Se experiment-resultat
dvc exp show
```

## Git Branching för ML

### Rekommenderad strategi
```
main
  │
  ├── develop
  │     │
  │     ├── feature/new-feature-engineering
  │     │
  │     ├── experiment/xgboost-tuning
  │     │     (kan mergas om bättre metrics)
  │     │
  │     └── experiment/transformer-model
  │           (kasta om dåliga resultat)
  │
  └── release/v1.2
```

### Experiment tracking i Git
```bash
# Skapa experiment-branch
git checkout -b experiment/bert-embeddings

# Kör experiment
python train.py

# Spara resultat
git add metrics/ models/*.dvc
git commit -m "exp: BERT embeddings - accuracy 0.92"

# Jämför med main
git diff main -- metrics/
dvc metrics diff main

# Om bra resultat → merge
git checkout develop
git merge experiment/bert-embeddings
```

## Semantic Versioning för Modeller

```
model-name-v{MAJOR}.{MINOR}.{PATCH}

MAJOR: Breaking API changes, ny modellarkitektur
MINOR: Ny träningsdata, hyperparameter-tuning
PATCH: Bugfixar, minor improvements

Exempel:
  fraud-detector-v1.0.0  # Initial release
  fraud-detector-v1.1.0  # Trained on new data
  fraud-detector-v1.1.1  # Fixed preprocessing bug
  fraud-detector-v2.0.0  # Changed from RF to XGBoost
```

## Praktiskt exempel

```bash
# 1. Setup nytt ML-projekt
mkdir ml-project && cd ml-project
git init
dvc init

# 2. Lägg till data
dvc add data/raw/dataset.csv
git add data/raw/dataset.csv.dvc .gitignore
git commit -m "Add initial dataset"

# 3. Skapa experiment
git checkout -b experiment/baseline

# 4. Träna modell
python train.py --model random_forest

# 5. Spara resultat
dvc add models/model.pkl
git add models/model.pkl.dvc metrics/
git commit -m "exp: baseline RF model - acc 0.85"

# 6. Prova ny approach
git checkout -b experiment/xgboost
python train.py --model xgboost

# 7. Jämför
dvc metrics diff experiment/baseline
# accuracy: 0.85 → 0.91

# 8. Merge bästa experiment
git checkout main
git merge experiment/xgboost
```

## Nästa steg

Med versionshantering på plats går vi vidare till:
- Cloud computing för ML
- Containerisering av modeller
"""
            },
            {
                "title": "Cloud Computing for ML",
                "difficulty": "medium",
                "estimated_minutes": 35,
                "xp_reward": 100,
                "content": r"""# Cloud Computing for ML

## Varför Cloud för ML?

```
┌─────────────────────────────────────────────────────────┐
│  Local Development         Cloud Training               │
│  ┌─────────────────┐       ┌─────────────────┐         │
│  │ Laptop GPU      │       │ 8x A100 80GB    │         │
│  │ 8GB VRAM        │       │ 640GB VRAM      │         │
│  │ Days to train   │   →   │ Hours to train  │         │
│  │ $2000 hardware  │       │ Pay per use     │         │
│  └─────────────────┘       └─────────────────┘         │
└─────────────────────────────────────────────────────────┘
```

## Cloud ML Services Comparison

| Service | AWS | GCP | Azure |
|---------|-----|-----|-------|
| **ML Platform** | SageMaker | Vertex AI | Azure ML |
| **Compute** | EC2, EKS | GCE, GKE | AKS, VMs |
| **GPU** | p4d, g5 | A2, L4 | NC, ND |
| **Storage** | S3 | GCS | Blob |
| **Feature Store** | SageMaker FS | Vertex FS | - |
| **Notebooks** | SageMaker | Workbench | ML Studio |

## AWS SageMaker

### Training Job
```python
import sagemaker
from sagemaker.pytorch import PyTorch

# Konfigurera session
session = sagemaker.Session()
role = sagemaker.get_execution_role()

# Definiera training job
estimator = PyTorch(
    entry_point='train.py',
    source_dir='src/',
    role=role,
    instance_count=1,
    instance_type='ml.p3.2xlarge',  # V100 GPU
    framework_version='2.0',
    py_version='py310',
    hyperparameters={
        'epochs': 10,
        'batch-size': 32,
        'learning-rate': 0.001,
    },
    output_path=f's3://{bucket}/models/',
)

# Starta träning
estimator.fit({
    'train': f's3://{bucket}/data/train/',
    'validation': f's3://{bucket}/data/validation/',
})
```

### Deploy Model
```python
# Deploy till endpoint
predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large',
)

# Gör predictions
result = predictor.predict(data)

# Cleanup
predictor.delete_endpoint()
```

## GCP Vertex AI

### Training med Custom Container
```python
from google.cloud import aiplatform

# Initiera
aiplatform.init(
    project='my-project',
    location='us-central1',
    staging_bucket='gs://my-bucket/staging'
)

# Definiera training job
job = aiplatform.CustomContainerTrainingJob(
    display_name='my-training-job',
    container_uri='gcr.io/my-project/training:latest',
    model_serving_container_image_uri='gcr.io/my-project/serving:latest',
)

# Kör träning
model = job.run(
    replica_count=1,
    machine_type='n1-standard-8',
    accelerator_type='NVIDIA_TESLA_V100',
    accelerator_count=1,
    base_output_dir='gs://my-bucket/output',
)

# Deploy
endpoint = model.deploy(
    machine_type='n1-standard-4',
    min_replica_count=1,
    max_replica_count=3,
)
```

## Spot/Preemptible Instances (Kostnadsoptimering)

### AWS Spot Instances
```python
# SageMaker med Spot
estimator = PyTorch(
    # ... andra params
    use_spot_instances=True,
    max_wait=7200,  # Max 2h väntetid
    max_run=3600,   # Max 1h körning
    checkpoint_s3_uri=f's3://{bucket}/checkpoints/',
)
```

### GCP Preemptible
```yaml
# Vertex AI config
machineSpec:
  machineType: n1-standard-8
  acceleratorType: NVIDIA_TESLA_V100
  acceleratorCount: 1
scheduling:
  preemptible: true  # 60-91% billigare!
```

## Multi-Cloud Storage Strategy

```python
# Abstraktion för multi-cloud storage
from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload(self, local_path: str, remote_path: str) -> None:
        pass

    @abstractmethod
    def download(self, remote_path: str, local_path: str) -> None:
        pass

class S3Storage(CloudStorage):
    def __init__(self, bucket: str):
        import boto3
        self.s3 = boto3.client('s3')
        self.bucket = bucket

    def upload(self, local_path: str, remote_path: str) -> None:
        self.s3.upload_file(local_path, self.bucket, remote_path)

    def download(self, remote_path: str, local_path: str) -> None:
        self.s3.download_file(self.bucket, remote_path, local_path)

class GCSStorage(CloudStorage):
    def __init__(self, bucket: str):
        from google.cloud import storage
        self.client = storage.Client()
        self.bucket = self.client.bucket(bucket)

    def upload(self, local_path: str, remote_path: str) -> None:
        blob = self.bucket.blob(remote_path)
        blob.upload_from_filename(local_path)

    def download(self, remote_path: str, local_path: str) -> None:
        blob = self.bucket.blob(remote_path)
        blob.download_to_filename(local_path)

# Användning
storage = S3Storage('my-ml-bucket') if USE_AWS else GCSStorage('my-ml-bucket')
storage.upload('model.pkl', 'models/v1/model.pkl')
```

## Kostnadsoptimering Tips

1. **Använd Spot/Preemptible** för träning (60-90% rabatt)
2. **Right-size instances** - börja litet, skala upp vid behov
3. **Auto-shutdown** notebooks och endpoints
4. **Checkpoint regelbundet** för Spot-tolerans
5. **Komprimera data** innan upload
6. **Använd rätt storage tier** (Glacier för arkivering)

```python
# Exempel: Auto-shutdown idle resources
import datetime

def check_and_shutdown_idle_endpoints():
    '''Stäng av endpoints utan trafik senaste 24h'''
    import boto3

    sm = boto3.client('sagemaker')
    cw = boto3.client('cloudwatch')

    endpoints = sm.list_endpoints()['Endpoints']

    for ep in endpoints:
        # Kolla invocations senaste 24h
        response = cw.get_metric_statistics(
            Namespace='AWS/SageMaker',
            MetricName='Invocations',
            Dimensions=[{'Name': 'EndpointName', 'Value': ep['EndpointName']}],
            StartTime=datetime.datetime.utcnow() - datetime.timedelta(days=1),
            EndTime=datetime.datetime.utcnow(),
            Period=86400,
            Statistics=['Sum']
        )

        if not response['Datapoints'] or response['Datapoints'][0]['Sum'] == 0:
            print(f"Shutting down idle endpoint: {ep['EndpointName']}")
            sm.delete_endpoint(EndpointName=ep['EndpointName'])
```

## Nästa steg

Med cloud-grunderna på plats går vi vidare till:
- Data Engineering för ML
- Containerisering av ML-workloads
"""
            },
            {
                "title": "Data Pipelines for ML",
                "difficulty": "medium",
                "estimated_minutes": 40,
                "xp_reward": 100,
                "content": r"""# Data Pipelines for ML

## Data Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      ML Data Pipeline                            │
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐     │
│  │ Sources  │ → │ Ingest   │ → │Transform │ → │ Feature  │     │
│  │          │   │          │   │          │   │ Store    │     │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘     │
│       │              │              │              │            │
│   Databases      Kafka/         Spark/          Online/        │
│   APIs           Airflow        dbt             Offline        │
│   Files                                                         │
└─────────────────────────────────────────────────────────────────┘
```

## Apache Airflow

### Installation
```bash
# Med Docker Compose
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.0/docker-compose.yaml'
docker compose up -d
```

### ML Training DAG
```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

default_args = {
    'owner': 'mlops',
    'depends_on_past': False,
    'email_on_failure': True,
    'email': ['alerts@company.com'],
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

def extract_data(**context):
    '''Extrahera data från sources'''
    import pandas as pd
    from sqlalchemy import create_engine

    engine = create_engine('postgresql://...')
    df = pd.read_sql('SELECT * FROM transactions WHERE date > %s', engine,
                     params=[context['ds']])  # ds = execution date

    output_path = f"/data/raw/{context['ds']}/transactions.parquet"
    df.to_parquet(output_path)

    return output_path

def validate_data(**context):
    '''Validera data quality'''
    import great_expectations as gx

    # Hämta path från föregående task
    ti = context['ti']
    data_path = ti.xcom_pull(task_ids='extract')

    # Kör validering
    context_gx = gx.get_context()
    checkpoint = context_gx.get_checkpoint("data_quality_checkpoint")
    result = checkpoint.run(batch_request={
        "path": data_path,
        "datasource_name": "transactions"
    })

    if not result.success:
        raise ValueError("Data validation failed!")

    return data_path

def transform_features(**context):
    '''Feature engineering'''
    import pandas as pd

    ti = context['ti']
    data_path = ti.xcom_pull(task_ids='validate')

    df = pd.read_parquet(data_path)

    # Feature engineering
    df['amount_log'] = np.log1p(df['amount'])
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    df['is_weekend'] = pd.to_datetime(df['timestamp']).dt.dayofweek >= 5

    # Aggregations per user
    user_stats = df.groupby('user_id').agg({
        'amount': ['mean', 'std', 'count'],
        'is_fraud': 'mean'
    }).reset_index()

    output_path = f"/data/features/{context['ds']}/features.parquet"
    df.to_parquet(output_path)

    return output_path

def train_model(**context):
    '''Träna modell'''
    import mlflow
    from sklearn.ensemble import RandomForestClassifier

    ti = context['ti']
    features_path = ti.xcom_pull(task_ids='transform')

    df = pd.read_parquet(features_path)
    X = df.drop('is_fraud', axis=1)
    y = df['is_fraud']

    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X, y)

        mlflow.sklearn.log_model(model, "model")
        mlflow.log_metrics({"accuracy": model.score(X, y)})

with DAG(
    'ml_training_pipeline',
    default_args=default_args,
    description='Daily ML model training',
    schedule_interval='0 2 * * *',  # Kör 02:00 varje dag
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['ml', 'training'],
) as dag:

    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
    )

    validate = PythonOperator(
        task_id='validate',
        python_callable=validate_data,
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_features,
    )

    train = PythonOperator(
        task_id='train',
        python_callable=train_model,
    )

    # Define dependencies
    extract >> validate >> transform >> train
```

## Prefect (Modern Alternative)

```python
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def extract_data(date: str) -> str:
    '''Extract med caching'''
    import pandas as pd
    # ... extraction logic
    return output_path

@task(retries=3, retry_delay_seconds=60)
def validate_data(data_path: str) -> str:
    '''Validate med automatic retries'''
    # ... validation logic
    return data_path

@task
def transform_features(data_path: str) -> str:
    '''Transform data'''
    # ... transformation logic
    return features_path

@task
def train_model(features_path: str) -> str:
    '''Train model'''
    # ... training logic
    return model_path

@flow(name="ML Training Pipeline")
def ml_pipeline(date: str):
    '''Main pipeline flow'''
    data_path = extract_data(date)
    validated_path = validate_data(data_path)
    features_path = transform_features(validated_path)
    model_path = train_model(features_path)

    return model_path

# Kör pipeline
if __name__ == "__main__":
    ml_pipeline(date="2024-01-15")
```

## Apache Spark för Stora Dataset

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml import Pipeline

# Initiera Spark
spark = SparkSession.builder \
    .appName("MLPipeline") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

# Läs data
df = spark.read.parquet("s3://bucket/data/")

# Feature engineering
df = df.withColumn("hour", hour(col("timestamp")))
df = df.withColumn("day_of_week", dayofweek(col("timestamp")))

# ML Pipeline
assembler = VectorAssembler(
    inputCols=["amount", "hour", "day_of_week", "user_age"],
    outputCol="features"
)

scaler = StandardScaler(
    inputCol="features",
    outputCol="scaled_features"
)

rf = RandomForestClassifier(
    featuresCol="scaled_features",
    labelCol="is_fraud",
    numTrees=100
)

pipeline = Pipeline(stages=[assembler, scaler, rf])

# Train
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)
model = pipeline.fit(train_df)

# Evaluate
predictions = model.transform(test_df)
accuracy = predictions.filter(col("prediction") == col("is_fraud")).count() / test_df.count()

# Save
model.write().overwrite().save("s3://bucket/models/fraud_detector")
```

## dbt för Feature Engineering

```sql
-- models/features/user_features.sql
{{ config(
    materialized='incremental',
    unique_key='user_id',
    on_schema_change='sync_all_columns'
) }}

WITH transactions AS (
    SELECT * FROM {{ ref('stg_transactions') }}
    {% if is_incremental() %}
    WHERE created_at > (SELECT MAX(updated_at) FROM {{ this }})
    {% endif %}
),

user_stats AS (
    SELECT
        user_id,
        COUNT(*) as transaction_count,
        SUM(amount) as total_amount,
        AVG(amount) as avg_amount,
        STDDEV(amount) as std_amount,
        MAX(amount) as max_amount,
        COUNT(CASE WHEN is_fraud THEN 1 END) as fraud_count,
        COUNT(CASE WHEN is_fraud THEN 1 END)::FLOAT / COUNT(*) as fraud_rate
    FROM transactions
    GROUP BY user_id
)

SELECT
    user_id,
    transaction_count,
    total_amount,
    avg_amount,
    COALESCE(std_amount, 0) as std_amount,
    max_amount,
    fraud_count,
    fraud_rate,
    CURRENT_TIMESTAMP as updated_at
FROM user_stats
```

## Best Practices

1. **Idempotency** - Pipelines ska kunna köras om utan problem
2. **Monitoring** - Logga execution time, data volumes, errors
3. **Testing** - Unit tests för transformations
4. **Documentation** - Beskriv data lineage
5. **Alerting** - Notifiera vid failures
"""
            },
            {
                "title": "Feature Stores",
                "difficulty": "medium",
                "estimated_minutes": 35,
                "xp_reward": 100,
                "content": r"""# Feature Stores

## Varför Feature Store?

```
Utan Feature Store:
┌─────────────────────────────────────────────────────────┐
│  Training                    Serving                    │
│  ┌─────────────┐            ┌─────────────┐            │
│  │ Python/     │            │ Java/       │            │
│  │ Spark       │            │ Go          │            │
│  │ features    │     ≠      │ features    │            │
│  └─────────────┘            └─────────────┘            │
│       ↓                           ↓                     │
│  Training/Serving skew! Modellen presterar sämre!       │
└─────────────────────────────────────────────────────────┘

Med Feature Store:
┌─────────────────────────────────────────────────────────┐
│              ┌─────────────────┐                        │
│              │  Feature Store  │                        │
│              │  ┌───────────┐  │                        │
│              │  │ Offline   │  │ ← Training             │
│              │  │ Store     │  │                        │
│              │  └───────────┘  │                        │
│              │  ┌───────────┐  │                        │
│              │  │ Online    │  │ ← Serving (low latency)│
│              │  │ Store     │  │                        │
│              │  └───────────┘  │                        │
│              └─────────────────┘                        │
│                     ↓                                   │
│  Samma features för träning och serving!                │
└─────────────────────────────────────────────────────────┘
```

## Feast - Open Source Feature Store

### Installation och Setup
```bash
pip install feast

# Initiera projekt
feast init fraud_detection
cd fraud_detection
```

### Feature Definitions
```python
# feature_repo/features.py
from datetime import timedelta
from feast import Entity, Feature, FeatureView, FileSource, ValueType
from feast.types import Float32, Int64

# Entity definition
user = Entity(
    name="user_id",
    value_type=ValueType.INT64,
    description="User identifier",
)

# Data source
user_stats_source = FileSource(
    path="data/user_stats.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

# Feature view
user_stats_fv = FeatureView(
    name="user_stats",
    entities=["user_id"],
    ttl=timedelta(days=1),
    features=[
        Feature(name="transaction_count_7d", dtype=Int64),
        Feature(name="avg_amount_7d", dtype=Float32),
        Feature(name="std_amount_7d", dtype=Float32),
        Feature(name="fraud_rate_7d", dtype=Float32),
    ],
    online=True,
    source=user_stats_source,
    tags={"team": "fraud"},
)

# On-demand feature (computed at request time)
from feast import on_demand_feature_view
from feast import Field
from feast.types import Float32
import pandas as pd

@on_demand_feature_view(
    sources=[user_stats_fv],
    schema=[Field(name="transaction_velocity", dtype=Float32)],
)
def user_velocity_features(inputs: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame()
    df["transaction_velocity"] = (
        inputs["transaction_count_7d"] / 7.0  # transactions per day
    )
    return df
```

### Apply och Materialize
```bash
# Apply feature definitions
feast apply

# Materialize features to online store
feast materialize-incremental $(date +%Y-%m-%dT%H:%M:%S)
```

### Training Data Retrieval
```python
from feast import FeatureStore
from datetime import datetime

store = FeatureStore(repo_path=".")

# Entity DataFrame (what we want features for)
entity_df = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5],
    "event_timestamp": [datetime(2024, 1, 15)] * 5,
})

# Get historical features (for training)
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "user_stats:transaction_count_7d",
        "user_stats:avg_amount_7d",
        "user_stats:std_amount_7d",
        "user_stats:fraud_rate_7d",
    ],
).to_df()

print(training_df)
```

### Online Serving
```python
from feast import FeatureStore

store = FeatureStore(repo_path=".")

# Get online features (for inference)
feature_vector = store.get_online_features(
    features=[
        "user_stats:transaction_count_7d",
        "user_stats:avg_amount_7d",
        "user_stats:fraud_rate_7d",
    ],
    entity_rows=[{"user_id": 12345}],
).to_dict()

print(feature_vector)
# {'user_id': [12345], 'transaction_count_7d': [42], 'avg_amount_7d': [150.5], ...}
```

## Feature Store Architecture

```yaml
# feature_store.yaml
project: fraud_detection
registry: s3://bucket/registry.pb
provider: aws

online_store:
  type: redis
  connection_string: ${REDIS_CONNECTION}

offline_store:
  type: redshift
  cluster_id: my-cluster
  database: features
  user: feast
  s3_staging_location: s3://bucket/staging/

entity_key_serialization_version: 2
```

## Feature Engineering Patterns

### Time-Window Features
```python
def compute_time_window_features(
    df: pd.DataFrame,
    entity_col: str,
    value_col: str,
    timestamp_col: str,
    windows: list[int] = [7, 14, 30]
) -> pd.DataFrame:
    '''Compute rolling window aggregations'''

    df = df.sort_values([entity_col, timestamp_col])

    for window in windows:
        # Rolling aggregations
        rolling = df.groupby(entity_col)[value_col].rolling(
            window=f'{window}D', on=timestamp_col
        )

        df[f'{value_col}_sum_{window}d'] = rolling.sum().values
        df[f'{value_col}_mean_{window}d'] = rolling.mean().values
        df[f'{value_col}_std_{window}d'] = rolling.std().values
        df[f'{value_col}_count_{window}d'] = rolling.count().values

    return df
```

### Streaming Features
```python
from feast import StreamFeatureView
from feast.data_source import KafkaSource

# Kafka source for real-time events
transactions_stream = KafkaSource(
    name="transactions_stream",
    kafka_bootstrap_servers="kafka:9092",
    topic="transactions",
    timestamp_field="event_timestamp",
    message_format=JsonFormat(schema=schema),
)

# Stream feature view
realtime_user_stats = StreamFeatureView(
    name="realtime_user_stats",
    entities=["user_id"],
    ttl=timedelta(minutes=5),
    features=[
        Feature(name="recent_transaction_count", dtype=Int64),
        Feature(name="recent_total_amount", dtype=Float32),
    ],
    source=transactions_stream,
    aggregations=[
        Aggregation(column="amount", function="count", time_window=timedelta(minutes=5)),
        Aggregation(column="amount", function="sum", time_window=timedelta(minutes=5)),
    ],
)
```

## Best Practices

1. **Konsistent namning** - `{entity}_{metric}_{window}`
2. **Dokumentation** - Beskriv varje feature
3. **Versioning** - Versionera feature definitions
4. **Monitoring** - Tracka feature freshness och null rates
5. **Testing** - Validera feature distributions
"""
            },
            {
                "title": "Data Lakes & Warehouses",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 75,
                "content": r"""# Data Lakes & Warehouses for ML

## Data Lake vs Data Warehouse

```
┌─────────────────────────────────────────────────────────────────┐
│                   DATA LAKE                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Schema-on-Read                                          │    │
│  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐               │    │
│  │  │JSON │ │CSV  │ │Parq │ │Image│ │Video│               │    │
│  │  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘               │    │
│  │  Raw, unprocessed, any format                           │    │
│  │  Perfect for ML exploration!                            │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                   DATA WAREHOUSE                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Schema-on-Write                                         │    │
│  │  ┌──────────────────────────────────────────┐           │    │
│  │  │  Structured Tables with defined schemas   │           │    │
│  │  │  Optimized for BI/Analytics queries       │           │    │
│  │  │  Clean, validated, aggregated             │           │    │
│  │  └──────────────────────────────────────────┘           │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                   LAKEHOUSE (Modern)                             │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Best of both worlds!                                    │    │
│  │  Delta Lake / Apache Iceberg / Apache Hudi               │    │
│  │  - ACID transactions                                     │    │
│  │  - Schema evolution                                      │    │
│  │  - Time travel                                           │    │
│  │  - Direct ML access to raw data                          │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

## Delta Lake

### Setup
```python
from delta import *
from pyspark.sql import SparkSession

# Spark med Delta Lake
spark = SparkSession.builder \
    .appName("DeltaLakeML") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()
```

### Write Data
```python
# Skriv som Delta
df.write.format("delta").mode("overwrite").save("/data/ml/features")

# Med partitionering
df.write.format("delta") \
    .partitionBy("date", "region") \
    .mode("overwrite") \
    .save("/data/ml/features")

# Append new data
new_df.write.format("delta").mode("append").save("/data/ml/features")
```

### Time Travel (Perfekt för ML Reproducibility!)
```python
# Läs specifik version
df_v0 = spark.read.format("delta").option("versionAsOf", 0).load("/data/ml/features")

# Läs vid specifik tidpunkt
df_yesterday = spark.read.format("delta") \
    .option("timestampAsOf", "2024-01-14") \
    .load("/data/ml/features")

# Se historik
from delta.tables import DeltaTable
dt = DeltaTable.forPath(spark, "/data/ml/features")
history_df = dt.history()
history_df.show()
```

### Schema Evolution
```python
# Lägg till ny kolumn automatiskt
new_df_with_extra_column.write.format("delta") \
    .mode("append") \
    .option("mergeSchema", "true") \
    .save("/data/ml/features")
```

## ML Data Organization

### Bronze/Silver/Gold Pattern
```
┌─────────────────────────────────────────────────────────────────┐
│                    Medallion Architecture                        │
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐                     │
│  │  BRONZE  │ → │  SILVER  │ → │   GOLD   │                     │
│  │  (Raw)   │   │ (Clean)  │   │(Features)│                     │
│  └──────────┘   └──────────┘   └──────────┘                     │
│       │              │              │                            │
│   Raw JSON/      Cleaned,       Aggregated,                     │
│   CSV ingest     validated,     feature-ready,                  │
│   from sources   deduplicated   for ML training                 │
└─────────────────────────────────────────────────────────────────┘
```

### Implementation
```python
# Bronze: Raw ingestion
raw_df = spark.read.json("s3://bucket/raw/events/")
raw_df.write.format("delta").save("s3://bucket/bronze/events/")

# Silver: Cleaned and validated
silver_df = spark.read.format("delta").load("s3://bucket/bronze/events/")
silver_df = silver_df \
    .dropDuplicates(["event_id"]) \
    .filter(col("user_id").isNotNull()) \
    .withColumn("event_date", to_date(col("timestamp")))

silver_df.write.format("delta") \
    .partitionBy("event_date") \
    .save("s3://bucket/silver/events/")

# Gold: ML-ready features
gold_df = spark.read.format("delta").load("s3://bucket/silver/events/")
features_df = gold_df.groupBy("user_id").agg(
    count("*").alias("event_count"),
    avg("amount").alias("avg_amount"),
    max("timestamp").alias("last_activity")
)
features_df.write.format("delta").save("s3://bucket/gold/user_features/")
```

## Data Catalog

### AWS Glue Catalog
```python
# Registrera Delta tabell i Glue Catalog
spark.sql('''
    CREATE TABLE IF NOT EXISTS ml_catalog.user_features
    USING DELTA
    LOCATION 's3://bucket/gold/user_features/'
''')

# Query via catalog
spark.sql("SELECT * FROM ml_catalog.user_features WHERE event_count > 10")
```

### Hive Metastore
```python
# Enable Hive support
spark = SparkSession.builder \
    .appName("ML") \
    .enableHiveSupport() \
    .getOrCreate()

# Create managed table
spark.sql('''
    CREATE TABLE ml_features.user_stats (
        user_id BIGINT,
        transaction_count INT,
        avg_amount DOUBLE,
        fraud_rate DOUBLE
    )
    USING DELTA
    PARTITIONED BY (dt STRING)
''')
```

## Best Practices for ML Data

1. **Partition by date** - Enkel incremental processing
2. **Use Parquet/Delta** - Columnar format för ML
3. **Track data versions** - Reproducerbarhet
4. **Separate train/validation/test** - Undvik data leakage
5. **Document lineage** - Spåra data origin

```python
# Exempel: ML-ready data structure
data/
├── bronze/           # Raw data as-is
│   └── events/
├── silver/           # Cleaned, validated
│   └── events/
├── gold/             # Feature tables
│   ├── user_features/
│   └── transaction_features/
└── ml/               # ML-specific datasets
    ├── train/
    │   ├── 2024-01-01/
    │   └── 2024-01-15/
    ├── validation/
    └── test/
```
"""
            },
            {
                "title": "Data Ingestion Architecture",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 75,
                "content": r"""# Data Ingestion Architecture

## Ingestion Patterns

```
┌─────────────────────────────────────────────────────────────────┐
│                    Data Ingestion Patterns                       │
│                                                                  │
│  BATCH                          STREAMING                        │
│  ┌─────────────┐                ┌─────────────┐                  │
│  │ Daily/      │                │ Real-time   │                  │
│  │ Hourly      │                │ Continuous  │                  │
│  │ Full/Incr   │                │ Events      │                  │
│  └─────────────┘                └─────────────┘                  │
│       │                              │                           │
│       ▼                              ▼                           │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              Data Lake / Feature Store                   │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

## Apache Kafka for Streaming

### Producer
```python
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8') if k else None,
)

def send_event(event: dict):
    '''Send event to Kafka'''
    producer.send(
        topic='ml-events',
        key=event.get('user_id'),
        value=event,
    )
    producer.flush()

# Exempel
send_event({
    'user_id': '12345',
    'event_type': 'transaction',
    'amount': 99.99,
    'timestamp': '2024-01-15T10:30:00Z',
})
```

### Consumer for ML
```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'ml-events',
    bootstrap_servers=['kafka:9092'],
    group_id='ml-feature-ingestion',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
)

def process_events():
    '''Consume and process events for ML'''
    batch = []
    batch_size = 1000

    for message in consumer:
        event = message.value
        batch.append(event)

        if len(batch) >= batch_size:
            # Process batch
            df = pd.DataFrame(batch)

            # Update feature store
            update_features(df)

            # Write to data lake
            write_to_delta(df)

            batch = []

    consumer.commit()
```

## Spark Structured Streaming

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StringType, DoubleType, TimestampType

spark = SparkSession.builder \
    .appName("StreamingML") \
    .getOrCreate()

# Schema för events
schema = StructType() \
    .add("user_id", StringType()) \
    .add("amount", DoubleType()) \
    .add("timestamp", TimestampType())

# Läs från Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "transactions") \
    .option("startingOffsets", "latest") \
    .load()

# Parse JSON
events = df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Windowed aggregations för features
windowed_features = events \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        col("user_id"),
        window(col("timestamp"), "5 minutes")
    ) \
    .agg(
        count("*").alias("transaction_count_5m"),
        sum("amount").alias("total_amount_5m"),
        avg("amount").alias("avg_amount_5m"),
    )

# Skriv till Delta Lake
query = windowed_features.writeStream \
    .format("delta") \
    .outputMode("update") \
    .option("checkpointLocation", "/checkpoints/features") \
    .start("/data/streaming_features/")

query.awaitTermination()
```

## Change Data Capture (CDC)

```python
# Debezium connector configuration
connector_config = {
    "name": "postgres-cdc",
    "config": {
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "database.hostname": "postgres",
        "database.port": "5432",
        "database.user": "debezium",
        "database.password": "${secrets.db_password}",
        "database.dbname": "production",
        "table.include.list": "public.users,public.transactions",
        "topic.prefix": "cdc",
        "plugin.name": "pgoutput",
    }
}

# Process CDC events
def process_cdc_event(event: dict):
    '''Handle CDC event'''
    operation = event['op']  # 'c' = create, 'u' = update, 'd' = delete

    if operation in ('c', 'u'):
        # Upsert to feature store
        after = event['after']
        upsert_feature(after)
    elif operation == 'd':
        # Handle deletion
        before = event['before']
        delete_feature(before['id'])
```

## Batch Ingestion with Airflow

```python
from airflow import DAG
from airflow.providers.amazon.aws.operators.s3 import S3ListOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG('batch_ingestion', schedule_interval='@hourly') as dag:

    # List new files
    list_files = S3ListOperator(
        task_id='list_new_files',
        bucket='raw-data',
        prefix='incoming/',
    )

    # Process with Spark
    process = SparkSubmitOperator(
        task_id='process_files',
        application='/jobs/ingest.py',
        conf={
            'spark.sql.adaptive.enabled': 'true',
        },
    )

    list_files >> process
```

## Data Quality Checks

```python
import great_expectations as gx

def validate_ingested_data(df: pd.DataFrame) -> bool:
    '''Validate data quality before ingestion'''

    context = gx.get_context()

    # Define expectations
    expectation_suite = context.create_expectation_suite("ingestion_checks")

    validator = context.get_validator(
        batch_request=batch_request,
        expectation_suite_name="ingestion_checks"
    )

    # Add expectations
    validator.expect_column_to_exist("user_id")
    validator.expect_column_values_to_not_be_null("user_id")
    validator.expect_column_values_to_be_unique("event_id")
    validator.expect_column_values_to_be_between("amount", 0, 1000000)

    # Run validation
    results = validator.validate()

    if not results.success:
        # Log failures
        for result in results.results:
            if not result.success:
                log_quality_failure(result)
        return False

    return True
```
"""
            },
            {
                "title": "ML Training Best Practices",
                "difficulty": "medium",
                "estimated_minutes": 35,
                "xp_reward": 100,
                "content": r"""# ML Training Best Practices

## Reproducibility

### Seed Everything
```python
import random
import numpy as np
import torch

def set_seed(seed: int = 42):
    \"\"\"Set seed for reproducibility\"\"\"
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    # For CUDA determinism (slower but reproducible)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)
```

### Configuration Management with Hydra
```yaml
# config/config.yaml
defaults:
  - model: random_forest
  - data: default
  - _self_

seed: 42
experiment_name: fraud_detection

training:
  test_size: 0.2
  cv_folds: 5
  early_stopping_rounds: 10
```

```yaml
# config/model/random_forest.yaml
name: random_forest
params:
  n_estimators: 100
  max_depth: 10
  min_samples_split: 5
  random_state: ${seed}
```

```python
import hydra
from omegaconf import DictConfig

@hydra.main(config_path="config", config_name="config")
def train(cfg: DictConfig):
    set_seed(cfg.seed)

    # Ladda data
    X_train, X_test, y_train, y_test = load_data(
        test_size=cfg.training.test_size
    )

    # Skapa modell från config
    if cfg.model.name == "random_forest":
        model = RandomForestClassifier(**cfg.model.params)
    elif cfg.model.name == "xgboost":
        model = XGBClassifier(**cfg.model.params)

    # Träna
    model.fit(X_train, y_train)

    return model

if __name__ == "__main__":
    train()
```

## Training Pipeline Structure

```python
from dataclasses import dataclass
from typing import Tuple, Dict, Any
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
import mlflow

@dataclass
class TrainingConfig:
    model_type: str
    model_params: Dict[str, Any]
    test_size: float = 0.2
    cv_folds: int = 5
    seed: int = 42

class MLTrainer:
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.model = None
        self.metrics = {}

    def prepare_data(
        self,
        df: pd.DataFrame,
        target_col: str
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        \"\"\"Split data with stratification\"\"\"
        X = df.drop(columns=[target_col])
        y = df[target_col]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=self.config.test_size,
            random_state=self.config.seed,
            stratify=y
        )

        return X_train, X_test, y_train, y_test

    def train(self, X_train: pd.DataFrame, y_train: pd.Series):
        \"\"\"Train model with cross-validation\"\"\"
        self.model = self._create_model()

        # Cross-validation
        cv_scores = cross_val_score(
            self.model, X_train, y_train,
            cv=self.config.cv_folds,
            scoring='f1_weighted'
        )

        self.metrics['cv_mean'] = cv_scores.mean()
        self.metrics['cv_std'] = cv_scores.std()

        # Final fit
        self.model.fit(X_train, y_train)

        return self.model

    def evaluate(self, X_test: pd.DataFrame, y_test: pd.Series) -> Dict:
        \"\"\"Evaluate model on test set\"\"\"
        y_pred = self.model.predict(X_test)

        report = classification_report(y_test, y_pred, output_dict=True)
        self.metrics['accuracy'] = report['accuracy']
        self.metrics['f1_weighted'] = report['weighted avg']['f1-score']
        self.metrics['precision'] = report['weighted avg']['precision']
        self.metrics['recall'] = report['weighted avg']['recall']

        return self.metrics

    def _create_model(self):
        \"\"\"Factory for creating models\"\"\"
        from sklearn.ensemble import RandomForestClassifier
        from xgboost import XGBClassifier

        models = {
            'random_forest': RandomForestClassifier,
            'xgboost': XGBClassifier,
        }

        model_class = models[self.config.model_type]
        return model_class(**self.config.model_params)
```

## Data Validation Before Training

```python
import great_expectations as gx
from great_expectations.core import ExpectationSuite

def validate_training_data(df: pd.DataFrame) -> bool:
    \"\"\"Validate data before training\"\"\"

    # Check for required columns
    required_cols = ['user_id', 'amount', 'is_fraud']
    missing = set(required_cols) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # Check for nulls
    null_counts = df.isnull().sum()
    if null_counts.any():
        print(f"Warning: Null values found:\n{null_counts[null_counts > 0]}")

    # Check class balance
    class_dist = df['is_fraud'].value_counts(normalize=True)
    if class_dist.min() < 0.01:
        print(f"Warning: Severe class imbalance: {class_dist.to_dict()}")

    # Check for data leakage
    if 'future_fraud' in df.columns:
        raise ValueError("Potential data leakage: 'future_fraud' column detected")

    return True

def check_train_test_distribution(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame
) -> Dict[str, float]:
    \"\"\"Check for distribution shift between train/test\"\"\"
    from scipy import stats

    shifts = {}
    for col in X_train.select_dtypes(include=[np.number]).columns:
        statistic, pvalue = stats.ks_2samp(X_train[col], X_test[col])
        if pvalue < 0.05:
            shifts[col] = pvalue

    if shifts:
        print(f"Warning: Distribution shift detected in columns: {list(shifts.keys())}")

    return shifts
```

## GPU Training

```python
import torch
from torch.utils.data import DataLoader, TensorDataset
from torch.cuda.amp import autocast, GradScaler

class PyTorchTrainer:
    def __init__(self, model: torch.nn.Module, config: dict):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = model.to(self.device)
        self.config = config
        self.scaler = GradScaler()  # Mixed precision

    def train_epoch(
        self,
        train_loader: DataLoader,
        optimizer: torch.optim.Optimizer,
        criterion: torch.nn.Module
    ) -> float:
        self.model.train()
        total_loss = 0

        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(self.device), target.to(self.device)

            optimizer.zero_grad()

            # Mixed precision training
            with autocast():
                output = self.model(data)
                loss = criterion(output, target)

            self.scaler.scale(loss).backward()
            self.scaler.step(optimizer)
            self.scaler.update()

            total_loss += loss.item()

        return total_loss / len(train_loader)

    def train(
        self,
        train_loader: DataLoader,
        val_loader: DataLoader,
        epochs: int = 10
    ):
        optimizer = torch.optim.AdamW(
            self.model.parameters(),
            lr=self.config['learning_rate'],
            weight_decay=self.config['weight_decay']
        )

        scheduler = torch.optim.lr_scheduler.OneCycleLR(
            optimizer,
            max_lr=self.config['learning_rate'],
            epochs=epochs,
            steps_per_epoch=len(train_loader)
        )

        criterion = torch.nn.CrossEntropyLoss()

        best_val_loss = float('inf')
        patience_counter = 0

        for epoch in range(epochs):
            train_loss = self.train_epoch(train_loader, optimizer, criterion)
            val_loss = self.validate(val_loader, criterion)

            scheduler.step()

            print(f"Epoch {epoch+1}: train_loss={train_loss:.4f}, val_loss={val_loss:.4f}")

            # Early stopping
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                patience_counter = 0
                self.save_checkpoint('best_model.pt')
            else:
                patience_counter += 1
                if patience_counter >= self.config['patience']:
                    print(f"Early stopping at epoch {epoch+1}")
                    break
```

## Distributed Training

```python
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

def setup_distributed():
    dist.init_process_group(backend='nccl')
    local_rank = int(os.environ['LOCAL_RANK'])
    torch.cuda.set_device(local_rank)
    return local_rank

def train_distributed():
    local_rank = setup_distributed()

    model = MyModel().cuda(local_rank)
    model = DDP(model, device_ids=[local_rank])

    # Training loop...

    dist.destroy_process_group()

# Launch: torchrun --nproc_per_node=4 train.py
```
"""
            },
            {
                "title": "Experiment Tracking",
                "difficulty": "medium",
                "estimated_minutes": 35,
                "xp_reward": 100,
                "content": r"""# Experiment Tracking

## Varför Experiment Tracking?

```
Utan tracking:
  "Vilken modell presterade bäst?"
  "Vilka hyperparameters använde jag?"
  "Vilken data version?"
  → Ingen aning! Kör om allt...

Med tracking:
  experiment_id: exp_2024_01_15_v3
  params: {lr: 0.001, layers: 3}
  metrics: {accuracy: 0.95}
  artifacts: model.pkl, plots/
  data_version: v1.2.3
  → Full reproducibility!
```

## MLflow

### Setup
```bash
# Installera
pip install mlflow

# Starta tracking server
mlflow server \
    --backend-store-uri postgresql://user:pass@localhost/mlflow \
    --default-artifact-root s3://bucket/mlflow-artifacts \
    --host 0.0.0.0 \
    --port 5000
```

### Basic Tracking
```python
import mlflow
from mlflow.tracking import MlflowClient

# Konfigurera tracking URI
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("fraud_detection")

# Enkel tracking
with mlflow.start_run(run_name="random_forest_v1"):
    # Log parameters
    mlflow.log_params({
        "n_estimators": 100,
        "max_depth": 10,
        "min_samples_split": 5,
    })

    # Train model
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    # Log metrics
    accuracy = model.score(X_test, y_test)
    mlflow.log_metrics({
        "accuracy": accuracy,
        "f1_score": f1,
        "precision": precision,
        "recall": recall,
    })

    # Log model
    mlflow.sklearn.log_model(
        model,
        "model",
        signature=mlflow.models.infer_signature(X_train, y_train)
    )

    # Log artifacts
    mlflow.log_artifact("confusion_matrix.png")
    mlflow.log_dict({"feature_importance": importance.tolist()}, "features.json")
```

### MLflow Projects
```yaml
# MLproject
name: fraud_detection

conda_env: conda.yaml

entry_points:
  main:
    parameters:
      data_path: {type: string, default: "data/"}
      model_type: {type: string, default: "random_forest"}
      n_estimators: {type: int, default: 100}
    command: "python train.py --data-path {data_path} --model {model_type} --n-estimators {n_estimators}"

  evaluate:
    parameters:
      model_uri: {type: string}
      test_data: {type: string}
    command: "python evaluate.py --model-uri {model_uri} --test-data {test_data}"
```

```bash
# Kör projekt
mlflow run . -P n_estimators=200 -P model_type=xgboost
```

### Autologging
```python
# Automatisk logging för sklearn
mlflow.sklearn.autolog()

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)  # Allt loggas automatiskt!

# För PyTorch
mlflow.pytorch.autolog()

# För TensorFlow
mlflow.tensorflow.autolog()

# För XGBoost
mlflow.xgboost.autolog()
```

## Weights & Biases

### Setup
```python
import wandb

wandb.login()

# Initiera run
run = wandb.init(
    project="fraud-detection",
    name="rf_experiment_v1",
    config={
        "n_estimators": 100,
        "max_depth": 10,
        "learning_rate": 0.01,
    }
)
```

### Tracking
```python
# Log metrics över tid
for epoch in range(epochs):
    train_loss = train_epoch(model, train_loader)
    val_loss = validate(model, val_loader)

    wandb.log({
        "epoch": epoch,
        "train_loss": train_loss,
        "val_loss": val_loss,
        "learning_rate": scheduler.get_last_lr()[0],
    })

# Log confusion matrix
wandb.log({
    "confusion_matrix": wandb.plot.confusion_matrix(
        y_true=y_test,
        preds=y_pred,
        class_names=["legitimate", "fraud"]
    )
})

# Log ROC curve
wandb.log({
    "roc_curve": wandb.plot.roc_curve(
        y_true=y_test,
        y_probas=y_proba,
        labels=["legitimate", "fraud"]
    )
})

# Spara modell som artifact
artifact = wandb.Artifact("fraud_model", type="model")
artifact.add_file("model.pkl")
run.log_artifact(artifact)
```

### Sweeps (Hyperparameter Search)
```yaml
# sweep_config.yaml
program: train.py
method: bayes
metric:
  name: val_f1
  goal: maximize
parameters:
  n_estimators:
    values: [50, 100, 200, 500]
  max_depth:
    distribution: int_uniform
    min: 3
    max: 20
  learning_rate:
    distribution: log_uniform_values
    min: 0.0001
    max: 0.1
```

```python
# Kör sweep
sweep_id = wandb.sweep(sweep_config, project="fraud-detection")
wandb.agent(sweep_id, function=train, count=20)
```

## Comparison & Analysis

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Hitta bästa experiment
experiment = client.get_experiment_by_name("fraud_detection")
runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    filter_string="metrics.f1_score > 0.9",
    order_by=["metrics.f1_score DESC"],
    max_results=10
)

# Jämför runs
for run in runs:
    print(f"Run: {run.info.run_id}")
    print(f"  F1: {run.data.metrics['f1_score']:.4f}")
    print(f"  Params: {run.data.params}")

# Promota bästa modell
best_run = runs[0]
mlflow.register_model(
    f"runs:/{best_run.info.run_id}/model",
    "fraud_detector"
)
```

## Best Practices

1. **Tag runs** med metadata (dataset version, git commit)
2. **Log input data hash** för reproducibility
3. **Nested runs** för hyperparameter tuning
4. **Artifacts** för plots, feature importance, etc.
5. **Automatisera** - integrera i CI/CD
"""
            },
            {
                "title": "Model Registry",
                "difficulty": "medium",
                "estimated_minutes": 30,
                "xp_reward": 100,
                "content": r"""# Model Registry

## Vad är en Model Registry?

```
┌─────────────────────────────────────────────────────────────────┐
│                      Model Registry                              │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │  fraud_detector                                         │     │
│  │  ├── Version 1 (Staging)    - RF, acc=0.92             │     │
│  │  ├── Version 2 (Production) - XGBoost, acc=0.95       │     │
│  │  ├── Version 3 (None)       - Neural Net, acc=0.94    │     │
│  │  └── Version 4 (Staging)    - Ensemble, acc=0.97       │     │
│  └────────────────────────────────────────────────────────┘     │
│                                                                  │
│  Stages: None → Staging → Production → Archived                 │
└─────────────────────────────────────────────────────────────────┘
```

## MLflow Model Registry

### Registrera Modell
```python
import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Registrera från run
result = mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name="fraud_detector"
)

print(f"Registered version: {result.version}")

# Med beskrivning
client.update_model_version(
    name="fraud_detector",
    version=result.version,
    description="XGBoost model trained on 2024-01 data. F1=0.95"
)

# Lägg till tags
client.set_model_version_tag(
    name="fraud_detector",
    version=result.version,
    key="dataset_version",
    value="v1.2.0"
)
```

### Stage Transitions
```python
# Promota till Staging
client.transition_model_version_stage(
    name="fraud_detector",
    version=4,
    stage="Staging",
    archive_existing_versions=False
)

# Efter validering → Production
client.transition_model_version_stage(
    name="fraud_detector",
    version=4,
    stage="Production",
    archive_existing_versions=True  # Arkivera tidigare prod-version
)

# Rollback
client.transition_model_version_stage(
    name="fraud_detector",
    version=2,  # Tidigare stabil version
    stage="Production"
)
```

### Ladda Modell från Registry
```python
import mlflow

# Ladda senaste Production-versionen
model = mlflow.pyfunc.load_model("models:/fraud_detector/Production")

# Ladda specifik version
model_v2 = mlflow.pyfunc.load_model("models:/fraud_detector/2")

# Gör predictions
predictions = model.predict(X_new)
```

## Model Governance

### Approval Workflow
```python
from typing import Literal
from pydantic import BaseModel

class ModelApproval(BaseModel):
    model_name: str
    version: int
    target_stage: Literal["Staging", "Production"]
    approver: str
    approval_date: str
    validation_results: dict
    risk_assessment: str

def request_promotion(
    model_name: str,
    version: int,
    target_stage: str,
    validation_results: dict
) -> ModelApproval:
    \"\"\"Request model promotion with approval workflow\"\"\"

    # Automatiska checks
    checks = {
        "accuracy_threshold": validation_results["accuracy"] > 0.90,
        "no_data_drift": validation_results["psi_score"] < 0.1,
        "latency_ok": validation_results["p99_latency_ms"] < 100,
        "bias_check": validation_results["fairness_score"] > 0.8,
    }

    if not all(checks.values()):
        failed = [k for k, v in checks.items() if not v]
        raise ValueError(f"Promotion blocked. Failed checks: {failed}")

    # Skapa approval request (skickas till Slack/Email)
    approval = ModelApproval(
        model_name=model_name,
        version=version,
        target_stage=target_stage,
        validation_results=validation_results,
        approver="pending",
        approval_date="pending",
        risk_assessment=assess_risk(validation_results)
    )

    return approval
```

### Model Card
```python
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class ModelCard:
    \"\"\"Documentation for deployed models\"\"\"
    name: str
    version: str
    description: str

    # Training details
    training_data: str
    training_date: str
    training_params: Dict

    # Performance
    metrics: Dict[str, float]
    evaluation_data: str

    # Usage
    input_schema: Dict
    output_schema: Dict
    example_usage: str

    # Limitations
    known_limitations: List[str]
    out_of_scope_uses: List[str]

    # Ethical considerations
    bias_analysis: str
    fairness_metrics: Dict[str, float]

# Exempel
card = ModelCard(
    name="fraud_detector",
    version="2.0.0",
    description="XGBoost-based fraud detection model",
    training_data="transactions_2023_01_to_2024_01",
    training_date="2024-01-15",
    training_params={"n_estimators": 200, "max_depth": 10},
    metrics={"accuracy": 0.95, "f1": 0.92, "auc": 0.98},
    evaluation_data="transactions_2024_01_holdout",
    input_schema={"amount": "float", "merchant": "string", "time": "datetime"},
    output_schema={"is_fraud": "bool", "confidence": "float"},
    example_usage="model.predict(transaction_data)",
    known_limitations=[
        "Lower accuracy on transactions > $10,000",
        "Not trained on crypto transactions"
    ],
    out_of_scope_uses=["Credit scoring", "Identity verification"],
    bias_analysis="Model tested for demographic parity across age groups",
    fairness_metrics={"demographic_parity": 0.95, "equalized_odds": 0.92}
)
```

## Model Versioning Strategy

```
fraud_detector-v{MAJOR}.{MINOR}.{PATCH}

MAJOR: Breaking changes
  - New input/output schema
  - Different model architecture
  - Significant retraining

MINOR: Improvements
  - Hyperparameter tuning
  - New training data
  - Feature additions

PATCH: Fixes
  - Bug fixes
  - Minor retraining
  - Documentation updates
```
"""
            },
            {
                "title": "Hyperparameter Tuning",
                "difficulty": "hard",
                "estimated_minutes": 35,
                "xp_reward": 100,
                "content": r"""# Hyperparameter Tuning

## Tuning Strategier

```
┌─────────────────────────────────────────────────────────────────┐
│                    Hyperparameter Search                         │
│                                                                  │
│  Grid Search          Random Search         Bayesian Opt        │
│  ┌─────────┐          ┌─────────┐          ┌─────────┐          │
│  │ ■ ■ ■ ■ │          │   ■     │          │       ■ │          │
│  │ ■ ■ ■ ■ │          │ ■   ■   │          │   ■     │          │
│  │ ■ ■ ■ ■ │          │     ■ ■ │          │ ■   ■   │          │
│  │ ■ ■ ■ ■ │          │ ■       │          │ ■ ■ ■ ■ │ ← Focus  │
│  └─────────┘          └─────────┘          └─────────┘           │
│  Exhaustive           Random samples       Smart sampling       │
│  O(n^d)               O(n)                 O(n log n)           │
└─────────────────────────────────────────────────────────────────┘
```

## Optuna

### Basic Usage
```python
import optuna
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

def objective(trial):
    \"\"\"Optuna objective function\"\"\"

    # Suggest hyperparameters
    params = {
        "n_estimators": trial.suggest_int("n_estimators", 50, 500),
        "max_depth": trial.suggest_int("max_depth", 3, 20),
        "min_samples_split": trial.suggest_int("min_samples_split", 2, 20),
        "min_samples_leaf": trial.suggest_int("min_samples_leaf", 1, 10),
        "max_features": trial.suggest_categorical("max_features", ["sqrt", "log2", None]),
    }

    model = RandomForestClassifier(**params, random_state=42, n_jobs=-1)

    # Cross-validation
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring="f1")

    return scores.mean()

# Skapa studie
study = optuna.create_study(
    study_name="fraud_detection_rf",
    direction="maximize",
    storage="sqlite:///optuna.db",
    load_if_exists=True,
)

# Optimera
study.optimize(
    objective,
    n_trials=100,
    timeout=3600,  # 1 hour
    n_jobs=4,      # Parallel trials
)

# Resultat
print(f"Best trial: {study.best_trial.value}")
print(f"Best params: {study.best_trial.params}")
```

### Advanced Pruning
```python
import optuna
from optuna.pruners import MedianPruner
from optuna.samplers import TPESampler

def objective_with_pruning(trial):
    \"\"\"Neural network training with early pruning\"\"\"

    # Hyperparameters
    n_layers = trial.suggest_int("n_layers", 1, 4)
    hidden_size = trial.suggest_int("hidden_size", 32, 256)
    lr = trial.suggest_float("lr", 1e-5, 1e-1, log=True)
    dropout = trial.suggest_float("dropout", 0.1, 0.5)

    model = build_model(n_layers, hidden_size, dropout)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(100):
        train_loss = train_epoch(model, train_loader, optimizer)
        val_loss = validate(model, val_loader)

        # Report intermediate value
        trial.report(val_loss, epoch)

        # Prune trial if not promising
        if trial.should_prune():
            raise optuna.TrialPruned()

    return val_loss

# Studie med pruning
study = optuna.create_study(
    direction="minimize",
    sampler=TPESampler(seed=42),
    pruner=MedianPruner(n_startup_trials=10, n_warmup_steps=20),
)

study.optimize(objective_with_pruning, n_trials=100)
```

## Ray Tune (Distributed)

```python
from ray import tune
from ray.tune.schedulers import ASHAScheduler
from ray.tune.search.optuna import OptunaSearch

def train_model(config):
    \"\"\"Training function for Ray Tune\"\"\"

    model = XGBClassifier(
        n_estimators=config["n_estimators"],
        max_depth=config["max_depth"],
        learning_rate=config["learning_rate"],
        subsample=config["subsample"],
    )

    for epoch in range(config["epochs"]):
        model.fit(X_train, y_train,
                  eval_set=[(X_val, y_val)],
                  early_stopping_rounds=10,
                  verbose=False)

        val_score = model.score(X_val, y_val)

        # Report to Ray
        tune.report(val_accuracy=val_score, epoch=epoch)

# Search space
search_space = {
    "n_estimators": tune.randint(50, 500),
    "max_depth": tune.randint(3, 15),
    "learning_rate": tune.loguniform(1e-4, 1e-1),
    "subsample": tune.uniform(0.5, 1.0),
    "epochs": 50,
}

# Scheduler for early stopping
scheduler = ASHAScheduler(
    metric="val_accuracy",
    mode="max",
    max_t=50,
    grace_period=10,
    reduction_factor=2,
)

# Run tuning
analysis = tune.run(
    train_model,
    config=search_space,
    num_samples=100,
    scheduler=scheduler,
    resources_per_trial={"cpu": 2, "gpu": 0.5},
    local_dir="./ray_results",
)

# Best config
best_config = analysis.get_best_config(metric="val_accuracy", mode="max")
print(f"Best config: {best_config}")
```

## Keras Tuner

```python
import keras_tuner as kt
import tensorflow as tf

def build_model(hp):
    \"\"\"Model builder for Keras Tuner\"\"\"
    model = tf.keras.Sequential()

    # Tune number of layers
    for i in range(hp.Int("num_layers", 1, 4)):
        model.add(tf.keras.layers.Dense(
            units=hp.Int(f"units_{i}", min_value=32, max_value=512, step=32),
            activation="relu"
        ))
        model.add(tf.keras.layers.Dropout(
            hp.Float(f"dropout_{i}", 0.1, 0.5, step=0.1)
        ))

    model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

    # Tune learning rate
    lr = hp.Float("learning_rate", 1e-4, 1e-2, sampling="log")

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model

# Bayesian optimization tuner
tuner = kt.BayesianOptimization(
    build_model,
    objective="val_accuracy",
    max_trials=50,
    directory="keras_tuner",
    project_name="fraud_detection"
)

# Search
tuner.search(
    X_train, y_train,
    epochs=50,
    validation_data=(X_val, y_val),
    callbacks=[tf.keras.callbacks.EarlyStopping(patience=5)]
)

# Best model
best_model = tuner.get_best_models(num_models=1)[0]
best_hp = tuner.get_best_hyperparameters(num_trials=1)[0]
```

## Best Practices

1. **Start med Random Search** - ofta 60 trials räcker
2. **Logscale för learning rates** - `log_uniform(1e-5, 0.1)`
3. **Early stopping/Pruning** - spara tid
4. **Reproducerbarhet** - sätt seeds
5. **Track allt** - logga till MLflow/W&B
"""
            },
            {
                "title": "CI/CD for ML Pipelines",
                "difficulty": "hard",
                "estimated_minutes": 40,
                "xp_reward": 110,
                "content": r"""# CI/CD for Machine Learning

## ML CI/CD vs Traditional CI/CD

```
┌──────────────────────────────────────────────────────────────────────────┐
│                      Traditional CI/CD                                    │
│  Code Change → Build → Test → Deploy                                     │
├──────────────────────────────────────────────────────────────────────────┤
│                      ML CI/CD                                             │
│  Code Change ─┐                                                           │
│  Data Change ─┼→ Validate → Train → Evaluate → Register → Deploy        │
│  Model Change┘     │          │        │          │          │           │
│                    ▼          ▼        ▼          ▼          ▼           │
│               Schema     Experiment  Metrics   Model      Endpoint      │
│               Tests      Tracking    Gates    Registry    Monitor       │
└──────────────────────────────────────────────────────────────────────────┘
```

## GitHub Actions for ML

### Training Pipeline
```yaml
# .github/workflows/ml-train.yml
name: ML Training Pipeline

on:
  push:
    paths:
      - 'src/model/**'
      - 'data/**'
      - 'configs/**'
  schedule:
    - cron: '0 2 * * 0'  # Weekly retraining
  workflow_dispatch:
    inputs:
      model_type:
        description: 'Model type to train'
        required: true
        default: 'xgboost'

env:
  MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}
  WANDB_API_KEY: ${{ secrets.WANDB_API_KEY }}

jobs:
  validate-data:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Validate data schema
        run: python scripts/validate_data.py

      - name: Check data quality
        run: |
          python -c "
          import great_expectations as gx
          context = gx.get_context()
          result = context.run_checkpoint('data_quality_checkpoint')
          if not result.success:
              raise ValueError('Data quality check failed')
          "

  train:
    needs: validate-data
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Train model
        id: train
        run: |
          python train.py \
            --config configs/production.yaml \
            --model-type ${{ github.event.inputs.model_type || 'xgboost' }}

          # Extract metrics
          echo "model_uri=$(cat outputs/model_uri.txt)" >> $GITHUB_OUTPUT
          echo "accuracy=$(cat outputs/accuracy.txt)" >> $GITHUB_OUTPUT

      - name: Upload model artifact
        uses: actions/upload-artifact@v4
        with:
          name: trained-model
          path: outputs/model/

    outputs:
      model_uri: ${{ steps.train.outputs.model_uri }}
      accuracy: ${{ steps.train.outputs.accuracy }}

  evaluate:
    needs: train
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Download model
        uses: actions/download-artifact@v4
        with:
          name: trained-model
          path: model/

      - name: Evaluate model
        id: evaluate
        run: |
          python evaluate.py \
            --model-path model/ \
            --test-data data/test.csv

      - name: Model quality gate
        run: |
          python scripts/quality_gate.py \
            --min-accuracy 0.90 \
            --max-latency-ms 50 \
            --metrics-file outputs/metrics.json

      - name: Generate model report
        run: |
          python scripts/generate_report.py \
            --metrics outputs/metrics.json \
            --output reports/model_report.md

      - name: Comment PR with results
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('reports/model_report.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: report
            });

  register:
    needs: [train, evaluate]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - uses: actions/checkout@v4

      - name: Download model
        uses: actions/download-artifact@v4
        with:
          name: trained-model
          path: model/

      - name: Register model
        run: |
          python scripts/register_model.py \
            --model-path model/ \
            --model-name fraud-detector \
            --stage staging
```

### Model Deployment
```yaml
# .github/workflows/ml-deploy.yml
name: Model Deployment

on:
  workflow_dispatch:
    inputs:
      model_version:
        description: 'Model version to deploy'
        required: true
      environment:
        description: 'Target environment'
        required: true
        type: choice
        options:
          - staging
          - production

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ github.event.inputs.environment }}

    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-west-1

      - name: Download model from registry
        run: |
          python scripts/download_model.py \
            --model-name fraud-detector \
            --version ${{ github.event.inputs.model_version }} \
            --output model/

      - name: Build inference container
        run: |
          docker build -t fraud-detector:${{ github.event.inputs.model_version }} \
            -f Dockerfile.inference .

      - name: Push to ECR
        run: |
          aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REGISTRY
          docker push $ECR_REGISTRY/fraud-detector:${{ github.event.inputs.model_version }}

      - name: Deploy to SageMaker
        run: |
          python scripts/deploy_sagemaker.py \
            --model-name fraud-detector \
            --image $ECR_REGISTRY/fraud-detector:${{ github.event.inputs.model_version }} \
            --environment ${{ github.event.inputs.environment }}

      - name: Smoke test
        run: |
          python scripts/smoke_test.py \
            --endpoint fraud-detector-${{ github.event.inputs.environment }}
```

## Data Version Control (DVC)

```yaml
# .github/workflows/dvc-pipeline.yml
name: DVC Pipeline

on:
  push:
    paths:
      - 'dvc.yaml'
      - 'params.yaml'
      - 'src/**'

jobs:
  run-pipeline:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: iterative/setup-dvc@v1

      - name: Configure DVC remote
        run: |
          dvc remote modify origin --local auth basic
          dvc remote modify origin --local user ${{ secrets.DVC_USER }}
          dvc remote modify origin --local password ${{ secrets.DVC_PASSWORD }}

      - name: Pull data
        run: dvc pull

      - name: Reproduce pipeline
        run: dvc repro

      - name: Push results
        run: dvc push

      - name: CML Report
        uses: iterative/setup-cml@v2
        env:
          REPO_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          cml comment create report.md
```

## Testing Strategies

```python
# tests/test_model.py
import pytest
import pandas as pd
import numpy as np

class TestModelTraining:
    \"\"\"Tests för modell-träning\"\"\"

    def test_model_trains_without_errors(self, sample_data, model_config):
        \"\"\"Model should complete training\"\"\"
        model = train_model(sample_data, model_config)
        assert model is not None

    def test_model_accuracy_above_threshold(self, trained_model, test_data):
        \"\"\"Model should meet minimum accuracy\"\"\"
        accuracy = trained_model.score(test_data.X, test_data.y)
        assert accuracy > 0.85

    def test_model_prediction_shape(self, trained_model, test_data):
        \"\"\"Predictions should have correct shape\"\"\"
        predictions = trained_model.predict(test_data.X)
        assert len(predictions) == len(test_data.y)

    def test_model_handles_edge_cases(self, trained_model):
        \"\"\"Model should handle edge cases gracefully\"\"\"
        edge_cases = pd.DataFrame({
            'amount': [0, 1e10, -1],
            'merchant': ['unknown', '', None],
        })
        # Should not raise
        predictions = trained_model.predict(edge_cases)
        assert all(p in [0, 1] for p in predictions)


class TestModelIntegrity:
    \"\"\"Tests för modell-integritet\"\"\"

    def test_model_reproducibility(self, sample_data, model_config):
        \"\"\"Same inputs should give same outputs\"\"\"
        model1 = train_model(sample_data, model_config)
        model2 = train_model(sample_data, model_config)

        preds1 = model1.predict(sample_data.X[:100])
        preds2 = model2.predict(sample_data.X[:100])

        assert np.array_equal(preds1, preds2)

    def test_model_feature_importance_stable(self, trained_model):
        \"\"\"Top features should be consistent\"\"\"
        importance = trained_model.feature_importances_
        top_features = np.argsort(importance)[-5:]

        # Verify known important features are present
        assert 'amount' in top_features
        assert 'merchant_risk_score' in top_features
```

## Best Practices

1. **Separate pipelines** för code, data, och modell
2. **Quality gates** - automatisk validering
3. **Canary deployments** - gradvis utrullning
4. **Rollback capability** - snabb återställning
5. **Comprehensive testing** - unit, integration, model tests
"""
            },
            {
                "title": "ML Pipeline Orchestration",
                "difficulty": "hard",
                "estimated_minutes": 40,
                "xp_reward": 110,
                "content": r"""# ML Pipeline Orchestration

## Orchestration Tools

```
┌────────────────────────────────────────────────────────────────────┐
│                    Orchestration Landscape                          │
│                                                                     │
│  General Purpose          │       ML-Specific                       │
│  ─────────────────────    │       ───────────────                   │
│  • Apache Airflow         │       • Kubeflow Pipelines              │
│  • Prefect                │       • MLflow Pipelines                │
│  • Dagster                │       • Metaflow                         │
│  • Luigi                  │       • ZenML                            │
│  • Argo Workflows         │       • Kedro                            │
└────────────────────────────────────────────────────────────────────┘
```

## Apache Airflow

### Basic ML DAG
```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.operators.s3 import S3CopyObjectOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args = {
    'owner': 'ml-team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email': ['ml-alerts@company.com'],
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'fraud_detection_training',
    default_args=default_args,
    description='Weekly fraud detection model training',
    schedule_interval='0 2 * * 0',  # Sundays 2 AM
    catchup=False,
    tags=['ml', 'fraud-detection'],
)

def extract_data(**context):
    \"\"\"Extract training data from data warehouse\"\"\"
    from data_pipeline import DataExtractor

    extractor = DataExtractor()
    df = extractor.get_training_data(
        start_date=context['data_interval_start'],
        end_date=context['data_interval_end'],
    )

    # Push to XCom
    output_path = f"s3://bucket/data/{context['ds']}/training.parquet"
    df.to_parquet(output_path)

    return output_path

def validate_data(**context):
    \"\"\"Validate data quality\"\"\"
    import great_expectations as gx

    data_path = context['ti'].xcom_pull(task_ids='extract_data')

    context = gx.get_context()
    result = context.run_checkpoint(
        checkpoint_name='training_data_checkpoint',
        batch_request={'path': data_path}
    )

    if not result.success:
        raise ValueError("Data validation failed")

    return data_path

def train_model(**context):
    \"\"\"Train model with MLflow tracking\"\"\"
    import mlflow
    from training import Trainer

    data_path = context['ti'].xcom_pull(task_ids='validate_data')

    with mlflow.start_run(run_name=f"training_{context['ds']}"):
        trainer = Trainer(config='configs/production.yaml')
        model_uri = trainer.train(data_path)

        mlflow.log_param("data_date", context['ds'])

    return model_uri

def evaluate_model(**context):
    \"\"\"Evaluate model performance\"\"\"
    import mlflow
    from evaluation import Evaluator

    model_uri = context['ti'].xcom_pull(task_ids='train_model')

    evaluator = Evaluator()
    metrics = evaluator.evaluate(
        model_uri=model_uri,
        test_data="s3://bucket/data/test.parquet"
    )

    # Quality gate
    if metrics['f1_score'] < 0.90:
        raise ValueError(f"Model quality below threshold: {metrics}")

    return metrics

def register_model(**context):
    \"\"\"Register model if it passes evaluation\"\"\"
    import mlflow

    model_uri = context['ti'].xcom_pull(task_ids='train_model')
    metrics = context['ti'].xcom_pull(task_ids='evaluate_model')

    result = mlflow.register_model(
        model_uri=model_uri,
        name="fraud-detector"
    )

    # Promote to staging
    client = mlflow.tracking.MlflowClient()
    client.transition_model_version_stage(
        name="fraud-detector",
        version=result.version,
        stage="Staging"
    )

    return result.version

# Define tasks
extract = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

validate = PythonOperator(
    task_id='validate_data',
    python_callable=validate_data,
    dag=dag,
)

train = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

evaluate = PythonOperator(
    task_id='evaluate_model',
    python_callable=evaluate_model,
    dag=dag,
)

register = PythonOperator(
    task_id='register_model',
    python_callable=register_model,
    dag=dag,
)

# Define dependencies
extract >> validate >> train >> evaluate >> register
```

## Prefect

```python
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta

@task(
    retries=3,
    retry_delay_seconds=60,
    cache_key_fn=task_input_hash,
    cache_expiration=timedelta(days=1),
)
def extract_data(date: str) -> str:
    \"\"\"Extract data with caching\"\"\"
    from data_pipeline import DataExtractor

    extractor = DataExtractor()
    df = extractor.get_training_data(date=date)

    output_path = f"data/training_{date}.parquet"
    df.to_parquet(output_path)

    return output_path

@task(retries=2)
def validate_data(data_path: str) -> str:
    \"\"\"Validate data quality\"\"\"
    import great_expectations as gx

    context = gx.get_context()
    result = context.run_checkpoint(
        checkpoint_name='data_quality',
        batch_request={'path': data_path}
    )

    if not result.success:
        raise ValueError("Validation failed")

    return data_path

@task(log_prints=True)
def train_model(data_path: str, config: dict) -> str:
    \"\"\"Train model\"\"\"
    import mlflow

    print(f"Training with config: {config}")

    with mlflow.start_run():
        # Training logic...
        model_uri = "runs:/abc123/model"

    return model_uri

@task
def deploy_model(model_uri: str, environment: str):
    \"\"\"Deploy model to environment\"\"\"
    from deployment import deploy_to_kubernetes

    deploy_to_kubernetes(
        model_uri=model_uri,
        namespace=f"ml-{environment}"
    )

@flow(name="fraud-detection-training")
def training_pipeline(
    date: str,
    config: dict,
    deploy: bool = False,
    environment: str = "staging"
):
    \"\"\"Main training flow\"\"\"

    # Extract and validate
    data_path = extract_data(date)
    validated_path = validate_data(data_path)

    # Train
    model_uri = train_model(validated_path, config)

    # Optionally deploy
    if deploy:
        deploy_model(model_uri, environment)

    return model_uri

# Run the flow
if __name__ == "__main__":
    training_pipeline(
        date="2024-01-15",
        config={"n_estimators": 100},
        deploy=True,
        environment="staging"
    )
```

## Kubeflow Pipelines

```python
from kfp import dsl
from kfp.dsl import component, Output, Input, Dataset, Model, Metrics

@component(
    base_image="python:3.11",
    packages_to_install=["pandas", "sklearn"]
)
def preprocess_data(
    input_data: Input[Dataset],
    output_data: Output[Dataset],
):
    import pandas as pd
    from sklearn.preprocessing import StandardScaler

    df = pd.read_parquet(input_data.path)

    # Preprocessing
    scaler = StandardScaler()
    df[['amount', 'age']] = scaler.fit_transform(df[['amount', 'age']])

    df.to_parquet(output_data.path)

@component(
    base_image="python:3.11",
    packages_to_install=["pandas", "sklearn", "xgboost", "mlflow"]
)
def train_model(
    training_data: Input[Dataset],
    model_artifact: Output[Model],
    metrics: Output[Metrics],
    n_estimators: int = 100,
    max_depth: int = 10,
):
    import pandas as pd
    import mlflow
    from xgboost import XGBClassifier
    from sklearn.model_selection import train_test_split

    df = pd.read_parquet(training_data.path)
    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

    model = XGBClassifier(n_estimators=n_estimators, max_depth=max_depth)
    model.fit(X_train, y_train)

    # Log metrics
    accuracy = model.score(X_val, y_val)
    metrics.log_metric('accuracy', accuracy)

    # Save model
    model.save_model(model_artifact.path)

@dsl.pipeline(
    name='fraud-detection-pipeline',
    description='Training pipeline for fraud detection'
)
def fraud_detection_pipeline(
    input_data_path: str,
    n_estimators: int = 100,
    max_depth: int = 10,
):
    # Preprocess
    preprocess_task = preprocess_data(input_data=input_data_path)

    # Train
    train_task = train_model(
        training_data=preprocess_task.outputs['output_data'],
        n_estimators=n_estimators,
        max_depth=max_depth,
    )

# Compile and run
from kfp import compiler

compiler.Compiler().compile(
    fraud_detection_pipeline,
    'pipeline.yaml'
)
```

## Best Practices

1. **Idempotent tasks** - kan köras om säkert
2. **Clear dependencies** - explicit DAG
3. **Monitoring** - alerts och dashboards
4. **Parameterization** - konfigurerbara pipelines
5. **Testing** - unit tester för tasks
"""
            },
            {
                "title": "Model Serving & Inference",
                "difficulty": "hard",
                "estimated_minutes": 40,
                "xp_reward": 110,
                "content": r"""# Model Serving & Inference

## Serving Patterns

```
┌─────────────────────────────────────────────────────────────────────┐
│                     Model Serving Patterns                           │
│                                                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                  │
│  │   Online    │  │    Batch    │  │  Streaming  │                  │
│  │  Inference  │  │  Inference  │  │  Inference  │                  │
│  │             │  │             │  │             │                  │
│  │ REST/gRPC   │  │ Spark/Dask  │  │ Kafka/Flink │                  │
│  │ <100ms      │  │ Hours       │  │ Near-RT     │                  │
│  │ Per request │  │ Bulk data   │  │ Continuous  │                  │
│  └─────────────┘  └─────────────┘  └─────────────┘                  │
└─────────────────────────────────────────────────────────────────────┘
```

## FastAPI Model Server

```python
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import List, Optional
import mlflow
import numpy as np
from prometheus_client import Counter, Histogram, generate_latest
import time

app = FastAPI(title="Fraud Detection API", version="1.0.0")

# Metrics
PREDICTIONS = Counter('model_predictions_total', 'Total predictions', ['result'])
LATENCY = Histogram('model_inference_latency_seconds', 'Inference latency')

# Load model at startup
model = None

@app.on_event("startup")
async def load_model():
    global model
    model = mlflow.pyfunc.load_model("models:/fraud-detector/Production")

class TransactionRequest(BaseModel):
    transaction_id: str
    amount: float = Field(..., gt=0)
    merchant_id: str
    user_id: str
    timestamp: str
    device_fingerprint: Optional[str] = None

class PredictionResponse(BaseModel):
    transaction_id: str
    is_fraud: bool
    fraud_probability: float
    model_version: str
    inference_time_ms: float

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: TransactionRequest):
    start_time = time.time()

    try:
        # Prepare features
        features = prepare_features(request)

        # Inference
        with LATENCY.time():
            probabilities = model.predict_proba(features)

        fraud_prob = float(probabilities[0][1])
        is_fraud = fraud_prob > 0.5

        # Track metrics
        PREDICTIONS.labels(result="fraud" if is_fraud else "legitimate").inc()

        inference_time = (time.time() - start_time) * 1000

        return PredictionResponse(
            transaction_id=request.transaction_id,
            is_fraud=is_fraud,
            fraud_probability=fraud_prob,
            model_version=model.metadata.get("version", "unknown"),
            inference_time_ms=inference_time,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class BatchRequest(BaseModel):
    transactions: List[TransactionRequest]

@app.post("/predict/batch")
async def predict_batch(request: BatchRequest):
    features = [prepare_features(tx) for tx in request.transactions]
    features_array = np.vstack(features)

    probabilities = model.predict_proba(features_array)

    results = []
    for i, tx in enumerate(request.transactions):
        results.append({
            "transaction_id": tx.transaction_id,
            "is_fraud": probabilities[i][1] > 0.5,
            "fraud_probability": float(probabilities[i][1]),
        })

    return {"predictions": results}

@app.get("/health")
async def health():
    return {"status": "healthy", "model_loaded": model is not None}

@app.get("/metrics")
async def metrics():
    return generate_latest()
```

## TensorFlow Serving

```bash
# Pull TensorFlow Serving image
docker pull tensorflow/serving

# Start server with model
docker run -p 8501:8501 \
    -v /path/to/model:/models/fraud_detector \
    -e MODEL_NAME=fraud_detector \
    tensorflow/serving
```

```python
import requests
import json

# REST API call
url = "http://localhost:8501/v1/models/fraud_detector:predict"

data = {
    "instances": [
        {"amount": 150.0, "merchant_type": "retail", "hour": 14}
    ]
}

response = requests.post(url, json=data)
predictions = response.json()["predictions"]
```

## Triton Inference Server

```python
# model_repository/fraud_detector/config.pbtxt
\"\"\"
name: "fraud_detector"
platform: "onnxruntime_onnx"
max_batch_size: 64
input [
  {
    name: "input"
    data_type: TYPE_FP32
    dims: [ 10 ]  # feature count
  }
]
output [
  {
    name: "output"
    data_type: TYPE_FP32
    dims: [ 2 ]  # class probabilities
  }
]
instance_group [
  {
    count: 2
    kind: KIND_GPU
  }
]
dynamic_batching {
  preferred_batch_size: [ 16, 32 ]
  max_queue_delay_microseconds: 100
}
\"\"\"

# Client code
import tritonclient.http as httpclient
import numpy as np

client = httpclient.InferenceServerClient(url="localhost:8000")

# Prepare input
inputs = [httpclient.InferInput("input", [1, 10], "FP32")]
inputs[0].set_data_from_numpy(features.astype(np.float32))

# Inference
outputs = [httpclient.InferRequestedOutput("output")]
result = client.infer("fraud_detector", inputs, outputs=outputs)

predictions = result.as_numpy("output")
```

## AWS SageMaker

```python
import sagemaker
from sagemaker.sklearn import SKLearnModel

# Deploy model
sklearn_model = SKLearnModel(
    model_data="s3://bucket/model/model.tar.gz",
    role="arn:aws:iam::123456789:role/SageMakerRole",
    framework_version="1.2-1",
    py_version="py3",
)

predictor = sklearn_model.deploy(
    instance_type="ml.t2.medium",
    initial_instance_count=2,
    endpoint_name="fraud-detector-endpoint",
)

# Invoke endpoint
import boto3
import json

runtime = boto3.client("sagemaker-runtime")

response = runtime.invoke_endpoint(
    EndpointName="fraud-detector-endpoint",
    ContentType="application/json",
    Body=json.dumps({"features": [100.0, 1, 14]})
)

predictions = json.loads(response["Body"].read())
```

## KServe (Kubernetes)

```yaml
# fraud-detector-isvc.yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: fraud-detector
spec:
  predictor:
    sklearn:
      storageUri: "gs://bucket/models/fraud-detector"
      resources:
        requests:
          cpu: "1"
          memory: "2Gi"
        limits:
          cpu: "2"
          memory: "4Gi"
  transformer:
    containers:
      - name: feature-transformer
        image: my-registry/feature-transformer:v1
        resources:
          requests:
            cpu: "0.5"
            memory: "1Gi"
```

```bash
kubectl apply -f fraud-detector-isvc.yaml

# Test inference
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"instances": [{"amount": 100.0}]}' \
    http://fraud-detector.default.example.com/v1/models/fraud-detector:predict
```

## A/B Testing

```python
from fastapi import FastAPI
import random

app = FastAPI()

# Model versions
models = {
    "v1": load_model("models:/fraud-detector/1"),
    "v2": load_model("models:/fraud-detector/2"),
}

# Traffic split
TRAFFIC_SPLIT = {"v1": 0.8, "v2": 0.2}

@app.post("/predict")
async def predict(request: TransactionRequest):
    # Select model based on traffic split
    model_version = random.choices(
        list(TRAFFIC_SPLIT.keys()),
        weights=list(TRAFFIC_SPLIT.values())
    )[0]

    model = models[model_version]
    result = model.predict(prepare_features(request))

    # Log for analysis
    log_prediction(
        transaction_id=request.transaction_id,
        model_version=model_version,
        prediction=result,
    )

    return {"prediction": result, "model_version": model_version}
```
"""
            },
            {
                "title": "ML Containerization",
                "difficulty": "medium",
                "estimated_minutes": 35,
                "xp_reward": 100,
                "content": r"""# ML Containerization

## Training Container

```dockerfile
# Dockerfile.train
FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy training code
COPY src/ ./src/
COPY configs/ ./configs/
COPY train.py .

# Environment variables
ENV MLFLOW_TRACKING_URI=http://mlflow:5000
ENV PYTHONUNBUFFERED=1

# Entry point
ENTRYPOINT ["python", "train.py"]
CMD ["--config", "configs/default.yaml"]
```

## Inference Container

```dockerfile
# Dockerfile.serve
FROM python:3.11-slim AS base

WORKDIR /app

# Install dependencies
COPY requirements-serve.txt .
RUN pip install --no-cache-dir -r requirements-serve.txt

# Multi-stage build - copy model
FROM base AS production

# Copy inference code
COPY src/inference/ ./src/inference/
COPY serve.py .

# Create non-root user
RUN useradd --create-home appuser
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
    CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8000"]
```

## GPU Container

```dockerfile
# Dockerfile.gpu
FROM nvidia/cuda:12.1-runtime-ubuntu22.04

WORKDIR /app

# Python installation
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# PyTorch with CUDA
RUN pip install --no-cache-dir \
    torch==2.1.0+cu121 \
    torchvision==0.16.0+cu121 \
    -f https://download.pytorch.org/whl/torch_stable.html

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "train.py"]
```

## Docker Compose for ML Stack

```yaml
# docker-compose.yml
version: '3.8'

services:
  mlflow:
    image: ghcr.io/mlflow/mlflow:v2.9.2
    ports:
      - "5000:5000"
    environment:
      - MLFLOW_BACKEND_STORE_URI=postgresql://mlflow:mlflow@postgres:5432/mlflow
      - MLFLOW_ARTIFACT_ROOT=s3://mlflow-artifacts
      - AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
      - AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
    command: mlflow server --host 0.0.0.0
    depends_on:
      - postgres

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_USER=mlflow
      - POSTGRES_PASSWORD=mlflow
      - POSTGRES_DB=mlflow
    volumes:
      - postgres_data:/var/lib/postgresql/data

  jupyter:
    build:
      context: .
      dockerfile: Dockerfile.jupyter
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/app/notebooks
      - ./data:/app/data
    environment:
      - MLFLOW_TRACKING_URI=http://mlflow:5000

  training:
    build:
      context: .
      dockerfile: Dockerfile.train
    volumes:
      - ./data:/app/data
      - ./models:/app/models
    environment:
      - MLFLOW_TRACKING_URI=http://mlflow:5000
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  inference:
    build:
      context: .
      dockerfile: Dockerfile.serve
    ports:
      - "8000:8000"
    environment:
      - MODEL_URI=models:/fraud-detector/Production
      - MLFLOW_TRACKING_URI=http://mlflow:5000
    deploy:
      replicas: 2

  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana

volumes:
  postgres_data:
  grafana_data:
```

## Kubernetes Deployment

```yaml
# k8s/model-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fraud-detector
  labels:
    app: fraud-detector
spec:
  replicas: 3
  selector:
    matchLabels:
      app: fraud-detector
  template:
    metadata:
      labels:
        app: fraud-detector
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8000"
    spec:
      containers:
        - name: model-server
          image: registry.company.com/fraud-detector:v1.2.0
          ports:
            - containerPort: 8000
          env:
            - name: MODEL_URI
              value: "models:/fraud-detector/Production"
            - name: MLFLOW_TRACKING_URI
              valueFrom:
                secretKeyRef:
                  name: mlflow-credentials
                  key: uri
          resources:
            requests:
              cpu: "1"
              memory: "2Gi"
            limits:
              cpu: "2"
              memory: "4Gi"
          livenessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 5
            periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: fraud-detector
spec:
  selector:
    app: fraud-detector
  ports:
    - port: 80
      targetPort: 8000
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: fraud-detector-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: fraud-detector
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Pods
      pods:
        metric:
          name: http_requests_per_second
        target:
          type: AverageValue
          averageValue: "100"
```

## Best Practices

1. **Slim base images** - minska attack surface
2. **Multi-stage builds** - separera build från runtime
3. **Pin versions** - reproducerbarhet
4. **Non-root user** - säkerhet
5. **Health checks** - container orchestration
6. **Resource limits** - förutsägbart beteende
"""
            },
            {
                "title": "Model Monitoring & Observability",
                "difficulty": "hard",
                "estimated_minutes": 40,
                "xp_reward": 110,
                "content": r"""# Model Monitoring & Observability

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
    \"\"\"Detect data drift using Evidently\"\"\"

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
    \"\"\"Calculate PSI for a feature\"\"\"

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
        \"\"\"Update accuracy based on delayed ground truth\"\"\"
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
        \"\"\"Check metrics against thresholds\"\"\"
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
        \"\"\"Send alert to Slack\"\"\"
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
"""
            },
            {
                "title": "Feature Stores",
                "difficulty": "hard",
                "estimated_minutes": 35,
                "xp_reward": 100,
                "content": r"""# Feature Stores

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
    \"\"\"Compute features on-demand at serving time\"\"\"

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
    \"\"\"Reusable feature engineering patterns\"\"\"

    @staticmethod
    def rolling_aggregates(
        df: pd.DataFrame,
        group_col: str,
        value_col: str,
        windows: List[int],
        timestamp_col: str = "timestamp"
    ) -> pd.DataFrame:
        \"\"\"Create rolling aggregate features\"\"\"

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
        \"\"\"Count encoding for categorical features\"\"\"

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
        \"\"\"Target encoding with smoothing\"\"\"

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
"""
            },
            {
                "title": "AutoML & Neural Architecture Search",
                "difficulty": "hard",
                "estimated_minutes": 30,
                "xp_reward": 100,
                "content": r"""# AutoML & Neural Architecture Search

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
"""
            },
            {
                "title": "Production MLOps Best Practices",
                "difficulty": "hard",
                "estimated_minutes": 40,
                "xp_reward": 120,
                "content": r"""# Production MLOps Best Practices

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
        report = f"# Production Readiness Report\n"
        report += f"## Model: {self.model_name} v{self.version}\n\n"

        for check in self.checks:
            emoji = {
                CheckStatus.PASSED: "✅",
                CheckStatus.FAILED: "❌",
                CheckStatus.WARNING: "⚠️",
                CheckStatus.SKIPPED: "⏭️",
            }[check.status]

            report += f"### {emoji} {check.name}\n"
            report += f"{check.description}\n"
            report += f"**Details:** {check.details}\n\n"

        return report

def run_production_checks(model_path: str, test_data_path: str) -> ProductionChecklist:
    \"\"\"Run all production readiness checks\"\"\"

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
        \"\"\"Deploy canary alongside stable model\"\"\"
        self.models = {
            "stable": stable_model,
            "canary": canary_model,
        }

    def route_request(self, request) -> str:
        \"\"\"Route request to appropriate model\"\"\"
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
        \"\"\"Record ground truth feedback\"\"\"
        self.metrics[model_version].append(correct)

    def evaluate_canary(self) -> str:
        \"\"\"Evaluate canary performance\"\"\"
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
        \"\"\"Gradually increase canary traffic\"\"\"
        self.config.canary_percentage = min(
            100.0,
            self.config.canary_percentage + step
        )

    def promote_canary(self):
        \"\"\"Promote canary to stable\"\"\"
        self.models["stable"] = self.models["canary"]
        self.config.canary_percentage = 0.0
        self.metrics = {"stable": [], "canary": []}

    def rollback(self):
        \"\"\"Rollback to stable\"\"\"
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
    \"\"\"ML-specific incident response runbook\"\"\"

    @staticmethod
    def model_accuracy_drop():
        return \"\"\"
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
        \"\"\"

    @staticmethod
    def high_latency():
        return \"\"\"
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
        \"\"\"
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
"""
            },
    ],
    "labs": [],
}


def get_module():
    """Returns the module definition."""
    return MODULE_MLOPS


def get_tasks():
    """Returns all tasks for this module."""
    return MODULE_MLOPS["tasks"]


def get_task_count():
    """Returns the number of tasks."""
    return len(get_tasks())
