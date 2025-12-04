# =============================================================================
# KUBERNETES MASTERY - BLOCK 2 PART 2: CONFIGMAPS, SECRETS & VOLUMES
# Noder 7-8 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
KUBERNETES BLOCK 2 PART 2 - CONFIGURATION & STORAGE
===================================================
Node 7: ConfigMaps & Secrets - Configuration Management
Node 8: Volumes & Persistent Storage
"""

NODE_7 = {
    "id": "k8s_node_7",
    "title": "ConfigMaps & Secrets - Configuration Management",
    "slug": "configmaps-secrets-configuration",
    "content": r'''# ⚙️ ConfigMaps & Secrets - Configuration Management

## 1. Introduktion & Kontext

ConfigMaps och Secrets är Kubernetes-resurser för att separera konfiguration från containerimages. Detta möjliggör samma image i olika miljöer (dev, staging, prod) med olika konfigurationer.

### Separation of Concerns

```
┌─────────────────────────────────────────────────────────────────────────┐
│                CONFIGURATION MANAGEMENT PRINCIPLE                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ❌ ANTI-PATTERN: Configuration i image                                 │
│  ┌──────────────────────────────────────────────────────────────┐      │
│  │                    CONTAINER IMAGE                            │      │
│  │  ┌────────────────────────────────────────────────────────┐  │      │
│  │  │  Application Code                                       │  │      │
│  │  │  + config/database.yml  ← Hårdkodad config             │  │      │
│  │  │  + .env                 ← Secrets i image! 😱          │  │      │
│  │  └────────────────────────────────────────────────────────┘  │      │
│  │  Ny image krävs för varje config-ändring                     │      │
│  └──────────────────────────────────────────────────────────────┘      │
│                                                                          │
│  ✅ BEST PRACTICE: ConfigMaps & Secrets                                 │
│  ┌──────────────────────────────────────────────────────────────┐      │
│  │                    CONTAINER IMAGE                            │      │
│  │  ┌────────────────────────────────────────────────────────┐  │      │
│  │  │  Application Code Only                                  │  │      │
│  │  │  (reads config from env/files at runtime)               │  │      │
│  │  └────────────────────────────────────────────────────────┘  │      │
│  └──────────────────────────────────────────────────────────────┘      │
│                        │                     │                          │
│                        ▼                     ▼                          │
│              ┌──────────────┐      ┌──────────────┐                    │
│              │  ConfigMap   │      │   Secret     │                    │
│              │              │      │              │                    │
│              │ DB_HOST=...  │      │ DB_PASS=...  │                    │
│              │ LOG_LEVEL=...│      │ API_KEY=...  │                    │
│              └──────────────┘      └──────────────┘                    │
│                                                                          │
│  ✅ Samma image i alla miljöer                                          │
│  ✅ Config-ändringar utan rebuild                                       │
│  ✅ Secrets hanteras separat                                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. ConfigMaps

### Skapa ConfigMaps

```bash
# Från literal values
kubectl create configmap app-config \
  --from-literal=DATABASE_HOST=postgres \
  --from-literal=LOG_LEVEL=info \
  --from-literal=CACHE_TTL=300

# Från fil
kubectl create configmap nginx-config \
  --from-file=nginx.conf

# Från directory (alla filer)
kubectl create configmap config-dir \
  --from-file=./config/

# Från env-fil
kubectl create configmap env-config \
  --from-env-file=app.env
```

### ConfigMap YAML

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: production
data:
  # Key-value pairs
  DATABASE_HOST: "postgres.production.svc"
  LOG_LEVEL: "info"
  CACHE_TTL: "300"

  # Multi-line config file
  app.properties: |
    server.port=8080
    server.timeout=30
    feature.flag.enabled=true

  # JSON config
  config.json: |
    {
      "database": {
        "host": "postgres",
        "port": 5432
      },
      "cache": {
        "enabled": true,
        "ttl": 300
      }
    }

  # YAML config
  settings.yaml: |
    logging:
      level: info
      format: json
    metrics:
      enabled: true
      port: 9090
```

### Använda ConfigMaps

#### Som Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
    - name: app
      image: myapp:v1

      # Enskilda env vars
      env:
        - name: DB_HOST
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: DATABASE_HOST

        - name: LOG_LEVEL
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: LOG_LEVEL
              optional: true        # Crashar inte om saknas

      # Alla keys som env vars
      envFrom:
        - configMapRef:
            name: app-config
            optional: false
        - prefix: APP_             # Prefix på alla keys
          configMapRef:
            name: app-config
```

#### Som Volym-mount

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
    - name: app
      image: myapp:v1
      volumeMounts:
        # Hela ConfigMap som directory
        - name: config-volume
          mountPath: /etc/config
          readOnly: true

        # Specifik fil
        - name: config-volume
          mountPath: /etc/app/app.properties
          subPath: app.properties
          readOnly: true

  volumes:
    - name: config-volume
      configMap:
        name: app-config
        # Valfritt: specifika items
        items:
          - key: app.properties
            path: app.properties
          - key: config.json
            path: config.json
        # Valfritt: file permissions
        defaultMode: 0644
```

## 3. Secrets

### Secret Types

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         SECRET TYPES                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Type                          │ Användning                             │
│  ─────────────────────────────┼────────────────────────────────────── │
│  Opaque                        │ Generiska secrets (default)           │
│  kubernetes.io/service-account │ ServiceAccount tokens                 │
│  kubernetes.io/dockerconfigjson│ Docker registry credentials          │
│  kubernetes.io/tls             │ TLS certificates                      │
│  kubernetes.io/basic-auth      │ Basic authentication                  │
│  kubernetes.io/ssh-auth        │ SSH keys                              │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Skapa Secrets

```bash
# Generisk secret
kubectl create secret generic db-secret \
  --from-literal=username=admin \
  --from-literal=password='S3cr3t!Pass'

# Från fil
kubectl create secret generic ssl-cert \
  --from-file=tls.crt \
  --from-file=tls.key

# Docker registry secret
kubectl create secret docker-registry regcred \
  --docker-server=registry.example.com \
  --docker-username=user \
  --docker-password=pass \
  --docker-email=user@example.com

# TLS secret
kubectl create secret tls app-tls \
  --cert=path/to/tls.crt \
  --key=path/to/tls.key
```

### Secret YAML

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
  namespace: production
type: Opaque
data:
  # Base64-encoded values
  username: YWRtaW4=              # echo -n 'admin' | base64
  password: UzNjcjN0IVBhc3M=      # echo -n 'S3cr3t!Pass' | base64

stringData:
  # Plaintext (konverteras till base64 automatiskt)
  api-key: my-api-key-12345
  config.yaml: |
    database:
      host: postgres
      port: 5432
```

### Använda Secrets

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
    - name: app
      image: myapp:v1

      # Som environment variables
      env:
        - name: DB_USERNAME
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: username

        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password

      # Alla secrets som env vars
      envFrom:
        - secretRef:
            name: db-secret

      # Som volym
      volumeMounts:
        - name: secrets
          mountPath: /etc/secrets
          readOnly: true

  # Image pull secret
  imagePullSecrets:
    - name: regcred

  volumes:
    - name: secrets
      secret:
        secretName: db-secret
        defaultMode: 0400         # Restriktiva permissions
```

## 4. Praktiska Övningar

### Övning 1: Komplett Config Setup

```bash
# Skapa ConfigMap
cat << 'EOF' | kubectl apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: webapp-config
data:
  APP_ENV: production
  LOG_LEVEL: info
  nginx.conf: |
    server {
        listen 80;
        location / {
            proxy_pass http://localhost:8080;
        }
    }
EOF

# Skapa Secret
cat << 'EOF' | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: webapp-secrets
type: Opaque
stringData:
  DB_PASSWORD: super-secret-password
  API_KEY: api-key-12345
EOF

# Skapa Pod som använder båda
cat << 'EOF' | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: webapp
spec:
  containers:
    - name: app
      image: nginx
      envFrom:
        - configMapRef:
            name: webapp-config
        - secretRef:
            name: webapp-secrets
      volumeMounts:
        - name: nginx-config
          mountPath: /etc/nginx/conf.d
  volumes:
    - name: nginx-config
      configMap:
        name: webapp-config
        items:
          - key: nginx.conf
            path: default.conf
EOF

# Verifiera
kubectl exec webapp -- env | grep -E "(APP_|LOG_|DB_|API_)"
kubectl exec webapp -- cat /etc/nginx/conf.d/default.conf
```

### Övning 2: Hot Reload med ConfigMaps

```yaml
# ConfigMap med annotation för reload
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  annotations:
    reloader.stakater.com/match: "true"   # Om Reloader installerad
data:
  settings.json: |
    {"feature_enabled": true}
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
  annotations:
    configmap.reloader.stakater.com/reload: "app-config"
spec:
  template:
    spec:
      containers:
        - name: app
          volumeMounts:
            - name: config
              mountPath: /etc/config
      volumes:
        - name: config
          configMap:
            name: app-config
```

## 5. Vanliga Fel & Lösningar

### ConfigMap/Secret Not Found

```bash
# Symptom
kubectl describe pod app
# Warning  Failed  ConfigMap "app-config" not found

# Lösning
kubectl get configmap app-config     # Finns den?
kubectl get configmap -A | grep app  # Rätt namespace?

# Skapa om saknas
kubectl create configmap app-config --from-literal=key=value
```

### Base64 Encoding Errors

```bash
# Fel: Invalid base64
# Orsak: Newline i encoded string

# Rätt sätt att koda
echo -n 'mypassword' | base64       # -n för att undvika newline

# Verifiera
echo 'bXlwYXNzd29yZA==' | base64 -d
```

## 6. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│               CONFIGMAPS & SECRETS BEST PRACTICES                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ ConfigMaps                                                          │
│     □ Använd för icke-känslig konfiguration                             │
│     □ Organisera per applikation/miljö                                  │
│     □ Versionera i Git                                                  │
│     □ Använd immutable: true för stabila configs                        │
│                                                                          │
│  ✅ Secrets                                                             │
│     □ ALDRIG commita i Git                                              │
│     □ Använd externa secret managers (Vault, AWS SM)                    │
│     □ Aktivera encryption at rest                                       │
│     □ Begränsa access med RBAC                                          │
│     □ Rotera secrets regelbundet                                        │
│                                                                          │
│  ✅ Gemensamt                                                           │
│     □ Använd readOnly: true på volume mounts                            │
│     □ Sätt restriktiva file permissions                                 │
│     □ Undvik envFrom om möjligt (explicit är bättre)                    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 7. External Secret Management

### HashiCorp Vault Integration

```yaml
# External Secrets Operator
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: vault-secret
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: vault-backend
    kind: ClusterSecretStore
  target:
    name: db-credentials
  data:
    - secretKey: username
      remoteRef:
        key: secret/data/db
        property: username
    - secretKey: password
      remoteRef:
        key: secret/data/db
        property: password
```

## 8-14. Sammanfattning & Task

### Comparison

| Aspekt | ConfigMap | Secret |
|--------|-----------|--------|
| **Data** | Non-sensitive | Sensitive |
| **Encoding** | Plain text | Base64 |
| **Size limit** | 1 MB | 1 MB |
| **Git** | ✅ Version control | ❌ Never commit |

### Praktisk Task

```bash
# 1. Skapa ConfigMap med app-settings
# 2. Skapa Secret med credentials
# 3. Deploya app som använder båda
# 4. Verifiera att config läses korrekt
```

---

**Nästa Node:** Volumes & Persistent Storage →
''',
    "xp_reward": 150,
    "estimated_minutes": 50,
    "prerequisites": ["k8s_node_6"],
    "learning_outcomes": [
        "Förstå ConfigMaps och Secrets",
        "Använda config som env och volumes",
        "Hantera känslig data säkert",
        "Implementera external secrets"
    ]
}

NODE_8 = {
    "id": "k8s_node_8",
    "title": "Volumes & Persistent Storage",
    "slug": "volumes-persistent-storage",
    "content": r'''# 💾 Volumes & Persistent Storage

## 1. Introduktion & Kontext

Containers är efemära - data försvinner när containern startas om. Kubernetes Volumes löser detta genom att tillhandahålla persistent storage som överlever container-restarts och kan delas mellan containers.

### Storage Challenge

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    THE PERSISTENT STORAGE PROBLEM                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  UTAN VOLUMES:                                                           │
│  ┌────────────────────────────────────────────────────────────────┐    │
│  │  Pod                                                            │    │
│  │  ┌──────────────────────────────────────────────────────────┐  │    │
│  │  │  Container                                                │  │    │
│  │  │  ┌────────────────────────────────────────────────────┐  │  │    │
│  │  │  │  /data  ← Data lagras här                          │  │  │    │
│  │  │  │         ← Container restarts = DATA BORTA 💥       │  │  │    │
│  │  │  └────────────────────────────────────────────────────┘  │  │    │
│  │  └──────────────────────────────────────────────────────────┘  │    │
│  └────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  MED VOLUMES:                                                            │
│  ┌────────────────────────────────────────────────────────────────┐    │
│  │  Pod                                                            │    │
│  │  ┌──────────────────────────────────────────────────────────┐  │    │
│  │  │  Container                                                │  │    │
│  │  │  ┌────────────────────────────────────────────────────┐  │  │    │
│  │  │  │  /data  ← Mounted volume                           │  │  │    │
│  │  │  └────────────────────────────────────────────────────┘  │  │    │
│  │  └────────────────────────────┬─────────────────────────────┘  │    │
│  │                               │                                 │    │
│  │  ┌────────────────────────────▼─────────────────────────────┐  │    │
│  │  │                     VOLUME                                │  │    │
│  │  │  • emptyDir: Pod-livstid                                 │  │    │
│  │  │  • hostPath: Node-livstid                                │  │    │
│  │  │  • PVC: Cluster-livstid ✅                               │  │    │
│  │  └──────────────────────────────────────────────────────────┘  │    │
│  └────────────────────────────────────────────────────────────────┘    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Volume Types

### EmptyDir

```yaml
# Skapas när pod startar, raderas när pod tas bort
apiVersion: v1
kind: Pod
metadata:
  name: shared-volume-pod
spec:
  containers:
    - name: writer
      image: busybox
      command: ['sh', '-c', 'while true; do date >> /data/log.txt; sleep 5; done']
      volumeMounts:
        - name: shared-data
          mountPath: /data

    - name: reader
      image: busybox
      command: ['sh', '-c', 'tail -f /data/log.txt']
      volumeMounts:
        - name: shared-data
          mountPath: /data

  volumes:
    - name: shared-data
      emptyDir: {}              # Skapas på node disk

    # Eller i minne (snabbare men använder RAM)
    - name: cache
      emptyDir:
        medium: Memory
        sizeLimit: 100Mi
```

### HostPath

```yaml
# Monterar katalog från node
apiVersion: v1
kind: Pod
metadata:
  name: hostpath-pod
spec:
  containers:
    - name: app
      image: nginx
      volumeMounts:
        - name: host-data
          mountPath: /data

  volumes:
    - name: host-data
      hostPath:
        path: /var/data         # Path på noden
        type: DirectoryOrCreate # Skapa om inte finns
```

### PersistentVolumeClaim

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pvc-pod
spec:
  containers:
    - name: app
      image: postgres:15
      volumeMounts:
        - name: postgres-data
          mountPath: /var/lib/postgresql/data

  volumes:
    - name: postgres-data
      persistentVolumeClaim:
        claimName: postgres-pvc   # Refererar till PVC
```

## 3. Persistent Volumes Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  PERSISTENT VOLUMES ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                         APPLICATION                               │  │
│  │                            POD                                    │  │
│  │  ┌──────────────────────────────────────────────────────────┐    │  │
│  │  │  volumeMounts:                                            │    │  │
│  │  │    - name: data                                           │    │  │
│  │  │      mountPath: /data                                     │    │  │
│  │  └──────────────────────────────────────────────────────────┘    │  │
│  │                              │                                    │  │
│  │                              ▼                                    │  │
│  │  ┌──────────────────────────────────────────────────────────┐    │  │
│  │  │  volumes:                                                 │    │  │
│  │  │    - name: data                                           │    │  │
│  │  │      persistentVolumeClaim:                               │    │  │
│  │  │        claimName: app-pvc                                 │    │  │
│  │  └──────────────────────────────────────────────────────────┘    │  │
│  └─────────────────────────────────┬────────────────────────────────┘  │
│                                    │                                    │
│                                    │ Binds to                          │
│                                    ▼                                    │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │               PERSISTENTVOLUMECLAIM (PVC)                         │  │
│  │  ┌──────────────────────────────────────────────────────────┐    │  │
│  │  │  name: app-pvc                                            │    │  │
│  │  │  accessModes: ReadWriteOnce                               │    │  │
│  │  │  resources.requests.storage: 10Gi                         │    │  │
│  │  │  storageClassName: standard                               │    │  │
│  │  └──────────────────────────────────────────────────────────┘    │  │
│  └─────────────────────────────────┬────────────────────────────────┘  │
│                                    │                                    │
│                                    │ Binds to                          │
│                                    ▼                                    │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                  PERSISTENTVOLUME (PV)                            │  │
│  │  ┌──────────────────────────────────────────────────────────┐    │  │
│  │  │  name: pv-001                                             │    │  │
│  │  │  capacity.storage: 10Gi                                   │    │  │
│  │  │  accessModes: ReadWriteOnce                               │    │  │
│  │  │  storageClassName: standard                               │    │  │
│  │  │  hostPath/nfs/awsElasticBlockStore/etc                    │    │  │
│  │  └──────────────────────────────────────────────────────────┘    │  │
│  └─────────────────────────────────┬────────────────────────────────┘  │
│                                    │                                    │
│                                    │ Provisions                        │
│                                    ▼                                    │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                      PHYSICAL STORAGE                             │  │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐    │  │
│  │  │  AWS EBS   │ │ GCP PD    │ │   NFS      │ │  Ceph      │    │  │
│  │  │  Volume    │ │ Volume    │ │   Share    │ │  Block     │    │  │
│  │  └────────────┘ └────────────┘ └────────────┘ └────────────┘    │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 4. PersistentVolume & PersistentVolumeClaim

### Manuell PV Provisioning

```yaml
# 1. Admin skapar PersistentVolume
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-database
  labels:
    type: ssd
spec:
  capacity:
    storage: 100Gi

  accessModes:
    - ReadWriteOnce           # En node kan mounta read-write

  persistentVolumeReclaimPolicy: Retain    # Behåll data efter unbind

  storageClassName: manual

  # Storage backend (välj en)
  hostPath:
    path: /mnt/data

  # Eller NFS
  # nfs:
  #   server: nfs-server.example.com
  #   path: /exports/data

  # Eller AWS EBS
  # awsElasticBlockStore:
  #   volumeID: vol-xxx
  #   fsType: ext4
---
# 2. User skapar PersistentVolumeClaim
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: database-pvc
spec:
  accessModes:
    - ReadWriteOnce

  resources:
    requests:
      storage: 50Gi           # Kan vara mindre än PV

  storageClassName: manual

  selector:                   # Valfritt: matcha specifik PV
    matchLabels:
      type: ssd
```

### Dynamic Provisioning med StorageClass

```yaml
# 1. StorageClass definieras (ofta av kluster-admin)
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: kubernetes.io/aws-ebs    # eller pd.csi.storage.gke.io
parameters:
  type: gp3                           # AWS EBS type
  iops: "3000"
  throughput: "125"
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
---
# 2. User skapar PVC - PV skapas automatiskt!
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: dynamic-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: fast-ssd
  resources:
    requests:
      storage: 20Gi
```

## 5. Access Modes

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          ACCESS MODES                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Mode               │ Abbrev │ Description                              │
│  ───────────────────┼────────┼──────────────────────────────────────── │
│  ReadWriteOnce      │ RWO    │ En node kan mounta read-write           │
│  ReadOnlyMany       │ ROX    │ Flera nodes kan mounta read-only        │
│  ReadWriteMany      │ RWX    │ Flera nodes kan mounta read-write       │
│  ReadWriteOncePod   │ RWOP   │ En pod kan mounta read-write (K8s 1.22+)│
│                                                                          │
│  Storage Support:                                                        │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Storage Type    │ RWO │ ROX │ RWX │                           │   │
│  │  ────────────────┼─────┼─────┼─────┤                           │   │
│  │  AWS EBS         │  ✅ │  ❌ │  ❌ │                           │   │
│  │  GCP PD          │  ✅ │  ✅ │  ❌ │                           │   │
│  │  Azure Disk      │  ✅ │  ❌ │  ❌ │                           │   │
│  │  NFS             │  ✅ │  ✅ │  ✅ │                           │   │
│  │  Ceph RBD        │  ✅ │  ✅ │  ❌ │                           │   │
│  │  CephFS          │  ✅ │  ✅ │  ✅ │                           │   │
│  │  AWS EFS         │  ✅ │  ✅ │  ✅ │                           │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 6. Praktiska Övningar

### Övning 1: PostgreSQL med Persistent Storage

```bash
cat << 'EOF' | kubectl apply -f -
# StorageClass (om inte finns)
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-storage
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
---
# PersistentVolume
apiVersion: v1
kind: PersistentVolume
metadata:
  name: postgres-pv
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-storage
  hostPath:
    path: /tmp/postgres-data
    type: DirectoryOrCreate
---
# PersistentVolumeClaim
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: local-storage
  resources:
    requests:
      storage: 5Gi
---
# PostgreSQL Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
        - name: postgres
          image: postgres:15
          env:
            - name: POSTGRES_PASSWORD
              value: mysecretpassword
            - name: PGDATA
              value: /var/lib/postgresql/data/pgdata
          ports:
            - containerPort: 5432
          volumeMounts:
            - name: postgres-storage
              mountPath: /var/lib/postgresql/data
      volumes:
        - name: postgres-storage
          persistentVolumeClaim:
            claimName: postgres-pvc
EOF

# Verifiera
kubectl get pv,pvc
kubectl get pods
kubectl exec -it deploy/postgres -- psql -U postgres -c "CREATE TABLE test(id int);"
```

### Övning 2: Volume Expansion

```bash
# Aktivera expansion i StorageClass
kubectl patch storageclass standard -p '{"allowVolumeExpansion": true}'

# Expandera PVC
kubectl patch pvc postgres-pvc -p '{"spec":{"resources":{"requests":{"storage":"10Gi"}}}}'

# Verifiera
kubectl get pvc postgres-pvc
```

## 7. Vanliga Fel & Lösningar

### PVC Stuck in Pending

```bash
# Symptom
kubectl get pvc
# NAME          STATUS    VOLUME   CAPACITY   ACCESS MODES   AGE
# my-pvc        Pending                                       5m

# Diagnos
kubectl describe pvc my-pvc

# Vanliga orsaker:
# 1. Ingen matchande PV
kubectl get pv

# 2. StorageClass finns inte
kubectl get storageclass

# 3. Kapacitet matchar inte
# PVC requests 100Gi men PV har bara 50Gi
```

### Volume Mount Permission Denied

```bash
# Symptom: Container kan inte skriva till volym

# Lösning 1: Sätt fsGroup i securityContext
spec:
  securityContext:
    fsGroup: 1000

# Lösning 2: Init container som fixar permissions
initContainers:
  - name: fix-permissions
    image: busybox
    command: ['sh', '-c', 'chown -R 1000:1000 /data']
    volumeMounts:
      - name: data
        mountPath: /data
```

## 8. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    STORAGE BEST PRACTICES                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Provisioning                                                        │
│     □ Använd dynamic provisioning med StorageClass                      │
│     □ Aktivera allowVolumeExpansion                                     │
│     □ Sätt WaitForFirstConsumer för bättre scheduling                  │
│                                                                          │
│  ✅ Data Protection                                                     │
│     □ Använd Retain reclaim policy för viktig data                      │
│     □ Implementera backup-strategi                                      │
│     □ Testa disaster recovery                                           │
│                                                                          │
│  ✅ Performance                                                         │
│     □ Välj rätt storage type (SSD vs HDD)                               │
│     □ Sätt IOPS/throughput baserat på workload                          │
│     □ Använd ReadWriteOncePod för exklusiv access                       │
│                                                                          │
│  ✅ Multi-tenancy                                                       │
│     □ ResourceQuotas för storage per namespace                          │
│     □ LimitRanges för PVC storlek                                       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 9-14. Sammanfattning & Task

### Volume Types Comparison

| Type | Livstid | Use Case |
|------|---------|----------|
| **emptyDir** | Pod | Temp data, cache |
| **hostPath** | Node | Node-level data |
| **PVC** | Cluster | Databases, persistent apps |
| **ConfigMap** | Cluster | Config files |
| **Secret** | Cluster | Sensitive config |

### Praktisk Task

```bash
# Skapa en komplett persistent setup:
# 1. StorageClass
# 2. PVC
# 3. Deployment med mounted volume
# 4. Verifiera data persistence genom pod restart
```

---

**Nästa Node:** StatefulSets - Stateful Applications →
''',
    "xp_reward": 155,
    "estimated_minutes": 60,
    "prerequisites": ["k8s_node_7"],
    "learning_outcomes": [
        "Förstå Kubernetes volume types",
        "Implementera PV och PVC",
        "Konfigurera StorageClass",
        "Hantera persistent data"
    ]
}

# Block 2 Part 2 exports
BLOCK_2_PART_2_NODES = [NODE_7, NODE_8]
