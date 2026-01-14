"""
Nginx & Load Balancing - High-Performance Web Server
=====================================================

Master Nginx for reverse proxy, load balancing, SSL termination, and high-performance
web serving. The #1 web server powering 33% of all websites.
"""

NGINX_FUNDAMENTALS = {
    "title": "Nginx & Load Balancing Mastery",
    "slug": "nginx-load-balancing",
    "description": "Master Nginx for production: reverse proxy, load balancing algorithms, SSL/TLS, caching, and performance optimization. Power high-traffic websites.",
    "difficulty": "intermediate",
    "estimated_minutes": 120,
    "xp_reward": 200,
    "order_index": 1,
    "content": r"""# Nginx & Load Balancing Mastery

## 🎯 TL;DR (30 seconds)

Nginx is a high-performance web server and reverse proxy that can handle 10,000+ concurrent connections. Use it for
load balancing, SSL termination, static file serving, and caching. Powers 33% of all websites including Netflix, Airbnb, NASA.

**Why this matters:** Every production website needs a reverse proxy. Nginx is the industry standard for performance,
reliability, and flexibility.

---

## 🚀 Why Nginx for Your Career

### Job Market Reality (2026)

**Job Postings Analysis:**
- 68% of DevOps roles require web server knowledge
- 55% specifically mention Nginx
- 72% of SRE roles work with load balancers

**Salary Impact (Sweden):**
| Role | Without Nginx | With Nginx Expertise | Difference |
|------|--------------|---------------------|------------|
| DevOps Engineer | 45,000 SEK | 51,000 SEK | **+13%** |
| SRE | 55,000 SEK | 63,000 SEK | **+15%** |
| Platform Engineer | 52,000 SEK | 60,000 SEK | **+15%** |

**Companies using Nginx:** Netflix, Airbnb, Dropbox, WordPress.com, GitHub

---

## 📖 THEORY: Why Nginx?

### Nginx vs Apache

| Feature | Nginx | Apache |
|---------|-------|--------|
| Connections | 10,000+ | 1,000s |
| Memory per connection | 1 MB | 3 MB |
| Static files | Excellent ✅ | Good |
| Dynamic content | Via proxy | Built-in |
| Configuration | Simple | Complex |
| Performance | High ✅ | Medium |

**Nginx architecture:** Event-driven, asynchronous, non-blocking
**Apache architecture:** Process/thread per connection

**Result:** Nginx handles way more concurrent connections with less memory.

---

## 🛠️ HANDS-ON: Install & Basic Config

### Step 1: Install Nginx

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install nginx -y

# Start service
sudo systemctl start nginx
sudo systemctl enable nginx

# Check status
sudo systemctl status nginx

# Test
curl http://localhost
```

**Using Docker:**
```bash
docker run -d \
  --name nginx \
  -p 80:80 \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro \
  -v $(pwd)/html:/usr/share/nginx/html:ro \
  nginx:alpine

# Check logs
docker logs nginx
```

---

### Step 2: Basic Configuration

**`/etc/nginx/nginx.conf`:**
```nginx
user nginx;
worker_processes auto;  # One per CPU core
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
    worker_connections 1024;  # Max connections per worker
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

    access_log /var/log/nginx/access.log main;

    # Performance
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;

    # Compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript;

    # Include virtual hosts
    include /etc/nginx/conf.d/*.conf;
}
```

---

### Step 3: Static Website

**`/etc/nginx/conf.d/website.conf`:**
```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    root /var/www/example.com;
    index index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }

    # Cache static assets
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

```bash
# Test configuration
sudo nginx -t

# Reload (zero-downtime)
sudo systemctl reload nginx
```

---

## 🎓 Reverse Proxy

### Proxy to Backend Application

**Scenario:** Python/Node.js app running on port 5000

**`/etc/nginx/conf.d/app.conf`:**
```nginx
upstream backend {
    server 127.0.0.1:5000;
}

server {
    listen 80;
    server_name app.example.com;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
}
```

**Result:**
```
User → Nginx (port 80) → Backend (port 5000)
```

---

## 🎓 Load Balancing

### Round-Robin (Default)

```nginx
upstream backend {
    server 10.0.1.10:5000;
    server 10.0.1.11:5000;
    server 10.0.1.12:5000;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
    }
}
```

**Result:** Requests distributed evenly: 10 → 11 → 12 → 10 → 11 → 12...

---

### Least Connections

```nginx
upstream backend {
    least_conn;  # Send to server with fewest connections
    server 10.0.1.10:5000;
    server 10.0.1.11:5000;
    server 10.0.1.12:5000;
}
```

**Use when:** Backend processing time varies significantly.

---

### IP Hash (Session Persistence)

```nginx
upstream backend {
    ip_hash;  # Same client IP → same backend
    server 10.0.1.10:5000;
    server 10.0.1.11:5000;
    server 10.0.1.12:5000;
}
```

**Use when:** Sessions stored on backend servers (not Redis/database).

---

### Weighted Load Balancing

```nginx
upstream backend {
    server 10.0.1.10:5000 weight=3;  # 60% traffic
    server 10.0.1.11:5000 weight=1;  # 20% traffic
    server 10.0.1.12:5000 weight=1;  # 20% traffic
}
```

**Use when:** Servers have different capacities.

---

### Health Checks

```nginx
upstream backend {
    server 10.0.1.10:5000 max_fails=3 fail_timeout=30s;
    server 10.0.1.11:5000 max_fails=3 fail_timeout=30s;
    server 10.0.1.12:5000 max_fails=3 fail_timeout=30s;
}
```

**Behavior:**
- If 3 consecutive requests fail
- Mark server down for 30 seconds
- Automatically recover when healthy

---

## 🔒 SSL/TLS Configuration

### Let's Encrypt Free SSL

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Get certificate
sudo certbot --nginx -d example.com -d www.example.com

# Auto-renewal (already configured)
sudo certbot renew --dry-run
```

**Result:** Certbot automatically updates nginx config with SSL!

---

### Manual SSL Configuration

```nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    # SSL certificates
    ssl_certificate /etc/nginx/ssl/example.com.crt;
    ssl_certificate_key /etc/nginx/ssl/example.com.key;

    # SSL settings (Mozilla Modern)
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256';
    ssl_prefer_server_ciphers off;

    # SSL optimization
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    ssl_stapling on;
    ssl_stapling_verify on;

    # HSTS (force HTTPS)
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    location / {
        proxy_pass http://backend;
    }
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name example.com;
    return 301 https://$server_name$request_uri;
}
```

---

## 🚀 Caching

### Proxy Caching

```nginx
# Define cache path
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=1g inactive=60m;

server {
    listen 80;
    server_name example.com;

    location / {
        proxy_cache my_cache;
        proxy_cache_valid 200 10m;  # Cache 200 responses for 10 minutes
        proxy_cache_valid 404 1m;   # Cache 404 for 1 minute
        proxy_cache_bypass $http_pragma $http_authorization;  # Bypass cache for auth
        add_header X-Cache-Status $upstream_cache_status;  # Debug header

        proxy_pass http://backend;
    }
}
```

**Cache headers in response:**
- `X-Cache-Status: HIT` → Served from cache
- `X-Cache-Status: MISS` → Fetched from backend

---

## 📊 Monitoring & Logging

### Access Log Analysis

```bash
# Top 10 URLs
awk '{print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -10

# Top 10 IPs
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -10

# Response codes
awk '{print $9}' /var/log/nginx/access.log | sort | uniq -c | sort -rn

# Slow requests (>1 second)
awk '$NF > 1000 {print $0}' /var/log/nginx/access.log
```

---

### Status Module

```nginx
server {
    listen 8080;
    location /nginx_status {
        stub_status on;
        access_log off;
        allow 127.0.0.1;
        deny all;
    }
}
```

```bash
curl http://localhost:8080/nginx_status

# Output:
# Active connections: 291
# server accepts handled requests
#  16630948 16630948 31070465
# Reading: 6 Writing: 179 Waiting: 106
```

---

## 🎓 Production Patterns

### Rate Limiting

```nginx
# Define rate limit zone
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;

server {
    location /api/ {
        limit_req zone=api_limit burst=20 nodelay;
        proxy_pass http://backend;
    }
}
```

**Behavior:**
- 10 requests/second per IP
- Burst up to 20 (then reject with 503)

---

### DDoS Protection

```nginx
# Connection limits
limit_conn_zone $binary_remote_addr zone=conn_limit:10m;

server {
    # Max 10 connections per IP
    limit_conn conn_limit 10;

    # Max body size (prevent huge uploads)
    client_max_body_size 10M;

    # Timeouts (prevent slowloris)
    client_body_timeout 10s;
    client_header_timeout 10s;
    send_timeout 10s;
}
```

---

### Security Headers

```nginx
server {
    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' https:" always;

    # Hide Nginx version
    server_tokens off;
}
```

---

## 🎤 Interview Questions & Answers

### Question 1: Performance

**Interviewer:** "How does Nginx handle 10,000 concurrent connections?"

❌ **Weak Answer:**
> "It's fast."

✅ **Strong Answer:**
> "Nginx uses event-driven, asynchronous, non-blocking architecture. Instead of one thread per connection like Apache, Nginx has worker processes (one per CPU core) that handle thousands of connections using epoll/kqueue. Connections are idle most of the time waiting for I/O, so one worker can multiplex many connections. Memory per connection is ~1MB vs 3MB for Apache. This allows handling C10K problem efficiently. Key tuning: worker_connections and OS limits like somaxconn, nofile."

**Why this impresses:** Shows deep architectural understanding.

---

### Question 2: Caching

**Interviewer:** "When should you use Nginx caching vs Redis/CDN?"

❌ **Weak Answer:**
> "Cache everything in Nginx."

✅ **Strong Answer:**
> "Nginx caching is best for: 1) Proxied HTTP responses from backend. 2) Edge caching before CDN. 3) Simple use cases. Use Redis when: 1) Need cache sharing across multiple Nginx instances. 2) Complex cache invalidation logic. 3) Application-level caching. Use CDN for: 1) Global distribution. 2) Static assets. 3) DDoS protection. Often use all three: CDN → Nginx cache → Redis → Database."

**Why this impresses:** Shows understanding of caching layers.

---

## 📚 Flashcards

**Q: What is Nginx?**
A: High-performance web server and reverse proxy.

**Q: What is reverse proxy?**
A: Server that sits in front of backends, forwarding client requests.

**Q: What is upstream?**
A: Group of backend servers for load balancing.

**Q: What is worker_processes?**
A: Number of Nginx worker processes (set to CPU core count).

**Q: What is worker_connections?**
A: Max connections each worker can handle.

**Q: What is least_conn?**
A: Load balancing algorithm - send to server with fewest connections.

**Q: What is ip_hash?**
A: Load balancing - same client IP goes to same backend (session persistence).

---

## 🎓 Quiz

### Question 1

**Which load balancing algorithm keeps sessions on same backend?**

A) round_robin
B) least_conn
C) ip_hash ✅
D) random

**Answer:** C ✅

**Explanation:** ip_hash ensures same client IP always routes to same backend server.

---

### Question 2

**What does proxy_pass do?**

A) Blocks requests
B) Forwards requests to backend ✅
C) Caches responses
D) Compresses data

**Answer:** B ✅

**Explanation:** proxy_pass forwards client requests to specified backend server.

---

## 🌟 Why This Module Prepares You for Jobs

✅ **Reverse proxy expertise** - Essential for all production systems
✅ **Load balancing mastery** - Scale horizontally with confidence
✅ **SSL/TLS configuration** - Secure production traffic
✅ **Performance optimization** - Handle high-traffic websites
✅ **Interview confidence** - Answer web server questions expertly

**Time to complete:** 2 hours
**Job market impact:** Required in 68% of DevOps roles
**Salary boost:** +13-15% average
**Real-world use:** Every production deployment needs this

---

**Module completed!** 🎉

**Next recommended:** DevSecOps Practices - Security in CI/CD pipelines
"""
}

# Export as MODULE dict
MODULE = {
    "id": "networking-nginx",
    "slug": "networking-nginx",
    "title": "Nginx & Load Balancing",
    "description": "Master Nginx for production: reverse proxy, load balancing, SSL/TLS, caching, and performance optimization. Power high-traffic websites with confidence.",
    "icon": "🌐",
    "category": "networking",
    "difficulty": "intermediate",
    "estimated_hours": 10,
    "tasks": [NGINX_FUNDAMENTALS],
}
