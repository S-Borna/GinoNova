/**
 * FastTrack Tools Data
 * Complete DevOps tools library
 */

import {
    FileJson,
    Box,
    Container,
    Terminal,
    Code,
    Monitor,
    Cloud,
    GitBranch,
    Cpu,
    Network,
    Database,
    Shield,
    Layers,
} from "lucide-react"

export interface CodeExample {
    title: string
    description: string
    language: string  // 'bash', 'yaml', 'python', 'json', etc.
    code: string
}

export interface Tool {
    slug: string
    name: string
    category: string
    icon: string
    shortDesc: string
    description: string
    installation: {
        apt?: string
        brew?: string
        pip?: string
        npm?: string
        other?: string
    }
    useCases: string[]
    keyFeatures: string[]
    codeExamples?: CodeExample[]  // NEW: Code examples
    officialUrl?: string
    docsUrl?: string
    flashcardCount: number
    quizCount: number
}

export const TOOL_CATEGORIES = [
    { id: "all", label: "Alla", icon: Layers },
    { id: "dataformat", label: "Dataformat", icon: FileJson },
    { id: "containers", label: "Containers", icon: Box },
    { id: "orchestration", label: "Orchestration", icon: Container },
    { id: "linux", label: "Linux & CLI", icon: Terminal },
    { id: "python", label: "Python", icon: Code },
    { id: "virtualization", label: "Virtualisering", icon: Monitor },
    { id: "cloud", label: "Cloud & IaC", icon: Cloud },
    { id: "cicd", label: "CI/CD", icon: GitBranch },
    { id: "monitoring", label: "Monitoring", icon: Cpu },
    { id: "network", label: "Nätverk", icon: Network },
    { id: "database", label: "Databaser", icon: Database },
    { id: "security", label: "Säkerhet", icon: Shield },
]

export const TOOLS_DATA: Tool[] = [
    // DATAFORMAT
    {
        slug: "yaml",
        name: "YAML",
        category: "dataformat",
        icon: "📄",
        shortDesc: "Human-readable data serialization",
        description: "YAML (YAML Ain't Markup Language) är ett dataformat som är lätt att läsa för människor. Används flitigt i Kubernetes, Docker Compose, Ansible och CI/CD-konfigurationer.",
        installation: {
            pip: "pip install pyyaml",
            npm: "npm install yaml"
        },
        useCases: ["Kubernetes manifests", "Docker Compose", "Ansible playbooks", "CI/CD pipelines", "Konfigurationsfiler"],
        keyFeatures: ["Indentation-baserad syntax", "Stöd för listor och maps", "Anchors & aliases", "Multi-document stöd"],
        codeExamples: [
            {
                title: "YAML Grundsyntax",
                description: "Grundläggande YAML-struktur med olika datatyper",
                language: "yaml",
                code: `# Kommentarer börjar med #
name: DevOpsHub
version: 2.0

# Nested objekt (indentation = 2 spaces)
database:
  host: localhost
  port: 5432
  credentials:
    username: admin
    password: secret

# Listor
environments:
  - development
  - staging
  - production

# Inline lista
tags: [docker, kubernetes, devops]

# Multiline string
description: |
  Detta är en lång beskrivning
  som sträcker sig över flera rader
  och behåller radbrytningar.

# Boolean och null
enabled: true
disabled: false
optional: null`
            },
            {
                title: "Anchors & Aliases",
                description: "Återanvänd data med anchors (&) och aliases (*)",
                language: "yaml",
                code: `# Definiera anchor med &
defaults: &defaults
  adapter: postgres
  pool: 5
  timeout: 30

# Återanvänd med alias *
development:
  <<: *defaults
  database: dev_db

staging:
  <<: *defaults
  database: staging_db
  pool: 10  # Override default

production:
  <<: *defaults
  database: prod_db
  pool: 25
  timeout: 60`
            },
            {
                title: "Multi-document YAML",
                description: "Flera dokument i samma fil separerade med ---",
                language: "yaml",
                code: `# Första dokumentet
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: production

# Andra dokumentet
---
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
stringData:
  API_KEY: abc123

# Tredje dokumentet
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3`
            }
        ],
        officialUrl: "https://yaml.org",
        docsUrl: "https://yaml.org/spec/1.2.2/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "json",
        name: "JSON",
        category: "dataformat",
        icon: "📋",
        shortDesc: "JavaScript Object Notation",
        description: "JSON är ett lättviktigt datautbytesformat baserat på JavaScript-syntax. Standard för API-kommunikation och konfiguration.",
        installation: {
            other: "Inbyggt i de flesta språk"
        },
        useCases: ["REST APIs", "Konfigurationsfiler", "NoSQL databaser", "Web storage", "Package manifests"],
        keyFeatures: ["Strikt syntax", "Bred språkstöd", "Lätt att parsa", "Självbeskrivande"],
        codeExamples: [
            {
                title: "JSON Grundstruktur",
                description: "Grundläggande JSON med olika datatyper",
                language: "json",
                code: `{
  "name": "DevOpsHub",
  "version": "2.0.0",
  "active": true,
  "users": 1500,
  "rating": 4.8,
  "features": [
    "modules",
    "quizzes",
    "flashcards"
  ],
  "database": {
    "host": "localhost",
    "port": 5432,
    "ssl": true
  },
  "metadata": null
}`
            },
            {
                title: "jq för JSON-manipulering",
                description: "Använd jq för att parsa och transformera JSON",
                language: "bash",
                code: `# Hämta specifikt fält
curl -s https://api.github.com/users/octocat | jq '.name'

# Filtrera array
echo '[{"name":"a","active":true},{"name":"b","active":false}]' | \\
  jq '[.[] | select(.active == true)]'

# Transformera data
cat data.json | jq '{
  username: .user.name,
  email: .user.email,
  active: .status == "active"
}'

# Hämta flera fält
cat package.json | jq '{name, version, main}'

# Iterera över array
cat users.json | jq '.users[] | "\\(.name): \\(.email)"'`
            },
            {
                title: "Python JSON-hantering",
                description: "Läs och skriv JSON med Python",
                language: "python",
                code: `import json

# Läs JSON från fil
with open('config.json', 'r') as f:
    config = json.load(f)

# Läs JSON från string
data = json.loads('{"name": "test", "value": 42}')

# Skriv JSON till fil (pretty print)
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Konvertera till JSON string
json_str = json.dumps(data, indent=2)

# Hantera custom objects
class User:
    def __init__(self, name):
        self.name = name

def serialize(obj):
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

json.dumps(User("Alice"), default=serialize)`
            }
        ],
        officialUrl: "https://www.json.org",
        docsUrl: "https://www.json.org/json-en.html",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "toml",
        name: "TOML",
        category: "dataformat",
        icon: "⚙️",
        shortDesc: "Tom's Obvious Minimal Language",
        description: "TOML är ett konfigurationsfilformat som är lätt att läsa. Populärt i Rust (Cargo.toml) och Python (pyproject.toml).",
        installation: {
            pip: "pip install toml",
            npm: "npm install @iarna/toml"
        },
        useCases: ["Python projects (pyproject.toml)", "Rust projects (Cargo.toml)", "Hugo sites", "Konfigurationsfiler"],
        keyFeatures: ["Explicit typning", "Nested tables", "Datum/tid-stöd", "Inline tables"],
        codeExamples: [
            {
                title: "TOML Grundsyntax",
                description: "Grundläggande TOML-struktur och datatyper",
                language: "toml",
                code: `# Kommentar
title = "DevOps Config"

[owner]
name = "Gino Nova"
dob = 1979-05-27T07:32:00-08:00  # First class datum/tid!

[database]
enabled = true
ports = [ 8000, 8001, 8002 ]
data = [ ["delta", "phi"], [3.14] ]
hosts = [
  "alpha",
  "omega"
]

[servers]

  [servers.alpha]
  ip = "10.0.0.1"
  role = "frontend"

  [servers.beta]
  ip = "10.0.0.2"
  role = "backend"`
            },
            {
                title: "pyproject.toml Exempel",
                description: "Modern Python-projektkonfiguration med pyproject.toml",
                language: "toml",
                code: `[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-devops-tool"
version = "1.0.0"
description = "A DevOps automation tool"
readme = "README.md"
requires-python = ">=3.10"
license = { text = "MIT" }
authors = [
    { name = "DevOps Team", email = "team@devops.io" }
]
dependencies = [
    "requests>=2.28.0",
    "pyyaml>=6.0",
    "click>=8.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
    "mypy>=1.0",
]

[project.scripts]
devtool = "my_devops_tool.cli:main"

[tool.black]
line-length = 88

[tool.mypy]
python_version = "3.11"
strict = true`
            },
            {
                title: "Python TOML-hantering",
                description: "Läs och skriv TOML med Python",
                language: "python",
                code: `import tomllib  # Python 3.11+ (inbyggt!)
import tomli_w  # För att skriva TOML

# Läs TOML (Python 3.11+)
with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)
    
print(config["project"]["name"])
print(config["project"]["dependencies"])

# Skriv TOML (med tomli-w)
data = {
    "project": {
        "name": "my-app",
        "version": "2.0.0",
        "dependencies": ["requests", "click"],
    },
    "tool": {
        "black": {"line-length": 88}
    }
}

with open("config.toml", "wb") as f:
    tomli_w.dump(data, f)`
            }
        ],
        officialUrl: "https://toml.io",
        docsUrl: "https://toml.io/en/v1.0.0",
        flashcardCount: 10,
        quizCount: 6
    },
    // CONTAINERS
    {
        slug: "docker",
        name: "Docker",
        category: "containers",
        icon: "🐳",
        shortDesc: "Container platform",
        description: "Docker är en plattform för att bygga, distribuera och köra applikationer i containers. Isolerar applikationer från underliggande system.",
        installation: {
            apt: "sudo apt install docker.io",
            brew: "brew install docker"
        },
        useCases: ["Applikationscontainers", "Microservices", "Utvecklingsmiljöer", "CI/CD builds", "Deployment"],
        keyFeatures: ["Dockerfile", "Docker Compose", "Multi-stage builds", "Volumes", "Networks", "Registry"],
        codeExamples: [
            {
                title: "Enkel Dockerfile",
                description: "En basic Dockerfile för en Node.js-applikation",
                language: "dockerfile",
                code: `# Basimage
FROM node:20-alpine

# Sätt arbetskatalog
WORKDIR /app

# Kopiera package files först (för cache)
COPY package*.json ./

# Installera dependencies
RUN npm ci --only=production

# Kopiera källkod
COPY . .

# Exponera port
EXPOSE 3000

# Starta applikationen
CMD ["node", "server.js"]`
            },
            {
                title: "Multi-stage Build",
                description: "Optimerad build med multi-stage för mindre images",
                language: "dockerfile",
                code: `# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
USER node
CMD ["node", "dist/server.js"]`
            },
            {
                title: "Docker CLI Kommandon",
                description: "Vanliga Docker-kommandon för dagligt bruk",
                language: "bash",
                code: `# Bygg image
docker build -t myapp:latest .

# Kör container
docker run -d -p 3000:3000 --name myapp myapp:latest

# Lista containers
docker ps -a

# Se loggar
docker logs -f myapp

# Gå in i container
docker exec -it myapp /bin/sh

# Stoppa och ta bort
docker stop myapp && docker rm myapp

# Rensa oanvända resurser
docker system prune -af`
            },
            {
                title: "Docker Volumes",
                description: "Hantera persistent data med volumes",
                language: "bash",
                code: `# Skapa named volume
docker volume create mydata

# Kör med volume
docker run -d \\
  -v mydata:/app/data \\
  -v $(pwd)/config:/app/config:ro \\
  myapp:latest

# Lista volumes
docker volume ls

# Inspektera volume
docker volume inspect mydata

# Ta bort volume
docker volume rm mydata`
            }
        ],
        officialUrl: "https://www.docker.com",
        docsUrl: "https://docs.docker.com",
        flashcardCount: 25,
        quizCount: 20
    },
    {
        slug: "podman",
        name: "Podman",
        category: "containers",
        icon: "🦭",
        shortDesc: "Daemonless container engine",
        description: "Podman är ett Docker-alternativ som kör containers utan daemon. Rootless by default, kompatibelt med Docker CLI.",
        installation: {
            apt: "sudo apt install podman",
            brew: "brew install podman"
        },
        useCases: ["Rootless containers", "Docker replacement", "Pod management", "Systemd integration"],
        keyFeatures: ["Daemonless", "Rootless", "Pod support", "Docker-kompatibel", "Systemd integration"],
        codeExamples: [
            {
                title: "Podman vs Docker Kommandon",
                description: "Podman har samma CLI som Docker - byt bara ut 'docker' mot 'podman'",
                language: "bash",
                code: `# Kör container (rootless by default!)
podman run -d -p 8080:80 nginx:alpine

# Lista containers
podman ps -a

# Bygga image från Dockerfile
podman build -t myapp:latest .

# Visa loggar
podman logs -f container_name

# Gå in i container
podman exec -it container_name /bin/sh

# Alias för Docker-kompatibilitet
alias docker=podman`
            },
            {
                title: "Podman Pods",
                description: "Pods grupperar containers som delar network namespace (som Kubernetes)",
                language: "bash",
                code: `# Skapa en pod
podman pod create --name mypod -p 8080:80

# Kör containers i podden
podman run -d --pod mypod nginx:alpine
podman run -d --pod mypod redis:alpine

# Lista pods
podman pod ls

# Visa containers i en pod
podman pod inspect mypod

# Stoppa hela podden
podman pod stop mypod

# Ta bort pod (inkl containers)
podman pod rm mypod`
            },
            {
                title: "Podman Systemd Integration",
                description: "Generera systemd service-filer för containers",
                language: "bash",
                code: `# Generera systemd unit-fil från körande container
podman generate systemd --new --name myapp > myapp.service

# Eller för en pod
podman generate systemd --new --name mypod --files

# Installera som user service
mkdir -p ~/.config/systemd/user/
cp myapp.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now myapp

# Kör container vid boot (lingering)
loginctl enable-linger $USER`
            }
        ],
        officialUrl: "https://podman.io",
        docsUrl: "https://docs.podman.io",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "containerd",
        name: "containerd",
        category: "containers",
        icon: "📦",
        shortDesc: "Container runtime",
        description: "containerd är en industri-standard container runtime som hanterar hela container-livscykeln. Används av Docker och Kubernetes.",
        installation: {
            apt: "sudo apt install containerd"
        },
        useCases: ["Kubernetes runtime", "Docker backend", "Container management", "Image management"],
        keyFeatures: ["OCI-kompatibel", "Snapshots", "CRI support", "Plugin architecture"],
        officialUrl: "https://containerd.io",
        docsUrl: "https://containerd.io/docs/",
        flashcardCount: 8,
        quizCount: 5
    },
    // ORCHESTRATION
    {
        slug: "kubernetes",
        name: "Kubernetes",
        category: "orchestration",
        icon: "☸️",
        shortDesc: "Container orchestration",
        description: "Kubernetes (K8s) är en open-source plattform för att automatisera deployment, skalning och hantering av containeriserade applikationer.",
        installation: {
            brew: "brew install kubectl",
            other: "curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
        },
        useCases: ["Container orchestration", "Microservices", "Auto-scaling", "Self-healing", "Rolling updates"],
        keyFeatures: ["Pods", "Services", "Deployments", "ConfigMaps", "Secrets", "Ingress", "Namespaces"],
        codeExamples: [
            {
                title: "Deployment Manifest",
                description: "En komplett Deployment med replicas och resource limits",
                language: "yaml",
                code: `apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  labels:
    app: myapp
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
      - name: myapp
        image: myapp:latest
        ports:
        - containerPort: 3000
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
            port: 3000
          initialDelaySeconds: 10
          periodSeconds: 5`
            },
            {
                title: "Service & Ingress",
                description: "Exponera applikation med Service och Ingress",
                language: "yaml",
                code: `# Service
apiVersion: v1
kind: Service
metadata:
  name: myapp-svc
spec:
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 3000
  type: ClusterIP
---
# Ingress
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp-svc
            port:
              number: 80`
            },
            {
                title: "ConfigMap & Secret",
                description: "Hantera konfiguration och hemligheter",
                language: "yaml",
                code: `# ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: myapp-config
data:
  APP_ENV: "production"
  LOG_LEVEL: "info"
  config.json: |
    {
      "features": {
        "darkMode": true
      }
    }
---
# Secret
apiVersion: v1
kind: Secret
metadata:
  name: myapp-secrets
type: Opaque
stringData:
  DB_PASSWORD: "supersecret"
  API_KEY: "abc123xyz"`
            },
            {
                title: "kubectl Kommandon",
                description: "Vanliga kubectl-kommandon för K8s-administration",
                language: "bash",
                code: `# Applicera manifest
kubectl apply -f deployment.yaml

# Lista resurser
kubectl get pods,svc,deploy -n default

# Describe för debugging
kubectl describe pod myapp-xyz123

# Loggar
kubectl logs -f deployment/myapp

# Exec in i pod
kubectl exec -it myapp-xyz123 -- /bin/sh

# Port-forward för lokal access
kubectl port-forward svc/myapp-svc 8080:80

# Skala deployment
kubectl scale deployment myapp --replicas=5

# Rollback
kubectl rollout undo deployment/myapp`
            }
        ],
        officialUrl: "https://kubernetes.io",
        docsUrl: "https://kubernetes.io/docs/",
        flashcardCount: 30,
        quizCount: 25
    },
    {
        slug: "helm",
        name: "Helm",
        category: "orchestration",
        icon: "⎈",
        shortDesc: "Kubernetes package manager",
        description: "Helm är pakethanteraren för Kubernetes. Använder charts för att definiera, installera och uppgradera Kubernetes-applikationer.",
        installation: {
            brew: "brew install helm",
            other: "curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash"
        },
        useCases: ["Application packaging", "Release management", "Dependency management", "Templating"],
        keyFeatures: ["Charts", "Values", "Releases", "Repositories", "Hooks", "Subcharts"],
        codeExamples: [
            {
                title: "Helm Grundkommandon",
                description: "Vanliga Helm CLI-operationer",
                language: "bash",
                code: `# Lägg till repository
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Sök efter charts
helm search repo nginx
helm search hub prometheus

# Installera chart
helm install my-nginx bitnami/nginx
helm install my-nginx bitnami/nginx -f values.yaml
helm install my-nginx bitnami/nginx --set service.type=LoadBalancer

# Lista installationer
helm list
helm list -n my-namespace

# Uppgradera release
helm upgrade my-nginx bitnami/nginx --set replicaCount=3
helm upgrade --install my-nginx bitnami/nginx  # Install or upgrade

# Rollback
helm rollback my-nginx 1
helm history my-nginx

# Avinstallera
helm uninstall my-nginx

# Visa rendered manifests
helm template my-nginx bitnami/nginx
helm get manifest my-nginx`
            },
            {
                title: "Skapa Helm Chart",
                description: "Struktur och templates för egen chart",
                language: "bash",
                code: `# Skapa ny chart
helm create myapp

# Chart-struktur:
# myapp/
# ├── Chart.yaml          # Chart metadata
# ├── values.yaml         # Default values
# ├── charts/             # Dependencies
# └── templates/
#     ├── deployment.yaml
#     ├── service.yaml
#     ├── ingress.yaml
#     ├── _helpers.tpl    # Template helpers
#     └── NOTES.txt       # Installation notes

# Validera chart
helm lint myapp/

# Package chart
helm package myapp/

# Installera lokal chart
helm install my-release ./myapp -f custom-values.yaml`
            },
            {
                title: "Helm Templates",
                description: "Go templating i Helm charts",
                language: "yaml",
                code: `# templates/deployment.yaml
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
          env:
            {{- range $key, $value := .Values.env }}
            - name: {{ $key }}
              value: {{ $value | quote }}
            {{- end }}

# values.yaml
replicaCount: 2
image:
  repository: myapp
  tag: "1.0.0"
service:
  port: 80
env:
  APP_ENV: production`
            }
        ],
        officialUrl: "https://helm.sh",
        docsUrl: "https://helm.sh/docs/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "docker-compose",
        name: "Docker Compose",
        category: "orchestration",
        icon: "🎼",
        shortDesc: "Multi-container Docker",
        description: "Docker Compose definierar och kör multi-container Docker-applikationer med en YAML-fil. Perfekt för lokal utveckling.",
        installation: {
            apt: "sudo apt install docker-compose-plugin",
            brew: "brew install docker-compose"
        },
        useCases: ["Lokal utveckling", "Multi-service apps", "Testing environments", "CI/CD"],
        keyFeatures: ["Services", "Networks", "Volumes", "Environment variables", "Depends_on", "Profiles"],
        codeExamples: [
            {
                title: "Fullstack App Setup",
                description: "Komplett exempel med frontend, backend och databas",
                language: "yaml",
                code: `version: "3.9"

services:
  # Frontend
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - API_URL=http://backend:8080
    depends_on:
      - backend
    volumes:
      - ./frontend/src:/app/src  # Hot reload
    networks:
      - app-network

  # Backend API
  backend:
    build:
      context: ./backend
    ports:
      - "8080:8080"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/myapp
      - REDIS_URL=redis://cache:6379
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    networks:
      - app-network

  # PostgreSQL Database
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d myapp"]
      interval: 5s
      timeout: 5s
      retries: 5
    networks:
      - app-network

  # Redis Cache
  cache:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - app-network

networks:
  app-network:
    driver: bridge

volumes:
  postgres_data:
  redis_data:`
            },
            {
                title: "CLI Kommandon",
                description: "Vanliga Docker Compose-kommandon",
                language: "bash",
                code: `# Starta alla services
docker compose up -d

# Starta med build
docker compose up -d --build

# Starta specifika services
docker compose up -d frontend backend

# Visa loggar
docker compose logs -f backend

# Lista services
docker compose ps

# Skala service
docker compose up -d --scale worker=3

# Stoppa allt
docker compose down

# Stoppa och ta bort volumes
docker compose down -v

# Kör kommando i service
docker compose exec backend npm run migrate

# Environment-specifik config
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d`
            },
            {
                title: "Profiles & Overrides",
                description: "Avancerad konfiguration för olika miljöer",
                language: "yaml",
                code: `version: "3.9"

services:
  app:
    image: myapp:latest
    profiles: ["production"]

  app-dev:
    build: .
    profiles: ["development"]
    volumes:
      - .:/app
    command: npm run dev

  monitoring:
    image: prometheus:latest
    profiles: ["debug", "production"]

  debug-tools:
    image: alpine
    profiles: ["debug"]
    command: sleep infinity

# Användning:
# docker compose --profile development up
# docker compose --profile production --profile debug up`
            }
        ],
        officialUrl: "https://docs.docker.com/compose/",
        docsUrl: "https://docs.docker.com/compose/compose-file/",
        flashcardCount: 18,
        quizCount: 12
    },
    // LINUX & CLI
    {
        slug: "bash",
        name: "Bash",
        category: "linux",
        icon: "💻",
        shortDesc: "Bourne Again Shell",
        description: "Bash är standard shell i de flesta Linux-distributioner. Kraftfullt scripting-språk för automation och systemadministration.",
        installation: {
            apt: "sudo apt install bash",
            other: "Förinstallerat på de flesta system"
        },
        useCases: ["Shell scripting", "Automation", "System administration", "CI/CD scripts", "Cron jobs"],
        keyFeatures: ["Variables", "Functions", "Conditionals", "Loops", "Pipes", "Redirections", "Subshells"],
        codeExamples: [
            {
                title: "Grundläggande Script",
                description: "Ett komplett Bash-script med error handling",
                language: "bash",
                code: `#!/bin/bash
set -euo pipefail  # Exit on error, undefined vars, pipe fails

# Färger för output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
NC='\\033[0m' # No Color

# Funktion för loggning
log() {
    echo -e "\${GREEN}[INFO]\${NC} \$1"
}

error() {
    echo -e "\${RED}[ERROR]\${NC} \$1" >&2
    exit 1
}

# Argument parsing
if [[ \$# -lt 1 ]]; then
    error "Usage: \$0 <environment>"
fi

ENVIRONMENT="\$1"
log "Deploying to \$ENVIRONMENT..."

# Din logik här
log "Deployment complete!"`
            },
            {
                title: "Loopar & Conditionals",
                description: "Iteration och villkorssatser i Bash",
                language: "bash",
                code: `#!/bin/bash

# For loop över array
SERVERS=("web1" "web2" "db1")
for server in "\${SERVERS[@]}"; do
    echo "Checking \$server..."
done

# While loop
counter=0
while [[ \$counter -lt 5 ]]; do
    echo "Count: \$counter"
    ((counter++))
done

# If-else
if [[ -f "/etc/passwd" ]]; then
    echo "File exists"
elif [[ -d "/etc" ]]; then
    echo "Directory exists"
else
    echo "Neither exists"
fi

# Case statement
case "\$1" in
    start)   echo "Starting..." ;;
    stop)    echo "Stopping..." ;;
    restart) echo "Restarting..." ;;
    *)       echo "Unknown command" ;;
esac`
            },
            {
                title: "Pipes & Redirection",
                description: "Dataflöde och output-hantering",
                language: "bash",
                code: `#!/bin/bash

# Pipe - skicka output till nästa kommando
cat /var/log/syslog | grep error | head -20

# Redirect stdout till fil
echo "Log entry" > output.log     # Skriv över
echo "Another entry" >> output.log # Append

# Redirect stderr
command 2> errors.log             # Endast stderr
command &> all_output.log         # Både stdout och stderr

# Läs från fil
while IFS= read -r line; do
    echo "Processing: \$line"
done < input.txt

# Process substitution
diff <(ls dir1) <(ls dir2)

# Command substitution
TODAY=\$(date +%Y-%m-%d)
FILES_COUNT=\$(ls -1 | wc -l)
echo "Idag: \$TODAY, Filer: \$FILES_COUNT"`
            },
            {
                title: "Funktioner & Argument",
                description: "Återanvändbar kod med funktioner",
                language: "bash",
                code: `#!/bin/bash

# Funktion med argument
deploy_service() {
    local service="\$1"
    local version="\${2:-latest}"  # Default värde

    echo "Deploying \$service:\$version"

    # Return status
    if docker pull "\$service:\$version"; then
        return 0
    else
        return 1
    fi
}

# Anropa funktion
if deploy_service "nginx" "1.25"; then
    echo "Success!"
else
    echo "Failed!"
fi

# Funktion med namngivna output
get_system_info() {
    local -n result=\$1  # nameref
    result[hostname]=\$(hostname)
    result[kernel]=\$(uname -r)
    result[uptime]=\$(uptime -p)
}

declare -A info
get_system_info info
echo "Host: \${info[hostname]}"`
            }
        ],
        officialUrl: "https://www.gnu.org/software/bash/",
        docsUrl: "https://www.gnu.org/software/bash/manual/",
        flashcardCount: 20,
        quizCount: 15
    },
    {
        slug: "alpine",
        name: "Alpine Linux",
        category: "linux",
        icon: "🏔️",
        shortDesc: "Minimal Linux distro",
        description: "Alpine Linux är en säkerhetsfokuserad, lättviktig Linux-distribution. Populär som bas-image för Docker containers (~5MB).",
        installation: {
            other: "docker pull alpine:latest"
        },
        useCases: ["Docker base images", "Minimal containers", "Edge computing", "Security-focused systems"],
        keyFeatures: ["musl libc", "BusyBox", "apk package manager", "~5MB storlek", "Security-hardened"],
        codeExamples: [
            {
                title: "apk Pakethantering",
                description: "Alpine's pakethanterare - snabb och enkel",
                language: "bash",
                code: `# Uppdatera paketindex
apk update

# Installera paket
apk add nginx curl git

# Installera utan cache (sparar utrymme i Docker)
apk add --no-cache python3 py3-pip

# Sök efter paket
apk search nginx

# Visa paketinfo
apk info nginx

# Lista installerade paket
apk list --installed

# Ta bort paket
apk del nginx

# Uppgradera alla paket
apk upgrade`
            },
            {
                title: "Alpine Dockerfile Best Practices",
                description: "Optimerad Dockerfile med Alpine",
                language: "dockerfile",
                code: `# Multi-stage build med Alpine
FROM python:3.11-alpine AS builder

# Installera build dependencies
RUN apk add --no-cache \\
    gcc \\
    musl-dev \\
    libffi-dev

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM python:3.11-alpine
WORKDIR /app

# Kopiera endast installerade packages
COPY --from=builder /root/.local /root/.local
COPY . .

# Skapa non-root user
RUN adduser -D -u 1000 appuser
USER appuser

ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]`
            },
            {
                title: "Alpine Service Management",
                description: "OpenRC istället för systemd",
                language: "bash",
                code: `# Alpine använder OpenRC (inte systemd)

# Starta/stoppa tjänst
rc-service nginx start
rc-service nginx stop
rc-service nginx restart

# Enable vid boot
rc-update add nginx default

# Disable vid boot
rc-update del nginx default

# Lista alla tjänster
rc-status

# Se specifik runlevel
rc-status --runlevel default

# Manuell service-kontroll
/etc/init.d/nginx status`
            }
        ],
        officialUrl: "https://alpinelinux.org",
        docsUrl: "https://wiki.alpinelinux.org",
        flashcardCount: 10,
        quizCount: 8
    },
    {
        slug: "systemd",
        name: "systemd",
        category: "linux",
        icon: "⚙️",
        shortDesc: "System & service manager",
        description: "systemd är init-systemet och service manager för moderna Linux-distributioner. Hanterar tjänster, logging och boot-processen.",
        installation: {
            other: "Förinstallerat på de flesta moderna Linux-distros"
        },
        useCases: ["Service management", "Boot process", "Logging (journald)", "Timers (cron replacement)", "Socket activation"],
        keyFeatures: ["Units", "Targets", "journalctl", "systemctl", "Timers", "Socket activation"],
        codeExamples: [
            {
                title: "systemctl Kommandon",
                description: "Hantera tjänster med systemctl",
                language: "bash",
                code: `# Starta/stoppa tjänst
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx    # Reload config utan restart

# Status
systemctl status nginx
systemctl is-active nginx
systemctl is-enabled nginx

# Enable/disable vid boot
sudo systemctl enable nginx
sudo systemctl disable nginx

# Lista tjänster
systemctl list-units --type=service
systemctl list-units --state=failed

# Visa dependencies
systemctl list-dependencies nginx

# Daemon reload (efter ändrad unit-fil)
sudo systemctl daemon-reload`
            },
            {
                title: "Skapa Service Unit",
                description: "Skapa egen systemd service",
                language: "ini",
                code: `# /etc/systemd/system/myapp.service
[Unit]
Description=My Application
Documentation=https://example.com/docs
After=network.target postgresql.service
Requires=postgresql.service

[Service]
Type=simple
User=appuser
Group=appgroup
WorkingDirectory=/opt/myapp

# Environment
Environment=NODE_ENV=production
EnvironmentFile=/opt/myapp/.env

# Kommando
ExecStart=/usr/bin/node /opt/myapp/server.js
ExecReload=/bin/kill -HUP $MAINPID
ExecStop=/bin/kill -TERM $MAINPID

# Restart policy
Restart=on-failure
RestartSec=5
StartLimitInterval=60
StartLimitBurst=3

# Security
NoNewPrivileges=true
ProtectSystem=strict
ReadWritePaths=/opt/myapp/data

[Install]
WantedBy=multi-user.target`
            },
            {
                title: "journalctl Logs",
                description: "Läs loggar med journalctl",
                language: "bash",
                code: `# Visa alla loggar
journalctl

# Senaste loggar (följ)
journalctl -f

# Loggar för specifik tjänst
journalctl -u nginx
journalctl -u nginx -f          # Follow
journalctl -u nginx --since today

# Tidsfilter
journalctl --since "2024-01-01"
journalctl --since "1 hour ago"
journalctl --since "2024-01-01" --until "2024-01-02"

# Prioritet/severity
journalctl -p err               # Errors och högre
journalctl -p warning

# Boot-loggar
journalctl -b                   # Nuvarande boot
journalctl -b -1                # Föregående boot
journalctl --list-boots

# Kernel messages
journalctl -k

# Output format
journalctl -o json-pretty
journalctl --no-pager

# Disk usage
journalctl --disk-usage
sudo journalctl --vacuum-time=7d`
            }
        ],
        officialUrl: "https://systemd.io",
        docsUrl: "https://www.freedesktop.org/software/systemd/man/",
        flashcardCount: 15,
        quizCount: 12
    },
    {
        slug: "nginx",
        name: "Nginx",
        category: "linux",
        icon: "🌐",
        shortDesc: "Web server & reverse proxy",
        description: "Nginx är en högpresterande web server, reverse proxy och load balancer. Används av miljontals webbplatser världen över.",
        installation: {
            apt: "sudo apt install nginx",
            brew: "brew install nginx"
        },
        useCases: ["Web server", "Reverse proxy", "Load balancer", "SSL termination", "Static file serving", "API gateway"],
        keyFeatures: ["Event-driven", "Low memory", "Upstream", "Location blocks", "SSL/TLS", "Caching"],
        codeExamples: [
            {
                title: "Reverse Proxy Config",
                description: "Konfigurera Nginx som reverse proxy för en app",
                language: "nginx",
                code: `# /etc/nginx/sites-available/myapp
server {
    listen 80;
    server_name myapp.example.com;

    # Redirect HTTP to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name myapp.example.com;

    # SSL Certificates
    ssl_certificate /etc/letsencrypt/live/myapp.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/myapp.example.com/privkey.pem;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;

    # Proxy till Node.js app
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }

    # API endpoint
    location /api {
        proxy_pass http://localhost:8080;
        proxy_read_timeout 60s;
    }
}`
            },
            {
                title: "Load Balancer",
                description: "Load balancing över flera servrar",
                language: "nginx",
                code: `# /etc/nginx/nginx.conf
upstream backend {
    # Load balancing method
    least_conn;  # eller: ip_hash, round-robin (default)

    server 10.0.1.10:3000 weight=3;
    server 10.0.1.11:3000 weight=2;
    server 10.0.1.12:3000 backup;

    # Health checks
    keepalive 32;
}

server {
    listen 80;

    location / {
        proxy_pass http://backend;
        proxy_next_upstream error timeout http_500;

        # Sticky sessions (optional)
        # sticky cookie srv_id expires=1h;
    }

    # Health check endpoint
    location /health {
        access_log off;
        return 200 "OK";
    }
}`
            },
            {
                title: "Nginx Kommandon",
                description: "Hantera Nginx från kommandoraden",
                language: "bash",
                code: `# Testa konfiguration
sudo nginx -t

# Starta/stoppa/restart
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx    # Reload utan downtime

# Status
sudo systemctl status nginx

# Aktivera site
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

# Loggar
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Debug
nginx -V                       # Version och modules
sudo nginx -T                  # Visa hela config`
            }
        ],
        officialUrl: "https://nginx.org",
        docsUrl: "https://nginx.org/en/docs/",
        flashcardCount: 20,
        quizCount: 15
    },
    // PYTHON
    {
        slug: "python-kwargs",
        name: "**kwargs",
        category: "python",
        icon: "🐍",
        shortDesc: "Keyword arguments",
        description: "**kwargs låter funktioner ta emot godtyckligt antal keyword arguments som en dictionary. Centralt koncept i Python.",
        installation: {
            other: "Inbyggt i Python"
        },
        useCases: ["Flexibla funktioner", "Wrapper functions", "Decorators", "API design", "Config passing"],
        keyFeatures: ["Dictionary unpacking", "Valfria parametrar", "Forwarding arguments", "Kombination med *args"],
        codeExamples: [
            {
                title: "*args och **kwargs Grunderna",
                description: "Flexibla funktionsparametrar",
                language: "python",
                code: `# *args - fångar positional arguments som tuple
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

# **kwargs - fångar keyword arguments som dict
def create_user(**kwargs):
    print(f"Creating user with: {kwargs}")
    return kwargs

user = create_user(name="Alice", role="admin", active=True)
# Output: Creating user with: {'name': 'Alice', 'role': 'admin', 'active': True}

# Kombinera båda
def flexible_func(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_func(1, 2, 3, name="test", value=42)
# Args: (1, 2, 3)
# Kwargs: {'name': 'test', 'value': 42}`
            },
            {
                title: "Dict/List Unpacking",
                description: "Packa upp datastrukturer med * och **",
                language: "python",
                code: `# Unpacking i funktionsanrop
def deploy(service, version, replicas=1):
    print(f"Deploying {service}:{version} with {replicas} replicas")

# Från dictionary
config = {"service": "nginx", "version": "1.25", "replicas": 3}
deploy(**config)  # Unpacking dict till kwargs

# Från lista
params = ["redis", "7.2"]
deploy(*params)  # Unpacking list till args

# Kombinera
base_config = {"version": "latest"}
deploy("postgres", **base_config, replicas=2)

# Merga dictionaries (Python 3.9+)
defaults = {"timeout": 30, "retries": 3}
overrides = {"retries": 5, "debug": True}
final = {**defaults, **overrides}  # {'timeout': 30, 'retries': 5, 'debug': True}`
            },
            {
                title: "Wrapper Functions & Decorators",
                description: "Forwarda arguments genom wrappers",
                language: "python",
                code: `import functools
import time

# Decorator som preservar original function signatur
def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # Forward alla args!
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.3f}s")
        return result
    return wrapper

@timing_decorator
def process_data(items, multiplier=1, verbose=False):
    if verbose:
        print(f"Processing {len(items)} items")
    return [x * multiplier for x in items]

# Wrapper som lägger till defaults
def with_defaults(func):
    default_kwargs = {"timeout": 30, "retry": True}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        merged = {**default_kwargs, **kwargs}
        return func(*args, **merged)
    return wrapper`
            }
        ],
        docsUrl: "https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments",
        flashcardCount: 8,
        quizCount: 6
    },
    {
        slug: "python-classes",
        name: "Python Classes",
        category: "python",
        icon: "🏛️",
        shortDesc: "Object-Oriented Python",
        description: "Python classes är grunden för objektorienterad programmering. Definierar objekt med attribut och metoder.",
        installation: {
            other: "Inbyggt i Python"
        },
        useCases: ["OOP", "Data modeling", "Encapsulation", "Inheritance", "Polymorphism"],
        keyFeatures: ["__init__", "self", "Inheritance", "Class methods", "Static methods", "Properties", "Dunder methods"],
        codeExamples: [
            {
                title: "Klass Grunderna",
                description: "Skapa klasser med attribut och metoder",
                language: "python",
                code: `class Server:
    """En server-klass för DevOps-hantering."""
    
    # Class attribute (delad av alla instanser)
    server_count = 0
    
    def __init__(self, hostname: str, ip: str, port: int = 22):
        # Instance attributes
        self.hostname = hostname
        self.ip = ip
        self.port = port
        self.status = "stopped"
        Server.server_count += 1
    
    def start(self):
        """Starta servern."""
        self.status = "running"
        print(f"{self.hostname} is now running")
    
    def stop(self):
        self.status = "stopped"
    
    def __str__(self):
        return f"Server({self.hostname} @ {self.ip})"
    
    def __repr__(self):
        return f"Server(hostname='{self.hostname}', ip='{self.ip}')"

# Användning
web = Server("web-01", "10.0.1.10")
db = Server("db-01", "10.0.1.20", port=5432)
web.start()
print(Server.server_count)  # 2`
            },
            {
                title: "Inheritance & Polymorphism",
                description: "Arv och metodöverlagring",
                language: "python",
                code: `from abc import ABC, abstractmethod

# Abstract base class
class Container(ABC):
    def __init__(self, name: str, image: str):
        self.name = name
        self.image = image
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class DockerContainer(Container):
    def start(self):
        print(f"docker run {self.image} --name {self.name}")
    
    def stop(self):
        print(f"docker stop {self.name}")

class PodmanContainer(Container):
    def start(self):
        print(f"podman run {self.image} --name {self.name}")
    
    def stop(self):
        print(f"podman stop {self.name}")

# Polymorphism - samma interface, olika implementation
def deploy_containers(containers: list[Container]):
    for c in containers:
        c.start()  # Anropar rätt implementation

containers = [
    DockerContainer("web", "nginx:alpine"),
    PodmanContainer("api", "python:3.11"),
]
deploy_containers(containers)`
            },
            {
                title: "Properties & Class Methods",
                description: "Avancerade attribut och metoder",
                language: "python",
                code: `from dataclasses import dataclass
from datetime import datetime

class Deployment:
    _deployments = []  # Class-level tracking
    
    def __init__(self, service: str, version: str):
        self._service = service
        self._version = version
        self._deployed_at = None
        Deployment._deployments.append(self)
    
    @property
    def service(self):
        """Getter - read-only access."""
        return self._service
    
    @property
    def version(self):
        return self._version
    
    @version.setter
    def version(self, value: str):
        """Setter med validering."""
        if not value:
            raise ValueError("Version cannot be empty")
        self._version = value
        self._deployed_at = datetime.now()
    
    @classmethod
    def get_all(cls) -> list:
        """Class method - tillgång till class state."""
        return cls._deployments
    
    @staticmethod
    def validate_version(version: str) -> bool:
        """Static method - ingen tillgång till self/cls."""
        import re
        return bool(re.match(r'^\\d+\\.\\d+\\.\\d+$', version))

# Användning
d = Deployment("nginx", "1.24.0")
d.version = "1.25.0"  # Använder setter
print(Deployment.get_all())  # Class method
print(Deployment.validate_version("1.0.0"))  # Static method`
            }
        ],
        docsUrl: "https://docs.python.org/3/tutorial/classes.html",
        flashcardCount: 15,
        quizCount: 12
    },
    {
        slug: "python-decorators",
        name: "Decorators",
        category: "python",
        icon: "🎀",
        shortDesc: "Function wrappers",
        description: "Decorators i Python är ett designmönster som låter dig modifiera funktioners beteende. Används för logging, caching, auth etc.",
        installation: {
            other: "Inbyggt i Python"
        },
        useCases: ["Logging", "Timing", "Caching", "Authentication", "Rate limiting", "Validation"],
        keyFeatures: ["@syntax", "Wrapper functions", "functools.wraps", "Chaining decorators", "Class decorators"],
        codeExamples: [
            {
                title: "Grundläggande Decorator",
                description: "Skapa och använda en enkel decorator",
                language: "python",
                code: `from functools import wraps

# Enkel decorator
def log_calls(func):
    @wraps(func)  # Behåll original funktionens metadata
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    """Add two numbers."""
    return a + b

# Samma som: add = log_calls(add)
result = add(2, 3)
# Output:
# Calling add with (2, 3), {}
# add returned 5`
            },
            {
                title: "Decorator med Argument",
                description: "Skapa parametriserade decorators",
                language: "python",
                code: `from functools import wraps
import time

# Decorator med argument
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    print(f"Attempt {attempts} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def fetch_data(url):
    # Kan kasta exception
    return requests.get(url).json()


# Timing decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper`
            },
            {
                title: "Praktiska Decorators",
                description: "Cache, auth och validation decorators",
                language: "python",
                code: `from functools import wraps, lru_cache

# Caching (inbyggd)
@lru_cache(maxsize=128)
def expensive_calculation(n):
    return sum(i**2 for i in range(n))


# Custom cache decorator
def cache(func):
    func._cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in func._cache:
            func._cache[args] = func(*args)
        return func._cache[args]
    return wrapper


# Authentication decorator
def require_auth(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionError("Authentication required")
        return func(request, *args, **kwargs)
    return wrapper


# Validation decorator
def validate_types(**type_hints):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for name, expected_type in type_hints.items():
                if name in kwargs:
                    if not isinstance(kwargs[name], expected_type):
                        raise TypeError(f"{name} must be {expected_type}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(age=int, name=str)
def create_user(name, age):
    return {"name": name, "age": age}`
            }
        ],
        docsUrl: "https://docs.python.org/3/glossary.html#term-decorator",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "virtualenv",
        name: "virtualenv",
        category: "python",
        icon: "📦",
        shortDesc: "Python virtual environments",
        description: "Virtual environments isolerar Python-projekt med egna dependencies. Förhindrar konflikter mellan projektens paket.",
        installation: {
            pip: "pip install virtualenv",
            other: "python -m venv (inbyggt)"
        },
        useCases: ["Project isolation", "Dependency management", "Testing", "Development environments"],
        keyFeatures: ["Isolerade environments", "requirements.txt", "activate/deactivate", "venv vs virtualenv"],
        docsUrl: "https://docs.python.org/3/library/venv.html",
        flashcardCount: 8,
        quizCount: 5
    },
    // VIRTUALIZATION
    {
        slug: "virtualbox",
        name: "VirtualBox",
        category: "virtualization",
        icon: "📟",
        shortDesc: "Desktop virtualization",
        description: "VirtualBox är en gratis virtualiseringsplattform från Oracle för att köra virtuella maskiner på din dator.",
        installation: {
            apt: "sudo apt install virtualbox",
            brew: "brew install --cask virtualbox"
        },
        useCases: ["Lokala VMs", "Testing", "Utvecklingsmiljöer", "Multi-OS testing", "Snapshots"],
        keyFeatures: ["Cross-platform", "Snapshots", "Shared folders", "Networking modes", "Guest additions"],
        officialUrl: "https://www.virtualbox.org",
        docsUrl: "https://www.virtualbox.org/manual/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "vagrant",
        name: "Vagrant",
        category: "virtualization",
        icon: "📦",
        shortDesc: "VM workflow automation",
        description: "Vagrant automatiserar skapande och hantering av virtuella utvecklingsmiljöer. Infrastructure as Code för VMs.",
        installation: {
            brew: "brew install vagrant",
            other: "https://www.vagrantup.com/downloads"
        },
        useCases: ["Reproducerbara miljöer", "Team development", "Testing infrastructure", "Local Kubernetes"],
        keyFeatures: ["Vagrantfile", "Boxes", "Provisioning", "Multi-machine", "Synced folders", "Port forwarding"],
        officialUrl: "https://www.vagrantup.com",
        docsUrl: "https://developer.hashicorp.com/vagrant/docs",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "kvm",
        name: "KVM",
        category: "virtualization",
        icon: "🖥️",
        shortDesc: "Linux kernel virtualization",
        description: "KVM (Kernel-based Virtual Machine) är en Linux-kernelmodul för full virtualisering. Höga prestanda, används i molntjänster.",
        installation: {
            apt: "sudo apt install qemu-kvm libvirt-daemon-system"
        },
        useCases: ["Server virtualization", "Cloud infrastructure", "High-performance VMs", "Live migration"],
        keyFeatures: ["Hardware-assisted", "QEMU integration", "libvirt", "Live migration", "Snapshots"],
        officialUrl: "https://www.linux-kvm.org",
        docsUrl: "https://www.linux-kvm.org/page/Documents",
        flashcardCount: 10,
        quizCount: 6
    },
    // CLOUD & IAC
    {
        slug: "terraform",
        name: "Terraform",
        category: "cloud",
        icon: "🏗️",
        shortDesc: "Infrastructure as Code",
        description: "Terraform är ett IaC-verktyg från HashiCorp för att bygga, ändra och versionshantera infrastruktur säkert och effektivt.",
        installation: {
            brew: "brew install terraform",
            other: "https://developer.hashicorp.com/terraform/downloads"
        },
        useCases: ["Cloud provisioning", "Multi-cloud", "Infrastructure versioning", "State management"],
        keyFeatures: ["HCL syntax", "Providers", "State", "Modules", "Plan/Apply", "Workspaces"],
        codeExamples: [
            {
                title: "AWS EC2 Instance",
                description: "Skapa en EC2-instans med Terraform",
                language: "hcl",
                code: `# Provider configuration
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "eu-north-1"
}

# Variables
variable "instance_type" {
  default = "t3.micro"
}

# EC2 Instance
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type

  tags = {
    Name        = "WebServer"
    Environment = "production"
  }
}

# Output
output "public_ip" {
  value = aws_instance.web.public_ip
}`
            },
            {
                title: "Terraform Modules",
                description: "Skapa återanvändbara moduler",
                language: "hcl",
                code: `# modules/vpc/main.tf
variable "cidr_block" {
  description = "CIDR block for VPC"
  type        = string
}

variable "environment" {
  type = string
}

resource "aws_vpc" "main" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = true

  tags = {
    Name = "\${var.environment}-vpc"
  }
}

output "vpc_id" {
  value = aws_vpc.main.id
}

# main.tf - använd modulen
module "production_vpc" {
  source      = "./modules/vpc"
  cidr_block  = "10.0.0.0/16"
  environment = "production"
}

module "staging_vpc" {
  source      = "./modules/vpc"
  cidr_block  = "10.1.0.0/16"
  environment = "staging"
}`
            },
            {
                title: "Terraform Kommandon",
                description: "Vanliga Terraform CLI-kommandon",
                language: "bash",
                code: `# Initiera projekt (ladda providers)
terraform init

# Formatera kod
terraform fmt -recursive

# Validera konfiguration
terraform validate

# Visa planerade ändringar
terraform plan

# Applicera ändringar
terraform apply

# Applicera utan bekräftelse
terraform apply -auto-approve

# Visa nuvarande state
terraform show

# Lista resurser
terraform state list

# Ta bort specifik resurs från state
terraform state rm aws_instance.web

# Importera befintlig resurs
terraform import aws_instance.web i-1234567890

# Förstör all infrastruktur
terraform destroy

# Workspace-hantering
terraform workspace list
terraform workspace new staging
terraform workspace select production`
            }
        ],
        officialUrl: "https://www.terraform.io",
        docsUrl: "https://developer.hashicorp.com/terraform/docs",
        flashcardCount: 20,
        quizCount: 15
    },
    {
        slug: "ansible",
        name: "Ansible",
        category: "cloud",
        icon: "🔧",
        shortDesc: "Configuration management",
        description: "Ansible är ett agentless automatiseringsverktyg för configuration management, application deployment och task automation.",
        installation: {
            pip: "pip install ansible",
            apt: "sudo apt install ansible"
        },
        useCases: ["Configuration management", "App deployment", "Orchestration", "Provisioning", "Security compliance"],
        keyFeatures: ["Agentless", "YAML playbooks", "Inventory", "Modules", "Roles", "Galaxy", "Idempotent"],
        codeExamples: [
            {
                title: "Ansible Playbook",
                description: "Installera och konfigurera Nginx på servrar",
                language: "yaml",
                code: `---
- name: Configure Web Servers
  hosts: webservers
  become: yes
  vars:
    http_port: 80
    app_name: myapp

  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
        cache_valid_time: 3600

    - name: Install Nginx
      apt:
        name: nginx
        state: present

    - name: Copy Nginx config
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/sites-available/default
      notify: Restart Nginx

    - name: Ensure Nginx is running
      service:
        name: nginx
        state: started
        enabled: yes

  handlers:
    - name: Restart Nginx
      service:
        name: nginx
        state: restarted`
            },
            {
                title: "Ansible Inventory",
                description: "Definiera hosts och grupper",
                language: "ini",
                code: `# inventory/hosts.ini

[webservers]
web1.example.com ansible_host=10.0.1.10
web2.example.com ansible_host=10.0.1.11

[databases]
db1.example.com ansible_host=10.0.2.10

# Gruppering av grupper
` + `[production` + `:children]` + `
webservers
databases

# Variabler för production-gruppen
` + `[production` + `:vars]` + `
ansible_user=deploy
ansible_ssh_private_key_file=~/.ssh/deploy_key
env=production

# Globala variabler för alla hosts
` + `[all` + `:vars]` + `
ansible_python_interpreter=/usr/bin/python3`
            },
            {
                title: "Ansible Kommandon",
                description: "Vanliga ansible CLI-kommandon",
                language: "bash",
                code: `# Ad-hoc kommandon
ansible all -m ping
ansible webservers -m shell -a "uptime"
ansible all -m apt -a "name=vim state=present" --become

# Kör playbook
ansible-playbook site.yml

# Kör med inventory
ansible-playbook -i inventory/prod site.yml

# Begränsa till specifika hosts
ansible-playbook site.yml --limit webservers

# Kör specifika tags
ansible-playbook site.yml --tags "nginx,deploy"

# Check mode (dry run)
ansible-playbook site.yml --check

# Verbose output
ansible-playbook site.yml -vvv

# Lista tasks
ansible-playbook site.yml --list-tasks

# Vault för hemligheter
ansible-vault create secrets.yml
ansible-vault edit secrets.yml
ansible-playbook site.yml --ask-vault-pass`
            }
        ],
        officialUrl: "https://www.ansible.com",
        docsUrl: "https://docs.ansible.com",
        flashcardCount: 18,
        quizCount: 12
    },
    {
        slug: "aws-cli",
        name: "AWS CLI",
        category: "cloud",
        icon: "☁️",
        shortDesc: "Amazon Web Services CLI",
        description: "AWS CLI är kommandoradsverktyget för att hantera AWS-tjänster. Automatisera och scripta din molninfrastruktur.",
        installation: {
            pip: "pip install awscli",
            brew: "brew install awscli"
        },
        useCases: ["AWS management", "Automation", "CI/CD integration", "Scripting", "Resource management"],
        keyFeatures: ["Profiles", "Output formats", "S3 sync", "Query filtering", "MFA support"],
        officialUrl: "https://aws.amazon.com/cli/",
        docsUrl: "https://docs.aws.amazon.com/cli/",
        flashcardCount: 15,
        quizCount: 10
    },
    // CI/CD
    {
        slug: "github-actions",
        name: "GitHub Actions",
        category: "cicd",
        icon: "🐙",
        shortDesc: "GitHub CI/CD",
        description: "GitHub Actions automatiserar software workflows direkt i GitHub. Build, test och deploy från ditt repository.",
        installation: {
            other: "Aktiveras i .github/workflows/"
        },
        useCases: ["CI/CD pipelines", "Automated testing", "Deployment", "Issue management", "Code review automation"],
        keyFeatures: ["Workflows", "Jobs", "Steps", "Actions marketplace", "Matrix builds", "Secrets", "Environments"],
        codeExamples: [
            {
                title: "CI/CD Pipeline",
                description: "Komplett pipeline för Node.js-projekt",
                language: "yaml",
                code: `# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '20'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: \${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run linting
        run: npm run lint

      - name: Run tests
        run: npm test -- --coverage

      - name: Upload coverage
        uses: codecov/codecov-action@v3

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Docker image
        run: |
          docker build -t myapp:\${{ github.sha }} .

      - name: Push to Registry
        if: github.ref == 'refs/heads/main'
        run: |
          echo \${{ secrets.DOCKER_PASSWORD }} | docker login -u \${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker push myapp:\${{ github.sha }}`
            },
            {
                title: "Matrix Testing",
                description: "Testa på flera versioner och plattformar",
                language: "yaml",
                code: `name: Matrix Test

on: [push, pull_request]

jobs:
  test:
    runs-on: \${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node: [18, 20, 22]
        exclude:
          - os: windows-latest
            node: 18
      fail-fast: false

    steps:
      - uses: actions/checkout@v4

      - name: Use Node.js \${{ matrix.node }}
        uses: actions/setup-node@v4
        with:
          node-version: \${{ matrix.node }}

      - run: npm ci
      - run: npm test

      - name: Upload results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: results-\${{ matrix.os }}-\${{ matrix.node }}
          path: test-results/`
            },
            {
                title: "Reusable Workflow",
                description: "Skapa återanvändbara workflows",
                language: "yaml",
                code: `# .github/workflows/reusable-deploy.yml
name: Reusable Deploy

on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
      app_version:
        required: true
        type: string
    secrets:
      deploy_key:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: \${{ inputs.environment }}
    steps:
      - name: Deploy to \${{ inputs.environment }}
        run: |
          echo "Deploying version \${{ inputs.app_version }}"
          # Deploy script here

# .github/workflows/main.yml - använd den
name: Main Pipeline
on:
  push:
    branches: [main]

jobs:
  deploy-staging:
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: staging
      app_version: \${{ github.sha }}
    secrets:
      deploy_key: \${{ secrets.STAGING_DEPLOY_KEY }}`
            }
        ],
        officialUrl: "https://github.com/features/actions",
        docsUrl: "https://docs.github.com/en/actions",
        flashcardCount: 18,
        quizCount: 12
    },
    {
        slug: "gitlab-ci",
        name: "GitLab CI/CD",
        category: "cicd",
        icon: "🦊",
        shortDesc: "GitLab pipelines",
        description: "GitLab CI/CD är inbyggt i GitLab för automatiserad build, test och deployment. Definieras i .gitlab-ci.yml.",
        installation: {
            other: "Aktiveras med .gitlab-ci.yml"
        },
        useCases: ["CI/CD pipelines", "Auto DevOps", "Container registry", "Deployment", "Security scanning"],
        keyFeatures: ["Stages", "Jobs", "Runners", "Artifacts", "Environments", "Auto DevOps", "Parent-child pipelines"],
        officialUrl: "https://docs.gitlab.com/ee/ci/",
        docsUrl: "https://docs.gitlab.com/ee/ci/yaml/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "jenkins",
        name: "Jenkins",
        category: "cicd",
        icon: "🎩",
        shortDesc: "Automation server",
        description: "Jenkins är en open-source automation server för att bygga, testa och deploya software. Extremt utbyggbart med plugins.",
        installation: {
            apt: "sudo apt install jenkins",
            brew: "brew install jenkins"
        },
        useCases: ["CI/CD pipelines", "Build automation", "Deployment", "Scheduled jobs", "Multi-platform builds"],
        keyFeatures: ["Pipelines (Jenkinsfile)", "Plugins", "Distributed builds", "Blue Ocean UI", "Credentials management"],
        officialUrl: "https://www.jenkins.io",
        docsUrl: "https://www.jenkins.io/doc/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "argocd",
        name: "ArgoCD",
        category: "cicd",
        icon: "🐙",
        shortDesc: "GitOps for Kubernetes",
        description: "ArgoCD är ett deklarativt GitOps continuous delivery-verktyg för Kubernetes. Synkar Git-state till klustret.",
        installation: {
            other: "kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml"
        },
        useCases: ["GitOps", "Kubernetes deployments", "Multi-cluster", "Application management", "Rollbacks"],
        keyFeatures: ["GitOps", "Application CRD", "Sync", "Health status", "Rollback", "SSO", "RBAC"],
        officialUrl: "https://argo-cd.readthedocs.io",
        docsUrl: "https://argo-cd.readthedocs.io/en/stable/",
        flashcardCount: 12,
        quizCount: 8
    },
    // MONITORING
    {
        slug: "prometheus",
        name: "Prometheus",
        category: "monitoring",
        icon: "🔥",
        shortDesc: "Metrics & monitoring",
        description: "Prometheus är ett monitoring och alerting toolkit. Pull-baserat system med kraftfull query language (PromQL).",
        installation: {
            brew: "brew install prometheus",
            other: "docker run prom/prometheus"
        },
        useCases: ["Metrics collection", "Alerting", "Kubernetes monitoring", "Application monitoring", "Infrastructure monitoring"],
        keyFeatures: ["Pull-based", "PromQL", "Alertmanager", "Service discovery", "Exporters", "Federation"],
        codeExamples: [
            {
                title: "Prometheus Config",
                description: "Grundläggande prometheus.yml konfiguration",
                language: "yaml",
                code: `# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - alertmanager:9093

rule_files:
  - "alerts/*.yml"

scrape_configs:
  # Prometheus själv
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Node Exporter
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']

  # Kubernetes pods (auto-discovery)
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)`
            },
            {
                title: "PromQL Queries",
                description: "Vanliga PromQL-frågor för metrics",
                language: "promql",
                code: `# CPU-användning per nod
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Minnesanvändning
(1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100

# HTTP request rate
rate(http_requests_total[5m])

# Request latency (p99)
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))

# Error rate
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) * 100

# Top 5 containers by CPU
topk(5, sum by(container) (rate(container_cpu_usage_seconds_total[5m])))

# Pod restarts
sum by(pod) (kube_pod_container_status_restarts_total)

# Disk space
(node_filesystem_size_bytes - node_filesystem_avail_bytes) / node_filesystem_size_bytes * 100`
            },
            {
                title: "Alert Rules",
                description: "Definiera alerts för Alertmanager",
                language: "yaml",
                code: `# alerts/node.yml
groups:
  - name: node-alerts
    rules:
      - alert: HighCpuUsage
        expr: 100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage on {{ $labels.instance }}"
          description: "CPU usage is {{ $value }}%"

      - alert: HighMemoryUsage
        expr: (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100 > 85
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High memory usage on {{ $labels.instance }}"

      - alert: DiskSpaceRunningLow
        expr: (node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100 < 15
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Low disk space on {{ $labels.mountpoint }}"`
            }
        ],
        officialUrl: "https://prometheus.io",
        docsUrl: "https://prometheus.io/docs/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "grafana",
        name: "Grafana",
        category: "monitoring",
        icon: "📊",
        shortDesc: "Visualization & dashboards",
        description: "Grafana är en plattform för monitoring och observability. Visualisera metrics, logs och traces med vackra dashboards.",
        installation: {
            apt: "sudo apt install grafana",
            brew: "brew install grafana"
        },
        useCases: ["Dashboards", "Alerting", "Data visualization", "Log analysis", "Metrics exploration"],
        keyFeatures: ["Datasources", "Dashboards", "Panels", "Alerting", "Annotations", "Variables", "Plugins"],
        officialUrl: "https://grafana.com",
        docsUrl: "https://grafana.com/docs/",
        flashcardCount: 12,
        quizCount: 8
    },
    // NETWORK
    {
        slug: "ssh",
        name: "SSH",
        category: "network",
        icon: "🔐",
        shortDesc: "Secure Shell",
        description: "SSH (Secure Shell) är ett protokoll för säker kommunikation över osäkra nätverk. Standard för remote access.",
        installation: {
            apt: "sudo apt install openssh-client",
            other: "Förinstallerat på de flesta system"
        },
        useCases: ["Remote access", "File transfer (SCP/SFTP)", "Tunneling", "Port forwarding", "Git authentication"],
        keyFeatures: ["Public key auth", "Config file", "Agent forwarding", "Tunneling", "Jump hosts", "SCP/SFTP"],
        codeExamples: [
            {
                title: "SSH Nycklar",
                description: "Generera och hantera SSH-nycklar",
                language: "bash",
                code: `# Generera ny SSH-nyckel (Ed25519 rekommenderas)
ssh-keygen -t ed25519 -C "din@email.com"

# Eller RSA 4096-bit
ssh-keygen -t rsa -b 4096 -C "din@email.com"

# Kopiera publik nyckel till server
ssh-copy-id user@server.com

# Manuellt (om ssh-copy-id saknas)
cat ~/.ssh/id_ed25519.pub | ssh user@server 'cat >> ~/.ssh/authorized_keys'

# Lista fingerprints
ssh-keygen -l -f ~/.ssh/id_ed25519.pub

# Starta ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Lista tillagda nycklar
ssh-add -l`
            },
            {
                title: "SSH Config",
                description: "Konfigurera ~/.ssh/config för enklare anslutning",
                language: "bash",
                code: `# ~/.ssh/config

# Generella inställningar
Host *
    AddKeysToAgent yes
    IdentitiesOnly yes
    ServerAliveInterval 60

# Produktionsserver
Host prod
    HostName 10.0.1.10
    User deploy
    IdentityFile ~/.ssh/deploy_key
    Port 22

# Via jump host (bastion)
Host internal-server
    HostName 192.168.1.100
    User admin
    ProxyJump bastion

Host bastion
    HostName bastion.example.com
    User jump-user
    IdentityFile ~/.ssh/bastion_key

# GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/github_key

# Användning:
# ssh prod              (istället för ssh deploy@10.0.1.10)
# ssh internal-server   (via bastion automatiskt)`
            },
            {
                title: "SSH Tunneling & Port Forward",
                description: "Skapa tunnlar och vidarebefordra portar",
                language: "bash",
                code: `# Local port forward (nå remote service lokalt)
# Nå remote-db:5432 via localhost:5433
ssh -L 5433:remote-db:5432 user@server

# Remote port forward (exponera lokal service)
# Exponera localhost:3000 på server:8080
ssh -R 8080:localhost:3000 user@server

# Dynamic port forward (SOCKS proxy)
ssh -D 1080 user@server
# Använd SOCKS proxy på localhost:1080

# SSH tunnel i bakgrunden
ssh -fN -L 5433:db:5432 user@server

# SCP - kopiera filer
scp file.txt user@server:/path/          # Upload
scp user@server:/path/file.txt .         # Download
scp -r folder/ user@server:/path/        # Rekursivt

# SFTP - interaktiv filöverföring
sftp user@server
# > put local.txt
# > get remote.txt
# > ls, cd, pwd, etc.`
            }
        ],
        docsUrl: "https://www.openssh.com/manual.html",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "ssl-tls",
        name: "SSL/TLS",
        category: "network",
        icon: "🔒",
        shortDesc: "Transport Layer Security",
        description: "TLS (och dess föregångare SSL) säkrar kommunikation över internet. Grund för HTTPS och säker datautbyte.",
        installation: {
            apt: "sudo apt install openssl"
        },
        useCases: ["HTTPS", "Secure APIs", "Email encryption", "VPN", "Certificate management"],
        keyFeatures: ["Certificates", "Certificate chains", "Let's Encrypt", "Certificate authorities", "TLS handshake"],
        officialUrl: "https://www.openssl.org",
        docsUrl: "https://www.openssl.org/docs/",
        flashcardCount: 12,
        quizCount: 8
    },
    // DATABASE
    {
        slug: "postgresql",
        name: "PostgreSQL",
        category: "database",
        icon: "🐘",
        shortDesc: "Relational database",
        description: "PostgreSQL är en kraftfull, open-source relationsdatabas med avancerade features som JSON-stöd och full-text search.",
        installation: {
            apt: "sudo apt install postgresql",
            brew: "brew install postgresql"
        },
        useCases: ["Web applications", "Data warehousing", "Geospatial data", "OLTP", "Analytics"],
        keyFeatures: ["ACID", "JSON/JSONB", "Full-text search", "Extensions", "Replication", "Partitioning"],
        codeExamples: [
            {
                title: "PostgreSQL Grundkommandon",
                description: "Vanliga psql-kommandon och SQL",
                language: "sql",
                code: `-- Anslut till databas
-- psql -U postgres -d mydb

-- Skapa databas och användare
CREATE DATABASE myapp;
CREATE USER appuser WITH ENCRYPTED PASSWORD 'secret';
GRANT ALL PRIVILEGES ON DATABASE myapp TO appuser;

-- Skapa tabell
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(100),
    data JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Index för prestanda
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_data ON users USING GIN(data);

-- CRUD operationer
INSERT INTO users (email, name, data)
VALUES ('test@example.com', 'Test', '{"role": "admin"}');

SELECT * FROM users WHERE data->>'role' = 'admin';

UPDATE users SET name = 'Updated' WHERE email = 'test@example.com';

DELETE FROM users WHERE id = 1;`
            },
            {
                title: "psql Meta-kommandon",
                description: "Navigera i psql-klienten",
                language: "bash",
                code: `# Anslut till databas
psql -h localhost -U postgres -d mydb

# Meta-kommandon i psql
\\l              # Lista databaser
\\c mydb         # Byt databas
\\dt             # Lista tabeller
\\d users        # Beskriv tabell
\\di             # Lista index
\\du             # Lista användare
\\df             # Lista funktioner

\\x              # Expanded output (toggle)
\\timing         # Visa query timing
\\e              # Editera query i editor
\\i file.sql     # Kör SQL-fil

\\q              # Avsluta psql

# Backup och restore
pg_dump mydb > backup.sql
pg_dump -Fc mydb > backup.dump    # Custom format
pg_restore -d mydb backup.dump

# Export till CSV
\\copy (SELECT * FROM users) TO 'users.csv' CSV HEADER`
            },
            {
                title: "Avancerade Features",
                description: "JSON, CTE och Window functions",
                language: "sql",
                code: `-- JSONB queries
SELECT name, data->>'role' as role
FROM users
WHERE data @> '{"active": true}';

-- Update JSON field
UPDATE users
SET data = jsonb_set(data, '{settings,theme}', '"dark"')
WHERE id = 1;

-- Common Table Expression (CTE)
WITH active_users AS (
    SELECT * FROM users
    WHERE data->>'active' = 'true'
)
SELECT COUNT(*) FROM active_users;

-- Window functions
SELECT
    name,
    created_at,
    ROW_NUMBER() OVER (ORDER BY created_at) as row_num,
    RANK() OVER (PARTITION BY data->>'role' ORDER BY created_at) as rank_in_role
FROM users;

-- Full-text search
ALTER TABLE users ADD COLUMN search_vector tsvector;
UPDATE users SET search_vector = to_tsvector('swedish', name || ' ' || email);
CREATE INDEX idx_search ON users USING GIN(search_vector);

SELECT * FROM users
WHERE search_vector @@ to_tsquery('swedish', 'admin');`
            }
        ],
        officialUrl: "https://www.postgresql.org",
        docsUrl: "https://www.postgresql.org/docs/",
        flashcardCount: 18,
        quizCount: 12
    },
    {
        slug: "redis",
        name: "Redis",
        category: "database",
        icon: "🔴",
        shortDesc: "In-memory data store",
        description: "Redis är en in-memory data structure store. Används som databas, cache och message broker med extremt snabb prestanda.",
        installation: {
            apt: "sudo apt install redis-server",
            brew: "brew install redis"
        },
        useCases: ["Caching", "Session storage", "Real-time analytics", "Message queues", "Leaderboards", "Rate limiting"],
        keyFeatures: ["In-memory", "Data structures", "Pub/Sub", "Lua scripting", "Cluster", "Persistence"],
        codeExamples: [
            {
                title: "Redis CLI Grundkommandon",
                description: "Grundläggande operationer med redis-cli",
                language: "bash",
                code: `# Anslut till Redis
redis-cli
redis-cli -h hostname -p 6379 -a password

# Strings
SET user:1:name "Alice"
GET user:1:name
SETEX session:abc 3600 "data"    # Expires efter 1h
INCR counter                     # Atomic increment
MSET key1 "val1" key2 "val2"     # Multiple set
MGET key1 key2

# Keys
KEYS user:*                      # Hitta keys (VARNING: blocking)
SCAN 0 MATCH user:* COUNT 100   # Bättre för produktion
EXISTS key1
DEL key1 key2
EXPIRE key1 60                   # Set TTL
TTL key1                         # Check TTL

# Server
INFO
DBSIZE
FLUSHDB                          # Clear current DB
FLUSHALL                         # Clear ALL DBs (farligt!)`
            },
            {
                title: "Datastrukturer",
                description: "Hashes, Lists, Sets och Sorted Sets",
                language: "bash",
                code: `# Hashes (objekt-liknande)
HSET user:1 name "Alice" email "alice@example.com" age 30
HGET user:1 name
HGETALL user:1
HINCRBY user:1 age 1

# Lists (köer)
LPUSH queue:jobs "job1"          # Lägg till i början
RPUSH queue:jobs "job2"          # Lägg till i slutet
LPOP queue:jobs                  # Ta från början
RPOP queue:jobs                  # Ta från slutet
LRANGE queue:jobs 0 -1           # Visa alla
BRPOP queue:jobs 30              # Blocking pop (30s timeout)

# Sets (unika värden)
SADD online:users "user:1" "user:2"
SMEMBERS online:users
SISMEMBER online:users "user:1"
SCARD online:users               # Count

# Sorted Sets (med score)
ZADD leaderboard 100 "player1" 85 "player2" 120 "player3"
ZRANGE leaderboard 0 -1 WITHSCORES
ZREVRANGE leaderboard 0 2 WITHSCORES  # Top 3
ZINCRBY leaderboard 10 "player1"`
            },
            {
                title: "Pub/Sub & Caching Pattern",
                description: "Real-time messaging och cache patterns",
                language: "bash",
                code: `# Pub/Sub
# Terminal 1: Subscriber
SUBSCRIBE news:sports news:tech

# Terminal 2: Publisher
PUBLISH news:sports "Match result: 2-1"

# Pattern subscribe
PSUBSCRIBE news:*

# Cache-Aside Pattern (pseudokod)
# 1. Kolla cache
# GET user:123
# 2. Om cache miss, hämta från DB
# 3. Spara i cache
# SETEX user:123 3600 "{json_data}"

# Rate Limiting Pattern
# INCR rate:user:123:minute
# EXPIRE rate:user:123:minute 60
# Om count > limit => reject

# Session Storage
SETEX session:abc123 86400 '{"user_id": 1, "role": "admin"}'
GET session:abc123
DEL session:abc123  # Logout`
            }
        ],
        officialUrl: "https://redis.io",
        docsUrl: "https://redis.io/docs/",
        flashcardCount: 15,
        quizCount: 10
    },
    // GIT
    {
        slug: "git",
        name: "Git",
        category: "cicd",
        icon: "📚",
        shortDesc: "Version control",
        description: "Git är det distribuerade versionshanteringssystemet som används av miljontals utvecklare. Grund för GitHub, GitLab etc.",
        installation: {
            apt: "sudo apt install git",
            brew: "brew install git"
        },
        useCases: ["Version control", "Collaboration", "Code review", "Branch management", "CI/CD integration"],
        keyFeatures: ["Branches", "Merge/Rebase", "Commits", "Tags", "Remote repos", "Hooks", "Submodules"],
        codeExamples: [
            {
                title: "Git Grundkommandon",
                description: "Vanliga Git-operationer för dagligt bruk",
                language: "bash",
                code: `# Konfigurera Git
git config --global user.name "Ditt Namn"
git config --global user.email "din@email.com"

# Skapa nytt repo
git init
git add .
git commit -m "Initial commit"

# Klona repo
git clone https://github.com/user/repo.git
git clone git@github.com:user/repo.git

# Dagligt arbete
git status
git diff
git add -p                    # Interaktiv staging
git commit -m "feat: add login"
git push origin main

# Hämta ändringar
git fetch origin
git pull origin main
git pull --rebase origin main`
            },
            {
                title: "Branching & Merging",
                description: "Arbeta med branches och merge",
                language: "bash",
                code: `# Skapa och byt branch
git branch feature/login
git checkout feature/login
# Eller kombinerat:
git checkout -b feature/login

# Lista branches
git branch -a                 # Alla branches
git branch -r                 # Remote branches

# Merge branch
git checkout main
git merge feature/login
git branch -d feature/login   # Ta bort lokal branch

# Rebase (renare historik)
git checkout feature/login
git rebase main
git checkout main
git merge feature/login       # Fast-forward merge

# Resolve conflicts
git merge feature/login
# Editera konfliktfiler
git add .
git commit -m "Merge feature/login"

# Avbryt merge
git merge --abort`
            },
            {
                title: "Avancerade Operationer",
                description: "Stash, reset, revert och mer",
                language: "bash",
                code: `# Stash (spara ändringar temporärt)
git stash
git stash save "WIP: login feature"
git stash list
git stash pop                 # Återställ senaste
git stash apply stash@{1}     # Återställ specifik

# Ångra ändringar
git checkout -- file.txt      # Återställ fil
git reset HEAD file.txt       # Unstage fil
git reset --soft HEAD~1       # Ångra commit, behåll ändringar
git reset --hard HEAD~1       # Ångra commit, ta bort ändringar

# Revert (säker undo i historik)
git revert abc123             # Skapa ny commit som ångrar

# Cherry-pick (plocka specifik commit)
git cherry-pick abc123

# Interactive rebase
git rebase -i HEAD~3          # Editera/squash commits

# Blame (vem skrev vad)
git blame file.txt

# Log
git log --oneline --graph
git log --author="namn" --since="1 week ago"`
            }
        ],
        officialUrl: "https://git-scm.com",
        docsUrl: "https://git-scm.com/doc",
        flashcardCount: 20,
        quizCount: 15
    },
    // ============================================================================
    // DEL 1: CLI & TERMINAL-VERKTYG (20 verktyg)
    // ============================================================================
    {
        slug: "curl",
        name: "cURL",
        category: "linux",
        icon: "🌐",
        shortDesc: "Data transfer tool",
        description: "cURL är ett kommandoradsverktyg för att överföra data med URL-syntax. Stödjer HTTP, HTTPS, FTP och många fler protokoll.",
        installation: {
            apt: "sudo apt install curl",
            brew: "brew install curl"
        },
        useCases: ["API testing", "File downloads", "HTTP requests", "Webhooks", "Scripting"],
        keyFeatures: ["-X method", "-H headers", "-d data", "-o output", "-v verbose", "Cookie handling"],
        codeExamples: [
            {
                title: "HTTP Requests",
                description: "Grundläggande HTTP-anrop med curl",
                language: "bash",
                code: `# GET request
curl https://api.example.com/users

# GET med headers
curl -H "Authorization: Bearer token123" \\
     -H "Accept: application/json" \\
     https://api.example.com/users

# POST med JSON body
curl -X POST \\
     -H "Content-Type: application/json" \\
     -d '{"name": "Test", "email": "test@example.com"}' \\
     https://api.example.com/users

# POST med form data
curl -X POST \\
     -d "username=admin&password=secret" \\
     https://api.example.com/login

# PUT request
curl -X PUT \\
     -H "Content-Type: application/json" \\
     -d '{"name": "Updated"}' \\
     https://api.example.com/users/1

# DELETE request
curl -X DELETE https://api.example.com/users/1`
            },
            {
                title: "Avancerade Options",
                description: "Debugging, auth och filhantering",
                language: "bash",
                code: `# Verbose output (debugging)
curl -v https://api.example.com/health

# Visa endast headers
curl -I https://example.com

# Spara response till fil
curl -o output.json https://api.example.com/data
curl -O https://example.com/file.zip  # Behåll filnamn

# Basic auth
curl -u username:password https://api.example.com/secure

# Bearer token
curl -H "Authorization: Bearer \$TOKEN" https://api.example.com/me

# Cookies
curl -c cookies.txt https://example.com/login  # Spara cookies
curl -b cookies.txt https://example.com/dashboard  # Använd cookies

# Follow redirects
curl -L https://short.url/abc

# Timeout
curl --connect-timeout 5 --max-time 30 https://api.example.com`
            },
            {
                title: "API Testing Scripts",
                description: "Praktiska one-liners för API-testning",
                language: "bash",
                code: `# Formatera JSON output (med jq)
curl -s https://api.example.com/users | jq '.'

# POST JSON från fil
curl -X POST \\
     -H "Content-Type: application/json" \\
     -d @payload.json \\
     https://api.example.com/users

# Upload fil
curl -X POST \\
     -F "file=@document.pdf" \\
     -F "description=My file" \\
     https://api.example.com/upload

# Retry på failure
curl --retry 3 --retry-delay 5 https://api.example.com

# Mät response time
curl -w "\\nTime: %{time_total}s\\n" -o /dev/null -s https://example.com

# Test webhook lokalt
curl -X POST \\
     -H "Content-Type: application/json" \\
     -d '{"event": "test", "data": {"id": 123}}' \\
     http://localhost:3000/webhook`
            }
        ],
        officialUrl: "https://curl.se",
        docsUrl: "https://curl.se/docs/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "wget",
        name: "Wget",
        category: "linux",
        icon: "📥",
        shortDesc: "Network downloader",
        description: "Wget är ett verktyg för att ladda ner filer från webben. Stödjer HTTP, HTTPS och FTP med resume-funktion.",
        installation: {
            apt: "sudo apt install wget",
            brew: "brew install wget"
        },
        useCases: ["File downloads", "Website mirroring", "Recursive downloads", "Background downloads"],
        keyFeatures: ["-r recursive", "-c continue", "-b background", "--mirror", "-O output", "-q quiet"],
        officialUrl: "https://www.gnu.org/software/wget/",
        docsUrl: "https://www.gnu.org/software/wget/manual/",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "grep",
        name: "grep",
        category: "linux",
        icon: "🔍",
        shortDesc: "Pattern matching",
        description: "grep söker efter mönster i text och filer. Ett av de mest använda Linux-verktygen för textbearbetning.",
        installation: {
            apt: "sudo apt install grep",
            other: "Förinstallerat på de flesta system"
        },
        useCases: ["Log analysis", "Code search", "Pattern matching", "Filtering output", "Pipeline processing"],
        keyFeatures: ["-r recursive", "-i ignore case", "-n line numbers", "-E regex", "-v invert", "-c count"],
        codeExamples: [
            {
                title: "Grundläggande Sökning",
                description: "Vanliga grep-mönster och options",
                language: "bash",
                code: `# Sök i fil
grep "error" logfile.txt

# Case-insensitive
grep -i "error" logfile.txt

# Visa radnummer
grep -n "error" logfile.txt

# Rekursiv sökning i katalog
grep -r "TODO" ./src

# Inkludera bara vissa filer
grep -r --include="*.py" "import" ./

# Exkludera filer/kataloger
grep -r --exclude-dir=node_modules "function" ./

# Visa endast matchande filnamn
grep -l "error" *.log

# Räkna matchningar
grep -c "error" logfile.txt`
            },
            {
                title: "Regex & Extended grep",
                description: "Använd reguljära uttryck med grep",
                language: "bash",
                code: `# Extended regex (-E eller egrep)
grep -E "error|warning|critical" logfile.txt

# Matcha början av rad
grep "^Error" logfile.txt

# Matcha slutet av rad
grep "failed$" logfile.txt

# Matcha hela ord
grep -w "error" logfile.txt  # Matchar inte "errors"

# IP-adresser
grep -E "([0-9]{1,3}\\.){3}[0-9]{1,3}" access.log

# Email-adresser
grep -E "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}" file.txt

# Datum format (YYYY-MM-DD)
grep -E "[0-9]{4}-[0-9]{2}-[0-9]{2}" logfile.txt`
            },
            {
                title: "Praktiska Exempel",
                description: "Grep i pipelines och scripts",
                language: "bash",
                code: `# Filtrera ps output
ps aux | grep nginx | grep -v grep

# Sök i loggar efter errors de senaste 24h
grep "$(date -d '1 day ago' +%Y-%m-%d)" error.log | grep -i error

# Visa kontext (rader före/efter)
grep -B 3 -A 3 "error" logfile.txt  # 3 rader före och efter
grep -C 5 "error" logfile.txt       # 5 rader kontext

# Invert match (allt UTOM pattern)
grep -v "DEBUG" application.log

# Multiple patterns från fil
grep -f patterns.txt logfile.txt

# Kombinera med andra verktyg
grep -r "TODO" ./src | wc -l        # Räkna TODOs
grep "ERROR" app.log | sort | uniq   # Unika errors
cat access.log | grep "POST" | grep -c "200"  # Lyckade POSTs`
            }
        ],
        docsUrl: "https://www.gnu.org/software/grep/manual/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "sed",
        name: "sed",
        category: "linux",
        icon: "✂️",
        shortDesc: "Stream editor",
        description: "sed är en stream editor för att transformera text. Perfekt för find-and-replace och textmanipulation i scripts.",
        installation: {
            apt: "sudo apt install sed",
            other: "Förinstallerat på de flesta system"
        },
        useCases: ["Text replacement", "Line deletion", "Text transformation", "Config file editing", "Batch processing"],
        keyFeatures: ["s/find/replace/", "-i in-place", "-n suppress", "Address ranges", "Hold buffer", "Multiple commands"],
        codeExamples: [
            {
                title: "Find & Replace",
                description: "Sök och ersätt text med sed",
                language: "bash",
                code: `# Grundläggande ersättning (första på varje rad)
sed 's/old/new/' file.txt

# Ersätt ALLA förekomster (global)
sed 's/old/new/g' file.txt

# Case-insensitive
sed 's/error/ERROR/gi' logfile.txt

# In-place editering (ändra fil direkt)
sed -i 's/localhost/0.0.0.0/g' config.conf

# Med backup
sed -i.bak 's/localhost/0.0.0.0/g' config.conf

# Andra delimiter (för paths)
sed 's|/var/log|/opt/logs|g' config.txt
sed 's#http://#https://#g' urls.txt

# Ersätt bara på specifik rad
sed '5s/old/new/' file.txt        # Bara rad 5
sed '10,20s/old/new/g' file.txt   # Rad 10-20`
            },
            {
                title: "Rad-operationer",
                description: "Ta bort, infoga och modifiera rader",
                language: "bash",
                code: `# Ta bort rad
sed '5d' file.txt                # Ta bort rad 5
sed '1,10d' file.txt             # Ta bort rad 1-10
sed '/pattern/d' file.txt        # Ta bort rader med pattern
sed '/^#/d' file.txt             # Ta bort kommentarer
sed '/^$/d' file.txt             # Ta bort tomma rader

# Infoga rad
sed '3i\\New line here' file.txt     # Före rad 3
sed '3a\\New line here' file.txt     # Efter rad 3
sed '/pattern/a\\New line' file.txt  # Efter matchande rad

# Visa specifika rader
sed -n '5p' file.txt             # Visa bara rad 5
sed -n '10,20p' file.txt         # Visa rad 10-20
sed -n '/start/,/end/p' file.txt # Visa block

# Skriv ut radnummer
sed -n '=' file.txt              # Alla radnummer
sed -n '/error/=' logfile.txt    # Radnummer för errors`
            },
            {
                title: "Praktiska DevOps-exempel",
                description: "sed i automation och scripts",
                language: "bash",
                code: `# Uppdatera config-fil
sed -i 's/^DEBUG=.*/DEBUG=false/' .env
sed -i 's/^PORT=.*/PORT=8080/' config.conf

# Kommentera ut rad
sed -i '/DISABLED_FEATURE/s/^/#/' config.txt

# Avkommentera rad
sed -i 's/^#ServerName/ServerName/' httpd.conf

# Extrahera värde
VERSION=$(sed -n 's/.*version": "\\([^"]*\\).*/\\1/p' package.json)

# Processa loggar
sed -n '/2024-01-15 10:/,/2024-01-15 11:/p' app.log

# Multipla kommandon
sed -e 's/foo/bar/g' -e 's/baz/qux/g' file.txt

# Från script-fil
sed -f transforms.sed input.txt

# Pipeline med andra verktyg
grep "ERROR" log.txt | sed 's/^.*ERROR: //' | sort | uniq -c`
            }
        ],
        docsUrl: "https://www.gnu.org/software/sed/manual/",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "awk",
        name: "AWK",
        category: "linux",
        icon: "📊",
        shortDesc: "Text processing language",
        description: "AWK är ett programmeringsspråk för textbearbetning. Extremt kraftfullt för att bearbeta strukturerad text och loggar.",
        installation: {
            apt: "sudo apt install gawk",
            other: "Förinstallerat på de flesta system"
        },
        useCases: ["Log parsing", "CSV processing", "Report generation", "Data extraction", "Column manipulation"],
        keyFeatures: ["Field splitting", "Pattern matching", "Built-in variables", "Functions", "BEGIN/END blocks"],
        codeExamples: [
            {
                title: "Kolumn-extraktion",
                description: "AWK delar automatiskt på whitespace",
                language: "bash",
                code: `# Skriv ut specifik kolumn
awk '{print $1}' file.txt         # Första kolumnen
awk '{print $NF}' file.txt        # Sista kolumnen
awk '{print $1, $3}' file.txt     # Kolumn 1 och 3

# Custom separator
awk -F':' '{print $1}' /etc/passwd    # : som separator
awk -F',' '{print $2}' data.csv       # CSV

# Output separator
awk -F',' '{OFS="\t"; print $1, $2}' file.csv

# ps + awk pipeline
ps aux | awk '{print $1, $2, $11}'    # user, pid, command

# Visa minneskonsumtion
ps aux | awk '{print $4, $11}' | sort -rn | head -10

# /etc/passwd parsing
awk -F':' '{print $1 " has shell: " $7}' /etc/passwd`
            },
            {
                title: "Pattern Matching & Filtering",
                description: "Villkor och pattern för filtrering",
                language: "bash",
                code: `# Filtrera på mönster
awk '/error/' logfile.txt             # Rader med "error"
awk '!/debug/' logfile.txt            # Rader UTAN "debug"

# Villkor på kolumn
awk '$3 > 100' data.txt               # Kolumn 3 större än 100
awk '$1 == "nginx"' services.txt      # Kolumn 1 är "nginx"
awk 'length($0) > 80' file.txt        # Rader längre än 80 tecken

# Kombinerade villkor
awk '/error/ && $3 > 10' logfile.txt
awk '$2 >= 50 && $2 <= 100' data.txt

# Reguljära uttryck
awk '$1 ~ /^web/' servers.txt         # Kolumn 1 börjar med "web"
awk '$3 !~ /[0-9]/' file.txt          # Kolumn 3 har inga siffror

# Range pattern (från-till)
awk '/START/,/END/' logfile.txt       # Block mellan START och END`
            },
            {
                title: "Beräkningar & Rapporter",
                description: "Aggregering och statistik med AWK",
                language: "bash",
                code: `# Summera kolumn
awk '{sum += $3} END {print "Total:", sum}' data.txt

# Räkna rader
awk 'END {print NR " lines"}' file.txt
awk '/error/ {count++} END {print count " errors"}' logfile.txt

# Genomsnitt
awk '{sum += $2; n++} END {print "Avg:", sum/n}' data.txt

# Min/Max
awk 'NR==1 || $3>max {max=$3} END {print "Max:", max}' data.txt

# Gruppera och räkna (som GROUP BY)
awk '{count[$1]++} END {for (k in count) print k, count[k]}' access.log

# BEGIN/END block
awk 'BEGIN {print "=== REPORT ==="; OFS="\t"}
     /error/ {errors++; print $1, $4}
     END {print "Total errors:", errors}' logfile.txt

# Formaterad output
awk '{printf "%-20s %10d\\n", $1, $2}' data.txt

# Aggregerad access log-analys
awk '{urls[$7]++} END {for (u in urls) print urls[u], u}' \\
    access.log | sort -rn | head -20`
            }
        ],
        docsUrl: "https://www.gnu.org/software/gawk/manual/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "find",
        name: "find",
        category: "linux",
        icon: "📂",
        shortDesc: "File search utility",
        description: "find söker efter filer och kataloger baserat på olika kriterier som namn, storlek, datum och typ.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["File search", "Batch operations", "Cleanup scripts", "Permission audits", "Disk analysis"],
        keyFeatures: ["-name pattern", "-type f/d", "-size", "-mtime", "-exec", "-delete", "-print0"],
        docsUrl: "https://www.gnu.org/software/findutils/manual/",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "xargs",
        name: "xargs",
        category: "linux",
        icon: "🔗",
        shortDesc: "Build command lines",
        description: "xargs bygger och kör kommandon från standard input. Perfekt för att kombinera med find och andra verktyg.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Batch processing", "Pipeline chaining", "Parallel execution", "File operations", "Command building"],
        keyFeatures: ["-I placeholder", "-P parallel", "-n max-args", "-0 null delimiter", "-t verbose"],
        docsUrl: "https://www.gnu.org/software/findutils/manual/",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "htop",
        name: "htop",
        category: "linux",
        icon: "📈",
        shortDesc: "Interactive process viewer",
        description: "htop är en interaktiv processvisare för Unix. Bättre än top med färger, scrollning och musinteraktion.",
        installation: {
            apt: "sudo apt install htop",
            brew: "brew install htop"
        },
        useCases: ["Process monitoring", "Resource usage", "Process management", "System diagnostics", "Performance tuning"],
        keyFeatures: ["Color display", "Mouse support", "Tree view", "Process filtering", "Custom columns", "Kill processes"],
        officialUrl: "https://htop.dev",
        docsUrl: "https://htop.dev/docs/",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "tmux",
        name: "tmux",
        category: "linux",
        icon: "🪟",
        shortDesc: "Terminal multiplexer",
        description: "tmux låter dig köra flera terminalsessioner i ett fönster. Sessioner överlever disconnects.",
        installation: {
            apt: "sudo apt install tmux",
            brew: "brew install tmux"
        },
        useCases: ["Remote sessions", "Session persistence", "Window management", "Pair programming", "Server administration"],
        keyFeatures: ["Sessions", "Windows", "Panes", "Detach/attach", "Key bindings", "Status bar", "Copy mode"],
        officialUrl: "https://github.com/tmux/tmux",
        docsUrl: "https://github.com/tmux/tmux/wiki",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "screen",
        name: "GNU Screen",
        category: "linux",
        icon: "📺",
        shortDesc: "Terminal multiplexer",
        description: "GNU Screen är en terminal multiplexer som låter dig köra flera sessioner från en terminal.",
        installation: {
            apt: "sudo apt install screen",
            brew: "brew install screen"
        },
        useCases: ["Persistent sessions", "Remote work", "Long-running processes", "Session sharing"],
        keyFeatures: ["Detach/reattach", "Multiple windows", "Session logging", "Screen splitting", "Scrollback"],
        officialUrl: "https://www.gnu.org/software/screen/",
        docsUrl: "https://www.gnu.org/software/screen/manual/",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "jq",
        name: "jq",
        category: "linux",
        icon: "📋",
        shortDesc: "JSON processor",
        description: "jq är en lättviktig och flexibel kommandorads-JSON-processor. Perfekt för att parsa API-svar.",
        installation: {
            apt: "sudo apt install jq",
            brew: "brew install jq"
        },
        useCases: ["JSON parsing", "API response processing", "Data transformation", "Config file manipulation", "Pipeline processing"],
        keyFeatures: ["Filters", "Selectors", "Functions", "Conditionals", "String interpolation", "Raw output"],
        officialUrl: "https://stedolan.github.io/jq/",
        docsUrl: "https://stedolan.github.io/jq/manual/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "yq",
        name: "yq",
        category: "linux",
        icon: "📄",
        shortDesc: "YAML processor",
        description: "yq är som jq men för YAML. Kommandoradsverktyg för att läsa, uppdatera och manipulera YAML-filer.",
        installation: {
            brew: "brew install yq",
            pip: "pip install yq"
        },
        useCases: ["YAML parsing", "Kubernetes manifests", "Config editing", "CI/CD pipelines", "Data conversion"],
        keyFeatures: ["jq-liknande syntax", "In-place editing", "YAML/JSON conversion", "Multiple documents", "Merge files"],
        officialUrl: "https://github.com/mikefarah/yq",
        docsUrl: "https://mikefarah.gitbook.io/yq/",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "tree",
        name: "tree",
        category: "linux",
        icon: "🌳",
        shortDesc: "Directory listing",
        description: "tree visar katalogstrukturen i ett trädformat. Perfekt för att visualisera projektstrukturer.",
        installation: {
            apt: "sudo apt install tree",
            brew: "brew install tree"
        },
        useCases: ["Directory visualization", "Documentation", "Project structure", "File system exploration"],
        keyFeatures: ["-L depth", "-d directories only", "-a all files", "-I exclude", "--gitignore", "-J JSON output"],
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "watch",
        name: "watch",
        category: "linux",
        icon: "👁️",
        shortDesc: "Execute periodically",
        description: "watch kör ett kommando upprepade gånger och visar output. Perfekt för att övervaka förändringar.",
        installation: {
            apt: "sudo apt install procps",
            other: "Förinstallerat på de flesta Linux-system"
        },
        useCases: ["Monitoring", "Log watching", "Resource tracking", "File changes", "Process monitoring"],
        keyFeatures: ["-n interval", "-d differences", "-c color", "-t no title", "-g exit on change"],
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "netcat",
        name: "Netcat (nc)",
        category: "network",
        icon: "🔌",
        shortDesc: "Network Swiss Army knife",
        description: "Netcat är ett mångsidigt nätverksverktyg för att läsa och skriva data över TCP/UDP-anslutningar.",
        installation: {
            apt: "sudo apt install netcat-openbsd",
            brew: "brew install netcat"
        },
        useCases: ["Port scanning", "File transfer", "Chat server", "Debugging", "Reverse shells", "Port listening"],
        keyFeatures: ["-l listen", "-p port", "-u UDP", "-v verbose", "-z scan", "-w timeout"],
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "dig",
        name: "dig",
        category: "network",
        icon: "🔍",
        shortDesc: "DNS lookup",
        description: "dig (Domain Information Groper) är ett verktyg för DNS-uppslag. Mer detaljerat än nslookup.",
        installation: {
            apt: "sudo apt install dnsutils",
            brew: "brew install bind"
        },
        useCases: ["DNS troubleshooting", "Record lookup", "DNS debugging", "Zone transfers", "Reverse lookups"],
        keyFeatures: ["+short", "+trace", "+noall +answer", "ANY query", "MX/TXT/CNAME records", "@server"],
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "nslookup",
        name: "nslookup",
        category: "network",
        icon: "🌐",
        shortDesc: "Name server lookup",
        description: "nslookup är ett klassiskt verktyg för att fråga DNS-servrar om domännamn och IP-adresser.",
        installation: {
            apt: "sudo apt install dnsutils",
            other: "Förinstallerat på de flesta system"
        },
        useCases: ["DNS lookup", "Troubleshooting", "Record queries", "Server testing"],
        keyFeatures: ["Interactive mode", "Server specification", "Record types", "Reverse lookup"],
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "traceroute",
        name: "traceroute",
        category: "network",
        icon: "🛤️",
        shortDesc: "Network path tracing",
        description: "traceroute visar nätverksvägen till en destination genom att lista alla hopp längs vägen.",
        installation: {
            apt: "sudo apt install traceroute",
            brew: "brew install traceroute"
        },
        useCases: ["Network debugging", "Latency analysis", "Route discovery", "ISP troubleshooting"],
        keyFeatures: ["-n numeric", "-w timeout", "-m max hops", "-I ICMP", "UDP/TCP modes"],
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "ping",
        name: "ping",
        category: "network",
        icon: "📡",
        shortDesc: "Network connectivity test",
        description: "ping testar nätverksanslutning genom att skicka ICMP-paket till en värd och mäta svarstid.",
        installation: {
            other: "Förinstallerat på alla system"
        },
        useCases: ["Connectivity testing", "Latency measurement", "Network diagnostics", "Host availability"],
        keyFeatures: ["-c count", "-i interval", "-s size", "-t TTL", "-W timeout", "Statistics"],
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "telnet",
        name: "telnet",
        category: "network",
        icon: "📞",
        shortDesc: "Network protocol client",
        description: "telnet är ett klassiskt protokoll för textbaserad kommunikation. Används ofta för att testa TCP-portar.",
        installation: {
            apt: "sudo apt install telnet",
            brew: "brew install telnet"
        },
        useCases: ["Port testing", "Protocol debugging", "SMTP testing", "HTTP debugging", "Legacy systems"],
        keyFeatures: ["Port connection", "Interactive mode", "Protocol testing", "Banner grabbing"],
        flashcardCount: 6,
        quizCount: 4
    },
    // ============================================================================
    // DEL 2: DEVOPS & AUTOMATION (20 verktyg)
    // ============================================================================
    {
        slug: "make",
        name: "Make",
        category: "linux",
        icon: "🔨",
        shortDesc: "Build automation",
        description: "Make är ett klassiskt build-verktyg som automatiserar kompilering och andra uppgifter via Makefiles.",
        installation: {
            apt: "sudo apt install make",
            brew: "brew install make"
        },
        useCases: ["Build automation", "Task running", "Dependency management", "CI/CD", "Project setup"],
        keyFeatures: ["Targets", "Dependencies", "Variables", "Pattern rules", "Phony targets", "Includes"],
        officialUrl: "https://www.gnu.org/software/make/",
        docsUrl: "https://www.gnu.org/software/make/manual/",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "cron",
        name: "Cron",
        category: "linux",
        icon: "⏰",
        shortDesc: "Job scheduler",
        description: "Cron är Unix/Linux standard för att schemalägga återkommande uppgifter. Kör scripts vid specifika tider.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Scheduled tasks", "Backups", "Log rotation", "System maintenance", "Automated reports"],
        keyFeatures: ["Crontab syntax", "User crontabs", "System crontabs", "@reboot", "Email notifications", "Logging"],
        docsUrl: "https://man7.org/linux/man-pages/man5/crontab.5.html",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "at",
        name: "at",
        category: "linux",
        icon: "📅",
        shortDesc: "One-time job scheduler",
        description: "at schemalägger engångsjobb att köras vid en specifik tidpunkt. Komplement till cron för enstaka uppgifter.",
        installation: {
            apt: "sudo apt install at",
            brew: "brew install at"
        },
        useCases: ["One-time tasks", "Delayed execution", "Maintenance windows", "Scheduled shutdowns"],
        keyFeatures: ["at command", "atq queue", "atrm remove", "Flexible time formats", "batch command"],
        docsUrl: "https://man7.org/linux/man-pages/man1/at.1.html",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "rsync",
        name: "rsync",
        category: "linux",
        icon: "🔄",
        shortDesc: "Fast file sync",
        description: "rsync är ett snabbt och mångsidigt verktyg för filkopiering. Överför endast ändrade delar av filer.",
        installation: {
            apt: "sudo apt install rsync",
            brew: "brew install rsync"
        },
        useCases: ["Backups", "File sync", "Remote transfers", "Mirroring", "Deployment"],
        keyFeatures: ["-a archive", "-v verbose", "-z compress", "--delete", "--exclude", "-e ssh", "--progress"],
        officialUrl: "https://rsync.samba.org",
        docsUrl: "https://rsync.samba.org/documentation.html",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "tar",
        name: "tar",
        category: "linux",
        icon: "📦",
        shortDesc: "Archive utility",
        description: "tar skapar och extraherar arkiv. Standard för att paketera filer i Unix/Linux-världen.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Archiving", "Backups", "Distribution", "Compression", "File bundling"],
        keyFeatures: ["-c create", "-x extract", "-v verbose", "-f file", "-z gzip", "-j bzip2", "-t list"],
        docsUrl: "https://www.gnu.org/software/tar/manual/",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "gzip",
        name: "gzip",
        category: "linux",
        icon: "🗜️",
        shortDesc: "File compression",
        description: "gzip är standard komprimeringsverktyg i Unix/Linux. Skapar .gz-filer med effektiv komprimering.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["File compression", "Log compression", "Bandwidth savings", "Storage optimization"],
        keyFeatures: ["-d decompress", "-k keep", "-r recursive", "-v verbose", "-1 to -9 levels", "gunzip"],
        docsUrl: "https://www.gnu.org/software/gzip/manual/",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "zip",
        name: "zip/unzip",
        category: "linux",
        icon: "📁",
        shortDesc: "ZIP archive utility",
        description: "zip/unzip hanterar ZIP-arkiv, det mest portabla arkivformatet som fungerar på alla plattformar.",
        installation: {
            apt: "sudo apt install zip unzip",
            brew: "brew install zip unzip"
        },
        useCases: ["Cross-platform archives", "File distribution", "Compression", "Backup"],
        keyFeatures: ["-r recursive", "-e encrypt", "-u update", "-d delete", "-l list", "Password protection"],
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "chmod",
        name: "chmod",
        category: "linux",
        icon: "🔐",
        shortDesc: "Change permissions",
        description: "chmod ändrar filrättigheter i Unix/Linux. Kontrollerar vem som kan läsa, skriva och köra filer.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Security", "Script execution", "Access control", "File sharing", "Web server setup"],
        keyFeatures: ["Numeric mode (755)", "Symbolic mode (u+x)", "-R recursive", "Special bits (setuid)", "umask"],
        docsUrl: "https://man7.org/linux/man-pages/man1/chmod.1.html",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "chown",
        name: "chown",
        category: "linux",
        icon: "👤",
        shortDesc: "Change ownership",
        description: "chown ändrar ägare och grupp för filer och kataloger. Viktigt för säkerhet och access control.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Access control", "Security", "Web server setup", "Deployment", "Multi-user systems"],
        keyFeatures: ["user:group", "-R recursive", "--reference", "-v verbose", "--from"],
        docsUrl: "https://man7.org/linux/man-pages/man1/chown.1.html",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "ln",
        name: "ln",
        category: "linux",
        icon: "🔗",
        shortDesc: "Create links",
        description: "ln skapar hårda och symboliska länkar mellan filer. Symboliska länkar är som genvägar.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Shortcuts", "Version management", "Configuration", "Shared libraries", "Dotfiles"],
        keyFeatures: ["-s symbolic", "-f force", "-n no-dereference", "Hard vs soft links", "-v verbose"],
        docsUrl: "https://man7.org/linux/man-pages/man1/ln.1.html",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "df",
        name: "df",
        category: "linux",
        icon: "💾",
        shortDesc: "Disk space usage",
        description: "df visar diskutrymme för filsystem. Viktigt för att övervaka lagringsstatus på servrar.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Disk monitoring", "Capacity planning", "System administration", "Alerts"],
        keyFeatures: ["-h human-readable", "-T filesystem type", "-i inodes", "--total", "-a all"],
        docsUrl: "https://man7.org/linux/man-pages/man1/df.1.html",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "du",
        name: "du",
        category: "linux",
        icon: "📏",
        shortDesc: "Directory size",
        description: "du visar diskutrymme använt av filer och kataloger. Perfekt för att hitta vad som tar plats.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Find large files", "Disk cleanup", "Quota management", "Storage analysis"],
        keyFeatures: ["-h human-readable", "-s summary", "-a all", "--max-depth", "-c total", "--exclude"],
        docsUrl: "https://man7.org/linux/man-pages/man1/du.1.html",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "ps",
        name: "ps",
        category: "linux",
        icon: "📋",
        shortDesc: "Process status",
        description: "ps visar information om körande processer. Grundläggande verktyg för processhantering.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Process listing", "Debugging", "System monitoring", "Script automation"],
        keyFeatures: ["aux", "-ef", "--forest", "-o custom output", "Process trees", "User filtering"],
        docsUrl: "https://man7.org/linux/man-pages/man1/ps.1.html",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "kill",
        name: "kill/killall",
        category: "linux",
        icon: "💀",
        shortDesc: "Terminate processes",
        description: "kill skickar signaler till processer, vanligtvis för att avsluta dem. killall avslutar processer efter namn.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Process termination", "Signal sending", "Graceful shutdown", "Force kill"],
        keyFeatures: ["-9 SIGKILL", "-15 SIGTERM", "-HUP reload", "killall by name", "pkill pattern"],
        docsUrl: "https://man7.org/linux/man-pages/man1/kill.1.html",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "top",
        name: "top",
        category: "linux",
        icon: "📊",
        shortDesc: "Process monitor",
        description: "top visar realtidsinformation om systemprocesser, CPU och minnesanvändning.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["System monitoring", "Performance analysis", "Resource tracking", "Process management"],
        keyFeatures: ["Interactive commands", "Sorting", "Filtering", "Kill processes", "CPU/Memory stats"],
        docsUrl: "https://man7.org/linux/man-pages/man1/top.1.html",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "free",
        name: "free",
        category: "linux",
        icon: "🧠",
        shortDesc: "Memory usage",
        description: "free visar mängden ledigt och använt minne i systemet, inklusive swap.",
        installation: {
            other: "Förinstallerat på alla Linux system"
        },
        useCases: ["Memory monitoring", "Performance tuning", "Capacity planning", "Troubleshooting"],
        keyFeatures: ["-h human-readable", "-m megabytes", "-g gigabytes", "-s interval", "-t total"],
        docsUrl: "https://man7.org/linux/man-pages/man1/free.1.html",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "uptime",
        name: "uptime",
        category: "linux",
        icon: "⏱️",
        shortDesc: "System uptime",
        description: "uptime visar hur länge systemet har körts, antal användare och systembelastning.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["System monitoring", "Health checks", "Load monitoring", "SLA tracking"],
        keyFeatures: ["Uptime display", "Load averages", "-p pretty format", "-s since"],
        docsUrl: "https://man7.org/linux/man-pages/man1/uptime.1.html",
        flashcardCount: 4,
        quizCount: 3
    },
    {
        slug: "uname",
        name: "uname",
        category: "linux",
        icon: "🖥️",
        shortDesc: "System information",
        description: "uname visar systeminformation som kernel-version, maskintyp och operativsystem.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["System info", "Scripting", "Compatibility checks", "Debugging"],
        keyFeatures: ["-a all", "-r kernel release", "-m machine", "-n hostname", "-s kernel name"],
        docsUrl: "https://man7.org/linux/man-pages/man1/uname.1.html",
        flashcardCount: 4,
        quizCount: 3
    },
    {
        slug: "hostname",
        name: "hostname",
        category: "linux",
        icon: "🏷️",
        shortDesc: "System hostname",
        description: "hostname visar eller sätter systemets värdnamn. Viktigt för nätverksidentifikation.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Identity", "Network config", "Scripting", "Logging"],
        keyFeatures: ["-f FQDN", "-i IP address", "-d domain", "hostnamectl (systemd)"],
        docsUrl: "https://man7.org/linux/man-pages/man1/hostname.1.html",
        flashcardCount: 4,
        quizCount: 3
    },
    {
        slug: "env",
        name: "env",
        category: "linux",
        icon: "🌍",
        shortDesc: "Environment variables",
        description: "env visar eller modifierar miljövariabler. Används för att köra kommandon med ändrad miljö.",
        installation: {
            other: "Förinstallerat på alla Unix/Linux system"
        },
        useCases: ["Environment display", "Variable setting", "Clean environment", "Script debugging"],
        keyFeatures: ["List variables", "-i ignore env", "-u unset", "VAR=value command", "printenv"],
        docsUrl: "https://man7.org/linux/man-pages/man1/env.1.html",
        flashcardCount: 6,
        quizCount: 4
    },
    // ============================================================================
    // DEL 3: CONTAINERS & CLOUD (20 verktyg)
    // ============================================================================
    {
        slug: "skopeo",
        name: "Skopeo",
        category: "containers",
        icon: "🔭",
        shortDesc: "Container image operations",
        description: "Skopeo inspekterar och kopierar container images mellan registries utan att behöva en daemon.",
        installation: {
            apt: "sudo apt install skopeo",
            brew: "brew install skopeo"
        },
        useCases: ["Image inspection", "Registry sync", "Image copying", "Signature verification"],
        keyFeatures: ["inspect", "copy", "sync", "delete", "No daemon needed", "Multi-registry support"],
        officialUrl: "https://github.com/containers/skopeo",
        docsUrl: "https://github.com/containers/skopeo/blob/main/docs/skopeo.1.md",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "buildah",
        name: "Buildah",
        category: "containers",
        icon: "🏗️",
        shortDesc: "Build OCI containers",
        description: "Buildah bygger OCI-kompatibla container images utan Docker daemon. Perfekt för CI/CD.",
        installation: {
            apt: "sudo apt install buildah",
            brew: "brew install buildah"
        },
        useCases: ["CI/CD builds", "Rootless builds", "Dockerfile alternative", "Image customization"],
        keyFeatures: ["from scratch", "bud (build using dockerfile)", "commit", "Rootless", "No daemon"],
        officialUrl: "https://buildah.io",
        docsUrl: "https://github.com/containers/buildah/tree/main/docs",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "cri-o",
        name: "CRI-O",
        category: "containers",
        icon: "⚙️",
        shortDesc: "Kubernetes container runtime",
        description: "CRI-O är en lättviktig container runtime specifikt designad för Kubernetes.",
        installation: {
            other: "Se docs för distribution-specifik installation"
        },
        useCases: ["Kubernetes runtime", "Production workloads", "Lightweight alternative", "Security-focused"],
        keyFeatures: ["OCI-compliant", "CRI implementation", "Kubernetes native", "Minimal footprint"],
        officialUrl: "https://cri-o.io",
        docsUrl: "https://cri-o.io/docs/",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "minikube",
        name: "Minikube",
        category: "orchestration",
        icon: "🎯",
        shortDesc: "Local Kubernetes",
        description: "Minikube kör en lokal Kubernetes-kluster på din maskin. Perfekt för utveckling och lärande.",
        installation: {
            brew: "brew install minikube",
            other: "curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64"
        },
        useCases: ["Local development", "Learning Kubernetes", "Testing", "CI/CD"],
        keyFeatures: ["start/stop", "Addons", "Multi-node", "Dashboard", "LoadBalancer", "Ingress"],
        officialUrl: "https://minikube.sigs.k8s.io",
        docsUrl: "https://minikube.sigs.k8s.io/docs/",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "kind",
        name: "kind",
        category: "orchestration",
        icon: "📦",
        shortDesc: "Kubernetes in Docker",
        description: "kind (Kubernetes IN Docker) kör lokala Kubernetes-kluster med Docker containers som noder.",
        installation: {
            brew: "brew install kind",
            other: "go install sigs.k8s.io/kind@latest"
        },
        useCases: ["Local testing", "CI/CD", "Development", "Multi-node clusters"],
        keyFeatures: ["Fast startup", "Multi-node", "Docker-based", "CI-friendly", "Config file"],
        officialUrl: "https://kind.sigs.k8s.io",
        docsUrl: "https://kind.sigs.k8s.io/docs/",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "k3s",
        name: "K3s",
        category: "orchestration",
        icon: "🚀",
        shortDesc: "Lightweight Kubernetes",
        description: "K3s är en certifierad lättviktig Kubernetes-distribution perfekt för edge, IoT och CI.",
        installation: {
            other: "curl -sfL https://get.k3s.io | sh -"
        },
        useCases: ["Edge computing", "IoT", "CI/CD", "Resource-constrained environments", "Development"],
        keyFeatures: ["Single binary", "SQLite default", "Low memory", "ARM support", "Auto TLS"],
        officialUrl: "https://k3s.io",
        docsUrl: "https://docs.k3s.io",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "k9s",
        name: "K9s",
        category: "orchestration",
        icon: "🐶",
        shortDesc: "Kubernetes CLI UI",
        description: "K9s är ett terminalgränssnitt för att hantera Kubernetes-kluster. Snabbt och intuitivt.",
        installation: {
            brew: "brew install derailed/k9s/k9s",
            other: "go install github.com/derailed/k9s@latest"
        },
        useCases: ["Cluster management", "Debugging", "Log viewing", "Resource navigation"],
        keyFeatures: ["Real-time views", "Log streaming", "Port forwarding", "Shell access", "Custom views"],
        officialUrl: "https://k9scli.io",
        docsUrl: "https://k9scli.io/topics/commands/",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "lens",
        name: "Lens",
        category: "orchestration",
        icon: "🔍",
        shortDesc: "Kubernetes IDE",
        description: "Lens är en kraftfull desktop-applikation för att hantera Kubernetes-kluster med grafiskt gränssnitt.",
        installation: {
            brew: "brew install --cask lens",
            other: "https://k8slens.dev/download"
        },
        useCases: ["Cluster management", "Multi-cluster", "Visualization", "Team collaboration"],
        keyFeatures: ["Multi-cluster", "Built-in terminal", "Metrics", "Extensions", "Helm support"],
        officialUrl: "https://k8slens.dev",
        docsUrl: "https://docs.k8slens.dev",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "kubectx",
        name: "kubectx",
        category: "orchestration",
        icon: "🔀",
        shortDesc: "Switch Kubernetes contexts",
        description: "kubectx gör det enkelt att växla mellan Kubernetes-kontexter (kluster).",
        installation: {
            brew: "brew install kubectx",
            other: "kubectl krew install ctx"
        },
        useCases: ["Multi-cluster", "Context switching", "Productivity", "DevOps workflows"],
        keyFeatures: ["Fast switching", "fzf integration", "List contexts", "Rename contexts"],
        officialUrl: "https://github.com/ahmetb/kubectx",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "kubens",
        name: "kubens",
        category: "orchestration",
        icon: "📂",
        shortDesc: "Switch Kubernetes namespaces",
        description: "kubens gör det enkelt att växla mellan Kubernetes namespaces.",
        installation: {
            brew: "brew install kubectx",
            other: "kubectl krew install ns"
        },
        useCases: ["Namespace switching", "Multi-tenant", "Development workflows"],
        keyFeatures: ["Fast switching", "fzf integration", "List namespaces", "Default namespace"],
        officialUrl: "https://github.com/ahmetb/kubectx",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "stern",
        name: "Stern",
        category: "orchestration",
        icon: "📜",
        shortDesc: "Multi-pod log tailing",
        description: "Stern visar loggar från flera pods och containers samtidigt med färgkodning.",
        installation: {
            brew: "brew install stern",
            other: "go install github.com/stern/stern@latest"
        },
        useCases: ["Log aggregation", "Debugging", "Microservices", "Real-time monitoring"],
        keyFeatures: ["Multi-pod", "Color-coded", "Regex filtering", "Container selection", "Timestamps"],
        officialUrl: "https://github.com/stern/stern",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "kustomize",
        name: "Kustomize",
        category: "orchestration",
        icon: "🎨",
        shortDesc: "Kubernetes configuration",
        description: "Kustomize anpassar Kubernetes YAML-konfigurationer utan templating. Inbyggt i kubectl.",
        installation: {
            brew: "brew install kustomize",
            other: "kubectl kustomize (inbyggt)"
        },
        useCases: ["Environment-specific configs", "Overlays", "Configuration management", "GitOps"],
        keyFeatures: ["Overlays", "Patches", "Generators", "Transformers", "No templates", "Built into kubectl"],
        officialUrl: "https://kustomize.io",
        docsUrl: "https://kubectl.docs.kubernetes.io/guides/introduction/kustomize/",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "kompose",
        name: "Kompose",
        category: "orchestration",
        icon: "🔄",
        shortDesc: "Docker Compose to Kubernetes",
        description: "Kompose konverterar Docker Compose-filer till Kubernetes-resurser.",
        installation: {
            brew: "brew install kompose",
            other: "curl -L https://github.com/kubernetes/kompose/releases/download/v1.31.2/kompose-linux-amd64 -o kompose"
        },
        useCases: ["Migration", "Learning", "Quick conversion", "Development to production"],
        keyFeatures: ["convert command", "Multiple output formats", "Helm charts", "OpenShift support"],
        officialUrl: "https://kompose.io",
        docsUrl: "https://kompose.io/user-guide/",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "lazydocker",
        name: "Lazydocker",
        category: "containers",
        icon: "🦥",
        shortDesc: "Docker terminal UI",
        description: "Lazydocker är ett terminalgränssnitt för Docker. Hantera containers, images och volumes visuellt.",
        installation: {
            brew: "brew install jesseduffield/lazydocker/lazydocker",
            other: "go install github.com/jesseduffield/lazydocker@latest"
        },
        useCases: ["Container management", "Log viewing", "Resource monitoring", "Quick operations"],
        keyFeatures: ["Visual interface", "Logs", "Stats", "Shell access", "Image management", "Prune"],
        officialUrl: "https://github.com/jesseduffield/lazydocker",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "dive",
        name: "Dive",
        category: "containers",
        icon: "🤿",
        shortDesc: "Docker image explorer",
        description: "Dive analyserar Docker images layer-för-layer för att hitta sätt att minska storlek.",
        installation: {
            brew: "brew install dive",
            other: "go install github.com/wagoodman/dive@latest"
        },
        useCases: ["Image optimization", "Size reduction", "CI/CD checks", "Debugging"],
        keyFeatures: ["Layer analysis", "Wasted space detection", "CI integration", "Image efficiency score"],
        officialUrl: "https://github.com/wagoodman/dive",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "trivy",
        name: "Trivy",
        category: "security",
        icon: "🔒",
        shortDesc: "Security scanner",
        description: "Trivy är en omfattande säkerhetsscanner för containers, filesystems, Git repos och mer.",
        installation: {
            brew: "brew install aquasecurity/trivy/trivy",
            apt: "sudo apt install trivy"
        },
        useCases: ["Vulnerability scanning", "CI/CD security", "Compliance", "IaC scanning"],
        keyFeatures: ["Container scanning", "Filesystem scan", "Git repo scan", "SBOM", "Secret detection"],
        officialUrl: "https://trivy.dev",
        docsUrl: "https://aquasecurity.github.io/trivy/",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "hadolint",
        name: "Hadolint",
        category: "containers",
        icon: "📝",
        shortDesc: "Dockerfile linter",
        description: "Hadolint är en smart Dockerfile-linter som hjälper dig skriva bästa praxis Dockerfiles.",
        installation: {
            brew: "brew install hadolint",
            other: "docker run hadolint/hadolint"
        },
        useCases: ["Dockerfile quality", "CI/CD checks", "Best practices", "Security"],
        keyFeatures: ["Best practice rules", "ShellCheck integration", "Ignore rules", "CI integration"],
        officialUrl: "https://github.com/hadolint/hadolint",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "dockle",
        name: "Dockle",
        category: "containers",
        icon: "🔍",
        shortDesc: "Container image linter",
        description: "Dockle är en säkerhets-linter för container images baserad på CIS Benchmark.",
        installation: {
            brew: "brew install goodwithtech/r/dockle",
            other: "docker run goodwithtech/dockle"
        },
        useCases: ["Image security", "Compliance", "CI/CD", "Best practices"],
        keyFeatures: ["CIS Benchmark", "Security checks", "Best practices", "CI-friendly output"],
        officialUrl: "https://github.com/goodwithtech/dockle",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "grype",
        name: "Grype",
        category: "security",
        icon: "🦅",
        shortDesc: "Vulnerability scanner",
        description: "Grype är en snabb vulnerability scanner för container images och filesystems.",
        installation: {
            brew: "brew install grype",
            other: "curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s"
        },
        useCases: ["Vulnerability scanning", "SBOM analysis", "CI/CD", "Security audits"],
        keyFeatures: ["Fast scanning", "SBOM support", "Multiple formats", "DB updates", "Ignore rules"],
        officialUrl: "https://github.com/anchore/grype",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "syft",
        name: "Syft",
        category: "security",
        icon: "📋",
        shortDesc: "SBOM generator",
        description: "Syft genererar Software Bill of Materials (SBOM) från container images och filesystems.",
        installation: {
            brew: "brew install syft",
            other: "curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s"
        },
        useCases: ["SBOM generation", "Compliance", "Supply chain security", "Vulnerability management"],
        keyFeatures: ["Multiple formats (SPDX, CycloneDX)", "Container support", "Filesystem support", "CI integration"],
        officialUrl: "https://github.com/anchore/syft",
        flashcardCount: 8,
        quizCount: 5
    },
    // ============================================================================
    // DEL 4: MONITORING & SECURITY (20 verktyg)
    // ============================================================================
    {
        slug: "loki",
        name: "Grafana Loki",
        category: "monitoring",
        icon: "📝",
        shortDesc: "Log aggregation",
        description: "Loki är ett loggaggregeringssystem från Grafana. Designat för att vara kostnadseffektivt och enkelt att driva.",
        installation: {
            brew: "brew install grafana/tap/loki",
            other: "docker run grafana/loki"
        },
        useCases: ["Log aggregation", "Grafana integration", "Kubernetes logging", "Cost-effective logging"],
        keyFeatures: ["LogQL", "Label-based indexing", "Promtail agent", "Grafana integration", "Multi-tenancy"],
        officialUrl: "https://grafana.com/oss/loki/",
        docsUrl: "https://grafana.com/docs/loki/latest/",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "jaeger",
        name: "Jaeger",
        category: "monitoring",
        icon: "🔍",
        shortDesc: "Distributed tracing",
        description: "Jaeger är ett distribuerat tracing-system för att övervaka och felsöka microservices.",
        installation: {
            other: "docker run jaegertracing/all-in-one"
        },
        useCases: ["Distributed tracing", "Performance monitoring", "Root cause analysis", "Service dependencies"],
        keyFeatures: ["Trace visualization", "Service topology", "OpenTelemetry support", "Adaptive sampling"],
        officialUrl: "https://www.jaegertracing.io",
        docsUrl: "https://www.jaegertracing.io/docs/",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "opentelemetry",
        name: "OpenTelemetry",
        category: "monitoring",
        icon: "📡",
        shortDesc: "Observability framework",
        description: "OpenTelemetry är en samling verktyg, APIs och SDKs för instrumentering, generering och insamling av telemetridata.",
        installation: {
            pip: "pip install opentelemetry-api opentelemetry-sdk",
            npm: "npm install @opentelemetry/api"
        },
        useCases: ["Distributed tracing", "Metrics", "Logging", "Vendor-neutral observability"],
        keyFeatures: ["Traces", "Metrics", "Logs", "Collector", "Auto-instrumentation", "Multiple backends"],
        officialUrl: "https://opentelemetry.io",
        docsUrl: "https://opentelemetry.io/docs/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "fluentd",
        name: "Fluentd",
        category: "monitoring",
        icon: "📊",
        shortDesc: "Data collector",
        description: "Fluentd är en unified logging layer som samlar in, transformerar och skickar loggar.",
        installation: {
            apt: "sudo apt install td-agent",
            brew: "brew install fluentd"
        },
        useCases: ["Log collection", "Data pipeline", "Cloud logging", "Container logging"],
        keyFeatures: ["Plugins", "Buffering", "Routing", "Multiple outputs", "High availability"],
        officialUrl: "https://www.fluentd.org",
        docsUrl: "https://docs.fluentd.org",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "logstash",
        name: "Logstash",
        category: "monitoring",
        icon: "🔄",
        shortDesc: "Data processing pipeline",
        description: "Logstash är en datainsamlings- och processerings-pipeline. Del av Elastic Stack (ELK).",
        installation: {
            apt: "sudo apt install logstash",
            brew: "brew install logstash"
        },
        useCases: ["Log processing", "ETL", "Data enrichment", "Centralized logging"],
        keyFeatures: ["Input plugins", "Filter plugins", "Output plugins", "Grok patterns", "Codecs"],
        officialUrl: "https://www.elastic.co/logstash",
        docsUrl: "https://www.elastic.co/guide/en/logstash/current/",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "filebeat",
        name: "Filebeat",
        category: "monitoring",
        icon: "📁",
        shortDesc: "Log shipper",
        description: "Filebeat är en lättviktig loggskeppare som övervakar loggfiler och vidarebefordrar dem.",
        installation: {
            apt: "sudo apt install filebeat",
            brew: "brew install filebeat"
        },
        useCases: ["Log shipping", "File monitoring", "Container logging", "Centralized logs"],
        keyFeatures: ["Lightweight", "Modules", "Autodiscover", "Backpressure handling", "Multiple outputs"],
        officialUrl: "https://www.elastic.co/beats/filebeat",
        docsUrl: "https://www.elastic.co/guide/en/beats/filebeat/current/",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "vault",
        name: "HashiCorp Vault",
        category: "security",
        icon: "🔐",
        shortDesc: "Secrets management",
        description: "Vault hanterar hemligheter och skyddar känslig data. Centraliserad secrets management.",
        installation: {
            brew: "brew install vault",
            other: "https://developer.hashicorp.com/vault/downloads"
        },
        useCases: ["Secrets management", "Dynamic credentials", "Encryption as service", "PKI"],
        keyFeatures: ["Secret engines", "Auth methods", "Dynamic secrets", "Encryption", "Leasing", "Audit"],
        officialUrl: "https://www.vaultproject.io",
        docsUrl: "https://developer.hashicorp.com/vault/docs",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "certbot",
        name: "Certbot",
        category: "security",
        icon: "📜",
        shortDesc: "Let's Encrypt client",
        description: "Certbot automatiserar hämtning och förnyelse av TLS/SSL-certifikat från Let's Encrypt.",
        installation: {
            apt: "sudo apt install certbot",
            brew: "brew install certbot"
        },
        useCases: ["SSL certificates", "HTTPS setup", "Certificate renewal", "Wildcard certs"],
        keyFeatures: ["Auto-renewal", "Multiple plugins", "Wildcard support", "DNS challenges", "Standalone mode"],
        officialUrl: "https://certbot.eff.org",
        docsUrl: "https://eff-certbot.readthedocs.io",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "fail2ban",
        name: "Fail2ban",
        category: "security",
        icon: "🚫",
        shortDesc: "Intrusion prevention",
        description: "Fail2ban skyddar mot brute-force attacker genom att blockera IP-adresser baserat på loggmönster.",
        installation: {
            apt: "sudo apt install fail2ban",
            brew: "brew install fail2ban"
        },
        useCases: ["SSH protection", "Web server security", "Brute-force prevention", "Log monitoring"],
        keyFeatures: ["Jails", "Filters", "Actions", "Ban time", "Whitelisting", "Email notifications"],
        officialUrl: "https://www.fail2ban.org",
        docsUrl: "https://www.fail2ban.org/wiki/index.php/MANUAL_0_8",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "ufw",
        name: "UFW",
        category: "security",
        icon: "🧱",
        shortDesc: "Uncomplicated Firewall",
        description: "UFW är ett användarvänligt gränssnitt för iptables. Förenklar brandväggshantering på Ubuntu/Debian.",
        installation: {
            apt: "sudo apt install ufw"
        },
        useCases: ["Firewall management", "Port control", "Network security", "Server hardening"],
        keyFeatures: ["allow/deny", "Application profiles", "Logging", "IPv6 support", "Rate limiting"],
        docsUrl: "https://help.ubuntu.com/community/UFW",
        flashcardCount: 8,
        quizCount: 5
    },
    {
        slug: "iptables",
        name: "iptables",
        category: "security",
        icon: "🔥",
        shortDesc: "Linux firewall",
        description: "iptables är Linux-kernelns brandvägg. Kraftfullt men komplext verktyg för nätverksfiltrering.",
        installation: {
            apt: "sudo apt install iptables",
            other: "Förinstallerat på de flesta Linux-system"
        },
        useCases: ["Firewall rules", "NAT", "Port forwarding", "Traffic shaping", "Security"],
        keyFeatures: ["Chains", "Tables", "Rules", "NAT", "Mangle", "Filter", "ACCEPT/DROP/REJECT"],
        docsUrl: "https://linux.die.net/man/8/iptables",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "nmap",
        name: "Nmap",
        category: "security",
        icon: "🗺️",
        shortDesc: "Network scanner",
        description: "Nmap är ett kraftfullt verktyg för nätverksutforskning och säkerhetsrevisioner.",
        installation: {
            apt: "sudo apt install nmap",
            brew: "brew install nmap"
        },
        useCases: ["Port scanning", "Network discovery", "Security auditing", "Service detection"],
        keyFeatures: ["-sS SYN scan", "-sV version", "-O OS detection", "-A aggressive", "Scripts (NSE)"],
        officialUrl: "https://nmap.org",
        docsUrl: "https://nmap.org/docs.html",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "wireshark",
        name: "Wireshark",
        category: "security",
        icon: "🦈",
        shortDesc: "Network analyzer",
        description: "Wireshark är världens mest använda nätverksprotokollanalysator för felsökning och analys.",
        installation: {
            apt: "sudo apt install wireshark",
            brew: "brew install --cask wireshark"
        },
        useCases: ["Network troubleshooting", "Protocol analysis", "Security analysis", "Education"],
        keyFeatures: ["Deep inspection", "Live capture", "Display filters", "Statistics", "Export options"],
        officialUrl: "https://www.wireshark.org",
        docsUrl: "https://www.wireshark.org/docs/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "tcpdump",
        name: "tcpdump",
        category: "security",
        icon: "📡",
        shortDesc: "Packet analyzer",
        description: "tcpdump är ett kommandorads-verktyg för att fånga och analysera nätverkstrafik.",
        installation: {
            apt: "sudo apt install tcpdump",
            brew: "brew install tcpdump"
        },
        useCases: ["Network debugging", "Traffic capture", "Security analysis", "Protocol debugging"],
        keyFeatures: ["-i interface", "-w write file", "-r read file", "BPF filters", "-n numeric"],
        docsUrl: "https://www.tcpdump.org/manpages/tcpdump.1.html",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "strace",
        name: "strace",
        category: "linux",
        icon: "🔬",
        shortDesc: "System call tracer",
        description: "strace spårar systemanrop och signaler för en process. Ovärderligt för debugging.",
        installation: {
            apt: "sudo apt install strace",
            brew: "brew install strace"
        },
        useCases: ["Debugging", "Performance analysis", "Security analysis", "Process tracing"],
        keyFeatures: ["-p pid", "-f follow forks", "-e trace", "-o output", "-t timestamps", "-c summary"],
        docsUrl: "https://strace.io/",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "ltrace",
        name: "ltrace",
        category: "linux",
        icon: "📚",
        shortDesc: "Library call tracer",
        description: "ltrace spårar biblioteksanrop i ett program. Komplement till strace.",
        installation: {
            apt: "sudo apt install ltrace"
        },
        useCases: ["Debugging", "Reverse engineering", "Performance analysis", "Library usage"],
        keyFeatures: ["-p pid", "-e filter", "-o output", "-c summary", "-S show syscalls"],
        docsUrl: "https://man7.org/linux/man-pages/man1/ltrace.1.html",
        flashcardCount: 6,
        quizCount: 4
    },
    {
        slug: "gdb",
        name: "GDB",
        category: "linux",
        icon: "🐛",
        shortDesc: "GNU Debugger",
        description: "GDB är GNU-projektets debugger för C, C++ och andra språk. Kraftfullt för felsökning.",
        installation: {
            apt: "sudo apt install gdb",
            brew: "brew install gdb"
        },
        useCases: ["Debugging", "Core dump analysis", "Reverse engineering", "Memory analysis"],
        keyFeatures: ["Breakpoints", "Watchpoints", "Stack traces", "Memory inspection", "Remote debugging"],
        officialUrl: "https://www.gnu.org/software/gdb/",
        docsUrl: "https://sourceware.org/gdb/documentation/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "valgrind",
        name: "Valgrind",
        category: "linux",
        icon: "🧪",
        shortDesc: "Memory debugger",
        description: "Valgrind är ett verktyg för minnesdebugning, minnesläckagedetektering och profilering.",
        installation: {
            apt: "sudo apt install valgrind",
            brew: "brew install valgrind"
        },
        useCases: ["Memory leaks", "Memory debugging", "Profiling", "Thread debugging"],
        keyFeatures: ["Memcheck", "Cachegrind", "Callgrind", "Helgrind", "DRD"],
        officialUrl: "https://valgrind.org",
        docsUrl: "https://valgrind.org/docs/manual/",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "perf",
        name: "perf",
        category: "linux",
        icon: "⚡",
        shortDesc: "Performance analyzer",
        description: "perf är Linux-kernelns profileringsverktyg för CPU-prestanda och systemanalys.",
        installation: {
            apt: "sudo apt install linux-tools-common"
        },
        useCases: ["CPU profiling", "Performance analysis", "Bottleneck detection", "System tuning"],
        keyFeatures: ["stat", "record", "report", "top", "Hardware counters", "Flame graphs"],
        docsUrl: "https://perf.wiki.kernel.org",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "bpftrace",
        name: "bpftrace",
        category: "linux",
        icon: "🔮",
        shortDesc: "Dynamic tracing",
        description: "bpftrace är ett högnivå-tracingspråk för Linux eBPF. Kraftfullt för systemanalys.",
        installation: {
            apt: "sudo apt install bpftrace",
            brew: "brew install bpftrace"
        },
        useCases: ["Dynamic tracing", "Performance analysis", "Debugging", "System observability"],
        keyFeatures: ["One-liners", "Probes", "Maps", "Aggregations", "Histograms", "Stack traces"],
        officialUrl: "https://bpftrace.org",
        docsUrl: "https://github.com/bpftrace/bpftrace/blob/master/docs/reference_guide.md",
        flashcardCount: 10,
        quizCount: 6
    },
    // ============================================================================
    // DEL 5: DATABASER & UTVECKLING (20 verktyg)
    // ============================================================================
    {
        slug: "mysql",
        name: "MySQL",
        category: "database",
        icon: "🐬",
        shortDesc: "Relational database",
        description: "MySQL är en av världens mest populära relationsdatabaser. Open source och snabb.",
        installation: {
            apt: "sudo apt install mysql-server",
            brew: "brew install mysql"
        },
        useCases: ["Web applications", "E-commerce", "Data warehousing", "CMS backends"],
        keyFeatures: ["InnoDB engine", "Replication", "Clustering", "Full-text search", "Stored procedures"],
        officialUrl: "https://www.mysql.com",
        docsUrl: "https://dev.mysql.com/doc/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "mongodb",
        name: "MongoDB",
        category: "database",
        icon: "🍃",
        shortDesc: "Document database",
        description: "MongoDB är en NoSQL dokumentdatabas med flexibelt schema. Populär för modern utveckling.",
        installation: {
            brew: "brew tap mongodb/brew && brew install mongodb-community",
            other: "docker run mongo"
        },
        useCases: ["Content management", "Real-time analytics", "IoT", "Mobile apps", "Catalogs"],
        keyFeatures: ["Document model", "Aggregation pipeline", "Sharding", "Replication", "Atlas cloud"],
        officialUrl: "https://www.mongodb.com",
        docsUrl: "https://docs.mongodb.com",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "sqlite",
        name: "SQLite",
        category: "database",
        icon: "📁",
        shortDesc: "Embedded database",
        description: "SQLite är en lättviktig, filbaserad SQL-databas. Perfekt för lokala applikationer och prototyper.",
        installation: {
            apt: "sudo apt install sqlite3",
            brew: "brew install sqlite"
        },
        useCases: ["Embedded apps", "Mobile apps", "Testing", "Configuration", "Local caching"],
        keyFeatures: ["Zero configuration", "Single file", "Full SQL", "Transactional", "Cross-platform"],
        officialUrl: "https://www.sqlite.org",
        docsUrl: "https://www.sqlite.org/docs.html",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "elasticsearch",
        name: "Elasticsearch",
        category: "database",
        icon: "🔎",
        shortDesc: "Search engine",
        description: "Elasticsearch är en distribuerad sökmotor och analysplattform baserad på Lucene.",
        installation: {
            brew: "brew install elasticsearch",
            other: "docker run elasticsearch:8.11.0"
        },
        useCases: ["Full-text search", "Log analytics", "Application monitoring", "Security analytics"],
        keyFeatures: ["RESTful API", "Distributed", "Real-time", "Schema-free", "Kibana integration"],
        officialUrl: "https://www.elastic.co/elasticsearch",
        docsUrl: "https://www.elastic.co/guide/en/elasticsearch/reference/current/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "rabbitmq",
        name: "RabbitMQ",
        category: "database",
        icon: "🐰",
        shortDesc: "Message broker",
        description: "RabbitMQ är en meddelandeköbroker som implementerar AMQP. Pålitlig och flexibel.",
        installation: {
            apt: "sudo apt install rabbitmq-server",
            brew: "brew install rabbitmq"
        },
        useCases: ["Message queuing", "Microservices", "Task queues", "Pub/sub", "Event streaming"],
        keyFeatures: ["Exchanges", "Queues", "Bindings", "Clustering", "Management UI", "Multiple protocols"],
        officialUrl: "https://www.rabbitmq.com",
        docsUrl: "https://www.rabbitmq.com/docs",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "kafka",
        name: "Apache Kafka",
        category: "database",
        icon: "📨",
        shortDesc: "Event streaming",
        description: "Kafka är en distribuerad event streaming-plattform för högpresterande datapipelines.",
        installation: {
            brew: "brew install kafka",
            other: "docker run confluentinc/cp-kafka"
        },
        useCases: ["Event streaming", "Log aggregation", "Stream processing", "Data integration", "Messaging"],
        keyFeatures: ["Topics", "Partitions", "Consumer groups", "Exactly-once", "Kafka Connect", "ksqlDB"],
        officialUrl: "https://kafka.apache.org",
        docsUrl: "https://kafka.apache.org/documentation/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "etcd",
        name: "etcd",
        category: "database",
        icon: "🔑",
        shortDesc: "Distributed key-value store",
        description: "etcd är en distribuerad, pålitlig key-value store. Används av Kubernetes för konfiguration.",
        installation: {
            brew: "brew install etcd",
            other: "docker run quay.io/coreos/etcd"
        },
        useCases: ["Service discovery", "Configuration management", "Kubernetes backend", "Leader election"],
        keyFeatures: ["Raft consensus", "Watch", "Leases", "Transactions", "gRPC API"],
        officialUrl: "https://etcd.io",
        docsUrl: "https://etcd.io/docs/",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "consul",
        name: "HashiCorp Consul",
        category: "database",
        icon: "🌐",
        shortDesc: "Service mesh",
        description: "Consul är en service mesh-lösning med service discovery, configuration och segmentering.",
        installation: {
            brew: "brew install consul",
            other: "https://developer.hashicorp.com/consul/downloads"
        },
        useCases: ["Service discovery", "Health checking", "KV store", "Service mesh", "Multi-datacenter"],
        keyFeatures: ["Service discovery", "Health checks", "KV store", "Service mesh", "DNS interface"],
        officialUrl: "https://www.consul.io",
        docsUrl: "https://developer.hashicorp.com/consul/docs",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "minio",
        name: "MinIO",
        category: "database",
        icon: "🪣",
        shortDesc: "Object storage",
        description: "MinIO är en högpresterande, S3-kompatibel objektlagring. Perfekt för on-premise moln.",
        installation: {
            brew: "brew install minio/stable/minio",
            other: "docker run minio/minio server /data"
        },
        useCases: ["Object storage", "Data lake", "Backup", "S3 replacement", "Machine learning"],
        keyFeatures: ["S3 compatible", "High performance", "Kubernetes native", "Encryption", "Versioning"],
        officialUrl: "https://min.io",
        docsUrl: "https://min.io/docs/minio/linux/index.html",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "httpd",
        name: "Apache HTTP Server",
        category: "linux",
        icon: "🪶",
        shortDesc: "Web server",
        description: "Apache HTTP Server är världens äldsta och en av de mest använda webbservrarna.",
        installation: {
            apt: "sudo apt install apache2",
            brew: "brew install httpd"
        },
        useCases: ["Web serving", "Reverse proxy", "Virtual hosts", "PHP hosting", ".htaccess"],
        keyFeatures: ["Modules", "Virtual hosts", ".htaccess", "mod_rewrite", "mod_ssl", "MPM"],
        officialUrl: "https://httpd.apache.org",
        docsUrl: "https://httpd.apache.org/docs/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "haproxy",
        name: "HAProxy",
        category: "network",
        icon: "⚖️",
        shortDesc: "Load balancer",
        description: "HAProxy är en pålitlig, högpresterande TCP/HTTP load balancer och proxy.",
        installation: {
            apt: "sudo apt install haproxy",
            brew: "brew install haproxy"
        },
        useCases: ["Load balancing", "High availability", "SSL termination", "Rate limiting"],
        keyFeatures: ["TCP/HTTP balancing", "Health checks", "Sticky sessions", "SSL offloading", "Stats"],
        officialUrl: "https://www.haproxy.org",
        docsUrl: "https://docs.haproxy.org",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "traefik",
        name: "Traefik",
        category: "network",
        icon: "🚦",
        shortDesc: "Cloud-native proxy",
        description: "Traefik är en modern reverse proxy och load balancer för microservices och containers.",
        installation: {
            brew: "brew install traefik",
            other: "docker run traefik"
        },
        useCases: ["Kubernetes ingress", "Docker routing", "Auto-discovery", "Let's Encrypt"],
        keyFeatures: ["Auto-discovery", "Kubernetes/Docker native", "Let's Encrypt", "Middlewares", "Dashboard"],
        officialUrl: "https://traefik.io",
        docsUrl: "https://doc.traefik.io/traefik/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "envoy",
        name: "Envoy",
        category: "network",
        icon: "🛡️",
        shortDesc: "Service proxy",
        description: "Envoy är en högpresterande edge och service proxy designad för molnbaserade applikationer.",
        installation: {
            brew: "brew install envoy",
            other: "docker run envoyproxy/envoy"
        },
        useCases: ["Service mesh", "API gateway", "Load balancing", "Observability"],
        keyFeatures: ["L3/L4 filter", "HTTP L7 filter", "Service discovery", "Health checking", "xDS API"],
        officialUrl: "https://www.envoyproxy.io",
        docsUrl: "https://www.envoyproxy.io/docs/envoy/latest/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "istio",
        name: "Istio",
        category: "orchestration",
        icon: "⛵",
        shortDesc: "Service mesh",
        description: "Istio är en komplett service mesh för Kubernetes med traffic management och säkerhet.",
        installation: {
            brew: "brew install istioctl",
            other: "curl -L https://istio.io/downloadIstio | sh -"
        },
        useCases: ["Traffic management", "Security", "Observability", "Policy enforcement"],
        keyFeatures: ["Envoy sidecar", "mTLS", "Traffic control", "Telemetry", "Authorization"],
        officialUrl: "https://istio.io",
        docsUrl: "https://istio.io/latest/docs/",
        flashcardCount: 15,
        quizCount: 10
    },
    {
        slug: "linkerd",
        name: "Linkerd",
        category: "orchestration",
        icon: "🔗",
        shortDesc: "Lightweight service mesh",
        description: "Linkerd är en lättviktig, snabb service mesh för Kubernetes. CNCF graduated project.",
        installation: {
            brew: "brew install linkerd",
            other: "curl -sL https://run.linkerd.io/install | sh"
        },
        useCases: ["Service mesh", "mTLS", "Observability", "Traffic splitting"],
        keyFeatures: ["Lightweight", "Rust proxy", "mTLS", "Golden metrics", "Traffic split"],
        officialUrl: "https://linkerd.io",
        docsUrl: "https://linkerd.io/docs/",
        flashcardCount: 10,
        quizCount: 7
    },
    {
        slug: "pulumi",
        name: "Pulumi",
        category: "cloud",
        icon: "🧬",
        shortDesc: "Infrastructure as Code",
        description: "Pulumi låter dig definiera infrastruktur med riktiga programmeringsspråk som Python, TypeScript.",
        installation: {
            brew: "brew install pulumi",
            npm: "npm install -g @pulumi/pulumi"
        },
        useCases: ["IaC", "Multi-cloud", "Modern languages", "DevOps automation"],
        keyFeatures: ["TypeScript/Python/Go", "State management", "Secrets", "Policy as Code", "Testing"],
        officialUrl: "https://www.pulumi.com",
        docsUrl: "https://www.pulumi.com/docs/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "crossplane",
        name: "Crossplane",
        category: "cloud",
        icon: "✈️",
        shortDesc: "Kubernetes-native IaC",
        description: "Crossplane låter dig hantera molnresurser med Kubernetes-manifest. Infrastructure as Data.",
        installation: {
            other: "kubectl create namespace crossplane-system && helm install crossplane crossplane-stable/crossplane"
        },
        useCases: ["Multi-cloud", "GitOps infrastructure", "Self-service platforms", "Kubernetes-native IaC"],
        keyFeatures: ["Custom resources", "Compositions", "Provider ecosystem", "GitOps friendly"],
        officialUrl: "https://crossplane.io",
        docsUrl: "https://docs.crossplane.io",
        flashcardCount: 10,
        quizCount: 6
    },
    {
        slug: "cdk",
        name: "AWS CDK",
        category: "cloud",
        icon: "☁️",
        shortDesc: "Cloud Development Kit",
        description: "AWS CDK låter dig definiera molninfrastruktur med programmeringsspråk och syntetisera CloudFormation.",
        installation: {
            npm: "npm install -g aws-cdk"
        },
        useCases: ["AWS infrastructure", "CloudFormation generation", "Reusable components", "DevOps"],
        keyFeatures: ["Constructs", "TypeScript/Python/Java", "L1/L2/L3 constructs", "Assets", "Testing"],
        officialUrl: "https://aws.amazon.com/cdk/",
        docsUrl: "https://docs.aws.amazon.com/cdk/",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "serverless",
        name: "Serverless Framework",
        category: "cloud",
        icon: "⚡",
        shortDesc: "Serverless deployment",
        description: "Serverless Framework förenklar deployment av serverless applikationer på AWS, Azure, GCP.",
        installation: {
            npm: "npm install -g serverless"
        },
        useCases: ["Lambda functions", "API Gateway", "Event-driven apps", "Multi-cloud serverless"],
        keyFeatures: ["serverless.yml", "Plugins", "Multi-provider", "Local development", "Variables"],
        officialUrl: "https://www.serverless.com",
        docsUrl: "https://www.serverless.com/framework/docs",
        flashcardCount: 12,
        quizCount: 8
    },
    {
        slug: "flyway",
        name: "Flyway",
        category: "database",
        icon: "✈️",
        shortDesc: "Database migrations",
        description: "Flyway är ett verktyg för versionshantering av databaser. Migrationer med SQL eller Java.",
        installation: {
            brew: "brew install flyway",
            other: "docker run flyway/flyway"
        },
        useCases: ["Database versioning", "CI/CD migrations", "Schema management", "Team collaboration"],
        keyFeatures: ["SQL migrations", "Versioning", "Baseline", "Repair", "Callbacks", "Placeholders"],
        officialUrl: "https://flywaydb.org",
        docsUrl: "https://documentation.red-gate.com/fd",
        flashcardCount: 10,
        quizCount: 7
    },
]
