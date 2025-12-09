# =============================================================================
# AI AGENTS - BLOCK 09: PRODUCTION (Noder 17-18) - V3 FORMAT
# =============================================================================

NODE_17_DEPLOYMENT = {
    "node_id": 17,
    "title": "Agent Deployment",
    "slug": "agent-deployment",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": [16],
    "content": '''
# Agent Deployment

Deploya AI-agenter till produktion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Agent Deployment?

Deployment ar processen att ta en agent fran utveckling till produktion. Det inkluderar containerisering, skalning och sakerhet.

| Steg | Beskrivning |
|------|-------------|
| Containerize | Packa agent i Docker |
| Configure | Miljövariabler, secrets |
| Deploy | Kubernetes, serverless |
| Scale | Auto-scaling policies |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Tillganglighet | Agents maste vara uppe |
| Skalbarhet | Hantera last-toppar |
| Sakerhet | Skydda API-nycklar |
| Kostnad | Optimera resurser |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Deployment Options

| Platform | Bast for | Komplexitet |
|----------|----------|-------------|
| Docker + K8s | Full kontroll | Hog |
| AWS Lambda | Serverless | Medium |
| Cloud Run | Container serverless | Lag |
| Modal | ML-fokuserat | Lag |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  PRODUCTION ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                    LOAD BALANCER                           │ │
│  └───────────────────────────────────────────────────────────┘ │
│                           │                                      │
│           ┌───────────────┼───────────────┐                     │
│           v               v               v                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  API POD 1  │  │  API POD 2  │  │  API POD N  │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│           │               │               │                      │
│           └───────────────┼───────────────┘                     │
│                           v                                      │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                    MESSAGE QUEUE                           │ │
│  │                  (Redis / RabbitMQ)                        │ │
│  └───────────────────────────────────────────────────────────┘ │
│                           │                                      │
│           ┌───────────────┼───────────────┐                     │
│           v               v               v                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ AGENT POD 1 │  │ AGENT POD 2 │  │ AGENT POD N │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                           │                                      │
│                           v                                      │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                   EXTERNAL SERVICES                        │ │
│  │          OpenAI / Anthropic / Vector DB / etc              │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dockerfile

```dockerfile
# Dockerfile for AI Agent
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY src/ ./src/
COPY config/ ./config/

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Run
ENV PYTHONUNBUFFERED=1
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## FastAPI Application

```python
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI(title="AI Agent Service")

# Configuration
class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    max_concurrent_tasks: int = int(os.getenv("MAX_CONCURRENT_TASKS", "10"))
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379")

settings = Settings()

# Request/Response models
class AgentRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    max_iterations: int = 10

class AgentResponse(BaseModel):
    response: str
    session_id: str
    iterations: int
    tokens_used: int

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

# Agent endpoint
@app.post("/agent/run", response_model=AgentResponse)
async def run_agent(request: AgentRequest, background_tasks: BackgroundTasks):
    from src.agent import Agent

    agent = Agent(api_key=settings.openai_api_key)
    result = await agent.run(
        message=request.message,
        session_id=request.session_id,
        max_iterations=request.max_iterations
    )

    # Log usage in background
    background_tasks.add_task(log_usage, result)

    return AgentResponse(
        response=result["output"],
        session_id=result["session_id"],
        iterations=result["iterations"],
        tokens_used=result["tokens"]
    )

async def log_usage(result: dict):
    # Logga till metrics system
    pass
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kubernetes Deployment

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-agent
  labels:
    app: ai-agent
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-agent
  template:
    metadata:
      labels:
        app: ai-agent
    spec:
      containers:
      - name: agent
        image: ai-agent:latest
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: agent-secrets
              key: openai-api-key
        - name: REDIS_URL
          value: "redis://redis:6379"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 30
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: ai-agent-service
spec:
  selector:
    app: ai-agent
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ai-agent-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ai-agent
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Secrets Management

```python
# secrets.py
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class SecretManager:
    """Hantera hemligheter sakert."""

    @staticmethod
    def get_secret(name: str, default: str = None) -> Optional[str]:
        # 1. Forst kolla miljovariabel
        value = os.getenv(name)
        if value:
            return value

        # 2. Sedan kolla fil (for Docker secrets)
        secret_path = f"/run/secrets/{name.lower()}"
        if os.path.exists(secret_path):
            with open(secret_path, "r") as f:
                return f.read().strip()

        # 3. Slutligen, returnera default
        return default

    @staticmethod
    def validate_required_secrets() -> None:
        required = ["OPENAI_API_KEY"]
        missing = [s for s in required if not SecretManager.get_secret(s)]

        if missing:
            raise ValueError(f"Missing required secrets: {missing}")

# Vid startup
SecretManager.validate_required_secrets()
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Rate Limiting

```python
from fastapi import HTTPException, Request
from functools import wraps
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, requests_per_minute: int = 60):
        self.rpm = requests_per_minute
        self.requests = defaultdict(list)

    def check(self, client_id: str) -> bool:
        now = time.time()
        minute_ago = now - 60

        # Rensa gamla requests
        self.requests[client_id] = [
            t for t in self.requests[client_id]
            if t > minute_ago
        ]

        if len(self.requests[client_id]) >= self.rpm:
            return False

        self.requests[client_id].append(now)
        return True

rate_limiter = RateLimiter(requests_per_minute=60)

def rate_limit():
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            client_id = request.client.host

            if not rate_limiter.check(client_id):
                raise HTTPException(
                    status_code=429,
                    detail="Rate limit exceeded"
                )

            return await func(request, *args, **kwargs)
        return wrapper
    return decorator
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Cold start | Ingen warmup | Preload models |
| OOM | For lite minne | Resource limits |
| API key leak | Dalig secret handling | Secret manager |
| Scaling lag | Langsam HPA | Custom metrics |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Containerize | Docker for portabilitet |
| Kubernetes | Orchestrering i skala |
| Secrets | Aldrig i kod eller images |
| Rate limit | Skydda mot overbelastning |

Kom ihag:
- Health checks ar kritiska
- Secrets aldrig i plain text
- HPA for automatisk skalning
- Logg allt for debugging
'''
}

NODE_18_MONITORING = {
    "node_id": 18,
    "title": "Agent Monitoring",
    "slug": "agent-monitoring",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [17],
    "content": '''
# Agent Monitoring

Overvaka och optimera AI-agenter i produktion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Agent Monitoring?

Monitoring ar processen att samla in, analysera och agera pa data om agentens beteende och prestanda.

| Aspekt | Exempel |
|--------|---------|
| Performance | Latency, throughput |
| Cost | Tokens, API calls |
| Quality | Accuracy, relevance |
| Health | Errors, uptime |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Aspekt | Beskrivning |
|--------|-------------|
| Visibility | Forsta vad som hander |
| Alerting | Snabb reaktion pa problem |
| Optimization | Hitta flaskhalsar |
| Cost control | Spara API-kostnader |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Key Metrics

| Metric | Typ | Alert threshold |
|--------|-----|-----------------|
| Response time | Performance | > 5s |
| Error rate | Health | > 1% |
| Token usage | Cost | > budget |
| Iterations | Quality | > max |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Monitoring Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  MONITORING ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                    AI AGENT                                │ │
│  │  ┌─────────────────────────────────────────────────────┐  │ │
│  │  │  Instrumentation (metrics, logs, traces)            │  │ │
│  │  └─────────────────────────────────────────────────────┘  │ │
│  └───────────────────────────────────────────────────────────┘ │
│           │                   │                   │              │
│           v                   v                   v              │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐       │
│  │  METRICS    │     │    LOGS     │     │   TRACES    │       │
│  │ Prometheus  │     │    Loki     │     │   Jaeger    │       │
│  └─────────────┘     └─────────────┘     └─────────────┘       │
│           │                   │                   │              │
│           └───────────────────┼───────────────────┘             │
│                               v                                  │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                      GRAFANA                               │ │
│  │  Dashboards | Alerts | Correlations                       │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Metrics Collection

```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server
import time
from functools import wraps

# Define metrics
AGENT_REQUESTS = Counter(
    "agent_requests_total",
    "Total agent requests",
    ["agent_name", "status"]
)

AGENT_LATENCY = Histogram(
    "agent_latency_seconds",
    "Agent response latency",
    ["agent_name"],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0]
)

TOKENS_USED = Counter(
    "agent_tokens_total",
    "Total tokens used",
    ["agent_name", "model"]
)

ACTIVE_SESSIONS = Gauge(
    "agent_active_sessions",
    "Number of active sessions",
    ["agent_name"]
)

ITERATIONS_HISTOGRAM = Histogram(
    "agent_iterations",
    "Number of iterations per request",
    ["agent_name"],
    buckets=[1, 2, 3, 5, 7, 10, 15, 20]
)

def track_metrics(agent_name: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()

            try:
                result = await func(*args, **kwargs)

                AGENT_REQUESTS.labels(agent_name=agent_name, status="success").inc()
                TOKENS_USED.labels(agent_name=agent_name, model="gpt-4o-mini").inc(
                    result.get("tokens", 0)
                )
                ITERATIONS_HISTOGRAM.labels(agent_name=agent_name).observe(
                    result.get("iterations", 1)
                )

                return result

            except Exception as e:
                AGENT_REQUESTS.labels(agent_name=agent_name, status="error").inc()
                raise

            finally:
                latency = time.time() - start_time
                AGENT_LATENCY.labels(agent_name=agent_name).observe(latency)

        return wrapper
    return decorator
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Structured Logging

```python
import structlog
from typing import Any
from datetime import datetime

# Configure structlog
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
)

logger = structlog.get_logger()

class AgentLogger:
    """Structured logging for agents."""

    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.log = logger.bind(agent=agent_name)

    def request_start(self, session_id: str, message: str) -> None:
        self.log.info(
            "agent_request_start",
            session_id=session_id,
            message_length=len(message)
        )

    def tool_call(self, tool_name: str, args: dict, duration_ms: float) -> None:
        self.log.info(
            "agent_tool_call",
            tool=tool_name,
            args=args,
            duration_ms=duration_ms
        )

    def iteration_complete(self, iteration: int, action: str) -> None:
        self.log.info(
            "agent_iteration",
            iteration=iteration,
            action=action
        )

    def request_complete(self, session_id: str, iterations: int, tokens: int) -> None:
        self.log.info(
            "agent_request_complete",
            session_id=session_id,
            iterations=iterations,
            tokens=tokens
        )

    def error(self, error: Exception, context: dict = None) -> None:
        self.log.error(
            "agent_error",
            error=str(error),
            error_type=type(error).__name__,
            context=context or {}
        )
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Distributed Tracing

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.requests import RequestsInstrumentor

# Setup tracer
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Export to Jaeger
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

# Auto-instrument HTTP requests
RequestsInstrumentor().instrument()

class TracedAgent:
    """Agent with distributed tracing."""

    def __init__(self, agent):
        self.agent = agent
        self.tracer = tracer

    async def run(self, message: str, session_id: str) -> dict:
        with self.tracer.start_as_current_span("agent.run") as span:
            span.set_attribute("agent.name", self.agent.config.name)
            span.set_attribute("session.id", session_id)
            span.set_attribute("message.length", len(message))

            try:
                with self.tracer.start_span("agent.reasoning") as reasoning_span:
                    result = await self.agent.run({"message": message})
                    reasoning_span.set_attribute("iterations", result.get("iterations", 0))

                span.set_attribute("tokens.used", result.get("tokens", 0))
                span.set_attribute("status", "success")

                return result

            except Exception as e:
                span.set_attribute("status", "error")
                span.set_attribute("error.message", str(e))
                span.record_exception(e)
                raise
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Alerting Rules

```yaml
# prometheus-rules.yaml
groups:
  - name: agent-alerts
    rules:
      # High error rate
      - alert: AgentHighErrorRate
        expr: |
          rate(agent_requests_total{status="error"}[5m])
          / rate(agent_requests_total[5m]) > 0.01
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High agent error rate"
          description: "Error rate is above 1%"

      # High latency
      - alert: AgentHighLatency
        expr: |
          histogram_quantile(0.95, rate(agent_latency_seconds_bucket[5m])) > 5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High agent latency"
          description: "95th percentile latency is above 5 seconds"

      # Token budget alert
      - alert: AgentTokenBudgetWarning
        expr: |
          increase(agent_tokens_total[1h]) > 100000
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: "High token usage"
          description: "Token usage exceeds 100k per hour"

      # Too many iterations
      - alert: AgentHighIterations
        expr: |
          histogram_quantile(0.9, rate(agent_iterations_bucket[5m])) > 8
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Agent using many iterations"
          description: "90th percentile iterations above 8"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cost Tracking

```python
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class CostTracker:
    """Track and alert on API costs."""

    daily_budget_usd: float = 100.0

    # Pricing per 1M tokens (approximate)
    PRICING = {
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4-turbo": {"input": 10.00, "output": 30.00}
    }

    def __init__(self):
        self.usage = []

    def record(self, model: str, input_tokens: int, output_tokens: int) -> None:
        cost = self._calculate_cost(model, input_tokens, output_tokens)
        self.usage.append({
            "timestamp": datetime.now(),
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost_usd": cost
        })

    def _calculate_cost(self, model: str, input_t: int, output_t: int) -> float:
        pricing = self.PRICING.get(model, self.PRICING["gpt-4o-mini"])
        return (input_t * pricing["input"] + output_t * pricing["output"]) / 1_000_000

    def get_daily_cost(self) -> float:
        today = datetime.now().date()
        return sum(
            u["cost_usd"] for u in self.usage
            if u["timestamp"].date() == today
        )

    def is_over_budget(self) -> bool:
        return self.get_daily_cost() > self.daily_budget_usd
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Metrics explosion | For manga labels | Begrana cardinality |
| Log flooding | For verbose | Log sampling |
| Trace gaps | Missing instrumentation | Auto-instrument |
| Alert fatigue | For kansliga alerts | Tune thresholds |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Metrics | Prometheus for numerisk data |
| Logs | Strukturerad JSON logging |
| Traces | Distributed tracing for flows |
| Alerts | Actionable, inte noise |

Kom ihag:
- Tre pillars: metrics, logs, traces
- Alerts ska vara actionable
- Track tokens for cost control
- Dashboards for visibility
'''
}

BLOCK_09_NODES = [NODE_17_DEPLOYMENT, NODE_18_MONITORING]
