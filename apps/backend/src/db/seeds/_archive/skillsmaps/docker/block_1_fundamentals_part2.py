# =============================================================================
# DOCKER MASTERY V3 - BLOCK 1 PART 2: DOCKERFILE & CONTAINER LIFECYCLE
# Noder 3-4 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
DOCKER BLOCK 1 PART 2 - BUILDING & RUNNING
==========================================
Node 3: Dockerfile Basics - Building Images
Node 4: Container Lifecycle - Management
"""

NODE_3 = {
    "id": "docker_node_3",
    "title": "Dockerfile Basics - Building Images",
    "slug": "dockerfile-basics-building-images",
    "content": r'''# 🏗️ Dockerfile Basics - Building Images

## 1. Introduktion & Kontext

En Dockerfile är en textfil med instruktioner för att bygga en Docker image. Den definierar exakt hur din applikation ska paketeras, från base image till slutgiltigt kommando.

### Dockerfile Anatomy

```
+-------------------------------------------------------------------------+
|                      DOCKERFILE ANATOMY                                  |
+-------------------------------------------------------------------------+
|                                                                          |
|  # Comment - dokumentation                                               |
|  ---------------------------------------------------------------------- |
|                                                                          |
|  FROM python:3.11-slim          # Base image (REQUIRED, alltid först)   |
|                                                                          |
|  LABEL maintainer="dev@co.com"  # Metadata                              |
|  LABEL version="1.0"                                                    |
|                                                                          |
|  ENV PYTHONDONTWRITEBYTECODE=1  # Environment variables                 |
|  ENV PYTHONUNBUFFERED=1                                                 |
|                                                                          |
|  WORKDIR /app                   # Sätt working directory                |
|                                                                          |
|  COPY requirements.txt .        # Kopiera dependencies först            |
|  RUN pip install --no-cache-dir -r requirements.txt  # Installera      |
|                                                                          |
|  COPY . .                       # Kopiera applikationskod               |
|                                                                          |
|  EXPOSE 8000                    # Dokumentera port (öppnar inte!)       |
|                                                                          |
|  USER appuser                   # Byt till non-root user                |
|                                                                          |
|  CMD ["python", "app.py"]       # Default command                       |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Dockerfile Instructions

```
+-------------------------------------------------------------------------+
|                   DOCKERFILE INSTRUCTIONS                                |
+-------------------------------------------------------------------------+
|                                                                          |
|  INSTRUCTION    | PURPOSE                  | EXAMPLE                    |
|  ---------------------------------------------------------------------  |
|  FROM           | Base image              | FROM python:3.11-slim       |
|  LABEL          | Metadata                | LABEL version="1.0"         |
|  ENV            | Environment vars        | ENV NODE_ENV=production     |
|  ARG            | Build-time vars         | ARG VERSION=1.0             |
|  WORKDIR        | Working directory       | WORKDIR /app                |
|  COPY           | Copy files              | COPY src/ /app/src/         |
|  ADD            | Copy + extract + URL    | ADD app.tar.gz /app/        |
|  RUN            | Execute command         | RUN pip install flask       |
|  EXPOSE         | Document port           | EXPOSE 8080                 |
|  USER           | Set user                | USER appuser                |
|  CMD            | Default command         | CMD ["python", "app.py"]    |
|  ENTRYPOINT     | Fixed entrypoint        | ENTRYPOINT ["python"]       |
|  VOLUME         | Mount point             | VOLUME /data                |
|  HEALTHCHECK    | Health check            | HEALTHCHECK CMD curl ...    |
|  SHELL          | Default shell           | SHELL ["/bin/bash", "-c"]   |
|  STOPSIGNAL     | Stop signal             | STOPSIGNAL SIGTERM          |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 3. COPY vs ADD

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# COPY - Preferred for most cases
# ═══════════════════════════════════════════════════════════════════════

# Kopiera en fil
COPY app.py /app/

# Kopiera katalog
COPY src/ /app/src/

# Kopiera med wildcard
COPY *.py /app/

# Kopiera med ownership
COPY --chown=appuser:appgroup app.py /app/

# ═══════════════════════════════════════════════════════════════════════
# ADD - Special features (använd sparsamt)
# ═══════════════════════════════════════════════════════════════════════

# Automatic tar extraction
ADD app.tar.gz /app/           # Extraheras automatiskt

# Download from URL (undvik - använd curl i RUN istället)
ADD https://example.com/file /app/

# ⚠️ RECOMMENDATION: Använd COPY om du inte behöver ADD:s features
# COPY är mer explicit och förutsägbar
```

## 4. RUN vs CMD vs ENTRYPOINT

```
+-------------------------------------------------------------------------+
|                 RUN vs CMD vs ENTRYPOINT                                 |
+-------------------------------------------------------------------------+
|                                                                          |
|  RUN - Körs vid BUILD time                                               |
|  ---------------------------------------------------------------------  |
|  RUN apt-get update                    # Skapar ny layer               |
|  RUN pip install flask                 # Installerar under build       |
|  RUN chmod +x /app/entrypoint.sh       # Körs EN gång vid build        |
|                                                                          |
|  CMD - Default command vid RUNTIME (kan överskrivas)                     |
|  ---------------------------------------------------------------------  |
|  CMD ["python", "app.py"]              # Exec form (preferred)          |
|  CMD python app.py                     # Shell form                     |
|                                                                          |
|  docker run myapp                      # Kör CMD: python app.py         |
|  docker run myapp bash                 # CMD ersätts med: bash          |
|                                                                          |
|  ENTRYPOINT - Fast command (svårt att överskrivas)                       |
|  ---------------------------------------------------------------------  |
|  ENTRYPOINT ["python"]                 # Fast startpunkt               |
|  CMD ["app.py"]                        # Default argument              |
|                                                                          |
|  docker run myapp                      # Kör: python app.py            |
|  docker run myapp script.py            # Kör: python script.py         |
|  docker run --entrypoint bash myapp    # Override entrypoint           |
|                                                                          |
|  KOMBINATIONER:                                                          |
|  ---------------------------------------------------------------------  |
|  ENTRYPOINT ["python"]                                                   |
|  CMD ["app.py"]                                                         |
|  # Resultat: python app.py                                              |
|                                                                          |
|  ENTRYPOINT ["/entrypoint.sh"]                                          |
|  CMD ["--help"]                                                         |
|  # Resultat: /entrypoint.sh --help                                      |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 5. Shell Form vs Exec Form

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# SHELL FORM - Körs via /bin/sh -c
# ═══════════════════════════════════════════════════════════════════════

RUN apt-get update && apt-get install -y curl
CMD python app.py
ENTRYPOINT python app.py

# Pros:
# - Environment variable expansion
# - Shell features (pipes, wildcards)

# Cons:
# - Startar extra shell process
# - Signalhantering kan misslyckas
# - PID 1 blir shell, inte din app

# ═══════════════════════════════════════════════════════════════════════
# EXEC FORM - Direkt execution (RECOMMENDED)
# ═══════════════════════════════════════════════════════════════════════

RUN ["apt-get", "update"]
CMD ["python", "app.py"]
ENTRYPOINT ["python", "app.py"]

# Pros:
# - Ingen extra shell process
# - Din app får PID 1
# - Korrekt signalhantering (SIGTERM)
# - Snabbare startup

# Cons:
# - Ingen shell expansion (måste vara explicit)

# ⚠️ RECOMMENDATION: Använd EXEC form för CMD och ENTRYPOINT
```

## 6. Practical Dockerfiles

### Python Application

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# PYTHON APPLICATION
# ═══════════════════════════════════════════════════════════════════════

FROM python:3.11-slim-bookworm

# Metadata
LABEL maintainer="dev@example.com"
LABEL version="1.0"

# Python optimization
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY --chown=appuser:appgroup . .

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Node.js Application

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# NODE.JS APPLICATION
# ═══════════════════════════════════════════════════════════════════════

FROM node:20-slim

ENV NODE_ENV=production

WORKDIR /app

# Copy package files first (better caching)
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production && npm cache clean --force

# Copy application
COPY --chown=node:node . .

USER node

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=10s \
    CMD node -e "require('http').get('http://localhost:3000/health')"

CMD ["node", "server.js"]
```

## 7. Build Commands

```bash
# ═══════════════════════════════════════════════════════════════════════
# DOCKER BUILD
# ═══════════════════════════════════════════════════════════════════════

# Basic build
docker build -t myapp .

# Build with tag
docker build -t myapp:v1.0.0 .
docker build -t myapp:v1.0.0 -t myapp:latest .

# Build from different Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# Build with build arguments
docker build --build-arg VERSION=1.0.0 -t myapp .

# Build without cache
docker build --no-cache -t myapp .

# Build with specific target (multi-stage)
docker build --target builder -t myapp:builder .

# Build and show output
docker build --progress=plain -t myapp .

# ═══════════════════════════════════════════════════════════════════════
# BUILDX (Advanced)
# ═══════════════════════════════════════════════════════════════════════

# Enable BuildKit (default i Docker 23+)
export DOCKER_BUILDKIT=1

# Build med buildx
docker buildx build -t myapp .

# Multi-platform build
docker buildx build --platform linux/amd64,linux/arm64 -t myapp .

# Build and push
docker buildx build --push -t registry.com/myapp:v1 .
```

## 8. .dockerignore

```bash
# ═══════════════════════════════════════════════════════════════════════
# .dockerignore - Exkludera filer från build context
# ═══════════════════════════════════════════════════════════════════════

# Version control
.git
.gitignore
.svn

# IDE
.vscode
.idea
*.swp
*.swo

# Python
__pycache__
*.py[cod]
*$py.class
.Python
.venv
venv
env
.eggs
*.egg-info

# Node.js
node_modules
npm-debug.log
yarn-error.log

# Build artifacts
dist
build
*.tar.gz

# Tests
tests
test
*.test.js
pytest.ini

# Documentation
docs
*.md
!README.md

# Docker
Dockerfile*
docker-compose*.yml
.docker

# Environment
.env
.env.*
*.local

# Logs
logs
*.log

# OS
.DS_Store
Thumbs.db
```

## 9. Praktiska Övningar

### Övning 1: Enkel Python App

```bash
# Skapa projektstruktur
mkdir docker-demo && cd docker-demo

# Python app
cat << 'EOF' > app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Docker!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF

# Requirements
cat << 'EOF' > requirements.txt
flask==3.0.0
gunicorn==21.2.0
EOF

# Dockerfile
cat << 'EOF' > Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
EOF

# .dockerignore
cat << 'EOF' > .dockerignore
.git
__pycache__
*.pyc
.venv
.env
EOF

# Bygg och kör
docker build -t flask-demo .
docker run -d -p 5000:5000 --name flask-app flask-demo

# Testa
curl http://localhost:5000
curl http://localhost:5000/health

# Cleanup
docker stop flask-app && docker rm flask-app
```

### Övning 2: Build Arguments

```dockerfile
# Dockerfile med ARG
FROM python:3.11-slim

ARG APP_VERSION=development
ARG BUILD_DATE

LABEL version="${APP_VERSION}"
LABEL build_date="${BUILD_DATE}"

ENV APP_VERSION=${APP_VERSION}

WORKDIR /app
COPY . .

CMD ["python", "-c", "import os; print(f'Version: {os.environ[\"APP_VERSION\"]}')"]
```

```bash
# Bygg med arguments
docker build \
  --build-arg APP_VERSION=1.2.3 \
  --build-arg BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ") \
  -t myapp:1.2.3 .

# Verifiera
docker run myapp:1.2.3
docker inspect myapp:1.2.3 | jq '.[0].Config.Labels'
```

## 10. Best Practices

```
+-------------------------------------------------------------------------+
|                 DOCKERFILE BEST PRACTICES                                |
+-------------------------------------------------------------------------+
|                                                                          |
|  ✅ Base Image                                                          |
|     □ Använd specifika tags (aldrig :latest)                           |
|     □ Välj slim/alpine för produktion                                  |
|     □ Använd official images                                           |
|                                                                          |
|  ✅ Layer Optimization                                                  |
|     □ Kombinera RUN-kommandon                                          |
|     □ Ordna instruktioner för caching                                  |
|     □ Ta bort temporary files i samma layer                            |
|                                                                          |
|  ✅ Security                                                            |
|     □ Använd non-root USER                                             |
|     □ Scanna images för vulnerabilities                                |
|     □ Minimera installed packages                                      |
|                                                                          |
|  ✅ Clarity                                                             |
|     □ Dokumentera med LABEL och kommentarer                            |
|     □ Använd .dockerignore                                             |
|     □ EXPOSE dokumenterade portar                                      |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 11-14. Sammanfattning

### Dockerfile Checklist

| Step | Instruction | Purpose |
|------|-------------|---------|
| 1 | FROM | Base image |
| 2 | LABEL | Metadata |
| 3 | ENV | Config |
| 4 | RUN | Install deps |
| 5 | COPY | Add code |
| 6 | USER | Security |
| 7 | EXPOSE | Document |
| 8 | CMD | Run |

---

**Nästa Node:** Container Lifecycle ->
''',
    "xp_reward": 160,
    "estimated_minutes": 65,
    "prerequisites": ["docker_node_2"],
    "learning_outcomes": [
        "Skriva Dockerfiles",
        "Förstå build process",
        "Optimera layer caching",
        "Använda best practices"
    ]
}

NODE_4 = {
    "id": "docker_node_4",
    "title": "Container Lifecycle - Management",
    "slug": "container-lifecycle-management",
    "content": r'''# 🔄 Container Lifecycle - Management

## 1. Introduktion & Kontext

Att förstå container lifecycle är kritiskt för att effektivt hantera och felsöka Docker-containers. En container går genom flera states från skapande till borttagning.

### Container States

```
+-------------------------------------------------------------------------+
|                     CONTAINER LIFECYCLE STATES                           |
+-------------------------------------------------------------------------+
|                                                                          |
|                          docker create                                   |
|                               |                                          |
|                               ▼                                          |
|  +-----------------------------------------------------------------+   |
|  |                        CREATED                                   |   |
|  |                   Container exists but                           |   |
|  |                   not yet started                                |   |
|  +------------------------+----------------------------------------+   |
|                           |                                             |
|                    docker start                                         |
|                           |                                             |
|                           ▼                                             |
|  +-----------------------------------------------------------------+   |
|  |                        RUNNING                                   |   |
|  |                   Container executing                            |   |
|  |                   main process                                   |   |
|  +-----+-----------------+-----------------+-----------------------+   |
|        |                 |                 |                            |
|  docker pause      docker stop       Process exits                      |
|        |                 |                 |                            |
|        ▼                 ▼                 ▼                            |
|  +----------+     +----------+     +----------+                        |
|  |  PAUSED  |     | STOPPING |     |  EXITED  |                        |
|  |          |     |          |     | (code)   |                        |
|  +----+-----+     +----+-----+     +----+-----+                        |
|       |                |                |                               |
| docker unpause   SIGTERM->SIGKILL   docker start                        |
|       |                |                |                               |
|       ▼                ▼                ▼                               |
|  +-----------------------------------------------------------------+   |
|  |                     RUNNING / EXITED                             |   |
|  +------------------------+----------------------------------------+   |
|                           |                                             |
|                      docker rm                                          |
|                           |                                             |
|                           ▼                                             |
|  +-----------------------------------------------------------------+   |
|  |                       REMOVED                                    |   |
|  |                  Container deleted                               |   |
|  +-----------------------------------------------------------------+   |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Lifecycle Commands

```bash
# ═══════════════════════════════════════════════════════════════════════
# CREATE - Skapa container utan att starta
# ═══════════════════════════════════════════════════════════════════════

docker create --name myapp nginx:alpine
docker create --name db -e POSTGRES_PASSWORD=secret postgres:15

# Verifiera
docker ps -a    # Status: Created

# ═══════════════════════════════════════════════════════════════════════
# START - Starta befintlig container
# ═══════════════════════════════════════════════════════════════════════

docker start myapp
docker start -a myapp          # Attach output
docker start -i myapp          # Interactive

# ═══════════════════════════════════════════════════════════════════════
# RUN - Create + Start i ett steg
# ═══════════════════════════════════════════════════════════════════════

docker run nginx:alpine                      # Förgrund
docker run -d nginx:alpine                   # Bakgrund (detached)
docker run -d --name web nginx:alpine        # Namnge
docker run --rm nginx:alpine cat /etc/hosts  # Auto-remove vid exit

# ═══════════════════════════════════════════════════════════════════════
# STOP - Graceful shutdown
# ═══════════════════════════════════════════════════════════════════════

docker stop myapp              # SIGTERM -> wait 10s -> SIGKILL
docker stop -t 30 myapp        # Custom timeout (30s)
docker stop $(docker ps -q)    # Stoppa alla körande

# ═══════════════════════════════════════════════════════════════════════
# KILL - Force shutdown
# ═══════════════════════════════════════════════════════════════════════

docker kill myapp              # SIGKILL (omedelbar)
docker kill -s SIGTERM myapp   # Specifik signal

# ═══════════════════════════════════════════════════════════════════════
# RESTART
# ═══════════════════════════════════════════════════════════════════════

docker restart myapp
docker restart -t 10 myapp     # Custom stop timeout

# ═══════════════════════════════════════════════════════════════════════
# PAUSE / UNPAUSE
# ═══════════════════════════════════════════════════════════════════════

docker pause myapp             # Freeze (SIGSTOP)
docker unpause myapp           # Resume

# ═══════════════════════════════════════════════════════════════════════
# REMOVE
# ═══════════════════════════════════════════════════════════════════════

docker rm myapp                # Ta bort stoppad container
docker rm -f myapp             # Force (stoppar först)
docker rm -v myapp             # + ta bort anonymous volumes
docker container prune         # Ta bort alla stoppade
```

## 3. Interactive Containers

```bash
# ═══════════════════════════════════════════════════════════════════════
# INTERACTIVE MODE (-it)
# ═══════════════════════════════════════════════════════════════════════

# -i (--interactive): Keep STDIN open
# -t (--tty): Allocate pseudo-TTY

# Starta interaktiv container
docker run -it ubuntu:22.04 bash
docker run -it --rm python:3.11 python

# Inuti containern:
# Ctrl+D eller exit -> Avsluta och stoppa
# Ctrl+P, Ctrl+Q    -> Detach utan att stoppa

# ═══════════════════════════════════════════════════════════════════════
# ATTACH - Anslut till körande container
# ═══════════════════════════════════════════════════════════════════════

docker attach myapp            # Anslut till main process
# ⚠️ Ctrl+C stoppar containern!

# ═══════════════════════════════════════════════════════════════════════
# EXEC - Kör kommando i körande container
# ═══════════════════════════════════════════════════════════════════════

# Exec one-off command
docker exec myapp ls -la /app
docker exec myapp cat /etc/hosts
docker exec myapp env

# Interaktiv shell
docker exec -it myapp bash
docker exec -it myapp sh       # Om ingen bash

# Som specifik user
docker exec -u root myapp whoami
docker exec -u 0 myapp id

# Med environment variable
docker exec -e DEBUG=true myapp ./script.sh

# Med working directory
docker exec -w /tmp myapp pwd
```

## 4. Logs & Monitoring

```bash
# ═══════════════════════════════════════════════════════════════════════
# LOGS
# ═══════════════════════════════════════════════════════════════════════

docker logs myapp              # Alla logs
docker logs -f myapp           # Follow (live)
docker logs --tail 100 myapp   # Senaste 100 rader
docker logs --since 1h myapp   # Senaste timmen
docker logs --until 2024-01-01T12:00:00 myapp
docker logs -t myapp           # Med timestamps

# Kombinera
docker logs -f --tail 50 myapp

# ═══════════════════════════════════════════════════════════════════════
# STATS - Resource monitoring
# ═══════════════════════════════════════════════════════════════════════

docker stats                   # Alla containers
docker stats myapp             # Specifik container
docker stats --no-stream       # Snapshot

# Output:
# CONTAINER   CPU %   MEM USAGE / LIMIT   MEM %   NET I/O   BLOCK I/O
# myapp       0.50%   50MiB / 512MiB      9.77%   1kB/0B    0B/0B

# ═══════════════════════════════════════════════════════════════════════
# TOP - Processer i container
# ═══════════════════════════════════════════════════════════════════════

docker top myapp               # ps-liknande output
docker top myapp aux           # Med aux format

# ═══════════════════════════════════════════════════════════════════════
# INSPECT - Detaljerad info
# ═══════════════════════════════════════════════════════════════════════

docker inspect myapp
docker inspect --format='{{.State.Status}}' myapp
docker inspect --format='{{.NetworkSettings.IPAddress}}' myapp
docker inspect --format='{{json .Config.Env}}' myapp | jq

# ═══════════════════════════════════════════════════════════════════════
# EVENTS - Docker daemon events
# ═══════════════════════════════════════════════════════════════════════

docker events                  # Live events
docker events --since 1h       # Senaste timmen
docker events --filter container=myapp
docker events --filter event=start
docker events --filter event=die
```

## 5. File Operations

```bash
# ═══════════════════════════════════════════════════════════════════════
# COPY - Between container and host
# ═══════════════════════════════════════════════════════════════════════

# Container -> Host
docker cp myapp:/app/config.json ./config.json
docker cp myapp:/var/log/ ./logs/

# Host -> Container
docker cp ./newconfig.json myapp:/app/config.json
docker cp ./data/ myapp:/app/data/

# ═══════════════════════════════════════════════════════════════════════
# DIFF - Filesystem changes
# ═══════════════════════════════════════════════════════════════════════

docker diff myapp
# A = Added
# C = Changed
# D = Deleted

# ═══════════════════════════════════════════════════════════════════════
# EXPORT / IMPORT - Container filesystem
# ═══════════════════════════════════════════════════════════════════════

# Export container filesystem som tar
docker export myapp > myapp-fs.tar
docker export myapp -o myapp-fs.tar

# Import tar som ny image
docker import myapp-fs.tar myapp-imported:v1

# ═══════════════════════════════════════════════════════════════════════
# COMMIT - Skapa image från container
# ═══════════════════════════════════════════════════════════════════════

# ⚠️ Undvik i produktion - använd Dockerfile istället
docker commit myapp myapp-snapshot:v1
docker commit -m "Added packages" myapp myapp-modified:v1
```

## 6. Restart Policies

```
+-------------------------------------------------------------------------+
|                     RESTART POLICIES                                     |
+-------------------------------------------------------------------------+
|                                                                          |
|  POLICY              | BEHAVIOR                                          |
|  ---------------------------------------------------------------------  |
|  no                  | Aldrig restart (default)                         |
|  on-failure          | Restart vid exit code != 0                       |
|  on-failure:N        | Max N restarts                                   |
|  always              | Alltid restart                                   |
|  unless-stopped      | Alltid, utom om manuellt stoppad                 |
|                                                                          |
|  EXEMPEL:                                                                |
|  ---------------------------------------------------------------------  |
|                                                                          |
|  # Always restart                                                        |
|  docker run -d --restart=always nginx                                    |
|                                                                          |
|  # Restart on failure, max 5 times                                       |
|  docker run -d --restart=on-failure:5 myapp                             |
|                                                                          |
|  # Update restart policy                                                 |
|  docker update --restart=always myapp                                    |
|                                                                          |
|  USE CASES:                                                              |
|  ---------------------------------------------------------------------  |
|  Production services    | always / unless-stopped                       |
|  Workers/Jobs           | on-failure:N                                  |
|  Development            | no                                            |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 7. Praktiska Övningar

### Övning 1: Lifecycle Walkthrough

```bash
# 1. Skapa container
docker create --name lifecycle-demo nginx:alpine
docker ps -a | grep lifecycle

# 2. Starta
docker start lifecycle-demo
docker ps | grep lifecycle

# 3. Pausa
docker pause lifecycle-demo
docker ps | grep lifecycle    # Status: (Paused)

# 4. Unpause
docker unpause lifecycle-demo

# 5. Exec
docker exec lifecycle-demo nginx -v
docker exec -it lifecycle-demo sh

# 6. Logs
docker logs lifecycle-demo

# 7. Stats
docker stats --no-stream lifecycle-demo

# 8. Stop
docker stop lifecycle-demo

# 9. Remove
docker rm lifecycle-demo
```

### Övning 2: Debug Container

```bash
# Starta container med problem
docker run -d --name debug-target nginx:alpine

# Inspektera
docker inspect debug-target | jq '.[0].State'
docker inspect --format='{{.NetworkSettings.IPAddress}}' debug-target

# Se logs
docker logs debug-target

# Shell access
docker exec -it debug-target sh

# Inuti:
cat /etc/nginx/nginx.conf
nginx -t
ls -la /usr/share/nginx/html/
curl localhost
exit

# Kopiera ut config
docker cp debug-target:/etc/nginx/nginx.conf ./nginx.conf

# Cleanup
docker stop debug-target && docker rm debug-target
```

### Övning 3: Restart Policy

```bash
# Container som crashar
docker run -d \
  --name crash-test \
  --restart=on-failure:3 \
  alpine sh -c 'echo "Starting..."; sleep 2; exit 1'

# Observera restarts
watch -n 1 'docker ps -a | grep crash-test'

# Se inspect för restart count
docker inspect crash-test | jq '.[0].RestartCount'

# Cleanup
docker rm -f crash-test
```

## 8. Resource Limits

```bash
# ═══════════════════════════════════════════════════════════════════════
# MEMORY LIMITS
# ═══════════════════════════════════════════════════════════════════════

docker run -d \
  --name limited \
  --memory=512m \
  --memory-swap=512m \
  nginx

# ═══════════════════════════════════════════════════════════════════════
# CPU LIMITS
# ═══════════════════════════════════════════════════════════════════════

docker run -d \
  --name cpu-limited \
  --cpus=1.5 \
  nginx

# ═══════════════════════════════════════════════════════════════════════
# KOMBINERAT
# ═══════════════════════════════════════════════════════════════════════

docker run -d \
  --name production-app \
  --memory=1g \
  --memory-swap=1g \
  --cpus=2 \
  --restart=unless-stopped \
  myapp

# ═══════════════════════════════════════════════════════════════════════
# UPDATE LIMITS
# ═══════════════════════════════════════════════════════════════════════

docker update --memory=1g --cpus=2 myapp
```

## 9. Best Practices

```
+-------------------------------------------------------------------------+
|              CONTAINER MANAGEMENT BEST PRACTICES                         |
+-------------------------------------------------------------------------+
|                                                                          |
|  ✅ Naming                                                               |
|     □ Använd --name för alla containers                                |
|     □ Följ naming convention: project-service-env                      |
|                                                                          |
|  ✅ Resources                                                           |
|     □ Sätt memory/CPU limits i produktion                              |
|     □ Använd restart policies                                          |
|                                                                          |
|  ✅ Cleanup                                                              |
|     □ Använd --rm för temporära containers                             |
|     □ Regelbunden docker container prune                               |
|                                                                          |
|  ✅ Debugging                                                           |
|     □ Använd exec för debugging, inte attach                           |
|     □ Övervaka med stats och logs                                      |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 10-14. Sammanfattning

### Quick Reference

| Action | Command |
|--------|---------|
| Create | `docker create` |
| Start | `docker start` |
| Run | `docker run` |
| Stop | `docker stop` |
| Kill | `docker kill` |
| Remove | `docker rm` |
| Logs | `docker logs` |
| Exec | `docker exec` |

---

**Nästa Node:** Docker Volumes ->
''',
    "xp_reward": 150,
    "estimated_minutes": 60,
    "prerequisites": ["docker_node_3"],
    "learning_outcomes": [
        "Förstå container lifecycle",
        "Hantera containers effektivt",
        "Debugga containers",
        "Konfigurera restart policies"
    ]
}

# Block 1 Part 2 exports
BLOCK_1_PART_2_NODES = [NODE_3, NODE_4]
