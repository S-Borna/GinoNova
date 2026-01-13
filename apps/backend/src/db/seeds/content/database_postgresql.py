"""
PostgreSQL for DevOps - Database Administration & Automation
=============================================================

Master PostgreSQL administration for production environments - backup strategies,
replication, monitoring, and performance tuning. 65% of DevOps jobs require database skills.
"""

POSTGRESQL_FUNDAMENTALS = {
    "title": "PostgreSQL for DevOps - Production Database Management",
    "slug": "postgresql-devops",
    "description": "Master PostgreSQL for production: backup/restore, replication, monitoring, performance tuning, and automation. Essential for 65% of DevOps roles.",
    "difficulty": "intermediate",
    "estimated_minutes": 120,
    "xp_reward": 200,
    "order_index": 1,
    "content": r"""# PostgreSQL for DevOps - Production Database Management

## 🎯 TL;DR (30 seconds)

PostgreSQL is the most popular open-source relational database. As a DevOps engineer, you need to automate backups,
set up replication, monitor performance, and handle production incidents. 65% of DevOps jobs require database skills.

**Why this matters:** Databases are the heart of applications. Lose data = lose your job. Master PostgreSQL operations
to prevent disasters and optimize performance.

---

## 🚀 Why PostgreSQL for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 65% of DevOps Engineer roles require database skills
- 78% of SRE roles require database operations knowledge
- 55% of Platform Engineer roles mention PostgreSQL

**Salary Impact (Sweden):**
| Role | Without DB Skills | With PostgreSQL | Difference |
|------|------------------|----------------|------------|
| Junior DevOps | 38,000 SEK | 43,000 SEK | **+13%** |
| DevOps Engineer | 45,000 SEK | 52,000 SEK | **+16%** |
| Senior SRE | 60,000 SEK | 70,000 SEK | **+17%** |

**Companies using PostgreSQL:** Instagram, Spotify, Reddit, Apple, Netflix, Discord

---

## 📖 THEORY: PostgreSQL Architecture

### What Makes PostgreSQL Special

**ACID Compliance:**
- **A**tomicity: All or nothing transactions
- **C**onsistency: Data integrity rules enforced
- **I**solation: Concurrent transactions don't interfere
- **D**urability: Committed data survives crashes

**PostgreSQL vs MySQL:**
| Feature | PostgreSQL | MySQL |
|---------|-----------|-------|
| ACID | Full ✅ | Partial |
| JSON support | Native JSONB | Limited |
| Full-text search | Built-in | Add-on |
| Extensibility | Very high | Limited |
| Replication | Streaming, Logical | Master-slave |
| Open source | Truly free | Owned by Oracle |

**Why DevOps teams prefer PostgreSQL:**
✅ Better for complex queries
✅ Built-in replication
✅ JSON support for logs/metrics
✅ Active community
✅ No vendor lock-in

---

## 🛠️ HANDS-ON: PostgreSQL Installation & Setup

### Step 1: Install PostgreSQL

**Ubuntu/Debian:**
```bash
# Add official PostgreSQL repository
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Install
sudo apt update
sudo apt install postgresql-15 postgresql-contrib-15 -y

# Check status
sudo systemctl status postgresql

# Version check
psql --version
```

**Using Docker (recommended for development):**
```bash
# Run PostgreSQL container
docker run -d \
  --name postgres-dev \
  -e POSTGRES_PASSWORD=devops2024 \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=myapp \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15-alpine

# Connect
docker exec -it postgres-dev psql -U admin -d myapp
```

---

### Step 2: Basic PostgreSQL Operations

**Connect to database:**
```bash
# As postgres user
sudo -u postgres psql

# With connection string
psql "postgresql://admin:devops2024@localhost:5432/myapp"
```

**Create database and user:**
```sql
-- Create database
CREATE DATABASE production_db;

-- Create user with password
CREATE USER app_user WITH ENCRYPTED PASSWORD 'secure_password_here';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE production_db TO app_user;

-- Connect to new database
\c production_db

-- Grant schema privileges
GRANT ALL ON SCHEMA public TO app_user;
GRANT ALL ON ALL TABLES IN SCHEMA public TO app_user;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO app_user;
```

**Common psql commands:**
```sql
\l                  -- List all databases
\c database_name    -- Connect to database
\dt                 -- List tables
\d table_name       -- Describe table
\du                 -- List users
\q                  -- Quit
```

---

## 🎓 PRODUCTION SKILL: Automated Backups

### Strategy 1: pg_dump for Logical Backups

**Backup script (`backup-postgres.sh`):**
```bash
#!/bin/bash
# PostgreSQL automated backup script

# Configuration
DB_NAME="production_db"
DB_USER="admin"
DB_HOST="localhost"
BACKUP_DIR="/var/backups/postgres"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_${DATE}.sql.gz"
RETENTION_DAYS=7

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup database (compressed)
echo "Starting backup of $DB_NAME..."
pg_dump -U $DB_USER -h $DB_HOST $DB_NAME | gzip > $BACKUP_FILE

# Check if backup succeeded
if [ $? -eq 0 ]; then
    echo "✅ Backup successful: $BACKUP_FILE"
    SIZE=$(du -h $BACKUP_FILE | cut -f1)
    echo "Backup size: $SIZE"
else
    echo "❌ Backup failed!"
    exit 1
fi

# Delete old backups (older than 7 days)
find $BACKUP_DIR -name "${DB_NAME}_*.sql.gz" -mtime +$RETENTION_DAYS -delete
echo "Deleted backups older than $RETENTION_DAYS days"

# Upload to S3 (optional)
if command -v aws &> /dev/null; then
    aws s3 cp $BACKUP_FILE s3://my-db-backups/postgres/
    echo "✅ Uploaded to S3"
fi

echo "Backup complete!"
```

**Make executable and schedule:**
```bash
chmod +x backup-postgres.sh

# Add to crontab (daily at 2 AM)
echo "0 2 * * * /usr/local/bin/backup-postgres.sh >> /var/log/postgres-backup.log 2>&1" | crontab -
```

---

### Strategy 2: pg_basebackup for Physical Backups

**Physical backup (faster for large databases):**
```bash
#!/bin/bash
# Physical backup with pg_basebackup

BACKUP_DIR="/var/backups/postgres/physical"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_PATH="$BACKUP_DIR/backup_$DATE"

mkdir -p $BACKUP_PATH

# Create physical backup
pg_basebackup -U postgres -D $BACKUP_PATH -Ft -z -P

echo "✅ Physical backup complete: $BACKUP_PATH"
```

**Restore from pg_dump:**
```bash
# Decompress and restore
gunzip -c backup_20260113_020000.sql.gz | psql -U admin -d production_db

# Or in one command
psql -U admin -d production_db < backup.sql
```

---

## 🔄 PRODUCTION SKILL: Replication Setup

### Master-Standby Streaming Replication

**Scenario:** High availability setup with automatic failover

**Master server configuration (`/etc/postgresql/15/main/postgresql.conf`):**
```conf
# Replication settings
wal_level = replica
max_wal_senders = 3
wal_keep_size = 1GB
synchronous_commit = on

# Archive logs
archive_mode = on
archive_command = 'cp %p /var/lib/postgresql/15/archive/%f'
```

**Create replication user on master:**
```sql
CREATE USER replicator WITH REPLICATION ENCRYPTED PASSWORD 'repl_password_123';
```

**Configure pg_hba.conf (allow standby to connect):**
```conf
# /etc/postgresql/15/main/pg_hba.conf
# TYPE  DATABASE        USER            ADDRESS                 METHOD
host    replication     replicator      192.168.1.0/24          md5
```

**Restart master:**
```bash
sudo systemctl restart postgresql
```

---

**Standby server setup:**
```bash
# Stop PostgreSQL on standby
sudo systemctl stop postgresql

# Remove old data
sudo rm -rf /var/lib/postgresql/15/main/*

# Clone from master
sudo -u postgres pg_basebackup -h 192.168.1.10 -U replicator -D /var/lib/postgresql/15/main -P -Xs -R

# Start standby
sudo systemctl start postgresql

# Verify replication status (on master)
sudo -u postgres psql -c "SELECT * FROM pg_stat_replication;"
```

**Output should show:**
```
 pid | usename    | state     | sent_lsn   | write_lsn  | flush_lsn
-----+------------+-----------+------------+------------+-----------
 1234| replicator | streaming | 0/3000000  | 0/3000000  | 0/3000000
```

---

## 📊 PRODUCTION SKILL: Monitoring & Performance

### Essential Queries for Monitoring

**1. Check database size:**
```sql
SELECT
    pg_database.datname as database_name,
    pg_size_pretty(pg_database_size(pg_database.datname)) as size
FROM pg_database
ORDER BY pg_database_size(pg_database.datname) DESC;
```

**2. Table sizes:**
```sql
SELECT
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size,
    pg_size_pretty(pg_indexes_size(schemaname||'.'||tablename)) as index_size
FROM pg_tables
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC
LIMIT 10;
```

**3. Active connections:**
```sql
SELECT
    count(*),
    state,
    usename
FROM pg_stat_activity
WHERE state IS NOT NULL
GROUP BY state, usename
ORDER BY count DESC;
```

**4. Long-running queries:**
```sql
SELECT
    pid,
    now() - query_start as duration,
    usename,
    state,
    query
FROM pg_stat_activity
WHERE state = 'active'
  AND now() - query_start > interval '1 minute'
ORDER BY duration DESC;
```

**5. Kill long-running query:**
```sql
-- Graceful termination
SELECT pg_cancel_backend(12345);

-- Force kill
SELECT pg_terminate_backend(12345);
```

**6. Cache hit ratio (should be >99%):**
```sql
SELECT
    sum(heap_blks_read) as heap_read,
    sum(heap_blks_hit) as heap_hit,
    sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) * 100 as cache_hit_ratio
FROM pg_statio_user_tables;
```

**7. Index usage:**
```sql
SELECT
    schemaname,
    tablename,
    indexname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes
ORDER BY idx_scan ASC;
```

**8. Unused indexes (candidates for removal):**
```sql
SELECT
    schemaname,
    tablename,
    indexname,
    idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
  AND indexname NOT LIKE '%_pkey';
```

---

### Performance Tuning Configuration

**Essential `postgresql.conf` settings for production:**
```conf
# Memory Settings (adjust based on available RAM)
shared_buffers = 4GB              # 25% of total RAM
effective_cache_size = 12GB       # 75% of total RAM
work_mem = 16MB                   # Per operation
maintenance_work_mem = 512MB      # For VACUUM, CREATE INDEX

# Connection Settings
max_connections = 100
superuser_reserved_connections = 3

# Checkpoint Settings (prevent I/O spikes)
checkpoint_timeout = 15min
checkpoint_completion_target = 0.9
wal_buffers = 16MB

# Query Planner
random_page_cost = 1.1           # Lower for SSD
effective_io_concurrency = 200   # Higher for SSD

# Logging (essential for troubleshooting)
log_destination = 'stderr'
logging_collector = on
log_directory = '/var/log/postgresql'
log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'
log_min_duration_statement = 1000  # Log queries >1 second
log_line_prefix = '%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h '
log_checkpoints = on
log_connections = on
log_disconnections = on
log_lock_waits = on

# Autovacuum (prevents table bloat)
autovacuum = on
autovacuum_max_workers = 3
autovacuum_naptime = 30s
```

**Apply changes:**
```bash
sudo systemctl reload postgresql
```

---

## 🔧 PRODUCTION SKILL: Connection Pooling

### PgBouncer Setup

**Why connection pooling?**
- PostgreSQL connections are heavy (each = OS process)
- Apps often open too many connections
- PgBouncer multiplexes connections

**Install PgBouncer:**
```bash
sudo apt install pgbouncer -y
```

**Configure `/etc/pgbouncer/pgbouncer.ini`:**
```ini
[databases]
myapp = host=localhost port=5432 dbname=production_db

[pgbouncer]
listen_addr = 0.0.0.0
listen_port = 6432
auth_type = md5
auth_file = /etc/pgbouncer/userlist.txt
admin_users = admin
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 25
reserve_pool_size = 5
reserve_pool_timeout = 3
log_connections = 1
log_disconnections = 1
```

**Create userlist.txt:**
```bash
echo '"app_user" "md5hash_of_password"' > /etc/pgbouncer/userlist.txt
```

**Start PgBouncer:**
```bash
sudo systemctl enable pgbouncer
sudo systemctl start pgbouncer

# Check status
sudo systemctl status pgbouncer
```

**Connect through PgBouncer:**
```bash
psql -h localhost -p 6432 -U app_user myapp
```

**Monitor PgBouncer:**
```bash
# Connect to admin console
psql -h localhost -p 6432 -U admin pgbouncer

# Show stats
SHOW STATS;
SHOW POOLS;
SHOW DATABASES;
```

---

## 🎤 Interview Questions & Answers

### Question 1: Backup Strategy

**Interviewer:** "How would you design a backup strategy for a 500GB production PostgreSQL database?"

❌ **Weak Answer:**
> "Use pg_dump daily."

✅ **Strong Answer:**
> "For a 500GB database, I'd use a layered approach: 1) Daily pg_basebackup (physical backup) at 2 AM to minimize impact. 2) Hourly WAL archiving to S3 for point-in-time recovery. 3) Weekly pg_dump for logical backup (easier to restore individual tables). 4) Test restores monthly on a staging environment. 5) Keep 30 days locally, 1 year in S3 Glacier for compliance. With WAL archiving, we can restore to any point in time within 30 days, which meets our RTO of 4 hours and RPO of 1 hour."

**Why this impresses:** Shows understanding of different backup types, compliance, and disaster recovery metrics.

---

### Question 2: Performance Issue

**Interviewer:** "A query that normally takes 100ms is suddenly taking 30 seconds. How do you troubleshoot?"

❌ **Weak Answer:**
> "Check the logs?"

✅ **Strong Answer:**
> "First, check `pg_stat_activity` for long-running queries and locks. Run `EXPLAIN ANALYZE` on the slow query to see the execution plan - likely either a missing index or outdated statistics. Check if autovacuum ran recently with `pg_stat_user_tables`. If table bloat is high, run `VACUUM ANALYZE`. Check cache hit ratio - if it dropped, shared_buffers might be too small. Also check disk I/O with `iostat` - maybe storage is saturated. Finally, review recent application changes that might have increased query volume."

**Why this impresses:** Systematic approach covering indexes, statistics, vacuuming, and resource constraints.

---

### Question 3: Replication Lag

**Interviewer:** "Your standby server is 5GB behind the master. What's happening and how do you fix it?"

❌ **Weak Answer:**
> "Network is slow?"

✅ **Strong Answer:**
> "Check `pg_stat_replication` on master for `write_lag` and `flush_lag`. Common causes: 1) Network bandwidth issue - check with `iftop` between servers. 2) Standby disk I/O bottleneck - check with `iostat`. 3) Long-running query on standby blocking WAL replay - check with hot_standby_feedback setting. 4) Insufficient `wal_keep_size` on master causing WAL recycling. Short term: increase `wal_keep_size`. Long term: tune standby performance, use replication slots to prevent WAL deletion, consider synchronous replication if lag is unacceptable."

**Why this impresses:** Demonstrates monitoring skills and understanding of replication mechanics.

---

## 🐛 Common Mistakes (Avoid These!)

### ❌ Mistake 1: Not Running VACUUM

**Problem:**
```sql
-- Table becomes bloated, queries slow down
SELECT pg_size_pretty(pg_total_relation_size('users'));
-- Shows 10GB for a table that should be 2GB
```

**Solution:**
```sql
-- Manual vacuum
VACUUM ANALYZE users;

-- Full vacuum (locks table, use with caution)
VACUUM FULL users;

-- Check last vacuum
SELECT
    relname,
    last_vacuum,
    last_autovacuum,
    n_dead_tup
FROM pg_stat_user_tables
WHERE relname = 'users';
```

---

### ❌ Mistake 2: Missing Indexes

**Problem:**
```sql
-- Slow query (sequential scan)
EXPLAIN SELECT * FROM orders WHERE customer_id = 123;
-- Seq Scan on orders (cost=0.00..12345.00 rows=1)
```

**Solution:**
```sql
-- Create index
CREATE INDEX idx_orders_customer_id ON orders(customer_id);

-- Verify index usage
EXPLAIN SELECT * FROM orders WHERE customer_id = 123;
-- Index Scan using idx_orders_customer_id (cost=0.42..8.44 rows=1)
```

---

### ❌ Mistake 3: Not Monitoring Connections

**Problem:** Application crashes with "too many connections" error

**Solution:**
```sql
-- Check connection limit
SHOW max_connections;

-- Current connections
SELECT count(*) FROM pg_stat_activity;

-- Increase limit (postgresql.conf)
max_connections = 200

-- Better: Use PgBouncer for connection pooling
```

---

## 📚 Flashcards

**Q: What is ACID?**
A: Atomicity, Consistency, Isolation, Durability - guarantees for database transactions.

**Q: pg_dump vs pg_basebackup?**
A: pg_dump = logical backup (SQL dump, slower, flexible). pg_basebackup = physical backup (faster, full cluster).

**Q: What is WAL?**
A: Write-Ahead Log - changes are written to log before data files, enables crash recovery and replication.

**Q: What is VACUUM?**
A: Reclaims storage from dead tuples (old row versions), prevents table bloat.

**Q: What is a replication slot?**
A: Ensures master keeps WAL files until standby consumes them, prevents replication break.

**Q: What is PgBouncer?**
A: Connection pooler that multiplexes client connections to reduce PostgreSQL overhead.

**Q: What is the cache hit ratio?**
A: Percentage of reads served from memory vs disk. Should be >99%.

**Q: What is autovacuum?**
A: Background process that automatically runs VACUUM to prevent bloat.

**Q: What is hot_standby?**
A: Allows read-only queries on standby servers during replication.

**Q: What is synchronous replication?**
A: Master waits for standby to confirm write before committing. Slower but no data loss.

---

## 🎓 Quiz

### Question 1

**Which backup method is fastest for a 1TB database?**

A) pg_dump
B) pg_dumpall
C) pg_basebackup ✅
D) Copy data directory

**Answer:** C ✅

**Explanation:** pg_basebackup is a physical backup that copies data files directly, much faster than logical dumps for large databases.

---

### Question 2

**What does VACUUM ANALYZE do?**

A) Deletes old backups
B) Reclaims space and updates statistics ✅
C) Backs up the database
D) Restarts the server

**Answer:** B ✅

**Explanation:** VACUUM reclaims dead tuple space, ANALYZE updates query planner statistics.

---

### Question 3

**Cache hit ratio of 85% means what?**

A) Database is performing well
B) Need more shared_buffers ✅
C) Disk is failing
D) Too many connections

**Answer:** B ✅

**Explanation:** Cache hit ratio should be >99%. 85% means 15% of reads hit disk, indicating insufficient memory allocation.

---

## 🎯 Portfolio Project: Production PostgreSQL Setup

**Build this for your GitHub:**

**Project:** Production-ready PostgreSQL cluster with monitoring

**Components:**
1. Master-standby replication (Docker Compose)
2. Automated backup script with S3 upload
3. PgBouncer connection pooling
4. Prometheus exporter for metrics
5. Grafana dashboards
6. Documentation and runbooks

**Why this impresses:**
- ✅ Demonstrates production skills
- ✅ High availability setup
- ✅ Automation and monitoring
- ✅ Complete documentation
- ✅ Shows DevOps thinking

**GitHub structure:**
```
postgres-ha-cluster/
├── docker-compose.yml
├── postgres/
│   ├── master/
│   │   └── postgresql.conf
│   └── standby/
│       └── postgresql.conf
├── pgbouncer/
│   └── pgbouncer.ini
├── scripts/
│   ├── backup.sh
│   ├── restore.sh
│   └── health-check.sh
├── monitoring/
│   ├── prometheus.yml
│   └── grafana-dashboard.json
└── README.md
```

---

## 🌟 Why This Module Prepares You for Jobs

✅ **Backup/restore mastery** - Prevent data loss disasters
✅ **Replication setup** - Build high-availability systems
✅ **Performance tuning** - Optimize slow databases
✅ **Production monitoring** - Detect issues proactively
✅ **Interview confidence** - Answer database questions expertly

**Time to complete:** 2 hours
**Job market impact:** Opens 65% of DevOps roles
**Salary boost:** +13-17% average
**Real-world value:** Skills you'll use daily

---

**Module completed!** 🎉

**Next recommended:** Redis Caching - Speed up your applications with in-memory data
"""
}

# Export as MODULE dict
MODULE = {
    "id": "database-postgresql",
    "slug": "database-postgresql",
    "title": "PostgreSQL for DevOps",
    "description": "Master PostgreSQL operations: backup strategies, replication, monitoring, performance tuning, and production troubleshooting. Essential for 65% of DevOps roles.",
    "icon": "🐘",
    "category": "databases",
    "difficulty": "intermediate",
    "estimated_hours": 10,
    "tasks": [POSTGRESQL_FUNDAMENTALS],
}
