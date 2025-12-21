# =============================================================================
# DOCKER MASTERY V3 - BLOCK 4 PART 1: CI/CD & DEBUGGING
# Noder 13-14 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
DOCKER BLOCK 4 PART 1 - OPERATIONS
==================================
Node 13: Docker in CI/CD - Automation
Node 14: Docker Debugging - Troubleshooting
"""

NODE_13 = {
    "id": "docker_node_13",
    "title": "Docker in CI/CD - Automation",
    "slug": "docker-in-ci-cd-automation",
    "content": r'''# 🔄 Docker in CI/CD

## 1. Introduktion & Kontext

Docker är fundamentalt för modern CI/CD. Det garanterar reproducerbarhet från utveckling till produktion och möjliggör snabba, pålitliga deployments.

### CI/CD Pipeline Overview

```
+-------------------------------------------------------------------------+
|                    DOCKER CI/CD PIPELINE                                 |
+-------------------------------------------------------------------------+
|                                                                          |
|  SOURCE        BUILD           TEST            DEPLOY                   |
|  ══════        ═════           ════            ══════                   |
|                                                                          |
|  +-----+      +---------+     +---------+     +-------------+          |
|  | Git | --►  | Docker  | --► | Docker  | --► | Deploy to   |          |
|  |Push |      | Build   |     | Test    |     | Production  |          |
|  +-----+      +----+----+     +----+----+     +------+------+          |
|                    |               |                  |                  |
|                    ▼               ▼                  ▼                  |
|              +----------+    +----------+     +--------------+         |
|              | Registry |    | Report   |     | Kubernetes/  |         |
|              |  Push    |    | Results  |     | Docker Swarm |         |
|              +----------+    +----------+     +--------------+         |
|                                                                          |
|  STAGES:                                                                 |
|  ---------------------------------------------------------------------  |
|  1. Checkout code                                                        |
|  2. Build Docker image                                                   |
|  3. Run tests in container                                              |
|  4. Scan for vulnerabilities                                            |
|  5. Push to registry                                                    |
|  6. Deploy to environment                                               |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. GitHub Actions

```yaml
# ═══════════════════════════════════════════════════════════════════════
# .github/workflows/docker.yml
# ═══════════════════════════════════════════════════════════════════════

name: Docker CI/CD

on:
  push:
    branches: [main, develop]
    tags: ['v*']
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # ===========================================
  # BUILD & TEST
  # ===========================================
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Registry
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha,prefix=

      - name: Build and export to Docker
        uses: docker/build-push-action@v5
        with:
          context: .
          load: true
          tags: ${{ env.IMAGE_NAME }}:test
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Run tests
        run: |
          docker run --rm ${{ env.IMAGE_NAME }}:test npm test

      - name: Scan for vulnerabilities
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.IMAGE_NAME }}:test
          format: 'table'
          exit-code: '1'
          severity: 'CRITICAL,HIGH'

      - name: Build and push
        if: github.event_name != 'pull_request'
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

## 3. Multi-platform Builds

```yaml
# ═══════════════════════════════════════════════════════════════════════
# MULTI-PLATFORM BUILD
# ═══════════════════════════════════════════════════════════════════════

- name: Set up QEMU
  uses: docker/setup-qemu-action@v3

- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3

- name: Build and push multi-platform
  uses: docker/build-push-action@v5
  with:
    context: .
    platforms: linux/amd64,linux/arm64
    push: true
    tags: ${{ steps.meta.outputs.tags }}
```

## 4. GitLab CI

```yaml
# ═══════════════════════════════════════════════════════════════════════
# .gitlab-ci.yml
# ═══════════════════════════════════════════════════════════════════════

stages:
  - build
  - test
  - scan
  - deploy

variables:
  DOCKER_TLS_CERTDIR: "/certs"
  IMAGE_TAG: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

build:
  stage: build
  image: docker:24.0
  services:
    - docker:24.0-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $IMAGE_TAG .
    - docker push $IMAGE_TAG

test:
  stage: test
  image: docker:24.0
  services:
    - docker:24.0-dind
  script:
    - docker pull $IMAGE_TAG
    - docker run --rm $IMAGE_TAG npm test

scan:
  stage: scan
  image: aquasec/trivy
  script:
    - trivy image --exit-code 1 --severity HIGH,CRITICAL $IMAGE_TAG
  allow_failure: true

deploy:
  stage: deploy
  image: docker:24.0
  only:
    - main
  script:
    - docker pull $IMAGE_TAG
    - docker tag $IMAGE_TAG $CI_REGISTRY_IMAGE:latest
    - docker push $CI_REGISTRY_IMAGE:latest
```

## 5. Build Caching

```yaml
# ═══════════════════════════════════════════════════════════════════════
# EFFICIENT CACHING STRATEGIES
# ═══════════════════════════════════════════════════════════════════════

# GitHub Actions - GHA cache
- name: Build with GHA cache
  uses: docker/build-push-action@v5
  with:
    context: .
    cache-from: type=gha
    cache-to: type=gha,mode=max

# Registry cache
- name: Build with registry cache
  uses: docker/build-push-action@v5
  with:
    context: .
    cache-from: type=registry,ref=${{ env.IMAGE_NAME }}:buildcache
    cache-to: type=registry,ref=${{ env.IMAGE_NAME }}:buildcache,mode=max

# Local cache
- name: Build with local cache
  uses: docker/build-push-action@v5
  with:
    context: .
    cache-from: type=local,src=/tmp/.buildx-cache
    cache-to: type=local,dest=/tmp/.buildx-cache-new,mode=max
```

## 6. Deployment Strategies

```yaml
# ═══════════════════════════════════════════════════════════════════════
# DEPLOYMENT TO KUBERNETES
# ═══════════════════════════════════════════════════════════════════════

deploy-k8s:
  needs: [build, test]
  runs-on: ubuntu-latest
  if: github.ref == 'refs/heads/main'
  steps:
    - uses: actions/checkout@v4

    - name: Set up kubectl
      uses: azure/setup-kubectl@v3

    - name: Configure kubeconfig
      run: |
        echo "${{ secrets.KUBECONFIG }}" | base64 -d > kubeconfig
        export KUBECONFIG=kubeconfig

    - name: Deploy
      run: |
        kubectl set image deployment/myapp \
          myapp=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
        kubectl rollout status deployment/myapp

# ═══════════════════════════════════════════════════════════════════════
# DEPLOYMENT TO DOCKER HOST
# ═══════════════════════════════════════════════════════════════════════

deploy-docker:
  needs: [build, test]
  runs-on: ubuntu-latest
  steps:
    - name: Deploy via SSH
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.SERVER_HOST }}
        username: ${{ secrets.SERVER_USER }}
        key: ${{ secrets.SSH_KEY }}
        script: |
          docker pull ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
          docker stop myapp || true
          docker rm myapp || true
          docker run -d --name myapp \
            -p 80:8000 \
            --restart unless-stopped \
            ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
```

## 7. Practical CI/CD Template

```yaml
# Complete production-ready workflow
name: Production Pipeline

on:
  push:
    branches: [main]
    tags: ['v*.*.*']

jobs:
  build-test-push:
    runs-on: ubuntu-latest
    outputs:
      image_tag: ${{ steps.meta.outputs.tags }}
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}
      - uses: docker/build-push-action@v5
        with:
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

## 8-14. Sammanfattning

### CI/CD Best Practices

| Practice | Benefit |
|----------|---------|
| Build caching | 10x faster builds |
| Multi-stage | Smaller images |
| Vulnerability scanning | Security |
| Automated tagging | Traceability |

---

**Nästa Node:** Docker Debugging ->
''',
    "xp_reward": 175,
    "estimated_minutes": 80,
    "prerequisites": ["docker_node_12"],
    "learning_outcomes": [
        "Konfigurera Docker CI/CD",
        "Använda GitHub Actions",
        "Optimera build caching",
        "Implementera deployment"
    ]
}

NODE_14 = {
    "id": "docker_node_14",
    "title": "Docker Debugging - Troubleshooting",
    "slug": "docker-debugging-troubleshooting",
    "content": r'''# 🔍 Docker Debugging

## 1. Introduktion & Kontext

Debugging Docker containers kräver specifika tekniker. Denna guide täcker essentiella verktyg och metoder för att diagnostisera och lösa problem.

### Debugging Workflow

```
+-------------------------------------------------------------------------+
|                    DOCKER DEBUGGING WORKFLOW                             |
+-------------------------------------------------------------------------+
|                                                                          |
|  1. IDENTIFY                                                             |
|     +-► docker ps -a          # Container status                        |
|     +-► docker logs           # Application logs                        |
|     +-► docker events         # Docker daemon events                    |
|                                                                          |
|  2. INSPECT                                                              |
|     +-► docker inspect        # Container config                        |
|     +-► docker stats          # Resource usage                          |
|     +-► docker top            # Running processes                       |
|                                                                          |
|  3. INTERACT                                                             |
|     +-► docker exec           # Run commands                            |
|     +-► docker attach         # Attach to process                       |
|     +-► docker cp             # Copy files                              |
|                                                                          |
|  4. ANALYZE                                                              |
|     +-► docker diff           # Filesystem changes                      |
|     +-► docker history        # Image layers                            |
|     +-► docker system df      # Disk usage                              |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Container Status

```bash
# ═══════════════════════════════════════════════════════════════════════
# CONTAINER STATUS & HEALTH
# ═══════════════════════════════════════════════════════════════════════

# Lista alla containers
docker ps -a

# Detaljerad status
docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Se exit codes
docker ps -a --filter "status=exited" --format "{{.Names}}: {{.Status}}"

# Exit codes:
# 0   - Normal exit
# 1   - Application error
# 137 - SIGKILL (OOM or docker kill)
# 139 - SIGSEGV (segmentation fault)
# 143 - SIGTERM (docker stop)

# Se varför container stoppade
docker inspect --format='{{.State.ExitCode}} - {{.State.Error}}' myapp
```

## 3. Logs Analysis

```bash
# ═══════════════════════════════════════════════════════════════════════
# LOG COMMANDS
# ═══════════════════════════════════════════════════════════════════════

# Alla logs
docker logs myapp

# Follow (live)
docker logs -f myapp

# Med timestamps
docker logs -t myapp

# Senaste N rader
docker logs --tail 100 myapp

# Sedan tidpunkt
docker logs --since 1h myapp
docker logs --since "2024-01-15T10:00:00" myapp

# Kombinera
docker logs -f --tail 100 --since 5m myapp

# ═══════════════════════════════════════════════════════════════════════
# LOG ANALYSIS TIPS
# ═══════════════════════════════════════════════════════════════════════

# Sök efter errors
docker logs myapp 2>&1 | grep -i error

# Sök efter exceptions
docker logs myapp 2>&1 | grep -iE "exception|traceback|error"

# Räkna fel
docker logs myapp 2>&1 | grep -c ERROR

# JSON logs (om konfigurerat)
docker logs myapp | jq 'select(.level == "error")'
```

## 4. Interactive Debugging

```bash
# ═══════════════════════════════════════════════════════════════════════
# EXEC - Kör kommandon i container
# ═══════════════════════════════════════════════════════════════════════

# Shell access
docker exec -it myapp bash
docker exec -it myapp sh       # Om ingen bash

# Som root (även om USER satt)
docker exec -u 0 -it myapp bash

# Kör specifikt kommando
docker exec myapp cat /app/config.json
docker exec myapp env
docker exec myapp ps aux
docker exec myapp netstat -tulpn

# ═══════════════════════════════════════════════════════════════════════
# DEBUG CONTAINER SOM INTE STARTAR
# ═══════════════════════════════════════════════════════════════════════

# Override entrypoint för att debugga
docker run -it --entrypoint bash myapp:latest

# Eller med shell
docker run -it myapp:latest sh

# Kolla varför den failar
docker run --rm myapp:latest cat /app/entrypoint.sh
```

## 5. Resource Monitoring

```bash
# ═══════════════════════════════════════════════════════════════════════
# STATS - Real-time resource usage
# ═══════════════════════════════════════════════════════════════════════

docker stats
docker stats myapp
docker stats --no-stream

# Format output
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# ═══════════════════════════════════════════════════════════════════════
# INSPECT - Detailed information
# ═══════════════════════════════════════════════════════════════════════

# Full inspect
docker inspect myapp

# Specifika delar
docker inspect --format='{{.State.Status}}' myapp
docker inspect --format='{{.NetworkSettings.IPAddress}}' myapp
docker inspect --format='{{json .Config.Env}}' myapp | jq
docker inspect --format='{{range .Mounts}}{{.Source}} -> {{.Destination}}{{"\n"}}{{end}}' myapp

# ═══════════════════════════════════════════════════════════════════════
# TOP - Processer i container
# ═══════════════════════════════════════════════════════════════════════

docker top myapp
docker top myapp aux
```

## 6. Network Debugging

```bash
# ═══════════════════════════════════════════════════════════════════════
# NETWORK TROUBLESHOOTING
# ═══════════════════════════════════════════════════════════════════════

# Lista networks
docker network ls

# Inspect network
docker network inspect bridge
docker network inspect mynetwork

# Se vilka containers på network
docker network inspect mynetwork --format '{{range .Containers}}{{.Name}} {{.IPv4Address}}{{"\n"}}{{end}}'

# DNS debugging
docker exec myapp nslookup db
docker exec myapp ping -c 3 db

# Port debugging
docker exec myapp netstat -tulpn
docker exec myapp curl -v http://api:8000/health

# ═══════════════════════════════════════════════════════════════════════
# NETWORK DEBUG CONTAINER
# ═══════════════════════════════════════════════════════════════════════

# Använd nicolaka/netshoot för avancerad debugging
docker run -it --rm --network mynetwork nicolaka/netshoot

# Inuti:
# nslookup db
# dig db
# curl http://api:8000
# tcpdump -i eth0
# nmap -sT api
```

## 7. Image & Filesystem

```bash
# ═══════════════════════════════════════════════════════════════════════
# IMAGE DEBUGGING
# ═══════════════════════════════════════════════════════════════════════

# Image history
docker history myapp:latest
docker history --no-trunc myapp:latest

# Image layers
docker inspect myapp:latest | jq '.[0].RootFS.Layers'

# ═══════════════════════════════════════════════════════════════════════
# FILESYSTEM CHANGES
# ═══════════════════════════════════════════════════════════════════════

# Se ändringar i container
docker diff myapp
# A = Added
# C = Changed
# D = Deleted

# Kopiera filer för analys
docker cp myapp:/app/logs ./debug-logs/
docker cp myapp:/var/log/ ./container-logs/

# ═══════════════════════════════════════════════════════════════════════
# DISK USAGE
# ═══════════════════════════════════════════════════════════════════════

docker system df
docker system df -v
```

## 8. Common Issues

```
+-------------------------------------------------------------------------+
|                    COMMON DOCKER ISSUES                                  |
+-------------------------------------------------------------------------+
|                                                                          |
|  ISSUE: Container exits immediately                                      |
|  ---------------------------------------------------------------------  |
|  DIAGNOSE: docker logs myapp                                            |
|  CAUSES:                                                                |
|  • CMD/ENTRYPOINT exits                                                 |
|  • Missing environment variables                                        |
|  • Permission errors                                                    |
|  FIX: docker run -it --entrypoint sh myapp                             |
|                                                                          |
|  ISSUE: OOM Killed (exit code 137)                                      |
|  ---------------------------------------------------------------------  |
|  DIAGNOSE: docker inspect --format='{{.State.OOMKilled}}' myapp        |
|  CAUSES: Memory limit exceeded                                          |
|  FIX: Increase --memory limit or optimize app                          |
|                                                                          |
|  ISSUE: Permission denied                                                |
|  ---------------------------------------------------------------------  |
|  DIAGNOSE: docker exec myapp ls -la /app                               |
|  CAUSES: USER mismatch, volume permissions                              |
|  FIX: chown in Dockerfile or use correct UID                           |
|                                                                          |
|  ISSUE: Container can't reach network                                   |
|  ---------------------------------------------------------------------  |
|  DIAGNOSE: docker exec myapp ping google.com                           |
|  CAUSES: Network config, DNS, firewall                                 |
|  FIX: Check network mode and DNS settings                              |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 9-14. Sammanfattning

### Debug Commands Reference

| Command | Purpose |
|---------|---------|
| `docker logs` | Application logs |
| `docker exec` | Run commands |
| `docker inspect` | Detailed info |
| `docker stats` | Resources |

---

**Nästa Node:** Build Optimization ->
''',
    "xp_reward": 170,
    "estimated_minutes": 75,
    "prerequisites": ["docker_node_13"],
    "learning_outcomes": [
        "Debugga Docker containers",
        "Analysera logs",
        "Felsöka nätverk",
        "Lösa vanliga problem"
    ]
}

# Block 4 Part 1 exports
BLOCK_4_PART_1_NODES = [NODE_13, NODE_14]

__all__ = ["NODE_13", "NODE_14", "BLOCK_4_PART_1_NODES"]
