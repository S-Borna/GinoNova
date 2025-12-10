# =============================================================================
# DOCKER PRODUCTION — Noder 17-20
# Premium Bootcamp-Quality Content
# =============================================================================

NODE_17_PRODUCTION_BASICS = {
    "id": "docker-production",
    "node_id": 17,
    "title": "Docker in Production",
    "slug": "docker-production",
    "description": "Kör Docker säkert och effektivt i produktionsmiljöer",
    "type": "concept",
    "difficulty": "hard",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [16],
    "content": '''# 🏭 Docker in Production

## Lärande mål
- Förstå produktionskrav för Docker
- Implementera säkerhets-best practices
- Konfigurera för hög tillgänglighet
- Hantera state och data

---

## 🎯 Production Checklist

### Security

- [ ] Non-root user i containers
- [ ] Read-only filesystem där möjligt
- [ ] Minimala base images
- [ ] Regelbunden image scanning
- [ ] Network segmentering
- [ ] Secrets via environment/secrets manager
- [ ] Resource limits konfigurerade

### Reliability

- [ ] Health checks på alla services
- [ ] Restart policies
- [ ] Logging konfigurerat
- [ ] Monitoring setup
- [ ] Backup-strategi för data

### Performance

- [ ] Multi-stage builds
- [ ] Optimerade images
- [ ] Resource limits
- [ ] Proper caching

---

## 🔒 Security Hardening

### Non-root Container

```dockerfile
FROM node:20-alpine

# Skapa app-user
RUN addgroup -g 1001 -S app && \\
    adduser -u 1001 -S app -G app

WORKDIR /app
COPY --chown=app:app . .

USER app
CMD ["node", "server.js"]
```

### Read-only Filesystem

```yaml
services:
  api:
    image: myapi:1.0
    read_only: true
    tmpfs:
      - /tmp
      - /var/run
    volumes:
      - logs:/app/logs
```

### Security Options

```yaml
services:
  api:
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
```

---

## 📊 Monitoring

### Prometheus Metrics

```yaml
services:
  api:
    image: myapi:1.0
    ports:
      - "3000:3000"
      - "9090:9090"  # Metrics endpoint

  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9091:9090"

  grafana:
    image: grafana/grafana
    ports:
      - "3001:3000"
    volumes:
      - grafana_data:/var/lib/grafana
```

### cAdvisor

```yaml
services:
  cadvisor:
    image: gcr.io/cadvisor/cadvisor
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker:/var/lib/docker:ro
    ports:
      - "8080:8080"
```

---

## 💾 Data Management

### Backup Strategy

```bash
# Backup PostgreSQL
docker exec postgres pg_dump -U app app > backup_$(date +%Y%m%d).sql

# Backup volume
docker run --rm \\
    -v postgres_data:/data:ro \\
    -v $(pwd)/backups:/backup \\
    alpine tar czf /backup/postgres_$(date +%Y%m%d).tar.gz -C /data .
```

### Volume Management

```yaml
services:
  postgres:
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /data/postgres
```

---

## 🏋️ Övningar

### Övning: Production-ready setup
```bash
# Skapa säker container
docker run -d \\
    --name secure-api \\
    --user 1000:1000 \\
    --read-only \\
    --tmpfs /tmp \\
    --cap-drop ALL \\
    --security-opt no-new-privileges:true \\
    --memory 256m \\
    --cpus 0.5 \\
    --restart unless-stopped \\
    myapi:1.0
```

---

**Nästa steg:** Node 18 - Container Orchestration Overview
''',
}


NODE_18_ORCHESTRATION = {
    "id": "container-orchestration",
    "node_id": 18,
    "title": "Container Orchestration Overview",
    "slug": "container-orchestration",
    "description": "Förstå behov och alternativ för container orchestration",
    "type": "concept",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 130,
    "prerequisites": [17],
    "content": '''# ⚙️ Container Orchestration Overview

## Lärande mål
- Förstå varför orchestration behövs
- Jämföra olika orchestration-plattformar
- Veta när Docker Compose räcker
- Förstå Kubernetes grunderna

---

## 📖 Varför Orchestration?

### Utmaningar med Docker på skala

```
+-----------------------------------------------------------------+
|               PRODUCTION CHALLENGES                              |
+-----------------------------------------------------------------+
|                                                                  |
|  • Hur startar vi om crashed containers?                        |
|  • Hur skalar vi över flera servrar?                           |
|  • Hur gör vi rolling updates utan downtime?                   |
|  • Hur load-balancear vi trafik?                               |
|  • Hur hanterar vi secrets säkert?                             |
|  • Hur övervakar vi hundratals containers?                     |
|                                                                  |
+-----------------------------------------------------------------+
```

---

## 🔄 Orchestration Platforms

### Docker Swarm

```bash
# Initiera Swarm
docker swarm init

# Deploya stack
docker stack deploy -c docker-compose.yml myapp

# Skala service
docker service scale myapp_api=5
```

**Fördelar:**
- Inbyggt i Docker
- Enkel att komma igång
- Samma compose-format

**Nackdelar:**
- Begränsade features
- Mindre community
- Färre produktions-use-cases

### Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api
  template:
    spec:
      containers:
      - name: api
        image: myapi:1.0
        ports:
        - containerPort: 3000
```

**Fördelar:**
- Industry standard
- Extremt kraftfullt
- Stort ekosystem
- Cloud-native

**Nackdelar:**
- Komplex learning curve
- Kräver mer resurser
- Overkill för små projekt

---

## 📊 Vad ska jag välja?

| Scenario | Rekommendation |
|----------|----------------|
| Local dev | Docker Compose |
| Single server prod | Docker Compose |
| 2-5 servrar, enkel setup | Docker Swarm |
| Cloud, enterprise, komplext | Kubernetes |
| Managed cloud | ECS, Cloud Run, etc |

---

## 🎯 Docker Compose vs Kubernetes

```yaml
# Docker Compose                    # Kubernetes
services:                           apiVersion: apps/v1
  api:                              kind: Deployment
    image: myapi:1.0                metadata:
    ports:                            name: api
      - "3000:3000"                 spec:
    deploy:                           replicas: 3
      replicas: 3                     template:
                                        spec:
                                          containers:
                                          - name: api
                                            image: myapi:1.0
```

---

**Nästa steg:** Node 19 - Docker CI/CD Integration
''',
}


NODE_19_CICD = {
    "id": "docker-cicd",
    "node_id": 19,
    "title": "Docker CI/CD Integration",
    "slug": "docker-cicd",
    "description": "Automatisera Docker builds och deployments i CI/CD pipelines",
    "type": "practice",
    "difficulty": "hard",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [18],
    "content": '''# 🔄 Docker CI/CD Integration

## Lärande mål
- Bygga Docker images i CI/CD
- Implementera säker image scanning
- Automatisera deployments
- Best practices för Docker i pipelines

---

## 🐙 GitHub Actions

### Basic Build & Push

```yaml
name: Docker Build

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and Push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            myuser/myapp:${{ github.sha }}
            myuser/myapp:latest
```

### Med Caching

```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3

- name: Build and Push
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: myuser/myapp:latest
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

### Med Vulnerability Scanning

```yaml
- name: Build
  uses: docker/build-push-action@v5
  with:
    context: .
    load: true
    tags: myapp:test

- name: Scan for vulnerabilities
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: myapp:test
    exit-code: '1'
    severity: 'CRITICAL,HIGH'
```

---

## 🦊 GitLab CI

```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

test:
  stage: test
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker run --rm $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA npm test

deploy:
  stage: deploy
  script:
    - docker pull $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - docker tag $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA $CI_REGISTRY_IMAGE:latest
    - docker push $CI_REGISTRY_IMAGE:latest
  only:
    - main
```

---

## 🔐 Security Best Practices

### 1. Scan alla images

```yaml
- name: Trivy scan
  run: |
    trivy image --exit-code 1 --severity HIGH,CRITICAL myimage:${{ github.sha }}
```

### 2. Signera images

```bash
# Cosign
cosign sign myregistry/myimage:v1.0
```

### 3. SBOM generation

```yaml
- name: Generate SBOM
  uses: anchore/sbom-action@v0
  with:
    image: myimage:${{ github.sha }}
```

---

## 📊 Tagging Strategy

```yaml
tags: |
  myuser/myapp:${{ github.sha }}
  myuser/myapp:${{ github.ref_name }}
  ${{ github.ref == 'refs/heads/main' && 'myuser/myapp:latest' || '' }}
```

---

**Nästa steg:** Node 20 - Docker Troubleshooting & Best Practices
''',
}


NODE_20_TROUBLESHOOTING = {
    "id": "docker-troubleshooting",
    "node_id": 20,
    "title": "Docker Troubleshooting & Best Practices",
    "slug": "docker-troubleshooting",
    "description": "Felsök vanliga Docker-problem och sammanfattning av best practices",
    "type": "deep_dive",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 140,
    "prerequisites": [19],
    "content": '''# 🔧 Docker Troubleshooting & Best Practices

## Lärande mål
- Felsöka vanliga Docker-problem
- Förstå debugging-verktyg
- Sammanfatta alla best practices
- Bygga en solid Docker-kunskap

---

## 🐛 Vanliga Problem

### 1. Container startar inte

```bash
# Kolla exit code
docker ps -a
# EXITED (1)

# Kolla loggar
docker logs mycontainer

# Kör interaktivt för debugging
docker run -it myimage sh
```

### 2. Permission denied

```bash
# Problem: Can't write to volume
# Lösning: Matcha user/group
docker run -u $(id -u):$(id -g) -v $(pwd)/data:/data myimage

# Eller fixa i Dockerfile
RUN chown -R 1000:1000 /app/data
USER 1000
```

### 3. Port already in use

```bash
# Hitta vad som använder porten
lsof -i :8080
# eller
docker ps | grep 8080

# Stoppa container
docker stop <container>
```

### 4. Build tar lång tid

```bash
# Optimera .dockerignore
node_modules
.git
*.md
tests/

# Använd BuildKit
DOCKER_BUILDKIT=1 docker build .

# Kolla cache-hits
docker build . 2>&1 | grep -i cache
```

### 5. Image för stor

```bash
# Analysera layers
docker history myimage:latest

# Identifiera stora filer
docker run --rm myimage du -sh /* 2>/dev/null | sort -h

# Lösning: Multi-stage build
```

---

## 🔍 Debugging Tools

### Docker inspect

```bash
# All info
docker inspect mycontainer

# Specifik info
docker inspect --format='{{.State.Status}}' mycontainer
docker inspect --format='{{.NetworkSettings.IPAddress}}' mycontainer
docker inspect --format='{{json .Mounts}}' mycontainer | jq
```

### Docker logs

```bash
# Senaste loggar
docker logs --tail 100 mycontainer

# Följ i realtid
docker logs -f mycontainer

# Med timestamps
docker logs -t mycontainer
```

### Docker exec

```bash
# Shell access
docker exec -it mycontainer sh

# Kör kommando
docker exec mycontainer cat /etc/hosts

# Som root
docker exec -u 0 mycontainer whoami
```

### Network debugging

```bash
# Netshoot container
docker run -it --network container:mycontainer nicolaka/netshoot

# Debugging kommandon
ping hostname
nslookup hostname
curl http://service:port
tcpdump -i any port 80
```

---

## ✅ Best Practices Summary

### Dockerfile

```dockerfile
# ✅ Specifik base image version
FROM python:3.11.7-slim-bookworm

# ✅ Multi-stage build
FROM node:20 AS builder
...
FROM node:20-alpine AS runtime

# ✅ Non-root user
RUN useradd -r appuser
USER appuser

# ✅ Layer caching
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ✅ Health check
HEALTHCHECK CMD curl -f http://localhost:3000/health
```

### docker-compose.yml

```yaml
services:
  api:
    # ✅ Health check
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000"]

    # ✅ Resource limits
    deploy:
      resources:
        limits:
          memory: 512M

    # ✅ Restart policy
    restart: unless-stopped

    # ✅ Logging
    logging:
      driver: json-file
      options:
        max-size: "10m"
```

### Security

- Non-root containers
- Read-only filesystem
- Minimal base images
- Regular scanning
- No secrets in images
- Network segmentation

### Performance

- Multi-stage builds
- Proper .dockerignore
- Layer caching optimization
- Named volumes for deps

---

## 🎉 Grattis!

Du har nu genomfört hela Docker Mastery SkillsMap!

**Du kan nu:**
- ✅ Bygga optimerade Docker images
- ✅ Hantera containers professionellt
- ✅ Konfigurera nätverk och volumes
- ✅ Använda Docker Compose
- ✅ Köra Docker i produktion
- ✅ Integrera Docker i CI/CD
- ✅ Felsöka Docker-problem

**Nästa steg:**
- 🎯 Kubernetes Mastery SkillsMap
- 🎯 CI/CD Mastery SkillsMap
- 🎯 Cloud (AWS/GCP/Azure) SkillsMaps
''',
}


NODES = [
    NODE_17_PRODUCTION_BASICS,
    NODE_18_ORCHESTRATION,
    NODE_19_CICD,
    NODE_20_TROUBLESHOOTING,
]
