# =============================================================================
# DOCKER MASTERY V3 - BLOCK 2 PART 2: DOCKER COMPOSE
# Noder 7-8 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
DOCKER BLOCK 2 PART 2 - COMPOSE
===============================
Node 7: Compose Basics - Multi-container Apps
Node 8: Compose Advanced - Production Features
"""

NODE_7 = {
    "id": "docker_node_7",
    "title": "Compose Basics - Multi-container Apps",
    "slug": "compose-basics-multi-container-apps",
    "content": r'''# 🎼 Docker Compose Basics

## 1. Introduktion & Kontext

Docker Compose är ett verktyg för att definiera och köra multi-container Docker applikationer. Med en YAML-fil kan du konfigurera alla dina services och starta dem med ett enda kommando.

### Compose vs Docker Run

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   COMPOSE VS DOCKER RUN                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  DOCKER RUN (Manual):                                                    │
│  ═══════════════════════════════════════════════════════════════════   │
│                                                                          │
│  docker network create myapp                                            │
│  docker volume create db-data                                           │
│                                                                          │
│  docker run -d \                                                        │
│    --name db \                                                          │
│    --network myapp \                                                    │
│    -e POSTGRES_PASSWORD=secret \                                        │
│    -v db-data:/var/lib/postgresql/data \                               │
│    postgres:15                                                          │
│                                                                          │
│  docker run -d \                                                        │
│    --name api \                                                         │
│    --network myapp \                                                    │
│    -e DATABASE_URL=postgresql://... \                                   │
│    -p 8000:8000 \                                                       │
│    myapi:latest                                                         │
│                                                                          │
│  DOCKER COMPOSE (Declarative):                                          │
│  ═══════════════════════════════════════════════════════════════════   │
│                                                                          │
│  docker compose up -d   ← Ett kommando!                                 │
│                                                                          │
│  Fördelar:                                                               │
│  ─────────────────────────────────────────────────────────────────────  │
│  ✓ Versionshanterat (YAML-fil i repo)                                  │
│  ✓ Reproducerbart                                                       │
│  ✓ Enkelt att dela                                                      │
│  ✓ Ett kommando för hela stacken                                       │
│  ✓ Automatisk nätverks- och volymhantering                             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Compose File Structure

```yaml
# ═══════════════════════════════════════════════════════════════════════
# docker-compose.yml - Basic Structure
# ═══════════════════════════════════════════════════════════════════════

# Version (optional i Compose v2+)
version: "3.9"

# Services (containers)
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"

  api:
    build: ./api
    environment:
      - NODE_ENV=production
    depends_on:
      - db

  db:
    image: postgres:15
    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: secret

# Volumes (persistent storage)
volumes:
  db-data:

# Networks (communication)
networks:
  frontend:
  backend:
```

### File Hierarchy

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    COMPOSE FILE STRUCTURE                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  docker-compose.yml                                                      │
│  ├── version: "3.9"                                                     │
│  │                                                                       │
│  ├── services:                    # Container definitions               │
│  │   ├── web:                                                           │
│  │   │   ├── image                                                      │
│  │   │   ├── build                                                      │
│  │   │   ├── ports                                                      │
│  │   │   ├── volumes                                                    │
│  │   │   ├── environment                                                │
│  │   │   ├── depends_on                                                 │
│  │   │   ├── networks                                                   │
│  │   │   └── ...                                                        │
│  │   └── db:                                                            │
│  │       └── ...                                                        │
│  │                                                                       │
│  ├── volumes:                     # Volume definitions                  │
│  │   └── db-data:                                                       │
│  │                                                                       │
│  ├── networks:                    # Network definitions                 │
│  │   ├── frontend:                                                      │
│  │   └── backend:                                                       │
│  │                                                                       │
│  ├── configs:                     # Config file definitions             │
│  │                                                                       │
│  └── secrets:                     # Secret definitions                  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3. Service Configuration

```yaml
# ═══════════════════════════════════════════════════════════════════════
# SERVICE OPTIONS
# ═══════════════════════════════════════════════════════════════════════

services:
  api:
    # Image or build
    image: myapi:1.0.0                    # Använd befintlig image
    build:                                 # Eller bygg
      context: ./api
      dockerfile: Dockerfile
      args:
        VERSION: 1.0.0

    # Container name
    container_name: myapi-container

    # Port mapping
    ports:
      - "8000:8000"                        # host:container
      - "127.0.0.1:9000:9000"              # Bind till localhost
      - "8080"                             # Random host port

    # Environment variables
    environment:
      NODE_ENV: production
      DATABASE_URL: postgresql://db:5432/mydb
    env_file:
      - .env
      - .env.production

    # Volumes
    volumes:
      - ./src:/app/src                     # Bind mount
      - api-data:/app/data                 # Named volume
      - /app/node_modules                  # Anonymous volume

    # Networks
    networks:
      - frontend
      - backend

    # Dependencies
    depends_on:
      - db
      - redis

    # Restart policy
    restart: unless-stopped                # no, always, on-failure

    # Resource limits
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M

    # Health check
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

    # Command override
    command: ["npm", "start"]
    entrypoint: ["/entrypoint.sh"]

    # Working directory
    working_dir: /app

    # User
    user: "1000:1000"
```

## 4. Compose Commands

```bash
# ═══════════════════════════════════════════════════════════════════════
# COMPOSE LIFECYCLE
# ═══════════════════════════════════════════════════════════════════════

# Starta services (bakgrund)
docker compose up -d

# Starta med build
docker compose up -d --build

# Starta specifik service
docker compose up -d api

# Stoppa services
docker compose stop

# Stoppa och ta bort
docker compose down

# Ta bort inkl. volumes
docker compose down -v

# ═══════════════════════════════════════════════════════════════════════
# BUILD
# ═══════════════════════════════════════════════════════════════════════

docker compose build
docker compose build --no-cache
docker compose build api                  # Specifik service

# ═══════════════════════════════════════════════════════════════════════
# MONITORING
# ═══════════════════════════════════════════════════════════════════════

docker compose ps                         # Lista services
docker compose ps -a                      # Inkl. stoppade
docker compose logs                       # Alla logs
docker compose logs -f api                # Follow specifik
docker compose logs --tail 100            # Senaste 100
docker compose top                        # Processer

# ═══════════════════════════════════════════════════════════════════════
# EXEC & RUN
# ═══════════════════════════════════════════════════════════════════════

docker compose exec api bash              # Shell i körande
docker compose exec db psql -U postgres   # Databaskommando
docker compose run --rm api npm test      # Kör en gång

# ═══════════════════════════════════════════════════════════════════════
# SCALING & RESTART
# ═══════════════════════════════════════════════════════════════════════

docker compose restart api                # Starta om service
docker compose up -d --scale api=3        # Skala horisontellt
```

## 5. Practical Example: Web Stack

```yaml
# ═══════════════════════════════════════════════════════════════════════
# docker-compose.yml - Complete Web Application
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

services:
  # ===========================================
  # NGINX Reverse Proxy
  # ===========================================
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - frontend
      - api
    networks:
      - frontend
    restart: unless-stopped

  # ===========================================
  # Frontend (React/Next.js)
  # ===========================================
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    environment:
      - NEXT_PUBLIC_API_URL=http://api:8000
    networks:
      - frontend
    restart: unless-stopped

  # ===========================================
  # Backend API (Python/FastAPI)
  # ===========================================
  api:
    build:
      context: ./api
      dockerfile: Dockerfile
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/myapp
      - REDIS_URL=redis://redis:6379
      - SECRET_KEY=${SECRET_KEY}
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - frontend
      - backend
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # ===========================================
  # PostgreSQL Database
  # ===========================================
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: myapp
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    networks:
      - backend
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # ===========================================
  # Redis Cache
  # ===========================================
  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    networks:
      - backend
    restart: unless-stopped

volumes:
  postgres-data:
  redis-data:

networks:
  frontend:
  backend:
```

## 6. Environment Variables

```yaml
# ═══════════════════════════════════════════════════════════════════════
# ENVIRONMENT VARIABLES
# ═══════════════════════════════════════════════════════════════════════

services:
  api:
    # Inline definition
    environment:
      - NODE_ENV=production
      - DEBUG=false
      - PORT=8000

    # Map syntax
    environment:
      NODE_ENV: production
      DEBUG: "false"
      PORT: "8000"

    # From host environment
    environment:
      - DATABASE_URL                      # Tar värde från host
      - SECRET_KEY=${SECRET_KEY}          # Explicit
      - API_KEY=${API_KEY:-default}       # Med default

    # From file
    env_file:
      - .env
      - .env.local
```

### .env File

```bash
# .env
DATABASE_URL=postgresql://postgres:secret@db:5432/myapp
SECRET_KEY=supersecretkey123
REDIS_URL=redis://redis:6379

# Compose-specifika variabler
COMPOSE_PROJECT_NAME=myproject
COMPOSE_FILE=docker-compose.yml
```

## 7. Praktiska Övningar

### Övning 1: Basic Compose

```bash
# Skapa projektstruktur
mkdir compose-demo && cd compose-demo

# docker-compose.yml
cat << 'EOF' > docker-compose.yml
version: "3.9"

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html:ro
EOF

# HTML fil
mkdir html
echo "<h1>Hello from Compose!</h1>" > html/index.html

# Kör
docker compose up -d

# Testa
curl http://localhost:8080

# Cleanup
docker compose down
```

### Övning 2: Multi-service

```bash
cat << 'EOF' > docker-compose.yml
version: "3.9"

services:
  app:
    image: python:3.11-slim
    command: python -m http.server 8000
    working_dir: /app
    volumes:
      - ./app:/app
    depends_on:
      - redis
    networks:
      - appnet

  redis:
    image: redis:alpine
    networks:
      - appnet

networks:
  appnet:
EOF

mkdir app
echo "Hello from Python!" > app/index.html

docker compose up -d
docker compose ps
docker compose logs app
docker compose down
```

## 8-14. Sammanfattning

### Compose Commands Reference

| Command | Description |
|---------|-------------|
| `docker compose up` | Starta |
| `docker compose down` | Stoppa & ta bort |
| `docker compose build` | Bygg images |
| `docker compose ps` | Lista services |
| `docker compose logs` | Visa logs |
| `docker compose exec` | Kör i container |

---

**Nästa Node:** Compose Advanced →
''',
    "xp_reward": 175,
    "estimated_minutes": 80,
    "prerequisites": ["docker_node_6"],
    "learning_outcomes": [
        "Förstå Docker Compose",
        "Skriva compose files",
        "Hantera multi-container apps",
        "Använda environment variables"
    ]
}

NODE_8 = {
    "id": "docker_node_8",
    "title": "Compose Advanced - Production Features",
    "slug": "compose-advanced-production-features",
    "content": r'''# 🚀 Docker Compose Advanced

## 1. Introduktion & Kontext

Avancerade Compose-funktioner möjliggör professionella deployment-workflows med override-filer, profiles, secrets och production-optimeringar.

### Advanced Compose Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   COMPOSE OVERRIDE PATTERN                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  BASE FILE (docker-compose.yml)                                         │
│  ═══════════════════════════════════════════════════════════════════   │
│  - Gemensam konfiguration                                               │
│  - Service definitions                                                  │
│  - Networks & volumes                                                   │
│                                                                          │
│           │                                                              │
│           │ MERGED WITH                                                  │
│           ▼                                                              │
│                                                                          │
│  ┌─────────────────────┐    ┌─────────────────────┐                    │
│  │ docker-compose.     │    │ docker-compose.     │                    │
│  │ override.yml        │    │ prod.yml            │                    │
│  │                     │    │                     │                    │
│  │ - Dev ports         │    │ - Prod settings     │                    │
│  │ - Volume mounts     │    │ - Resource limits   │                    │
│  │ - Debug mode        │    │ - No ports exposed  │                    │
│  │                     │    │ - Replicas          │                    │
│  └─────────────────────┘    └─────────────────────┘                    │
│                                                                          │
│  USAGE:                                                                  │
│  ─────────────────────────────────────────────────────────────────────  │
│  docker compose up                     # base + override (auto)         │
│  docker compose -f ... -f prod.yml up  # base + prod                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Multiple Compose Files

```yaml
# ═══════════════════════════════════════════════════════════════════════
# docker-compose.yml - BASE
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

services:
  api:
    build:
      context: ./api
    environment:
      - DATABASE_URL=postgresql://db:5432/myapp
    depends_on:
      - db
    networks:
      - backend

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: myapp
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - backend

volumes:
  postgres-data:

networks:
  backend:
```

```yaml
# ═══════════════════════════════════════════════════════════════════════
# docker-compose.override.yml - DEVELOPMENT (auto-loaded)
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

services:
  api:
    build:
      target: development
    volumes:
      - ./api/src:/app/src                 # Hot reload
    ports:
      - "8000:8000"
    environment:
      - DEBUG=true
      - LOG_LEVEL=debug

  db:
    ports:
      - "5432:5432"                         # Expose for local tools
    environment:
      POSTGRES_PASSWORD: devpassword
```

```yaml
# ═══════════════════════════════════════════════════════════════════════
# docker-compose.prod.yml - PRODUCTION
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

services:
  api:
    build:
      target: production
    restart: always
    environment:
      - DEBUG=false
      - LOG_LEVEL=warn
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 1G
        reservations:
          cpus: '1'
          memory: 512M
      replicas: 3

  db:
    restart: always
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 4G

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

```bash
# Användning
docker compose up -d                                  # Dev (auto override)
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d  # Prod
docker compose --profile debug up -d                  # Med profile
```

## 3. Profiles

```yaml
# ═══════════════════════════════════════════════════════════════════════
# COMPOSE PROFILES
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

services:
  api:
    image: myapi:latest
    # Ingen profile = alltid startad

  db:
    image: postgres:15
    # Ingen profile = alltid startad

  adminer:
    image: adminer
    ports:
      - "8080:8080"
    profiles:
      - debug                              # Endast med --profile debug
      - tools

  prometheus:
    image: prom/prometheus
    profiles:
      - monitoring

  grafana:
    image: grafana/grafana
    profiles:
      - monitoring

  test-runner:
    build:
      context: .
      dockerfile: Dockerfile.test
    profiles:
      - test
```

```bash
# Profile användning
docker compose up -d                          # api + db endast
docker compose --profile debug up -d          # api + db + adminer
docker compose --profile monitoring up -d     # api + db + prometheus + grafana
docker compose --profile test up -d           # api + db + test-runner

# Multipla profiles
docker compose --profile debug --profile monitoring up -d
```

## 4. Secrets & Configs

```yaml
# ═══════════════════════════════════════════════════════════════════════
# SECRETS - Sensitive data
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

services:
  api:
    image: myapi:latest
    secrets:
      - db_password
      - api_key
    environment:
      - DB_PASSWORD_FILE=/run/secrets/db_password

  db:
    image: postgres:15
    secrets:
      - db_password
    environment:
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt         # Från fil
  api_key:
    environment: API_KEY                     # Från environment

# ═══════════════════════════════════════════════════════════════════════
# CONFIGS - Configuration files
# ═══════════════════════════════════════════════════════════════════════

services:
  nginx:
    image: nginx:alpine
    configs:
      - source: nginx_config
        target: /etc/nginx/nginx.conf
      - source: ssl_cert
        target: /etc/nginx/ssl/cert.pem

configs:
  nginx_config:
    file: ./nginx/nginx.conf
  ssl_cert:
    file: ./certs/server.crt
```

## 5. Depends On Advanced

```yaml
# ═══════════════════════════════════════════════════════════════════════
# ADVANCED DEPENDENCY MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

services:
  api:
    build: ./api
    depends_on:
      db:
        condition: service_healthy           # Vänta på healthcheck
      redis:
        condition: service_started           # Vänta på start
      migrations:
        condition: service_completed_successfully  # Vänta på completion

  db:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 10
      start_period: 30s

  redis:
    image: redis:alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

  migrations:
    build: ./api
    command: ["python", "manage.py", "migrate"]
    depends_on:
      db:
        condition: service_healthy
```

## 6. Extensions & Anchors (YAML)

```yaml
# ═══════════════════════════════════════════════════════════════════════
# YAML ANCHORS - Återanvänd konfiguration
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

# Define anchor
x-logging: &default-logging
  driver: json-file
  options:
    max-size: "10m"
    max-file: "3"

x-healthcheck: &default-healthcheck
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s

x-common-env: &common-env
  TZ: Europe/Stockholm
  LOG_LEVEL: info

services:
  api:
    image: myapi:latest
    logging: *default-logging               # Use anchor
    environment:
      <<: *common-env                       # Merge anchor
      API_PORT: "8000"
    healthcheck:
      <<: *default-healthcheck
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]

  worker:
    image: myworker:latest
    logging: *default-logging
    environment:
      <<: *common-env
      WORKER_CONCURRENCY: "4"
    healthcheck:
      <<: *default-healthcheck
      test: ["CMD", "celery", "inspect", "ping"]
```

## 7. Production Compose

```yaml
# ═══════════════════════════════════════════════════════════════════════
# PRODUCTION-READY COMPOSE
# ═══════════════════════════════════════════════════════════════════════

version: "3.9"

x-logging: &logging
  driver: json-file
  options:
    max-size: "50m"
    max-file: "5"

services:
  traefik:
    image: traefik:v2.10
    command:
      - "--api.dashboard=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - traefik-certs:/letsencrypt
    logging: *logging
    restart: always
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 256M

  api:
    image: ${REGISTRY}/myapi:${VERSION:-latest}
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.api.rule=Host(`api.example.com`)"
      - "traefik.http.services.api.loadbalancer.server.port=8000"
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - REDIS_URL=${REDIS_URL}
    secrets:
      - api_secret
    logging: *logging
    restart: always
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
      replicas: 2

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
      POSTGRES_DB: production
    secrets:
      - db_password
    volumes:
      - postgres-data:/var/lib/postgresql/data
    logging: *logging
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 4G

volumes:
  postgres-data:
  traefik-certs:

secrets:
  db_password:
    external: true
  api_secret:
    external: true
```

## 8. Praktiska Övningar

### Övning 1: Override Files

```bash
mkdir compose-override && cd compose-override

# Base
cat << 'EOF' > docker-compose.yml
services:
  app:
    image: nginx:alpine
    environment:
      - ENV=base
EOF

# Override
cat << 'EOF' > docker-compose.override.yml
services:
  app:
    ports:
      - "8080:80"
    environment:
      - ENV=development
      - DEBUG=true
EOF

# Test
docker compose config    # Se merged config
docker compose up -d
docker compose exec app env | grep -E "ENV|DEBUG"
docker compose down
```

### Övning 2: Profiles

```bash
cat << 'EOF' > docker-compose.yml
services:
  app:
    image: nginx:alpine
    ports:
      - "8080:80"

  debug:
    image: busybox
    command: sleep infinity
    profiles:
      - debug

  monitoring:
    image: alpine
    command: sleep infinity
    profiles:
      - monitoring
EOF

# Testa profiles
docker compose up -d                         # Endast app
docker compose ps
docker compose --profile debug up -d         # app + debug
docker compose ps
docker compose down
```

## 9-14. Sammanfattning

### Compose File Hierarchy

| File | Auto-loaded | Purpose |
|------|-------------|---------|
| `docker-compose.yml` | Yes | Base config |
| `docker-compose.override.yml` | Yes | Dev overrides |
| `docker-compose.prod.yml` | No | Production |
| `docker-compose.test.yml` | No | Testing |

---

**Nästa Node:** Dockerfile Best Practices →
''',
    "xp_reward": 180,
    "estimated_minutes": 85,
    "prerequisites": ["docker_node_7"],
    "learning_outcomes": [
        "Använda override files",
        "Konfigurera profiles",
        "Hantera secrets",
        "Bygga production-ready compose"
    ]
}

# Block 2 Part 2 exports
BLOCK_2_PART_2_NODES = [NODE_7, NODE_8]
