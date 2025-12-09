# =============================================================================
# SYSTEM DESIGN MODULE - V3 Docker-style format
# =============================================================================
# 20 noder totalt
# Svensk text, inga emojis, Unicode-separatorer, ASCII-diagram, markdown-tabeller
# =============================================================================

SYSTEM_DESIGN_MODULE = {
    "id": "system-design",
    "title": "System Design",
    "description": "Designa skalbara, robusta och hogpresterande system",
    "icon": "architecture",
    "category": "architecture",
    "difficulty": "advanced",
    "estimated_hours": 35,
    "total_xp": 3100,
    "prerequisites": ["sql", "linux"],
    "nodes": [
        # =====================================================================
        # NODE 1: Introduction to System Design
        # =====================================================================
        {
            "title": "Introduction to System Design",
            "slug": "system-design-intro",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 120,
            "content": """# Introduction to System Design

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor System Design ar viktigt |
|----------|--------------------------------|
| **Skalning** | Hantera miljoner anvandare |
| **Tillganglighet** | 99.99% uptime |
| **Prestanda** | Sub-100ms response |
| **Kostnader** | Optimera infrastruktur |
| **Underhall** | Hallbar arkitektur |

Som DevOps-ingenjor maste du forsta:

- **Requirements** funktionella och icke-funktionella
- **Trade-offs** mellan olika losningar
- **Estimering** av kapacitet och resurser

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar System Design?

```
┌─────────────────────────────────────────────────────────┐
│                    SYSTEM DESIGN                        │
│                                                         │
│  Processen att definiera arkitektur, komponenter,       │
│  moduler och granssnitt for ett system som uppfyller    │
│  specificerade krav.                                    │
└─────────────────────────────────────────────────────────┘
```

### System Design Process

```
┌──────────────────────────────────────────────────────────┐
│  1. REQUIREMENTS GATHERING                               │
│     ├── Functional: Vad systemet ska gora               │
│     └── Non-functional: Hur bra det ska gora det        │
├──────────────────────────────────────────────────────────┤
│  2. HIGH-LEVEL DESIGN                                    │
│     ├── System komponenter                              │
│     ├── Data flow                                       │
│     └── Integrationer                                   │
├──────────────────────────────────────────────────────────┤
│  3. DETAILED DESIGN                                      │
│     ├── Database schema                                 │
│     ├── API endpoints                                   │
│     └── Algoritmer                                      │
├──────────────────────────────────────────────────────────┤
│  4. IDENTIFY BOTTLENECKS                                 │
│     ├── Single points of failure                        │
│     ├── Performance bottlenecks                         │
│     └── Data hotspots                                   │
└──────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Functional vs Non-Functional Requirements

### Functional Requirements

```
Vad systemet SKA gora:

- Anvandare kan logga in
- Systemet sparar meddelanden
- Anvandare kan soka produkter
- Systemet skickar notifikationer
```

### Non-Functional Requirements

| Krav | Beskrivning | Exempel |
|------|-------------|---------|
| **Skalbarhet** | Hantera tillvaxt | 10M anvandare |
| **Latency** | Svarstid | < 100ms |
| **Availability** | Upptid | 99.99% |
| **Durability** | Datasakerhet | Ingen dataforlust |
| **Security** | Sakerhet | E2E kryptering |
| **Maintainability** | Underhall | Enkel deploy |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Back-of-the-Envelope Estimation

```
Snabb kapacitetsplanering:

┌─────────────────────────────────────────────────────────┐
│ TRAFFIC ESTIMATION                                      │
├─────────────────────────────────────────────────────────┤
│ Daily Active Users (DAU):     10,000,000               │
│ Requests per user per day:    10                        │
│ Total requests per day:       100,000,000              │
│                                                         │
│ Requests per second (RPS):                             │
│ = 100M / (24 * 60 * 60)                                │
│ = 100M / 86,400                                        │
│ = ~1,157 RPS                                           │
│                                                         │
│ Peak traffic (5x average):    ~5,800 RPS               │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ STORAGE ESTIMATION                                      │
├─────────────────────────────────────────────────────────┤
│ Messages per user per day:    5                         │
│ Message size:                 500 bytes                 │
│                                                         │
│ Daily data:                                            │
│ = 10M * 5 * 500 bytes                                  │
│ = 25 GB per dag                                        │
│ = ~750 GB per manad                                    │
│ = ~9 TB per ar                                         │
└─────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Latency Numbers - Maste kunna

| Operation | Tid | Kommentar |
|-----------|-----|-----------|
| L1 cache reference | 0.5 ns | Snabbast |
| L2 cache reference | 7 ns | |
| RAM reference | 100 ns | |
| SSD random read | 150 us | 1000x RAM |
| HDD seek | 10 ms | Undvik |
| Same datacenter round trip | 0.5 ms | |
| Cross-continent round trip | 150 ms | EU till US |

### Storage Units

| Enhet | Bytes | Exempel |
|-------|-------|---------|
| 1 KB | 1,000 | Kort text |
| 1 MB | 1,000,000 | Bild |
| 1 GB | 1,000,000,000 | Video |
| 1 TB | 1,000,000,000,000 | Databas |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## System Design Interview Framework

```
┌──────────────────────────────────────────────────────────┐
│  STEG 1: CLARIFY REQUIREMENTS (5 min)                   │
│  ────────────────────────────────────────               │
│  - Vad ar use cases?                                    │
│  - Hur manga anvandare?                                 │
│  - Read/write ratio?                                    │
│  - Vilka features ar kritiska?                          │
├──────────────────────────────────────────────────────────┤
│  STEG 2: ESTIMATE SCALE (5 min)                         │
│  ────────────────────────────────────────               │
│  - QPS (queries per second)                             │
│  - Storage requirements                                 │
│  - Bandwidth                                            │
├──────────────────────────────────────────────────────────┤
│  STEG 3: HIGH-LEVEL DESIGN (10 min)                     │
│  ────────────────────────────────────────               │
│  - Rita komponenter                                     │
│  - Visa data flow                                       │
│  - Identifiera APIs                                     │
├──────────────────────────────────────────────────────────┤
│  STEG 4: DETAILED DESIGN (15 min)                       │
│  ────────────────────────────────────────               │
│  - Database design                                      │
│  - Caching strategy                                     │
│  - API design                                           │
├──────────────────────────────────────────────────────────┤
│  STEG 5: IDENTIFY BOTTLENECKS (5 min)                   │
│  ────────────────────────────────────────               │
│  - Single points of failure                             │
│  - Scaling strategies                                   │
│  - Monitoring/alerting                                  │
└──────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - System Design

| Begrepp | Beskrivning |
|---------|-------------|
| **Scalability** | Hantera okad last |
| **Availability** | System ar tillgangligt |
| **Reliability** | System fungerar korrekt |
| **Latency** | Tid for request |
| **Throughput** | Requests per sekund |
| **Consistency** | Data ar samma overallt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Over-engineering | For komplex losning | Borja enkelt |
| Under-estimation | For lite kapacitet | 10x marginal |
| Single point of failure | Ingen redundans | Replikering |
| Tight coupling | Beroenden | Microservices |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Requirements** | Borja alltid har |
| **Estimation** | Back-of-envelope |
| **Trade-offs** | Allt har kostnad |
| **Iterera** | Borja enkelt, utoka |
| **Bottlenecks** | Identifiera tidigt |

**Kom ihag:**
- Borja med requirements (funktionella + icke-funktionella)
- Gor snabba estimeringar for att validera
- Det finns inga perfekta losningar, bara trade-offs
- Borja enkelt och skala vid behov
- Identifiera flaskhalsar och single points of failure
"""
        },
        # =====================================================================
        # NODE 2: Scalability Fundamentals
        # =====================================================================
        {
            "title": "Scalability Fundamentals",
            "slug": "scalability-fundamentals",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 130,
            "content": """# Scalability Fundamentals

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor skalbarhet ar viktigt |
|----------|------------------------------|
| **Tillvaxt** | Hantera fler anvandare |
| **Kostnad** | Betala for det du anvander |
| **Prestanda** | Behalla snabbhet under last |
| **Resiliens** | Overleva traffic spikes |
| **Flexibilitet** | Skala upp och ner |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vertikal vs Horisontell Skalning

```
VERTIKAL SKALNING (Scale Up)
────────────────────────────
Lagga till mer kraft till EN maskin

     Fore              Efter
  ┌─────────┐      ┌─────────┐
  │  4 CPU  │      │ 16 CPU  │
  │  8 GB   │  ->  │ 64 GB   │
  │ 100 GB  │      │  1 TB   │
  └─────────┘      └─────────┘

Fordelar:
+ Enkelt att implementera
+ Ingen kodandring kravs
+ Ingen komplexitet

Nackdelar:
- Har en ovre grans
- Single point of failure
- Dyrt vid hoga specifikationer
```

```
HORISONTELL SKALNING (Scale Out)
────────────────────────────────
Lagga till FLER maskiner

     Fore                    Efter
  ┌─────────┐      ┌─────────┐ ┌─────────┐ ┌─────────┐
  │ Server  │      │ Server  │ │ Server  │ │ Server  │
  │   #1    │  ->  │   #1    │ │   #2    │ │   #3    │
  └─────────┘      └─────────┘ └─────────┘ └─────────┘

Fordelar:
+ Teoretiskt oandlig skalning
+ Redundans och fault tolerance
+ Kostnadseffektivt med commodity hardware

Nackdelar:
- Kraver load balancer
- Mer komplex arkitektur
- Data consistency utmaningar
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Stateless vs Stateful

### Stateless Design

```
┌──────────────────────────────────────────────────────────┐
│                    STATELESS                             │
├──────────────────────────────────────────────────────────┤
│  Varje request innehaller ALL information som behovs    │
│  Servern sparar INGENTING mellan requests               │
└──────────────────────────────────────────────────────────┘

     Request 1          Request 2          Request 3
    ┌─────────┐        ┌─────────┐        ┌─────────┐
    │ Token:  │        │ Token:  │        │ Token:  │
    │ abc123  │        │ abc123  │        │ abc123  │
    │ Data:X  │        │ Data:Y  │        │ Data:Z  │
    └────┬────┘        └────┬────┘        └────┬────┘
         │                  │                  │
         v                  v                  v
    ┌─────────┐        ┌─────────┐        ┌─────────┐
    │ Server  │        │ Server  │        │ Server  │
    │   A     │        │   B     │        │   C     │
    └─────────┘        └─────────┘        └─────────┘

Fordelar:
+ Enkel horisontell skalning
+ Vilken server som helst kan hantera request
+ Enkel failover
```

### Stateful Design (problem)

```
┌──────────────────────────────────────────────────────────┐
│                    STATEFUL                              │
├──────────────────────────────────────────────────────────┤
│  Servern sparar session state                           │
│  Anvandaren MASTE alltid traffa samma server            │
└──────────────────────────────────────────────────────────┘

Problem: Session affinity / sticky sessions kravs
         Om servern gar ner forsvinner all state
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skalningsstrategier

### 1. Database Scaling

```
READ REPLICAS
─────────────
                    ┌─────────────┐
                    │   Primary   │
                    │  (Writes)   │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           v               v               v
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │  Replica 1  │ │  Replica 2  │ │  Replica 3  │
    │  (Reads)    │ │  (Reads)    │ │  (Reads)    │
    └─────────────┘ └─────────────┘ └─────────────┘

SHARDING
────────
Data delas upp baserat pa shard key

    User ID 1-1000     User ID 1001-2000   User ID 2001-3000
    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
    │   Shard 1   │    │   Shard 2   │    │   Shard 3   │
    └─────────────┘    └─────────────┘    └─────────────┘
```

### 2. Application Scaling

```
AUTO-SCALING
────────────
              CPU > 70%           CPU < 30%
                  │                   │
                  v                   v
            ┌─────────┐         ┌─────────┐
            │ Scale   │         │ Scale   │
            │   UP    │         │  DOWN   │
            └─────────┘         └─────────┘
                  │                   │
                  v                   v
         ┌───┐ ┌───┐ ┌───┐      ┌───┐ ┌───┐
         │ S │ │ S │ │ S │      │ S │ │ S │
         └───┘ └───┘ └───┘      └───┘ └───┘
          3 servrar              2 servrar
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Skalbarhet

| Strategi | Anvand nar |
|----------|------------|
| Vertikal | Snabb fix, liten skala |
| Horisontell | Stor skala, redundans |
| Read replicas | Manga reads |
| Sharding | Massiv data |
| Caching | Repetitiva queries |
| CDN | Statiskt innehall |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Session lost | Stateful design | Externalisera state |
| Hot spots | Dålig shard key | Valj battre key |
| Over-scaling | For aggressiv | Tune thresholds |
| Under-scaling | For konservativ | Monitor och justera |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Stateless** | Mojliggor enkel skalning |
| **Horisontell** | Foredra over vertikal |
| **Auto-scaling** | Reagera pa last |
| **Trade-offs** | Komplexitet vs kapacitet |

**Kom ihag:**
- Design for stateless fran borjan
- Horisontell skalning ar mer flexibel
- Externalisera state (Redis, DB)
- Auto-scaling sparar pengar
- Monitorera for att veta nar du ska skala
"""
        },
        # =====================================================================
        # NODE 3: Load Balancing
        # =====================================================================
        {
            "title": "Load Balancing",
            "slug": "load-balancing",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 120,
            "content": """# Load Balancing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor load balancing ar viktigt |
|----------|----------------------------------|
| **Distribution** | Fordela trafik jamnt |
| **Availability** | Failover vid problem |
| **Skalning** | Lagg till/ta bort servrar |
| **Prestanda** | Undvik overbelastning |
| **SSL Termination** | Centraliserad HTTPS |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar en Load Balancer?

```
                        ┌─────────────────┐
                        │  Load Balancer  │
                        │                 │
      Request ────────> │  Distribuerar   │
                        │    trafik       │
                        └────────┬────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              v                  v                  v
        ┌──────────┐       ┌──────────┐       ┌──────────┐
        │ Server 1 │       │ Server 2 │       │ Server 3 │
        │  (25%)   │       │  (50%)   │       │  (25%)   │
        └──────────┘       └──────────┘       └──────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Load Balancing Algoritmer

### Round Robin

```
Request 1 -> Server A
Request 2 -> Server B
Request 3 -> Server C
Request 4 -> Server A  (borjar om)
Request 5 -> Server B
...

+ Enkelt
+ Rattvist
- Tar ej hansyn till serverkapacitet
```

### Weighted Round Robin

```
Server A (vikt 3): Tar 3 requests
Server B (vikt 2): Tar 2 requests
Server C (vikt 1): Tar 1 request

Request 1,2,3 -> Server A
Request 4,5   -> Server B
Request 6     -> Server C
Request 7,8,9 -> Server A
...

+ Hansyn till kapacitet
+ Flexibelt
```

### Least Connections

```
         Aktiva connections
Server A:    5
Server B:    3   <-- Nasta request gar hit
Server C:    8

+ Bra for langa requests
+ Dynamisk fordelning
```

### IP Hash

```
hash(client_ip) % antal_servrar = server_index

Client 192.168.1.1 -> alltid Server A
Client 192.168.1.2 -> alltid Server B

+ Session persistence utan cookies
- Ojamn fordelning mojlig
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Layer 4 vs Layer 7

### Layer 4 (Transport)

```
┌──────────────────────────────────────────────────────────┐
│  LAYER 4 LOAD BALANCING                                  │
├──────────────────────────────────────────────────────────┤
│  Baserat pa: IP-adress och port                         │
│  Snabbare: Tittar inte pa innehall                      │
│  Anvandning: TCP/UDP trafik                             │
└──────────────────────────────────────────────────────────┘

     TCP Connection
    ┌────────────────┐
    │ Src: 10.0.0.1  │
    │ Dst: LB IP     │──────> Load Balancer ──> Server
    │ Port: 443      │
    └────────────────┘
```

### Layer 7 (Application)

```
┌──────────────────────────────────────────────────────────┐
│  LAYER 7 LOAD BALANCING                                  │
├──────────────────────────────────────────────────────────┤
│  Baserat pa: HTTP headers, URL, cookies                 │
│  Smartare: Content-based routing                        │
│  Anvandning: HTTP/HTTPS trafik                          │
└──────────────────────────────────────────────────────────┘

     HTTP Request
    ┌────────────────┐
    │ GET /api/users │──> API servers
    │ GET /images/*  │──> Static servers
    │ GET /admin/*   │──> Admin servers
    └────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Health Checks

```
Load Balancer utfor regelbundna health checks:

    LB ──── GET /health ────> Server A  (200 OK)     [HEALTHY]
    LB ──── GET /health ────> Server B  (200 OK)     [HEALTHY]
    LB ──── GET /health ────> Server C  (timeout)    [UNHEALTHY]

         ┌──────────────────────────────────────┐
         │          TRAFFIC ROUTING             │
         ├──────────────────────────────────────┤
         │  Server A: [====] Receives traffic   │
         │  Server B: [====] Receives traffic   │
         │  Server C: [----] Removed from pool  │
         └──────────────────────────────────────┘

Health Check Types:
- TCP: Kan vi oppna en connection?
- HTTP: Returnerar endpoint 200?
- Custom: Applikationsspecifik logik
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## High Availability Setup

```
                    ┌─────────────┐
                    │     DNS     │
                    └──────┬──────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              v                         v
       ┌─────────────┐          ┌─────────────┐
       │     LB 1    │◄────────►│     LB 2    │
       │  (Active)   │  VRRP    │  (Standby)  │
       └──────┬──────┘          └─────────────┘
              │
    ┌─────────┼─────────┐
    v         v         v
┌───────┐ ┌───────┐ ┌───────┐
│ Srv 1 │ │ Srv 2 │ │ Srv 3 │
└───────┘ └───────┘ └───────┘

Om LB 1 gar ner tar LB 2 over automatiskt
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Load Balancers

| Produkt | Typ | Anvandning |
|---------|-----|------------|
| **NGINX** | L7 | Web, reverse proxy |
| **HAProxy** | L4/L7 | High performance |
| **AWS ALB** | L7 | AWS, HTTP routing |
| **AWS NLB** | L4 | AWS, TCP/UDP |
| **GCP LB** | L4/L7 | Google Cloud |
| **Azure LB** | L4 | Azure |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Uneven load | Fel algoritm | Byt till weighted |
| Session loss | Ingen persistence | Sticky sessions |
| Single LB failure | Ingen redundans | HA setup |
| Slow health check | For langsam | Tune intervall |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Algoritm** | Valj efter use case |
| **Health checks** | Alltid konfigurera |
| **L4 vs L7** | L7 for smartare routing |
| **HA** | Tva LBs minimum |

**Kom ihag:**
- Least Connections bast for varierande requests
- Health checks ar kritiska for reliability
- L7 for content-based routing
- Alltid redundanta load balancers i prod
"""
        },
        # =====================================================================
        # NODE 4: Caching Strategies
        # =====================================================================
        {
            "title": "Caching Strategies",
            "slug": "caching-strategies",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 130,
            "content": """# Caching Strategies

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor caching ar viktigt |
|----------|---------------------------|
| **Latency** | Snabbare svarstider |
| **Database load** | Minska queries |
| **Throughput** | Hantera mer trafik |
| **Kostnad** | Mindre compute behov |
| **UX** | Battre anvandarupplevelse |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cache Hierarki

```
┌─────────────────────────────────────────────────────────────┐
│                    CACHE HIERARKI                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────┐                                          │
│   │  Browser    │  <-- Snabbast (lokal)                    │
│   │   Cache     │      ~1ms                                │
│   └──────┬──────┘                                          │
│          │                                                 │
│   ┌──────v──────┐                                          │
│   │    CDN      │  <-- Edge location                       │
│   │   Cache     │      ~10-50ms                            │
│   └──────┬──────┘                                          │
│          │                                                 │
│   ┌──────v──────┐                                          │
│   │ Application │  <-- Redis/Memcached                     │
│   │   Cache     │      ~1-5ms                              │
│   └──────┬──────┘                                          │
│          │                                                 │
│   ┌──────v──────┐                                          │
│   │  Database   │  <-- Query cache                         │
│   │   Cache     │      ~10-100ms                           │
│   └──────┬──────┘                                          │
│          │                                                 │
│   ┌──────v──────┐                                          │
│   │   Origin    │  <-- Disk I/O                            │
│   │  Database   │      ~100-1000ms                         │
│   └─────────────┘                                          │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cache-Aside (Lazy Loading)

```
┌──────────────────────────────────────────────────────────┐
│  CACHE-ASIDE PATTERN                                     │
└──────────────────────────────────────────────────────────┘

READ Operation:
                                  ┌─────────┐
                           1. Get │  Cache  │
    ┌──────────┐ ──────────────> └────┬────┘
    │   App    │                      │
    └────┬─────┘ <────────────────────┘
         │        2a. Hit: Return data
         │
         │ 2b. Miss: Query DB
         v
    ┌──────────┐
    │ Database │
    └────┬─────┘
         │
         │ 3. Store in cache
         v
    ┌──────────┐
    │  Cache   │
    └──────────┘

WRITE Operation:
    1. Write to database
    2. Invalidate cache (eller uppdatera)
```

### Kod Exempel

```python
def get_user(user_id):
    # 1. Check cache first
    cached = cache.get(f"user:{user_id}")
    if cached:
        return cached

    # 2. Cache miss - query database
    user = db.query(User).get(user_id)

    # 3. Store in cache for next time
    cache.set(f"user:{user_id}", user, ttl=3600)

    return user
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Write-Through Cache

```
┌──────────────────────────────────────────────────────────┐
│  WRITE-THROUGH PATTERN                                   │
└──────────────────────────────────────────────────────────┘

WRITE Operation:
    ┌──────────┐
    │   App    │
    └────┬─────┘
         │ 1. Write
         v
    ┌──────────┐
    │  Cache   │ ────── 2. Sync write ────> ┌──────────┐
    └──────────┘                            │ Database │
                                            └──────────┘

+ Data alltid konsistent
+ Latency vid writes
- Hojer write-latency
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Write-Behind (Write-Back)

```
┌──────────────────────────────────────────────────────────┐
│  WRITE-BEHIND PATTERN                                    │
└──────────────────────────────────────────────────────────┘

WRITE Operation:
    ┌──────────┐
    │   App    │
    └────┬─────┘
         │ 1. Write (returns immediately)
         v
    ┌──────────┐
    │  Cache   │ ─── 2. Async batch write ──> ┌──────────┐
    └──────────┘     (later)                  │ Database │
                                              └──────────┘

+ Lag write-latency
+ Batching mojligt
- Risk for data loss
- Komplexitet
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cache Invalidation Strategies

```
┌───────────────────────────────────────────────────────────┐
│            INVALIDATION STRATEGIES                        │
├───────────────────────────────────────────────────────────┤
│                                                           │
│  1. TIME-BASED (TTL)                                      │
│     ┌──────────────────────────────────────┐             │
│     │ cache.set(key, value, ttl=3600)      │             │
│     │ # Expires after 1 hour               │             │
│     └──────────────────────────────────────┘             │
│                                                           │
│  2. EVENT-BASED                                           │
│     ┌──────────────────────────────────────┐             │
│     │ def update_user(user):               │             │
│     │     db.update(user)                  │             │
│     │     cache.delete(f"user:{user.id}")  │             │
│     └──────────────────────────────────────┘             │
│                                                           │
│  3. VERSION-BASED                                         │
│     ┌──────────────────────────────────────┐             │
│     │ key = f"user:{id}:v{version}"        │             │
│     │ # Ny version = ny cache key          │             │
│     └──────────────────────────────────────┘             │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cache Stampede Prevention

```
Problem: Manga requests samtidigt vid cache miss

    Request 1 ──┐
    Request 2 ──┼──> Cache Miss ──> All hit DB simultaneously!
    Request 3 ──┤
    Request 4 ──┘

Losningar:

1. LOCKING (endast en hamtar)
   ┌────────────────────────────────────────┐
   │ Request 1: Acquire lock, fetch from DB │
   │ Request 2-4: Wait for lock release     │
   │ Request 1: Store in cache, release     │
   │ Request 2-4: Get from cache            │
   └────────────────────────────────────────┘

2. PROBABILISTIC EARLY EXPIRATION
   ┌────────────────────────────────────────┐
   │ TTL = 3600                             │
   │ Refresh at: 3000 + random(0-600)       │
   │ Requests refreshar vid olika tider    │
   └────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Cache Teknologier

| Teknologi | Typ | Anvandning |
|-----------|-----|------------|
| **Redis** | In-memory | Session, cache, pub/sub |
| **Memcached** | In-memory | Simple key-value |
| **Varnish** | HTTP cache | Full page caching |
| **CDN** | Edge cache | Static content |
| **Browser** | Client | Assets, API responses |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Stale data | For lang TTL | Kortare TTL eller invalidering |
| Cache miss storm | TTL expires | Staggered expiration |
| Memory exhaustion | For mycket data | Eviction policy |
| Hot keys | Ojamn fordelning | Replication |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Cache-aside** | Vanligaste pattern |
| **TTL** | Balansera freshness vs hit rate |
| **Invalidering** | Hardaste problemet |
| **Stampede** | Planera for det |

**Kom ihag:**
- "There are only two hard things: cache invalidation and naming things"
- Borja med cache-aside, optimera sen
- Monitor cache hit ratio (mal: over 90%)
- Redis ar ofta ratt val for de flesta behov
"""
        },
        # =====================================================================
        # NODE 5: Database Fundamentals
        # =====================================================================
        {
            "title": "Database Fundamentals",
            "slug": "database-fundamentals",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 140,
            "content": """# Database Fundamentals

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor databaser ar viktigt |
|----------|----------------------------|
| **Persistence** | Permanent datalagring |
| **Performance** | Query optimization |
| **Scaling** | Hantera tillvaxt |
| **Backup** | Disaster recovery |
| **Compliance** | Data governance |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## SQL vs NoSQL

```
SQL DATABASES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
  │   Users     │    │   Orders    │    │  Products   │
  ├─────────────┤    ├─────────────┤    ├─────────────┤
  │ id          │───>│ user_id     │    │ id          │
  │ name        │    │ product_id  │<───│ name        │
  │ email       │    │ quantity    │    │ price       │
  └─────────────┘    └─────────────┘    └─────────────┘

  + ACID compliance
  + Relationella queries
  + Schema enforcement
  - Svart att skala horisontellt

  Exempel: PostgreSQL, MySQL, Oracle

NoSQL DATABASES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Document Store:           Key-Value:
  ┌───────────────────┐    ┌────────────────────┐
  │ {                 │    │ "user:123" -> data │
  │   "_id": "123",   │    │ "session:abc" -> {}│
  │   "name": "Anna", │    └────────────────────┘
  │   "orders": [...]│
  │ }                 │    Wide Column:
  └───────────────────┘    ┌────────────────────┐
                           │ Row -> Column Fam  │
  Graph:                   │      -> Columns    │
  (User)--[BOUGHT]->(Prod) └────────────────────┘

  + Flexibelt schema
  + Horisontell skalning
  - Eventual consistency (ofta)

  Exempel: MongoDB, Redis, Cassandra, Neo4j
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ACID Properties

```
A - ATOMICITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Allt eller inget"

Transaction:
1. Debit account A  -$100  ┐
2. Credit account B +$100  ┘ Bada eller ingen

C - CONSISTENCY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Fran ett giltigt state till ett annat"

Before: Total = $1000
After:  Total = $1000 (fortfarande)

I - ISOLATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Transaktioner ser inte varandras mellantillstand"

T1: Read balance -> $100
T2: Read balance -> $100 (inte T1:s ocommittade -$50)

D - DURABILITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Committade transaktioner overlever krasch"

COMMIT; <-- Skrivet till disk/log
[SERVER CRASH]
[RESTART] <-- Data finns kvar
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Indexering

```
UTAN INDEX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SELECT * FROM users WHERE email = 'a@b.com'

Soks igenom ALLA rader: O(n)
1000000 rader = 1000000 jamforelser

MED INDEX (B-Tree)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                  [M]
                 /   \\
              [F]     [S]
             / \\     / \\
          [A-E] [G-L] [N-R] [T-Z]

Binary search: O(log n)
1000000 rader = ~20 jamforelser

Index Types:
- B-Tree: Default, bra for ranges
- Hash: Exakt match, snabbare
- Full-text: Sokning i text
- Composite: Flera kolumner
```

### Index Best Practices

```sql
-- Bra: Index pa ofta sokta kolumner
CREATE INDEX idx_users_email ON users(email);

-- Bra: Composite for multi-column queries
CREATE INDEX idx_orders_user_date
ON orders(user_id, created_at);

-- Undvik: For manga index (slower writes)
-- Undvik: Index pa lag-selektivitet kolumner
-- Undvik: Index pa kolumner som andras ofta
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Normalisering

```
ONORMALISERAT (Redundans)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Orders:
┌────────────────────────────────────────────┐
│ order_id │ customer_name │ customer_email  │
├──────────┼───────────────┼─────────────────┤
│ 1        │ Anna          │ anna@mail.com   │
│ 2        │ Anna          │ anna@mail.com   │ DUBLETT
│ 3        │ Anna          │ anna@mail.com   │ DUBLETT
└────────────────────────────────────────────┘

NORMALISERAT (3NF)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Customers:              Orders:
┌──────────────────┐   ┌───────────────────┐
│ id │ name │email │   │ id │ customer_id  │
├────┼──────┼──────┤   ├────┼──────────────┤
│ 1  │ Anna │a@... │   │ 1  │ 1            │
└──────────────────┘   │ 2  │ 1            │
                       │ 3  │ 1            │
                       └───────────────────┘

+ Ingen redundans
+ Enklare uppdateringar
- Mer JOINs
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Database Val

| Anvandning | Rekommenderad DB |
|------------|------------------|
| **OLTP** | PostgreSQL, MySQL |
| **Analytics** | ClickHouse, BigQuery |
| **Caching** | Redis |
| **Documents** | MongoDB |
| **Time-series** | TimescaleDB, InfluxDB |
| **Graph** | Neo4j |
| **Search** | Elasticsearch |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Slow queries | Missing index | EXPLAIN + add index |
| Connection exhaustion | Pooling saknas | Use connection pool |
| N+1 queries | ORM lazy load | Eager loading / JOIN |
| Deadlocks | Lock contention | Consistent ordering |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **SQL** | ACID, relationer, schema |
| **NoSQL** | Flexibilitet, skalning |
| **Index** | Kritiskt for performance |
| **ACID** | Garantier for transaktioner |

**Kom ihag:**
- Valj databas efter use case
- Index ar gratis for reads, kostar for writes
- EXPLAIN ar din basta van
- PostgreSQL ar oftast ratt val att borja med
"""
        },
        # =====================================================================
        # NODE 6: Database Replication
        # =====================================================================
        {
            "title": "Database Replication",
            "slug": "database-replication",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 140,
            "content": """# Database Replication

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor replication ar viktigt |
|----------|------------------------------|
| **High Availability** | Failover vid krasch |
| **Read Scaling** | Fordela lasningar |
| **Geo-distribution** | Narmare anvandare |
| **Backup** | Point-in-time recovery |
| **Analytics** | Separata read replicas |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Master-Slave (Primary-Replica)

```
┌──────────────────────────────────────────────────────────┐
│              MASTER-SLAVE REPLICATION                    │
└──────────────────────────────────────────────────────────┘

                     ┌─────────────┐
     Writes ────────>│   MASTER    │
                     │  (Primary)  │
                     └──────┬──────┘
                            │
              Replication   │   (async/sync)
                            │
            ┌───────────────┼───────────────┐
            │               │               │
            v               v               v
      ┌──────────┐    ┌──────────┐    ┌──────────┐
      │  SLAVE   │    │  SLAVE   │    │  SLAVE   │
      │ Replica 1│    │ Replica 2│    │ Replica 3│
      └────┬─────┘    └────┬─────┘    └────┬─────┘
           │               │               │
           └───────────────┼───────────────┘
                           │
                        Reads

+ Enkelt att forsta
+ Bra read scaling
- Single point of failure (master)
- Write bottleneck
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Master-Master (Multi-Master)

```
┌──────────────────────────────────────────────────────────┐
│              MASTER-MASTER REPLICATION                   │
└──────────────────────────────────────────────────────────┘

     Writes/Reads              Writes/Reads
          │                         │
          v                         v
    ┌──────────┐              ┌──────────┐
    │ MASTER 1 │<────────────>│ MASTER 2 │
    │          │  Bi-dir      │          │
    └──────────┘  Replication └──────────┘

+ Ingen single point of failure
+ Write scaling
- Konflikthantering komplex
- Eventual consistency risk
```

### Konflikthantering

```
Problem: Samma rad uppdateras pa bada masters

Master 1: UPDATE users SET name='Anna' WHERE id=1
Master 2: UPDATE users SET name='Erik' WHERE id=1

Losningar:
1. Last Write Wins (timestamp)
2. Application-level conflict resolution
3. Konflikt-fria CRDT datastrukturer
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Synchronous vs Asynchronous

```
SYNCHRONOUS REPLICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Client ──> Master ──> Replica ──> ACK ──> Master ──> Client
                                   │
                      Vantar pa bekraftelse

+ Ingen data loss
+ Stark konsistens
- Hogre latency
- Replika-problem paverkar writes

ASYNCHRONOUS REPLICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Client ──> Master ──> Client (returnerar direkt)
               │
               └──> Replica (i bakgrunden)

+ Lag latency
+ Replika-problem paverkar ej writes
- Mojlig data loss vid krasch
- Replication lag
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Replication Lag

```
┌──────────────────────────────────────────────────────────┐
│                 REPLICATION LAG                          │
└──────────────────────────────────────────────────────────┘

Timeline:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
t=0     Master: INSERT user (id=1, name='Anna')
t=0     Client: "Success!"
t=0.5   Replica: (not yet received)
t=0.5   Client: SELECT * FROM users WHERE id=1
        -> Reads from replica -> "User not found!"
t=1     Replica: INSERT user (id=1, name='Anna')
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Losningar:
1. Read-your-writes: Las fran master efter write
2. Monotonic reads: Samma replika per session
3. Synchronous replication (for kritisk data)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Failover Strategier

```
AUTOMATIC FAILOVER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

      ┌──────────┐
      │  Master  │ <── Health check fails!
      │   [X]    │
      └──────────┘
           │
           │ Sentinel/Orchestrator detects
           v
      ┌──────────┐
      │ Replica  │ ─── Promoted to Master
      │   [OK]   │
      └──────────┘
           │
           v
      Other replicas reconfigured

MANUAL FAILOVER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. DBA detects issue
2. Stops writes to old master
3. Promotes replica
4. Updates connection strings
5. Resumes operations
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Replication

| Databas | Replication Typ |
|---------|-----------------|
| **PostgreSQL** | Streaming (sync/async) |
| **MySQL** | Binlog, GTID |
| **MongoDB** | Replica Sets |
| **Redis** | Async, Sentinel |
| **CockroachDB** | Raft consensus |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Replication lag | Slow replica | Tune eller upgrade |
| Split brain | Network partition | Quorum/fencing |
| Data loss | Async + master crash | Sync for kritisk data |
| Stale reads | Lag | Read-your-writes |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Master-Slave** | Enkel read scaling |
| **Sync vs Async** | Consistency vs latency |
| **Lag** | Planera for det |
| **Failover** | Automatisera om mojligt |

**Kom ihag:**
- Replication ar inte backup
- Monitor replication lag aktivt
- Test failover regelbundet
- Read-your-writes for kritiska floden
"""
        },
        # =====================================================================
        # NODE 7: Database Sharding
        # =====================================================================
        {
            "title": "Database Sharding",
            "slug": "database-sharding",
            "difficulty": "advanced",
            "estimated_minutes": 55,
            "xp_reward": 150,
            "content": """# Database Sharding

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor sharding ar viktigt |
|----------|---------------------------|
| **Write Scaling** | Distribuera writes |
| **Data Volume** | For stor for en server |
| **Performance** | Parallella queries |
| **Isolation** | Tenant-separation |
| **Compliance** | Data residency |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Sharding?

```
┌──────────────────────────────────────────────────────────┐
│                 SINGLE DATABASE                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │ Users Table: 100 million rows                      │ │
│  │ All on ONE server                                  │ │
│  │ [SLOW QUERIES, STORAGE LIMIT, BOTTLENECK]         │ │
│  └────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘

                         │
                         │ Sharding
                         v

┌──────────────────────────────────────────────────────────┐
│                  SHARDED DATABASE                        │
│                                                          │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐     │
│  │   Shard 1    │ │   Shard 2    │ │   Shard 3    │     │
│  │  Users A-H   │ │  Users I-P   │ │  Users Q-Z   │     │
│  │  33M rows    │ │  33M rows    │ │  34M rows    │     │
│  └──────────────┘ └──────────────┘ └──────────────┘     │
│                                                          │
│  [PARALLEL QUERIES, DISTRIBUTED, SCALABLE]              │
└──────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Sharding Strategier

### Range-Based Sharding

```
RANGE-BASED SHARDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Shard Key: user_id

┌─────────────────────────────────────────────────────────┐
│ user_id 1-1000000       -> Shard 1                      │
│ user_id 1000001-2000000 -> Shard 2                      │
│ user_id 2000001-3000000 -> Shard 3                      │
└─────────────────────────────────────────────────────────┘

+ Enkelt att implementera
+ Range queries effektiva
- Hotspots (nya users alltid pa sista shard)
- Ojamn distribution over tid
```

### Hash-Based Sharding

```
HASH-BASED SHARDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

shard_id = hash(user_id) % num_shards

user_id=12345 -> hash(12345) % 3 = 1 -> Shard 1
user_id=67890 -> hash(67890) % 3 = 0 -> Shard 0
user_id=11111 -> hash(11111) % 3 = 2 -> Shard 2

+ Jamn distribution
+ Undviker hotspots
- Range queries ineffektiva
- Resharding ar komplext
```

### Directory-Based Sharding

```
DIRECTORY-BASED SHARDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌───────────────────────────────────┐
│          LOOKUP SERVICE           │
├───────────────────────────────────┤
│ tenant_id │ shard_location        │
├───────────┼───────────────────────┤
│ acme      │ shard-eu-1            │
│ globex    │ shard-us-1            │
│ initech   │ shard-eu-2            │
└───────────┴───────────────────────┘

+ Flexibel mapping
+ Enkel resharding
- Extra lookup latency
- Lookup service = SPOF
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Shard Key Val

```
BRA SHARD KEYS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Hog kardinalitet (manga unika varden)
- Jamn distribution
- Anvands i de flesta queries
- Immutable (andras aldrig)

Exempel:
- tenant_id (multi-tenant SaaS)
- user_id (user-centric app)
- region (geo-distribution)

DALIGA SHARD KEYS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Lag kardinalitet (status: active/inactive)
- Monotonically increasing (timestamp)
- Frequently updated columns
- Nullable columns
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cross-Shard Queries

```
PROBLEM: Query som behover data fran flera shards

SELECT * FROM orders WHERE status = 'pending'

        ┌──────────┐
        │  Router  │
        └────┬─────┘
             │
   ┌─────────┼─────────┐
   v         v         v
┌──────┐ ┌──────┐ ┌──────┐
│Shard1│ │Shard2│ │Shard3│
│ 100  │ │  50  │ │  75  │
└──────┘ └──────┘ └──────┘
   │         │         │
   └─────────┼─────────┘
             v
      Merge: 225 results

LOSNINGAR:
1. Scatter-Gather: Query alla shards, merge resultat
2. Denormalisering: Kopiera data till varje shard
3. Global Tables: Replicated reference data
4. Application-level joins
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Resharding

```
NAR: Shard blir for stor eller ojamn distribution

BEFORE:                    AFTER:
┌────────┐ ┌────────┐     ┌────────┐ ┌────────┐ ┌────────┐
│Shard 1 │ │Shard 2 │     │Shard 1 │ │Shard 2 │ │Shard 3 │
│ 70%    │ │ 30%    │ --> │ 35%    │ │ 30%    │ │ 35%    │
└────────┘ └────────┘     └────────┘ └────────┘ └────────┘

STRATEGIER:
1. Double-write under migration
2. Background data copy
3. Consistent hashing (minimerar flytt)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Sharding Solutions

| Databas | Sharding Support |
|---------|------------------|
| **MongoDB** | Native sharding |
| **Vitess** | MySQL sharding layer |
| **CockroachDB** | Automatic sharding |
| **Citus** | PostgreSQL extension |
| **Cassandra** | Native partitioning |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Hotspot | Dalig shard key | Byt till hash-based |
| Slow queries | Cross-shard | Denormalisera |
| Uneven shards | Growth pattern | Resharding |
| Complex joins | Distributed data | Application joins |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Shard Key** | Viktigaste beslutet |
| **Hash** | Bast for jamn distribution |
| **Range** | Bra for range queries |
| **Komplexitet** | Undvik om mojligt |

**Kom ihag:**
- Sharda inte for tidigt (premature optimization)
- Shard key kan inte andras latt
- Cross-shard queries ar dyra
- Overvag managed solutions (Vitess, CockroachDB)
"""
        },
        # =====================================================================
        # NODE 8: CAP Theorem
        # =====================================================================
        {
            "title": "CAP Theorem",
            "slug": "cap-theorem",
            "difficulty": "advanced",
            "estimated_minutes": 45,
            "xp_reward": 140,
            "content": """# CAP Theorem

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor CAP ar viktigt |
|----------|----------------------|
| **Arkitekturbeslut** | Valj ratt tradeoffs |
| **Databasval** | Forsta begransningar |
| **Failure modes** | Planera for partitions |
| **SLA design** | Ratt forvantan |
| **Systemforstaelse** | Distributed systems |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## De tre egenskaperna

```
┌──────────────────────────────────────────────────────────┐
│                    CAP THEOREM                           │
│                                                          │
│        C - Consistency (Konsistens)                      │
│        A - Availability (Tillganglighet)                 │
│        P - Partition Tolerance (Partitionstolerans)      │
│                                                          │
│  "Du kan bara valja TVA av tre i ett distribuerat system"│
└──────────────────────────────────────────────────────────┘

                      C
                     /\\
                    /  \\
                   /    \\
                  / CP   \\
                 /        \\
                /    CA    \\
               /____________\\
              P              A
                    AP
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## C - Consistency

```
CONSISTENCY (Linearizability)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Alla noder ser samma data vid samma tidpunkt.

    Client A: WRITE x=5 ──> Node 1

         Node 1 ────── sync ────── Node 2
         x=5                       x=5

    Client B: READ x ──> Node 2
    Result: x=5 (alltid samma som senaste write)

STARKT KONSISTENT:
- Alla lasningar returnerar senaste skrivning
- Ingen stale data
- "Som en enda dator"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## A - Availability

```
AVAILABILITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Varje request far ett svar (success eller failure).

    Client ──> Request ──> System ──> Response
                             │
                     Aldrig "no response"
                     Alltid svar inom rimlig tid

HOGT TILLGANGLIGT:
- 99.99% uptime
- Alltid svarar
- Kan vara stale data
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## P - Partition Tolerance

```
PARTITION TOLERANCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Systemet fortsatter fungera trots natverkspartitioner.

    ┌──────────────┐          ┌──────────────┐
    │    Node 1    │    X     │    Node 2    │
    │              │<--//-->  │              │
    │   Region A   │  Network │   Region B   │
    └──────────────┘ Partition└──────────────┘

PARTITION TOLERANT:
- Hanterar natverksfel
- Distribuerade system MASTE ha detta
- Fragor: Vad gor vi nar partition uppstar?
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CAP Kombinationer

```
┌──────────────────────────────────────────────────────────┐
│  CP - CONSISTENCY + PARTITION TOLERANCE                  │
├──────────────────────────────────────────────────────────┤
│  Vid partition: Vissa requests nekas (unavailable)       │
│  Garanti: Data alltid konsistent                        │
│                                                          │
│  Exempel: MongoDB (i vissa configs), HBase, Redis       │
│  Use case: Bank transaktioner, inventory                │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│  AP - AVAILABILITY + PARTITION TOLERANCE                 │
├──────────────────────────────────────────────────────────┤
│  Vid partition: Svarar alltid, men data kan vara stale  │
│  Garanti: System alltid tillgangligt                    │
│                                                          │
│  Exempel: Cassandra, DynamoDB, CouchDB                  │
│  Use case: Social media feeds, shopping carts           │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│  CA - CONSISTENCY + AVAILABILITY                         │
├──────────────────────────────────────────────────────────┤
│  Endast mojligt utan partitioner (single node)          │
│  I praktiken: Distribuerade system MASTE ha P           │
│                                                          │
│  Exempel: Single-node PostgreSQL, MySQL                 │
│  Use case: Smarre applikationer                         │
└──────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Partition Scenario

```
SCENARIO: Network partition mellan datacenters

             BEFORE PARTITION
             ━━━━━━━━━━━━━━━━
    ┌────────────┐     ┌────────────┐
    │ Datacenter │<--->│ Datacenter │
    │     A      │sync │     B      │
    │   x=100    │     │   x=100    │
    └────────────┘     └────────────┘

             PARTITION OCCURS
             ━━━━━━━━━━━━━━━━
    ┌────────────┐  X  ┌────────────┐
    │ Datacenter │     │ Datacenter │
    │     A      │     │     B      │
    └────────────┘     └────────────┘

Client A writes x=200 to DC A
Client B writes x=300 to DC B

             CP CHOICE:
             ━━━━━━━━━━
    DC A: Accept write (x=200)
    DC B: REJECT write (unavailable)
    Result: Konsistent men ej fullt tillganglig

             AP CHOICE:
             ━━━━━━━━━━
    DC A: Accept write (x=200)
    DC B: Accept write (x=300)
    Result: Tillgangligt men konflikt uppstar
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## PACELC - Utokad modell

```
┌──────────────────────────────────────────────────────────┐
│  PACELC: Mer nyanserad an CAP                           │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  if (Partition) {                                        │
│      choose: Availability OR Consistency                 │
│  } else {                                                │
│      choose: Latency OR Consistency                      │
│  }                                                       │
│                                                          │
│  PA/EL: Availability vid partition, Latency normalt     │
│         (Cassandra, DynamoDB)                           │
│                                                          │
│  PC/EC: Consistency alltid                              │
│         (MongoDB, HBase)                                │
│                                                          │
│  PA/EC: Availability vid partition, Consistency normalt │
│         (Yahoo PNUTS)                                   │
└──────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Databaser och CAP

| Databas | CAP | PACELC |
|---------|-----|--------|
| **PostgreSQL** | CA (single) | PC/EC |
| **MongoDB** | CP | PC/EC |
| **Cassandra** | AP | PA/EL |
| **DynamoDB** | AP | PA/EL |
| **Redis Cluster** | CP | PC/EC |
| **CockroachDB** | CP | PC/EC |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Split brain | Partition utan quorum | Fencing, quorum |
| Stale reads | AP system | Tunable consistency |
| Unavailability | CP under partition | Failover strategy |
| Data conflicts | AP writes | CRDT, last-write-wins |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **P ar obligatoriskt** | Natverksfel hander |
| **CP vs AP** | Beror pa use case |
| **Tunable** | Manga DBs later dig valja |
| **PACELC** | Mer praktisk modell |

**Kom ihag:**
- CAP ar ett spectrum, inte binart
- Valj CP for pengar/kritisk data
- Valj AP for UX/tillganglighet
- "Eventual consistency" ar okej for mycket
"""
        },
        # =====================================================================
        # NODE 9: Message Queues
        # =====================================================================
        {
            "title": "Message Queues",
            "slug": "message-queues",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 130,
            "content": """# Message Queues

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor message queues ar viktigt |
|----------|----------------------------------|
| **Decoupling** | Loskopp producers/consumers |
| **Async** | Icke-blockerande operationer |
| **Buffering** | Hantera trafiktoppar |
| **Reliability** | Garanterad leverans |
| **Scaling** | Oberoende skalning |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundkoncept

```
SYNCHRONOUS (Utan queue)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User ──> API ──> Email Service ──> Response
              │
              └── Vantar pa email att skickas (slow!)

ASYNCHRONOUS (Med queue)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User ──> API ──> Queue ──> Response (snabbt!)
                   │
                   └──> Email Worker ──> Skickar email
                        (i bakgrunden)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Queue Arkitektur

```
┌──────────────────────────────────────────────────────────┐
│               MESSAGE QUEUE ARCHITECTURE                 │
└──────────────────────────────────────────────────────────┘

  ┌──────────┐    ┌──────────────────────┐    ┌──────────┐
  │ Producer │───>│       QUEUE          │───>│ Consumer │
  │          │    │  ┌──┬──┬──┬──┬──┐   │    │          │
  │ Service A│    │  │M1│M2│M3│M4│M5│   │    │ Worker 1 │
  └──────────┘    │  └──┴──┴──┴──┴──┘   │    └──────────┘
                  │                      │
  ┌──────────┐    │  FIFO (vanligtvis)   │    ┌──────────┐
  │ Producer │───>│                      │───>│ Consumer │
  │          │    └──────────────────────┘    │          │
  │ Service B│                                │ Worker 2 │
  └──────────┘                                └──────────┘

Producer: Skickar meddelanden
Queue: Lagrar meddelanden
Consumer: Processerar meddelanden
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Point-to-Point vs Pub/Sub

```
POINT-TO-POINT (Queue)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Producer ──> [Queue] ──> Consumer
                 │
    Meddelande tas bort efter konsumtion
    EN consumer per meddelande

PUB/SUB (Topic)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    ┌──> Subscriber A
Publisher ──> Topic─┼──> Subscriber B
                    └──> Subscriber C
                 │
    Meddelande levereras till ALLA subscribers
    MANGA consumers per meddelande
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Delivery Guarantees

```
AT-MOST-ONCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Producer ──> Queue ──> Consumer
              │
    Meddelandet KAN forsvinna
    Ingen retry

Use case: Metrics, logs (ok att tappa nagra)

AT-LEAST-ONCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Producer ──> Queue ──> Consumer ──> ACK
              │           │
              └───────────┘ Retry om ingen ACK

    Meddelandet KAN levereras flera ganger
    Consumer maste vara idempotent!

Use case: De flesta fall (payments, orders)

EXACTLY-ONCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Svart att uppna i distribuerade system
    Kraver transaktioner + deduplication

Use case: Finansiella transaktioner
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dead Letter Queue

```
┌──────────────────────────────────────────────────────────┐
│               DEAD LETTER QUEUE (DLQ)                    │
└──────────────────────────────────────────────────────────┘

                                    ┌─────────────────┐
                    Fail x 3        │  Dead Letter    │
                 ┌─────────────────>│     Queue       │
                 │                  │                 │
┌─────────┐    ┌─┴───────┐        └────────┬────────┘
│ Queue   │───>│ Consumer │                 │
└─────────┘    └─────────┘                  v
                                    Manual inspection
                                    or alerting

DLQ anvands for:
- Felaktiga meddelanden
- Poison pills
- Retry-exhausted messages
- Debugging och analys
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Consumer Patterns

```
COMPETING CONSUMERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

       ┌─────────┐
       │Consumer1│◄──┐
       └─────────┘   │
                     │
┌─────────┐   ┌──────┴──────┐
│ Queue   │──>│ Load Balance│
└─────────┘   └──────┬──────┘
                     │
       ┌─────────┐   │
       │Consumer2│◄──┘
       └─────────┘

+ Horisontell skalning
+ Fel-tolerant

CONSUMER GROUPS (Kafka)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Topic Partitions:
┌──────┐ ┌──────┐ ┌──────┐
│ P0   │ │ P1   │ │ P2   │
└───┬──┘ └───┬──┘ └───┬──┘
    │        │        │
    v        v        v
┌──────┐ ┌──────┐ ┌──────┐
│ C0   │ │ C1   │ │ C2   │
└──────┘ └──────┘ └──────┘
  Consumer Group A
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Queue Teknologier

| Teknologi | Typ | Anvandning |
|-----------|-----|------------|
| **RabbitMQ** | Traditional | Task queues, RPC |
| **Kafka** | Log-based | Event streaming |
| **AWS SQS** | Managed | Simple queuing |
| **Redis** | In-memory | Fast pub/sub |
| **NATS** | Lightweight | Microservices |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Lost messages | At-most-once | At-least-once + ACK |
| Duplicates | Retry | Idempotent consumers |
| Queue buildup | Slow consumer | Scale consumers |
| Poison messages | Bad data | DLQ + validation |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Decoupling** | Huvudsyfte |
| **Durability** | Persistera viktiga msg |
| **Idempotency** | Kritiskt for consumers |
| **DLQ** | Alltid konfigurera |

**Kom ihag:**
- Kafka for event streaming, RabbitMQ for tasks
- At-least-once + idempotency ar ofta bast
- Monitor queue depth aktivt
- DLQ ar kritisk for debugging
"""
        },
        # =====================================================================
        # NODE 10: CDN & Edge Computing
        # =====================================================================
        {
            "title": "CDN & Edge Computing",
            "slug": "cdn-edge",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 120,
            "content": """# CDN & Edge Computing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor CDN ar viktigt |
|----------|----------------------|
| **Latency** | Content narmare user |
| **Performance** | Snabbare laddningstid |
| **Availability** | Global redundans |
| **DDoS** | Edge absorption |
| **Kostnad** | Minska origin load |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar en CDN?

```
UTAN CDN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User i Tokyo ────────────────────> Origin i Stockholm
                 200ms RTT
                 Alla requests gar till origin

MED CDN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                          ┌─────────────────┐
                          │  Origin Server  │
                          │   Stockholm     │
                          └────────┬────────┘
                                   │
               Cache miss          │
          ┌────────────────────────┴──────────────────────┐
          │                        │                      │
    ┌─────┴─────┐           ┌──────┴──────┐        ┌──────┴──────┐
    │ Edge PoP  │           │  Edge PoP   │        │  Edge PoP   │
    │   Tokyo   │           │   London    │        │  New York   │
    └─────┬─────┘           └─────────────┘        └─────────────┘
          │ 20ms
          │ Cache hit
    ┌─────┴─────┐
    │   User    │
    │   Tokyo   │
    └───────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CDN Caching

```
REQUEST FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. User requests: https://cdn.example.com/image.jpg

2. DNS resolves to nearest edge

3. Edge checks cache:
   ┌────────────────────────────────────────┐
   │  CACHE HIT?                            │
   ├────────────────────────────────────────┤
   │  YES: Return cached content (fast!)    │
   │  NO:  Fetch from origin, cache, return │
   └────────────────────────────────────────┘

CACHE HEADERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cache-Control: max-age=86400        # Cache 1 dag
Cache-Control: s-maxage=3600        # CDN cache 1 timme
Cache-Control: no-cache             # Validera varje gang
Cache-Control: no-store             # Aldrig cacha
ETag: "abc123"                      # Version for validation
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Push vs Pull CDN

```
PULL CDN (Origin Pull)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Request ──> Edge (cache miss) ──> Origin
                │
            Cachar svaret
                │
Request ──> Edge (cache hit) ──> Return

+ Automatiskt
+ Enkelt att konfigurera
- Forsta request ar langsammare

PUSH CDN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Deploy: Upload content to ALL edges

┌────────┐    Push    ┌────────┐
│ Origin │ ──────────>│ Edge 1 │
│        │ ──────────>│ Edge 2 │
│        │ ──────────>│ Edge 3 │
└────────┘            └────────┘

+ Ingen cold start
+ Full kontroll
- Manuell hantering
- Mer komplext
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Edge Computing

```
TRADITIONAL: Compute at origin
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User ──> CDN (static only) ──> Origin (all logic)
                                    │
                              200ms latency

EDGE COMPUTING: Compute at edge
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                   ┌──────────────────┐
User ──> CDN Edge ─┤ Run code here!   │
          20ms     │ - A/B testing    │
                   │ - Auth           │
                   │ - Personalization│
                   │ - API routing    │
                   └──────────────────┘

EDGE FUNCTIONS (Cloudflare Workers, Vercel Edge)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

// Runs at edge, not origin
export default {
  async fetch(request) {
    const country = request.cf.country
    if (country === 'SE') {
      return Response.redirect('/sv')
    }
    return fetch(request)
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cache Invalidation

```
STRATEGIER FOR INVALIDERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. TTL-based (vanta ut)
   Cache-Control: max-age=3600
   + Enkelt
   - Kan visa gammal data

2. Purge (rensa manuellt)
   curl -X PURGE https://cdn.example.com/image.jpg
   + Omedelbar uppdatering
   - Kraver API-anrop

3. Cache Tags (gruppera)
   Surrogate-Key: product-123 category-shoes
   Purge alla med tag: product-123
   + Flexibelt
   + Effektivt

4. Versioned URLs (cache busting)
   /styles.v123.css  -->  /styles.v124.css
   + Omedelbar
   + Enkel
   - Kraver URL-andringar
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - CDN Providers

| Provider | Edge Functions | Use Case |
|----------|----------------|----------|
| **Cloudflare** | Workers | General, free tier |
| **AWS CloudFront** | Lambda@Edge | AWS ecosystem |
| **Vercel** | Edge Functions | Next.js, frontend |
| **Fastly** | Compute@Edge | High performance |
| **Akamai** | EdgeWorkers | Enterprise |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Stale content | For lang TTL | Kortare TTL eller purge |
| Cache miss storm | TTL sync | Staggered expiration |
| Origin overload | Cache bypass | Check headers |
| Wrong region | DNS config | Anycast eller geo-routing |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Static** | CDN for allt statiskt |
| **TTL** | Balansera freshness |
| **Edge** | Flytta logik narmare |
| **Headers** | Cache-Control ar nyckeln |

**Kom ihag:**
- CDN ar nastan alltid ratt val
- Set Cache-Control headers korrekt
- Edge functions for latency-kritisk logik
- Monitor cache hit ratio (mal: over 90%)
"""
        },
        # =====================================================================
        # NODE 11: API Design
        # =====================================================================
        {
            "title": "API Design",
            "slug": "api-design",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 130,
            "content": """# API Design

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor API design ar viktigt |
|----------|------------------------------|
| **Integration** | Service-kommunikation |
| **Skalning** | Efficient data transfer |
| **Versioning** | Backward compatibility |
| **DX** | Developer experience |
| **Security** | Auth och authorization |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## REST API Principles

```
REST FUNDAMENTALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Resources (substantiv, inte verb):
  /users          (inte /getUsers)
  /users/123      (inte /getUserById)
  /users/123/orders

HTTP Methods:
  GET     - Las data (idempotent)
  POST    - Skapa ny resurs
  PUT     - Ersatt hela resursen
  PATCH   - Delvis uppdatering
  DELETE  - Ta bort resurs

STATUS CODES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2xx - Success
  200 OK           - GET success
  201 Created      - POST success
  204 No Content   - DELETE success

4xx - Client Error
  400 Bad Request  - Invalid input
  401 Unauthorized - Not authenticated
  403 Forbidden    - Not authorized
  404 Not Found    - Resource missing
  422 Unprocessable- Validation error

5xx - Server Error
  500 Internal     - Server fel
  502 Bad Gateway  - Upstream error
  503 Unavailable  - Overloaded
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## REST API Exempel

```
CRUD OPERATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Lista alla users
GET /api/v1/users
Response: 200 OK
{
  "data": [{"id": 1, "name": "Anna"}, ...],
  "meta": {"total": 100, "page": 1}
}

# Hamta en user
GET /api/v1/users/123
Response: 200 OK
{"id": 123, "name": "Anna", "email": "anna@ex.com"}

# Skapa user
POST /api/v1/users
Body: {"name": "Erik", "email": "erik@ex.com"}
Response: 201 Created
{"id": 124, "name": "Erik", ...}

# Uppdatera user
PATCH /api/v1/users/123
Body: {"name": "Anna K"}
Response: 200 OK

# Ta bort user
DELETE /api/v1/users/123
Response: 204 No Content
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GraphQL

```
┌──────────────────────────────────────────────────────────┐
│                     GRAPHQL                              │
├──────────────────────────────────────────────────────────┤
│  + Klienten bestammer vilken data                       │
│  + En endpoint for allt                                 │
│  + Starkt typat schema                                  │
│  - Komplexare implementation                            │
│  - Caching mer utmanande                               │
└──────────────────────────────────────────────────────────┘

REST: Multiple endpoints, fixed response
GET /users/123         -> {id, name, email, address, ...}
GET /users/123/orders  -> [{...}, {...}]

GraphQL: One endpoint, flexible response
POST /graphql
{
  query {
    user(id: 123) {
      name
      orders {
        id
        total
      }
    }
  }
}

Response:
{
  "data": {
    "user": {
      "name": "Anna",
      "orders": [
        {"id": 1, "total": 100}
      ]
    }
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## gRPC

```
┌──────────────────────────────────────────────────────────┐
│                       gRPC                               │
├──────────────────────────────────────────────────────────┤
│  + Hog performance (binary, HTTP/2)                     │
│  + Stark typing med Protocol Buffers                    │
│  + Bidirectional streaming                              │
│  - Svarare att debugga                                  │
│  - Begransat browserstod                                │
└──────────────────────────────────────────────────────────┘

Protocol Buffer definition:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

syntax = "proto3";

service UserService {
  rpc GetUser(GetUserRequest) returns (User);
  rpc ListUsers(ListRequest) returns (stream User);
}

message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}

USE CASES:
- Microservice-to-microservice
- Real-time streaming
- Performance-critical APIs
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## API Versioning

```
URL PATH (rekommenderas)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/api/v1/users
/api/v2/users

+ Tydligt och explicit
+ Enkelt att implementera
- URL andras vid ny version

HEADER-BASED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Accept: application/vnd.api+json; version=2

+ Renare URLs
- Svarare att testa

QUERY PARAMETER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/api/users?version=2

+ Enkelt att testa
- Mindre REST-ful
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pagination

```
OFFSET-BASED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GET /users?limit=20&offset=40

+ Enkelt
+ Kan hoppa till sida
- Slow vid stora offset (OFFSET 10000)
- Inconsistent vid inserts

CURSOR-BASED (rekommenderas)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GET /users?limit=20&cursor=eyJpZCI6MTIzfQ==

Response:
{
  "data": [...],
  "pagination": {
    "next_cursor": "eyJpZCI6MTQzfQ==",
    "has_more": true
  }
}

+ Konsistent resultat
+ Effektiv (index-based)
- Kan inte hoppa till sida
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - API Val

| Anvandning | Protokoll |
|------------|-----------|
| **Public API** | REST |
| **Mobile apps** | GraphQL |
| **Microservices** | gRPC |
| **Real-time** | WebSocket, gRPC |
| **Internal** | gRPC eller REST |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| N+1 queries | Overfetching | Include/expand param |
| Breaking changes | Ingen versioning | Version fran start |
| Slow pagination | OFFSET | Cursor-based |
| Over-fetching | Fixed responses | GraphQL eller sparse |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **REST** | Standard for de flesta fall |
| **Versioning** | Gor det fran borjan |
| **Pagination** | Cursor for skalning |
| **Status codes** | Anvand korrekt |

**Kom ihag:**
- Konsistens ar viktigare an "perfect"
- Dokumentera med OpenAPI/Swagger
- Cursor-pagination for stora datasets
- gRPC for intern microservice-kommunikation
"""
        },
        # =====================================================================
        # NODE 12: Microservices Architecture
        # =====================================================================
        {
            "title": "Microservices Architecture",
            "slug": "microservices",
            "difficulty": "advanced",
            "estimated_minutes": 60,
            "xp_reward": 160,
            "content": """# Microservices Architecture

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor microservices ar viktigt |
|----------|--------------------------------|
| **Skalning** | Skala tjanster individuellt |
| **Deploy** | Oberoende deployments |
| **Teams** | Team ownership |
| **Resilience** | Isolerade failures |
| **Tech diversity** | Ratt verktyg per tjanst |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Monolith vs Microservices

```
MONOLITH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────────────────────────────────────┐
│              MONOLITH                    │
├──────────────────────────────────────────┤
│  ┌────────┐ ┌────────┐ ┌────────┐       │
│  │  UI    │ │ Orders │ │ Users  │       │
│  └────────┘ └────────┘ └────────┘       │
│  ┌────────┐ ┌────────┐ ┌────────┐       │
│  │Payments│ │Inventory│ │Shipping│       │
│  └────────┘ └────────┘ └────────┘       │
│                                          │
│  ┌──────────────────────────────────┐   │
│  │         SHARED DATABASE          │   │
│  └──────────────────────────────────┘   │
└──────────────────────────────────────────┘

+ Enkel development och deploy
+ Enkel debugging
- En deploy for allt
- Scaling: allt eller inget
- Tech lock-in

MICROSERVICES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌────────┐   ┌────────┐   ┌────────┐   ┌─────────┐
│ Orders │   │ Users  │   │Payments│   │Inventory│
│Service │   │Service │   │Service │   │ Service │
└───┬────┘   └───┬────┘   └───┬────┘   └────┬────┘
    │            │            │             │
┌───┴────┐   ┌───┴────┐   ┌───┴────┐   ┌────┴────┐
│   DB   │   │   DB   │   │   DB   │   │   DB    │
└────────┘   └────────┘   └────────┘   └─────────┘

+ Oberoende deploy
+ Individuell skalning
+ Tech flexibility
- Komplexare ops
- Distributed debugging
- Network latency
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Service Communication

```
SYNCHRONOUS (Request/Response)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Order Service ──HTTP/gRPC──> User Service
      │                           │
      └──────── Response ─────────┘

+ Enkelt att forsta
+ Omedelbart svar
- Tight coupling
- Latency kedja

ASYNCHRONOUS (Event-Driven)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Order Service ──> Message Queue ──> User Service
                                ──> Email Service
                                ──> Analytics

+ Loskopp tjansterna
+ Resilient
- Eventual consistency
- Mer komplext
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## API Gateway

```
┌──────────────────────────────────────────────────────────┐
│                      API GATEWAY                         │
└──────────────────────────────────────────────────────────┘

                    ┌────────────────────┐
     Clients ──────>│    API Gateway     │
                    ├────────────────────┤
                    │ - Authentication   │
                    │ - Rate limiting    │
                    │ - Request routing  │
                    │ - Load balancing   │
                    │ - SSL termination  │
                    └─────────┬──────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         v                    v                    v
    ┌─────────┐         ┌─────────┐         ┌─────────┐
    │ Orders  │         │  Users  │         │ Products│
    │ Service │         │ Service │         │ Service │
    └─────────┘         └─────────┘         └─────────┘

Exempel: Kong, AWS API Gateway, Nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Database per Service

```
SHARED DATABASE (anti-pattern)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────┐  ┌─────────┐  ┌─────────┐
│Service A│  │Service B│  │Service C│
└────┬────┘  └────┬────┘  └────┬────┘
     │            │            │
     └────────────┼────────────┘
                  v
          ┌─────────────┐
          │ Shared DB   │  <-- TIGHT COUPLING!
          └─────────────┘

DATABASE PER SERVICE (best practice)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────┐  ┌─────────┐  ┌─────────┐
│Service A│  │Service B│  │Service C│
└────┬────┘  └────┬────┘  └────┬────┘
     │            │            │
     v            v            v
┌─────────┐  ┌─────────┐  ┌─────────┐
│  DB A   │  │  DB B   │  │  DB C   │
└─────────┘  └─────────┘  └─────────┘

+ Oberoende schema evolution
+ Ratt databas for varje tjanst
- Data duplication
- Distributed transactions
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Saga Pattern

```
PROBLEM: Distribuerade transaktioner

Order koper:
1. Reserve inventory
2. Charge payment
3. Update order status

Vad hander om steg 2 failar efter steg 1?

SAGA: Kompenserade transaktioner
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Success path:
Reserve ──> Charge ──> Update ──> Complete

Failure at Charge:
Reserve ──> Charge (FAIL)
    │
    └── Compensate: Release reservation

┌────────────────────────────────────────────────────────┐
│  T1          T2          T3                            │
│  Reserve --> Charge --> Update                         │
│                                                        │
│  C1          C2          C3                            │
│  Release <-- Refund <-- Rollback (compensations)      │
└────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Circuit Breaker

```
┌──────────────────────────────────────────────────────────┐
│               CIRCUIT BREAKER PATTERN                    │
└──────────────────────────────────────────────────────────┘

         ┌─────────┐
         │ CLOSED  │ Normal operation
         └────┬────┘ Requests go through
              │
     Failures exceed threshold
              │
              v
         ┌─────────┐
         │  OPEN   │ Fast fail
         └────┬────┘ No requests sent
              │
     Timeout expires
              │
              v
         ┌─────────┐
         │HALF-OPEN│ Test requests
         └────┬────┘
              │
    Success?──┼──Failure?
      │       │        │
      v       │        v
   CLOSED     │      OPEN

Forhindrar kaskadfel!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Microservices Tools

| Kategori | Verktyg |
|----------|---------|
| **Container** | Docker, Kubernetes |
| **Gateway** | Kong, Nginx, Traefik |
| **Service Mesh** | Istio, Linkerd |
| **Observability** | Jaeger, Prometheus |
| **Messaging** | Kafka, RabbitMQ |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Distributed monolith | Tight coupling | Event-driven, async |
| Cascade failures | No isolation | Circuit breaker |
| Data inconsistency | Shared DB | Database per service |
| Debugging nightmare | No tracing | Distributed tracing |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Start small** | Borja med monolith |
| **Bounded context** | Tydliga granser |
| **Async** | Prefer events over sync |
| **Observability** | Masten fran dag 1 |

**Kom ihag:**
- "Microservices are not free lunch"
- Borja med monolith, bryt ut nar nodvandigt
- Varje tjanst = eget team
- Investera i observability tidigt
"""
        },
        # =====================================================================
        # NODE 13: Service Discovery
        # =====================================================================
        {
            "title": "Service Discovery",
            "slug": "service-discovery",
            "difficulty": "advanced",
            "estimated_minutes": 45,
            "xp_reward": 130,
            "content": """# Service Discovery

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor service discovery ar viktigt |
|----------|-------------------------------------|
| **Dynamic IPs** | Containrar andrar adresser |
| **Auto-scaling** | Nya instanser dyker upp |
| **Failover** | Hitta friska instanser |
| **Load balancing** | Fordela over instanser |
| **Decoupling** | Hardkoda ej adresser |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Problemet

```
UTAN SERVICE DISCOVERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

config.yaml:
  user_service: http://10.0.0.5:8080
  order_service: http://10.0.0.6:8080
  payment_service: http://10.0.0.7:8080

Problem:
- Vad hander nar user_service flyttar?
- Vad hander nar vi skalar till 3 instanser?
- Manuell konfiguppdatering = downtime!

MED SERVICE DISCOVERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

config.yaml:
  user_service: user-service  # Logiskt namn!

Service registry hanterar mapping:
  user-service -> [10.0.0.5:8080, 10.0.0.8:8080, 10.0.0.9:8080]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Client-Side vs Server-Side

```
CLIENT-SIDE DISCOVERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌────────┐   1. Query    ┌──────────────┐
│ Client │──────────────>│   Service    │
│        │               │   Registry   │
│        │<──────────────│              │
└───┬────┘   2. Return   └──────────────┘
    │        addresses
    │
    │ 3. Direct call
    v
┌──────────┐
│ Service  │
│ Instance │
└──────────┘

+ Klienten valjer instans
+ Flexibel load balancing
- Klientlogik mer komplex
- Varje sprak behover impl

SERVER-SIDE DISCOVERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌────────┐              ┌───────────────┐
│ Client │─────────────>│ Load Balancer │
│        │              │   /Router     │
└────────┘              └───────┬───────┘
                                │
           ┌────────────────────┼────────────────────┐
           │                    │                    │
           v                    v                    v
     ┌──────────┐         ┌──────────┐         ┌──────────┐
     │Instance 1│         │Instance 2│         │Instance 3│
     └──────────┘         └──────────┘         └──────────┘

+ Enklare klienter
+ Centraliserad logik
- Extra hopp (latency)
- LB kan bli flaskhals
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Service Registration

```
SELF-REGISTRATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────┐  1. Register  ┌──────────────┐
│ Service  │──────────────>│   Service    │
│ Instance │               │   Registry   │
└──────────┘               └──────────────┘

Service startup:
1. Service startar
2. Registrerar sig med namn och adress
3. Skickar heartbeats
4. Avregistrerar vid shutdown

THIRD-PARTY REGISTRATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────┐               ┌──────────────┐
│ Service  │               │   Service    │
│ Instance │               │   Registry   │
└──────────┘               └──────┬───────┘
      │                           │
      │ Watch                     │
      v                           │
┌──────────────┐                  │
│  Registrar   │──────────────────┘
│ (K8s, Consul)│   Register/Deregister
└──────────────┘

Kubernetes gor detta automatiskt!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## DNS-Based Discovery

```
KUBERNETES DNS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Service name: user-service
Namespace: default

DNS: user-service.default.svc.cluster.local

┌────────────┐    DNS Query     ┌─────────────┐
│   Pod A    │─────────────────>│  Kube-DNS   │
│            │                  │             │
│            │<─────────────────│             │
└────────────┘   10.96.0.100    └─────────────┘

Requests till user-service:
  http://user-service:8080/api/users

+ Enkelt
+ Inbyggt i Kubernetes
- Inga health checks i basic DNS
- TTL caching issues
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Health Checking

```
┌──────────────────────────────────────────────────────────┐
│               HEALTH CHECK FLOW                          │
└──────────────────────────────────────────────────────────┘

Service Registry
      │
      │ Health check varje 10s
      v
┌──────────┐  GET /health  ┌──────────┐
│ Registry │──────────────>│ Instance │
│          │               │          │
│          │<──────────────│          │
└──────────┘   200 OK      └──────────┘

Health Status:
- HEALTHY: Receives traffic
- UNHEALTHY: Removed from pool
- DRAINING: No new connections

Health Endpoint:
GET /health
{
  "status": "healthy",
  "checks": {
    "database": "ok",
    "redis": "ok",
    "disk": "ok"
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Service Discovery Tools

| Verktyg | Typ | Platform |
|---------|-----|----------|
| **Consul** | Full-featured | Multi-platform |
| **etcd** | Key-value | Kubernetes base |
| **Eureka** | Netflix OSS | Java/Spring |
| **Kubernetes** | Native | K8s only |
| **AWS Cloud Map** | Managed | AWS |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Stale endpoints | Ingen health check | Active health checks |
| Registry down | SPOF | HA registry cluster |
| DNS caching | Stale IPs | Short TTL |
| Slow startup | Registrar innan ready | Readiness probe |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Dynamiskt** | Hardkoda aldrig IPs |
| **Health checks** | Kritiskt for reliability |
| **Kubernetes** | Inbyggd discovery |
| **DNS** | Enklast for de flesta |

**Kom ihag:**
- Kubernetes Services loser de flesta behov
- Consul for mer avancerade scenarios
- Readiness probes viktiga for graceful startup
- Service mesh (Istio) for komplex discovery
"""
        },
        # =====================================================================
        # NODE 14: Rate Limiting & Throttling
        # =====================================================================
        {
            "title": "Rate Limiting & Throttling",
            "slug": "rate-limiting",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 120,
            "content": """# Rate Limiting & Throttling

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor rate limiting ar viktigt |
|----------|--------------------------------|
| **DDoS** | Skydda mot angrepp |
| **Abuse** | Forhindra missbruk |
| **Fairness** | Jamn resursfordelning |
| **Cost** | Begransar cloud-kostnader |
| **Stability** | Forhindra overbelastning |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Rate Limit vs Throttling

```
RATE LIMITING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Max 100 requests per minut"

Request 1-100:  [OK]
Request 101:    [DENIED - 429 Too Many Requests]

Avvisar requests over gransen

THROTTLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Max 10 requests per sekund, koar resten"

Request 1-10:   [Processed immediately]
Request 11-20:  [Queued, processed later]

Saktar ner istallet for att avvisa
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Token Bucket Algorithm

```
TOKEN BUCKET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────┐
│                                                         │
│     Tokens added at fixed rate (e.g., 10/second)       │
│                      │                                  │
│                      v                                  │
│            ┌─────────────────┐                         │
│            │     BUCKET      │  Max capacity: 100      │
│            │  ● ● ● ● ● ● ●  │                         │
│            │  ● ● ● ● ● ● ●  │  Current: 14 tokens    │
│            └────────┬────────┘                         │
│                     │                                  │
│                     v                                  │
│                 Request arrives                        │
│                     │                                  │
│         Token available? ─── No ──> REJECT (429)      │
│              │                                         │
│             Yes                                        │
│              │                                         │
│              v                                         │
│         Remove token                                   │
│         Process request                                │
│                                                         │
└─────────────────────────────────────────────────────────┘

+ Tillater bursts (upp till bucket size)
+ Smooth long-term rate
+ Enkel implementation
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Leaky Bucket Algorithm

```
LEAKY BUCKET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────┐
│                                                         │
│              Requests added to bucket                   │
│                      │                                  │
│                      v                                  │
│            ┌─────────────────┐                         │
│            │     BUCKET      │  If full: REJECT       │
│            │  R R R R R R R  │                         │
│            │  R R R R R R R  │                         │
│            └────────┬────────┘                         │
│                     │ Fixed rate leak                  │
│                     │ (e.g., 10/second)               │
│                     v                                  │
│                 Process                                │
│                                                         │
└─────────────────────────────────────────────────────────┘

+ Jamn output rate
+ Forutsagbar belastning
- Ingen burst tolerance
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Fixed Window vs Sliding Window

```
FIXED WINDOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Timeline:
|-------- Window 1 --------|-------- Window 2 --------|
0:00                      1:00                      2:00

Limit: 100 requests per window

Problem: Burst vid window-grans
|              90 requests |100 requests              |
           0:59           1:00           1:01

190 requests pa 2 sekunder!

SLIDING WINDOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Request at 1:30:
  Count = (requests 0:30-1:00) * 0.5 + (requests 1:00-1:30)

        ┌─────────────────────────────────┐
        │      Rolling 60s window         │
        │<───────────────────────────────>│
        └─────────────────────────────────┘
       0:30                              1:30

+ Ingen burst vid granser
- Mer komplex att implementera
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Rate Limit Headers

```
HTTP RESPONSE HEADERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HTTP/1.1 200 OK
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1623456789

eller standard (RFC draft):
RateLimit-Limit: 100
RateLimit-Remaining: 45
RateLimit-Reset: 60

429 TOO MANY REQUESTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HTTP/1.1 429 Too Many Requests
Retry-After: 30
Content-Type: application/json

{
  "error": "rate_limit_exceeded",
  "message": "Too many requests",
  "retry_after": 30
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Rate Limiting Strategies

```
BY USER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
key = user_id
limit = 1000/hour per user

BY IP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
key = client_ip
limit = 100/minute per IP

Problem: NAT, proxies (manga users = samma IP)

BY API KEY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
key = api_key
limit = varies by plan

Free: 100/day
Pro: 10000/day
Enterprise: unlimited

BY ENDPOINT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
/api/search: 10/minute (expensive)
/api/users: 100/minute (cheap)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Distributed Rate Limiting

```
┌──────────────────────────────────────────────────────────┐
│              DISTRIBUTED RATE LIMITING                   │
└──────────────────────────────────────────────────────────┘

Problem: Flera API servers

     ┌──────────┐
     │ Client   │
     └────┬─────┘
          │
     ┌────┴─────┐
     │    LB    │
     └────┬─────┘
          │
  ┌───────┼───────┐
  v       v       v
┌───┐   ┌───┐   ┌───┐
│S1 │   │S2 │   │S3 │   <-- Varje har lokal counter?
└───┘   └───┘   └───┘

Losning: Centralized store (Redis)

┌───┐   ┌───┐   ┌───┐
│S1 │   │S2 │   │S3 │
└─┬─┘   └─┬─┘   └─┬─┘
  │       │       │
  └───────┼───────┘
          v
    ┌──────────┐
    │  Redis   │  <-- Single source of truth
    │ (INCR)   │
    └──────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Rate Limiting Tools

| Verktyg | Anvandning |
|---------|------------|
| **Redis** | Counter storage |
| **Nginx** | Limit req module |
| **Kong** | API Gateway plugin |
| **AWS WAF** | Rate-based rules |
| **Cloudflare** | Edge rate limiting |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Burst at window | Fixed window | Sliding window |
| Redis SPOF | Single instance | Redis cluster |
| IP limit unfair | NAT/shared IP | User-based limits |
| Missing headers | No info to client | Add rate headers |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Token bucket** | Bast for de flesta |
| **Sliding window** | Jamn fordelning |
| **Headers** | Informera klienten |
| **Distributed** | Redis for shared state |

**Kom ihag:**
- Alltid inkludera rate limit headers
- 429 med Retry-After ar standard
- Token bucket for burst tolerance
- Redis INCR for distributed counting
"""
        },
        # =====================================================================
        # NODE 15: Distributed Systems
        # =====================================================================
        {
            "title": "Distributed Systems",
            "slug": "distributed-systems",
            "difficulty": "advanced",
            "estimated_minutes": 60,
            "xp_reward": 170,
            "content": """# Distributed Systems

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor distribuerade system ar viktigt |
|----------|---------------------------------------|
| **Scale** | En server racker inte |
| **Reliability** | Redundans mot failures |
| **Latency** | Geografisk distribution |
| **Availability** | 99.99% uptime |
| **Modern apps** | Cloud-native ar distributed |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## The Eight Fallacies

```
DE ATTA VILLFARELSERNA OM DISTRIBUERADE SYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Natverket ar pålitligt          <- DET AR DET INTE
2. Latency ar noll                 <- DET AR DET INTE
3. Bandwidth ar oandlig            <- DET AR DET INTE
4. Natverket ar sakert             <- DET AR DET INTE
5. Topologin andras aldrig         <- DET GOR DEN
6. Det finns en administrator      <- DET GOR DET INTE
7. Transport-kostnad ar noll       <- DET AR DET INTE
8. Natverket ar homogent           <- DET AR DET INTE

Konsekvens:
- Planera for failures
- Implementera retries och timeouts
- Designa for eventual consistency
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Distributed System Challenges

```
┌──────────────────────────────────────────────────────────┐
│              FUNDAMENTAL CHALLENGES                      │
└──────────────────────────────────────────────────────────┘

1. PARTIAL FAILURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Vissa delar kan failar medan andra fungerar

   ┌──────┐     ┌──────┐     ┌──────┐
   │Node A│     │Node B│     │Node C│
   │  OK  │     │ FAIL │     │  OK  │
   └──────┘     └──────┘     └──────┘

2. NETWORK PARTITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Noder kan inte kommunicera

   [Node A] ──X──X──X── [Node B]
        Network failure

3. CLOCK SYNCHRONIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Varje nod har sin egen klocka

   Node A: 10:00:00.000
   Node B: 10:00:00.003  <- 3ms difference
   Node C: 09:59:59.998  <- 2ms behind

   Vem hande forst?
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Consensus Algorithms

```
PROBLEMET: Hur enas flera noder om ett varde?

┌──────┐  ┌──────┐  ┌──────┐
│Node A│  │Node B│  │Node C│
│ v=5  │  │ v=7  │  │ v=5  │
└──────┘  └──────┘  └──────┘

Vilket varde ar "sant"?

PAXOS/RAFT: Consensus protocols
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RAFT Roles:
┌─────────────────────────────────────────────────────────┐
│  LEADER: En nod som koordinerar                        │
│  FOLLOWER: Replikerar ledarens beslut                  │
│  CANDIDATE: Vill bli leader                            │
└─────────────────────────────────────────────────────────┘

     ┌──────────┐
     │  LEADER  │
     │ (Node A) │
     └────┬─────┘
          │ Append entries
    ┌─────┴─────┐
    v           v
┌──────┐    ┌──────┐
│FOLLOW│    │FOLLOW│
│Node B│    │Node C│
└──────┘    └──────┘

Quorum: Majoritet maste vara overens (2 av 3)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Timeouts and Retries

```
TIMEOUT STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

            Request
Client ───────────────> Server
   │                       │
   │ Timeout: 5 seconds    │
   │<──────────────────────│ Response
   │                       │
   │ If no response:       │
   │ - Retry?              │
   │ - Fail?               │
   │ - Fallback?           │

RETRY WITH EXPONENTIAL BACKOFF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Attempt 1: Wait 1 second
Attempt 2: Wait 2 seconds
Attempt 3: Wait 4 seconds
Attempt 4: Wait 8 seconds
Attempt 5: Give up

def retry_with_backoff(func, max_retries=5):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception:
            if attempt == max_retries - 1:
                raise
            sleep(2 ** attempt)  # Exponential backoff

+ JITTER (randomness)
sleep(2 ** attempt + random(0, 1000)ms)
Undvik thundering herd
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Idempotency

```
PROBLEMET: Retry kan orsaka dubbletter

Request: "Skapa order"
    │
    v
[Server skapar order] ──> Response forsvinner
    │
    │ Client timeout, retry
    v
[Server skapar SAMMA order igen] <- DABBEL ORDER!

LOSNING: Idempotency key
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

POST /orders
Idempotency-Key: abc-123-xyz
{
  "product": "widget",
  "quantity": 1
}

Server:
1. Check if key exists in cache
2. If exists: Return cached response
3. If not: Process, store result with key

+ Samma request = samma resultat
+ Safe to retry
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Distributed Transactions

```
TWO-PHASE COMMIT (2PC)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 1: PREPARE
┌─────────────┐    "Can you commit?"
│ Coordinator │───────────────────>┌──────────┐
│             │                    │Participant│
│             │<───────────────────│           │
└─────────────┘    "Yes/No"        └──────────┘

Phase 2: COMMIT/ABORT
┌─────────────┐    "Commit!" (if all yes)
│ Coordinator │───────────────────>┌──────────┐
│             │    "Abort!" (if any no)
└─────────────┘                    └──────────┘

Problem: Coordinator failure = stuck transactions

SAGA PATTERN (better for microservices)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

T1 ──> T2 ──> T3 ──> Success!
 │      │      │
 C1 <── C2 <── C3   (Compensations if failure)

+ No distributed locks
+ Better availability
- Eventual consistency
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Distributed Systems Tools

| Verktyg | Anvandning |
|---------|------------|
| **etcd** | Distributed KV, consensus |
| **ZooKeeper** | Coordination, config |
| **Consul** | Service mesh, discovery |
| **Redis Cluster** | Distributed cache |
| **Kafka** | Distributed messaging |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Cascade failure | No isolation | Circuit breaker |
| Split brain | Network partition | Quorum, fencing |
| Duplicate processing | Retry | Idempotency keys |
| Clock skew | Different clocks | Vector clocks, NTP |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Failures** | Planera for dem |
| **Idempotency** | Gor allt idempotent |
| **Timeouts** | Alltid med exponential backoff |
| **Consensus** | Raft/etcd for coordination |

**Kom ihag:**
- Allt kan och kommer att faila
- Natverk ar opålitligt
- Idempotency ar din basta van
- Embrace eventual consistency
"""
        },
        # =====================================================================
        # NODE 16: Consistency Patterns
        # =====================================================================
        {
            "title": "Consistency Patterns",
            "slug": "consistency-patterns",
            "difficulty": "advanced",
            "estimated_minutes": 50,
            "xp_reward": 150,
            "content": """# Consistency Patterns

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor consistency patterns ar viktigt |
|----------|---------------------------------------|
| **Korrekthet** | Data som stammer |
| **UX** | Vad anvandare ser |
| **Debugging** | Forsta beteende |
| **Trade-offs** | Prestanda vs korrekthet |
| **Architecture** | Systemdesign beslut |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Consistency Spectrum

```
┌──────────────────────────────────────────────────────────┐
│              CONSISTENCY SPECTRUM                        │
└──────────────────────────────────────────────────────────┘

STRONG                                              EVENTUAL
  │                                                      │
  │  Linearizable  Sequential  Causal    Eventual       │
  │      │             │          │          │          │
  ├──────┼─────────────┼──────────┼──────────┼──────────┤
  │                                                      │
  │  Hogre latency                     Lagre latency    │
  │  Lagre tillganglighet              Hogre tillg.     │
  │  Enklare att resonera              Mer komplext     │
  │                                                      │
└──────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Strong Consistency

```
LINEARIZABILITY (Starkaste)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Alla operationer verkar ske vid en atomisk punkt i tiden.

Timeline:
─────────────────────────────────────────────────────────>

Client A: ───WRITE x=1─────────────────────────────────>
                    │
                    │ (write completes)
                    │
Client B: ─────────────READ x──────────────────────────>
                         │
                         └── MUST return 1

Garantier:
- Alla ser samma ordning
- Lasningar returnerar senaste write
- Som en enda dator

Anvandning: Bank transaktioner, inventory
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Eventual Consistency

```
EVENTUAL CONSISTENCY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Om inga nya writes gor, kommer alla replikor
 TILL SLUT returnera samma varde"

Timeline:
─────────────────────────────────────────────────────────>

t=0   Write x=1 to Node A
      Node A: x=1
      Node B: x=0 (stale)
      Node C: x=0 (stale)

t=100ms  Replication
         Node A: x=1
         Node B: x=1
         Node C: x=0 (still replicating)

t=200ms  All synced
         Node A: x=1
         Node B: x=1
         Node C: x=1

Under 0-200ms kan olika klienter se olika varden!

Anvandning: Social media feeds, likes, counters
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Read-Your-Writes

```
READ-YOUR-WRITES CONSISTENCY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Garanti: En klient ser alltid sina egna skrivningar

┌──────────────────────────────────────────────────────────┐
│                                                          │
│  Client A:  WRITE profile="Anna" ──> Node 1             │
│             READ profile ──> Node 2                      │
│                    │                                     │
│             Should return "Anna"!                        │
│                                                          │
└──────────────────────────────────────────────────────────┘

Implementation:
1. Sticky sessions (alltid samma replica)
2. Read from master after write
3. Inkludera write timestamp, las fran updated replica

Anvandning: User profile updates, settings
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Monotonic Reads

```
MONOTONIC READS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Garanti: Om en klient last varde v, ser den aldrig ett
         tidigare varde i efterfoljande lasningar

UTAN MONOTONIC READS:
─────────────────────────────────────────────────────────>

Read 1 (Node B): x=5
Read 2 (Node A): x=3  <- OLDER VALUE! Confusing!
Read 3 (Node B): x=5

"Tiden gar baklanges" for anvandaren

MED MONOTONIC READS:
─────────────────────────────────────────────────────────>

Read 1 (Node B): x=5
Read 2 (Node A): x=5  <- Same or newer
Read 3 (Node C): x=7  <- Newer is OK

Implementation: Session affinity, version tracking
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Causal Consistency

```
CAUSAL CONSISTENCY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Operationer som ar kausalt relaterade ses i ratt ordning.

Exempel: Kommentarer

User A: Posts comment "Hello"
User B: Replies "Hi there!" (to User A's comment)

KAUSALT KORREKT:
  "Hello"          (visas forst)
  └── "Hi there!"  (visas efter)

KAUSALT INKORREKT:
  "Hi there!"  <- Svar till vad?
  "Hello"

Implementation: Vector clocks, causal timestamps

Vector Clock Example:
{A: 1, B: 0}  "Hello"
{A: 1, B: 1}  "Hi there!" (knows about A:1)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Quorum

```
QUORUM: N/W/R
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

N = Total replicas
W = Write quorum (replicas that must ACK write)
R = Read quorum (replicas to read from)

Rule: W + R > N  (garanterar overlap)

EXAMPLE: N=3, W=2, R=2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write x=5:
┌──────┐ ┌──────┐ ┌──────┐
│ R1   │ │ R2   │ │ R3   │
│ x=5  │ │ x=5  │ │ x=?  │ (2 of 3 ACK = success)
│ ACK  │ │ ACK  │ │      │
└──────┘ └──────┘ └──────┘

Read x:
┌──────┐ ┌──────┐
│ R1   │ │ R3   │  Read from 2 replicas
│ x=5  │ │ x=?  │  At least one has x=5
└──────┘ └──────┘  Return x=5

CONFIGURATIONS:
N=3, W=3, R=1: Strong consistency (slow writes)
N=3, W=1, R=3: Fast writes, slow reads
N=3, W=2, R=2: Balanced
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Consistency Levels

| Pattern | Use Case | Trade-off |
|---------|----------|-----------|
| **Strong** | Bank, inventory | High latency |
| **Eventual** | Feeds, likes | Stale reads |
| **Read-your-writes** | User profile | Session sticky |
| **Causal** | Comments, chat | Complexity |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Stale reads | Eventual consistency | Read-your-writes |
| Time travel | No monotonic reads | Session affinity |
| Lost updates | Concurrent writes | Optimistic locking |
| Split brain | Partition | Quorum |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Trade-off** | Consistency vs availability |
| **Eventual** | OK for de flesta fall |
| **Strong** | For pengar och kritisk data |
| **Quorum** | W+R > N for consistency |

**Kom ihag:**
- Valj consistency level per operation
- Eventual ar ofta okej med bra UX
- Read-your-writes loser manga problem
- Quorum ger tunable consistency
"""
        },
        # =====================================================================
        # NODE 17: Event-Driven Architecture
        # =====================================================================
        {
            "title": "Event-Driven Architecture",
            "slug": "event-driven",
            "difficulty": "advanced",
            "estimated_minutes": 55,
            "xp_reward": 160,
            "content": """# Event-Driven Architecture

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor EDA ar viktigt |
|----------|----------------------|
| **Decoupling** | Oberoende tjanster |
| **Scalability** | Asynkron processing |
| **Resilience** | Felhantering |
| **Real-time** | Omedelbar reaktion |
| **Audit** | Komplett historik |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Request-Driven vs Event-Driven

```
REQUEST-DRIVEN (Synchronous)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User ──> Order Service ──> Inventory ──> Payment ──> Email
              │                │            │          │
              └────────────────┴────────────┴──────────┘
                        Waits for all to complete

- Tight coupling
- Slow (chain of calls)
- One failure = all fail

EVENT-DRIVEN (Asynchronous)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User ──> Order Service ──> "OrderCreated" event
              │
              └──> Returns immediately!

         Event Bus
            │
     ┌──────┼──────┐──────┐
     v      v      v      v
Inventory Payment Email Analytics
 Service  Service Service Service

+ Loose coupling
+ Fast response
+ Independent failures
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Event Types

```
┌──────────────────────────────────────────────────────────┐
│                    EVENT TYPES                           │
└──────────────────────────────────────────────────────────┘

1. DOMAIN EVENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Affarshandelser som har skett

   OrderCreated { orderId, customerId, items, total }
   PaymentReceived { paymentId, orderId, amount }
   UserRegistered { userId, email, timestamp }

2. INTEGRATION EVENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   For kommunikation mellan bounded contexts

   InventoryReserved { orderId, items }
   ShipmentDispatched { orderId, trackingId }

3. NOTIFICATION EVENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   "Nagot hande, om nagon bryr sig"

   PriceChanged { productId, oldPrice, newPrice }
   StockLow { productId, quantity }
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Event Sourcing

```
TRADITIONAL: Store current state
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Account Table:
┌────────────┬─────────┐
│ account_id │ balance │
├────────────┼─────────┤
│ 123        │ 500     │  <- Only current state
└────────────┴─────────┘

EVENT SOURCING: Store events
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Event Store:
┌────────────┬──────────────────┬────────┐
│ account_id │ event            │ amount │
├────────────┼──────────────────┼────────┤
│ 123        │ AccountCreated   │ 0      │
│ 123        │ MoneyDeposited   │ 1000   │
│ 123        │ MoneyWithdrawn   │ -300   │
│ 123        │ MoneyWithdrawn   │ -200   │
└────────────┴──────────────────┴────────┘

Current balance = replay all events = 500

+ Komplett historik
+ Audit trail
+ Temporal queries
- Mer komplex
- Storage
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CQRS

```
CQRS: Command Query Responsibility Segregation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Separera writes (commands) fran reads (queries)

          ┌────────────────────────────────────┐
          │            API Gateway             │
          └──────────────┬─────────────────────┘
                         │
            ┌────────────┴────────────┐
            │                         │
            v                         v
    ┌───────────────┐        ┌───────────────┐
    │   COMMAND     │        │    QUERY      │
    │   SERVICE     │        │   SERVICE     │
    │               │        │               │
    │ CreateOrder   │        │ GetOrders     │
    │ UpdateOrder   │        │ SearchOrders  │
    └───────┬───────┘        └───────┬───────┘
            │                        │
            v                        v
    ┌───────────────┐        ┌───────────────┐
    │  Write DB     │───────>│   Read DB     │
    │  (normalized) │ events │ (denormalized)│
    └───────────────┘        └───────────────┘

+ Optimerad for varje use case
+ Separat skalning
- Eventual consistency mellan DBs
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Event-Driven Patterns

```
CHOREOGRAPHY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tjanster reagerar pa events, ingen central koordinator

Order ──"OrderCreated"──> Event Bus
                             │
              ┌──────────────┼──────────────┐
              v              v              v
          Inventory      Payment        Email
          "ItemsReserved" "PaymentDone" "EmailSent"

+ Loskopplat
- Svart att se hela flodet

ORCHESTRATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Central orchestrator styr flodet

         ┌─────────────────┐
         │   Orchestrator  │
         │  (Saga Manager) │
         └────────┬────────┘
                  │
    ┌─────────────┼─────────────┐
    v             v             v
Inventory     Payment       Email
    │             │             │
    └─────────────┴─────────────┘
          Reports back

+ Tydligt flode
- Central koordinator
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Event Schema

```
EVENT STRUCTURE (CloudEvents)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "specversion": "1.0",
  "id": "uuid-123",
  "source": "order-service",
  "type": "com.example.OrderCreated",
  "time": "2024-01-15T10:30:00Z",
  "datacontenttype": "application/json",
  "data": {
    "orderId": "order-456",
    "customerId": "cust-789",
    "items": [...],
    "total": 199.99
  }
}

SCHEMA EVOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Add fields (backward compatible)
- Deprecate, don't remove
- Use schema registry (Avro, Protobuf)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Event Tools

| Verktyg | Anvandning |
|---------|------------|
| **Kafka** | High-throughput streaming |
| **RabbitMQ** | Traditional messaging |
| **AWS EventBridge** | Serverless events |
| **NATS** | Lightweight pub/sub |
| **Redis Streams** | Simple event store |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Event ordering | Parallel consumers | Partition by key |
| Duplicate events | At-least-once | Idempotent handlers |
| Lost events | No persistence | Durable queues |
| Schema breaking | No versioning | Schema registry |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Events** | Fakta som har hant |
| **Decoupling** | Huvudfordel |
| **Idempotency** | Kritiskt for handlers |
| **Schema** | Planera for evolution |

**Kom ihag:**
- Events ar immutable (handa i datet)
- Handlers maste vara idempotenta
- Kafka for storskalig streaming
- Event sourcing ar kraftfullt men komplext
"""
        },
        # =====================================================================
        # NODE 18: Monitoring & Observability
        # =====================================================================
        {
            "title": "Monitoring & Observability",
            "slug": "monitoring-observability",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 140,
            "content": """# Monitoring & Observability

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor observability ar viktigt |
|----------|--------------------------------|
| **Debugging** | Hitta rotorsak |
| **Performance** | Identifiera flaskhalsar |
| **Proactive** | Upptack problem fore users |
| **SLAs** | Visa uppfyllnad |
| **Incidents** | Snabbare MTTR |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Three Pillars of Observability

```
┌──────────────────────────────────────────────────────────┐
│              THREE PILLARS                               │
└──────────────────────────────────────────────────────────┘

┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│    LOGS      │    │   METRICS    │    │   TRACES     │
│              │    │              │    │              │
│ What happened│    │ How much/many│    │ Request flow │
│ Discrete     │    │ Aggregated   │    │ Distributed  │
│ events       │    │ numbers      │    │ context      │
└──────────────┘    └──────────────┘    └──────────────┘

Together: Complete picture of system health
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Logs

```
LOG LEVELS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEBUG   -> Detaljerad info for debugging
INFO    -> Normala handelser
WARNING -> Potentiellt problem
ERROR   -> Fel som hindrar operation
FATAL   -> Systemet maste stoppas

STRUCTURED LOGGING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DALIGT:
"User 123 created order 456 for $99.99"

BRA (JSON):
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "INFO",
  "message": "Order created",
  "user_id": "123",
  "order_id": "456",
  "amount": 99.99,
  "trace_id": "abc-123-xyz"
}

+ Sokbart
+ Parseable
+ Korrelering med trace_id
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Metrics

```
METRIC TYPES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COUNTER: Okar bara (requests, errors)
┌──────────────────────────────────────┐
│  http_requests_total = 12345         │
│  ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲                 │
└──────────────────────────────────────┘

GAUGE: Kan oka/minska (temperature, queue size)
┌──────────────────────────────────────┐
│  memory_usage_bytes = 2.5GB          │
│  ─────────/\\────/\\───────           │
└──────────────────────────────────────┘

HISTOGRAM: Distribution (latency, sizes)
┌──────────────────────────────────────┐
│  request_duration_seconds            │
│  p50=0.1s, p90=0.5s, p99=1.2s       │
└──────────────────────────────────────┘

THE FOUR GOLDEN SIGNALS (Google SRE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. LATENCY    - How long requests take
2. TRAFFIC    - Requests per second
3. ERRORS     - Error rate
4. SATURATION - How "full" is the system
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Distributed Tracing

```
PROBLEM: Hur foljer jag ett request genom flera tjanster?

Request: GET /checkout
─────────────────────────────────────────────────────────>
API Gateway -> Order -> Inventory -> Payment -> Email

Var tog det 5 sekunder?

TRACING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Trace ID: abc-123 (samma genom hela kedjan)

┌─────────────────────────────────────────────────────────┐
│ Span: API Gateway (100ms)                               │
│  └─ Span: Order Service (2000ms)                       │
│      ├─ Span: Inventory (500ms)                        │
│      └─ Span: Payment (1400ms)  <- BOTTLENECK!         │
│          └─ Span: Email (50ms)                         │
└─────────────────────────────────────────────────────────┘

Headers:
traceparent: 00-abc123-def456-01
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Alerting

```
ALERT RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Prometheus alerting rule
- alert: HighErrorRate
  expr: rate(http_errors_total[5m]) > 0.1
  for: 5m
  labels:
    severity: critical
  annotations:
    summary: "High error rate detected"

ALERT FATIGUE PREVENTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Alert pa symptom, inte orsaker
- Ha actionable alerts
- Severity levels (page vs ticket)
- Dedup och grouping
- On-call rotation

┌────────────────────────────────────────────────────────┐
│  SYMPTOM-BASED ALERTING                                │
├────────────────────────────────────────────────────────┤
│  DALIGT: "CPU > 90%"  <- Kanske okej                  │
│  BRA: "Latency p99 > 2s" <- User-facing impact        │
└────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dashboards

```
DASHBOARD BEST PRACTICES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────┐
│  OVERVIEW DASHBOARD                                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │ Requests │ │  Errors  │ │ Latency  │ │   CPU    │  │
│  │  15K/s   │ │   0.1%   │ │  120ms   │ │   45%    │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│                                                         │
│  ┌────────────────────────────────────────────────────┐│
│  │  Request Rate Over Time                            ││
│  │  ────────────────/\\────────────────               ││
│  └────────────────────────────────────────────────────┘│
│                                                         │
│  USE Method: Utilization, Saturation, Errors          │
│  RED Method: Rate, Errors, Duration                   │
│                                                         │
└─────────────────────────────────────────────────────────┘

Hierarki:
1. Overview (hog niva)
2. Service-specific
3. Debug/deep-dive
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Observability Stack

| Kategori | Verktyg |
|----------|---------|
| **Metrics** | Prometheus, Datadog |
| **Logs** | Elasticsearch, Loki |
| **Traces** | Jaeger, Zipkin |
| **Dashboards** | Grafana |
| **APM** | New Relic, Datadog |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Alert fatigue | For manga alerts | Symptom-based |
| Slow debugging | Ingen tracing | Implement tracing |
| Missing context | Unstructured logs | Structured logging |
| Cardinality explosion | High-card labels | Label review |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Three pillars** | Logs, metrics, traces |
| **Golden signals** | Latency, traffic, errors, saturation |
| **Structured logs** | JSON, trace_id |
| **Actionable alerts** | Symptom-based |

**Kom ihag:**
- Observability fran dag 1
- Trace ID genom hela kedjan
- Alert pa user-facing symptoms
- Prometheus + Grafana ar standard
"""
        },
        # =====================================================================
        # NODE 19: Security in System Design
        # =====================================================================
        {
            "title": "Security in System Design",
            "slug": "security-design",
            "difficulty": "advanced",
            "estimated_minutes": 55,
            "xp_reward": 150,
            "content": """# Security in System Design

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor security design ar viktigt |
|----------|----------------------------------|
| **Data breaches** | Skydda anvandare |
| **Compliance** | GDPR, SOC2, HIPAA |
| **Trust** | Anvandarfortroende |
| **Cost** | Incidenter ar dyra |
| **Availability** | DDoS protection |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Defense in Depth

```
┌──────────────────────────────────────────────────────────┐
│              DEFENSE IN DEPTH                            │
└──────────────────────────────────────────────────────────┘

    Layer 1: PERIMETER
    ┌────────────────────────────────────────────────────┐
    │  WAF, DDoS Protection, CDN                         │
    │                                                    │
    │    Layer 2: NETWORK                                │
    │    ┌──────────────────────────────────────────┐   │
    │    │  Firewalls, VPCs, Security Groups        │   │
    │    │                                          │   │
    │    │    Layer 3: APPLICATION                  │   │
    │    │    ┌────────────────────────────────┐   │   │
    │    │    │  Auth, Input validation, HTTPS │   │   │
    │    │    │                                │   │   │
    │    │    │    Layer 4: DATA               │   │   │
    │    │    │    ┌────────────────────┐     │   │   │
    │    │    │    │ Encryption at rest │     │   │   │
    │    │    │    │ Access control     │     │   │   │
    │    │    │    └────────────────────┘     │   │   │
    │    │    └────────────────────────────────┘   │   │
    │    └──────────────────────────────────────────┘   │
    └────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Authentication

```
AUTHENTICATION METHODS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. PASSWORD + MFA
   User ──> Password ──> OTP/TOTP ──> Authenticated

2. OAUTH 2.0 / OIDC
   ┌────────┐     ┌───────────────┐     ┌────────┐
   │ Client │────>│ Auth Provider │────>│  API   │
   └────────┘     │ (Google/Okta) │     └────────┘
                  └───────────────┘
                       │
                  ID Token + Access Token

3. API KEYS
   GET /api/data
   X-API-Key: sk_live_abc123

JWT STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Header.Payload.Signature

{                          {
  "alg": "RS256",           "sub": "user123",
  "typ": "JWT"              "exp": 1623456789,
}                           "roles": ["admin"]
                          }

BASTA PRAXIS:
- Korta expiry (15 min access, longer refresh)
- RS256 over HS256 for distributed systems
- Inkludera aldrig secrets i payload
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Authorization

```
AUTHORIZATION MODELS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RBAC (Role-Based Access Control)
┌────────────────────────────────────────────────────────┐
│                                                        │
│  User ──> Role ──> Permissions                        │
│                                                        │
│  anna@ex.com ──> Admin ──> [read, write, delete]     │
│  erik@ex.com ──> Viewer ──> [read]                   │
│                                                        │
└────────────────────────────────────────────────────────┘

ABAC (Attribute-Based Access Control)
┌────────────────────────────────────────────────────────┐
│                                                        │
│  Policy: "user.department == resource.department"     │
│                                                        │
│  User {dept: "sales"} ──> Resource {dept: "sales"}   │
│  ALLOWED                                              │
│                                                        │
│  User {dept: "sales"} ──> Resource {dept: "eng"}     │
│  DENIED                                               │
│                                                        │
└────────────────────────────────────────────────────────┘

PRINCIPLE OF LEAST PRIVILEGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ge endast de permissions som behovs, inget mer.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Encryption

```
ENCRYPTION IN TRANSIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Client ══════ TLS 1.3 ══════> Server
       │                   │
       └── Encrypted ──────┘

- HTTPS everywhere
- TLS 1.3 minimum
- HSTS header
- Certificate pinning (mobile)

ENCRYPTION AT REST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────┐
│  DATABASE                                               │
│  ┌───────────────────────────────────────────────────┐ │
│  │ AES-256 encrypted                                 │ │
│  │ user_data: [encrypted blob]                       │ │
│  └───────────────────────────────────────────────────┘ │
│                                                         │
│  KEY MANAGEMENT                                         │
│  ┌───────────────────────────────────────────────────┐ │
│  │ AWS KMS / HashiCorp Vault / Azure Key Vault       │ │
│  │ Master key ──> Data keys (rotated)               │ │
│  └───────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Common Vulnerabilities

```
OWASP TOP 10 (simplified)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. INJECTION (SQL, NoSQL, LDAP)
   DALIGT: query = "SELECT * FROM users WHERE id=" + input
   BRA:    query = "SELECT * FROM users WHERE id=$1", [input]

2. BROKEN AUTHENTICATION
   - Svaga passwords
   - Ingen MFA
   - Session fixation

3. SENSITIVE DATA EXPOSURE
   - Loggar credentials
   - Okrypterad data
   - Exponerade API keys

4. XSS (Cross-Site Scripting)
   DALIGT: innerHTML = userInput
   BRA:    textContent = userInput (escaped)

5. BROKEN ACCESS CONTROL
   - IDOR (Insecure Direct Object Reference)
   GET /api/users/123/data  <- Ar jag user 123?
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Secrets Management

```
ALDRIG:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Hardcoded secrets i kod
- Secrets i git
- Okrypterade env files

ALLTID:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────┐
│  SECRETS MANAGEMENT                                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐                                      │
│  │ HashiCorp    │                                      │
│  │   Vault      │ ──> App fetches at runtime          │
│  └──────────────┘                                      │
│                                                         │
│  ┌──────────────┐                                      │
│  │  AWS Secrets │                                      │
│  │   Manager    │ ──> Injected as env vars            │
│  └──────────────┘                                      │
│                                                         │
│  ┌──────────────┐                                      │
│  │  K8s Secrets │                                      │
│  │  (encrypted) │ ──> Mounted as volume               │
│  └──────────────┘                                      │
│                                                         │
└─────────────────────────────────────────────────────────┘

Rotera secrets regelbundet!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Security Tools

| Kategori | Verktyg |
|----------|---------|
| **Secrets** | Vault, AWS Secrets Manager |
| **WAF** | Cloudflare, AWS WAF |
| **Scanning** | Snyk, SonarQube |
| **Auth** | Auth0, Okta, Keycloak |
| **Certificates** | Let's Encrypt, ACM |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| SQL injection | String concat | Parameterized queries |
| Leaked secrets | Git history | Vault + rotation |
| Broken auth | Weak passwords | MFA required |
| IDOR | No authz check | Resource-level authz |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Defense in depth** | Flera lager |
| **Least privilege** | Minimum nodvandigt |
| **Encrypt** | Transit och at-rest |
| **Secrets** | Aldrig hardcoded |

**Kom ihag:**
- Security ar allas ansvar
- Shift left (security tidigt)
- OWASP Top 10 ar minimum
- Rotera secrets regelbundet
"""
        },
        # =====================================================================
        # NODE 20: Real-World System Design Cases
        # =====================================================================
        {
            "title": "Real-World System Design Cases",
            "slug": "real-world-cases",
            "difficulty": "advanced",
            "estimated_minutes": 60,
            "xp_reward": 180,
            "content": """# Real-World System Design Cases

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor real-world cases ar viktigt |
|----------|-----------------------------------|
| **Interviews** | Systemdesign-intervjuer |
| **Patterns** | Lara av beprovat |
| **Trade-offs** | Forsta beslut |
| **Scale** | Tanka i miljarder |
| **Practice** | Applicera kunskap |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Case 1: URL Shortener (bit.ly)

```
REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Shorten URLs (write)
- Redirect to original (read)
- Analytics (clicks)
- 100M URLs/day, 10:1 read/write ratio

HIGH-LEVEL DESIGN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────┐     ┌─────────────┐     ┌─────────────┐
│ Client  │────>│ API Gateway │────>│ URL Service │
└─────────┘     └─────────────┘     └──────┬──────┘
                                           │
                    ┌──────────────────────┼──────────────────────┐
                    v                      v                      v
              ┌──────────┐          ┌──────────┐          ┌──────────┐
              │  Cache   │          │ Database │          │ Analytics│
              │ (Redis)  │          │(Cassandra)│          │ (Kafka)  │
              └──────────┘          └──────────┘          └──────────┘

KEY DECISIONS:
- Base62 encoding (a-zA-Z0-9) for short codes
- 7 chars = 62^7 = 3.5 trillion combinations
- Cache hot URLs (90% reads)
- Cassandra for write-heavy + horizontal scale
- Kafka for async analytics
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Case 2: Twitter Timeline

```
REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Post tweets
- Follow users
- View home timeline
- 500M tweets/day, 300M MAU

TWO APPROACHES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PULL MODEL (Fan-out on read):
User opens app -> Query all follows -> Merge + sort
+ Realtime
- Slow for users with many follows

PUSH MODEL (Fan-out on write):
Tweet posted -> Push to all followers' timelines
+ Fast read
- Slow write for celebrities (millions of followers)

HYBRID (Twitter's approach):
┌────────────────────────────────────────────────────────┐
│                                                        │
│  Regular users (<1000 followers): PUSH                │
│  - Pre-compute timeline in Redis                      │
│                                                        │
│  Celebrities (>1000 followers): PULL                  │
│  - Merge at read time                                 │
│                                                        │
└────────────────────────────────────────────────────────┘

Timeline Cache (Redis):
user:123:timeline -> [tweet_id_1, tweet_id_2, ...]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Case 3: Chat System (WhatsApp)

```
REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- 1:1 and group messaging
- Online/offline status
- Message delivery confirmation
- 100M concurrent users

ARCHITECTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────┐                         ┌──────────┐
│ Client A │<──WebSocket──>┌────────┐│ Client B │
└──────────┘               │  Chat  │└──────────┘
                           │ Server │
                           │ Cluster│
                           └───┬────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        v                      v                      v
  ┌──────────┐           ┌──────────┐          ┌──────────┐
  │  Redis   │           │ Message  │          │ Presence │
  │(Session) │           │   Queue  │          │ Service  │
  └──────────┘           └──────────┘          └──────────┘

MESSAGE FLOW:
1. A sends message
2. Server stores in queue (if B offline)
3. Server pushes to B via WebSocket
4. B sends ACK
5. Server marks as delivered

PRESENCE:
- Heartbeat every 30s
- Redis TTL for online status
- Broadcast status changes to contacts
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Case 4: Distributed File Storage (S3/Dropbox)

```
REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Upload/download files
- File sync across devices
- Deduplication
- Versioning

ARCHITECTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────┐     ┌─────────────┐
│ Client   │────>│ API Server  │
└──────────┘     └──────┬──────┘
                        │
        ┌───────────────┼───────────────┐
        v               v               v
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  Metadata    │ │   Block      │ │    CDN       │
│   Service    │ │   Storage    │ │  (Download)  │
│  (Postgres)  │ │  (HDFS/S3)   │ │              │
└──────────────┘ └──────────────┘ └──────────────┘

CHUNKING + DEDUP:
┌────────────────────────────────────────────────────────┐
│  File (100MB)                                          │
│  ┌────┐┌────┐┌────┐┌────┐┌────┐                      │
│  │ C1 ││ C2 ││ C3 ││ C4 ││ C5 │ <- 4MB chunks       │
│  └────┘└────┘└────┘└────┘└────┘                      │
│                                                        │
│  Each chunk: SHA256 hash as ID                        │
│  Same content = same hash = store once                │
│                                                        │
│  File metadata:                                        │
│  {chunks: [hash1, hash2, hash3, hash4, hash5]}       │
└────────────────────────────────────────────────────────┘

SYNC:
- Client sends file tree with hashes
- Server compares, sends delta
- Conflict resolution: Last-write-wins or manual
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Case 5: Rate Limiter

```
REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Limit: 100 requests/minute per user
- Distributed across multiple servers
- Low latency (<1ms overhead)

DESIGN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

         Request
            │
            v
┌────────────────────┐
│ Rate Limit Check   │
│                    │
│ GET user:123:count │──> Redis
│                    │
│ count < 100?       │
│   YES: INCR, allow │
│   NO:  deny (429)  │
│                    │
└────────────────────┘

REDIS IMPLEMENTATION (Sliding Window):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

-- Lua script for atomic operation
local key = "ratelimit:" .. user_id
local current = redis.call("INCR", key)
if current == 1 then
    redis.call("EXPIRE", key, 60)
end
if current > 100 then
    return 0  -- denied
end
return 1  -- allowed

+ Atomic
+ Fast (<1ms)
+ Distributed
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## System Design Interview Framework

```
STEP-BY-STEP APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. CLARIFY REQUIREMENTS (5 min)
   - Functional: What should it do?
   - Non-functional: Scale, latency, availability
   - Constraints: Budget, timeline

2. BACK-OF-ENVELOPE (5 min)
   - Users: 100M DAU
   - Storage: 1KB/request * 100M = 100GB/day
   - Bandwidth: Peak 10K req/sec

3. HIGH-LEVEL DESIGN (10 min)
   - Draw boxes and arrows
   - API design
   - Data flow

4. DEEP DIVE (15 min)
   - Database choice
   - Caching strategy
   - Specific algorithms

5. WRAP UP (5 min)
   - Trade-offs
   - Bottlenecks
   - Future improvements
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Common Patterns

| Problem | Pattern |
|---------|---------|
| **High read** | Cache + CDN |
| **High write** | Message queue + async |
| **Search** | Elasticsearch |
| **Real-time** | WebSocket + Redis pub/sub |
| **Analytics** | Kafka + data warehouse |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Over-engineering | For tidigt | Start simple, iterate |
| Ignoring scale | "It works locally" | Back-of-envelope first |
| Single point of failure | No redundancy | Replicate everything |
| No monitoring | "Ship it" | Observability from day 1 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Requirements** | Forstå problemet forst |
| **Trade-offs** | Inget ar gratis |
| **Scale** | Tanka 10x, 100x |
| **Practice** | Rita system dagligen |

**Kom ihag:**
- Det finns inget "ratt" svar
- Kommunicera trade-offs tydligt
- Borja enkelt, oka komplexitet
- Ovning gor mastare - designa nagot varje dag
"""
        },
    ]
}
