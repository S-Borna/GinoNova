# =============================================================================
# BLOCK 5: ADVANCED (Noder 17-20)
# =============================================================================

NODE_17_RATE_LIMITING = {
    "node_id": 17,
    "title": "Rate Limiting & Throttling",
    "slug": "rate-limiting",
    "estimated_minutes": 45,
    "xp_reward": 130,
    "prerequisites": [16],
    "content": '''# 🚦 Rate Limiting & Throttling

## Varför detta är kritiskt
> "Utan rate limiting är du en DDoS-attack bort från bankrutt. Skydda dina resurser, respektera dina kostnader, ge alla rättvis tillgång."

## Vad du kommer lära dig
- ✅ Rate limiting algorithms (Token Bucket, Sliding Window)
- ✅ Distributed rate limiting med Redis
- ✅ Graceful degradation
- ✅ Response headers och best practices

---

## Varför Rate Limiting?

```yaml
Skydd mot:
  - DDoS-attacker
  - Brute force
  - Scraping
  - API abuse
  - Oavsiktlig överanvändning

Fördelar:
  - Stabil service
  - Fair usage
  - Kostnadskontroll
  - SLA compliance
```

## Rate Limiting Algorithms

```yaml
Fixed Window:
  - X requests per minute
  - Resets på minutgräns

  Problem: Burst vid gränsövergång
  |---100---|---100---|
       ^50     ^50
       = 100 på 1 sekund!

Sliding Window Log:
  - Logga alla requests med timestamp
  - Räkna requests i sliding window

  + Exakt
  - Mer minne

Sliding Window Counter:
  - Weighted average av windows
  - Kompromiss

  current_rate = (prev_count * weight) + current_count
  weight = (60 - seconds_into_current) / 60

Token Bucket:
  - Bucket med tokens
  - Tokens refill över tid
  - Request konsumerar token

  + Tillåter bursts
  + Flexibelt
```

## Token Bucket Implementation

```python
import time

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate  # tokens per second
        self.last_refill = time.time()

    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        new_tokens = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill = now

    def consume(self, tokens=1):
        self._refill()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

# Usage
bucket = TokenBucket(capacity=100, refill_rate=10)  # 10/sec

if bucket.consume():
    process_request()
else:
    return "429 Too Many Requests"
```

## Distributed Rate Limiting

```python
# Redis-based sliding window
import redis
import time

def is_rate_limited(user_id, limit=100, window=60):
    key = f"ratelimit:{user_id}"
    now = time.time()

    pipe = redis.pipeline()
    # Remove old entries
    pipe.zremrangebyscore(key, 0, now - window)
    # Add current request
    pipe.zadd(key, {str(now): now})
    # Count requests
    pipe.zcard(key)
    # Set expiry
    pipe.expire(key, window)

    results = pipe.execute()
    request_count = results[2]

    return request_count > limit

# Leaky bucket with Redis
def leaky_bucket(user_id, rate=10, capacity=100):
    key = f"bucket:{user_id}"
    now = time.time()

    # Atomic operation with Lua script
    script = """
    local tokens = tonumber(redis.call('get', KEYS[1]) or ARGV[2])
    local last = tonumber(redis.call('get', KEYS[2]) or ARGV[3])
    local now = tonumber(ARGV[3])
    local rate = tonumber(ARGV[1])
    local capacity = tonumber(ARGV[2])

    local elapsed = now - last
    tokens = math.min(capacity, tokens + elapsed * rate)

    if tokens >= 1 then
        tokens = tokens - 1
        redis.call('set', KEYS[1], tokens)
        redis.call('set', KEYS[2], now)
        return 1
    end
    return 0
    """
    return redis.eval(script, 2, f"{key}:tokens", f"{key}:last", rate, capacity, now)
```

## Rate Limiting Strategies

```yaml
Per User:
  - Authenticated users
  - Fair allocation
  - Different tiers

Per IP:
  - Unauthenticated requests
  - Potential för false positives (NAT)

Per API Key:
  - B2B integrations
  - Billing

Per Endpoint:
  - Dyra endpoints (search)
  - Skydda resurser

Global:
  - Systemskydd
  - Last resort
```

## Graceful Degradation

```python
# Tiered response
def handle_request(user_id):
    # Check rate limits
    rate = get_current_rate(user_id)

    if rate > CRITICAL_LIMIT:
        return Response(status=503, body="Service unavailable")

    if rate > HIGH_LIMIT:
        # Serve from cache only
        return get_cached_response()

    if rate > MEDIUM_LIMIT:
        # Simplified response
        return get_simplified_response()

    # Full response
    return get_full_response()
```

## Response Headers

```yaml
Headers:
  X-RateLimit-Limit: 100
  X-RateLimit-Remaining: 42
  X-RateLimit-Reset: 1640000000
  Retry-After: 30

Response på 429:
  {
    "error": "rate_limit_exceeded",
    "message": "Too many requests",
    "retry_after": 30
  }
```

| Algorithm | Bursts | Memory | Accuracy |
|-----------|--------|--------|----------|
| Fixed Window | High | Low | Low |
| Sliding Log | None | High | High |
| Sliding Counter | Medium | Medium | Medium |
| Token Bucket | Controlled | Low | High |

**Nästa steg:** Node 18 - Observability
''',
}

NODE_18_OBSERVABILITY = {
    "node_id": 18,
    "title": "Observability: Logs, Metrics, Traces",
    "slug": "observability",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [14],
    "content": '''# 👁️ Observability: Logs, Metrics, Traces

## Varför detta är kritiskt
> "Om du inte kan mäta det, kan du inte fixa det. Observability är skillnaden mellan 'något är fel' och 'request X failade i service Y på grund av Z'."

## Vad du kommer lära dig
- ✅ Three Pillars: Logs, Metrics, Traces
- ✅ Structured logging
- ✅ Prometheus metrics
- ✅ Distributed tracing med OpenTelemetry

---

## Three Pillars of Observability

```
+----------------------------------------------------+
|                  Observability                      |
+---------------+---------------+--------------------+
|     Logs      |    Metrics    |      Traces        |
|               |               |                    |
|  What         |  How much     |  How requests      |
|  happened     |  & trends     |  flow through      |
|               |               |                    |
|  Debugging    |  Alerting     |  Performance       |
|  Forensics    |  Dashboards   |  Dependencies      |
+---------------+---------------+--------------------+
```

## Logging

```yaml
Log Levels:
  DEBUG: Detailed debugging
  INFO: General information
  WARN: Potential problems
  ERROR: Error conditions
  FATAL: Application crash

Structured Logging:
  {
    "timestamp": "2024-01-15T10:30:00Z",
    "level": "ERROR",
    "service": "order-service",
    "trace_id": "abc123",
    "user_id": 456,
    "message": "Payment failed",
    "error": "Card declined",
    "duration_ms": 234
  }
```

```python
import structlog

log = structlog.get_logger()

def process_order(order_id, user_id):
    log = log.bind(order_id=order_id, user_id=user_id)

    log.info("processing_order_started")

    try:
        result = payment_service.charge(order_id)
        log.info("payment_successful", amount=result.amount)
    except PaymentError as e:
        log.error("payment_failed", error=str(e))
        raise
```

## Metrics

```yaml
Types:
  Counter:
    - Only increases
    - Requests, errors
    - http_requests_total

  Gauge:
    - Can go up/down
    - Current value
    - active_connections

  Histogram:
    - Distribution
    - Latency buckets
    - request_duration_seconds

  Summary:
    - Quantiles
    - P50, P95, P99
```

```python
from prometheus_client import Counter, Histogram, Gauge

# Metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 5.0]
)

ACTIVE_REQUESTS = Gauge(
    'http_requests_active',
    'Active HTTP requests'
)

# Usage
@app.middleware
async def metrics_middleware(request, call_next):
    ACTIVE_REQUESTS.inc()
    start = time.time()

    response = await call_next(request)

    duration = time.time() - start
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        status=response.status_code
    ).inc()
    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.path
    ).observe(duration)
    ACTIVE_REQUESTS.dec()

    return response
```

## Distributed Tracing

```
Request Flow:
+---------+     +---------+     +---------+
| Gateway |----►| Orders  |----►| Payment |
+---------+     +---------+     +---------+
  Span A          Span B          Span C

Trace ID: abc-123 (same for all spans)

Span A: Gateway
+-- trace_id: abc-123
+-- span_id: 001
+-- parent_id: null
+-- start: 0ms
+-- duration: 150ms

Span B: Orders
+-- trace_id: abc-123
+-- span_id: 002
+-- parent_id: 001
+-- start: 10ms
+-- duration: 100ms

Span C: Payment
+-- trace_id: abc-123
+-- span_id: 003
+-- parent_id: 002
+-- start: 50ms
+-- duration: 40ms
```

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# Setup
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

# Usage
async def process_order(order_id):
    with tracer.start_as_current_span("process_order") as span:
        span.set_attribute("order_id", order_id)

        with tracer.start_as_current_span("validate_order"):
            validate(order_id)

        with tracer.start_as_current_span("charge_payment"):
            await payment_service.charge(order_id)
```

## Observability Stack

```yaml
Logs:
  - Collection: Fluentd, Vector
  - Storage: Elasticsearch, Loki
  - UI: Kibana, Grafana

Metrics:
  - Collection: Prometheus
  - Storage: Prometheus, VictoriaMetrics
  - UI: Grafana

Traces:
  - Collection: OpenTelemetry
  - Storage: Jaeger, Tempo
  - UI: Jaeger UI, Grafana

All-in-One:
  - Datadog
  - New Relic
  - Splunk
```

## Alerting

```yaml
# Prometheus alerting rules
groups:
  - name: api-alerts
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m]))
          / sum(rate(http_requests_total[5m])) > 0.01
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"

      - alert: SlowRequests
        expr: |
          histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 1
        for: 10m
        labels:
          severity: warning
```

| Tool | Purpose | Type |
|------|---------|------|
| Prometheus | Metrics | OSS |
| Grafana | Visualization | OSS |
| Jaeger | Tracing | OSS |
| ELK Stack | Logs | OSS |
| Datadog | All-in-one | SaaS |

**Nästa steg:** Node 19 - System Design Patterns
''',
}

NODE_19_PATTERNS = {
    "node_id": 19,
    "title": "System Design Patterns",
    "slug": "patterns",
    "estimated_minutes": 60,
    "xp_reward": 165,
    "prerequisites": [14, 12],
    "content": '''# 🧱 System Design Patterns

## Varför detta är kritiskt
> "Återuppfinn inte hjulet. CQRS, Event Sourcing, Strangler Fig - dessa patterns löser problem som tusentals ingenjörer redan kämpat med."

## Vad du kommer lära dig
- ✅ CQRS (Command Query Responsibility Segregation)
- ✅ Event Sourcing
- ✅ Strangler Fig för legacy migration
- ✅ Bulkhead och Sidecar patterns

---

## CQRS (Command Query Responsibility Segregation)

```yaml
Koncept:
  - Separera läsning från skrivning
  - Olika modeller för queries och commands

Write Side:
  - Commands -> Write Model -> Event Store

Read Side:
  - Event Store -> Projections -> Read Model -> Queries

Benefits:
  - Optimera read/write separat
  - Skalbar
  - Enklare modeller
```

```
                Command                    Query
                   |                         |
                   ▼                         ▼
            +-----------+             +-----------+
            |  Command  |             |   Query   |
            |  Handler  |             |  Handler  |
            +-----+-----+             +-----+-----+
                  |                         |
                  ▼                         ▼
            +-----------+             +-----------+
            |   Write   |   Events    |   Read    |
            |   Model   |------------►|   Model   |
            +-----------+             +-----------+
                  |                         |
                  ▼                         ▼
            +-----------+             +-----------+
            |Event Store|             | View DB   |
            +-----------+             +-----------+
```

## Event Sourcing + CQRS

```python
# Event Store
class EventStore:
    def save(self, aggregate_id, events):
        for event in events:
            db.insert("events", {
                "aggregate_id": aggregate_id,
                "event_type": event.__class__.__name__,
                "data": event.to_dict(),
                "timestamp": datetime.utcnow()
            })

    def get_events(self, aggregate_id):
        return db.query("SELECT * FROM events WHERE aggregate_id = ?", aggregate_id)

# Order Aggregate
class Order:
    def __init__(self, events):
        self.status = "pending"
        self.items = []
        for event in events:
            self.apply(event)

    def apply(self, event):
        if isinstance(event, OrderCreated):
            self.id = event.order_id
        elif isinstance(event, ItemAdded):
            self.items.append(event.item)
        elif isinstance(event, OrderCompleted):
            self.status = "completed"

# Read Model Projection
class OrderProjection:
    def handle(self, event):
        if isinstance(event, OrderCreated):
            read_db.insert("orders_view", {
                "id": event.order_id,
                "status": "pending"
            })
```

## Strangler Fig Pattern

```yaml
Koncept:
  - Gradvis migration från legacy
  - Nya features i ny system
  - Gamla features migreras stegvis

Process:
  1. Identifiera migration boundary
  2. Proxy framför legacy
  3. Implementera i nytt system
  4. Route trafik till nytt
  5. Ta bort legacy
```

```
Before:
  +-----------------------------+
  |       Legacy System         |
  |   Everything in one place   |
  +-----------------------------+

During:
  +---------------------------------------------+
  |                  Proxy                      |
  +----------------+----------------------------+
         +---------+---------+
         ▼                   ▼
  +-------------+     +-------------+
  |   Legacy    |     |    New      |
  |  (shrinking)|     | (growing)   |
  +-------------+     +-------------+

After:
  +-----------------------------+
  |        New System           |
  |   Modern architecture       |
  +-----------------------------+
```

## Sidecar Pattern

```yaml
Koncept:
  - Helper container vid sidan av main
  - Delar resurser (nätverk, storage)
  - Cross-cutting concerns

Use Cases:
  - Logging/monitoring
  - Proxy (Envoy)
  - TLS termination
  - Configuration
```

```yaml
# Kubernetes sidecar example
apiVersion: v1
kind: Pod
spec:
  containers:
    - name: app
      image: myapp:latest
      ports:
        - containerPort: 8080

    - name: envoy-sidecar
      image: envoyproxy/envoy:latest
      ports:
        - containerPort: 9901
```

## Bulkhead Pattern

```python
# Isolera failures
from concurrent.futures import ThreadPoolExecutor

class BulkheadExecutor:
    def __init__(self, max_workers):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.semaphore = threading.Semaphore(max_workers)

    def submit(self, fn, *args):
        if not self.semaphore.acquire(blocking=False):
            raise BulkheadFullException("Bulkhead full")

        def wrapper():
            try:
                return fn(*args)
            finally:
                self.semaphore.release()

        return self.executor.submit(wrapper)

# Usage - separate pools per service
payment_pool = BulkheadExecutor(max_workers=10)
inventory_pool = BulkheadExecutor(max_workers=10)

# Payment issues don't affect inventory
payment_pool.submit(process_payment, order_id)
inventory_pool.submit(check_inventory, item_id)
```

## Ambassador Pattern

```yaml
Koncept:
  - Proxy för externa services
  - Retry, circuit breaker
  - Monitoring

Similar to:
  - Sidecar (but for outbound)
  - API Gateway (but per-service)
```

## Backend for Frontend (BFF)

```
                    +-------------+
                    |   Mobile    |
                    |   Client    |
                    +------+------+
                           |
                    +------▼------+
                    | Mobile BFF  |
                    +------+------+
                           |
         +-----------------+-----------------+
         |                 |                 |
    +----▼----+       +----▼----+       +----▼----+
    | Users   |       | Orders  |       |Products |
    +---------+       +---------+       +---------+
         |                 |                 |
         |          +------▼------+          |
         |          |  Web BFF    |          |
         |          +------+------+          |
         |                 |                 |
         |          +------▼------+          |
         |          |    Web      |          |
         |          |   Client    |          |
         |          +-------------+          |
```

| Pattern | Use Case |
|---------|----------|
| CQRS | Complex domains |
| Event Sourcing | Audit, replay |
| Strangler Fig | Legacy migration |
| Sidecar | Cross-cutting concerns |
| Bulkhead | Fault isolation |
| BFF | Client-specific APIs |

**Nästa steg:** Node 20 - Case Studies
''',
}

NODE_20_CASE_STUDIES = {
    "node_id": 20,
    "title": "Case Studies",
    "slug": "case-studies",
    "estimated_minutes": 60,
    "xp_reward": 170,
    "prerequisites": [19],
    "content": '''# 📚 Case Studies

## Varför detta är kritiskt
> "Teori är bra. Praktik är bättre. Dessa case studies är vad som skiljer junior från senior - du har nu sett hur Twitter, WhatsApp och URL shorteners faktiskt byggs."

## Vad du kommer lära dig
- ✅ URL Shortener design
- ✅ Twitter Timeline feed
- ✅ Chat system (WhatsApp-stil)
- ✅ System Design interview framework

---

## URL Shortener (bit.ly)

```yaml
Requirements:
  - Shorten long URLs
  - Redirect to original
  - Analytics

Scale:
  - 100M URLs created/month
  - 10B redirects/month

Design:
  Write Path:
    1. Generate short code
    2. Store: short_code -> long_url
    3. Return shortened URL

  Read Path:
    1. Lookup short_code
    2. 301 Redirect
    3. Log analytics (async)

Components:
  - API servers (stateless)
  - Cache (Redis): Hot URLs
  - Database (MySQL/Postgres): All URLs
  - Analytics (Kafka -> ClickHouse)
```

```
+----------------------------------------------------+
|                    Client                          |
+------------------------+---------------------------+
                         |
                +--------▼--------+
                |  Load Balancer  |
                +--------+--------+
                         |
                +--------▼--------+
                |   API Servers   |
                +--------+--------+
            +------------+------------+
            ▼            ▼            ▼
       +--------+   +--------+   +--------+
       | Cache  |   |   DB   |   | Kafka  |
       |(Redis) |   |        |   |        |
       +--------+   +--------+   +--------+
                                      |
                               +------▼------+
                               | ClickHouse  |
                               | (Analytics) |
                               +-------------+
```

## Twitter Timeline

```yaml
Requirements:
  - Post tweets
  - Home timeline (followers' tweets)
  - User timeline

Scale:
  - 500M tweets/day
  - 300M users
  - P99 latency < 500ms

Approaches:

  Pull Model:
    - Query followers' tweets on request
    - N queries per timeline
    - Slow for high-follower users

  Push Model (Fan-out):
    - Pre-compute timelines
    - Write tweet -> push to all follower caches
    - Fast reads, expensive writes

  Hybrid:
    - Push for normal users
    - Pull for celebrities (millions of followers)
```

```
Tweet Post:
  1. Write to DB
  2. Fan-out to follower timelines (async)
  3. For celebrities: mark for pull

Timeline Read:
  1. Read pre-computed timeline from cache
  2. Merge with celebrity tweets (pull)
  3. Return sorted
```

## Design Chat System (WhatsApp)

```yaml
Requirements:
  - 1:1 messaging
  - Group chats
  - Online status
  - Message delivery receipts

Scale:
  - 100B messages/day
  - 2B users

Design:
  WebSocket Servers:
    - Persistent connections
    - Real-time delivery

  Message Queue:
    - Buffer for offline users
    - Reliable delivery

  Database:
    - Messages: Cassandra (write-heavy)
    - Users: MySQL
```

```
User A                                    User B
   |                                         |
   | WebSocket                    WebSocket  |
   ▼                                         ▼
+----------+                          +----------+
| WS Server|                          | WS Server|
|  (Pod 1) |                          |  (Pod 2) |
+----+-----+                          +----+-----+
     |                                     |
     |         +--------------+            |
     +--------►|  Redis Pub/  |◄-----------+
               |     Sub      |
               +--------------+
                      |
               +------▼------+
               |  Cassandra  |
               |  (Messages) |
               +-------------+
```

## Design Rate Limiter

```yaml
Requirements:
  - 100 requests/user/minute
  - Low latency
  - Distributed

Design:
  - Sliding window counter
  - Redis for state
  - Lua script for atomicity

Implementation:
  key: rate_limit:{user_id}:{minute}
  Operations:
    1. INCR current window
    2. Get previous window count
    3. Calculate weighted rate
    4. Allow or reject
```

## Design Notification System

```yaml
Requirements:
  - Push, Email, SMS
  - Priority levels
  - Delivery tracking

Design:
  +------------+
  | Service A  |--+
  +------------+  |
  +------------+  |    +-----------------+
  | Service B  |--+---►| Notification    |
  +------------+  |    | Service         |
  +------------+  |    +--------+--------+
  | Service C  |--+             |
  +------------+         +------+------+
                         ▼             ▼
                    +--------+    +--------+
                    |  Push  |    | Email  |
                    | Queue  |    | Queue  |
                    +----+---+    +---+----+
                         |            |
                         ▼            ▼
                    +--------+   +--------+
                    | FCM/   |   |Sendgrid|
                    | APNs   |   |        |
                    +--------+   +--------+
```

## Interview Tips

```yaml
Framework:
  1. Clarify (5 min):
     - Functional requirements
     - Scale (users, data, RPS)
     - Constraints

  2. High-Level (10 min):
     - Core components
     - Data flow
     - APIs

  3. Deep Dive (20 min):
     - Database choice
     - Scaling strategy
     - Trade-offs

  4. Wrap Up (5 min):
     - Bottlenecks
     - Monitoring
     - Future improvements
```

---

🎉 **Grattis!** Du har slutfört System Design SkillsMap!

Du kan nu:
- Designa skalbara system
- Välja rätt databaser och caching
- Implementera microservices
- Hantera distribuerade system
''',
}

SYSTEM_DESIGN_BLOCK_5 = [
    NODE_17_RATE_LIMITING,
    NODE_18_OBSERVABILITY,
    NODE_19_PATTERNS,
    NODE_20_CASE_STUDIES,
]
