# =============================================================================
# DOCKER MASTERY V3 - BLOCK 5 PART 1: SWARM & PRODUCTION
# Noder 17-18 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
DOCKER BLOCK 5 PART 1 - ORCHESTRATION
=====================================
Node 17: Docker Swarm - Native Orchestration
Node 18: Production Patterns - Best Practices
"""

NODE_17 = {
    "id": "docker_node_17",
    "title": "Docker Swarm - Native Orchestration",
    "slug": "docker-swarm-native-orchestration",
    "content": r'''# 🐝 Docker Swarm

## 1. Introduktion & Kontext

Docker Swarm ar Dockers inbyggda orchestration-losning. Den gor det mojligt att hantera ett kluster av Docker-noder som en enda virtuell host.

### Swarm Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DOCKER SWARM ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│                        MANAGER NODES                                     │
│                   (Raft Consensus Group)                                │
│                                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                  │
│  │   Manager 1  │  │   Manager 2  │  │   Manager 3  │                  │
│  │   (Leader)   │◄─►│  (Follower)  │◄─►│  (Follower)  │                  │
│  │              │  │              │  │              │                  │
│  │  - API       │  │  - API       │  │  - API       │                  │
│  │  - Scheduler │  │  - Standby   │  │  - Standby   │                  │
│  │  - Raft      │  │  - Raft      │  │  - Raft      │                  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                  │
│         │                 │                 │                           │
│         └─────────────────┼─────────────────┘                           │
│                           │                                             │
│                    WORKER NODES                                         │
│                                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                  │
│  │   Worker 1   │  │   Worker 2   │  │   Worker 3   │                  │
│  │              │  │              │  │              │                  │
│  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │                  │
│  │  │Task 1.1│  │  │  │Task 1.2│  │  │  │Task 2.1│  │                  │
│  │  └────────┘  │  │  └────────┘  │  │  └────────┘  │                  │
│  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │                  │
│  │  │Task 2.2│  │  │  │Task 3.1│  │  │  │Task 3.2│  │                  │
│  │  └────────┘  │  │  └────────┘  │  │  └────────┘  │                  │
│  └──────────────┘  └──────────────┘  └──────────────┘                  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Swarm Setup

```bash
# ═══════════════════════════════════════════════════════════════════════
# INITIALIZE SWARM
# ═══════════════════════════════════════════════════════════════════════

# Init on manager node
docker swarm init --advertise-addr 192.168.1.10

# Output gives join token for workers:
# docker swarm join --token SWMTKN-1-xxx 192.168.1.10:2377

# Get tokens
docker swarm join-token worker
docker swarm join-token manager

# Join as worker (run on worker node)
docker swarm join --token SWMTKN-1-xxx 192.168.1.10:2377

# Join as manager
docker swarm join --token SWMTKN-1-yyy 192.168.1.10:2377

# ═══════════════════════════════════════════════════════════════════════
# NODE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════

# List nodes
docker node ls

# Inspect node
docker node inspect worker1

# Promote worker to manager
docker node promote worker1

# Demote manager to worker
docker node demote manager2

# Drain node (for maintenance)
docker node update --availability drain worker1

# Reactivate node
docker node update --availability active worker1

# Remove node
docker node rm worker1

# Leave swarm
docker swarm leave
docker swarm leave --force  # On last manager
```

## 3. Services

```bash
# ═══════════════════════════════════════════════════════════════════════
# CREATE SERVICE
# ═══════════════════════════════════════════════════════════════════════

# Basic service
docker service create --name web nginx:alpine

# With replicas
docker service create \
  --name api \
  --replicas 3 \
  --publish 8000:8000 \
  myapi:latest

# Full options
docker service create \
  --name api \
  --replicas 3 \
  --publish published=8000,target=8000 \
  --env NODE_ENV=production \
  --secret db_password \
  --config nginx_config \
  --mount type=volume,source=api-data,target=/data \
  --network backend \
  --constraint 'node.role==worker' \
  --limit-cpu 1 \
  --limit-memory 512M \
  --restart-condition any \
  --update-parallelism 1 \
  --update-delay 10s \
  myapi:latest

# ═══════════════════════════════════════════════════════════════════════
# MANAGE SERVICES
# ═══════════════════════════════════════════════════════════════════════

# List services
docker service ls

# Service details
docker service ps api
docker service inspect api
docker service logs api
docker service logs -f --tail 100 api

# Scale service
docker service scale api=5
docker service update --replicas 5 api

# Update service
docker service update --image myapi:v2 api
docker service update --env-add NEW_VAR=value api
docker service update --limit-memory 1G api

# Remove service
docker service rm api
```

## 4. Stack Deploy

```yaml
# ═══════════════════════════════════════════════════════════════════════
# docker-stack.yml
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

services:
  api:
    image: myapi:latest
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
        failure_action: rollback
      rollback_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
      resources:
        limits:
          cpus: '1'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M
      placement:
        constraints:
          - node.role == worker
    ports:
      - "8000:8000"
    networks:
      - backend
    secrets:
      - db_password
    environment:
      - DATABASE_URL_FILE=/run/secrets/db_password

  db:
    image: postgres:15
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.labels.db == true
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend
    secrets:
      - db_password
    environment:
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password

networks:
  backend:
    driver: overlay

volumes:
  db-data:

secrets:
  db_password:
    external: true
```

```bash
# Deploy stack
docker stack deploy -c docker-stack.yml myapp

# List stacks
docker stack ls

# Stack services
docker stack services myapp

# Stack tasks
docker stack ps myapp

# Remove stack
docker stack rm myapp
```

## 5. Networking

```bash
# ═══════════════════════════════════════════════════════════════════════
# OVERLAY NETWORKS
# ═══════════════════════════════════════════════════════════════════════

# Create overlay network
docker network create --driver overlay backend

# Encrypted overlay
docker network create --driver overlay --opt encrypted=true secure-net

# Attachable (for standalone containers)
docker network create --driver overlay --attachable debug-net

# ═══════════════════════════════════════════════════════════════════════
# INGRESS ROUTING MESH
# ═══════════════════════════════════════════════════════════════════════

# All nodes route traffic to services
# Request to any node:8000 routes to service
docker service create \
  --name web \
  --publish 8000:80 \
  --replicas 3 \
  nginx
```

## 6. Secrets & Configs

```bash
# ═══════════════════════════════════════════════════════════════════════
# SECRETS
# ═══════════════════════════════════════════════════════════════════════

# Create from file
docker secret create db_password ./secrets/db_password.txt

# Create from stdin
echo "supersecret" | docker secret create api_key -

# List secrets
docker secret ls

# Inspect secret (no value shown)
docker secret inspect db_password

# Remove secret
docker secret rm db_password

# ═══════════════════════════════════════════════════════════════════════
# CONFIGS
# ═══════════════════════════════════════════════════════════════════════

# Create config
docker config create nginx_config ./nginx.conf

# List configs
docker config ls

# Inspect config
docker config inspect nginx_config

# Remove config
docker config rm nginx_config
```

## 7-14. Sammanfattning

### Swarm Commands Reference

| Command | Purpose |
|---------|---------|
| `docker swarm init` | Initialize cluster |
| `docker service create` | Deploy service |
| `docker stack deploy` | Deploy stack |
| `docker service scale` | Scale replicas |

---

**Nasta Node:** Production Patterns →
''',
    "xp_reward": 180,
    "estimated_minutes": 85,
    "prerequisites": ["docker_node_16"],
    "learning_outcomes": [
        "Konfigurera Docker Swarm",
        "Deploya services och stacks",
        "Hantera overlay networks",
        "Anvanda secrets och configs"
    ]
}

NODE_18 = {
    "id": "docker_node_18",
    "title": "Production Patterns - Best Practices",
    "slug": "production-patterns-best-practices",
    "content": r'''# 🏭 Production Patterns

## 1. Introduktion & Kontext

Production Docker deployments kraver robusta patterns for sakkerhet, skalbarhet och tillganglighet. Denna guide samlar beprövade produktionsmönster.

### Production Checklist

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PRODUCTION READINESS CHECKLIST                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  SECURITY                                                                │
│  □ Non-root user in containers                                          │
│  □ Read-only filesystem where possible                                  │
│  □ Secrets management (not env vars)                                    │
│  □ Image vulnerability scanning                                         │
│  □ Network segmentation                                                 │
│  □ Resource limits set                                                  │
│                                                                          │
│  RELIABILITY                                                             │
│  □ Health checks configured                                             │
│  □ Restart policies defined                                             │
│  □ Graceful shutdown handling                                           │
│  □ Rolling updates configured                                           │
│  □ Rollback strategy defined                                            │
│                                                                          │
│  OBSERVABILITY                                                           │
│  □ Structured logging (JSON)                                            │
│  □ Metrics exposed                                                      │
│  □ Distributed tracing                                                  │
│  □ Log aggregation                                                      │
│                                                                          │
│  PERFORMANCE                                                             │
│  □ Optimized images (multi-stage)                                       │
│  □ Resource limits tuned                                                │
│  □ Connection pooling                                                   │
│  □ Caching strategies                                                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Production Compose

```yaml
# ═══════════════════════════════════════════════════════════════════════
# docker-compose.prod.yml
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

x-logging: &default-logging
  driver: json-file
  options:
    max-size: "50m"
    max-file: "5"

x-healthcheck: &default-healthcheck
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 60s

services:
  traefik:
    image: traefik:v2.10
    command:
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.le.acme.httpchallenge=true"
      - "--certificatesresolvers.le.acme.email=${ACME_EMAIL}"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - traefik-certs:/letsencrypt
    logging: *default-logging
    restart: always
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 256M

  api:
    image: ${REGISTRY}/api:${VERSION}
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.api.rule=Host(`api.example.com`)"
      - "traefik.http.routers.api.tls.certresolver=le"
    environment:
      - DATABASE_URL_FILE=/run/secrets/database_url
      - REDIS_URL=redis://redis:6379
    secrets:
      - database_url
    logging: *default-logging
    restart: always
    healthcheck:
      <<: *default-healthcheck
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy

  db:
    image: postgres:15-alpine
    volumes:
      - postgres-data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
      POSTGRES_DB: production
    secrets:
      - db_password
    logging: *default-logging
    restart: always
    healthcheck:
      <<: *default-healthcheck
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 4G

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    logging: *default-logging
    restart: always
    healthcheck:
      <<: *default-healthcheck
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M

volumes:
  postgres-data:
  redis-data:
  traefik-certs:

secrets:
  database_url:
    file: ./secrets/database_url
  db_password:
    file: ./secrets/db_password
```

## 3. Zero-Downtime Deployment

```yaml
# ═══════════════════════════════════════════════════════════════════════
# ROLLING UPDATE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════

services:
  api:
    deploy:
      replicas: 3
      update_config:
        parallelism: 1           # Update one at a time
        delay: 30s               # Wait between updates
        failure_action: rollback # Rollback on failure
        monitor: 60s             # Monitor for this long
        max_failure_ratio: 0.3   # Max 30% can fail
        order: start-first       # Start new before stopping old
      rollback_config:
        parallelism: 1
        delay: 10s
        failure_action: pause
        monitor: 60s
        order: stop-first
```

```bash
# ═══════════════════════════════════════════════════════════════════════
# DEPLOYMENT SCRIPT
# ═══════════════════════════════════════════════════════════════════════

#!/bin/bash
set -e

VERSION=$1
REGISTRY=ghcr.io/myorg

# Pull new image
docker pull ${REGISTRY}/api:${VERSION}

# Update with zero downtime
docker service update \
  --image ${REGISTRY}/api:${VERSION} \
  --update-parallelism 1 \
  --update-delay 30s \
  --update-failure-action rollback \
  myapp_api

# Wait for rollout
docker service rollout status myapp_api

echo "Deployment complete: ${VERSION}"
```

## 4. Graceful Shutdown

```python
# ═══════════════════════════════════════════════════════════════════════
# PYTHON GRACEFUL SHUTDOWN
# ═══════════════════════════════════════════════════════════════════════

import signal
import sys
import asyncio

shutdown_event = asyncio.Event()

def handle_signal(signum, frame):
    print(f"Received signal {signum}")
    shutdown_event.set()

signal.signal(signal.SIGTERM, handle_signal)
signal.signal(signal.SIGINT, handle_signal)

async def main():
    # Start server
    server = await start_server()

    # Wait for shutdown signal
    await shutdown_event.wait()

    # Graceful shutdown
    print("Shutting down gracefully...")

    # Stop accepting new connections
    server.close()
    await server.wait_closed()

    # Complete in-flight requests (timeout)
    await asyncio.wait_for(
        complete_pending_requests(),
        timeout=30.0
    )

    # Cleanup
    await cleanup_resources()

    print("Shutdown complete")
    sys.exit(0)
```

## 5. Logging Best Practices

```python
# ═══════════════════════════════════════════════════════════════════════
# STRUCTURED LOGGING
# ═══════════════════════════════════════════════════════════════════════

import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        if hasattr(record, 'request_id'):
            log_record['request_id'] = record.request_id

        if record.exc_info:
            log_record['exception'] = self.formatException(record.exc_info)

        return json.dumps(log_record)

# Setup
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)
```

## 6. Resource Management

```yaml
# ═══════════════════════════════════════════════════════════════════════
# RESOURCE LIMITS BY SERVICE TYPE
# ═══════════════════════════════════════════════════════════════════════

services:
  # Web/API service
  api:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M

  # Background worker
  worker:
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G

  # Database
  db:
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 8G
        reservations:
          cpus: '2'
          memory: 4G

  # Cache
  redis:
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
        reservations:
          cpus: '0.25'
          memory: 256M
```

## 7-14. Sammanfattning

### Production Checklist

| Area | Key Items |
|------|-----------|
| Security | Non-root, secrets, scanning |
| Reliability | Health checks, restarts |
| Observability | Logging, metrics |
| Performance | Limits, caching |

---

**Nasta Node:** Docker Monitoring →
''',
    "xp_reward": 185,
    "estimated_minutes": 90,
    "prerequisites": ["docker_node_17"],
    "learning_outcomes": [
        "Implementera production patterns",
        "Konfigurera zero-downtime deployments",
        "Hantera graceful shutdown",
        "Satta upp strukturerad logging"
    ]
}

# Block 5 Part 1 exports
BLOCK_5_PART_1_NODES = [NODE_17, NODE_18]

__all__ = ["NODE_17", "NODE_18", "BLOCK_5_PART_1_NODES"]
