# =============================================================================
# BLOCK 4: OPTIMIZATION (Noder 13-16)
# =============================================================================

NODE_13_INDEXING = {
    "node_id": 13,
    "title": "Indexing",
    "slug": "indexing",
    "estimated_minutes": 60,
    "xp_reward": 165,
    "prerequisites": [5],
    "content": '''# Indexing

Index ar datastrukturer som dramatiskt snabbar upp datasokningar. Ratt index kan gora skillnaden mellan en query som tar 10 sekunder och en som tar 10 millisekunder.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

```
┌─────────────────────────────────────────────────────────────────┐
│                     INDEX IMPACT                                │
├─────────────────────────────────────────────────────────────────┤
│  Utan index:                                                    │
│  SELECT * FROM logs WHERE timestamp > '2024-01-01'             │
│  -> Seq Scan: 10,000,000 rader -> 15 sekunder                  │
├─────────────────────────────────────────────────────────────────┤
│  Med index:                                                     │
│  CREATE INDEX idx_logs_ts ON logs(timestamp)                   │
│  -> Index Scan: 50,000 rader -> 50 millisekunder               │
├─────────────────────────────────────────────────────────────────┤
│  Skillnad: 300x snabbare!                                       │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Index Basics

```sql
-- Index pa en kolumn
CREATE INDEX idx_servers_status
ON servers(status);

-- Composite index (flera kolumner)
CREATE INDEX idx_servers_env_status
ON servers(environment, status);
```

VIKTIGT - Kolumnordning i composite index:

```
┌─────────────────────────────────────────────────────────────────┐
│  INDEX: (environment, status)                                   │
├─────────────────────────────────────────────────────────────────┤
│  FUNGERAR:                                                      │
│  - WHERE environment = 'prod'                                   │
│  - WHERE environment = 'prod' AND status = 'active'            │
├─────────────────────────────────────────────────────────────────┤
│  FUNGERAR INTE:                                                 │
│  - WHERE status = 'active'  (anvander INTE index!)             │
└─────────────────────────────────────────────────────────────────┘
  Tumregel: Forsta kolumnen maste finnas i WHERE
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Index-typer

```sql
-- B-tree (DEFAULT) - for jamforelser och sorting
CREATE INDEX idx_servers_created
ON servers(created_at);
-- Bra for: =, <, >, <=, >=, BETWEEN, ORDER BY

-- Hash - endast exakt matchning
CREATE INDEX idx_servers_hostname_hash
ON servers USING hash(hostname);
-- Bra for: = (endast)

-- GIN - for arrays, JSONB, full-text search
CREATE INDEX idx_servers_tags_gin
ON servers USING gin(tags);
-- Bra for: @>, ?, ?|, ?&, full-text

-- GiST - for geometriska data, ranges
CREATE INDEX idx_events_during_gist
ON events USING gist(during);
-- Bra for: &&, @>, <@, ranges

-- BRIN - for stora sorterade tabeller
CREATE INDEX idx_logs_time_brin
ON logs USING brin(timestamp);
-- Bra for: Append-only tabeller, 1000x mindre an B-tree
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Partial Index

Indexera bara en delmangd av rader - sparar utrymme och snabbare:

```sql
-- Bara aktiva servrar (90% av queries)
CREATE INDEX idx_active_servers
ON servers(hostname)
WHERE status = 'active';

-- Query som anvander indexet
SELECT * FROM servers
WHERE status = 'active' AND hostname = 'web1';

-- Bara icke-processerade jobb
CREATE INDEX idx_pending_jobs
ON jobs(created_at)
WHERE status = 'pending';

-- Perfekt for job queues - indexet krymper nar jobb processeras!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Expression Index

Index pa beraknade varden:

```sql
-- Index pa LOWER(hostname)
CREATE INDEX idx_servers_lower_hostname
ON servers(LOWER(hostname));

-- Query MASTE matcha exakt!
SELECT * FROM servers
WHERE LOWER(hostname) = 'web1';  -- Anvander index

SELECT * FROM servers
WHERE hostname = 'web1';  -- Anvander INTE index!

-- Index pa JSON-falt
CREATE INDEX idx_config_port
ON configs((settings->>'port'));

-- Index pa datum-del
CREATE INDEX idx_logs_date
ON logs(DATE(timestamp));
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Unique Index

Enforcerar unikhet och ger snabb lookup:

```sql
-- Unique index
CREATE UNIQUE INDEX idx_servers_hostname_unique
ON servers(hostname);

-- Partial unique - unik bland icke-raderade
CREATE UNIQUE INDEX idx_active_hostname_unique
ON servers(hostname)
WHERE deleted_at IS NULL;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Covering Index (INCLUDE)

Inkludera extra kolumner for index-only scan:

```sql
-- Index med inkluderade kolumner
CREATE INDEX idx_servers_status_covering
ON servers(status)
INCLUDE (hostname, ip_address);

-- Denna query behover aldrig lasa tabellen!
SELECT hostname, ip_address
FROM servers
WHERE status = 'active';
-- -> Index Only Scan (snabbast mojligt)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Concurrent Index

Skapa index utan att blockera tabellen:

```sql
-- UTAN CONCURRENTLY - blockerar writes!
CREATE INDEX idx_servers_env ON servers(environment);

-- MED CONCURRENTLY - tar langre tid men blockerar inte
CREATE INDEX CONCURRENTLY idx_servers_env
ON servers(environment);
```

ALLTID anvand CONCURRENTLY i produktion!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Index Maintenance

```sql
-- Lista alla index pa en tabell
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'servers';

-- Index-storlek
SELECT
    indexrelname AS index_name,
    pg_size_pretty(pg_relation_size(indexrelid)) AS size
FROM pg_stat_user_indexes
WHERE relname = 'servers'
ORDER BY pg_relation_size(indexrelid) DESC;

-- Oanvanda index (potential att ta bort)
SELECT
    indexrelname,
    idx_scan AS times_used
FROM pg_stat_user_indexes
WHERE idx_scan = 0
AND indexrelname NOT LIKE '%_pkey';

-- Ta bort index
DROP INDEX IF EXISTS idx_servers_status;

-- Rebuild index (concurrent)
REINDEX INDEX CONCURRENTLY idx_servers_hostname;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Index-typ | Operatorer | Anvandning |
|-----------|------------|------------|
| B-tree | =, <, >, <=, >=, BETWEEN | Default, mest anvand |
| Hash | = | Endast exakt matchning |
| GIN | @>, ?, ?|, ?& | Arrays, JSONB, full-text |
| GiST | &&, @>, <@ | Geometri, ranges |
| BRIN | <, > | Stora sorterade tabeller |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

### Index pa lag-selektivitet kolumn

```sql
-- FEL - status har bara 3 varden, index hjalper inte
CREATE INDEX idx_status ON servers(status);
SELECT * FROM servers WHERE status = 'active';  -- 80% av rader!

-- BATTRE - partial index eller inget index alls
CREATE INDEX idx_inactive ON servers(hostname) WHERE status = 'inactive';
```

### Glommer expression-matchning

```sql
-- FEL - index pa hostname, query pa LOWER(hostname)
CREATE INDEX idx_hostname ON servers(hostname);
SELECT * FROM servers WHERE LOWER(hostname) = 'web1';  -- Seq Scan!

-- RATT - expression index
CREATE INDEX idx_lower_hostname ON servers(LOWER(hostname));
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktisk ovning

```sql
-- DevOps: Optimera vanliga queries

-- 1. Server lookup pa hostname (case-insensitive)
CREATE INDEX idx_servers_lower_hostname ON servers(LOWER(hostname));

-- 2. Deployment-historik per server
CREATE INDEX idx_deployments_server_date
ON deployments(server_id, deployed_at DESC);

-- 3. Job queue - bara pending jobs
CREATE INDEX idx_jobs_pending
ON jobs(priority DESC, created_at)
WHERE status = 'pending';

-- 4. Log-sokning (BRIN for tidsbaserad data)
CREATE INDEX idx_logs_timestamp_brin ON logs USING brin(timestamp);

-- Verifiera att index anvands
EXPLAIN ANALYZE SELECT * FROM servers WHERE LOWER(hostname) = 'web1';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- B-tree ar default och fungerar for de flesta fall
- Composite index kolumnordning ar kritisk - forsta kolumnen maste vara i WHERE
- Partial index for subsets (t.ex. status = 'active')
- Expression index maste matcha query exakt (LOWER, DATE, etc.)
- Covering index med INCLUDE for index-only scans
- ALLTID anvand CONCURRENTLY i produktion
- GIN for JSONB och arrays, BRIN for stora tidsserier
- Monitorera oanvanda index och ta bort dem
- Index snabbar upp reads men saktar ner writes - balansera
- Kolla alltid EXPLAIN for att verifiera att index anvands

Nasta steg: Node 14 - Query Optimization och EXPLAIN
''',
}

NODE_14_EXPLAIN = {
    "node_id": 14,
    "title": "Query Optimization & EXPLAIN",
    "slug": "explain",
    "estimated_minutes": 60,
    "xp_reward": 170,
    "prerequisites": [13],
    "content": '''# Query Optimization och EXPLAIN

EXPLAIN ar ditt viktigaste verktyg for att forsta varfor queries ar langsamma. Det visar exakt hur PostgreSQL planerar att exekvera din query.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXPLAIN USE CASES                            │
├─────────────────────────────────────────────────────────────────┤
│  - Identifiera varfor dashboard ar langsam                     │
│  - Verifiera att index anvands                                 │
│  - Hitta N+1 query-problem                                     │
│  - Optimera batch-jobb och rapporter                           │
│  - Planera for skalning - hur haller queries vid 10x data?     │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## EXPLAIN Basics

```sql
-- Visa query plan (kor INTE queryn)
EXPLAIN SELECT * FROM servers WHERE status = 'active';

-- Kor queryn och visa faktiska tider
EXPLAIN ANALYZE SELECT * FROM servers WHERE status = 'active';

-- Med buffer-statistik (I/O)
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM servers WHERE status = 'active';

-- Alla detaljer
EXPLAIN (ANALYZE, BUFFERS, TIMING, VERBOSE)
SELECT * FROM servers WHERE status = 'active';

-- JSON-format (for verktyg)
EXPLAIN (FORMAT JSON)
SELECT * FROM servers WHERE status = 'active';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Lasa EXPLAIN Output

```
Seq Scan on servers  (cost=0.00..35.50 rows=1230 width=112)
  Filter: (status = 'active'::text)
  Rows Removed by Filter: 270

┌─────────────────────────────────────────────────────────────────┐
│  cost=0.00..35.50                                               │
│  ├── 0.00 = startup cost (tid innan forsta raden)              │
│  └── 35.50 = total cost (estimerad, inte sekunder!)            │
├─────────────────────────────────────────────────────────────────┤
│  rows=1230 = estimerat antal rader som returneras               │
├─────────────────────────────────────────────────────────────────┤
│  width=112 = bytes per rad                                      │
└─────────────────────────────────────────────────────────────────┘
```

Med ANALYZE far du faktiska tider:

```
Seq Scan on servers  (cost=0.00..35.50 rows=1230 width=112)
                     (actual time=0.015..0.892 rows=1500 loops=1)

┌─────────────────────────────────────────────────────────────────┐
│  actual time=0.015..0.892  (millisekunder)                      │
│  ├── 0.015 = tid till forsta rad                               │
│  └── 0.892 = total tid                                          │
├─────────────────────────────────────────────────────────────────┤
│  rows=1500 = faktiskt antal rader (jfr estimat 1230)           │
├─────────────────────────────────────────────────────────────────┤
│  loops=1 = antal ganger noden exekverades                       │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Scan Types

```
┌─────────────────┬────────────────────────────────────────────────┐
│ SCAN TYPE       │ BESKRIVNING                                    │
├─────────────────┼────────────────────────────────────────────────┤
│ Seq Scan        │ Laser ALLA rader i tabellen                   │
│                 │ Daligt for stora tabeller med selektiv query  │
├─────────────────┼────────────────────────────────────────────────┤
│ Index Scan      │ Anvander index, laser sedan tabell for data   │
│                 │ Bra for selektiva queries                     │
├─────────────────┼────────────────────────────────────────────────┤
│ Index Only Scan │ ALL data finns i index - laser aldrig tabell  │
│                 │ Snabbast mojligt!                             │
├─────────────────┼────────────────────────────────────────────────┤
│ Bitmap Scan     │ Kombinerar flera index, sedan laser tabell    │
│                 │ Bra for OR-villkor eller lag selektivitet     │
└─────────────────┴────────────────────────────────────────────────┘
```

```sql
-- Seq Scan (ingen index eller for manga rader)
EXPLAIN SELECT * FROM logs;
-- Seq Scan on logs

-- Index Scan (anvander index)
EXPLAIN SELECT * FROM servers WHERE id = 1;
-- Index Scan using servers_pkey on servers
--   Index Cond: (id = 1)

-- Index Only Scan (alla kolumner i index)
EXPLAIN SELECT id FROM servers WHERE id = 1;
-- Index Only Scan using servers_pkey on servers

-- Bitmap Scan (OR-villkor)
EXPLAIN SELECT * FROM servers WHERE status = 'active' OR environment = 'prod';
-- Bitmap Heap Scan on servers
--   -> BitmapOr
--        -> Bitmap Index Scan on idx_status
--        -> Bitmap Index Scan on idx_env
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Join Strategier

```sql
EXPLAIN SELECT * FROM servers s
JOIN deployments d ON s.id = d.server_id;
```

```
┌─────────────────┬────────────────────────────────────────────────┐
│ JOIN TYPE       │ NAR DET ANVANDS                                │
├─────────────────┼────────────────────────────────────────────────┤
│ Nested Loop     │ Liten yttre tabell, index pa inre             │
│                 │ Bra: 100 x 1 lookup                           │
├─────────────────┼────────────────────────────────────────────────┤
│ Hash Join       │ Equality joins, medelstor data                │
│                 │ Bygger hashtabell, probar mot den             │
├─────────────────┼────────────────────────────────────────────────┤
│ Merge Join      │ Bada tabeller sorterade pa join-kolumn        │
│                 │ Effektivt for stora sorterade dataset         │
└─────────────────┴────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga Problem och Losningar

### Problem 1: Seq Scan pa stor tabell

```sql
-- Seq Scan (DALIGT for 10M rader)
EXPLAIN SELECT * FROM logs WHERE timestamp > '2024-01-01';
-- Seq Scan on logs
--   Filter: (timestamp > '2024-01-01')

-- LOSNING: Skapa index
CREATE INDEX idx_logs_timestamp ON logs(timestamp);

-- Nu: Index Scan
EXPLAIN SELECT * FROM logs WHERE timestamp > '2024-01-01';
-- Index Scan using idx_logs_timestamp on logs
```

### Problem 2: Index anvands inte (function pa kolumn)

```sql
-- Seq Scan (function forhindrar index)
EXPLAIN SELECT * FROM servers WHERE UPPER(hostname) = 'WEB1';
-- Seq Scan on servers

-- LOSNING: Expression index
CREATE INDEX idx_upper_hostname ON servers(UPPER(hostname));
```

### Problem 3: Estimat stammer inte

```sql
-- Estimat: 10 rader, Faktiskt: 100,000 rader
-- -> Fel query plan!

-- LOSNING: Uppdatera statistik
ANALYZE servers;
-- Eller specifika kolumner
ANALYZE servers(status, environment);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Optimization Tips

```sql
-- 1. Undvik SELECT * - hamta bara vad du behover
SELECT id, hostname FROM servers;  -- Battre

-- 2. LIMIT tidigt
SELECT * FROM logs
WHERE timestamp > '2024-01-01'
ORDER BY timestamp DESC
LIMIT 100;

-- 3. Anvand IN istallet for multipla OR
-- Daligt
WHERE status = 'active' OR status = 'pending' OR status = 'running'
-- Battre
WHERE status IN ('active', 'pending', 'running')

-- 4. EXISTS istallet for IN med subquery
-- Langsamt (laddar hela subquery forst)
WHERE server_id IN (SELECT id FROM servers WHERE status = 'active')
-- Snabbare (stannar vid forsta traff)
WHERE EXISTS (
    SELECT 1 FROM servers WHERE id = deployments.server_id AND status = 'active'
)

-- 5. Undvik OFFSET for paginering av stora dataset
-- Daligt (laser alla rader upp till offset)
SELECT * FROM logs ORDER BY id LIMIT 10 OFFSET 100000;
-- Battre (keyset pagination)
SELECT * FROM logs WHERE id > 100000 ORDER BY id LIMIT 10;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ANALYZE och VACUUM

```sql
-- Uppdatera statistik for query planner
ANALYZE servers;

-- Specifika kolumner
ANALYZE servers(status, environment);

-- VACUUM: Atervinn utrymme fran raderade rader
VACUUM servers;

-- VACUUM ANALYZE: Bada pa en gang
VACUUM ANALYZE servers;

-- VACUUM FULL: Komprimera tabellen (laser tabellen!)
VACUUM FULL servers;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Scan Type | Nar det ar bra | Nar det ar daligt |
|-----------|----------------|-------------------|
| Seq Scan | Sma tabeller, ingen selektivitet | Stora tabeller med selektiva queries |
| Index Scan | Selektiv query (fa rader) | Manga rader (>10% av tabell) |
| Index Only Scan | Alla kolumner i index | - |
| Bitmap Scan | OR-villkor, medel selektivitet | - |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktisk ovning

```sql
-- Analysera och optimera denna query
EXPLAIN ANALYZE
SELECT
    s.hostname,
    COUNT(d.id) AS deploy_count,
    MAX(d.deployed_at) AS last_deploy
FROM servers s
LEFT JOIN deployments d ON s.id = d.server_id
WHERE s.environment = 'production'
  AND d.deployed_at > NOW() - INTERVAL '30 days'
GROUP BY s.id, s.hostname
ORDER BY deploy_count DESC
LIMIT 10;

-- Forvantade index:
CREATE INDEX idx_servers_env ON servers(environment);
CREATE INDEX idx_deploys_server_date ON deployments(server_id, deployed_at);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- EXPLAIN visar planen, EXPLAIN ANALYZE kor queryn och visar faktiska tider
- Seq Scan pa stor tabell ar oftast ett problem - skapa index
- Index Only Scan ar snabbast - alla kolumner finns i index
- Funktioner pa kolumner forhindrar index - anvand expression index
- Estimat vs faktiskt avvikelse = kor ANALYZE for att uppdatera statistik
- EXISTS ar ofta snabbare an IN med subquery
- Undvik OFFSET for paginering - anvand keyset pagination
- VACUUM ANALYZE regelbundet for bast prestanda
- cost ar INTE tid - det ar en estimerad enhet
- Kor alltid EXPLAIN innan du deployer nya queries till produktion

Nasta steg: Node 15 - Partitioning
''',
}

NODE_15_PARTITIONING = {
    "node_id": 15,
    "title": "Partitioning",
    "slug": "partitioning",
    "estimated_minutes": 50,
    "xp_reward": 150,
    "prerequisites": [14],
    "content": '''# Partitioning

Partitioning delar upp stora tabeller i mindre, hanterbara delar. Queries scannar bara relevanta partitioner istallet for hela tabellen.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

```
┌─────────────────────────────────────────────────────────────────┐
│                    PARTITIONING USE CASES                       │
├─────────────────────────────────────────────────────────────────┤
│  LOGS-TABELL:                                                   │
│  - 100M rader, vaxer 1M/dag                                    │
│  - De flesta queries pa senaste 7 dagarna                      │
│  - Gammal data ska arkiveras                                   │
├─────────────────────────────────────────────────────────────────┤
│  MED PARTITIONING:                                              │
│  - Manatliga partitioner                                       │
│  - Query pa senaste veckan scannar 1 partition (3M rader)      │
│  - Arkivera genom att DROP:a gammal partition (instant!)       │
│  - VACUUM per partition (snabbare, mindre lock)                │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Fordelar och Nackdelar

```
FORDELAR:
+ Partition pruning - scannar bara relevanta partitioner
+ Snabbare maintenance (VACUUM, REINDEX per partition)
+ Enkel arkivering - DROP partition istallet for DELETE
+ Parallell I/O mojlig

NACKDELAR:
- Mer komplexitet i schema
- Overhead for routing vid INSERT
- Begransningar pa UNIQUE constraints och foreign keys
- Kraver planering for partition-strategi
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Range Partitioning

Vanligast for tidsbaserad data:

```sql
-- Skapa partitionerad tabell
CREATE TABLE logs (
    id BIGSERIAL,
    timestamp TIMESTAMPTZ NOT NULL,
    level VARCHAR(20),
    message TEXT,
    server_id INTEGER
) PARTITION BY RANGE (timestamp);

-- Skapa partitioner for varje manad
CREATE TABLE logs_2024_01 PARTITION OF logs
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE logs_2024_02 PARTITION OF logs
FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');

CREATE TABLE logs_2024_03 PARTITION OF logs
FOR VALUES FROM ('2024-03-01') TO ('2024-04-01');

-- Default partition for data som inte matchar nagon
CREATE TABLE logs_default PARTITION OF logs DEFAULT;

-- INSERT routas automatiskt till ratt partition
INSERT INTO logs (timestamp, level, message)
VALUES ('2024-02-15 10:00:00', 'ERROR', 'Connection failed');
-- -> Hamnar i logs_2024_02

-- Query med partition pruning
EXPLAIN SELECT * FROM logs WHERE timestamp >= '2024-02-01';
-- Scannar BARA logs_2024_02 och senare!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## List Partitioning

For diskreta varden som environment eller region:

```sql
CREATE TABLE servers (
    id SERIAL,
    hostname VARCHAR(100) NOT NULL,
    environment VARCHAR(20) NOT NULL,
    ip_address INET
) PARTITION BY LIST (environment);

CREATE TABLE servers_prod PARTITION OF servers
FOR VALUES IN ('production');

CREATE TABLE servers_staging PARTITION OF servers
FOR VALUES IN ('staging');

CREATE TABLE servers_dev PARTITION OF servers
FOR VALUES IN ('development', 'testing');

-- Query pa production scannar bara servers_prod
SELECT * FROM servers WHERE environment = 'production';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hash Partitioning

For jamn fordelning nar det inte finns naturlig partition-nyckel:

```sql
CREATE TABLE sessions (
    id UUID NOT NULL,
    user_id INTEGER,
    data JSONB,
    created_at TIMESTAMPTZ
) PARTITION BY HASH (id);

-- Skapa 4 partitioner
CREATE TABLE sessions_0 PARTITION OF sessions
FOR VALUES WITH (MODULUS 4, REMAINDER 0);

CREATE TABLE sessions_1 PARTITION OF sessions
FOR VALUES WITH (MODULUS 4, REMAINDER 1);

CREATE TABLE sessions_2 PARTITION OF sessions
FOR VALUES WITH (MODULUS 4, REMAINDER 2);

CREATE TABLE sessions_3 PARTITION OF sessions
FOR VALUES WITH (MODULUS 4, REMAINDER 3);

-- Data fordelas jamt over partitionerna
-- Bra for parallelisering av queries
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Sub-partitioning

Kombinera strategier:

```sql
-- Forst range pa tid, sedan list pa environment
CREATE TABLE metrics (
    timestamp TIMESTAMPTZ NOT NULL,
    environment VARCHAR(20) NOT NULL,
    metric_name VARCHAR(100),
    value NUMERIC
) PARTITION BY RANGE (timestamp);

-- Skapa manatlig partition som ar sub-partitionerad
CREATE TABLE metrics_2024_01 PARTITION OF metrics
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01')
PARTITION BY LIST (environment);

-- Sub-partitioner
CREATE TABLE metrics_2024_01_prod
PARTITION OF metrics_2024_01
FOR VALUES IN ('production');

CREATE TABLE metrics_2024_01_staging
PARTITION OF metrics_2024_01
FOR VALUES IN ('staging');
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Partition Management

```sql
-- Se alla partitioner
SELECT
    inhrelid::regclass AS partition,
    pg_get_expr(relpartbound, inhrelid) AS bounds
FROM pg_inherits
JOIN pg_class ON pg_class.oid = inhrelid
WHERE inhparent = 'logs'::regclass;

-- Detach partition (for arkivering)
ALTER TABLE logs DETACH PARTITION logs_2024_01;
-- Nu ar logs_2024_01 en vanlig tabell - kan flyttas/dumpas

-- Attach partition (aterinfora)
ALTER TABLE logs ATTACH PARTITION logs_2024_01
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

-- Drop partition (SNABB radering!)
DROP TABLE logs_2024_01;
-- Instant! Ingen DELETE som skannar miljontals rader
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Index pa Partitionerade Tabeller

```sql
-- Index skapas automatiskt pa ALLA partitioner
CREATE INDEX idx_logs_level ON logs(level);

-- Index pa specifik partition
CREATE INDEX idx_logs_2024_02_server ON logs_2024_02(server_id);

-- Varje partition kan ha egna index
-- Bra for partition-specifik optimering
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Automatisk Partition med pg_partman

```sql
-- Installera extension
CREATE EXTENSION pg_partman;

-- Skapa parent med automatiska partitioner
SELECT partman.create_parent(
    p_parent_table := 'public.logs',
    p_control := 'timestamp',
    p_type := 'native',
    p_interval := 'monthly',
    p_premake := 3  -- Skapa 3 framtida partitioner
);

-- Schemalagd maintenance (skapa nya partitioner, droppa gamla)
SELECT partman.run_maintenance();

-- Konfigurera retention
UPDATE partman.part_config
SET retention = '12 months',
    retention_keep_table = false  -- DROP gamla partitioner
WHERE parent_table = 'public.logs';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Partition Type | Anvandning | Exempel |
|----------------|------------|---------|
| RANGE | Tidsserier, numeriska intervall | logs per manad |
| LIST | Diskreta varden | environment, region |
| HASH | Jamn fordelning | sessions, large tables |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

### Glommer DEFAULT partition

```sql
-- FEL - INSERT misslyckas om data inte matchar nagon partition
INSERT INTO logs (timestamp, ...) VALUES ('2025-01-01', ...);
-- ERROR: no partition found

-- RATT - skapa default partition
CREATE TABLE logs_default PARTITION OF logs DEFAULT;
```

### Query utan partition key i WHERE

```sql
-- DALIGT - scannar ALLA partitioner
SELECT * FROM logs WHERE level = 'ERROR';

-- BRA - inkluderar partition key
SELECT * FROM logs
WHERE timestamp >= NOW() - INTERVAL '7 days'
  AND level = 'ERROR';
-- Scannar bara relevanta partitioner!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktisk ovning

```sql
-- Skapa partitionerad deployment-historik
CREATE TABLE deployment_history (
    id BIGSERIAL,
    deployed_at TIMESTAMPTZ NOT NULL,
    server_id INTEGER NOT NULL,
    version VARCHAR(50),
    status VARCHAR(20),
    duration_ms INTEGER
) PARTITION BY RANGE (deployed_at);

-- Skapa kvartalsvisa partitioner
CREATE TABLE deployments_2024_q1 PARTITION OF deployment_history
FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

CREATE TABLE deployments_2024_q2 PARTITION OF deployment_history
FOR VALUES FROM ('2024-04-01') TO ('2024-07-01');

-- Index pa alla partitioner
CREATE INDEX idx_deploys_server ON deployment_history(server_id);

-- Verifiera partition pruning
EXPLAIN SELECT * FROM deployment_history
WHERE deployed_at >= '2024-02-01' AND deployed_at < '2024-03-01';
-- Ska bara scanna deployments_2024_q1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- Partitioning delar stora tabeller i mindre delar for battre prestanda
- RANGE for tidsserier, LIST for kategorier, HASH for jamn fordelning
- Partition pruning kraver partition key i WHERE - annars scannas alla partitioner
- DROP PARTITION ar instant - anvand for att arkivera gammal data
- VACUUM/REINDEX kan koras per partition utan att pverka andra
- Skapa alltid DEFAULT partition for att fanga oforutsedda varden
- pg_partman automatiserar skapande och radering av partitioner
- Sub-partitioning for komplexa scenarier (tid + kategori)
- Index skapas automatiskt pa alla partitioner
- Planera partitionsstrategi noggrant - svart att andra senare

Nasta steg: Node 16 - JSON och JSONB
''',
}

NODE_16_JSON = {
    "node_id": 16,
    "title": "JSON & JSONB",
    "slug": "json-jsonb",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [2],
    "content": '''# JSON och JSONB

JSONB kombinerar flexibiliteten fran NoSQL med kraften i SQL. Perfekt for semi-strukturerad data, metadata, konfigurationer och API-responses.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

```
┌─────────────────────────────────────────────────────────────────┐
│                    JSONB USE CASES                              │
├─────────────────────────────────────────────────────────────────┤
│  Server metadata:                                               │
│  - tags, labels, annotations                                   │
│  - Cloud provider-specifik data                                │
│  - Custom attributes som varierar per server                   │
├─────────────────────────────────────────────────────────────────┤
│  Deployment info:                                               │
│  - Environment variables                                       │
│  - Config overrides                                            │
│  - Build metadata                                              │
├─────────────────────────────────────────────────────────────────┤
│  Audit logs:                                                    │
│  - Request/response bodies                                     │
│  - Diff av andringar                                           │
│  - Flexibel loggning utan schema-andringar                     │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## JSON vs JSONB

```
┌─────────────────┬────────────────────────────────────────────────┐
│ JSON            │ JSONB (rekommenderas!)                         │
├─────────────────┼────────────────────────────────────────────────┤
│ Sparar exakt    │ Binart format, ingen whitespace               │
│ text inkl.      │                                                │
│ whitespace      │                                                │
├─────────────────┼────────────────────────────────────────────────┤
│ Ingen indexing  │ Stodjer GIN index for snabba lookups          │
├─────────────────┼────────────────────────────────────────────────┤
│ Snabbare INSERT │ Snabbare queries                              │
├─────────────────┼────────────────────────────────────────────────┤
│ Bevarar         │ Ingen duplicerade nycklar                     │
│ duplicates      │                                                │
└─────────────────┴────────────────────────────────────────────────┘

Tumregel: Anvand ALLTID JSONB om du inte har specifik anledning for JSON
```

```sql
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb
);

INSERT INTO servers (hostname, metadata) VALUES
('web1', '{"region": "eu-west-1", "tier": "premium", "tags": ["web", "prod"]}'),
('db1', '{"region": "eu-west-1", "tier": "standard", "replicas": 2}');
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Lasa JSON-data

```sql
-- -> hamtar JSON-element (returnerar JSONB)
SELECT metadata->'region' FROM servers;
-- "eu-west-1" (med citattecken - det ar JSON)

-- ->> hamtar som TEXT (utan citattecken)
SELECT metadata->>'region' FROM servers;
-- eu-west-1 (ren text)

-- Nestade varden
SELECT metadata->'config'->'database'->>'host' FROM servers;

-- Med path-notation (#> och #>>)
SELECT metadata #> '{config,database,host}' FROM servers;     -- JSONB
SELECT metadata #>> '{config,database,host}' FROM servers;    -- TEXT

-- Array-element (0-indexerat)
SELECT metadata->'tags'->0 FROM servers;   -- Forsta elementet
SELECT metadata->'tags'->>1 FROM servers;  -- Andra som text
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Filtrera JSON-data

```sql
-- Exakt matchning pa text
SELECT * FROM servers WHERE metadata->>'region' = 'eu-west-1';

-- Cast till nummer for jamforelse
SELECT * FROM servers WHERE (metadata->>'replicas')::int > 1;

-- @> Contains (finns i)
SELECT * FROM servers WHERE metadata @> '{"tier": "premium"}';

-- <@ Contained by (ar del av)
SELECT * FROM servers WHERE '{"tier": "premium"}' <@ metadata;

-- ? Key exists
SELECT * FROM servers WHERE metadata ? 'replicas';

-- ?| Any of keys exists (OR)
SELECT * FROM servers WHERE metadata ?| array['replicas', 'shards'];

-- ?& All keys exist (AND)
SELECT * FROM servers WHERE metadata ?& array['region', 'tier'];

-- Array contains
SELECT * FROM servers WHERE metadata->'tags' ? 'prod';
SELECT * FROM servers WHERE metadata @> '{"tags": ["prod"]}';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Modifiera JSON-data

```sql
-- Satt/andara varde
UPDATE servers
SET metadata = jsonb_set(metadata, '{region}', '"eu-north-1"')
WHERE hostname = 'web1';

-- Satt nested varde (skapar path om det inte finns)
UPDATE servers
SET metadata = jsonb_set(metadata, '{config,timeout}', '30', true)
WHERE hostname = 'web1';

-- Ta bort nyckel
UPDATE servers
SET metadata = metadata - 'region'
WHERE hostname = 'web1';

-- Ta bort nested nyckel
UPDATE servers
SET metadata = metadata #- '{config,password}'
WHERE hostname = 'web1';

-- Merge/concatenate (|| operatorn)
UPDATE servers
SET metadata = metadata || '{"updated": true, "version": 2}'
WHERE hostname = 'web1';

-- Lagg till i array
UPDATE servers
SET metadata = jsonb_set(
    metadata,
    '{tags}',
    (metadata->'tags') || '"new-tag"'::jsonb
)
WHERE hostname = 'web1';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## JSONB Functions

```sql
-- Hamta alla nycklar
SELECT jsonb_object_keys(metadata) FROM servers WHERE id = 1;

-- JSON till rader (key-value pairs)
SELECT key, value
FROM servers, jsonb_each(metadata)
WHERE id = 1;
-- key     | value
-- region  | "eu-west-1"
-- tier    | "premium"

-- jsonb_each_text for text-varden
SELECT key, value
FROM servers, jsonb_each_text(metadata)
WHERE id = 1;

-- Array till rader
SELECT jsonb_array_elements(metadata->'tags') AS tag
FROM servers WHERE id = 1;

-- Bygga JSONB
SELECT jsonb_build_object(
    'hostname', hostname,
    'region', metadata->>'region',
    'is_premium', metadata->>'tier' = 'premium'
) AS server_info
FROM servers;

-- Aggregera till array
SELECT jsonb_agg(hostname) AS all_hosts FROM servers;
-- ["web1", "db1"]

-- Aggregera till object
SELECT jsonb_object_agg(hostname, metadata->'region') AS hosts_by_region
FROM servers;
-- {"web1": "eu-west-1", "db1": "eu-west-1"}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Indexering av JSONB

```sql
-- GIN index for contains (@>) och key exists (?)
CREATE INDEX idx_servers_metadata_gin
ON servers USING gin(metadata);

-- Nu ar dessa queries snabba:
SELECT * FROM servers WHERE metadata @> '{"tier": "premium"}';
SELECT * FROM servers WHERE metadata ? 'replicas';

-- GIN med jsonb_path_ops (mindre, snabbare for @>)
CREATE INDEX idx_servers_metadata_pathops
ON servers USING gin(metadata jsonb_path_ops);

-- Expression index for specifik path
CREATE INDEX idx_servers_region
ON servers((metadata->>'region'));

-- Nu ar denna snabb:
SELECT * FROM servers WHERE metadata->>'region' = 'eu-west-1';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## JSON Path (PostgreSQL 12+)

Mer kraftfullt satt att query:a JSON:

```sql
-- @@ operator for path predicates
SELECT * FROM servers
WHERE metadata @@ '$.tier == "premium"';

-- Hamta varden med path
SELECT jsonb_path_query(metadata, '$.tags[*]') AS tag
FROM servers;

-- Filtrera i path
SELECT jsonb_path_query(
    '{"servers": [{"name": "web1", "cpu": 80}, {"name": "db1", "cpu": 30}]}'::jsonb,
    '$.servers[*] ? (@.cpu > 50)'
);
-- {"name": "web1", "cpu": 80}

-- First match
SELECT jsonb_path_query_first(metadata, '$.tags[0]')
FROM servers;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Operator | Funktion | Returtyp |
|----------|----------|----------|
| -> | Hamta element | JSONB |
| ->> | Hamta element | TEXT |
| #> | Hamta via path | JSONB |
| #>> | Hamta via path | TEXT |
| @> | Contains | BOOLEAN |
| ? | Key exists | BOOLEAN |
| ?| | Any key exists | BOOLEAN |
| ?& | All keys exist | BOOLEAN |
| - | Remove key | JSONB |
| #- | Remove via path | JSONB |
| || | Merge/concat | JSONB |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

### Glommer citattecken i jsonb_set

```sql
-- FEL - saknar citattecken runt text
UPDATE servers SET metadata = jsonb_set(metadata, '{region}', 'eu-north-1');
-- ERROR: invalid input syntax

-- RATT - text maste vara giltig JSON
UPDATE servers SET metadata = jsonb_set(metadata, '{region}', '"eu-north-1"');
```

### Index anvands inte

```sql
-- FEL - expression index pa ->>, men query pa ->
CREATE INDEX idx_region ON servers((metadata->>'region'));
SELECT * FROM servers WHERE metadata->'region' = '"eu-west-1"';  -- Seq Scan!

-- RATT - matcha index och query
SELECT * FROM servers WHERE metadata->>'region' = 'eu-west-1';   -- Index Scan!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktisk ovning

```sql
-- DevOps: Server metadata management

-- Skapa tabell
CREATE TABLE server_inventory (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Index for snabba lookups
CREATE INDEX idx_inventory_metadata ON server_inventory USING gin(metadata);
CREATE INDEX idx_inventory_env ON server_inventory((metadata->>'environment'));

-- Lagg till servrar
INSERT INTO server_inventory (hostname, metadata) VALUES
('web-1', '{"environment": "production", "tier": "frontend", "tags": ["web", "nginx"], "resources": {"cpu": 4, "ram": 16}}'),
('api-1', '{"environment": "production", "tier": "backend", "tags": ["api", "python"], "resources": {"cpu": 8, "ram": 32}}'),
('db-1', '{"environment": "production", "tier": "database", "tags": ["postgres", "primary"], "resources": {"cpu": 16, "ram": 64}}');

-- Query: Alla production servrar
SELECT hostname FROM server_inventory
WHERE metadata @> '{"environment": "production"}';

-- Query: Servrar med mer an 16GB RAM
SELECT hostname, metadata->'resources'->>'ram' AS ram_gb
FROM server_inventory
WHERE (metadata->'resources'->>'ram')::int > 16;

-- Query: Servrar med specifik tag
SELECT hostname FROM server_inventory
WHERE metadata->'tags' ? 'nginx';

-- Uppdatera: Lagg till monitored flag
UPDATE server_inventory
SET metadata = metadata || '{"monitored": true}'
WHERE metadata @> '{"environment": "production"}';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- Anvand JSONB inte JSON - battre prestanda och indexering
- -> returnerar JSONB, ->> returnerar TEXT
- @> (contains) ar huvudoperatorn for filtrering
- ? kontrollerar om en nyckel existerar
- GIN index for @> och ?, expression index for ->>/specificka paths
- jsonb_set for att uppdatera, || for att merge, - for att ta bort
- Textstranger i jsonb_set maste inkludera citattecken: '"value"'
- jsonb_each och jsonb_array_elements for att "explode" JSON till rader
- JSON Path (@@) ger kraftfullare query-mojligheter i PG12+
- Perfekt for semi-strukturerad data som varierar mellan rader

Nasta steg: Node 17 - Database Design Patterns
''',
}

SQL_BLOCK_4 = [
    NODE_13_INDEXING,
    NODE_14_EXPLAIN,
    NODE_15_PARTITIONING,
    NODE_16_JSON,
]
