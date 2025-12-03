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
    "content": '''
# Indexing

Snabba upp queries.

## Index Basics

```sql
-- Index på en kolumn
CREATE INDEX idx_servers_status
ON servers(status);

-- Flera kolumner (composite)
CREATE INDEX idx_servers_env_status
ON servers(environment, status);

-- Ordningen spelar roll!
-- (environment, status) fungerar för:
--   WHERE environment = 'prod'
--   WHERE environment = 'prod' AND status = 'active'
-- Men INTE för:
--   WHERE status = 'active'  (använder inte index)
```

## Index Types

```sql
-- B-tree (default) - jämförelser
CREATE INDEX idx_servers_created
ON servers(created_at);

-- Hash - bara equality
CREATE INDEX idx_servers_hostname_hash
ON servers USING hash(hostname);

-- GIN - arrays, JSONB, full-text
CREATE INDEX idx_servers_tags_gin
ON servers USING gin(tags);

-- GiST - geometric, ranges
CREATE INDEX idx_events_during_gist
ON events USING gist(during);

-- BRIN - stora tabeller, sorterade
CREATE INDEX idx_logs_time_brin
ON logs USING brin(timestamp);
```

## Partial Index

```sql
-- Index bara aktiva servrar
CREATE INDEX idx_active_servers
ON servers(hostname)
WHERE status = 'active';

-- Sparar utrymme, snabbare
SELECT * FROM servers
WHERE status = 'active' AND hostname = 'web1';
```

## Expression Index

```sql
-- Index på expression
CREATE INDEX idx_servers_lower_hostname
ON servers(LOWER(hostname));

-- Query måste matcha exakt
SELECT * FROM servers
WHERE LOWER(hostname) = 'web1';  -- Använder index

SELECT * FROM servers
WHERE hostname = 'web1';  -- Använder INTE index
```

## Unique Index

```sql
-- Unique constraint skapar implicit index
CREATE UNIQUE INDEX idx_servers_hostname_unique
ON servers(hostname);

-- Partial unique
CREATE UNIQUE INDEX idx_active_hostname
ON servers(hostname)
WHERE status != 'deleted';
```

## Covering Index (INCLUDE)

```sql
-- Include extra columns i index
CREATE INDEX idx_servers_status_covering
ON servers(status)
INCLUDE (hostname, ip_address);

-- Index-only scan möjlig
SELECT hostname, ip_address
FROM servers
WHERE status = 'active';
```

## Index Maintenance

```sql
-- Lista indexes
SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'servers';

-- Index storlek
SELECT
    indexrelname AS index,
    pg_size_pretty(pg_relation_size(indexrelid)) AS size
FROM pg_stat_user_indexes
WHERE relname = 'servers';

-- Drop index
DROP INDEX IF EXISTS idx_servers_status;

-- Rebuild (concurrent)
REINDEX INDEX CONCURRENTLY idx_servers_hostname;
```

## Concurrent Index

```sql
-- Skapar index utan att locka tabellen
CREATE INDEX CONCURRENTLY idx_servers_env
ON servers(environment);

-- Viktigt för produktion!
-- Tar längre tid men blockerar inte
```

| Index Type | Användning |
|------------|------------|
| B-tree | =, <, >, BETWEEN |
| Hash | Endast = |
| GIN | Arrays, JSONB, full-text |
| GiST | Geometri, ranges |
| BRIN | Stora sorterade tabeller |

**Nästa steg:** Node 14 - Query Optimization
''',
}

NODE_14_EXPLAIN = {
    "node_id": 14,
    "title": "Query Optimization & EXPLAIN",
    "slug": "explain",
    "estimated_minutes": 60,
    "xp_reward": 170,
    "prerequisites": [13],
    "content": '''
# Query Optimization & EXPLAIN

Förstå och förbättra query performance.

## EXPLAIN Basics

```sql
-- Query plan
EXPLAIN SELECT * FROM servers WHERE status = 'active';

-- Med faktisk exekvering
EXPLAIN ANALYZE SELECT * FROM servers WHERE status = 'active';

-- Mer detaljer
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM servers WHERE status = 'active';

-- JSON format
EXPLAIN (FORMAT JSON)
SELECT * FROM servers;
```

## Läsa EXPLAIN Output

```
Seq Scan on servers  (cost=0.00..35.50 rows=1230 width=112)
  Filter: (status = 'active'::text)

-- cost=startup..total (estimerat)
-- rows: estimerat antal rader
-- width: bytes per rad

Index Scan using idx_status on servers
  (cost=0.29..8.30 rows=1 width=112)
  Index Cond: (status = 'active'::text)
```

## Scan Types

```sql
-- Seq Scan: Läser hela tabellen
EXPLAIN SELECT * FROM servers;
-- Seq Scan on servers

-- Index Scan: Använder index, läser tabell
EXPLAIN SELECT * FROM servers WHERE id = 1;
-- Index Scan using servers_pkey

-- Index Only Scan: Allt i index
EXPLAIN SELECT id FROM servers WHERE id = 1;
-- Index Only Scan using servers_pkey

-- Bitmap Scan: Multiple index lookups
EXPLAIN SELECT * FROM servers
WHERE status = 'active' OR environment = 'prod';
-- Bitmap Heap Scan
--   -> BitmapOr
--        -> Bitmap Index Scan on idx_status
--        -> Bitmap Index Scan on idx_env
```

## Join Strategies

```sql
-- Nested Loop: Bra för små tabeller
-- Hash Join: Bra för equality joins
-- Merge Join: Bra för sorterade data

EXPLAIN SELECT *
FROM servers s
JOIN deployments d ON s.id = d.server_id;

-- Vanliga resultat:
-- Hash Join
--   Hash Cond: (d.server_id = s.id)
--   -> Seq Scan on deployments
--   -> Hash
--        -> Seq Scan on servers
```

## Common Issues

```sql
-- Problem: Seq Scan på stor tabell
EXPLAIN SELECT * FROM logs WHERE timestamp > '2024-01-01';
-- Seq Scan (dåligt för stor tabell)

-- Lösning: Index
CREATE INDEX idx_logs_timestamp ON logs(timestamp);

-- Problem: Index inte använt
EXPLAIN SELECT * FROM servers WHERE UPPER(hostname) = 'WEB1';
-- Seq Scan (function på kolumn)

-- Lösning: Expression index
CREATE INDEX idx_upper_hostname ON servers(UPPER(hostname));
```

## Optimization Tips

```sql
-- 1. Undvik SELECT *
SELECT id, hostname FROM servers;  -- Bättre

-- 2. Limit tidigt
SELECT * FROM logs
WHERE timestamp > '2024-01-01'
ORDER BY timestamp
LIMIT 100;

-- 3. Undvik OR, använd IN
-- Dåligt
WHERE status = 'active' OR status = 'pending'
-- Bättre
WHERE status IN ('active', 'pending')

-- 4. EXISTS istället för IN med subquery
-- Dåligt
WHERE server_id IN (SELECT id FROM servers WHERE status = 'active')
-- Bättre
WHERE EXISTS (
    SELECT 1 FROM servers
    WHERE id = deployments.server_id AND status = 'active'
)
```

## ANALYZE

```sql
-- Uppdatera statistik
ANALYZE servers;

-- Specifika kolumner
ANALYZE servers(status, environment);

-- Vacuum och analyze
VACUUM ANALYZE servers;
```

| Scan Type | När? |
|-----------|------|
| Seq Scan | Små tabeller, inga index |
| Index Scan | Selektiv query, behöver data |
| Index Only Scan | Alla kolumner i index |
| Bitmap Scan | OR-villkor, låg selektivitet |

**Nästa steg:** Node 15 - Partitioning
''',
}

NODE_15_PARTITIONING = {
    "node_id": 15,
    "title": "Partitioning",
    "slug": "partitioning",
    "estimated_minutes": 50,
    "xp_reward": 150,
    "prerequisites": [14],
    "content": '''
# Partitioning

Dela upp stora tabeller.

## Why Partition?

```
Fördelar:
- Snabbare queries (partition pruning)
- Enklare maintenance (vacuum, reindex per partition)
- Arkivera gammal data
- Parallell I/O

Nackdelar:
- Mer komplexitet
- Overhead för routing
- Constraints på foreign keys
```

## Range Partitioning

```sql
-- Partitionerad tabell
CREATE TABLE logs (
    id SERIAL,
    timestamp TIMESTAMPTZ NOT NULL,
    level VARCHAR(20),
    message TEXT
) PARTITION BY RANGE (timestamp);

-- Skapa partitioner
CREATE TABLE logs_2024_01 PARTITION OF logs
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE logs_2024_02 PARTITION OF logs
FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');

-- Default partition
CREATE TABLE logs_default PARTITION OF logs DEFAULT;

-- Query går automatiskt till rätt partition
SELECT * FROM logs WHERE timestamp >= '2024-01-15';
```

## List Partitioning

```sql
CREATE TABLE servers (
    id SERIAL,
    hostname VARCHAR(100),
    environment VARCHAR(20) NOT NULL
) PARTITION BY LIST (environment);

CREATE TABLE servers_prod PARTITION OF servers
FOR VALUES IN ('production');

CREATE TABLE servers_staging PARTITION OF servers
FOR VALUES IN ('staging');

CREATE TABLE servers_dev PARTITION OF servers
FOR VALUES IN ('development');
```

## Hash Partitioning

```sql
CREATE TABLE sessions (
    id UUID NOT NULL,
    user_id INTEGER,
    data JSONB
) PARTITION BY HASH (id);

-- 4 partitioner
CREATE TABLE sessions_0 PARTITION OF sessions
FOR VALUES WITH (MODULUS 4, REMAINDER 0);

CREATE TABLE sessions_1 PARTITION OF sessions
FOR VALUES WITH (MODULUS 4, REMAINDER 1);

CREATE TABLE sessions_2 PARTITION OF sessions
FOR VALUES WITH (MODULUS 4, REMAINDER 2);

CREATE TABLE sessions_3 PARTITION OF sessions
FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

## Sub-partitioning

```sql
CREATE TABLE metrics (
    timestamp TIMESTAMPTZ NOT NULL,
    environment VARCHAR(20) NOT NULL,
    value NUMERIC
) PARTITION BY RANGE (timestamp);

CREATE TABLE metrics_2024_01 PARTITION OF metrics
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01')
PARTITION BY LIST (environment);

CREATE TABLE metrics_2024_01_prod
PARTITION OF metrics_2024_01
FOR VALUES IN ('production');
```

## Partition Management

```sql
-- Detach partition (utan att radera)
ALTER TABLE logs DETACH PARTITION logs_2024_01;

-- Attach partition
ALTER TABLE logs ATTACH PARTITION logs_2024_01
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

-- Drop partition
DROP TABLE logs_2024_01;

-- Index på partitionerad tabell
CREATE INDEX idx_logs_level ON logs(level);
-- Skapas på alla partitioner!
```

## Automatisk Partition

```sql
-- Med pg_partman extension
CREATE EXTENSION pg_partman;

SELECT partman.create_parent(
    'public.logs',
    'timestamp',
    'native',
    'monthly'
);

-- Maintenance
SELECT partman.run_maintenance();
```

| Partition Type | Användning |
|----------------|------------|
| Range | Datum/tid, numeriska intervall |
| List | Diskreta värden (status, region) |
| Hash | Jämn fördelning |

**Nästa steg:** Node 16 - JSON & JSONB
''',
}

NODE_16_JSON = {
    "node_id": 16,
    "title": "JSON & JSONB",
    "slug": "json-jsonb",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [2],
    "content": '''
# JSON & JSONB

Semi-strukturerad data i SQL.

## JSON vs JSONB

```sql
-- JSON: Sparar exakt text
-- JSONB: Binärt format, snabbare queries

CREATE TABLE configs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    settings JSONB  -- Föredra JSONB
);

INSERT INTO configs (name, settings) VALUES
('web', '{"port": 8080, "ssl": true, "timeout": 30}'),
('worker', '{"threads": 4, "queue": "default"}');
```

## Query JSON

```sql
-- Hämta nyckel (returnerar JSON)
SELECT settings->'port' FROM configs;
-- "8080" (som JSON)

-- Hämta som text
SELECT settings->>'port' FROM configs;
-- 8080 (som text)

-- Nested
SELECT settings->'database'->'host' FROM configs;

-- Path
SELECT settings #> '{database,host}' FROM configs;
SELECT settings #>> '{database,host}' FROM configs;  -- Som text
```

## Filter JSON

```sql
-- Jämföra
SELECT * FROM configs
WHERE settings->>'port' = '8080';

-- Cast till nummer
SELECT * FROM configs
WHERE (settings->>'port')::int > 8000;

-- Contains
SELECT * FROM configs
WHERE settings @> '{"ssl": true}';

-- Key exists
SELECT * FROM configs
WHERE settings ? 'ssl';

-- Any key exists
SELECT * FROM configs
WHERE settings ?| array['ssl', 'tls'];

-- All keys exist
SELECT * FROM configs
WHERE settings ?& array['port', 'timeout'];
```

## Modify JSON

```sql
-- Set value
UPDATE configs
SET settings = jsonb_set(settings, '{port}', '9090')
WHERE name = 'web';

-- Set nested
UPDATE configs
SET settings = jsonb_set(settings, '{database,pool}', '10')
WHERE name = 'web';

-- Remove key
UPDATE configs
SET settings = settings - 'timeout'
WHERE name = 'web';

-- Remove nested
UPDATE configs
SET settings = settings #- '{database,password}'
WHERE name = 'web';

-- Concatenate/merge
UPDATE configs
SET settings = settings || '{"debug": true}'
WHERE name = 'web';
```

## JSONB Functions

```sql
-- Alla nycklar
SELECT jsonb_object_keys(settings) FROM configs;

-- Till rows
SELECT * FROM jsonb_each(
    '{"port": 8080, "ssl": true}'::jsonb
);
-- key  | value
-- port | 8080
-- ssl  | true

-- Array elements
SELECT jsonb_array_elements('[1,2,3]'::jsonb);

-- Bygga JSON
SELECT jsonb_build_object(
    'hostname', hostname,
    'ip', ip_address
) FROM servers;

-- Aggregera till array
SELECT jsonb_agg(hostname) FROM servers;

-- Aggregera till object
SELECT jsonb_object_agg(id, hostname) FROM servers;
```

## Index JSON

```sql
-- GIN index för contains/exists
CREATE INDEX idx_configs_settings_gin
ON configs USING gin(settings);

-- Expression index för specifik path
CREATE INDEX idx_configs_port
ON configs((settings->>'port'));

-- Jsonb_path_ops (mer effektiv för @>)
CREATE INDEX idx_configs_settings_pathops
ON configs USING gin(settings jsonb_path_ops);
```

## JSON Path (PostgreSQL 12+)

```sql
-- JSON Path query
SELECT settings @@ '$.port > 8000' FROM configs;

-- Hämta med path
SELECT jsonb_path_query(
    settings,
    '$.database.host'
) FROM configs;

-- Filter
SELECT jsonb_path_query(
    '{"servers": [{"name": "web1"}, {"name": "web2"}]}'::jsonb,
    '$.servers[*] ? (@.name == "web1")'
);
```

| Operator | Funktion |
|----------|----------|
| -> | Hämta JSON |
| ->> | Hämta som text |
| @> | Contains |
| ? | Key exists |
| - | Remove key |
| II | Merge (concat) |

**Nästa steg:** Node 17 - Database Design
''',
}

SQL_BLOCK_4 = [
    NODE_13_INDEXING,
    NODE_14_EXPLAIN,
    NODE_15_PARTITIONING,
    NODE_16_JSON,
]
