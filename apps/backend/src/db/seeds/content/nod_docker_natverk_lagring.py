"""
NOD: Docker-nätverk och Datalagring: Kommunikation och Persistence
==================================================================
Förstå volymer, bind mounts, port mapping och containernätverk för databeständighet och kommunikation
"""

DOCKER_NATVERK_LAGRING_NODE = {
    "title": "Docker-nätverk och Datalagring: Kommunikation och Persistence",
    "slug": "docker-natverk-lagring",
    "description": "Förstå volymer, bind mounts, port mapping och containernätverk för databeständighet och kommunikation",
    "difficulty": "medium",
    "estimated_minutes": 60,
    "xp_reward": 130,
    "order_index": 9,
    "content": r"""# Docker-nätverk och Datalagring: Kommunikation och Persistence

Tematiskt fokus: Hur containrar kommunicerar och bevarar data

## Lagringsstrategier: Volymer jämfört med Bind Mounts

### Volymer: Docker-hanterad lagring (optimal för databaser)

Volymer representerar Docker-kontrollerad lagring som persisterar oberoende av containerns livscykel.

```bash
# Skapa volym
docker volume create mydata

# Visa alla volymer
docker volume ls

# Detaljerad volym-information
docker volume inspect mydata

# Montera volym i container
docker run -d -v mydata:/var/lib/mysql mysql

# Alternativt med --mount (modernare syntax)
docker run -d --mount type=volume,source=mydata,target=/var/lib/mysql mysql
```

**Styrkor**:
- Docker ansvarar för lagringsplatsen
- Plattformsoberoende
- Delningsbara mellan flera containrar
- Enklare backup och migration

**Användningsområden**: Databasdata, beständig information som måste överleva container-borttagning.

```bash
# Exempel: MySQL med beständig volym
docker run -d \
  --name mysql \
  -v mysql_data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0

# Information bevaras trots att containern tas bort
docker stop mysql
docker rm mysql
# Volymen mysql_data finns fortfarande kvar
```

### Bind Mounts: Lokala mappar (optimalt för utveckling)

Bind mounts kopplar en host-katalog direkt till containern.

```bash
# Bind mount
docker run -d -v /host/path:/container/path nginx

# Med --mount syntax
docker run -d --mount type=bind,source=/host/path,target=/container/path nginx

# Skrivskyddad bind mount
docker run -d -v /host/path:/container/path:ro nginx
```

**Styrkor**:
- Omedelbar åtkomst till host-filer
- Förändringar reflekteras direkt
- Utmärkt för utvecklingsmiljöer

**Svagheter**:
- Beror på host-filsystemet
- Potentiella prestandaproblem på macOS/Windows

**Användningsområden**: Utvecklingsarbete, konfiguration, loggfiler.

```bash
# Exempel: Utvecklingsmiljö med bind mount
docker run -d \
  --name app \
  -v $(pwd)/src:/app/src \
  -v $(pwd)/config:/app/config:ro \
  myapp

# Kodändringar i src/ syns direkt i containern
```

### tmpfs Mounts: In-memory lagring

```bash
# tmpfs mount (enbart i RAM)
docker run -d --tmpfs /tmp nginx

# Med --mount syntax
docker run -d --mount type=tmpfs,destination=/tmp nginx
```

**Användningsområden**: Tillfällig data som inte kräver persistens.

## Port Mapping: Distinktionen mellan host-port och container-port

### Grundprinciper för port mapping

```bash
# Format: -p host_port:container_port
docker run -d -p 8080:80 nginx

# Åtkomst via localhost:8080
curl http://localhost:8080
```

**Förklaring**:
- **8080**: Port på värdmaskinen
- **80**: Port inne i containern (nginx lyssningsport)

### Varianter av port mapping

```bash
# Specifik host-IP och port
docker run -d -p 127.0.0.1:8080:80 nginx
# Tillgänglig endast via localhost:8080

# Alla nätverksgränssnitt (standard)
docker run -d -p 8080:80 nginx
# Nåbar via samtliga IP-adresser på hosten

# Slumpmässig host-port
docker run -d -p 80 nginx
# Docker tilldelar en ledig port automatiskt

# Flera portmappningar
docker run -d -p 8080:80 -p 8443:443 nginx
```

### Kontrollera port mappings

```bash
# Visa mappade portar
docker port <container_id>

# Alternativt
docker ps
# PORTS-kolumnen visar alla mappningar
```

## Nätverksfunktioner: Bridge-nätverk och Container-to-Container kommunikation

### Standard Bridge Network

Som standard kopplas alla containrar till bridge-nätverket.

```bash
# Visa tillgängliga nätverk
docker network ls

# Detaljerad information om bridge network
docker network inspect bridge
```

**Begränsningar med standard bridge**:
- Containrar nås endast via IP-adress
- Saknar DNS-resolution (container-namn fungerar inte)

### Skapa Anpassat Bridge Network

```bash
# Skapa eget bridge network
docker network create mynetwork

# Starta containrar på samma nätverk
docker run -d --name app1 --network mynetwork nginx
docker run -d --name app2 --network mynetwork nginx

# Containrar kan nu nå varandra via namn
docker exec app1 ping app2
# Fungerar! app2 översätts till IP via DNS
```

**Fördelar**:
- DNS-resolution fungerar mellan containrar
- Nätverksisolering
- Förenklad kommunikation

### Docker DNS (127.0.0.11)

Docker tillhandahåller en intern DNS-server på 127.0.0.11 för namnuppslagning mellan containrar.

```bash
# Inne i en container på custom network:
cat /etc/resolv.conf
# nameserver 127.0.0.11

# DNS översätter container-namn till IP
ping db
# PING db (172.18.0.3) 56(84) bytes of data

# Fungerar enbart på custom networks, INTE standard bridge
```

**Viktigt**:
- Aktiv endast på anpassade bridge networks, inte standard bridge
- Containrar på identiskt custom network når varandra via namn
- DNS-servern är inbyggd och hanteras automatiskt av Docker

### Container-namnkonflikter

Docker förhindrar flera containrar med identiska namn.

```bash
# Första containern
docker run -d --name myapp nginx

# Försök med samma namn
docker run -d --name myapp nginx
# Error: Conflict. The container name "/myapp" is already in use

# Lösningsalternativ:
# 1. Radera befintlig container först
docker rm myapp
docker run -d --name myapp nginx

# 2. Välj ett annat namn
docker run -d --name myapp2 nginx

# 3. Låt Docker generera namn automatiskt (utan --name)
docker run -d nginx
# Docker tilldelar unikt namn automatiskt
```

### --dns flaggan

Konfigurera anpassad DNS-server för en specifik container.

```bash
# Använd specifik DNS
docker run -d --dns 8.8.8.8 nginx

# Flera DNS-servrar
docker run -d --dns 8.8.8.8 --dns 1.1.1.1 nginx

# I containern:
cat /etc/resolv.conf
# nameserver 8.8.8.8
# nameserver 1.1.1.1
```

**Användningsområden**: När du behöver använda specifik DNS (t.ex. intern företags-DNS) istället för standardinställningar.

### Nätverkstyper

```bash
# Bridge (standard för containrar på samma host)
docker network create --driver bridge mynet

# Host (delar hostens nätverk - endast Linux)
docker network create --driver host mynet

# None (ingen nätverksanslutning)
docker network create --driver none mynet

# Starta container utan nätverksåtkomst
docker run --network none nginx
# Containern får ingen IP och saknar extern nätverksanslutning
# (endast loopback 127.0.0.1 tillgängligt)

# Overlay (för Docker Swarm, multi-host)
docker network create --driver overlay mynet
```

## Praktiskt exempel: Webbapplikation + Databas

```bash
# Skapa dedikerat nätverk
docker network create appnet

# Starta databas
docker run -d \
  --name db \
  --network appnet \
  -v db_data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0

# Starta webbapplikation
docker run -d \
  --name web \
  --network appnet \
  -p 8080:80 \
  -e DB_HOST=db \
  -e DB_PASSWORD=secret \
  myapp

# Webbappen kan nu nå db via "db" (DNS-resolution)
# curl http://localhost:8080 ansluter till databasen via hostname "db"
```

## Avancerade lagringsmetoder

### Named Volumes med specifik driver

```bash
# Skapa volym med driver
docker volume create --driver local \
  --opt type=nfs \
  --opt o=addr=192.168.1.100 \
  --opt device=:/path/to/nfs \
  nfs-volume
```

### Volume Backup och Återställning

```bash
# Backup av volym
docker run --rm \
  -v mydata:/data \
  -v $(pwd):/backup \
  ubuntu tar czf /backup/mydata-backup.tar.gz /data

# Återställning av volym
docker run --rm \
  -v mydata:/data \
  -v $(pwd):/backup \
  ubuntu tar xzf /backup/mydata-backup.tar.gz -C /data
```

### Volymdelning mellan flera containrar

```bash
# Skapa delad volym
docker volume create shared_data

# Container 1: Skriver information
docker run -d \
  --name writer \
  -v shared_data:/data \
  alpine sh -c "echo 'Hello' > /data/file.txt"

# Container 2: Läser information
docker run --rm \
  -v shared_data:/data \
  alpine cat /data/file.txt
# Output: Hello
```

## Nätverksdiagnostik

### Testa nätverksförbindelser

```bash
# Ping mellan containrar
docker exec container1 ping container2

# Testa porttillgänglighet
docker exec container1 nc -zv container2 3306

# Visa nätverksinformation
docker network inspect mynetwork
```

### Portexponering mellan containrar

```bash
# Containrar på samma nätverk BEHÖVER INTE port mapping
# De når varandra direkt via container-porten

# Container 1 lyssnar på port 80
docker run -d --name app1 --network mynet nginx

# Container 2 når app1 direkt på port 80
docker exec app2 curl http://app1:80
# Ingen -p flagga nödvändig!
```

## Praktiska applikationsscenarier

### Utvecklingsmiljö

```bash
# Nätverk för utveckling
docker network create devnet

# Databas
docker run -d \
  --name dev-db \
  --network devnet \
  -v $(pwd)/db-data:/var/lib/mysql \
  mysql:8.0

# Applikation med hot-reload (bind mount)
docker run -d \
  --name dev-app \
  --network devnet \
  -p 3000:3000 \
  -v $(pwd)/src:/app/src \
  node:16 npm run dev
```

### Produktionsmiljö

```bash
# Nätverk för produktion
docker network create prodnet

# Databas med beständig volym
docker run -d \
  --name prod-db \
  --network prodnet \
  -v prod_db_data:/var/lib/mysql \
  mysql:8.0

# Applikation med read-only filsystem
docker run -d \
  --name prod-app \
  --network prodnet \
  -p 80:3000 \
  --read-only \
  --tmpfs /tmp \
  myapp:latest
```

## Centrala lärdomar

- **Volymer**: Docker-hanterad lagring, optimal för databaser och beständig data
- **Bind Mounts**: Mappa host-kataloger, optimalt för utveckling
- **Bind Mount döljer innehåll**: Befintligt innehåll i container-mapp döljs av bind mount
- **Port Mapping**: `-p host:container` exponerar container-port på värdmaskinen
- **Port Publishing**: Skapar iptables-regler automatiskt för trafikdirigering
- **Bridge Networks**: Skapa custom network för DNS-resolution mellan containrar
- **Docker DNS (127.0.0.11)**: Inbyggd DNS för namnuppslagning (fungerar endast på custom networks)
- **Container-namnkonflikter**: Docker tillåter inte identiska container-namn
- **--dns**: Konfigurera anpassad DNS för specifik container
- **--network none**: Ingen nätverksåtkomst (endast loopback tillgängligt)
- **IPAM**: Hanterar IP-tilldelning i Docker-nätverk (subnet, gateway, IP-range)
- **docker network disconnect**: Koppla bort container från nätverk
- **docker inspect -f**: Extrahera specifik data med Go templates
- **Container Communication**: På samma nätverk når containrar varandra via namn
- **Storage Strategy**: Volymer för produktion, bind mounts för utveckling

"""
}
