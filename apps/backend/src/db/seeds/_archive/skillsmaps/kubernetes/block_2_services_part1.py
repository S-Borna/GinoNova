# =============================================================================
# KUBERNETES MASTERY - BLOCK 2 PART 1: SERVICES & INGRESS
# Noder 5-6 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
KUBERNETES BLOCK 2 PART 1 - SERVICES & NETWORKING
=================================================
Node 5: Services - Networking & Load Balancing
Node 6: Ingress - HTTP/HTTPS Routing
"""

NODE_5 = {
    "id": "k8s_node_5",
    "title": "Services - Networking & Load Balancing",
    "slug": "services-networking-load-balancing",
    "content": r'''# 🌐 Services - Networking & Load Balancing

## 1. Introduktion & Kontext

Kubernetes Services löser ett fundamentalt problem: Pods är efemära med dynamiska IP-adresser, men applikationer behöver stabila endpoints. Services tillhandahåller en stabil abstraktion för att exponera applikationer.

### Problemet Services Löser

```
+-------------------------------------------------------------------------+
|                    THE SERVICE ABSTRACTION PROBLEM                       |
+-------------------------------------------------------------------------+
|                                                                          |
|  UTAN SERVICE:                                                           |
|  +----------+                                                           |
|  | Frontend |                                                           |
|  |   Pod    |                                                           |
|  +----+-----+                                                           |
|       |  "Vilken backend-IP ska jag använda?"                           |
|       |  "Pod IPs ändras hela tiden!"                                   |
|       ▼                                                                  |
|  +---------+  +---------+  +---------+                                 |
|  |Backend-1|  |Backend-2|  |Backend-3|                                 |
|  |10.1.0.5 |  |10.1.0.8 |  |10.1.0.12|  <- IPs ändras vid restart      |
|  +---------+  +---------+  +---------+                                 |
|                                                                          |
|  MED SERVICE:                                                            |
|  +----------+                                                           |
|  | Frontend |                                                           |
|  |   Pod    |                                                           |
|  +----+-----+                                                           |
|       |  "Anslut till backend-service:8080"                             |
|       ▼                                                                  |
|  +---------------------------------------------------------+           |
|  |                    SERVICE                               |           |
|  |        backend-service.default.svc.cluster.local        |           |
|  |                 ClusterIP: 10.96.1.100                   |           |
|  +-----------------------+---------------------------------+           |
|                          |  Load Balancing                              |
|       +------------------+------------------+                          |
|       ▼                  ▼                  ▼                           |
|  +---------+  +---------+  +---------+                                 |
|  |Backend-1|  |Backend-2|  |Backend-3|                                 |
|  +---------+  +---------+  +---------+                                 |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Service Types

### ClusterIP (Default)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend-service
  namespace: default
spec:
  type: ClusterIP                    # Default, kan utelämnas
  selector:
    app: backend                     # Matchar pod labels
  ports:
    - name: http
      protocol: TCP
      port: 80                       # Service port
      targetPort: 8080              # Container port
    - name: grpc
      protocol: TCP
      port: 9090
      targetPort: 9090
```

```
+-------------------------------------------------------------------------+
|                        ClusterIP SERVICE                                 |
+-------------------------------------------------------------------------+
|                                                                          |
|  Åtkomst: Endast inom klustret                                          |
|                                                                          |
|  +----------------------------------------------------------------+    |
|  |                      KUBERNETES CLUSTER                         |    |
|  |                                                                  |    |
|  |  +------------+        +--------------------+                  |    |
|  |  | Any Pod    |-------▶|  ClusterIP Service |                  |    |
|  |  | in cluster |        |  10.96.1.100:80    |                  |    |
|  |  +------------+        +---------+----------+                  |    |
|  |                                  |                              |    |
|  |                       +----------+----------+                  |    |
|  |                       ▼          ▼          ▼                  |    |
|  |                  +------+   +------+   +------+               |    |
|  |                  | Pod  |   | Pod  |   | Pod  |               |    |
|  |                  +------+   +------+   +------+               |    |
|  |                                                                  |    |
|  +----------------------------------------------------------------+    |
|                                                                          |
|  ❌ Ej åtkomlig från utsidan                                           |
|                                                                          |
+-------------------------------------------------------------------------+
```

### NodePort

```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  type: NodePort
  selector:
    app: frontend
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30080              # Port på varje node (30000-32767)
```

```
+-------------------------------------------------------------------------+
|                         NodePort SERVICE                                 |
+-------------------------------------------------------------------------+
|                                                                          |
|  Åtkomst: node-ip:nodePort från utsidan                                 |
|                                                                          |
|  EXTERNAL WORLD                                                          |
|       |                                                                  |
|       |  http://192.168.1.10:30080                                      |
|       |  http://192.168.1.11:30080                                      |
|       |  http://192.168.1.12:30080                                      |
|       ▼                                                                  |
|  +----------------------------------------------------------------+    |
|  |                      KUBERNETES CLUSTER                         |    |
|  |                                                                  |    |
|  |  +----------------+  +----------------+  +----------------+   |    |
|  |  |    Node 1      |  |    Node 2      |  |    Node 3      |   |    |
|  |  | 192.168.1.10   |  | 192.168.1.11   |  | 192.168.1.12   |   |    |
|  |  |     :30080     |  |     :30080     |  |     :30080     |   |    |
|  |  +-------+--------+  +-------+--------+  +-------+--------+   |    |
|  |          |                   |                   |             |    |
|  |          +-------------------+-------------------+             |    |
|  |                              |                                  |    |
|  |                    +---------▼---------+                       |    |
|  |                    |   NodePort Svc    |                       |    |
|  |                    |  ClusterIP + Port |                       |    |
|  |                    +---------+---------+                       |    |
|  |                              |                                  |    |
|  |               +--------------+--------------+                  |    |
|  |               ▼              ▼              ▼                  |    |
|  |          +------+       +------+       +------+               |    |
|  |          | Pod  |       | Pod  |       | Pod  |               |    |
|  |          +------+       +------+       +------+               |    |
|  |                                                                  |    |
|  +----------------------------------------------------------------+    |
|                                                                          |
+-------------------------------------------------------------------------+
```

### LoadBalancer

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-service
  annotations:
    # Cloud-specifika annotations
    service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
    service.beta.kubernetes.io/aws-load-balancer-internal: "false"
spec:
  type: LoadBalancer
  selector:
    app: api
  ports:
    - port: 443
      targetPort: 8443
  loadBalancerSourceRanges:         # IP whitelist
    - 10.0.0.0/8
    - 192.168.0.0/16
```

```
+-------------------------------------------------------------------------+
|                       LoadBalancer SERVICE                               |
+-------------------------------------------------------------------------+
|                                                                          |
|  Åtkomst: Via cloud provider load balancer                              |
|                                                                          |
|  INTERNET                                                                |
|       |                                                                  |
|       |  https://api.example.com (DNS -> LB IP)                         |
|       ▼                                                                  |
|  +-----------------------------------------------------------------+   |
|  |                 CLOUD LOAD BALANCER                              |   |
|  |            (AWS ALB/NLB, GCP LB, Azure LB)                      |   |
|  |                   External IP: 52.1.2.3                          |   |
|  +----------------------------+------------------------------------+   |
|                               |                                         |
|  +----------------------------+------------------------------------+   |
|  |          KUBERNETES CLUSTER                                      |   |
|  |                            |                                     |   |
|  |  +----------------+  +----+-----------+  +----------------+    |   |
|  |  |    Node 1      |  |    ▼           |  |    Node 3      |    |   |
|  |  |                |  |  LoadBalancer  |  |                |    |   |
|  |  |                |  |    Service     |  |                |    |   |
|  |  +----------------+  +----------------+  +----------------+    |   |
|  |                            |                                     |   |
|  |               +------------+------------+                       |   |
|  |               ▼            ▼            ▼                       |   |
|  |          +------+     +------+     +------+                    |   |
|  |          | Pod  |     | Pod  |     | Pod  |                    |   |
|  |          +------+     +------+     +------+                    |   |
|  |                                                                  |   |
|  +----------------------------------------------------------------+   |
|                                                                          |
|  ✅ Extern IP från cloud provider                                       |
|  ✅ SSL termination (om konfigurerat)                                   |
|  ✅ Health checks                                                        |
|                                                                          |
+-------------------------------------------------------------------------+
```

### ExternalName

```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-db
spec:
  type: ExternalName
  externalName: database.external-provider.com   # CNAME-alias
```

### Headless Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres-headless
spec:
  clusterIP: None                   # Headless!
  selector:
    app: postgres
  ports:
    - port: 5432
```

## 3. Service Discovery

### DNS-baserad Discovery

```
+-------------------------------------------------------------------------+
|                       SERVICE DNS RESOLUTION                             |
+-------------------------------------------------------------------------+
|                                                                          |
|  Full DNS Name:                                                          |
|  <service>.<namespace>.svc.cluster.local                                |
|                                                                          |
|  Exempel:                                                                |
|  backend-service.production.svc.cluster.local                           |
|                                                                          |
|  Kortformer (inom samma namespace):                                      |
|  +------------------------------------------------------------------+  |
|  |                                                                    |  |
|  |  backend-service                         # Samma namespace        |  |
|  |  backend-service.production              # Specifik namespace    |  |
|  |  backend-service.production.svc          # Med svc suffix        |  |
|  |  backend-service.production.svc.cluster.local  # Full FQDN      |  |
|  |                                                                    |  |
|  +------------------------------------------------------------------+  |
|                                                                          |
|  Headless Service DNS (för StatefulSets):                               |
|  <pod-name>.<service>.<namespace>.svc.cluster.local                     |
|                                                                          |
|  Exempel:                                                                |
|  postgres-0.postgres-headless.default.svc.cluster.local                 |
|  postgres-1.postgres-headless.default.svc.cluster.local                 |
|                                                                          |
+-------------------------------------------------------------------------+
```

### Testa DNS Resolution

```bash
# Starta debug pod
kubectl run dns-test --image=busybox:1.36 --rm -it -- sh

# I podden:
nslookup backend-service
nslookup backend-service.default.svc.cluster.local

# Visa full DNS config
cat /etc/resolv.conf
# nameserver 10.96.0.10
# search default.svc.cluster.local svc.cluster.local cluster.local
# options ndots:5
```

## 4. Endpoints & EndpointSlices

```bash
# Visa endpoints
kubectl get endpoints backend-service
# NAME              ENDPOINTS                                      AGE
# backend-service   10.244.0.5:8080,10.244.1.3:8080,10.244.2.7:8080  5m

# Detaljerad endpoint info
kubectl describe endpoints backend-service

# EndpointSlices (modernare, bättre skalning)
kubectl get endpointslices -l kubernetes.io/service-name=backend-service
```

## 5. Praktiska Övningar

### Övning 1: Skapa Service-hierarki

```bash
# Backend deployment
cat << 'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
        - name: backend
          image: nginx
          ports:
            - containerPort: 80
---
# ClusterIP Service
apiVersion: v1
kind: Service
metadata:
  name: backend-clusterip
spec:
  type: ClusterIP
  selector:
    app: backend
  ports:
    - port: 80
      targetPort: 80
---
# NodePort Service
apiVersion: v1
kind: Service
metadata:
  name: backend-nodeport
spec:
  type: NodePort
  selector:
    app: backend
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
EOF

# Verifiera
kubectl get svc
kubectl get endpoints
```

### Övning 2: Service Connectivity Test

```bash
# Skapa test pod
kubectl run test-pod --image=curlimages/curl --rm -it -- sh

# Testa ClusterIP
curl backend-clusterip:80

# Testa med full DNS
curl backend-clusterip.default.svc.cluster.local:80

# Testa NodePort (från host)
curl <node-ip>:30080
```

## 6. Vanliga Fel & Lösningar

### Service har inga endpoints

```bash
# Symptom
kubectl get endpoints my-service
# NAME         ENDPOINTS   AGE
# my-service   <none>      5m

# Diagnos
# 1. Kolla att selector matchar pod labels
kubectl get svc my-service -o yaml | grep -A5 selector
kubectl get pods --show-labels

# 2. Kolla att pods är Ready
kubectl get pods -l app=myapp

# 3. Kolla port configuration
kubectl describe svc my-service
kubectl describe pod <pod-name>
```

### DNS Resolution Failure

```bash
# Symptom
nslookup my-service
# server can't find my-service: NXDOMAIN

# Diagnos
# 1. Verifiera att CoreDNS körs
kubectl get pods -n kube-system -l k8s-app=kube-dns

# 2. Kolla CoreDNS logs
kubectl logs -n kube-system -l k8s-app=kube-dns

# 3. Verifiera service existerar
kubectl get svc my-service
```

## 7. Best Practices

```
+-------------------------------------------------------------------------+
|                     SERVICE BEST PRACTICES                               |
+-------------------------------------------------------------------------+
|                                                                          |
|  ✅ Service Type Val                                                    |
|     □ ClusterIP: Intern kommunikation (default)                         |
|     □ NodePort: Development/test, direktåtkomst                         |
|     □ LoadBalancer: Production extern åtkomst                           |
|     □ ExternalName: Externa tjänster                                    |
|                                                                          |
|  ✅ Naming & Labels                                                     |
|     □ Konsekvent namngivning (app-name-service)                         |
|     □ Matcha selector med pod labels                                    |
|     □ Använd named ports                                                |
|                                                                          |
|  ✅ Security                                                            |
|     □ Begränsa LoadBalancer med sourceRanges                            |
|     □ Använd NetworkPolicies                                            |
|     □ TLS termination i Ingress, inte Service                           |
|                                                                          |
|  ✅ Performance                                                         |
|     □ sessionAffinity för stateful apps                                 |
|     □ externalTrafficPolicy: Local för performance                      |
|     □ Undvik NodePort i produktion                                      |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 8. Advanced Service Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: advanced-service
  annotations:
    # Timeout settings
    service.kubernetes.io/topology-aware-hints: "auto"
spec:
  type: ClusterIP

  # Session affinity
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 10800       # 3 timmar

  # IP families (dual-stack)
  ipFamilies:
    - IPv4
    - IPv6
  ipFamilyPolicy: PreferDualStack

  selector:
    app: myapp
  ports:
    - name: http
      port: 80
      targetPort: http            # Named port
    - name: https
      port: 443
      targetPort: https
```

## 9-14. Sammanfattning & Task

### Service Type Comparison

| Type | Åtkomst | Use Case |
|------|---------|----------|
| **ClusterIP** | Intern | Microservices |
| **NodePort** | node:port | Dev/Test |
| **LoadBalancer** | Extern IP | Production |
| **ExternalName** | DNS alias | External services |
| **Headless** | Pod DNS | StatefulSets |

### Praktisk Task

```bash
# Skapa komplett service-setup:
# 1. Backend med ClusterIP
# 2. Frontend med LoadBalancer
# 3. Testa connectivity

kubectl apply -f services.yaml
kubectl get svc,endpoints
kubectl run test --image=busybox --rm -it -- wget -qO- backend:80
```

---

**Nästa Node:** Ingress - HTTP/HTTPS Routing ->
''',
    "xp_reward": 155,
    "estimated_minutes": 55,
    "prerequisites": ["k8s_node_4"],
    "learning_outcomes": [
        "Förstå Service-konceptet",
        "Implementera olika service types",
        "Konfigurera service discovery",
        "Felsöka service connectivity"
    ]
}

NODE_6 = {
    "id": "k8s_node_6",
    "title": "Ingress - HTTP/HTTPS Routing",
    "slug": "ingress-http-https-routing",
    "content": r'''# 🚪 Ingress - HTTP/HTTPS Routing

## 1. Introduktion & Kontext

Ingress är en API-resurs som hanterar extern HTTP/HTTPS-åtkomst till tjänster i klustret. Det tillhandahåller URL-baserad routing, SSL-terminering, och name-based virtual hosting.

### Varför Ingress?

```
+-------------------------------------------------------------------------+
|                    INGRESS VS LOADBALANCER                               |
+-------------------------------------------------------------------------+
|                                                                          |
|  UTAN INGRESS (Multiple LoadBalancers):                                 |
|                                                                          |
|  Internet --+--▶ LB1 ($18/month) --▶ api-service                       |
|             +--▶ LB2 ($18/month) --▶ web-service                       |
|             +--▶ LB3 ($18/month) --▶ admin-service                     |
|             +--▶ LB4 ($18/month) --▶ docs-service                      |
|                                                                          |
|             💸 Kostnad: $72/month för 4 services                        |
|             ❌ Ingen delad SSL                                          |
|             ❌ Ingen path-baserad routing                               |
|                                                                          |
|  MED INGRESS (Single Load Balancer):                                    |
|                                                                          |
|  Internet --▶ LB ($18/month) --▶ Ingress Controller                    |
|                                        |                                |
|                                        +-- /api/*    --▶ api-service   |
|                                        +-- /         --▶ web-service   |
|                                        +-- /admin/*  --▶ admin-service |
|                                        +-- /docs/*   --▶ docs-service  |
|                                                                          |
|             💰 Kostnad: $18/month för alla services                     |
|             ✅ SSL termination på en plats                              |
|             ✅ Host-baserad routing                                     |
|             ✅ Path-baserad routing                                     |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Ingress Architecture

```
+-------------------------------------------------------------------------+
|                      INGRESS ARCHITECTURE                                |
+-------------------------------------------------------------------------+
|                                                                          |
|  EXTERNAL TRAFFIC                                                        |
|        |                                                                 |
|        |  https://api.example.com                                       |
|        |  https://web.example.com                                       |
|        ▼                                                                 |
|  +-----------------------------------------------------------------+   |
|  |                    CLOUD LOAD BALANCER                           |   |
|  |                (Points to Ingress Controller)                    |   |
|  +----------------------------+------------------------------------+   |
|                               |                                         |
|  +----------------------------+------------------------------------+   |
|  |         KUBERNETES CLUSTER |                                     |   |
|  |                            ▼                                     |   |
|  |  +---------------------------------------------------------+    |   |
|  |  |               INGRESS CONTROLLER                         |    |   |
|  |  |           (nginx-ingress / traefik / etc)               |    |   |
|  |  |                                                          |    |   |
|  |  |  Watches: Ingress resources                              |    |   |
|  |  |  Updates: nginx.conf / routing rules                     |    |   |
|  |  |  Handles: SSL termination                                |    |   |
|  |  +---------------------------+-----------------------------+    |   |
|  |                              |                                   |   |
|  |           +------------------+------------------+               |   |
|  |           |                  |                  |               |   |
|  |           ▼                  ▼                  ▼               |   |
|  |  +--------------+   +--------------+   +--------------+        |   |
|  |  |  Ingress     |   |  Ingress     |   |  Ingress     |        |   |
|  |  |  Resource    |   |  Resource    |   |  Resource    |        |   |
|  |  |  (api.yaml)  |   |  (web.yaml)  |   |  (admin.yaml)|        |   |
|  |  +------+-------+   +------+-------+   +------+-------+        |   |
|  |         |                  |                  |                 |   |
|  |         ▼                  ▼                  ▼                 |   |
|  |  +--------------+   +--------------+   +--------------+        |   |
|  |  | api-service  |   | web-service  |   |admin-service |        |   |
|  |  +------+-------+   +------+-------+   +------+-------+        |   |
|  |         |                  |                  |                 |   |
|  |         ▼                  ▼                  ▼                 |   |
|  |      [Pods]             [Pods]             [Pods]              |   |
|  |                                                                  |   |
|  +----------------------------------------------------------------+   |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 3. Ingress Controller Installation

### NGINX Ingress Controller

```bash
# Helm installation (rekommenderat)
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

helm install ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx \
  --create-namespace \
  --set controller.replicaCount=2 \
  --set controller.service.type=LoadBalancer

# Verifiera installation
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx

# Kubectl apply installation
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.4/deploy/static/provider/cloud/deploy.yaml
```

### Traefik Ingress Controller

```bash
helm repo add traefik https://traefik.github.io/charts
helm install traefik traefik/traefik \
  --namespace traefik \
  --create-namespace
```

## 4. Ingress Resources

### Basic Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: basic-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx            # Viktigt!
  rules:
    - host: app.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web-service
                port:
                  number: 80
```

### Path-based Routing

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: path-based-ingress
  annotations:
    nginx.ingress.kubernetes.io/use-regex: "true"
spec:
  ingressClassName: nginx
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /api/v1
            pathType: Prefix
            backend:
              service:
                name: api-v1-service
                port:
                  number: 80

          - path: /api/v2
            pathType: Prefix
            backend:
              service:
                name: api-v2-service
                port:
                  number: 80

          - path: /health
            pathType: Exact
            backend:
              service:
                name: health-service
                port:
                  number: 80
```

### Host-based Routing

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: multi-host-ingress
spec:
  ingressClassName: nginx
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 80

    - host: web.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web-service
                port:
                  number: 80

    - host: admin.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: admin-service
                port:
                  number: 80
```

## 5. TLS/SSL Configuration

### Skapa TLS Secret

```bash
# Generera självsignerat cert (för test)
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout tls.key -out tls.crt \
  -subj "/CN=*.example.com"

# Skapa secret
kubectl create secret tls example-tls \
  --cert=tls.crt \
  --key=tls.key

# Eller via YAML
cat << 'EOF' | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: example-tls
type: kubernetes.io/tls
data:
  tls.crt: <base64-encoded-cert>
  tls.key: <base64-encoded-key>
EOF
```

### Ingress med TLS

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: tls-ingress
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - api.example.com
        - web.example.com
      secretName: example-tls
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 80
    - host: web.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web-service
                port:
                  number: 80
```

### Cert-Manager Integration

```bash
# Installera cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.2/cert-manager.yaml

# Skapa ClusterIssuer för Let's Encrypt
cat << 'EOF' | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: admin@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      - http01:
          ingress:
            class: nginx
EOF

# Ingress med automatisk cert
cat << 'EOF' | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: auto-tls-ingress
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - api.example.com
      secretName: api-tls-cert      # Skapas automatiskt
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 80
EOF
```

## 6. Advanced Annotations

### NGINX Ingress Annotations

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: advanced-ingress
  annotations:
    # SSL/TLS
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"

    # Timeouts
    nginx.ingress.kubernetes.io/proxy-connect-timeout: "60"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "60"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "60"

    # Body size
    nginx.ingress.kubernetes.io/proxy-body-size: "50m"

    # Rate limiting
    nginx.ingress.kubernetes.io/limit-rps: "100"
    nginx.ingress.kubernetes.io/limit-connections: "10"

    # Cors
    nginx.ingress.kubernetes.io/enable-cors: "true"
    nginx.ingress.kubernetes.io/cors-allow-origin: "https://example.com"

    # Authentication
    nginx.ingress.kubernetes.io/auth-type: basic
    nginx.ingress.kubernetes.io/auth-secret: basic-auth
    nginx.ingress.kubernetes.io/auth-realm: "Authentication Required"

    # Rewrite
    nginx.ingress.kubernetes.io/rewrite-target: /$2

    # Custom headers
    nginx.ingress.kubernetes.io/configuration-snippet: |
      add_header X-Frame-Options "SAMEORIGIN";
      add_header X-Content-Type-Options "nosniff";
spec:
  ingressClassName: nginx
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /api(/|$)(.*)
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 80
```

## 7. Praktiska Övningar

### Övning 1: Komplett Ingress Setup

```bash
# 1. Deploya backend services
cat << 'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: nginx
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  selector:
    app: api
  ports:
    - port: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: nginx
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
  ports:
    - port: 80
EOF

# 2. Skapa Ingress
cat << 'EOF' | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: main-ingress
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
spec:
  ingressClassName: nginx
  rules:
    - host: api.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 80
    - host: web.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web-service
                port:
                  number: 80
EOF

# 3. Testa (lägg till i /etc/hosts)
# <INGRESS_IP> api.local web.local
curl http://api.local
curl http://web.local
```

## 8. Vanliga Fel & Lösningar

### 404 Not Found

```bash
# Diagnos
kubectl describe ingress my-ingress
kubectl get svc -l <service-selector>
kubectl get endpoints <service-name>

# Vanliga orsaker:
# 1. Fel service name i ingress
# 2. Service har inga endpoints
# 3. pathType fel (Prefix vs Exact)
```

### 502 Bad Gateway

```bash
# Diagnos
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx

# Vanliga orsaker:
# 1. Backend service nere
# 2. Fel port i service
# 3. Health check failing
```

## 9. Best Practices

```
+-------------------------------------------------------------------------+
|                      INGRESS BEST PRACTICES                              |
+-------------------------------------------------------------------------+
|                                                                          |
|  ✅ Security                                                            |
|     □ Alltid SSL/TLS i produktion                                       |
|     □ Använd cert-manager för automatiska certs                         |
|     □ Aktivera HSTS                                                     |
|     □ Sätt security headers                                             |
|                                                                          |
|  ✅ Performance                                                         |
|     □ Sätt lämpliga timeouts                                            |
|     □ Konfigurera rate limiting                                         |
|     □ Använd gzip compression                                           |
|                                                                          |
|  ✅ Organization                                                        |
|     □ En ingress per applikation/team                                   |
|     □ Använd ingressClassName                                           |
|     □ Dokumentera annotations                                           |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 10-14. Sammanfattning & Task

### Ingress Features

| Feature | Beskrivning |
|---------|-------------|
| **Path routing** | /api/* -> service A |
| **Host routing** | api.example.com -> service A |
| **TLS** | SSL termination |
| **Annotations** | Controller-specific config |

---

**Nästa Node:** ConfigMaps & Secrets ->
''',
    "xp_reward": 160,
    "estimated_minutes": 60,
    "prerequisites": ["k8s_node_5"],
    "learning_outcomes": [
        "Förstå Ingress-arkitekturen",
        "Konfigurera path och host routing",
        "Implementera TLS/SSL",
        "Använda Ingress annotations"
    ]
}

# Block 2 Part 1 exports
BLOCK_2_PART_1_NODES = [NODE_5, NODE_6]
