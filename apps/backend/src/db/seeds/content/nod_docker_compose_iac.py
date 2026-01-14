"""
NOD: Docker Compose och Infrastructure as Code: Orkestrering av komplexa miljöer
================================================================================
Hantera multi-container-applikationer med YAML-konfiguration och immutable infrastructure-principer
"""

DOCKER_COMPOSE_NODE = {
    "title": "Docker Compose och Infrastructure as Code: Orkestrering av komplexa miljöer",
    "slug": "docker-compose-iac",
    "description": "Hantera multi-container-applikationer med YAML-konfiguration och immutable infrastructure-principer",
    "difficulty": "medium",
    "estimated_minutes": 70,
    "xp_reward": 150,
    "order_index": 10,
    "content": r"""# Docker Compose och Infrastructure as Code: Orkestrering av komplexa miljöer

Tematiskt fokus: Definiera och hantera hela applikationsmiljöer med en fil

## YAML Syntax: Betydelsen av indentering och struktur

Docker Compose baseras på YAML-format. Korrekt indentering är avgörande!

```yaml
# docker-compose.yml
version: "3.8"  # Compose fil-version

services:       # Samtliga tjänster definieras här
  web:          # Tjänstens namn
    image: nginx
    ports:
      - "8080:80"
```

**Grundregler**:
- Använd mellanslag, aldrig tabb-tecken
- Indentering ska vara enhetlig (typiskt 2 mellanslag)
- Kolon (`:`) måste följas av mellanslag
- Listor indikeras med bindestreck (`-`)

```yaml
# KORREKT
services:
  web:
    image: nginx
    ports:
      - "8080:80"
      - "8443:443"

# INKORREKT (felaktig indentering)
services:
web:
image: nginx
```

## Services: Centraliserad definition av miljövariabler, nätverk och volymer

### Grundläggande tjänstedefinition

```yaml
version: "3.8"

services:
  web:
    image: nginx:latest
    container_name: my_nginx
    ports:
      - "8080:80"
    environment:
      - NGINX_HOST=example.com
      - NGINX_PORT=80
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - appnet
```

### Miljövariabler

```yaml
services:
  app:
    image: myapp
    # Alternativ 1: Lista-format
    environment:
      - DB_HOST=db
      - DB_PASSWORD=secret
      - NODE_ENV=production

    # Alternativ 2: Dictionary-format
    environment:
      DB_HOST: db
      DB_PASSWORD: secret
      NODE_ENV: production

    # Alternativ 3: Från fil
    env_file:
      - .env
      - .env.production
```

### Nätverk

```yaml
services:
  web:
    image: nginx
    networks:
      - frontend
      - backend

  db:
    image: mysql
    networks:
      - backend

# Definiera nätverk
networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
```

### Volymer

```yaml
services:
  db:
    image: mysql
    volumes:
      # Namngiven volym
      - db_data:/var/lib/mysql
      # Bind mount
      - ./config:/etc/mysql/conf.d
      # Anonym volym
      - /tmp

# Definiera volymer
volumes:
  db_data:
    driver: local
```

## Orchestration Lite: Kontrollera startsekvens med depends_on

`depends_on` garanterar att tjänster startar i korrekt ordningsföljd.

```yaml
services:
  web:
    image: nginx
    depends_on:
      - db
      - redis
    # Web initieras EFTER db och redis

  db:
    image: mysql

  redis:
    image: redis
```

**OBS**: `depends_on` väntar bara på att containern startar, inte att tjänsten är fullt funktionell!

```yaml
# För att vänta på att tjänsten är fullt funktionell, använd healthcheck
services:
  web:
    image: nginx
    depends_on:
      db:
        condition: service_healthy

  db:
    image: mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
```

## Livscykel: docker-compose up -d, down och ps

### docker-compose up

```bash
# Starta samtliga tjänster
docker-compose up

# Starta i bakgrunden (-d = detached)
docker-compose up -d

# Bygga images innan uppstart
docker-compose up --build

# Bygga utan cache
docker-compose build --no-cache

# Bygga specifik tjänst
docker-compose build web

# Bygga och starta utan cache
docker-compose build --no-cache
docker-compose up -d

# Starta specifik tjänst
docker-compose up web

# Starta med override-fil
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
```

### docker-compose down

```bash
# Stoppa och radera containrar
docker-compose down

# Inkludera borttagning av volymer
docker-compose down -v

# Inkludera borttagning av images
docker-compose down --rmi all
```

### docker-compose ps

```bash
# Visa tjänststatus
docker-compose ps

# Utökad information
docker-compose ps -a
```

### Övriga viktiga kommandon

```bash
# Visa loggar
docker-compose logs
docker-compose logs -f web  # Följ loggar för web-tjänsten

# Exekvera kommando i tjänst
docker-compose exec web ls /app
```

### docker-compose exec vs docker exec

```bash
# docker-compose exec: Kör i tjänst definierad i compose-fil
docker-compose exec web bash

# docker exec: Kör direkt i container (kräver container-ID/namn)
docker exec myapp_web bash

# Distinktion: docker-compose exec använder tjänstnamnet från YAML
# docker exec använder container-namnet (kan skilja sig)
```

### Starta/stoppa tjänster

```bash
docker-compose start
docker-compose stop
docker-compose restart web
```

### Skalera tjänster

```bash
docker-compose up -d --scale web=3
# Kör 3 instanser av web-tjänsten

# Alternativt med docker-compose scale (äldre syntax)
docker-compose scale web=3

# OBS: Container-namn får suffix (_1, _2, _3) vid skalning
# myapp_web_1, myapp_web_2, myapp_web_3
```

## Komplett Exempel: Multi-Service Application

```yaml
version: "3.8"

services:
  # Webbserver
  web:
    build: .
    container_name: myapp_web
    ports:
      - "8080:80"
    environment:
      - DB_HOST=db
      - REDIS_HOST=redis
    volumes:
      - ./src:/app/src
      - ./logs:/app/logs
    depends_on:
      - db
      - redis
    networks:
      - appnet
    restart: unless-stopped

  # Databas
  db:
    image: mysql:8.0
    container_name: myapp_db
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: myapp
      MYSQL_USER: appuser
      MYSQL_PASSWORD: apppassword
    volumes:
      - db_data:/var/lib/mysql
      - ./db-init:/docker-entrypoint-initdb.d
    networks:
      - appnet
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis cache
  redis:
    image: redis:7-alpine
    container_name: myapp_redis
    volumes:
      - redis_data:/data
    networks:
      - appnet
    restart: unless-stopped
    command: redis-server --appendonly yes

  # Worker (bakgrundsjobb)
  worker:
    build: .
    command: node worker.js
    environment:
      - DB_HOST=db
      - REDIS_HOST=redis
    depends_on:
      - db
      - redis
    networks:
      - appnet
    restart: unless-stopped

# Nätverk
networks:
  appnet:
    driver: bridge

  # Externt nätverk (existerar redan, skapas inte av Compose)
  external_net:
    external: true
    name: existing_network

# Volymer
volumes:
  db_data:
    driver: local
  redis_data:
    driver: local
```

## Externa nätverk vs Compose-skapade nätverk

### Compose-skapade nätverk: Skapas automatiskt av Docker Compose

```yaml
networks:
  appnet:
    driver: bridge
# Skapas vid docker-compose up
# Raderas vid docker-compose down (om -v används)
```

### Externa nätverk: Existerar redan, skapas inte av Compose

```yaml
networks:
  external_net:
    external: true
    name: existing_network
# Använder existerande nätverk
# Raderas INTE vid docker-compose down
```

**Användningsområden**: När du behöver använda ett nätverk som skapats manuellt eller av ett annat Compose-projekt.

## Miljöspecifika Compose-filer

### docker-compose.yml (Utveckling)

```yaml
version: "3.8"

services:
  web:
    build: .
    volumes:
      - ./src:/app/src  # Hot reload
    environment:
      - NODE_ENV=development
```

### docker-compose.prod.yml (Produktion)

```yaml
version: "3.8"

services:
  web:
    image: myapp:latest
    # Inga volymer (read-only)
    environment:
      - NODE_ENV=production
    restart: always
```

```bash
# Utveckling
docker-compose up

# Produktion
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### docker-compose.override.yml

Docker Compose läser automatiskt `docker-compose.override.yml` om filen existerar och kombinerar den med huvudfilen.

```yaml
# docker-compose.yml (primär fil)
version: "3.8"
services:
  web:
    image: nginx
    ports:
      - "80:80"

# docker-compose.override.yml (laddas automatiskt)
version: "3.8"
services:
  web:
    volumes:
      - ./src:/app/src  # Adderas till huvudfilen
    environment:
      - DEBUG=true      # Adderas till huvudfilen
```

**Användningsområden**:
- Lokal utvecklingsmiljö (bind mounts, debug-portar)
- Miljöspecifika konfigurationer
- Överskriver eller kompletterar inställningar från huvudfilen

**Viktigt**: `docker-compose.override.yml` laddas automatiskt - ingen `-f` flagga krävs.

## Immutable Infrastructure

Immutable Infrastructure betyder att containrar är oföränderliga. Istället för att modifiera en körande container, bygger du en ny image och ersätter containern.

### Koncept

```bash
# ❌ DÅLIG PRAXIS: Modifiera körande container
docker exec myapp apt-get install newpackage
docker exec myapp nano /etc/config

# ✅ BRA PRAXIS: Bygg ny image och ersätt
docker-compose build myapp
docker-compose up -d --no-deps myapp
```

### Praktiskt exempel

```yaml
services:
  web:
    build: .
    # Vid ändringar:
    # 1. Modifiera Dockerfile eller källkod
    # 2. docker-compose build web
    # 3. docker-compose up -d --no-deps web
    # Containern ersätts med ny image
```

**Fördelar**:
- Reproducerbarhet (identisk image = identiskt resultat)
- Enklare rollback (återgå till tidigare image)
- Versionskontroll (varje image är versionerad)
- Säkerhet (ingen risk för manuella ändringar i produktionsmiljö)

## Best Practices

### 1. Använd .env-filer

Docker Compose läser automatiskt `.env`-filen i samma katalog.

```bash
# .env (i samma katalog som docker-compose.yml)
DB_PASSWORD=secret
REDIS_PASSWORD=secret
DB_HOST=db
```

```yaml
services:
  db:
    environment:
      MYSQL_PASSWORD: ${DB_PASSWORD}  # Läses från .env
      MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}

  web:
    environment:
      - DB_HOST=${DB_HOST}  # Läses från .env
```

**Viktigt**:
- `.env`-filen läses automatiskt av Docker Compose
- Använd `${VAR}` syntax i docker-compose.yml
- `.env` bör INTE versionshanteras (lägg till i .gitignore)
- Skapa `.env.example` med exempel-värden för dokumentation

### 2. Health Checks

```yaml
services:
  web:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:80/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

### 3. Resursbegränsningar

```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: "0.5"
          memory: 512M
        reservations:
          cpus: "0.25"
          memory: 256M
```

### 4. Loggningskonfiguration

```yaml
services:
  web:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## Centrala lärdomar

- **YAML Syntax**: Mellanslag för indentering, enhetlig struktur
- **Services**: Centraliserad definition av miljövariabler, nätverk och volymer
- **.env-filen**: Läses automatiskt av Docker Compose, använd `${VAR}` syntax
- **docker-compose.override.yml**: Laddas automatiskt och kombineras med huvudfilen (för lokal utveckling)
- **docker-compose exec vs docker exec**: exec använder tjänstnamn, docker exec använder container-namn
- **docker-compose build --no-cache**: Bygga images utan cache
- **restart: always vs unless-stopped**: always startar alltid, unless-stopped respekterar manuell avstängning
- **docker-compose scale / --scale**: Skalera tjänster till flera instanser
- **Externa nätverk**: Använd befintliga nätverk (raderas inte vid down)
- **Immutable Infrastructure**: Bygg ny image istället för att modifiera körande container
- **depends_on**: Kontrollerar startsekvens (men väntar inte på tjänstens beredskap)
- **docker-compose up -d**: Starta i bakgrunden
- **docker-compose down**: Stoppa och radera (använd `-v` för volymer, `--rmi all` för images)
- **docker-compose ps**: Visa tjänststatus i projektet
- **Multi-file**: Använd separata compose-filer för olika miljöer
- **Infrastructure as Code**: Hela miljön definierad i versionshanterade filer

"""
}
