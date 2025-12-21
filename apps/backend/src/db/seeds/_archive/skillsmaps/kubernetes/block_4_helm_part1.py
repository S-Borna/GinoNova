# =============================================================================
# KUBERNETES MASTERY - BLOCK 4 PART 1: HELM BASICS & CHARTS
# Noder 13-14 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
KUBERNETES BLOCK 4 PART 1 - HELM PACKAGE MANAGEMENT
====================================================
Node 13: Helm Basics - Package Manager
Node 14: Helm Charts - Creating Custom Charts
"""

NODE_13 = {
    "id": "k8s_node_13",
    "title": "Helm Basics - Package Manager",
    "slug": "helm-basics-package-manager",
    "content": r'''# 📦 Helm Basics - Kubernetes Package Manager

## 1. Introduktion & Kontext

Helm är "apt/yum för Kubernetes". Det gör det enkelt att paketera, distribuera och versionshantera Kubernetes-applikationer via Charts - förkonfigurerade paket av K8s-resurser.

### Varför Helm?

```
+-------------------------------------------------------------------------+
|                      UTAN HELM VS MED HELM                               |
+-------------------------------------------------------------------------+
|                                                                          |
|  UTAN HELM (kubectl apply)                                               |
|  +-----------------------------------------------------------------+   |
|  |  Problem:                                                        |   |
|  |  • Manuell hantering av 10+ YAML-filer per app                  |   |
|  |  • Copy-paste för varje miljö (dev/staging/prod)                |   |
|  |  • Ingen versionering                                           |   |
|  |  • Svårt att rollback                                           |   |
|  |  • Ingen dependency management                                   |   |
|  |                                                                  |   |
|  |  deployment.yaml    service.yaml    configmap.yaml               |   |
|  |  secret.yaml        ingress.yaml    pdb.yaml                    |   |
|  |  hpa.yaml           serviceaccount.yaml   networkpolicy.yaml    |   |
|  |       |                  |                      |                |   |
|  |       +------------------+----------------------+                |   |
|  |                          |                                       |   |
|  |                    kubectl apply -f .                            |   |
|  +-----------------------------------------------------------------+   |
|                                                                          |
|  MED HELM                                                                |
|  +-----------------------------------------------------------------+   |
|  |  Fördelar:                                                       |   |
|  |  • En command för hela applikationen                            |   |
|  |  • Versionering och rollback                                    |   |
|  |  • Templating för olika miljöer                                 |   |
|  |  • Dependency management                                         |   |
|  |  • Release management                                           |   |
|  |                                                                  |   |
|  |  +--------------------------------------------------------+     |   |
|  |  |            myapp-chart (v1.2.3)                        |     |   |
|  |  |   templates/     +     values.yaml    ->  K8s Resources |     |   |
|  |  +--------------------------------------------------------+     |   |
|  |                          |                                       |   |
|  |                   helm install myapp ./myapp-chart               |   |
|  +-----------------------------------------------------------------+   |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Helm Architecture

```
+-------------------------------------------------------------------------+
|                      HELM ARCHITECTURE                                   |
+-------------------------------------------------------------------------+
|                                                                          |
|  +-----------------------------------------------------------------+   |
|  |                        HELM CLIENT                               |   |
|  |                    (Lokalt på din maskin)                        |   |
|  +---------------------------+-------------------------------------+   |
|                              |                                          |
|                              | 1. helm install/upgrade                  |
|                              |                                          |
|  +---------------------------▼-------------------------------------+   |
|  |                      KUBERNETES API                              |   |
|  +---------------------------+-------------------------------------+   |
|                              |                                          |
|         +--------------------+--------------------+                    |
|         |                    |                    |                     |
|         ▼                    ▼                    ▼                     |
|  +------------+      +------------+      +------------+               |
|  | Deployment |      |  Service   |      | ConfigMap  |               |
|  +------------+      +------------+      +------------+               |
|                                                                          |
|  RELEASE STATE: Lagras som Secrets i kubernetes                         |
|  (helm-release-v1.myapp.v1, helm-release-v1.myapp.v2, ...)             |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 3. Installation & Setup

```bash
# macOS
brew install helm

# Linux
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Verify
helm version

# Add official repo
helm repo add stable https://charts.helm.sh/stable
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Search for charts
helm search repo nginx
helm search hub wordpress    # Artifact Hub
```

## 4. Core Commands

```bash
# ============= REPO MANAGEMENT =============
helm repo list                           # Lista repos
helm repo add NAME URL                   # Lägg till repo
helm repo update                         # Uppdatera cache
helm repo remove NAME                    # Ta bort repo

# ============= SEARCH =============
helm search repo KEYWORD                 # Sök i lokala repos
helm search hub KEYWORD                  # Sök på Artifact Hub

# ============= INSTALL =============
helm install RELEASE CHART               # Installera
helm install RELEASE CHART -f values.yaml
helm install RELEASE CHART --set key=value
helm install RELEASE CHART --namespace NS --create-namespace

# ============= UPGRADE & ROLLBACK =============
helm upgrade RELEASE CHART               # Uppgradera
helm upgrade --install RELEASE CHART     # Install om ej finns
helm rollback RELEASE REVISION           # Rollback till revision

# ============= STATUS & INFO =============
helm list                                # Lista releases
helm list -A                             # Alla namespaces
helm status RELEASE                      # Release status
helm history RELEASE                     # Release history
helm get values RELEASE                  # User-supplied values
helm get manifest RELEASE                # Deployed manifests

# ============= UNINSTALL =============
helm uninstall RELEASE                   # Ta bort release
helm uninstall RELEASE --keep-history    # Behåll history
```

## 5. Praktiska Övningar

### Övning 1: Install från Repo

```bash
# Lägg till Bitnami repo
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Sök efter nginx
helm search repo bitnami/nginx

# Installera nginx
helm install my-nginx bitnami/nginx --namespace web --create-namespace

# Verifiera
kubectl get all -n web
helm list -n web
helm status my-nginx -n web

# Se values som kan konfigureras
helm show values bitnami/nginx

# Uppgradera med custom values
helm upgrade my-nginx bitnami/nginx \
  --namespace web \
  --set replicaCount=3 \
  --set service.type=NodePort

# Se history
helm history my-nginx -n web

# Rollback
helm rollback my-nginx 1 -n web

# Cleanup
helm uninstall my-nginx -n web
```

### Övning 2: Values Files

```bash
# Skapa values file
cat << 'EOF' > nginx-values.yaml
replicaCount: 3

service:
  type: ClusterIP
  port: 80

resources:
  limits:
    cpu: 200m
    memory: 256Mi
  requests:
    cpu: 100m
    memory: 128Mi

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPU: 80
EOF

# Install med values file
helm install my-nginx bitnami/nginx \
  -f nginx-values.yaml \
  --namespace web \
  --create-namespace

# Override values file med --set
helm upgrade my-nginx bitnami/nginx \
  -f nginx-values.yaml \
  --set replicaCount=5 \
  --namespace web
```

### Övning 3: Dry Run & Template

```bash
# Dry run - simulera install
helm install my-nginx bitnami/nginx --dry-run

# Template - visa genererade manifests
helm template my-nginx bitnami/nginx > manifests.yaml

# Template med values
helm template my-nginx bitnami/nginx -f nginx-values.yaml

# Debug mode
helm install my-nginx bitnami/nginx --dry-run --debug
```

## 6. Values Hierarchy

```
+-------------------------------------------------------------------------+
|                      VALUES HIERARCHY (Prioritet)                        |
+-------------------------------------------------------------------------+
|                                                                          |
|  HÖGST PRIORITET                                                         |
|       ▲                                                                  |
|       |  4. --set flag                                                   |
|       |     helm install ... --set replicaCount=5                       |
|       |                                                                  |
|       |  3. --set-file flag                                             |
|       |     helm install ... --set-file ca.crt=./ca.crt                 |
|       |                                                                  |
|       |  2. -f (values file)                                            |
|       |     helm install ... -f prod-values.yaml -f secrets.yaml        |
|       |     (senare filer har högre prioritet)                          |
|       |                                                                  |
|       |  1. Chart default values.yaml                                   |
|       ▼     (inbyggda i chart)                                          |
|  LÄGST PRIORITET                                                         |
|                                                                          |
|  EXEMPEL:                                                                |
|  ---------------------------------------------------------------------  |
|  chart/values.yaml:        replicaCount: 1                              |
|  prod-values.yaml:         replicaCount: 3                              |
|  --set replicaCount=5:     replicaCount: 5  <- VINNARE                  |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 7. Best Practices

```
+-------------------------------------------------------------------------+
|                      HELM BEST PRACTICES                                 |
+-------------------------------------------------------------------------+
|                                                                          |
|  ✅ Version Control                                                      |
|     □ Versionshantera values-filer (Git)                               |
|     □ Använd semantic versioning för charts                            |
|     □ Dokumentera ändringar i CHANGELOG                                |
|                                                                          |
|  ✅ Environment Separation                                              |
|     □ Separata values-filer per miljö                                  |
|     □ values-dev.yaml, values-staging.yaml, values-prod.yaml           |
|     □ Secrets hanteras separat (Sealed Secrets, Vault)                 |
|                                                                          |
|  ✅ Release Naming                                                      |
|     □ Konsistent naming convention                                     |
|     □ Inkludera miljö: myapp-prod, myapp-staging                       |
|     □ Använd --generate-name sparsamt                                  |
|                                                                          |
|  ✅ Testing                                                             |
|     □ Alltid dry-run före install/upgrade                              |
|     □ helm lint för chart validation                                   |
|     □ helm test för release testing                                    |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 8-14. Sammanfattning & Task

### Quick Reference

| Command | Description |
|---------|-------------|
| `helm install NAME CHART` | Install release |
| `helm upgrade NAME CHART` | Upgrade release |
| `helm rollback NAME REV` | Rollback to revision |
| `helm list` | List releases |
| `helm uninstall NAME` | Remove release |

---

**Nästa Node:** Helm Charts ->
''',
    "xp_reward": 150,
    "estimated_minutes": 50,
    "prerequisites": ["k8s_node_12"],
    "learning_outcomes": [
        "Förstå Helm-konceptet",
        "Installera och konfigurera Helm",
        "Hantera releases",
        "Använda values files"
    ]
}

NODE_14 = {
    "id": "k8s_node_14",
    "title": "Helm Charts - Creating Custom Charts",
    "slug": "helm-charts-creating-custom-charts",
    "content": r'''# 📊 Helm Charts - Creating Custom Charts

## 1. Introduktion & Kontext

Nu när du kan använda Helm, är det dags att skapa egna Charts. En Chart är en samling filer som beskriver en relaterad uppsättning Kubernetes-resurser.

### Chart Structure

```
+-------------------------------------------------------------------------+
|                      HELM CHART STRUCTURE                                |
+-------------------------------------------------------------------------+
|                                                                          |
|  myapp/                                                                  |
|  +-- Chart.yaml             # Chart metadata                            |
|  +-- Chart.lock             # Dependency lock file                      |
|  +-- values.yaml            # Default values                            |
|  +-- values.schema.json     # Schema för values validation              |
|  +-- .helmignore            # Files att ignorera                        |
|  |                                                                       |
|  +-- charts/                # Subdirectory för dependencies             |
|  |   +-- postgresql/                                                    |
|  |                                                                       |
|  +-- templates/             # Template filer                            |
|  |   +-- NOTES.txt          # Post-install notes                        |
|  |   +-- _helpers.tpl       # Template helpers/partials                 |
|  |   +-- deployment.yaml                                                |
|  |   +-- service.yaml                                                   |
|  |   +-- configmap.yaml                                                 |
|  |   +-- secret.yaml                                                    |
|  |   +-- ingress.yaml                                                   |
|  |   +-- hpa.yaml                                                       |
|  |   +-- serviceaccount.yaml                                            |
|  |                                                                       |
|  +-- crds/                  # Custom Resource Definitions               |
|  |                                                                       |
|  +-- tests/                 # Helm tests                                |
|      +-- test-connection.yaml                                           |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 2. Chart.yaml

```yaml
apiVersion: v2                 # v2 för Helm 3
name: myapp
description: A Helm chart for MyApp
type: application              # application | library

# Version av chartet själv
version: 1.0.0

# Version av applikationen
appVersion: "2.5.0"

# Keywords för search
keywords:
  - webapp
  - nodejs
  - api

home: https://myapp.example.com
sources:
  - https://github.com/company/myapp

maintainers:
  - name: Team DevOps
    email: devops@example.com

# Dependencies
dependencies:
  - name: postgresql
    version: "12.x.x"
    repository: https://charts.bitnami.com/bitnami
    condition: postgresql.enabled

  - name: redis
    version: "17.x.x"
    repository: https://charts.bitnami.com/bitnami
    condition: redis.enabled
```

## 3. Templates & Templating

### Basic Template

```yaml
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "myapp.fullname" . }}
  labels:
    {{- include "myapp.labels" . | nindent 4 }}
spec:
  {{- if not .Values.autoscaling.enabled }}
  replicas: {{ .Values.replicaCount }}
  {{- end }}
  selector:
    matchLabels:
      {{- include "myapp.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "myapp.selectorLabels" . | nindent 8 }}
    spec:
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}

      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}

          ports:
            - name: http
              containerPort: {{ .Values.service.targetPort }}

          {{- if .Values.env }}
          env:
            {{- range $key, $value := .Values.env }}
            - name: {{ $key }}
              value: {{ $value | quote }}
            {{- end }}
          {{- end }}

          {{- if .Values.livenessProbe.enabled }}
          livenessProbe:
            httpGet:
              path: {{ .Values.livenessProbe.path }}
              port: http
            initialDelaySeconds: {{ .Values.livenessProbe.initialDelaySeconds }}
          {{- end }}

          resources:
            {{- toYaml .Values.resources | nindent 12 }}

      {{- with .Values.nodeSelector }}
      nodeSelector:
        {{- toYaml . | nindent 8 }}
      {{- end }}
```

### Helper Functions (_helpers.tpl)

```yaml
# templates/_helpers.tpl

{{/*
Expand the name of the chart.
*/}}
{{- define "myapp.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "myapp.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "myapp.labels" -}}
helm.sh/chart: {{ include "myapp.chart" . }}
{{ include "myapp.selectorLabels" . }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "myapp.selectorLabels" -}}
app.kubernetes.io/name: {{ include "myapp.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

## 4. Values.yaml

```yaml
# values.yaml - Default values

replicaCount: 1

image:
  repository: mycompany/myapp
  pullPolicy: IfNotPresent
  tag: ""  # Defaults to Chart.AppVersion

imagePullSecrets: []
nameOverride: ""
fullnameOverride: ""

serviceAccount:
  create: true
  annotations: {}
  name: ""

service:
  type: ClusterIP
  port: 80
  targetPort: 3000

ingress:
  enabled: false
  className: nginx
  annotations: {}
  hosts:
    - host: myapp.local
      paths:
        - path: /
          pathType: Prefix
  tls: []

resources:
  limits:
    cpu: 200m
    memory: 256Mi
  requests:
    cpu: 100m
    memory: 128Mi

autoscaling:
  enabled: false
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 80

env:
  NODE_ENV: production
  LOG_LEVEL: info

livenessProbe:
  enabled: true
  path: /health
  initialDelaySeconds: 30

readinessProbe:
  enabled: true
  path: /ready
  initialDelaySeconds: 5

nodeSelector: {}
tolerations: []
affinity: {}

# Dependency configuration
postgresql:
  enabled: true
  auth:
    database: myapp
    username: myapp

redis:
  enabled: false
```

## 5. Praktiska Övningar

### Övning 1: Skapa Chart

```bash
# Skapa nytt chart
helm create myapp

# Struktur
ls -la myapp/

# Validera
helm lint myapp

# Template locally
helm template myrelease myapp

# Install locally
helm install myrelease myapp --dry-run --debug
```

### Övning 2: Custom Chart

```bash
mkdir -p myapi/templates

# Chart.yaml
cat << 'EOF' > myapi/Chart.yaml
apiVersion: v2
name: myapi
description: My API Service
version: 1.0.0
appVersion: "1.0.0"
EOF

# values.yaml
cat << 'EOF' > myapi/values.yaml
replicaCount: 2
image:
  repository: nginx
  tag: latest
service:
  type: ClusterIP
  port: 80
EOF

# Deployment template
cat << 'EOF' > myapi/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-{{ .Chart.Name }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}-{{ .Chart.Name }}
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}-{{ .Chart.Name }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: 80
EOF

# Service template
cat << 'EOF' > myapi/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}-{{ .Chart.Name }}
spec:
  type: {{ .Values.service.type }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: 80
  selector:
    app: {{ .Release.Name }}-{{ .Chart.Name }}
EOF

# Test
helm lint myapi
helm template test myapi
helm install test myapi --dry-run
```

### Övning 3: Dependencies

```bash
# Lägg till dependency i Chart.yaml
cat << 'EOF' >> myapi/Chart.yaml

dependencies:
  - name: redis
    version: "17.x.x"
    repository: https://charts.bitnami.com/bitnami
    condition: redis.enabled
EOF

# Uppdatera values.yaml
cat << 'EOF' >> myapi/values.yaml

redis:
  enabled: true
  auth:
    enabled: false
EOF

# Bygg dependencies
helm dependency update myapi
helm dependency list myapi

# Install med dependencies
helm install myapi-prod myapi
```

## 6. Template Functions

```
+-------------------------------------------------------------------------+
|                   COMMON TEMPLATE FUNCTIONS                              |
+-------------------------------------------------------------------------+
|                                                                          |
|  STRING FUNCTIONS                                                        |
|  ---------------------------------------------------------------------  |
|  {{ .Values.name | quote }}          # "value"                          |
|  {{ .Values.name | upper }}          # VALUE                            |
|  {{ .Values.name | lower }}          # value                            |
|  {{ .Values.name | title }}          # Value                            |
|  {{ .Values.name | trunc 63 }}       # Truncate to 63 chars             |
|  {{ .Values.name | trimSuffix "-" }} # Remove trailing -                |
|  {{ "hello" | b64enc }}              # Base64 encode                    |
|                                                                          |
|  FLOW CONTROL                                                            |
|  ---------------------------------------------------------------------  |
|  {{- if .Values.enabled }}                                              |
|  {{- else if .Values.other }}                                           |
|  {{- else }}                                                            |
|  {{- end }}                                                             |
|                                                                          |
|  {{- with .Values.nodeSelector }}                                       |
|    {{- toYaml . | nindent 8 }}                                          |
|  {{- end }}                                                             |
|                                                                          |
|  {{- range .Values.servers }}                                           |
|    - {{ . }}                                                            |
|  {{- end }}                                                             |
|                                                                          |
|  YAML/JSON                                                              |
|  ---------------------------------------------------------------------  |
|  {{ .Values.data | toYaml }}         # Convert to YAML                  |
|  {{ .Values.data | toJson }}         # Convert to JSON                  |
|  {{ .Values.data | nindent 4 }}      # Indent 4 spaces                  |
|                                                                          |
|  DEFAULTS                                                               |
|  ---------------------------------------------------------------------  |
|  {{ .Values.tag | default "latest" }}                                   |
|  {{ .Values.port | default 8080 }}                                      |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 7. Best Practices

```
+-------------------------------------------------------------------------+
|                   CHART BEST PRACTICES                                   |
+-------------------------------------------------------------------------+
|                                                                          |
|  ✅ Structure                                                            |
|     □ Använd helm create som startpunkt                                 |
|     □ Inkludera NOTES.txt med användningsinstruktioner                  |
|     □ Dokumentera values i values.yaml med kommentarer                  |
|                                                                          |
|  ✅ Templates                                                            |
|     □ Använd _helpers.tpl för återanvändbara functions                  |
|     □ Följ naming conventions (include "chart.fullname")               |
|     □ Undvik hårdkodade värden                                          |
|                                                                          |
|  ✅ Values                                                               |
|     □ Ge sane defaults                                                  |
|     □ Använd nested structure för relaterade values                     |
|     □ Inkludera .Values.schema.json för validation                      |
|                                                                          |
|  ✅ Testing                                                             |
|     □ helm lint före varje release                                      |
|     □ helm template för debugging                                       |
|     □ Inkludera tests/ med helm test                                    |
|                                                                          |
+-------------------------------------------------------------------------+
```

## 8-14. Sammanfattning & Task

### Chart Development Flow

```
+-------------------------------------------------------------------------+
|                                                                          |
|  1. helm create myapp                                                   |
|           |                                                              |
|           ▼                                                              |
|  2. Edit Chart.yaml, values.yaml, templates/                            |
|           |                                                              |
|           ▼                                                              |
|  3. helm lint myapp                                                     |
|           |                                                              |
|           ▼                                                              |
|  4. helm template myapp                                                 |
|           |                                                              |
|           ▼                                                              |
|  5. helm install --dry-run                                              |
|           |                                                              |
|           ▼                                                              |
|  6. helm install                                                        |
|           |                                                              |
|           ▼                                                              |
|  7. helm test                                                           |
|                                                                          |
+-------------------------------------------------------------------------+
```

---

**Nästa Node:** Network Policies ->
''',
    "xp_reward": 170,
    "estimated_minutes": 65,
    "prerequisites": ["k8s_node_13"],
    "learning_outcomes": [
        "Skapa custom Helm charts",
        "Förstå template syntax",
        "Hantera dependencies",
        "Använda helper functions"
    ]
}

# Block 4 Part 1 exports
BLOCK_4_PART_1_NODES = [NODE_13, NODE_14]
