"""
MongoDB for DevOps - NoSQL Database Operations
===============================================

Master MongoDB for modern applications - document database operations, replication,
sharding, backup strategies, and monitoring. Used by 50% of startups and scale-ups.
"""

MONGODB_FUNDAMENTALS = {
    "title": "MongoDB for DevOps - NoSQL Operations & Scaling",
    "slug": "mongodb-devops",
    "description": "Master MongoDB operations: CRUD operations, indexing, replication, sharding, backup strategies, and production monitoring. Essential NoSQL skills.",
    "difficulty": "intermediate",
    "estimated_minutes": 115,
    "xp_reward": 190,
    "order_index": 1,
    "content": r"""# MongoDB for DevOps - NoSQL Operations & Scaling

## 🎯 TL;DR (30 seconds)

MongoDB is a document database that stores JSON-like documents. Unlike SQL, it's schema-flexible and scales
horizontally. Perfect for rapid development, unstructured data, and high-write applications. 50% of startups use MongoDB.

**Why this matters:** Modern apps need flexible schemas and horizontal scaling. MongoDB enables rapid iteration
and handles massive data volumes that would break traditional SQL databases.

---

## 🚀 Why MongoDB for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 50% of startup DevOps roles require NoSQL experience
- 45% of Backend Engineer roles mention MongoDB
- 55% of Full-Stack roles work with MongoDB

**Salary Impact (Sweden):**
| Role | Without NoSQL | With MongoDB | Difference |
|------|--------------|--------------|------------|
| Junior DevOps | 38,000 SEK | 41,000 SEK | **+8%** |
| Backend Engineer | 43,000 SEK | 48,000 SEK | **+12%** |
| Senior DevOps | 55,000 SEK | 62,000 SEK | **+13%** |

**Companies using MongoDB:** Adobe, eBay, EA, Cisco, Forbes, Bosch, SEGA

**Use cases:**
- Content management systems (CMS)
- Real-time analytics
- IoT sensor data
- User profiles and personalization
- Catalogs and product listings

---

## 📖 THEORY: SQL vs NoSQL (MongoDB)

### When to Use MongoDB vs PostgreSQL

**MongoDB wins for:**
✅ Flexible/evolving schemas
✅ Rapid prototyping
✅ Hierarchical data (nested documents)
✅ High-write workloads
✅ Horizontal scaling (sharding)
✅ Unstructured or semi-structured data

**PostgreSQL wins for:**
✅ Complex transactions (banking, e-commerce)
✅ Complex queries and joins
✅ Strict data integrity
✅ Mature ecosystem
✅ Better for relational data

**Example: User profiles**

**SQL (PostgreSQL):**
```sql
-- 3 tables, complex joins
CREATE TABLE users (id INT, name VARCHAR, email VARCHAR);
CREATE TABLE addresses (user_id INT, street VARCHAR, city VARCHAR);
CREATE TABLE preferences (user_id INT, theme VARCHAR, language VARCHAR);

SELECT * FROM users
JOIN addresses ON users.id = addresses.user_id
JOIN preferences ON users.id = preferences.user_id
WHERE users.id = 123;
```

**NoSQL (MongoDB):**
```javascript
// Single document, no joins
{
  "_id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "address": {
    "street": "123 Main St",
    "city": "Stockholm"
  },
  "preferences": {
    "theme": "dark",
    "language": "sv"
  }
}

db.users.findOne({_id: 123})
```

---

## 🛠️ HANDS-ON: MongoDB Installation & Setup

### Step 1: Install MongoDB

**Ubuntu/Debian:**
```bash
# Import public key
wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | sudo apt-key add -

# Add MongoDB repository
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

# Install
sudo apt update
sudo apt install -y mongodb-org

# Start service
sudo systemctl start mongod
sudo systemctl enable mongod

# Check status
sudo systemctl status mongod

# Connect
mongosh
```

**Using Docker (recommended):**
```bash
# Run MongoDB container
docker run -d \
  --name mongodb-dev \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=devops2024 \
  -p 27017:27017 \
  -v mongodb_data:/data/db \
  mongo:7.0

# Connect with mongosh
docker exec -it mongodb-dev mongosh -u admin -p devops2024 --authenticationDatabase admin
```

---

### Step 2: Basic MongoDB Operations

**Connect and show databases:**
```javascript
// Connect
mongosh "mongodb://admin:devops2024@localhost:27017"

// Show databases
show dbs

// Switch to database (creates if doesn't exist)
use myapp

// Show collections (tables)
show collections
```

---

### Step 3: CRUD Operations

**Create (Insert):**
```javascript
// Insert one document
db.users.insertOne({
  name: "John Doe",
  email: "john@example.com",
  age: 30,
  role: "developer",
  skills: ["JavaScript", "Python", "Docker"],
  address: {
    city: "Stockholm",
    country: "Sweden"
  },
  created_at: new Date()
})

// Insert multiple documents
db.users.insertMany([
  {
    name: "Alice Smith",
    email: "alice@example.com",
    age: 28,
    role: "devops",
    skills: ["Kubernetes", "Terraform", "AWS"]
  },
  {
    name: "Bob Johnson",
    email: "bob@example.com",
    age: 35,
    role: "sre",
    skills: ["Prometheus", "Grafana", "Python"]
  }
])
```

**Read (Query):**
```javascript
// Find all
db.users.find()

// Find with filter
db.users.find({ role: "devops" })

// Find one
db.users.findOne({ email: "john@example.com" })

// Find with multiple conditions
db.users.find({
  role: "developer",
  age: { $gte: 25 }
})

// Projection (select specific fields)
db.users.find(
  { role: "devops" },
  { name: 1, email: 1, _id: 0 }  // 1 = include, 0 = exclude
)

// Array queries
db.users.find({ skills: "Docker" })  // Has Docker skill

// Nested document queries
db.users.find({ "address.city": "Stockholm" })

// Regex search
db.users.find({ name: /John/i })  // Case-insensitive

// Count
db.users.countDocuments({ role: "devops" })

// Sort and limit
db.users.find().sort({ age: -1 }).limit(5)  // Top 5 oldest
```

**Update:**
```javascript
// Update one document
db.users.updateOne(
  { email: "john@example.com" },
  { $set: { age: 31, updated_at: new Date() } }
)

// Update multiple documents
db.users.updateMany(
  { role: "developer" },
  { $set: { department: "engineering" } }
)

// Increment value
db.users.updateOne(
  { email: "john@example.com" },
  { $inc: { login_count: 1 } }
)

// Add to array
db.users.updateOne(
  { email: "john@example.com" },
  { $push: { skills: "Kubernetes" } }
)

// Remove from array
db.users.updateOne(
  { email: "john@example.com" },
  { $pull: { skills: "Docker" } }
)

// Upsert (update or insert)
db.users.updateOne(
  { email: "new@example.com" },
  { $set: { name: "New User", role: "viewer" } },
  { upsert: true }
)
```

**Delete:**
```javascript
// Delete one
db.users.deleteOne({ email: "john@example.com" })

// Delete many
db.users.deleteMany({ role: "viewer" })

// Delete all documents (keep collection)
db.users.deleteMany({})

// Drop entire collection
db.users.drop()
```

---

## 🎓 Indexing for Performance

### Why Indexes Matter

**Without index:**
```javascript
// Scans ALL documents (slow!)
db.users.find({ email: "john@example.com" }).explain("executionStats")
// executionTimeMillis: 450ms for 1M documents
```

**With index:**
```javascript
// Create index
db.users.createIndex({ email: 1 })

// Now fast!
db.users.find({ email: "john@example.com" }).explain("executionStats")
// executionTimeMillis: 2ms
```

---

### Index Types & Usage

**1. Single field index:**
```javascript
// Ascending
db.users.createIndex({ email: 1 })

// Descending
db.users.createIndex({ created_at: -1 })
```

**2. Compound index (multiple fields):**
```javascript
// Index on role + age
db.users.createIndex({ role: 1, age: -1 })

// Efficient for these queries:
db.users.find({ role: "developer" })
db.users.find({ role: "developer", age: { $gte: 25 } })
db.users.find({ role: "developer" }).sort({ age: -1 })
```

**3. Unique index:**
```javascript
// Ensure email is unique
db.users.createIndex({ email: 1 }, { unique: true })

// Attempt to insert duplicate will fail
```

**4. Text index (full-text search):**
```javascript
// Create text index
db.articles.createIndex({ title: "text", content: "text" })

// Search
db.articles.find({ $text: { $search: "kubernetes docker" } })
```

**5. TTL index (auto-delete old documents):**
```javascript
// Delete documents 30 days after created_at
db.sessions.createIndex(
  { created_at: 1 },
  { expireAfterSeconds: 2592000 }  // 30 days
)
```

---

### Index Management

```javascript
// List all indexes
db.users.getIndexes()

// Drop index
db.users.dropIndex("email_1")

// Drop all indexes (except _id)
db.users.dropIndexes()

// Analyze index usage
db.users.aggregate([
  { $indexStats: {} }
])
```

---

## 🔄 Replication (High Availability)

### Replica Set Setup

**Why replica sets?**
- Automatic failover if primary fails
- Read scaling (route reads to secondaries)
- Zero-downtime maintenance

**Docker Compose setup (`docker-compose.yml`):**
```yaml
version: '3.8'

services:
  mongo1:
    image: mongo:7.0
    command: mongod --replSet rs0 --bind_ip_all
    ports:
      - "27017:27017"
    volumes:
      - mongo1_data:/data/db

  mongo2:
    image: mongo:7.0
    command: mongod --replSet rs0 --bind_ip_all
    ports:
      - "27018:27017"
    volumes:
      - mongo2_data:/data/db

  mongo3:
    image: mongo:7.0
    command: mongod --replSet rs0 --bind_ip_all
    ports:
      - "27019:27017"
    volumes:
      - mongo3_data:/data/db

volumes:
  mongo1_data:
  mongo2_data:
  mongo3_data:
```

**Initialize replica set:**
```bash
# Start containers
docker-compose up -d

# Connect to first node
docker exec -it <container_id> mongosh

# Initialize replica set
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017" },
    { _id: 1, host: "mongo2:27017" },
    { _id: 2, host: "mongo3:27017" }
  ]
})

# Check status
rs.status()

# Check which is primary
rs.isMaster()
```

**Connect to replica set from application:**
```python
from pymongo import MongoClient

client = MongoClient(
    "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0"
)

# Automatically routes to primary for writes
db = client.myapp
db.users.insert_one({"name": "John"})

# Route reads to secondary (eventual consistency)
from pymongo import ReadPreference
db.users.find().with_options(read_preference=ReadPreference.SECONDARY)
```

---

## 🎓 Backup & Restore Strategies

### Strategy 1: mongodump (Logical Backup)

**Backup all databases:**
```bash
# Backup to directory
mongodump --uri="mongodb://admin:password@localhost:27017" --out=/backup/mongo-$(date +%Y%m%d)

# Backup single database
mongodump --uri="mongodb://admin:password@localhost:27017" --db=myapp --out=/backup/myapp

# Compressed backup
mongodump --uri="mongodb://admin:password@localhost:27017" --archive=/backup/mongo.gz --gzip

# Backup and upload to S3
mongodump --uri="mongodb://admin:password@localhost:27017" --archive | gzip | aws s3 cp - s3://backups/mongo-$(date +%Y%m%d).gz
```

**Restore:**
```bash
# Restore all databases
mongorestore --uri="mongodb://admin:password@localhost:27017" /backup/mongo-20260113

# Restore single database
mongorestore --uri="mongodb://admin:password@localhost:27017" --db=myapp /backup/myapp

# Restore from compressed
mongorestore --uri="mongodb://admin:password@localhost:27017" --archive=/backup/mongo.gz --gzip
```

---

### Strategy 2: Automated Backup Script

**`backup-mongodb.sh`:**
```bash
#!/bin/bash

MONGO_URI="mongodb://admin:password@localhost:27017"
BACKUP_DIR="/var/backups/mongodb"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_PATH="$BACKUP_DIR/backup_$DATE"
RETENTION_DAYS=7

mkdir -p $BACKUP_DIR

echo "Starting MongoDB backup..."

# Backup with compression
mongodump --uri="$MONGO_URI" --archive="$BACKUP_PATH.gz" --gzip

if [ $? -eq 0 ]; then
    SIZE=$(du -h "$BACKUP_PATH.gz" | cut -f1)
    echo "✅ Backup successful: $BACKUP_PATH.gz ($SIZE)"

    # Upload to S3
    aws s3 cp "$BACKUP_PATH.gz" s3://my-backups/mongodb/
    echo "✅ Uploaded to S3"

    # Delete old backups
    find $BACKUP_DIR -name "backup_*.gz" -mtime +$RETENTION_DAYS -delete
    echo "Cleaned old backups (>$RETENTION_DAYS days)"
else
    echo "❌ Backup failed!"
    exit 1
fi
```

**Schedule with cron:**
```bash
chmod +x backup-mongodb.sh

# Daily at 3 AM
echo "0 3 * * * /usr/local/bin/backup-mongodb.sh >> /var/log/mongodb-backup.log 2>&1" | crontab -
```

---

## 📊 Monitoring & Performance

### Essential Monitoring Queries

**1. Database stats:**
```javascript
// Current database stats
db.stats()

// Collection stats
db.users.stats()

// Index sizes
db.users.stats().indexSizes
```

**2. Active operations:**
```javascript
// Show current operations
db.currentOp()

// Filter long-running queries (>5 seconds)
db.currentOp({
  "active": true,
  "secs_running": { "$gt": 5 }
})

// Kill slow query
db.killOp(123456)  // operation ID
```

**3. Query profiler:**
```javascript
// Enable profiler (level 2 = all operations)
db.setProfilingLevel(2)

// Level 1 = slow queries only (>100ms)
db.setProfilingLevel(1, { slowms: 100 })

// View slow queries
db.system.profile.find().sort({ ts: -1 }).limit(10)

// Disable profiler
db.setProfilingLevel(0)
```

**4. Server status:**
```javascript
db.serverStatus()

// Connections
db.serverStatus().connections

// Operations per second
db.serverStatus().opcounters

// Memory usage
db.serverStatus().mem
```

---

### Production Configuration

**`/etc/mongod.conf`:**
```yaml
# Network
net:
  port: 27017
  bindIp: 0.0.0.0  # Production: specific IP only

# Security
security:
  authorization: enabled

# Storage
storage:
  dbPath: /var/lib/mongodb
  journal:
    enabled: true
  wiredTiger:
    engineConfig:
      cacheSizeGB: 8  # 50% of RAM

# Logging
systemLog:
  destination: file
  path: /var/log/mongodb/mongod.log
  logAppend: true
  logRotate: reopen

# Replication
replication:
  replSetName: rs0

# Sharding (if needed)
# sharding:
#   clusterRole: shardsvr
```

---

## 🎤 Interview Questions & Answers

### Question 1: Schema Design

**Interviewer:** "How would you model a blog with posts and comments in MongoDB?"

❌ **Weak Answer:**
> "Separate collections for posts and comments."

✅ **Strong Answer:**
> "Depends on access patterns. If comments are always shown with posts and rarely accessed independently, embed them: `{post: {...}, comments: [{...}]}`. Advantages: single query, atomic updates, better performance. But if a post can have thousands of comments, I'd use a separate collection to avoid document size limits (16MB). Hybrid approach: embed first 10 comments, store rest separately. MongoDB rule of thumb: embed if one-to-few relationship, reference if one-to-many."

**Why this impresses:** Shows understanding of embedding vs referencing and trade-offs.

---

### Question 2: Scaling

**Interviewer:** "Your MongoDB cluster is struggling with high write load. How do you scale?"

❌ **Weak Answer:**
> "Add more RAM."

✅ **Strong Answer:**
> "First, verify it's write bottleneck with `db.serverStatus().opcounters`. Solutions: 1) Vertical scaling: increase CPU/RAM, use faster SSDs. 2) Horizontal scaling: implement sharding to distribute writes across multiple servers. Choose shard key carefully - ideally high cardinality and even distribution (e.g., user_id hash). 3) Optimize indexes - unnecessary indexes slow writes. 4) Batch writes when possible. 5) Use replica set and route reads to secondaries to reduce primary load. Sharding is the ultimate MongoDB scaling solution."

**Why this impresses:** Demonstrates systematic approach and MongoDB-specific knowledge.

---

### Question 3: Troubleshooting

**Interviewer:** "A query that was fast yesterday is slow today. How do you debug?"

❌ **Weak Answer:**
> "Restart MongoDB."

✅ **Strong Answer:**
> "First, run `explain('executionStats')` to see execution plan. Check: 1) Is index being used? If showing COLLSCAN, add index. 2) Check index efficiency - high `docsExamined` vs `nReturned` means poor selectivity. 3) Collection grew significantly? Check `db.collection.stats()`. 4) Check for lock contention with `db.currentOp()`. 5) Enable profiler to see slow queries. 6) Check server resources - disk I/O, RAM, CPU. 7) Indexes might be outdated - MongoDB chooses execution plan based on statistics."

**Why this impresses:** Shows systematic debugging methodology and MongoDB expertise.

---

## 📚 Flashcards

**Q: What is a document in MongoDB?**
A: JSON-like object (BSON) that is the basic unit of data, similar to a row in SQL.

**Q: What is a collection?**
A: Group of documents, similar to a table in SQL.

**Q: What is BSON?**
A: Binary JSON - MongoDB's internal format for storing documents.

**Q: What is _id?**
A: Unique identifier for each document, automatically created if not provided.

**Q: What is a replica set?**
A: Group of MongoDB servers maintaining same data for high availability.

**Q: What is sharding?**
A: Distributing data across multiple machines for horizontal scaling.

**Q: What is the document size limit?**
A: 16 MB per document.

**Q: Embed vs Reference?**
A: Embed for one-to-few (performance), reference for one-to-many (flexibility).

**Q: What is the aggregation pipeline?**
A: Framework for data processing - filter, group, transform documents.

**Q: What is mongodump?**
A: Tool for logical backups of MongoDB databases.

---

## 🎓 Quiz

### Question 1

**Which query finds users aged 25 or older?**

A) `db.users.find({ age: >= 25 })`
B) `db.users.find({ age: { $gte: 25 } })` ✅
C) `db.users.find({ age >= 25 })`
D) `db.users.find({ age: ">= 25" })`

**Answer:** B ✅

**Explanation:** MongoDB uses $gte operator for greater-than-or-equal queries.

---

### Question 2

**What does the following do?**
```javascript
db.users.createIndex({ email: 1 }, { unique: true })
```

A) Creates a non-unique index
B) Creates a unique constraint on email ✅
C) Deletes duplicate emails
D) Sorts by email

**Answer:** B ✅

**Explanation:** unique: true creates a unique index, preventing duplicate emails.

---

### Question 3

**In a replica set with 3 nodes, how many nodes must acknowledge a write by default?**

A) 1 (primary only) ✅
B) 2 (majority)
C) 3 (all)
D) 0 (fire and forget)

**Answer:** A ✅

**Explanation:** Default write concern is w:1 (primary only). Use w:"majority" for stronger durability.

---

## 🌟 Why This Module Prepares You for Jobs

✅ **NoSQL expertise** - Essential for modern architectures
✅ **CRUD mastery** - Work with document databases confidently
✅ **Scaling knowledge** - Implement sharding and replication
✅ **Performance tuning** - Optimize with indexes and profiling
✅ **Production operations** - Backup, monitoring, troubleshooting

**Time to complete:** 2 hours
**Job market impact:** Required in 50% of startups
**Salary boost:** +8-13% average
**Career flexibility:** Opens both DevOps and Backend roles

---

**Module completed!** 🎉

**Next recommended:** Apache Kafka - Master event streaming for distributed systems
"""
}

# Export as MODULE dict
MODULE = {
    "id": "database-mongodb",
    "slug": "database-mongodb",
    "title": "MongoDB Operations & Scaling",
    "description": "Master MongoDB for production: document operations, indexing, replication, sharding, backup strategies, and performance monitoring. Essential NoSQL skills for modern applications.",
    "icon": "🍃",
    "category": "databases",
    "difficulty": "intermediate",
    "estimated_hours": 9,
    "tasks": [MONGODB_FUNDAMENTALS],
}
