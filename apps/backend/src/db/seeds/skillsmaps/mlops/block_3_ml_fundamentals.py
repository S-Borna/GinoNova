"""
MLOps SkillsMap - Block 3: ML Fundamentals
Nodes 9-12: Training, Experiment Tracking, Model Registry, Hyperparameter Tuning
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
        "content": '''# ML Training Best Practices

## Reproducibility

### Seed Everything
```python
import random
import numpy as np
import torch

def set_seed(seed: int = 42):
    """Set seed for reproducibility"""
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
        """Split data with stratification"""
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
        """Train model with cross-validation"""
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
        """Evaluate model on test set"""
        y_pred = self.model.predict(X_test)

        report = classification_report(y_test, y_pred, output_dict=True)
        self.metrics['accuracy'] = report['accuracy']
        self.metrics['f1_weighted'] = report['weighted avg']['f1-score']
        self.metrics['precision'] = report['weighted avg']['precision']
        self.metrics['recall'] = report['weighted avg']['recall']

        return self.metrics

    def _create_model(self):
        """Factory for creating models"""
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
    """Validate data before training"""

    # Check for required columns
    required_cols = ['user_id', 'amount', 'is_fraud']
    missing = set(required_cols) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # Check for nulls
    null_counts = df.isnull().sum()
    if null_counts.any():
        print(f"Warning: Null values found:\\n{null_counts[null_counts > 0]}")

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
    """Check for distribution shift between train/test"""
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
'''
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
        "content": '''# Experiment Tracking

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
mlflow server \\
    --backend-store-uri postgresql://user:pass@localhost/mlflow \\
    --default-artifact-root s3://bucket/mlflow-artifacts \\
    --host 0.0.0.0 \\
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
'''
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
        "content": '''# Model Registry

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
    """Request model promotion with approval workflow"""

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
    """Documentation for deployed models"""
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
'''
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
        "content": '''# Hyperparameter Tuning

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
    """Optuna objective function"""

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
    """Neural network training with early pruning"""

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
    """Training function for Ray Tune"""

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
    """Model builder for Keras Tuner"""
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
'''
    },
]
