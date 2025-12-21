"""
Kubernetes Fundamentals - Tasks 1-10
Premium Bootcamp-Quality Content
"""

TASKS_FUNDAMENTALS = [
    {
        "title": "Kubernetes Architecture & Concepts",
        "difficulty": "beginner",
        "estimated_minutes": 50,
        "xp_reward": 130,
        "content": r"""
# ☸️ Kubernetes Architecture & Concepts

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå vad Kubernetes är och löser
- Lära dig Kubernetes arkitektur
- Förstå Control Plane och Worker Nodes
- Grundläggande Kubernetes objekt

---

## 📖 Vad är Kubernetes?

Kubernetes (K8s) är en **container orchestration platform** som automatiserar deployment, scaling och management av containerized applications.

```
+-------------------------------------------------------------+
|                  KUBERNETES CLUSTER                          |
+-------------------------------------------------------------+
|                                                              |
|  +-------------------------------------------------------+ |
|  |                   CONTROL PLANE                        | |
|  |  +----------+ +----------+ +----------+ +----------+ | |
|  |  | API      | | etcd     | |Scheduler | |Controller| | |
|  |  | Server   | |          | |          | | Manager  | | |
|  |  +----------+ +----------+ +----------+ +----------+ | |
|  +-------------------------------------------------------+ |
|                           |                                 |
|          +----------------+----------------+               |
|          |                |                |                |
|  +-------▼-------+ +------▼------+ +------▼------+        |
|  |  Worker Node  | | Worker Node | | Worker Node |        |
|  |  +---------+  | | +---------+ | | +---------+ |        |
|  |  | kubelet |  | | | kubelet | | | | kubelet | |        |
|  |  | kube-   |  | | | kube-   | | | | kube-   | |        |
|  |  | proxy   |  | | | proxy   | | | | proxy   | |        |
|  |  | Pods    |  | | | Pods    | | | | Pods    | |        |
|  |  +---------+  | | +---------+ | | +---------+ |        |
|  +---------------+ +-------------+ +-------------+        |
|                                                             |
+-------------------------------------------------------------+
```

---

## 🏗️ Control Plane Components

| Komponent | Ansvar |
|-----------|--------|
| **API Server** | Exponerar K8s API, frontend för control plane |
| **etcd** | Key-value store för all cluster data |
| **Scheduler** | Väljer vilken node som kör nya pods |
| **Controller Manager** | Kör controller-processer |

---

## 🖥️ Worker Node Components

```
+-------------------------------------------------------------+
|                      WORKER NODE                             |
+-------------------------------------------------------------+
|                                                              |
|  +-----------------------------------------------------+   |
|  |                      kubelet                         |   |
|  |  - Kommunicerar med API server                      |   |
|  |  - Startar/stoppar containers                       |   |
|  |  - Rapporterar node status                          |   |
|  +-----------------------------------------------------+   |
|                                                              |
|  +-----------------------------------------------------+   |
|  |                    kube-proxy                        |   |
|  |  - Nätverksregler på noden                          |   |
|  |  - Service discovery                                |   |
|  |  - Load balancing                                   |   |
|  +-----------------------------------------------------+   |
|                                                              |
|  +-----------------------------------------------------+   |
|  |              Container Runtime                       |   |
|  |  - containerd, CRI-O                                |   |
|  |  - Kör containers                                   |   |
|  +-----------------------------------------------------+   |
|                                                              |
+-------------------------------------------------------------+
```

---

## 📦 Core Objects

```yaml
# Pod - Minsta deployable unit
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: nginx
    image: nginx:1.25

# Deployment - Deklarativ pod management
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: myapp:v1

# Service - Nätverks-endpoint
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080
```

---

## 🔧 kubectl Basics

```bash
# Cluster info
kubectl cluster-info
kubectl get nodes

# Namespaces
kubectl get namespaces
kubectl create namespace dev

# Basic CRUD
kubectl get pods
kubectl get pods -n kube-system
kubectl describe pod my-pod
kubectl delete pod my-pod

# Apply manifests
kubectl apply -f deployment.yaml
kubectl delete -f deployment.yaml
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Utforska Cluster
```bash
# Se cluster components
kubectl get componentstatuses
kubectl get nodes -o wide

# Se system pods
kubectl get pods -n kube-system

# Beskriv en node
kubectl describe node <node-name>
```

---

## 📚 Sammanfattning

| Object | Syfte |
|--------|-------|
| Pod | Kör containers |
| Deployment | Manage pod replicas |
| Service | Nätverks-access |
| Namespace | Isolering |

**Nästa steg:** Setting Up Local Kubernetes

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Setting Up Local Kubernetes",
        "difficulty": "beginner",
        "estimated_minutes": 45,
        "xp_reward": 120,
        "content": r"""
# 🖥️ Setting Up Local Kubernetes

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Installera lokala Kubernetes-miljöer
- Förstå skillnader mellan verktyg
- Konfigurera kubectl
- Verifiera installation

---

## 📖 Local Kubernetes Options

```
+-------------------------------------------------------------+
|               LOCAL KUBERNETES OPTIONS                       |
+-------------------------------------------------------------+
|                                                              |
|  +-------------+  +-------------+  +-------------+         |
|  |   Docker    |  |  minikube   |  |    kind     |         |
|  |   Desktop   |  |             |  |             |         |
|  +------+------+  +------+------+  +------+------+         |
|         |                |                |                 |
|  Enklast         Mest features    CI/CD fokus             |
|  Single node     Multi-node       Multi-cluster           |
|  GUI included    Addons           Snabbast                |
|                                                             |
|  +-------------+  +-------------+                          |
|  |    k3d      |  |    k3s      |                          |
|  |             |  |             |                          |
|  +------+------+  +------+------+                          |
|         |                |                                  |
|  k3s i Docker    Lightweight K8s                           |
|  Multi-cluster   Edge/IoT                                  |
|                                                             |
+-------------------------------------------------------------+
```

---

## 🐳 Docker Desktop Kubernetes

```bash
# Aktivera via Docker Desktop Settings
# Settings -> Kubernetes -> Enable Kubernetes

# Verifiera
kubectl config current-context
# docker-desktop

kubectl get nodes
# NAME             STATUS   ROLES           AGE
# docker-desktop   Ready    control-plane   1d
```

---

## 🔷 minikube

```bash
# Installation macOS
brew install minikube

# Installation Linux
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Starta cluster
minikube start
minikube start --cpus=4 --memory=8192

# Addons
minikube addons list
minikube addons enable ingress
minikube addons enable metrics-server

# Dashboard
minikube dashboard

# Service URL
minikube service my-service --url

# Stoppa/Ta bort
minikube stop
minikube delete
```

---

## 📦 kind (Kubernetes in Docker)

```bash
# Installation
brew install kind

# Skapa cluster
kind create cluster

# Med config
cat <<EOF | kind create cluster --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
EOF

# Lista clusters
kind get clusters

# Ladda lokal image
kind load docker-image myapp:latest

# Ta bort
kind delete cluster
```

---

## ⚙️ kubectl Configuration

```bash
# Se config
kubectl config view

# Se contexts
kubectl config get-contexts

# Byt context
kubectl config use-context docker-desktop
kubectl config use-context minikube

# Sätt default namespace
kubectl config set-context --current --namespace=dev

# Alias (lägg i .bashrc/.zshrc)
alias k='kubectl'
alias kgp='kubectl get pods'
alias kgs='kubectl get svc'
alias kgd='kubectl get deployments'
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Starta minikube
```bash
# Starta
minikube start

# Verifiera
kubectl get nodes
kubectl get pods -A

# Kör en pod
kubectl run nginx --image=nginx

# Cleanup
kubectl delete pod nginx
```

---

## 📚 Sammanfattning

| Verktyg | Best For |
|---------|----------|
| Docker Desktop | Enkel start |
| minikube | Development |
| kind | CI/CD, multi-node |
| k3d | Lightweight |

**Nästa steg:** Pods Deep Dive

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Pods Deep Dive",
        "difficulty": "beginner",
        "estimated_minutes": 55,
        "xp_reward": 140,
        "content": r"""
# 🫛 Pods Deep Dive

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå Pod-konceptet fullt ut
- Pod lifecycle och states
- Multi-container patterns
- Resource management

---

## 📖 What is a Pod?

```
+-------------------------------------------------------------+
|                          POD                                 |
+-------------------------------------------------------------+
|                                                              |
|  Shared:                                                     |
|  +-----------------------------------------------------+   |
|  |  • Network namespace (samma IP)                      |   |
|  |  • IPC namespace                                     |   |
|  |  • Volumes                                          |   |
|  +-----------------------------------------------------+   |
|                                                              |
|  +-------------+  +-------------+  +-------------+        |
|  | Container 1 |  | Container 2 |  | Container 3 |        |
|  |    (app)    |  |  (sidecar)  |  |   (proxy)   |        |
|  |             |  |             |  |             |        |
|  | :8080       |  | :9090       |  | :15001      |        |
|  +-------------+  +-------------+  +-------------+        |
|                                                              |
|  IP: 10.244.0.5                                             |
|                                                              |
+-------------------------------------------------------------+
```

---

## 📝 Pod Manifest

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
  namespace: default
  labels:
    app: my-app
    environment: dev
  annotations:
    description: "My application pod"
spec:
  containers:
  - name: app
    image: myapp:v1.0.0
    ports:
    - containerPort: 8080
      name: http
    env:
    - name: DATABASE_URL
      value: "postgresql://db:5432/app"
    - name: SECRET_KEY
      valueFrom:
        secretKeyRef:
          name: app-secrets
          key: secret-key
    resources:
      requests:
        memory: "128Mi"
        cpu: "100m"
      limits:
        memory: "256Mi"
        cpu: "500m"
    livenessProbe:
      httpGet:
        path: /health
        port: 8080
      initialDelaySeconds: 10
      periodSeconds: 10
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 5
  restartPolicy: Always
```

---

## 🔄 Pod Lifecycle

```
+-------------------------------------------------------------+
|                    POD LIFECYCLE                             |
+-------------------------------------------------------------+
|                                                              |
|  Pending ------▶ Running ------▶ Succeeded                  |
|     |               |                                        |
|     |               ▼                                        |
|     |           Failed                                       |
|     |                                                        |
|     +----------▶ Unknown                                    |
|                                                              |
|  Container States:                                          |
|  +----------+  +----------+  +----------+                 |
|  | Waiting  |  | Running  |  |Terminated|                 |
|  +----------+  +----------+  +----------+                 |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🔧 Pod Commands

```bash
# Skapa pod
kubectl run nginx --image=nginx:alpine

# Skapa från manifest
kubectl apply -f pod.yaml

# Lista pods
kubectl get pods
kubectl get pods -o wide
kubectl get pods -w  # Watch

# Detaljer
kubectl describe pod my-app

# Loggar
kubectl logs my-app
kubectl logs my-app -f  # Follow
kubectl logs my-app -c sidecar  # Specific container

# Exec
kubectl exec -it my-app -- bash
kubectl exec my-app -- cat /etc/hosts

# Port forward
kubectl port-forward my-app 8080:8080

# Ta bort
kubectl delete pod my-app
```

---

## 🏗️ Multi-Container Patterns

```yaml
# Sidecar Pattern
apiVersion: v1
kind: Pod
metadata:
  name: app-with-logging
spec:
  containers:
  - name: app
    image: myapp:v1
    volumeMounts:
    - name: logs
      mountPath: /var/log/app
  - name: log-shipper
    image: fluentd:latest
    volumeMounts:
    - name: logs
      mountPath: /var/log/app
  volumes:
  - name: logs
    emptyDir: {}
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Pod Lifecycle
```bash
# Skapa pod
kubectl run test-pod --image=nginx:alpine

# Observera status
kubectl get pod test-pod -w

# Inspektera
kubectl describe pod test-pod

# Se loggar
kubectl logs test-pod

# Exec in
kubectl exec -it test-pod -- sh

# Cleanup
kubectl delete pod test-pod
```

---

## 📚 Sammanfattning

| Probe | Syfte |
|-------|-------|
| livenessProbe | Är containern levande? |
| readinessProbe | Kan den ta emot traffic? |
| startupProbe | Har den startat? |

**Nästa steg:** Deployments & ReplicaSets

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Deployments & ReplicaSets",
        "difficulty": "medium",
        "estimated_minutes": 55,
        "xp_reward": 150,
        "content": r"""
# 🚀 Deployments & ReplicaSets

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå Deployment-konceptet
- ReplicaSet relationship
- Rolling updates och rollbacks
- Deployment strategies

---

## 📖 Deployment Architecture

```
+-------------------------------------------------------------+
|                      DEPLOYMENT                              |
|                    (my-app)                                  |
+-------------------------------------------------------------+
|                                                              |
|  Spec:                                                       |
|  - replicas: 3                                              |
|  - strategy: RollingUpdate                                  |
|                                                              |
|  +-----------------------------------------------------+   |
|  |                   REPLICASET                         |   |
|  |               (my-app-7d9f4b8c5)                     |   |
|  +-----------------------------------------------------+   |
|  |                                                      |   |
|  |   +---------+   +---------+   +---------+         |   |
|  |   |  Pod 1  |   |  Pod 2  |   |  Pod 3  |         |   |
|  |   | my-app  |   | my-app  |   | my-app  |         |   |
|  |   |  :8080  |   |  :8080  |   |  :8080  |         |   |
|  |   +---------+   +---------+   +---------+         |   |
|  |                                                      |   |
|  +-----------------------------------------------------+   |
|                                                              |
+-------------------------------------------------------------+
```

---

## 📝 Deployment Manifest

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: myapp:v1.0.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "500m"
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

---

## 🔄 Rolling Updates

```
+-------------------------------------------------------------+
|                  ROLLING UPDATE                              |
+-------------------------------------------------------------+
|                                                              |
|  Before:  [v1] [v1] [v1]                                    |
|                                                              |
|  Step 1:  [v1] [v1] [v1] [v2]   <- maxSurge: 1              |
|                                                              |
|  Step 2:  [v1] [v1] [v2] [v2]   <- 1 old terminated         |
|                                                              |
|  Step 3:  [v1] [v2] [v2] [v2]                               |
|                                                              |
|  Step 4:  [v2] [v2] [v2]        <- Complete!                 |
|                                                              |
+-------------------------------------------------------------+
```

```bash
# Uppdatera image
kubectl set image deployment/my-app app=myapp:v2.0.0

# Eller edit
kubectl edit deployment my-app

# Se rollout status
kubectl rollout status deployment/my-app

# Rollout history
kubectl rollout history deployment/my-app

# Rollback
kubectl rollout undo deployment/my-app
kubectl rollout undo deployment/my-app --to-revision=2
```

---

## 🔧 Deployment Commands

```bash
# Skapa deployment
kubectl create deployment nginx --image=nginx:alpine --replicas=3

# Från manifest
kubectl apply -f deployment.yaml

# Lista
kubectl get deployments
kubectl get rs  # ReplicaSets

# Skala
kubectl scale deployment my-app --replicas=5

# Autoscale
kubectl autoscale deployment my-app --min=3 --max=10 --cpu-percent=80

# Pausa/Återuppta rollout
kubectl rollout pause deployment/my-app
kubectl rollout resume deployment/my-app
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Complete Deployment
```bash
# Skapa deployment
kubectl create deployment web --image=nginx:1.24 --replicas=3

# Verifiera
kubectl get deploy,rs,pods

# Uppdatera
kubectl set image deployment/web nginx=nginx:1.25

# Watch rollout
kubectl rollout status deployment/web

# Rollback
kubectl rollout undo deployment/web

# Cleanup
kubectl delete deployment web
```

---

## 📚 Sammanfattning

| Strategy | Beskrivning |
|----------|-------------|
| RollingUpdate | Gradvis uppdatering (default) |
| Recreate | Ta ner alla, starta nya |

**Nästa steg:** Services & Networking

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
    },
    {
        "title": "Services & Networking",
        "difficulty": "medium",
        "estimated_minutes": 60,
        "xp_reward": 160,
        "content": r"""
# 🌐 Services & Networking

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå Service-typer
- Kubernetes DNS
- Network policies
- Load balancing

---

## 📖 Service Types

```
+-------------------------------------------------------------+
|                    SERVICE TYPES                             |
+-------------------------------------------------------------+
|                                                              |
|  ClusterIP (default)        NodePort                        |
|  +-----------------+       +-----------------+             |
|  |  Internal only  |       | Node IP:Port    |             |
|  |  10.96.0.1:80   |       | <NodeIP>:30080  |             |
|  |       ▼         |       |       ▼         |             |
|  |    [Pods]       |       |    [Pods]       |             |
|  +-----------------+       +-----------------+             |
|                                                              |
|  LoadBalancer               ExternalName                    |
|  +-----------------+       +-----------------+             |
|  |  Cloud LB       |       |  DNS CNAME      |             |
|  |  External IP    |       |  -> external.com |             |
|  |       ▼         |       |                 |             |
|  |    [Pods]       |       |                 |             |
|  +-----------------+       +-----------------+             |
|                                                              |
+-------------------------------------------------------------+
```

---

## 📝 Service Manifests

```yaml
# ClusterIP (default)
apiVersion: v1
kind: Service
metadata:
  name: my-app
spec:
  type: ClusterIP
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080

---
# NodePort
apiVersion: v1
kind: Service
metadata:
  name: my-app-nodeport
spec:
  type: NodePort
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080  # 30000-32767

---
# LoadBalancer
apiVersion: v1
kind: Service
metadata:
  name: my-app-lb
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080
```

---

## 🔗 Kubernetes DNS

```
+-------------------------------------------------------------+
|                   KUBERNETES DNS                             |
+-------------------------------------------------------------+
|                                                              |
|  Service DNS Format:                                        |
|  <service-name>.<namespace>.svc.cluster.local               |
|                                                              |
|  Examples:                                                   |
|  +-----------------------------------------------------+   |
|  |  my-app                    -> my-app.default.svc...   |   |
|  |  my-app.default            -> my-app.default.svc...   |   |
|  |  postgres.database         -> postgres.database.svc...|   |
|  |  redis.cache.svc.cluster.local (full)               |   |
|  +-----------------------------------------------------+   |
|                                                              |
|  Pod DNS:                                                    |
|  <pod-ip-dashes>.<namespace>.pod.cluster.local              |
|  10-244-0-5.default.pod.cluster.local                       |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🔒 Network Policies

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
```

---

## 🔧 Service Commands

```bash
# Skapa service
kubectl expose deployment my-app --port=80 --target-port=8080

# Lista services
kubectl get svc
kubectl get endpoints

# Beskriv service
kubectl describe svc my-app

# Test DNS från pod
kubectl run test --rm -it --image=busybox -- nslookup my-app

# Port forward
kubectl port-forward svc/my-app 8080:80
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Service Discovery
```bash
# Skapa deployment + service
kubectl create deployment web --image=nginx
kubectl expose deployment web --port=80

# Test från annan pod
kubectl run test --rm -it --image=busybox -- sh
# Inside: wget -O- http://web
# Inside: nslookup web

# Cleanup
kubectl delete deployment web
kubectl delete svc web
```

---

## 📚 Sammanfattning

| Type | Access | Use Case |
|------|--------|----------|
| ClusterIP | Internal | Default, microservices |
| NodePort | Node IP | Development, testing |
| LoadBalancer | External | Production |
| ExternalName | DNS | External services |

**Nästa steg:** ConfigMaps & Secrets

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "ConfigMaps & Secrets",
        "difficulty": "medium",
        "estimated_minutes": 50,
        "xp_reward": 145,
        "content": r"""
# 🔐 ConfigMaps & Secrets

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Hantera konfiguration med ConfigMaps
- Säker secrets management
- Montera som volumes eller env vars
- Best practices

---

## 📖 ConfigMaps vs Secrets

```
+-------------------------------------------------------------+
|             CONFIGMAPS vs SECRETS                            |
+-------------------------------------------------------------+
|                                                              |
|  ConfigMap                      Secret                       |
|  +-------------------+         +-------------------+       |
|  | Non-sensitive     |         | Sensitive data    |       |
|  | configuration     |         | Base64 encoded    |       |
|  |                   |         | Encrypted at rest |       |
|  | • App settings    |         | • Passwords       |       |
|  | • Config files    |         | • API keys        |       |
|  | • Feature flags   |         | • TLS certs       |       |
|  +-------------------+         +-------------------+       |
|                                                              |
+-------------------------------------------------------------+
```

---

## 📝 ConfigMap

```yaml
# ConfigMap manifest
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  # Key-value
  DATABASE_HOST: "postgres"
  LOG_LEVEL: "info"

  # File content
  app.conf: |
    server {
      listen 80;
      server_name localhost;
    }
```

```bash
# Skapa från literal
kubectl create configmap app-config \
  --from-literal=DATABASE_HOST=postgres \
  --from-literal=LOG_LEVEL=info

# Från fil
kubectl create configmap nginx-config --from-file=nginx.conf

# Från directory
kubectl create configmap app-files --from-file=config/
```

---

## 🔒 Secrets

```yaml
# Secret manifest
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  # Base64 encoded
  DB_PASSWORD: cGFzc3dvcmQxMjM=  # password123
  API_KEY: c2VjcmV0a2V5MTIz      # secretkey123

# Eller stringData (auto-encode)
---
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
stringData:
  DB_PASSWORD: password123
  API_KEY: secretkey123
```

```bash
# Skapa secret
kubectl create secret generic app-secrets \
  --from-literal=DB_PASSWORD=password123 \
  --from-literal=API_KEY=secretkey123

# Från fil
kubectl create secret generic tls-secret \
  --from-file=tls.crt \
  --from-file=tls.key

# TLS secret
kubectl create secret tls my-tls --cert=tls.crt --key=tls.key
```

---

## 🔗 Using in Pods

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
  - name: app
    image: myapp:v1

    # Som environment variables
    env:
    - name: DATABASE_HOST
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: DATABASE_HOST
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: app-secrets
          key: DB_PASSWORD

    # Alla från ConfigMap/Secret
    envFrom:
    - configMapRef:
        name: app-config
    - secretRef:
        name: app-secrets

    # Som volume
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
    - name: secret-volume
      mountPath: /etc/secrets
      readOnly: true

  volumes:
  - name: config-volume
    configMap:
      name: app-config
  - name: secret-volume
    secret:
      secretName: app-secrets
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Config & Secrets
```bash
# Skapa ConfigMap
kubectl create configmap web-config \
  --from-literal=APP_ENV=production

# Skapa Secret
kubectl create secret generic web-secrets \
  --from-literal=API_KEY=mysecretkey

# Skapa pod som använder dem
kubectl run web --image=nginx --dry-run=client -o yaml > pod.yaml
# Edit pod.yaml to add envFrom

# Verifiera
kubectl exec web -- env | grep -E "APP_ENV|API_KEY"
```

---

## 📚 Sammanfattning

| Method | Use Case |
|--------|----------|
| Env var | Single values |
| EnvFrom | All values |
| Volume | Files, multi-key |

**Nästa steg:** Persistent Storage

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Persistent Storage",
        "difficulty": "medium",
        "estimated_minutes": 55,
        "xp_reward": 155,
        "content": r"""
# 💾 Persistent Storage

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå Kubernetes storage-modellen
- PersistentVolumes och Claims
- Storage Classes
- StatefulSets för stateful apps

---

## 📖 Storage Architecture

```
+-------------------------------------------------------------+
|                KUBERNETES STORAGE MODEL                      |
+-------------------------------------------------------------+
|                                                              |
|  +------------------------------------------------------+  |
|  |                        Pod                            |  |
|  |  +------------------------------------------------+  |  |
|  |  |              volumeMounts                       |  |  |
|  |  |              /data                             |  |  |
|  |  +--------------------+---------------------------+  |  |
|  +-----------------------+------------------------------+  |
|                          |                                  |
|                          ▼                                  |
|  +------------------------------------------------------+  |
|  |           PersistentVolumeClaim (PVC)                |  |
|  |           name: my-data                               |  |
|  |           storage: 10Gi                               |  |
|  +------------------------+-----------------------------+  |
|                          | Binds to                        |
|                          ▼                                  |
|  +------------------------------------------------------+  |
|  |           PersistentVolume (PV)                       |  |
|  |           capacity: 10Gi                              |  |
|  |           storageClassName: standard                  |  |
|  +------------------------+-----------------------------+  |
|                          |                                  |
|                          ▼                                  |
|  +------------------------------------------------------+  |
|  |              Actual Storage                           |  |
|  |    (AWS EBS, GCP PD, Azure Disk, NFS, etc.)         |  |
|  +------------------------------------------------------+  |
|                                                              |
+-------------------------------------------------------------+
```

---

## 📝 PersistentVolume & Claim

```yaml
# PersistentVolume (provisioned by admin)
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: standard
  hostPath:
    path: /data/my-pv

---
# PersistentVolumeClaim (requested by user)
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: standard

---
# Pod using PVC
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
  - name: app
    image: myapp:v1
    volumeMounts:
    - name: data
      mountPath: /data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: my-pvc
```

---

## 📊 Storage Classes

```yaml
# StorageClass for dynamic provisioning
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
  iopsPerGB: "10"
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer

---
# PVC using StorageClass
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: fast-storage
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: fast-ssd
  resources:
    requests:
      storage: 20Gi
```

---

## 🔧 Storage Commands

```bash
# Lista PVs och PVCs
kubectl get pv
kubectl get pvc

# Beskriv
kubectl describe pvc my-pvc

# Se storage classes
kubectl get storageclass
kubectl get sc

# Ta bort PVC
kubectl delete pvc my-pvc
```

---

## 📊 Access Modes

| Mode | Abbr | Description |
|------|------|-------------|
| ReadWriteOnce | RWO | Single node read/write |
| ReadOnlyMany | ROX | Multi-node read only |
| ReadWriteMany | RWX | Multi-node read/write |

---

## 🏋️ Praktiska Övningar

### Övning 1: Persistent Storage
```bash
# Skapa PVC
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
EOF

# Verifiera
kubectl get pvc

# Använd i pod
kubectl run test-pod --image=nginx \
  --overrides='{
    "spec": {
      "containers": [{
        "name": "nginx",
        "image": "nginx",
        "volumeMounts": [{"name": "data", "mountPath": "/data"}]
      }],
      "volumes": [{
        "name": "data",
        "persistentVolumeClaim": {"claimName": "test-pvc"}
      }]
    }
  }'
```

---

## 📚 Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| PV | Admin-provisioned storage |
| PVC | User request for storage |
| StorageClass | Dynamic provisioning |
| ReclaimPolicy | Vad händer när PVC tas bort |

**Nästa steg:** Ingress Controllers

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
    },
    {
        "title": "Ingress Controllers",
        "difficulty": "medium",
        "estimated_minutes": 55,
        "xp_reward": 155,
        "content": r"""
# 🚪 Ingress Controllers

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå Ingress-konceptet
- Konfigurera routing
- TLS termination
- Path-based och host-based routing

---

## 📖 Ingress Architecture

```
+-------------------------------------------------------------+
|                   INGRESS FLOW                               |
+-------------------------------------------------------------+
|                                                              |
|  Internet                                                    |
|      |                                                       |
|      ▼                                                       |
|  +-----------------------------------------------------+   |
|  |              Load Balancer                           |   |
|  |           (Cloud Provider)                           |   |
|  +------------------------+----------------------------+   |
|                           |                                 |
|                           ▼                                 |
|  +-----------------------------------------------------+   |
|  |           Ingress Controller                         |   |
|  |        (nginx, traefik, etc.)                        |   |
|  +------------------------+----------------------------+   |
|                           |                                 |
|              +------------+------------+                   |
|              |            |            |                    |
|              ▼            ▼            ▼                    |
|  +--------------+ +--------------+ +--------------+       |
|  |  api.app.com | | web.app.com  | | app.com/api  |       |
|  |   Service A  | |   Service B  | |   Service C  |       |
|  +--------------+ +--------------+ +--------------+       |
|                                                             |
+-------------------------------------------------------------+
```

---

## 📝 Ingress Resource

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - myapp.example.com
    secretName: myapp-tls
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend
            port:
              number: 80
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api
            port:
              number: 8080
```

---

## 🔧 Install Ingress Controller

```bash
# nginx-ingress (Helm)
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm install ingress-nginx ingress-nginx/ingress-nginx

# Eller kubectl
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.0/deploy/static/provider/cloud/deploy.yaml

# Verifiera
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx
```

---

## 🔐 TLS Configuration

```bash
# Skapa TLS secret
kubectl create secret tls myapp-tls \
  --cert=tls.crt \
  --key=tls.key

# Eller med cert-manager
```

```yaml
# Ingress med TLS
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: secure-ingress
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - myapp.example.com
    secretName: myapp-tls
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend
            port:
              number: 80
```

---

## 🏗️ Host-Based Routing

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: multi-host-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: main-app
            port:
              number: 80
  - host: api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 8080
  - host: admin.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: admin-panel
            port:
              number: 3000
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Setup Ingress
```bash
# Install nginx-ingress (minikube)
minikube addons enable ingress

# Skapa deployment + service
kubectl create deployment web --image=nginx
kubectl expose deployment web --port=80

# Skapa ingress
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
spec:
  rules:
  - host: web.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web
            port:
              number: 80
EOF

# Test (lägg till i /etc/hosts)
# <minikube-ip> web.local
curl http://web.local
```

---

## 📚 Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| Ingress | API object för extern access |
| Ingress Controller | Implementation (nginx, traefik) |
| pathType | Prefix, Exact, ImplementationSpecific |

**Nästa steg:** Helm Package Manager

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Helm Package Manager",
        "difficulty": "medium",
        "estimated_minutes": 55,
        "xp_reward": 155,
        "content": r"""
# 📦 Helm Package Manager

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå Helm och charts
- Installera och hantera releases
- Skapa egna charts
- Templating och values

---

## 📖 What is Helm?

```
+-------------------------------------------------------------+
|                     HELM ARCHITECTURE                        |
+-------------------------------------------------------------+
|                                                              |
|  +-------------+    +-------------+    +-------------+     |
|  |   Chart     |---▶|   Release   |---▶|  K8s        |     |
|  |  (Package)  |    | (Instance)  |    |  Resources  |     |
|  +-------------+    +-------------+    +-------------+     |
|                                                              |
|  Chart = Package containing:                                |
|  • templates/     - Kubernetes manifests                   |
|  • values.yaml    - Default configuration                  |
|  • Chart.yaml     - Metadata                               |
|                                                              |
|  Release = Installed instance of a chart                   |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🔧 Helm Commands

```bash
# Installation
brew install helm

# Lägg till repos
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add stable https://charts.helm.sh/stable
helm repo update

# Sök charts
helm search repo nginx
helm search hub prometheus

# Installera chart
helm install my-nginx bitnami/nginx
helm install my-nginx bitnami/nginx -n web --create-namespace

# Med custom values
helm install my-nginx bitnami/nginx -f values.yaml
helm install my-nginx bitnami/nginx --set service.type=NodePort

# Lista releases
helm list
helm list -A  # Alla namespaces

# Uppgradera
helm upgrade my-nginx bitnami/nginx --set replicaCount=3

# Rollback
helm rollback my-nginx 1

# Ta bort
helm uninstall my-nginx
```

---

## 📝 Chart Structure

```
mychart/
+-- Chart.yaml          # Chart metadata
+-- values.yaml         # Default values
+-- charts/             # Dependencies
+-- templates/          # Template files
|   +-- deployment.yaml
|   +-- service.yaml
|   +-- ingress.yaml
|   +-- _helpers.tpl    # Template helpers
|   +-- NOTES.txt       # Post-install notes
+-- .helmignore         # Files to ignore
```

```yaml
# Chart.yaml
apiVersion: v2
name: myapp
description: My Application Helm Chart
type: application
version: 1.0.0
appVersion: "1.0.0"

# values.yaml
replicaCount: 3
image:
  repository: myapp
  tag: "1.0.0"
  pullPolicy: IfNotPresent
service:
  type: ClusterIP
  port: 80
```

---

## 🎨 Templating

```yaml
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "myapp.fullname" . }}
  labels:
    {{- include "myapp.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "myapp.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "myapp.selectorLabels" . | nindent 8 }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: {{ .Values.service.port }}
        {{- if .Values.resources }}
        resources:
          {{- toYaml .Values.resources | nindent 12 }}
        {{- end }}
```

---

## 🔧 Helm Development

```bash
# Skapa ny chart
helm create mychart

# Lint chart
helm lint mychart/

# Template (se genererad yaml)
helm template mychart/
helm template my-release mychart/ -f custom-values.yaml

# Dry run
helm install --dry-run --debug my-release mychart/

# Package chart
helm package mychart/

# Push till repo
helm push mychart-1.0.0.tgz oci://registry.example.com/charts
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Deploy with Helm
```bash
# Lägg till repo
helm repo add bitnami https://charts.bitnami.com/bitnami

# Install Redis
helm install my-redis bitnami/redis --set auth.enabled=false

# Se status
helm status my-redis

# Get values
helm get values my-redis

# Upgrade
helm upgrade my-redis bitnami/redis --set replica.replicaCount=3

# Cleanup
helm uninstall my-redis
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| helm install | Installera chart |
| helm upgrade | Uppgradera release |
| helm rollback | Återställ version |
| helm template | Visa genererad YAML |
| helm create | Skapa ny chart |

**Nästa steg:** Kubernetes RBAC

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Kubernetes RBAC",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 🔐 Kubernetes RBAC

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå RBAC-modellen
- ServiceAccounts
- Roles och ClusterRoles
- RoleBindings

---

## 📖 RBAC Model

```
+-------------------------------------------------------------+
|                      RBAC MODEL                              |
+-------------------------------------------------------------+
|                                                              |
|  WHO                  WHAT                  WHERE            |
|  +--------------+    +--------------+    +--------------+  |
|  |   Subject    |    |    Verbs     |    |  Resources   |  |
|  |              |    |              |    |              |  |
|  | • User       |    | • get        |    | • pods       |  |
|  | • Group      |---▶| • list       |---▶| • services   |  |
|  | • Service    |    | • create     |    | • secrets    |  |
|  |   Account    |    | • delete     |    | • configmaps |  |
|  +--------------+    +--------------+    +--------------+  |
|                                                              |
|  +-----------------------------------------------------+   |
|  |                    RoleBinding                       |   |
|  |  Connects Subject to Role/ClusterRole               |   |
|  +-----------------------------------------------------+   |
|                                                              |
+-------------------------------------------------------------+
```

---

## 👤 ServiceAccount

```yaml
# ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-app-sa
  namespace: default

---
# Pod using ServiceAccount
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  serviceAccountName: my-app-sa
  containers:
  - name: app
    image: myapp:v1
```

```bash
# Skapa ServiceAccount
kubectl create serviceaccount my-app-sa

# Lista
kubectl get sa

# Skapa token
kubectl create token my-app-sa
```

---

## 📝 Role & ClusterRole

```yaml
# Role (namespace-scoped)
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: default
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["pods/log"]
  verbs: ["get"]

---
# ClusterRole (cluster-wide)
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list"]
```

---

## 🔗 RoleBinding & ClusterRoleBinding

```yaml
# RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: ServiceAccount
  name: my-app-sa
  namespace: default
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io

---
# ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: read-secrets-global
subjects:
- kind: ServiceAccount
  name: monitoring-sa
  namespace: monitoring
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

---

## 🔧 RBAC Commands

```bash
# Skapa role
kubectl create role pod-reader \
  --verb=get,list,watch \
  --resource=pods

# Skapa clusterrole
kubectl create clusterrole node-reader \
  --verb=get,list \
  --resource=nodes

# Skapa rolebinding
kubectl create rolebinding my-app-binding \
  --role=pod-reader \
  --serviceaccount=default:my-app-sa

# Kontrollera access
kubectl auth can-i list pods --as=system:serviceaccount:default:my-app-sa
kubectl auth can-i create deployments --as=developer

# Se vem som kan göra vad
kubectl auth can-i --list
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Setup RBAC
```bash
# Skapa namespace och SA
kubectl create namespace dev
kubectl create sa developer -n dev

# Skapa role
kubectl create role developer-role \
  -n dev \
  --verb=get,list,create,delete \
  --resource=pods,services

# Bind role
kubectl create rolebinding developer-binding \
  -n dev \
  --role=developer-role \
  --serviceaccount=dev:developer

# Test
kubectl auth can-i create pods -n dev \
  --as=system:serviceaccount:dev:developer
# yes

kubectl auth can-i create deployments -n dev \
  --as=system:serviceaccount:dev:developer
# no
```

---

## 📚 Sammanfattning

| Resource | Scope | Use Case |
|----------|-------|----------|
| Role | Namespace | App permissions |
| ClusterRole | Cluster | Node access, CRDs |
| RoleBinding | Namespace | Bind to namespace |
| ClusterRoleBinding | Cluster | Cluster-wide access |

**Nästa steg:** Advanced Kubernetes Patterns

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
    },
]
