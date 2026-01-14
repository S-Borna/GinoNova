"""
Redis for DevOps - In-Memory Caching & Data Structures
=======================================================

Master Redis for caching, session storage, queues, and pub/sub messaging.
Redis speeds up applications 10-100x and is used in 60% of high-traffic systems.
"""

REDIS_FUNDAMENTALS = {
    "title": "Redis for DevOps - High-Performance Caching",
    "slug": "redis-devops",
    "description": "Master Redis for production: caching strategies, data structures, persistence, replication, and performance optimization. Critical for scaling applications.",
    "difficulty": "intermediate",
    "estimated_minutes": 110,
    "xp_reward": 180,
    "order_index": 1,
    "content": r"""# Redis for DevOps - High-Performance Caching

## 🎯 TL;DR (30 seconds)

Redis is an in-memory data store that makes applications 10-100x faster. Use it for caching database queries,
storing sessions, rate limiting, real-time leaderboards, and pub/sub messaging. 60% of high-traffic systems use Redis.

**Why this matters:** Every millisecond counts. Redis takes load off databases and enables features impossible with
traditional databases. Master Redis = master performance optimization.

---

## 🚀 Why Redis for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 60% of Senior DevOps roles require caching knowledge
- 72% of SRE roles mention Redis or similar
- 55% of Backend Engineer roles require Redis

**Salary Impact (Sweden):**
| Role | Without Caching | With Redis Skills | Difference |
|------|----------------|-------------------|------------|
| Junior DevOps | 38,000 SEK | 42,000 SEK | **+11%** |
| DevOps Engineer | 45,000 SEK | 51,000 SEK | **+13%** |
| Senior SRE | 60,000 SEK | 68,000 SEK | **+13%** |

**Companies using Redis:** Twitter, GitHub, Snapchat, StackOverflow, Airbnb, Uber

**Performance impact:**
- Without Redis: 500 req/sec, 200ms latency
- With Redis: 10,000 req/sec, 5ms latency
- **20x throughput, 40x faster response**

---

## 📖 THEORY: What is Redis?

### Redis = Remote Dictionary Server

**Key characteristics:**
- In-memory data store (microsecond latency)
- Key-value database with rich data structures
- Single-threaded (no race conditions!)
- Optional persistence to disk
- Built-in replication and clustering

**Redis vs Memcached:**
| Feature | Redis | Memcached |
|---------|-------|-----------|
| Data structures | Strings, Lists, Sets, Hashes, Sorted Sets | Only strings |
| Persistence | RDB, AOF | None |
| Replication | Built-in | None |
| Pub/Sub | Yes | No |
| Lua scripting | Yes | No |
| Transactions | Yes | No |

**Winner:** Redis for almost everything. Memcached only if you need pure simple caching.

---

## 🛠️ HANDS-ON: Redis Installation & Setup

### Step 1: Install Redis

**Ubuntu/Debian:**
```bash
# Install from official repo
sudo apt update
sudo apt install redis-server -y

# Check status
sudo systemctl status redis-server

# Test connection
redis-cli ping
# Should return: PONG
```

**Using Docker (recommended):**
```bash
# Run Redis container
docker run -d \
  --name redis-dev \
  -p 6379:6379 \
  -v redis-data:/data \
  redis:7-alpine \
  redis-server --appendonly yes

# Connect with CLI
docker exec -it redis-dev redis-cli

# Test
127.0.0.1:6379> PING
PONG
```

**Configure Redis (`/etc/redis/redis.conf`):**
```conf
# Bind to localhost only (security)
bind 127.0.0.1 ::1

# Set password
requirepass your_strong_password_here

# Max memory (set to 70-80% of available RAM)
maxmemory 2gb

# Eviction policy when memory full
maxmemory-policy allkeys-lru

# Persistence (snapshot)
save 900 1       # Save after 900 sec if 1 key changed
save 300 10      # Save after 300 sec if 10 keys changed
save 60 10000    # Save after 60 sec if 10000 keys changed

# AOF persistence (more durable)
appendonly yes
appendfsync everysec
```

---

### Step 2: Basic Redis Commands

**Connect to Redis:**
```bash
# Without password
redis-cli

# With password
redis-cli -a your_password

# Remote connection
redis-cli -h redis.example.com -p 6379 -a password
```

**String operations:**
```redis
# Set key-value
SET user:1000:name "John Doe"

# Get value
GET user:1000:name

# Set with expiration (10 seconds)
SETEX session:abc123 10 "user_data_here"

# Set if not exists (atomic)
SETNX lock:resource1 "locked"

# Increment counter (atomic)
INCR page_views
INCRBY page_views 10

# Multiple operations
MSET key1 "value1" key2 "value2" key3 "value3"
MGET key1 key2 key3
```

---

## 🎓 Redis Data Structures Deep Dive

### 1. Strings (Most Common)

**Use case: Caching database queries**
```python
import redis
import json
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_user(user_id):
    cache_key = f"user:{user_id}"

    # Try cache first
    cached = r.get(cache_key)
    if cached:
        print("✅ Cache hit!")
        return json.loads(cached)

    # Cache miss - fetch from database
    print("❌ Cache miss - fetching from DB")
    user = fetch_from_database(user_id)  # Slow DB query

    # Store in cache for 5 minutes
    r.setex(cache_key, 300, json.dumps(user))

    return user

def fetch_from_database(user_id):
    time.sleep(0.5)  # Simulate slow DB query
    return {"id": user_id, "name": "John Doe", "email": "john@example.com"}

# First call: Cache miss (500ms)
print(get_user(1000))

# Second call: Cache hit (1ms)
print(get_user(1000))
```

---

### 2. Hashes (Structured Data)

**Use case: Store user sessions**
```redis
# Store session data
HSET session:abc123 user_id 1000
HSET session:abc123 username "john"
HSET session:abc123 last_seen 1640000000

# Or all at once
HMSET session:abc123 user_id 1000 username "john" last_seen 1640000000

# Get all fields
HGETALL session:abc123

# Get specific field
HGET session:abc123 username

# Check if field exists
HEXISTS session:abc123 user_id

# Delete field
HDEL session:abc123 last_seen
```

**Python example:**
```python
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Create session
session_id = "abc123"
r.hset(f"session:{session_id}", mapping={
    "user_id": "1000",
    "username": "john",
    "role": "admin",
    "login_time": "2026-01-13T10:00:00"
})

# Set expiration (30 minutes)
r.expire(f"session:{session_id}", 1800)

# Get session
session_data = r.hgetall(f"session:{session_id}")
print(session_data)
# {'user_id': '1000', 'username': 'john', 'role': 'admin', ...}
```

---

### 3. Lists (Queues & Activity Feeds)

**Use case: Task queue (background jobs)**
```redis
# Producer: Add tasks to queue
LPUSH queue:emails "send_email:user123@example.com"
LPUSH queue:emails "send_email:user456@example.com"

# Consumer: Process tasks
BRPOP queue:emails 0
# Returns: ["queue:emails", "send_email:user123@example.com"]

# Get queue length
LLEN queue:emails

# View queue without removing
LRANGE queue:emails 0 -1
```

**Python worker:**
```python
import redis
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def worker():
    print("Worker started, waiting for tasks...")
    while True:
        # Block until task available (timeout=5sec)
        task = r.brpop("queue:emails", timeout=5)

        if task:
            queue_name, task_data = task
            print(f"Processing: {task_data}")
            process_email(task_data)
        else:
            print("No tasks, waiting...")

def process_email(task_data):
    # Simulate email sending
    time.sleep(1)
    print(f"✅ Email sent: {task_data}")

# Run worker
# worker()
```

---

### 4. Sets (Unique Collections)

**Use case: Online users, tags, recommendations**
```redis
# Add users to online set
SADD online_users "user:1000"
SADD online_users "user:2000"
SADD online_users "user:3000"

# Check if user online
SISMEMBER online_users "user:1000"  # Returns 1 (true)

# Get all online users
SMEMBERS online_users

# Count online users
SCARD online_users

# Remove user
SREM online_users "user:1000"

# Set operations (intersection, union, diff)
SADD user:1000:friends "user:2000" "user:3000" "user:4000"
SADD user:2000:friends "user:1000" "user:3000" "user:5000"

# Mutual friends (intersection)
SINTER user:1000:friends user:2000:friends
# Returns: ["user:3000"]
```

---

### 5. Sorted Sets (Leaderboards, Rankings)

**Use case: Game leaderboard**
```redis
# Add players with scores
ZADD leaderboard 1000 "player:alice"
ZADD leaderboard 850 "player:bob"
ZADD leaderboard 1200 "player:charlie"
ZADD leaderboard 950 "player:diana"

# Get top 3 players (highest scores)
ZREVRANGE leaderboard 0 2 WITHSCORES
# Returns:
# 1) "player:charlie" 2) "1200"
# 3) "player:alice" 4) "1000"
# 5) "player:diana" 6) "950"

# Get player rank (0-indexed)
ZREVRANK leaderboard "player:alice"  # Returns 1 (2nd place)

# Get player score
ZSCORE leaderboard "player:alice"  # Returns 1000

# Increment score
ZINCRBY leaderboard 100 "player:alice"  # Now 1100

# Get players in score range
ZRANGEBYSCORE leaderboard 900 1100 WITHSCORES

# Remove player
ZREM leaderboard "player:bob"
```

**Python leaderboard:**
```python
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def add_score(player_id, score):
    r.zadd("leaderboard", {f"player:{player_id}": score})
    print(f"Added {player_id} with score {score}")

def get_top_10():
    top_players = r.zrevrange("leaderboard", 0, 9, withscores=True)
    print("\n🏆 Top 10 Leaderboard:")
    for rank, (player, score) in enumerate(top_players, 1):
        print(f"{rank}. {player}: {int(score)} points")

def get_player_rank(player_id):
    rank = r.zrevrank("leaderboard", f"player:{player_id}")
    score = r.zscore("leaderboard", f"player:{player_id}")
    if rank is not None:
        print(f"{player_id} is rank #{rank + 1} with {int(score)} points")
    else:
        print(f"{player_id} not found")

# Usage
add_score("alice", 1000)
add_score("bob", 850)
add_score("charlie", 1200)
get_top_10()
get_player_rank("alice")
```

---

## 🚀 PRODUCTION PATTERNS

### Pattern 1: Cache-Aside (Most Common)

**Strategy:**
1. Check cache first
2. If miss, fetch from DB
3. Store in cache
4. Return data

**Python implementation:**
```python
import redis
import psycopg2
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
db = psycopg2.connect("dbname=myapp user=admin password=xxx")

def get_product(product_id):
    cache_key = f"product:{product_id}"

    # 1. Check cache
    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)

    # 2. Cache miss - fetch from DB
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()

    if product:
        # 3. Store in cache (5 minutes TTL)
        r.setex(cache_key, 300, json.dumps(product))

    return product

def update_product(product_id, data):
    # Update database
    cursor = db.cursor()
    cursor.execute("UPDATE products SET name = %s WHERE id = %s",
                   (data['name'], product_id))
    db.commit()

    # Invalidate cache
    r.delete(f"product:{product_id}")
```

---

### Pattern 2: Rate Limiting

**Scenario:** Allow max 100 API requests per minute per user

```python
import redis
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def is_rate_limited(user_id, max_requests=100, window_seconds=60):
    key = f"rate_limit:{user_id}:{int(time.time() // window_seconds)}"

    # Increment request count
    current = r.incr(key)

    # Set expiration on first request
    if current == 1:
        r.expire(key, window_seconds)

    # Check if over limit
    if current > max_requests:
        return True

    return False

# Usage in API endpoint
def api_endpoint(user_id):
    if is_rate_limited(user_id):
        return {"error": "Rate limit exceeded. Try again in 1 minute."}, 429

    # Process request
    return {"data": "success"}, 200
```

---

### Pattern 3: Distributed Locking

**Scenario:** Prevent concurrent processing of same task

```python
import redis
import time
import uuid

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

class RedisLock:
    def __init__(self, key, timeout=10):
        self.key = f"lock:{key}"
        self.timeout = timeout
        self.token = str(uuid.uuid4())

    def acquire(self):
        # Set key only if it doesn't exist (atomic)
        return r.set(self.key, self.token, nx=True, ex=self.timeout)

    def release(self):
        # Only release if we own the lock (check token)
        lua_script = '''
        if redis.call("get", KEYS[1]) == ARGV[1] then
            return redis.call("del", KEYS[1])
        else
            return 0
        end
        '''
        return r.eval(lua_script, 1, self.key, self.token)

# Usage
def process_invoice(invoice_id):
    lock = RedisLock(f"invoice:{invoice_id}", timeout=30)

    if not lock.acquire():
        print("Another process is handling this invoice")
        return

    try:
        # Process invoice (may take some time)
        print(f"Processing invoice {invoice_id}...")
        time.sleep(2)
        print("Invoice processed!")
    finally:
        lock.release()

# Concurrent calls will be serialized
# process_invoice(12345)
```

---

## 📊 Monitoring & Performance

### Essential Redis Commands

**1. Server info:**
```redis
INFO
INFO server
INFO stats
INFO memory
INFO replication
```

**2. Memory usage:**
```redis
# Total memory used
INFO memory

# Memory usage by key pattern
MEMORY USAGE user:1000:profile

# Find large keys
redis-cli --bigkeys
```

**3. Slow queries:**
```redis
# Enable slow log
CONFIG SET slowlog-log-slower-than 10000  # 10ms

# View slow queries
SLOWLOG GET 10
```

**4. Connected clients:**
```redis
# List all clients
CLIENT LIST

# Kill specific client
CLIENT KILL 127.0.0.1:12345
```

**5. Key operations:**
```redis
# Count keys
DBSIZE

# Find keys by pattern
KEYS user:*  # DON'T use in production (blocks server!)

# Better: Use SCAN
SCAN 0 MATCH user:* COUNT 100

# Check key type
TYPE user:1000:profile

# Check TTL
TTL session:abc123

# Remove expiration
PERSIST session:abc123
```

---

## 🔧 Production Configuration

**Redis configuration for production (`redis.conf`):**
```conf
# Security
bind 127.0.0.1 ::1
requirepass strong_password_here_min_32_chars
rename-command FLUSHDB ""
rename-command FLUSHALL ""
rename-command CONFIG ""

# Memory
maxmemory 4gb
maxmemory-policy allkeys-lru
maxmemory-samples 5

# Persistence (RDB snapshots)
save 900 1
save 300 10
save 60 10000
stop-writes-on-bgsave-error yes
rdbcompression yes

# Persistence (AOF - more durable)
appendonly yes
appendfsync everysec
no-appendfsync-on-rewrite no
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

# Replication (if slave)
# replicaof master-ip 6379
# masterauth master-password

# Performance
tcp-backlog 511
timeout 300
tcp-keepalive 300
```

---

## 🔄 Redis Replication & High Availability

### Master-Slave Replication

**Master setup (redis-master.conf):**
```conf
bind 0.0.0.0
port 6379
requirepass master_password
```

**Slave setup (redis-slave.conf):**
```conf
bind 0.0.0.0
port 6379
requirepass slave_password
replicaof master-ip 6379
masterauth master_password
replica-read-only yes
```

**Start servers:**
```bash
redis-server redis-master.conf &
redis-server redis-slave.conf &

# Check replication status (on master)
redis-cli -a master_password INFO replication
```

---

### Redis Sentinel (Automatic Failover)

**Sentinel configuration:**
```conf
# sentinel.conf
port 26379
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel auth-pass mymaster master_password
sentinel down-after-milliseconds mymaster 5000
sentinel parallel-syncs mymaster 1
sentinel failover-timeout mymaster 10000
```

**Start sentinel:**
```bash
redis-sentinel sentinel.conf
```

---

## 🎤 Interview Questions & Answers

### Question 1: Cache Strategy

**Interviewer:** "When would you use Redis instead of caching in application memory?"

❌ **Weak Answer:**
> "Redis is faster."

✅ **Strong Answer:**
> "Use Redis when: 1) Multiple application servers need shared cache (avoid duplicate caching). 2) Cache needs to survive application restarts. 3) Cache size exceeds available RAM per instance. 4) Need features like TTL, atomic operations, or pub/sub. Use in-memory caching for: single-server apps, very hot data (sub-millisecond latency needed), or when network hop overhead matters."

**Why this impresses:** Shows understanding of trade-offs and architectural thinking.

---

### Question 2: Performance

**Interviewer:** "Your Redis instance is hitting 100% CPU. What's the problem?"

❌ **Weak Answer:**
> "Need more CPU."

✅ **Strong Answer:**
> "Redis is single-threaded, so 100% CPU means one core is maxed. Common causes: 1) Expensive commands like KEYS (use SCAN instead). 2) Large sorted set operations. 3) Too many connections (check CLIENT LIST). 4) Network I/O bottleneck (check bandwidth). Solutions: Use Redis Cluster to distribute load, optimize queries, use pipelining to reduce network round-trips, consider Redis 6+ with threaded I/O for network operations."

**Why this impresses:** Demonstrates knowledge of Redis architecture and optimization.

---

### Question 3: Data Loss

**Interviewer:** "How do you prevent data loss in Redis?"

❌ **Weak Answer:**
> "Use backups."

✅ **Strong Answer:**
> "Redis has two persistence options: 1) RDB snapshots - fast, compact, but potential data loss between snapshots. Configure with 'save 60 1000' for acceptable RPO. 2) AOF (Append-Only File) - logs every write, can replay to recover. Use 'appendfsync everysec' for good balance. For critical data, use both RDB + AOF. Additionally: Enable replication for redundancy, use Redis Sentinel for automatic failover, test restores regularly. Remember: Redis is primarily a cache - critical data should have a persistent source of truth."

**Why this impresses:** Shows understanding of durability options and production considerations.

---

## 📚 Flashcards

**Q: What is Redis?**
A: In-memory data structure store used as cache, database, and message broker.

**Q: Why is Redis fast?**
A: Data stored in RAM (not disk), single-threaded (no locks), optimized C code.

**Q: What are Redis data structures?**
A: Strings, Lists, Sets, Sorted Sets, Hashes, Bitmaps, HyperLogLogs, Streams.

**Q: What is cache-aside pattern?**
A: Check cache first, if miss fetch from DB and populate cache.

**Q: What is TTL?**
A: Time-To-Live - automatic expiration of keys after specified seconds.

**Q: RDB vs AOF?**
A: RDB = snapshots (fast, less durable). AOF = write log (slower, more durable).

**Q: What is Redis Sentinel?**
A: Monitoring and automatic failover system for Redis high availability.

**Q: What is Redis Cluster?**
A: Distributed Redis setup for horizontal scaling and sharding.

**Q: What is SCAN vs KEYS?**
A: SCAN iterates without blocking. KEYS blocks and should never be used in production.

**Q: What is pipelining?**
A: Sending multiple commands without waiting for individual responses. Reduces network latency.

---

## 🎓 Quiz

### Question 1

**Which data structure should you use for a leaderboard?**

A) List
B) Set
C) Sorted Set ✅
D) Hash

**Answer:** C ✅

**Explanation:** Sorted Sets maintain scores and allow efficient range queries and ranking operations.

---

### Question 2

**What happens when Redis reaches maxmemory with allkeys-lru policy?**

A) Redis crashes
B) Redis rejects writes
C) Redis evicts least recently used keys ✅
D) Redis clears all data

**Answer:** C ✅

**Explanation:** allkeys-lru evicts least recently used keys to make room for new data.

---

### Question 3

**Which persistence option provides better durability?**

A) RDB only
B) AOF with appendfsync everysec ✅
C) No persistence
D) RDB + no AOF

**Answer:** B ✅

**Explanation:** AOF logs every write, losing at most 1 second of data. RDB only saves snapshots periodically.

---

## 🌟 Why This Module Prepares You for Jobs

✅ **Caching mastery** - Speed up applications 10-100x
✅ **Data structures expertise** - Use right tool for each problem
✅ **Production patterns** - Rate limiting, locking, queues
✅ **Performance tuning** - Optimize Redis for scale
✅ **Interview confidence** - Answer Redis questions expertly

**Time to complete:** 2 hours
**Job market impact:** Required in 60% of senior roles
**Salary boost:** +11-13% average
**Performance impact:** 20x faster applications

---

**Module completed!** 🎉

**Next recommended:** MongoDB Operations - Master NoSQL document databases
"""
}

# Export as MODULE dict
MODULE = {
    "id": "database-redis",
    "slug": "database-redis",
    "title": "Redis Caching & Data Structures",
    "description": "Master Redis for production: caching strategies, data structures, persistence, replication, and performance optimization. Speed up applications 10-100x.",
    "icon": "⚡",
    "category": "databases",
    "difficulty": "intermediate",
    "estimated_hours": 9,
    "tasks": [REDIS_FUNDAMENTALS],
}
