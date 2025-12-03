"""
MLOps SkillsMap - Block 1: Fundamentals
Nodes 1-4: Programming, Version Control, Cloud, Containers
"""

BLOCK_1_NODES = [
    # Node 1: Introduction to MLOps
    {
        "id": "mlops-intro",
        "slug": "mlops-introduction",
        "title": "Introduction to MLOps",
        "order_index": 1,
        "estimated_minutes": 25,
        "xp_reward": 50,
        "difficulty": "easy",
        "node_type": "concept",
        "prerequisites": [],
        "content": """# Introduction to MLOps

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
        print(f"\\n{level.upper()}:")
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

    # Node 2: Python for ML
    {
        "id": "mlops-python",
        "slug": "python-for-ml",
        "title": "Python for Machine Learning",
        "order_index": 2,
        "estimated_minutes": 35,
        "xp_reward": 75,
        "difficulty": "easy",
        "node_type": "practice",
        "prerequisites": ["mlops-intro"],
        "content": """# Python for Machine Learning

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

    # Node 3: Version Control for ML
    {
        "id": "mlops-version-control",
        "slug": "version-control-ml",
        "title": "Version Control for ML",
        "order_index": 3,
        "estimated_minutes": 30,
        "xp_reward": 75,
        "difficulty": "medium",
        "node_type": "practice",
        "prerequisites": ["mlops-python"],
        "content": """# Version Control for ML

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

    # Node 4: Cloud Computing for ML
    {
        "id": "mlops-cloud",
        "slug": "cloud-computing-ml",
        "title": "Cloud Computing for ML",
        "order_index": 4,
        "estimated_minutes": 35,
        "xp_reward": 100,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["mlops-version-control"],
        "content": """# Cloud Computing for ML

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
]
