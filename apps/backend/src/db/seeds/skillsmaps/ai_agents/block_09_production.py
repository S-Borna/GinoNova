"""
AI Agents SkillsMap - Block 09: Production
Nodes 17-18: Deployment, Monitoring & Observability
"""

BLOCK_09_NODES = [
    {
        "id": "ai-agents-17",
        "slug": "agent-production-deployment",
        "title": "Production Deployment",
        "order_index": 17,
        "estimated_minutes": 45,
        "xp_reward": 120,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["ai-agents-16"],
        "content": """# Agent Production Deployment

## Varför detta är viktigt

Att bygga en agent som fungerar lokalt är lätt. Att deploya den till produktion
med tusentals användare, hög tillgänglighet och rimliga kostnader — det är svårt.

Denna modul täcker allt du behöver för att ta din agent från laptop till prod.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Designa skalbar agent-arkitektur
- ✅ Implementera rate limiting och cost controls
- ✅ Hantera concurrent requests
- ✅ Bygga för high availability
- ✅ Implementera graceful degradation

## Kärnkoncept

### Production Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   PRODUCTION AGENT ARCHITECTURE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                          LOAD BALANCER                                │   │
│  │                    (nginx / AWS ALB / CloudFlare)                     │   │
│  └───────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│  ┌───────────────────────────────▼──────────────────────────────────────┐   │
│  │                          API GATEWAY                                  │   │
│  │  • Authentication        • Rate Limiting       • Request Validation  │   │
│  └───────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│  ┌───────────────────────────────▼──────────────────────────────────────┐   │
│  │                       AGENT SERVICE (Replicated)                      │   │
│  │  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐            │   │
│  │  │  Agent 1  │ │  Agent 2  │ │  Agent 3  │ │  Agent N  │            │   │
│  │  │  (Pod)    │ │  (Pod)    │ │  (Pod)    │ │  (Pod)    │            │   │
│  │  └─────┬─────┘ └─────┬─────┘ └─────┬─────┘ └─────┬─────┘            │   │
│  │        └─────────────┴─────────────┴─────────────┘                   │   │
│  │                              │                                        │   │
│  └──────────────────────────────┼───────────────────────────────────────┘   │
│                                 │                                            │
│        ┌────────────────────────┼────────────────────────┐                  │
│        ▼                        ▼                        ▼                  │
│  ┌───────────────┐       ┌───────────────┐       ┌───────────────┐         │
│  │    Redis      │       │   Postgres    │       │  Vector DB    │         │
│  │  (Sessions,   │       │  (User data,  │       │  (Embeddings, │         │
│  │   Cache)      │       │   Logs)       │       │   RAG)        │         │
│  └───────────────┘       └───────────────┘       └───────────────┘         │
│                                                                              │
│  External APIs:                                                              │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐                   │
│  │   OpenAI      │  │   Anthropic   │  │  Tool APIs    │                   │
│  │   (LLM)       │  │   (Fallback)  │  │  (Integrations)│                  │
│  └───────────────┘  └───────────────┘  └───────────────┘                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Deployment Patterns

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT PATTERNS                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. STATELESS AGENTS (Recommended)                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • State stored externally (Redis/DB)                               │   │
│  │  • Any instance can handle any request                              │   │
│  │  • Easy horizontal scaling                                          │   │
│  │  • Simple failover                                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  2. QUEUE-BASED PROCESSING                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Request ──► Queue ──► Worker Pool ──► Response                     │   │
│  │              (RabbitMQ/SQS)                                         │   │
│  │                                                                      │   │
│  │  Benefits:                                                          │   │
│  │  • Handles burst traffic                                            │   │
│  │  • Natural rate limiting                                            │   │
│  │  • Retry built-in                                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  3. STREAMING RESPONSES                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Request ──► Agent ══► SSE/WebSocket ══► Client                    │   │
│  │                   (streaming tokens)                                │   │
│  │                                                                      │   │
│  │  Benefits:                                                          │   │
│  │  • Better UX (immediate feedback)                                   │   │
│  │  • Lower perceived latency                                          │   │
│  │  • Can cancel mid-response                                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Production Setup

### 1. Stateless Agent Service

```python
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import redis.asyncio as redis
import json
import uuid
from typing import AsyncGenerator

app = FastAPI()

# External state store
redis_client = redis.from_url("redis://localhost:6379")

class ChatRequest(BaseModel):
    session_id: str
    message: str

class AgentService:
    \"\"\"Stateless agent service.\"\"\"

    def __init__(self):
        from openai import AsyncOpenAI
        self.client = AsyncOpenAI()

    async def get_session_state(self, session_id: str) -> dict:
        \"\"\"Load state from Redis.\"\"\"
        data = await redis_client.get(f"session:{session_id}")
        if data:
            return json.loads(data)
        return {"messages": [], "context": {}}

    async def save_session_state(self, session_id: str, state: dict):
        \"\"\"Save state to Redis with TTL.\"\"\"
        await redis_client.setex(
            f"session:{session_id}",
            3600,  # 1 hour TTL
            json.dumps(state)
        )

    async def process_message(
        self,
        session_id: str,
        message: str
    ) -> AsyncGenerator[str, None]:
        \"\"\"Process message and stream response.\"\"\"
        # Load state
        state = await self.get_session_state(session_id)

        # Add user message
        state["messages"].append({"role": "user", "content": message})

        # Prepare messages for LLM
        messages = [
            {"role": "system", "content": "You are a helpful DevOps assistant."},
            *state["messages"][-10:]  # Last 10 messages
        ]

        # Stream response
        full_response = ""
        async for chunk in await self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True
        ):
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                full_response += content
                yield content

        # Save updated state
        state["messages"].append({"role": "assistant", "content": full_response})
        await self.save_session_state(session_id, state)

agent_service = AgentService()

@app.post("/chat")
async def chat(request: ChatRequest):
    \"\"\"Non-streaming chat endpoint.\"\"\"
    response_parts = []
    async for chunk in agent_service.process_message(
        request.session_id,
        request.message
    ):
        response_parts.append(chunk)

    return {"response": "".join(response_parts)}

@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    \"\"\"Streaming chat endpoint.\"\"\"
    async def generate():
        async for chunk in agent_service.process_message(
            request.session_id,
            request.message
        ):
            yield f"data: {json.dumps({'content': chunk})}\\n\\n"
        yield "data: [DONE]\\n\\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )
```

### 2. Rate Limiting

```python
from fastapi import Request, HTTPException
from datetime import datetime, timedelta
import asyncio

class RateLimiter:
    \"\"\"Token bucket rate limiter with Redis backend.\"\"\"

    def __init__(
        self,
        requests_per_minute: int = 60,
        tokens_per_minute: int = 100000  # LLM tokens
    ):
        self.requests_per_minute = requests_per_minute
        self.tokens_per_minute = tokens_per_minute

    async def check_rate_limit(self, user_id: str) -> dict:
        \"\"\"Check if user is within rate limits.\"\"\"
        key = f"ratelimit:{user_id}"
        now = datetime.now().timestamp()
        window_start = now - 60

        # Get current usage
        pipe = redis_client.pipeline()
        pipe.zremrangebyscore(key, 0, window_start)  # Remove old entries
        pipe.zcard(key)  # Count entries in window
        pipe.get(f"tokens:{user_id}")  # Get token usage

        results = await pipe.execute()
        request_count = results[1]
        token_usage = int(results[2] or 0)

        if request_count >= self.requests_per_minute:
            return {
                "allowed": False,
                "reason": "Request rate limit exceeded",
                "retry_after": 60
            }

        if token_usage >= self.tokens_per_minute:
            return {
                "allowed": False,
                "reason": "Token rate limit exceeded",
                "retry_after": 60
            }

        # Record this request
        await redis_client.zadd(key, {str(now): now})
        await redis_client.expire(key, 120)

        return {
            "allowed": True,
            "remaining_requests": self.requests_per_minute - request_count - 1,
            "remaining_tokens": self.tokens_per_minute - token_usage
        }

    async def record_token_usage(self, user_id: str, tokens: int):
        \"\"\"Record token usage.\"\"\"
        key = f"tokens:{user_id}"
        await redis_client.incrby(key, tokens)
        await redis_client.expire(key, 60)

rate_limiter = RateLimiter()

# Middleware
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    user_id = request.headers.get("X-User-ID", "anonymous")

    result = await rate_limiter.check_rate_limit(user_id)

    if not result["allowed"]:
        raise HTTPException(
            status_code=429,
            detail=result["reason"],
            headers={"Retry-After": str(result["retry_after"])}
        )

    response = await call_next(request)

    # Add rate limit headers
    response.headers["X-RateLimit-Remaining"] = str(result.get("remaining_requests", 0))

    return response
```

### 3. Cost Controls

```python
from dataclasses import dataclass
from typing import Optional
import tiktoken

@dataclass
class CostConfig:
    input_cost_per_1k: float = 0.0015  # GPT-4o-mini input
    output_cost_per_1k: float = 0.0060  # GPT-4o-mini output
    max_input_tokens: int = 8000
    max_output_tokens: int = 4000
    daily_budget_usd: float = 100.0

class CostController:
    \"\"\"Control and track LLM costs.\"\"\"

    def __init__(self, config: CostConfig = None):
        self.config = config or CostConfig()
        self.encoder = tiktoken.encoding_for_model("gpt-4o-mini")

    def estimate_cost(self, messages: list[dict], max_output: int = None) -> dict:
        \"\"\"Estimate cost before making a call.\"\"\"
        input_tokens = sum(
            len(self.encoder.encode(m["content"]))
            for m in messages
        )

        max_output = max_output or self.config.max_output_tokens

        input_cost = (input_tokens / 1000) * self.config.input_cost_per_1k
        max_output_cost = (max_output / 1000) * self.config.output_cost_per_1k

        return {
            "input_tokens": input_tokens,
            "max_output_tokens": max_output,
            "estimated_min_cost": input_cost,
            "estimated_max_cost": input_cost + max_output_cost
        }

    async def check_budget(self, user_id: str, estimated_cost: float) -> bool:
        \"\"\"Check if user has budget for this request.\"\"\"
        key = f"daily_cost:{user_id}:{datetime.now().strftime('%Y-%m-%d')}"
        current_cost = float(await redis_client.get(key) or 0)

        return (current_cost + estimated_cost) <= self.config.daily_budget_usd

    async def record_cost(self, user_id: str, input_tokens: int, output_tokens: int):
        \"\"\"Record actual cost after request.\"\"\"
        cost = (
            (input_tokens / 1000) * self.config.input_cost_per_1k +
            (output_tokens / 1000) * self.config.output_cost_per_1k
        )

        key = f"daily_cost:{user_id}:{datetime.now().strftime('%Y-%m-%d')}"
        await redis_client.incrbyfloat(key, cost)
        await redis_client.expire(key, 86400 * 2)  # Keep 2 days

        return cost

cost_controller = CostController()
```

### 4. Kubernetes Deployment

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: agent-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: agent-service
  template:
    metadata:
      labels:
        app: agent-service
    spec:
      containers:
      - name: agent
        image: your-registry/agent-service:latest
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: agent-secrets
              key: openai-api-key
        - name: REDIS_URL
          value: "redis://redis-service:6379"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: agent-service
spec:
  selector:
    app: agent-service
  ports:
  - port: 80
    targetPort: 8000
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: agent-service-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: agent-service
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### 5. Health Checks

```python
from fastapi import FastAPI
from datetime import datetime

@app.get("/health")
async def health():
    \"\"\"Liveness probe.\"\"\"
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/ready")
async def ready():
    \"\"\"Readiness probe.\"\"\"
    checks = {
        "redis": await check_redis(),
        "openai": await check_openai()
    }

    all_healthy = all(checks.values())

    if not all_healthy:
        raise HTTPException(status_code=503, detail=checks)

    return {"status": "ready", "checks": checks}

async def check_redis() -> bool:
    try:
        await redis_client.ping()
        return True
    except:
        return False

async def check_openai() -> bool:
    try:
        # Light check - just verify API key works
        from openai import AsyncOpenAI
        client = AsyncOpenAI()
        await client.models.list()
        return True
    except:
        return False
```

## Vanliga problem

### Problem: "High latency under load"

```python
# Lösning: Connection pooling och async
import httpx

class OptimizedLLMClient:
    def __init__(self):
        self.client = httpx.AsyncClient(
            limits=httpx.Limits(
                max_connections=100,
                max_keepalive_connections=20
            ),
            timeout=httpx.Timeout(60.0)
        )
```

### Problem: "Costs spiraling out of control"

```python
# Lösning: Hard limits och alerts
async def enforce_hard_limit(user_id: str, estimated_cost: float):
    if estimated_cost > 1.0:  # $1 per request max
        raise HTTPException(400, "Request too expensive")

    daily_total = await get_daily_cost(user_id)
    if daily_total > 50:  # $50/day max
        raise HTTPException(429, "Daily budget exceeded")
```

## Praktisk övning

**Uppgift:** Implementera Graceful Degradation

```python
\"\"\"
TODO: Bygg ett fallback-system som:

1. Primär: GPT-4o för komplexa queries
2. Fallback 1: GPT-4o-mini om GPT-4o är nere/slow
3. Fallback 2: Cached responses om alla LLMs är nere
4. Fallback 3: "Vi upplever problem" message

Implementera:
- CircuitBreaker för varje provider
- Automatic failover
- Cost-aware routing (billigare modell om budget låg)
\"\"\"

class ResilientAgent:
    def __init__(self):
        # Din kod här
        pass

    async def chat(self, message: str, user_id: str) -> str:
        # Din kod här
        pass

# Test
agent = ResilientAgent()
# Ska fungera även om OpenAI är nere
response = await agent.chat("Hello", "user_123")
```

## Sammanfattning

- ✅ **Stateless design** för enkel skalning
- ✅ **Rate limiting** för kostnadskontroll
- ✅ **Health checks** för K8s integration
- ✅ **Graceful degradation** för resiliens

## Nästa steg

- **Node 18:** Monitoring & Observability
- **Node 19:** Autonomous Agents

---
*Pro tip: Börja med rate limiting DAG 1 — det är svårare att lägga till senare!*
"""
    },
    {
        "id": "ai-agents-18",
        "slug": "agent-monitoring-observability",
        "title": "Monitoring & Observability",
        "order_index": 18,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["ai-agents-17"],
        "content": """# Agent Monitoring & Observability

## Varför detta är viktigt

Agenter är som black boxes — utan ordentlig observability vet du inte:

- **Varför** agenten tog ett visst beslut
- **Hur mycket** det kostade
- **Var** bottlenecks finns
- **När** något börjar gå fel

God observability gör skillnaden mellan "det funkar inte" och "jag vet exakt vad som är fel".

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Implementera structured logging för agenter
- ✅ Bygga metrics dashboards
- ✅ Tracing för multi-agent systems
- ✅ Alerting för anomalier
- ✅ Cost tracking och reporting

## Kärnkoncept

### Observability Stack

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OBSERVABILITY STACK                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                           AGENT                                       │   │
│  │  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐              │   │
│  │  │    LOGS       │ │    METRICS    │ │    TRACES     │              │   │
│  │  │  (Structured) │ │  (Counters,   │ │  (Distributed)│              │   │
│  │  │               │ │   Gauges)     │ │               │              │   │
│  │  └───────┬───────┘ └───────┬───────┘ └───────┬───────┘              │   │
│  └──────────┼─────────────────┼─────────────────┼────────────────────────┘   │
│             │                 │                 │                            │
│             ▼                 ▼                 ▼                            │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐                    │
│  │    Loki /     │  │  Prometheus   │  │    Jaeger /   │                    │
│  │  Elasticsearch│  │               │  │    Tempo      │                    │
│  └───────┬───────┘  └───────┬───────┘  └───────┬───────┘                    │
│          │                  │                  │                             │
│          └──────────────────┴──────────────────┘                             │
│                             │                                                │
│                             ▼                                                │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                         GRAFANA                                       │   │
│  │  ┌───────────────────────────────────────────────────────────────┐   │   │
│  │  │  • Agent Performance Dashboard                                │   │   │
│  │  │  • Cost Tracking Dashboard                                    │   │   │
│  │  │  • Error Rate Alerts                                          │   │   │
│  │  │  • Token Usage Graphs                                         │   │   │
│  │  └───────────────────────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Metrics

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    KEY AGENT METRICS                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  LATENCY METRICS                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • agent_response_time_seconds (histogram)                          │   │
│  │  • llm_request_duration_seconds (histogram)                         │   │
│  │  • tool_execution_duration_seconds (histogram)                      │   │
│  │  • time_to_first_token_seconds (histogram)                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  COST METRICS                                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • llm_input_tokens_total (counter)                                 │   │
│  │  • llm_output_tokens_total (counter)                                │   │
│  │  • estimated_cost_usd_total (counter)                               │   │
│  │  • cost_per_conversation (histogram)                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ERROR METRICS                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • agent_errors_total (counter, by type)                            │   │
│  │  • llm_request_failures_total (counter, by error)                   │   │
│  │  • tool_execution_errors_total (counter, by tool)                   │   │
│  │  • rate_limit_hits_total (counter)                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  USAGE METRICS                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • active_sessions (gauge)                                          │   │
│  │  • messages_per_session (histogram)                                 │   │
│  │  • tool_calls_per_request (histogram)                               │   │
│  │  • conversations_completed_total (counter)                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Implementera Observability

### 1. Structured Logging

```python
import structlog
from datetime import datetime
import json
from typing import Any

# Configure structlog
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory()
)

logger = structlog.get_logger()

class AgentLogger:
    \"\"\"Structured logging for agent interactions.\"\"\"

    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.log = logger.bind(agent_id=agent_id)

    def log_request(self, session_id: str, message: str, metadata: dict = None):
        self.log.info(
            "agent_request_received",
            session_id=session_id,
            message_length=len(message),
            message_preview=message[:100],
            **(metadata or {})
        )

    def log_llm_call(
        self,
        session_id: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        duration_ms: float,
        cost_usd: float
    ):
        self.log.info(
            "llm_call_completed",
            session_id=session_id,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
            duration_ms=duration_ms,
            cost_usd=cost_usd
        )

    def log_tool_call(
        self,
        session_id: str,
        tool_name: str,
        success: bool,
        duration_ms: float,
        error: str = None
    ):
        level = "info" if success else "error"
        getattr(self.log, level)(
            "tool_call_completed",
            session_id=session_id,
            tool_name=tool_name,
            success=success,
            duration_ms=duration_ms,
            error=error
        )

    def log_response(
        self,
        session_id: str,
        response_length: int,
        total_duration_ms: float,
        tool_calls: int,
        llm_calls: int
    ):
        self.log.info(
            "agent_response_sent",
            session_id=session_id,
            response_length=response_length,
            total_duration_ms=total_duration_ms,
            tool_calls=tool_calls,
            llm_calls=llm_calls
        )

    def log_error(
        self,
        session_id: str,
        error_type: str,
        error_message: str,
        stack_trace: str = None
    ):
        self.log.error(
            "agent_error",
            session_id=session_id,
            error_type=error_type,
            error_message=error_message,
            stack_trace=stack_trace
        )

# Usage
agent_logger = AgentLogger("devops-agent-1")

agent_logger.log_request("sess_123", "Deploy auth-service to prod")
agent_logger.log_llm_call(
    session_id="sess_123",
    model="gpt-4o-mini",
    input_tokens=500,
    output_tokens=200,
    duration_ms=1200,
    cost_usd=0.003
)
```

### 2. Prometheus Metrics

```python
from prometheus_client import Counter, Histogram, Gauge, generate_latest
from fastapi import Response

# Define metrics
AGENT_REQUEST_DURATION = Histogram(
    'agent_request_duration_seconds',
    'Time spent processing agent requests',
    ['agent_id', 'status'],
    buckets=[0.1, 0.5, 1, 2, 5, 10, 30, 60]
)

LLM_TOKENS = Counter(
    'llm_tokens_total',
    'Total LLM tokens used',
    ['agent_id', 'model', 'token_type']  # input/output
)

LLM_COST = Counter(
    'llm_cost_usd_total',
    'Total LLM cost in USD',
    ['agent_id', 'model']
)

TOOL_CALLS = Counter(
    'tool_calls_total',
    'Total tool calls',
    ['agent_id', 'tool_name', 'status']  # success/failure
)

ACTIVE_SESSIONS = Gauge(
    'active_sessions',
    'Number of active sessions',
    ['agent_id']
)

ERROR_COUNT = Counter(
    'agent_errors_total',
    'Total agent errors',
    ['agent_id', 'error_type']
)

class MetricsCollector:
    \"\"\"Collect and expose Prometheus metrics.\"\"\"

    def __init__(self, agent_id: str):
        self.agent_id = agent_id

    def record_request(self, duration: float, status: str):
        AGENT_REQUEST_DURATION.labels(
            agent_id=self.agent_id,
            status=status
        ).observe(duration)

    def record_llm_usage(
        self,
        model: str,
        input_tokens: int,
        output_tokens: int,
        cost: float
    ):
        LLM_TOKENS.labels(
            agent_id=self.agent_id,
            model=model,
            token_type="input"
        ).inc(input_tokens)

        LLM_TOKENS.labels(
            agent_id=self.agent_id,
            model=model,
            token_type="output"
        ).inc(output_tokens)

        LLM_COST.labels(
            agent_id=self.agent_id,
            model=model
        ).inc(cost)

    def record_tool_call(self, tool_name: str, success: bool):
        TOOL_CALLS.labels(
            agent_id=self.agent_id,
            tool_name=tool_name,
            status="success" if success else "failure"
        ).inc()

    def set_active_sessions(self, count: int):
        ACTIVE_SESSIONS.labels(agent_id=self.agent_id).set(count)

    def record_error(self, error_type: str):
        ERROR_COUNT.labels(
            agent_id=self.agent_id,
            error_type=error_type
        ).inc()

# Endpoint for Prometheus to scrape
@app.get("/metrics")
async def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )
```

### 3. Distributed Tracing

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# Setup tracer
trace.set_tracer_provider(TracerProvider())
jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

tracer = trace.get_tracer(__name__)

# Instrument FastAPI
FastAPIInstrumentor.instrument_app(app)

class TracedAgent:
    \"\"\"Agent with distributed tracing.\"\"\"

    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.tracer = trace.get_tracer(f"agent.{agent_id}")

    async def process_message(self, session_id: str, message: str):
        with self.tracer.start_as_current_span("process_message") as span:
            span.set_attribute("session_id", session_id)
            span.set_attribute("message_length", len(message))

            # Think step
            with self.tracer.start_span("think") as think_span:
                decision = await self._think(message)
                think_span.set_attribute("decision", decision["action"])

            # Tool execution
            if decision["action"] == "use_tool":
                with self.tracer.start_span("execute_tool") as tool_span:
                    tool_span.set_attribute("tool", decision["tool"])
                    result = await self._execute_tool(decision["tool"], decision["args"])
                    tool_span.set_attribute("success", result["success"])

            # Generate response
            with self.tracer.start_span("generate_response") as resp_span:
                response = await self._generate_response(decision)
                resp_span.set_attribute("response_length", len(response))

            return response
```

### 4. Dashboard (Grafana JSON)

```json
{
  "dashboard": {
    "title": "Agent Monitoring",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(agent_request_duration_seconds_count[5m])",
            "legendFormat": "{{agent_id}}"
          }
        ]
      },
      {
        "title": "Response Time (p95)",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(agent_request_duration_seconds_bucket[5m]))",
            "legendFormat": "p95"
          }
        ]
      },
      {
        "title": "Daily Cost",
        "type": "stat",
        "targets": [
          {
            "expr": "sum(increase(llm_cost_usd_total[24h]))",
            "legendFormat": "Cost (USD)"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(agent_errors_total[5m])",
            "legendFormat": "{{error_type}}"
          }
        ],
        "alert": {
          "conditions": [
            {
              "evaluator": {"type": "gt", "params": [0.1]},
              "operator": {"type": "and"},
              "query": {"params": ["A", "5m", "now"]}
            }
          ]
        }
      },
      {
        "title": "Token Usage by Model",
        "type": "piechart",
        "targets": [
          {
            "expr": "sum(increase(llm_tokens_total[24h])) by (model)",
            "legendFormat": "{{model}}"
          }
        ]
      }
    ]
  }
}
```

### 5. Alerting Rules

```yaml
# prometheus-rules.yaml
groups:
  - name: agent-alerts
    rules:
      - alert: HighErrorRate
        expr: rate(agent_errors_total[5m]) > 0.1
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "High error rate detected"
          description: "Agent {{ $labels.agent_id }} has error rate > 10%"

      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(agent_request_duration_seconds_bucket[5m])) > 10
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High latency detected"
          description: "p95 latency > 10s for agent {{ $labels.agent_id }}"

      - alert: DailyCostExceeded
        expr: sum(increase(llm_cost_usd_total[24h])) > 100
        labels:
          severity: critical
        annotations:
          summary: "Daily cost limit exceeded"
          description: "Daily LLM cost exceeded $100"

      - alert: LLMServiceDown
        expr: up{job="llm-proxy"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "LLM service is down"
```

## Praktisk övning

**Uppgift:** Bygg ett Custom Dashboard

```python
\"\"\"
TODO: Bygg en real-time monitoring dashboard med:

1. Metrics endpoint som returnerar:
   - Current active sessions
   - Requests per minute
   - Average response time
   - Error rate
   - Cost per hour

2. WebSocket endpoint för real-time updates

3. Health score beräkning:
   health_score = 100 - (error_rate * 50) - (p95_latency_penalty)
\"\"\"

from fastapi import WebSocket

class AgentDashboard:
    def __init__(self, metrics: MetricsCollector):
        # Din kod här
        pass

    async def get_dashboard_data(self) -> dict:
        # Din kod här
        pass

    async def stream_updates(self, websocket: WebSocket):
        # Din kod här
        pass

    def calculate_health_score(self) -> float:
        # Din kod här
        pass

# Mount on FastAPI
dashboard = AgentDashboard(metrics_collector)

@app.get("/dashboard")
async def dashboard_data():
    return await dashboard.get_dashboard_data()
```

## Sammanfattning

- ✅ **Structured logging** med context
- ✅ **Prometheus metrics** för alla key indicators
- ✅ **Distributed tracing** för debugging
- ✅ **Grafana dashboards** för visualization
- ✅ **Alerting** för proaktiv monitoring

## Nästa steg

- **Node 19:** Autonomous Agents
- **Node 20:** Future of AI Agents

---
*Pro tip: Log ALLT i början — du kan alltid filtrera senare, men du kan inte logga det du missade!*
"""
    }
]
