# =============================================================================
# DOCKER NETWORKING — Noder 9-12
# Premium Bootcamp-Quality Content
# =============================================================================

NODE_09_NETWORKING_BASICS = {
    "id": "docker-networking-basics",
    "node_id": 9,
    "title": "Docker Networking Fundamentals",
    "slug": "docker-networking-basics",
    "description": "Förstå hur Docker-nätverk fungerar och de olika nätverkstyperna",
    "type": "concept",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [8],
    "content": '''# 🌐 Docker Networking Fundamentals

## Lärande mål
- Förstå Docker nätverksarkitektur
- Kunna använda alla nätverkstyper
- Konfigurera container-kommunikation
- Implementera DNS för service discovery

---

## 📖 Nätverksarkitektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOCKER NETWORK ARCHITECTURE                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   HOST                                                          │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                                                          │  │
│   │   ┌─────────┐    ┌─────────┐    ┌─────────┐            │  │
│   │   │   C1    │    │   C2    │    │   C3    │            │  │
│   │   │ web     │    │  api    │    │   db    │            │  │
│   │   │ :80     │    │ :3000   │    │ :5432   │            │  │
│   │   └────┬────┘    └────┬────┘    └────┬────┘            │  │
│   │        │              │              │                  │  │
│   │   ┌────┴──────────────┴──────────────┴────┐            │  │
│   │   │         DOCKER NETWORK (bridge)       │            │  │
│   │   │         172.17.0.0/16                 │            │  │
│   │   └──────────────────┬────────────────────┘            │  │
│   │                      │                                  │  │
│   │   ┌──────────────────┴────────────────────┐            │  │
│   │   │           docker0 bridge              │            │  │
│   │   │           172.17.0.1                  │            │  │
│   │   └──────────────────┬────────────────────┘            │  │
│   │                      │                                  │  │
│   └──────────────────────┼──────────────────────────────────┘  │
│                          │                                      │
│   ┌──────────────────────┴────────────────────────┐            │
│   │              HOST NETWORK (eth0)              │            │
│   │              192.168.1.100                    │            │
│   └───────────────────────────────────────────────┘            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Nätverkstyper

### 1. Bridge (default)

```bash
# Isolerat nätverk för containers
docker run -d --name web nginx
docker inspect web | grep IPAddress
# "IPAddress": "172.17.0.2"

# Containers på samma bridge kan kommunicera via IP
docker run -it alpine ping 172.17.0.2
```

### 2. Host

```bash
# Container delar host-nätverk (ingen isolering)
docker run -d --network host nginx
# nginx är nu på localhost:80 direkt

# Användning: Max prestanda, men ingen port-mappning
```

### 3. None

```bash
# Ingen nätverksanslutning
docker run -d --network none alpine sleep 1000

# Användning: Säkerhetskänsliga workloads
```

### 4. Custom Bridge (rekommenderat)

```bash
# Skapa eget nätverk
docker network create mynetwork

# Starta containers på nätverket
docker run -d --name web --network mynetwork nginx
docker run -d --name api --network mynetwork node:20

# DNS fungerar automatiskt!
docker exec api ping web  # ✅ Fungerar!
```

---

## 📡 DNS & Service Discovery

### Automatisk DNS på custom networks

```bash
# Skapa nätverk
docker network create backend

# Starta containers
docker run -d --name postgres --network backend postgres:15
docker run -d --name redis --network backend redis:7
docker run -d --name api --network backend myapi:1.0

# I api kan du nu ansluta till:
# postgres:5432 (inte IP!)
# redis:6379
```

```python
# I din app
import psycopg2
conn = psycopg2.connect(
    host="postgres",  # Container-namn = hostname!
    port=5432,
    user="postgres"
)
```

### Network aliases

```bash
# Flera namn för samma container
docker run -d --name db \\
    --network backend \\
    --network-alias postgres \\
    --network-alias database \\
    postgres:15

# Nu fungerar både:
# postgres:5432
# database:5432
# db:5432
```

---

## 🔌 Port Exposure

### Port mapping

```bash
# -p HOST:CONTAINER
docker run -d -p 8080:80 nginx
# localhost:8080 → container:80

# Endast localhost
docker run -d -p 127.0.0.1:8080:80 nginx

# Slumpmässig host-port
docker run -d -p 80 nginx
docker port <container>  # Se vilken port

# UDP
docker run -d -p 53:53/udp dns-server
```

### EXPOSE i Dockerfile

```dockerfile
# Dokumentation (gör inget själv)
EXPOSE 8080

# Vid körning måste du fortfarande:
docker run -p 8080:8080 myapp
```

---

## 🛠️ Nätverkskommandon

```bash
# Lista nätverk
docker network ls

# Inspektera
docker network inspect bridge

# Skapa
docker network create --driver bridge mynetwork
docker network create --subnet 10.0.0.0/24 mynetwork

# Anslut container till nätverk
docker network connect mynetwork mycontainer

# Koppla bort
docker network disconnect mynetwork mycontainer

# Ta bort
docker network rm mynetwork

# Städa oanvända
docker network prune
```

---

## 🏋️ Övningar

### Övning: Multi-container kommunikation
```bash
# 1. Skapa nätverk
docker network create webapp

# 2. Starta database
docker run -d --name db --network webapp \\
    -e POSTGRES_PASSWORD=secret postgres:15

# 3. Testa DNS
docker run --rm --network webapp alpine ping -c 3 db

# 4. Städa
docker stop db && docker rm db
docker network rm webapp
```

---

**Nästa steg:** Node 10 - Advanced Networking
''',
}


NODE_10_ADVANCED_NETWORKING = {
    "id": "docker-advanced-networking",
    "node_id": 10,
    "title": "Advanced Docker Networking",
    "slug": "docker-advanced-networking",
    "description": "Avancerade nätverkskonfigurationer och felsökning",
    "type": "practice",
    "difficulty": "hard",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [9],
    "content": '''# 🔧 Advanced Docker Networking

## Lärande mål
- Konfigurera custom subnets
- Implementera overlay networks
- Felsöka nätverksproblem
- Förstå iptables och NAT

---

## 🌐 Custom Network Configuration

### Subnet och Gateway

```bash
# Skapa nätverk med specifik subnet
docker network create \\
    --driver bridge \\
    --subnet 10.10.0.0/16 \\
    --gateway 10.10.0.1 \\
    --ip-range 10.10.1.0/24 \\
    production

# Tilldela statisk IP
docker run -d --name db \\
    --network production \\
    --ip 10.10.1.100 \\
    postgres:15
```

### Multi-network containers

```bash
# Container på flera nätverk
docker network create frontend
docker network create backend

docker run -d --name api myapi:1.0

docker network connect frontend api
docker network connect backend api

# api kan nu nå containers på båda nätverken
```

---

## 🔍 Felsökning

### Network debugging

```bash
# Se container-nätverk
docker inspect --format='{{.NetworkSettings.Networks}}' mycontainer

# Se alla anslutna containers
docker network inspect mynetwork

# Debugging container
docker run -it --network mynetwork nicolaka/netshoot

# I netshoot:
ping api
nslookup api
curl http://api:3000
tcpdump -i any port 80
```

### Vanliga problem

```bash
# Problem: Containers kan inte nå varandra
# Lösning: Se till att de är på samma custom network

# Problem: Port already in use
lsof -i :8080
docker ps | grep 8080

# Problem: DNS fungerar inte
# Lösning: Använd custom network (inte default bridge)
```

---

## 🔒 Network Security

### Internal networks

```bash
# Nätverk utan extern åtkomst
docker network create --internal secure-backend

# Containers kan kommunicera internt
# Men inte nå internet
```

### Isolerade nätverk

```bash
# Frontend-nätverk (kan nå internet)
docker network create frontend

# Backend-nätverk (isolerat)
docker network create --internal backend

# API på båda (gateway)
docker run -d --name api myapi
docker network connect frontend api
docker network connect backend api
```

---

**Nästa steg:** Node 11 - Docker Port Management
''',
}


NODE_11_PORT_MANAGEMENT = {
    "id": "docker-port-management",
    "node_id": 11,
    "title": "Port Management & Load Balancing",
    "slug": "docker-port-management",
    "description": "Hantera portar och sätt upp enkel load balancing",
    "type": "practice",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "prerequisites": [10],
    "content": '''# 🔌 Port Management & Load Balancing

## Lärande mål
- Hantera port-mappningar effektivt
- Sätta upp reverse proxy
- Konfigurera enkel load balancing

---

## 🔧 Port Mapping Patterns

### Dynamisk vs Statisk

```bash
# Statisk (förutsägbar)
docker run -d -p 8080:80 nginx
# Alltid på localhost:8080

# Dynamisk (Docker väljer)
docker run -d -p 80 nginx
docker port <container>
# 80/tcp -> 0.0.0.0:49153
```

### Flera portar

```bash
# HTTP och HTTPS
docker run -d \\
    -p 80:80 \\
    -p 443:443 \\
    nginx

# Port range
docker run -d -p 8080-8090:8080-8090 myapp
```

---

## 🔄 Nginx Reverse Proxy

```bash
# Skapa nätverk
docker network create webapps

# Starta applikationer
docker run -d --name app1 --network webapps myapp:1.0
docker run -d --name app2 --network webapps myapp:2.0

# nginx.conf
cat > nginx.conf << 'EOF'
upstream apps {
    server app1:3000;
    server app2:3000;
}

server {
    listen 80;
    location / {
        proxy_pass http://apps;
    }
}
EOF

# Starta nginx
docker run -d --name proxy \\
    --network webapps \\
    -p 80:80 \\
    -v $(pwd)/nginx.conf:/etc/nginx/conf.d/default.conf \\
    nginx
```

---

## ⚖️ Enkel Load Balancing

### Round-robin med DNS

```bash
# Flera containers med samma alias
docker run -d --network webapps --network-alias api myapi
docker run -d --network webapps --network-alias api myapi
docker run -d --network webapps --network-alias api myapi

# DNS returnerar olika IPs round-robin
docker run --rm --network webapps alpine nslookup api
```

---

**Nästa steg:** Node 12 - Container-to-Container Communication
''',
}


NODE_12_CONTAINER_COMMUNICATION = {
    "id": "container-communication",
    "node_id": 12,
    "title": "Container-to-Container Communication",
    "slug": "container-communication",
    "description": "Best practices för kommunikation mellan containers",
    "type": "deep_dive",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [11],
    "content": '''# 🔗 Container-to-Container Communication

## Lärande mål
- Designa multi-container arkitekturer
- Implementera service mesh patterns
- Hantera secrets mellan containers
- Optimera för prestanda

---

## 🏗️ Arkitektur Patterns

### Sidecar Pattern

```
┌─────────────────────────────────────────┐
│              POD (Compose service)       │
│  ┌───────────────┐  ┌───────────────┐   │
│  │  Main App     │  │  Sidecar      │   │
│  │  (api)        │──│  (logging)    │   │
│  └───────────────┘  └───────────────┘   │
└─────────────────────────────────────────┘
```

```yaml
# docker-compose.yml
services:
  api:
    image: myapi:1.0
    network_mode: "service:logging"

  logging:
    image: fluent/fluentd
```

### Ambassador Pattern

```yaml
services:
  api:
    image: myapi:1.0

  ambassador:
    image: nginx
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - "80:80"
```

---

## 🔒 Secrets Sharing

### Docker Secrets (Swarm)

```bash
# Skapa secret
echo "supersecret" | docker secret create db_password -

# Använd i service
docker service create \\
    --secret db_password \\
    --env DB_PASSWORD_FILE=/run/secrets/db_password \\
    myapi
```

### Environment files

```bash
# .env
DB_HOST=postgres
DB_PASSWORD=secret

# docker run
docker run --env-file .env myapi
```

---

## 📡 Communication Patterns

### Sync (HTTP/gRPC)

```python
# Service A → Service B
import requests
response = requests.get("http://service-b:3000/api/data")
```

### Async (Message Queue)

```yaml
services:
  api:
    image: myapi

  worker:
    image: myworker

  redis:
    image: redis:7
```

---

**Nästa steg:** Node 13 - Docker Compose Fundamentals
''',
}


NODES = [
    NODE_09_NETWORKING_BASICS,
    NODE_10_ADVANCED_NETWORKING,
    NODE_11_PORT_MANAGEMENT,
    NODE_12_CONTAINER_COMMUNICATION,
]
