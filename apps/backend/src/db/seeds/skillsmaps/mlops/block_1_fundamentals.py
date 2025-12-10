"""
MLOps SkillsMap - Block 1: Fundamentals
Nodes 1-4: Introduction, Python for ML, Version Control, Cloud Computing
V3 Format - Swedish, No Emojis
"""

BLOCK_1_NODES = [
    # Node 1: Introduction to MLOps
    {
        "id": "mlops-intro",
        "slug": "mlops-introduction",
        "title": "Introduktion till MLOps",
        "order_index": 1,
        "estimated_minutes": 25,
        "xp_reward": 50,
        "difficulty": "easy",
        "node_type": "concept",
        "prerequisites": [],
        "content": """# Introduktion till MLOps

------------------------------------------------------------

## Vad ar MLOps?

MLOps (Machine Learning Operations) ar en uppsattning praktiker och verktyg for att automatisera och effektivisera hela ML-livscykeln - fran experiment till produktion.

MLOps kombinerar:
- Maskininlarning (ML)
- DevOps-principer
- Datahantering

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Automation | Automatiserar hela ML-livscykeln fran data till produktion |
| Reproducerbarhet | Garanterar att experiment kan aterupprepas exakt |
| Skalbarhet | Mojliggor skalning av ML-system i produktion |
| Samarbete | Forbattrar samarbetet mellan data scientists och DevOps |
| Kvalitet | Sakertstaller kvalitet genom automatiserade tester |

------------------------------------------------------------

## Snabbreferens

| Begrepp | Definition |
|---------|------------|
| MLOps | Praktiker for ML-livscykelhantering |
| ML Pipeline | Automatiserat arbetsflode for ML |
| Model Registry | Central lagring for ML-modeller |
| Feature Store | Central lagring for ML-features |
| CT | Continuous Training - automatisk omtraning |

------------------------------------------------------------

## Utan MLOps vs Med MLOps

Utan MLOps (ML-skuld):

```
+---------------------------------------------------------+
|  Data Scientists Laptop                                 |
|  +-------------+  +-------------+  +-------------+     |
|  | Notebook    |->| model.pkl   |->| Det funkar! |     |
|  | experiment  |  | (lokal)     |  |             |     |
|  +-------------+  +-------------+  +-------------+     |
|                                                         |
|  Manader senare: Vilken version? Vilken data?          |
+---------------------------------------------------------+
```

Med MLOps:

```
+---------------------------------------------------------+
|                    MLOps Pipeline                        |
|                                                          |
|  +--------+  +--------+  +--------+  +------------+    |
|  | Data   |->| Train  |->| Test   |->| Deploy     |    |
|  | Ingest |  | Model  |  | Valid. |  | Monitor    |    |
|  +--------+  +--------+  +--------+  +------------+    |
|       |          |           |             |            |
|       v          v           v             v            |
|  +-------------------------------------------------+   |
|  |        Version Control + Experiment Tracking     |   |
|  |        Model Registry + Feature Store            |   |
|  +-------------------------------------------------+   |
+---------------------------------------------------------+
```

------------------------------------------------------------

## MLOps Mognadsnivaar

### Level 0: Manuell
- Jupyter notebooks
- Manuell deployment
- Ingen versionshantering av modeller
- Ingen automatiserad testning

### Level 1: ML Pipeline Automation
- Automatiserade tranings-pipelines
- Experiment tracking
- Model registry
- Continuous Training (CT)

### Level 2: CI/CD Pipeline Automation
- Automatiserad CI/CD for ML
- A/B-testning
- Continuous Monitoring
- Automatiserad omtraning

------------------------------------------------------------

## MLOps vs DevOps

| Aspekt | DevOps | MLOps |
|--------|--------|-------|
| Artefakt | Kod | Kod + Data + Modell |
| Testning | Unit/Integration | + Datavalidering, Modellvalidering |
| Deployment | Applikation | Model serving |
| Monitoring | App metrics | + Data drift, Model drift |
| Versioning | Kod | Kod + Data + Modell |

------------------------------------------------------------

## MLOps Komponenter

```
+---------------------------------------------------------+
|                     MLOps Stack                          |
+---------------------------------------------------------+
|  Monitoring     | Prometheus, Grafana, Evidently AI     |
+---------------------------------------------------------+
|  Model Serving  | TensorFlow Serving, Seldon, KServe    |
+---------------------------------------------------------+
|  Orchestration  | Airflow, Kubeflow, Prefect, Dagster   |
+---------------------------------------------------------+
|  Experiment     | MLflow, Weights and Biases, Neptune   |
|  Tracking       |                                       |
+---------------------------------------------------------+
|  Feature Store  | Feast, Tecton, Hopsworks              |
+---------------------------------------------------------+
|  Data Pipeline  | Spark, dbt, Airflow, Kafka            |
+---------------------------------------------------------+
|  Infrastructure | Kubernetes, Docker, Terraform         |
+---------------------------------------------------------+
```

------------------------------------------------------------

## Karriarvagar i MLOps

| Roll | Fokus |
|------|-------|
| ML Engineer | Modelltraning och optimering |
| MLOps Engineer | Infrastruktur och pipelines |
| Data Engineer | Data pipelines |
| Platform Engineer | Bygger ML-plattformar |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Modell fungerar lokalt men inte i prod | Miljoskillnader | Anvand containers och standardiserade miljoer |
| Kan inte reproducera resultat | Saknar versionshantering | Implementera DVC och MLflow |
| Modellen presterar samre over tid | Data drift | Implementera kontinuerlig monitoring |
| Lang tid till produktion | Manuella processer | Automatisera med CI/CD pipelines |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| MLOps | Kombinerar ML med DevOps-principer |
| Automation | Nyckeln till skalbar ML |
| Reproducerbarhet | Kritiskt for produktionskvalitet |
| Monitoring | Modeller maste overvakas kontinuerligt |

### Kom ihag
- MLOps ar mer an bara deployment - det ar hela livscykeln
- Borja enkelt och bygg ut gradvis
- Versionshantera allt: kod, data och modeller
- Automatisera sa mycket som mojligt
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

------------------------------------------------------------

## Vad ar Python for ML?

Python ar det dominerande spraket for maskininlarning tack vare sitt rika ekosystem av bibliotek och verktyg. Har fokuserar vi pa ML-specifika bibliotek och monster.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Standardisering | Python ar industristandard for ML |
| Ekosystem | Rikt utbud av bibliotek och verktyg |
| Integration | Enkelt att integrera med DevOps-verktyg |
| Reproducerbarhet | Bra stod for miljohantering |

------------------------------------------------------------

## Snabbreferens

| Bibliotek | Anvandning |
|-----------|------------|
| NumPy | Numeriska berakningar |
| Pandas | Datahantering |
| scikit-learn | Klassisk ML |
| PyTorch | Deep Learning |
| MLflow | Experiment tracking |

------------------------------------------------------------

## ML Python Stack

```
+---------------------------------------------------------+
|                    ML Python Ecosystem                   |
+---------------------------------------------------------+
|  Deep Learning  | PyTorch, TensorFlow, JAX              |
+---------------------------------------------------------+
|  ML Frameworks  | scikit-learn, XGBoost, LightGBM       |
+---------------------------------------------------------+
|  Data Proc.     | Pandas, NumPy, Polars, Dask           |
+---------------------------------------------------------+
|  Visualization  | Matplotlib, Seaborn, Plotly           |
+---------------------------------------------------------+
|  MLOps Tools    | MLflow, DVC, Hydra, ONNX              |
+---------------------------------------------------------+
```

------------------------------------------------------------

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

# Skapa virtuell miljo
uv venv

# Installera dependencies
uv pip install -r requirements.txt
```

------------------------------------------------------------

## NumPy Essentials

```python
import numpy as np

# Vektoroperationer (snabbare an Python-loopar)
X = np.random.randn(1000, 10)  # 1000 samples, 10 features
y = np.random.randint(0, 2, 1000)  # Binary labels

# Broadcasting - automatisk dimension-matchning
weights = np.array([0.1, 0.2, 0.3])
data = np.array([[1, 2, 3], [4, 5, 6]])
result = data * weights

# Effektiva operationer
mean = X.mean(axis=0)  # Medelvarde per kolumn
std = X.std(axis=0)    # Standardavvikelse per kolumn
X_normalized = (X - mean) / std  # Normalisering

# Matrix operationer
W = np.random.randn(10, 5)  # Weight matrix
output = X @ W  # Matrix multiplication
```

------------------------------------------------------------

## Pandas for Data Prep

```python
import pandas as pd

# Ladda och inspektera data
df = pd.read_csv("data/training_data.csv")
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Feature engineering pipeline
def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['age'] = df['age'].fillna(df['age'].median())
    df['age_bucket'] = pd.cut(df['age'], bins=[0, 18, 35, 50, 100],
                              labels=['young', 'adult', 'middle', 'senior'])
    df = pd.get_dummies(df, columns=['category'], prefix='cat')
    df['income_log'] = np.log1p(df['income'])
    return df

df_processed = prepare_features(df)
```

------------------------------------------------------------

## Scikit-learn Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score

numeric_features = ['age', 'income', 'credit_score']
categorical_features = ['occupation', 'education']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline.fit(X_train, y_train)
scores = cross_val_score(pipeline, X_train, y_train, cv=5)
print(f"CV Score: {scores.mean():.3f} (+/- {scores.std():.3f})")

import joblib
joblib.dump(pipeline, 'models/pipeline.joblib')
```

------------------------------------------------------------

## PyTorch Basics

```python
import torch
import torch.nn as nn

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

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
        print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(train_loader):.4f}")
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| ImportError | Saknad dependency | Kontrollera requirements.txt |
| Version conflict | Inkompatibla versioner | Anvand virtuell miljo |
| Memory error | For stor data | Anvand chunking eller Dask |
| Slow training | Ej optimerad kod | Anvand vektoroperationer |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| Environment | Anvand alltid virtuella miljoer |
| Pipelines | Bygg reproducerbara pipelines |
| Typing | Anvand type hints for battre kod |
| Vectorization | Undvik Python-loopar for numerik |

### Kom ihag
- Versionera dina dependencies exakt
- Anvand scikit-learn pipelines for reproducerbarhet
- Testa din kod med pytest
- Dokumentera dina funktioner
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

------------------------------------------------------------

## Vad ar ML Version Control?

ML-versionshantering ar speciell eftersom du maste hantera mer an bara kod - du behover ocksa versionera data och modeller.

```
Traditional Software:
  Kod -> Applikation

Machine Learning:
  Kod + Data + Config + Modell -> ML System

  Alla maste versionshanteras!
```

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Reproducerbarhet | Aterskapa exakt samma resultat |
| Sparbarhet | Spara och jamfor experiment |
| Samarbete | Team kan dela data och modeller |
| Rollback | Aterstall tidigare versioner vid problem |

------------------------------------------------------------

## Snabbreferens

| Verktyg | Anvandning |
|---------|------------|
| Git | Kod-versionshantering |
| DVC | Data och modell-versionshantering |
| MLflow | Experiment tracking |
| Git LFS | Stora filer i Git |

------------------------------------------------------------

## Rekommenderad projektstruktur

```
ml-project/
+-- .git/
+-- .gitignore
+-- .dvc/
+-- pyproject.toml
+-- README.md
+-- configs/
|   +-- config.yaml
|   +-- model/
+-- data/
|   +-- raw/          # Tracked by DVC
|   +-- processed/    # Tracked by DVC
+-- models/           # Tracked by DVC
+-- notebooks/
+-- src/
|   +-- data/
|   +-- features/
|   +-- models/
|   +-- evaluation/
+-- tests/
+-- dvc.yaml
```

------------------------------------------------------------

## DVC - Data Version Control

### Installation och setup

```bash
pip install dvc dvc-s3
dvc init
dvc remote add -d myremote s3://my-bucket/dvc-storage
```

### Versionhantera data

```bash
# Lagg till data under DVC
dvc add data/raw/training_data.csv

# Git-committa .dvc-filen
git add data/raw/training_data.csv.dvc
git commit -m "Add training data v1"

# Pusha data till remote
dvc push

# Hamta data
dvc pull
```

------------------------------------------------------------

## DVC Pipeline

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

  train:
    cmd: python src/models/train.py
    deps:
      - src/models/train.py
      - data/processed/train.csv
    outs:
      - models/model.pkl
    metrics:
      - metrics/train_metrics.json:
          cache: false

  evaluate:
    cmd: python src/evaluation/evaluate.py
    deps:
      - models/model.pkl
      - data/processed/test.csv
    metrics:
      - metrics/test_metrics.json:
          cache: false
```

------------------------------------------------------------

## Git Branching for ML

```
main
  |
  +-- develop
  |     |
  |     +-- feature/new-feature-engineering
  |     |
  |     +-- experiment/xgboost-tuning
  |     |
  |     +-- experiment/transformer-model
  |
  +-- release/v1.2
```

------------------------------------------------------------

## Semantic Versioning for Modeller

```
model-name-v{MAJOR}.{MINOR}.{PATCH}

MAJOR: Breaking API changes, ny modellarkitektur
MINOR: Ny traningsdata, hyperparameter-tuning
PATCH: Bugfixar, minor improvements
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Data inte synkad | Glomde dvc pull | Kor dvc pull efter git pull |
| Stor .git folder | Data i git | Flytta till DVC |
| Kan inte reproducera | Saknar params | Lagg till params i dvc.yaml |
| Merge conflicts | Binara filer | Anvand DVC for stora filer |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| DVC | Anvand for data och modeller |
| Git | Anvand for kod och config |
| Branching | Experiment i separata branches |
| Versioning | Semantic versioning for modeller |

### Kom ihag
- Git for kod, DVC for data och modeller
- Tagg releases med semantic versioning
- Dokumentera varje experiment
- Automatisera med DVC pipelines
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

------------------------------------------------------------

## Vad ar Cloud for ML?

Cloud computing ger tillgang till skalbar berakningskraft och lagringskapacitet for att trana och kora ML-modeller.

```
+---------------------------------------------------------+
|  Local Development         Cloud Training               |
|  +-----------------+       +-----------------+         |
|  | Laptop GPU      |       | 8x A100 80GB    |         |
|  | 8GB VRAM        |       | 640GB VRAM      |         |
|  | Dagar att trana |  ->   | Timmar att trana|         |
|  +-----------------+       +-----------------+         |
+---------------------------------------------------------+
```

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Skalbarhet | Skala upp vid behov, skala ner nar klart |
| Kostnadseffektivitet | Betala endast for anvandning |
| Tillganglighet | Tillgang till kraftfull GPU overallt |
| Managed Services | Fardiga tjanster for ML |

------------------------------------------------------------

## Snabbreferens

| Service | AWS | GCP | Azure |
|---------|-----|-----|-------|
| ML Platform | SageMaker | Vertex AI | Azure ML |
| Compute | EC2, EKS | GCE, GKE | AKS, VMs |
| GPU | p4d, g5 | A2, L4 | NC, ND |
| Storage | S3 | GCS | Blob |

------------------------------------------------------------

## AWS SageMaker

```python
import sagemaker
from sagemaker.pytorch import PyTorch

session = sagemaker.Session()
role = sagemaker.get_execution_role()

estimator = PyTorch(
    entry_point='train.py',
    source_dir='src/',
    role=role,
    instance_count=1,
    instance_type='ml.p3.2xlarge',
    framework_version='2.0',
    py_version='py310',
    hyperparameters={
        'epochs': 10,
        'batch-size': 32,
        'learning-rate': 0.001,
    },
    output_path=f's3://{bucket}/models/',
)

estimator.fit({
    'train': f's3://{bucket}/data/train/',
    'validation': f's3://{bucket}/data/validation/',
})

predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large',
)
```

------------------------------------------------------------

## GCP Vertex AI

```python
from google.cloud import aiplatform

aiplatform.init(
    project='my-project',
    location='us-central1',
    staging_bucket='gs://my-bucket/staging'
)

job = aiplatform.CustomContainerTrainingJob(
    display_name='my-training-job',
    container_uri='gcr.io/my-project/training:latest',
    model_serving_container_image_uri='gcr.io/my-project/serving:latest',
)

model = job.run(
    replica_count=1,
    machine_type='n1-standard-8',
    accelerator_type='NVIDIA_TESLA_V100',
    accelerator_count=1,
)

endpoint = model.deploy(
    machine_type='n1-standard-4',
    min_replica_count=1,
    max_replica_count=3,
)
```

------------------------------------------------------------

## Kostnadsoptimering

| Tips | Besparing |
|------|-----------|
| Spot/Preemptible | 60-90% |
| Right-size instances | 20-50% |
| Auto-shutdown | 30-70% |
| Ratt storage tier | 50-90% |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Hog kostnad | Glommda resurser | Implementera auto-shutdown |
| Spot avbrott | Preemption | Anvand checkpointing |
| Lag prestanda | Fel instance type | Right-size baserat pa workload |
| Data transfer cost | Regioner | Halla data i samma region |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| Spot instances | Anvand for traning, spara 60-90% |
| Managed services | Forenklar MLOps |
| Auto-scaling | Skala efter behov |
| Cost monitoring | Overvaka kostnader kontinuerligt |

### Kom ihag
- Anvand Spot/Preemptible for traning
- Implementera checkpointing for fault tolerance
- Stang av resurser nar de inte anvands
- Overvaka kostnader med budgetalarm
"""
    },
]
