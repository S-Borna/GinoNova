# =============================================================================
# BLOCK 3: ADVANCED QUERIES (Noder 9-12)
# =============================================================================

NODE_09_CTE_WINDOW = {
    "node_id": 9,
    "title": "CTEs & Window Functions",
    "slug": "cte-window",
    "estimated_minutes": 60,
    "xp_reward": 165,
    "prerequisites": [8],
    "content": '''
# CTEs & Window Functions

Kraftfulla query-tekniker.

## Common Table Expressions (CTE)

```sql
-- Basic CTE
WITH active_servers AS (
    SELECT * FROM servers
    WHERE status = 'active'
)
SELECT * FROM active_servers
WHERE environment = 'production';

-- Multiple CTEs
WITH
production AS (
    SELECT * FROM servers WHERE environment = 'production'
),
active AS (
    SELECT * FROM production WHERE status = 'active'
),
with_deploys AS (
    SELECT
        a.*,
        COUNT(d.id) as deploy_count
    FROM active a
    LEFT JOIN deployments d ON a.id = d.server_id
    GROUP BY a.id
)
SELECT * FROM with_deploys
WHERE deploy_count > 10;
```

## Recursive CTE

```sql
-- Hierarkisk data
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    parent_id INTEGER REFERENCES categories(id)
);

-- Alla ancestors
WITH RECURSIVE ancestors AS (
    -- Base case
    SELECT id, name, parent_id, 0 as level
    FROM categories
    WHERE id = 10

    UNION ALL

    -- Recursive case
    SELECT c.id, c.name, c.parent_id, a.level + 1
    FROM categories c
    JOIN ancestors a ON c.id = a.parent_id
)
SELECT * FROM ancestors;

-- Generera sekvens
WITH RECURSIVE dates AS (
    SELECT CURRENT_DATE as date
    UNION ALL
    SELECT date + 1
    FROM dates
    WHERE date < CURRENT_DATE + 30
)
SELECT * FROM dates;
```

## Window Functions

```sql
-- ROW_NUMBER
SELECT
    hostname,
    environment,
    ROW_NUMBER() OVER (ORDER BY created_at) as row_num
FROM servers;

-- Partition by
SELECT
    hostname,
    environment,
    ROW_NUMBER() OVER (
        PARTITION BY environment
        ORDER BY created_at
    ) as env_row_num
FROM servers;
```

## Ranking Functions

```sql
-- ROW_NUMBER: Alltid unik
-- RANK: Samma för ties, hoppar över
-- DENSE_RANK: Samma för ties, hoppar inte

SELECT
    hostname,
    request_count,
    ROW_NUMBER() OVER (ORDER BY request_count DESC) as row_num,
    RANK() OVER (ORDER BY request_count DESC) as rank,
    DENSE_RANK() OVER (ORDER BY request_count DESC) as dense_rank
FROM servers;

-- request_count: 100, 100, 80, 70
-- ROW_NUMBER:     1,   2,   3,  4
-- RANK:           1,   1,   3,  4  (hoppar 2)
-- DENSE_RANK:     1,   1,   2,  3  (hoppar inte)
```

## Aggregate Window Functions

```sql
SELECT
    hostname,
    environment,
    request_count,
    SUM(request_count) OVER () as total,
    SUM(request_count) OVER (PARTITION BY environment) as env_total,
    ROUND(100.0 * request_count / SUM(request_count) OVER (), 2) as pct_of_total
FROM servers;

-- Running total
SELECT
    date,
    revenue,
    SUM(revenue) OVER (ORDER BY date) as running_total
FROM daily_revenue;

-- Moving average
SELECT
    date,
    value,
    AVG(value) OVER (
        ORDER BY date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) as moving_avg_7d
FROM metrics;
```

## LAG / LEAD

```sql
-- Jämför med föregående/nästa rad
SELECT
    hostname,
    created_at,
    LAG(created_at) OVER (ORDER BY created_at) as prev_created,
    created_at - LAG(created_at) OVER (ORDER BY created_at) as time_since_prev
FROM servers;

-- Change from previous
SELECT
    date,
    value,
    value - LAG(value) OVER (ORDER BY date) as daily_change,
    ROUND(
        100.0 * (value - LAG(value) OVER (ORDER BY date)) / LAG(value) OVER (ORDER BY date),
        2
    ) as pct_change
FROM daily_metrics;
```

## FIRST_VALUE / LAST_VALUE

```sql
SELECT
    hostname,
    environment,
    created_at,
    FIRST_VALUE(hostname) OVER (
        PARTITION BY environment
        ORDER BY created_at
    ) as first_in_env,
    LAST_VALUE(hostname) OVER (
        PARTITION BY environment
        ORDER BY created_at
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) as last_in_env
FROM servers;
```

| Function | Returnerar |
|----------|------------|
| ROW_NUMBER | Sekvensnummer |
| RANK | Ranking med gaps |
| DENSE_RANK | Ranking utan gaps |
| LAG | Föregående värde |
| LEAD | Nästa värde |
| SUM/AVG OVER | Running aggregat |

**Nästa steg:** Node 10 - Views & Materialized Views
''',
}

NODE_10_VIEWS = {
    "node_id": 10,
    "title": "Views & Materialized Views",
    "slug": "views",
    "estimated_minutes": 45,
    "xp_reward": 130,
    "prerequisites": [5],
    "content": '''
# Views & Materialized Views

Virtuella och cachade tabeller.

## Regular Views

```sql
-- Skapa view
CREATE VIEW active_production_servers AS
SELECT
    id,
    hostname,
    ip_address,
    created_at
FROM servers
WHERE status = 'active'
  AND environment = 'production';

-- Använda view
SELECT * FROM active_production_servers;

-- View med JOIN
CREATE VIEW server_deployment_stats AS
SELECT
    s.id,
    s.hostname,
    s.environment,
    COUNT(d.id) as deployment_count,
    MAX(d.deployed_at) as last_deployment
FROM servers s
LEFT JOIN deployments d ON s.id = d.server_id
GROUP BY s.id;

-- View med CTE
CREATE VIEW deployment_trends AS
WITH daily AS (
    SELECT
        DATE(deployed_at) as date,
        COUNT(*) as count
    FROM deployments
    GROUP BY DATE(deployed_at)
)
SELECT
    date,
    count,
    AVG(count) OVER (
        ORDER BY date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) as rolling_avg
FROM daily;
```

## Update Views

```sql
-- Updatebar view (enkla views)
CREATE VIEW active_servers AS
SELECT * FROM servers WHERE status = 'active';

-- Fungerar:
UPDATE active_servers
SET status = 'maintenance'
WHERE id = 1;

-- WITH CHECK OPTION
CREATE VIEW active_servers AS
SELECT * FROM servers WHERE status = 'active'
WITH CHECK OPTION;

-- Nu failar detta (bryter villkoret):
UPDATE active_servers
SET status = 'inactive'  -- Error!
WHERE id = 1;
```

## Replace & Drop

```sql
-- Ersätt view
CREATE OR REPLACE VIEW active_servers AS
SELECT id, hostname, ip_address, status
FROM servers
WHERE status = 'active';

-- Ta bort view
DROP VIEW IF EXISTS active_servers;

-- Med beroenden
DROP VIEW active_servers CASCADE;
```

## Materialized Views

```sql
-- Sparar resultatet fysiskt
CREATE MATERIALIZED VIEW mv_deployment_stats AS
SELECT
    DATE(deployed_at) as date,
    service_name,
    COUNT(*) as deployments,
    AVG(duration_seconds) as avg_duration
FROM deployments
GROUP BY DATE(deployed_at), service_name;

-- Querying är snabbt
SELECT * FROM mv_deployment_stats
WHERE date > CURRENT_DATE - 7;

-- Refresh manuellt
REFRESH MATERIALIZED VIEW mv_deployment_stats;

-- Concurrent refresh (utan lock)
REFRESH MATERIALIZED VIEW CONCURRENTLY mv_deployment_stats;
-- Kräver UNIQUE INDEX!

-- Index på materialized view
CREATE UNIQUE INDEX mv_deploy_stats_idx
ON mv_deployment_stats(date, service_name);
```

## Användningsfall

```sql
-- Dashboard cache
CREATE MATERIALIZED VIEW mv_dashboard AS
SELECT
    environment,
    COUNT(*) as total_servers,
    COUNT(CASE WHEN status = 'active' THEN 1 END) as active,
    COUNT(CASE WHEN status = 'offline' THEN 1 END) as offline
FROM servers
GROUP BY environment;

-- Refresh varje minut (via cron/scheduler)
REFRESH MATERIALIZED VIEW mv_dashboard;
```

## View vs Materialized View

| Egenskap | View | Materialized View |
|----------|------|-------------------|
| Data | Virtuell | Sparad |
| Hastighet | Beräknas varje gång | Snabb read |
| Freshness | Alltid aktuell | Kan vara gammal |
| Storage | Ingen | Tar plats |
| Update | Automatisk | Manuell REFRESH |

**Nästa steg:** Node 11 - Transactions & Locking
''',
}

NODE_11_TRANSACTIONS = {
    "node_id": 11,
    "title": "Transactions & Locking",
    "slug": "transactions",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [4],
    "content": '''
# Transactions & Locking

ACID och concurrency control.

## ACID

```
A - Atomicity    : Allt eller inget
C - Consistency  : Alltid giltigt tillstånd
I - Isolation    : Transaktioner påverkar inte varandra
D - Durability   : Committed data överlever crash
```

## Basic Transaction

```sql
BEGIN;

-- Överföring mellan konton
UPDATE accounts SET balance = balance - 100
WHERE id = 1;

UPDATE accounts SET balance = balance + 100
WHERE id = 2;

-- Allt OK?
COMMIT;

-- Problem? Ångra allt
ROLLBACK;
```

## Savepoints

```sql
BEGIN;

UPDATE servers SET status = 'maintenance'
WHERE id = 1;

SAVEPOINT before_risky;

-- Riskfylld operation
DELETE FROM logs WHERE server_id = 1;

-- Ops, ångra bara denna
ROLLBACK TO before_risky;

-- Fortsätt med annat
UPDATE servers SET status = 'active'
WHERE id = 1;

COMMIT;
```

## Isolation Levels

```sql
-- Read Uncommitted: Ser uncommitted data (dirty reads)
-- Read Committed: Ser endast committed (default PostgreSQL)
-- Repeatable Read: Samma resultat hela transaktionen
-- Serializable: Full isolation

-- Sätt isolation level
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

-- Eller
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

## Locking

```sql
-- Row-level lock
SELECT * FROM servers
WHERE id = 1
FOR UPDATE;  -- Lock för update

-- Skip locked rows (queue processing)
SELECT * FROM jobs
WHERE status = 'pending'
ORDER BY created_at
LIMIT 1
FOR UPDATE SKIP LOCKED;

-- No wait (fail om locked)
SELECT * FROM servers
WHERE id = 1
FOR UPDATE NOWAIT;

-- Share lock (read lock)
SELECT * FROM servers
WHERE id = 1
FOR SHARE;
```

## Advisory Locks

```sql
-- Application-level locks
SELECT pg_advisory_lock(12345);

-- Do exclusive work
UPDATE some_table SET ...;

SELECT pg_advisory_unlock(12345);

-- Try lock (non-blocking)
SELECT pg_try_advisory_lock(12345);

-- Session vs Transaction
SELECT pg_advisory_xact_lock(12345);  -- Released on commit/rollback
```

## Deadlock Prevention

```sql
-- Deadlock exempel:
-- Transaction 1: Lock A, wait for B
-- Transaction 2: Lock B, wait for A

-- Prevention: Låsa i samma ordning!
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
SELECT * FROM accounts WHERE id = 2 FOR UPDATE;
-- Bearbeta...
COMMIT;

-- Timeout
SET lock_timeout = '5s';
```

## Praktiskt Exempel

```sql
-- Safe deployment registration
BEGIN;

-- Lock server
SELECT * FROM servers
WHERE id = 1
FOR UPDATE;

-- Check current status
-- (application logic)

-- Register deployment
INSERT INTO deployments (server_id, version, status)
VALUES (1, 'v2.0.0', 'running');

-- Update server
UPDATE servers
SET current_version = 'v2.0.0',
    last_deployment = NOW()
WHERE id = 1;

COMMIT;
```

| Isolation Level | Dirty Read | Non-repeatable | Phantom |
|-----------------|------------|----------------|---------|
| Read Uncommitted | Ja | Ja | Ja |
| Read Committed | Nej | Ja | Ja |
| Repeatable Read | Nej | Nej | Ja |
| Serializable | Nej | Nej | Nej |

**Nästa steg:** Node 12 - Stored Procedures & Functions
''',
}

NODE_12_STORED_PROCS = {
    "node_id": 12,
    "title": "Stored Procedures & Functions",
    "slug": "stored-procs",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [11],
    "content": '''
# Stored Procedures & Functions

Server-side logic.

## Functions

```sql
-- Enkel funktion
CREATE OR REPLACE FUNCTION get_server_count()
RETURNS INTEGER AS $$
BEGIN
    RETURN (SELECT COUNT(*) FROM servers);
END;
$$ LANGUAGE plpgsql;

-- Använda
SELECT get_server_count();

-- Med parameter
CREATE OR REPLACE FUNCTION get_servers_by_status(p_status VARCHAR)
RETURNS TABLE(id INTEGER, hostname VARCHAR, ip_address INET) AS $$
BEGIN
    RETURN QUERY
    SELECT s.id, s.hostname, s.ip_address
    FROM servers s
    WHERE s.status = p_status;
END;
$$ LANGUAGE plpgsql;

-- Använda
SELECT * FROM get_servers_by_status('active');
```

## Procedures (PostgreSQL 11+)

```sql
-- Procedure kan COMMIT/ROLLBACK
CREATE OR REPLACE PROCEDURE deploy_to_server(
    p_server_id INTEGER,
    p_version VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    -- Create deployment
    INSERT INTO deployments (server_id, version, status)
    VALUES (p_server_id, p_version, 'running');

    -- Update server
    UPDATE servers
    SET current_version = p_version,
        updated_at = NOW()
    WHERE id = p_server_id;

    COMMIT;
END;
$$;

-- Använda
CALL deploy_to_server(1, 'v2.0.0');
```

## Trigger Functions

```sql
-- Audit trigger
CREATE OR REPLACE FUNCTION audit_trigger()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO audit_log (table_name, operation, new_data)
        VALUES (TG_TABLE_NAME, 'INSERT', row_to_json(NEW));
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO audit_log (table_name, operation, old_data, new_data)
        VALUES (TG_TABLE_NAME, 'UPDATE', row_to_json(OLD), row_to_json(NEW));
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO audit_log (table_name, operation, old_data)
        VALUES (TG_TABLE_NAME, 'DELETE', row_to_json(OLD));
    END IF;
    RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;

-- Attach trigger
CREATE TRIGGER servers_audit
AFTER INSERT OR UPDATE OR DELETE ON servers
FOR EACH ROW EXECUTE FUNCTION audit_trigger();

-- Updated_at trigger
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_at
BEFORE UPDATE ON servers
FOR EACH ROW EXECUTE FUNCTION update_modified_column();
```

## Error Handling

```sql
CREATE OR REPLACE FUNCTION safe_divide(a NUMERIC, b NUMERIC)
RETURNS NUMERIC AS $$
BEGIN
    IF b = 0 THEN
        RAISE EXCEPTION 'Division by zero';
    END IF;
    RETURN a / b;
EXCEPTION
    WHEN division_by_zero THEN
        RAISE NOTICE 'Caught division by zero';
        RETURN NULL;
    WHEN OTHERS THEN
        RAISE NOTICE 'Error: %', SQLERRM;
        RETURN NULL;
END;
$$ LANGUAGE plpgsql;
```

## Dynamic SQL

```sql
CREATE OR REPLACE FUNCTION get_table_count(table_name TEXT)
RETURNS INTEGER AS $$
DECLARE
    result INTEGER;
BEGIN
    EXECUTE format('SELECT COUNT(*) FROM %I', table_name)
    INTO result;
    RETURN result;
END;
$$ LANGUAGE plpgsql;

SELECT get_table_count('servers');
```

## Drop Functions

```sql
-- Drop function
DROP FUNCTION IF EXISTS get_server_count();

-- Drop med signature (för overloaded)
DROP FUNCTION get_servers_by_status(VARCHAR);

-- Drop trigger
DROP TRIGGER IF EXISTS servers_audit ON servers;
```

| Typ | Returnerar | Transaction Control |
|-----|------------|---------------------|
| Function | Värde/Table | Nej |
| Procedure | Void | Ja (COMMIT/ROLLBACK) |
| Trigger | TRIGGER | Nej |

**Nästa steg:** Node 13 - Indexing
''',
}

SQL_BLOCK_3 = [
    NODE_09_CTE_WINDOW,
    NODE_10_VIEWS,
    NODE_11_TRANSACTIONS,
    NODE_12_STORED_PROCS,
]
