# =============================================================================
# BLOCK 1: SQL FUNDAMENTALS (Noder 1-4)
# =============================================================================

NODE_01_SQL_INTRO = {
    "node_id": 1,
    "title": "SQL Introduktion",
    "slug": "sql-intro",
    "estimated_minutes": 45,
    "xp_reward": 100,
    "prerequisites": [],
    "content": '''# 🗃️ SQL Introduktion

## Varför detta är kritiskt
> "SQL är språket som talar till all data. Som DevOps hanterar du databaser dagligen - migrations, backups, monitoring, debugging. Utan SQL är du blind."

## Vad du kommer lära dig
- ✅ SQL syntax och grundläggande queries
- ✅ PostgreSQL installation och setup
- ✅ DDL, DML, DCL och TCL kategorier
- ✅ Första tabeller och CRUD operations

---

## Databaser

| Databas | Användning |
|---------|-----------|
| PostgreSQL | Enterprise, DevOps favorit |
| MySQL | Webb, WordPress |
| SQLite | Embedded, lokal |
| SQL Server | Microsoft stack |

## Installation (PostgreSQL)

```bash
# macOS
brew install postgresql@16
brew services start postgresql@16

# Ubuntu
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql

# Docker
docker run -d --name postgres \\
  -e POSTGRES_PASSWORD=secret \\
  -p 5432:5432 \\
  postgres:16

# Anslut
psql -U postgres
```

## Första Queries

```sql
-- Skapa databas
CREATE DATABASE devops_db;

-- Anslut
\\c devops_db

-- Skapa tabell
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL,
    ip_address INET,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Infoga data
INSERT INTO servers (hostname, ip_address)
VALUES ('web01', '192.168.1.10');

-- Hämta data
SELECT * FROM servers;
```

## SQL Kategorier

| Kategori | Kommandon | Syfte |
|----------|-----------|-------|
| DDL | CREATE, ALTER, DROP | Struktur |
| DML | SELECT, INSERT, UPDATE, DELETE | Data |
| DCL | GRANT, REVOKE | Rättigheter |
| TCL | COMMIT, ROLLBACK | Transaktioner |

**Nästa steg:** Node 2 - Data Types
''',
}

NODE_02_DATA_TYPES = {
    "node_id": 2,
    "title": "Data Types",
    "slug": "data-types",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "prerequisites": [1],
    "content": '''# 📊 SQL Data Types

## Varför detta är viktigt
> "Rätt datatyp = rätt prestanda och dataintegritet. Fel val kan kosta dig TB i lagring eller millisekunder i query-tid."

## Vad du kommer lära dig
- ✅ Numeriska typer (INTEGER, DECIMAL, etc.)
- ✅ Text och binära typer
- ✅ Datum och tid
- ✅ Speciella typer (JSON, ARRAY, UUID)

---

## Numeriska

```sql
-- Heltal
SMALLINT        -- -32,768 to 32,767
INTEGER         -- -2B to 2B
BIGINT          -- Mycket stora tal
SERIAL          -- Auto-increment (PostgreSQL)

-- Decimaler
DECIMAL(10,2)   -- Exakt, för pengar
NUMERIC(10,2)   -- Samma som DECIMAL
REAL            -- 6 decimaler
DOUBLE PRECISION -- 15 decimaler

-- Exempel
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    quantity INTEGER NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    weight REAL
);
```

## Text

```sql
CHAR(n)         -- Fast längd, paddad
VARCHAR(n)      -- Variabel längd, max n
TEXT            -- Obegränsad längd

-- Exempel
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE,
    bio TEXT
);
```

## Datum & Tid

```sql
DATE            -- 2024-01-15
TIME            -- 14:30:00
TIMESTAMP       -- 2024-01-15 14:30:00
TIMESTAMPTZ     -- Med timezone (rekommenderat)
INTERVAL        -- Tidsperiod

-- Exempel
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    event_date DATE,
    start_time TIME,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Queries
SELECT * FROM events
WHERE event_date > CURRENT_DATE;

SELECT * FROM events
WHERE created_at > NOW() - INTERVAL '7 days';
```

## Boolean & Special

```sql
BOOLEAN         -- true/false/null
UUID            -- Universellt unikt ID
JSON / JSONB    -- JSON data (JSONB = binär)
ARRAY           -- Lista av värden
INET            -- IP-adress

-- Exempel
CREATE TABLE config (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    enabled BOOLEAN DEFAULT true,
    settings JSONB,
    allowed_ips INET[],
    tags TEXT[]
);

INSERT INTO config (settings, tags)
VALUES (
    '{"timeout": 30, "retries": 3}'::jsonb,
    ARRAY['production', 'critical']
);
```

## PostgreSQL Specifika

```sql
-- JSONB queries
SELECT * FROM config
WHERE settings->>'timeout' = '30';

SELECT * FROM config
WHERE settings @> '{"retries": 3}';

-- Array queries
SELECT * FROM config
WHERE 'production' = ANY(tags);
```

| Typ | Användning |
|-----|-----------|
| VARCHAR | Namn, email |
| TEXT | Beskrivningar |
| INTEGER | ID, räknare |
| DECIMAL | Pengar |
| TIMESTAMPTZ | Tidsstämplar |
| JSONB | Flexibel data |
| UUID | Distribuerade system |

**Nästa steg:** Node 3 - CREATE & ALTER
''',
}

NODE_03_DDL_CREATE = {
    "node_id": 3,
    "title": "CREATE & ALTER",
    "slug": "ddl-create",
    "estimated_minutes": 55,
    "xp_reward": 130,
    "prerequisites": [2],
    "content": '''# 🏗️ CREATE & ALTER - DDL

## Varför detta är kritiskt
> "Databasschema är fundamentet för din applikation. Ett dåligt schema = dålig prestanda och buggar för evigt."

## Vad du kommer lära dig
- ✅ CREATE TABLE med constraints
- ✅ Primary keys och foreign keys
- ✅ ALTER TABLE för schema changes
- ✅ Indexes för prestanda

---

## CREATE TABLE

```sql
CREATE TABLE deployments (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    version VARCHAR(20) NOT NULL,
    environment VARCHAR(20) NOT NULL,
    deployed_by VARCHAR(50),
    deployed_at TIMESTAMPTZ DEFAULT NOW(),
    status VARCHAR(20) DEFAULT 'pending',
    metadata JSONB,

    -- Constraints
    CONSTRAINT valid_env CHECK (
        environment IN ('dev', 'staging', 'prod')
    ),
    CONSTRAINT valid_status CHECK (
        status IN ('pending', 'running', 'success', 'failed')
    )
);

-- Med foreign key
CREATE TABLE deployment_logs (
    id SERIAL PRIMARY KEY,
    deployment_id INTEGER REFERENCES deployments(id) ON DELETE CASCADE,
    message TEXT NOT NULL,
    level VARCHAR(10) DEFAULT 'info',
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

## Constraints

```sql
-- Primary Key
id SERIAL PRIMARY KEY

-- Unique
email VARCHAR(255) UNIQUE

-- Not Null
username VARCHAR(50) NOT NULL

-- Default
created_at TIMESTAMPTZ DEFAULT NOW()

-- Check
CHECK (age >= 0 AND age < 150)

-- Foreign Key
REFERENCES other_table(id) ON DELETE CASCADE

-- Composite Primary Key
PRIMARY KEY (user_id, role_id)
```

## ALTER TABLE

```sql
-- Lägg till kolumn
ALTER TABLE deployments
ADD COLUMN rollback_version VARCHAR(20);

-- Ta bort kolumn
ALTER TABLE deployments
DROP COLUMN metadata;

-- Ändra datatyp
ALTER TABLE deployments
ALTER COLUMN version TYPE VARCHAR(50);

-- Lägg till constraint
ALTER TABLE deployments
ADD CONSTRAINT unique_deploy
UNIQUE (service_name, version, environment);

-- Ta bort constraint
ALTER TABLE deployments
DROP CONSTRAINT unique_deploy;

-- Rename kolumn
ALTER TABLE deployments
RENAME COLUMN deployed_by TO deployer;

-- Rename tabell
ALTER TABLE deployments
RENAME TO releases;
```

## DROP & TRUNCATE

```sql
-- Ta bort tabell helt
DROP TABLE IF EXISTS old_table;

-- Ta bort med beroenden
DROP TABLE deployments CASCADE;

-- Töm tabell (behåll struktur)
TRUNCATE TABLE logs;

-- Töm med reset av serial
TRUNCATE TABLE logs RESTART IDENTITY;
```

## Index

```sql
-- Skapa index
CREATE INDEX idx_deployments_service
ON deployments(service_name);

-- Unikt index
CREATE UNIQUE INDEX idx_users_email
ON users(email);

-- Composite index
CREATE INDEX idx_deployments_env_status
ON deployments(environment, status);

-- Partial index
CREATE INDEX idx_active_deployments
ON deployments(service_name)
WHERE status = 'running';
```

| Kommando | Syfte |
|----------|-------|
| CREATE TABLE | Skapa tabell |
| ALTER TABLE | Modifiera struktur |
| DROP TABLE | Ta bort tabell |
| TRUNCATE | Töm data |
| CREATE INDEX | Skapa index |

**Nästa steg:** Node 4 - INSERT, UPDATE, DELETE
''',
}

NODE_04_DML_BASICS = {
    "node_id": 4,
    "title": "INSERT, UPDATE, DELETE",
    "slug": "dml-basics",
    "estimated_minutes": 50,
    "xp_reward": 125,
    "prerequisites": [3],
    "content": '''# ✏️ INSERT, UPDATE, DELETE - DML

## Varför detta är viktigt
> "CRUD operations är bröd och smör i databashantering. Men UPDATE och DELETE utan WHERE kan förstöra hela din databas på sekunder."

## Vad du kommer lära dig
- ✅ INSERT med RETURNING
- ✅ UPDATE med säker WHERE
- ✅ DELETE och TRUNCATE
- ✅ UPSERT (ON CONFLICT)

---

## INSERT

```sql
-- Enkel insert
INSERT INTO servers (hostname, ip_address)
VALUES ('web01', '192.168.1.10');

-- Flera rader
INSERT INTO servers (hostname, ip_address) VALUES
    ('web02', '192.168.1.11'),
    ('web03', '192.168.1.12'),
    ('db01', '192.168.1.20');

-- Med alla kolumner explicit
INSERT INTO servers (id, hostname, ip_address, status, created_at)
VALUES (100, 'cache01', '192.168.1.30', 'active', NOW());

-- Returnera inserted data
INSERT INTO servers (hostname, ip_address)
VALUES ('web04', '192.168.1.13')
RETURNING id, hostname;

-- Insert från SELECT
INSERT INTO server_backups (server_id, hostname)
SELECT id, hostname FROM servers
WHERE status = 'active';
```

## UPDATE

```sql
-- Enkel update
UPDATE servers
SET status = 'maintenance'
WHERE hostname = 'web01';

-- Flera kolumner
UPDATE servers
SET
    status = 'active',
    updated_at = NOW()
WHERE id = 1;

-- Med RETURNING
UPDATE servers
SET status = 'inactive'
WHERE hostname LIKE 'old-%'
RETURNING id, hostname, status;

-- Update med JOIN (PostgreSQL)
UPDATE servers s
SET status = 'decommissioned'
FROM decommission_list d
WHERE s.id = d.server_id;

-- Conditional update
UPDATE servers
SET status = CASE
    WHEN last_seen < NOW() - INTERVAL '1 hour' THEN 'stale'
    WHEN last_seen < NOW() - INTERVAL '1 day' THEN 'offline'
    ELSE status
END;
```

## DELETE

```sql
-- Enkel delete
DELETE FROM servers
WHERE status = 'decommissioned';

-- Delete med RETURNING
DELETE FROM servers
WHERE hostname = 'old-web01'
RETURNING *;

-- Delete med subquery
DELETE FROM logs
WHERE server_id IN (
    SELECT id FROM servers
    WHERE status = 'deleted'
);

-- Delete alla (använd TRUNCATE istället)
DELETE FROM temp_data;
-- Bättre:
TRUNCATE TABLE temp_data;
```

## UPSERT (INSERT ON CONFLICT)

```sql
-- Insert or update
INSERT INTO servers (hostname, ip_address, status)
VALUES ('web01', '192.168.1.10', 'active')
ON CONFLICT (hostname)
DO UPDATE SET
    ip_address = EXCLUDED.ip_address,
    status = EXCLUDED.status,
    updated_at = NOW();

-- Insert or ignore
INSERT INTO servers (hostname, ip_address)
VALUES ('web01', '192.168.1.10')
ON CONFLICT (hostname)
DO NOTHING;
```

## Transaktioner

```sql
BEGIN;

UPDATE accounts SET balance = balance - 100
WHERE id = 1;

UPDATE accounts SET balance = balance + 100
WHERE id = 2;

-- Om allt OK
COMMIT;

-- Om fel
ROLLBACK;
```

| Operation | Syfte |
|-----------|-------|
| INSERT | Lägg till data |
| UPDATE | Modifiera data |
| DELETE | Ta bort data |
| UPSERT | Insert eller Update |
| TRUNCATE | Töm tabell snabbt |

**Nästa steg:** Node 5 - SELECT Basics
''',
}

SQL_BLOCK_1 = [
    NODE_01_SQL_INTRO,
    NODE_02_DATA_TYPES,
    NODE_03_DDL_CREATE,
    NODE_04_DML_BASICS,
]
