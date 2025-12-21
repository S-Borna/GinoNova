"""
MLOps SkillsMap - Block 3: ML Fundamentals
Nodes 9-12: Training, Experiment Tracking, Model Registry, Hyperparameter Tuning
V3 Format - Swedish, No Emojis
"""

BLOCK_3_NODES = [
    # Node 9: ML Training Best Practices
    {
        "id": "mlops-training",
        "slug": "ml-training-practices",
        "title": "ML Training Best Practices",
        "order_index": 9,
        "estimated_minutes": 35,
        "xp_reward": 100,
        "difficulty": "medium",
        "node_type": "practice",
        "prerequisites": ["mlops-data-ingestion"],
        "content": """# ML Training Best Practices

------------------------------------------------------------

## Vad ar ML Training Best Practices?

Best practices for ML-traning sakertstaller reproducerbarhet, skalbarhet och produktionskvalitet for dina modeller.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Reproducerbarhet | Samma resultat varje gang |
| Skalbarhet | Effektiv traning pa stora dataset |
| Kvalitet | Validering och testning |
| Automation | Automatiserade pipelines |

------------------------------------------------------------

## Snabbreferens

| Begrepp | Beskrivning |
|---------|-------------|
| Seed | Satt for reproducerbarhet |
| Cross-validation | K-fold for robust evaluering |
| Early stopping | Undvik overfitting |
| Checkpointing | Spara progress |

------------------------------------------------------------

## Reproducibility

### Seed Everything

```python
import random
import numpy as np
import torch

def set_seed(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
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

seed: 42
experiment_name: fraud_detection

training:
  test_size: 0.2
  cv_folds: 5
  early_stopping_rounds: 10
```

```python
import hydra
from omegaconf import DictConfig

@hydra.main(config_path="config", config_name="config")
def train(cfg: DictConfig):
    set_seed(cfg.seed)
    X_train, X_test, y_train, y_test = load_data(test_size=cfg.training.test_size)

    if cfg.model.name == "random_forest":
        model = RandomForestClassifier(**cfg.model.params)

    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    train()
```

------------------------------------------------------------

## Training Pipeline Structure

```python
from dataclasses import dataclass
from typing import Tuple, Dict, Any
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score

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

    def prepare_data(self, df: pd.DataFrame, target_col: str):
        X = df.drop(columns=[target_col])
        y = df[target_col]
        return train_test_split(
            X, y, test_size=self.config.test_size,
            random_state=self.config.seed, stratify=y
        )

    def train(self, X_train, y_train):
        self.model = self._create_model()
        cv_scores = cross_val_score(
            self.model, X_train, y_train,
            cv=self.config.cv_folds, scoring='f1_weighted'
        )
        self.metrics['cv_mean'] = cv_scores.mean()
        self.metrics['cv_std'] = cv_scores.std()
        self.model.fit(X_train, y_train)
        return self.model

    def evaluate(self, X_test, y_test):
        from sklearn.metrics import classification_report
        y_pred = self.model.predict(X_test)
        report = classification_report(y_test, y_pred, output_dict=True)
        self.metrics['accuracy'] = report['accuracy']
        self.metrics['f1_weighted'] = report['weighted avg']['f1-score']
        return self.metrics
```

------------------------------------------------------------

## Data Validation Before Training

```python
def validate_training_data(df: pd.DataFrame) -> bool:
    required_cols = ['user_id', 'amount', 'is_fraud']
    missing = set(required_cols) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    null_counts = df.isnull().sum()
    if null_counts.any():
        print(f"Warning: Null values found")

    class_dist = df['is_fraud'].value_counts(normalize=True)
    if class_dist.min() < 0.01:
        print(f"Warning: Severe class imbalance")

    return True
```

------------------------------------------------------------

## GPU Training with PyTorch

```python
import torch
from torch.utils.data import DataLoader
from torch.cuda.amp import autocast, GradScaler

class PyTorchTrainer:
    def __init__(self, model, config):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = model.to(self.device)
        self.config = config
        self.scaler = GradScaler()

    def train_epoch(self, train_loader, optimizer, criterion):
        self.model.train()
        total_loss = 0
        for data, target in train_loader:
            data, target = data.to(self.device), target.to(self.device)
            optimizer.zero_grad()
            with autocast():
                output = self.model(data)
                loss = criterion(output, target)
            self.scaler.scale(loss).backward()
            self.scaler.step(optimizer)
            self.scaler.update()
            total_loss += loss.item()
        return total_loss / len(train_loader)
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Ej reproducerbart | Saknar seed | Satt seed for alla libraries |
| Overfitting | For komplex modell | Anvand early stopping |
| Slow training | Ej GPU | Aktivera CUDA och mixed precision |
| Data leakage | Fel split | Anvand temporal split |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| Seeds | Satt for reproducerbarhet |
| Config | Anvand Hydra eller liknande |
| Validation | Validera data fore traning |
| Checkpointing | Spara modeller regelbundet |

### Kom ihag
- Satt seeds for reproducerbarhet
- Anvand configuration management
- Validera data fore traning
- Implementera early stopping
"""
    },

    # Node 10: Experiment Tracking
    {
        "id": "mlops-experiment-tracking",
        "slug": "experiment-tracking",
        "title": "Experiment Tracking",
        "order_index": 10,
        "estimated_minutes": 35,
        "xp_reward": 100,
        "difficulty": "medium",
        "node_type": "practice",
        "prerequisites": ["mlops-training"],
        "content": """# Experiment Tracking

------------------------------------------------------------

## Vad ar Experiment Tracking?

Experiment tracking ar att systematiskt logga och organisera ML-experiment for att kunna jamfora, reproducera och analysera resultat.

```
Utan tracking:
  Vilken modell presterade bast?
  Vilka hyperparameters anvande jag?
  Vilken data version?
  -> Ingen aning! Kor om allt...

Med tracking:
  experiment_id: exp_2024_01_15_v3
  params: {lr: 0.001, layers: 3}
  metrics: {accuracy: 0.95}
  artifacts: model.pkl, plots/
  -> Full reproducibility!
```

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Reproducerbarhet | Aterskapa exakt samma resultat |
| Jamforelse | Jamfor modeller systematiskt |
| Samarbete | Dela experiment med teamet |
| Governance | Dokumentation for compliance |

------------------------------------------------------------

## Snabbreferens

| Verktyg | Beskrivning |
|---------|-------------|
| MLflow | Open source, populart |
| Weights and Biases | Cloud-first, rich UI |
| Neptune | Enterprise features |
| Comet ML | Collaborative features |

------------------------------------------------------------

## MLflow

### Setup

```bash
pip install mlflow

mlflow server \\
    --backend-store-uri postgresql://user:pass@localhost/mlflow \\
    --default-artifact-root s3://bucket/mlflow-artifacts \\
    --host 0.0.0.0 --port 5000
```

### Basic Tracking

```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("fraud_detection")

with mlflow.start_run(run_name="random_forest_v1"):
    mlflow.log_params({
        "n_estimators": 100,
        "max_depth": 10,
        "min_samples_split": 5,
    })

    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    mlflow.log_metrics({
        "accuracy": accuracy,
        "f1_score": f1,
        "precision": precision,
        "recall": recall,
    })

    mlflow.sklearn.log_model(
        model, "model",
        signature=mlflow.models.infer_signature(X_train, y_train)
    )

    mlflow.log_artifact("confusion_matrix.png")
```

### Autologging

```python
mlflow.sklearn.autolog()
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)  # Allt loggas automatiskt!

mlflow.pytorch.autolog()
mlflow.tensorflow.autolog()
mlflow.xgboost.autolog()
```

------------------------------------------------------------

## Weights and Biases

### Setup

```python
import wandb

wandb.login()

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
for epoch in range(epochs):
    train_loss = train_epoch(model, train_loader)
    val_loss = validate(model, val_loader)

    wandb.log({
        "epoch": epoch,
        "train_loss": train_loss,
        "val_loss": val_loss,
    })

wandb.log({
    "confusion_matrix": wandb.plot.confusion_matrix(
        y_true=y_test, preds=y_pred, class_names=["legitimate", "fraud"]
    )
})

artifact = wandb.Artifact("fraud_model", type="model")
artifact.add_file("model.pkl")
run.log_artifact(artifact)
```

------------------------------------------------------------

## Comparison och Analysis

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()

experiment = client.get_experiment_by_name("fraud_detection")
runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    filter_string="metrics.f1_score > 0.9",
    order_by=["metrics.f1_score DESC"],
    max_results=10
)

for run in runs:
    print(f"Run: {run.info.run_id}")
    print(f"  F1: {run.data.metrics['f1_score']:.4f}")
    print(f"  Params: {run.data.params}")

best_run = runs[0]
mlflow.register_model(
    f"runs:/{best_run.info.run_id}/model",
    "fraud_detector"
)
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Saknar context | Ej loggat params | Logga alla hyperparameters |
| Kan inte reproducera | Saknar data version | Logga data hash |
| Svart att jamfora | Inkonsistent namngivning | Standardisera metrics |
| Fullt storage | For manga artifacts | Implementera retention policy |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| Tag runs | Med metadata och git commit |
| Log data hash | For reproducerbarhet |
| Nested runs | For hyperparameter tuning |
| Artifacts | Spara plots och feature importance |

### Kom ihag
- Logga allt: params, metrics, artifacts
- Tagga med git commit
- Anvand autolog nar mojligt
- Jamfor experiment systematiskt
"""
    },

    # Node 11: Model Registry
    {
        "id": "mlops-model-registry",
        "slug": "model-registry",
        "title": "Model Registry",
        "order_index": 11,
        "estimated_minutes": 30,
        "xp_reward": 100,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["mlops-experiment-tracking"],
        "content": """# Model Registry

------------------------------------------------------------

## Vad ar en Model Registry?

En model registry ar en centraliserad plats for att lagra, versionera och hantera ML-modeller genom deras livscykel.

```
+-----------------------------------------------------------------+
|                      Model Registry                              |
|                                                                  |
|  +--------------------------------------------------------+     |
|  |  fraud_detector                                         |     |
|  |  +-- Version 1 (Staging)    - RF, acc=0.92             |     |
|  |  +-- Version 2 (Production) - XGBoost, acc=0.95       |     |
|  |  +-- Version 3 (None)       - Neural Net, acc=0.94    |     |
|  |  +-- Version 4 (Staging)    - Ensemble, acc=0.97       |     |
|  +--------------------------------------------------------+     |
|                                                                  |
|  Stages: None -> Staging -> Production -> Archived              |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Versioning | Hantera modellversioner |
| Stage management | Kontrollera deployment stages |
| Governance | Godkannande och audit trail |
| Rollback | Snabb aterstallning |

------------------------------------------------------------

## Snabbreferens

| Stage | Beskrivning |
|-------|-------------|
| None | Nyregistrerad modell |
| Staging | Under testning |
| Production | Live i produktion |
| Archived | Utgatt version |

------------------------------------------------------------

## MLflow Model Registry

### Registrera Modell

```python
import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()

result = mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name="fraud_detector"
)

print(f"Registered version: {result.version}")

client.update_model_version(
    name="fraud_detector",
    version=result.version,
    description="XGBoost model trained on 2024-01 data. F1=0.95"
)

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

# Efter validering -> Production
client.transition_model_version_stage(
    name="fraud_detector",
    version=4,
    stage="Production",
    archive_existing_versions=True
)

# Rollback
client.transition_model_version_stage(
    name="fraud_detector",
    version=2,
    stage="Production"
)
```

### Ladda Modell fran Registry

```python
import mlflow

model = mlflow.pyfunc.load_model("models:/fraud_detector/Production")
model_v2 = mlflow.pyfunc.load_model("models:/fraud_detector/2")

predictions = model.predict(X_new)
```

------------------------------------------------------------

## Model Governance

```python
from dataclasses import dataclass
from typing import Dict

@dataclass
class ModelCard:
    name: str
    version: str
    description: str
    training_data: str
    training_date: str
    metrics: Dict[str, float]
    known_limitations: list
    bias_analysis: str

card = ModelCard(
    name="fraud_detector",
    version="2.0.0",
    description="XGBoost-based fraud detection model",
    training_data="transactions_2023_01_to_2024_01",
    training_date="2024-01-15",
    metrics={"accuracy": 0.95, "f1": 0.92, "auc": 0.98},
    known_limitations=["Lower accuracy on transactions > $10,000"],
    bias_analysis="Model tested for demographic parity"
)
```

------------------------------------------------------------

## Model Versioning Strategy

```
fraud_detector-v{MAJOR}.{MINOR}.{PATCH}

MAJOR: Breaking changes
  - New input/output schema
  - Different model architecture

MINOR: Improvements
  - Hyperparameter tuning
  - New training data

PATCH: Fixes
  - Bug fixes
  - Minor retraining
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Fel modell i prod | Ingen stage management | Anvand staging stages |
| Kan inte rollback | Saknar versioner | Versionera alla modeller |
| Saknar metadata | Ej dokumenterat | Skapa model cards |
| Godkannande saknas | Ingen governance | Implementera approval workflow |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| Stages | None -> Staging -> Production -> Archived |
| Versioning | Semantic versioning for modeller |
| Governance | Model cards och approval workflows |
| Rollback | Ha alltid en backup-version |

### Kom ihag
- Registrera alla produktionsmodeller
- Anvand stages for kontrollerad deployment
- Dokumentera med model cards
- Planera for rollback
"""
    },

    # Node 12: Hyperparameter Tuning
    {
        "id": "mlops-hyperparameter-tuning",
        "slug": "hyperparameter-tuning",
        "title": "Hyperparameter Tuning",
        "order_index": 12,
        "estimated_minutes": 35,
        "xp_reward": 100,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["mlops-model-registry"],
        "content": """# Hyperparameter Tuning

------------------------------------------------------------

## Vad ar Hyperparameter Tuning?

Hyperparameter tuning ar processen att hitta de optimala hyperparametrarna for en ML-modell for att maximera prestanda.

```
+-----------------------------------------------------------------+
|                    Hyperparameter Search                         |
|                                                                  |
|  Grid Search          Random Search         Bayesian Opt        |
|  +---------+          +---------+          +---------+          |
|  | # # # # |          |   #     |          |       # |          |
|  | # # # # |          | #   #   |          |   #     |          |
|  | # # # # |          |     # # |          | #   #   |          |
|  | # # # # |          | #       |          | # # # # | <- Focus |
|  +---------+          +---------+          +---------+           |
|  Exhaustive           Random samples       Smart sampling       |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Prestanda | Optimera modellprestanda |
| Automation | Automatisera sokning |
| Reproducerbarhet | Dokumentera basta params |
| Effektivitet | Spara tid med smart sokning |

------------------------------------------------------------

## Snabbreferens

| Metod | Beskrivning |
|-------|-------------|
| Grid Search | Exhaustive, O(n^d) |
| Random Search | Sampling, ofta battre |
| Bayesian | Smart, fokuserar pa lovande |
| Pruning | Avbryt daliga trials tidigt |

------------------------------------------------------------

## Optuna

### Basic Usage

```python
import optuna
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

def objective(trial):
    params = {
        "n_estimators": trial.suggest_int("n_estimators", 50, 500),
        "max_depth": trial.suggest_int("max_depth", 3, 20),
        "min_samples_split": trial.suggest_int("min_samples_split", 2, 20),
        "max_features": trial.suggest_categorical("max_features", ["sqrt", "log2", None]),
    }

    model = RandomForestClassifier(**params, random_state=42, n_jobs=-1)
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring="f1")
    return scores.mean()

study = optuna.create_study(
    study_name="fraud_detection_rf",
    direction="maximize",
    storage="sqlite:///optuna.db",
)

study.optimize(objective, n_trials=100, timeout=3600, n_jobs=4)

print(f"Best trial: {study.best_trial.value}")
print(f"Best params: {study.best_trial.params}")
```

### Advanced Pruning

```python
import optuna
from optuna.pruners import MedianPruner
from optuna.samplers import TPESampler

def objective_with_pruning(trial):
    n_layers = trial.suggest_int("n_layers", 1, 4)
    hidden_size = trial.suggest_int("hidden_size", 32, 256)
    lr = trial.suggest_float("lr", 1e-5, 1e-1, log=True)
    dropout = trial.suggest_float("dropout", 0.1, 0.5)

    model = build_model(n_layers, hidden_size, dropout)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(100):
        train_loss = train_epoch(model, train_loader, optimizer)
        val_loss = validate(model, val_loader)
        trial.report(val_loss, epoch)
        if trial.should_prune():
            raise optuna.TrialPruned()

    return val_loss

study = optuna.create_study(
    direction="minimize",
    sampler=TPESampler(seed=42),
    pruner=MedianPruner(n_startup_trials=10, n_warmup_steps=20),
)
study.optimize(objective_with_pruning, n_trials=100)
```

------------------------------------------------------------

## Ray Tune (Distributed)

```python
from ray import tune
from ray.tune.schedulers import ASHAScheduler

def train_model(config):
    model = XGBClassifier(
        n_estimators=config["n_estimators"],
        max_depth=config["max_depth"],
        learning_rate=config["learning_rate"],
    )

    for epoch in range(config["epochs"]):
        model.fit(X_train, y_train)
        val_score = model.score(X_val, y_val)
        tune.report(val_accuracy=val_score, epoch=epoch)

search_space = {
    "n_estimators": tune.randint(50, 500),
    "max_depth": tune.randint(3, 15),
    "learning_rate": tune.loguniform(1e-4, 1e-1),
    "epochs": 50,
}

scheduler = ASHAScheduler(
    metric="val_accuracy", mode="max",
    max_t=50, grace_period=10, reduction_factor=2,
)

analysis = tune.run(
    train_model,
    config=search_space,
    num_samples=100,
    scheduler=scheduler,
    resources_per_trial={"cpu": 2, "gpu": 0.5},
)

best_config = analysis.get_best_config(metric="val_accuracy", mode="max")
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Overfitting | For manga trials | Anvand holdout set |
| Lang tid | Grid search | Byt till Bayesian |
| Suboptimal | For fa trials | Oka antal trials |
| Ej reproducerbart | Saknar seed | Satt seed |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| Random > Grid | Random ar ofta battre |
| Bayesian | For dyra modeller |
| Pruning | Spara tid med early stopping |
| Logging | Logga alla trials till MLflow |

### Kom ihag
- Borja med Random Search
- Anvand log scale for learning rates
- Implementera early stopping/pruning
- Logga allt till experiment tracker
"""
    },
]
