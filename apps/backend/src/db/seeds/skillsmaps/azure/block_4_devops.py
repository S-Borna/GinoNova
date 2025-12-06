"""
Azure Cloud SkillsMap - Block 4: DevOps & Automation
Nodes 13-16: Azure DevOps, Container Registry, ARM/Bicep, Azure Pipelines
"""

from typing import Any

# ============================================================================
# NODE 13: AZURE DEVOPS
# ============================================================================

AZURE_NODE_13_DEVOPS = {
    "node_id": 13,
    "title": "Azure DevOps Services",
    "slug": "azure-devops-services",
    "description": "DevOps-plattformen för planering, kodning och deployment",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 110,
    "topics_covered": [
        "azure devops", "boards", "repos", "pipelines",
        "artifacts", "test plans", "wiki"
    ],
    "content": """
# Azure DevOps Services

> *"Plan smarter, collaborate better, ship faster."*

---

## 🎯 Why This Matters

Azure DevOps är komplett DevOps-plattform:
- **Boards** - agil planering (Scrum/Kanban)
- **Repos** - Git-hosting med PRs
- **Pipelines** - CI/CD automation
- **Artifacts** - package management
- **Test Plans** - manuell/automatisk testning

---

## 🧠 Azure DevOps Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    AZURE DEVOPS SERVICES                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                      ORGANIZATION                         │   │
│  │  ┌─────────────────────────────────────────────────────┐ │   │
│  │  │                     PROJECT                          │ │   │
│  │  │                                                      │ │   │
│  │  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │ │   │
│  │  │  │ BOARDS  │ │  REPOS  │ │PIPELINES│ │ARTIFACTS│   │ │   │
│  │  │  │         │ │         │ │         │ │         │   │ │   │
│  │  │  │ Work    │ │ Git     │ │ Build   │ │ NuGet   │   │ │   │
│  │  │  │ Items   │ │ hosting │ │ Release │ │ npm     │   │ │   │
│  │  │  │ Sprints │ │ PRs     │ │ YAML    │ │ Maven   │   │ │   │
│  │  │  │ Kanban  │ │ Branch  │ │ Classic │ │ Python  │   │ │   │
│  │  │  │         │ │ policies│ │         │ │ Docker  │   │ │   │
│  │  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘   │ │   │
│  │  │                                                      │ │   │
│  │  │  ┌─────────┐ ┌─────────┐                            │ │   │
│  │  │  │  TEST   │ │  WIKI   │                            │ │   │
│  │  │  │ PLANS   │ │         │                            │ │   │
│  │  │  │ Manual  │ │ Project │                            │ │   │
│  │  │  │ tests   │ │ docs    │                            │ │   │
│  │  │  └─────────┘ └─────────┘                            │ │   │
│  │  └─────────────────────────────────────────────────────┘ │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  PRICING:                                                       │
│  - Free: 5 users, unlimited public/private repos                │
│  - Basic: $6/user/month                                         │
│  - Basic + Test Plans: $52/user/month                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Komma igång

```bash
# 1. Gå till https://dev.azure.com
# 2. Skapa organization
# 3. Skapa projekt

# CLI: Installera Azure DevOps extension
az extension add --name azure-devops

# Logga in
az devops login --organization https://dev.azure.com/myorg

# Konfigurera defaults
az devops configure --defaults organization=https://dev.azure.com/myorg project=MyProject

# Lista projekt
az devops project list --output table
```

---

## 💻 Azure Boards

```bash
# Skapa work item
az boards work-item create \\
    --title "Implement user authentication" \\
    --type "User Story" \\
    --assigned-to "developer@company.com" \\
    --area "MyProject\\Backend" \\
    --iteration "MyProject\\Sprint 1"

# Lista work items i sprint
az boards query \\
    --wiql "SELECT [System.Id], [System.Title], [System.State] FROM WorkItems WHERE [System.IterationPath] = 'MyProject\\Sprint 1'"

# Uppdatera work item
az boards work-item update \\
    --id 123 \\
    --state "In Progress"

# Skapa relation (parent/child)
az boards work-item relation add \\
    --id 123 \\
    --relation-type "System.LinkTypes.Hierarchy-Forward" \\
    --target-id 456
```

---

## 💻 Azure Repos

```bash
# Lista repos
az repos list --output table

# Skapa repo
az repos create --name "my-new-repo"

# Clone
git clone https://dev.azure.com/myorg/MyProject/_git/my-new-repo

# Branch policies (via CLI eller Portal)
# Portal: Repos → Branches → ... → Branch policies
# - Require minimum reviewers
# - Check for linked work items
# - Build validation
# - Comment resolution

# Skapa Pull Request
az repos pr create \\
    --source-branch feature/auth \\
    --target-branch main \\
    --title "Add user authentication" \\
    --description "Implements OAuth2 login" \\
    --work-items 123 456
```

---

## 💻 Azure Artifacts

```bash
# Skapa feed
az artifacts feed create --name "my-packages"

# NuGet: Lägg till feed
dotnet nuget add source https://pkgs.dev.azure.com/myorg/_packaging/my-packages/nuget/v3/index.json \\
    --name "AzureArtifacts" \\
    --username "user" \\
    --password "PAT"

# npm: Konfigurera .npmrc
# registry=https://pkgs.dev.azure.com/myorg/_packaging/my-packages/npm/registry/
# always-auth=true

# Publicera npm package
npm publish

# Python: pip install från feed
pip install my-package --index-url https://pkgs.dev.azure.com/myorg/_packaging/my-packages/pypi/simple/
```

---

## 💻 Service Connections

```bash
# Skapa service connection till Azure (för pipelines)
# Portal: Project Settings → Service connections → New service connection

# Via CLI (ARM service connection)
az devops service-endpoint azurerm create \\
    --name "Azure-Production" \\
    --azure-rm-subscription-id "xxx" \\
    --azure-rm-subscription-name "Production" \\
    --azure-rm-tenant-id "xxx" \\
    --azure-rm-service-principal-id "xxx" \\
    --azure-rm-service-principal-key "xxx"

# Visa service connections
az devops service-endpoint list --output table
```

---

## 💻 Project Settings

```bash
# Best practices för projekt:
# 1. Branch policies på main
# 2. Require work item linking
# 3. Build validation (CI) på PRs
# 4. Minimum 1 reviewer
# 5. Resolve all comments before merge

# Security: begränsa permissions
# Project Settings → Permissions → Groups
# - Contributors: läs/skriv repos
# - Readers: endast läs
# - Project Administrators: full kontroll
```

---

## ⚠️ Vanliga Problem

### Problem 1: PAT (Personal Access Token) expired

```bash
# Skapa ny PAT
# Portal → User Settings → Personal access tokens → New Token

# Scopes att välja:
# - Code: Read & write
# - Build: Read & execute
# - Packaging: Read & write
```

---

## ✅ Sammanfattning

- **Boards** för agil projekthantering
- **Repos** för Git med branch policies
- **Artifacts** för package management
- **Service Connections** kopplar till Azure
- **Free tier** är generös för små team
""",
}


# ============================================================================
# NODE 14: AZURE CONTAINER REGISTRY
# ============================================================================

AZURE_NODE_14_ACR = {
    "node_id": 14,
    "title": "Azure Container Registry",
    "slug": "azure-container-registry",
    "description": "Privat Docker registry i Azure",
    "difficulty": "intermediate",
    "estimated_minutes": 50,
    "xp_reward": 100,
    "topics_covered": [
        "container registry", "docker", "images", "tasks",
        "geo-replication", "security", "webhooks"
    ],
    "content": """
# Azure Container Registry

> *"Your private Docker Hub, but in Azure."*

---

## 🎯 Why This Matters

ACR är managed container registry:
- **Privat** - säker lagring av container images
- **Integrerat** - sömlöst med AKS, App Service, Functions
- **CI/CD** - ACR Tasks bygger images
- **Geo-replicated** - snabb pull från närmaste region

---

## 🧠 ACR Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    AZURE CONTAINER REGISTRY                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    ACR: myregistry                        │   │
│  │                                                           │   │
│  │  ┌──────────────────────────────────────────────────┐    │   │
│  │  │  REPOSITORY: myapp                                │    │   │
│  │  │  ┌─────────┐ ┌─────────┐ ┌─────────┐            │    │   │
│  │  │  │ :latest │ │ :v1.0.0 │ │ :abc123 │            │    │   │
│  │  │  │  (tag)  │ │  (tag)  │ │ (commit)│            │    │   │
│  │  │  └─────────┘ └─────────┘ └─────────┘            │    │   │
│  │  └──────────────────────────────────────────────────┘    │   │
│  │                                                           │   │
│  │  ┌──────────────────────────────────────────────────┐    │   │
│  │  │  REPOSITORY: api                                  │    │   │
│  │  │  ┌─────────┐ ┌─────────┐                         │    │   │
│  │  │  │ :prod   │ │ :dev    │                         │    │   │
│  │  │  └─────────┘ └─────────┘                         │    │   │
│  │  └──────────────────────────────────────────────────┘    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  TIERS:                                                         │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ Basic        │ Standard     │ Premium                   │    │
│  │ - 10GB       │ - 100GB      │ - 500GB                   │    │
│  │ - ~$5/mån    │ - ~$20/mån   │ - ~$50/mån                │    │
│  │              │              │ - Geo-replication         │    │
│  │              │              │ - Private Link            │    │
│  │              │              │ - Content trust           │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Skapa ACR

```bash
# Skapa Container Registry
az acr create \\
    --name myregistry123 \\
    --resource-group rg-demo \\
    --location northeurope \\
    --sku Standard \\
    --admin-enabled true

# Visa login server
az acr show --name myregistry123 --query loginServer

# Logga in med Docker
az acr login --name myregistry123

# Alternativt med credentials
docker login myregistry123.azurecr.io \\
    --username myregistry123 \\
    --password $(az acr credential show --name myregistry123 --query "passwords[0].value" -o tsv)
```

---

## 💻 Push/Pull Images

```bash
# Tagga lokal image för ACR
docker tag myapp:latest myregistry123.azurecr.io/myapp:latest
docker tag myapp:latest myregistry123.azurecr.io/myapp:v1.0.0

# Push till ACR
docker push myregistry123.azurecr.io/myapp:latest
docker push myregistry123.azurecr.io/myapp:v1.0.0

# Lista repositories
az acr repository list --name myregistry123 --output table

# Lista tags
az acr repository show-tags --name myregistry123 --repository myapp --output table

# Pull image
docker pull myregistry123.azurecr.io/myapp:v1.0.0
```

---

## 💻 ACR Tasks (Build i molnet)

```bash
# Quick build (bygg direkt i ACR)
az acr build \\
    --registry myregistry123 \\
    --image myapp:{{.Run.ID}} \\
    --file Dockerfile \\
    .

# Automatisk build vid git push
az acr task create \\
    --name build-on-push \\
    --registry myregistry123 \\
    --context https://github.com/myorg/myapp.git \\
    --file Dockerfile \\
    --image myapp:{{.Run.ID}} \\
    --git-access-token $GITHUB_PAT

# Multi-step task (YAML)
cat << 'EOF' > acr-task.yaml
version: v1.1.0
steps:
  - build: -t {{.Run.Registry}}/myapp:{{.Run.ID}} -f Dockerfile .
  - push:
    - {{.Run.Registry}}/myapp:{{.Run.ID}}
    - {{.Run.Registry}}/myapp:latest
  - cmd: docker run {{.Run.Registry}}/myapp:{{.Run.ID}} npm test
EOF

az acr task create \\
    --name build-test-push \\
    --registry myregistry123 \\
    --context https://github.com/myorg/myapp.git \\
    --file acr-task.yaml
```

---

## 💻 Security

```bash
# Aktivera Content Trust (signerade images)
az acr config content-trust update \\
    --name myregistry123 \\
    --status Enabled

# Private Link (ingen public access)
az acr update \\
    --name myregistry123 \\
    --public-network-enabled false

# Skapa private endpoint
az network private-endpoint create \\
    --name pe-acr \\
    --resource-group rg-demo \\
    --vnet-name vnet-myapp \\
    --subnet snet-private \\
    --private-connection-resource-id $(az acr show --name myregistry123 --query id -o tsv) \\
    --group-id registry \\
    --connection-name acr-connection

# RBAC för pull-only access
az role assignment create \\
    --role AcrPull \\
    --assignee <principal-id> \\
    --scope $(az acr show --name myregistry123 --query id -o tsv)
```

---

## 💻 Integration med AKS

```bash
# Attach ACR till AKS (enklast!)
az aks update \\
    --name aks-myapp \\
    --resource-group rg-demo \\
    --attach-acr myregistry123

# Nu kan AKS pusha/pulla utan explicit credentials!

# I Kubernetes deployment:
# image: myregistry123.azurecr.io/myapp:v1.0.0
```

---

## 💻 Cleanup & Retention

```bash
# Radera gammal tag
az acr repository delete \\
    --name myregistry123 \\
    --image myapp:old-tag \\
    --yes

# Purge untagged images (manifests)
az acr run \\
    --registry myregistry123 \\
    --cmd "acr purge --filter 'myapp:.*' --untagged --ago 30d --dry-run" \\
    /dev/null

# Faktisk purge (utan --dry-run)
az acr run \\
    --registry myregistry123 \\
    --cmd "acr purge --filter 'myapp:.*' --untagged --ago 30d" \\
    /dev/null

# Scheduled cleanup (task)
az acr task create \\
    --name weekly-purge \\
    --registry myregistry123 \\
    --cmd "acr purge --filter '.*:.*' --untagged --ago 7d" \\
    --schedule "0 0 * * 0" \\
    --context /dev/null
```

---

## ⚠️ Vanliga Problem

### Problem 1: "unauthorized: authentication required"

```bash
# Logga in igen
az acr login --name myregistry123

# Kontrollera token
docker logout myregistry123.azurecr.io
az acr login --name myregistry123
```

---

## ✅ Sammanfattning

- **ACR** är private Docker registry
- **ACR Tasks** bygger images i molnet
- **Attach till AKS** för sömlös integration
- **Premium** för geo-replication och private link
- **Purge policies** håller registret rent
""",
}


# ============================================================================
# NODE 15: ARM TEMPLATES & BICEP
# ============================================================================

AZURE_NODE_15_BICEP = {
    "node_id": 15,
    "title": "ARM Templates & Bicep",
    "slug": "azure-arm-bicep",
    "description": "Infrastructure as Code för Azure",
    "difficulty": "intermediate",
    "estimated_minutes": 65,
    "xp_reward": 120,
    "topics_covered": [
        "arm templates", "bicep", "iac", "deployments",
        "parameters", "modules", "what-if"
    ],
    "content": """
# ARM Templates & Bicep

> *"Define your infrastructure in code, deploy it anywhere."*

---

## 🎯 Why This Matters

Infrastructure as Code för Azure:
- **Reproducerbart** - samma infra varje gång
- **Version-kontroll** - Git för infrastruktur
- **Automation** - deploy med CI/CD
- **Validering** - what-if innan deployment

---

## 🧠 ARM vs Bicep

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARM TEMPLATES vs BICEP                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ARM TEMPLATE (JSON)           BICEP (.bicep)                   │
│  ┌─────────────────────┐      ┌─────────────────────┐          │
│  │ {                   │      │ param location string│          │
│  │   "$schema": "...", │  →   │ param name string    │          │
│  │   "parameters": {   │      │                      │          │
│  │     "location": {}  │      │ resource sa 'Micro.. │          │
│  │   },                │      │   name: name         │          │
│  │   "resources": [...]│      │   location: location │          │
│  │ }                   │      │ }                    │          │
│  └─────────────────────┘      └─────────────────────┘          │
│                                                                  │
│  ARM:                          Bicep:                           │
│  ✓ Azure native               ✓ Enklare syntax                  │
│  ✗ Verbose (mycket JSON)      ✓ Typad, IntelliSense             │
│  ✗ Svårt att läsa             ✓ Moduler                         │
│                               ✓ Kompileras till ARM              │
│                                                                  │
│  REKOMMENDATION: Använd Bicep för nya projekt!                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Bicep Basics

```bicep
// main.bicep

// ========================================
// PARAMETERS
// ========================================
@description('Azure region for resources')
param location string = resourceGroup().location

@description('Environment name')
@allowed(['dev', 'test', 'prod'])
param environment string = 'dev'

@description('Application name')
@minLength(3)
@maxLength(20)
param appName string

// ========================================
// VARIABLES
// ========================================
var storageAccountName = 'st${appName}${environment}${uniqueString(resourceGroup().id)}'
var appServicePlanName = 'asp-${appName}-${environment}'
var webAppName = 'app-${appName}-${environment}'

// ========================================
// RESOURCES
// ========================================

// Storage Account
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
  }
  tags: {
    environment: environment
  }
}

// App Service Plan
resource appServicePlan 'Microsoft.Web/serverfarms@2023-01-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: environment == 'prod' ? 'P1v3' : 'B1'
  }
  kind: 'linux'
  properties: {
    reserved: true
  }
}

// Web App
resource webApp 'Microsoft.Web/sites@2023-01-01' = {
  name: webAppName
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: 'NODE|18-lts'
      appSettings: [
        {
          name: 'STORAGE_CONNECTION_STRING'
          value: storageAccount.properties.primaryEndpoints.blob
        }
      ]
    }
  }
}

// ========================================
// OUTPUTS
// ========================================
output webAppUrl string = 'https://${webApp.properties.defaultHostName}'
output storageAccountName string = storageAccount.name
```

---

## 💻 Parameters File

```json
// parameters.prod.json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "environment": {
      "value": "prod"
    },
    "appName": {
      "value": "mywebapp"
    }
  }
}
```

---

## 💻 Deploy Bicep

```bash
# Installera Bicep (inkluderat i Azure CLI)
az bicep version
az bicep upgrade

# Validera template
az deployment group validate \\
    --resource-group rg-demo \\
    --template-file main.bicep \\
    --parameters environment=dev appName=myapp

# What-if (preview changes)
az deployment group what-if \\
    --resource-group rg-demo \\
    --template-file main.bicep \\
    --parameters environment=dev appName=myapp

# Deploy
az deployment group create \\
    --resource-group rg-demo \\
    --template-file main.bicep \\
    --parameters environment=dev appName=myapp

# Deploy med parameter-fil
az deployment group create \\
    --resource-group rg-demo \\
    --template-file main.bicep \\
    --parameters @parameters.prod.json

# Visa deployment outputs
az deployment group show \\
    --resource-group rg-demo \\
    --name main \\
    --query properties.outputs
```

---

## 💻 Bicep Modules

```bicep
// modules/storage.bicep
param name string
param location string = resourceGroup().location
param sku string = 'Standard_LRS'

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: name
  location: location
  sku: {
    name: sku
  }
  kind: 'StorageV2'
}

output connectionString string = 'DefaultEndpointsProtocol=https;AccountName=${storageAccount.name};AccountKey=${storageAccount.listKeys().keys[0].value}'
output primaryEndpoint string = storageAccount.properties.primaryEndpoints.blob

// main.bicep - använd modul
module storage 'modules/storage.bicep' = {
  name: 'storage-deployment'
  params: {
    name: 'stmyapp${uniqueString(resourceGroup().id)}'
    location: location
    sku: 'Standard_LRS'
  }
}

// Referera till module output
output storageEndpoint string = storage.outputs.primaryEndpoint
```

---

## 💻 Loops & Conditions

```bicep
// Loop över lista
param locations array = ['northeurope', 'westeurope']

resource storageAccounts 'Microsoft.Storage/storageAccounts@2023-01-01' = [for (loc, i) in locations: {
  name: 'st${uniqueString(resourceGroup().id)}${i}'
  location: loc
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}]

// Conditional deployment
param deployRedis bool = false

resource redisCache 'Microsoft.Cache/redis@2023-04-01' = if (deployRedis) {
  name: 'redis-${uniqueString(resourceGroup().id)}'
  location: resourceGroup().location
  properties: {
    sku: {
      name: 'Basic'
      family: 'C'
      capacity: 0
    }
  }
}
```

---

## 💻 Complete Example: Full Stack

```bicep
// infra/main.bicep
targetScope = 'resourceGroup'

param environment string
param location string = resourceGroup().location

// Modules
module network 'modules/network.bicep' = {
  name: 'network'
  params: {
    location: location
    environment: environment
  }
}

module database 'modules/database.bicep' = {
  name: 'database'
  params: {
    location: location
    subnetId: network.outputs.dbSubnetId
  }
}

module webapp 'modules/webapp.bicep' = {
  name: 'webapp'
  params: {
    location: location
    dbConnectionString: database.outputs.connectionString
  }
}

output appUrl string = webapp.outputs.url
```

---

## ⚠️ Vanliga Problem

### Problem 1: "Resource already exists"

```bash
# Bicep är deklarativt - existerande resurser uppdateras
# Men om name ändras skapas ny resurs

# Lösning: använd what-if först
az deployment group what-if ...
```

---

## ✅ Sammanfattning

- **Bicep** är enklare än ARM JSON
- **Modules** för återanvändbara komponenter
- **What-if** innan deployment
- **Parameters** för miljö-specifik config
- **Loops & conditions** för dynamiska templates
""",
}


# ============================================================================
# NODE 16: AZURE PIPELINES
# ============================================================================

AZURE_NODE_16_PIPELINES = {
    "node_id": 16,
    "title": "Azure Pipelines",
    "slug": "azure-pipelines",
    "description": "CI/CD automation med Azure Pipelines",
    "difficulty": "intermediate",
    "estimated_minutes": 70,
    "xp_reward": 130,
    "topics_covered": [
        "azure pipelines", "yaml", "stages", "jobs",
        "environments", "approvals", "templates"
    ],
    "content": """
# Azure Pipelines

> *"Automate your build, test, and deployment."*

---

## 🎯 Why This Matters

Azure Pipelines för CI/CD:
- **Multi-platform** - Windows, Linux, macOS
- **Language-agnostic** - alla språk och frameworks
- **Cloud-native** - tight Azure-integration
- **YAML-based** - pipeline as code

---

## 🧠 Pipeline Structure

```
┌─────────────────────────────────────────────────────────────────┐
│                    AZURE PIPELINE STRUCTURE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PIPELINE (azure-pipelines.yml)                                 │
│  │                                                               │
│  ├── TRIGGER (when to run)                                      │
│  │   └── branches, paths, tags                                  │
│  │                                                               │
│  ├── VARIABLES                                                   │
│  │   └── inline, groups, secrets                                │
│  │                                                               │
│  └── STAGES                                                      │
│      │                                                           │
│      ├── Stage: Build                                           │
│      │   └── Jobs                                               │
│      │       └── Job: Build                                     │
│      │           └── Steps                                      │
│      │               ├── checkout                               │
│      │               ├── script: npm install                    │
│      │               ├── script: npm test                       │
│      │               └── publish artifact                       │
│      │                                                           │
│      ├── Stage: Deploy-Dev                                      │
│      │   └── Jobs                                               │
│      │       └── Deployment: dev                                │
│      │           └── Steps                                      │
│      │               └── deploy to dev                          │
│      │                                                           │
│      └── Stage: Deploy-Prod                                     │
│          └── condition: succeeded()                             │
│          └── Jobs                                               │
│              └── Deployment: prod                               │
│                  └── approval required                          │
│                  └── Steps                                      │
│                      └── deploy to prod                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Basic Pipeline

```yaml
# azure-pipelines.yml

trigger:
  branches:
    include:
      - main
      - develop
  paths:
    exclude:
      - '*.md'
      - 'docs/**'

pool:
  vmImage: 'ubuntu-latest'

variables:
  nodeVersion: '18.x'
  
stages:
  - stage: Build
    displayName: 'Build & Test'
    jobs:
      - job: BuildJob
        displayName: 'Build Application'
        steps:
          - task: NodeTool@0
            inputs:
              versionSpec: $(nodeVersion)
            displayName: 'Install Node.js'
          
          - script: |
              npm ci
              npm run build
              npm test
            displayName: 'Install, Build, Test'
          
          - task: PublishTestResults@2
            inputs:
              testResultsFormat: 'JUnit'
              testResultsFiles: '**/test-results.xml'
            displayName: 'Publish Test Results'
          
          - task: PublishBuildArtifacts@1
            inputs:
              pathtoPublish: 'dist'
              artifactName: 'app'
            displayName: 'Publish Artifact'
```

---

## 💻 Multi-Stage Pipeline

```yaml
# azure-pipelines.yml

trigger:
  - main

variables:
  - group: 'my-variable-group'  # Från Library
  - name: dockerRegistry
    value: 'myregistry.azurecr.io'

stages:
  # ========================================
  # STAGE 1: BUILD
  # ========================================
  - stage: Build
    displayName: 'Build'
    jobs:
      - job: Build
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: Docker@2
            inputs:
              containerRegistry: 'ACR-Connection'
              repository: 'myapp'
              command: 'buildAndPush'
              Dockerfile: 'Dockerfile'
              tags: |
                $(Build.BuildId)
                latest
          
          - publish: 'k8s'
            artifact: 'manifests'
  
  # ========================================
  # STAGE 2: DEPLOY TO DEV
  # ========================================
  - stage: DeployDev
    displayName: 'Deploy to Dev'
    dependsOn: Build
    condition: succeeded()
    jobs:
      - deployment: DeployDev
        displayName: 'Deploy to Dev Environment'
        environment: 'dev'
        pool:
          vmImage: 'ubuntu-latest'
        strategy:
          runOnce:
            deploy:
              steps:
                - download: current
                  artifact: manifests
                
                - task: KubernetesManifest@0
                  inputs:
                    action: 'deploy'
                    kubernetesServiceConnection: 'AKS-Dev'
                    namespace: 'default'
                    manifests: '$(Pipeline.Workspace)/manifests/*.yaml'
                    containers: '$(dockerRegistry)/myapp:$(Build.BuildId)'
  
  # ========================================
  # STAGE 3: DEPLOY TO PROD
  # ========================================
  - stage: DeployProd
    displayName: 'Deploy to Production'
    dependsOn: DeployDev
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployProd
        displayName: 'Deploy to Production'
        environment: 'production'  # Requires approval!
        pool:
          vmImage: 'ubuntu-latest'
        strategy:
          runOnce:
            deploy:
              steps:
                - download: current
                  artifact: manifests
                
                - task: KubernetesManifest@0
                  inputs:
                    action: 'deploy'
                    kubernetesServiceConnection: 'AKS-Prod'
                    namespace: 'default'
                    manifests: '$(Pipeline.Workspace)/manifests/*.yaml'
                    containers: '$(dockerRegistry)/myapp:$(Build.BuildId)'
```

---

## 💻 Environments & Approvals

```bash
# Skapa environment i Portal:
# Pipelines → Environments → New environment

# Konfigurera approvals:
# Environment → ... → Approvals and checks → Add check → Approvals

# Approvals konfiguration:
# - Required approvers
# - Timeout (ex: 7 dagar)
# - Instructions
```

---

## 💻 Templates

```yaml
# templates/build-template.yml
parameters:
  - name: nodeVersion
    type: string
    default: '18.x'

steps:
  - task: NodeTool@0
    inputs:
      versionSpec: ${{ parameters.nodeVersion }}
  
  - script: npm ci
    displayName: 'Install dependencies'
  
  - script: npm run build
    displayName: 'Build'
  
  - script: npm test
    displayName: 'Test'

# azure-pipelines.yml - använd template
stages:
  - stage: Build
    jobs:
      - job: Build
        steps:
          - template: templates/build-template.yml
            parameters:
              nodeVersion: '20.x'
```

---

## 💻 Secrets & Variable Groups

```yaml
# Variable group från Library
variables:
  - group: 'production-secrets'  # Innehåller: DB_PASSWORD, API_KEY

# Använd i script
steps:
  - script: |
      echo "Connecting to database..."
      # $(DB_PASSWORD) är masked i logs
      npm run migrate
    env:
      DATABASE_URL: $(DB_CONNECTION_STRING)
      
# Key Vault integration
variables:
  - group: 'kv-secrets'  # Linked to Azure Key Vault
```

---

## 💻 PR Validation

```yaml
# azure-pipelines.yml
trigger:
  - main

pr:
  branches:
    include:
      - main
  paths:
    exclude:
      - '*.md'

stages:
  - stage: Validate
    displayName: 'PR Validation'
    jobs:
      - job: Build
        steps:
          - script: npm ci && npm test
          - script: npm run lint
          
      - job: SecurityScan
        steps:
          - task: CredScan@2
          - task: OWASP@2
```

---

## ⚠️ Vanliga Problem

### Problem 1: "Pipeline not triggered"

```yaml
# Kontrollera trigger syntax
trigger:
  branches:
    include:
      - main  # Inte 'master' om du bytt namn
  
# Path filters kan blockera
paths:
  include:
    - 'src/**'  # Om ändring är i docs/, triggas inte
```

---

## ✅ Sammanfattning

- **YAML pipelines** för versionskontrollerad CI/CD
- **Stages** för build → test → deploy flow
- **Environments** med approvals för production
- **Templates** för återanvändbarhet
- **Variable groups** för secrets management
""",
}


# Export all nodes from Block 4
BLOCK_4_NODES = [
    AZURE_NODE_13_DEVOPS,
    AZURE_NODE_14_ACR,
    AZURE_NODE_15_BICEP,
    AZURE_NODE_16_PIPELINES,
]
