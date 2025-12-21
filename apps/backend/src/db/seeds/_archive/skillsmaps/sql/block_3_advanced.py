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
    "content": '''# CTEs och Window Functions

CTEs (Common Table Expressions) och window functions ar tva av de mest kraftfulla verktygen i modern SQL for att skriva lasbara och effektiva queries.

------------------------------------------------------------------

## Varfor viktigt for DevOps?

```
+-----------------------------------------------------------------+
|                    CTE & WINDOW USE CASES                       |
+-----------------------------------------------------------------+
|  CTEs:                                                          |
|  - Bryt ner komplexa queries i lasbara steg                    |
|  - Rekursiva hierarkier (org-struktur, dependencies)           |
|  - Atervand subqueries utan upprepning                         |
+-----------------------------------------------------------------+
|  Window Functions:                                              |
|  - Ranka servrar efter performance                             |
|  - Running totals for deployments over tid                     |
|  - Jamfor varje rad mot genomsnitt                             |
|  - Berakna forandringar mellan rader                           |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Common Table Expressions (CTE)

WITH-satsen definierar temporara resultat som kan atervandas:

```sql
-- Basic CTE
WITH active_servers AS (
    SELECT * FROM servers
    WHERE status = 'active'
)
SELECT * FROM active_servers
WHERE environment = 'production';

-- Multipla CTEs - byggblock
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
        COUNT(d.id) AS deploy_count
    FROM active a
    LEFT JOIN deployments d ON a.id = d.server_id
    GROUP BY a.id, a.hostname, a.environment, a.status,
             a.ip_address, a.created_at
)
SELECT * FROM with_deploys
WHERE deploy_count > 10;
```

Varje CTE kan referera till tidigare definierade CTEs.

------------------------------------------------------------------

## Recursive CTE

For hierarkisk data eller sekvenser:

```sql
-- Hierarkisk data (org-struktur)
WITH RECURSIVE team_hierarchy AS (
    -- Base case: rot-niva
    SELECT id, name, parent_team_id, 0 AS level
    FROM teams
    WHERE parent_team_id IS NULL

    UNION ALL

    -- Recursive case: barn
    SELECT t.id, t.name, t.parent_team_id, th.level + 1
    FROM teams t
    JOIN team_hierarchy th ON t.parent_team_id = th.id
)
SELECT * FROM team_hierarchy ORDER BY level, name;

-- Generera datum-sekvens
WITH RECURSIVE dates AS (
    SELECT CURRENT_DATE AS date
    UNION ALL
    SELECT date + 1
    FROM dates
    WHERE date < CURRENT_DATE + 30
)
SELECT date FROM dates;

-- DevOps: Dependency chain
WITH RECURSIVE deps AS (
    SELECT service_id, depends_on_id, 1 AS depth
    FROM service_dependencies
    WHERE service_id = 'web-api'

    UNION ALL

    SELECT sd.service_id, sd.depends_on_id, d.depth + 1
    FROM service_dependencies sd
    JOIN deps d ON sd.service_id = d.depends_on_id
    WHERE d.depth < 10  -- Forhindra oandlig loop
)
SELECT DISTINCT depends_on_id, depth FROM deps;
```

------------------------------------------------------------------

## Window Functions - Grunderna

Window functions beraknar varden over en "fonster" av rader utan att gruppera:

```
+--------------------------------------------------------------+
|  function() OVER (                                           |
|      [PARTITION BY col1, col2]   -- Dela upp i grupper      |
|      [ORDER BY col3]             -- Ordning inom grupp      |
|      [frame_clause]              -- Vilka rader i fonstret  |
|  )                                                           |
+--------------------------------------------------------------+
```

```sql
-- ROW_NUMBER: Unik numrering
SELECT
    hostname,
    environment,
    ROW_NUMBER() OVER (ORDER BY created_at) AS row_num
FROM servers;

-- PARTITION BY: Numrera inom grupp
SELECT
    hostname,
    environment,
    ROW_NUMBER() OVER (
        PARTITION BY environment
        ORDER BY created_at
    ) AS env_row_num
FROM servers;
```

------------------------------------------------------------------

## Ranking Functions

Tre varianter for ranking:

```sql
SELECT
    hostname,
    request_count,
    ROW_NUMBER() OVER (ORDER BY request_count DESC) AS row_num,
    RANK() OVER (ORDER BY request_count DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY request_count DESC) AS dense_rank
FROM servers;
```

```
+-----------------+-----------+----------+------+------------+
| request_count   | ROW_NUM   | RANK     | DENSE_RANK      |
+-----------------+-----------+----------+-----------------+
| 100             | 1         | 1        | 1               |
| 100             | 2         | 1        | 1               |
| 80              | 3         | 3        | 2               |
| 70              | 4         | 4        | 3               |
+-----------------+-----------+----------+-----------------+
  ROW_NUMBER: Alltid unik
  RANK: Ties far samma, hoppar over nasta
  DENSE_RANK: Ties far samma, hoppar INTE over
```

------------------------------------------------------------------

## Aggregate Window Functions

Aggregera utan att forlora rader:

```sql
-- Jamfor varje server mot totalt och environment-totalt
SELECT
    hostname,
    environment,
    request_count,
    SUM(request_count) OVER () AS total,
    SUM(request_count) OVER (PARTITION BY environment) AS env_total,
    ROUND(100.0 * request_count / SUM(request_count) OVER (), 2) AS pct_of_total
FROM servers;

-- Running total (kumulativ summa)
SELECT
    DATE(deployed_at) AS date,
    COUNT(*) AS daily_deploys,
    SUM(COUNT(*)) OVER (ORDER BY DATE(deployed_at)) AS running_total
FROM deployments
GROUP BY DATE(deployed_at);

-- Moving average (glidande medelvarde)
SELECT
    date,
    value,
    AVG(value) OVER (
        ORDER BY date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_avg_7d
FROM daily_metrics;
```

------------------------------------------------------------------

## LAG och LEAD

Jamfor med foregaende eller nasta rad:

```sql
-- LAG: Foregaende rad
SELECT
    hostname,
    created_at,
    LAG(created_at) OVER (ORDER BY created_at) AS prev_created,
    created_at - LAG(created_at) OVER (ORDER BY created_at) AS days_since_prev
FROM servers;

-- DevOps: Deployment frequency change
SELECT
    DATE(deployed_at) AS date,
    COUNT(*) AS deploys,
    LAG(COUNT(*)) OVER (ORDER BY DATE(deployed_at)) AS prev_day,
    COUNT(*) - LAG(COUNT(*)) OVER (ORDER BY DATE(deployed_at)) AS change
FROM deployments
GROUP BY DATE(deployed_at)
ORDER BY date DESC;

-- LEAD: Nasta rad
SELECT
    hostname,
    created_at,
    LEAD(created_at) OVER (ORDER BY created_at) AS next_created
FROM servers;
```

------------------------------------------------------------------

## FIRST_VALUE och LAST_VALUE

```sql
SELECT
    hostname,
    environment,
    created_at,
    FIRST_VALUE(hostname) OVER (
        PARTITION BY environment
        ORDER BY created_at
    ) AS oldest_server,
    LAST_VALUE(hostname) OVER (
        PARTITION BY environment
        ORDER BY created_at
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS newest_server
FROM servers;
```

VIKTIGT: LAST_VALUE kraver explicit frame for att fungera korrekt!

------------------------------------------------------------------

## Snabbreferens

| Function | Beskrivning | Anvandning |
|----------|-------------|------------|
| ROW_NUMBER() | Unik numrering | Paginering, deduplicering |
| RANK() | Ranking med gaps | Top-N med ties |
| DENSE_RANK() | Ranking utan gaps | Konsekutiv ranking |
| LAG(col, n) | Varde n rader bakut | Change detection |
| LEAD(col, n) | Varde n rader framat | Forecasting |
| SUM() OVER | Running/window sum | Kumulativa berakningar |
| AVG() OVER | Running/window avg | Moving averages |
| FIRST_VALUE() | Forsta i fonster | Min within group |
| LAST_VALUE() | Sista i fonster | Max within group |
| NTILE(n) | Dela i n buckets | Percentiler |

------------------------------------------------------------------

## Vanliga fel och losningar

### LAST_VALUE ger fel resultat

```sql
-- FEL - default frame ar RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
SELECT LAST_VALUE(hostname) OVER (ORDER BY created_at) AS newest
FROM servers;

-- RATT - explicit frame
SELECT LAST_VALUE(hostname) OVER (
    ORDER BY created_at
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
) AS newest
FROM servers;
```

### Window function i WHERE

```sql
-- FEL - window functions kan inte anvandas i WHERE
SELECT * FROM servers
WHERE ROW_NUMBER() OVER (ORDER BY created_at) <= 10;

-- RATT - anvand CTE eller subquery
WITH numbered AS (
    SELECT *, ROW_NUMBER() OVER (ORDER BY created_at) AS rn
    FROM servers
)
SELECT * FROM numbered WHERE rn <= 10;
```

------------------------------------------------------------------

## Praktisk ovning

```sql
-- DevOps Dashboard: Server ranking och trends
WITH daily_deploys AS (
    SELECT
        DATE(deployed_at) AS date,
        server_id,
        COUNT(*) AS deploys,
        COUNT(CASE WHEN status = 'success' THEN 1 END) AS successful
    FROM deployments
    WHERE deployed_at > NOW() - INTERVAL '30 days'
    GROUP BY DATE(deployed_at), server_id
),
ranked AS (
    SELECT
        date,
        server_id,
        deploys,
        successful,
        RANK() OVER (PARTITION BY date ORDER BY deploys DESC) AS daily_rank,
        SUM(deploys) OVER (PARTITION BY server_id ORDER BY date) AS running_total,
        LAG(deploys) OVER (PARTITION BY server_id ORDER BY date) AS prev_day
    FROM daily_deploys
)
SELECT
    date,
    server_id,
    deploys,
    daily_rank,
    running_total,
    deploys - COALESCE(prev_day, 0) AS change_from_prev
FROM ranked
WHERE daily_rank <= 5
ORDER BY date DESC, daily_rank;
```

------------------------------------------------------------------

## Key Takeaways

Kom ihag:

- CTEs gor komplexa queries lasbara - bryt ner i logiska steg
- Recursive CTEs for hierarkier - glom inte termineringsvillkor
- ROW_NUMBER ar alltid unik, RANK/DENSE_RANK hanterar ties olika
- PARTITION BY ar som GROUP BY men bevarar alla rader
- LAG/LEAD for att jamfora med foregaende/nasta rad
- SUM/AVG OVER for running totals och moving averages
- Window functions kan INTE anvandas i WHERE - anvand CTE
- LAST_VALUE kraver explicit ROWS BETWEEN frame
- Kombinera CTEs och window functions for kraftfulla analyser

Nasta steg: Node 10 - Views och Materialized Views
''',
}

NODE_10_VIEWS = {
    "node_id": 10,
    "title": "Views & Materialized Views",
    "slug": "views",
    "estimated_minutes": 45,
    "xp_reward": 130,
    "prerequisites": [5],
    "content": '''# Views och Materialized Views

Views ar sparade queries som beter sig som tabeller. De abstraherar komplexitet och ger ett konsistent granssnitt till underliggande data.

------------------------------------------------------------------

## Varfor viktigt for DevOps?

```
+-----------------------------------------------------------------+
|                    VIEW ANVANDNINGAR                            |
+-----------------------------------------------------------------+
|  Regular Views:                                                 |
|  - Forenkla komplexa JOINs for dashboards                      |
|  - Dolja kanslig data (kolumn-maskning)                        |
|  - Konsistent API mot foranderliga tabellstrukturer            |
+-----------------------------------------------------------------+
|  Materialized Views:                                            |
|  - Cacha dyra aggregeringar for dashboards                     |
|  - Pre-berakna rapporter som kors periodiskt                   |
|  - Snabba upp read-heavy workloads                             |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Regular Views

En view ar en namngiven query - ingen data lagras:

```sql
-- Enkel view
CREATE VIEW active_production_servers AS
SELECT
    id,
    hostname,
    ip_address,
    created_at
FROM servers
WHERE status = 'active'
  AND environment = 'production';

-- Anvanda view som tabell
SELECT * FROM active_production_servers;
SELECT COUNT(*) FROM active_production_servers;

-- View med JOIN
CREATE VIEW server_deployment_stats AS
SELECT
    s.id,
    s.hostname,
    s.environment,
    COUNT(d.id) AS deployment_count,
    MAX(d.deployed_at) AS last_deployment,
    COUNT(CASE WHEN d.status = 'failed' THEN 1 END) AS failed_count
FROM servers s
LEFT JOIN deployments d ON s.id = d.server_id
GROUP BY s.id, s.hostname, s.environment;

-- View med CTE och Window Functions
CREATE VIEW deployment_trends AS
WITH daily AS (
    SELECT
        DATE(deployed_at) AS date,
        COUNT(*) AS count
    FROM deployments
    GROUP BY DATE(deployed_at)
)
SELECT
    date,
    count,
    AVG(count) OVER (
        ORDER BY date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_7d
FROM daily;
```

------------------------------------------------------------------

## Updaterbara Views

Enkla views kan uppdateras direkt:

```sql
-- Enkel view utan JOINs/aggregat ar updatebar
CREATE VIEW active_servers AS
SELECT id, hostname, ip_address, status
FROM servers
WHERE status = 'active';

-- UPDATE fungerar - andrar underliggande tabell
UPDATE active_servers
SET ip_address = '10.0.0.50'
WHERE id = 1;

-- WITH CHECK OPTION - forhindra att rader "forsvinner" fran viewn
CREATE VIEW active_servers_checked AS
SELECT id, hostname, ip_address, status
FROM servers
WHERE status = 'active'
WITH CHECK OPTION;

-- Detta misslyckas - status = 'inactive' bryter viewns villkor
UPDATE active_servers_checked
SET status = 'inactive'  -- ERROR!
WHERE id = 1;
```

------------------------------------------------------------------

## Hantera Views

```sql
-- Ersatt befintlig view
CREATE OR REPLACE VIEW active_servers AS
SELECT id, hostname, ip_address, status, environment
FROM servers
WHERE status = 'active';

-- Ta bort view
DROP VIEW IF EXISTS active_servers;

-- Ta bort med beroenden (cascading)
DROP VIEW server_stats CASCADE;

-- Se view-definition
SELECT pg_get_viewdef('active_servers', true);
```

------------------------------------------------------------------

## Materialized Views

Materialized views sparar resultatet fysiskt - snabb lasning men maste refreshas:

```sql
-- Skapa materialized view
CREATE MATERIALIZED VIEW mv_deployment_stats AS
SELECT
    DATE(deployed_at) AS date,
    environment,
    COUNT(*) AS deployments,
    COUNT(CASE WHEN status = 'success' THEN 1 END) AS successful,
    ROUND(AVG(duration_seconds), 2) AS avg_duration
FROM deployments d
JOIN servers s ON d.server_id = s.id
GROUP BY DATE(deployed_at), environment;

-- Query ar snabb - laser fran sparad data
SELECT * FROM mv_deployment_stats
WHERE date > CURRENT_DATE - 7;

-- Manuell refresh - uppdaterar all data
REFRESH MATERIALIZED VIEW mv_deployment_stats;

-- Concurrent refresh - utan att blocka lasningar
-- Kraver UNIQUE INDEX!
CREATE UNIQUE INDEX mv_deploy_stats_idx
ON mv_deployment_stats(date, environment);

REFRESH MATERIALIZED VIEW CONCURRENTLY mv_deployment_stats;
```

------------------------------------------------------------------

## DevOps Dashboard Materialized View

```sql
-- Dashboard-cache for snabb rendering
CREATE MATERIALIZED VIEW mv_dashboard AS
SELECT
    environment,
    COUNT(*) AS total_servers,
    COUNT(CASE WHEN status = 'active' THEN 1 END) AS active,
    COUNT(CASE WHEN status = 'offline' THEN 1 END) AS offline,
    COUNT(CASE WHEN status = 'maintenance' THEN 1 END) AS maintenance,
    ROUND(100.0 * COUNT(CASE WHEN status = 'active' THEN 1 END) / COUNT(*), 1) AS uptime_pct
FROM servers
GROUP BY environment;

-- Index for snabba lookups
CREATE INDEX mv_dashboard_env_idx ON mv_dashboard(environment);

-- Refresh schema (kors via cron eller pg_cron)
-- Varje minut: REFRESH MATERIALIZED VIEW CONCURRENTLY mv_dashboard;
```

Scheduling refresh:

```sql
-- Med pg_cron extension
SELECT cron.schedule(
    'refresh-dashboard',
    '*/5 * * * *',  -- Var 5:e minut
    'REFRESH MATERIALIZED VIEW CONCURRENTLY mv_dashboard'
);
```

------------------------------------------------------------------

## Snabbreferens

| Egenskap | View | Materialized View |
|----------|------|-------------------|
| Data lagrad | Nej (virtuell) | Ja (fysisk) |
| Lashastighet | Beraknas varje gang | Mycket snabb |
| Dataaktualitet | Alltid aktuell | Kan vara gammal |
| Diskutrymme | Inget | Tar plats |
| Uppdatering | Automatisk | Manuell REFRESH |
| Indexering | Nej | Ja |
| UPDATE/INSERT | Ja (enkla views) | Nej |

------------------------------------------------------------------

## Vanliga fel och losningar

### Glommer CONCURRENTLY-krav

```sql
-- FEL - CONCURRENTLY kraver unique index
REFRESH MATERIALIZED VIEW CONCURRENTLY mv_stats;
-- ERROR: cannot refresh concurrently without unique index

-- RATT - skapa index forst
CREATE UNIQUE INDEX mv_stats_idx ON mv_stats(date, environment);
REFRESH MATERIALIZED VIEW CONCURRENTLY mv_stats;
```

### View blir for komplex

```sql
-- FEL - allt i en gigantisk view
CREATE VIEW mega_dashboard AS
SELECT ... -- 100 rader med JOINs och subqueries

-- BATTRE - bryt ner i mindre views
CREATE VIEW v_server_basics AS ...;
CREATE VIEW v_deployment_stats AS ...;
CREATE VIEW v_combined_dashboard AS
SELECT * FROM v_server_basics
JOIN v_deployment_stats USING (server_id);
```

------------------------------------------------------------------

## Praktisk ovning

```sql
-- 1. Skapa view for aktiva servrar med deployment-info
CREATE VIEW v_active_servers AS
SELECT
    s.id,
    s.hostname,
    s.environment,
    s.ip_address,
    COUNT(d.id) AS total_deploys,
    MAX(d.deployed_at) AS last_deploy,
    COUNT(CASE WHEN d.status = 'failed' AND d.deployed_at > NOW() - INTERVAL '7 days' THEN 1 END) AS recent_failures
FROM servers s
LEFT JOIN deployments d ON s.id = d.server_id
WHERE s.status = 'active'
GROUP BY s.id, s.hostname, s.environment, s.ip_address;

-- 2. Materialized view for vecko-rapport
CREATE MATERIALIZED VIEW mv_weekly_report AS
SELECT
    DATE_TRUNC('week', deployed_at) AS week,
    environment,
    COUNT(*) AS total_deployments,
    COUNT(CASE WHEN status = 'success' THEN 1 END) AS successful,
    ROUND(100.0 * COUNT(CASE WHEN status = 'success' THEN 1 END) / COUNT(*), 1) AS success_rate
FROM deployments d
JOIN servers s ON d.server_id = s.id
GROUP BY DATE_TRUNC('week', deployed_at), environment;

CREATE UNIQUE INDEX mv_weekly_idx ON mv_weekly_report(week, environment);
```

------------------------------------------------------------------

## Key Takeaways

Kom ihag:

- Views ar sparade queries - abstraherar komplexitet
- Enkla views utan JOINs/aggregat kan uppdateras direkt
- WITH CHECK OPTION forhindrar att rader "forsvinner" fran viewn
- Materialized views lagrar data fysiskt - maste refreshas
- REFRESH CONCURRENTLY kraver UNIQUE INDEX
- Anvand materialized views for dyra aggregeringar och dashboards
- Indexera materialized views for snabba lookups
- Bryt ner komplexa views i mindre, atervandningsbara delar
- Schemalag refresh av materialized views med pg_cron eller extern scheduler

Nasta steg: Node 11 - Transactions och Locking
''',
}

NODE_11_TRANSACTIONS = {
    "node_id": 11,
    "title": "Transactions & Locking",
    "slug": "transactions",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [4],
    "content": '''# Transactions och Locking

Transactions garanterar att en grupp databasoperationer antingen genomfors helt eller inte alls. ACID-principerna ar grundlaggande for dataintegritet.

------------------------------------------------------------------

## Varfor viktigt for DevOps?

```
+-----------------------------------------------------------------+
|                    TRANSACTION USE CASES                        |
+-----------------------------------------------------------------+
|  - Deployment registration: server + deployment maste lyckas   |
|  - Rollback vid fel: ingen halvfardid data                     |
|  - Job queues: hamta och lasa jobb atomiskt                    |
|  - Audit logging: operation + logg i samma transaktion         |
|  - Config updates: flera tabeller maste uppdateras tillsammans |
+-----------------------------------------------------------------+
```

Utan transactions kan ett avbrott lamna databasen i inkonsistent tillstand - t.ex. deployment registrerad men server inte uppdaterad.

------------------------------------------------------------------

## ACID-principerna

```
+-----------------------------------------------------------------+
|  A - Atomicity     Allt eller inget                            |
|                    Alla operationer lyckas eller alla rullas   |
|                    tillbaka                                     |
+-----------------------------------------------------------------+
|  C - Consistency   Alltid giltigt tillstand                    |
|                    Constraints, triggers, regler foljs         |
+-----------------------------------------------------------------+
|  I - Isolation     Transaktioner paverkar inte varandra        |
|                    Som om de kors sekventiellt                 |
+-----------------------------------------------------------------+
|  D - Durability    Committed data overlever crash              |
|                    Skrivet till disk innan COMMIT returnerar   |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Basic Transaction

```sql
BEGIN;

-- Steg 1: Registrera deployment
INSERT INTO deployments (server_id, version, status, deployed_at)
VALUES (1, 'v2.0.0', 'running', NOW())
RETURNING id;

-- Steg 2: Uppdatera server
UPDATE servers
SET current_version = 'v2.0.0',
    last_deployment = NOW()
WHERE id = 1;

-- Steg 3: Logga
INSERT INTO audit_log (action, entity_type, entity_id)
VALUES ('deploy', 'server', 1);

-- Allt OK - genomfor
COMMIT;
```

Vid fel:

```sql
BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Nagot gick fel - angra ALLT
ROLLBACK;
```

------------------------------------------------------------------

## Savepoints

Partiell rollback inom transaktion:

```sql
BEGIN;

-- Saker operation
UPDATE servers SET status = 'maintenance' WHERE id = 1;

SAVEPOINT before_risky;

-- Riskfylld operation
DELETE FROM logs WHERE server_id = 1 AND created_at < NOW() - INTERVAL '90 days';

-- Ops, for manga rader! Angra bara detta
ROLLBACK TO before_risky;

-- Fortsatt med annat
UPDATE servers SET status = 'active' WHERE id = 1;

COMMIT;  -- Endast maintenance->active sparas, DELETE angrad
```

------------------------------------------------------------------

## Isolation Levels

Hur mycket transaktioner "ser" av varandras andringar:

```
+----------------------+---------+--------------+---------+
| Isolation Level      | Dirty   | Non-repeat   | Phantom |
|                      | Read    | Read         | Read    |
+----------------------+---------+--------------+---------+
| Read Uncommitted     | Ja      | Ja           | Ja      |
| Read Committed *     | Nej     | Ja           | Ja      |
| Repeatable Read      | Nej     | Nej          | Ja      |
| Serializable         | Nej     | Nej          | Nej     |
+----------------------+---------+--------------+---------+
  * PostgreSQL default
```

```sql
-- Satt isolation level
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
-- ... operationer ...
COMMIT;

-- Eller efter BEGIN
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- ...
COMMIT;
```

DevOps-tumregel: Read Committed racker for de flesta fall. Anvand SERIALIZABLE for kritiska berakningar som maste vara 100% korrekta.

------------------------------------------------------------------

## Row-Level Locking

Lasa rader for att forhindra konkurrenta andringar:

```sql
-- FOR UPDATE: Exklusivt las for UPDATE/DELETE
SELECT * FROM servers
WHERE id = 1
FOR UPDATE;

-- FOR SHARE: Delat las (blockerar UPDATE men tillater lasning)
SELECT * FROM servers
WHERE id = 1
FOR SHARE;

-- NOWAIT: Misslyckas omedelbart om laset
SELECT * FROM servers
WHERE id = 1
FOR UPDATE NOWAIT;

-- SKIP LOCKED: Hoppa over lasta rader (perfekt for job queues!)
SELECT * FROM jobs
WHERE status = 'pending'
ORDER BY created_at
LIMIT 1
FOR UPDATE SKIP LOCKED;
```

------------------------------------------------------------------

## Job Queue Pattern

Klassiskt monster for distribuerad jobbhantering:

```sql
-- Worker hamtar och lasar ett jobb atomiskt
BEGIN;

SELECT id, payload FROM jobs
WHERE status = 'pending'
ORDER BY priority DESC, created_at
LIMIT 1
FOR UPDATE SKIP LOCKED;

-- Markera som paborjat
UPDATE jobs
SET status = 'processing',
    started_at = NOW(),
    worker_id = 'worker-1'
WHERE id = <job_id>;

COMMIT;

-- ... utfor jobbet ...

-- Markera som klart
UPDATE jobs
SET status = 'completed',
    completed_at = NOW()
WHERE id = <job_id>;
```

------------------------------------------------------------------

## Advisory Locks

Applikations-niva las (inte kopplade till rader):

```sql
-- Session-level lock (manuell release)
SELECT pg_advisory_lock(12345);
-- ... exklusivt arbete ...
SELECT pg_advisory_unlock(12345);

-- Transaction-level lock (auto-release vid COMMIT/ROLLBACK)
BEGIN;
SELECT pg_advisory_xact_lock(12345);
-- ... arbete ...
COMMIT;  -- Las slApps automatiskt

-- Try lock (icke-blockerande)
SELECT pg_try_advisory_lock(12345);  -- Returnerar true/false
```

Anvandning: Forhindra att flera processer kor samma batch-jobb samtidigt.

------------------------------------------------------------------

## Deadlock Prevention

Deadlock: Tva transaktioner vantar pa varandra.

```
Transaction 1:  Lock A -> Want B (waiting)
Transaction 2:  Lock B -> Want A (waiting)
= DEADLOCK!
```

Prevention-strategier:

```sql
-- 1. Lasa alltid i samma ordning
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;  -- Alltid lagst id forst
SELECT * FROM accounts WHERE id = 2 FOR UPDATE;
-- ...
COMMIT;

-- 2. Satt timeout
SET lock_timeout = '5s';

-- 3. Anvand NOWAIT for snabb fail
SELECT * FROM servers WHERE id = 1 FOR UPDATE NOWAIT;
```

------------------------------------------------------------------

## Snabbreferens

| Kommando | Beskrivning |
|----------|-------------|
| BEGIN | Starta transaktion |
| COMMIT | Genomfor alla andringar |
| ROLLBACK | Angra alla andringar |
| SAVEPOINT name | Skapa aterstallningspunkt |
| ROLLBACK TO name | Angra till savepoint |
| FOR UPDATE | Exklusivt radlas |
| FOR SHARE | Delat radlas |
| SKIP LOCKED | Hoppa over lasta rader |
| NOWAIT | Misslyckas om laset |
| pg_advisory_lock(id) | Applikationslas |

------------------------------------------------------------------

## Vanliga fel och losningar

### Glomd COMMIT

```sql
-- FEL - transaktion forblir oppen, lasen haller
BEGIN;
UPDATE servers SET status = 'active' WHERE id = 1;
-- ... glommer COMMIT ...
-- Andra sessions blockeras!

-- RATT - alltid COMMIT eller ROLLBACK
BEGIN;
UPDATE servers SET status = 'active' WHERE id = 1;
COMMIT;
```

### Deadlock

```sql
-- FEL - olika ordning i olika transaktioner
-- Session 1: Lock server 1, then 2
-- Session 2: Lock server 2, then 1

-- RATT - samma ordning overallt
-- Alltid: ORDER BY id, lasa i stigande ordning
```

------------------------------------------------------------------

## Praktisk ovning

```sql
-- Saker deployment-registrering
BEGIN;

-- Lasa servern
SELECT * FROM servers WHERE id = 1 FOR UPDATE;

-- Kontrollera status (applikationslogik)
-- IF status != 'active' THEN ROLLBACK

-- Registrera deployment
INSERT INTO deployments (server_id, version, status, deployed_at)
VALUES (1, 'v2.0.0', 'running', NOW())
RETURNING id;

-- Uppdatera server
UPDATE servers
SET current_version = 'v2.0.0',
    last_deployment = NOW(),
    status = 'deploying'
WHERE id = 1;

-- Allt OK
COMMIT;
```

------------------------------------------------------------------

## Key Takeaways

Kom ihag:

- ACID garanterar dataintegritet - Atomicity ar nyckeln
- BEGIN startar transaktion, COMMIT/ROLLBACK avslutar
- SAVEPOINT tillater partiell rollback inom transaktion
- Read Committed ar default och racker for de flesta fall
- FOR UPDATE lasar rader for exklusiv access
- SKIP LOCKED ar perfekt for job queues - hoppar over upptagna rader
- Advisory locks for applikations-niva koordinering
- Undvik deadlocks: lasa alltid resurser i samma ordning
- Satt lock_timeout for att undvika eviga vantan
- Glom aldrig COMMIT/ROLLBACK - oppna transaktioner blockerar

Nasta steg: Node 12 - Stored Procedures och Functions
''',
}

NODE_12_STORED_PROCS = {
    "node_id": 12,
    "title": "Stored Procedures & Functions",
    "slug": "stored-procs",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [11],
    "content": '''# Stored Procedures och Functions

Functions och procedures flyttar logik till databasen - minskar natverksrundturer, centraliserar affarslogik och mojliggor triggers for automatisering.

------------------------------------------------------------------

## Varfor viktigt for DevOps?

```
+-----------------------------------------------------------------+
|              FUNCTIONS & PROCEDURES USE CASES                   |
+-----------------------------------------------------------------+
|  Functions:                                                     |
|  - Berakna deployment success rate                             |
|  - Hamta server health metrics                                 |
|  - Validera input data                                         |
+-----------------------------------------------------------------+
|  Procedures:                                                    |
|  - Utfor deployment med flera steg                             |
|  - Rensa gamla loggar och data                                 |
|  - Batch-uppdateringar med commit-punkter                      |
+-----------------------------------------------------------------+
|  Triggers:                                                      |
|  - Automatisk audit logging                                    |
|  - Uppdatera updated_at timestamp                              |
|  - Validera data fore INSERT/UPDATE                            |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Function vs Procedure

```
+-----------------------------------------------------------------+
|  FUNCTION                      |  PROCEDURE (PostgreSQL 11+)   |
+--------------------------------+--------------------------------+
|  Returnerar varde/tabell       |  Returnerar void               |
|  Kan anvandas i SELECT         |  Anropas med CALL              |
|  Kan INTE COMMIT/ROLLBACK      |  KAN COMMIT/ROLLBACK           |
|  For berakningar och queries   |  For side effects och batch    |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Basic Functions

```sql
-- Enkel function - returnerar ett varde
CREATE OR REPLACE FUNCTION get_server_count()
RETURNS INTEGER AS $$
BEGIN
    RETURN (SELECT COUNT(*) FROM servers);
END;
$$ LANGUAGE plpgsql;

-- Anvandning
SELECT get_server_count();

-- Function med parametrar
CREATE OR REPLACE FUNCTION get_server_count_by_env(p_environment VARCHAR)
RETURNS INTEGER AS $$
DECLARE
    v_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO v_count
    FROM servers
    WHERE environment = p_environment;

    RETURN v_count;
END;
$$ LANGUAGE plpgsql;

-- Anvandning
SELECT get_server_count_by_env('production');
```

------------------------------------------------------------------

## Table-Returning Functions

```sql
-- Returnera tabell
CREATE OR REPLACE FUNCTION get_servers_by_status(p_status VARCHAR)
RETURNS TABLE(
    id INTEGER,
    hostname VARCHAR,
    ip_address INET,
    environment VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT s.id, s.hostname, s.ip_address, s.environment
    FROM servers s
    WHERE s.status = p_status;
END;
$$ LANGUAGE plpgsql;

-- Anvandning - som vanlig tabell!
SELECT * FROM get_servers_by_status('active')
WHERE environment = 'production';

-- Function med OUT-parametrar
CREATE OR REPLACE FUNCTION get_deployment_stats(
    p_server_id INTEGER,
    OUT total_deploys INTEGER,
    OUT successful INTEGER,
    OUT failed INTEGER,
    OUT success_rate NUMERIC
) AS $$
BEGIN
    SELECT
        COUNT(*),
        COUNT(CASE WHEN status = 'success' THEN 1 END),
        COUNT(CASE WHEN status = 'failed' THEN 1 END),
        ROUND(100.0 * COUNT(CASE WHEN status = 'success' THEN 1 END) / NULLIF(COUNT(*), 0), 2)
    INTO total_deploys, successful, failed, success_rate
    FROM deployments
    WHERE server_id = p_server_id;
END;
$$ LANGUAGE plpgsql;

-- Anvandning
SELECT * FROM get_deployment_stats(1);
```

------------------------------------------------------------------

## Procedures (PostgreSQL 11+)

Procedures kan hantera transactions internt:

```sql
-- Procedure for deployment
CREATE OR REPLACE PROCEDURE deploy_to_server(
    p_server_id INTEGER,
    p_version VARCHAR,
    p_engineer_id INTEGER
)
LANGUAGE plpgsql AS $$
DECLARE
    v_deployment_id INTEGER;
BEGIN
    -- Skapa deployment
    INSERT INTO deployments (server_id, version, status, engineer_id, deployed_at)
    VALUES (p_server_id, p_version, 'running', p_engineer_id, NOW())
    RETURNING id INTO v_deployment_id;

    -- Uppdatera server
    UPDATE servers
    SET current_version = p_version,
        last_deployment = NOW(),
        updated_at = NOW()
    WHERE id = p_server_id;

    -- Logga
    INSERT INTO audit_log (action, entity_type, entity_id, details)
    VALUES ('deploy', 'server', p_server_id,
            jsonb_build_object('version', p_version, 'deployment_id', v_deployment_id));

    COMMIT;
END;
$$;

-- Anropa med CALL
CALL deploy_to_server(1, 'v2.0.0', 42);
```

------------------------------------------------------------------

## Trigger Functions

Triggers kor automatiskt vid INSERT/UPDATE/DELETE:

```sql
-- Updated_at trigger (MYCKET vanlig)
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Koppla till tabell
CREATE TRIGGER set_updated_at
BEFORE UPDATE ON servers
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

-- Nu uppdateras updated_at automatiskt vid varje UPDATE!
UPDATE servers SET status = 'active' WHERE id = 1;
```

------------------------------------------------------------------

## Audit Trigger

```sql
-- Skapa audit-tabell
CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY,
    table_name VARCHAR(100),
    operation VARCHAR(10),
    old_data JSONB,
    new_data JSONB,
    changed_by VARCHAR(100),
    changed_at TIMESTAMP DEFAULT NOW()
);

-- Generisk audit trigger
CREATE OR REPLACE FUNCTION audit_trigger()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO audit_log (table_name, operation, new_data, changed_by)
        VALUES (TG_TABLE_NAME, 'INSERT', row_to_json(NEW)::jsonb, current_user);
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO audit_log (table_name, operation, old_data, new_data, changed_by)
        VALUES (TG_TABLE_NAME, 'UPDATE', row_to_json(OLD)::jsonb, row_to_json(NEW)::jsonb, current_user);
        RETURN NEW;
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO audit_log (table_name, operation, old_data, changed_by)
        VALUES (TG_TABLE_NAME, 'DELETE', row_to_json(OLD)::jsonb, current_user);
        RETURN OLD;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Koppla till tabeller
CREATE TRIGGER servers_audit
AFTER INSERT OR UPDATE OR DELETE ON servers
FOR EACH ROW EXECUTE FUNCTION audit_trigger();

CREATE TRIGGER deployments_audit
AFTER INSERT OR UPDATE OR DELETE ON deployments
FOR EACH ROW EXECUTE FUNCTION audit_trigger();
```

------------------------------------------------------------------

## Error Handling

```sql
CREATE OR REPLACE FUNCTION safe_deploy(
    p_server_id INTEGER,
    p_version VARCHAR
)
RETURNS BOOLEAN AS $$
DECLARE
    v_server_status VARCHAR;
BEGIN
    -- Hamta server status
    SELECT status INTO v_server_status
    FROM servers
    WHERE id = p_server_id;

    -- Validera
    IF v_server_status IS NULL THEN
        RAISE EXCEPTION 'Server % not found', p_server_id;
    END IF;

    IF v_server_status != 'active' THEN
        RAISE EXCEPTION 'Server % is not active (status: %)', p_server_id, v_server_status
            USING HINT = 'Set server to active before deploying';
    END IF;

    -- Utfor deployment
    INSERT INTO deployments (server_id, version, status)
    VALUES (p_server_id, p_version, 'running');

    RETURN TRUE;

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Deploy failed: % - %', SQLSTATE, SQLERRM;
        RETURN FALSE;
END;
$$ LANGUAGE plpgsql;
```

------------------------------------------------------------------

## Dynamic SQL

For flexibla queries:

```sql
CREATE OR REPLACE FUNCTION get_table_count(p_table_name TEXT)
RETURNS INTEGER AS $$
DECLARE
    v_count INTEGER;
BEGIN
    -- format() med %I escapar identifiers sakert
    EXECUTE format('SELECT COUNT(*) FROM %I', p_table_name)
    INTO v_count;

    RETURN v_count;
END;
$$ LANGUAGE plpgsql;

-- Anvandning
SELECT get_table_count('servers');
SELECT get_table_count('deployments');
```

VARNING: Anvand ALLTID format() med %I for tabellnamn for att undvika SQL injection!

------------------------------------------------------------------

## Snabbreferens

| Konstruktion | Beskrivning |
|--------------|-------------|
| CREATE FUNCTION | Skapa function |
| CREATE PROCEDURE | Skapa procedure (PG11+) |
| RETURNS type | Returtyp |
| RETURNS TABLE(...) | Returnera tabell |
| LANGUAGE plpgsql | PL/pgSQL sprak |
| DECLARE | Deklarera variabler |
| BEGIN...END | Funktionsblock |
| RETURN / RETURN QUERY | Returnera varde/rader |
| CALL procedure() | Anropa procedure |
| CREATE TRIGGER | Skapa trigger |
| NEW / OLD | Trigger-radvarden |
| TG_OP | Trigger operation (INSERT/UPDATE/DELETE) |
| RAISE EXCEPTION | Kasta fel |
| RAISE NOTICE | Logga meddelande |

------------------------------------------------------------------

## Vanliga fel och losningar

### Glommer RETURN i trigger

```sql
-- FEL - trigger returnerar inget
CREATE FUNCTION my_trigger() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log VALUES (...);
    -- Glommer RETURN!
END;

-- RATT - alltid returnera NEW, OLD eller NULL
CREATE FUNCTION my_trigger() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log VALUES (...);
    RETURN NEW;  -- For INSERT/UPDATE
    -- RETURN OLD;  -- For DELETE
END;
```

### SQL Injection i dynamic SQL

```sql
-- FEL - direkt string concatenation
EXECUTE 'SELECT * FROM ' || p_table_name;  -- FARLIGT!

-- RATT - anvand format() med %I
EXECUTE format('SELECT * FROM %I', p_table_name);  -- SAKERT
```

------------------------------------------------------------------

## Praktisk ovning

```sql
-- 1. Health check function
CREATE OR REPLACE FUNCTION check_server_health(p_server_id INTEGER)
RETURNS TABLE(
    hostname VARCHAR,
    status VARCHAR,
    last_deploy TIMESTAMP,
    deploy_count_30d INTEGER,
    failure_rate NUMERIC
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.hostname,
        s.status,
        MAX(d.deployed_at) AS last_deploy,
        COUNT(d.id)::INTEGER AS deploy_count_30d,
        ROUND(100.0 * COUNT(CASE WHEN d.status = 'failed' THEN 1 END) / NULLIF(COUNT(d.id), 0), 2)
    FROM servers s
    LEFT JOIN deployments d ON s.id = d.server_id
        AND d.deployed_at > NOW() - INTERVAL '30 days'
    WHERE s.id = p_server_id
    GROUP BY s.id, s.hostname, s.status;
END;
$$ LANGUAGE plpgsql;

-- 2. Cleanup procedure
CREATE OR REPLACE PROCEDURE cleanup_old_logs(p_days INTEGER DEFAULT 90)
LANGUAGE plpgsql AS $$
DECLARE
    v_deleted INTEGER;
BEGIN
    DELETE FROM audit_log
    WHERE changed_at < NOW() - (p_days || ' days')::INTERVAL;

    GET DIAGNOSTICS v_deleted = ROW_COUNT;

    RAISE NOTICE 'Deleted % old audit log entries', v_deleted;

    COMMIT;
END;
$$;

-- Anvandning
SELECT * FROM check_server_health(1);
CALL cleanup_old_logs(60);
```

------------------------------------------------------------------

## Key Takeaways

Kom ihag:

- Functions returnerar varden och kan anvandas i SELECT
- Procedures (PG11+) kan COMMIT/ROLLBACK internt - bra for batch
- RETURNS TABLE for functions som returnerar flera rader
- Triggers kor automatiskt vid INSERT/UPDATE/DELETE
- NEW innehaller nya varden, OLD innehaller gamla varden i triggers
- Returnera alltid NEW, OLD eller NULL fran triggers
- Anvand format() med %I for dynamiska tabellnamn - undviker SQL injection
- RAISE EXCEPTION for att kasta fel, RAISE NOTICE for loggning
- Error handling med EXCEPTION-block fangar och hanterar fel
- updated_at trigger ar extremt vanlig - implementera pa alla tabeller

Nasta steg: Node 13 - Indexing Fundamentals
''',
}

SQL_BLOCK_3 = [
    NODE_09_CTE_WINDOW,
    NODE_10_VIEWS,
    NODE_11_TRANSACTIONS,
    NODE_12_STORED_PROCS,
]
