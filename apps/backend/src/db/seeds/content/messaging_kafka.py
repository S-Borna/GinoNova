"""
Apache Kafka - Event Streaming Platform
========================================

Master Apache Kafka for distributed event streaming - producers, consumers, topics,
partitions, and stream processing. Used by 40% of Fortune 500 companies.
"""

KAFKA_FUNDAMENTALS = {
    "title": "Apache Kafka - Event Streaming Mastery",
    "slug": "kafka-event-streaming",
    "description": "Master Kafka for production: producers, consumers, topics, partitions, stream processing, and operational best practices. Power real-time data pipelines.",
    "difficulty": "advanced",
    "estimated_minutes": 130,
    "xp_reward": 220,
    "order_index": 1,
    "content": r"""# Apache Kafka - Event Streaming Mastery

## 🎯 TL;DR (30 seconds)

Kafka is a distributed event streaming platform that handles millions of events per second. Think of it as a
massively scalable message queue that never forgets. Used for real-time analytics, log aggregation, and
microservice communication. 40% of Fortune 500 use Kafka.

**Why this matters:** Modern architectures are event-driven. Kafka enables real-time processing at scale,
decouples services, and provides a source of truth for all events. Master Kafka = master distributed systems.

---

## 🚀 Why Kafka for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 55% of Senior DevOps roles require streaming/messaging knowledge
- 68% of Data Engineer roles require Kafka
- 45% of Platform Engineer roles mention Kafka

**Salary Impact (Sweden):**
| Role | Without Kafka | With Kafka Skills | Difference |
|------|--------------|-------------------|------------|
| DevOps Engineer | 45,000 SEK | 52,000 SEK | **+16%** |
| Platform Engineer | 52,000 SEK | 60,000 SEK | **+15%** |
| Senior SRE | 60,000 SEK | 72,000 SEK | **+20%** |

**Companies using Kafka:** LinkedIn (created it), Netflix, Uber, Spotify, Airbnb, Twitter, PayPal

**Scale examples:**
- LinkedIn: 7 trillion messages/day
- Netflix: 700 billion events/day
- Uber: 1 trillion messages/day

---

## 📖 THEORY: What is Kafka?

### Core Concepts

**1. Topics:** Categories for messages (like database tables)
**2. Partitions:** Topics split across multiple servers for parallelism
**3. Producers:** Applications that publish messages
**4. Consumers:** Applications that read messages
**5. Brokers:** Kafka servers that store data
**6. ZooKeeper/KRaft:** Cluster coordination (KRaft is newer, no ZooKeeper needed)

**Kafka vs Traditional Message Queues:**

| Feature | Kafka | RabbitMQ | Amazon SQS |
|---------|-------|----------|------------|
| Throughput | Million/sec | Thousand/sec | Thousand/sec |
| Message retention | Days/weeks | Until consumed | 14 days max |
| Ordering | Per partition | Per queue | FIFO queues only |
| Replay | Yes ✅ | No | No |
| Use case | Event streaming | Task queues | Simple queues |

**Key insight:** Kafka is a distributed commit log, not just a queue. Messages persist and can be replayed.

---

## 🛠️ HANDS-ON: Kafka Setup with Docker

### Step 1: Install Kafka

**Docker Compose setup (`docker-compose.yml`):**
```yaml
version: '3.8'

services:
  kafka:
    image: apache/kafka:3.7.0
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      # KRaft mode (no ZooKeeper needed)
      KAFKA_NODE_ID: 1
      KAFKA_PROCESS_ROLES: broker,controller
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@kafka:9093
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      KAFKA_LOG_DIRS: /tmp/kraft-combined-logs
      CLUSTER_ID: 'MkU3OEVBNTcwNTJENDM2Qk'
    volumes:
      - kafka-data:/var/lib/kafka/data

  kafka-ui:
    image: provectuslabs/kafka-ui:latest
    container_name: kafka-ui
    ports:
      - "8080:8080"
    environment:
      KAFKA_CLUSTERS_0_NAME: local
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:9092
    depends_on:
      - kafka

volumes:
  kafka-data:
```

**Start Kafka:**
```bash
docker-compose up -d

# Check logs
docker logs kafka

# Access Kafka UI
open http://localhost:8080
```

---

### Step 2: Basic Kafka Commands

**Create topic:**
```bash
# Create topic with 3 partitions
docker exec -it kafka kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create \
  --topic user-events \
  --partitions 3 \
  --replication-factor 1

# List topics
docker exec -it kafka kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --list

# Describe topic
docker exec -it kafka kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --describe \
  --topic user-events
```

**Produce messages (console):**
```bash
# Start producer
docker exec -it kafka kafka-console-producer.sh \
  --bootstrap-server localhost:9092 \
  --topic user-events

# Type messages (hit Enter after each):
{"user_id": 123, "action": "login", "timestamp": "2026-01-13T10:00:00Z"}
{"user_id": 456, "action": "purchase", "amount": 99.99}
{"user_id": 789, "action": "logout"}
```

**Consume messages (console):**
```bash
# Start consumer from beginning
docker exec -it kafka kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic user-events \
  --from-beginning

# Consumer with group (enables offset management)
docker exec -it kafka kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic user-events \
  --group user-events-processor \
  --from-beginning
```

---

## 🎓 Producer Programming (Python)

### Install Kafka Client

```bash
pip install confluent-kafka
```

---

### Simple Producer

```python
from confluent_kafka import Producer
import json
import time

# Producer configuration
config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

producer = Producer(config)

def delivery_callback(err, msg):
    """Called once message is delivered or fails"""
    if err:
        print(f'❌ Message delivery failed: {err}')
    else:
        print(f'✅ Message delivered to {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}')

# Produce messages
for i in range(10):
    event = {
        'user_id': 1000 + i,
        'action': 'page_view',
        'page': f'/products/{i}',
        'timestamp': time.time()
    }

    # Serialize to JSON
    value = json.dumps(event)

    # Send to Kafka (async)
    producer.produce(
        topic='user-events',
        key=str(event['user_id']),  # Messages with same key go to same partition
        value=value,
        callback=delivery_callback
    )

    # Trigger delivery callbacks
    producer.poll(0)

# Wait for all messages to be delivered
producer.flush()
print('All messages sent!')
```

---

### Production-Grade Producer

```python
from confluent_kafka import Producer, KafkaError
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KafkaProducerService:
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.config = {
            'bootstrap.servers': bootstrap_servers,
            'client.id': 'production-app',

            # Performance tuning
            'linger.ms': 10,  # Wait 10ms to batch messages
            'batch.size': 32768,  # 32 KB batch size
            'compression.type': 'snappy',  # Compress messages

            # Reliability
            'acks': 'all',  # Wait for all replicas (slowest, most reliable)
            'retries': 10,  # Retry failed sends
            'max.in.flight.requests.per.connection': 5,

            # Idempotence (prevent duplicates)
            'enable.idempotence': True
        }

        self.producer = Producer(self.config)
        self.delivery_count = {'success': 0, 'error': 0}

    def delivery_callback(self, err, msg):
        if err:
            self.delivery_count['error'] += 1
            logger.error(f'Message delivery failed: {err}')
        else:
            self.delivery_count['success'] += 1
            logger.info(f'Message delivered: {msg.topic()}[{msg.partition()}] @ {msg.offset()}')

    def send_event(self, topic, event_data, key=None):
        """Send event to Kafka topic"""
        try:
            value = json.dumps(event_data)

            self.producer.produce(
                topic=topic,
                key=key,
                value=value,
                callback=self.delivery_callback
            )

            # Poll to trigger callbacks
            self.producer.poll(0)

        except BufferError:
            logger.error('Local producer queue full. Wait or increase queue.buffering.max.messages')
            self.producer.poll(1)  # Wait for queue to clear

    def close(self):
        """Flush pending messages and close"""
        logger.info('Flushing remaining messages...')
        self.producer.flush(timeout=30)
        logger.info(f'Stats: {self.delivery_count}')

# Usage
producer_service = KafkaProducerService()

# Send user registration event
producer_service.send_event(
    topic='user-events',
    event_data={
        'event_type': 'user_registered',
        'user_id': 12345,
        'email': 'user@example.com',
        'timestamp': time.time()
    },
    key='12345'  # All events for user 12345 go to same partition
)

producer_service.close()
```

---

## 🎓 Consumer Programming (Python)

### Simple Consumer

```python
from confluent_kafka import Consumer
import json

config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'  # Start from beginning if no offset saved
}

consumer = Consumer(config)
consumer.subscribe(['user-events'])

print('Consuming messages...')

try:
    while True:
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue

        if msg.error():
            print(f'Consumer error: {msg.error()}')
            continue

        # Process message
        event = json.loads(msg.value().decode('utf-8'))
        print(f'Received event: {event}')
        print(f'  Partition: {msg.partition()}, Offset: {msg.offset()}')

        # Commit offset after processing
        consumer.commit()

except KeyboardInterrupt:
    print('Shutting down consumer...')
finally:
    consumer.close()
```

---

### Production-Grade Consumer with Error Handling

```python
from confluent_kafka import Consumer, KafkaError
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KafkaConsumerService:
    def __init__(self, topics, group_id, bootstrap_servers='localhost:9092'):
        self.config = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest',

            # Performance
            'fetch.min.bytes': 1024,  # Wait for 1KB before fetch
            'fetch.wait.max.ms': 500,  # Max wait 500ms

            # Reliability
            'enable.auto.commit': False,  # Manual commit for better control
            'max.poll.interval.ms': 300000,  # 5 minutes max processing time
        }

        self.consumer = Consumer(self.config)
        self.consumer.subscribe(topics)
        self.running = True

    def process_event(self, event):
        """Override this method with your business logic"""
        logger.info(f'Processing event: {event}')

        # Your business logic here
        # e.g., save to database, call API, etc.

    def start(self):
        """Start consuming messages"""
        logger.info('Starting consumer...')

        try:
            while self.running:
                msg = self.consumer.poll(timeout=1.0)

                if msg is None:
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        logger.info(f'Reached end of partition {msg.partition()}')
                    else:
                        logger.error(f'Consumer error: {msg.error()}')
                    continue

                try:
                    # Deserialize
                    event = json.loads(msg.value().decode('utf-8'))

                    # Process event
                    self.process_event(event)

                    # Commit offset after successful processing
                    self.consumer.commit(message=msg)

                except json.JSONDecodeError as e:
                    logger.error(f'Invalid JSON: {e}')
                    # Commit offset to skip bad message
                    self.consumer.commit(message=msg)

                except Exception as e:
                    logger.error(f'Processing error: {e}')
                    # DON'T commit - message will be reprocessed
                    # In production: send to dead-letter queue after N retries

        except KeyboardInterrupt:
            logger.info('Shutdown requested')
        finally:
            self.stop()

    def stop(self):
        """Graceful shutdown"""
        self.running = False
        logger.info('Closing consumer...')
        self.consumer.close()

# Usage
consumer = KafkaConsumerService(
    topics=['user-events'],
    group_id='user-events-processor'
)

consumer.start()
```

---

## 🎓 Advanced: Consumer Groups & Parallelism

### Understanding Consumer Groups

**Key concept:** Multiple consumers in the same group share partition load.

**Example: Topic with 6 partitions**

**Single consumer (slow):**
```
Consumer 1 → Partitions 0,1,2,3,4,5 (handles all)
```

**3 consumers in group (parallel):**
```
Consumer 1 → Partitions 0,1
Consumer 2 → Partitions 2,3
Consumer 3 → Partitions 4,5
```

**Rule:** Max useful consumers = number of partitions

**More consumers than partitions:**
```
Topic: 3 partitions
Consumers: 5

Consumer 1 → Partition 0
Consumer 2 → Partition 1
Consumer 3 → Partition 2
Consumer 4 → IDLE (no work)
Consumer 5 → IDLE (no work)
```

---

## 🔧 Production Operations

### 1. Monitor Lag (Critical!)

**Consumer lag = how far behind consumers are**

```bash
# Check consumer group lag
docker exec -it kafka kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --describe \
  --group user-events-processor

# Output:
# GROUP                  TOPIC         PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG
# user-events-processor  user-events   0          100            100             0
# user-events-processor  user-events   1          150            200             50  ⚠️
# user-events-processor  user-events   2          120            120             0
```

**Lag of 50 means consumer is 50 messages behind!**

**Solutions for high lag:**
- Add more consumers (up to partition count)
- Optimize processing speed
- Increase partitions (requires repartitioning)

---

### 2. Retention Configuration

```bash
# Set topic retention to 7 days
docker exec -it kafka kafka-configs.sh \
  --bootstrap-server localhost:9092 \
  --entity-type topics \
  --entity-name user-events \
  --alter \
  --add-config retention.ms=604800000

# Set size-based retention (10 GB)
docker exec -it kafka kafka-configs.sh \
  --bootstrap-server localhost:9092 \
  --entity-type topics \
  --entity-name user-events \
  --alter \
  --add-config retention.bytes=10737418240
```

---

### 3. Replication for High Availability

```bash
# Create topic with replication factor 3
kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create \
  --topic critical-events \
  --partitions 6 \
  --replication-factor 3

# Verify replicas
kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --describe \
  --topic critical-events

# Output shows leader and replicas per partition:
# Topic: critical-events  Partition: 0  Leader: 1  Replicas: 1,2,3  Isr: 1,2,3
```

**Replication factor guidelines:**
- Development: 1
- Production: 3 (survives 2 broker failures)
- Critical systems: 5

---

## 🎤 Interview Questions & Answers

### Question 1: Architecture

**Interviewer:** "Explain how Kafka achieves high throughput."

❌ **Weak Answer:**
> "Kafka is fast because it's written in Java."

✅ **Strong Answer:**
> "Kafka achieves high throughput through several optimizations: 1) Sequential disk writes - append-only log is much faster than random writes. 2) Zero-copy transfer - messages go directly from disk to network without application memory. 3) Batching - producers and consumers batch multiple messages. 4) Compression - messages compressed per batch. 5) Partitioning - parallel processing across partitions. 6) Page cache - OS caches frequently accessed data in RAM. These combine to achieve millions of messages per second on commodity hardware."

**Why this impresses:** Shows deep understanding of performance optimizations.

---

### Question 2: Delivery Guarantees

**Interviewer:** "How do you ensure exactly-once message processing?"

❌ **Weak Answer:**
> "Set acks=all."

✅ **Strong Answer:**
> "Exactly-once is hard in distributed systems. Kafka provides: 1) Producer idempotence - prevents duplicate writes if retry. Enable with `enable.idempotence=true`. 2) Transactions - atomic writes to multiple partitions. 3) Consumer side: use manual commit and process messages idempotently (e.g., use message key as idempotency key in database). True exactly-once requires cooperation between producer, Kafka, and consumer. In practice, at-least-once with idempotent processing is often the pragmatic solution."

**Why this impresses:** Shows understanding of distributed system challenges.

---

### Question 3: Partitioning Strategy

**Interviewer:** "How do you choose a good partition key?"

❌ **Weak Answer:**
> "Random UUID."

✅ **Strong Answer:**
> "Good partition key has: 1) High cardinality - many unique values for even distribution. 2) Related events grouped - same key goes to same partition for ordering. 3) Avoid hot partitions - don't use timestamp or sequential ID where recent values get all traffic. Examples: Good: user_id (high cardinality, user events ordered), customer_id. Bad: timestamp (recent time is hot), boolean field (only 2 partitions used). For random distribution with no ordering needs, use null key - Kafka round-robins."

**Why this impresses:** Demonstrates practical partitioning experience.

---

## 📚 Flashcards

**Q: What is a Kafka topic?**
A: Category/feed name where messages are published. Similar to a database table.

**Q: What is a partition?**
A: Unit of parallelism - topics are split into partitions for distributed processing.

**Q: What is a consumer group?**
A: Multiple consumers working together to consume a topic, sharing partition load.

**Q: What is an offset?**
A: Sequential ID for messages in a partition. Tracks consumer position.

**Q: What is replication factor?**
A: Number of copies of each partition. RF=3 means data exists on 3 brokers.

**Q: What is ISR?**
A: In-Sync Replicas - replicas that are caught up with the leader.

**Q: What does acks=all mean?**
A: Producer waits for all replicas to acknowledge write. Slowest but safest.

**Q: What is consumer lag?**
A: Difference between latest offset and consumer's current offset. Indicates backlog.

**Q: What is compaction?**
A: Retention policy that keeps only latest value per key. Used for state.

**Q: What is KRaft?**
A: Kafka's new consensus protocol replacing ZooKeeper for cluster management.

---

## 🎓 Quiz

### Question 1

**What happens if you have 5 consumers in a group but topic has 3 partitions?**

A) Error - not allowed
B) All consumers read all partitions
C) 3 consumers active, 2 idle ✅
D) Round-robin message distribution

**Answer:** C ✅

**Explanation:** Max useful consumers = partition count. Extra consumers sit idle as standby.

---

### Question 2

**Which producer setting provides strongest durability guarantee?**

A) acks=0
B) acks=1
C) acks=all ✅
D) acks=majority

**Answer:** C ✅

**Explanation:** acks=all waits for all in-sync replicas to acknowledge. Slowest but safest.

---

### Question 3

**Messages with the same key always go to:**

A) Random partition
B) First partition
C) Same partition ✅
D) All partitions

**Answer:** C ✅

**Explanation:** Kafka hashes key to determine partition, ensuring ordering for same key.

---

## 🎯 Portfolio Project: Real-Time Analytics Pipeline

**Build this for your GitHub:**

**Project:** Event-driven microservices with Kafka

**Components:**
1. User activity producer (Python)
2. Real-time analytics consumer
3. Data aggregation service
4. Kafka Connect for database sync
5. Monitoring with Kafka UI
6. Docker Compose orchestration

**Why this impresses:**
- ✅ Production Kafka setup
- ✅ Producer/Consumer patterns
- ✅ Error handling and retry logic
- ✅ Monitoring and observability
- ✅ Complete documentation

---

## 🌟 Why This Module Prepares You for Jobs

✅ **Event streaming expertise** - Critical for modern architectures
✅ **Distributed systems knowledge** - Understand scalability patterns
✅ **Production operations** - Monitor lag, handle failures
✅ **Performance tuning** - Optimize throughput and latency
✅ **Interview confidence** - Answer Kafka questions expertly

**Time to complete:** 2.5 hours
**Job market impact:** Required in 55% of senior DevOps roles
**Salary boost:** +15-20% average
**Scale capability:** Handle billions of events per day

---

**Module completed!** 🎉

**Next recommended:** RabbitMQ Message Queuing - Master traditional messaging patterns
"""
}

# Export as MODULE dict
MODULE = {
    "id": "messaging-kafka",
    "slug": "messaging-kafka",
    "title": "Apache Kafka Event Streaming",
    "description": "Master Kafka for production: event streaming, producers, consumers, topics, partitions, and operational best practices. Power real-time data pipelines at massive scale.",
    "icon": "📨",
    "category": "messaging",
    "difficulty": "advanced",
    "estimated_hours": 12,
    "tasks": [KAFKA_FUNDAMENTALS],
}
