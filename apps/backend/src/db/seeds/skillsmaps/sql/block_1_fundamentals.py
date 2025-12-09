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
    "content": '''# SQL Introduktion

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

SQL ar spraket som kommunicerar med all data. Som DevOps-ingenjor hanterar
du databaser dagligen - migrations, backups, monitoring och debugging.
Utan SQL ar du blind i produktionsmiljon.

Nar en deployment failar och du behover kolla vilka rader som paverkades,
eller nar du ska automatisera backups - da behover du SQL.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar SQL?

SQL (Structured Query Language) ar ett standardiserat sprak for att
hantera relationsdatabaser. Det anvands for att:

```
┌─────────────────────────────────────────────────────────────────┐
│                     SQL OVERSIKT                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│   │  Applikation │    │  Applikation │    │   DevOps    │        │
│   │   (Backend) │    │   (Frontend)│    │   Scripts   │        │
│   └──────┬──────┘    └──────┬──────┘    └──────┬──────┘        │
│          │                  │                  │                │
│          └────────────┬─────┴──────────────────┘                │
│                       │                                         │
│                       ▼                                         │
│              ┌────────────────┐                                 │
│              │   SQL Queries  │                                 │
│              └────────┬───────┘                                 │
│                       │                                         │
│                       ▼                                         │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                    DATABAS                               │  │
│   │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │  │
│   │  │ users   │  │ orders  │  │ servers │  │  logs   │    │  │
│   │  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Databaser - Jamforelse

| Databas | Anvandning | Styrka |
|---------|------------|--------|
| PostgreSQL | Enterprise, DevOps | ACID, JSON, extensioner |
| MySQL | Webb, WordPress | Snabb, enkel |
| SQLite | Embedded, lokal | Ingen server kravs |
| SQL Server | Microsoft stack | Windows integration |
| MariaDB | MySQL-fork | Open source |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Installation - PostgreSQL

### macOS

```bash
# Installera med Homebrew
brew install postgresql@16
brew services start postgresql@16

# Verifiera
psql --version
```

### Ubuntu/Debian

```bash
# Installera
sudo apt update
sudo apt install postgresql postgresql-contrib

# Starta tjansten
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Verifiera
sudo -u postgres psql -c "SELECT version();"
```

### Docker (Rekommenderat for DevOps)

```bash
# Starta PostgreSQL container
docker run -d \\
  --name postgres-dev \\
  -e POSTGRES_USER=devops \\
  -e POSTGRES_PASSWORD=secret123 \\
  -e POSTGRES_DB=devops_db \\
  -p 5432:5432 \\
  -v postgres_data:/var/lib/postgresql/data \\
  postgres:16-alpine

# Anslut till databasen
docker exec -it postgres-dev psql -U devops -d devops_db
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## SQL Kategorier

```
┌─────────────────────────────────────────────────────────────────┐
│                    SQL KOMMANDO-KATEGORIER                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  DDL (Data Definition Language)                                 │
│  ├── CREATE  - Skapa tabeller, index, databaser                │
│  ├── ALTER   - Andrar struktur                                 │
│  ├── DROP    - Ta bort objekt                                  │
│  └── TRUNCATE - Tom tabell                                     │
│                                                                 │
│  DML (Data Manipulation Language)                               │
│  ├── SELECT  - Hamta data                                      │
│  ├── INSERT  - Lagg till data                                  │
│  ├── UPDATE  - Uppdatera data                                  │
│  └── DELETE  - Ta bort data                                    │
│                                                                 │
│  DCL (Data Control Language)                                    │
│  ├── GRANT   - Ge rattigheter                                  │
│  └── REVOKE  - Ta bort rattigheter                             │
│                                                                 │
│  TCL (Transaction Control Language)                             │
│  ├── COMMIT  - Spara transaktion                               │
│  ├── ROLLBACK - Angra transaktion                              │
│  └── SAVEPOINT - Skapa aterstallningspunkt                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Forsta Queries - CRUD Operations

### Skapa databas och tabell

```sql
-- Skapa en ny databas
CREATE DATABASE devops_db;

-- Anslut till databasen (psql)
\\c devops_db

-- Skapa en tabell for serverinventering
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL,
    ip_address INET,
    environment VARCHAR(20) DEFAULT 'development',
    status VARCHAR(20) DEFAULT 'active',
    cpu_cores INTEGER,
    ram_gb INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### INSERT - Lagg till data

```sql
-- Infoga en rad
INSERT INTO servers (hostname, ip_address, environment, cpu_cores, ram_gb)
VALUES ('web-prod-01', '10.0.1.10', 'production', 4, 16);

-- Infoga flera rader
INSERT INTO servers (hostname, ip_address, environment, cpu_cores, ram_gb)
VALUES
    ('web-prod-02', '10.0.1.11', 'production', 4, 16),
    ('db-prod-01', '10.0.2.10', 'production', 8, 64),
    ('cache-prod-01', '10.0.3.10', 'production', 2, 8);
```

### SELECT - Hamta data

```sql
-- Hamta alla rader
SELECT * FROM servers;

-- Hamta specifika kolumner
SELECT hostname, ip_address, status FROM servers;

-- Filtrera med WHERE
SELECT * FROM servers WHERE environment = 'production';
```

### UPDATE - Uppdatera data

```sql
-- Uppdatera en rad
UPDATE servers
SET status = 'maintenance', updated_at = NOW()
WHERE hostname = 'web-prod-01';
```

### DELETE - Ta bort data

```sql
-- Ta bort specifik rad
DELETE FROM servers WHERE hostname = 'old-server';

-- VARNING: Utan WHERE tas ALLA rader bort!
-- DELETE FROM servers;  -- FARLIGT!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Kommando | Syntax | Beskrivning |
|----------|--------|-------------|
| CREATE DATABASE | `CREATE DATABASE namn;` | Skapa databas |
| CREATE TABLE | `CREATE TABLE namn (kolumner);` | Skapa tabell |
| INSERT | `INSERT INTO tabell VALUES (...);` | Lagg till rad |
| SELECT | `SELECT kolumner FROM tabell;` | Hamta data |
| UPDATE | `UPDATE tabell SET kol=varde WHERE ...;` | Uppdatera |
| DELETE | `DELETE FROM tabell WHERE ...;` | Ta bort rad |
| DROP TABLE | `DROP TABLE namn;` | Ta bort tabell |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

### Problem 1: Permission denied

```bash
# Fel
psql: error: connection refused

# Losning - kontrollera att PostgreSQL kors
sudo systemctl status postgresql
sudo systemctl start postgresql
```

### Problem 2: Database does not exist

```sql
-- Fel
FATAL: database "mydb" does not exist

-- Losning - skapa databasen forst
CREATE DATABASE mydb;
```

### Problem 3: Relation does not exist

```sql
-- Fel
ERROR: relation "servers" does not exist

-- Losning - kontrollera att du ar i ratt databas
\\c devops_db
\\dt  -- Lista tabeller
```

### Problem 4: UPDATE/DELETE utan WHERE

```sql
-- FARLIGT! Paverkar ALLA rader
UPDATE servers SET status = 'offline';
DELETE FROM servers;

-- SAKERT - anvand alltid WHERE
UPDATE servers SET status = 'offline' WHERE id = 5;
DELETE FROM servers WHERE status = 'decommissioned';

-- Tips: Kor SELECT forst for att se vilka rader som paverkas
SELECT * FROM servers WHERE status = 'decommissioned';
-- Om OK, kor DELETE
DELETE FROM servers WHERE status = 'decommissioned';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktisk ovning

Skapa en enkel deployment-tracker:

```sql
-- 1. Skapa databas
CREATE DATABASE deployment_tracker;
\\c deployment_tracker

-- 2. Skapa tabell
CREATE TABLE deployments (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    version VARCHAR(20) NOT NULL,
    environment VARCHAR(20) NOT NULL,
    deployed_by VARCHAR(50),
    deployed_at TIMESTAMP DEFAULT NOW(),
    status VARCHAR(20) DEFAULT 'pending'
);

-- 3. Lagg till testdata
INSERT INTO deployments (service_name, version, environment, deployed_by, status)
VALUES
    ('api-gateway', 'v2.1.0', 'production', 'jenkins', 'success'),
    ('user-service', 'v1.5.2', 'production', 'github-actions', 'success'),
    ('payment-service', 'v3.0.0', 'staging', 'manual', 'pending');

-- 4. Fraga datan
SELECT service_name, version, status
FROM deployments
WHERE environment = 'production';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- SQL ar standardsprak for alla relationsdatabaser
- Fyra kategorier: DDL (struktur), DML (data), DCL (rattigheter), TCL (transaktioner)
- CRUD: Create, Read, Update, Delete - grundlaggande operationer
- PostgreSQL ar forstahandsvalet for DevOps - robust och feature-rich
- Docker ar perfekt for lokal databasutveckling
- Anvand ALLTID WHERE vid UPDATE och DELETE for att undvika katastrofer
- Testa med SELECT innan du kor destruktiva operationer

Nasta steg: Node 2 - Data Types
''',
}

NODE_02_DATA_TYPES = {
    "node_id": 2,
    "title": "Data Types",
    "slug": "data-types",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "prerequisites": [1],
    "content": '''# Data Types i SQL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

Ratt datatyp ar avgörande for prestanda och dataintegritet. Ett felaktigt
val kan kosta dig terabytes i lagring eller millisekunder i query-tid.
Som DevOps maste du forsta vilka typer som passar for loggar, metrics,
timestamps och konfigurationsdata.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Datatyper - Oversikt

```
┌─────────────────────────────────────────────────────────────────┐
│                    SQL DATATYPER                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  NUMERISKA                      TEXT                            │
│  ├── SMALLINT (2 bytes)         ├── CHAR(n)    - Fast langd    │
│  ├── INTEGER  (4 bytes)         ├── VARCHAR(n) - Variabel      │
│  ├── BIGINT   (8 bytes)         └── TEXT       - Obegransad    │
│  ├── SERIAL   (auto-increment)                                  │
│  ├── DECIMAL  (exakt)           DATUM & TID                     │
│  └── REAL/DOUBLE (approx)       ├── DATE       - Bara datum    │
│                                 ├── TIME       - Bara tid      │
│  BOOLEAN                        ├── TIMESTAMP  - Datum + tid   │
│  └── true/false/null            └── TIMESTAMPTZ - Med timezone │
│                                                                 │
│  SPECIELLA (PostgreSQL)                                         │
│  ├── UUID    - Unika ID                                        │
│  ├── JSONB   - JSON data                                       │
│  ├── ARRAY   - Listor                                          │
│  └── INET    - IP-adresser                                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Numeriska typer

### Heltal

```sql
-- Heltalstyper och deras range
SMALLINT        -- -32,768 till 32,767 (2 bytes)
INTEGER         -- -2 miljarder till 2 miljarder (4 bytes)
BIGINT          -- Extremt stora tal (8 bytes)
SERIAL          -- Auto-increment INTEGER
BIGSERIAL       -- Auto-increment BIGINT

-- Praktiskt exempel: Server metrics
CREATE TABLE server_metrics (
    id SERIAL PRIMARY KEY,
    server_id INTEGER NOT NULL,
    cpu_percent SMALLINT CHECK (cpu_percent BETWEEN 0 AND 100),
    memory_mb INTEGER,
    disk_bytes BIGINT,
    process_count SMALLINT
);

-- Insert
INSERT INTO server_metrics (server_id, cpu_percent, memory_mb, disk_bytes)
VALUES (1, 75, 8192, 500000000000);
```

### Decimaltal

```sql
-- Exakta tal (for pengar, procent)
DECIMAL(precision, scale)  -- DECIMAL(10,2) = 12345678.90
NUMERIC(precision, scale)  -- Samma som DECIMAL

-- Approximerade tal (for vetenskapliga berakningar)
REAL                       -- 6 decimalers precision
DOUBLE PRECISION           -- 15 decimalers precision

-- Praktiskt exempel: Kostnadsuppfoljning
CREATE TABLE cloud_costs (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(100),
    monthly_cost DECIMAL(10,2) NOT NULL,
    usage_hours REAL,
    cost_per_hour DECIMAL(8,4)
);

-- VIKTIGT: Anvand DECIMAL for pengar, aldrig REAL/DOUBLE!
-- REAL: 10.00 + 10.00 + 10.00 kan bli 29.999999
-- DECIMAL: 10.00 + 10.00 + 10.00 = 30.00 (exakt)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Text typer

```sql
-- Fast langd (paddas med mellanslag)
CHAR(n)         -- Exakt n tecken, bra for koder som 'SE', 'US'

-- Variabel langd
VARCHAR(n)      -- Max n tecken, sparar bara det som behovs
TEXT            -- Obegransad langd

-- Praktiskt exempel: Anvandartabell
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    country_code CHAR(2) NOT NULL,      -- 'SE', 'US', 'DE'
    username VARCHAR(50) NOT NULL,       -- Max 50 tecken
    email VARCHAR(255) UNIQUE NOT NULL,  -- RFC standard
    bio TEXT,                            -- Obegransad
    api_key CHAR(32)                     -- Fast langd for nycklar
);

-- Jamforelse
SELECT
    LENGTH('hello'::CHAR(10)) AS char_len,    -- 10 (paddad)
    LENGTH('hello'::VARCHAR(10)) AS varchar_len; -- 5 (faktisk)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Datum och Tid

```sql
-- Typer
DATE            -- 2024-01-15
TIME            -- 14:30:00
TIMESTAMP       -- 2024-01-15 14:30:00 (utan timezone)
TIMESTAMPTZ     -- 2024-01-15 14:30:00+01 (med timezone) REKOMMENDERAD!
INTERVAL        -- Tidsperiod: '1 day', '2 hours 30 minutes'

-- Praktiskt exempel: Deployment log
CREATE TABLE deployment_log (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    deployed_at TIMESTAMPTZ DEFAULT NOW(),  -- Alltid med timezone!
    completed_at TIMESTAMPTZ,
    duration INTERVAL GENERATED ALWAYS AS (completed_at - deployed_at) STORED
);

-- Insert
INSERT INTO deployment_log (service_name, deployed_at, completed_at)
VALUES ('api-gateway', '2024-01-15 10:00:00+01', '2024-01-15 10:05:30+01');

-- Queries med datum
SELECT * FROM deployment_log
WHERE deployed_at > NOW() - INTERVAL '24 hours';

SELECT * FROM deployment_log
WHERE deployed_at::DATE = CURRENT_DATE;

SELECT * FROM deployment_log
WHERE deployed_at BETWEEN '2024-01-01' AND '2024-01-31';
```

### Viktigt om Timezones

```sql
-- ALLTID anvand TIMESTAMPTZ i produktion!
-- Annars far du problem med servrar i olika tidszoner

-- Konvertera mellan tidszoner
SELECT
    deployed_at,
    deployed_at AT TIME ZONE 'Europe/Stockholm' AS local_time,
    deployed_at AT TIME ZONE 'UTC' AS utc_time
FROM deployment_log;

-- Satt default timezone for session
SET timezone = 'Europe/Stockholm';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Boolean

```sql
-- Varden: TRUE, FALSE, NULL
BOOLEAN         -- Alias: BOOL

-- Praktiskt exempel
CREATE TABLE feature_flags (
    id SERIAL PRIMARY KEY,
    feature_name VARCHAR(100) UNIQUE NOT NULL,
    is_enabled BOOLEAN DEFAULT false,
    is_beta BOOLEAN DEFAULT false,
    rollout_percent INTEGER CHECK (rollout_percent BETWEEN 0 AND 100)
);

-- Insert
INSERT INTO feature_flags (feature_name, is_enabled, is_beta)
VALUES
    ('dark_mode', true, false),
    ('new_dashboard', true, true),
    ('ai_assistant', false, true);

-- Queries
SELECT * FROM feature_flags WHERE is_enabled = true;
SELECT * FROM feature_flags WHERE is_enabled AND NOT is_beta;
SELECT * FROM feature_flags WHERE is_enabled IS NOT NULL;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## PostgreSQL Specialtyper

### UUID

```sql
-- Universellt unika identifierare
-- Perfekt for distribuerade system

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE api_keys (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id INTEGER NOT NULL,
    key_name VARCHAR(100),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    expires_at TIMESTAMPTZ
);

-- Insert (auto-genererat ID)
INSERT INTO api_keys (user_id, key_name)
VALUES (1, 'Production API Key');

-- Resultat: id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'
```

### JSONB

```sql
-- Lagra JSON-data (JSONB ar snabbare an JSON)
CREATE TABLE server_config (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL,
    config JSONB NOT NULL,
    tags JSONB DEFAULT '[]'::jsonb
);

-- Insert
INSERT INTO server_config (hostname, config, tags)
VALUES (
    'web-prod-01',
    '{
        "cpu_limit": 4,
        "memory_limit": "16Gi",
        "environment": {
            "NODE_ENV": "production",
            "LOG_LEVEL": "info"
        }
    }',
    '["production", "web", "critical"]'
);

-- Query JSONB
SELECT * FROM server_config
WHERE config->>'cpu_limit' = '4';

SELECT * FROM server_config
WHERE config @> '{"environment": {"NODE_ENV": "production"}}';

SELECT * FROM server_config
WHERE tags ? 'production';  -- Innehaller 'production'?
```

### ARRAY

```sql
-- Lagra listor av varden
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL,
    ip_addresses INET[],
    tags TEXT[],
    ports INTEGER[]
);

-- Insert
INSERT INTO servers (hostname, ip_addresses, tags, ports)
VALUES (
    'web-prod-01',
    ARRAY['10.0.1.10'::inet, '10.0.2.10'::inet],
    ARRAY['production', 'web', 'nginx'],
    ARRAY[80, 443, 8080]
);

-- Query arrays
SELECT * FROM servers WHERE 'production' = ANY(tags);
SELECT * FROM servers WHERE tags @> ARRAY['production', 'web'];
SELECT * FROM servers WHERE 443 = ANY(ports);
```

### INET (IP-adresser)

```sql
CREATE TABLE firewall_rules (
    id SERIAL PRIMARY KEY,
    rule_name VARCHAR(100),
    source_ip INET,
    destination_ip INET,
    allowed BOOLEAN DEFAULT true
);

-- Query
SELECT * FROM firewall_rules
WHERE source_ip << '10.0.0.0/8';  -- Inom subnet
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Typ | Anvandning | Exempel |
|-----|------------|---------|
| INTEGER | ID, rakare | `user_id INTEGER` |
| SERIAL | Auto-ID | `id SERIAL PRIMARY KEY` |
| DECIMAL(10,2) | Pengar | `price DECIMAL(10,2)` |
| VARCHAR(n) | Text med max | `email VARCHAR(255)` |
| TEXT | Lang text | `description TEXT` |
| TIMESTAMPTZ | Tidsstampel | `created_at TIMESTAMPTZ` |
| BOOLEAN | Sant/falskt | `is_active BOOLEAN` |
| UUID | Unika ID | `api_key UUID` |
| JSONB | Flexibel data | `config JSONB` |
| ARRAY | Listor | `tags TEXT[]` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

### Problem 1: REAL/DOUBLE for pengar

```sql
-- FEL - oexakta berakningar
CREATE TABLE orders_bad (
    total REAL  -- DÅLIGT!
);

-- RATT - exakta berakningar
CREATE TABLE orders_good (
    total DECIMAL(10,2)  -- BRA!
);
```

### Problem 2: TIMESTAMP utan timezone

```sql
-- FEL - forlorar timezone-info
created_at TIMESTAMP

-- RATT - bevarar timezone
created_at TIMESTAMPTZ
```

### Problem 3: VARCHAR for allt

```sql
-- FEL - VARCHAR for fasta varden
status VARCHAR(20)  -- 'active', 'inactive'...

-- BÄTTRE - anvand ENUM eller CHECK
status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'pending'))

-- Eller skapa enum-typ
CREATE TYPE status_enum AS ENUM ('active', 'inactive', 'pending');
status status_enum
```

### Problem 4: For sma heltal

```sql
-- FEL - overflow risk
view_count SMALLINT  -- Max 32,767

-- RATT for rakare som kan bli stora
view_count INTEGER   -- Max 2 miljarder
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- Anvand DECIMAL for pengar, aldrig REAL eller DOUBLE
- Anvand TIMESTAMPTZ istallet for TIMESTAMP - timezone ar kritiskt
- VARCHAR for variabel text, CHAR endast for fasta langder (landskoder etc)
- INTEGER racker for de flesta ID:n, BIGINT for extremt stora tal
- SERIAL for auto-increment primary keys
- JSONB ar kraftfullt for flexibel data i PostgreSQL
- UUID ar perfekt for distribuerade system
- Valj datatyp baserat pa domanen, inte pa "vad som fungerar"

Nasta steg: Node 3 - CREATE & ALTER
''',
}

NODE_03_DDL_CREATE = {
    "node_id": 3,
    "title": "CREATE & ALTER",
    "slug": "ddl-create",
    "estimated_minutes": 55,
    "xp_reward": 130,
    "prerequisites": [2],
    "content": '''# CREATE & ALTER - DDL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

Databasschema ar fundamentet for din applikation. Ett dalgt designat schema
leder till dalig prestanda och buggar som ar extremt svara att fixa i
produktion. Som DevOps hanterar du migrations, schema-uppdateringar och
rollbacks - DDL-kunskap ar essentiellt.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## DDL Oversikt

```
┌─────────────────────────────────────────────────────────────────┐
│                 DDL - Data Definition Language                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CREATE                         ALTER                           │
│  ├── DATABASE                   ├── ADD COLUMN                 │
│  ├── TABLE                      ├── DROP COLUMN                │
│  ├── INDEX                      ├── ALTER COLUMN               │
│  ├── VIEW                       ├── ADD CONSTRAINT             │
│  └── SEQUENCE                   └── RENAME                     │
│                                                                 │
│  DROP                           TRUNCATE                        │
│  ├── DATABASE                   └── Tomma tabell snabbt        │
│  ├── TABLE                          (behall struktur)          │
│  ├── INDEX                                                      │
│  └── CASCADE (beroenden)                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CREATE TABLE

### Grundlaggande syntax

```sql
CREATE TABLE tabellnamn (
    kolumn1 datatyp [constraints],
    kolumn2 datatyp [constraints],
    ...
    [tabell-constraints]
);
```

### Praktiskt exempel: Deployment Tracker

```sql
-- Huvudtabell for deployments
CREATE TABLE deployments (
    -- Primary key med auto-increment
    id SERIAL PRIMARY KEY,

    -- Obligatoriska falt
    service_name VARCHAR(100) NOT NULL,
    version VARCHAR(20) NOT NULL,
    environment VARCHAR(20) NOT NULL,

    -- Valfria falt med defaults
    deployed_by VARCHAR(50),
    deployed_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    status VARCHAR(20) DEFAULT 'pending',

    -- Flexibel metadata
    config JSONB DEFAULT '{}',
    tags TEXT[] DEFAULT '{}',

    -- Check constraints
    CONSTRAINT valid_environment CHECK (
        environment IN ('development', 'staging', 'production')
    ),
    CONSTRAINT valid_status CHECK (
        status IN ('pending', 'running', 'success', 'failed', 'rolled_back')
    ),

    -- Unik kombination
    CONSTRAINT unique_deployment UNIQUE (service_name, version, environment)
);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Constraints

```
┌─────────────────────────────────────────────────────────────────┐
│                     SQL CONSTRAINTS                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PRIMARY KEY                                                    │
│  └── Unik identifierare, kan inte vara NULL                    │
│      id SERIAL PRIMARY KEY                                      │
│                                                                 │
│  FOREIGN KEY                                                    │
│  └── Referens till annan tabell                                │
│      user_id INTEGER REFERENCES users(id)                       │
│                                                                 │
│  UNIQUE                                                         │
│  └── Varde maste vara unikt i kolumnen                         │
│      email VARCHAR(255) UNIQUE                                  │
│                                                                 │
│  NOT NULL                                                       │
│  └── Kolumnen kan inte vara NULL                               │
│      username VARCHAR(50) NOT NULL                              │
│                                                                 │
│  DEFAULT                                                        │
│  └── Standardvarde om inget anges                              │
│      created_at TIMESTAMPTZ DEFAULT NOW()                       │
│                                                                 │
│  CHECK                                                          │
│  └── Validera varden                                           │
│      age INTEGER CHECK (age >= 0 AND age < 150)                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Foreign Keys med ON DELETE/UPDATE

```sql
-- Relaterad tabell for deployment-loggar
CREATE TABLE deployment_logs (
    id SERIAL PRIMARY KEY,
    deployment_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    level VARCHAR(10) DEFAULT 'info',
    created_at TIMESTAMPTZ DEFAULT NOW(),

    -- Foreign key med cascade delete
    CONSTRAINT fk_deployment
        FOREIGN KEY (deployment_id)
        REFERENCES deployments(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- ON DELETE optioner:
-- CASCADE     - Ta bort relaterade rader automatiskt
-- SET NULL    - Satt till NULL
-- SET DEFAULT - Satt till default-varde
-- RESTRICT    - Forhindra delete om relationer finns
-- NO ACTION   - Samma som RESTRICT (default)
```

### Composite Primary Key

```sql
-- Manga-till-manga relation
CREATE TABLE user_roles (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    role_id INTEGER REFERENCES roles(id) ON DELETE CASCADE,
    assigned_at TIMESTAMPTZ DEFAULT NOW(),
    assigned_by INTEGER REFERENCES users(id),

    -- Composite primary key
    PRIMARY KEY (user_id, role_id)
);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ALTER TABLE

### Lagg till kolumn

```sql
-- Enkel kolumn
ALTER TABLE deployments
ADD COLUMN rollback_version VARCHAR(20);

-- Med default (for befintliga rader)
ALTER TABLE deployments
ADD COLUMN is_canary BOOLEAN DEFAULT false;

-- Med NOT NULL och default
ALTER TABLE deployments
ADD COLUMN priority INTEGER NOT NULL DEFAULT 0;
```

### Ta bort kolumn

```sql
-- Enkel borttagning
ALTER TABLE deployments
DROP COLUMN rollback_version;

-- Med cascade (om beroenden finns)
ALTER TABLE deployments
DROP COLUMN old_field CASCADE;
```

### Andra kolumn

```sql
-- Andra datatyp
ALTER TABLE deployments
ALTER COLUMN version TYPE VARCHAR(50);

-- Satt/ta bort NOT NULL
ALTER TABLE deployments
ALTER COLUMN deployed_by SET NOT NULL;

ALTER TABLE deployments
ALTER COLUMN deployed_by DROP NOT NULL;

-- Andra default
ALTER TABLE deployments
ALTER COLUMN status SET DEFAULT 'queued';

ALTER TABLE deployments
ALTER COLUMN status DROP DEFAULT;
```

### Hantera constraints

```sql
-- Lagg till constraint
ALTER TABLE deployments
ADD CONSTRAINT check_priority CHECK (priority BETWEEN 0 AND 10);

-- Ta bort constraint
ALTER TABLE deployments
DROP CONSTRAINT check_priority;

-- Lagg till foreign key
ALTER TABLE deployment_logs
ADD CONSTRAINT fk_deployment
    FOREIGN KEY (deployment_id)
    REFERENCES deployments(id);
```

### Rename

```sql
-- Rename kolumn
ALTER TABLE deployments
RENAME COLUMN deployed_by TO deployer;

-- Rename tabell
ALTER TABLE deployments
RENAME TO releases;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## DROP och TRUNCATE

### DROP - Ta bort objekt

```sql
-- Ta bort tabell (om den finns)
DROP TABLE IF EXISTS old_deployments;

-- Ta bort med alla beroenden
DROP TABLE deployments CASCADE;

-- Ta bort databas
DROP DATABASE IF EXISTS old_db;
```

### TRUNCATE - Tom tabell snabbt

```sql
-- Snabbare an DELETE for stora tabeller
TRUNCATE TABLE logs;

-- Med reset av SERIAL/sequence
TRUNCATE TABLE logs RESTART IDENTITY;

-- Flera tabeller
TRUNCATE TABLE logs, audit_trail RESTART IDENTITY;

-- Med cascade for foreign keys
TRUNCATE TABLE deployments CASCADE;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## INDEX - Prestanda

### Skapa index

```sql
-- Enkelt index
CREATE INDEX idx_deployments_service
ON deployments(service_name);

-- Unikt index
CREATE UNIQUE INDEX idx_users_email
ON users(email);

-- Composite index (ordning spelar roll!)
CREATE INDEX idx_deployments_env_status
ON deployments(environment, status);

-- Partial index (endast vissa rader)
CREATE INDEX idx_active_deployments
ON deployments(service_name)
WHERE status IN ('pending', 'running');

-- Index for JSONB
CREATE INDEX idx_config_settings
ON deployments USING gin(config);

-- Index for array
CREATE INDEX idx_tags
ON deployments USING gin(tags);
```

### Nar ska man skapa index?

```
┌─────────────────────────────────────────────────────────────────┐
│                  INDEX BESLUTSTRÄ                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Skapa index om:                                                │
│  ├── Kolumnen anvands ofta i WHERE                             │
│  ├── Kolumnen anvands i JOIN                                   │
│  ├── Kolumnen anvands i ORDER BY                               │
│  └── Tabellen ar stor (>10,000 rader)                          │
│                                                                 │
│  Undvik index om:                                               │
│  ├── Tabellen ar liten                                         │
│  ├── Kolumnen uppdateras mycket                                │
│  ├── Kolumnen har lag kardinalitet (fa unika varden)           │
│  └── Du redan har manga index (saktar ner INSERT/UPDATE)       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Kommando | Syntax | Beskrivning |
|----------|--------|-------------|
| CREATE TABLE | `CREATE TABLE namn (...)` | Skapa tabell |
| ADD COLUMN | `ALTER TABLE t ADD COLUMN c typ` | Lagg till kolumn |
| DROP COLUMN | `ALTER TABLE t DROP COLUMN c` | Ta bort kolumn |
| ALTER COLUMN | `ALTER TABLE t ALTER COLUMN c ...` | Andra kolumn |
| ADD CONSTRAINT | `ALTER TABLE t ADD CONSTRAINT ...` | Lagg till regel |
| DROP TABLE | `DROP TABLE IF EXISTS t` | Ta bort tabell |
| TRUNCATE | `TRUNCATE TABLE t` | Tom tabell |
| CREATE INDEX | `CREATE INDEX i ON t(c)` | Skapa index |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

### Problem 1: NOT NULL pa befintliga rader

```sql
-- FEL - misslyckas om NULL-varden finns
ALTER TABLE deployments
ADD COLUMN priority INTEGER NOT NULL;

-- LOSNING - lagg till med default forst
ALTER TABLE deployments
ADD COLUMN priority INTEGER NOT NULL DEFAULT 0;
```

### Problem 2: Foreign key constraint violation

```sql
-- FEL - kan inte ta bort om relationer finns
DROP TABLE deployments;
-- ERROR: cannot drop table deployments because other objects depend on it

-- LOSNING 1 - cascade
DROP TABLE deployments CASCADE;

-- LOSNING 2 - ta bort beroende forst
DROP TABLE deployment_logs;
DROP TABLE deployments;
```

### Problem 3: Andra datatyp med existerande data

```sql
-- FEL - kan inte konvertera
ALTER TABLE deployments
ALTER COLUMN version TYPE INTEGER;
-- ERROR: column "version" cannot be cast to type integer

-- LOSNING - explicit cast
ALTER TABLE deployments
ALTER COLUMN version TYPE INTEGER USING version::integer;

-- Eller skapa ny kolumn, migrera, ta bort gammal
ALTER TABLE deployments ADD COLUMN version_int INTEGER;
UPDATE deployments SET version_int = version::integer WHERE version ~ '^[0-9]+$';
ALTER TABLE deployments DROP COLUMN version;
ALTER TABLE deployments RENAME COLUMN version_int TO version;
```

### Problem 4: Index paverkar inte query

```sql
-- Kontrollera om index anvands
EXPLAIN ANALYZE SELECT * FROM deployments WHERE service_name = 'api';

-- Om "Seq Scan" visas, anvands inte index
-- Vanliga orsaker:
-- 1. Tabellen ar for liten
-- 2. Query returnerar manga rader (>10-15% av tabellen)
-- 3. Kolumnen har function/cast: WHERE LOWER(name) = 'api'
-- 4. Statistik ar inaktuell: ANALYZE deployments;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktisk ovning

Skapa ett komplett schema for en CI/CD pipeline tracker:

```sql
-- 1. Skapa databas
CREATE DATABASE cicd_tracker;
\\c cicd_tracker

-- 2. Skapa tabeller
CREATE TABLE pipelines (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    repository_url TEXT NOT NULL,
    default_branch VARCHAR(50) DEFAULT 'main',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE pipeline_runs (
    id SERIAL PRIMARY KEY,
    pipeline_id INTEGER NOT NULL REFERENCES pipelines(id) ON DELETE CASCADE,
    commit_sha CHAR(40) NOT NULL,
    branch VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    started_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    duration_seconds INTEGER GENERATED ALWAYS AS (
        EXTRACT(EPOCH FROM (completed_at - started_at))::INTEGER
    ) STORED,

    CONSTRAINT valid_status CHECK (
        status IN ('pending', 'running', 'success', 'failed', 'cancelled')
    )
);

-- 3. Skapa index
CREATE INDEX idx_runs_pipeline ON pipeline_runs(pipeline_id);
CREATE INDEX idx_runs_status ON pipeline_runs(status) WHERE status IN ('pending', 'running');
CREATE INDEX idx_runs_started ON pipeline_runs(started_at DESC);

-- 4. Verifiera
\\dt
\\di
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- CREATE TABLE med ratt constraints fran borjan - refaktorering ar dyrt
- Anvand SERIAL eller UUID for primary keys
- Foreign keys med ON DELETE CASCADE forenklar datahantering
- Lagg till NOT NULL med DEFAULT for befintliga tabeller
- Index forbattrar lasning men saktar ner skrivning
- TRUNCATE ar snabbare an DELETE for stora tabeller
- DROP CASCADE ar kraftfullt men farligt - dubbelkolla beroenden
- Anvand IF EXISTS for idempotenta migrations

Nasta steg: Node 4 - INSERT, UPDATE, DELETE
''',
}

NODE_04_DML_BASICS = {
    "node_id": 4,
    "title": "INSERT, UPDATE, DELETE",
    "slug": "dml-basics",
    "estimated_minutes": 50,
    "xp_reward": 125,
    "prerequisites": [3],
    "content": '''# INSERT, UPDATE, DELETE - DML

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

CRUD-operationer ar brod och smor i databashantering. Men UPDATE och DELETE
utan WHERE kan forstora hela din databas pa sekunder. Som DevOps maste du
kunna manipulera data sakert for migrations, datarensning och debugging.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## DML Oversikt

```
┌─────────────────────────────────────────────────────────────────┐
│              DML - Data Manipulation Language                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  INSERT                         UPDATE                          │
│  ├── Enkel rad                  ├── Enkel kolumn               │
│  ├── Flera rader                ├── Flera kolumner             │
│  ├── INSERT ... SELECT          ├── UPDATE ... FROM            │
│  ├── RETURNING                  ├── Conditional (CASE)         │
│  └── ON CONFLICT (UPSERT)       └── RETURNING                  │
│                                                                 │
│  DELETE                         MERGE (SQL Standard)            │
│  ├── Med WHERE                  └── INSERT or UPDATE           │
│  ├── Med subquery                   (PostgreSQL: ON CONFLICT)  │
│  ├── RETURNING                                                  │
│  └── TRUNCATE (snabbare)                                       │
│                                                                 │
│  VIKTIGT: Anvand ALLTID WHERE vid UPDATE/DELETE!               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## INSERT

### Grundlaggande INSERT

```sql
-- Enkel rad med specifika kolumner
INSERT INTO servers (hostname, ip_address, environment)
VALUES ('web-prod-01', '10.0.1.10', 'production');

-- Med alla kolumner (ordningen maste matcha)
INSERT INTO servers
VALUES (DEFAULT, 'web-prod-02', '10.0.1.11', 'production', 'active', NOW());

-- Flera rader samtidigt
INSERT INTO servers (hostname, ip_address, environment)
VALUES
    ('web-prod-03', '10.0.1.12', 'production'),
    ('web-staging-01', '10.0.2.10', 'staging'),
    ('web-dev-01', '10.0.3.10', 'development');
```

### INSERT med RETURNING

```sql
-- Fa tillbaka det skapade ID:t
INSERT INTO servers (hostname, ip_address)
VALUES ('new-server', '10.0.1.50')
RETURNING id;

-- Returnera flera kolumner
INSERT INTO servers (hostname, ip_address, environment)
VALUES ('new-server-2', '10.0.1.51', 'production')
RETURNING id, hostname, created_at;

-- Returnera allt
INSERT INTO servers (hostname, ip_address)
VALUES ('new-server-3', '10.0.1.52')
RETURNING *;
```

### INSERT fran SELECT

```sql
-- Kopiera data fran en tabell till en annan
INSERT INTO server_backups (server_id, hostname, backup_date)
SELECT id, hostname, NOW()
FROM servers
WHERE status = 'active';

-- Med transformation
INSERT INTO audit_log (action, table_name, record_id, old_data)
SELECT
    'ARCHIVE',
    'servers',
    id,
    row_to_json(servers)::TEXT
FROM servers
WHERE status = 'decommissioned';
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## UPSERT - INSERT ON CONFLICT

```sql
-- Insert eller uppdatera om konflikt (PostgreSQL)
INSERT INTO servers (hostname, ip_address, status)
VALUES ('web-prod-01', '10.0.1.10', 'active')
ON CONFLICT (hostname)
DO UPDATE SET
    ip_address = EXCLUDED.ip_address,
    status = EXCLUDED.status,
    updated_at = NOW();

-- EXCLUDED refererar till den nya raden som skulle inserts

-- Insert eller ignorera
INSERT INTO servers (hostname, ip_address)
VALUES ('web-prod-01', '10.0.1.10')
ON CONFLICT (hostname)
DO NOTHING;

-- Conflict pa composite key
INSERT INTO server_tags (server_id, tag)
VALUES (1, 'production')
ON CONFLICT (server_id, tag)
DO NOTHING;

-- Conflict med WHERE (conditional update)
INSERT INTO config (key, value, version)
VALUES ('max_connections', '100', 2)
ON CONFLICT (key)
DO UPDATE SET
    value = EXCLUDED.value,
    version = EXCLUDED.version
WHERE config.version < EXCLUDED.version;  -- Endast om ny version ar hogre
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## UPDATE

### Grundlaggande UPDATE

```sql
-- Uppdatera en kolumn
UPDATE servers
SET status = 'maintenance'
WHERE hostname = 'web-prod-01';

-- Uppdatera flera kolumner
UPDATE servers
SET
    status = 'active',
    ip_address = '10.0.1.100',
    updated_at = NOW()
WHERE id = 5;

-- Med RETURNING
UPDATE servers
SET status = 'offline'
WHERE hostname LIKE 'old-%'
RETURNING id, hostname, status;
```

### UPDATE med berakningar

```sql
-- Oka varde
UPDATE metrics
SET request_count = request_count + 1
WHERE server_id = 1;

-- Anvand COALESCE for NULL-hantering
UPDATE servers
SET
    last_checked = NOW(),
    check_count = COALESCE(check_count, 0) + 1
WHERE environment = 'production';
```

### Conditional UPDATE med CASE

```sql
-- Uppdatera baserat pa villkor
UPDATE servers
SET status = CASE
    WHEN last_heartbeat < NOW() - INTERVAL '5 minutes' THEN 'stale'
    WHEN last_heartbeat < NOW() - INTERVAL '1 hour' THEN 'offline'
    WHEN last_heartbeat IS NULL THEN 'unknown'
    ELSE 'active'
END
WHERE environment = 'production';

-- Prioritetsbaserad update
UPDATE deployments
SET priority = CASE environment
    WHEN 'production' THEN 1
    WHEN 'staging' THEN 2
    WHEN 'development' THEN 3
    ELSE 4
END;
```

### UPDATE med JOIN (PostgreSQL syntax)

```sql
-- Uppdatera baserat pa data fran annan tabell
UPDATE servers s
SET
    status = 'decommissioned',
    decommissioned_at = NOW()
FROM decommission_requests d
WHERE s.id = d.server_id
  AND d.approved = true
  AND d.approved_at < NOW();

-- Med subquery
UPDATE servers
SET status = 'offline'
WHERE id IN (
    SELECT server_id
    FROM health_checks
    WHERE status = 'failed'
    GROUP BY server_id
    HAVING COUNT(*) > 3
);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## DELETE

### Grundlaggande DELETE

```sql
-- Ta bort specifika rader
DELETE FROM servers
WHERE status = 'decommissioned';

-- Ta bort med datum
DELETE FROM logs
WHERE created_at < NOW() - INTERVAL '90 days';

-- Med RETURNING (se vad som togs bort)
DELETE FROM servers
WHERE hostname = 'old-server'
RETURNING *;
```

### DELETE med subquery

```sql
-- Ta bort baserat pa annan tabell
DELETE FROM deployment_logs
WHERE deployment_id IN (
    SELECT id
    FROM deployments
    WHERE environment = 'development'
      AND deployed_at < NOW() - INTERVAL '30 days'
);

-- Med EXISTS
DELETE FROM servers s
WHERE EXISTS (
    SELECT 1
    FROM decommission_list d
    WHERE d.server_id = s.id
);

-- Med NOT EXISTS (ta bort orphans)
DELETE FROM server_tags
WHERE NOT EXISTS (
    SELECT 1
    FROM servers
    WHERE servers.id = server_tags.server_id
);
```

### DELETE vs TRUNCATE

```sql
-- DELETE - loggad, kan ha WHERE, triggar triggers
DELETE FROM logs;  -- Langsam for stora tabeller

-- TRUNCATE - snabb, ingen loggning per rad, inga triggers
TRUNCATE TABLE logs;

-- TRUNCATE med restart identity
TRUNCATE TABLE logs RESTART IDENTITY;

-- TRUNCATE flera tabeller
TRUNCATE TABLE logs, audit_trail RESTART IDENTITY;

-- TRUNCATE med cascade (foreign keys)
TRUNCATE TABLE deployments CASCADE;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Transaktioner

```sql
-- Starta transaktion
BEGIN;

-- Utfor operationer
UPDATE accounts
SET balance = balance - 100
WHERE id = 1;

UPDATE accounts
SET balance = balance + 100
WHERE id = 2;

-- Om allt OK - spara
COMMIT;

-- Om nagot gick fel - angra allt
ROLLBACK;

-- Med SAVEPOINT for delvis rollback
BEGIN;

INSERT INTO orders (customer_id, total) VALUES (1, 500);
SAVEPOINT order_created;

INSERT INTO order_items (order_id, product_id, quantity) VALUES (1, 10, 2);
-- Om detta misslyckas kan vi gora:
ROLLBACK TO SAVEPOINT order_created;
-- Ordern finns kvar, men inte items

COMMIT;
```

### Transaktion best practices

```sql
-- Halla transaktioner korta
BEGIN;
-- Gor bara det nödvändiga
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Undvik SELECT inne i transaktion om möjligt
-- (lasar rader och blockerar andra)

-- Anvand explicit locking vid behov
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- Nu ar raden last tills COMMIT
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Operation | Syntax | Beskrivning |
|-----------|--------|-------------|
| INSERT | `INSERT INTO t (c) VALUES (v)` | Lagg till rad |
| INSERT multi | `INSERT INTO t (c) VALUES (v1), (v2)` | Flera rader |
| INSERT SELECT | `INSERT INTO t SELECT ... FROM t2` | Kopiera data |
| UPSERT | `INSERT ... ON CONFLICT DO UPDATE` | Insert eller update |
| UPDATE | `UPDATE t SET c=v WHERE ...` | Uppdatera rader |
| UPDATE JOIN | `UPDATE t SET c=v FROM t2 WHERE t.id=t2.id` | Update med join |
| DELETE | `DELETE FROM t WHERE ...` | Ta bort rader |
| TRUNCATE | `TRUNCATE TABLE t` | Tom tabell snabbt |
| RETURNING | `INSERT/UPDATE/DELETE ... RETURNING *` | Returnera paverkade rader |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

### Problem 1: UPDATE/DELETE utan WHERE

```sql
-- FARLIGT! Paverkar ALLA rader
UPDATE servers SET status = 'offline';  -- Hela tabellen!
DELETE FROM servers;  -- Allt borta!

-- SAKERT TILLVAGAGANGSSATT:
-- 1. Kor forst SELECT for att se vilka rader som paverkas
SELECT * FROM servers WHERE status = 'decommissioned';

-- 2. Om OK, kor samma WHERE i UPDATE/DELETE
DELETE FROM servers WHERE status = 'decommissioned';

-- 3. Anvand LIMIT for extra sakerhet (PostgreSQL)
DELETE FROM logs
WHERE created_at < '2024-01-01'
LIMIT 1000;  -- Gor i batchar
```

### Problem 2: Foreign key constraint

```sql
-- FEL - kan inte ta bort parent om children finns
DELETE FROM deployments WHERE id = 1;
-- ERROR: update or delete violates foreign key constraint

-- LOSNING 1: Ta bort children forst
DELETE FROM deployment_logs WHERE deployment_id = 1;
DELETE FROM deployments WHERE id = 1;

-- LOSNING 2: Anvand ON DELETE CASCADE vid tabell-skapande
-- (se Node 3)

-- LOSNING 3: Anvand CASCADE i DELETE (om stodjs)
DELETE FROM deployments WHERE id = 1 CASCADE;
```

### Problem 3: Deadlock vid UPDATE

```sql
-- Kan orsaka deadlock om tva transaktioner uppdaterar
-- samma rader i olika ordning

-- LOSNING: Uppdatera i konsekvent ordning
UPDATE accounts SET balance = balance - 100
WHERE id IN (1, 2)
ORDER BY id;  -- Alltid samma ordning
```

### Problem 4: INSERT returnerar inte ID

```sql
-- Problem: Behovs id for nasta operation
INSERT INTO orders (customer_id) VALUES (1);
-- Hur far jag order_id?

-- LOSNING: Anvand RETURNING
INSERT INTO orders (customer_id) VALUES (1)
RETURNING id;

-- Eller i applikationskod (lastval)
INSERT INTO orders (customer_id) VALUES (1);
SELECT lastval();  -- Returnerar senast genererade SERIAL
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktisk ovning

Hantera en deployment-pipeline med DML:

```sql
-- Setup
CREATE TABLE IF NOT EXISTS deployments (
    id SERIAL PRIMARY KEY,
    service VARCHAR(100) NOT NULL,
    version VARCHAR(20) NOT NULL,
    env VARCHAR(20) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    deployed_at TIMESTAMPTZ DEFAULT NOW()
);

-- 1. INSERT: Ny deployment
INSERT INTO deployments (service, version, env)
VALUES ('api-gateway', 'v2.1.0', 'production')
RETURNING id, service, status;

-- 2. UPDATE: Markera som running
UPDATE deployments
SET status = 'running'
WHERE service = 'api-gateway' AND version = 'v2.1.0' AND env = 'production'
RETURNING *;

-- 3. UPSERT: Uppdatera om finns, annars skapa
INSERT INTO deployments (service, version, env, status)
VALUES ('api-gateway', 'v2.1.0', 'production', 'success')
ON CONFLICT (service, version, env)  -- Kraver UNIQUE constraint
DO UPDATE SET status = EXCLUDED.status;

-- 4. DELETE: Rensa gamla deployments
DELETE FROM deployments
WHERE deployed_at < NOW() - INTERVAL '30 days'
  AND env = 'development'
RETURNING id, service;

-- 5. Transaktion: Atomic deployment update
BEGIN;
UPDATE deployments SET status = 'rolling_back' WHERE id = 1;
INSERT INTO deployment_logs (deployment_id, message) VALUES (1, 'Rollback initiated');
COMMIT;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- Anvand ALLTID WHERE vid UPDATE och DELETE - annars paverkas alla rader
- Kor SELECT forst for att se vilka rader som paverkas
- Anvand RETURNING for att se resultatet av INSERT/UPDATE/DELETE
- ON CONFLICT (UPSERT) ar kraftfullt for idempotenta operationer
- TRUNCATE ar mycket snabbare an DELETE for stora tabeller
- Transaktioner (BEGIN/COMMIT/ROLLBACK) garanterar atomicitet
- Undvik langa transaktioner - de lasar resurser
- Anvand LIMIT vid batched deletes for att undvika lange lås

Nasta steg: Node 5 - SELECT Basics
''',
}

SQL_BLOCK_1 = [
    NODE_01_SQL_INTRO,
    NODE_02_DATA_TYPES,
    NODE_03_DDL_CREATE,
    NODE_04_DML_BASICS,
]
