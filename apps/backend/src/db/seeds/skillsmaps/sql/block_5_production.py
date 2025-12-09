# =============================================================================
# BLOCK 5: PRODUCTION (Noder 17-20)
# =============================================================================

NODE_17_DB_DESIGN = {
    "node_id": 17,
    "title": "Database Design",
    "slug": "db-design",
    "estimated_minutes": 60,
    "xp_reward": 165,
    "prerequisites": [3],
    "content": '''# Database Design

Bra databasdesign ar grunden for allt - prestanda, skalbarhet och underhallbarhet. Ett daligt schema kan inte fixas med index eller kraftfullare servrar.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

```
┌─────────────────────────────────────────────────────────────────┐
│                    DATABASE DESIGN IMPACT                       │
├─────────────────────────────────────────────────────────────────┤
│  BRA DESIGN:                                                    │
│  - Queries ar enkla att skriva och forsta                      │
│  - Index fungerar effektivt                                    │
│  - Data ar konsistent utan manuell validering                  │
│  - Schema ar sjalvdokumenterande                               │
├─────────────────────────────────────────────────────────────────┤
│  DALIGT DESIGN:                                                 │
│  - Komplexa queries for enkla fragor                           │
│  - Duplicerad data som blir inkonsistent                       │
│  - Ingen referentiell integritet                               │
│  - Evigt teknisk skuld                                         │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Normalisering

Normalisering eliminerar redundans och beroenden:

```
┌──────────┬────────────────────────────────────────────────────────┐
│ 1NF      │ Atomiska varden - inga listor i en kolumn             │
│          │ Varje rad ar unik (har primary key)                   │
├──────────┼────────────────────────────────────────────────────────┤
│ 2NF      │ Inga partial dependencies                              │
│          │ Alla non-key kolumner beror pa HELA primary key       │
├──────────┼────────────────────────────────────────────────────────┤
│ 3NF      │ Inga transitive dependencies                           │
│          │ Non-key kolumner beror BARA pa primary key            │
└──────────┴────────────────────────────────────────────────────────┘
```

```sql
-- BRYTER 1NF - lista i en kolumn
CREATE TABLE servers_bad (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100),
    ip_addresses VARCHAR(255)  -- "10.0.0.1,10.0.0.2,10.0.0.3"
);

-- UPPFYLLER 1NF - separat tabell for IP-adresser
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL
);

CREATE TABLE server_ips (
    id SERIAL PRIMARY KEY,
    server_id INTEGER REFERENCES servers(id) ON DELETE CASCADE,
    ip_address INET NOT NULL,
    is_primary BOOLEAN DEFAULT false
);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Relationships

```sql
-- ONE-TO-MANY: Ett team har manga servrar
CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL,
    team_id INTEGER REFERENCES teams(id) ON DELETE SET NULL
);

-- MANY-TO-MANY: Servrar kan ha manga tags, tags kan finnas pa manga servrar
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE server_tags (
    server_id INTEGER REFERENCES servers(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (server_id, tag_id)
);

-- ONE-TO-ONE: En server har exakt en detaljerad config
CREATE TABLE server_configs (
    server_id INTEGER PRIMARY KEY REFERENCES servers(id) ON DELETE CASCADE,
    config_data JSONB NOT NULL,
    last_updated TIMESTAMPTZ DEFAULT NOW()
);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Naming Conventions

```
TABELLER:
  - snake_case
  - Singular (server, deployment, team)
  - Junction tables: plural (server_tags)

KOLUMNER:
  - snake_case
  - Beskrivande (created_at, ip_address, hostname)
  - Foreign keys: <tabell>_id (team_id, server_id)

INDEX:
  - idx_<tabell>_<kolumner>
  - idx_servers_status
  - idx_deployments_server_created

CONSTRAINTS:
  - <tabell>_<kolumn>_<typ>
  - servers_hostname_unique
  - deployments_server_id_fkey
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga Patterns

```sql
-- SOFT DELETE
ALTER TABLE servers ADD COLUMN deleted_at TIMESTAMPTZ;

-- Partial index for aktiva poster
CREATE INDEX idx_servers_active ON servers(id)
WHERE deleted_at IS NULL;

-- TIMESTAMPS (pa alla tabeller)
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- STATUS SOM ENUM
CREATE TYPE server_status AS ENUM (
    'pending', 'active', 'maintenance', 'offline', 'deleted'
);

ALTER TABLE servers ADD COLUMN status server_status DEFAULT 'pending';

-- UUID SOM PRIMARY KEY (for distribuerade system)
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER NOT NULL,
    data JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Schema Organisation

```sql
-- Separata schemas for olika domanomraden
CREATE SCHEMA core;
CREATE SCHEMA monitoring;
CREATE SCHEMA billing;
CREATE SCHEMA audit;

-- Tabeller i respektive schema
CREATE TABLE core.servers (...);
CREATE TABLE core.teams (...);
CREATE TABLE monitoring.metrics (...);
CREATE TABLE monitoring.alerts (...);
CREATE TABLE billing.invoices (...);
CREATE TABLE audit.changes (...);

-- Satt search path for applikationen
SET search_path TO core, monitoring, public;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Anti-patterns att undvika

```sql
-- ANTI-PATTERN: Entity-Attribute-Value (EAV)
CREATE TABLE server_attributes (
    server_id INTEGER,
    attribute_name VARCHAR(100),
    attribute_value TEXT
);
-- Problem: Ingen type safety, svarjoined queries

-- BATTRE: Riktiga kolumner eller JSONB
ALTER TABLE servers ADD COLUMN metadata JSONB DEFAULT '{}';

-- ANTI-PATTERN: Polymorphic associations
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    commentable_type VARCHAR(50),  -- 'server' eller 'deployment'
    commentable_id INTEGER,
    content TEXT
);
-- Problem: Ingen referentiell integritet

-- BATTRE: Separata foreign keys med CHECK constraint
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    server_id INTEGER REFERENCES servers(id),
    deployment_id INTEGER REFERENCES deployments(id),
    content TEXT NOT NULL,
    CHECK (
        (server_id IS NOT NULL AND deployment_id IS NULL) OR
        (server_id IS NULL AND deployment_id IS NOT NULL)
    )
);
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Normal Form | Regel |
|-------------|-------|
| 1NF | Atomiska varden, unika rader |
| 2NF | Inga partial dependencies pa composite key |
| 3NF | Inga transitive dependencies |

| Relationship | Implementation |
|--------------|----------------|
| 1:1 | Foreign key som ar PRIMARY KEY |
| 1:N | Foreign key i "many"-tabellen |
| M:N | Junction table med composite key |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

### Ingen ON DELETE-strategi

```sql
-- FEL - vad hander nar team raderas?
CREATE TABLE servers (
    team_id INTEGER REFERENCES teams(id)  -- Default: NO ACTION
);
-- DELETE fran teams failar om servrar finns

-- ALTERNATIV:
ON DELETE CASCADE    -- Radera servrar automatiskt
ON DELETE SET NULL   -- Satt team_id till NULL
ON DELETE RESTRICT   -- Samma som NO ACTION (explicit)
```

### Over-normalisering

```sql
-- FEL - separat tabell for status
CREATE TABLE server_statuses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);
-- Onodigt for statisk lista

-- BATTRE - anvand ENUM
CREATE TYPE server_status AS ENUM ('active', 'inactive', 'maintenance');
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktisk ovning

```sql
-- Design: Server inventory system

-- Teams som ager servrar
CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Servrar med metadata
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL UNIQUE,
    ip_address INET,
    team_id INTEGER REFERENCES teams(id) ON DELETE SET NULL,
    environment VARCHAR(20) NOT NULL,
    status server_status DEFAULT 'pending',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    deleted_at TIMESTAMPTZ
);

-- Tags for kategorisering (M:N)
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE server_tags (
    server_id INTEGER REFERENCES servers(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (server_id, tag_id)
);

-- Index
CREATE INDEX idx_servers_team ON servers(team_id);
CREATE INDEX idx_servers_env ON servers(environment);
CREATE INDEX idx_servers_active ON servers(id) WHERE deleted_at IS NULL;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- Normalisera till 3NF som standard - denormalisera endast med mattning
- Anvand konsekvent namngivning - snake_case, singular, beskrivande
- Alla tabeller ska ha created_at/updated_at timestamps
- Anvand ENUM for statiska varden, JSONB for flexibel metadata
- Implementera soft delete med deleted_at nar data maste bevaras
- Definiera alltid ON DELETE-strategi for foreign keys
- Separata schemas for olika domanomraden
- Undvik EAV och polymorphic associations - de ger problem pa sikt
- UUID for distribuerade system, SERIAL for enkla applikationer
- Dokumentera design decisions - du kommer tacka dig sjalv senare

Nasta steg: Node 18 - Migrations
''',
}

NODE_18_MIGRATIONS = {
    "node_id": 18,
    "title": "Migrations",
    "slug": "migrations",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [17],
    "content": '''# Migrations

Migrations ar versionshanterade schema-andringar. Aldrig gor manuella andringar i produktion - allt gar genom migrations som ar granskade, testade och kan rullas tillbaka.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

```
┌─────────────────────────────────────────────────────────────────┐
│                    MIGRATIONS BENEFITS                          │
├─────────────────────────────────────────────────────────────────┤
│  - Versionskontroll: Schema-andringar ar sparbara i Git        │
│  - Code review: Andringar granskas innan deploy                │
│  - Reproducerbarhet: Samma schema i dev, staging, prod         │
│  - Rollback: Kan angra misslyckade andringar                   │
│  - Audit trail: Vet vem som andrade vad och nar                │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Migration Basics

Varje migration har UP (apply) och DOWN (rollback):

```sql
-- Migrationshistorik sparas i databasen
CREATE TABLE schema_migrations (
    version VARCHAR(14) PRIMARY KEY,
    applied_at TIMESTAMPTZ DEFAULT NOW()
);

-- Migration-filnamn: <timestamp>_<beskrivning>.sql
-- 20240115120000_create_servers.sql
```

```sql
-- 20240115120000_create_servers.up.sql
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL UNIQUE,
    ip_address INET,
    environment VARCHAR(20) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_servers_status ON servers(status);
CREATE INDEX idx_servers_environment ON servers(environment);

-- 20240115120000_create_servers.down.sql
DROP INDEX IF EXISTS idx_servers_environment;
DROP INDEX IF EXISTS idx_servers_status;
DROP TABLE IF EXISTS servers;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Sakra Migrations

```
┌───────────────────────────────────────────────────────────────┐
│  SAKERT (minimal lock, kan rullas tillbaka)                   │
├───────────────────────────────────────────────────────────────┤
│  - ADD COLUMN (nullable)                                      │
│  - ADD COLUMN med DEFAULT (PG11+)                            │
│  - DROP COLUMN                                                │
│  - CREATE INDEX CONCURRENTLY                                  │
│  - DROP INDEX CONCURRENTLY                                    │
│  - ADD CONSTRAINT (check, foreign key med NOT VALID)         │
└───────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────┐
│  FARLIGT (lang lock, kraver planering)                        │
├───────────────────────────────────────────────────────────────┤
│  - ADD COLUMN med NOT NULL utan default                      │
│  - ALTER COLUMN TYPE                                          │
│  - RENAME COLUMN                                              │
│  - CREATE INDEX (utan CONCURRENTLY)                          │
│  - ADD CONSTRAINT (med immediate validation)                  │
└───────────────────────────────────────────────────────────────┘
```

```sql
-- SAKERT: Lagg till nullable kolumn
ALTER TABLE servers ADD COLUMN region VARCHAR(50);

-- SAKERT: Lagg till kolumn med default (PG11+, instant)
ALTER TABLE servers ADD COLUMN is_active BOOLEAN DEFAULT true;

-- FARLIGT: NOT NULL utan default
ALTER TABLE servers ADD COLUMN team_id INTEGER NOT NULL;
-- ERROR: kolumn kan inte vara NOT NULL utan default

-- SAKERT: Tre-stegs approach for NOT NULL
-- Steg 1: Nullable
ALTER TABLE servers ADD COLUMN team_id INTEGER;

-- Steg 2: Backfill (kan ta tid, gor i batches)
UPDATE servers SET team_id = 1 WHERE team_id IS NULL;

-- Steg 3: Lagg till constraint
ALTER TABLE servers ALTER COLUMN team_id SET NOT NULL;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Expand-Contract Pattern

For faror operationer som RENAME COLUMN:

```
┌──────────────────────────────────────────────────────────────┐
│  1. EXPAND: Lagg till ny kolumn                              │
│  2. MIGRATE: Kopiera data, dual-write                        │
│  3. CONTRACT: Ta bort gammal kolumn                          │
└──────────────────────────────────────────────────────────────┘
```

```sql
-- Byt namn pa "ip" till "ip_address"

-- Migration 1: EXPAND
ALTER TABLE servers ADD COLUMN ip_address INET;

-- Applikationen uppdateras for att skriva till BADA kolumner
-- dual_write = True

-- Migration 2: MIGRATE
UPDATE servers SET ip_address = ip WHERE ip_address IS NULL;

-- Applikationen uppdateras for att lasa fran ip_address
-- read_from = 'ip_address'

-- Migration 3: CONTRACT (veckor/manader senare)
ALTER TABLE servers DROP COLUMN ip;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Index-operationer

```sql
-- FARLIGT: Lasar tabellen under skapandet
CREATE INDEX idx_servers_hostname ON servers(hostname);
-- Pa stor tabell: minuter till timmar av lock!

-- SAKERT: Skapar utan lock (men tar langre tid)
CREATE INDEX CONCURRENTLY idx_servers_hostname ON servers(hostname);

-- OBSERVERA: CONCURRENTLY kan inte koras i transaktion
-- Maste koras utanfor BEGIN/COMMIT

-- Ta bort index sakert
DROP INDEX CONCURRENTLY IF EXISTS idx_servers_hostname;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Migration-verktyg

```bash
# golang-migrate
migrate create -ext sql -dir migrations -seq create_servers
migrate -path migrations -database "postgresql://user:pass@host/db" up
migrate -path migrations -database "postgresql://user:pass@host/db" down 1

# Alembic (Python)
alembic init alembic
alembic revision -m "create_servers"
alembic upgrade head
alembic downgrade -1

# Flyway (Java/generell)
flyway migrate
flyway info
flyway undo
```

Alembic exempel (Python):

```python
# alembic/versions/20240115_create_servers.py
from alembic import op
import sqlalchemy as sa

revision = '20240115'
down_revision = None

def upgrade():
    op.create_table(
        'servers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('hostname', sa.String(100), nullable=False),
        sa.Column('status', sa.String(20), server_default='pending'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now())
    )
    op.create_index('idx_servers_status', 'servers', ['status'])

def downgrade():
    op.drop_index('idx_servers_status')
    op.drop_table('servers')
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Operation | Saker? | Lock-tid |
|-----------|--------|----------|
| ADD COLUMN (nullable) | Ja | Kort |
| ADD COLUMN med DEFAULT | Ja | Kort (PG11+) |
| DROP COLUMN | Ja | Kort |
| CREATE INDEX | Nej | Lang |
| CREATE INDEX CONCURRENTLY | Ja | Ingen |
| RENAME COLUMN | Nej | Kort (bryter app) |
| ALTER COLUMN TYPE | Nej | Lang |
| ADD NOT NULL | Nej | Kort (kraver data) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

### Index utan CONCURRENTLY

```sql
-- FEL - lasar tabellen i produktion
CREATE INDEX idx_logs_timestamp ON logs(timestamp);

-- RATT - ingen lock
CREATE INDEX CONCURRENTLY idx_logs_timestamp ON logs(timestamp);
```

### Glommer down-migration

```sql
-- up.sql finns men down.sql saknas
-- Problem: Kan inte rulla tillbaka vid fel!

-- Skriv ALLTID bada
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Migration Checklist

```
PRE-DEPLOY:
[ ] Testat pa staging med produktions-liknande data
[ ] Estimerat lock-tid
[ ] Kontrollerat diskutrymme
[ ] Planerat rollback-strategi
[ ] Code review godkand

DEPLOY:
[ ] Tagit backup
[ ] Kort driftfonstret
[ ] Kort migration
[ ] Verifierat data-integritet
[ ] Monitorerat prestanda

POST-DEPLOY:
[ ] Kort ANALYZE pa andrande tabeller
[ ] Kontrollerat slow query log
[ ] Dokumenterat andringar
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktisk ovning

```sql
-- Migration: Lagg till deployments-tabell

-- 20240116_create_deployments.up.sql
CREATE TABLE deployments (
    id SERIAL PRIMARY KEY,
    server_id INTEGER NOT NULL REFERENCES servers(id) ON DELETE CASCADE,
    version VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    deployed_by INTEGER,
    deployed_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ
);

-- Index CONCURRENTLY for att undvika lock
-- Maste koras separat, utanfor transaktion
CREATE INDEX CONCURRENTLY idx_deployments_server
ON deployments(server_id);

CREATE INDEX CONCURRENTLY idx_deployments_status
ON deployments(status);

-- 20240116_create_deployments.down.sql
DROP INDEX CONCURRENTLY IF EXISTS idx_deployments_status;
DROP INDEX CONCURRENTLY IF EXISTS idx_deployments_server;
DROP TABLE IF EXISTS deployments;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- Aldrig manuella schema-andringar i produktion - alltid migrations
- Varje migration har UP och DOWN - maste kunna rullas tillbaka
- CONCURRENTLY for alla index-operationer i produktion
- Expand-Contract for farliga andringar (rename, type change)
- Tre-stegs approach for NOT NULL: nullable -> backfill -> constraint
- Testa migrations pa staging med produktions-liknande datamangd
- Ta backup innan migration i produktion
- Koda defensivt: IF EXISTS, IF NOT EXISTS
- Gor migrations sma - lattare att rulla tillbaka
- Lock-tid ar kritisk - estimera och kommunicera

Nasta steg: Node 19 - Backup och Recovery
''',
}

NODE_19_BACKUP = {
    "node_id": 19,
    "title": "Backup & Recovery",
    "slug": "backup-recovery",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [18],
    "content": '''# Backup och Recovery

Backups ar din forsakring mot katastrofer. En backup du aldrig testat ar inte en backup - det ar falsk trygghet. Testa restore regelbundet!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

```
┌─────────────────────────────────────────────────────────────────┐
│                    BACKUP SCENARIOS                             │
├─────────────────────────────────────────────────────────────────┤
│  - Hardvaruhaveri: Disk kraschar                               │
│  - Manskliga fel: Nagon kor DELETE utan WHERE                  │
│  - Ransomware: Data krypteras av angripare                     │
│  - Korruption: Data blir ogiltig                               │
│  - Compliance: Krav pa databevarande                           │
├─────────────────────────────────────────────────────────────────┤
│  UTAN BACKUP: Foretaget stannar, data ar borta for alltid      │
│  MED BACKUP: Stundtals nedtid, men data aterhamtas             │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Backup-typer

```
┌─────────────────┬────────────────────────────────────────────────┐
│ LOGICAL BACKUP  │ SQL-statements eller data-export               │
│ (pg_dump)       │ + Portabelt mellan versioner                  │
│                 │ + Kan aterstalla enskilda tabeller            │
│                 │ - Langsammare backup/restore                  │
│                 │ - Ingen Point-in-Time Recovery                │
├─────────────────┼────────────────────────────────────────────────┤
│ PHYSICAL BACKUP │ Binara datafiler                               │
│ (pg_basebackup) │ + Snabbare backup/restore                     │
│                 │ + Stodjer PITR                                │
│                 │ - Kraver samma PostgreSQL-version             │
│                 │ - Allt-eller-inget restore                    │
└─────────────────┴────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## pg_dump - Logical Backup

```bash
# Full database backup (SQL-format)
pg_dump -h localhost -U postgres mydb > backup.sql

# Custom format (komprimerad, flexibel restore)
pg_dump -Fc -h localhost -U postgres mydb > backup.dump

# Directory format (parallell, battre for stora databaser)
pg_dump -Fd -j 4 -h localhost -U postgres mydb -f backup_dir/

# Endast schema (inga data)
pg_dump --schema-only mydb > schema.sql

# Endast data (inget schema)
pg_dump --data-only mydb > data.sql

# Specifik tabell
pg_dump -t servers -t deployments mydb > tables.sql

# Exkludera tabeller (t.ex. logs)
pg_dump --exclude-table='logs*' mydb > backup_no_logs.sql
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## pg_restore - Aterstallning

```bash
# Fran custom format
pg_restore -d mydb backup.dump

# Skapa ny databas och aterstall
createdb mydb_restored
pg_restore -d mydb_restored backup.dump

# Parallell restore (snabbare)
pg_restore -j 4 -d mydb backup_dir/

# Endast specifik tabell
pg_restore -t servers -d mydb backup.dump

# Lista innehall i backup
pg_restore -l backup.dump

# Fran SQL-format (anvand psql)
psql -d mydb -f backup.sql
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## pg_dumpall - Alla databaser

```bash
# Alla databaser + roller + tablespaces
pg_dumpall -h localhost -U postgres > full_cluster.sql

# Endast roller (users)
pg_dumpall --roles-only > roles.sql

# Endast tablespaces
pg_dumpall --tablespaces-only > tablespaces.sql

# Aterstall
psql -f full_cluster.sql postgres
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## pg_basebackup - Physical Backup

```bash
# Standard basebackup
pg_basebackup -h localhost -U replication_user \
    -D /backups/base \
    -Fp -Xs -P

# Med komprimering (tar.gz)
pg_basebackup -h localhost -U replication_user \
    -D /backups/base \
    -Ft -z -Xs -P

# Flaggor:
# -Fp = plain format (fil-kopior)
# -Ft = tar format
# -z = gzip komprimering
# -Xs = stream WAL under backup
# -P = visa progress
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Point-in-Time Recovery (PITR)

Aterstall till exakt tidpunkt:

```bash
# 1. Aktivera WAL archiving (postgresql.conf)
wal_level = replica
archive_mode = on
archive_command = 'cp %p /var/lib/pgsql/archive/%f'

# 2. Ta basebackup
pg_basebackup -D /backups/base -Fp -Xs -P

# 3. Vid behov av recovery, skapa recovery.signal
touch /var/lib/pgsql/data/recovery.signal

# 4. Konfigurera recovery (postgresql.conf)
restore_command = 'cp /var/lib/pgsql/archive/%f %p'
recovery_target_time = '2024-01-15 10:30:00'

# 5. Starta PostgreSQL - den aterhamtar till angiven tid
```

PITR ar kritiskt for att aterstalla fran "oops"-moment:
- DELETE utan WHERE
- DROP TABLE
- Bad migration

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Backup-script

```bash
#!/bin/bash
# backup.sh - Daglig backup med retention

DB_NAME="production"
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
RETENTION_DAYS=30

# Skapa backup
echo "Starting backup of $DB_NAME..."
pg_dump -Fc "$DB_NAME" > "$BACKUP_DIR/${DB_NAME}_${DATE}.dump"

# Verifiera att backup skapades
if [ $? -eq 0 ] && [ -s "$BACKUP_DIR/${DB_NAME}_${DATE}.dump" ]; then
    echo "Backup successful: ${DB_NAME}_${DATE}.dump"

    # Kontrollera storlek
    SIZE=$(du -h "$BACKUP_DIR/${DB_NAME}_${DATE}.dump" | cut -f1)
    echo "Backup size: $SIZE"

    # Ta bort gamla backups
    find "$BACKUP_DIR" -name "${DB_NAME}_*.dump" -mtime +$RETENTION_DAYS -delete
    echo "Removed backups older than $RETENTION_DAYS days"
else
    echo "ERROR: Backup failed!" >&2
    exit 1
fi
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Testa Backup (KRITISKT!)

```bash
# 1. Lista innehall
pg_restore -l backup.dump

# 2. Aterstall till test-databas
createdb test_restore
pg_restore -d test_restore backup.dump

# 3. Verifiera data
psql -d test_restore -c "
    SELECT
        (SELECT COUNT(*) FROM servers) AS servers,
        (SELECT COUNT(*) FROM deployments) AS deployments,
        (SELECT MAX(created_at) FROM servers) AS latest_server;
"

# 4. Jamfor med produktion
# Ska vara samma antal rader, senaste timestamps

# 5. Rensa
dropdb test_restore
```

REGEL: Testa restore minst en gang per manad!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cloud Backup

```bash
# Till AWS S3
pg_dump -Fc mydb | aws s3 cp - s3://mybucket/backups/db_$(date +%Y%m%d).dump

# Fran S3
aws s3 cp s3://mybucket/backups/db_20240115.dump - | pg_restore -d mydb

# Med gzip (mindre storlek)
pg_dump mydb | gzip | aws s3 cp - s3://mybucket/backups/db_$(date +%Y%m%d).sql.gz

# Till Google Cloud Storage
pg_dump -Fc mydb | gsutil cp - gs://mybucket/backups/db_$(date +%Y%m%d).dump

# Till Azure Blob
pg_dump -Fc mydb | az storage blob upload --data @- \
    --container backups --name db_$(date +%Y%m%d).dump
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Backup-typ | Hastighet | Storlek | PITR | Flexibilitet |
|------------|-----------|---------|------|--------------|
| pg_dump SQL | Langsam | Stor | Nej | Hog |
| pg_dump Custom | Medium | Liten | Nej | Hog |
| pg_dump Dir | Snabb | Medium | Nej | Hog |
| pg_basebackup | Snabb | Stor | Ja | Lag |
| WAL Archiving | N/A | Medium | Ja | N/A |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

### Backup utan verifiering

```bash
# FEL - bara skapa backup utan att testa
pg_dump mydb > backup.sql
# Aldrig testad - kanske korrupt!

# RATT - alltid verifiera
pg_dump -Fc mydb > backup.dump
pg_restore -l backup.dump  # Lista innehall
# Periodiskt: full restore till test-db
```

### Ingen PITR-setup

```
# FEL - bara dagliga backups
# Om nagon kor DELETE kl 14:00, och backup ar fran kl 02:00,
# forlorar du 12 timmar data!

# RATT - WAL archiving for PITR
archive_mode = on
archive_command = 'cp %p /archive/%f'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Backup Checklist

```
DAGLIGEN:
[ ] Backup kor automatiskt (cron/scheduler)
[ ] Backup-storlek ar rimlig (inte 0 bytes)
[ ] Notifiering vid misslyckande

VECKOVIS:
[ ] Verifiera att restore fungerar
[ ] Kontrollera diskutrymme for backups
[ ] Granska retention policy

MANATLIGEN:
[ ] Full restore-test till separat server
[ ] Granska och uppdatera backup-strategi
[ ] Dokumentera RTO/RPO (Recovery Time/Point Objective)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- Backup du aldrig testat ar inte en backup - testa restore regelbundet!
- pg_dump -Fc (custom format) ar bast for de flesta fall
- pg_basebackup + WAL archiving for Point-in-Time Recovery
- 3-2-1 regeln: 3 kopior, 2 mediatyper, 1 offsite
- Automatisera backups med schemalagda jobb
- Monitorera backup-status och storlek
- Dokumentera och testa din recovery-procedur
- RTO (Recovery Time Objective): Hur snabbt maste du vara uppe?
- RPO (Recovery Point Objective): Hur mycket data kan du forlora?
- Spara backups offsite (cloud) - skyddar mot datacenter-katastrofer

Nasta steg: Node 20 - Monitoring och Best Practices
''',
}

NODE_20_MONITORING = {
    "node_id": 20,
    "title": "Monitoring & Best Practices",
    "slug": "monitoring-best-practices",
    "estimated_minutes": 55,
    "xp_reward": 160,
    "prerequisites": [14, 19],
    "content": '''# Monitoring och Best Practices

Monitoring ger dig insikt i databashalsan. Utan monitoring ser du problemen forst nar anvandare klagar - da ar det ofta for sent.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

```
┌─────────────────────────────────────────────────────────────────┐
│                    MONITORING BENEFITS                          │
├─────────────────────────────────────────────────────────────────┤
│  - Upptack problem INNAN anvandare marker                      │
│  - Kapacitetsplanering: nar behover vi skala?                  │
│  - Prestandaanalys: vilka queries ar langsamma?                │
│  - Sakerhet: upptack onormala monster                          │
│  - Postmortem: forsta vad som hande vid incident               │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Nyckelmetriker

```sql
-- Aktiva connections
SELECT
    count(*) AS total_connections,
    count(*) FILTER (WHERE state = 'active') AS active,
    count(*) FILTER (WHERE state = 'idle') AS idle,
    count(*) FILTER (WHERE state = 'idle in transaction') AS idle_in_transaction
FROM pg_stat_activity
WHERE datname = current_database();

-- Connections per databas
SELECT datname, count(*) AS connections
FROM pg_stat_activity
GROUP BY datname
ORDER BY connections DESC;

-- Database-storlek
SELECT
    datname,
    pg_size_pretty(pg_database_size(datname)) AS size
FROM pg_database
WHERE datname NOT IN ('template0', 'template1')
ORDER BY pg_database_size(datname) DESC;

-- Tabell-storlekar
SELECT
    schemaname || '.' || relname AS table_name,
    pg_size_pretty(pg_total_relation_size(relid)) AS total_size,
    pg_size_pretty(pg_relation_size(relid)) AS table_size,
    pg_size_pretty(pg_indexes_size(relid)) AS index_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC
LIMIT 20;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## pg_stat_statements - Query Analysis

```sql
-- Aktivera extension
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Langsamma queries (hogst mean time)
SELECT
    substring(query, 1, 100) AS query_preview,
    calls,
    round(mean_exec_time::numeric, 2) AS mean_ms,
    round(total_exec_time::numeric, 2) AS total_ms,
    rows
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 20;

-- Mest resurskravande (total tid)
SELECT
    substring(query, 1, 100) AS query_preview,
    calls,
    round(total_exec_time::numeric / 1000, 2) AS total_seconds,
    round(mean_exec_time::numeric, 2) AS mean_ms
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 20;

-- Reset statistik
SELECT pg_stat_statements_reset();
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Lock Monitoring

```sql
-- Visa blockerade queries
SELECT
    blocked.pid AS blocked_pid,
    blocked.usename AS blocked_user,
    blocked.query AS blocked_query,
    blocking.pid AS blocking_pid,
    blocking.usename AS blocking_user,
    blocking.query AS blocking_query,
    now() - blocked.query_start AS blocked_duration
FROM pg_stat_activity blocked
JOIN pg_locks blocked_locks ON blocked.pid = blocked_locks.pid
JOIN pg_locks blocking_locks
    ON blocked_locks.locktype = blocking_locks.locktype
    AND blocked_locks.relation = blocking_locks.relation
    AND blocked_locks.pid != blocking_locks.pid
JOIN pg_stat_activity blocking ON blocking_locks.pid = blocking.pid
WHERE NOT blocked_locks.granted
  AND blocking_locks.granted;

-- Doda blockerande query (forsiktigt!)
SELECT pg_terminate_backend(12345);  -- Ersatt med blocking_pid

-- Langkorda queries
SELECT
    pid,
    now() - query_start AS duration,
    state,
    substring(query, 1, 100) AS query
FROM pg_stat_activity
WHERE state != 'idle'
  AND query_start < now() - interval '5 minutes'
ORDER BY query_start;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Index Health

```sql
-- Index-anvandning
SELECT
    schemaname,
    relname AS table_name,
    indexrelname AS index_name,
    idx_scan AS times_used,
    pg_size_pretty(pg_relation_size(indexrelid)) AS size
FROM pg_stat_user_indexes
ORDER BY idx_scan DESC;

-- OANVANDA index (kandidater for borttagning)
SELECT
    schemaname || '.' || relname AS table_name,
    indexrelname AS index_name,
    pg_size_pretty(pg_relation_size(indexrelid)) AS size
FROM pg_stat_user_indexes
WHERE idx_scan = 0
  AND indexrelname NOT LIKE '%_pkey'
ORDER BY pg_relation_size(indexrelid) DESC;

-- Index bloat (fragmentation)
SELECT
    schemaname,
    relname AS table_name,
    indexrelname AS index_name,
    pg_size_pretty(pg_relation_size(indexrelid)) AS index_size,
    idx_scan
FROM pg_stat_user_indexes
ORDER BY pg_relation_size(indexrelid) DESC
LIMIT 20;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Table Health

```sql
-- Dead tuples (behover VACUUM)
SELECT
    schemaname,
    relname AS table_name,
    n_live_tup AS live_rows,
    n_dead_tup AS dead_rows,
    round(100.0 * n_dead_tup / nullif(n_live_tup + n_dead_tup, 0), 2) AS dead_pct,
    last_vacuum,
    last_autovacuum
FROM pg_stat_user_tables
WHERE n_dead_tup > 1000
ORDER BY n_dead_tup DESC;

-- Tabeller som inte vacuumats nyligen
SELECT
    schemaname || '.' || relname AS table_name,
    last_vacuum,
    last_autovacuum,
    n_dead_tup
FROM pg_stat_user_tables
WHERE (last_vacuum IS NULL OR last_vacuum < now() - interval '7 days')
  AND (last_autovacuum IS NULL OR last_autovacuum < now() - interval '7 days')
  AND n_dead_tup > 100
ORDER BY n_dead_tup DESC;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Connection Pooling (PgBouncer)

```ini
# pgbouncer.ini

[databases]
mydb = host=localhost port=5432 dbname=mydb

[pgbouncer]
listen_port = 6432
listen_addr = *
auth_type = md5
auth_file = /etc/pgbouncer/userlist.txt

# Pool-lage
pool_mode = transaction    # Rekommenderat

# Begransningar
max_client_conn = 1000     # Max klient-connections
default_pool_size = 20     # Connections per db/user
min_pool_size = 5          # Minsta antal connections
reserve_pool_size = 5      # Extra vid behov
```

Pool modes:
- **session**: En connection per session (minst effektiv)
- **transaction**: En connection per transaktion (rekommenderat)
- **statement**: En connection per statement (mest aggressiv)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## PostgreSQL Configuration

```ini
# postgresql.conf - viktiga parametrar

# Minne
shared_buffers = 256MB           # 25% av RAM (max 8-16GB)
effective_cache_size = 768MB     # 75% av RAM
work_mem = 64MB                  # Per operation/sort
maintenance_work_mem = 256MB     # For VACUUM, INDEX

# Connections
max_connections = 100            # Anvand connection pooler!

# WAL
wal_level = replica              # For PITR
max_wal_size = 1GB
min_wal_size = 80MB

# Checkpoints
checkpoint_completion_target = 0.9

# Logging
log_min_duration_statement = 1000  # Logga queries over 1 sekund
log_statement = 'ddl'              # Logga schema-andringar
log_lock_waits = on                # Logga lock-vantan

# Autovacuum
autovacuum = on
autovacuum_vacuum_scale_factor = 0.1
autovacuum_analyze_scale_factor = 0.05
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Maintenance

```sql
-- VACUUM: Atervinn utrymme fran raderade rader
VACUUM servers;

-- VACUUM ANALYZE: Atervinn + uppdatera statistik
VACUUM ANALYZE servers;

-- VACUUM FULL: Komprimera tabellen (LASAR TABELLEN!)
-- Anvand endast vid extremt bloat
VACUUM FULL servers;

-- ANALYZE: Uppdatera endast statistik
ANALYZE servers;

-- REINDEX: Bygg om index
REINDEX TABLE servers;
REINDEX INDEX CONCURRENTLY idx_servers_status;  -- Utan lock

-- Cluster: Fysiskt ordna tabell efter index
CLUSTER servers USING idx_servers_created;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Alertgranser

| Metrik | Varning | Kritisk |
|--------|---------|---------|
| Connections | 80% av max | 95% av max |
| Disk space | 80% | 90% |
| Replication lag | 30 sekunder | 5 minuter |
| Long queries | 30 sekunder | 5 minuter |
| Dead tuples | 10% av live | 25% av live |
| Cache hit ratio | < 95% | < 90% |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Monitoring Checklist

```
KONTINUERLIGT (var minut):
[ ] Connection count och state
[ ] Aktiva/langkorda queries
[ ] Replication lag (om replica)
[ ] Diskutrymme

DAGLIGEN:
[ ] Granska slow query log
[ ] Kolla table bloat (dead tuples)
[ ] Index usage statistik
[ ] Backup-status

VECKOVIS:
[ ] Verifiera backup restore
[ ] Kolla oanvanda index
[ ] Granska connection pool stats
[ ] Kapacitetsplanering

MANATLIGEN:
[ ] Full performance review
[ ] Schema-optimering
[ ] Uppdatera dokumentation
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktisk ovning - Monitoring Query

```sql
-- Komplett halsocheck
WITH stats AS (
    SELECT
        (SELECT count(*) FROM pg_stat_activity) AS total_connections,
        (SELECT count(*) FROM pg_stat_activity WHERE state = 'active') AS active_queries,
        (SELECT count(*) FROM pg_stat_activity WHERE state = 'idle in transaction') AS idle_in_tx,
        (SELECT pg_size_pretty(pg_database_size(current_database()))) AS db_size,
        (SELECT round(100.0 * sum(heap_blks_hit) / nullif(sum(heap_blks_hit) + sum(heap_blks_read), 0), 2)
         FROM pg_statio_user_tables) AS cache_hit_ratio,
        (SELECT count(*) FROM pg_stat_user_tables WHERE n_dead_tup > n_live_tup * 0.1) AS bloated_tables,
        (SELECT count(*) FROM pg_stat_user_indexes WHERE idx_scan = 0) AS unused_indexes
)
SELECT * FROM stats;
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

Kom ihag:

- Monitorera kontinuerligt: connections, queries, disk, replication
- pg_stat_statements ar ditt viktigaste verktyg for query-analys
- Anvand connection pooler (PgBouncer) - PostgreSQL skapar en process per connection
- Konfigurera alerting for kritiska metriker
- VACUUM regelbudet - autovacuum ar bra men inte alltid tillrackligt
- Kolla oanvanda index - de kostar vid writes
- Log slow queries - log_min_duration_statement
- Cache hit ratio bor vara over 95%
- Testa backup restore - inte bara att backup kor
- Dokumentera din monitoring-setup och eskaleringsprocess

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GRATTIS! Du har slutfort SQL SkillsMap!

Du beharkskar nu:

- SQL syntax och queries
- Avancerade tekniker: CTEs, Window Functions, JSONB
- Databasdesign och normalisering
- Prestandaoptimering med index och EXPLAIN
- Migrations och schema-hantering
- Backup, recovery och PITR
- Monitoring och best practices for produktion

Nasta steg: Applicera kunskapen i verkliga DevOps-scenarier!
''',
}

SQL_BLOCK_5 = [
    NODE_17_DB_DESIGN,
    NODE_18_MIGRATIONS,
    NODE_19_BACKUP,
    NODE_20_MONITORING,
]
