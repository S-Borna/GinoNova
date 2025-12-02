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


# =============================================================================
# BLOCK 2: SERVICES & NETWORKING (Noder 5-8)
# =============================================================================

NODE_05_SERVICES = {
    "node_id": 5,
    "title": "Services",
    "slug": "services",
    "estimated_minutes": 55,
    "xp_reward": 145,
    "prerequisites": [4],
    "content": '''
# Kubernetes Services

Stabil nätverksendpoint för pods.

## Service Types

```yaml
# ClusterIP (default) - Intern åtkomst
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080
  type: ClusterIP
```

## NodePort

```yaml
# NodePort - Extern via node IP
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30080
  type: NodePort
```

## LoadBalancer

```yaml
# LoadBalancer - Cloud LB
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
  ports:
    - port: 80
      targetPort: 8080
  type: LoadBalancer
```

## Service DNS

```bash
# DNS format
<service>.<namespace>.svc.cluster.local

# Exempel
myapp.default.svc.cluster.local
myapp.default    # Kortform
myapp            # Samma namespace
```

| Type | Åtkomst |
|------|---------|
| ClusterIP | Endast internt |
| NodePort | nodeIP:nodePort |
| LoadBalancer | Extern IP |
| ExternalName | DNS alias |

**Nästa steg:** Node 6 - Ingress
''',
}

NODE_06_INGRESS = {
    "node_id": 6,
    "title": "Ingress",
    "slug": "ingress",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [5],
    "content": '''
# Ingress

HTTP/S routing till services.

## Ingress Controller

```bash
# Installera NGINX Ingress
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml

# Verifiera
kubectl get pods -n ingress-nginx
```

## Basic Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp
spec:
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: myapp
                port:
                  number: 80
```

## Path-based Routing

```yaml
spec:
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /api/v1
            pathType: Prefix
            backend:
              service:
                name: api-v1
                port:
                  number: 80
          - path: /api/v2
            pathType: Prefix
            backend:
              service:
                name: api-v2
                port:
                  number: 80
```

## TLS

```yaml
spec:
  tls:
    - hosts:
        - myapp.example.com
      secretName: myapp-tls
  rules:
    - host: myapp.example.com
```

```bash
# Skapa TLS secret
kubectl create secret tls myapp-tls \\
  --cert=tls.crt \\
  --key=tls.key
```

**Nästa steg:** Node 7 - ConfigMaps & Secrets
''',
}

NODE_07_CONFIGMAPS_SECRETS = {
    "node_id": 7,
    "title": "ConfigMaps & Secrets",
    "slug": "configmaps-secrets",
    "estimated_minutes": 50,
    "xp_reward": 140,
    "prerequisites": [6],
    "content": '''
# ConfigMaps & Secrets

Konfigurations- och hemlighetshantering.

## ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_HOST: postgres
  LOG_LEVEL: info
  config.json: |
    {"feature": true}
```

```bash
# Skapa från fil
kubectl create configmap app-config --from-file=config.json

# Från literals
kubectl create configmap app-config --from-literal=LOG_LEVEL=debug
```

## Secrets

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  password: cGFzc3dvcmQxMjM=  # base64
stringData:
  username: admin  # Klartext (konverteras)
```

```bash
# Skapa secret
kubectl create secret generic db-secret \\
  --from-literal=password=secret123
```

## Använda i Pod

```yaml
spec:
  containers:
    - name: app
      env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
        - name: LOG_LEVEL
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: LOG_LEVEL
      envFrom:
        - configMapRef:
            name: app-config
      volumeMounts:
        - name: config
          mountPath: /etc/config
  volumes:
    - name: config
      configMap:
        name: app-config
```

**Nästa steg:** Node 8 - Volumes & Storage
''',
}

NODE_08_VOLUMES_STORAGE = {
    "node_id": 8,
    "title": "Volumes & Storage",
    "slug": "volumes-storage",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [7],
    "content": '''
# Kubernetes Volumes & Storage

Persistent data i K8s.

## EmptyDir

```yaml
spec:
  containers:
    - name: app
      volumeMounts:
        - name: cache
          mountPath: /cache
  volumes:
    - name: cache
      emptyDir: {}
```

## PersistentVolume & Claim

```yaml
# PersistentVolume
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-data
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: standard
  hostPath:
    path: /data

---
# PersistentVolumeClaim
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard
```

## Använda PVC

```yaml
spec:
  containers:
    - name: app
      volumeMounts:
        - name: data
          mountPath: /data
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: app-data
```

## StorageClass

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
reclaimPolicy: Delete
allowVolumeExpansion: true
```

| Access Mode | Beskrivning |
|-------------|-------------|
| ReadWriteOnce | En node r/w |
| ReadOnlyMany | Flera nodes ro |
| ReadWriteMany | Flera nodes r/w |

**Nästa steg:** Node 9 - StatefulSets
''',
}

KUBERNETES_SKILLSMAP_BLOCK_2 = [
    NODE_05_SERVICES,
    NODE_06_INGRESS,
    NODE_07_CONFIGMAPS_SECRETS,
    NODE_08_VOLUMES_STORAGE,
]

# Block 3-5 kommer i nästa commits
