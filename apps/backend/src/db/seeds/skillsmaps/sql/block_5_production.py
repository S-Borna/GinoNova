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
    "content": '''# 🏛️ Database Design

## Varför detta är kritiskt
> "Ett dåligt schema kan inte fixas med index. Database design är grunden - gör det rätt från början eller lev med teknisk skuld för evigt."

## Vad du kommer lära dig
- ✅ Normalisering (1NF, 2NF, 3NF)
- ✅ Relationships (1:1, 1:N, M:N)
- ✅ Naming conventions
- ✅ Denormalisering för performance

---

## Normalization

```sql
-- 1NF: Atomic values, no repeating groups
-- Dåligt
CREATE TABLE servers (
    id SERIAL,
    hostname VARCHAR(100),
    ips VARCHAR(255)  -- "10.0.0.1,10.0.0.2"
);

-- Bra (1NF)
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100)
);
CREATE TABLE server_ips (
    server_id INTEGER REFERENCES servers(id),
    ip_address INET
);

-- 2NF: Bort med partial dependencies
-- 3NF: Bort med transitive dependencies
```

## Relationships

```sql
-- One-to-Many
CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    team_id INTEGER REFERENCES teams(id),
    hostname VARCHAR(100)
);

-- Many-to-Many
CREATE TABLE servers (id SERIAL PRIMARY KEY, hostname VARCHAR);
CREATE TABLE tags (id SERIAL PRIMARY KEY, name VARCHAR);

CREATE TABLE server_tags (
    server_id INTEGER REFERENCES servers(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (server_id, tag_id)
);

-- One-to-One
CREATE TABLE server_configs (
    server_id INTEGER PRIMARY KEY REFERENCES servers(id),
    config_data JSONB
);
```

## Naming Conventions

```sql
-- Snake_case för allt
-- Singular för tabeller
-- Plural för junction tables

-- Tabeller
CREATE TABLE server (...);
CREATE TABLE deployment (...);

-- Junction
CREATE TABLE server_tags (...);

-- Kolumner
hostname
ip_address
created_at
updated_at

-- Foreign keys
server_id
team_id

-- Index
idx_servers_status
idx_deployments_server_id

-- Constraints
servers_pkey
servers_hostname_unique
servers_team_id_fkey
```

## Common Patterns

```sql
-- Soft delete
ALTER TABLE servers ADD COLUMN deleted_at TIMESTAMPTZ;

CREATE INDEX idx_servers_active
ON servers(id) WHERE deleted_at IS NULL;

-- Timestamps
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Status enum
CREATE TYPE server_status AS ENUM (
    'pending', 'active', 'maintenance', 'offline', 'deleted'
);

ALTER TABLE servers ADD COLUMN status server_status DEFAULT 'pending';

-- UUID primary key
CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER,
    data JSONB
);
```

## Schema Organization

```sql
-- Separata schemas
CREATE SCHEMA core;
CREATE SCHEMA monitoring;
CREATE SCHEMA billing;

CREATE TABLE core.servers (...);
CREATE TABLE monitoring.metrics (...);
CREATE TABLE billing.invoices (...);

-- Search path
SET search_path TO core, monitoring, public;
```

## Anti-patterns

```sql
-- ❌ EAV (Entity-Attribute-Value)
CREATE TABLE attributes (
    entity_id INTEGER,
    attribute_name VARCHAR,
    attribute_value VARCHAR
);
-- Svårt att query, ingen type safety

-- ✅ Istället: Proper columns eller JSONB

-- ❌ Polymorphic associations
CREATE TABLE comments (
    id SERIAL,
    commentable_type VARCHAR,  -- 'server' or 'deployment'
    commentable_id INTEGER
);
-- Ingen referential integrity

-- ✅ Istället: Separate foreign keys
CREATE TABLE comments (
    id SERIAL,
    server_id INTEGER REFERENCES servers(id),
    deployment_id INTEGER REFERENCES deployments(id),
    CHECK (
        (server_id IS NOT NULL AND deployment_id IS NULL) OR
        (server_id IS NULL AND deployment_id IS NOT NULL)
    )
);
```

| Normal Form | Regel |
|-------------|-------|
| 1NF | Atomiska värden |
| 2NF | Inga partial dependencies |
| 3NF | Inga transitive dependencies |

**Nästa steg:** Node 18 - Migrations
''',
}

NODE_18_MIGRATIONS = {
    "node_id": 18,
    "title": "Migrations",
    "slug": "migrations",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [17],
    "content": '''# 🔄 Migrations

## Varför detta är kritiskt
> "Ingen ändrar schemat manuellt i prod. Migrations är den enda vägen - versionshanterad, granskad, och rollback-redo."

## Vad du kommer lära dig
- ✅ Migration tools (Alembic, Flyway, golang-migrate)
- ✅ Safe vs dangerous operations
- ✅ Expand-Contract pattern
- ✅ Zero-downtime schema changes

---

## Migration Basics

```sql
-- En migration är en fil med:
-- UP: Applicera change
-- DOWN: Rollback change

-- Migrationshistorik sparas i databas
CREATE TABLE schema_migrations (
    version VARCHAR(14) PRIMARY KEY,
    applied_at TIMESTAMPTZ DEFAULT NOW()
);
```

## SQL Migration Files

```sql
-- 20240115120000_create_servers.up.sql
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) NOT NULL,
    ip_address INET,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_servers_status ON servers(status);

-- 20240115120000_create_servers.down.sql
DROP TABLE IF EXISTS servers;
```

## Safe Migrations

```sql
-- ✅ Add column (safe)
ALTER TABLE servers ADD COLUMN environment VARCHAR(20);

-- ✅ Add nullable column with default
ALTER TABLE servers ADD COLUMN region VARCHAR(20) DEFAULT 'us-east-1';

-- ⚠️ Adding NOT NULL requires default or backfill
-- Steg 1: Add nullable
ALTER TABLE servers ADD COLUMN team_id INTEGER;

-- Steg 2: Backfill
UPDATE servers SET team_id = 1 WHERE team_id IS NULL;

-- Steg 3: Add constraint
ALTER TABLE servers ALTER COLUMN team_id SET NOT NULL;
```

## Dangerous Operations

```sql
-- ❌ Rename column (breaks application)
ALTER TABLE servers RENAME COLUMN ip TO ip_address;

-- ✅ Expand-Contract pattern:
-- 1. Add new column
ALTER TABLE servers ADD COLUMN ip_address INET;
-- 2. Dual-write i application
-- 3. Migrate data
UPDATE servers SET ip_address = ip WHERE ip_address IS NULL;
-- 4. Switch reads to new column
-- 5. Stop writing to old
-- 6. Drop old column (later migration)
ALTER TABLE servers DROP COLUMN ip;

-- ❌ Change column type (locks table)
ALTER TABLE servers ALTER COLUMN status TYPE VARCHAR(50);

-- ✅ For large tables, use new column approach
```

## Index Operations

```sql
-- ❌ CREATE INDEX locks table
CREATE INDEX idx_servers_hostname ON servers(hostname);

-- ✅ CONCURRENTLY doesn't lock
CREATE INDEX CONCURRENTLY idx_servers_hostname ON servers(hostname);

-- Same for drop
DROP INDEX CONCURRENTLY idx_servers_hostname;
```

## Migration Tools

```bash
# golang-migrate
migrate create -ext sql -dir migrations -seq create_servers
migrate -path migrations -database "postgresql://..." up
migrate -path migrations -database "postgresql://..." down 1

# Alembic (Python)
alembic revision -m "create_servers"
alembic upgrade head
alembic downgrade -1

# Flyway (Java)
flyway migrate
flyway undo
```

## Alembic Example

```python
# alembic/versions/20240115_create_servers.py
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'servers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('hostname', sa.String(100), nullable=False),
        sa.Column('status', sa.String(20), default='pending'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now())
    )
    op.create_index('idx_servers_status', 'servers', ['status'])

def downgrade():
    op.drop_index('idx_servers_status')
    op.drop_table('servers')
```

## Migration Checklist

```yaml
Pre-deploy:
  - [ ] Test migration on staging
  - [ ] Estimate lock time
  - [ ] Check disk space
  - [ ] Plan rollback

Deploy:
  - [ ] Take backup
  - [ ] Run migration
  - [ ] Verify data integrity
  - [ ] Monitor performance

Post-deploy:
  - [ ] ANALYZE updated tables
  - [ ] Check slow queries
  - [ ] Document changes
```

| Operation | Safe? | Lock? |
|-----------|-------|-------|
| ADD COLUMN | Ja | Kort |
| DROP COLUMN | Ja | Kort |
| ADD INDEX | Nej* | Lång |
| ADD INDEX CONCURRENTLY | Ja | Nej |
| RENAME COLUMN | Nej | Kort |
| CHANGE TYPE | Nej | Lång |

**Nästa steg:** Node 19 - Backup & Recovery
''',
}

NODE_19_BACKUP = {
    "node_id": 19,
    "title": "Backup & Recovery",
    "slug": "backup-recovery",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [18],
    "content": '''# 💾 Backup & Recovery

## Varför detta är kritiskt
> "Backups du aldrig testat är inte backups - de är falsk trygghet. En dag kommer du behöva dem, och då är det för sent att upptäcka att de inte fungerar."

## Vad du kommer lära dig
- ✅ pg_dump/pg_restore
- ✅ Physical vs Logical backups
- ✅ Point-in-Time Recovery (PITR)
- ✅ Cloud backup strategies

---

## Backup Types

```
Logical Backup:
- SQL-format
- Portabelt
- Långsammare restore
- Mindre flexibelt för PITR

Physical Backup:
- Binära filer
- Snabbare restore
- Kräver samma version
- Stödjer PITR
```

## pg_dump

```bash
# Full database dump
pg_dump -h localhost -U postgres mydb > backup.sql

# Custom format (komprimerad)
pg_dump -Fc mydb > backup.dump

# Endast schema
pg_dump --schema-only mydb > schema.sql

# Endast data
pg_dump --data-only mydb > data.sql

# Specifik tabell
pg_dump -t servers mydb > servers.sql

# Exkludera tabeller
pg_dump --exclude-table=logs mydb > backup.sql

# Parallell dump
pg_dump -Fd -j 4 mydb -f backup_dir/
```

## pg_restore

```bash
# Från custom format
pg_restore -d mydb backup.dump

# Skapa databas först
createdb mydb_restored
pg_restore -d mydb_restored backup.dump

# Parallell restore
pg_restore -j 4 -d mydb backup_dir/

# Specifik tabell
pg_restore -t servers -d mydb backup.dump

# List contents
pg_restore -l backup.dump
```

## pg_dumpall

```bash
# Alla databaser + roles
pg_dumpall > full_backup.sql

# Endast roles
pg_dumpall --roles-only > roles.sql

# Restore
psql -f full_backup.sql postgres
```

## Physical Backup

```bash
# pg_basebackup
pg_basebackup -h localhost -D /backups/base -Fp -Xs -P

# Med komprimering
pg_basebackup -h localhost -D /backups/base -Ft -z -Xs -P

# Restore:
# 1. Stoppa PostgreSQL
# 2. Kopiera backup till data directory
# 3. Skapa recovery.signal
# 4. Starta PostgreSQL
```

## Point-in-Time Recovery (PITR)

```bash
# 1. Aktivera WAL archiving (postgresql.conf)
archive_mode = on
archive_command = 'cp %p /archive/%f'

# 2. Ta basebackup
pg_basebackup -D /backups/base -Ft -z -Xs -P

# 3. Vid recovery, specificera target
# postgresql.conf / recovery.signal
restore_command = 'cp /archive/%f %p'
recovery_target_time = '2024-01-15 10:30:00'
```

## Backup Script

```bash
#!/bin/bash
# backup.sh

DB_NAME="production"
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
RETENTION_DAYS=30

# Create backup
pg_dump -Fc $DB_NAME > "$BACKUP_DIR/${DB_NAME}_${DATE}.dump"

# Verify
if [ $? -eq 0 ]; then
    echo "Backup successful: ${DB_NAME}_${DATE}.dump"

    # Remove old backups
    find $BACKUP_DIR -name "*.dump" -mtime +$RETENTION_DAYS -delete
else
    echo "Backup failed!" >&2
    exit 1
fi
```

## Verify Backup

```bash
# Lista innehåll
pg_restore -l backup.dump

# Test restore till annan databas
createdb test_restore
pg_restore -d test_restore backup.dump

# Verifiera data
psql -d test_restore -c "SELECT COUNT(*) FROM servers;"

# Cleanup
dropdb test_restore
```

## Cloud Backup

```bash
# Till S3
pg_dump -Fc mydb | aws s3 cp - s3://bucket/backup.dump

# Från S3
aws s3 cp s3://bucket/backup.dump - | pg_restore -d mydb

# Med gzip
pg_dump mydb | gzip | aws s3 cp - s3://bucket/backup.sql.gz
```

| Backup Type | Speed | Size | PITR |
|-------------|-------|------|------|
| pg_dump SQL | Slow | Large | No |
| pg_dump Custom | Medium | Small | No |
| pg_basebackup | Fast | Large | Yes |
| WAL Archiving | N/A | Medium | Yes |

**Nästa steg:** Node 20 - Monitoring & Best Practices
''',
}

NODE_20_MONITORING = {
    "node_id": 20,
    "title": "Monitoring & Best Practices",
    "slug": "monitoring-best-practices",
    "estimated_minutes": 55,
    "xp_reward": 160,
    "prerequisites": [14, 19],
    "content": '''# 📊 Monitoring & Best Practices

## Varför detta är kritiskt
> "En databas utan monitoring är som att köra bil med ögonbindel. Du märker problemen först när du kraschar - och då är det redan för sent."

## Vad du kommer lära dig
- ✅ Key PostgreSQL metrics
- ✅ pg_stat_statements analysis
- ✅ Connection pooling
- ✅ Production checklist

---

## Key Metrics

```sql
-- Aktiva connections
SELECT count(*) FROM pg_stat_activity;

-- Connections per database
SELECT datname, count(*)
FROM pg_stat_activity
GROUP BY datname;

-- Slow queries (behöver pg_stat_statements)
SELECT
    query,
    calls,
    mean_exec_time,
    total_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- Table sizes
SELECT
    relname AS table_name,
    pg_size_pretty(pg_total_relation_size(relid)) AS total_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;
```

## Locks & Blocking

```sql
-- Blocked queries
SELECT
    blocked.pid AS blocked_pid,
    blocked.query AS blocked_query,
    blocking.pid AS blocking_pid,
    blocking.query AS blocking_query
FROM pg_stat_activity blocked
JOIN pg_locks blocked_locks ON blocked.pid = blocked_locks.pid
JOIN pg_locks blocking_locks ON blocked_locks.locktype = blocking_locks.locktype
    AND blocked_locks.relation = blocking_locks.relation
JOIN pg_stat_activity blocking ON blocking_locks.pid = blocking.pid
WHERE NOT blocked_locks.granted
  AND blocking_locks.granted;

-- Kill blocking query
SELECT pg_terminate_backend(12345);
```

## Performance Views

```sql
-- Index usage
SELECT
    schemaname,
    relname AS table,
    indexrelname AS index,
    idx_scan AS scans,
    idx_tup_read AS tuples_read
FROM pg_stat_user_indexes
ORDER BY idx_scan DESC;

-- Unused indexes
SELECT
    schemaname || '.' || relname AS table,
    indexrelname AS index,
    pg_size_pretty(pg_relation_size(i.indexrelid)) AS size
FROM pg_stat_user_indexes ui
JOIN pg_index i ON ui.indexrelid = i.indexrelid
WHERE NOT indisunique
  AND idx_scan = 0
ORDER BY pg_relation_size(i.indexrelid) DESC;

-- Table bloat
SELECT
    schemaname,
    relname,
    n_dead_tup,
    n_live_tup,
    ROUND(100.0 * n_dead_tup / NULLIF(n_live_tup + n_dead_tup, 0), 2) AS dead_pct
FROM pg_stat_user_tables
WHERE n_dead_tup > 1000
ORDER BY n_dead_tup DESC;
```

## Connection Pooling

```yaml
# PgBouncer config
[databases]
mydb = host=localhost dbname=mydb

[pgbouncer]
listen_port = 6432
listen_addr = *
auth_type = md5
auth_file = /etc/pgbouncer/userlist.txt
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 20
```

## Query Guidelines

```sql
-- ✅ Use specific columns
SELECT id, hostname FROM servers;

-- ❌ Avoid SELECT *
SELECT * FROM servers;

-- ✅ Limit results
SELECT * FROM logs ORDER BY timestamp DESC LIMIT 100;

-- ✅ Use prepared statements
PREPARE get_server(int) AS
SELECT * FROM servers WHERE id = $1;
EXECUTE get_server(1);

-- ✅ Batch inserts
INSERT INTO logs (message, timestamp)
VALUES
    ('msg1', NOW()),
    ('msg2', NOW()),
    ('msg3', NOW());
```

## Maintenance

```sql
-- Vacuum - reclaim space
VACUUM servers;

-- Vacuum analyze - reclaim + update stats
VACUUM ANALYZE servers;

-- Full vacuum - compact (locks table!)
VACUUM FULL servers;

-- Reindex
REINDEX TABLE servers;
REINDEX INDEX CONCURRENTLY idx_servers_status;

-- Update statistics
ANALYZE servers;
```

## Configuration

```ini
# postgresql.conf essentials

# Memory
shared_buffers = 256MB          # 25% of RAM
effective_cache_size = 768MB    # 75% of RAM
work_mem = 64MB                 # Per operation
maintenance_work_mem = 256MB    # For VACUUM, INDEX

# Connections
max_connections = 100

# WAL
wal_level = replica
max_wal_size = 1GB
min_wal_size = 80MB

# Logging
log_min_duration_statement = 1000  # Log slow queries (ms)
log_statement = 'ddl'               # Log DDL statements
```

## Monitoring Checklist

```yaml
Continuous:
  - [ ] Active connections
  - [ ] Query response time
  - [ ] Replication lag
  - [ ] Disk space

Daily:
  - [ ] Slow query log
  - [ ] Table bloat
  - [ ] Unused indexes

Weekly:
  - [ ] Backup verification
  - [ ] Index usage stats
  - [ ] Connection pool stats
```

| Metric | Warning | Critical |
|--------|---------|----------|
| Connections | 80% max | 95% max |
| Disk | 80% | 90% |
| Replication lag | 30s | 5min |
| Long queries | 30s | 5min |

---

🎉 **Grattis!** Du har slutfört SQL SkillsMap!

Du har lärt dig:
- SQL grundläggande syntax
- Avancerade queries och joins
- Performance optimization
- Production best practices
''',
}

SQL_BLOCK_5 = [
    NODE_17_DB_DESIGN,
    NODE_18_MIGRATIONS,
    NODE_19_BACKUP,
    NODE_20_MONITORING,
]
