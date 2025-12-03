"""
MLOps SkillsMap - Block 2: Data Engineering
Nodes 5-8: Pipelines, Feature Stores, Data Lakes, Ingestion
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
spark = SparkSession.builder \\
    .appName("MLPipeline") \\
    .config("spark.sql.adaptive.enabled", "true") \\
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

    # Node 7: Data Lakes & Warehouses
    {
        "id": "mlops-data-lakes",
        "slug": "data-lakes-warehouses",
        "title": "Data Lakes & Warehouses",
        "order_index": 7,
        "estimated_minutes": 30,
        "xp_reward": 75,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["mlops-feature-stores"],
        "content": """# Data Lakes & Warehouses for ML

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
spark = SparkSession.builder \\
    .appName("DeltaLakeML") \\
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \\
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \\
    .getOrCreate()
```

### Write Data
```python
# Skriv som Delta
df.write.format("delta").mode("overwrite").save("/data/ml/features")

# Med partitionering
df.write.format("delta") \\
    .partitionBy("date", "region") \\
    .mode("overwrite") \\
    .save("/data/ml/features")

# Append new data
new_df.write.format("delta").mode("append").save("/data/ml/features")
```

### Time Travel (Perfekt för ML Reproducibility!)
```python
# Läs specifik version
df_v0 = spark.read.format("delta").option("versionAsOf", 0).load("/data/ml/features")

# Läs vid specifik tidpunkt
df_yesterday = spark.read.format("delta") \\
    .option("timestampAsOf", "2024-01-14") \\
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
new_df_with_extra_column.write.format("delta") \\
    .mode("append") \\
    .option("mergeSchema", "true") \\
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
silver_df = silver_df \\
    .dropDuplicates(["event_id"]) \\
    .filter(col("user_id").isNotNull()) \\
    .withColumn("event_date", to_date(col("timestamp")))

silver_df.write.format("delta") \\
    .partitionBy("event_date") \\
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
spark = SparkSession.builder \\
    .appName("ML") \\
    .enableHiveSupport() \\
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

spark = SparkSession.builder \\
    .appName("StreamingML") \\
    .getOrCreate()

# Schema för events
schema = StructType() \\
    .add("user_id", StringType()) \\
    .add("amount", DoubleType()) \\
    .add("timestamp", TimestampType())

# Läs från Kafka
df = spark.readStream \\
    .format("kafka") \\
    .option("kafka.bootstrap.servers", "kafka:9092") \\
    .option("subscribe", "transactions") \\
    .option("startingOffsets", "latest") \\
    .load()

# Parse JSON
events = df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Windowed aggregations för features
windowed_features = events \\
    .withWatermark("timestamp", "10 minutes") \\
    .groupBy(
        col("user_id"),
        window(col("timestamp"), "5 minutes")
    ) \\
    .agg(
        count("*").alias("transaction_count_5m"),
        sum("amount").alias("total_amount_5m"),
        avg("amount").alias("avg_amount_5m"),
    )

# Skriv till Delta Lake
query = windowed_features.writeStream \\
    .format("delta") \\
    .outputMode("update") \\
    .option("checkpointLocation", "/checkpoints/features") \\
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
]
