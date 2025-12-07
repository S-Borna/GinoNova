"""
Docker Mastery Module
=====================

20 noder med svensk pedagogisk stil.
Komplett Docker-kunskap - från grunderna till produktion.

Track: containers
Difficulty: intermediate
Estimated Hours: 25
"""

MODULE = {
    "name": "Docker Mastery",
    "slug": "docker-mastery",
    "description": "Komplett Docker-kunskap - från containers till produktion med naturlig svensk pedagogik",
    "track_slug": "containers",
    "order_index": 18,
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "prerequisites": ["linux-mastery"],
    "icon": "🐳",
    "color": "#2496ED",
    "tasks": [
        {
            "title": "Docker Fundamentals & Architecture",
            "slug": "docker-fundamentals-architecture",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Docker Fundamentals & Architecture

## Varför behöver du kunna detta?

Som DevOps-ingenjör kommer du använda Docker dagligen. Du måste förstå:

- **Vad containers faktiskt är** så du kan felsöka när saker går fel
- **Hur Docker-arkitekturen fungerar** så du vet var problem kan uppstå
- **Skillnaden mellan containers och VMs** så du kan välja rätt verktyg

---

## Så fungerar Docker

Tänk på Docker som en **standardiserad fraktcontainer** för mjukvara. Precis som fraktcontainrar revolutionerade sjöfarten genom att standardisera hur gods transporteras, revolutionerar Docker hur mjukvara levereras.

---

## Container vs Virtual Machine

```bash
# Virtual Machine (VM)
┌─────────────────────────────────────┐
│           Din App                    │
├─────────────────────────────────────┤
│        Guest OS (hela!)              │  # 1-10 GB
├─────────────────────────────────────┤
│         Hypervisor                   │
├─────────────────────────────────────┤
│          Host OS                     │
└─────────────────────────────────────┘

# Container
┌─────────────────────────────────────┐
│           Din App                    │
├─────────────────────────────────────┤
│     Container Runtime (Docker)       │  # MB istället för GB
├─────────────────────────────────────┤
│          Host OS                     │
└─────────────────────────────────────┘
```

**Containers delar Host OS kernel** - det är därför de är så snabba och lätta!

---

## Docker-arkitekturen

```bash
┌──────────────────────────────────────────────────────────┐
│                     Docker Client                         │
│                    (docker CLI)                           │
└─────────────────────────┬────────────────────────────────┘
                          │ REST API
                          ▼
┌──────────────────────────────────────────────────────────┐
│                    Docker Daemon                          │
│                     (dockerd)                             │
├──────────────────────────────────────────────────────────┤
│  Images  │  Containers  │  Networks  │  Volumes          │
└──────────────────────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│                   Container Runtime                       │
│                    (containerd)                           │
└──────────────────────────────────────────────────────────┘
```

---

## Grundläggande kommandon

```bash
# Kolla att Docker är installerat och kör
docker version              # Visar client och server version
docker info                 # Detaljerad info om Docker-installation

# Kör din första container
docker run hello-world      # Laddar ner image och kör container

# Lista containers
docker ps                   # Visar körande containers
docker ps -a                # Visar ALLA containers (även stoppade)

# Lista images
docker images               # Visar alla lokala images
```

---

## Vad händer när du kör "docker run"?

```bash
docker run nginx
```

1. **Docker Client** skickar kommandot till Docker Daemon
2. **Daemon** kollar om `nginx` image finns lokalt
3. Om inte → laddar ner från **Docker Hub**
4. **Daemon** skapar en container från imagen
5. **Daemon** allokerar filsystem, nätverk, etc.
6. **Daemon** startar containern

---

## Key Takeaways

- Docker containers är **inte VMs** - de delar host OS kernel
- **Docker Client** pratar med **Docker Daemon** via REST API
- **Images** är read-only templates, **Containers** är körande instanser
- `docker run` = pull + create + start i ett kommando
""",
        },
        {
            "title": "Docker Images Deep Dive",
            "slug": "docker-images-deep-dive",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Docker Images Deep Dive

## Varför behöver du kunna detta?

Images är grunden för allt i Docker. Du måste förstå:

- **Hur images byggs upp** så du kan optimera storlek och build-tid
- **Layers och caching** så du inte slösar tid på onödiga rebuilds
- **Tagging-strategier** så du kan hantera versioner i produktion

---

## Vad är en Docker Image?

Tänk på en image som en **snapshot av ett filsystem** plus metadata om hur containern ska köras. Det är som en mall eller recept - du kan skapa hur många containers som helst från samma image.

---

## Image Layers

```bash
# Varje instruktion i Dockerfile skapar ett layer
┌─────────────────────────────────────┐
│  Layer 4: COPY app.py              │  ← Ditt app-lager
├─────────────────────────────────────┤
│  Layer 3: RUN pip install flask     │  ← Dependencies
├─────────────────────────────────────┤
│  Layer 2: RUN apt-get update        │  ← System packages
├─────────────────────────────────────┤
│  Layer 1: FROM python:3.11          │  ← Base image
└─────────────────────────────────────┘
```

**Varje layer är immutable** - ändrar du något skapas ett nytt layer ovanpå.

---

## Arbeta med Images

```bash
# Ladda ner en image
docker pull nginx                    # Senaste versionen (latest)
docker pull nginx:1.25               # Specifik version
docker pull nginx:1.25-alpine        # Alpine-variant (mindre)

# Lista lokala images
docker images                        # Alla images
docker images nginx                  # Filtrera på namn

# Inspektera en image
docker inspect nginx                 # All metadata som JSON
docker history nginx                 # Visa alla layers

# Ta bort images
docker rmi nginx                     # Ta bort specifik image
docker image prune                   # Ta bort oanvända images
docker image prune -a                # Ta bort ALLA oanvända
```

---

## Image Tagging

```bash
# Format: registry/repository:tag
docker.io/library/nginx:1.25
│         │       │     │
│         │       │     └── Tag (version)
│         │       └── Repository (image-namn)
│         └── Namespace (user/org)
└── Registry (docker.io är default)

# Tagga en image
docker tag nginx:latest myregistry.com/nginx:v1.0
docker tag nginx:latest nginx:production

# Pusha till registry
docker push myregistry.com/nginx:v1.0
```

---

## Layer Caching

```bash
# Docker cachar layers för snabbare builds
# Om inget ändrats → använd cached layer

# DÅLIGT - cache invalideras vid varje kodändring
FROM python:3.11
COPY . /app                    # ← Ändras ofta → allt efter invalideras
RUN pip install -r requirements.txt

# BRA - dependencies cachas separat
FROM python:3.11
COPY requirements.txt /app/    # ← Ändras sällan
RUN pip install -r requirements.txt  # ← Cachas!
COPY . /app                    # ← Bara detta körs om vid kodändring
```

---

## Image-storlek

```bash
# Jämför storlekar
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

# Typiska storlekar:
# python:3.11          ~1 GB
# python:3.11-slim     ~150 MB
# python:3.11-alpine   ~50 MB

# Alpine är minst men kan ha kompatibilitetsproblem
# Slim är en bra kompromiss
```

---

## Key Takeaways

- Images består av **read-only layers** stackade på varandra
- **Layer caching** sparar tid - ordna Dockerfile smart
- Använd **specifika tags** i produktion, aldrig `latest`
- **Slim/Alpine** varianter sparar diskutrymme och minskar attack-yta
""",
        },
        {
            "title": "Container Lifecycle Management",
            "slug": "container-lifecycle-management",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Container Lifecycle Management

## Varför behöver du kunna detta?

Containers har en livscykel precis som processer. Du måste förstå:

- **Hur du startar och stoppar** containers korrekt
- **Skillnaden mellan stop och kill** för graceful shutdown
- **Hur du felsöker** containers som beter sig konstigt

---

## Container States

```bash
┌─────────┐     docker create     ┌─────────┐
│         │ ──────────────────▶   │ Created │
│  Image  │                       └────┬────┘
│         │                            │ docker start
└─────────┘                            ▼
                                 ┌─────────┐
              docker run ──────▶ │ Running │ ◀─── docker restart
                                 └────┬────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    │ docker stop     │ docker kill     │ exit/crash
                    ▼                 ▼                 ▼
              ┌─────────┐       ┌─────────┐       ┌─────────┐
              │ Exited  │       │ Exited  │       │ Exited  │
              │ (0)     │       │ (137)   │       │ (1)     │
              └─────────┘       └─────────┘       └─────────┘
```

---

## Starta Containers

```bash
# Kör container i förgrunden
docker run nginx                 # Blockerar terminalen

# Kör i bakgrunden (detached)
docker run -d nginx              # Returnerar container ID

# Kör med namn
docker run -d --name webserver nginx

# Kör och ta bort när den stoppar
docker run --rm nginx            # Perfekt för engångsjobb

# Kör interaktivt
docker run -it ubuntu bash       # -i = interactive, -t = tty
```

---

## Hantera körande containers

```bash
# Lista körande containers
docker ps

# Följ loggar
docker logs webserver            # Visa loggar
docker logs -f webserver         # Följ i realtid (tail -f)
docker logs --tail 100 webserver # Senaste 100 rader

# Kör kommandon i körande container
docker exec webserver ls /etc    # Kör kommando
docker exec -it webserver bash   # Öppna shell

# Inspektera container
docker inspect webserver         # All metadata
docker stats                     # CPU, minne, nätverk live
docker top webserver             # Processer i containern
```

---

## Stoppa Containers

```bash
# Graceful stop (skickar SIGTERM, väntar 10s, sen SIGKILL)
docker stop webserver

# Forcerad stop (SIGKILL direkt)
docker kill webserver

# Stoppa med timeout
docker stop -t 30 webserver      # Vänta 30 sekunder

# Starta om
docker restart webserver

# Pausa/återuppta (fryser processer)
docker pause webserver
docker unpause webserver
```

---

## Ta bort Containers

```bash
# Ta bort stoppad container
docker rm webserver

# Forcera borttagning av körande container
docker rm -f webserver

# Ta bort alla stoppade containers
docker container prune

# Ta bort alla containers (körande och stoppade)
docker rm -f $(docker ps -aq)
```

---

## Exit Codes

```bash
# Vanliga exit codes:
# 0   = Success (normal exit)
# 1   = General error
# 137 = SIGKILL (docker kill eller OOM)
# 143 = SIGTERM (docker stop)

# Kolla exit code
docker inspect webserver --format='{{.State.ExitCode}}'

# Kolla varför container stoppade
docker inspect webserver --format='{{.State.OOMKilled}}'
```

---

## Felsökning

```bash
# Container startar inte? Kolla loggar
docker logs container_name

# Container crashar direkt? Kör interaktivt
docker run -it image_name sh

# Kolla events
docker events                    # Realtids-events
docker events --since 1h         # Senaste timmen
```

---

## Key Takeaways

- Använd `docker stop` för **graceful shutdown** (SIGTERM)
- Använd `docker kill` bara när stop inte fungerar
- `--rm` flaggan är perfekt för **engångscontainers**
- **Exit codes** berättar varför containern stoppade
""",
        },
        {
            "title": "Dockerfile Mastery",
            "slug": "dockerfile-mastery",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Dockerfile Mastery

## Varför behöver du kunna detta?

Dockerfile är receptet för dina images. Du måste kunna:

- **Skriva effektiva Dockerfiles** som bygger snabbt
- **Optimera för storlek och säkerhet**
- **Förstå varje instruktion** så du kan felsöka build-problem

---

## Dockerfile Struktur

```dockerfile
# Kommentar
INSTRUKTION argument
```

Docker läser Dockerfile uppifrån och ner. Varje instruktion skapar ett nytt layer.

---

## De viktigaste instruktionerna

```dockerfile
# FROM - Välj base image (MÅSTE vara först)
FROM python:3.11-slim

# WORKDIR - Sätt arbetskatalog (skapar om den inte finns)
WORKDIR /app

# COPY - Kopiera filer från host till image
COPY requirements.txt .
COPY src/ ./src/

# RUN - Kör kommandon under build
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y curl

# ENV - Sätt miljövariabler
ENV PYTHONUNBUFFERED=1
ENV APP_ENV=production

# EXPOSE - Dokumentera vilken port appen lyssnar på
EXPOSE 8000

# CMD - Default-kommando när container startar
CMD ["python", "app.py"]
```

---

## COPY vs ADD

```dockerfile
# COPY - Enkel kopiering (rekommenderas)
COPY app.py /app/
COPY . /app/

# ADD - Kan mer men undvik om möjligt
ADD https://example.com/file.tar.gz /app/  # Laddar ner URL
ADD archive.tar.gz /app/                    # Auto-extraherar

# Använd COPY om du inte behöver ADD:s extra funktioner
```

---

## CMD vs ENTRYPOINT

```dockerfile
# CMD - Kan överskrivas vid docker run
CMD ["python", "app.py"]
# docker run myimage              → python app.py
# docker run myimage python test.py → python test.py (CMD ignoreras)

# ENTRYPOINT - Körs alltid, CMD blir argument
ENTRYPOINT ["python"]
CMD ["app.py"]
# docker run myimage              → python app.py
# docker run myimage test.py      → python test.py

# Kombinera för flexibilitet
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver"]
# docker run myimage              → python manage.py runserver
# docker run myimage migrate      → python manage.py migrate
```

---

## Optimerad Dockerfile

```dockerfile
# 1. Välj minimal base image
FROM python:3.11-slim

# 2. Sätt miljövariabler tidigt
ENV PYTHONUNBUFFERED=1 \\
    PYTHONDONTWRITEBYTECODE=1 \\
    PIP_NO_CACHE_DIR=1

# 3. Skapa non-root user
RUN useradd --create-home appuser

# 4. Sätt arbetskatalog
WORKDIR /app

# 5. Kopiera dependencies först (layer caching!)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 6. Kopiera applikationskod
COPY --chown=appuser:appuser . .

# 7. Byt till non-root user
USER appuser

# 8. Dokumentera port
EXPOSE 8000

# 9. Healthcheck
HEALTHCHECK --interval=30s --timeout=3s \\
    CMD curl -f http://localhost:8000/health || exit 1

# 10. Startkommando
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

---

## Multi-stage Builds

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# Resultat: Bara nginx + statiska filer, inte Node.js!
```

---

## .dockerignore

```bash
# .dockerignore - exkludera från COPY/ADD
node_modules
.git
.env
*.log
__pycache__
.pytest_cache
Dockerfile
docker-compose.yml
```

---

## Key Takeaways

- **Ordning spelar roll** - sätt saker som ändras sällan först (caching)
- **Multi-stage builds** minskar image-storlek dramatiskt
- Kör alltid som **non-root user** i produktion
- Använd **.dockerignore** för snabbare builds
""",
        },
        {
            "title": "Docker Networking",
            "slug": "docker-networking",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Docker Networking

## Varför behöver du kunna detta?

Containers behöver prata med varandra och omvärlden. Du måste förstå:

- **Olika network drivers** och när du använder vilken
- **Hur containers hittar varandra** via DNS
- **Port mapping** för att exponera tjänster

---

## Network Drivers

```bash
# Bridge (default) - containers på samma host
docker network create mynetwork

# Host - container delar hosts nätverk (ingen isolation)
docker run --network host nginx

# None - ingen nätverksåtkomst
docker run --network none alpine

# Overlay - containers över flera hosts (Swarm/Kubernetes)
docker network create -d overlay myoverlay
```

---

## Bridge Network (Default)

```bash
# Skapa ett nätverk
docker network create backend-net

# Starta containers i nätverket
docker run -d --name db --network backend-net postgres
docker run -d --name api --network backend-net myapi

# Nu kan api nå db via hostname "db"
# Inuti api-containern: ping db → fungerar!

# Lista nätverk
docker network ls

# Inspektera nätverk
docker network inspect backend-net
```

---

## Container DNS

```bash
# Docker har inbyggd DNS för containers i samma nätverk
# Hostname = container name

# Exempel: api behöver nå databas
docker run -d --name postgres --network mynet postgres
docker run -d --name api --network mynet \\
    -e DATABASE_URL=postgresql://postgres:5432/db \\
    myapi

# Inuti api: "postgres" resolvas automatiskt till rätt IP
```

---

## Port Mapping

```bash
# Exponera port till host
docker run -p 8080:80 nginx
#          │    │
#          │    └── Container port (nginx lyssnar på 80)
#          └── Host port (du når via localhost:8080)

# Exponera till specifik IP
docker run -p 127.0.0.1:8080:80 nginx  # Bara localhost

# Random host port
docker run -p 80 nginx                  # Docker väljer port
docker port container_name              # Se vilken port

# Flera portar
docker run -p 80:80 -p 443:443 nginx
```

---

## Praktiskt exempel

```bash
# Scenario: Web app + databas

# 1. Skapa nätverk
docker network create webapp-net

# 2. Starta databas (ingen port exponerad utåt!)
docker run -d \\
    --name db \\
    --network webapp-net \\
    -e POSTGRES_PASSWORD=secret \\
    postgres

# 3. Starta app som pratar med db internt
docker run -d \\
    --name webapp \\
    --network webapp-net \\
    -e DATABASE_HOST=db \\
    -p 8080:8000 \\
    mywebapp

# Resultat:
# - webapp nåbar på localhost:8080
# - db INTE nåbar utifrån (säkrare!)
# - webapp kan nå db via hostname "db"
```

---

## Network Troubleshooting

```bash
# Se vilka nätverk en container är i
docker inspect container_name --format='{{.NetworkSettings.Networks}}'

# Se alla containers i ett nätverk
docker network inspect mynet --format='{{range .Containers}}{{.Name}} {{end}}'

# Testa connectivity från container
docker exec webapp ping db
docker exec webapp curl http://api:8000/health

# Se nätverksstatistik
docker stats --format "table {{.Name}}\t{{.NetIO}}"
```

---

## Koppla container till flera nätverk

```bash
# Container kan vara i flera nätverk
docker network connect frontend-net webapp
docker network connect backend-net webapp

# Nu kan webapp prata med båda nätverken

# Koppla bort
docker network disconnect frontend-net webapp
```

---

## Key Takeaways

- Använd **user-defined bridge networks** för isolation
- Containers i samma nätverk kan nå varandra via **hostname**
- **Exponera bara nödvändiga portar** till host
- `-p 127.0.0.1:8080:80` begränsar till localhost
""",
        },
        {
            "title": "Docker Volumes & Persistence",
            "slug": "docker-volumes-persistence",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Volumes & Persistence

## Varför behöver du kunna detta?

Containers är ephemeral - data försvinner när de tas bort. Du måste förstå:

- **Hur du persisterar data** som databaser och uploads
- **Skillnaden mellan volumes och bind mounts**
- **Backup och restore** av container-data

---

## Problemet utan volumes

```bash
# Starta databas
docker run -d --name db postgres

# Skriv data...
# Stoppa och ta bort
docker rm -f db

# All data är BORTA! 💥
```

---

## Tre sätt att persistera data

```bash
# 1. Volumes (Docker-managed) - REKOMMENDERAS
docker run -v mydata:/var/lib/postgresql/data postgres

# 2. Bind mounts (host path)
docker run -v /host/path:/container/path postgres

# 3. tmpfs (RAM-disk, försvinner vid stopp)
docker run --tmpfs /tmp postgres
```

---

## Volumes (Docker-managed)

```bash
# Skapa volume
docker volume create dbdata

# Använd volume
docker run -d \\
    --name postgres \\
    -v dbdata:/var/lib/postgresql/data \\
    postgres

# Lista volumes
docker volume ls

# Inspektera volume
docker volume inspect dbdata

# Ta bort volume
docker volume rm dbdata

# Ta bort oanvända volumes
docker volume prune
```

---

## Bind Mounts

```bash
# Montera host-katalog i container
docker run -v $(pwd)/app:/app myimage

# Read-only mount
docker run -v $(pwd)/config:/etc/app/config:ro myimage

# Användningsområden:
# - Utveckling (live reload)
# - Konfig-filer
# - Loggar du vill nå från host
```

---

## Volumes vs Bind Mounts

```bash
# Volumes
# ✅ Docker hanterar lagring
# ✅ Fungerar på alla plattformar
# ✅ Kan backas upp med docker-kommandon
# ✅ Kan delas mellan containers

# Bind mounts
# ✅ Du kontrollerar exakt var data sparas
# ✅ Bra för utveckling (hot reload)
# ❌ Beroende av host path
# ❌ Permissions kan bli krångligt
```

---

## Praktiskt exempel: Databas

```bash
# Skapa persistent PostgreSQL
docker volume create pgdata

docker run -d \\
    --name postgres \\
    -v pgdata:/var/lib/postgresql/data \\
    -e POSTGRES_PASSWORD=secret \\
    postgres

# Data överlever container restart/removal
docker rm -f postgres
docker run -d --name postgres -v pgdata:/var/lib/postgresql/data postgres
# Data finns kvar! ✅
```

---

## Backup och Restore

```bash
# Backup volume till tar-fil
docker run --rm \\
    -v pgdata:/source:ro \\
    -v $(pwd):/backup \\
    alpine tar czf /backup/pgdata-backup.tar.gz -C /source .

# Restore från backup
docker run --rm \\
    -v pgdata:/target \\
    -v $(pwd):/backup \\
    alpine tar xzf /backup/pgdata-backup.tar.gz -C /target
```

---

## Key Takeaways

- Använd **volumes för produktionsdata** (databaser, uploads)
- Använd **bind mounts för utveckling** (kod, config)
- Data i volumes **överlever** container removal
- **Backup regelbundet** - volumes är inte automatiskt säkrade
""",
        },
        {
            "title": "Docker Compose Fundamentals",
            "slug": "docker-compose-fundamentals",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Docker Compose Fundamentals

## Varför behöver du kunna detta?

Att köra `docker run` med 10 flaggor för flera containers är opraktiskt. Du behöver:

- **Definiera hela stacken** i en fil
- **Starta allt med ett kommando**
- **Versionshantera infrastrukturen** som kod

---

## Vad är Docker Compose?

Docker Compose låter dig definiera multi-container applikationer i en YAML-fil. Istället för:

```bash
docker network create mynet
docker run -d --name db --network mynet -v dbdata:/data postgres
docker run -d --name api --network mynet -p 8080:8000 -e DB_HOST=db myapi
```

Skriver du:

```yaml
# docker-compose.yml
services:
  db:
    image: postgres
    volumes:
      - dbdata:/data
  api:
    image: myapi
    ports:
      - "8080:8000"
    environment:
      - DB_HOST=db

volumes:
  dbdata:
```

---

## Grundläggande struktur

```yaml
# docker-compose.yml
version: "3.8"  # Compose file version (optional i nya versioner)

services:       # Containers att köra
  service1:
    image: ...
  service2:
    build: ...

volumes:        # Named volumes
  data:

networks:       # Custom networks
  frontend:
  backend:
```

---

## Service-konfiguration

```yaml
services:
  webapp:
    # Välj image ELLER build
    image: nginx:alpine
    # ELLER
    build: ./app
    build:
      context: ./app
      dockerfile: Dockerfile.prod

    # Port mapping
    ports:
      - "8080:80"
      - "443:443"

    # Miljövariabler
    environment:
      - NODE_ENV=production
      - API_KEY=secret
    env_file:
      - .env

    # Volumes
    volumes:
      - ./app:/app          # Bind mount
      - data:/var/lib/data  # Named volume

    # Dependencies
    depends_on:
      - db
      - redis

    # Restart policy
    restart: unless-stopped

    # Resource limits
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

---

## Grundläggande kommandon

```bash
# Starta alla services
docker compose up

# Starta i bakgrunden
docker compose up -d

# Stoppa alla services
docker compose down

# Stoppa och ta bort volumes
docker compose down -v

# Se status
docker compose ps

# Se loggar
docker compose logs
docker compose logs -f webapp  # Följ specifik service

# Bygg om images
docker compose build
docker compose up --build  # Build + start
```

---

## Komplett exempel

```yaml
# docker-compose.yml
services:
  # Frontend
  web:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - API_URL=http://api:8000
    depends_on:
      - api

  # Backend API
  api:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    volumes:
      - ./backend:/app  # Hot reload i utveckling

  # Database
  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=app
    volumes:
      - pgdata:/var/lib/postgresql/data
    # Ingen port exponerad - bara intern access

  # Cache
  redis:
    image: redis:alpine

volumes:
  pgdata:
```

---

## Key Takeaways

- **En fil = hela stacken** - lätt att versionshantera
- Services i samma compose-fil får **automatiskt nätverk**
- Använd **depends_on** för start-ordning
- `docker compose down -v` tar bort **allt** inkl volumes
""",
        },
        {
            "title": "Docker Compose Advanced Patterns",
            "slug": "docker-compose-advanced-patterns",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Docker Compose Advanced Patterns

## Varför behöver du kunna detta?

Grundläggande Compose räcker för utveckling, men produktion kräver mer:

- **Miljöspecifik konfiguration** (dev vs prod)
- **Healthchecks och restart policies**
- **Skalning och load balancing**

---

## Multiple Compose Files

```bash
# Bas-konfiguration
# docker-compose.yml
services:
  api:
    build: .
    environment:
      - DATABASE_URL=postgresql://db:5432/app

# Development overrides
# docker-compose.override.yml (laddas automatiskt)
services:
  api:
    volumes:
      - .:/app  # Hot reload
    environment:
      - DEBUG=true

# Production overrides
# docker-compose.prod.yml
services:
  api:
    image: myregistry/api:${VERSION}
    restart: always
    deploy:
      replicas: 3

# Kör med specifik override
docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

---

## Healthchecks

```yaml
services:
  api:
    image: myapi
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  db:
    image: postgres
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Vänta på att dependency är healthy
  api:
    depends_on:
      db:
        condition: service_healthy
```

---

## Environment Variables

```yaml
services:
  api:
    image: myapi
    environment:
      # Direkt värde
      - NODE_ENV=production
      # Från host environment
      - API_KEY=${API_KEY}
      # Med default
      - PORT=${PORT:-8000}

    # Eller från fil
    env_file:
      - .env
      - .env.local
```

```bash
# .env
POSTGRES_PASSWORD=secret
API_KEY=abc123
```

---

## Profiles

```yaml
services:
  api:
    image: myapi
    # Alltid aktiv (inget profile)

  debug-tools:
    image: busybox
    profiles:
      - debug
    # Startas bara med: docker compose --profile debug up

  monitoring:
    image: prometheus
    profiles:
      - monitoring
      - production
```

```bash
# Starta med specifika profiles
docker compose --profile debug up
docker compose --profile monitoring --profile debug up
```

---

## Skalning

```yaml
services:
  worker:
    image: myworker
    deploy:
      replicas: 3  # Starta 3 instanser
      resources:
        limits:
          cpus: '0.5'
          memory: 256M
```

```bash
# Skala dynamiskt
docker compose up -d --scale worker=5
```

---

## Secrets

```yaml
services:
  api:
    image: myapi
    secrets:
      - db_password
      - api_key

secrets:
  db_password:
    file: ./secrets/db_password.txt
  api_key:
    environment: API_KEY
```

```bash
# I containern läses secrets från:
# /run/secrets/db_password
# /run/secrets/api_key
```

---

## Extension Fields (YAML anchors)

```yaml
# Återanvänd konfiguration
x-common-env: &common-env
  LOG_LEVEL: info
  TZ: Europe/Stockholm

x-healthcheck: &default-healthcheck
  interval: 30s
  timeout: 10s
  retries: 3

services:
  api:
    environment:
      <<: *common-env
      SERVICE_NAME: api
    healthcheck:
      <<: *default-healthcheck
      test: curl -f http://localhost:8000/health

  worker:
    environment:
      <<: *common-env
      SERVICE_NAME: worker
```

---

## Key Takeaways

- Använd **override files** för miljöspecifik config
- **Healthchecks** är kritiska för produktion
- **Profiles** för att gruppera valfria services
- **Secrets** för känslig data (inte environment variables)
""",
        },
        {
            "title": "Docker Security Best Practices",
            "slug": "docker-security-best-practices",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker Security Best Practices

## Varför behöver du kunna detta?

Containers är inte automatiskt säkra. Du måste förstå:

- **Vanliga säkerhetsrisker** och hur du undviker dem
- **Principle of least privilege** för containers
- **Image scanning** för sårbarheter

---

## Kör ALDRIG som root

```dockerfile
# DÅLIGT - kör som root (default)
FROM python:3.11
COPY app.py /app/
CMD ["python", "/app/app.py"]

# BRA - skapa och använd non-root user
FROM python:3.11
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /home/appuser
COPY --chown=appuser:appuser app.py .
USER appuser
CMD ["python", "app.py"]
```

---

## Minimal Base Images

```dockerfile
# DÅLIGT - full OS med massa onödiga paket
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3

# BRA - minimal image
FROM python:3.11-slim

# BÄST (om möjligt) - distroless
FROM gcr.io/distroless/python3
```

```bash
# Jämför storlekar:
# ubuntu:22.04     ~77 MB
# python:3.11      ~1 GB
# python:3.11-slim ~150 MB
# distroless       ~50 MB
```

---

## Använd specifika tags

```dockerfile
# DÅLIGT - kan ändras när som helst
FROM python:latest
FROM nginx

# BRA - specifik version
FROM python:3.11.7-slim
FROM nginx:1.25.3-alpine

# BÄST - sha256 digest (immutable)
FROM python@sha256:abc123...
```

---

## Read-only filsystem

```bash
# Kör container med read-only root filesystem
docker run --read-only myimage

# Tillåt skrivning till specifika paths
docker run --read-only \\
    --tmpfs /tmp \\
    --tmpfs /var/run \\
    -v logs:/var/log \\
    myimage
```

---

## Begränsa capabilities

```bash
# Containers får för många Linux capabilities by default
# Ta bort alla och lägg till bara det som behövs

docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myimage

# Vanliga capabilities:
# NET_BIND_SERVICE - bind to ports < 1024
# CHOWN - change file ownership
# SETUID/SETGID - change user/group ID
```

---

## Resource Limits

```bash
# Utan limits kan en container ta alla resurser
docker run \\
    --memory=512m \\
    --memory-swap=512m \\
    --cpus=0.5 \\
    --pids-limit=100 \\
    myimage
```

```yaml
# docker-compose.yml
services:
  api:
    image: myapi
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          memory: 256M
```

---

## Image Scanning

```bash
# Scanna image för sårbarheter
docker scout cves myimage
docker scout recommendations myimage

# Trivy (populärt open source alternativ)
trivy image myimage

# Snyk
snyk container test myimage
```

---

## Secrets Hantering

```bash
# DÅLIGT - secrets i environment variables
docker run -e DATABASE_PASSWORD=secret123 myimage

# DÅLIGT - secrets i Dockerfile
ENV API_KEY=secret123

# BRA - Docker secrets
docker secret create db_pass ./password.txt
docker run --secret db_pass myimage
# Läses från /run/secrets/db_pass

# BRA - External secret management
# HashiCorp Vault, AWS Secrets Manager, etc.
```

---

## Network Security

```bash
# Isolera containers i egna nätverk
docker network create --internal backend
# --internal = ingen internet-access

# Exponera bara nödvändiga portar
docker run -p 127.0.0.1:8080:8080 myimage  # Bara localhost
```

---

## Security Checklist

```bash
# ✅ Non-root user
# ✅ Minimal base image (slim/alpine/distroless)
# ✅ Specifika image tags
# ✅ Read-only filesystem där möjligt
# ✅ Dropped capabilities
# ✅ Resource limits
# ✅ No secrets i images/env vars
# ✅ Regelbunden image scanning
# ✅ Isolerade nätverk
```

---

## Key Takeaways

- **Kör aldrig som root** - skapa en appuser
- **Minimal images** = mindre attack surface
- **Scanna images** regelbundet för CVEs
- **Secrets hör inte hemma** i env vars eller Dockerfiles
""",
        },
        {
            "title": "Docker in Production",
            "slug": "docker-in-production",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Docker in Production

## Varför behöver du kunna detta?

Att köra Docker lokalt är en sak - produktion är en annan. Du måste förstå:

- **Logging och monitoring** för att veta vad som händer
- **Restart policies** för att hantera crashes
- **Resource management** för stabil drift

---

## Restart Policies

```bash
# no - starta aldrig om (default)
docker run --restart no myimage

# always - starta alltid om (även vid reboot)
docker run --restart always myimage

# unless-stopped - som always, men inte om manuellt stoppad
docker run --restart unless-stopped myimage

# on-failure - bara vid crash (exit code != 0)
docker run --restart on-failure:5 myimage  # Max 5 försök
```

```yaml
# docker-compose.yml
services:
  api:
    image: myapi
    restart: unless-stopped
```

---

## Logging

```bash
# Se loggar
docker logs container_name
docker logs -f container_name      # Follow
docker logs --tail 100 container_name
docker logs --since 1h container_name

# Log drivers
docker run --log-driver json-file \\
    --log-opt max-size=10m \\
    --log-opt max-file=3 \\
    myimage

# Centraliserad logging (exempel: Fluentd)
docker run --log-driver fluentd \\
    --log-opt fluentd-address=localhost:24224 \\
    myimage
```

---

## Monitoring

```bash
# Real-time stats
docker stats

# Format output
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# Health status
docker inspect --format='{{.State.Health.Status}}' container_name
```

---

## Healthchecks

```dockerfile
# I Dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1
```

```bash
# Vid runtime
docker run --health-cmd="curl -f http://localhost:8000/health" \\
    --health-interval=30s \\
    --health-timeout=3s \\
    --health-retries=3 \\
    myimage

# Kolla health status
docker inspect --format='{{json .State.Health}}' container_name
```

---

## Production Docker Compose

```yaml
# docker-compose.prod.yml
services:
  api:
    image: myregistry/api:${VERSION:-latest}
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
    healthcheck:
      test: curl -f http://localhost:8000/health
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
    environment:
      - NODE_ENV=production
    secrets:
      - db_password

  db:
    image: postgres:15
    restart: unless-stopped
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: pg_isready -U postgres
      interval: 10s
      timeout: 5s
      retries: 5
    # Ingen port exponerad utåt!

secrets:
  db_password:
    external: true

volumes:
  pgdata:
```

---

## Blue-Green Deployment

```bash
# Starta ny version
docker compose -p myapp-green up -d

# Testa att den fungerar
curl http://localhost:8081/health

# Byt trafik (via load balancer/nginx)
# ...

# Ta bort gamla versionen
docker compose -p myapp-blue down
```

---

## Rolling Updates

```bash
# Med Docker Swarm
docker service update --image myimage:v2 myservice

# Med Compose (manuellt)
docker compose pull
docker compose up -d --no-deps --build api
```

---

## Backup Strategy

```bash
# Backup volumes regelbundet
docker run --rm \\
    -v mydata:/source:ro \\
    -v $(pwd)/backups:/backup \\
    alpine tar czf /backup/mydata-$(date +%Y%m%d).tar.gz -C /source .

# Backup databas
docker exec postgres pg_dump -U postgres mydb > backup.sql
```

---

## Key Takeaways

- Använd `restart: unless-stopped` för produktionscontainers
- **Healthchecks** är obligatoriska i produktion
- **Resource limits** förhindrar att en container tar ner allt
- **Centraliserad logging** för att kunna felsöka
""",
        },
        {
            "title": "Docker Registry & Image Distribution",
            "slug": "docker-registry-image-distribution",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Registry & Image Distribution

## Varför behöver du kunna detta?

Images måste lagras och distribueras. Du måste förstå:

- **Hur registries fungerar** och vilka alternativ som finns
- **Push och pull** av images
- **Private registries** för företagsbruk

---

## Vad är ett Registry?

Ett registry är en lagringsplats för Docker images. Tänk på det som "npm för containers".

```bash
# Image naming convention
registry.example.com/namespace/repository:tag
│                    │         │          │
│                    │         │          └── Version (default: latest)
│                    │         └── Image name
│                    └── User/Organization
└── Registry URL (default: docker.io)
```

---

## Docker Hub (Public)

```bash
# Logga in
docker login

# Tagga för Docker Hub
docker tag myimage username/myimage:v1.0

# Pusha till Docker Hub
docker push username/myimage:v1.0

# Pulla
docker pull username/myimage:v1.0
```

---

## Private Registries

```bash
# AWS ECR
aws ecr get-login-password --region eu-north-1 | \\
    docker login --username AWS --password-stdin 123456789.dkr.ecr.eu-north-1.amazonaws.com

docker tag myimage 123456789.dkr.ecr.eu-north-1.amazonaws.com/myimage:v1
docker push 123456789.dkr.ecr.eu-north-1.amazonaws.com/myimage:v1

# Google Container Registry
gcloud auth configure-docker
docker tag myimage gcr.io/my-project/myimage:v1
docker push gcr.io/my-project/myimage:v1

# Azure Container Registry
az acr login --name myregistry
docker tag myimage myregistry.azurecr.io/myimage:v1
docker push myregistry.azurecr.io/myimage:v1

# GitHub Container Registry
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
docker tag myimage ghcr.io/username/myimage:v1
docker push ghcr.io/username/myimage:v1
```

---

## Self-hosted Registry

```bash
# Starta eget registry
docker run -d -p 5000:5000 --name registry registry:2

# Använd det
docker tag myimage localhost:5000/myimage:v1
docker push localhost:5000/myimage:v1
docker pull localhost:5000/myimage:v1
```

---

## Image Tagging Strategy

```bash
# Semantisk versioning
myimage:1.0.0          # Specifik version
myimage:1.0            # Minor version
myimage:1              # Major version
myimage:latest         # Senaste (undvik i produktion!)

# Git-baserad
myimage:main           # Branch
myimage:abc123f        # Commit SHA
myimage:v1.2.3-abc123f # Version + SHA

# Timestamp
myimage:20241207-143022
```

---

## Multi-platform Images

```bash
# Bygg för flera arkitekturer
docker buildx create --name mybuilder --use

docker buildx build \\
    --platform linux/amd64,linux/arm64 \\
    -t myimage:v1 \\
    --push \\
    .

# Inspektera manifest
docker manifest inspect myimage:v1
```

---

## Key Takeaways

- **Docker Hub** för public images, **private registry** för företaget
- Använd **specifika tags** i produktion, aldrig `latest`
- **Multi-platform builds** för ARM/AMD64 kompatibilitet
- Logga in innan push/pull till private registries
""",
        },
        {
            "title": "Docker Multi-stage Builds",
            "slug": "docker-multi-stage-builds",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Multi-stage Builds

## Varför behöver du kunna detta?

Build-verktyg och dependencies behövs inte i produktion. Du måste kunna:

- **Separera build och runtime** för mindre images
- **Kopiera artefakter** mellan stages
- **Optimera för säkerhet** genom att exkludera build-verktyg

---

## Problemet utan multi-stage

```dockerfile
# Allt i en stage = stor image med onödiga verktyg
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
# Image innehåller: Node.js, npm, devDependencies, source code, build tools...
# Storlek: ~1 GB
CMD ["node", "dist/index.js"]
```

---

## Multi-stage lösningen

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-slim
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER node
CMD ["node", "dist/index.js"]
# Image innehåller: Bara runtime + compiled code
# Storlek: ~150 MB
```

---

## Go Example (statisk binär)

```dockerfile
# Build stage
FROM golang:1.21 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o /app/server

# Production stage - minimal!
FROM scratch
COPY --from=builder /app/server /server
USER 1000
ENTRYPOINT ["/server"]
# Image storlek: ~10-20 MB (bara binären!)
```

---

## Python Example

```dockerfile
# Build stage
FROM python:3.11 AS builder
WORKDIR /app
RUN pip install --user poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt -o requirements.txt
RUN pip install --user -r requirements.txt

# Production stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
USER nobody
CMD ["python", "app.py"]
```

---

## React/Frontend Example

```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage - bara statiska filer!
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
# Image storlek: ~25 MB
```

---

## Flera build stages

```dockerfile
# Base stage med gemensamma dependencies
FROM node:18-slim AS base
WORKDIR /app
COPY package*.json ./

# Development dependencies
FROM base AS dev-deps
RUN npm ci

# Production dependencies
FROM base AS prod-deps
RUN npm ci --omit=dev

# Build
FROM dev-deps AS builder
COPY . .
RUN npm run build

# Test (kan köras separat)
FROM dev-deps AS tester
COPY . .
RUN npm test

# Production
FROM node:18-slim
WORKDIR /app
COPY --from=prod-deps /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
USER node
CMD ["node", "dist/index.js"]
```

---

## Kopiera från externa images

```dockerfile
# Kopiera verktyg från annan image
FROM alpine
COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin/
COPY --from=hashicorp/terraform:latest /bin/terraform /usr/local/bin/
```

---

## Key Takeaways

- **Separera build och runtime** - dramatiskt mindre images
- `COPY --from=stage` kopierar filer mellan stages
- Bara **sista FROM** blir den slutliga imagen
- Använd **slim/alpine/scratch** för production stage
""",
        },
        {
            "title": "Docker Performance Optimization",
            "slug": "docker-performance-optimization",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker Performance Optimization

## Varför behöver du kunna detta?

Långsamma builds och stora images kostar tid och pengar. Du måste kunna:

- **Optimera build-tid** genom smart caching
- **Minska image-storlek** för snabbare deploys
- **Förbättra runtime-prestanda**

---

## Build Cache Optimization

```dockerfile
# DÅLIGT - cache invalideras vid varje kodändring
FROM python:3.11
COPY . /app
RUN pip install -r requirements.txt

# BRA - dependencies cachas separat
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt  # Cachas om requirements.txt inte ändras
COPY . .
```

---

## Layer Order Matters

```dockerfile
# Ordna från minst till mest ändrade
FROM node:18-slim

# 1. System packages (ändras sällan)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 2. Dependencies (ändras ibland)
COPY package*.json ./
RUN npm ci

# 3. Application code (ändras ofta)
COPY . .

# 4. Build (beror på kod)
RUN npm run build
```

---

## Minska antal layers

```dockerfile
# DÅLIGT - varje RUN skapar ett layer
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN rm -rf /var/lib/apt/lists/*

# BRA - kombinera till ett layer
RUN apt-get update && \\
    apt-get install -y \\
        curl \\
        git && \\
    rm -rf /var/lib/apt/lists/*
```

---

## .dockerignore

```bash
# .dockerignore - exkludera onödiga filer från COPY
node_modules
.git
.gitignore
*.md
Dockerfile*
docker-compose*
.env*
__pycache__
*.pyc
.pytest_cache
coverage
.nyc_output
dist
build
```

---

## BuildKit Features

```bash
# Aktivera BuildKit (snabbare builds)
export DOCKER_BUILDKIT=1
docker build .

# Eller
docker buildx build .

# Cache mount - cachar paketmanagers
FROM python:3.11
RUN --mount=type=cache,target=/root/.cache/pip \\
    pip install -r requirements.txt

# Bind mount - undviker COPY för build-time filer
RUN --mount=type=bind,source=package.json,target=/app/package.json \\
    npm install
```

---

## Image Size Reduction

```dockerfile
# 1. Välj minimal base image
FROM python:3.11-slim  # istället för python:3.11

# 2. Ta bort cache och temp-filer
RUN pip install --no-cache-dir -r requirements.txt

# 3. Ta bort package manager cache
RUN apt-get update && \\
    apt-get install -y curl && \\
    apt-get clean && \\
    rm -rf /var/lib/apt/lists/*

# 4. Multi-stage build (kopiera bara det som behövs)
```

---

## Analysera image-storlek

```bash
# Se layers och storlekar
docker history myimage

# Dive - interaktiv analys
dive myimage

# Docker Scout
docker scout quickview myimage
```

---

## Runtime Performance

```bash
# Resource limits
docker run \\
    --cpus=2 \\
    --memory=2g \\
    --memory-swap=2g \\  # Disable swap
    myimage

# CPU pinning (specifika cores)
docker run --cpuset-cpus="0,1" myimage

# Ulimits
docker run --ulimit nofile=65535:65535 myimage
```

---

## Storage Driver

```bash
# Kolla aktuell storage driver
docker info | grep "Storage Driver"

# overlay2 är rekommenderat för de flesta
# Undvik devicemapper och aufs
```

---

## Key Takeaways

- **Ordning spelar roll** - sätt saker som ändras sällan först
- Använd **.dockerignore** för snabbare COPY
- **BuildKit** ger snabbare builds och bättre caching
- **Analysera images** med `dive` eller `docker history`
""",
        },
        {
            "title": "Docker Debugging & Troubleshooting",
            "slug": "docker-debugging-troubleshooting",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Debugging & Troubleshooting

## Varför behöver du kunna detta?

Containers kommer att krasha och bete sig konstigt. Du måste kunna:

- **Hitta vad som gick fel** via loggar och inspect
- **Debugga körande containers** utan att störa produktion
- **Hantera vanliga problem** snabbt

---

## Container startar inte

```bash
# Steg 1: Kolla loggar
docker logs container_name
docker logs --tail 50 container_name

# Steg 2: Kolla exit code
docker inspect container_name --format='{{.State.ExitCode}}'
# 0 = OK, 1 = Error, 137 = OOM/Kill, 143 = SIGTERM

# Steg 3: Kör interaktivt för att debugga
docker run -it --entrypoint sh myimage
docker run -it --entrypoint bash myimage

# Steg 4: Kolla events
docker events --since 10m
```

---

## Inspektera containers

```bash
# Full metadata
docker inspect container_name

# Specifik info
docker inspect container_name --format='{{.State.Status}}'
docker inspect container_name --format='{{.NetworkSettings.IPAddress}}'
docker inspect container_name --format='{{json .Config.Env}}'

# Processer i container
docker top container_name

# Resource usage
docker stats container_name
```

---

## Debugga körande container

```bash
# Öppna shell i körande container
docker exec -it container_name sh
docker exec -it container_name bash

# Kör kommando utan shell
docker exec container_name cat /etc/hosts
docker exec container_name env

# Som root (om container kör som non-root)
docker exec -u 0 container_name bash
```

---

## Nätverksproblem

```bash
# Kolla container IP
docker inspect container_name --format='{{.NetworkSettings.IPAddress}}'

# Lista nätverk
docker network ls

# Inspektera nätverk
docker network inspect bridge

# Testa connectivity från container
docker exec container_name ping other_container
docker exec container_name curl http://other_container:8080
docker exec container_name nslookup other_container

# Kolla port mappings
docker port container_name
```

---

## Loggproblem

```bash
# Inga loggar? Appen kanske loggar till fil
docker exec container_name cat /var/log/app.log

# Loggar för stora? Kolla log settings
docker inspect container_name --format='{{json .HostConfig.LogConfig}}'

# Rensa loggar (json-file driver)
truncate -s 0 $(docker inspect --format='{{.LogPath}}' container_name)
```

---

## Disk/Storage problem

```bash
# Kolla disk usage
docker system df

# Detaljerad
docker system df -v

# Rensa oanvända resurser
docker system prune        # Containers, networks, images
docker system prune -a     # + alla oanvända images
docker system prune --volumes  # + volumes

# Kolla volume
docker volume inspect myvolume
```

---

## OOM (Out of Memory)

```bash
# Kolla om container blev OOM-killed
docker inspect container_name --format='{{.State.OOMKilled}}'

# Kolla memory limit vs usage
docker stats container_name --no-stream

# Öka memory limit
docker update --memory=2g container_name
```

---

## Image problem

```bash
# Image finns inte
docker pull myimage:tag  # Pulla explicit

# Kolla image layers
docker history myimage

# Inspektera image
docker inspect myimage

# Verifiera image
docker image inspect myimage --format='{{.Id}}'
```

---

## Debug Dockerfile

```bash
# Bygg med output
DOCKER_BUILDKIT=0 docker build -t myimage .

# Stanna vid specifik stage
docker build --target builder -t myimage-debug .

# Kör en "failed" build interaktivt
# 1. Hitta sista lyckade layer ID i build output
# 2. docker run -it <layer-id> sh
```

---

## Vanliga fel och lösningar

```bash
# "Permission denied"
# → Kolla att USER i Dockerfile har rätt rättigheter
# → Kolla volume permissions

# "Port already in use"
docker ps | grep :8080
docker stop container_using_port

# "No space left on device"
docker system prune -a --volumes

# "Cannot connect to Docker daemon"
sudo systemctl start docker
# Eller: lägg till user i docker-gruppen
```

---

## Key Takeaways

- **Loggar först** - `docker logs` är din bästa vän
- **Exit codes berättar** varför container stoppade
- `docker exec -it` för att **debugga körande containers**
- `docker system prune` när **disken är full**
""",
        },
        {
            "title": "Docker with CI/CD",
            "slug": "docker-with-cicd",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker with CI/CD

## Varför behöver du kunna detta?

Docker och CI/CD hör ihop. Du måste kunna:

- **Bygga och testa** images automatiskt
- **Pusha till registry** från pipeline
- **Deploya** nya versioner automatiskt

---

## GitHub Actions

```yaml
# .github/workflows/docker.yml
name: Docker Build & Push

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: |
            username/myapp:latest
            username/myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

---

## GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - deploy

variables:
  IMAGE_TAG: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $IMAGE_TAG .
    - docker push $IMAGE_TAG

test:
  stage: test
  image: $IMAGE_TAG
  script:
    - npm test

deploy:
  stage: deploy
  script:
    - docker pull $IMAGE_TAG
    - docker stop myapp || true
    - docker rm myapp || true
    - docker run -d --name myapp -p 80:8000 $IMAGE_TAG
  only:
    - main
```

---

## Smart Tagging Strategy

```yaml
# GitHub Actions - multiple tags
- name: Docker meta
  id: meta
  uses: docker/metadata-action@v5
  with:
    images: username/myapp
    tags: |
      type=ref,event=branch
      type=ref,event=pr
      type=semver,pattern={{version}}
      type=sha,prefix=

# Resultat:
# - main branch: myapp:main
# - PR #123: myapp:pr-123
# - Tag v1.2.3: myapp:1.2.3
# - Alltid: myapp:abc1234 (SHA)
```

---

## Layer Caching i CI

```yaml
# GitHub Actions med cache
- name: Build and push
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: myapp:latest
    cache-from: type=gha
    cache-to: type=gha,mode=max

# Eller registry-based cache
    cache-from: type=registry,ref=myapp:buildcache
    cache-to: type=registry,ref=myapp:buildcache,mode=max
```

---

## Security Scanning i Pipeline

```yaml
# GitHub Actions
- name: Run Trivy vulnerability scanner
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: myapp:${{ github.sha }}
    format: 'sarif'
    output: 'trivy-results.sarif'

- name: Upload Trivy scan results
  uses: github/codeql-action/upload-sarif@v2
  with:
    sarif_file: 'trivy-results.sarif'
```

---

## Multi-platform Builds

```yaml
- name: Set up QEMU
  uses: docker/setup-qemu-action@v3

- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3

- name: Build and push
  uses: docker/build-push-action@v5
  with:
    context: .
    platforms: linux/amd64,linux/arm64
    push: true
    tags: myapp:latest
```

---

## Deploy with Docker Compose

```yaml
deploy:
  stage: deploy
  script:
    - ssh user@server "
        cd /app &&
        docker compose pull &&
        docker compose up -d --remove-orphans
      "
  environment:
    name: production
  only:
    - main
```

---

## Key Takeaways

- **Tagga med SHA** för spårbarhet
- **Cache layers** för snabbare builds
- **Scanna images** för sårbarheter i pipeline
- **Multi-platform** för ARM/AMD64 stöd
""",
        },
        {
            "title": "Docker Swarm Basics",
            "slug": "docker-swarm-basics",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Swarm Basics

## Varför behöver du kunna detta?

Swarm är Dockers inbyggda orkestrering. Du behöver förstå det för att:

- **Köra containers över flera hosts**
- **Förstå orkestreringskoncept** innan Kubernetes
- **Hantera enklare produktionsmiljöer**

---

## Vad är Docker Swarm?

Docker Swarm är clustering och orkestrering inbyggt i Docker. Det är enklare än Kubernetes men har färre features.

```bash
# Swarm arkitektur
┌─────────────────────────────────────────────────────┐
│                    Manager Nodes                     │
│  (Hanterar klustret, schemalägger tasks)            │
├─────────────────────────────────────────────────────┤
│                    Worker Nodes                      │
│  (Kör containers/tasks)                              │
└─────────────────────────────────────────────────────┘
```

---

## Initiera Swarm

```bash
# Gör denna maskin till manager
docker swarm init

# Visa join token för workers
docker swarm join-token worker

# Lägg till worker (kör på worker-maskinen)
docker swarm join --token SWMTKN-xxx manager-ip:2377

# Lista noder
docker node ls
```

---

## Services

```bash
# Skapa en service (istället för docker run)
docker service create --name web --replicas 3 -p 8080:80 nginx

# Lista services
docker service ls

# Se tasks (containers) för en service
docker service ps web

# Skala service
docker service scale web=5

# Uppdatera service
docker service update --image nginx:1.25 web

# Ta bort service
docker service rm web
```

---

## Stacks (Swarm + Compose)

```yaml
# docker-compose.yml (för Swarm)
version: "3.8"
services:
  web:
    image: nginx
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
    ports:
      - "80:80"
```

```bash
# Deploya stack
docker stack deploy -c docker-compose.yml mystack

# Lista stacks
docker stack ls

# Se services i stack
docker stack services mystack

# Ta bort stack
docker stack rm mystack
```

---

## Rolling Updates

```bash
# Uppdatera image med rolling update
docker service update \\
    --image nginx:1.25 \\
    --update-parallelism 1 \\
    --update-delay 10s \\
    web

# Rollback om något går fel
docker service rollback web
```

---

## Key Takeaways

- **Swarm är enklare** än Kubernetes men mindre kraftfullt
- **Services** ersätter containers för skalning
- **Stacks** är Compose-filer för Swarm
- Bra för **mindre produktionsmiljöer**
""",
        },
        {
            "title": "Docker Best Practices Summary",
            "slug": "docker-best-practices-summary",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 75,
            "content": """# Docker Best Practices Summary

## Varför behöver du kunna detta?

En sammanfattning av alla best practices för att skriva professionella Dockerfiles och köra containers i produktion.

---

## Dockerfile Best Practices

```dockerfile
# 1. Använd specifik base image tag
FROM python:3.11.7-slim  # Inte python:latest

# 2. Använd multi-stage builds
FROM node:18 AS builder
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html

# 3. Minimera layers
RUN apt-get update && \\
    apt-get install -y curl && \\
    rm -rf /var/lib/apt/lists/*

# 4. Ordna för cache
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# 5. Kör som non-root
RUN useradd --create-home appuser
USER appuser

# 6. Lägg till healthcheck
HEALTHCHECK --interval=30s CMD curl -f http://localhost:8000/health

# 7. Använd COPY istället för ADD
COPY app.py /app/

# 8. Sätt labels
LABEL maintainer="team@example.com"
LABEL version="1.0"
```

---

## Image Best Practices

```bash
# 1. Använd slim/alpine varianter
FROM python:3.11-slim   # Istället för python:3.11

# 2. Scanna för vulnerabilities
docker scout cves myimage
trivy image myimage

# 3. Tagga med version och SHA
myimage:1.2.3
myimage:abc123f

# 4. Undvik latest i produktion
# Aldrig: docker pull myimage:latest
# Alltid: docker pull myimage:1.2.3

# 5. Signera images (Docker Content Trust)
export DOCKER_CONTENT_TRUST=1
docker push myimage:1.2.3
```

---

## Container Best Practices

```bash
# 1. Sätt resource limits
docker run --memory=512m --cpus=0.5 myimage

# 2. Använd restart policies
docker run --restart unless-stopped myimage

# 3. Exponera bara nödvändiga portar
docker run -p 127.0.0.1:8080:8080 myimage

# 4. Använd read-only filesystem
docker run --read-only --tmpfs /tmp myimage

# 5. Drop capabilities
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE myimage

# 6. Isolera i nätverk
docker network create --internal backend
```

---

## Docker Compose Best Practices

```yaml
services:
  api:
    image: myapi:${VERSION}  # Använd variabler
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 512M
    healthcheck:
      test: curl -f http://localhost:8000/health
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
    secrets:
      - db_password  # Secrets, inte env vars

secrets:
  db_password:
    external: true
```

---

## Checklista

```bash
# Dockerfile
☐ Specifik base image tag
☐ Multi-stage build
☐ Non-root user
☐ Healthcheck
☐ .dockerignore
☐ Minimala layers

# Security
☐ Image scanning
☐ No secrets i image
☐ Resource limits
☐ Read-only filesystem
☐ Dropped capabilities

# Produktion
☐ Restart policy
☐ Centraliserad logging
☐ Health monitoring
☐ Backup strategy
```

---

## Key Takeaways

- **Optimera för säkerhet** - non-root, minimal image, scanning
- **Optimera för storlek** - multi-stage, slim images
- **Optimera för cache** - ordna Dockerfile smart
- **Följ checklistan** innan deploy till produktion
""",
        },
        {
            "title": "Docker Development Workflow",
            "slug": "docker-development-workflow",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Docker Development Workflow

## Varför behöver du kunna detta?

Docker förändrar hur du utvecklar. Du behöver förstå:

- **Hur du sätter upp lokal utvecklingsmiljö** med Docker
- **Hot reload och debugging** i containers
- **Skillnaden mellan dev och prod** konfiguration

---

## Development vs Production

```yaml
# docker-compose.yml (bas)
services:
  api:
    build: .
    environment:
      - DATABASE_URL=postgresql://db:5432/app

# docker-compose.override.yml (dev - laddas automatiskt)
services:
  api:
    build:
      target: development
    volumes:
      - .:/app           # Hot reload
      - /app/node_modules # Preserve node_modules
    environment:
      - DEBUG=true
    ports:
      - "8000:8000"
      - "9229:9229"      # Debug port

# docker-compose.prod.yml (prod)
services:
  api:
    image: myregistry/api:${VERSION}
    restart: unless-stopped
```

---

## Hot Reload Setup

```dockerfile
# Dockerfile med dev target
FROM node:18-slim AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci

# Development
FROM base AS development
RUN npm install -g nodemon
CMD ["nodemon", "src/index.js"]

# Production
FROM base AS production
COPY . .
RUN npm run build
CMD ["node", "dist/index.js"]
```

---

## Användbart dev-kommando

```bash
# Starta dev environment
docker compose up

# Bygg om efter Dockerfile-ändringar
docker compose up --build

# Kör kommando i container
docker compose exec api npm test
docker compose exec api sh

# Se loggar
docker compose logs -f api

# Starta om en service
docker compose restart api
```

---

## Debugging i Container

```yaml
# docker-compose.override.yml
services:
  api:
    ports:
      - "9229:9229"  # Node.js debug port
    command: ["node", "--inspect=0.0.0.0:9229", "src/index.js"]
```

```json
// VS Code launch.json
{
  "type": "node",
  "request": "attach",
  "name": "Docker: Attach",
  "port": 9229,
  "address": "localhost",
  "localRoot": "${workspaceFolder}",
  "remoteRoot": "/app"
}
```

---

## Database i Development

```yaml
services:
  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=devpassword
      - POSTGRES_DB=app
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql  # Seed data
    ports:
      - "5432:5432"  # Tillgänglig från host för DB-klient

volumes:
  pgdata:
```

---

## Makefile för vanliga tasks

```makefile
# Makefile
.PHONY: dev prod test shell logs

dev:
	docker compose up

prod:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

test:
	docker compose exec api npm test

shell:
	docker compose exec api sh

logs:
	docker compose logs -f

clean:
	docker compose down -v
	docker system prune -f
```

---

## Key Takeaways

- **Override files** för miljöspecifik config
- **Volume mounts** för hot reload
- **Expose debug ports** för VS Code attach
- **Makefile** för vanliga kommandon
""",
        },
        {
            "title": "Docker Ecosystem & Tools",
            "slug": "docker-ecosystem-tools",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 65,
            "content": """# Docker Ecosystem & Tools

## Varför behöver du kunna detta?

Docker är mer än bara Docker Engine. Du behöver känna till:

- **Verktyg som kompletterar Docker**
- **Alternativ och relaterade teknologier**
- **Var Docker passar in i DevOps-landskapet**

---

## Docker Desktop

```bash
# Inkluderar:
# - Docker Engine
# - Docker Compose
# - Docker Scout (security scanning)
# - Kubernetes (single-node)
# - Extensions

# Bra för lokal utveckling på Mac/Windows
# I produktion: använd Docker Engine direkt på Linux
```

---

## Podman (Docker-alternativ)

```bash
# Podman - daemonless, rootless containers
# Kompatibel med Docker CLI

podman run nginx           # Samma syntax som docker
podman build -t myimage .  # Samma Dockerfiles

# Fördelar:
# - Ingen daemon (säkrare)
# - Rootless by default
# - Kompatibel med Docker
```

---

## Image Scanning Tools

```bash
# Docker Scout (inbyggt)
docker scout cves myimage
docker scout recommendations myimage

# Trivy (open source)
trivy image myimage

# Snyk
snyk container test myimage

# Grype
grype myimage
```

---

## Container Registries

```bash
# Public
# - Docker Hub (docker.io)
# - GitHub Container Registry (ghcr.io)
# - Quay.io

# Cloud-managed
# - AWS ECR
# - Google Artifact Registry
# - Azure Container Registry

# Self-hosted
# - Harbor
# - GitLab Container Registry
# - Nexus
```

---

## Image Analysis Tools

```bash
# Dive - analysera layers
dive myimage

# Docker History
docker history myimage

# Skopeo - kopiera mellan registries
skopeo copy docker://docker.io/nginx docker://myregistry/nginx
```

---

## Build Tools

```bash
# BuildKit (standard i nya Docker)
DOCKER_BUILDKIT=1 docker build .

# Buildx (multi-platform)
docker buildx build --platform linux/amd64,linux/arm64 .

# Kaniko (build i Kubernetes utan Docker daemon)
# Används i CI/CD pipelines

# Buildah (OCI image builder)
buildah build-using-dockerfile -t myimage .
```

---

## Orchestration

```bash
# Docker Swarm - inbyggt i Docker
docker swarm init

# Kubernetes - standard för produktion
kubectl apply -f deployment.yaml

# Nomad - HashiCorp alternativ
nomad job run myapp.nomad

# ECS - AWS managed containers
aws ecs create-service ...
```

---

## Monitoring & Logging

```bash
# Prometheus + Grafana
# - Metrics collection och visualization

# ELK Stack (Elasticsearch, Logstash, Kibana)
# - Centraliserad logging

# Datadog, New Relic
# - Managed monitoring

# cAdvisor
# - Container resource monitoring
```

---

## Key Takeaways

- **Docker Scout/Trivy** för security scanning
- **Buildx** för multi-platform builds
- **Kubernetes** är standard för större deployments
- **Harbor** för self-hosted registry
""",
        },
        {
            "title": "Docker Certification Path",
            "slug": "docker-certification-path",
            "difficulty": "easy",
            "estimated_minutes": 30,
            "xp_reward": 60,
            "content": """# Docker Certification Path

## Varför behöver du kunna detta?

Docker-certifieringar validerar dina kunskaper. Du behöver veta:

- **Vilka certifieringar som finns**
- **Vad de täcker**
- **Hur du förbereder dig**

---

## Docker Certified Associate (DCA)

```bash
# Den primära Docker-certifieringen
# Täcker:

# 1. Orchestration (25%)
# - Swarm setup och management
# - Services och stacks
# - Networking i Swarm

# 2. Image Creation & Management (20%)
# - Dockerfile best practices
# - Multi-stage builds
# - Registry operations

# 3. Installation & Configuration (15%)
# - Docker Engine installation
# - Storage drivers
# - Logging drivers

# 4. Networking (15%)
# - Network drivers
# - DNS och service discovery
# - Load balancing

# 5. Security (15%)
# - Image security
# - Secrets management
# - Content trust

# 6. Storage & Volumes (10%)
# - Volume types
# - Backup strategies
```

---

## Förberedelse

```bash
# 1. Hands-on erfarenhet (viktigast!)
# - Bygg egna images
# - Sätt upp multi-container apps
# - Deploya till Swarm

# 2. Officiell dokumentation
# docs.docker.com

# 3. Practice exams
# - Whizlabs
# - Practice tests online

# 4. Labs
# - Play with Docker (labs.play-with-docker.com)
# - Katacoda scenarios
```

---

## Relaterade Certifieringar

```bash
# Kubernetes certifieringar (nästa steg)
# - CKA (Certified Kubernetes Administrator)
# - CKAD (Certified Kubernetes Application Developer)
# - CKS (Certified Kubernetes Security Specialist)

# Cloud certifieringar med container-fokus
# - AWS Certified DevOps Engineer
# - Azure DevOps Engineer Expert
# - Google Professional Cloud DevOps Engineer
```

---

## Study Checklist

```bash
☐ Dockerfile syntax och best practices
☐ Docker Compose för multi-container apps
☐ Docker networking (bridge, host, overlay)
☐ Docker volumes och storage
☐ Docker Swarm basics
☐ Image security och scanning
☐ Registry operations
☐ Logging och monitoring
☐ Troubleshooting containers
```

---

## Key Takeaways

- **DCA** är bra första certifiering
- **Hands-on experience** är viktigast
- **Kubernetes-cert** är naturligt nästa steg
- Öva med **Play with Docker** labs
""",
        },
    ],
}
