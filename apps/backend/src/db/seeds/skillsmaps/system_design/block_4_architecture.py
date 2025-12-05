# =============================================================================
# BLOCK 4: ARCHITECTURE (Noder 13-16)
# =============================================================================

NODE_13_QUEUES = {
    "node_id": 13,
    "title": "Message Queues & Event Streaming",
    "slug": "message-queues",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [8],
    "content": '''# 📨 Message Queues & Event Streaming

## Varför detta är kritiskt
> "Synkrona anrop = dominoeffekt av failures. En queue mellan services = resilience. Det är skillnaden mellan 'allt är nere' och 'vi processar i kö'."

## Vad du kommer lära dig
- ✅ Queue vs Pub/Sub patterns
- ✅ Kafka, RabbitMQ, SQS jämförelse
- ✅ Delivery guarantees (At-least-once, Exactly-once)
- ✅ Idempotency och backpressure

---

## Varför Message Queues?

```yaml
Problem med synkrona anrop:
  - Tight coupling
  - Cascading failures
  - Blocked waiting
  - Poor scalability

Fördelar med queues:
  - Decoupling
  - Buffering (peak traffic)
  - Resilience
  - Async processing
```

## Queue vs Pub/Sub

```
Message Queue (Point-to-Point):
                    ┌─────────────┐
Producer ──────────►│    Queue    │───────► Consumer
                    └─────────────┘
  - En consumer per message
  - Load balancing möjlig

Pub/Sub (Fan-out):
                    ┌─────────────┐
Publisher ─────────►│    Topic    │───┬──► Subscriber 1
                    └─────────────┘   ├──► Subscriber 2
                                      └──► Subscriber 3
  - Alla subscribers får message
  - Event notification
```

## Message Queue Patterns

```yaml
Work Queue:
  - Multiple workers
  - Load balanced
  - At-least-once delivery

Request-Reply:
  - Sync over async
  - Correlation ID
  - Reply queue

Dead Letter Queue (DLQ):
  - Failed messages
  - Retry logic
  - Debugging
```

## Queue Technologies

```yaml
RabbitMQ:
  Protocol: AMQP
  Features:
    - Flexible routing
    - Message acknowledgment
    - Plugins (federation, shovel)
  Best for: Traditional messaging

Apache Kafka:
  Protocol: Custom (TCP)
  Features:
    - High throughput
    - Persistent log
    - Replay capability
  Best for: Event streaming, logs

Amazon SQS:
  Protocol: HTTP
  Features:
    - Fully managed
    - FIFO available
    - DLQ built-in
  Best for: AWS workloads

Redis Streams:
  Protocol: RESP
  Features:
    - Consumer groups
    - Persistence
    - Already have Redis
  Best for: Simple streaming
```

## Kafka Architecture

```
                    ┌─────────────────────────────────┐
                    │          Kafka Cluster          │
                    │  ┌─────────────────────────┐    │
Producer ──────────►│  │    Topic: orders        │    │
                    │  │  ┌───┐ ┌───┐ ┌───┐      │    │
                    │  │  │P0 │ │P1 │ │P2 │      │    │◄─── Consumer Group
                    │  │  └───┘ └───┘ └───┘      │    │
                    │  └─────────────────────────┘    │
                    └─────────────────────────────────┘

Partitions:
  - Ordered within partition
  - Parallel processing
  - Key-based routing
```

## Delivery Guarantees

```yaml
At-Most-Once:
  - Fire and forget
  - Fast, unreliable
  - Metrics, logs

At-Least-Once:
  - Retry on failure
  - Duplicates possible
  - Most common
  - Requires idempotency

Exactly-Once:
  - No duplicates, no loss
  - Hard/expensive
  - Kafka supports with transactions
```

## Idempotency

```python
# Problem: At-least-once kan ge duplicates
# Lösning: Idempotent consumers

# Approach 1: Idempotency key
def process_order(order_id, data):
    if redis.setnx(f"processed:{order_id}", 1):
        # First time - process
        db.create_order(order_id, data)
        redis.expire(f"processed:{order_id}", 86400)
    else:
        # Duplicate - skip
        log.info(f"Duplicate order {order_id}, skipping")

# Approach 2: Database constraint
def process_payment(payment_id, amount):
    try:
        db.execute("""
            INSERT INTO payments (id, amount)
            VALUES (?, ?)
            ON CONFLICT (id) DO NOTHING
        """, payment_id, amount)
    except DuplicateKeyError:
        pass  # Already processed
```

## Event Sourcing

```yaml
Traditional:
  - Store current state
  - UPDATE user SET balance = 100

Event Sourcing:
  - Store events
  - Events: [Deposited(50), Withdrew(20), Deposited(70)]
  - Replay to get state

Benefits:
  - Complete audit trail
  - Time travel
  - Event replay
  - Debugging

Drawbacks:
  - More storage
  - Complex queries
  - Event versioning
```

## Backpressure

```python
# Prevent queue overflow

# Consumer-side throttling
async def consume_with_backpressure():
    semaphore = asyncio.Semaphore(100)  # Max concurrent

    async for message in queue:
        await semaphore.acquire()
        asyncio.create_task(
            process_with_release(message, semaphore)
        )

# Producer-side circuit breaker
def produce_with_circuit_breaker(message):
    queue_size = queue.size()

    if queue_size > HIGH_WATERMARK:
        raise BackpressureError("Queue full")

    queue.push(message)
```

| Technology | Throughput | Ordering | Persistence |
|------------|------------|----------|-------------|
| RabbitMQ | Medium | Queue-level | Optional |
| Kafka | Very High | Partition | Yes |
| SQS | Medium | FIFO option | Yes |
| Redis Streams | High | Stream | Yes |

**Nästa steg:** Node 14 - Microservices
''',
}

NODE_14_MICROSERVICES = {
    "node_id": 14,
    "title": "Microservices Architecture",
    "slug": "microservices",
    "estimated_minutes": 60,
    "xp_reward": 165,
    "prerequisites": [13],
    "content": '''# 🧩 Microservices Architecture

## Varför detta är kritiskt
> "Monolither skalas inte i organisationer. Microservices låter team arbeta oberoende - men komplexiteten flyttas bara, den försvinner inte."

## Vad du kommer lära dig
- ✅ Monolith vs Microservices trade-offs
- ✅ Service discovery
- ✅ Circuit breaker pattern
- ✅ Saga pattern för distribuerade transaktioner

---

## Monolith vs Microservices

```yaml
Monolith:
  ┌────────────────────────────────┐
  │          Application           │
  │  ┌──────┐ ┌──────┐ ┌──────┐   │
  │  │Users │ │Orders│ │Payment│  │
  │  └──────┘ └──────┘ └──────┘   │
  │         Single Deploy          │
  └────────────────────────────────┘

Microservices:
  ┌────────┐   ┌────────┐   ┌────────┐
  │ Users  │   │ Orders │   │Payment │
  │Service │   │Service │   │Service │
  └───┬────┘   └───┬────┘   └───┬────┘
      │            │            │
      └────────────┴────────────┘
           Independent Deploys
```

## Microservices Characteristics

```yaml
Single Responsibility:
  - En service = ett business domain
  - Loose coupling
  - High cohesion

Independent Deployment:
  - Deploy utan att påverka andra
  - Egen release cycle
  - A/B testing per service

Technology Freedom:
  - Välj rätt språk/framework
  - Python för ML, Go för performance
  - Egen databas

Decentralized Data:
  - Database per service
  - Ingen delad databas
  - Event-driven sync
```

## Service Communication

```yaml
Synchronous:
  REST:
    - HTTP/JSON
    - Enkelt, välkänt
    - Latency overhead

  gRPC:
    - Binary protocol
    - Snabbare
    - Type-safe (protobuf)

Asynchronous:
  Message Queue:
    - Fire-and-forget
    - Decoupled
    - Eventual consistency

  Event Streaming:
    - Kafka
    - Event sourcing
    - Real-time
```

## Service Discovery

```yaml
Client-Side Discovery:
  Client → Registry → Get address → Call service

  Tools: Eureka, Consul

Server-Side Discovery:
  Client → Load Balancer → Service
  LB queries registry internally

  Tools: Kubernetes, AWS ALB

DNS-Based:
  Client → DNS → IP → Service

  Tools: Route53, CoreDNS
```

```
┌────────────────────────────────────────────┐
│              Service Registry              │
│  ┌──────────────────────────────────────┐  │
│  │ users-service:                       │  │
│  │   - 10.0.0.1:8080                    │  │
│  │   - 10.0.0.2:8080                    │  │
│  │ orders-service:                      │  │
│  │   - 10.0.1.1:8080                    │  │
│  └──────────────────────────────────────┘  │
└────────────────────────────────────────────┘
         ▲                    │
         │ Register           │ Discover
         │                    ▼
    ┌─────────┐          ┌─────────┐
    │Service A│─────────►│Service B│
    └─────────┘          └─────────┘
```

## API Gateway Pattern

```yaml
API Gateway:
  - Single entry point
  - Authentication
  - Rate limiting
  - Request routing
  - Aggregation

Backend for Frontend (BFF):
  - Gateway per client type
  - Mobile BFF
  - Web BFF
  - Tailored APIs
```

## Circuit Breaker

```python
from circuitbreaker import circuit

class CircuitBreakerStates:
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject calls
    HALF_OPEN = "half_open"  # Testing recovery

@circuit(failure_threshold=5, recovery_timeout=30)
def call_external_service(user_id):
    response = requests.get(f"http://users-service/users/{user_id}")
    response.raise_for_status()
    return response.json()

# Usage
try:
    user = call_external_service(123)
except CircuitBreakerError:
    # Circuit is open, use fallback
    user = get_cached_user(123)
```

## Saga Pattern

```yaml
Problem:
  - Distributed transactions
  - No 2PC across services

Saga:
  - Sequence of local transactions
  - Compensating transactions on failure

Choreography:
  Service A → Event → Service B → Event → Service C

Orchestration:
  Saga Orchestrator coordinates all services
```

```
Order Saga (Choreography):

1. Order Service: Create order (pending)
         │
         ▼ OrderCreated event
2. Payment Service: Process payment
         │
         ├── PaymentSucceeded → 3. Inventory Service
         │                            │
         │                            ▼
         │                      ReserveStock
         │                            │
         │                      InventoryReserved → Complete order
         │
         └── PaymentFailed → Compensate: Cancel order
```

## Challenges

```yaml
Complexity:
  - Distributed systems are hard
  - More moving parts
  - Network failures

Data Consistency:
  - No ACID across services
  - Eventual consistency
  - Saga pattern

Testing:
  - Integration testing complex
  - Contract testing
  - Consumer-driven contracts

Debugging:
  - Distributed tracing
  - Correlation IDs
  - Centralized logging
```

| Pattern | Use Case |
|---------|----------|
| API Gateway | External traffic |
| Service Mesh | Internal traffic |
| Circuit Breaker | Fault tolerance |
| Saga | Distributed transactions |
| Event Sourcing | Audit, replay |

**Nästa steg:** Node 15 - API Design
''',
}

NODE_15_API_DESIGN = {
    "node_id": 15,
    "title": "API Design",
    "slug": "api-design",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [8],
    "content": '''# 🔌 API Design

## Varför detta är kritiskt
> "Ett dåligt API är som en dålig kontrakt - det skapar konflikter i åratal. Designa rätt från början, dokumentera allt."

## Vad du kommer lära dig
- ✅ REST principles och best practices
- ✅ HTTP status codes
- ✅ Pagination och rate limiting
- ✅ REST vs GraphQL vs gRPC

---

## REST Principles

```yaml
Resources:
  - Nouns, not verbs
  - /users, /orders, /products
  - Hierarchical: /users/123/orders

HTTP Methods:
  GET: Read
  POST: Create
  PUT: Replace
  PATCH: Partial update
  DELETE: Remove

Stateless:
  - Ingen server-side session
  - Varje request är komplett
  - Skalbar

HATEOAS:
  - Hypermedia as the Engine of Application State
  - Links i responses
  - Self-documenting
```

## REST API Design

```yaml
# Good URL design
GET    /users              # List users
GET    /users/123          # Get user
POST   /users              # Create user
PUT    /users/123          # Replace user
PATCH  /users/123          # Update user
DELETE /users/123          # Delete user

GET    /users/123/orders   # User's orders
POST   /users/123/orders   # Create order for user

# Query parameters
GET /users?status=active&sort=created_at&limit=10

# Bad examples
GET  /getUsers            # Verb i URL
POST /createUser          # Verb i URL
GET  /users/123/delete    # GET för delete
```

## Response Design

```python
# Success response
{
    "data": {
        "id": 123,
        "name": "John Doe",
        "email": "john@example.com"
    },
    "meta": {
        "request_id": "abc-123"
    }
}

# List with pagination
{
    "data": [...],
    "pagination": {
        "page": 1,
        "per_page": 20,
        "total": 100,
        "total_pages": 5
    },
    "links": {
        "self": "/users?page=1",
        "next": "/users?page=2",
        "last": "/users?page=5"
    }
}

# Error response
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid input",
        "details": [
            {
                "field": "email",
                "message": "Invalid email format"
            }
        ]
    },
    "meta": {
        "request_id": "abc-123"
    }
}
```

## HTTP Status Codes

```yaml
2xx Success:
  200: OK (general success)
  201: Created (POST success)
  204: No Content (DELETE success)

3xx Redirection:
  301: Moved Permanently
  304: Not Modified (caching)

4xx Client Errors:
  400: Bad Request (validation)
  401: Unauthorized (not authenticated)
  403: Forbidden (not authorized)
  404: Not Found
  409: Conflict
  422: Unprocessable Entity
  429: Too Many Requests

5xx Server Errors:
  500: Internal Server Error
  502: Bad Gateway
  503: Service Unavailable
  504: Gateway Timeout
```

## Versioning

```yaml
URL Path:
  /v1/users
  /v2/users

  + Enkelt, explicit
  - Bryter URL struktur

Header:
  Accept: application/vnd.api+json; version=1
  X-API-Version: 2

  + Ren URL
  - Svårare att testa

Query Parameter:
  /users?version=1

  + Enkelt
  - Förorenar query string
```

## Pagination

```python
# Offset-based (simple)
GET /users?offset=20&limit=10

def get_users(offset, limit):
    return db.query("SELECT * FROM users LIMIT ? OFFSET ?", limit, offset)
# Problem: Inkonsistent vid nya rows

# Cursor-based (better)
GET /users?cursor=abc123&limit=10

def get_users(cursor, limit):
    last_id = decode_cursor(cursor)
    users = db.query("""
        SELECT * FROM users
        WHERE id > ?
        ORDER BY id
        LIMIT ?
    """, last_id, limit)

    next_cursor = encode_cursor(users[-1].id)
    return {"data": users, "next_cursor": next_cursor}
```

## Rate Limiting

```yaml
Strategies:
  Fixed Window:
    - 100 requests per minute
    - Resets at minute boundary
    - Simple but bursty

  Sliding Window:
    - Smoother
    - More complex

  Token Bucket:
    - Tokens refill over time
    - Allows bursts
    - Flexible

Headers:
  X-RateLimit-Limit: 100
  X-RateLimit-Remaining: 45
  X-RateLimit-Reset: 1640000000
  Retry-After: 30
```

## GraphQL Alternative

```graphql
# Single endpoint
POST /graphql

# Query
query {
  user(id: 123) {
    name
    email
    orders(last: 5) {
      id
      total
    }
  }
}

# Benefits
# - Client specifies fields
# - Single request for related data
# - Strongly typed

# Drawbacks
# - Caching harder
# - N+1 queries
# - Complexity
```

| Style | Best For |
|-------|----------|
| REST | CRUD, simple APIs |
| GraphQL | Complex queries, mobile |
| gRPC | Internal services, performance |
| WebSocket | Real-time, bidirectional |

**Nästa steg:** Node 16 - Security
''',
}

NODE_16_SECURITY = {
    "node_id": 16,
    "title": "Security Design",
    "slug": "security",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [15],
    "content": '''# 🔒 Security Design

## Varför detta är kritiskt
> "Säkerhet är inte en feature - det är en grundförutsättning. Ett intrång kan döda ett företag. Defense in depth är din enda strategi."

## Vad du kommer lära dig
- ✅ Defense in depth
- ✅ Authentication (JWT, OAuth 2.0)
- ✅ Authorization (RBAC, ABAC)
- ✅ OWASP Top 10 och hur du undviker dem

---

## Defense in Depth

```
┌─────────────────────────────────────────────────────┐
│                    Network                          │
│  ┌───────────────────────────────────────────────┐  │
│  │               WAF / DDoS                      │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │           Load Balancer                 │  │  │
│  │  │  ┌───────────────────────────────────┐  │  │  │
│  │  │  │         API Gateway               │  │  │  │
│  │  │  │  ┌─────────────────────────────┐  │  │  │  │
│  │  │  │  │        Application          │  │  │  │  │
│  │  │  │  │  ┌───────────────────────┐  │  │  │  │  │
│  │  │  │  │  │      Database         │  │  │  │  │  │
│  │  │  │  │  └───────────────────────┘  │  │  │  │  │
│  │  │  │  └─────────────────────────────┘  │  │  │  │
│  │  │  └───────────────────────────────────┘  │  │  │
│  │  └─────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

## Authentication

```yaml
Password-Based:
  - Hash passwords (bcrypt, argon2)
  - Salt per user
  - Never store plain text

Token-Based:
  JWT:
    - Stateless
    - Self-contained
    - Expiration

  Opaque Tokens:
    - Server-side validation
    - Revocable
    - Database lookup

OAuth 2.0:
  - Third-party auth
  - Scopes
  - Flows: Authorization Code, Client Credentials

Multi-Factor:
  - Something you know (password)
  - Something you have (phone)
  - Something you are (biometric)
```

## JWT Security

```python
import jwt
from datetime import datetime, timedelta

SECRET_KEY = os.environ["JWT_SECRET"]

def create_token(user_id):
    payload = {
        "sub": user_id,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=1),
        "jti": str(uuid.uuid4())  # Unique token ID
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthError("Token expired")
    except jwt.InvalidTokenError:
        raise AuthError("Invalid token")
```

## Authorization

```yaml
RBAC (Role-Based):
  - User → Role → Permissions
  - Admin, Editor, Viewer

ABAC (Attribute-Based):
  - Policy-based
  - User attributes + Resource attributes + Context

ACL (Access Control List):
  - Per-resource permissions
  - User X can read Resource Y
```

```python
# RBAC implementation
ROLES = {
    "admin": ["read", "write", "delete", "admin"],
    "editor": ["read", "write"],
    "viewer": ["read"]
}

def has_permission(user, permission):
    user_roles = get_user_roles(user)
    for role in user_roles:
        if permission in ROLES.get(role, []):
            return True
    return False

@require_permission("write")
def update_resource(resource_id, data):
    # User must have "write" permission
    pass
```

## Encryption

```yaml
At Rest:
  - Database encryption
  - Disk encryption
  - Key management (KMS)

In Transit:
  - TLS 1.3
  - Certificate management
  - mTLS for service-to-service

Application-Level:
  - Encrypt sensitive fields
  - PII protection
  - Key rotation
```

## Common Vulnerabilities

```yaml
OWASP Top 10:

1. Injection (SQL, NoSQL):
   ❌ query = f"SELECT * FROM users WHERE id = {user_input}"
   ✅ query = "SELECT * FROM users WHERE id = ?"

2. Broken Authentication:
   - Weak passwords
   - Session fixation
   - Missing brute-force protection

3. XSS (Cross-Site Scripting):
   - Sanitize output
   - Content-Security-Policy
   - HttpOnly cookies

4. CSRF (Cross-Site Request Forgery):
   - CSRF tokens
   - SameSite cookies

5. Broken Access Control:
   - Verify authorization per request
   - Don't trust client-side
```

## Security Headers

```nginx
# NGINX security headers
add_header X-Content-Type-Options nosniff;
add_header X-Frame-Options DENY;
add_header X-XSS-Protection "1; mode=block";
add_header Content-Security-Policy "default-src 'self'";
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
add_header Referrer-Policy "strict-origin-when-cross-origin";
```

## Secrets Management

```yaml
Dont:
  - Hardcoded secrets
  - Secrets in git
  - Secrets in logs

Do:
  - Environment variables
  - Secrets manager (Vault, AWS SM)
  - Encrypted config

Vault Example:
  1. App authenticates to Vault
  2. Gets short-lived credentials
  3. Vault rotates secrets automatically
```

| Layer | Security Measure |
|-------|------------------|
| Network | Firewall, VPN, WAF |
| Transport | TLS, mTLS |
| Application | Auth, AuthZ, Input validation |
| Data | Encryption at rest |
| Operations | Audit logs, monitoring |

**Nästa steg:** Node 17 - Rate Limiting & Throttling
''',
}

SYSTEM_DESIGN_BLOCK_4 = [
    NODE_13_QUEUES,
    NODE_14_MICROSERVICES,
    NODE_15_API_DESIGN,
    NODE_16_SECURITY,
]
