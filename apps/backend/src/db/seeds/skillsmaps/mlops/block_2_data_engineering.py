"""
MLOps SkillsMap - Block 2: Data Engineering
Nodes 5-8: Pipelines, Feature Stores, Data Lakes, Ingestion
V3 Format - Swedish, No Emojis
"""

BLOCK_2_NODES = [
    # Node 5: Data Pipelines
    {
        "id": "mlops-data-pipelines",
        "slug": "data-pipelines",
        "title": "Data Pipelines for ML",
        "order_index": 5,
        "estimated_minutes": 40,
        "xp_reward": 100,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["mlops-cloud"],
        "content": """# Data Pipelines for ML

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Data Pipelines?

Data pipelines ar automatiserade arbetsfloden som extraherar, transformerar och laddar data for ML-traning och inferens.

```
┌─────────────────────────────────────────────────────────────────┐
│                      ML Data Pipeline                            │
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐     │
│  │ Sources  │ -> │ Ingest   │ -> │Transform │ -> │ Feature  │     │
│  │          │   │          │   │          │   │ Store    │     │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘     │
│       │              │              │              │            │
│   Databases      Kafka/         Spark/          Online/        │
│   APIs           Airflow        dbt             Offline        │
│   Files                                                         │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Automation | Automatiserar datafloden fran kalla till modell |
| Reproducerbarhet | Samma data ger samma resultat |
| Skalbarhet | Hanterar stora datavolymer |
| Kvalitet | Inbyggd datavalidering |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Verktyg | Anvandning |
|---------|------------|
| Apache Airflow | Workflow orchestration |
| Prefect | Modern Python orchestration |
| Apache Spark | Storskalig dataprocessning |
| dbt | SQL-baserad transformation |
| Kafka | Streaming data |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Apache Airflow

### ML Training DAG

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'mlops',
    'depends_on_past': False,
    'email_on_failure': True,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

def extract_data(**context):
    import pandas as pd
    from sqlalchemy import create_engine
    engine = create_engine('postgresql://...')
    df = pd.read_sql('SELECT * FROM transactions WHERE date > %s', engine,
                     params=[context['ds']])
    output_path = f"/data/raw/{context['ds']}/transactions.parquet"
    df.to_parquet(output_path)
    return output_path

def validate_data(**context):
    import great_expectations as gx
    ti = context['ti']
    data_path = ti.xcom_pull(task_ids='extract')
    context_gx = gx.get_context()
    checkpoint = context_gx.get_checkpoint("data_quality_checkpoint")
    result = checkpoint.run(batch_request={"path": data_path})
    if not result.success:
        raise ValueError("Data validation failed!")
    return data_path

def train_model(**context):
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

with DAG(
    'ml_training_pipeline',
    default_args=default_args,
    schedule_interval='0 2 * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    extract = PythonOperator(task_id='extract', python_callable=extract_data)
    validate = PythonOperator(task_id='validate', python_callable=validate_data)
    train = PythonOperator(task_id='train', python_callable=train_model)
    extract >> validate >> train
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Prefect (Modern Alternative)

```python
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def extract_data(date: str) -> str:
    import pandas as pd
    # extraction logic
    return output_path

@task(retries=3, retry_delay_seconds=60)
def validate_data(data_path: str) -> str:
    # validation logic
    return data_path

@task
def train_model(features_path: str) -> str:
    # training logic
    return model_path

@flow(name="ML Training Pipeline")
def ml_pipeline(date: str):
    data_path = extract_data(date)
    validated_path = validate_data(data_path)
    model_path = train_model(validated_path)
    return model_path

if __name__ == "__main__":
    ml_pipeline(date="2024-01-15")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Apache Spark for Stora Dataset

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml import Pipeline

spark = SparkSession.builder \\
    .appName("MLPipeline") \\
    .config("spark.sql.adaptive.enabled", "true") \\
    .getOrCreate()

df = spark.read.parquet("s3://bucket/data/")

assembler = VectorAssembler(
    inputCols=["amount", "hour", "day_of_week", "user_age"],
    outputCol="features"
)

scaler = StandardScaler(inputCol="features", outputCol="scaled_features")

rf = RandomForestClassifier(
    featuresCol="scaled_features",
    labelCol="is_fraud",
    numTrees=100
)

pipeline = Pipeline(stages=[assembler, scaler, rf])
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)
model = pipeline.fit(train_df)
model.write().overwrite().save("s3://bucket/models/fraud_detector")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Pipeline failar | Data schema andrad | Lagg till schema validation |
| Timeout | For stor data | Partitionera och parallellisera |
| Memory overflow | Ineffektiv kod | Anvand chunking eller Spark |
| Inkonsistent data | Saknar validering | Implementera Great Expectations |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| Idempotency | Pipelines ska kunna koras om utan problem |
| Monitoring | Logga execution time, data volumes, errors |
| Testing | Unit tests for transformations |
| Documentation | Beskriv data lineage |

### Kom ihag
- Bygg pipelines som ar idempotenta
- Validera data i varje steg
- Anvand caching for effektivitet
- Dokumentera datafloden
"""
    },

    # Node 6: Feature Stores
    {
        "id": "mlops-feature-stores",
        "slug": "feature-stores",
        "title": "Feature Stores",
        "order_index": 6,
        "estimated_minutes": 35,
        "xp_reward": 100,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["mlops-data-pipelines"],
        "content": """# Feature Stores

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar en Feature Store?

En feature store ar en centraliserad plattform for att lagra, hantera och servera ML-features for bade traning och inferens.

```
┌─────────────────────────────────────────────────────────┐
│              ┌─────────────────┐                        │
│              │  Feature Store  │                        │
│              │  ┌───────────┐  │                        │
│              │  │ Offline   │  │ <- Training            │
│              │  │ Store     │  │                        │
│              │  └───────────┘  │                        │
│              │  ┌───────────┐  │                        │
│              │  │ Online    │  │ <- Serving (low latency)│
│              │  │ Store     │  │                        │
│              │  └───────────┘  │                        │
│              └─────────────────┘                        │
│                     │                                   │
│  Samma features for traning och serving!                │
└─────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Konsistens | Samma features for traning och serving |
| Ateranvandning | Dela features mellan team och modeller |
| Tidsbesparing | Undvik duplicerat feature engineering |
| Point-in-time | Korrekt historisk data for traning |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Verktyg | Beskrivning |
|---------|-------------|
| Feast | Open source feature store |
| Tecton | Enterprise feature store |
| Hopsworks | Full ML platform |
| AWS SageMaker FS | Managed AWS service |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Feast - Open Source Feature Store

### Setup

```bash
pip install feast
feast init fraud_detection
cd fraud_detection
```

### Feature Definitions

```python
from datetime import timedelta
from feast import Entity, Feature, FeatureView, FileSource, ValueType
from feast.types import Float32, Int64

user = Entity(
    name="user_id",
    value_type=ValueType.INT64,
    description="User identifier",
)

user_stats_source = FileSource(
    path="data/user_stats.parquet",
    timestamp_field="event_timestamp",
)

user_stats_fv = FeatureView(
    name="user_stats",
    entities=["user_id"],
    ttl=timedelta(days=1),
    features=[
        Feature(name="transaction_count_7d", dtype=Int64),
        Feature(name="avg_amount_7d", dtype=Float32),
        Feature(name="fraud_rate_7d", dtype=Float32),
    ],
    online=True,
    source=user_stats_source,
)
```

### Apply och Materialize

```bash
feast apply
feast materialize-incremental $(date +%Y-%m-%dT%H:%M:%S)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Training Data Retrieval

```python
from feast import FeatureStore
from datetime import datetime
import pandas as pd

store = FeatureStore(repo_path=".")

entity_df = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5],
    "event_timestamp": [datetime(2024, 1, 15)] * 5,
})

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "user_stats:transaction_count_7d",
        "user_stats:avg_amount_7d",
        "user_stats:fraud_rate_7d",
    ],
).to_df()

print(training_df)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Online Serving

```python
from feast import FeatureStore

store = FeatureStore(repo_path=".")

feature_vector = store.get_online_features(
    features=[
        "user_stats:transaction_count_7d",
        "user_stats:avg_amount_7d",
        "user_stats:fraud_rate_7d",
    ],
    entity_rows=[{"user_id": 12345}],
).to_dict()

print(feature_vector)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Feature Engineering Patterns

```python
def compute_time_window_features(
    df: pd.DataFrame,
    entity_col: str,
    value_col: str,
    windows: list[int] = [7, 14, 30]
) -> pd.DataFrame:
    df = df.sort_values([entity_col, 'timestamp'])
    for window in windows:
        rolling = df.groupby(entity_col)[value_col].rolling(f'{window}D')
        df[f'{value_col}_sum_{window}d'] = rolling.sum().values
        df[f'{value_col}_mean_{window}d'] = rolling.mean().values
        df[f'{value_col}_std_{window}d'] = rolling.std().values
    return df
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Training/serving skew | Olika feature berakning | Anvand feature store |
| Data leakage | Fel timestamp | Anvand point-in-time joins |
| Stale features | Ej uppdaterade | Implementera materialization schedule |
| Slow online serving | Komplex berakning | Forberakna och cacha |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| Konsistens | Samma features overallt |
| Point-in-time | Korrekt historisk data |
| Ateranvandning | Dela features mellan modeller |
| Dokumentation | Beskriv varje feature |

### Kom ihag
- Anvand feature store for konsistens
- Dokumentera alla features
- Overvaka feature freshness
- Implementera feature versioning
"""
    },

    # Node 7: Data Lakes & Warehouses
    {
        "id": "mlops-data-lakes",
        "slug": "data-lakes-warehouses",
        "title": "Data Lakes och Warehouses",
        "order_index": 7,
        "estimated_minutes": 30,
        "xp_reward": 75,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["mlops-feature-stores"],
        "content": """# Data Lakes och Warehouses for ML

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar skillnaden?

```
┌─────────────────────────────────────────────────────────────────┐
│                   DATA LAKE                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Schema-on-Read                                          │    │
│  │  JSON, CSV, Parquet, Images, Video                       │    │
│  │  Raw, unprocessed, any format                           │    │
│  │  Perfekt for ML exploration!                            │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                   DATA WAREHOUSE                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Schema-on-Write                                         │    │
│  │  Structured Tables with defined schemas                  │    │
│  │  Optimized for BI/Analytics queries                      │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                   LAKEHOUSE (Modern)                             │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Best of both worlds!                                    │    │
│  │  Delta Lake / Apache Iceberg / Apache Hudi               │    │
│  │  ACID transactions + Schema evolution + Time travel      │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Lagring | Centraliserad datalagring for ML |
| Versioning | Time travel for reproducerbarhet |
| Skalbarhet | Hanterar petabytes av data |
| Integration | Stodjer ML-verktyg och frameworks |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Verktyg | Beskrivning |
|---------|-------------|
| Delta Lake | Open source lakehouse |
| Apache Iceberg | Table format for data lakes |
| Apache Hudi | Streaming data lake |
| Databricks | Managed lakehouse platform |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Delta Lake

### Setup

```python
from delta import *
from pyspark.sql import SparkSession

spark = SparkSession.builder \\
    .appName("DeltaLakeML") \\
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \\
    .config("spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog") \\
    .getOrCreate()
```

### Write Data

```python
df.write.format("delta").mode("overwrite").save("/data/ml/features")

df.write.format("delta") \\
    .partitionBy("date", "region") \\
    .mode("overwrite") \\
    .save("/data/ml/features")
```

### Time Travel (Perfekt for ML Reproducibility)

```python
# Las specifik version
df_v0 = spark.read.format("delta").option("versionAsOf", 0).load("/data/ml/features")

# Las vid specifik tidpunkt
df_yesterday = spark.read.format("delta") \\
    .option("timestampAsOf", "2024-01-14") \\
    .load("/data/ml/features")

# Se historik
from delta.tables import DeltaTable
dt = DeltaTable.forPath(spark, "/data/ml/features")
history_df = dt.history()
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Medallion Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Medallion Architecture                        │
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐                     │
│  │  BRONZE  │ -> │  SILVER  │ -> │   GOLD   │                     │
│  │  (Raw)   │   │ (Clean)  │   │(Features)│                     │
│  └──────────┘   └──────────┘   └──────────┘                     │
│       │              │              │                            │
│   Raw JSON/      Cleaned,       Aggregated,                     │
│   CSV ingest     validated,     feature-ready,                  │
│   from sources   deduplicated   for ML training                 │
└─────────────────────────────────────────────────────────────────┘
```

```python
# Bronze: Raw ingestion
raw_df = spark.read.json("s3://bucket/raw/events/")
raw_df.write.format("delta").save("s3://bucket/bronze/events/")

# Silver: Cleaned and validated
silver_df = spark.read.format("delta").load("s3://bucket/bronze/events/")
silver_df = silver_df.dropDuplicates(["event_id"]).filter(col("user_id").isNotNull())
silver_df.write.format("delta").save("s3://bucket/silver/events/")

# Gold: ML-ready features
gold_df = spark.read.format("delta").load("s3://bucket/silver/events/")
features_df = gold_df.groupBy("user_id").agg(
    count("*").alias("event_count"),
    avg("amount").alias("avg_amount"),
)
features_df.write.format("delta").save("s3://bucket/gold/user_features/")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Slow queries | Ingen partitionering | Partitionera pa datum |
| Data inconsistency | Ingen ACID | Anvand Delta Lake |
| Kan inte reproducera | Ingen versioning | Anvand time travel |
| Schema drift | Schema evolution | Aktivera mergeSchema |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| Lakehouse | Best of both worlds |
| Time travel | For ML reproducerbarhet |
| Medallion | Bronze/Silver/Gold pattern |
| Partitionering | For prestanda |

### Kom ihag
- Anvand lakehouse for ML-data
- Partitionera pa datum
- Anvand time travel for reproducerbarhet
- Folj medallion architecture
"""
    },

    # Node 8: Data Ingestion
    {
        "id": "mlops-data-ingestion",
        "slug": "data-ingestion",
        "title": "Data Ingestion Architecture",
        "order_index": 8,
        "estimated_minutes": 30,
        "xp_reward": 75,
        "difficulty": "medium",
        "node_type": "practice",
        "prerequisites": ["mlops-data-lakes"],
        "content": """# Data Ingestion Architecture

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Data Ingestion?

Data ingestion ar processen att hamta data fran olika kallor och ladda den i ett centralt lager for bearbetning och analys.

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
│       v                              v                           │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              Data Lake / Feature Store                   │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Datakvalitet | Validering vid ingest |
| Skalbarhet | Hantera stora volymer |
| Latens | Batch vs streaming |
| Tillforlitlighet | Fault tolerance |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Verktyg | Anvandning |
|---------|------------|
| Apache Kafka | Streaming platform |
| Debezium | CDC (Change Data Capture) |
| Airbyte | Data integration |
| Spark Streaming | Storskalig streaming |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Apache Kafka for Streaming

### Producer

```python
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

def send_event(event: dict):
    producer.send(topic='ml-events', key=event.get('user_id'), value=event)
    producer.flush()

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
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
)

def process_events():
    batch = []
    batch_size = 1000
    for message in consumer:
        batch.append(message.value)
        if len(batch) >= batch_size:
            df = pd.DataFrame(batch)
            update_features(df)
            write_to_delta(df)
            batch = []
    consumer.commit()
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Spark Structured Streaming

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window

spark = SparkSession.builder.appName("StreamingML").getOrCreate()

schema = StructType() \\
    .add("user_id", StringType()) \\
    .add("amount", DoubleType()) \\
    .add("timestamp", TimestampType())

df = spark.readStream \\
    .format("kafka") \\
    .option("kafka.bootstrap.servers", "kafka:9092") \\
    .option("subscribe", "transactions") \\
    .load()

events = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

windowed_features = events \\
    .withWatermark("timestamp", "10 minutes") \\
    .groupBy(col("user_id"), window(col("timestamp"), "5 minutes")) \\
    .agg(
        count("*").alias("transaction_count_5m"),
        sum("amount").alias("total_amount_5m"),
    )

query = windowed_features.writeStream \\
    .format("delta") \\
    .outputMode("update") \\
    .option("checkpointLocation", "/checkpoints/features") \\
    .start("/data/streaming_features/")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Data Quality Checks

```python
import great_expectations as gx

def validate_ingested_data(df: pd.DataFrame) -> bool:
    context = gx.get_context()
    validator = context.get_validator(batch_request=batch_request)

    validator.expect_column_to_exist("user_id")
    validator.expect_column_values_to_not_be_null("user_id")
    validator.expect_column_values_to_be_unique("event_id")
    validator.expect_column_values_to_be_between("amount", 0, 1000000)

    results = validator.validate()
    return results.success
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Data loss | Ingen checkpointing | Aktivera checkpoints |
| Duplicates | At-least-once delivery | Implementera deduplication |
| Schema mismatch | Schema drift | Schema registry |
| High latency | For stor batch | Minska batch storlek |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| Batch vs Stream | Valj baserat pa latenskrav |
| Validation | Validera vid ingestion |
| Idempotency | Hantera duplicates |
| Monitoring | Overvaka ingestion pipeline |

### Kom ihag
- Validera data tidigt i pipelinen
- Implementera checkpointing
- Hantera schema evolution
- Overvaka latens och throughput
"""
    },
]
