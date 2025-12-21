# =============================================================================
# DOCKER MASTERY V3 - BLOCK 5 PART 2: MONITORING & SCALE
# Noder 19-20 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
DOCKER BLOCK 5 PART 2 - OPERATIONS AT SCALE
============================================
Node 19: Docker Monitoring - Observability
Node 20: Docker at Scale - Enterprise Patterns
"""

NODE_19 = {
    "id": "docker_node_19",
    "title": "Docker Monitoring - Observability",
    "slug": "docker-monitoring-observability",
    "content": r'''# 📊 Docker Monitoring

## 1. Introduktion & Kontext

Observability ar kritiskt for produktions-Docker-miljoer. Det innefattar metrics, logging och tracing for att forsta systemets beteende.

### Observability Pillars

```
+-------------------------------------------------------------------------+
|                    OBSERVABILITY PILLARS                                 |
+-------------------------------------------------------------------------+
|                                                                          |
|                         OBSERVABILITY                                    |
|                              |                                           |
|            +-----------------+-----------------+                        |
|            |                 |                 |                        |
|            ▼                 ▼                 ▼                        |
|     +----------+      +----------+      +----------+                   |
|     |  METRICS |      |   LOGS   |      |  TRACES  |                   |
|     |          |      |          |      |          |                   |
|     | What is  |      | What     |      | How      |                   |
|     |happening |      |happened  |      | it flows |                   |
|     |          |      |          |      |          |                   |
|     |Prometheus|      | Loki/ELK |      | Jaeger   |                   |
|     | Grafana  |      | Grafana  |      | Zipkin   |                   |
|     +----------+      +----------+      +----------+                   |
|                                                                          |
|  METRICS: Quantitative data (CPU, memory, requests/sec)                 |
|  LOGS: Qualitative events (errors, warnings, info)                      |
|  TRACES: Request flow across services                                   |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Prometheus Stack

```yaml
# ═══════════════════════════════════════════════════════════════════════
# docker-compose.monitoring.yml
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

services:
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=15d'
    ports:
      - "9090:9090"
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    volumes:
      - grafana-data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning:ro
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD}
      - GF_USERS_ALLOW_SIGN_UP=false
    ports:
      - "3000:3000"
    restart: unless-stopped
    depends_on:
      - prometheus

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    ports:
      - "8080:8080"
    restart: unless-stopped

  node-exporter:
    image: prom/node-exporter:latest
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.sysfs=/host/sys'
      - '--path.rootfs=/rootfs'
    ports:
      - "9100:9100"
    restart: unless-stopped

volumes:
  prometheus-data:
  grafana-data:
```

### Prometheus Config

```yaml
# prometheus/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'docker'
    static_configs:
      - targets: ['host.docker.internal:9323']

  - job_name: 'api'
    static_configs:
      - targets: ['api:8000']
    metrics_path: /metrics
```

## 3. Application Metrics

```python
# ═══════════════════════════════════════════════════════════════════════
# PYTHON/FASTAPI PROMETHEUS METRICS
# ═══════════════════════════════════════════════════════════════════════

from prometheus_client import Counter, Histogram, Gauge, generate_latest
from fastapi import FastAPI, Request, Response
import time

app = FastAPI()

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)

ACTIVE_REQUESTS = Gauge(
    'http_requests_active',
    'Active HTTP requests'
)

# Middleware
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    ACTIVE_REQUESTS.inc()
    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.url.path
    ).observe(duration)

    ACTIVE_REQUESTS.dec()

    return response

# Metrics endpoint
@app.get("/metrics")
async def metrics():
    return Response(
        content=generate_latest(),
        media_type="text/plain"
    )
```

## 4. Log Aggregation

```yaml
# ═══════════════════════════════════════════════════════════════════════
# LOKI STACK
# ═══════════════════════════════════════════════════════════════════════

services:
  loki:
    image: grafana/loki:latest
    ports:
      - "3100:3100"
    volumes:
      - loki-data:/loki
    command: -config.file=/etc/loki/local-config.yaml
    restart: unless-stopped

  promtail:
    image: grafana/promtail:latest
    volumes:
      - /var/log:/var/log:ro
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
      - ./promtail/config.yml:/etc/promtail/config.yml:ro
    command: -config.file=/etc/promtail/config.yml
    restart: unless-stopped
    depends_on:
      - loki
```

### Promtail Config

```yaml
# promtail/config.yml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://loki:3100/loki/api/v1/push

scrape_configs:
  - job_name: containers
    static_configs:
      - targets:
          - localhost
        labels:
          job: containerlogs
          __path__: /var/lib/docker/containers/*/*log

    pipeline_stages:
      - json:
          expressions:
            output: log
            stream: stream
            attrs:
      - json:
          expressions:
            tag:
          source: attrs
      - regex:
          expression: '^(?P<container_name>[^/]+)'
          source: tag
      - labels:
          container_name:
          stream:
      - output:
          source: output
```

## 5. Docker Metrics

```bash
# ═══════════════════════════════════════════════════════════════════════
# ENABLE DOCKER METRICS
# ═══════════════════════════════════════════════════════════════════════

# /etc/docker/daemon.json
{
  "metrics-addr": "0.0.0.0:9323",
  "experimental": true
}

# Restart Docker
sudo systemctl restart docker

# Test metrics
curl http://localhost:9323/metrics
```

## 6. Alerting

```yaml
# ═══════════════════════════════════════════════════════════════════════
# ALERTMANAGER CONFIG
# ═══════════════════════════════════════════════════════════════════════

# alertmanager/alertmanager.yml
global:
  smtp_smarthost: 'smtp.example.com:587'
  smtp_from: 'alerts@example.com'

route:
  group_by: ['alertname', 'severity']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: 'team-email'

receivers:
  - name: 'team-email'
    email_configs:
      - to: 'team@example.com'

  - name: 'slack'
    slack_configs:
      - api_url: 'https://hooks.slack.com/services/xxx'
        channel: '#alerts'
```

### Alert Rules

```yaml
# prometheus/alert_rules.yml
groups:
  - name: containers
    rules:
      - alert: ContainerDown
        expr: absent(container_last_seen{name=~".+"})
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Container down"

      - alert: HighCPU
        expr: rate(container_cpu_usage_seconds_total[5m]) > 0.9
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage"

      - alert: HighMemory
        expr: container_memory_usage_bytes / container_spec_memory_limit_bytes > 0.9
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High memory usage"
```

## 7-14. Sammanfattning

### Monitoring Stack

| Component | Purpose |
|-----------|---------|
| Prometheus | Metrics collection |
| Grafana | Visualization |
| Loki | Log aggregation |
| Alertmanager | Alerting |

---

**Nasta Node:** Docker at Scale ->
''',
    "xp_reward": 180,
    "estimated_minutes": 85,
    "prerequisites": ["docker_node_18"],
    "learning_outcomes": [
        "Satta upp Prometheus och Grafana",
        "Implementera application metrics",
        "Konfigurera log aggregation",
        "Skapa alerting rules"
    ]
}

NODE_20 = {
    "id": "docker_node_20",
    "title": "Docker at Scale - Enterprise Patterns",
    "slug": "docker-at-scale-enterprise-patterns",
    "content": r'''# 🌐 Docker at Scale

## 1. Introduktion & Kontext

Att kora Docker i enterprise-skala kraver specifika patterns och strategier for att hantera komplexitet, sakerhet och prestanda.

### Scale Considerations

```
+-------------------------------------------------------------------------+
|                    DOCKER AT SCALE                                       |
+-------------------------------------------------------------------------+
|                                                                          |
|  SCALE DIMENSIONS:                                                       |
|  ---------------------------------------------------------------------  |
|                                                                          |
|  HORIZONTAL                     VERTICAL                                |
|  ----------                     --------                                |
|  More containers                Bigger containers                       |
|  More nodes                     More resources per container            |
|  Load balancing                 Optimized images                        |
|                                                                          |
|  ORGANIZATIONAL                 OPERATIONAL                             |
|  --------------                 -----------                             |
|  Multiple teams                 CI/CD pipelines                         |
|  Multiple environments          Monitoring at scale                     |
|  Image governance               Incident response                       |
|                                                                          |
|  CHALLENGES AT SCALE:                                                   |
|  ---------------------------------------------------------------------  |
|  • Image sprawl (100s of images)                                        |
|  • Registry management                                                  |
|  • Secret distribution                                                  |
|  • Network complexity                                                   |
|  • Log volume (TB/day)                                                 |
|  • Cost optimization                                                    |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Image Management

```bash
# ═══════════════════════════════════════════════════════════════════════
# IMAGE LIFECYCLE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════

# Image naming convention
${REGISTRY}/${TEAM}/${APP}:${VERSION}

# Examples:
gcr.io/mycompany/platform/api:v1.2.3
gcr.io/mycompany/platform/api:v1.2.3-abc1234
gcr.io/mycompany/platform/api:latest

# ═══════════════════════════════════════════════════════════════════════
# IMAGE CLEANUP POLICY
# ═══════════════════════════════════════════════════════════════════════

# Registry cleanup (GCR example)
gcloud container images list-tags gcr.io/myproject/api \
  --filter="timestamp.datetime < '2024-01-01'" \
  --format='get(digest)' | \
  xargs -I {} gcloud container images delete gcr.io/myproject/api@{} --quiet

# Docker system cleanup
docker system prune -a --volumes --filter "until=168h"
```

## 3. Multi-Environment Strategy

```yaml
# ═══════════════════════════════════════════════════════════════════════
# ENVIRONMENT-SPECIFIC COMPOSE FILES
# ═══════════════════════════════════════════════════════════════════════

# docker-compose.yml (base)
services:
  api:
    image: ${REGISTRY}/api:${VERSION}
    environment:
      - LOG_LEVEL=${LOG_LEVEL:-info}

# docker-compose.dev.yml
services:
  api:
    volumes:
      - ./src:/app/src
    environment:
      - LOG_LEVEL=debug
    ports:
      - "8000:8000"

# docker-compose.staging.yml
services:
  api:
    deploy:
      replicas: 2
    environment:
      - LOG_LEVEL=info

# docker-compose.prod.yml
services:
  api:
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: '2'
          memory: 2G
    environment:
      - LOG_LEVEL=warn
```

```bash
# Usage
docker compose -f docker-compose.yml -f docker-compose.dev.yml up
docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

## 4. Security at Scale

```yaml
# ═══════════════════════════════════════════════════════════════════════
# SECURITY POLICIES
# ═══════════════════════════════════════════════════════════════════════

# Base secure image
FROM gcr.io/distroless/base-debian12

# ═══════════════════════════════════════════════════════════════════════
# SUPPLY CHAIN SECURITY
# ═══════════════════════════════════════════════════════════════════════

# Sign images with cosign
cosign sign --key cosign.key ${REGISTRY}/api:v1.0.0

# Verify before deploy
cosign verify --key cosign.pub ${REGISTRY}/api:v1.0.0

# ═══════════════════════════════════════════════════════════════════════
# POLICY ENFORCEMENT (OPA/Gatekeeper)
# ═══════════════════════════════════════════════════════════════════════

# policy.rego
package docker

deny[msg] {
    input.user == "root"
    msg = "Containers must not run as root"
}

deny[msg] {
    not input.healthcheck
    msg = "Containers must have healthcheck"
}
```

## 5. GitOps Workflow

```yaml
# ═══════════════════════════════════════════════════════════════════════
# ARGOCD APPLICATION
# ═══════════════════════════════════════════════════════════════════════

# argocd/application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/manifests
    targetRevision: HEAD
    path: apps/myapp
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

## 6. Cost Optimization

```
+-------------------------------------------------------------------------+
|                    COST OPTIMIZATION STRATEGIES                          |
+-------------------------------------------------------------------------+
|                                                                          |
|  IMAGE OPTIMIZATION                                                      |
|  □ Use multi-stage builds (reduce size 50-90%)                          |
|  □ Use distroless/alpine bases                                          |
|  □ Remove development dependencies                                      |
|  □ Cleanup in same layer                                                |
|                                                                          |
|  RESOURCE OPTIMIZATION                                                  |
|  □ Right-size container resources                                       |
|  □ Use auto-scaling                                                     |
|  □ Implement resource quotas                                            |
|  □ Spot/preemptible instances                                          |
|                                                                          |
|  REGISTRY OPTIMIZATION                                                  |
|  □ Implement retention policies                                         |
|  □ Use regional registries                                              |
|  □ Cache base images                                                    |
|  □ Lifecycle policies                                                   |
|                                                                          |
|  BUILD OPTIMIZATION                                                     |
|  □ Efficient caching                                                    |
|  □ Parallel builds                                                      |
|  □ Incremental builds                                                   |
|  □ Remote cache                                                         |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 7. Team Workflows

```yaml
# ═══════════════════════════════════════════════════════════════════════
# TEAM-BASED REGISTRY STRUCTURE
# ═══════════════════════════════════════════════════════════════════════

# Registry structure
registry.example.com/
+-- platform/              # Platform team
|   +-- api
|   +-- gateway
|   +-- auth
+-- data/                  # Data team
|   +-- etl
|   +-- warehouse
|   +-- ml-models
+-- frontend/              # Frontend team
|   +-- web
|   +-- mobile-api
|   +-- cdn
+-- shared/                # Shared images
    +-- base-python
    +-- base-node
    +-- ci-tools
```

## 8. Disaster Recovery

```bash
# ═══════════════════════════════════════════════════════════════════════
# BACKUP STRATEGIES
# ═══════════════════════════════════════════════════════════════════════

# Volume backup
docker run --rm \
  -v mydata:/source:ro \
  -v $(pwd)/backups:/backup \
  alpine tar czf /backup/mydata-$(date +%Y%m%d).tar.gz -C /source .

# Registry backup (mirror)
skopeo sync \
  --src docker \
  --dest dir \
  registry.example.com/myapp \
  ./backup/

# ═══════════════════════════════════════════════════════════════════════
# RESTORE PROCEDURES
# ═══════════════════════════════════════════════════════════════════════

# Volume restore
docker run --rm \
  -v newvolume:/target \
  -v $(pwd)/backups:/backup:ro \
  alpine tar xzf /backup/mydata-20240115.tar.gz -C /target
```

## 9-14. Sammanfattning & Kursavslut

### Docker Mastery Checklist

| Module | Key Topics |
|--------|------------|
| Basics | Images, containers, Dockerfile |
| Storage | Volumes, bind mounts |
| Network | Bridge, overlay, DNS |
| Compose | Multi-container, profiles |
| Security | Non-root, scanning, secrets |
| CI/CD | Build, test, deploy |
| Production | Swarm, monitoring, scale |

### Nasta Steg

Efter Docker Mastery, fortsatt till:
- Kubernetes for advanced orchestration
- Terraform for infrastructure as code
- GitOps for declarative deployments

---

**GRATTIS! Du har slutfort Docker Mastery!** 🎉
''',
    "xp_reward": 200,
    "estimated_minutes": 95,
    "prerequisites": ["docker_node_19"],
    "learning_outcomes": [
        "Hantera Docker i enterprise-skala",
        "Implementera GitOps workflows",
        "Optimera kostnader",
        "Planera disaster recovery"
    ]
}

# Block 5 Part 2 exports
BLOCK_5_PART_2_NODES = [NODE_19, NODE_20]

__all__ = ["NODE_19", "NODE_20", "BLOCK_5_PART_2_NODES"]
