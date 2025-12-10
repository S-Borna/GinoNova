# =============================================================================
# BLOCK 1: FUNDAMENTALS (Noder 1-4)
# =============================================================================

NODE_01_INTRO = {
    "node_id": 1,
    "title": "Introduction to System Design",
    "slug": "intro",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "prerequisites": [],
    "content": '''# 🏗️ Introduction to System Design

## Varför detta är kritiskt
> "En junior kodar features. En senior designar system. System Design är skillnaden mellan 'det funkar' och 'det skalar till miljoner användare'."

## Vad du kommer lära dig
- ✅ System Design-processen
- ✅ Functional vs Non-Functional Requirements
- ✅ Back-of-the-envelope estimation
- ✅ Latency numbers alla DevOps-ingenjörer måste känna till

---

## Vad är System Design?

```
System Design = Processen att definiera arkitektur,
komponenter, moduler och gränssnitt för ett system
som uppfyller specificerade krav.
```

## Varför System Design?

```yaml
Skäl:
  - Hantera miljontals användare
  - Garantera hög tillgänglighet (99.99%)
  - Optimera för prestanda
  - Möjliggöra framtida skalning
  - Minimera kostnader
  - Underhållbar kodbas
```

## System Design Process

```
1. Requirements Gathering
   +-- Functional Requirements
   |   +-- Vad systemet ska göra
   +-- Non-Functional Requirements
       +-- Skalbarhet
       +-- Tillgänglighet
       +-- Latency
       +-- Consistency

2. High-Level Design
   +-- System komponenter
   +-- Data flow
   +-- Integrationer

3. Detailed Design
   +-- Database schema
   +-- API endpoints
   +-- Algoritmer

4. Identify Bottlenecks
   +-- Single points of failure
   +-- Performance bottlenecks
   +-- Data hotspots
```

## Functional vs Non-Functional

```yaml
Functional Requirements:
  - "Användare kan logga in"
  - "Systemet sparar meddelanden"
  - "Användare kan söka produkter"

Non-Functional Requirements:
  Skalbarhet: "Hantera 10M användare"
  Latency: "< 100ms response time"
  Availability: "99.99% uptime"
  Durability: "Ingen dataförlust"
  Security: "End-to-end kryptering"
```

## Back-of-the-Envelope Estimation

```python
# Snabba uppskattningar för system design

# Användare och trafik
daily_active_users = 10_000_000
requests_per_user_per_day = 10
total_requests_per_day = 100_000_000

# Requests per sekund
rps = total_requests_per_day / (24 * 60 * 60)
# = ~1,157 RPS

# Peak traffic (5x average)
peak_rps = rps * 5
# = ~5,800 RPS

# Data storage
messages_per_user_per_day = 5
message_size_bytes = 500
daily_data = 10_000_000 * 5 * 500
# = 25 GB per dag
# = ~9 TB per år
```

## Vanliga Numbers att Känna Till

```
Latency Numbers:
+-- L1 cache: 0.5 ns
+-- L2 cache: 7 ns
+-- RAM: 100 ns
+-- SSD random read: 150 μs
+-- HDD seek: 10 ms
+-- Network (same datacenter): 0.5 ms
+-- Network (cross-continent): 150 ms
+-- Disk read 1MB (SSD): 1 ms

Storage:
+-- 1 char = 1 byte (ASCII)
+-- 1 char = 4 bytes (UTF-8 max)
+-- UUID = 36 chars = 36 bytes
+-- Timestamp = 8 bytes
+-- Integer = 4-8 bytes

Scale:
+-- 1 KB = 1,000 bytes
+-- 1 MB = 1,000,000 bytes
+-- 1 GB = 1,000,000,000 bytes
+-- 1 TB = 1,000,000,000,000 bytes
```

## System Design Interview

```yaml
Framework:
  1. Clarify Requirements (5 min):
     - Vad är use cases?
     - Hur många användare?
     - Read/write ratio?

  2. High-Level Design (10 min):
     - Rita diagram
     - Huvudkomponenter
     - Data flow

  3. Deep Dive (20 min):
     - Database design
     - API design
     - Skalningsstrategier

  4. Identify Issues (5 min):
     - Single points of failure
     - Bottlenecks
     - Förbättringar
```

| Term | Betydelse |
|------|-----------|
| SLA | Service Level Agreement |
| SLO | Service Level Objective |
| SLI | Service Level Indicator |
| RPS | Requests Per Second |
| QPS | Queries Per Second |
| P99 | 99th percentile latency |

**Nästa steg:** Node 2 - Performance vs Scalability
''',
}

NODE_02_PERFORMANCE = {
    "node_id": 2,
    "title": "Performance vs Scalability",
    "slug": "performance-scalability",
    "estimated_minutes": 50,
    "xp_reward": 140,
    "prerequisites": [1],
    "content": '''# ⚡ Performance vs Scalability

## Varför detta är kritiskt
> "Performance utan scalability = en demo. Scalability utan performance = en långsam app. Du behöver båda för produktion."

## Vad du kommer lära dig
- ✅ Latency vs Throughput
- ✅ Vertical vs Horizontal Scaling
- ✅ Amdahl's Law
- ✅ Performance testing strategier

---

## Definitioner

```yaml
Performance:
  - Hur snabbt systemet svarar
  - Mäts i latency, throughput
  - Fokus: En request

Scalability:
  - Hur systemet hanterar ökad last
  - Mäts i kapacitet
  - Fokus: Många requests
```

## Performance Metrics

```python
# Latency - Tid för en request
latency = time_response_received - time_request_sent

# Throughput - Requests per tidsenhet
throughput = total_requests / time_period

# Response Time vs Latency
response_time = latency + processing_time

# Percentiles
p50 = median_latency      # 50% snabbare
p95 = 95th_percentile     # 95% snabbare
p99 = 99th_percentile     # 99% snabbare (viktigt!)
```

## Latency vs Throughput

```
High Throughput + High Latency:
+-- Batch processing
+-- ETL jobs
+-- Background tasks

Low Latency + Lower Throughput:
+-- Real-time APIs
+-- Gaming servers
+-- Trading systems

Ideal: Low Latency + High Throughput
+-- Optimerad kod
+-- Caching
+-- Rätt infrastruktur
```

## Vertical vs Horizontal Scaling

```yaml
Vertical Scaling (Scale Up):
  Vad: Mer CPU, RAM, disk
  Fördelar:
    - Enkelt
    - Ingen kodändring
  Nackdelar:
    - Har en gräns
    - Single point of failure
    - Dyrt vid höga nivåer
  Exempel: 2 CPU -> 64 CPU

Horizontal Scaling (Scale Out):
  Vad: Fler servrar
  Fördelar:
    - Nästan obegränsat
    - Redundans
    - Kostnadseffektivt
  Nackdelar:
    - Mer komplexitet
    - Data consistency
    - Load balancing behövs
  Exempel: 1 server -> 100 servrar
```

## Scaling Patterns

```
                    +-------------+
                    |   Users     |
                    +------+------+
                           |
                    +------▼------+
                    |Load Balancer|
                    +------+------+
           +---------------+---------------+
           |               |               |
    +------▼------+ +------▼------+ +------▼------+
    |  Server 1   | |  Server 2   | |  Server 3   |
    +------+------+ +------+------+ +------+------+
           |               |               |
           +---------------+---------------+
                           |
                    +------▼------+
                    |  Database   |
                    +-------------+
```

## Performance Optimization

```yaml
Application Layer:
  - Effektiva algoritmer (O(n) vs O(n²))
  - Caching
  - Connection pooling
  - Async processing

Database Layer:
  - Indexering
  - Query optimization
  - Denormalization
  - Read replicas

Infrastructure:
  - CDN för statiskt content
  - Geografisk distribution
  - Bättre hardware
  - Load balancing
```

## Amdahl's Law

```python
# Speedup begränsas av den sekventiella delen

def amdahls_speedup(p, n):
    """
    p = andel som kan parallelliseras
    n = antal processorer
    """
    return 1 / ((1 - p) + p / n)

# Om 90% kan parallelliseras:
speedup = amdahls_speedup(0.9, 10)
# = 5.26x (inte 10x!)

# Om 99% kan parallelliseras:
speedup = amdahls_speedup(0.99, 100)
# = 50x (fortfarande inte 100x)
```

## Performance Testing

```yaml
Load Testing:
  - Simulera förväntad last
  - Verktyg: k6, JMeter, Locust

Stress Testing:
  - Testa bortom normal kapacitet
  - Hitta breaking point

Spike Testing:
  - Plötslig lastökning
  - Testa auto-scaling

Soak Testing:
  - Långvarig test
  - Hitta memory leaks
```

| Skalningstyp | När? |
|--------------|------|
| Vertical | Små system, snabb fix |
| Horizontal | Stora system, långsiktigt |
| Hybrid | Kombination för optimering |

**Nästa steg:** Node 3 - Availability & Consistency
''',
}

NODE_03_AVAILABILITY = {
    "node_id": 3,
    "title": "Availability & Consistency",
    "slug": "availability-consistency",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [2],
    "content": '''# 🔄 Availability & Consistency

## Varför detta är kritiskt
> "99.9% uptime låter bra tills du inser att det är 8.7 timmar nere per år. För en bank är det katastrofalt. Förstå dina krav."

## Vad du kommer lära dig
- ✅ Availability "nines" (99.9%, 99.99%)
- ✅ Failover patterns (Active-Passive, Active-Active)
- ✅ Consistency models
- ✅ CAP Theorem basics

---

## Availability (Tillgänglighet)

```yaml
Definition: Systemet är tillgängligt för användare

Mäts i "nines":
  99%:     3.65 dagar/år nere
  99.9%:   8.76 timmar/år nere
  99.99%:  52.6 minuter/år nere
  99.999%: 5.26 minuter/år nere
```

## Beräkna Availability

```python
# Series (alla måste funka)
total_availability = a1 * a2 * a3

# Web + App + DB
availability = 0.999 * 0.999 * 0.999
# = 99.7%

# Parallel (redundans)
total_availability = 1 - ((1 - a1) * (1 - a2))

# Två load balancers (99.9% var)
availability = 1 - ((1 - 0.999) * (1 - 0.999))
# = 99.9999%
```

## Availability Patterns

```yaml
Failover:
  Active-Passive:
    - En aktiv, en standby
    - Standby tar över vid failure
    - Enkel men ineffektiv

  Active-Active:
    - Båda hanterar trafik
    - Omdirigering vid failure
    - Bättre resursutnyttjande

Replication:
  Master-Slave:
    - Writes till master
    - Reads från slaves
    - Enkel, men master SPOF

  Master-Master:
    - Writes till båda
    - Mer komplex
    - Conflict resolution behövs
```

## Consistency (Konsistens)

```yaml
Definition: Alla läsningar ger senaste data

Strong Consistency:
  - Alla ser samma data samtidigt
  - Högre latency
  - Banker, transaktioner

Eventual Consistency:
  - Data synkas så småningom
  - Lägre latency
  - Social media, DNS

Weak Consistency:
  - Ingen garanti
  - Lägst latency
  - VoIP, gaming
```

## Consistency Models

```
             +----------------------------------+
             |        Strong Consistency        |
             |   Alla ser samma data direkt     |
             +----------------------------------+
                            |
             +----------------------------------+
             |     Sequential Consistency       |
             |   Alla ser samma ordning         |
             +----------------------------------+
                            |
             +----------------------------------+
             |       Causal Consistency         |
             |   Relaterade ops i ordning       |
             +----------------------------------+
                            |
             +----------------------------------+
             |      Eventual Consistency        |
             |   Konvergerar så småningom       |
             +----------------------------------+
```

## CAP Theorem

```yaml
Du kan bara ha 2 av 3:

Consistency: Alla noder ser samma data
Availability: Varje request får response
Partition Tolerance: Fungerar trots nätverksfel

Verkligheten:
  - Nätverksfel händer (P krävs)
  - Välj mellan C och A

CP Systems:
  - MongoDB, Redis, HBase
  - Prioriterar consistency
  - Kan neka requests vid partition

AP Systems:
  - Cassandra, DynamoDB, CouchDB
  - Prioriterar availability
  - Eventual consistency
```

## PACELC Theorem

```
IF Partition:
  Choose Availability or Consistency
ELSE:
  Choose Latency or Consistency

Exempel:
  PA/EL: DynamoDB, Cassandra
         (Availability vid partition, Latency annars)

  PC/EC: MongoDB, HBase
         (Consistency alltid)

  PA/EC: (Ovanligt)
```

## Consistency Patterns i Praktiken

```python
# Read-your-writes consistency
# Användaren ser sina egna ändringar

def update_profile(user_id, data):
    write_to_master(user_id, data)
    # Läs från master för denna session
    invalidate_session_cache(user_id)

# Quorum
# W + R > N garanterar consistency
# W = antal write acks
# R = antal read nodes
# N = total replicas

# Exempel: N=3, W=2, R=2
# 2 + 2 > 3 ✓
```

| Pattern | Konsistens | Latency | Användning |
|---------|------------|---------|------------|
| Strong | Hög | Hög | Banker |
| Eventual | Låg | Låg | Social media |
| Read-your-writes | Medium | Medium | User profiles |

**Nästa steg:** Node 4 - CAP & PACELC Deep Dive
''',
}

NODE_04_CAP = {
    "node_id": 4,
    "title": "CAP & PACELC Deep Dive",
    "slug": "cap-pacelc",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [3],
    "content": '''# 🎯 CAP & PACELC Deep Dive

## Varför detta är kritiskt
> "Varje arkitekturbeslut är en trade-off. CAP och PACELC tvingar dig att förstå vad du offrar - innan produktionen avslöjar det åt dig."

## Vad du kommer lära dig
- ✅ CP vs AP systems
- ✅ PACELC theorem
- ✅ Consistency levels
- ✅ Conflict resolution strategier

---

## CAP Theorem Visualiserat

```
                 Consistency (C)
                      ▲
                     /|\\
                    / | \\
                   /  |  \\
                  /   |   \\
                 /    |    \\
                /  CP | CA  \\
               /      |      \\
              /       |       \\
             ---------+---------
            /         |         \\
           /    AP    |          \\
          /           |           \\
         ▼            |            ▼
  Availability (A) ◄--+--► Partition Tolerance (P)

CA: Existerar ej i distribuerade system
    (Partition händer alltid)
```

## CP Systems (Consistency + Partition Tolerance)

```yaml
Egenskaper:
  - Neka requests vid partition
  - Stark konsistens
  - Banking, inventory

Databaser:
  - MongoDB (default)
  - HBase
  - Redis Cluster
  - Zookeeper
  - etcd

Användning:
  - Finansiella transaktioner
  - Inventory management
  - Konfigurationshantering
```

## AP Systems (Availability + Partition Tolerance)

```yaml
Egenskaper:
  - Alltid tillgänglig
  - Eventual consistency
  - Social media, analytics

Databaser:
  - Cassandra
  - DynamoDB
  - CouchDB
  - Riak

Användning:
  - Social media feeds
  - Analytics/metrics
  - DNS
  - Shopping carts
```

## Välj Rätt System

```python
# Beslutsträd

if requires_strong_consistency:
    if can_tolerate_unavailability:
        return "CP System"
    else:
        return "Single-node database"
else:
    if requires_high_availability:
        return "AP System"
    else:
        return "CP System"

# Specifika use cases:
use_cases = {
    "Bank transactions": "CP",
    "Social media likes": "AP",
    "E-commerce inventory": "CP",
    "User sessions": "AP",
    "Order processing": "CP",
    "Analytics events": "AP",
}
```

## PACELC i Detalj

```
P -> A eller C?
E -> L eller C?

System Examples:

Cassandra (PA/EL):
  - Partition: Availability
  - Else: Low Latency
  - Tunable consistency

DynamoDB (PA/EL):
  - Partition: Availability
  - Else: Low Latency
  - Eventually consistent reads

MongoDB (PC/EC):
  - Partition: Consistency
  - Else: Consistency
  - Strong consistency default

HBase (PC/EC):
  - Partition: Consistency
  - Else: Consistency
  - Strong consistency
```

## Consistency Levels

```yaml
# Cassandra/DynamoDB style

ONE:
  - Snabbast
  - Minst konsistent
  - Läs/skriv till en nod

QUORUM:
  - Balanserat
  - Majority av replicas
  - (N/2 + 1)

ALL:
  - Långsammast
  - Starkast konsistens
  - Alla replicas måste svara
```

## Praktiskt Exempel

```python
# Shopping Cart - AP system
class ShoppingCart:
    """
    AP: Användaren kan alltid lägga till produkter
    Eventual consistency är OK
    """
    def add_item(self, item):
        # Skriv lokalt först
        local_cart.add(item)
        # Synka async till andra noder
        async_replicate(item)

# Inventory - CP system
class Inventory:
    """
    CP: Vi kan inte sälja det vi inte har
    Strong consistency krävs
    """
    def reserve_item(self, item_id):
        # Distributed lock
        with distributed_lock(item_id):
            count = get_count(item_id)
            if count > 0:
                decrement(item_id)
                return True
            return False
```

## Conflict Resolution

```yaml
Last-Write-Wins (LWW):
  - Enkel
  - Timestamp bestämmer
  - Kan förlora data

Vector Clocks:
  - Spårar kausalitet
  - Detekterar konflikter
  - Mer komplex

Application-Level:
  - Merge strategier
  - User intervention
  - Domänspecifik
```

```python
# Vector Clock exempel
vector_clock = {
    "node_a": 3,
    "node_b": 2,
    "node_c": 1
}

# Vid write på node_a:
vector_clock["node_a"] += 1

# Jämför versioner
def is_concurrent(vc1, vc2):
    """Returnerar True om versionerna är concurrent (konflikt)"""
    vc1_greater = any(vc1[k] > vc2.get(k, 0) for k in vc1)
    vc2_greater = any(vc2[k] > vc1.get(k, 0) for k in vc2)
    return vc1_greater and vc2_greater
```

| Scenario | Välj | Varför |
|----------|------|--------|
| Bank | CP | Pengar får inte försvinna |
| Shopping cart | AP | UX viktigare |
| Inventory | CP | Overselling = dåligt |
| Social feed | AP | Gammal data OK |
| Config store | CP | Korrekt config kritiskt |

**Nästa steg:** Node 5 - Load Balancing
''',
}

SYSTEM_DESIGN_BLOCK_1 = [
    NODE_01_INTRO,
    NODE_02_PERFORMANCE,
    NODE_03_AVAILABILITY,
    NODE_04_CAP,
]
