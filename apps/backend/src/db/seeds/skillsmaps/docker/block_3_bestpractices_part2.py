# =============================================================================
# DOCKER MASTERY V3 - BLOCK 3 PART 2: SECURITY & REGISTRY
# Noder 11-12 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
DOCKER BLOCK 3 PART 2 - SECURITY & DISTRIBUTION
================================================
Node 11: Docker Security - Hardening
Node 12: Docker Registry - Image Distribution
"""

NODE_11 = {
    "id": "docker_node_11",
    "title": "Docker Security - Hardening",
    "slug": "docker-security-hardening",
    "content": r'''# 🔒 Docker Security

## 1. Introduktion & Kontext

Docker security är kritiskt för production deployments. Felkonfigurerade containers kan exponera hela host-systemet. Denna guide täcker essential security practices.

### Security Layers

```
+-------------------------------------------------------------------------+
|                    DOCKER SECURITY LAYERS                                |
+-------------------------------------------------------------------------+
|                                                                          |
|  +-----------------------------------------------------------------+   |
|  | LAYER 5: RUNTIME SECURITY                                        |   |
|  | • Read-only filesystem                                           |   |
|  | • Dropped capabilities                                           |   |
|  | • Seccomp profiles                                               |   |
|  +-----------------------------------------------------------------+   |
|                          ▲                                               |
|  +-----------------------------------------------------------------+   |
|  | LAYER 4: CONTAINER CONFIG                                        |   |
|  | • Non-root user                                                  |   |
|  | • Resource limits                                                |   |
|  | • Network isolation                                              |   |
|  +-----------------------------------------------------------------+   |
|                          ▲                                               |
|  +-----------------------------------------------------------------+   |
|  | LAYER 3: IMAGE SECURITY                                          |   |
|  | • Vulnerability scanning                                         |   |
|  | • Trusted base images                                            |   |
|  | • Image signing                                                  |   |
|  +-----------------------------------------------------------------+   |
|                          ▲                                               |
|  +-----------------------------------------------------------------+   |
|  | LAYER 2: DOCKERFILE SECURITY                                     |   |
|  | • Minimal packages                                               |   |
|  | • No secrets in image                                            |   |
|  | • Specific versions                                              |   |
|  +-----------------------------------------------------------------+   |
|                          ▲                                               |
|  +-----------------------------------------------------------------+   |
|  | LAYER 1: HOST SECURITY                                           |   |
|  | • Docker daemon config                                           |   |
|  | • User namespace remapping                                       |   |
|  | • AppArmor/SELinux                                               |   |
|  +-----------------------------------------------------------------+   |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Non-root User

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# NON-ROOT USER (CRITICAL!)
# ═══════════════════════════════════════════════════════════════════════

# ❌ BAD: Running as root (default)
FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python", "app.py"]  # Körs som root!

# ✅ GOOD: Create and use non-root user
FROM python:3.11-slim

# Skapa user och grupp
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

COPY --chown=appuser:appgroup . .

# Byt till non-root user
USER appuser

CMD ["python", "app.py"]  # Körs som appuser

# ═══════════════════════════════════════════════════════════════════════
# ALPINE VERSION
# ═══════════════════════════════════════════════════════════════════════

FROM node:20-alpine

# Alpine använder adduser/addgroup
RUN addgroup -g 1001 -S nodejs && \
    adduser -S -u 1001 -G nodejs nodejs

WORKDIR /app

COPY --chown=nodejs:nodejs . .

USER nodejs

CMD ["node", "server.js"]
```

## 3. Image Scanning

```bash
# ═══════════════════════════════════════════════════════════════════════
# VULNERABILITY SCANNING
# ═══════════════════════════════════════════════════════════════════════

# Docker Scout (built-in)
docker scout cves myimage:latest
docker scout quickview myimage:latest
docker scout recommendations myimage:latest

# Trivy (popular open source)
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy image myimage:latest

# Snyk
docker scan myimage:latest

# Grype
grype myimage:latest

# ═══════════════════════════════════════════════════════════════════════
# CI/CD INTEGRATION
# ═══════════════════════════════════════════════════════════════════════

# GitHub Actions example
# - name: Scan image
#   uses: aquasecurity/trivy-action@master
#   with:
#     image-ref: 'myimage:${{ github.sha }}'
#     format: 'table'
#     exit-code: '1'
#     severity: 'CRITICAL,HIGH'
```

## 4. Runtime Security

```bash
# ═══════════════════════════════════════════════════════════════════════
# READ-ONLY FILESYSTEM
# ═══════════════════════════════════════════════════════════════════════

docker run -d \
  --name secure-app \
  --read-only \
  --tmpfs /tmp \
  --tmpfs /var/run \
  myapp

# ═══════════════════════════════════════════════════════════════════════
# DROP CAPABILITIES
# ═══════════════════════════════════════════════════════════════════════

# Se vilka capabilities som finns
docker run --rm alpine capsh --print

# Ta bort alla och lägg till specifika
docker run -d \
  --name secure-app \
  --cap-drop=ALL \
  --cap-add=NET_BIND_SERVICE \
  myapp

# ═══════════════════════════════════════════════════════════════════════
# SECURITY OPTIONS
# ═══════════════════════════════════════════════════════════════════════

docker run -d \
  --name secure-app \
  --security-opt=no-new-privileges:true \
  --security-opt=apparmor:docker-default \
  myapp

# ═══════════════════════════════════════════════════════════════════════
# RESOURCE LIMITS
# ═══════════════════════════════════════════════════════════════════════

docker run -d \
  --name limited-app \
  --memory=512m \
  --memory-swap=512m \
  --cpus=1 \
  --pids-limit=100 \
  myapp
```

## 5. Secret Management

```yaml
# ═══════════════════════════════════════════════════════════════════════
# DOCKER COMPOSE SECRETS
# ═══════════════════════════════════════════════════════════════════════

# ❌ BAD: Secrets i environment
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: supersecret123  # Synlig i inspect!

# ✅ GOOD: Docker secrets
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt

# ═══════════════════════════════════════════════════════════════════════
# EXTERNAL SECRETS (produktion)
# ═══════════════════════════════════════════════════════════════════════

secrets:
  db_password:
    external: true           # Skapad separat med docker secret create
  api_key:
    environment: API_KEY     # Från host environment
```

```bash
# Dockerfile: Läs secret
#!/bin/sh
DB_PASSWORD=$(cat /run/secrets/db_password)
exec python app.py
```

## 6. Network Security

```yaml
# ═══════════════════════════════════════════════════════════════════════
# NETWORK ISOLATION
# ═══════════════════════════════════════════════════════════════════════

services:
  frontend:
    networks:
      - frontend-net

  api:
    networks:
      - frontend-net      # Nåbar från frontend
      - backend-net       # Nåbar från db

  db:
    networks:
      - backend-net       # INTE nåbar från frontend!

networks:
  frontend-net:
  backend-net:
    internal: true        # Ingen extern access
```

## 7. Secure Dockerfile

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# SECURE DOCKERFILE TEMPLATE
# ═══════════════════════════════════════════════════════════════════════

# 1. Använd specifik version
FROM python:3.11.7-slim-bookworm

# 2. Sätt säkra labels
LABEL maintainer="security@example.com" \
      version="1.0.0" \
      description="Secure Python application"

# 3. Skapa non-root user tidigt
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# 4. Installera endast nödvändiga paket
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 5. Sätt workspace
WORKDIR /app

# 6. Kopiera dependencies först
COPY --chown=appuser:appgroup requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 7. Kopiera kod
COPY --chown=appuser:appgroup . .

# 8. Byt till non-root user
USER appuser

# 9. Exponera endast nödvändig port
EXPOSE 8000

# 10. Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

# 11. Använd exec form
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

## 8. Security Checklist

```
+-------------------------------------------------------------------------+
|                    DOCKER SECURITY CHECKLIST                             |
+-------------------------------------------------------------------------+
|                                                                          |
|  IMAGE SECURITY:                                                         |
|  □ Use official/verified base images                                    |
|  □ Pin specific image versions (not :latest)                            |
|  □ Scan images for vulnerabilities                                      |
|  □ Use minimal base images (slim/alpine/distroless)                    |
|  □ Sign images with Docker Content Trust                                |
|                                                                          |
|  DOCKERFILE:                                                             |
|  □ Run as non-root USER                                                 |
|  □ Don't store secrets in images                                        |
|  □ Use COPY instead of ADD                                              |
|  □ Set HEALTHCHECK                                                      |
|  □ Use multi-stage builds                                               |
|                                                                          |
|  RUNTIME:                                                                |
|  □ Drop unnecessary capabilities                                        |
|  □ Use read-only filesystem where possible                              |
|  □ Set resource limits (memory, CPU, PIDs)                              |
|  □ Use security-opt no-new-privileges                                   |
|  □ Use Docker secrets for sensitive data                                |
|                                                                          |
|  NETWORK:                                                                |
|  □ Use user-defined networks                                            |
|  □ Don't expose unnecessary ports                                       |
|  □ Use internal networks for backend services                           |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 9-14. Sammanfattning

### Security Commands Reference

| Command | Purpose |
|---------|---------|
| `docker scout` | Scan vulnerabilities |
| `--read-only` | Read-only filesystem |
| `--cap-drop` | Remove capabilities |
| `--security-opt` | Security options |

---

**Nästa Node:** Docker Registry ->
''',
    "xp_reward": 175,
    "estimated_minutes": 75,
    "prerequisites": ["docker_node_10"],
    "learning_outcomes": [
        "Implementera container security",
        "Använda non-root users",
        "Scanna images för sårbarheter",
        "Konfigurera runtime security"
    ]
}

NODE_12 = {
    "id": "docker_node_12",
    "title": "Docker Registry - Image Distribution",
    "slug": "docker-registry-image-distribution",
    "content": r'''# 📦 Docker Registry

## 1. Introduktion & Kontext

Docker Registry är tjänster för att lagra och distribuera Docker images. Förståelse av registry-operationer är kritiskt för CI/CD och team-collaboration.

### Registry Ecosystem

```
+-------------------------------------------------------------------------+
|                    DOCKER REGISTRY ECOSYSTEM                             |
+-------------------------------------------------------------------------+
|                                                                          |
|  PUBLIC REGISTRIES:                                                      |
|  ═══════════════════════════════════════════════════════════════════   |
|  +-----------------+ +-----------------+ +-----------------+           |
|  |   Docker Hub    | |   GitHub GHCR   | |  Quay.io        |           |
|  |   docker.io     | |   ghcr.io       | |  quay.io        |           |
|  |   (default)     | |                 | |                 |           |
|  +-----------------+ +-----------------+ +-----------------+           |
|                                                                          |
|  CLOUD PROVIDER REGISTRIES:                                             |
|  ═══════════════════════════════════════════════════════════════════   |
|  +-----------------+ +-----------------+ +-----------------+           |
|  |     AWS ECR     | |   Google GCR    | |   Azure ACR     |           |
|  | xxx.dkr.ecr.    | |   gcr.io/       | |   xxx.azurecr.  |           |
|  | region.amazon.. | |   project/      | |   io/           |           |
|  +-----------------+ +-----------------+ +-----------------+           |
|                                                                          |
|  SELF-HOSTED:                                                           |
|  ═══════════════════════════════════════════════════════════════════   |
|  +-----------------+ +-----------------+ +-----------------+           |
|  | Docker Registry | |    Harbor       | |   GitLab        |           |
|  |  (Official)     | |  (Enterprise)   | |  Registry       |           |
|  +-----------------+ +-----------------+ +-----------------+           |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Image Naming

```
+-------------------------------------------------------------------------+
|                    IMAGE NAMING CONVENTION                               |
+-------------------------------------------------------------------------+
|                                                                          |
|  FULL FORMAT:                                                            |
|  [registry/][namespace/]repository[:tag][@digest]                       |
|                                                                          |
|  EXAMPLES:                                                               |
|  ---------------------------------------------------------------------  |
|                                                                          |
|  nginx                                                                   |
|  -> docker.io/library/nginx:latest                                       |
|                                                                          |
|  nginx:1.24-alpine                                                      |
|  -> docker.io/library/nginx:1.24-alpine                                  |
|                                                                          |
|  myuser/myapp:v1.0.0                                                    |
|  -> docker.io/myuser/myapp:v1.0.0                                        |
|                                                                          |
|  ghcr.io/myorg/myapp:latest                                             |
|  -> GitHub Container Registry                                            |
|                                                                          |
|  123456789.dkr.ecr.eu-west-1.amazonaws.com/myapp:v1                     |
|  -> AWS ECR                                                              |
|                                                                          |
|  gcr.io/my-project/myapp:latest                                         |
|  -> Google Container Registry                                            |
|                                                                          |
|  myregistry.azurecr.io/myapp:latest                                     |
|  -> Azure Container Registry                                             |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 3. Registry Operations

```bash
# ═══════════════════════════════════════════════════════════════════════
# LOGIN
# ═══════════════════════════════════════════════════════════════════════

# Docker Hub
docker login
docker login -u username

# Other registries
docker login ghcr.io
docker login gcr.io
docker login myregistry.azurecr.io

# With password from file
cat ~/my_password.txt | docker login -u username --password-stdin

# ═══════════════════════════════════════════════════════════════════════
# TAG & PUSH
# ═══════════════════════════════════════════════════════════════════════

# Tag for registry
docker tag myapp:latest myuser/myapp:v1.0.0
docker tag myapp:latest ghcr.io/myorg/myapp:v1.0.0

# Push to registry
docker push myuser/myapp:v1.0.0
docker push ghcr.io/myorg/myapp:v1.0.0

# Push all tags
docker push myuser/myapp --all-tags

# ═══════════════════════════════════════════════════════════════════════
# PULL
# ═══════════════════════════════════════════════════════════════════════

docker pull nginx:1.24-alpine
docker pull ghcr.io/myorg/myapp:v1.0.0

# Pull by digest (immutable)
docker pull nginx@sha256:abc123...

# ═══════════════════════════════════════════════════════════════════════
# SEARCH & INSPECT
# ═══════════════════════════════════════════════════════════════════════

docker search nginx
docker search --filter is-official=true nginx

# Inspect remote image
docker manifest inspect nginx:latest
```

## 4. Tagging Strategy

```
+-------------------------------------------------------------------------+
|                    IMAGE TAGGING STRATEGY                                |
+-------------------------------------------------------------------------+
|                                                                          |
|  SEMANTIC VERSIONING:                                                    |
|  ═══════════════════════════════════════════════════════════════════   |
|  myapp:1.0.0              # Specific version                            |
|  myapp:1.0                # Minor version (rolling)                     |
|  myapp:1                  # Major version (rolling)                     |
|  myapp:latest             # Latest release                              |
|                                                                          |
|  GIT-BASED:                                                              |
|  ═══════════════════════════════════════════════════════════════════   |
|  myapp:abc1234            # Git short SHA                               |
|  myapp:main-abc1234       # Branch + SHA                                |
|  myapp:pr-123             # Pull request                                |
|                                                                          |
|  ENVIRONMENT:                                                            |
|  ═══════════════════════════════════════════════════════════════════   |
|  myapp:dev                # Development                                 |
|  myapp:staging            # Staging                                     |
|  myapp:prod               # Production                                  |
|                                                                          |
|  COMBINED (Recommended):                                                 |
|  ═══════════════════════════════════════════════════════════════════   |
|  myapp:v1.2.3             # Release version                             |
|  myapp:v1.2.3-abc1234     # Version + commit                            |
|  myapp:latest             # Most recent                                 |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 5. Self-hosted Registry

```bash
# ═══════════════════════════════════════════════════════════════════════
# RUN LOCAL REGISTRY
# ═══════════════════════════════════════════════════════════════════════

# Basic registry
docker run -d \
  --name registry \
  -p 5000:5000 \
  registry:2

# Push to local registry
docker tag myapp:latest localhost:5000/myapp:v1
docker push localhost:5000/myapp:v1

# Pull from local registry
docker pull localhost:5000/myapp:v1

# ═══════════════════════════════════════════════════════════════════════
# REGISTRY WITH PERSISTENCE
# ═══════════════════════════════════════════════════════════════════════

docker run -d \
  --name registry \
  -p 5000:5000 \
  -v registry-data:/var/lib/registry \
  -e REGISTRY_STORAGE_DELETE_ENABLED=true \
  registry:2
```

### Docker Compose Registry

```yaml
# docker-compose.yml
services:
  registry:
    image: registry:2
    ports:
      - "5000:5000"
    volumes:
      - registry-data:/var/lib/registry
      - ./config.yml:/etc/docker/registry/config.yml
    environment:
      - REGISTRY_STORAGE_DELETE_ENABLED=true

  registry-ui:
    image: joxit/docker-registry-ui
    ports:
      - "8080:80"
    environment:
      - REGISTRY_TITLE=My Registry
      - REGISTRY_URL=http://registry:5000
    depends_on:
      - registry

volumes:
  registry-data:
```

## 6. Cloud Registry Setup

### AWS ECR

```bash
# Login till ECR
aws ecr get-login-password --region eu-west-1 | \
  docker login --username AWS --password-stdin \
  123456789.dkr.ecr.eu-west-1.amazonaws.com

# Tag och push
docker tag myapp:latest 123456789.dkr.ecr.eu-west-1.amazonaws.com/myapp:v1
docker push 123456789.dkr.ecr.eu-west-1.amazonaws.com/myapp:v1
```

### GitHub Container Registry

```bash
# Login med PAT
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# Tag och push
docker tag myapp:latest ghcr.io/myorg/myapp:v1
docker push ghcr.io/myorg/myapp:v1
```

### Google Container Registry

```bash
# Configure gcloud
gcloud auth configure-docker

# Tag och push
docker tag myapp:latest gcr.io/my-project/myapp:v1
docker push gcr.io/my-project/myapp:v1
```

## 7. CI/CD Integration

```yaml
# ═══════════════════════════════════════════════════════════════════════
# GITHUB ACTIONS
# ═══════════════════════════════════════════════════════════════════════

name: Build and Push

on:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=semver,pattern={{version}}
            type=sha,prefix=

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

## 8-14. Sammanfattning

### Registry Commands Reference

| Command | Purpose |
|---------|---------|
| `docker login` | Authenticate |
| `docker tag` | Tag for registry |
| `docker push` | Upload image |
| `docker pull` | Download image |

---

**Nästa Node:** Docker in CI/CD ->
''',
    "xp_reward": 165,
    "estimated_minutes": 70,
    "prerequisites": ["docker_node_11"],
    "learning_outcomes": [
        "Arbeta med Docker registries",
        "Tagga images korrekt",
        "Pusha och pulla images",
        "Sätta upp privat registry"
    ]
}

# Block 3 Part 2 exports
BLOCK_3_PART_2_NODES = [NODE_11, NODE_12]
