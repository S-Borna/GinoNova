"""
NOD 3.3: Docker Compose
=======================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 3: DEVOPS
"""

DOCKER_COMPOSE_NODE = {
    "title": "Docker Compose",
    "slug": "docker-compose",
    "description": "Multi-container applikationer med docker-compose.yml - services, volumes, networks och environment.",
    "difficulty": "medium",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "order_index": 3,
    "content": r"""# Docker Compose

> **TL;DR:** `docker compose up -d` startar hela stacken. `docker compose down -v` tar bort allt inkl volymer. En YAML-fil = hela infrastrukturen!

---

## 📖 TEORI: Vad är Docker Compose?

**Docker Compose** = Verktyg för multi-container applikationer
- YAML-fil (docker-compose.yml) beskriver ALLA tjänster
- **Ett kommando** startar hela stacken
- Ersätter långa `docker run`-kommandon

### Varför Compose?

| Utan Compose | Med Compose |
|--------------|-------------|
| Långa docker run-kommandon | En YAML-fil |
| Manuell nätverkshantering | Automatiskt nätverk |
| Svårt att reproducera | Versionshanterat (IaC) |
| Komplex start-ordning | depends_on |

### Infrastructure as Code (IaC)

```
┌─────────────────────────────────────────────────┐
│   docker-compose.yml = Din infrastruktur i kod │
│   Kan versionshanteras med Git                  │
│   Samma fil fungerar överallt                   │
└─────────────────────────────────────────────────┘
```

---

## 📖 docker-compose.yml struktur

### Grundläggande mall

```yaml
version: '3.8'  # Kan utelämnas i nyare versioner

services:
  # Service 1
  web:
    image: nginx:alpine
    ports:
      - "80:80"

  # Service 2
  api:
    build: ./api
    environment:
      - DB_HOST=db
    depends_on:
      - db

  # Service 3
  db:
    image: postgres:15
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:

networks:
  default:
    driver: bridge
```

### Sektioner förklarade

| Sektion | Beskrivning |
|---------|-------------|
| version | Compose-filversion (valfritt nu) |
| services | Container-definitioner |
| volumes | Named volumes för persistens |
| networks | Custom nätverk (valfritt) |

---

## 📖 Services - Detaljerat

### Använda färdig image

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
```

### Bygga från Dockerfile

```yaml
services:
  api:
    build: ./api                    # Katalog med Dockerfile
    # eller mer detaljerat:
    build:
      context: ./api
      dockerfile: Dockerfile.prod
      args:
        - VERSION=1.0
```

### Alla vanliga service-options

```yaml
services:
  myapp:
    image: myapp:latest
    container_name: myapp-container  # Specifikt namn
    ports:
      - "8080:80"
    volumes:
      - ./data:/app/data
    environment:
      - NODE_ENV=production
    depends_on:
      - db
    restart: unless-stopped          # Restart policy
    command: ["npm", "start"]        # Override CMD
    working_dir: /app
    user: "1000:1000"
```

---

## 📖 Volumes (VIKTIGT!)

> "Volumes bevarar data mellan container-restarts"

### Tre typer

```yaml
services:
  db:
    volumes:
      # 1. Named volume (Docker hanterar)
      - db_data:/var/lib/postgresql/data

      # 2. Bind mount (lokal katalog)
      - ./config:/etc/app/config

      # 3. Read-only mount
      - ./config:/etc/app/config:ro

# Named volumes MÅSTE deklareras
volumes:
  db_data:
```

### Named volume vs Bind mount

| Named Volume | Bind Mount |
|--------------|------------|
| Docker hanterar | Du hanterar |
| Bra för databaser | Bra för config/kod |
| Portabelt | Kräver specifik path |
| db_data:/path | ./local:/path |

---

## 📖 Environment Variables (VIKTIGT!)

> "Separerar secrets från kod"

### Tre sätt

```yaml
services:
  db:
    # 1. Direkt i YAML (lista)
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=myapp

    # 2. Direkt i YAML (objekt)
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: myapp

    # 3. Från .env-fil
    environment:
      - POSTGRES_PASSWORD=${DB_PASSWORD}
```

### .env-fil (VIKTIGT!)

```bash
# .env (LÄGG TILL I .gitignore!)
DB_PASSWORD=supersecret
POSTGRES_USER=admin
API_KEY=abc123
```

```yaml
# docker-compose.yml
services:
  db:
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_USER: ${POSTGRES_USER}
```

⚠️ **ALDRIG committa .env med secrets till Git!**

---

## 📖 depends_on (VIKTIGT!)

> "Kontrollerar startordning av services"

```yaml
services:
  web:
    depends_on:
      - api        # api startar FÖRE web

  api:
    depends_on:
      - db         # db startar FÖRE api

  db:
    image: postgres:15
```

### ⚠️ VIKTIGT att förstå

```
depends_on väntar på att containern STARTAR
INTE att tjänsten är REDO!

db-containern startar → api startar direkt
Men PostgreSQL kanske inte är redo än!

Lösning: Healthchecks eller wait-scripts
```

---

## 📖 Ports och Networks

### Port-mapping

```yaml
services:
  web:
    ports:
      - "8080:80"      # host:container
      - "443:443"
      - "3000"         # Random host-port
```

### Automatiskt nätverk

```yaml
# Alla services i samma Compose-fil kan nå varandra
# via SERVICE-NAMN som hostname!

services:
  web:
    # Kan nå api på hostname "api"
    environment:
      - API_URL=http://api:3000

  api:
    # Kan nå db på hostname "db"
    environment:
      - DATABASE_URL=postgres://db:5432/myapp

  db:
    image: postgres:15
```

---

## 📖 Compose-kommandon

### Starta och stoppa

```bash
# Starta alla tjänster
docker compose up

# Starta i bakgrunden
docker compose up -d

# Bygg images och starta
docker compose up --build

# Starta specifik service
docker compose up -d web

# Stoppa (behåller containers)
docker compose stop

# Stoppa och ta bort containers
docker compose down

# Ta bort INKLUSIVE volumes (DATA!)
docker compose down -v
```

### Status och loggar

```bash
# Visa status
docker compose ps

# Visa loggar
docker compose logs

# Följ loggar
docker compose logs -f

# Loggar för specifik service
docker compose logs -f web
docker compose logs --tail 100 api
```

### Interagera

```bash
# Kör kommando i service
docker compose exec web bash
docker compose exec db psql -U postgres

# Kör engångskommando
docker compose run --rm web npm test
```

### Skalning

```bash
# Skala service
docker compose up -d --scale web=3

# Nu finns web-1, web-2, web-3
docker compose ps
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: WordPress + MariaDB (från kursen)

```yaml
# docker-compose.yml
version: '3.8'

services:
  wordpress:
    image: wordpress:latest
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: ${WP_DB_PASSWORD}
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress_data:/var/www/html
    depends_on:
      - db
    restart: unless-stopped

  db:
    image: mariadb:10.6
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: ${WP_DB_PASSWORD}
    volumes:
      - db_data:/var/lib/mysql
    restart: unless-stopped

volumes:
  wordpress_data:
  db_data:
```

**.env:**
```bash
MYSQL_ROOT_PASSWORD=supersecret
WP_DB_PASSWORD=wordpress_password
```

**Köra:**
```bash
docker compose up -d
# Öppna http://localhost:8080
```

### Exempel 2: 3-tier med Caddy reverse proxy

```yaml
version: '3.8'

services:
  # Frontend
  frontend:
    image: nginx:alpine
    volumes:
      - ./frontend:/usr/share/nginx/html:ro
    depends_on:
      - api

  # Backend API
  api:
    build: ./api
    environment:
      - DATABASE_URL=postgres://postgres:secret@db:5432/myapp
    depends_on:
      - db

  # Database
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: myapp
    volumes:
      - db_data:/var/lib/postgresql/data

  # Reverse Proxy
  caddy:
    image: caddy:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - caddy_data:/data

volumes:
  db_data:
  caddy_data:
```

### Exempel 3: Development environment

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    volumes:
      # Bind mount för hot-reload
      - .:/app
      - /app/node_modules    # Exkludera node_modules
    environment:
      - NODE_ENV=development
    command: npm run dev

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: devpassword
      POSTGRES_DB: devdb
    ports:
      - "5432:5432"          # Exponera för lokala verktyg
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | docker compose up -d gör? | Startar alla services i bakgrunden |
| 2 | docker compose down -v gör? | Stoppar och tar bort ALLT inkl volumes |
| 3 | depends_on gör? | Kontrollerar startordning |
| 4 | Named volume syntax? | db_data:/var/lib/data |
| 5 | Bind mount syntax? | ./local:/container |
| 6 | ${VAR} i compose läser från? | .env-fil |
| 7 | docker compose logs -f gör? | Följer loggar i realtid |
| 8 | docker compose exec web bash? | Öppnar shell i web-service |
| 9 | Hur når services varandra? | Via service-namn som hostname |
| 10 | docker compose ps visar? | Status för alla services |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad är Docker Compose?**
- A) En container
- B) Verktyg för multi-container applikationer ✅
- C) Ett operativsystem
- D) En image

**2. Vilken fil beskriver Compose-stacken?**
- A) Dockerfile
- B) compose.json
- C) docker-compose.yml ✅
- D) stack.yaml

**3. Hur startar du alla services i bakgrunden?**
- A) docker compose start
- B) docker compose up -d ✅
- C) docker compose run -d
- D) docker compose begin

**4. Vad gör docker compose down -v?**
- A) Bara stoppar
- B) Tar bort containers
- C) Tar bort allt inkl volumes ✅
- D) Visar version

**5. Hur refererar services till varandra?**
- A) Via IP-adress
- B) Via container-ID
- C) Via service-namn som hostname ✅
- D) Via port

**6. Var ska secrets som passwords lagras?**
- A) I docker-compose.yml
- B) I .env-fil (gitignored) ✅
- C) I Dockerfile
- D) Hårdkodade

**7. Vad gör depends_on?**
- A) Installerar dependencies
- B) Kontrollerar startordning ✅
- C) Väntar på att tjänst är redo
- D) Linkar containers

**8. Hur kör du kommando i körande service?**
- A) docker compose run
- B) docker compose exec ✅
- C) docker compose cmd
- D) docker compose bash

**9. Skillnad mellan named volume och bind mount?**
- A) Ingen skillnad
- B) Named = Docker hanterar, Bind = lokal path ✅
- C) Bind är snabbare
- D) Named är temporärt

**10. docker compose up --build gör?**
- A) Bara bygger
- B) Bygger images OCH startar ✅
- C) Bygger utan cache
- D) Visar build-log

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Enkel nginx + html
```bash
# 1. Skapa projektmapp
mkdir -p /tmp/compose-test && cd /tmp/compose-test

# 2. Skapa HTML
mkdir html
echo "<h1>Hello from Compose!</h1>" > html/index.html

# 3. Skapa docker-compose.yml
cat > docker-compose.yml << 'EOF'
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html:ro
EOF

# 4. Starta
docker compose up -d

# 5. Testa
curl localhost:8080

# 6. Visa status
docker compose ps

# 7. Städa
docker compose down
cd && rm -rf /tmp/compose-test
```

### Övning 2: App + Database
```bash
# 1. Skapa projektmapp
mkdir -p /tmp/app-db && cd /tmp/app-db

# 2. Skapa .env
cat > .env << 'EOF'
POSTGRES_PASSWORD=secretpass
EOF

# 3. Skapa docker-compose.yml
cat > docker-compose.yml << 'EOF'
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: testdb
    volumes:
      - db_data:/var/lib/postgresql/data

  adminer:
    image: adminer
    ports:
      - "8080:8080"
    depends_on:
      - db

volumes:
  db_data:
EOF

# 4. Starta
docker compose up -d

# 5. Kolla loggar
docker compose logs db

# 6. Öppna http://localhost:8080
# Server: db, User: postgres, Password: secretpass, Database: testdb

# 7. Städa (inkl data)
docker compose down -v
cd && rm -rf /tmp/app-db
```

### Övning 3: Utforska kommandon
```bash
# Med en körande stack:

# 1. Visa alla services
docker compose ps

# 2. Följ loggar
docker compose logs -f

# 3. Gå in i container
docker compose exec db bash
psql -U postgres
\l
\q
exit

# 4. Skala (om möjligt)
docker compose up -d --scale web=2
docker compose ps
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Konsekvens | Lösning |
|---------|------------|---------|
| Committa .env | Läcker secrets | Lägg i .gitignore! |
| Glömma volumes: | Named volumes funkar inte | Deklarera i volumes: |
| depends_on = ready | Tjänst inte redo | Använd healthcheck/wait |
| down utan -v | Gamla data kvar | -v för clean slate |

---

## 📝 SAMMANFATTNING

```yaml
# GRUNDLÄGGANDE STRUKTUR
services:
  web:
    image: nginx:alpine           # Eller build: ./
    ports:
      - "8080:80"                 # host:container
    volumes:
      - ./html:/usr/share/nginx/html  # bind mount
      - data:/app/data            # named volume
    environment:
      - API_URL=http://api:3000   # service-namn som host
    depends_on:
      - api
    restart: unless-stopped

volumes:
  data:                           # Deklarera named volumes
```

```bash
# KOMMANDON
docker compose up -d              # Starta bakgrund
docker compose up --build         # Bygg + starta
docker compose down               # Stoppa + ta bort
docker compose down -v            # + ta bort volumes
docker compose ps                 # Status
docker compose logs -f            # Följ loggar
docker compose exec web bash      # Shell i service
docker compose up -d --scale web=3  # Skala

# VIKTIGA KONCEPT
# - Services når varandra via namn (web, api, db)
# - .env för secrets (gitignore!)
# - depends_on = startordning (ej readiness)
# - Named volumes för persistens
# - Bind mounts för lokal utveckling
```

"""
}

