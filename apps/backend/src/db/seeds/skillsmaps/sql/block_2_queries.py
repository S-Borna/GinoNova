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
    "content": '''
# SELECT Basics

Hämta data från databasen.

## Grundläggande SELECT

```sql
-- Alla kolumner
SELECT * FROM servers;

-- Specifika kolumner
SELECT hostname, ip_address, status
FROM servers;

-- Med alias
SELECT
    hostname AS server_name,
    ip_address AS ip,
    status
FROM servers;

-- Beräknade kolumner
SELECT
    hostname,
    created_at,
    NOW() - created_at AS age
FROM servers;
```

## WHERE

```sql
-- Equality
SELECT * FROM servers
WHERE status = 'active';

-- Comparison
SELECT * FROM servers
WHERE created_at > '2024-01-01';

-- IN
SELECT * FROM servers
WHERE status IN ('active', 'maintenance');

-- BETWEEN
SELECT * FROM servers
WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';

-- LIKE pattern matching
SELECT * FROM servers
WHERE hostname LIKE 'web%';      -- Börjar med 'web'
WHERE hostname LIKE '%01';       -- Slutar med '01'
WHERE hostname LIKE '%prod%';    -- Innehåller 'prod'
WHERE hostname LIKE 'web__';     -- web + 2 tecken

-- ILIKE (case-insensitive, PostgreSQL)
SELECT * FROM servers
WHERE hostname ILIKE '%WEB%';

-- NULL check
SELECT * FROM servers
WHERE ip_address IS NULL;

SELECT * FROM servers
WHERE ip_address IS NOT NULL;
```

## AND, OR, NOT

```sql
-- AND
SELECT * FROM servers
WHERE status = 'active'
  AND environment = 'production';

-- OR
SELECT * FROM servers
WHERE status = 'maintenance'
   OR status = 'offline';

-- Kombinerat (använd parenteser!)
SELECT * FROM servers
WHERE environment = 'production'
  AND (status = 'active' OR status = 'maintenance');

-- NOT
SELECT * FROM servers
WHERE NOT status = 'deleted';

SELECT * FROM servers
WHERE hostname NOT LIKE 'test%';
```

## ORDER BY

```sql
-- Ascending (default)
SELECT * FROM servers
ORDER BY hostname;

-- Descending
SELECT * FROM servers
ORDER BY created_at DESC;

-- Multiple columns
SELECT * FROM servers
ORDER BY status ASC, hostname DESC;

-- NULL handling
SELECT * FROM servers
ORDER BY ip_address NULLS LAST;
```

## LIMIT & OFFSET

```sql
-- Första 10
SELECT * FROM servers
LIMIT 10;

-- Pagination
SELECT * FROM servers
ORDER BY id
LIMIT 10 OFFSET 20;  -- Sida 3 (0-indexed)

-- Top N per kategori (med window function)
SELECT * FROM (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY environment ORDER BY created_at DESC) as rn
    FROM servers
) t
WHERE rn <= 5;
```

## DISTINCT

```sql
-- Unika värden
SELECT DISTINCT status
FROM servers;

-- Distinct on multiple columns
SELECT DISTINCT environment, status
FROM servers;

-- DISTINCT ON (PostgreSQL)
SELECT DISTINCT ON (environment) *
FROM servers
ORDER BY environment, created_at DESC;
```

| Clause | Syfte |
|--------|-------|
| SELECT | Välj kolumner |
| FROM | Källa |
| WHERE | Filter |
| ORDER BY | Sortering |
| LIMIT | Begränsa antal |
| DISTINCT | Unika värden |

**Nästa steg:** Node 6 - JOINs
''',
}

NODE_06_JOINS = {
    "node_id": 6,
    "title": "JOINs",
    "slug": "joins",
    "estimated_minutes": 60,
    "xp_reward": 155,
    "prerequisites": [5],
    "content": '''
# SQL JOINs

Kombinera data från flera tabeller.

## Setup Exempel

```sql
CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE engineers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    team_id INTEGER REFERENCES teams(id)
);

INSERT INTO teams VALUES (1, 'Platform'), (2, 'SRE'), (3, 'Empty Team');
INSERT INTO engineers VALUES
    (1, 'Alice', 1),
    (2, 'Bob', 1),
    (3, 'Charlie', 2),
    (4, 'Diana', NULL);  -- No team
```

## INNER JOIN

```sql
-- Endast matchande rader
SELECT e.name AS engineer, t.name AS team
FROM engineers e
INNER JOIN teams t ON e.team_id = t.id;

-- Resultat:
-- Alice    | Platform
-- Bob      | Platform
-- Charlie  | SRE
-- (Diana saknas - inget team_id)
-- (Empty Team saknas - inga engineers)
```

## LEFT JOIN

```sql
-- Alla från vänster, matchande från höger
SELECT e.name AS engineer, t.name AS team
FROM engineers e
LEFT JOIN teams t ON e.team_id = t.id;

-- Resultat:
-- Alice    | Platform
-- Bob      | Platform
-- Charlie  | SRE
-- Diana    | NULL      ← Inkluderad!
```

## RIGHT JOIN

```sql
-- Alla från höger, matchande från vänster
SELECT e.name AS engineer, t.name AS team
FROM engineers e
RIGHT JOIN teams t ON e.team_id = t.id;

-- Resultat:
-- Alice    | Platform
-- Bob      | Platform
-- Charlie  | SRE
-- NULL     | Empty Team  ← Inkluderad!
```

## FULL OUTER JOIN

```sql
-- Alla från båda sidor
SELECT e.name AS engineer, t.name AS team
FROM engineers e
FULL OUTER JOIN teams t ON e.team_id = t.id;

-- Resultat:
-- Alice    | Platform
-- Bob      | Platform
-- Charlie  | SRE
-- Diana    | NULL
-- NULL     | Empty Team
```

## Multiple JOINs

```sql
SELECT
    d.id AS deployment_id,
    s.hostname,
    e.name AS deployed_by,
    t.name AS team
FROM deployments d
JOIN servers s ON d.server_id = s.id
JOIN engineers e ON d.engineer_id = e.id
LEFT JOIN teams t ON e.team_id = t.id
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
-- 4 engineers × 3 teams = 12 rader
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
    "content": '''
# Aggregations & GROUP BY

Summera och gruppera data.

## Aggregate Functions

```sql
-- COUNT
SELECT COUNT(*) FROM servers;                    -- Alla rader
SELECT COUNT(ip_address) FROM servers;           -- Non-null
SELECT COUNT(DISTINCT status) FROM servers;      -- Unika

-- SUM
SELECT SUM(request_count) FROM metrics;

-- AVG
SELECT AVG(response_time) FROM metrics;

-- MIN / MAX
SELECT MIN(created_at), MAX(created_at) FROM servers;

-- STRING_AGG (PostgreSQL)
SELECT STRING_AGG(hostname, ', ') FROM servers
WHERE status = 'active';
-- Resultat: "web01, web02, web03"

-- ARRAY_AGG (PostgreSQL)
SELECT ARRAY_AGG(hostname) FROM servers;
-- Resultat: {web01,web02,web03}
```

## GROUP BY

```sql
-- Räkna per status
SELECT status, COUNT(*) as count
FROM servers
GROUP BY status;

-- Flera kolumner
SELECT environment, status, COUNT(*)
FROM servers
GROUP BY environment, status;

-- Med aggregat
SELECT
    environment,
    COUNT(*) as total_servers,
    COUNT(CASE WHEN status = 'active' THEN 1 END) as active_servers
FROM servers
GROUP BY environment;
```

## HAVING

```sql
-- Filter på aggregerade värden
SELECT status, COUNT(*) as count
FROM servers
GROUP BY status
HAVING COUNT(*) > 5;

-- Komplext exempel
SELECT
    team_id,
    AVG(salary) as avg_salary
FROM engineers
GROUP BY team_id
HAVING AVG(salary) > 100000
ORDER BY avg_salary DESC;
```

## WHERE vs HAVING

```sql
-- WHERE: Filtrerar FÖRE aggregering
-- HAVING: Filtrerar EFTER aggregering

SELECT environment, COUNT(*) as count
FROM servers
WHERE created_at > '2024-01-01'   -- Filter på rader
GROUP BY environment
HAVING COUNT(*) > 10;              -- Filter på grupper
```

## Praktiska Exempel

```sql
-- Deployments per dag
SELECT
    DATE(deployed_at) as deploy_date,
    COUNT(*) as deployments,
    COUNT(CASE WHEN status = 'success' THEN 1 END) as successful,
    ROUND(
        100.0 * COUNT(CASE WHEN status = 'success' THEN 1 END) / COUNT(*),
        2
    ) as success_rate
FROM deployments
WHERE deployed_at > NOW() - INTERVAL '30 days'
GROUP BY DATE(deployed_at)
ORDER BY deploy_date DESC;

-- Top 5 services by deployments
SELECT
    service_name,
    COUNT(*) as deploy_count,
    MAX(deployed_at) as last_deploy
FROM deployments
GROUP BY service_name
ORDER BY deploy_count DESC
LIMIT 5;

-- Servers per environment med status breakdown
SELECT
    environment,
    COUNT(*) as total,
    SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) as active,
    SUM(CASE WHEN status = 'maintenance' THEN 1 ELSE 0 END) as maintenance,
    SUM(CASE WHEN status = 'offline' THEN 1 ELSE 0 END) as offline
FROM servers
GROUP BY environment;
```

## ROLLUP & CUBE

```sql
-- ROLLUP: Subtotals + grand total
SELECT
    environment,
    status,
    COUNT(*)
FROM servers
GROUP BY ROLLUP(environment, status);

-- CUBE: Alla kombinationer
SELECT
    environment,
    status,
    COUNT(*)
FROM servers
GROUP BY CUBE(environment, status);
```

| Function | Beräknar |
|----------|----------|
| COUNT() | Antal rader |
| SUM() | Summa |
| AVG() | Medelvärde |
| MIN() | Minsta värde |
| MAX() | Största värde |
| STRING_AGG() | Konkatenera |

**Nästa steg:** Node 8 - Subqueries
''',
}

NODE_08_SUBQUERIES = {
    "node_id": 8,
    "title": "Subqueries",
    "slug": "subqueries",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [7],
    "content": '''
# Subqueries

Nästlade queries.

## Scalar Subquery

```sql
-- Returnerar ett värde
SELECT
    hostname,
    (SELECT COUNT(*) FROM deployments WHERE server_id = s.id) as deploy_count
FROM servers s;

-- I WHERE
SELECT * FROM servers
WHERE created_at > (
    SELECT AVG(created_at) FROM servers
);
```

## Subquery i WHERE

```sql
-- IN med subquery
SELECT * FROM servers
WHERE team_id IN (
    SELECT id FROM teams
    WHERE name LIKE '%Platform%'
);

-- NOT IN
SELECT * FROM servers
WHERE id NOT IN (
    SELECT server_id FROM deployments
    WHERE status = 'failed'
);

-- EXISTS
SELECT * FROM teams t
WHERE EXISTS (
    SELECT 1 FROM engineers e
    WHERE e.team_id = t.id
);

-- NOT EXISTS
SELECT * FROM servers s
WHERE NOT EXISTS (
    SELECT 1 FROM deployments d
    WHERE d.server_id = s.id
    AND d.deployed_at > NOW() - INTERVAL '30 days'
);
```

## Subquery i FROM (Derived Table)

```sql
-- Använda aggregat i WHERE
SELECT * FROM (
    SELECT
        team_id,
        COUNT(*) as member_count
    FROM engineers
    GROUP BY team_id
) team_stats
WHERE member_count > 5;

-- Komplexa beräkningar
SELECT
    env_stats.environment,
    env_stats.total_servers,
    env_stats.active_servers,
    ROUND(100.0 * env_stats.active_servers / env_stats.total_servers, 2) as active_pct
FROM (
    SELECT
        environment,
        COUNT(*) as total_servers,
        COUNT(CASE WHEN status = 'active' THEN 1 END) as active_servers
    FROM servers
    GROUP BY environment
) env_stats;
```

## Correlated Subquery

```sql
-- Refererar yttre query
SELECT s.*
FROM servers s
WHERE s.created_at = (
    SELECT MAX(s2.created_at)
    FROM servers s2
    WHERE s2.environment = s.environment
);

-- "Senaste deployment per server"
SELECT d.*
FROM deployments d
WHERE d.deployed_at = (
    SELECT MAX(d2.deployed_at)
    FROM deployments d2
    WHERE d2.server_id = d.server_id
);
```

## Lateral Join (PostgreSQL)

```sql
-- Subquery som kan referera yttre
SELECT s.hostname, latest.*
FROM servers s
CROSS JOIN LATERAL (
    SELECT deployed_at, status
    FROM deployments d
    WHERE d.server_id = s.id
    ORDER BY deployed_at DESC
    LIMIT 3
) latest;
```

## ANY / ALL

```sql
-- ANY: Minst en matchar
SELECT * FROM servers
WHERE created_at > ANY (
    SELECT deployed_at FROM deployments
    WHERE status = 'failed'
);

-- ALL: Alla måste matcha
SELECT * FROM servers
WHERE created_at > ALL (
    SELECT deployed_at FROM deployments
    WHERE status = 'failed'
);
```

## CTE vs Subquery

```sql
-- Subquery (svårläst)
SELECT * FROM (
    SELECT * FROM (
        SELECT * FROM servers
        WHERE status = 'active'
    ) active_servers
    WHERE environment = 'production'
) prod_active;

-- CTE (läsbart)
WITH active_servers AS (
    SELECT * FROM servers
    WHERE status = 'active'
),
prod_active AS (
    SELECT * FROM active_servers
    WHERE environment = 'production'
)
SELECT * FROM prod_active;
```

| Typ | Användning |
|-----|-----------|
| Scalar | Ett värde |
| IN/NOT IN | Jämför med lista |
| EXISTS | Kolla om rader finns |
| Derived table | Som datakälla |
| Correlated | Refererar yttre query |
| LATERAL | Avancerad korrelation |

**Nästa steg:** Node 9 - CTEs & Window Functions
''',
}

SQL_BLOCK_2 = [
    NODE_05_SELECT_BASICS,
    NODE_06_JOINS,
    NODE_07_AGGREGATIONS,
    NODE_08_SUBQUERIES,
]
