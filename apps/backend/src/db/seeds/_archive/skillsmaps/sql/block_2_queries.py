# =============================================================================
# BLOCK 2: QUERIES (Noder 5-8)
# =============================================================================

NODE_05_SELECT_BASICS = {
    "node_id": 5,
    "title": "SELECT Basics",
    "slug": "select-basics",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": [4],
    "content": '''# SELECT Basics

------------------------------------------------------------------

## Varfor viktigt for DevOps?

SELECT ar det absolut vanligaste SQL-kommandot. Att kunna skriva
effektiva queries ar skillnaden mellan millisekunder och minuter.
Som DevOps anvander du SELECT for monitoring, debugging, rapporter
och datautvinning fran loggar och metrics.

------------------------------------------------------------------

## SELECT Anatomy

```
+-----------------------------------------------------------------+
|                    SELECT STATEMENT                             |
+-----------------------------------------------------------------+
|                                                                 |
|  SELECT kolumn1, kolumn2, ...    <- Vilka kolumner               |
|  FROM tabell                      <- Fran vilken tabell          |
|  WHERE villkor                    <- Filtrera rader              |
|  ORDER BY kolumn                  <- Sortera resultat            |
|  LIMIT antal                      <- Begransar antal             |
|                                                                 |
|  Ordning av exekvering:                                         |
|  1. FROM   - Valj tabell                                       |
|  2. WHERE  - Filtrera rader                                    |
|  3. SELECT - Valj kolumner                                     |
|  4. ORDER BY - Sortera                                         |
|  5. LIMIT  - Begransar                                         |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Grundlaggande SELECT

### Alla kolumner

```sql
-- Hamta alla kolumner och rader
SELECT * FROM servers;

-- OBS: Undvik * i produktion - specificera kolumner!
```

### Specifika kolumner

```sql
-- Endast valda kolumner
SELECT hostname, ip_address, status
FROM servers;

-- Med alias for battre lasbarhet
SELECT
    hostname AS server_name,
    ip_address AS ip,
    status AS current_status
FROM servers;

-- Alias med mellanslag (kraver quotes)
SELECT
    hostname AS "Server Name",
    ip_address AS "IP Address"
FROM servers;
```

### Beraknade kolumner

```sql
-- Skapa nya kolumner med berakningar
SELECT
    hostname,
    cpu_cores,
    ram_gb,
    cpu_cores * 2 AS virtual_cpus,
    ram_gb * 1024 AS ram_mb
FROM servers;

-- Med datum-berakningar
SELECT
    hostname,
    created_at,
    NOW() - created_at AS age,
    EXTRACT(DAYS FROM NOW() - created_at) AS days_old
FROM servers;

-- Konkatenering
SELECT
    hostname || ' (' || ip_address || ')' AS server_info
FROM servers;

-- CONCAT function
SELECT
    CONCAT(hostname, ' - ', environment) AS description
FROM servers;
```

------------------------------------------------------------------

## WHERE - Filtrering

### Jamforelse-operatorer

```sql
-- Likhet
SELECT * FROM servers WHERE status = 'active';

-- Ej lika
SELECT * FROM servers WHERE status != 'deleted';
SELECT * FROM servers WHERE status <> 'deleted';  -- Alternativ syntax

-- Storre/mindre an
SELECT * FROM servers WHERE cpu_cores > 4;
SELECT * FROM servers WHERE ram_gb >= 16;
SELECT * FROM servers WHERE created_at < '2024-01-01';
```

### IN - Flera varden

```sql
-- Matcha mot lista
SELECT * FROM servers
WHERE status IN ('active', 'maintenance', 'standby');

-- Motsatsen
SELECT * FROM servers
WHERE environment NOT IN ('development', 'testing');
```

### BETWEEN - Intervall

```sql
-- Numeriskt intervall
SELECT * FROM servers
WHERE cpu_cores BETWEEN 4 AND 8;

-- Datum-intervall
SELECT * FROM deployments
WHERE deployed_at BETWEEN '2024-01-01' AND '2024-12-31';

-- Ekvivalent med
SELECT * FROM servers
WHERE cpu_cores >= 4 AND cpu_cores <= 8;
```

### LIKE - Pattern Matching

```sql
-- Borjar med
SELECT * FROM servers WHERE hostname LIKE 'web%';

-- Slutar med
SELECT * FROM servers WHERE hostname LIKE '%01';

-- Innehaller
SELECT * FROM servers WHERE hostname LIKE '%prod%';

-- Exakt antal tecken (underscore = 1 tecken)
SELECT * FROM servers WHERE hostname LIKE 'web__';  -- web01, web02...

-- ILIKE - Case-insensitive (PostgreSQL)
SELECT * FROM servers WHERE hostname ILIKE '%WEB%';

-- Escape special characters
SELECT * FROM configs WHERE value LIKE '%\\%%' ESCAPE '\\';  -- Sok efter %
```

### NULL-hantering

```sql
-- NULL kan INTE jamforas med =
SELECT * FROM servers WHERE ip_address = NULL;     -- FUNGERAR INTE!

-- Anvand IS NULL / IS NOT NULL
SELECT * FROM servers WHERE ip_address IS NULL;
SELECT * FROM servers WHERE ip_address IS NOT NULL;

-- COALESCE - default for NULL
SELECT
    hostname,
    COALESCE(ip_address::TEXT, 'No IP assigned') AS ip
FROM servers;
```

------------------------------------------------------------------

## Logiska operatorer - AND, OR, NOT

```sql
-- AND - Bada villkor maste vara sanna
SELECT * FROM servers
WHERE status = 'active'
  AND environment = 'production';

-- OR - Minst ett villkor maste vara sant
SELECT * FROM servers
WHERE status = 'maintenance'
   OR status = 'offline';

-- NOT - Negera villkor
SELECT * FROM servers
WHERE NOT status = 'deleted';

SELECT * FROM servers
WHERE hostname NOT LIKE 'test%';
```

### Prioritet och parenteser

```sql
-- VIKTIGT: AND har hogre prioritet an OR!
-- Utan parenteser:
SELECT * FROM servers
WHERE status = 'active' OR status = 'maintenance' AND environment = 'production';
-- Tolkas som: active OR (maintenance AND production)

-- Med parenteser - klar avsikt:
SELECT * FROM servers
WHERE (status = 'active' OR status = 'maintenance')
  AND environment = 'production';

-- Komplex logik
SELECT * FROM servers
WHERE environment = 'production'
  AND (
    status = 'active'
    OR (status = 'maintenance' AND scheduled_end < NOW())
  );
```

------------------------------------------------------------------

## ORDER BY - Sortering

```sql
-- Ascending (standard, kan utelamnas)
SELECT * FROM servers ORDER BY hostname ASC;
SELECT * FROM servers ORDER BY hostname;  -- Samma sak

-- Descending
SELECT * FROM servers ORDER BY created_at DESC;

-- Flera kolumner
SELECT * FROM servers
ORDER BY environment ASC, hostname DESC;

-- Sortera pa beraknad kolumn
SELECT
    hostname,
    cpu_cores * ram_gb AS compute_score
FROM servers
ORDER BY compute_score DESC;

-- Sortera pa kolumn-nummer (undvik i produktion)
SELECT hostname, ip_address, status FROM servers
ORDER BY 3;  -- Tredje kolumnen (status)

-- NULL-hantering i sortering
SELECT * FROM servers ORDER BY ip_address NULLS FIRST;
SELECT * FROM servers ORDER BY ip_address NULLS LAST;
```

------------------------------------------------------------------

## LIMIT och OFFSET - Paginering

```sql
-- Begransar antal resultat
SELECT * FROM servers LIMIT 10;

-- Paginering: OFFSET hoppar over rader
SELECT * FROM servers
ORDER BY id
LIMIT 10 OFFSET 0;   -- Sida 1 (rader 1-10)

SELECT * FROM servers
ORDER BY id
LIMIT 10 OFFSET 10;  -- Sida 2 (rader 11-20)

SELECT * FROM servers
ORDER BY id
LIMIT 10 OFFSET 20;  -- Sida 3 (rader 21-30)

-- Formel: OFFSET = (sidnummer - 1) * LIMIT
```

### Effektiv paginering for stora tabeller

```sql
-- Problem: OFFSET ar langsamt for stora tabeller
-- For sida 1000: databasen maste lasa 10000 rader

-- Losning: Keyset pagination (snabbare)
-- Forsta sidan
SELECT * FROM servers
ORDER BY id
LIMIT 10;

-- Nasta sida (anvand sista id fran foregaende)
SELECT * FROM servers
WHERE id > 1234  -- sista id fran foregaende query
ORDER BY id
LIMIT 10;
```

------------------------------------------------------------------

## DISTINCT - Unika varden

```sql
-- Unika varden i en kolumn
SELECT DISTINCT status FROM servers;

-- Unika kombinationer
SELECT DISTINCT environment, status FROM servers;

-- COUNT med DISTINCT
SELECT COUNT(DISTINCT environment) FROM servers;

-- DISTINCT ON (PostgreSQL) - forsta raden per grupp
SELECT DISTINCT ON (environment) *
FROM servers
ORDER BY environment, created_at DESC;
-- Ger nyaste servern per environment
```

------------------------------------------------------------------

## Snabbreferens

| Clause | Syntax | Beskrivning |
|--------|--------|-------------|
| SELECT | `SELECT col1, col2` | Valj kolumner |
| FROM | `FROM tabell` | Kalla |
| WHERE = | `WHERE col = 'val'` | Exakt matchning |
| WHERE IN | `WHERE col IN (...)` | Matcha lista |
| WHERE LIKE | `WHERE col LIKE '%pattern%'` | Monster |
| WHERE IS NULL | `WHERE col IS NULL` | Kolla NULL |
| AND/OR | `WHERE a AND b OR c` | Logik |
| ORDER BY | `ORDER BY col DESC` | Sortera |
| LIMIT | `LIMIT 10 OFFSET 20` | Paginera |
| DISTINCT | `SELECT DISTINCT col` | Unika |

------------------------------------------------------------------

## Vanliga fel och losningar

### Problem 1: NULL-jamforelse

```sql
-- FEL - returnerar inga rader!
SELECT * FROM servers WHERE ip_address = NULL;

-- RATT
SELECT * FROM servers WHERE ip_address IS NULL;
```

### Problem 2: OR utan parenteser

```sql
-- FEL - oforvantad logik
SELECT * FROM servers
WHERE environment = 'prod' OR environment = 'staging'
  AND status = 'active';
-- Tolkas som: prod OR (staging AND active)

-- RATT
SELECT * FROM servers
WHERE (environment = 'prod' OR environment = 'staging')
  AND status = 'active';

-- BATTRE - anvand IN
SELECT * FROM servers
WHERE environment IN ('prod', 'staging')
  AND status = 'active';
```

### Problem 3: LIKE med % i borjan

```sql
-- Langsamt - kan inte anvanda index
SELECT * FROM servers WHERE hostname LIKE '%prod%';

-- Snabbt - kan anvanda index
SELECT * FROM servers WHERE hostname LIKE 'prod%';

-- For full-text sok, anvand speciella index (GIN/GiST)
```

### Problem 4: SELECT * i produktion

```sql
-- FEL - hamtar onodiga kolumner
SELECT * FROM large_table;

-- RATT - specificera vad du behover
SELECT id, hostname, status FROM large_table;
```

------------------------------------------------------------------

## Praktisk ovning

Bygg en server-rapport:

```sql
-- 1. Aktiva produktions-servrar
SELECT hostname, ip_address, cpu_cores, ram_gb
FROM servers
WHERE environment = 'production'
  AND status = 'active'
ORDER BY hostname;

-- 2. Servrar skapade senaste 7 dagarna
SELECT *
FROM servers
WHERE created_at > NOW() - INTERVAL '7 days'
ORDER BY created_at DESC;

-- 3. Sok servrar med monster
SELECT hostname, environment
FROM servers
WHERE hostname LIKE 'web-%'
   OR hostname LIKE 'api-%'
ORDER BY environment, hostname;

-- 4. Top 10 servrar med mest RAM
SELECT hostname, environment, ram_gb
FROM servers
WHERE status = 'active'
ORDER BY ram_gb DESC
LIMIT 10;

-- 5. Servrar utan IP (behover konfigureras)
SELECT hostname, status, created_at
FROM servers
WHERE ip_address IS NULL
ORDER BY created_at;
```

------------------------------------------------------------------

## Key Takeaways

Kom ihag:

- Undvik SELECT * - specificera de kolumner du behover
- Anvand IS NULL/IS NOT NULL for NULL-kontroller, inte = NULL
- Anvand alltid parenteser med AND/OR for tydlig logik
- IN ar battre an flera OR for samma kolumn
- LIKE med % i borjan ar langsamt - kan inte anvanda index
- ORDER BY kravs for garanterad ordning - databaser lovar inte ordning
- Anvand keyset pagination istallet for OFFSET for stora dataset
- DISTINCT kan vara langsamt - overdag om det verkligen behovs

Nasta steg: Node 6 - JOINs
''',
}

NODE_06_JOINS = {
    "node_id": 6,
    "title": "JOINs",
    "slug": "joins",
    "estimated_minutes": 60,
    "xp_reward": 155,
    "prerequisites": [5],
    "content": '''# SQL JOINs

------------------------------------------------------------------

## Varfor viktigt for DevOps?

Relationsdatabaser ar designade for JOINs. Utan JOINs har du bara
spreadsheets. Med JOINs kan du kombinera data fran servrar, deployments,
loggar och anvandare i en enda kraftfull query. Forsta JOINs ar
fundamentalt for att bygga meningsfulla rapporter och dashboards.

------------------------------------------------------------------

## JOIN-typer Visualiserat

```
+-----------------------------------------------------------------+
|                     SQL JOIN TYPER                              |
+-----------------------------------------------------------------+
|                                                                 |
|  INNER JOIN                     LEFT JOIN                       |
|  +-----+-----+                  +-----+-----+                  |
|  |  A  |#####|  B  |            |#####|#####|  B  |            |
|  |     |#####|     |            |#####|#####|     |            |
|  +-----+-----+                  +-----+-----+                  |
|  Endast matchande               Alla A + matchande B            |
|                                                                 |
|  RIGHT JOIN                     FULL OUTER JOIN                 |
|  +-----+-----+                  +-----+-----+                  |
|  |  A  |#####|#####|            |#####|#####|#####|            |
|  |     |#####|#####|            |#####|#####|#####|            |
|  +-----+-----+                  +-----+-----+                  |
|  Alla B + matchande A           Alla fran bada                  |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Setup - Exempel-tabeller

```sql
-- Team-tabell
CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

-- Engineers med team-koppling
CREATE TABLE engineers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    team_id INTEGER REFERENCES teams(id)
);

-- Testdata
INSERT INTO teams VALUES
    (1, 'Platform'),
    (2, 'SRE'),
    (3, 'Empty Team');  -- Inget team-medlem

INSERT INTO engineers VALUES
    (1, 'Alice', 1),    -- Platform
    (2, 'Bob', 1),      -- Platform
    (3, 'Charlie', 2),  -- SRE
    (4, 'Diana', NULL); -- Inget team
```

------------------------------------------------------------------

## INNER JOIN

Returnerar endast rader som har matchning i BADA tabeller.

```sql
SELECT
    e.name AS engineer,
    t.name AS team
FROM engineers e
INNER JOIN teams t ON e.team_id = t.id;

-- Resultat:
-- engineer | team
-- ---------|----------
-- Alice    | Platform
-- Bob      | Platform
-- Charlie  | SRE
--
-- Diana saknas (inget team_id)
-- Empty Team saknas (inga engineers)
```

### Praktiskt DevOps-exempel

```sql
-- Deployments med server-info
SELECT
    d.id AS deploy_id,
    d.version,
    d.status,
    s.hostname,
    s.environment
FROM deployments d
INNER JOIN servers s ON d.server_id = s.id
WHERE d.deployed_at > NOW() - INTERVAL '24 hours';
```

------------------------------------------------------------------

## LEFT JOIN (LEFT OUTER JOIN)

Returnerar ALLA rader fran vanster tabell + matchande fran hoger.

```sql
SELECT
    e.name AS engineer,
    t.name AS team
FROM engineers e
LEFT JOIN teams t ON e.team_id = t.id;

-- Resultat:
-- engineer | team
-- ---------|----------
-- Alice    | Platform
-- Bob      | Platform
-- Charlie  | SRE
-- Diana    | NULL      <- Inkluderad trots inget team!
```

### Hitta rader UTAN matchning

```sql
-- Engineers utan team
SELECT e.name
FROM engineers e
LEFT JOIN teams t ON e.team_id = t.id
WHERE t.id IS NULL;

-- Servrar utan deployments
SELECT s.hostname
FROM servers s
LEFT JOIN deployments d ON s.id = d.server_id
WHERE d.id IS NULL;
```

------------------------------------------------------------------

## RIGHT JOIN (RIGHT OUTER JOIN)

Returnerar ALLA rader fran hoger tabell + matchande fran vanster.

```sql
SELECT
    e.name AS engineer,
    t.name AS team
FROM engineers e
RIGHT JOIN teams t ON e.team_id = t.id;

-- Resultat:
-- engineer | team
-- ---------|------------
-- Alice    | Platform
-- Bob      | Platform
-- Charlie  | SRE
-- NULL     | Empty Team  <- Inkluderat trots inga engineers!
```

Notera: RIGHT JOIN ar ovanligt - de flesta foredrar LEFT JOIN och
byter ordning pa tabellerna.

------------------------------------------------------------------

## FULL OUTER JOIN

Returnerar ALLA rader fran BADA tabeller.

```sql
SELECT
    e.name AS engineer,
    t.name AS team
FROM engineers e
FULL OUTER JOIN teams t ON e.team_id = t.id;

-- Resultat:
-- engineer | team
-- ---------|------------
-- Alice    | Platform
-- Bob      | Platform
-- Charlie  | SRE
-- Diana    | NULL        <- Engineer utan team
-- NULL     | Empty Team  <- Team utan engineers
```

### Hitta alla orphans

```sql
-- Rader som saknar matchning i NAGON tabell
SELECT
    e.name AS engineer,
    t.name AS team
FROM engineers e
FULL OUTER JOIN teams t ON e.team_id = t.id
WHERE e.id IS NULL OR t.id IS NULL;
```

------------------------------------------------------------------

## Multiple JOINs

```sql
-- Kombinera flera tabeller
SELECT
    d.id AS deployment_id,
    d.version,
    d.status,
    s.hostname,
    s.environment,
    e.name AS deployed_by,
    t.name AS team
FROM deployments d
INNER JOIN servers s ON d.server_id = s.id
INNER JOIN engineers e ON d.engineer_id = e.id
LEFT JOIN teams t ON e.team_id = t.id  -- Vad om engineer saknar team?
WHERE d.status = 'success'
  AND s.environment = 'production';
```

### JOIN-ordning spelar roll

```sql
-- Starta med "huvud"-tabellen
-- LEFT JOIN for optionella relationer
-- INNER JOIN for obligatoriska relationer

SELECT *
FROM deployments d                              -- Huvudtabell
INNER JOIN servers s ON d.server_id = s.id      -- Maste ha server
LEFT JOIN engineers e ON d.engineer_id = e.id   -- Kanske saknar engineer
LEFT JOIN deployment_logs l ON d.id = l.deployment_id;  -- Kanske inga loggar
```

------------------------------------------------------------------

## Self JOIN

Joina en tabell med sig sjalv.

```sql
-- Hitta engineers i samma team
SELECT
    e1.name AS engineer1,
    e2.name AS engineer2,
    t.name AS shared_team
FROM engineers e1
INNER JOIN engineers e2 ON e1.team_id = e2.team_id
INNER JOIN teams t ON e1.team_id = t.id
WHERE e1.id < e2.id;  -- Undvik dubbletter

-- Hierarki (manager/report)
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    manager_id INTEGER REFERENCES employees(id)
);

SELECT
    emp.name AS employee,
    mgr.name AS manager
FROM employees emp
LEFT JOIN employees mgr ON emp.manager_id = mgr.id;
```

------------------------------------------------------------------

## CROSS JOIN

Cartesian product - alla kombinationer.

```sql
-- Alla kombinationer
SELECT e.name, t.name
FROM engineers e
CROSS JOIN teams t;
-- 4 engineers x 3 teams = 12 rader

-- Praktiskt: Generera alla mojliga tilldelningar
SELECT
    s.hostname,
    time_slot
FROM servers s
CROSS JOIN generate_series(
    '2024-01-01'::date,
    '2024-01-07'::date,
    '1 day'::interval
) AS time_slot;
```

------------------------------------------------------------------

## JOIN Prestanda

### Index for JOIN-kolumner

```sql
-- Skapa index pa foreign keys!
CREATE INDEX idx_deployments_server ON deployments(server_id);
CREATE INDEX idx_deployments_engineer ON deployments(engineer_id);
CREATE INDEX idx_engineers_team ON engineers(team_id);
```

### Undvik N+1 med JOIN

```sql
-- FEL: N+1 queries (i applikationskod)
-- For varje deployment, gor en query for server...

-- RATT: En JOIN-query
SELECT d.*, s.hostname
FROM deployments d
JOIN servers s ON d.server_id = s.id;
```

### EXPLAIN for analys

```sql
EXPLAIN ANALYZE
SELECT d.*, s.hostname
FROM deployments d
JOIN servers s ON d.server_id = s.id;

-- Titta efter:
-- "Seq Scan" = full table scan (langsamt)
-- "Index Scan" = anvander index (snabbt)
-- "Nested Loop" vs "Hash Join" vs "Merge Join"
```

------------------------------------------------------------------

## Snabbreferens

| JOIN-typ | Returnerar | Anvandning |
|----------|------------|------------|
| INNER JOIN | Matchande fran bada | Standard-join |
| LEFT JOIN | Alla vanster + matchande hoger | Inkludera alla fran huvudtabell |
| RIGHT JOIN | Alla hoger + matchande vanster | Ovanligt, byt ordning istallet |
| FULL OUTER | Alla fran bada | Hitta orphans |
| CROSS JOIN | Alla kombinationer | Generera kombinationer |
| Self JOIN | Tabell med sig sjalv | Hierarkier |

------------------------------------------------------------------

## Vanliga fel och losningar

### Problem 1: Duplicerade rader

```sql
-- Manga-till-manga skapar dubbletter
SELECT u.name, r.role_name
FROM users u
JOIN user_roles ur ON u.id = ur.user_id
JOIN roles r ON ur.role_id = r.id;
-- Om user har 3 roles far du 3 rader per user

-- LOSNING: Aggregera roller
SELECT u.name, STRING_AGG(r.role_name, ', ') AS roles
FROM users u
JOIN user_roles ur ON u.id = ur.user_id
JOIN roles r ON ur.role_id = r.id
GROUP BY u.id, u.name;
```

### Problem 2: Felaktig JOIN-typ

```sql
-- INNER JOIN tappar rader
SELECT s.hostname, COUNT(d.id) AS deploy_count
FROM servers s
INNER JOIN deployments d ON s.id = d.server_id
GROUP BY s.id;
-- Servrar utan deployments visas INTE!

-- LOSNING: LEFT JOIN
SELECT s.hostname, COUNT(d.id) AS deploy_count
FROM servers s
LEFT JOIN deployments d ON s.id = d.server_id
GROUP BY s.id;
```

### Problem 3: JOIN utan index

```sql
-- Langsamt utan index
SELECT * FROM large_table a
JOIN another_large_table b ON a.foreign_key = b.id;

-- LOSNING: Skapa index
CREATE INDEX idx_foreign_key ON large_table(foreign_key);
```

### Problem 4: Cartesian product oavsiktligt

```sql
-- FEL: Glom ON-clause
SELECT * FROM servers, deployments;  -- CROSS JOIN!

-- RATT: Explicit ON-clause
SELECT * FROM servers s
JOIN deployments d ON s.id = d.server_id;
```

------------------------------------------------------------------

## Praktisk ovning

Bygg en deployment-rapport med JOINs:

```sql
-- 1. Senaste deployments med all info
SELECT
    d.id,
    d.version,
    d.status,
    s.hostname,
    s.environment,
    e.name AS deployer,
    t.name AS team,
    d.deployed_at
FROM deployments d
INNER JOIN servers s ON d.server_id = s.id
LEFT JOIN engineers e ON d.engineer_id = e.id
LEFT JOIN teams t ON e.team_id = t.id
WHERE d.deployed_at > NOW() - INTERVAL '7 days'
ORDER BY d.deployed_at DESC;

-- 2. Servrar som aldrig deployats till
SELECT s.hostname, s.environment, s.created_at
FROM servers s
LEFT JOIN deployments d ON s.id = d.server_id
WHERE d.id IS NULL;

-- 3. Engineers med antal deployments
SELECT
    e.name,
    t.name AS team,
    COUNT(d.id) AS deploy_count
FROM engineers e
LEFT JOIN teams t ON e.team_id = t.id
LEFT JOIN deployments d ON e.id = d.engineer_id
GROUP BY e.id, e.name, t.name
ORDER BY deploy_count DESC;
```

------------------------------------------------------------------

## Key Takeaways

Kom ihag:

- INNER JOIN returnerar endast matchande rader fran bada tabeller
- LEFT JOIN behaller alla rader fran vanster tabell
- Anvand LEFT JOIN + WHERE IS NULL for att hitta saknade relationer
- Skapa alltid index pa foreign key-kolumner for prestanda
- Var forsiktig med JOIN-ordning vid flera JOINs
- CROSS JOIN skapar cartesian product - anvand sparsamt
- Analysera queries med EXPLAIN ANALYZE for att hitta flaskhalsar
- Aggregera resultat med GROUP BY for att undvika dubbletter

WHERE d.status = 'success';
```

## Self JOIN

```sql
-- Hitta engineers i samma team
SELECT
    e1.name AS engineer1,
    e2.name AS engineer2,
    t.name AS team
FROM engineers e1
JOIN engineers e2 ON e1.team_id = e2.team_id AND e1.id < e2.id
JOIN teams t ON e1.team_id = t.id;
```

## CROSS JOIN

```sql
-- Alla kombinationer (cartesian product)
SELECT e.name, t.name
FROM engineers e
CROSS JOIN teams t;
-- 4 engineers x 3 teams = 12 rader
```

## JOIN vs Subquery

```sql
-- JOIN approach
SELECT s.hostname, COUNT(d.id) as deploy_count
FROM servers s
LEFT JOIN deployments d ON s.id = d.server_id
GROUP BY s.id;

-- Subquery approach
SELECT
    hostname,
    (SELECT COUNT(*) FROM deployments WHERE server_id = s.id) as deploy_count
FROM servers s;
```

| JOIN Type | Inkluderar |
|-----------|------------|
| INNER | Endast matchande |
| LEFT | Alla vänster + matchande höger |
| RIGHT | Alla höger + matchande vänster |
| FULL | Alla från båda |
| CROSS | Alla kombinationer |

**Nästa steg:** Node 7 - Aggregations
''',
}

NODE_07_AGGREGATIONS = {
    "node_id": 7,
    "title": "Aggregations & GROUP BY",
    "slug": "aggregations",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [6],
    "content": '''# Aggregations & GROUP BY

------------------------------------------------------------------

## Varfor viktigt for DevOps?

Aggregations omvandlar ra data till insikter. Hur manga servrar per
region? Genomsnittlig responstid? Max CPU-anvandning? Deploy success
rate? Utan aggregations ar din data bara siffror. Med aggregations
blir den information som driver beslut.

------------------------------------------------------------------

## Aggregation Oversikt

```
+-----------------------------------------------------------------+
|                  AGGREGATE FUNCTIONS                            |
+-----------------------------------------------------------------+
|                                                                 |
|  RAKNA                          BERAKNA                         |
|  +-- COUNT(*)     - Alla rader  +-- SUM(col)   - Summa         |
|  +-- COUNT(col)   - Non-NULL    +-- AVG(col)   - Medelvarde    |
|  +-- COUNT(DISTINCT col)        +-- MIN(col)   - Minimum       |
|                                 +-- MAX(col)   - Maximum       |
|                                                                 |
|  SAMLA (PostgreSQL)                                             |
|  +-- STRING_AGG(col, sep) - Konkatenera till string            |
|  +-- ARRAY_AGG(col)       - Samla till array                   |
|  +-- JSON_AGG(col)        - Samla till JSON                    |
|                                                                 |
|  Anvand med GROUP BY for per-kategori aggregation              |
|                                                                 |
+-----------------------------------------------------------------+
```

------------------------------------------------------------------

## Grundlaggande Aggregate Functions

### COUNT

```sql
-- Rakna alla rader
SELECT COUNT(*) FROM servers;

-- Rakna non-NULL varden
SELECT COUNT(ip_address) FROM servers;

-- Rakna unika varden
SELECT COUNT(DISTINCT status) FROM servers;
SELECT COUNT(DISTINCT environment) FROM servers;
```

### SUM, AVG, MIN, MAX

```sql
-- Summa
SELECT SUM(cpu_cores) AS total_cores FROM servers;
SELECT SUM(ram_gb) AS total_ram_gb FROM servers;

-- Medelvarde
SELECT AVG(response_time_ms) FROM metrics;
SELECT ROUND(AVG(cpu_usage), 2) AS avg_cpu FROM metrics;

-- Minimum och maximum
SELECT
    MIN(created_at) AS oldest_server,
    MAX(created_at) AS newest_server
FROM servers;

SELECT
    MIN(response_time_ms) AS fastest,
    MAX(response_time_ms) AS slowest,
    AVG(response_time_ms) AS average
FROM metrics
WHERE timestamp > NOW() - INTERVAL '1 hour';
```

### STRING_AGG och ARRAY_AGG (PostgreSQL)

```sql
-- Konkatenera till komma-separerad string
SELECT STRING_AGG(hostname, ', ') AS all_hosts
FROM servers
WHERE status = 'active';
-- Resultat: "web01, web02, web03, db01"

-- Med sortering
SELECT STRING_AGG(hostname, ', ' ORDER BY hostname)
FROM servers;

-- Samla till array
SELECT ARRAY_AGG(hostname) AS host_array
FROM servers
WHERE environment = 'production';
-- Resultat: {web01,web02,db01}

-- JSON aggregation
SELECT JSON_AGG(row_to_json(s)) AS servers_json
FROM servers s
WHERE status = 'active';
```

------------------------------------------------------------------

## GROUP BY

Grupperar rader och tillater aggregation per grupp.

```sql
-- Rakna per status
SELECT status, COUNT(*) AS count
FROM servers
GROUP BY status;

-- Resultat:
-- status      | count
-- ------------|-------
-- active      | 15
-- maintenance | 3
-- offline     | 2

-- Gruppera pa flera kolumner
SELECT environment, status, COUNT(*)
FROM servers
GROUP BY environment, status
ORDER BY environment, status;

-- Aggregera per grupp
SELECT
    environment,
    COUNT(*) AS total_servers,
    SUM(cpu_cores) AS total_cores,
    SUM(ram_gb) AS total_ram,
    ROUND(AVG(cpu_cores), 1) AS avg_cores
FROM servers
GROUP BY environment;
```

### GROUP BY med uttryck

```sql
-- Gruppera pa datum (inte timestamp)
SELECT
    DATE(deployed_at) AS deploy_date,
    COUNT(*) AS deployments
FROM deployments
GROUP BY DATE(deployed_at)
ORDER BY deploy_date DESC;

-- Gruppera pa manad
SELECT
    DATE_TRUNC('month', created_at) AS month,
    COUNT(*) AS new_servers
FROM servers
GROUP BY DATE_TRUNC('month', created_at)
ORDER BY month;

-- Gruppera pa beraknad kolumn
SELECT
    CASE
        WHEN ram_gb < 8 THEN 'small'
        WHEN ram_gb < 32 THEN 'medium'
        ELSE 'large'
    END AS size_category,
    COUNT(*) AS count
FROM servers
GROUP BY size_category;
```

------------------------------------------------------------------

## HAVING - Filtrera efter aggregering

WHERE filtrerar FORE aggregering.
HAVING filtrerar EFTER aggregering.

```sql
-- Hitta status med mer an 5 servrar
SELECT status, COUNT(*) AS count
FROM servers
GROUP BY status
HAVING COUNT(*) > 5;

-- Kombination av WHERE och HAVING
SELECT
    environment,
    COUNT(*) AS server_count,
    AVG(cpu_cores) AS avg_cores
FROM servers
WHERE status = 'active'           -- Filtrera fore aggregering
GROUP BY environment
HAVING COUNT(*) > 2               -- Filtrera efter aggregering
ORDER BY server_count DESC;

-- Hitta team med hog genomsnittslon
SELECT
    t.name AS team,
    COUNT(e.id) AS members,
    ROUND(AVG(e.salary), 0) AS avg_salary
FROM teams t
JOIN engineers e ON t.id = e.team_id
GROUP BY t.id, t.name
HAVING AVG(e.salary) > 100000
ORDER BY avg_salary DESC;
```

------------------------------------------------------------------

## Conditional Aggregation med CASE

```sql
-- Rakna med villkor
SELECT
    environment,
    COUNT(*) AS total,
    COUNT(CASE WHEN status = 'active' THEN 1 END) AS active,
    COUNT(CASE WHEN status = 'maintenance' THEN 1 END) AS maintenance,
    COUNT(CASE WHEN status = 'offline' THEN 1 END) AS offline
FROM servers
GROUP BY environment;

-- Berakna procent
SELECT
    environment,
    COUNT(*) AS total,
    ROUND(
        100.0 * COUNT(CASE WHEN status = 'active' THEN 1 END) / COUNT(*),
        1
    ) AS active_percent
FROM servers
GROUP BY environment;

-- Deployment success rate
SELECT
    DATE(deployed_at) AS date,
    COUNT(*) AS total,
    COUNT(CASE WHEN status = 'success' THEN 1 END) AS successful,
    COUNT(CASE WHEN status = 'failed' THEN 1 END) AS failed,
    ROUND(
        100.0 * COUNT(CASE WHEN status = 'success' THEN 1 END) / NULLIF(COUNT(*), 0),
        2
    ) AS success_rate
FROM deployments
WHERE deployed_at > NOW() - INTERVAL '30 days'
GROUP BY DATE(deployed_at)
ORDER BY date DESC;
```

------------------------------------------------------------------

## ROLLUP och CUBE

### ROLLUP - Subtotals

```sql
-- Subtotals och grand total
SELECT
    COALESCE(environment, 'TOTAL') AS environment,
    COALESCE(status, 'SUBTOTAL') AS status,
    COUNT(*) AS count
FROM servers
GROUP BY ROLLUP(environment, status);

-- Resultat inkluderar:
-- production  | active     | 10
-- production  | offline    | 2
-- production  | SUBTOTAL   | 12  <- subtotal per environment
-- staging     | active     | 5
-- staging     | SUBTOTAL   | 5
-- TOTAL       | SUBTOTAL   | 17  <- grand total
```

### CUBE - Alla kombinationer

```sql
-- Alla mojliga kombinationer
SELECT
    environment,
    status,
    COUNT(*)
FROM servers
GROUP BY CUBE(environment, status);

-- Ger subtotals for BADE environment och status
```

------------------------------------------------------------------

## Snabbreferens

| Funktion | Beskrivning | Exempel |
|----------|-------------|---------|
| COUNT(*) | Rakna alla rader | `SELECT COUNT(*) FROM t` |
| COUNT(col) | Rakna non-NULL | `SELECT COUNT(email) FROM t` |
| SUM(col) | Summa | `SELECT SUM(amount) FROM t` |
| AVG(col) | Medelvarde | `SELECT AVG(price) FROM t` |
| MIN(col) | Minimum | `SELECT MIN(date) FROM t` |
| MAX(col) | Maximum | `SELECT MAX(date) FROM t` |
| STRING_AGG | Konkatenera | `STRING_AGG(name, ', ')` |
| GROUP BY | Gruppera | `GROUP BY category` |
| HAVING | Filter aggregat | `HAVING COUNT(*) > 5` |

------------------------------------------------------------------

## Vanliga fel och losningar

### Problem 1: Kolumn inte i GROUP BY

```sql
-- FEL
SELECT hostname, status, COUNT(*)
FROM servers
GROUP BY status;
-- ERROR: column "hostname" must appear in GROUP BY clause

-- RATT - inkludera i GROUP BY eller aggregera
SELECT status, COUNT(*), STRING_AGG(hostname, ', ')
FROM servers
GROUP BY status;
```

### Problem 2: WHERE med aggregat

```sql
-- FEL
SELECT status, COUNT(*)
FROM servers
WHERE COUNT(*) > 5
GROUP BY status;
-- ERROR: aggregate functions not allowed in WHERE

-- RATT - anvand HAVING
SELECT status, COUNT(*)
FROM servers
GROUP BY status
HAVING COUNT(*) > 5;
```

### Problem 3: NULL i aggregation

```sql
-- COUNT(*) vs COUNT(col)
SELECT
    COUNT(*) AS total_rows,        -- Alla rader
    COUNT(ip_address) AS with_ip   -- Endast non-NULL
FROM servers;

-- AVG ignorerar NULL
SELECT AVG(response_time) FROM metrics;  -- NULL-rader ignoreras

-- Inkludera NULL som 0
SELECT AVG(COALESCE(response_time, 0)) FROM metrics;
```

### Problem 4: Division by zero

```sql
-- FEL - kan ge division by zero
SELECT
    successful / total AS rate
FROM ...;

-- RATT - anvand NULLIF
SELECT
    successful / NULLIF(total, 0) AS rate
FROM ...;
```

------------------------------------------------------------------

## Praktisk ovning

Bygg en DevOps dashboard-rapport:

```sql
-- 1. Server-inventering per environment
SELECT
    environment,
    COUNT(*) AS servers,
    SUM(cpu_cores) AS total_cores,
    SUM(ram_gb) AS total_ram_gb,
    STRING_AGG(DISTINCT status, ', ') AS statuses
FROM servers
GROUP BY environment
ORDER BY servers DESC;

-- 2. Daglig deployment-rapport
SELECT
    DATE(deployed_at) AS date,
    COUNT(*) AS total,
    COUNT(CASE WHEN status = 'success' THEN 1 END) AS success,
    COUNT(CASE WHEN status = 'failed' THEN 1 END) AS failed,
    ROUND(100.0 * COUNT(CASE WHEN status = 'success' THEN 1 END) / COUNT(*), 1) AS success_pct
FROM deployments
WHERE deployed_at > NOW() - INTERVAL '7 days'
GROUP BY DATE(deployed_at)
ORDER BY date DESC;

-- 3. Top deployers denna manad
SELECT
    e.name AS engineer,
    COUNT(d.id) AS deployments,
    COUNT(CASE WHEN d.status = 'success' THEN 1 END) AS successful
FROM engineers e
JOIN deployments d ON e.id = d.engineer_id
WHERE d.deployed_at > DATE_TRUNC('month', NOW())
GROUP BY e.id, e.name
HAVING COUNT(d.id) > 0
ORDER BY deployments DESC
LIMIT 10;
```

------------------------------------------------------------------

## Key Takeaways

Kom ihag:

- COUNT(*) raknar alla rader, COUNT(col) raknar non-NULL
- GROUP BY kraver att alla icke-aggregerade kolumner finns med
- WHERE filtrerar fore aggregering, HAVING filtrerar efter
- Anvand CASE inuti aggregat for conditional counting
- STRING_AGG ar kraftfullt for att skapa kommaseparerade listor
- NULLIF(x, 0) forhindrar division by zero
- ROLLUP ger subtotals, CUBE ger alla kombinationer
- Aggregat ignorerar NULL-varden (utom COUNT(*))

Nasta steg: Node 8 - Subqueries
''',
}

NODE_08_SUBQUERIES = {
    "node_id": 8,
    "title": "Subqueries",
    "slug": "subqueries",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [7],
    "content": '''# Subqueries

Subqueries ar queries inuti andra queries - ett av de mest kraftfulla verktygen i SQL for att bygga komplexa datahamtningar steg for steg.

------------------------------------------------------------------

## Varfor viktigt for DevOps?

```
+-----------------------------------------------------------------+
|                    SUBQUERY ANVANDNINGAR                        |
+-----------------------------------------------------------------+
|  "Hitta servrar utan deployments senaste 30 dagarna"           |
|  "Visa bara teams med fler an 5 medlemmar"                     |
|  "Jamfor server metrics mot genomsnitt"                        |
|  "Filtrera pa aggregerade varden"                              |
+-----------------------------------------------------------------+
```

Som DevOps-ingenjor behover du ofta svara pa fragor som kraver
flera steg: "Vilka servrar har aldrig haft en lyckad deployment?"
eller "Visa alerts for servrar over genomsnittsbelastning."

------------------------------------------------------------------

## Subquery-typer oversikt

```
+------------------+------------------+------------------+
|  SCALAR          |  TABLE           |  CORRELATED      |
|  Returnerar      |  Returnerar      |  Refererar       |
|  ETT varde       |  RADER           |  yttre query     |
+------------------+------------------+------------------+
|  SELECT          |  IN / NOT IN     |  Kors for        |
|  (subquery)      |  EXISTS          |  varje rad       |
|  as column       |  FROM (derived)  |  i yttre query   |
+------------------+------------------+------------------+
```

------------------------------------------------------------------

## Scalar Subquery

Returnerar exakt ETT varde - anvands som kolumn eller i jamforelser:

```sql
-- Som kolumn - rakna deployments per server
SELECT
    hostname,
    environment,
    (SELECT COUNT(*)
     FROM deployments
     WHERE server_id = s.id) AS deploy_count
FROM servers s;

-- I WHERE - servrar skapade efter genomsnitt
SELECT * FROM servers
WHERE created_at > (
    SELECT AVG(created_at) FROM servers
);

-- I SELECT - jamfor mot total
SELECT
    hostname,
    cpu_cores,
    (SELECT SUM(cpu_cores) FROM servers) AS total_cores,
    ROUND(100.0 * cpu_cores / (SELECT SUM(cpu_cores) FROM servers), 2) AS pct
FROM servers;
```

------------------------------------------------------------------

## IN och NOT IN

Filtrera baserat pa en lista fran subquery:

```sql
-- IN: Servrar som tillhor Platform-teams
SELECT * FROM servers
WHERE team_id IN (
    SELECT id FROM teams
    WHERE name LIKE '%Platform%'
);

-- NOT IN: Servrar utan misslyckade deployments
SELECT * FROM servers
WHERE id NOT IN (
    SELECT server_id
    FROM deployments
    WHERE status = 'failed'
    AND server_id IS NOT NULL  -- VIKTIGT! NULL-hantering
);

-- Multipla kolumner (PostgreSQL)
SELECT * FROM deployments
WHERE (server_id, engineer_id) IN (
    SELECT s.id, s.team_lead_id
    FROM servers s
);
```

VARNING: NOT IN med NULL-varden ger ovantat resultat!

```sql
-- Om subquery innehaller NULL returneras INGA rader
-- Anvand NOT EXISTS istallet for sakerhet
```

------------------------------------------------------------------

## EXISTS och NOT EXISTS

Kontrollera om rader finns - ofta snabbare an IN:

```sql
-- EXISTS: Teams med minst en ingenjor
SELECT * FROM teams t
WHERE EXISTS (
    SELECT 1 FROM engineers e
    WHERE e.team_id = t.id
);

-- NOT EXISTS: Servrar utan nyliga deployments
SELECT * FROM servers s
WHERE NOT EXISTS (
    SELECT 1 FROM deployments d
    WHERE d.server_id = s.id
    AND d.deployed_at > NOW() - INTERVAL '30 days'
);

-- EXISTS vs IN performance
-- EXISTS stannar vid forsta traff
-- IN laddar hela listan forst
```

EXISTS-queryn returnerar bara 1 - vardet spelar ingen roll, bara att raden finns.

------------------------------------------------------------------

## Derived Tables (Subquery i FROM)

Anvand subquery som en virtuell tabell:

```sql
-- Filtrera pa aggregat (kan inte goras i WHERE direkt)
SELECT * FROM (
    SELECT
        team_id,
        COUNT(*) AS member_count,
        AVG(years_experience) AS avg_experience
    FROM engineers
    GROUP BY team_id
) team_stats
WHERE member_count > 5
AND avg_experience > 3;

-- DevOps: Server health per environment
SELECT
    env_stats.environment,
    env_stats.total_servers,
    env_stats.active_servers,
    ROUND(100.0 * env_stats.active_servers / env_stats.total_servers, 2) AS active_pct
FROM (
    SELECT
        environment,
        COUNT(*) AS total_servers,
        COUNT(CASE WHEN status = 'active' THEN 1 END) AS active_servers
    FROM servers
    GROUP BY environment
) env_stats
ORDER BY active_pct DESC;
```

------------------------------------------------------------------

## Correlated Subqueries

Refererar yttre query - kors for VARJE rad:

```sql
-- Senaste server per environment
SELECT s.*
FROM servers s
WHERE s.created_at = (
    SELECT MAX(s2.created_at)
    FROM servers s2
    WHERE s2.environment = s.environment
);

-- Senaste deployment per server
SELECT d.*
FROM deployments d
WHERE d.deployed_at = (
    SELECT MAX(d2.deployed_at)
    FROM deployments d2
    WHERE d2.server_id = d.server_id
);

-- Engineers med fler deployments an team-genomsnitt
SELECT e.name, e.team_id,
    (SELECT COUNT(*) FROM deployments WHERE engineer_id = e.id) AS my_deploys
FROM engineers e
WHERE (SELECT COUNT(*) FROM deployments WHERE engineer_id = e.id) > (
    SELECT AVG(deploy_count) FROM (
        SELECT COUNT(*) AS deploy_count
        FROM deployments d2
        JOIN engineers e2 ON d2.engineer_id = e2.id
        WHERE e2.team_id = e.team_id
        GROUP BY d2.engineer_id
    ) team_avg
);
```

VARNING: Correlated subqueries kan vara lAngsamma - overväg JOIN eller CTE.

------------------------------------------------------------------

## LATERAL Join (PostgreSQL)

Som correlated subquery men mer flexibel:

```sql
-- Senaste 3 deployments per server
SELECT s.hostname, latest.*
FROM servers s
CROSS JOIN LATERAL (
    SELECT deployed_at, status, version
    FROM deployments d
    WHERE d.server_id = s.id
    ORDER BY deployed_at DESC
    LIMIT 3
) latest;

-- Med LEFT JOIN LATERAL (inkludera servrar utan deployments)
SELECT s.hostname, COALESCE(latest.deploy_count, 0) AS deploys
FROM servers s
LEFT JOIN LATERAL (
    SELECT COUNT(*) AS deploy_count
    FROM deployments d
    WHERE d.server_id = s.id
    AND d.deployed_at > NOW() - INTERVAL '7 days'
) latest ON true;
```

------------------------------------------------------------------

## ANY och ALL

Jamfor mot subquery-resultat:

```sql
-- ANY: Sant om MINST EN rad matchar
SELECT * FROM servers
WHERE cpu_cores > ANY (
    SELECT cpu_cores FROM servers WHERE environment = 'production'
);
-- Samma som: WHERE cpu_cores > MIN(production cores)

-- ALL: Sant om ALLA rader matchar
SELECT * FROM servers
WHERE created_at > ALL (
    SELECT deployed_at FROM deployments WHERE status = 'failed'
);
-- Samma som: WHERE created_at > MAX(failed deployment dates)

-- = ANY ar samma som IN
SELECT * FROM servers
WHERE environment = ANY (ARRAY['production', 'staging']);
```

------------------------------------------------------------------

## Snabbreferens

| Subquery-typ | Syntax | Anvandning |
|--------------|--------|------------|
| Scalar | SELECT (SELECT ...) | Enskilt varde som kolumn |
| IN | WHERE col IN (SELECT ...) | Matcha mot lista |
| NOT IN | WHERE col NOT IN (SELECT ...) | Exkludera lista (akta NULL!) |
| EXISTS | WHERE EXISTS (SELECT ...) | Kontrollera om rader finns |
| NOT EXISTS | WHERE NOT EXISTS (SELECT ...) | Kontrollera att rader saknas |
| Derived | FROM (SELECT ...) AS alias | Subquery som tabell |
| Correlated | WHERE col = (SELECT ... WHERE outer.col) | Refererar yttre query |
| LATERAL | CROSS/LEFT JOIN LATERAL | Flexibel korrelation |
| ANY | WHERE col > ANY (SELECT ...) | Jamfor mot nagon rad |
| ALL | WHERE col > ALL (SELECT ...) | Jamfor mot alla rader |

------------------------------------------------------------------

## Vanliga fel och losningar

### NOT IN med NULL

```sql
-- FEL - returnerar inga rader om subquery har NULL
SELECT * FROM servers
WHERE id NOT IN (SELECT server_id FROM deployments);

-- RATT - filtrera bort NULL eller anvand NOT EXISTS
SELECT * FROM servers s
WHERE NOT EXISTS (
    SELECT 1 FROM deployments d WHERE d.server_id = s.id
);
```

### Correlated subquery i SELECT

```sql
-- FEL - korrelerad subquery kors per rad (langsamt)
SELECT
    hostname,
    (SELECT COUNT(*) FROM deployments WHERE server_id = servers.id)
FROM servers;

-- BATTRE - anvand JOIN
SELECT s.hostname, COUNT(d.id) AS deploy_count
FROM servers s
LEFT JOIN deployments d ON s.id = d.server_id
GROUP BY s.id, s.hostname;
```

### Multipla subqueries som gor samma sak

```sql
-- FEL - samma subquery upprepas
SELECT
    (SELECT COUNT(*) FROM deployments) AS total,
    (SELECT COUNT(*) FROM deployments WHERE status = 'success') AS success;

-- BATTRE - en query med conditional aggregat
SELECT
    COUNT(*) AS total,
    COUNT(CASE WHEN status = 'success' THEN 1 END) AS success
FROM deployments;
```

------------------------------------------------------------------

## Praktisk ovning

Bygg subqueries for DevOps-analys:

```sql
-- 1. Servrar utan deployment senaste 7 dagarna
SELECT hostname, environment, last_deployment
FROM servers s
WHERE NOT EXISTS (
    SELECT 1 FROM deployments d
    WHERE d.server_id = s.id
    AND d.deployed_at > NOW() - INTERVAL '7 days'
);

-- 2. Teams med success rate under genomsnitt
WITH team_rates AS (
    SELECT
        t.name AS team_name,
        COUNT(d.id) AS total_deploys,
        COUNT(CASE WHEN d.status = 'success' THEN 1 END) AS successful,
        100.0 * COUNT(CASE WHEN d.status = 'success' THEN 1 END) / NULLIF(COUNT(d.id), 0) AS rate
    FROM teams t
    JOIN engineers e ON t.id = e.team_id
    JOIN deployments d ON e.id = d.engineer_id
    GROUP BY t.id, t.name
)
SELECT * FROM team_rates
WHERE rate < (SELECT AVG(rate) FROM team_rates);

-- 3. Top 3 senaste deployments per server (LATERAL)
SELECT s.hostname, deploys.*
FROM servers s
CROSS JOIN LATERAL (
    SELECT version, status, deployed_at
    FROM deployments d
    WHERE d.server_id = s.id
    ORDER BY deployed_at DESC
    LIMIT 3
) deploys
ORDER BY s.hostname, deploys.deployed_at DESC;
```

------------------------------------------------------------------

## Key Takeaways

Kom ihag:

- Scalar subquery returnerar ETT varde - anvands i SELECT eller WHERE
- EXISTS ar ofta snabbare an IN - stannar vid forsta traff
- NOT IN med NULL returnerar inga rader - anvand NOT EXISTS istallet
- Derived tables later dig filtrera pa aggregat i WHERE
- Correlated subqueries kors per rad - kan vara langsamma
- LATERAL ar Postgres-specifik men mycket kraftfull
- ANY matchar minst en rad, ALL matchar alla rader
- Overväg CTE for lasbarhet vid komplexa nestade subqueries
- Subqueries i SELECT gar ofta att ersatta med JOIN for battre prestanda

Nasta steg: Node 9 - CTEs och rekursiva queries
''',
}

SQL_BLOCK_2 = [
    NODE_05_SELECT_BASICS,
    NODE_06_JOINS,
    NODE_07_AGGREGATIONS,
    NODE_08_SUBQUERIES,
]
