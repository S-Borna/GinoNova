"""
MLOps SkillsMap - Block 4: MLOps Infrastructure
Nodes 13-16: CI/CD for ML, Orchestration, Containerization, Infrastructure as Code
"""

BLOCK_4_NODES = [
    # Node 13: CI/CD for ML
    {
        "id": "mlops-cicd",
        "slug": "cicd-for-ml",
        "title": "CI/CD for ML Pipelines",
        "order_index": 13,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["mlops-hyperparameter-tuning"],
        "content": '''# CI/CD for ML Pipelines

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor CI/CD for ML ar viktigt |
|----------|-------------------------------|
| **Reproducerbarhet** | Saker pa att modeller kan aterskapas |
| **Kvalitetskontroll** | Automatiserade tester for modellprestanda |
| **Snabbare iteration** | Kortare tid fran experiment till produktion |
| **Teamsamarbete** | Standardiserade processer for ML-team |

Du maste forsta:

- **ML-specifika pipelines** - skiljer sig fran traditionell CI/CD
- **Data- och modellvalidering** - kvalitetsportar for ML
- **Experiment tracking** - spara och jamfor modeller

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
          python train.py \\
            --config configs/production.yaml \\
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
          python evaluate.py \\
            --model-path model/ \\
            --test-data data/test.csv

      - name: Model quality gate
        run: |
          python scripts/quality_gate.py \\
            --min-accuracy 0.90 \\
            --max-latency-ms 50 \\
            --metrics-file outputs/metrics.json

      - name: Generate model report
        run: |
          python scripts/generate_report.py \\
            --metrics outputs/metrics.json \\
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
          python scripts/register_model.py \\
            --model-path model/ \\
            --model-name fraud-detector \\
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
          python scripts/download_model.py \\
            --model-name fraud-detector \\
            --version ${{ github.event.inputs.model_version }} \\
            --output model/

      - name: Build inference container
        run: |
          docker build -t fraud-detector:${{ github.event.inputs.model_version }} \\
            -f Dockerfile.inference .

      - name: Push to ECR
        run: |
          aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REGISTRY
          docker push $ECR_REGISTRY/fraud-detector:${{ github.event.inputs.model_version }}

      - name: Deploy to SageMaker
        run: |
          python scripts/deploy_sagemaker.py \\
            --model-name fraud-detector \\
            --image $ECR_REGISTRY/fraud-detector:${{ github.event.inputs.model_version }} \\
            --environment ${{ github.event.inputs.environment }}

      - name: Smoke test
        run: |
          python scripts/smoke_test.py \\
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
    """Tests för modell-träning"""

    def test_model_trains_without_errors(self, sample_data, model_config):
        """Model should complete training"""
        model = train_model(sample_data, model_config)
        assert model is not None

    def test_model_accuracy_above_threshold(self, trained_model, test_data):
        """Model should meet minimum accuracy"""
        accuracy = trained_model.score(test_data.X, test_data.y)
        assert accuracy > 0.85

    def test_model_prediction_shape(self, trained_model, test_data):
        """Predictions should have correct shape"""
        predictions = trained_model.predict(test_data.X)
        assert len(predictions) == len(test_data.y)

    def test_model_handles_edge_cases(self, trained_model):
        """Model should handle edge cases gracefully"""
        edge_cases = pd.DataFrame({
            'amount': [0, 1e10, -1],
            'merchant': ['unknown', '', None],
        })
        # Should not raise
        predictions = trained_model.predict(edge_cases)
        assert all(p in [0, 1] for p in predictions)


class TestModelIntegrity:
    """Tests för modell-integritet"""

    def test_model_reproducibility(self, sample_data, model_config):
        """Same inputs should give same outputs"""
        model1 = train_model(sample_data, model_config)
        model2 = train_model(sample_data, model_config)

        preds1 = model1.predict(sample_data.X[:100])
        preds2 = model2.predict(sample_data.X[:100])

        assert np.array_equal(preds1, preds2)

    def test_model_feature_importance_stable(self, trained_model):
        """Top features should be consistent"""
        importance = trained_model.feature_importances_
        top_features = np.argsort(importance)[-5:]

        # Verify known important features are present
        assert 'amount' in top_features
        assert 'merchant_risk_score' in top_features
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **CI/CD for ML** | Automatiserade pipelines for modelltraning och deploy |
| **Quality Gate** | Automatisk validering av modellprestanda |
| **DVC** | Data Version Control - versionshantering for data |
| **CML** | Continuous Machine Learning - rapporter i PR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Model training timeout | For lang traningstid | Oka runner timeout eller optimera |
| Data validation failed | Schema andrat | Uppdatera schema eller fixa data |
| Model accuracy drop | Datadrift eller bugg | Analysera data och modell |
| Deploy failed | Container/endpoint fel | Kolla loggar och resurser |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **ML CI/CD** | Hanterar kod, data OCH modeller |
| **Quality gates** | Stoppa daliga modeller automatiskt |
| **DVC** | Versionshantera stora datafiler |
| **Testing** | Unit, integration och modelltester |

**Kom ihag:**

- ML-pipelines har fler triggers an vanlig CI/CD
- Data- och modellvalidering ar kritiskt
- Automatisera sa mycket som mojligt
- Ha alltid rollback-mojlighet
'''
    },

    # Node 14: ML Orchestration
    {
        "id": "mlops-orchestration",
        "slug": "ml-orchestration",
        "title": "ML Pipeline Orchestration",
        "order_index": 14,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["mlops-cicd"],
        "content": '''# ML Pipeline Orchestration

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor orkestration ar viktigt |
|----------|-------------------------------|
| **Komplexa pipelines** | Hantera beroenden mellan steg |
| **Schemalagd traning** | Automatisk omtraning |
| **Felhantering** | Retry och alerting |
| **Skalbarhet** | Parallell exekvering |

Du maste forsta:

- **DAGs** - Directed Acyclic Graphs for arbetsfloden
- **Schedulering** - nar och hur pipelines kors
- **Monitoring** - overvakning av pipeline-halsa

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
    """Extract training data from data warehouse"""
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
    """Validate data quality"""
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
    """Train model with MLflow tracking"""
    import mlflow
    from training import Trainer

    data_path = context['ti'].xcom_pull(task_ids='validate_data')

    with mlflow.start_run(run_name=f"training_{context['ds']}"):
        trainer = Trainer(config='configs/production.yaml')
        model_uri = trainer.train(data_path)

        mlflow.log_param("data_date", context['ds'])

    return model_uri

def evaluate_model(**context):
    """Evaluate model performance"""
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
    """Register model if it passes evaluation"""
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
    """Extract data with caching"""
    from data_pipeline import DataExtractor

    extractor = DataExtractor()
    df = extractor.get_training_data(date=date)

    output_path = f"data/training_{date}.parquet"
    df.to_parquet(output_path)

    return output_path

@task(retries=2)
def validate_data(data_path: str) -> str:
    """Validate data quality"""
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
    """Train model"""
    import mlflow

    print(f"Training with config: {config}")

    with mlflow.start_run():
        # Training logic...
        model_uri = "runs:/abc123/model"

    return model_uri

@task
def deploy_model(model_uri: str, environment: str):
    """Deploy model to environment"""
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
    """Main training flow"""

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Verktyg | Anvandning |
|---------|------------|
| **Airflow** | General-purpose orkestration |
| **Prefect** | Modern Python-first orkestrator |
| **Kubeflow** | ML-pipelines pa Kubernetes |
| **Dagster** | Data-aware orkestration |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Task timeout | For lang exekvering | Oka timeout eller optimera |
| Dependency failed | Upstream task misslyckades | Kolla upstream loggar |
| Resource exhaustion | For manga parallella tasks | Begranser concurrency |
| Scheduler lag | For manga DAGs | Optimera scheduler config |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **DAG** | Definiera beroenden mellan tasks |
| **Idempotens** | Tasks ska kunna koras om sakert |
| **Monitoring** | Overvaka pipeline-halsa |
| **Parametrisering** | Gor pipelines konfigurerbara |

**Kom ihag:**

- Valj orkestrator baserat pa teamets behov
- Borja enkelt, skala upp vid behov
- Testa tasks individuellt
- Ha bra felhantering och alerting
'''
    },

    # Node 15: Model Serving
    {
        "id": "mlops-serving",
        "slug": "model-serving",
        "title": "Model Serving och Inference",
        "order_index": 15,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["mlops-orchestration"],
        "content": '''# Model Serving och Inference

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor model serving ar viktigt |
|----------|--------------------------------|
| **Produktion** | Gor modeller tillgangliga for applikationer |
| **Skalbarhet** | Hantera hog last och manga requests |
| **Latency** | Saker pa snabba svarstider |
| **Reliability** | Modeller maste alltid vara tillgangliga |

Du maste forsta:

- **Serving patterns** - online, batch, streaming
- **API design** - REST/gRPC for modeller
- **Skalning** - hantera varierande last

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
docker run -p 8501:8501 \\
    -v /path/to/model:/models/fraud_detector \\
    -e MODEL_NAME=fraud_detector \\
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
"""
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
"""

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
curl -X POST \\
    -H "Content-Type: application/json" \\
    -d '{"instances": [{"amount": 100.0}]}' \\
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Verktyg | Anvandning |
|---------|------------|
| **FastAPI** | Snabb Python API-server |
| **Triton** | NVIDIA:s inference server |
| **SageMaker** | AWS managed ML-platform |
| **KServe** | Kubernetes ML serving |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| High latency | Modell for stor/langsam | Optimera eller byt modell |
| OOM errors | For lite minne | Oka resurser eller batcha |
| Cold start | Modell ej laddad | Warmup requests |
| Version mismatch | Fel modellversion | Kontrollera deployment |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Online vs Batch** | Valj baserat pa latency-krav |
| **Skalning** | Autoscaling baserat pa last |
| **A/B testing** | Jamfor modellversioner i produktion |
| **Monitoring** | Overvaka latency och errors |

**Kom ihag:**

- Ha alltid health checks
- Overvaka inference latency
- Implementera graceful degradation
- Testa med realistisk last
'''
    },

    # Node 16: Containerization for ML
    {
        "id": "mlops-containers",
        "slug": "ml-containerization",
        "title": "ML Containerization",
        "order_index": 16,
        "estimated_minutes": 35,
        "xp_reward": 100,
        "difficulty": "medium",
        "node_type": "practice",
        "prerequisites": ["mlops-serving"],
        "content": '''# ML Containerization

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor containerization ar viktigt |
|----------|-----------------------------------|
| **Reproducerbarhet** | Samma miljo overallt |
| **Portabilitet** | Kor pa vilken plattform som helst |
| **Isolation** | Separera dependencies |
| **Skalning** | Enkel horisontell skalning |

Du maste forsta:

- **ML-specifika images** - GPU-stod, stora modeller
- **Multi-stage builds** - separera training och inference
- **Optimering** - minimera image-storlek

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Training Container

```dockerfile
# Dockerfile.train
FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \\
    build-essential \\
    git \\
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
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \\
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
RUN apt-get update && apt-get install -y \\
    python3.11 \\
    python3-pip \\
    && rm -rf /var/lib/apt/lists/*

# PyTorch with CUDA
RUN pip install --no-cache-dir \\
    torch==2.1.0+cu121 \\
    torchvision==0.16.0+cu121 \\
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Multi-stage build** | Separera build och runtime |
| **Distroless** | Minimal base image utan shell |
| **GPU images** | CUDA-baserade images for ML |
| **HPA** | Horizontal Pod Autoscaler |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Image too large | For manga lager/dependencies | Multi-stage build |
| CUDA mismatch | Fel CUDA-version | Matcha host GPU drivers |
| OOMKilled | For lite minne | Oka memory limits |
| Slow startup | Stor modell att ladda | Warmup eller preload |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Slim images** | Minska storlek och attack surface |
| **Multi-stage** | Separera build fran runtime |
| **Health checks** | Nodvandigt for orchestration |
| **Resource limits** | Forutsagbart beteende |

**Kom ihag:**

- Pinning av versioner ar kritiskt for reproducerbarhet
- Kor aldrig som root i produktion
- Testa images lokalt innan deploy
- Overvaka resource-anvandning
'''
    },
]
