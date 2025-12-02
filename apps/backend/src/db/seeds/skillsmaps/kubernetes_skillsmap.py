# =============================================================================
# KUBERNETES SKILLSMAP - 20 NODER
# Akhilesh Pedagogical Style: Intro → Koncept → Kommandon → Tips → Task
# =============================================================================

KUBERNETES_SKILLSMAP_INFO = {
    "name": "Kubernetes Mastery",
    "slug": "kubernetes-mastery",
    "description": "Behärska container orchestration från pods till produktion",
    "total_nodes": 20,
    "estimated_hours": 30,
    "difficulty": "advanced",
    "prerequisites": ["docker-mastery"],
    "skills": ["Kubernetes", "Pods", "Services", "Deployments", "Helm", "Networking"],
}


# =============================================================================
# BLOCK 1: K8S FUNDAMENTALS (Noder 1-4)
# =============================================================================

NODE_01_K8S_INTRO = {
    "node_id": 1,
    "title": "Kubernetes Introduktion",
    "slug": "k8s-intro",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "prerequisites": [],
    "content": '''
# Kubernetes Introduktion

Kubernetes (K8s) är industristandard för container orchestration.

## Varför Kubernetes?

| Behov | K8s Lösning |
|-------|-------------|
| Skalning | Auto-scaling |
| High Availability | Self-healing |
| Load Balancing | Services |
| Zero-downtime | Rolling updates |
| Secret Management | Secrets/ConfigMaps |

## Arkitektur

```
┌─────────────────────────────────────────┐
│            Control Plane                │
├─────────┬─────────┬─────────┬──────────┤
│ API     │ etcd    │Scheduler│Controller│
│ Server  │         │         │ Manager  │
└────┬────┴────┬────┴────┬────┴────┬─────┘
     │         │         │         │
┌────▼────┬────▼────┬────▼────┬────▼─────┐
│ Node 1  │ Node 2  │ Node 3  │ Node N   │
├─────────┼─────────┼─────────┼──────────┤
│ kubelet │ kubelet │ kubelet │ kubelet  │
│ pods    │ pods    │ pods    │ pods     │
└─────────┴─────────┴─────────┴──────────┘
```

## Lokalt Kluster

```bash
# Minikube
minikube start
minikube dashboard

# Kind (K8s in Docker)
kind create cluster

# Docker Desktop
# Aktivera Kubernetes i settings

# Verifiera
kubectl cluster-info
kubectl get nodes
```

**Nästa steg:** Node 2 - kubectl Basics
''',
}

NODE_02_KUBECTL_BASICS = {
    "node_id": 2,
    "title": "kubectl Basics",
    "slug": "kubectl-basics",
    "estimated_minutes": 45,
    "xp_reward": 110,
    "prerequisites": [1],
    "content": '''
# kubectl Basics

CLI-verktyget för Kubernetes.

## Grundläggande Kommandon

```bash
# Cluster info
kubectl cluster-info
kubectl get nodes

# Lista resurser
kubectl get pods
kubectl get services
kubectl get deployments
kubectl get all

# Alla namespaces
kubectl get pods -A
kubectl get pods --all-namespaces
```

## Skapa Resurser

```bash
# Imperativt
kubectl run nginx --image=nginx
kubectl create deployment web --image=nginx

# Deklarativt (rekommenderat)
kubectl apply -f deployment.yaml

# Från URL
kubectl apply -f https://example.com/manifest.yaml
```

## Inspektera

```bash
# Describe
kubectl describe pod nginx
kubectl describe node node1

# Logs
kubectl logs mypod
kubectl logs -f mypod         # Follow
kubectl logs mypod -c mycontainer  # Specifik container

# Exec
kubectl exec -it mypod -- bash
kubectl exec mypod -- ls /app
```

## Kontext & Namespace

```bash
# Byt namespace
kubectl config set-context --current --namespace=dev

# Lista contexts
kubectl config get-contexts

# Byt context
kubectl config use-context production
```

| Kommando | Beskrivning |
|----------|-------------|
| get | Lista resurser |
| describe | Detaljerad info |
| apply | Skapa/uppdatera |
| delete | Ta bort |
| logs | Container logs |
| exec | Kör kommando |

**Nästa steg:** Node 3 - Pods
''',
}

NODE_03_PODS = {
    "node_id": 3,
    "title": "Pods",
    "slug": "pods",
    "estimated_minutes": 55,
    "xp_reward": 130,
    "prerequisites": [2],
    "content": '''
# Pods

Pods är minsta deployable unit.

## Pod YAML

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
  labels:
    app: myapp
spec:
  containers:
    - name: app
      image: nginx:1.24
      ports:
        - containerPort: 80
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"
```

## Skapa & Hantera

```bash
# Skapa pod
kubectl apply -f pod.yaml

# Status
kubectl get pods
kubectl get pod myapp -o wide
kubectl get pod myapp -o yaml

# Ta bort
kubectl delete pod myapp
kubectl delete -f pod.yaml
```

## Multi-container Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi
spec:
  containers:
    - name: app
      image: myapp
      ports:
        - containerPort: 8080
    - name: sidecar
      image: fluentd
      volumeMounts:
        - name: logs
          mountPath: /var/log
  volumes:
    - name: logs
      emptyDir: {}
```

## Pod Lifecycle

```
Pending → Running → Succeeded/Failed
              ↓
          CrashLoopBackOff
```

| State | Beskrivning |
|-------|-------------|
| Pending | Väntar på scheduling |
| Running | Kör |
| Succeeded | Avslutad OK |
| Failed | Avslutad med fel |
| Unknown | Node-kommunikation borta |

**Nästa steg:** Node 4 - Deployments
''',
}

NODE_04_DEPLOYMENTS = {
    "node_id": 4,
    "title": "Deployments",
    "slug": "deployments",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "prerequisites": [3],
    "content": '''
# Deployments

Deklarativ pod-hantering med replicas.

## Deployment YAML

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: app
          image: myapp:v1
          ports:
            - containerPort: 8080
```

## Hantera Deployments

```bash
# Skapa
kubectl apply -f deployment.yaml

# Skala
kubectl scale deployment myapp --replicas=5

# Uppdatera image
kubectl set image deployment/myapp app=myapp:v2

# Rollout status
kubectl rollout status deployment/myapp

# Historia
kubectl rollout history deployment/myapp

# Rollback
kubectl rollout undo deployment/myapp
kubectl rollout undo deployment/myapp --to-revision=2
```

## Update Strategy

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # Extra pods under update
      maxUnavailable: 0  # Alltid min replicas
```

## ReplicaSet

```bash
# Deployment skapar ReplicaSet
kubectl get rs

# ReplicaSet hanterar Pods
kubectl get pods -l app=myapp
```

| Strategy | Beskrivning |
|----------|-------------|
| RollingUpdate | Gradvis ersättning |
| Recreate | Stoppa alla, starta nya |

**Nästa steg:** Node 5 - Services
''',
}

KUBERNETES_SKILLSMAP_BLOCK_1 = [
    NODE_01_K8S_INTRO,
    NODE_02_KUBECTL_BASICS,
    NODE_03_PODS,
    NODE_04_DEPLOYMENTS,
]

# Block 2-5 kommer i nästa commits
