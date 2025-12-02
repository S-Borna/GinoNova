# =============================================================================
# DOCKER SKILLSMAP - 20 NODER
# Akhilesh Pedagogical Style: Intro → Koncept → Kommandon → Tips → Task
# =============================================================================

DOCKER_SKILLSMAP_INFO = {
    "name": "Docker Mastery",
    "slug": "docker-mastery",
    "description": "Behärska containerisering från grunden till produktion",
    "total_nodes": 20,
    "estimated_hours": 25,
    "difficulty": "intermediate",
    "prerequisites": ["linux-fundamentals"],
    "skills": ["Docker", "Containers", "Images", "Compose", "Networking", "Security"],
}


# =============================================================================
# BLOCK 1: DOCKER FUNDAMENTALS (Noder 1-4)
# =============================================================================

NODE_01_DOCKER_INTRO = {
    "node_id": 1,
    "title": "Docker Introduktion",
    "slug": "docker-intro",
    "estimated_minutes": 45,
    "xp_reward": 100,
    "prerequisites": [],
    "content": '''
# Docker Introduktion

Containers revolutionerade hur vi bygger och deployar applikationer.

## Varför Docker?

| Problem | Docker-lösning |
|---------|----------------|
| "Works on my machine" | Identisk miljö överallt |
| Tunga VMs | Lättvikts-containers |
| Dependency hell | Isolerade beroenden |
| Långsam deploy | Sekunder att starta |

## Installation

```bash
# macOS
brew install --cask docker

# Ubuntu
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# Verifiera
docker --version
docker run hello-world
```

## Grundläggande Kommandon

```bash
# Kör container
docker run nginx

# Lista containers
docker ps        # Körande
docker ps -a     # Alla

# Stoppa/ta bort
docker stop <id>
docker rm <id>
```

## Container vs VM

```
┌─────────────────────────────────────┐
│           Containers                │
├─────────┬─────────┬─────────────────┤
│  App A  │  App B  │     App C       │
├─────────┴─────────┴─────────────────┤
│           Docker Engine             │
├─────────────────────────────────────┤
│           Host OS (Linux)           │
└─────────────────────────────────────┘
```

**Nästa steg:** Node 2 - Docker Images
''',
}

NODE_02_DOCKER_IMAGES = {
    "node_id": 2,
    "title": "Docker Images",
    "slug": "docker-images",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "prerequisites": [1],
    "content": '''
# Docker Images

Images är blueprints för containers.

## Image Kommandon

```bash
# Sök images
docker search python

# Ladda ner image
docker pull python:3.11-slim

# Lista images
docker images

# Ta bort image
docker rmi python:3.11

# Image info
docker inspect python:3.11
```

## Image Naming

```
registry/repository:tag

docker.io/library/python:3.11-slim
└──────┘ └──────┘ └────┘ └────────┘
registry  org     image    tag
```

## Layers

```bash
# Se layers
docker history python:3.11-slim

# Varje instruktion = ny layer
FROM python:3.11-slim     # Layer 1
COPY . /app               # Layer 2
RUN pip install           # Layer 3
```

## Taggar

```bash
# Tagga image
docker tag myapp:latest myapp:v1.0.0
docker tag myapp:latest registry.com/myapp:v1.0.0

# Push till registry
docker push registry.com/myapp:v1.0.0
```

| Tag | Användning |
|-----|-----------|
| latest | Default (undvik i prod) |
| v1.0.0 | Semantisk version |
| sha-abc123 | Git commit |
| slim/alpine | Mindre variant |

**Nästa steg:** Node 3 - Dockerfile Basics
''',
}

NODE_03_DOCKERFILE_BASICS = {
    "node_id": 3,
    "title": "Dockerfile Basics",
    "slug": "dockerfile-basics",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": [2],
    "content": '''
# Dockerfile Basics

Dockerfile definierar hur en image byggs.

## Grundläggande Dockerfile

```dockerfile
# Base image
FROM python:3.11-slim

# Metadata
LABEL maintainer="dev@example.com"

# Arbetskatalog
WORKDIR /app

# Kopiera filer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponera port
EXPOSE 8000

# Startkommando
CMD ["python", "app.py"]
```

## Bygga Image

```bash
# Bygg image
docker build -t myapp:v1 .

# Med annan Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# No cache
docker build --no-cache -t myapp:v1 .
```

## Viktiga Instruktioner

| Instruktion | Syfte |
|-------------|-------|
| FROM | Base image |
| WORKDIR | Sätt arbetskatalog |
| COPY | Kopiera filer |
| RUN | Kör kommando (build-time) |
| CMD | Default kommando (runtime) |
| ENTRYPOINT | Fast startpunkt |
| EXPOSE | Dokumentera port |
| ENV | Miljövariabler |

## RUN vs CMD vs ENTRYPOINT

```dockerfile
# RUN - körs vid build
RUN apt-get update && apt-get install -y curl

# CMD - default kommando (kan överskrivas)
CMD ["python", "app.py"]

# ENTRYPOINT - fast kommando
ENTRYPOINT ["python"]
CMD ["app.py"]  # Argument till ENTRYPOINT
```

**Nästa steg:** Node 4 - Container Lifecycle
''',
}

NODE_04_CONTAINER_LIFECYCLE = {
    "node_id": 4,
    "title": "Container Lifecycle",
    "slug": "container-lifecycle",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [3],
    "content": '''
# Container Lifecycle

Förstå containers livscykel.

## Lifecycle States

```
Created → Running → Paused → Stopped → Removed
```

## Hantera Containers

```bash
# Skapa utan starta
docker create --name myapp nginx

# Starta
docker start myapp

# Pausa/återuppta
docker pause myapp
docker unpause myapp

# Stoppa (graceful)
docker stop myapp

# Döda (force)
docker kill myapp

# Ta bort
docker rm myapp

# Starta och ta bort automatiskt
docker run --rm nginx
```

## Interaktiva Containers

```bash
# Interaktiv terminal
docker run -it ubuntu bash

# Attach till körande container
docker attach myapp

# Exec kommando i container
docker exec -it myapp bash
docker exec myapp ls -la /app
```

## Logs & Stats

```bash
# Se logs
docker logs myapp
docker logs -f myapp        # Follow
docker logs --tail 100 myapp

# Resource usage
docker stats
docker stats myapp

# Inspect container
docker inspect myapp
```

## Cleanup

```bash
# Ta bort stoppade containers
docker container prune

# Ta bort oanvända images
docker image prune

# Ta bort allt oanvänt
docker system prune -a
```

**Nästa steg:** Node 5 - Docker Volumes
''',
}

DOCKER_SKILLSMAP_BLOCK_1 = [
    NODE_01_DOCKER_INTRO,
    NODE_02_DOCKER_IMAGES,
    NODE_03_DOCKERFILE_BASICS,
    NODE_04_CONTAINER_LIFECYCLE,
]


# =============================================================================
# BLOCK 2: VOLUMES & NETWORKING (Noder 5-8)
# =============================================================================

NODE_05_DOCKER_VOLUMES = {
    "node_id": 5,
    "title": "Docker Volumes",
    "slug": "docker-volumes",
    "estimated_minutes": 50,
    "xp_reward": 135,
    "prerequisites": [4],
    "content": '''
# Docker Volumes

Persistent data i Docker.

## Volume-typer

```bash
# Named volume (rekommenderat)
docker volume create mydata
docker run -v mydata:/app/data nginx

# Bind mount (host path)
docker run -v /host/path:/container/path nginx
docker run -v $(pwd):/app nginx

# tmpfs (in-memory)
docker run --tmpfs /tmp nginx
```

## Volume Kommandon

```bash
# Lista volumes
docker volume ls

# Inspektera
docker volume inspect mydata

# Ta bort
docker volume rm mydata

# Ta bort oanvända
docker volume prune
```

## Praktiskt Exempel

```bash
# PostgreSQL med persistent data
docker run -d \\
  --name postgres \\
  -v pgdata:/var/lib/postgresql/data \\
  -e POSTGRES_PASSWORD=secret \\
  postgres:15

# Backup volume
docker run --rm \\
  -v pgdata:/data \\
  -v $(pwd):/backup \\
  alpine tar czf /backup/pgdata.tar.gz /data
```

## Read-only Mounts

```bash
# Read-only
docker run -v myconfig:/etc/config:ro nginx

# Read-write (default)
docker run -v mydata:/data:rw nginx
```

**Nästa steg:** Node 6 - Docker Networking
''',
}

NODE_06_DOCKER_NETWORKING = {
    "node_id": 6,
    "title": "Docker Networking",
    "slug": "docker-networking",
    "estimated_minutes": 55,
    "xp_reward": 145,
    "prerequisites": [5],
    "content": '''
# Docker Networking

Container-kommunikation.

## Network Drivers

| Driver | Användning |
|--------|-----------|
| bridge | Default, isolerat nätverk |
| host | Delad med host |
| none | Ingen nätverksåtkomst |
| overlay | Multi-host (Swarm) |

## Network Kommandon

```bash
# Lista nätverk
docker network ls

# Skapa nätverk
docker network create mynet

# Inspektera
docker network inspect mynet

# Koppla container
docker network connect mynet myapp
docker network disconnect mynet myapp
```

## Container DNS

```bash
# Containers på samma nätverk kan nå varandra via namn
docker network create app-net

docker run -d --name db --network app-net postgres
docker run -d --name api --network app-net myapi

# Inuti api-container:
# postgres://db:5432/mydb  # "db" resolvas automatiskt
```

## Port Mapping

```bash
# Publicera port
docker run -p 8080:80 nginx      # host:container
docker run -p 80 nginx           # Random host port
docker run -P nginx              # Alla EXPOSE:ade portar

# Bind till specifik IP
docker run -p 127.0.0.1:8080:80 nginx
```

## Praktiskt Exempel

```bash
# Frontend + Backend + DB
docker network create myapp

docker run -d --name db \\
  --network myapp \\
  -e POSTGRES_PASSWORD=secret \\
  postgres

docker run -d --name api \\
  --network myapp \\
  -e DATABASE_URL=postgres://db:5432 \\
  myapi

docker run -d --name web \\
  --network myapp \\
  -p 80:80 \\
  -e API_URL=http://api:3000 \\
  myfrontend
```

**Nästa steg:** Node 7 - Docker Compose Basics
''',
}

NODE_07_COMPOSE_BASICS = {
    "node_id": 7,
    "title": "Docker Compose Basics",
    "slug": "compose-basics",
    "estimated_minutes": 60,
    "xp_reward": 155,
    "prerequisites": [6],
    "content": '''
# Docker Compose Basics

Multi-container applikationer.

## docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - API_URL=http://api:8000
    depends_on:
      - api

  api:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgres://db:5432/app
    depends_on:
      - db

  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=secret

volumes:
  pgdata:
```

## Compose Kommandon

```bash
# Starta alla services
docker compose up
docker compose up -d          # Detached

# Stoppa
docker compose down
docker compose down -v        # + ta bort volumes

# Bygg om images
docker compose build
docker compose up --build

# Logs
docker compose logs
docker compose logs -f api

# Skala services
docker compose up -d --scale api=3
```

## Service Kommandon

```bash
# Kör kommando i service
docker compose exec api bash
docker compose exec db psql -U postgres

# Starta enskild service
docker compose up -d db

# Restart
docker compose restart api
```

**Nästa steg:** Node 8 - Docker Compose Advanced
''',
}

NODE_08_COMPOSE_ADVANCED = {
    "node_id": 8,
    "title": "Docker Compose Advanced",
    "slug": "compose-advanced",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [7],
    "content": '''
# Docker Compose Advanced

Avancerade Compose-features.

## Miljövariabler

```yaml
# .env fil
services:
  api:
    environment:
      - DB_HOST=${DB_HOST:-localhost}
    env_file:
      - .env
      - .env.local
```

## Health Checks

```yaml
services:
  api:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  db:
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
```

## Depends On med Condition

```yaml
services:
  api:
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
```

## Profiles

```yaml
services:
  web:
    profiles: ["frontend"]
  
  api:
    profiles: ["backend", "full"]
  
  debug:
    profiles: ["debug"]
    image: busybox

# docker compose --profile backend up
```

## Override Files

```yaml
# docker-compose.yml (base)
services:
  api:
    image: myapi:latest

# docker-compose.override.yml (dev - auto-loaded)
services:
  api:
    build: .
    volumes:
      - ./src:/app/src

# docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

## Networks & Aliases

```yaml
services:
  api:
    networks:
      frontend:
        aliases:
          - backend-api
      backend:

networks:
  frontend:
  backend:
    internal: true  # Ingen extern åtkomst
```

**Nästa steg:** Node 9 - Dockerfile Best Practices
''',
}

DOCKER_SKILLSMAP_BLOCK_2 = [
    NODE_05_DOCKER_VOLUMES,
    NODE_06_DOCKER_NETWORKING,
    NODE_07_COMPOSE_BASICS,
    NODE_08_COMPOSE_ADVANCED,
]

# Block 3-5 kommer i nästa commits
