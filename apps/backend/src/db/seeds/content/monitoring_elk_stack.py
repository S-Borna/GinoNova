"""
ELK Stack - Elasticsearch, Logstash, Kibana
============================================

Master the ELK Stack for log aggregation, search, and analysis. The industry standard
for centralized logging used by 55% of DevOps teams.

Coverage:
- Elasticsearch full-text search
- Logstash pipelines and parsing
- Kibana visualizations and dashboards
- Filebeat and log shipping
- Query DSL and aggregations
"""

ELK_FUNDAMENTALS = {
    "title": "ELK Stack - Complete Log Management",
    "slug": "elk-stack-fundamentals",
    "description": "Master Elasticsearch, Logstash, and Kibana for centralized logging. Learn log aggregation, search, parsing, and visualization.",
    "difficulty": "intermediate",
    "estimated_minutes": 120,
    "xp_reward": 200,
    "order_index": 1,
    "content": r"""# ELK Stack - Complete Log Management

## 🎯 TL;DR (30 seconds)

ELK Stack = Elasticsearch (search engine) + Logstash (log processor) + Kibana (visualization).
Aggregate logs from 100 servers into one place, search in milliseconds, create dashboards.

**Why this matters:** Without centralized logging, you SSH to 50 servers and grep log files for hours.
With ELK, you search all logs from one web UI in seconds. 55% of DevOps jobs use ELK.

---

## 🚀 Why ELK Stack for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 55% of DevOps Engineer roles use ELK Stack
- 68% of SRE roles use ELK or similar (Loki, Splunk)
- 45% of Platform Engineer roles manage logging infrastructure

**Salary Impact (Sweden):**
| Role | Without Logging | With ELK | Difference |
|------|----------------|----------|------------|
| Junior DevOps | 38,000 SEK | 43,000 SEK | **+13%** |
| DevOps Engineer | 45,000 SEK | 52,000 SEK | **+16%** |
| Senior SRE | 60,000 SEK | 70,000 SEK | **+17%** |

**Companies using ELK:** Netflix, LinkedIn, Medium, Adobe, Cisco, eBay

---

## 📖 THEORY: What is the ELK Stack?

### The Logging Problem

**Scenario: Production bug - users report errors**

❌ **Without ELK (The Old Way):**
```bash
# SSH to server 1
ssh server1.prod.com
tail -f /var/log/app.log | grep ERROR
# Nothing here...

# SSH to server 2
ssh server2.prod.com
tail -f /var/log/app.log | grep ERROR
# Nothing here either...

# Repeat for 50 servers... 😰
# 2 hours later, find the error on server 37
```

✅ **With ELK:**
```
Open Kibana → Search: "ERROR" AND "status:500"
Results: 47 errors in last 5 minutes
All from service: payment-api, pod: api-67d9f
Click → See full stack trace
Total time: 30 seconds ✅
```

---

### ELK Components Explained

```
┌─────────────────────────────────────────────────────────┐
│                    YOUR SERVERS                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │ App 1    │  │ App 2    │  │ App 3    │             │
│  │ logs to  │  │ logs to  │  │ logs to  │             │
│  │ file     │  │ file     │  │ file     │             │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘             │
│       │             │             │                     │
│       └─────────────┴─────────────┘                     │
│                     │                                   │
│              ┌──────▼──────┐                            │
│              │  Filebeat   │  ← Ships logs              │
│              └──────┬──────┘                            │
└─────────────────────┼─────────────────────────────────┘
                      │
              ┌───────▼────────┐
              │   Logstash     │  ← Parses & enriches
              │  (pipeline)    │
              └───────┬────────┘
                      │
              ┌───────▼────────┐
              │ Elasticsearch  │  ← Stores & indexes
              │  (search DB)   │
              └───────┬────────┘
                      │
              ┌───────▼────────┐
              │    Kibana      │  ← Visualizes & searches
              │   (Web UI)     │
              └────────────────┘
```

**1. Filebeat** - Lightweight log shipper
- Watches log files
- Sends new lines to Logstash/Elasticsearch
- Handles backpressure and retries

**2. Logstash** - Log processing pipeline
- Parses unstructured logs into structured data
- Enriches (add geolocation, lookup user info)
- Filters and transforms

**3. Elasticsearch** - Search and storage
- Stores logs in indexed format
- Full-text search in milliseconds
- Distributed and scalable

**4. Kibana** - Visualization and UI
- Web interface for searching logs
- Create dashboards and graphs
- Set up alerts

---

## 🛠️ HANDS-ON: ELK Stack Setup

### Step 1: Start ELK Stack with Docker

**Create docker-compose.yml:**
```yaml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.10.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - 9200:9200
    volumes:
      - es_data:/usr/share/elasticsearch/data

  logstash:
    image: docker.elastic.co/logstash/logstash:8.10.0
    ports:
      - 5000:5000
      - 9600:9600
    volumes:
      - ./logstash/pipeline:/usr/share/logstash/pipeline
    depends_on:
      - elasticsearch

  kibana:
    image: docker.elastic.co/kibana/kibana:8.10.0
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    ports:
      - 5601:5601
    depends_on:
      - elasticsearch

volumes:
  es_data:
```

**Start the stack:**
```bash
docker-compose up -d

# Wait 30 seconds for startup
# Access Kibana: http://localhost:5601
```

**Verify Elasticsearch:**
```bash
curl http://localhost:9200

# Response:
{
  "name" : "elasticsearch",
  "cluster_name" : "docker-cluster",
  "version" : {
    "number" : "8.10.0"
  }
}
```

---

### Step 2: Create Logstash Pipeline

**Create logstash/pipeline/logstash.conf:**
```ruby
input {
  tcp {
    port => 5000
    codec => json
  }
}

filter {
  # Parse JSON logs
  if [message] =~ /^\{/ {
    json {
      source => "message"
    }
  }

  # Parse common log format (Apache/Nginx)
  grok {
    match => {
      "message" => '%{IPORHOST:client_ip} %{USER:ident} %{USER:auth} \[%{HTTPDATE:timestamp}\] "%{WORD:method} %{DATA:request} HTTP/%{NUMBER:http_version}" %{NUMBER:response_code} %{NUMBER:bytes}'
    }
  }

  # Add geolocation based on IP
  geoip {
    source => "client_ip"
    target => "geoip"
  }

  # Parse timestamp
  date {
    match => [ "timestamp", "dd/MMM/yyyy:HH:mm:ss Z" ]
    target => "@timestamp"
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "logs-%{+YYYY.MM.dd}"
  }

  # Also print to console for debugging
  stdout {
    codec => rubydebug
  }
}
```

**Restart Logstash:**
```bash
docker-compose restart logstash
```

---

### Step 3: Send Logs to Logstash

**Example 1: Python application logging**

```python
# app.py
import logging
import json
import socket
from datetime import datetime

class LogstashHandler(logging.Handler):
    def __init__(self, host='localhost', port=5000):
        super().__init__()
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def emit(self, record):
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'host': socket.gethostname(),
            'path': record.pathname,
            'line': record.lineno
        }

        try:
            self.sock.sendall((json.dumps(log_entry) + '\n').encode('utf-8'))
        except Exception as e:
            print(f"Failed to send log: {e}")

# Setup logger
logger = logging.getLogger('myapp')
logger.setLevel(logging.INFO)
logger.addHandler(LogstashHandler())

# Use it
logger.info("Application started")
logger.warning("High memory usage detected", extra={'memory_pct': 85})
logger.error("Database connection failed", extra={'db': 'postgres', 'error': 'timeout'})
```

---

**Example 2: Filebeat for file-based logs**

**Install Filebeat:**
```bash
# Linux
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.10.0-linux-x86_64.tar.gz
tar xzvf filebeat-8.10.0-linux-x86_64.tar.gz
cd filebeat-8.10.0-linux-x86_64
```

**Configure filebeat.yml:**
```yaml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/nginx/access.log
      - /var/log/app/*.log
    fields:
      environment: production
      service: web-app

output.logstash:
  hosts: ["localhost:5000"]

# Optional: Parse JSON logs
json.keys_under_root: true
json.add_error_key: true
```

**Start Filebeat:**
```bash
./filebeat -e -c filebeat.yml
```

---

### Step 4: Search Logs in Kibana

**Open Kibana: http://localhost:5601**

**Create Index Pattern:**
```
1. Menu → Stack Management → Index Patterns
2. Create index pattern: logs-*
3. Timestamp field: @timestamp
4. Create
```

**Discover (Search) Interface:**
```
Menu → Discover

Search bar:
- level:ERROR
- message:"connection failed"
- response_code:500
- client_ip:"192.168.1.100"

Time range selector: Last 15 minutes / Last 24 hours / Custom

Filter by fields:
- Add filter → level → is → ERROR
- Add filter → service → is → payment-api
```

---

## 🔍 Elasticsearch Query DSL

### Basic Queries (REST API)

**Search all documents:**
```bash
curl -X GET "localhost:9200/logs-*/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": {}
  }
}
'
```

**Full-text search:**
```bash
curl -X GET "localhost:9200/logs-*/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "message": "database connection failed"
    }
  }
}
'
```

**Exact match (keyword field):**
```bash
curl -X GET "localhost:9200/logs-*/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "term": {
      "level.keyword": "ERROR"
    }
  }
}
'
```

**Range query (time-based):**
```bash
curl -X GET "localhost:9200/logs-*/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "range": {
      "@timestamp": {
        "gte": "now-1h",
        "lte": "now"
      }
    }
  }
}
'
```

**Boolean query (AND/OR):**
```bash
curl -X GET "localhost:9200/logs-*/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "bool": {
      "must": [
        { "match": { "level": "ERROR" }},
        { "match": { "service": "payment-api" }}
      ],
      "must_not": [
        { "match": { "message": "expected" }}
      ],
      "filter": [
        {
          "range": {
            "@timestamp": {
              "gte": "now-1h"
            }
          }
        }
      ]
    }
  }
}
'
```

---

### Aggregations (Analytics)

**Count by log level:**
```bash
curl -X GET "localhost:9200/logs-*/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "size": 0,
  "aggs": {
    "levels": {
      "terms": {
        "field": "level.keyword"
      }
    }
  }
}
'
```

**Error rate over time (histogram):**
```bash
curl -X GET "localhost:9200/logs-*/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "size": 0,
  "aggs": {
    "errors_over_time": {
      "date_histogram": {
        "field": "@timestamp",
        "fixed_interval": "1h"
      },
      "aggs": {
        "error_count": {
          "filter": {
            "term": { "level.keyword": "ERROR" }
          }
        }
      }
    }
  }
}
'
```

**Top 10 error messages:**
```bash
curl -X GET "localhost:9200/logs-*/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "size": 0,
  "query": {
    "term": { "level.keyword": "ERROR" }
  },
  "aggs": {
    "top_errors": {
      "terms": {
        "field": "message.keyword",
        "size": 10
      }
    }
  }
}
'
```

---

## 📊 Kibana Dashboards & Visualizations

### Creating Visualizations

**1. Line Chart - Logs over time**
```
Visualize → Create → Line

Y-axis: Count
X-axis: Date Histogram, @timestamp, Auto interval

Filters: level:ERROR
Split series: level.keyword
```

**2. Pie Chart - Log level distribution**
```
Visualize → Create → Pie

Metrics: Count
Buckets: Terms, field: level.keyword
```

**3. Data Table - Top error messages**
```
Visualize → Create → Data Table

Metrics: Count
Buckets: Terms, field: message.keyword, Size: 10
Sort: Descending
```

**4. Tag Cloud - Most common terms**
```
Visualize → Create → Tag Cloud

Tags: Terms, field: message.keyword
Size: 50
```

---

### Creating a Dashboard

**Dashboard: Application Health**

**Row 1: Overview**
- Total logs (metric)
- Error count (metric)
- Warning count (metric)
- Error rate % (metric)

**Row 2: Trends**
- Logs over time (line chart)
- Errors over time (area chart)

**Row 3: Details**
- Top error messages (data table)
- Log level distribution (pie chart)
- Services with errors (bar chart)

**Row 4: Raw Logs**
- Recent errors (saved search/log stream)

---

## 🔧 Advanced Logstash Patterns

### Parsing Complex Logs

**Java stack traces:**
```ruby
filter {
  multiline {
    pattern => "^\s"
    what => "previous"
  }

  grok {
    match => {
      "message" => "(?<timestamp>%{TIMESTAMP_ISO8601}) %{LOGLEVEL:level} %{JAVACLASS:class} - %{GREEDYDATA:message}"
    }
    overwrite => ["message"]
  }
}
```

**JSON nested fields:**
```ruby
filter {
  json {
    source => "message"
  }

  # Extract nested fields
  if [user][id] {
    mutate {
      add_field => { "user_id" => "%{[user][id]}" }
    }
  }
}
```

**Custom parsing with Ruby:**
```ruby
filter {
  ruby {
    code => '
      response_time = event.get("response_time")
      if response_time > 1000
        event.set("slow_request", true)
        event.set("severity", "warning")
      end
    '
  }
}
```

---

## 🎤 Interview Questions & Answers

### Question 1: Architecture

**Interviewer:** "Why use Logstash instead of sending logs directly to Elasticsearch?"

❌ **Weak Answer:**
> "Logstash processes logs."

✅ **Strong Answer:**
> "Logstash provides several benefits: 1) Parsing - transforms unstructured logs into structured documents with grok patterns. 2) Enrichment - adds geolocation, user lookups, or external API data. 3) Filtering - drops debug logs in production or PII data. 4) Buffering - handles backpressure if Elasticsearch is slow. 5) Multiple outputs - send to Elasticsearch, S3, and Kafka simultaneously. However, Logstash is resource-intensive. For simple log shipping, Filebeat can send directly to Elasticsearch using ingest pipelines for parsing."

**Why this impresses:** Shows understanding of pipeline trade-offs and alternatives.

---

### Question 2: Performance

**Interviewer:** "Elasticsearch is slow. How do you troubleshoot?"

❌ **Weak Answer:**
> "Add more servers."

✅ **Strong Answer:**
> "Several diagnostic steps: 1) Check cluster health: `GET /_cluster/health` - red/yellow status indicates problems. 2) Check slow query logs: `GET /_nodes/stats` for slow queries. 3) Examine index size and shard count - too many small shards hurt performance. 4) Check heap usage - if near 85%, increase heap or add nodes. 5) Optimize queries - avoid wildcards at beginning, use filters instead of queries when possible. 6) Review index mappings - too many fields causes mapping explosion. 7) Consider ILM policies to archive old data. Common fixes: increase heap, optimize queries, adjust shard count, enable caching."

**Why this impresses:** Demonstrates systematic performance analysis.

---

### Question 3: Data Management

**Interviewer:** "How do you handle log retention and prevent disk full?"

❌ **Weak Answer:**
> "Delete old logs manually."

✅ **Strong Answer:**
> "Use Index Lifecycle Management (ILM). Configure policies: Hot phase (0-7 days) keeps data on fast SSDs for searching. Warm phase (7-30 days) moves to slower disks, reduces replicas. Cold phase (30-90 days) searchable snapshots in S3. Delete phase (>90 days) removes indices. Example policy: rollover indices daily, keep 30 days hot, 60 days warm, then delete. Set up alerts when disk usage >80%. Consider using data streams for automatic index management. For critical logs, archive to S3 before deletion for compliance."

**Why this impresses:** Shows understanding of data lifecycle and cost optimization.

---

### Question 4: Troubleshooting

**Interviewer:** "Logs aren't appearing in Kibana. How do you debug?"

❌ **Weak Answer:**
> "Check if everything is running."

✅ **Strong Answer:**
> "Follow the data path: 1) Verify application is logging - check log files exist and are growing. 2) Check Filebeat status - `./filebeat test output` verifies Logstash connection. 3) Check Logstash - look at stdout output, confirm it's receiving and processing logs. 4) Check Elasticsearch - `GET /logs-*/_count` shows document count. 5) Check Kibana index pattern - ensure it matches index names and refresh fields list. 6) Check time range - logs might be from wrong timeframe. Common issues: firewall blocking ports, incorrect index pattern, Logstash parsing errors dropping logs, wrong timestamp format."

**Why this impresses:** Shows systematic debugging methodology.

---

## ⚠️ Common Mistakes (Avoid These!)

### ❌ Mistake 1: Logging Everything

**DON'T:**
```python
logger.debug(f"Variable x is {x}")  # Every line
logger.debug(f"Entering function foo")
logger.debug(f"Loop iteration {i}")
# 1 million logs per second = Elasticsearch dies
```

**DO:**
```python
logger.info("Request processed", extra={
    'user_id': user_id,
    'duration_ms': duration,
    'status': status
})
logger.error("Payment failed", extra={
    'order_id': order_id,
    'error': str(e)
})
# Only meaningful events
```

**Why:** Volume costs money and slows search. Log signal, not noise.

---

### ❌ Mistake 2: Unstructured Logs

**DON'T:**
```python
logger.info(f"User {user_id} purchased {item} for ${price}")
# String makes it hard to search and aggregate
```

**DO:**
```python
logger.info("Purchase completed", extra={
    'user_id': user_id,
    'item': item,
    'price': price,
    'currency': 'USD'
})
# Structured = searchable and aggregatable
```

**Why:** Structured logs enable powerful queries and dashboards.

---

### ❌ Mistake 3: No Index Rotation

**DON'T:**
```
All logs in one index: logs
Size: 500GB
Queries: Super slow
```

**DO:**
```
Daily indices: logs-2026.01.13
Automatic rollover
Old indices deleted after 30 days
```

**Why:** Manageable index size, faster queries, easier deletion.

---

## 📚 Flashcards

**Q: What is Elasticsearch?**
A: Distributed search and analytics engine, stores logs as JSON documents with full-text indexing.

**Q: What is Logstash?**
A: Data processing pipeline that parses, transforms, and enriches logs before sending to Elasticsearch.

**Q: What is Kibana?**
A: Web UI for searching, visualizing, and creating dashboards from Elasticsearch data.

**Q: What is Filebeat?**
A: Lightweight log shipper that watches log files and sends them to Logstash or Elasticsearch.

**Q: What is grok?**
A: Pattern matching language in Logstash for parsing unstructured logs into fields.

**Q: What is an index?**
A: Collection of documents in Elasticsearch, similar to a database table.

**Q: What is a shard?**
A: Subdivision of an index, allows horizontal scaling across multiple nodes.

**Q: What is ILM?**
A: Index Lifecycle Management - automates index rollover, archival, and deletion based on age/size.

**Q: What is a mapping?**
A: Schema definition in Elasticsearch, defines field types (text, keyword, number, date).

**Q: What is Beats?**
A: Family of lightweight shippers (Filebeat, Metricbeat, Packetbeat) for different data types.

---

## 🎓 Quiz

### Question 1

**What component parses unstructured logs into structured data?**

A) Elasticsearch
B) Kibana
C) Logstash ✅
D) Filebeat

**Answer:** C ✅

**Explanation:** Logstash uses grok patterns and filters to parse logs into structured JSON.

---

### Question 2

**Why use daily indices instead of one large index?**

A) Daily indices are required by Elasticsearch
B) Easier to delete old data and improve query performance ✅
C) Daily indices cost less money
D) Kibana only works with daily indices

**Answer:** B ✅

**Explanation:** Smaller indices are faster to query and easier to manage (delete entire index vs individual documents).

---

### Question 3

**What's the best field type for exact matching in Elasticsearch?**

A) text
B) keyword ✅
C) string
D) match

**Answer:** B ✅

**Explanation:** Keyword fields are not analyzed, enabling exact matches. Text fields are analyzed for full-text search.

---

## 🎯 Portfolio Project: Complete ELK Setup

**Build for your GitHub:**

**Project:** Production-ready ELK stack with sample applications

**Components:**
1. Docker Compose ELK stack
2. Python/Node.js app with structured logging
3. Filebeat configuration for multiple log types
4. Logstash pipelines with grok patterns
5. Kibana dashboards (errors, performance, business metrics)
6. ILM policy configuration
7. Complete documentation

**Why this impresses:**
- ✅ Full ELK implementation
- ✅ Real application integration
- ✅ Custom parsing pipelines
- ✅ Production configurations
- ✅ Documentation with examples

**GitHub structure:**
```
elk-logging-stack/
├── docker-compose.yml
├── elasticsearch/
│   └── ilm-policy.json
├── logstash/
│   └── pipeline/
│       ├── nginx.conf
│       ├── app.conf
│       └── patterns/
├── kibana/
│   └── dashboards/
├── filebeat/
│   └── filebeat.yml
├── sample-app/
│   ├── app.py
│   └── logging-config.yml
└── README.md
```

---

## 🌟 Why This Module Prepares You for Jobs

✅ **Centralized logging** - Essential production skill
✅ **Query mastery** - Search logs effectively
✅ **Pipeline building** - Parse any log format
✅ **Dashboard creation** - Visualize log insights
✅ **Troubleshooting** - Debug production issues fast

**Time to complete:** 2 hours
**Job market impact:** Opens 55% of DevOps roles
**Salary boost:** +13-16% average

---

**Module completed!** 🎉

**Next recommended:** Datadog APM - Modern application performance monitoring
"""
}

# Export as MODULE dict
MODULE = {
    "id": "monitoring-elk-stack",
    "slug": "monitoring-elk-stack",
    "title": "ELK Stack (Elasticsearch, Logstash, Kibana)",
    "description": "Master the ELK Stack for centralized logging: log aggregation, Elasticsearch queries, Logstash pipelines, Kibana dashboards. Used by 55% of DevOps teams.",
    "icon": "🔍",
    "category": "monitoring",
    "difficulty": "intermediate",
    "estimated_hours": 10,
    "tasks": [ELK_FUNDAMENTALS],
}
