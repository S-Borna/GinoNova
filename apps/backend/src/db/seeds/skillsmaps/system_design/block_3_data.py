# =============================================================================
# BLOCK 3: DATA (Noder 9-12)
# =============================================================================

NODE_09_DATABASES = {
    "node_id": 9,
    "title": "Database Types & Selection",
    "slug": "databases",
    "estimated_minutes": 60,
    "xp_reward": 165,
    "prerequisites": [3],
    "content": '''# 🗄️ Database Types & Selection

## Varför detta är kritiskt
> "Fel databas = teknisk skuld från dag 1. PostgreSQL för allt? MongoDB för allt? Nej. Rätt verktyg för rätt jobb."

## Vad du kommer lära dig
- ✅ SQL vs NoSQL trade-offs
- ✅ NoSQL categories (Key-Value, Document, Wide Column, Graph)
- ✅ Database selection matrix
- ✅ Polyglot persistence

---

## SQL vs NoSQL

```yaml
SQL (Relational):
  Struktur: Tabeller, rader, kolumner
  Schema: Strikt, fördefinierat
  ACID: Ja
  Skalning: Primärt vertikal
  Query: SQL (standardiserat)
  Best for:
    - Komplex relationer
    - Transaktioner
    - Konsistens kritisk

NoSQL:
  Struktur: Varierande (document, key-value, etc)
  Schema: Flexibelt
  ACID: Varierande (ofta BASE)
  Skalning: Horisontell
  Query: Databas-specifik
  Best for:
    - Hög skalbarhet
    - Flexibel data
    - Eventual consistency OK
```

## NoSQL Categories

```yaml
Key-Value Store:
  Struktur: key -> value
  Use cases:
    - Caching
    - Sessions
    - Shopping carts
  Exempel: Redis, DynamoDB, Memcached

Document Store:
  Struktur: key -> JSON/BSON document
  Use cases:
    - Content management
    - User profiles
    - Catalogs
  Exempel: MongoDB, CouchDB, Firestore

Wide Column:
  Struktur: Row key -> column families
  Use cases:
    - Time series
    - Analytics
    - Large scale
  Exempel: Cassandra, HBase, Bigtable

Graph:
  Struktur: Nodes + Edges
  Use cases:
    - Social networks
    - Recommendations
    - Fraud detection
  Exempel: Neo4j, Amazon Neptune
```

## Database Selection Matrix

```
+------------------+----------------------------------+
|    Use Case      |        Recommended DB            |
+------------------+----------------------------------+
| Financial trans  | PostgreSQL, MySQL               |
| User sessions    | Redis, DynamoDB                 |
| Product catalog  | MongoDB, PostgreSQL             |
| Analytics/OLAP   | ClickHouse, Snowflake           |
| Time series      | TimescaleDB, InfluxDB           |
| Full-text search | Elasticsearch, Meilisearch      |
| Social graph     | Neo4j, Amazon Neptune           |
| Caching          | Redis, Memcached                |
| Queue            | Redis, SQS, RabbitMQ            |
+------------------+----------------------------------+
```

## When to Use What

```python
def choose_database(requirements):
    if requirements.needs_transactions:
        if requirements.complex_queries:
            return "PostgreSQL"
        return "MySQL"

    if requirements.needs_horizontal_scale:
        if requirements.document_model:
            return "MongoDB"
        if requirements.high_write_throughput:
            return "Cassandra"
        return "DynamoDB"

    if requirements.needs_caching:
        return "Redis"

    if requirements.needs_search:
        return "Elasticsearch"

    if requirements.needs_graph:
        return "Neo4j"

    return "PostgreSQL"  # Safe default
```

## Polyglot Persistence

```
+-----------------------------------------------------+
|                    Application                       |
+-----------------------+-----------------------------+
                        |
    +-------------------+-------------------+
    |                   |                   |
+---▼---+          +----▼----+         +----▼----+
| Redis |          |PostgreSQL|        |  Elastic |
|(Cache)|          | (Core)  |         | (Search) |
+-------+          +---------+         +----------+
```

## ACID vs BASE

```yaml
ACID (SQL):
  Atomicity: Allt eller inget
  Consistency: Giltigt tillstånd
  Isolation: Concurrent transactions
  Durability: Persisterad data

BASE (NoSQL):
  Basically Available: Alltid tillgänglig
  Soft state: Kan ändras över tid
  Eventually consistent: Konsistent så småningom
```

## Database Per Service

```yaml
Pattern: Varje microservice äger sin databas

Fördelar:
  - Loose coupling
  - Independent scaling
  - Technology freedom
  - Failure isolation

Utmaningar:
  - Data consistency
  - Joins across services
  - Transactions across services
  - Data duplication
```

| Database | Type | Best For |
|----------|------|----------|
| PostgreSQL | SQL | General purpose |
| MongoDB | Document | Flexible schema |
| Redis | Key-Value | Caching, sessions |
| Cassandra | Wide Column | High write throughput |
| Neo4j | Graph | Relationships |
| Elasticsearch | Search | Full-text search |

**Nästa steg:** Node 10 - Database Replication
''',
}

NODE_10_REPLICATION = {
    "node_id": 10,
    "title": "Database Replication",
    "slug": "replication",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [9],
    "content": '''# 🔄 Database Replication

## Varför detta är kritiskt
> "En databas utan replicas är en tickande bomb. Hårddiskar dör, datacenters brinner - replikering är din livförsäkring."

## Vad du kommer lära dig
- ✅ Master-Slave vs Master-Master
- ✅ Synchronous vs Asynchronous replication
- ✅ Replication lag hantering
- ✅ Failover strategier

---

## Varför Replikera?

```yaml
High Availability:
  - Failover vid crash
  - No single point of failure

Read Scalability:
  - Fler servrar för reads
  - Distribuera load

Geographic Distribution:
  - Data nära användare
  - Lägre latency

Disaster Recovery:
  - Backup i annan region
  - Business continuity
```

## Master-Slave (Primary-Replica)

```
         Writes
           |
           ▼
     +-----------+
     |  Master   |
     | (Primary) |
     +-----+-----+
           | Replication
     +-----+-----+---------+
     ▼           ▼         ▼
+---------+ +---------+ +---------+
| Slave 1 | | Slave 2 | | Slave 3 |
|(Replica)| |(Replica)| |(Replica)|
+----+----+ +----+----+ +----+----+
     |           |           |
     +-----------+-----------+
              Reads
```

```yaml
Master-Slave:
  Writes: Endast till master
  Reads: Från slaves

  Fördelar:
    - Read scalability
    - Enkel modell
    - Failover möjlig

  Nackdelar:
    - Write bottleneck
    - Replication lag
    - Failover komplexitet
```

## Master-Master (Multi-Primary)

```
     +---------------------------+
     |         Writes            |
     |                           |
     ▼                           ▼
+---------+                 +---------+
| Master1 |◄---Replication--►| Master2 |
|         |                 |         |
+----+----+                 +----+----+
     |                           |
     ▼                           ▼
   Reads                       Reads
```

```yaml
Master-Master:
  Writes: Till vilken master som helst
  Reads: Från vilken som helst

  Fördelar:
    - Write scalability
    - Geographic distribution
    - No single point of failure

  Nackdelar:
    - Conflict resolution
    - Mer komplext
    - Eventual consistency
```

## Synchronous vs Asynchronous

```yaml
Synchronous Replication:
  - Master väntar på replica ack
  - Strong consistency
  - Högre latency
  - Risk för unavailability

  Transaction:
    1. Write to master
    2. Write to replica
    3. Replica ACK
    4. Commit on master
    5. Return to client

Asynchronous Replication:
  - Master väntar inte
  - Eventual consistency
  - Lägre latency
  - Risk för data loss

  Transaction:
    1. Write to master
    2. Commit on master
    3. Return to client
    4. (Background) Replicate to slaves
```

## Replication Lag

```python
# Replication lag = tid mellan master write och replica update

# Problemscenario:
# 1. User updates profile (-> master)
# 2. User refreshes page (-> slave)
# 3. Slave har inte fått update än
# 4. User ser gammal data!

# Lösningar:

# Read-your-writes consistency
def get_profile(user_id, session):
    if session.just_updated:
        return read_from_master(user_id)
    return read_from_replica(user_id)

# Monotonic reads
def get_data(user_id, last_read_timestamp):
    replica = get_replica_with_timestamp_gte(last_read_timestamp)
    return replica.read(user_id)
```

## PostgreSQL Replication

```sql
-- Primary: Enable replication
-- postgresql.conf
wal_level = replica
max_wal_senders = 5
max_replication_slots = 5

-- pg_hba.conf
host replication replicator 10.0.0.0/24 md5

-- Replica: Setup streaming replication
-- standby.signal file + primary_conninfo in postgresql.conf
primary_conninfo = 'host=primary port=5432 user=replicator'
```

## MySQL Replication

```sql
-- Master configuration
-- my.cnf
[mysqld]
server-id = 1
log_bin = mysql-bin
binlog_format = ROW

-- Replica configuration
-- my.cnf
[mysqld]
server-id = 2
relay_log = relay-bin
read_only = ON

-- Setup replication
CHANGE MASTER TO
  MASTER_HOST='primary',
  MASTER_USER='replicator',
  MASTER_PASSWORD='password',
  MASTER_LOG_FILE='mysql-bin.000001',
  MASTER_LOG_POS=0;
START SLAVE;
```

## Failover

```yaml
Automatic Failover:
  - Detect master failure
  - Promote replica
  - Redirect traffic

  Tools:
    - PostgreSQL: Patroni, repmgr
    - MySQL: Orchestrator, ProxySQL
    - Redis: Sentinel

Manual Failover:
  - DBA triggers promotion
  - Update DNS/config
  - More control
```

| Replication Type | Consistency | Latency | Data Safety |
|------------------|-------------|---------|-------------|
| Sync | Strong | High | High |
| Semi-sync | Medium | Medium | Medium |
| Async | Eventual | Low | Lower |

**Nästa steg:** Node 11 - Sharding
''',
}

NODE_11_SHARDING = {
    "node_id": 11,
    "title": "Database Sharding",
    "slug": "sharding",
    "estimated_minutes": 60,
    "xp_reward": 170,
    "prerequisites": [10],
    "content": '''# 🔀 Database Sharding

## Varför detta är kritiskt
> "100 miljoner rader i en tabell? Vertikal skalning tar slut. Sharding är din enda väg framåt - men gör det fel och du har kaos."

## Vad du kommer lära dig
- ✅ Sharding strategies (Range, Hash, Directory)
- ✅ Consistent hashing
- ✅ Shard key selection
- ✅ Cross-shard query patterns

---

## Vad är Sharding?

```
Utan Sharding:
+----------------------------+
|     Single Database        |
|   (100M rows, 1TB)         |
|   Performance issues!      |
+----------------------------+

Med Sharding:
+----------+  +----------+  +----------+  +----------+
| Shard 1  |  | Shard 2  |  | Shard 3  |  | Shard 4  |
| A-F      |  | G-L      |  | M-R      |  | S-Z      |
| 25M rows |  | 25M rows |  | 25M rows |  | 25M rows |
+----------+  +----------+  +----------+  +----------+
```

## Sharding Strategies

```yaml
Range-Based Sharding:
  Hur: Dela baserat på värde-range
  Exempel:
    Shard 1: user_id 1-1000000
    Shard 2: user_id 1000001-2000000
  Fördelar:
    - Enkelt att implementera
    - Range queries fungerar
  Nackdelar:
    - Hotspots (nya users -> sista shard)
    - Obalanserad distribution

Hash-Based Sharding:
  Hur: hash(key) % num_shards
  Exempel:
    hash("user123") % 4 = 2 -> Shard 2
  Fördelar:
    - Jämn distribution
    - Ingen hotspot
  Nackdelar:
    - Range queries svåra
    - Resharding komplext

Directory-Based Sharding:
  Hur: Lookup table
  Fördelar:
    - Flexibelt
    - Custom logic
  Nackdelar:
    - Lookup latency
    - Directory = SPOF
```

## Consistent Hashing

```
Problem med hash % N:
  - Vid N ändring -> nästan alla keys flyttas
  - Resharding = massiv data migration

Consistent Hashing:
  - Ring av hash values
  - Servers placerade på ring
  - Key -> närmaste server clockwise
  - Vid server add/remove -> endast nearby keys flyttas
```

```python
import hashlib

class ConsistentHash:
    def __init__(self, nodes, virtual_nodes=100):
        self.ring = {}
        self.sorted_keys = []

        for node in nodes:
            for i in range(virtual_nodes):
                key = self._hash(f"{node}:{i}")
                self.ring[key] = node
                self.sorted_keys.append(key)

        self.sorted_keys.sort()

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def get_node(self, key):
        hash_val = self._hash(key)
        for ring_key in self.sorted_keys:
            if hash_val <= ring_key:
                return self.ring[ring_key]
        return self.ring[self.sorted_keys[0]]
```

## Shard Key Selection

```yaml
Bra Shard Key:
  - Hög kardinalitet (många unika värden)
  - Jämn distribution
  - Matchar query patterns
  - Stabil (ändras inte)

Dåliga Shard Keys:
  - timestamp (hotspot på nya shards)
  - boolean (endast 2 shards)
  - country (ojämn distribution)

Exempel:
  E-commerce:
    ✓ customer_id (för customer queries)
    ✓ order_id (för order queries)
    ✗ order_date (hotspot)

  Social Media:
    ✓ user_id
    ✗ created_at (hotspot)
```

## Cross-Shard Queries

```yaml
Problem:
  - JOINs över shards
  - Aggregeringar
  - Global sorting

Lösningar:
  1. Denormalization:
     - Duplicera data per shard
     - Konsistens-utmaning

  2. Application-level joins:
     - Query varje shard
     - Merge i application
     - Mer kod, mer latency

  3. Scatter-Gather:
     - Broadcast query till alla shards
     - Samla och aggregera resultat

  4. Avoid:
     - Designa bort behovet
     - Colocate relaterad data
```

## Vitess (YouTube's Sharding)

```yaml
# Vitess architecture
+--------------+
|    VTGate    |  <- Query router
+------+-------+
       |
+------+-------+
|   VTTablet   |  <- Per-shard proxy
+------+-------+
       |
+------+-------+
|    MySQL     |  <- Actual database
+--------------+

Features:
  - Automatic sharding
  - Online resharding
  - Query routing
  - Connection pooling
```

## When NOT to Shard

```yaml
Alternativ först:
  1. Vertical scaling (bigger machine)
  2. Read replicas
  3. Caching layer
  4. Query optimization
  5. Archiving old data

Sharda när:
  - Vertikal skalning når limit
  - Write throughput bottleneck
  - Dataset > single machine
  - Geographic distribution krävs
```

| Strategy | Distribution | Range Query | Resharding |
|----------|--------------|-------------|------------|
| Range | Uneven | Easy | Easy |
| Hash | Even | Hard | Hard |
| Consistent Hash | Even | Hard | Easier |
| Directory | Flexible | Depends | Flexible |

**Nästa steg:** Node 12 - Caching
''',
}

NODE_12_CACHING = {
    "node_id": 12,
    "title": "Caching Strategies",
    "slug": "caching",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [9],
    "content": '''# ⚡ Caching Strategies

## Varför detta är kritiskt
> "Databasen är långsam. RAM är snabb. Caching är skillnaden mellan 500ms och 5ms - och mellan arg användare och glad användare."

## Vad du kommer lära dig
- ✅ Caching patterns (Cache-Aside, Write-Through, Write-Behind)
- ✅ Cache invalidation strategier
- ✅ Cache stampede prevention
- ✅ Redis vs Memcached

---

## Cache Layers

```
+----------------------------------------------------+
|                    User Request                    |
+------------------------+---------------------------+
                         |
                +--------▼--------+
                |  Browser Cache  |  <- Client-side
                +--------+--------+
                         |
                +--------▼--------+
                |      CDN        |  <- Edge
                +--------+--------+
                         |
                +--------▼--------+
                |  Load Balancer  |
                +--------+--------+
                         |
                +--------▼--------+
                | Application     |  <- In-memory
                | Cache (Local)   |
                +--------+--------+
                         |
                +--------▼--------+
                | Distributed     |  <- Redis/Memcached
                | Cache           |
                +--------+--------+
                         |
                +--------▼--------+
                |    Database     |  <- Query cache
                +-----------------+
```

## Caching Patterns

```yaml
Cache-Aside (Lazy Loading):
  Read:
    1. Check cache
    2. If miss -> read from DB
    3. Store in cache
    4. Return data

  Write:
    1. Write to DB
    2. Invalidate cache

Read-Through:
  Read:
    1. Always read from cache
    2. Cache fetches from DB on miss

  Write:
    - Same as cache-aside

Write-Through:
  Write:
    1. Write to cache
    2. Cache writes to DB synchronously
    3. Return to client

Write-Behind (Write-Back):
  Write:
    1. Write to cache
    2. Return to client
    3. Cache writes to DB async (batched)
```

## Cache-Aside Implementation

```python
import redis
import json

cache = redis.Redis()
TTL = 3600  # 1 hour

def get_user(user_id):
    # 1. Check cache
    cache_key = f"user:{user_id}"
    cached = cache.get(cache_key)

    if cached:
        return json.loads(cached)

    # 2. Cache miss - fetch from DB
    user = db.query("SELECT * FROM users WHERE id = ?", user_id)

    # 3. Store in cache
    cache.setex(cache_key, TTL, json.dumps(user))

    return user

def update_user(user_id, data):
    # 1. Update DB
    db.execute("UPDATE users SET ... WHERE id = ?", data, user_id)

    # 2. Invalidate cache
    cache.delete(f"user:{user_id}")
```

## Write-Through vs Write-Behind

```python
# Write-Through: Synchronous, consistent
def write_through(key, value):
    cache.set(key, value)
    db.write(key, value)  # Sync
    return "OK"

# Write-Behind: Async, faster
def write_behind(key, value):
    cache.set(key, value)
    queue.push({"key": key, "value": value})  # Async
    return "OK"

# Background worker for write-behind
def process_writes():
    while True:
        batch = queue.pop_batch(100)
        db.batch_write(batch)
```

## Cache Invalidation

```yaml
Strategies:

TTL (Time-to-Live):
  - Automatic expiration
  - Simple but can serve stale data
  - cache.setex(key, 3600, value)

Event-Based:
  - Invalidate on data change
  - More complex but fresh data
  - Pub/sub for distributed

Version-Based:
  - Key includes version
  - user:123:v5 -> user:123:v6
  - Old versions auto-expire
```

## Cache Stampede Prevention

```python
# Problem: Cache expires -> all requests hit DB

# Solution 1: Locking
def get_with_lock(key):
    value = cache.get(key)
    if value:
        return value

    lock = cache.setnx(f"lock:{key}", 1)
    if lock:
        try:
            value = db.fetch(key)
            cache.setex(key, TTL, value)
        finally:
            cache.delete(f"lock:{key}")
    else:
        # Wait and retry
        time.sleep(0.1)
        return get_with_lock(key)

    return value

# Solution 2: Probabilistic early expiration
def get_with_early_refresh(key):
    value, ttl = cache.get_with_ttl(key)

    # Refresh early with probability
    if ttl < TTL * 0.1:  # < 10% TTL remaining
        if random.random() < 0.1:  # 10% chance
            refresh_async(key)

    return value
```

## Redis vs Memcached

```yaml
Redis:
  Data Structures: Strings, Lists, Sets, Hashes, Sorted Sets
  Persistence: RDB, AOF
  Replication: Master-Slave, Cluster
  Features: Pub/Sub, Lua scripting, Transactions
  Best for: Complex data, persistence needed

Memcached:
  Data Structures: Only strings
  Persistence: None
  Replication: None (client-side)
  Features: Simple, multi-threaded
  Best for: Simple caching, multi-core
```

## Cache Sizing

```python
# Estimate cache size

# Per-item size
user_size = 500  # bytes average
num_hot_users = 100_000  # frequently accessed

# Total size
total_size = user_size * num_hot_users
# = 50 MB

# With overhead (~20%)
recommended = total_size * 1.2
# = 60 MB

# Rule of thumb: 20% of data = 80% of access
# Cache the 20% most accessed data
```

| Pattern | Consistency | Performance | Complexity |
|---------|-------------|-------------|------------|
| Cache-Aside | Medium | Good | Low |
| Read-Through | Medium | Good | Medium |
| Write-Through | High | Medium | Medium |
| Write-Behind | Lower | Best | High |

**Nästa steg:** Node 13 - Message Queues
''',
}

SYSTEM_DESIGN_BLOCK_3 = [
    NODE_09_DATABASES,
    NODE_10_REPLICATION,
    NODE_11_SHARDING,
    NODE_12_CACHING,
]
