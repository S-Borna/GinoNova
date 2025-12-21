# =============================================================================
# DOCKER MASTERY V3 - BLOCK 2 PART 1: VOLUMES & NETWORKING
# Noder 5-6 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
DOCKER BLOCK 2 PART 1 - DATA & NETWORK
======================================
Node 5: Docker Volumes - Persistent Data
Node 6: Docker Networking - Container Communication
"""

NODE_5 = {
    "id": "docker_node_5",
    "title": "Docker Volumes - Persistent Data",
    "slug": "docker-volumes-persistent-data",
    "content": r'''# 💾 Docker Volumes - Persistent Data

## 1. Introduktion & Kontext

Containers är ephemeral - när de tas bort försvinner all data. Docker Volumes löser detta genom att erbjuda persistent storage som överlever container lifecycle.

### Storage Types Overview

```
+-------------------------------------------------------------------------+
|                    DOCKER STORAGE TYPES                                  |
+-------------------------------------------------------------------------+
|                                                                          |
|  HOST                              DOCKER                                |
|  ════                              ══════                                |
|                                                                          |
|  +-------------+                   +-----------------------------+     |
|  | /host/path  |◄------------------|     BIND MOUNT              |     |
|  |  (file)     |   Host path       |     Direct mapping          |     |
|  +-------------+   mounted         |     Development use         |     |
|                                    +-----------------------------+     |
|                                                                          |
|  +-------------+                   +-----------------------------+     |
|  | /var/lib/   |◄------------------|     NAMED VOLUME            |     |
|  | docker/     |   Docker          |     Docker-managed          |     |
|  | volumes/    |   managed         |     Production use          |     |
|  +-------------+                   +-----------------------------+     |
|                                                                          |
|                                    +-----------------------------+     |
|                                    |     TMPFS MOUNT             |     |
|                                    |     Memory only             |     |
|                                    |     Sensitive data          |     |
|                                    +-----------------------------+     |
|                                                                          |
|  COMPARISON:                                                             |
|  ---------------------------------------------------------------------  |
|  Type          | Managed | Portable | Performance | Use Case           |
|  Bind Mount    | No      | No       | Native      | Development        |
|  Named Volume  | Yes     | Yes      | Native      | Production         |
|  tmpfs         | Yes     | No       | Fast (RAM)  | Secrets, temp      |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Named Volumes

```bash
# ═══════════════════════════════════════════════════════════════════════
# CREATE VOLUMES
# ═══════════════════════════════════════════════════════════════════════

# Skapa named volume
docker volume create mydata
docker volume create --name postgres-data

# Med labels
docker volume create \
  --label environment=production \
  --label app=database \
  prod-db-data

# ═══════════════════════════════════════════════════════════════════════
# LIST & INSPECT
# ═══════════════════════════════════════════════════════════════════════

docker volume ls
docker volume ls --filter label=environment=production
docker volume inspect mydata

# Inspect output:
# [
#     {
#         "CreatedAt": "2024-01-15T10:00:00Z",
#         "Driver": "local",
#         "Labels": {},
#         "Mountpoint": "/var/lib/docker/volumes/mydata/_data",
#         "Name": "mydata",
#         "Options": {},
#         "Scope": "local"
#     }
# ]

# ═══════════════════════════════════════════════════════════════════════
# USE VOLUMES
# ═══════════════════════════════════════════════════════════════════════

# Mount volume till container
docker run -d \
  --name postgres \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:15

# Alternativ syntax (--mount)
docker run -d \
  --name postgres \
  --mount type=volume,source=postgres-data,target=/var/lib/postgresql/data \
  postgres:15

# ═══════════════════════════════════════════════════════════════════════
# REMOVE VOLUMES
# ═══════════════════════════════════════════════════════════════════════

docker volume rm mydata
docker volume rm $(docker volume ls -q)     # Ta bort alla
docker volume prune                          # Ta bort oanvända
docker volume prune -f                       # Utan bekräftelse
```

## 3. Bind Mounts

```bash
# ═══════════════════════════════════════════════════════════════════════
# BIND MOUNT - Host path mapping
# ═══════════════════════════════════════════════════════════════════════

# -v syntax
docker run -d \
  --name web \
  -v $(pwd)/src:/app/src \
  -p 3000:3000 \
  node:20

# --mount syntax (mer explicit)
docker run -d \
  --name web \
  --mount type=bind,source=$(pwd)/src,target=/app/src \
  -p 3000:3000 \
  node:20

# ═══════════════════════════════════════════════════════════════════════
# READ-ONLY BIND MOUNT
# ═══════════════════════════════════════════════════════════════════════

docker run -d \
  --name web \
  -v $(pwd)/config:/app/config:ro \
  nginx

docker run -d \
  --name web \
  --mount type=bind,source=$(pwd)/config,target=/app/config,readonly \
  nginx

# ═══════════════════════════════════════════════════════════════════════
# DEVELOPMENT SETUP
# ═══════════════════════════════════════════════════════════════════════

# Full development mount med hot-reload
docker run -d \
  --name dev-server \
  -v $(pwd):/app \
  -v /app/node_modules \
  -p 3000:3000 \
  node:20 npm run dev

# Förklaring:
# -v $(pwd):/app        -> Mappa hela projektet
# -v /app/node_modules  -> Anonymous volume för node_modules
#                         (förhindrar att host's node_modules överskrivs)
```

## 4. tmpfs Mounts

```bash
# ═══════════════════════════════════════════════════════════════════════
# TMPFS - In-memory storage
# ═══════════════════════════════════════════════════════════════════════

# Basic tmpfs
docker run -d \
  --name secure-app \
  --tmpfs /tmp \
  myapp

# Med storlek och permissions
docker run -d \
  --name secure-app \
  --mount type=tmpfs,target=/secrets,tmpfs-size=100m,tmpfs-mode=0700 \
  myapp

# Use cases:
# - Temporära filer
# - Secrets som inte ska skrivas till disk
# - Cache data
# - Session data
```

## 5. Volume Drivers & Plugins

```
+-------------------------------------------------------------------------+
|                    VOLUME DRIVERS                                        |
+-------------------------------------------------------------------------+
|                                                                          |
|  DRIVER          | USE CASE                                              |
|  ---------------------------------------------------------------------  |
|  local           | Default, lokal disk                                  |
|  nfs             | Network File System                                  |
|  ceph            | Distributed storage                                  |
|  aws-ebs         | Amazon EBS volumes                                   |
|  azure-file      | Azure File Storage                                   |
|  gcs             | Google Cloud Storage                                 |
|                                                                          |
|  EXEMPEL NFS:                                                           |
|  ---------------------------------------------------------------------  |
|                                                                          |
|  docker volume create \                                                  |
|    --driver local \                                                     |
|    --opt type=nfs \                                                     |
|    --opt o=addr=192.168.1.10,rw \                                      |
|    --opt device=:/export/data \                                        |
|    nfs-data                                                             |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 6. Backup & Restore

```bash
# ═══════════════════════════════════════════════════════════════════════
# BACKUP VOLUME
# ═══════════════════════════════════════════════════════════════════════

# Metod 1: Temporary container
docker run --rm \
  -v postgres-data:/source:ro \
  -v $(pwd)/backups:/backup \
  alpine tar czf /backup/postgres-backup.tar.gz -C /source .

# Metod 2: docker cp från stoppad container
docker stop postgres
docker cp postgres:/var/lib/postgresql/data ./backup/
docker start postgres

# ═══════════════════════════════════════════════════════════════════════
# RESTORE VOLUME
# ═══════════════════════════════════════════════════════════════════════

# Skapa ny volume
docker volume create postgres-restored

# Återställ data
docker run --rm \
  -v postgres-restored:/target \
  -v $(pwd)/backups:/backup:ro \
  alpine sh -c "cd /target && tar xzf /backup/postgres-backup.tar.gz"

# ═══════════════════════════════════════════════════════════════════════
# AUTOMATED BACKUP SCRIPT
# ═══════════════════════════════════════════════════════════════════════

#!/bin/bash
# backup-volume.sh

VOLUME_NAME=$1
BACKUP_DIR=/backups
DATE=$(date +%Y%m%d_%H%M%S)

docker run --rm \
  -v ${VOLUME_NAME}:/source:ro \
  -v ${BACKUP_DIR}:/backup \
  alpine tar czf /backup/${VOLUME_NAME}_${DATE}.tar.gz -C /source .

# Behåll endast senaste 7 dagars backups
find ${BACKUP_DIR} -name "${VOLUME_NAME}_*.tar.gz" -mtime +7 -delete

echo "Backup complete: ${VOLUME_NAME}_${DATE}.tar.gz"
```

## 7. Practical Database Example

```bash
# ═══════════════════════════════════════════════════════════════════════
# POSTGRESQL WITH PERSISTENT STORAGE
# ═══════════════════════════════════════════════════════════════════════

# Skapa volume
docker volume create postgres-data

# Starta database
docker run -d \
  --name postgres \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secretpassword \
  -e POSTGRES_DB=myapp \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15

# Verifiera
docker exec postgres pg_isready

# Skapa testdata
docker exec -it postgres psql -U admin -d myapp -c "
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);
INSERT INTO users (name) VALUES ('Test User');
"

# Stoppa och ta bort container
docker stop postgres && docker rm postgres

# Starta ny container med samma volume
docker run -d \
  --name postgres-new \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secretpassword \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15

# Verifiera att data finns kvar
docker exec -it postgres-new psql -U admin -d myapp -c "SELECT * FROM users;"
# -> Visar 'Test User' - data persistent!
```

## 8. Praktiska Övningar

### Övning 1: Volume Basics

```bash
# Skapa och använd volume
docker volume create test-data

# Skriv data
docker run --rm \
  -v test-data:/data \
  alpine sh -c "echo 'Hello Volumes!' > /data/test.txt"

# Läs data från annan container
docker run --rm \
  -v test-data:/data:ro \
  alpine cat /data/test.txt

# Cleanup
docker volume rm test-data
```

### Övning 2: Development Mount

```bash
# Skapa projekt
mkdir volume-demo && cd volume-demo
echo 'console.log("Hello!")' > app.js

# Kör med bind mount
docker run --rm \
  -v $(pwd):/app \
  -w /app \
  node:20 node app.js

# Ändra fil och kör igen
echo 'console.log("Updated!")' > app.js
docker run --rm \
  -v $(pwd):/app \
  -w /app \
  node:20 node app.js
```

## 9-14. Sammanfattning

### Volume Commands Reference

| Command | Description |
|---------|-------------|
| `docker volume create` | Skapa volume |
| `docker volume ls` | Lista volumes |
| `docker volume inspect` | Detaljer |
| `docker volume rm` | Ta bort |
| `docker volume prune` | Cleanup |

### Mount Syntax Comparison

| Feature | -v syntax | --mount syntax |
|---------|-----------|----------------|
| Readability | Compact | Explicit |
| Error handling | Silently creates | Errors if missing |
| Recommended | Quick use | Production |

---

**Nästa Node:** Docker Networking ->
''',
    "xp_reward": 165,
    "estimated_minutes": 70,
    "prerequisites": ["docker_node_4"],
    "learning_outcomes": [
        "Förstå Docker storage types",
        "Använda Named Volumes",
        "Konfigurera Bind Mounts",
        "Backup och restore data"
    ]
}

NODE_6 = {
    "id": "docker_node_6",
    "title": "Docker Networking - Container Communication",
    "slug": "docker-networking-container-communication",
    "content": r'''# 🌐 Docker Networking - Container Communication

## 1. Introduktion & Kontext

Docker networking möjliggör kommunikation mellan containers, med host, och med omvärlden. Förståelse av network types och DNS är essentiellt för multi-container applications.

### Network Architecture

```
+-------------------------------------------------------------------------+
|                    DOCKER NETWORK ARCHITECTURE                           |
+-------------------------------------------------------------------------+
|                                                                          |
|    EXTERNAL                        HOST                                  |
|    ════════                        ════                                  |
|                                                                          |
|    Internet ◄-------------------► eth0: 192.168.1.10                    |
|                                     |                                    |
|                                     | NAT                                |
|                                     |                                    |
|    +--------------------------------+--------------------------------+  |
|    |                      docker0: 172.17.0.1                         |  |
|    |                      (DEFAULT BRIDGE)                            |  |
|    |                                                                  |  |
|    |   +-----------------+    +-----------------+                   |  |
|    |   |   Container A   |    |   Container B   |                   |  |
|    |   |   172.17.0.2    |◄--►|   172.17.0.3    |                   |  |
|    |   +-----------------+    +-----------------+                   |  |
|    |                                                                  |  |
|    +------------------------------------------------------------------+  |
|                                                                          |
|    +------------------------------------------------------------------+  |
|    |                    app-network: 172.18.0.0/16                    |  |
|    |                    (USER-DEFINED BRIDGE)                         |  |
|    |                                                                  |  |
|    |   +-----------------+    +-----------------+                   |  |
|    |   |   web: 172.18.0.2|◄--►|   db: 172.18.0.3|                   |  |
|    |   |   DNS: "web"     |    |   DNS: "db"     |                   |  |
|    |   +-----------------+    +-----------------+                   |  |
|    |                                                                  |  |
|    |   Container "web" kan nå "db" via hostname!                     |  |
|    |   curl http://db:5432 ✓                                         |  |
|    |                                                                  |  |
|    +------------------------------------------------------------------+  |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Network Types

```
+-------------------------------------------------------------------------+
|                      DOCKER NETWORK DRIVERS                              |
+-------------------------------------------------------------------------+
|                                                                          |
|  DRIVER        | ISOLATION | DNS  | USE CASE                            |
|  ---------------------------------------------------------------------  |
|  bridge        | Yes       | No*  | Default, single host               |
|  user bridge   | Yes       | Yes  | Production, multi-container        |
|  host          | No        | N/A  | Performance, direct network        |
|  none          | Total     | No   | Security, custom networking        |
|  overlay       | Yes       | Yes  | Multi-host (Swarm/K8s)             |
|  macvlan       | Yes       | No   | Legacy apps, direct MAC            |
|  ipvlan        | Yes       | No   | L2/L3 network integration          |
|                                                                          |
|  * Default bridge har DNS men endast via --link (deprecated)            |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 3. Network Commands

```bash
# ═══════════════════════════════════════════════════════════════════════
# LIST NETWORKS
# ═══════════════════════════════════════════════════════════════════════

docker network ls

# Default output:
# NETWORK ID     NAME      DRIVER    SCOPE
# abc123456789   bridge    bridge    local
# def987654321   host      host      local
# ghi456789012   none      null      local

# ═══════════════════════════════════════════════════════════════════════
# CREATE NETWORK
# ═══════════════════════════════════════════════════════════════════════

# Basic bridge network
docker network create app-network

# Med specifik subnet
docker network create \
  --driver bridge \
  --subnet 172.20.0.0/16 \
  --gateway 172.20.0.1 \
  custom-network

# Med labels
docker network create \
  --label environment=production \
  prod-network

# ═══════════════════════════════════════════════════════════════════════
# INSPECT NETWORK
# ═══════════════════════════════════════════════════════════════════════

docker network inspect app-network
docker network inspect bridge --format '{{json .Containers}}'

# ═══════════════════════════════════════════════════════════════════════
# CONNECT / DISCONNECT
# ═══════════════════════════════════════════════════════════════════════

# Connect running container to network
docker network connect app-network mycontainer
docker network connect --ip 172.20.0.100 custom-network mycontainer

# Disconnect
docker network disconnect app-network mycontainer

# ═══════════════════════════════════════════════════════════════════════
# REMOVE NETWORK
# ═══════════════════════════════════════════════════════════════════════

docker network rm app-network
docker network prune                 # Ta bort oanvända
```

## 4. Container Networking

```bash
# ═══════════════════════════════════════════════════════════════════════
# RUN WITH NETWORK
# ═══════════════════════════════════════════════════════════════════════

# Default bridge
docker run -d --name web nginx

# Specifik network
docker run -d --name web --network app-network nginx

# Host network (ingen isolering)
docker run -d --name web --network host nginx

# No network
docker run -d --name isolated --network none alpine sleep infinity

# ═══════════════════════════════════════════════════════════════════════
# PORT MAPPING
# ═══════════════════════════════════════════════════════════════════════

# Basic port mapping
docker run -d -p 8080:80 nginx         # host:container

# Bind to specific interface
docker run -d -p 127.0.0.1:8080:80 nginx

# Random host port
docker run -d -p 80 nginx              # Docker väljer port
docker run -d -P nginx                 # Alla EXPOSE ports

# UDP port
docker run -d -p 5353:53/udp dns-server

# Multiple ports
docker run -d \
  -p 80:80 \
  -p 443:443 \
  -p 8080:8080 \
  myapp

# Se mappade portar
docker port mycontainer
```

## 5. DNS & Service Discovery

```
+-------------------------------------------------------------------------+
|                    DOCKER DNS RESOLUTION                                 |
+-------------------------------------------------------------------------+
|                                                                          |
|  USER-DEFINED BRIDGE NETWORK:                                           |
|  ═══════════════════════════════════════════════════════════════════   |
|                                                                          |
|  docker network create app-net                                          |
|  docker run -d --name api --network app-net myapi                       |
|  docker run -d --name db --network app-net postgres                     |
|                                                                          |
|  +-----------------------------------------------------------------+   |
|  |                    app-net (172.20.0.0/16)                       |   |
|  |                                                                   |   |
|  |   +--------------+           +--------------+                   |   |
|  |   |     api      |---DNS----►|      db      |                   |   |
|  |   | 172.20.0.2   |           | 172.20.0.3   |                   |   |
|  |   +--------------+           +--------------+                   |   |
|  |                                                                   |   |
|  |   # Från api container:                                          |   |
|  |   ping db          ✓  -> 172.20.0.3                              |   |
|  |   curl http://db   ✓                                            |   |
|  |   psql -h db       ✓                                            |   |
|  |                                                                   |   |
|  +-----------------------------------------------------------------+   |
|                                                                          |
|  CONTAINER ALIASES:                                                      |
|  ═══════════════════════════════════════════════════════════════════   |
|                                                                          |
|  docker run -d \                                                        |
|    --name postgres \                                                    |
|    --network app-net \                                                  |
|    --network-alias db \                                                 |
|    --network-alias database \                                           |
|    postgres:15                                                          |
|                                                                          |
|  # Nu nåbar via: postgres, db, database                                 |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 6. Multi-Container Example

```bash
# ═══════════════════════════════════════════════════════════════════════
# MULTI-CONTAINER APPLICATION
# ═══════════════════════════════════════════════════════════════════════

# Skapa nätverk
docker network create webstack

# Database
docker run -d \
  --name db \
  --network webstack \
  -e POSTGRES_PASSWORD=secret \
  -v db-data:/var/lib/postgresql/data \
  postgres:15

# Redis cache
docker run -d \
  --name redis \
  --network webstack \
  redis:7-alpine

# Backend API
docker run -d \
  --name api \
  --network webstack \
  -e DATABASE_URL=postgresql://postgres:secret@db:5432/postgres \
  -e REDIS_URL=redis://redis:6379 \
  -p 8000:8000 \
  myapi

# Frontend
docker run -d \
  --name frontend \
  --network webstack \
  -e API_URL=http://api:8000 \
  -p 3000:3000 \
  myfrontend

# Verifiera kommunikation
docker exec api ping -c 2 db
docker exec api ping -c 2 redis
docker exec frontend curl -s http://api:8000/health
```

## 7. Host Network Mode

```bash
# ═══════════════════════════════════════════════════════════════════════
# HOST NETWORK - Ingen isolering
# ═══════════════════════════════════════════════════════════════════════

# Container använder host's network stack direkt
docker run -d --network host nginx

# Fördelar:
# - Bästa performance (ingen NAT overhead)
# - Container bindar direkt till host ports

# Nackdelar:
# - Ingen port isolation
# - Kan inte köra flera containers på samma port
# - Fungerar endast på Linux

# Use case: High-performance applications
docker run -d \
  --name prometheus \
  --network host \
  prom/prometheus
```

## 8. Praktiska Övningar

### Övning 1: Network Basics

```bash
# Skapa nätverk
docker network create test-net

# Starta två containers
docker run -d --name server1 --network test-net alpine sleep infinity
docker run -d --name server2 --network test-net alpine sleep infinity

# Testa DNS
docker exec server1 ping -c 2 server2
docker exec server2 ping -c 2 server1

# Cleanup
docker stop server1 server2
docker rm server1 server2
docker network rm test-net
```

### Övning 2: Multi-network Setup

```bash
# Frontend network
docker network create frontend-net

# Backend network
docker network create backend-net

# API container på båda nätverk
docker run -d --name api --network backend-net alpine sleep infinity
docker network connect frontend-net api

# Frontend (endast frontend-net)
docker run -d --name web --network frontend-net alpine sleep infinity

# Database (endast backend-net)
docker run -d --name db --network backend-net alpine sleep infinity

# Verifiera
docker exec web ping -c 1 api      # ✓
docker exec web ping -c 1 db       # ✗ (olika nätverk)
docker exec api ping -c 1 db       # ✓
docker exec api ping -c 1 web      # ✓

# Cleanup
docker stop web api db
docker rm web api db
docker network rm frontend-net backend-net
```

## 9-14. Sammanfattning

### Network Commands Reference

| Command | Description |
|---------|-------------|
| `docker network ls` | Lista nätverk |
| `docker network create` | Skapa nätverk |
| `docker network connect` | Anslut container |
| `docker network disconnect` | Koppla från |
| `docker network rm` | Ta bort |

---

**Nästa Node:** Docker Compose Basics ->
''',
    "xp_reward": 170,
    "estimated_minutes": 75,
    "prerequisites": ["docker_node_5"],
    "learning_outcomes": [
        "Förstå Docker networking",
        "Konfigurera network types",
        "Använda DNS discovery",
        "Bygga multi-container apps"
    ]
}

# Block 2 Part 1 exports
BLOCK_2_PART_1_NODES = [NODE_5, NODE_6]
