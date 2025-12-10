# =============================================================================
# DOCKER COMPOSE — Noder 13-16
# Premium Bootcamp-Quality Content
# =============================================================================

NODE_13_COMPOSE_BASICS = {
    "id": "docker-compose-basics",
    "node_id": 13,
    "title": "Docker Compose Fundamentals",
    "slug": "docker-compose-basics",
    "description": "Definiera och kör multi-container applikationer med Compose",
    "type": "concept",
    "difficulty": "medium",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": [12],
    "content": '''# 🐙 Docker Compose Fundamentals

## Lärande mål
- Förstå varför Docker Compose behövs
- Skriva docker-compose.yml från scratch
- Hantera multi-container applikationer
- Använda compose-kommandon effektivt

---

## 📖 Varför Docker Compose?

### Utan Compose — Kaos

```bash
# Starta 5 containers manuellt...
docker network create myapp
docker volume create postgres_data
docker run -d --name postgres --network myapp -v postgres_data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=secret postgres:15
docker run -d --name redis --network myapp redis:7
docker run -d --name api --network myapp -e DATABASE_URL=postgres://... myapi:1.0
docker run -d --name worker --network myapp myworker:1.0
docker run -d --name nginx --network myapp -p 80:80 mynginx:1.0

# Städa upp...
docker stop postgres redis api worker nginx
docker rm postgres redis api worker nginx
docker network rm myapp
docker volume rm postgres_data
```

### Med Compose — Enkelt

```yaml
# docker-compose.yml
services:
  postgres:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: secret

  redis:
    image: redis:7

  api:
    build: ./api
    depends_on:
      - postgres
      - redis

  worker:
    build: ./worker
    depends_on:
      - redis

  nginx:
    build: ./nginx
    ports:
      - "80:80"
    depends_on:
      - api

volumes:
  postgres_data:
```

```bash
# Starta allt
docker compose up -d

# Städa upp
docker compose down
```

---

## 📝 Compose File Syntax

### Version och Services

```yaml
# docker-compose.yml (modern format - ingen version behövs)
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"

  api:
    build: ./api
    environment:
      NODE_ENV: production
```

### Build vs Image

```yaml
services:
  # Använd befintlig image
  redis:
    image: redis:7-alpine

  # Bygg från Dockerfile
  api:
    build: ./api

  # Bygg med options
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.prod
      args:
        NODE_ENV: production
```

### Environment

```yaml
services:
  api:
    image: myapi:1.0

    # Inline
    environment:
      NODE_ENV: production
      DATABASE_URL: postgres://...

    # Eller från fil
    env_file:
      - .env
      - .env.local
```

### Volumes

```yaml
services:
  postgres:
    image: postgres:15
    volumes:
      # Named volume (persistent)
      - postgres_data:/var/lib/postgresql/data
      # Bind mount (development)
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  postgres_data:  # Deklarera named volumes
```

### Ports

```yaml
services:
  web:
    ports:
      - "80:80"         # HOST:CONTAINER
      - "443:443"
      - "8080"          # Random host port
      - "127.0.0.1:3000:3000"  # Endast localhost
```

### Networks

```yaml
services:
  api:
    networks:
      - frontend
      - backend

  postgres:
    networks:
      - backend

networks:
  frontend:
  backend:
    internal: true  # Ingen extern åtkomst
```

### Depends On

```yaml
services:
  api:
    depends_on:
      - postgres
      - redis
    # Startar efter postgres och redis
    # MEN väntar inte på att de är "ready"

  # Med health check
  api:
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started
```

---

## 🛠️ Compose Kommandon

```bash
# Starta
docker compose up              # Förgrund
docker compose up -d           # Bakgrund (detached)
docker compose up --build      # Bygg om images

# Stoppa
docker compose stop            # Stoppa containers
docker compose down            # Stoppa och ta bort
docker compose down -v         # + ta bort volumes
docker compose down --rmi all  # + ta bort images

# Status
docker compose ps              # Lista services
docker compose logs            # Visa loggar
docker compose logs -f api     # Följ specifik service

# Skalning
docker compose up -d --scale api=3

# Kör kommandon
docker compose exec api bash
docker compose run --rm api npm test
```

---

## 🎯 Komplett exempel

### Projektstruktur

```
myproject/
+-- docker-compose.yml
+-- api/
|   +-- Dockerfile
|   +-- package.json
|   +-- src/
+-- frontend/
|   +-- Dockerfile
|   +-- src/
+-- .env
```

### docker-compose.yml

```yaml
services:
  # Database
  postgres:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: myapp
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myapp"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Cache
  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data

  # API
  api:
    build:
      context: ./api
      target: production
    environment:
      DATABASE_URL: postgres://myapp:${DB_PASSWORD}@postgres:5432/myapp
      REDIS_URL: redis://redis:6379
      NODE_ENV: production
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started
    restart: unless-stopped

  # Frontend
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - api
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
```

### .env

```env
DB_PASSWORD=supersecret123
```

---

## 🏋️ Övningar

### Övning: Full-stack app
```bash
mkdir compose-demo && cd compose-demo

# Skapa docker-compose.yml
cat > docker-compose.yml << 'EOF'
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html

  api:
    image: python:3.11-alpine
    command: python -m http.server 5000
    working_dir: /app
    volumes:
      - ./api:/app
EOF

# Skapa content
mkdir -p html api
echo "<h1>Hello Compose!</h1>" > html/index.html
echo "print('API ready')" > api/app.py

# Starta
docker compose up -d

# Testa
curl localhost:8080

# Städa
docker compose down
```

---

**Nästa steg:** Node 14 - Docker Compose for Development
''',
}


NODE_14_COMPOSE_DEVELOPMENT = {
    "id": "compose-development",
    "node_id": 14,
    "title": "Docker Compose for Development",
    "slug": "compose-development",
    "description": "Optimera Compose för snabb och smidig utveckling",
    "type": "practice",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [13],
    "content": '''# 💻 Docker Compose for Development

## Lärande mål
- Konfigurera hot-reload för alla språk
- Debugga containers effektivt
- Hantera development vs production configs
- Optimera build-tider

---

## 🔥 Hot Reload Setup

### Node.js

```yaml
services:
  api:
    build: ./api
    volumes:
      - ./api/src:/app/src          # Synka källkod
      - /app/node_modules           # Behåll container-node_modules
    command: npm run dev            # Nodemon/ts-node-dev
    environment:
      NODE_ENV: development
```

### Python

```yaml
services:
  api:
    build: ./api
    volumes:
      - ./api:/app
    command: uvicorn main:app --reload --host 0.0.0.0
    environment:
      PYTHONDONTWRITEBYTECODE: 1
```

### React/Next.js

```yaml
services:
  frontend:
    build: ./frontend
    volumes:
      - ./frontend/src:/app/src
      - ./frontend/public:/app/public
      - /app/node_modules
      - /app/.next            # Cache
    ports:
      - "3000:3000"
    environment:
      WATCHPACK_POLLING: "true"  # För Docker Desktop
```

---

## 🐛 Debugging

### Attach debugger

```yaml
services:
  api:
    build: ./api
    ports:
      - "3000:3000"
      - "9229:9229"  # Node.js debug port
    command: node --inspect=0.0.0.0:9229 src/index.js
```

### VS Code launch.json

```json
{
  "type": "node",
  "request": "attach",
  "name": "Docker: Attach",
  "port": 9229,
  "remoteRoot": "/app",
  "localRoot": "${workspaceFolder}/api"
}
```

---

## 📁 Multiple Compose Files

### Override pattern

```bash
myproject/
+-- docker-compose.yml          # Base config
+-- docker-compose.override.yml # Dev (auto-loaded)
+-- docker-compose.prod.yml     # Production
```

### docker-compose.yml (base)

```yaml
services:
  api:
    build: ./api
    depends_on:
      - postgres

  postgres:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### docker-compose.override.yml (dev)

```yaml
services:
  api:
    volumes:
      - ./api/src:/app/src
    ports:
      - "3000:3000"
      - "9229:9229"
    environment:
      NODE_ENV: development

  postgres:
    ports:
      - "5432:5432"  # Expose för lokala tools
```

### docker-compose.prod.yml

```yaml
services:
  api:
    image: myregistry/api:${VERSION}
    restart: always
    deploy:
      replicas: 3
    environment:
      NODE_ENV: production
```

### Användning

```bash
# Development (auto-laddar override)
docker compose up

# Production
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

---

## ⚡ Performance Tips

### 1. Cache node_modules

```yaml
services:
  api:
    volumes:
      - ./api:/app
      - api_node_modules:/app/node_modules

volumes:
  api_node_modules:
```

### 2. Build cache

```bash
# Använd BuildKit
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker compose build
```

### 3. Bind mount specifika filer

```yaml
volumes:
  - ./src:/app/src      # ✅ Specifik
  - ./:/app             # ❌ Hela projektet (långsamt)
```

---

**Nästa steg:** Node 15 - Docker Compose for Production
''',
}


NODE_15_COMPOSE_PRODUCTION = {
    "id": "compose-production",
    "node_id": 15,
    "title": "Docker Compose for Production",
    "slug": "compose-production",
    "description": "Säkra och robusta Compose-konfigurationer för produktion",
    "type": "practice",
    "difficulty": "hard",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [14],
    "content": '''# 🚀 Docker Compose for Production

## Lärande mål
- Konfigurera produktion-säkra services
- Implementera health checks
- Hantera secrets och environment
- Sätta upp logging och monitoring

---

## 🔒 Production Configuration

### Health Checks

```yaml
services:
  api:
    image: myapi:1.0
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    restart: unless-stopped

  postgres:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
```

### Resource Limits

```yaml
services:
  api:
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M
```

### Restart Policies

```yaml
services:
  api:
    restart: unless-stopped
    # Alternativ:
    # - "no"
    # - "always"
    # - "on-failure"
    # - "unless-stopped"
```

---

## 🔐 Secrets Management

### Environment Variables

```yaml
services:
  api:
    environment:
      DB_PASSWORD: ${DB_PASSWORD}
    # Eller
    env_file:
      - .env.production
```

### Docker Secrets (Swarm mode)

```yaml
services:
  api:
    secrets:
      - db_password
    environment:
      DB_PASSWORD_FILE: /run/secrets/db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

---

## 📊 Logging

### Centralized Logging

```yaml
services:
  api:
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  # Eller extern logging
  api:
    logging:
      driver: "fluentd"
      options:
        fluentd-address: "localhost:24224"
```

---

## 🎯 Production-Ready docker-compose.prod.yml

```yaml
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
    depends_on:
      api:
        condition: service_healthy
    restart: always
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  api:
    image: myregistry/api:${VERSION:-latest}
    environment:
      NODE_ENV: production
      DATABASE_URL: postgres://app:${DB_PASSWORD}@postgres:5432/app
    depends_on:
      postgres:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          memory: 512M
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: "50m"
        max-file: "5"

  postgres:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: app
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: always

volumes:
  postgres_data:
```

---

**Nästa steg:** Node 16 - Docker Compose Advanced Patterns
''',
}


NODE_16_COMPOSE_ADVANCED = {
    "id": "compose-advanced",
    "node_id": 16,
    "title": "Docker Compose Advanced Patterns",
    "slug": "compose-advanced",
    "description": "Avancerade mönster och tekniker för komplexa deployments",
    "type": "deep_dive",
    "difficulty": "hard",
    "estimated_minutes": 60,
    "xp_reward": 160,
    "prerequisites": [15],
    "content": '''# 🎯 Docker Compose Advanced Patterns

## Lärande mål
- Implementera avancerade deployment-mönster
- Använda profiles för olika miljöer
- Sätta upp zero-downtime deployments
- Hantera komplext state

---

## 📋 Profiles

```yaml
services:
  api:
    image: myapi:1.0

  postgres:
    image: postgres:15

  # Endast för development
  adminer:
    image: adminer
    profiles:
      - debug
    ports:
      - "8080:8080"

  # Endast för testing
  test-runner:
    image: myapi:test
    profiles:
      - test
    command: npm test
```

```bash
# Starta utan profiles
docker compose up

# Starta med debug profile
docker compose --profile debug up

# Flera profiles
docker compose --profile debug --profile test up
```

---

## 🔄 Zero-Downtime Deployment

### Blue-Green med Compose

```yaml
services:
  nginx:
    image: nginx
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - "80:80"

  api-blue:
    image: myapi:${BLUE_VERSION}

  api-green:
    image: myapi:${GREEN_VERSION}
```

```bash
# Deploy ny version
docker compose up -d api-green

# Testa
curl http://api-green:3000/health

# Switch traffic (uppdatera nginx.conf)
docker compose exec nginx nginx -s reload

# Ta bort gammal
docker compose stop api-blue
```

---

## 📦 Extensions (x-*)

### Reusable Blocks

```yaml
x-common: &common
  restart: unless-stopped
  logging:
    driver: json-file
    options:
      max-size: "10m"

x-api-env: &api-env
  NODE_ENV: production
  LOG_LEVEL: info

services:
  api-1:
    <<: *common
    image: myapi:1.0
    environment:
      <<: *api-env

  api-2:
    <<: *common
    image: myapi:1.0
    environment:
      <<: *api-env
```

---

## 🔗 Service Dependencies

### Wait-for patterns

```yaml
services:
  api:
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started
      migrations:
        condition: service_completed_successfully

  migrations:
    image: myapi:1.0
    command: npm run migrate
```

---

## 📊 Scaling

```bash
# Skala service
docker compose up -d --scale api=3

# Med load balancer
docker compose up -d --scale api=3 nginx
```

```yaml
services:
  nginx:
    image: nginx
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - api

  api:
    image: myapi:1.0
    # deploy.replicas ignoreras utan Swarm
```

---

**Nästa steg:** Node 17 - Docker in Production
''',
}


NODES = [
    NODE_13_COMPOSE_BASICS,
    NODE_14_COMPOSE_DEVELOPMENT,
    NODE_15_COMPOSE_PRODUCTION,
    NODE_16_COMPOSE_ADVANCED,
]
