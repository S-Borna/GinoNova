# =============================================================================
# BLOCK 2: INFRASTRUCTURE (Noder 5-8)
# =============================================================================

NODE_05_LOAD_BALANCING = {
    "node_id": 5,
    "title": "Load Balancing",
    "slug": "load-balancing",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [2],
    "content": '''# ⚖️ Load Balancing

## Varför detta är kritiskt
> "En server är en single point of failure. En load balancer är skillnaden mellan 'sajten är nere' och 'en server dog, ingen märkte'."

## Vad du kommer lära dig
- ✅ Load balancing algorithms (Round Robin, Least Connections)
- ✅ Layer 4 vs Layer 7
- ✅ Health checks
- ✅ Session persistence strategier

---

## Vad är Load Balancing?

```
                    ┌─────────────┐
                    │   Client    │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │Load Balancer│
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           │               │               │
    ┌──────▼──────┐ ┌──────▼──────┐ ┌──────▼──────┐
    │  Server 1   │ │  Server 2   │ │  Server 3   │
    │  (25%)      │ │  (50%)      │ │  (25%)      │
    └─────────────┘ └─────────────┘ └─────────────┘
```

## Load Balancing Algorithms

```yaml
Round Robin:
  - Roterande distribution
  - Enkel men naiv
  - Ignorerar serverkapacitet

Weighted Round Robin:
  - Vikter baserat på kapacitet
  - Server A (4x), Server B (2x), Server C (1x)

Least Connections:
  - Skickar till server med minst aktiva connections
  - Bra för varierande request-längd

Least Response Time:
  - Kombination av connections + response time
  - Bäst för UX

IP Hash:
  - Hash av client IP → specifik server
  - Sticky sessions utan cookies

Random:
  - Slumpmässig distribution
  - Överraskande effektiv
```

## Layer 4 vs Layer 7

```yaml
Layer 4 (Transport):
  Baserat på: IP, port, TCP/UDP
  Fördelar:
    - Snabbare
    - Mindre overhead
    - Protocol agnostic
  Begränsningar:
    - Ingen content inspection
    - Ingen cookie-based routing

Layer 7 (Application):
  Baserat på: HTTP headers, URL, cookies, content
  Fördelar:
    - Smart routing
    - SSL termination
    - Caching
    - Compression
  Begränsningar:
    - Mer overhead
    - Komplexare
```

## Layer 7 Routing

```nginx
# NGINX Layer 7 routing
upstream api_servers {
    server api1.example.com:8080;
    server api2.example.com:8080;
}

upstream web_servers {
    server web1.example.com:80;
    server web2.example.com:80;
}

server {
    location /api/ {
        proxy_pass http://api_servers;
    }

    location / {
        proxy_pass http://web_servers;
    }

    # Cookie-based routing
    location /dashboard {
        if ($cookie_version = "v2") {
            proxy_pass http://v2_servers;
        }
        proxy_pass http://v1_servers;
    }
}
```

## Health Checks

```yaml
Active Health Checks:
  - Load balancer pingar servrar
  - Ta bort ohälsosamma
  - Lägg tillbaka när friska

Passive Health Checks:
  - Övervaka live trafik
  - Räkna failures
  - Snabbare detection
```

```nginx
# NGINX health check
upstream backend {
    server backend1.example.com:8080;
    server backend2.example.com:8080;

    # Passive: 3 failures = 30s timeout
    server backend3.example.com:8080 max_fails=3 fail_timeout=30s;
}

# Active health check (NGINX Plus)
upstream backend {
    zone backend 64k;
    server backend1.example.com:8080;
    health_check interval=5s fails=3 passes=2;
}
```

## Session Persistence

```yaml
Problem:
  - User loggar in på Server A
  - Nästa request går till Server B
  - Session finns inte!

Lösningar:
  Sticky Sessions:
    - Cookie/IP hash → samma server
    - Enkelt men obalanserat

  Shared Session Store:
    - Redis/Memcached
    - Alla servrar delar
    - Bäst för skalbarhet

  Stateless (JWT):
    - Session i token
    - Ingen server state
    - Bäst om möjligt
```

## Load Balancer HA

```
           ┌─────────────────────┐
           │      Clients        │
           └──────────┬──────────┘
                      │
        ┌─────────────┴─────────────┐
        │                           │
   ┌────▼────┐                 ┌────▼────┐
   │   LB1   │◄───heartbeat───►│   LB2   │
   │ (Active)│                 │(Passive)│
   └────┬────┘                 └────┬────┘
        │                           │
        └─────────────┬─────────────┘
                      │
              ┌───────┴───────┐
              │   Servers     │
              └───────────────┘
```

## Cloud Load Balancers

```yaml
AWS:
  ALB: Layer 7, HTTP/HTTPS
  NLB: Layer 4, TCP/UDP, ultra-low latency
  CLB: Legacy, both layers

GCP:
  Global LB: Anycast IP, global distribution
  Regional LB: Single region

Azure:
  Application Gateway: Layer 7
  Load Balancer: Layer 4
```

| Algorithm | Use Case |
|-----------|----------|
| Round Robin | Homogena servrar |
| Weighted | Olika kapacitet |
| Least Connections | Varierande request tid |
| IP Hash | Session persistence |

**Nästa steg:** Node 6 - CDN
''',
}

NODE_06_CDN = {
    "node_id": 6,
    "title": "Content Delivery Networks",
    "slug": "cdn",
    "estimated_minutes": 45,
    "xp_reward": 130,
    "prerequisites": [5],
    "content": '''# 🌍 Content Delivery Networks (CDN)

## Varför detta är kritiskt
> "300ms latency från Sydney till Stockholm dödar UX. En CDN-edge 5ms bort räddar den. Fysikens lagar gäller även för bytes."

## Vad du kommer lära dig
- ✅ Push vs Pull CDN
- ✅ Cache headers och invalidering
- ✅ Edge computing
- ✅ CDN providers jämförelse

---

## Vad är en CDN?

```
Utan CDN:
User (Sydney) ──────────────────► Origin (Stockholm)
                 300ms latency

Med CDN:
User (Sydney) ────► Edge (Sydney) ────► Origin (Stockholm)
                5ms (cache hit)

```

## Hur CDN Fungerar

```
         ┌─────────────────────────────────────┐
         │            Internet                 │
         └─────────────────────────────────────┘
                          │
    ┌─────────────────────┼─────────────────────┐
    │                     │                     │
┌───▼───┐            ┌───▼───┐            ┌───▼───┐
│ Edge  │            │ Edge  │            │ Edge  │
│(Europe)│           │(Asia) │            │(US)   │
└───┬───┘            └───┬───┘            └───┬───┘
    │                    │                    │
    └────────────────────┼────────────────────┘
                         │
                  ┌──────▼──────┐
                  │   Origin    │
                  │   Server    │
                  └─────────────┘
```

## Push vs Pull CDN

```yaml
Push CDN:
  Hur: Du laddar upp content till CDN
  Fördelar:
    - Full kontroll
    - Ingen origin load
  Nackdelar:
    - Manuell hantering
    - Mer komplext
  Bra för:
    - Stort statiskt content
    - Video streaming
    - Sällan ändrat content

Pull CDN:
  Hur: CDN hämtar från origin vid request
  Fördelar:
    - Automatisk
    - Enklare setup
  Nackdelar:
    - Origin load vid cache miss
    - Första request långsam
  Bra för:
    - Dynamiskt content
    - Webbsidor
    - API responses
```

## CDN Caching

```yaml
Cache Headers:
  Cache-Control: max-age=31536000  # 1 år
  Cache-Control: no-cache          # Validera varje gång
  Cache-Control: no-store          # Aldrig cache
  Cache-Control: private           # Endast browser
  Cache-Control: public            # CDN kan cacha

ETag:
  - Unik identifier för content
  - Client skickar If-None-Match
  - Server returnerar 304 Not Modified
```

```python
# CDN-vänliga headers
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/static/<path:filename>')
def static_file(filename):
    response = make_response(get_file(filename))
    # Cache i 1 år (immutable content)
    response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
    return response

@app.route('/api/data')
def api_data():
    response = make_response(get_data())
    # Cache i 5 minuter, stale-while-revalidate
    response.headers['Cache-Control'] = 'public, max-age=300, stale-while-revalidate=60'
    return response
```

## Cache Invalidation

```yaml
Strategier:

TTL (Time to Live):
  - Enklast
  - Content expires automatiskt
  - Risk för stale data

Purge:
  - Manuell invalidering
  - API call till CDN
  - Kan ta tid att propagera

Versioned URLs:
  - /css/style.v1.css → /css/style.v2.css
  - Ingen invalidering behövs
  - Bäst för statiskt content
```

```bash
# Cloudflare purge
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone}/purge_cache" \\
     -H "Authorization: Bearer {token}" \\
     -d '{"files":["https://example.com/image.jpg"]}'

# AWS CloudFront invalidation
aws cloudfront create-invalidation \\
    --distribution-id EDFDVBD6EXAMPLE \\
    --paths "/images/*" "/css/*"
```

## CDN Providers

```yaml
Cloudflare:
  - Generös free tier
  - DDoS protection
  - Edge compute (Workers)

AWS CloudFront:
  - Integrerat med AWS
  - Lambda@Edge
  - Bra för S3

Fastly:
  - Instant purge
  - VCL configuration
  - Edge compute

Akamai:
  - Enterprise
  - Störst nätverk
  - Dyrt
```

## Edge Computing

```javascript
// Cloudflare Worker - Edge computing
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  // A/B testing at the edge
  const bucket = Math.random() < 0.5 ? 'A' : 'B'

  const response = await fetch(request)
  const html = await response.text()

  // Modify response at edge
  const modified = html.replace(
    '{{BUCKET}}',
    bucket
  )

  return new Response(modified, {
    headers: response.headers
  })
}
```

| CDN Type | Best For |
|----------|----------|
| Push | Video, large files |
| Pull | Websites, APIs |
| Edge Compute | Dynamic content |

**Nästa steg:** Node 7 - DNS
''',
}

NODE_07_DNS = {
    "node_id": 7,
    "title": "Domain Name System",
    "slug": "dns",
    "estimated_minutes": 45,
    "xp_reward": 130,
    "prerequisites": [1],
    "content": '''# 📡 Domain Name System (DNS)

## Varför detta är kritiskt
> "DNS är internets telefonbok - och ofta det första som går sönder. Förstår du inte DNS, förstår du inte varför 'det funkar inte'."

## Vad du kommer lära dig
- ✅ DNS resolution flow
- ✅ Record types (A, CNAME, MX, TXT)
- ✅ TTL strategier
- ✅ DNS för high availability

---

## DNS Resolution

```
1. User: "example.com"
           │
           ▼
2. Browser Cache ──(miss)──► 3. OS Cache
                                    │
                              (miss)│
                                    ▼
4. Recursive Resolver (ISP) ◄───────┘
           │
           │ (miss)
           ▼
5. Root Name Server (.): "Ask .com TLD"
           │
           ▼
6. TLD Name Server (.com): "Ask example.com NS"
           │
           ▼
7. Authoritative Name Server: "93.184.216.34"
           │
           ▼
8. Response cached, returned to user
```

## DNS Record Types

```yaml
A Record:
  - Maps domain to IPv4
  - example.com → 93.184.216.34

AAAA Record:
  - Maps domain to IPv6
  - example.com → 2606:2800:220:1:248:1893:25c8:1946

CNAME Record:
  - Alias to another domain
  - www.example.com → example.com
  - Kan inte vara på root domain

NS Record:
  - Nameserver för domain
  - example.com NS → ns1.provider.com

MX Record:
  - Mail server
  - Priority (lägre = högre prioritet)

TXT Record:
  - Text data
  - SPF, DKIM, domain verification

SRV Record:
  - Service location
  - _http._tcp.example.com
```

## TTL (Time to Live)

```yaml
Kort TTL (60-300s):
  Fördelar:
    - Snabba ändringar
    - Bra för failover
  Nackdelar:
    - Mer DNS queries
    - Högre latency

Lång TTL (3600-86400s):
  Fördelar:
    - Färre queries
    - Snabbare resolution
  Nackdelar:
    - Långsam propagation
    - Svårt vid incidenter
```

## DNS Load Balancing

```yaml
Round Robin DNS:
  example.com A 1.2.3.4
  example.com A 1.2.3.5
  example.com A 1.2.3.6

  # Roterande svar
  # Ingen health check!

Weighted DNS (Route 53):
  example.com A 1.2.3.4 weight=70
  example.com A 1.2.3.5 weight=30

Geolocation DNS:
  EU users → eu.example.com
  US users → us.example.com

Latency-based DNS:
  Routing till närmaste region
```

## DNS för High Availability

```yaml
# AWS Route 53 Health Checks

Primary (Active):
  Type: A
  Value: 1.2.3.4
  Health Check: HTTP /health
  Failover: PRIMARY

Secondary (Passive):
  Type: A
  Value: 5.6.7.8
  Health Check: HTTP /health
  Failover: SECONDARY

# Vid primary failure → traffic går till secondary
```

## DNS Security

```yaml
DNSSEC:
  - Signerade DNS records
  - Förhindrar spoofing
  - Chain of trust

DNS over HTTPS (DoH):
  - Krypterade DNS queries
  - Privacy
  - Port 443

DNS over TLS (DoT):
  - Krypterade queries
  - Dedicated port 853
```

## DNS i System Design

```
┌────────────────────────────────────────────────────┐
│                  Internet                          │
└────────────────────────────────────────────────────┘
                      │
                      ▼
            ┌─────────────────┐
            │   Route 53      │
            │ (Geolocation)   │
            └────────┬────────┘
         ┌───────────┴───────────┐
         │                       │
    ┌────▼────┐             ┌────▼────┐
    │  EU LB  │             │  US LB  │
    └────┬────┘             └────┬────┘
         │                       │
    ┌────▼────┐             ┌────▼────┐
    │EU Cluster│            │US Cluster│
    └─────────┘             └─────────┘
```

## DNS Providers

```yaml
Cloud Providers:
  - AWS Route 53
  - Google Cloud DNS
  - Azure DNS

Specialized:
  - Cloudflare DNS
  - NS1
  - Dyn (Oracle)

Free:
  - Cloudflare (generous free)
  - Hurricane Electric
```

| Record | Use Case |
|--------|----------|
| A/AAAA | IP mapping |
| CNAME | Aliases |
| MX | Email routing |
| TXT | Verification |
| NS | Delegation |

**Nästa steg:** Node 8 - Reverse Proxy
''',
}

NODE_08_PROXY = {
    "node_id": 8,
    "title": "Reverse Proxy & API Gateway",
    "slug": "reverse-proxy",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [5],
    "content": '''# 🚪 Reverse Proxy & API Gateway

## Varför detta är kritiskt
> "Exponera aldrig dina backend-servrar direkt. En reverse proxy är din frontdörr - SSL, caching, rate limiting, allt på ett ställe."

## Vad du kommer lära dig
- ✅ Forward vs Reverse Proxy
- ✅ SSL termination
- ✅ API Gateway features
- ✅ Service Mesh vs API Gateway

---

## Forward vs Reverse Proxy

```yaml
Forward Proxy:
  Client → Forward Proxy → Internet → Server
  - Döljer client
  - Corporate firewalls
  - Caching för clients

Reverse Proxy:
  Client → Internet → Reverse Proxy → Server
  - Döljer server
  - Load balancing
  - SSL termination
  - Caching
```

```
Forward Proxy:
┌────────┐     ┌─────────┐     ┌────────┐
│ Client ├────►│  Proxy  ├────►│ Server │
└────────┘     └─────────┘     └────────┘
  (känd)        (döljer client)  (ser proxy)

Reverse Proxy:
┌────────┐     ┌─────────┐     ┌────────┐
│ Client ├────►│  Proxy  ├────►│ Server │
└────────┘     └─────────┘     └────────┘
  (ser proxy)   (döljer server)  (dold)
```

## Reverse Proxy Benefits

```yaml
SSL/TLS Termination:
  - HTTPS på proxy
  - HTTP internt
  - Enklare cert management

Caching:
  - Cache responses
  - Minska backend load

Compression:
  - Gzip/Brotli
  - Snabbare responses

Security:
  - Hide backend topology
  - Rate limiting
  - WAF integration

Load Balancing:
  - Distribuera trafik
  - Health checks
```

## NGINX Reverse Proxy

```nginx
# Basic reverse proxy
upstream backend {
    server backend1:8080;
    server backend2:8080;
}

server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/ssl/cert.pem;
    ssl_certificate_key /etc/ssl/key.pem;

    # Proxy settings
    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Caching
    location /static/ {
        proxy_pass http://backend;
        proxy_cache_valid 200 1d;
        add_header X-Cache-Status $upstream_cache_status;
    }
}
```

## API Gateway

```yaml
Definition:
  - Single entry point för alla APIs
  - Mer features än reverse proxy

Features:
  - Request/Response transformation
  - Authentication/Authorization
  - Rate limiting
  - API versioning
  - Analytics
  - Developer portal
```

```
                    ┌─────────────────┐
                    │   API Gateway   │
                    │                 │
                    │  - Auth         │
                    │  - Rate limit   │
                    │  - Transform    │
                    │  - Route        │
                    └────────┬────────┘
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────▼────┐         ┌────▼────┐         ┌────▼────┐
    │ Users   │         │ Orders  │         │Products │
    │ Service │         │ Service │         │ Service │
    └─────────┘         └─────────┘         └─────────┘
```

## API Gateway Features

```yaml
# Kong API Gateway example

Services:
  - name: user-service
    url: http://users:8080

Routes:
  - name: user-routes
    service: user-service
    paths:
      - /api/users

Plugins:
  - name: rate-limiting
    config:
      minute: 100
      policy: local

  - name: jwt
    config:
      secret_is_base64: false

  - name: request-transformer
    config:
      add:
        headers:
          - X-Custom-Header:value
```

## Popular Solutions

```yaml
NGINX:
  - Reverse proxy
  - Load balancer
  - Kan vara API gateway med Plus

Kong:
  - Built on NGINX
  - Plugin ecosystem
  - Open source + Enterprise

AWS API Gateway:
  - Serverless
  - Lambda integration
  - Pay per request

Traefik:
  - Cloud native
  - Auto-discovery
  - Kubernetes native

Envoy:
  - Service mesh dataplane
  - gRPC support
  - Observability
```

## Service Mesh vs API Gateway

```yaml
API Gateway:
  - North-South traffic (external → internal)
  - External clients
  - Authentication
  - Rate limiting

Service Mesh:
  - East-West traffic (service → service)
  - Internal communication
  - mTLS
  - Observability
```

```
                External
                   │
            ┌──────▼──────┐
            │ API Gateway │  ◄── North-South
            └──────┬──────┘
    ┌──────────────┼──────────────┐
    │              │              │
┌───▼───┐      ┌───▼───┐      ┌───▼───┐
│Svc A  │◄────►│Svc B  │◄────►│Svc C  │
└───────┘      └───────┘      └───────┘
          ▲                ▲
          └────────────────┘
             East-West (Service Mesh)
```

| Component | Use Case |
|-----------|----------|
| Reverse Proxy | SSL, caching, basic LB |
| Load Balancer | Traffic distribution |
| API Gateway | API management |
| Service Mesh | Service-to-service |

**Nästa steg:** Node 9 - Database Types
''',
}

SYSTEM_DESIGN_BLOCK_2 = [
    NODE_05_LOAD_BALANCING,
    NODE_06_CDN,
    NODE_07_DNS,
    NODE_08_PROXY,
]
