# =============================================================================
# KUBERNETES MASTERY - BLOCK 1 PART 1: K8S INTRODUCTION & ARCHITECTURE
# Noder 1-2 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
KUBERNETES BLOCK 1 PART 1 - FUNDAMENTALS
========================================
Node 1: Kubernetes Introduction & Why K8s
Node 2: kubectl Mastery - CLI Deep Dive

Varje nod följer 14-sektions strukturen från Linux Mastery:
1. Introduktion & Kontext
2. Teknisk Djupdykning
3. Arkitektur & Komponenter
4. ASCII-diagram
5. Hands-on Kommandon
6. Praktiska Övningar
7. Vanliga Fel & Lösningar
8. Best Practices
9. Verkliga Scenarion
10. Integration & Kopplingar
11. Sammanfattning
12. Nästa Steg
13. Praktisk Task
14. Quiz/Självtest
"""

NODE_1 = {
    "id": "k8s_node_1",
    "title": "Kubernetes Introduction & Why K8s",
    "slug": "kubernetes-introduction-why-k8s",
    "content": r'''# ☸️ Kubernetes Introduction & Why K8s

## 1. Introduktion & Kontext

Kubernetes (K8s) har revolutionerat hur vi deployar, skalar och hanterar containeriserade applikationer. Utvecklat ursprungligen av Google baserat på deras interna system Borg, är Kubernetes nu industristandard för container orchestration.

### Varför Heter Det Kubernetes?

Kubernetes kommer från grekiskans κυβερνήτης (kybernetes) som betyder "styrman" eller "pilot". K8s är en förkortning där 8:an representerar de åtta bokstäverna mellan K och s.

### Historisk Kontext

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CONTAINER ORCHESTRATION EVOLUTION                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  2000s          2010s              2014          2015         Nu        │
│    │              │                  │             │           │         │
│    ▼              ▼                  ▼             ▼           ▼         │
│  ┌─────┐     ┌─────────┐      ┌──────────┐  ┌─────────┐  ┌─────────┐   │
│  │Borg │     │ Docker  │      │Kubernetes│  │  CNCF   │  │K8s 1.30+│   │
│  │@Goog│────▶│Container│─────▶│ Open     │─▶│Graduated│─▶│Industry │   │
│  │le   │     │  2013   │      │ Source   │  │ 2018    │  │Standard │   │
│  └─────┘     └─────────┘      └──────────┘  └─────────┘  └─────────┘   │
│                                                                          │
│  Legacy VM     Container        Container    Cloud Native   Multi-Cloud │
│  Management    Revolution       Orchestration Foundation    Standard    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Teknisk Djupdykning

### Vad Kubernetes Löser

| Problem | Traditionell Lösning | Kubernetes Lösning |
|---------|---------------------|-------------------|
| **Skalning** | Manuell VM-provisioning | Auto-scaling baserat på metrics |
| **High Availability** | Load balancers + failover | Self-healing & replicas |
| **Deployment** | Manuella script, downtime | Rolling updates, zero-downtime |
| **Service Discovery** | Hårdkodade IP:er, DNS | Inbyggd DNS, Services |
| **Load Balancing** | Externa load balancers | Inbyggd service load balancing |
| **Secret Management** | Filer, env vars i kod | Secrets & ConfigMaps |
| **Storage** | Manuell mount, NFS | Persistent Volumes, CSI |
| **Configuration** | Manuell per server | Declarative YAML |
| **Rollback** | Manuell återställning | `kubectl rollout undo` |
| **Resource Management** | Överprovisioning | Requests/Limits per pod |

### Kubernetes vs Alternativ

```
┌──────────────────────────────────────────────────────────────────────┐
│              CONTAINER ORCHESTRATION COMPARISON                       │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  Feature          │ Kubernetes │ Docker Swarm │ Nomad  │ ECS         │
│  ─────────────────┼────────────┼──────────────┼────────┼─────────────│
│  Complexity       │ High       │ Low          │ Medium │ Medium      │
│  Scalability      │ Excellent  │ Good         │ Good   │ Good        │
│  Learning Curve   │ Steep      │ Gentle       │ Medium │ Medium      │
│  Community        │ Massive    │ Declining    │ Growing│ AWS-focused │
│  Multi-cloud      │ Yes        │ Limited      │ Yes    │ AWS only    │
│  Auto-scaling     │ Advanced   │ Basic        │ Good   │ Good        │
│  Service Mesh     │ Excellent  │ Limited      │ Good   │ App Mesh    │
│  Ecosystem        │ Huge       │ Small        │ Growing│ AWS-only    │
│                                                                       │
│  Recommendation: Kubernetes för production, Docker Swarm för dev     │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

## 3. Arkitektur & Komponenter

### Control Plane (Master) Komponenter

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        KUBERNETES CONTROL PLANE                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                      CONTROL PLANE                               │    │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────────┐ │    │
│  │  │   kube-api-    │  │     etcd       │  │   kube-scheduler   │ │    │
│  │  │    server      │  │                │  │                    │ │    │
│  │  │                │  │  ┌──────────┐  │  │  ┌──────────────┐  │ │    │
│  │  │  ┌──────────┐  │  │  │ Key-Value│  │  │  │ Pod Placement│  │ │    │
│  │  │  │  REST    │  │  │  │  Store   │  │  │  │ Algorithm    │  │ │    │
│  │  │  │  API     │  │  │  │          │  │  │  │              │  │ │    │
│  │  │  │ Gateway  │  │  │  │ Cluster  │  │  │  │ Node Select  │  │ │    │
│  │  │  └──────────┘  │  │  │  State   │  │  │  │ Affinity     │  │ │    │
│  │  │                │  │  └──────────┘  │  │  └──────────────┘  │ │    │
│  │  └───────┬────────┘  └───────┬────────┘  └─────────┬──────────┘ │    │
│  │          │                   │                     │            │    │
│  │          └───────────────────┼─────────────────────┘            │    │
│  │                              │                                   │    │
│  │  ┌───────────────────────────▼────────────────────────────────┐ │    │
│  │  │              kube-controller-manager                        │ │    │
│  │  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐   │ │    │
│  │  │  │ Deployment  │ │ ReplicaSet  │ │   Node Controller   │   │ │    │
│  │  │  │ Controller  │ │ Controller  │ │                     │   │ │    │
│  │  │  └─────────────┘ └─────────────┘ └─────────────────────┘   │ │    │
│  │  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐   │ │    │
│  │  │  │   Service   │ │  Endpoint   │ │  ServiceAccount     │   │ │    │
│  │  │  │ Controller  │ │ Controller  │ │  Controller         │   │ │    │
│  │  │  └─────────────┘ └─────────────┘ └─────────────────────┘   │ │    │
│  │  └────────────────────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Worker Node Komponenter

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          KUBERNETES WORKER NODE                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                         WORKER NODE                              │    │
│  │                                                                  │    │
│  │  ┌────────────────────────────────────────────────────────────┐ │    │
│  │  │                        kubelet                              │ │    │
│  │  │  • Registrerar noden med API server                        │ │    │
│  │  │  • Hanterar pod lifecycle                                  │ │    │
│  │  │  • Rapporterar node status                                 │ │    │
│  │  │  • Monterar volumes                                        │ │    │
│  │  │  • Kör container probes (liveness/readiness)               │ │    │
│  │  └────────────────────────────────────────────────────────────┘ │    │
│  │                                                                  │    │
│  │  ┌────────────────────────────────────────────────────────────┐ │    │
│  │  │                      kube-proxy                             │ │    │
│  │  │  • Hanterar network rules (iptables/IPVS)                  │ │    │
│  │  │  • Service load balancing                                  │ │    │
│  │  │  • ClusterIP, NodePort, LoadBalancer                       │ │    │
│  │  └────────────────────────────────────────────────────────────┘ │    │
│  │                                                                  │    │
│  │  ┌────────────────────────────────────────────────────────────┐ │    │
│  │  │                  Container Runtime                          │ │    │
│  │  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │ │    │
│  │  │  │containerd│  │  CRI-O  │  │ Docker  │  │  Other  │       │ │    │
│  │  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘       │ │    │
│  │  └────────────────────────────────────────────────────────────┘ │    │
│  │                                                                  │    │
│  │  ┌──────────────────┐  ┌──────────────────┐                     │    │
│  │  │      Pod 1       │  │      Pod 2       │                     │    │
│  │  │  ┌────┐ ┌────┐  │  │  ┌────┐          │                     │    │
│  │  │  │ C1 │ │ C2 │  │  │  │ C1 │          │                     │    │
│  │  │  └────┘ └────┘  │  │  └────┘          │                     │    │
│  │  └──────────────────┘  └──────────────────┘                     │    │
│  │                                                                  │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 4. Fullständig Kluster-arkitektur

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    KUBERNETES CLUSTER ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│     USERS/CLIENTS                           EXTERNAL SYSTEMS                 │
│     ┌─────────┐                             ┌─────────────┐                  │
│     │ kubectl │                             │  CI/CD      │                  │
│     │   CLI   │                             │  (Jenkins,  │                  │
│     └────┬────┘                             │   GitLab)   │                  │
│          │                                  └──────┬──────┘                  │
│          │                                         │                         │
│          ▼                                         ▼                         │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                          CONTROL PLANE                                 │  │
│  │  ┌─────────────┐ ┌─────────────┐ ┌──────────────┐ ┌────────────────┐  │  │
│  │  │ API Server  │ │    etcd     │ │  Scheduler   │ │ Controller Mgr │  │  │
│  │  │  Port 6443  │ │ Port 2379   │ │              │ │                │  │  │
│  │  └──────┬──────┘ └─────────────┘ └──────────────┘ └────────────────┘  │  │
│  │         │                                                              │  │
│  └─────────┼──────────────────────────────────────────────────────────────┘  │
│            │                                                                  │
│            │                   INTERNAL NETWORK                              │
│  ┌─────────┴─────────────────────────────────────────────────────────────┐  │
│  │                                                                        │  │
│  │   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐   │  │
│  │   │   WORKER NODE 1  │  │   WORKER NODE 2  │  │   WORKER NODE 3  │   │  │
│  │   │                  │  │                  │  │                  │   │  │
│  │   │  ┌────────────┐  │  │  ┌────────────┐  │  │  ┌────────────┐  │   │  │
│  │   │  │  kubelet   │  │  │  │  kubelet   │  │  │  │  kubelet   │  │   │  │
│  │   │  │ kube-proxy │  │  │  │ kube-proxy │  │  │  │ kube-proxy │  │   │  │
│  │   │  │ containerd │  │  │  │ containerd │  │  │  │ containerd │  │   │  │
│  │   │  └────────────┘  │  │  └────────────┘  │  │  └────────────┘  │   │  │
│  │   │                  │  │                  │  │                  │   │  │
│  │   │  ┌─────┐┌─────┐  │  │  ┌─────┐┌─────┐  │  │  ┌─────┐┌─────┐  │   │  │
│  │   │  │Pod1 ││Pod2 │  │  │  │Pod3 ││Pod4 │  │  │  │Pod5 ││Pod6 │  │   │  │
│  │   │  └─────┘└─────┘  │  │  └─────┘└─────┘  │  │  └─────┘└─────┘  │   │  │
│  │   │                  │  │                  │  │                  │   │  │
│  │   └──────────────────┘  └──────────────────┘  └──────────────────┘   │  │
│  │                                                                        │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 5. Lokalt Utvecklingskluster

### Installation av Minikube

```bash
# macOS
brew install minikube
minikube start --driver=docker --cpus=4 --memory=8192

# Linux
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start --driver=docker

# Windows (PowerShell som Admin)
choco install minikube
minikube start --driver=hyperv

# Verifiera installation
minikube status
kubectl cluster-info
```

### Installation av Kind (Kubernetes in Docker)

```bash
# macOS/Linux
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

# Skapa kluster
kind create cluster --name dev-cluster

# Med anpassad konfiguration
cat << 'EOF' > kind-config.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings:
      - containerPort: 30000
        hostPort: 30000
        protocol: TCP
  - role: worker
  - role: worker
EOF

kind create cluster --config kind-config.yaml --name multi-node
```

### Installation av k3s (Lightweight Kubernetes)

```bash
# Single-node installation
curl -sfL https://get.k3s.io | sh -

# Verifiera
sudo k3s kubectl get nodes

# Kopiera kubeconfig
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown $USER ~/.kube/config
```

## 6. Praktiska Övningar

### Övning 1: Starta ditt första kluster

```bash
# Starta Minikube med specifika resurser
minikube start \
  --cpus=4 \
  --memory=8192 \
  --disk-size=50g \
  --driver=docker

# Verifiera att klustret körs
kubectl cluster-info
kubectl get nodes -o wide

# Kontrollera alla system-pods
kubectl get pods -n kube-system

# Öppna Kubernetes Dashboard
minikube dashboard
```

### Övning 2: Utforska kluster-komponenter

```bash
# Lista alla namespaces
kubectl get namespaces

# Inspektera kube-system namespace
kubectl get all -n kube-system

# Visa detaljerad node-info
kubectl describe node minikube

# Visa kluster-events
kubectl get events --sort-by='.lastTimestamp' -A
```

## 7. Vanliga Fel & Lösningar

### Problem 1: Minikube startar inte

```bash
# Symptom
minikube start
# Error: minikube failed to start

# Lösning 1: Rensa och starta om
minikube delete --all --purge
minikube start --driver=docker

# Lösning 2: Kontrollera Docker
docker info
systemctl status docker

# Lösning 3: Prova annan driver
minikube start --driver=virtualbox
```

### Problem 2: kubectl kan inte ansluta

```bash
# Symptom
kubectl get nodes
# The connection to the server localhost:8080 was refused

# Lösning: Sätt kubeconfig
export KUBECONFIG=~/.kube/config
minikube update-context

# Verifiera
kubectl config current-context
kubectl config view
```

## 8. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                 KUBERNETES BEST PRACTICES CHECKLISTA                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Lokalt Utveckling                                                   │
│     □ Använd Minikube eller Kind för utveckling                         │
│     □ Matcha K8s-version med produktion                                 │
│     □ Testa manifests lokalt innan deploy                               │
│     □ Använd namespace per projekt                                      │
│                                                                          │
│  ✅ Produktion                                                          │
│     □ Minst 3 control plane noder (HA)                                  │
│     □ Separera etcd på egna noder                                       │
│     □ Använd managed K8s (EKS, GKE, AKS) om möjligt                     │
│     □ Aktivera RBAC                                                     │
│     □ Sätt resource requests/limits                                     │
│     □ Implementera NetworkPolicies                                      │
│                                                                          │
│  ✅ Säkerhet                                                            │
│     □ Uppdatera K8s regelbundet                                         │
│     □ Scanna container images                                           │
│     □ Använd Pod Security Standards                                     │
│     □ Kryptera secrets at rest                                          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 9. Verkliga Scenarion

### Scenario: Migrera från VMs till Kubernetes

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     VM → KUBERNETES MIGRATION PATH                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  BEFORE (Traditional VMs)           AFTER (Kubernetes)                  │
│  ========================           ===================                  │
│                                                                          │
│  ┌─────────────────────┐           ┌─────────────────────┐              │
│  │   VM 1: Frontend    │           │    Deployment:      │              │
│  │   - nginx           │           │    frontend         │              │
│  │   - 4 CPU, 8GB RAM  │    ──▶   │    replicas: 3      │              │
│  │   - Manual scaling  │           │    autoscaling: on  │              │
│  └─────────────────────┘           └─────────────────────┘              │
│                                                                          │
│  ┌─────────────────────┐           ┌─────────────────────┐              │
│  │   VM 2: Backend     │           │    Deployment:      │              │
│  │   - node.js         │           │    backend          │              │
│  │   - 8 CPU, 16GB RAM │    ──▶   │    replicas: 5      │              │
│  │   - Load balancer   │           │    HPA: 3-10 pods   │              │
│  └─────────────────────┘           └─────────────────────┘              │
│                                                                          │
│  ┌─────────────────────┐           ┌─────────────────────┐              │
│  │   VM 3: Database    │           │    StatefulSet:     │              │
│  │   - PostgreSQL      │           │    postgres         │              │
│  │   - Backup scripts  │    ──▶   │    PV: 100Gi        │              │
│  │   - Manual failover │           │    Auto-failover    │              │
│  └─────────────────────┘           └─────────────────────┘              │
│                                                                          │
│  Benefits:                                                               │
│  • 60% cost reduction (efficient resource usage)                        │
│  • 99.99% uptime (self-healing)                                         │
│  • 5-minute deployments (was 2 hours)                                   │
│  • Instant rollback capability                                          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 10. Integration & Kopplingar

### Kubernetes i DevOps Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    KUBERNETES DEVOPS INTEGRATION                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│    Developer        CI/CD              Kubernetes      Monitoring        │
│        │              │                    │               │             │
│        │ git push     │                    │               │             │
│        ├─────────────▶│                    │               │             │
│        │              │ build & test       │               │             │
│        │              ├───────────────────▶│               │             │
│        │              │ kubectl apply      │               │             │
│        │              ├───────────────────▶│               │             │
│        │              │                    │ metrics       │             │
│        │              │                    ├──────────────▶│             │
│        │              │                    │               │             │
│        │◀─────────────┼────────────────────┼───────────────┤             │
│        │    alerts/feedback               │               │             │
│                                                                          │
│  Tools:                                                                  │
│  • GitLab CI / GitHub Actions / Jenkins                                 │
│  • ArgoCD / Flux (GitOps)                                               │
│  • Prometheus / Grafana (Monitoring)                                    │
│  • Istio / Linkerd (Service Mesh)                                       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 11. Sammanfattning

### Nyckelkoncept

| Koncept | Beskrivning | Importance |
|---------|-------------|------------|
| **Container Orchestration** | Automatiserad hantering av containers | ⭐⭐⭐⭐⭐ |
| **Declarative Config** | Önskat tillstånd i YAML | ⭐⭐⭐⭐⭐ |
| **Self-Healing** | Automatisk återstart/ersättning | ⭐⭐⭐⭐⭐ |
| **Horizontal Scaling** | Lägg till/ta bort replicas | ⭐⭐⭐⭐⭐ |
| **Service Discovery** | Automatisk DNS & load balancing | ⭐⭐⭐⭐ |
| **Rolling Updates** | Zero-downtime deployments | ⭐⭐⭐⭐ |

## 12. Nästa Steg

Efter att du förstår Kubernetes fundamentals, fortsätt med:

1. **Node 2**: kubectl Mastery - Lär dig CLI:n på djupet
2. **Node 3**: Pods - Minsta deployable unit
3. **Node 4**: Deployments - Replica management
4. **Node 5**: Services - Nätverks-abstraktioner

## 13. Praktisk Task

### Uppgift: Sätt upp ditt första K8s-kluster

```bash
# Steg 1: Installera kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Steg 2: Installera Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Steg 3: Starta kluster
minikube start --cpus=4 --memory=8192

# Steg 4: Verifiera
kubectl get nodes
kubectl get pods -A
kubectl cluster-info

# Steg 5: Deploya test-app
kubectl create deployment hello-k8s --image=nginx
kubectl expose deployment hello-k8s --port=80 --type=NodePort
minikube service hello-k8s
```

## 14. Quiz: Kubernetes Introduction

### Fråga 1
Vilken komponent lagrar klustrets tillstånd?

a) kube-apiserver
b) etcd ✓
c) kubelet
d) kube-proxy

### Fråga 2
Vad hanterar kube-scheduler?

a) Container runtime
b) Network policies
c) Pod placement på noder ✓
d) Secret encryption

### Fråga 3
Vilken komponent körs på varje worker node?

a) etcd
b) kube-scheduler
c) kubelet ✓
d) controller-manager

### Fråga 4
Vad är fördelen med declarative configuration?

a) Snabbare deployment
b) Idempotent - kan köras flera gånger ✓
c) Mindre YAML
d) Inget behov av kubectl

---

**Nästa Node:** kubectl Mastery - CLI Deep Dive →
''',
    "xp_reward": 150,
    "estimated_minutes": 60,
    "prerequisites": ["docker_node_20"],
    "learning_outcomes": [
        "Förstå varför Kubernetes behövs",
        "Kunna förklara K8s arkitektur",
        "Sätta upp lokalt utvecklingskluster",
        "Förstå Control Plane vs Worker Node"
    ]
}

NODE_2 = {
    "id": "k8s_node_2",
    "title": "kubectl Mastery - CLI Deep Dive",
    "slug": "kubectl-mastery-cli-deep-dive",
    "content": r'''# 🎯 kubectl Mastery - CLI Deep Dive

## 1. Introduktion & Kontext

kubectl (kube-control) är command-line verktyget för att interagera med Kubernetes kluster. Att behärska kubectl är fundamentalt för alla som arbetar med Kubernetes.

### Uttal & Bakgrund

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         KUBECTL PRONUNCIATION                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  "kube-control"     "kube-c-t-l"      "kube-cuddle"     "kubectl"       │
│       ↓                  ↓                 ↓               ↓             │
│  [officiellt]      [bokstaverat]      [skämt]         [vanligast]       │
│                                                                          │
│  Alla varianter är accepterade i communityn!                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Teknisk Djupdykning

### kubectl Arkitektur

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      KUBECTL ARCHITECTURE                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌─────────────┐                                                        │
│   │   kubectl   │                                                        │
│   │   command   │                                                        │
│   └──────┬──────┘                                                        │
│          │                                                               │
│          ▼                                                               │
│   ┌─────────────────────────────────────────────────┐                   │
│   │              ~/.kube/config                      │                   │
│   │  ┌─────────────────────────────────────────┐    │                   │
│   │  │ clusters:                                │    │                   │
│   │  │   - cluster:                             │    │                   │
│   │  │       server: https://192.168.49.2:8443 │    │                   │
│   │  │       certificate-authority: ca.crt      │    │                   │
│   │  │ users:                                   │    │                   │
│   │  │   - user:                                │    │                   │
│   │  │       client-certificate: client.crt    │    │                   │
│   │  │ contexts:                                │    │                   │
│   │  │   - context:                             │    │                   │
│   │  │       cluster: minikube                  │    │                   │
│   │  │       user: minikube                     │    │                   │
│   │  └─────────────────────────────────────────┘    │                   │
│   └──────────────────────┬──────────────────────────┘                   │
│                          │                                               │
│                          │ HTTPS/TLS                                    │
│                          ▼                                               │
│   ┌─────────────────────────────────────────────────┐                   │
│   │              kube-apiserver                      │                   │
│   │  ┌─────────────────────────────────────────┐    │                   │
│   │  │ 1. Authentication (certs, tokens)       │    │                   │
│   │  │ 2. Authorization (RBAC)                 │    │                   │
│   │  │ 3. Admission Control                    │    │                   │
│   │  │ 4. Validation                           │    │                   │
│   │  │ 5. Persist to etcd                      │    │                   │
│   │  └─────────────────────────────────────────┘    │                   │
│   └─────────────────────────────────────────────────┘                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Kommando-struktur

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    KUBECTL COMMAND STRUCTURE                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  kubectl  [command]  [TYPE]  [NAME]  [flags]                            │
│     │        │         │       │        │                                │
│     │        │         │       │        └── -o yaml, --namespace dev    │
│     │        │         │       └── nginx-deployment, pod/mypod          │
│     │        │         └── pods, deployments, services, nodes           │
│     │        └── get, create, apply, delete, describe, logs             │
│     └── The CLI binary                                                  │
│                                                                          │
│  Examples:                                                               │
│  kubectl get pods -n production -o wide                                 │
│  kubectl describe deployment nginx -n staging                           │
│  kubectl logs -f pod/api-server -c sidecar                              │
│  kubectl exec -it pod/debug -- /bin/bash                                │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3. Essential Commands Reference

### CRUD Operations

```bash
# CREATE - Skapa resurser
kubectl create namespace dev
kubectl create deployment nginx --image=nginx:1.24
kubectl create service clusterip nginx --tcp=80:80
kubectl create configmap config --from-literal=key=value
kubectl create secret generic db-pass --from-literal=password=secret

# READ - Läs/lista resurser
kubectl get pods                        # Lista pods
kubectl get pods -o wide               # Med mer info
kubectl get pods -o yaml               # Full YAML output
kubectl get pods -o json               # JSON output
kubectl get pods --show-labels         # Visa labels
kubectl get pods -l app=nginx          # Filter på label
kubectl get all                        # Alla resurser
kubectl get all -A                     # Alla namespaces

# UPDATE - Uppdatera resurser
kubectl apply -f deployment.yaml       # Declarative update
kubectl edit deployment nginx          # Öppna i editor
kubectl set image deploy/nginx nginx=nginx:1.25
kubectl scale deploy nginx --replicas=5
kubectl patch deploy nginx -p '{"spec":{"replicas":3}}'

# DELETE - Ta bort resurser
kubectl delete pod nginx               # Ta bort pod
kubectl delete -f deployment.yaml      # Ta bort från fil
kubectl delete pods --all              # Alla pods
kubectl delete pods -l app=nginx       # Alla med label
kubectl delete namespace dev           # Hela namespace
```

### Inspection & Debugging

```bash
# DESCRIBE - Detaljerad information
kubectl describe pod nginx
kubectl describe node worker-1
kubectl describe deployment api-server
kubectl describe service frontend

# LOGS - Container logs
kubectl logs nginx                     # Senaste logs
kubectl logs -f nginx                  # Follow/stream
kubectl logs nginx --previous          # Crashed container
kubectl logs nginx -c sidecar          # Specifik container
kubectl logs -l app=api --all-containers=true
kubectl logs nginx --since=1h          # Senaste timmen
kubectl logs nginx --tail=100          # Senaste 100 rader

# EXEC - Kör kommandon i container
kubectl exec nginx -- ls /app          # Kör kommando
kubectl exec -it nginx -- /bin/bash    # Interaktiv shell
kubectl exec nginx -c sidecar -- cat /etc/config

# DEBUG - Avancerad debugging
kubectl debug pod/nginx --image=busybox
kubectl debug node/worker-1 --image=ubuntu
kubectl run debug --image=busybox --rm -it -- sh
```

## 4. Avancerade Kommandon

### Output Formatting

```bash
# JSON/YAML Output
kubectl get pod nginx -o yaml
kubectl get pod nginx -o json
kubectl get pods -o yaml > pods.yaml

# Custom Columns
kubectl get pods -o custom-columns=NAME:.metadata.name,STATUS:.status.phase,IP:.status.podIP

# JSONPath
kubectl get pods -o jsonpath='{.items[*].metadata.name}'
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.phase}{"\n"}{end}'
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}'

# Go Template
kubectl get pods -o go-template='{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}'
```

### Sorting & Filtering

```bash
# Sort by field
kubectl get pods --sort-by=.metadata.creationTimestamp
kubectl get pods --sort-by=.status.startTime
kubectl get events --sort-by=.lastTimestamp

# Field Selectors
kubectl get pods --field-selector=status.phase=Running
kubectl get pods --field-selector=spec.nodeName=worker-1
kubectl get events --field-selector=type=Warning

# Label Selectors
kubectl get pods -l 'app=nginx'
kubectl get pods -l 'app in (nginx, apache)'
kubectl get pods -l 'app!=nginx'
kubectl get pods -l 'app,environment=production'
```

### Context & Namespace Management

```bash
# Contexts
kubectl config get-contexts                    # Lista contexts
kubectl config current-context                 # Nuvarande context
kubectl config use-context production          # Byt context
kubectl config set-context --current --namespace=dev

# Skapa ny context
kubectl config set-context dev-context \
  --cluster=minikube \
  --user=minikube \
  --namespace=development

# Namespace shortcuts
kubectl get pods -n kube-system
kubectl get pods --all-namespaces
kubectl get pods -A                            # Kort form

# Sätt default namespace
kubectl config set-context --current --namespace=production
```

## 5. Produktivitets-tricks

### Aliases & Shortcuts

```bash
# Lägg till i ~/.bashrc eller ~/.zshrc
alias k='kubectl'
alias kg='kubectl get'
alias kd='kubectl describe'
alias kaf='kubectl apply -f'
alias kdf='kubectl delete -f'
alias kl='kubectl logs'
alias ke='kubectl exec -it'

# Med namespace
alias kgp='kubectl get pods'
alias kgpa='kubectl get pods -A'
alias kgd='kubectl get deployments'
alias kgs='kubectl get services'
alias kgn='kubectl get nodes'

# Avancerade
alias kctx='kubectl config use-context'
alias kns='kubectl config set-context --current --namespace'
alias kdel='kubectl delete'
alias krun='kubectl run --rm -it --image'
```

### Bash/Zsh Completion

```bash
# Bash completion
source <(kubectl completion bash)
echo 'source <(kubectl completion bash)' >> ~/.bashrc

# Zsh completion
source <(kubectl completion zsh)
echo 'source <(kubectl completion zsh)' >> ~/.zshrc

# Completion for alias
complete -F __start_kubectl k
```

### kubectl Plugins (Krew)

```bash
# Installera Krew plugin manager
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)

export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"

# Installera plugins
kubectl krew install ctx              # Context switcher
kubectl krew install ns               # Namespace switcher
kubectl krew install neat             # Clean YAML output
kubectl krew install tree             # Resource hierarchy
kubectl krew install images           # List container images
kubectl krew install pod-logs         # Multi-pod logs

# Använd plugins
kubectl ctx production
kubectl ns staging
kubectl get pod nginx -o yaml | kubectl neat
kubectl tree deployment nginx
```

## 6. Praktiska Övningar

### Övning 1: Resource Discovery

```bash
# Lista alla API-resurser
kubectl api-resources

# Lista resurs-versioner
kubectl api-versions

# Förklara en resurs
kubectl explain pod
kubectl explain pod.spec
kubectl explain pod.spec.containers
kubectl explain deployment.spec.strategy

# Visa alla fält för en resurs
kubectl explain pod --recursive
```

### Övning 2: Imperativ vs Declarativ

```bash
# IMPERATIV - Snabba tester
kubectl run nginx --image=nginx
kubectl expose pod nginx --port=80
kubectl scale deployment nginx --replicas=3

# DECLARATIV - Production
cat << 'EOF' > nginx-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.24
        ports:
        - containerPort: 80
EOF

kubectl apply -f nginx-deployment.yaml
```

### Övning 3: Debugging Session

```bash
# Scenario: Pod startar inte
kubectl get pods
# NAME    READY   STATUS             RESTARTS   AGE
# nginx   0/1     ImagePullBackOff   0          2m

# Steg 1: Describe
kubectl describe pod nginx
# Events visar: Failed to pull image "nginx:lates" (typo)

# Steg 2: Fixa
kubectl set image pod/nginx nginx=nginx:latest

# Steg 3: Verifiera
kubectl get pods -w   # Watch mode
kubectl logs nginx
```

## 7. Vanliga Fel & Lösningar

### Fel 1: Context/kubeconfig problem

```bash
# Symptom
kubectl get pods
# error: no configuration has been provided

# Lösning
export KUBECONFIG=~/.kube/config
kubectl config view
kubectl config get-contexts

# Multiple kubeconfig files
export KUBECONFIG=~/.kube/config:~/.kube/prod-config
kubectl config get-contexts
```

### Fel 2: Permission Denied

```bash
# Symptom
kubectl get pods
# Error: pods is forbidden: User cannot list resource "pods"

# Diagnos
kubectl auth can-i get pods
kubectl auth can-i get pods --as=system:serviceaccount:default:default

# Lösning: Kontakta admin för RBAC
kubectl create rolebinding view-pods \
  --clusterrole=view \
  --serviceaccount=default:default
```

### Fel 3: Resource Not Found

```bash
# Symptom
kubectl get pods nginx
# Error: pods "nginx" not found

# Diagnos
kubectl get pods -A | grep nginx        # Kanske i annat namespace
kubectl get pods -n production          # Prova specifikt namespace
kubectl get all -l app=nginx            # Sök via label
```

## 8. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    KUBECTL BEST PRACTICES                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Kommandorad                                                         │
│     □ Använd aliaser för vanliga kommandon                              │
│     □ Aktivera shell completion                                          │
│     □ Installera krew för plugins                                       │
│     □ Använd -o wide/yaml för mer info                                  │
│                                                                          │
│  ✅ Säkerhet                                                            │
│     □ Undvik --all-namespaces i produktion                              │
│     □ Dubbelkolla context innan kubectl delete                          │
│     □ Använd dry-run för kritiska ändringar                             │
│     □ Versionshantera kubeconfig                                        │
│                                                                          │
│  ✅ Workflow                                                            │
│     □ Använd kubectl apply (declarativ) för produktion                  │
│     □ Spara manifests i Git                                             │
│     □ Använd kubectl diff innan apply                                   │
│     □ Logga kritiska kommandon                                          │
│                                                                          │
│  ✅ Debugging                                                           │
│     □ Starta med kubectl get events                                     │
│     □ Använd kubectl describe för detaljer                              │
│     □ Kör kubectl logs -f för realtidslogging                           │
│     □ Använd kubectl exec för interaktiv debug                          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 9. Verkliga Scenarion

### Scenario: Production Incident Response

```bash
# 1. Snabb överblick
kubectl get pods -A | grep -v Running
kubectl get events --sort-by='.lastTimestamp' -A | tail -20

# 2. Identifiera problematisk pod
kubectl get pods -l app=api-server -o wide
kubectl describe pod api-server-xyz

# 3. Kolla logs
kubectl logs api-server-xyz --previous   # Om crashed
kubectl logs api-server-xyz --tail=100

# 4. Resource usage
kubectl top pods
kubectl top nodes

# 5. Snabb fix (om nödvändigt)
kubectl rollout undo deployment/api-server

# 6. Verifiera
kubectl rollout status deployment/api-server
kubectl get pods -l app=api-server
```

## 10. Integration & Kopplingar

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    KUBECTL ECOSYSTEM INTEGRATION                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  kubectl ──────┬──────────────────────────────────────────────────      │
│                │                                                         │
│                ├──▶ k9s (Terminal UI)                                   │
│                │    └── Interaktiv resurshantering                      │
│                │                                                         │
│                ├──▶ Lens (Desktop UI)                                   │
│                │    └── Full IDE för Kubernetes                         │
│                │                                                         │
│                ├──▶ kubectx/kubens                                      │
│                │    └── Snabbt context/namespace-byte                   │
│                │                                                         │
│                ├──▶ stern                                               │
│                │    └── Multi-pod log tailing                           │
│                │                                                         │
│                ├──▶ kubectl plugins (krew)                              │
│                │    └── Utökad funktionalitet                           │
│                │                                                         │
│                └──▶ CI/CD Integration                                   │
│                     └── GitLab, GitHub Actions, Jenkins                 │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 11. Sammanfattning

### Kommando-kategorier

| Kategori | Kommandon | Användning |
|----------|-----------|------------|
| **CRUD** | get, create, apply, delete | Daglig hantering |
| **Debug** | describe, logs, exec | Felsökning |
| **Config** | config, context | Kluster-hantering |
| **Info** | api-resources, explain | Lärande |
| **Advanced** | patch, edit, diff | Avancerad användning |

## 12. Nästa Steg

Fortsätt med:
1. **Node 3**: Pods - K8s minsta deployment unit
2. **Node 4**: Deployments - Replica management
3. Öva kubectl dagligen!

## 13. Praktisk Task

```bash
# Övningsuppgift: kubectl mastery check

# 1. Lista alla pods i alla namespaces, sorterade efter creation time
kubectl get pods -A --sort-by=.metadata.creationTimestamp

# 2. Hitta alla pods som inte är i Running state
kubectl get pods -A --field-selector=status.phase!=Running

# 3. Exportera alla deployments i namespace "production" till YAML
kubectl get deployments -n production -o yaml > prod-deployments.yaml

# 4. Visa resource usage för alla pods
kubectl top pods -A

# 5. Skapa en temporär debug-pod
kubectl run debug --image=busybox --rm -it -- sh
```

## 14. Quiz: kubectl Mastery

### Fråga 1
Vilket kommando visar detaljerad information om en pod?

a) kubectl get pod nginx -v
b) kubectl describe pod nginx ✓
c) kubectl info pod nginx
d) kubectl show pod nginx

### Fråga 2
Hur följer man logs i realtid?

a) kubectl logs nginx --follow
b) kubectl logs -f nginx ✓
c) kubectl logs nginx --stream
d) kubectl logs nginx -r

### Fråga 3
Hur byter man namespace permanent?

a) kubectl ns production
b) kubectl use namespace production
c) kubectl config set-context --current --namespace=production ✓
d) kubectl switch namespace production

---

**Nästa Node:** Pods - K8s Minsta Deployment Unit →
''',
    "xp_reward": 145,
    "estimated_minutes": 55,
    "prerequisites": ["k8s_node_1"],
    "learning_outcomes": [
        "Behärska kubectl CRUD operationer",
        "Använda avancerad output formatting",
        "Konfigurera produktivitets-verktyg",
        "Debugga med kubectl"
    ]
}

# Block 1 Part 1 exports
BLOCK_1_PART_1_NODES = [NODE_1, NODE_2]
