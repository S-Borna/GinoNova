"""
Azure Cloud SkillsMap - Block 1: Azure Fundamentals
Nodes 1-4: Intro, Resource Management, Portal/CLI, Subscriptions
"""

from typing import Any

# ============================================================================
# NODE 1: INTRODUCTION TO AZURE
# ============================================================================

AZURE_NODE_1_INTRO = {
    "node_id": 1,
    "title": "Introduction to Azure",
    "slug": "azure-introduction",
    "description": "Förstå Microsoft Azure och cloud computing koncept",
    "difficulty": "beginner",
    "estimated_minutes": 45,
    "xp_reward": 80,
    "topics_covered": [
        "azure overview", "cloud computing", "regions", "availability zones",
        "iaas", "paas", "saas", "azure services"
    ],
    "content": """
# Introduction to Azure

> *"The cloud isn't about where you store your stuff - it's about what you can do."*

---

## 🎯 Why This Matters

Microsoft Azure är världens näst största molnplattform:
- **200+ tjänster** - compute, storage, AI, IoT och mer
- **60+ regioner** - global täckning
- **$80B+ omsättning** - massivt ekosystem
- **Enterprise-fokus** - stark integration med Microsoft-produkter

---

## 🧠 Cloud Computing Models

```
┌─────────────────────────────────────────────────────────────────┐
│              CLOUD COMPUTING MODELS                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ON-PREMISES        IaaS           PaaS           SaaS         │
│  ┌───────────┐   ┌───────────┐  ┌───────────┐  ┌───────────┐   │
│  │Applications│   │Applications│  │Applications│  │Applications│   │
│  ├───────────┤   ├───────────┤  ├───────────┤  ├───────────┤   │
│  │  Runtime  │   │  Runtime  │  │  Runtime  │  │  Runtime  │   │
│  ├───────────┤   ├───────────┤  ├───────────┤  ├───────────┤   │
│  │    OS     │   │    OS     │  │    OS     │  │    OS     │   │
│  ├───────────┤   ├───────────┤  ├───────────┤  ├───────────┤   │
│  │   VMs     │   │   VMs     │  │   VMs     │  │   VMs     │   │
│  ├───────────┤   ├───────────┤  ├───────────┤  ├───────────┤   │
│  │  Storage  │   │  Storage  │  │  Storage  │  │  Storage  │   │
│  ├───────────┤   ├───────────┤  ├───────────┤  ├───────────┤   │
│  │ Network   │   │ Network   │  │ Network   │  │ Network   │   │
│  └───────────┘   └───────────┘  └───────────┘  └───────────┘   │
│       │              │              │              │             │
│     YOU           YOU/AZURE      AZURE          AZURE           │
│   MANAGE          MANAGE         MANAGES        MANAGES         │
│                                                                  │
│  Examples:       Examples:      Examples:      Examples:        │
│  Your server     Azure VMs      App Service    Microsoft 365    │
│  room            Azure          Functions      Dynamics 365     │
│                  Storage        AKS            Power BI         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Azure Global Infrastructure

```
┌─────────────────────────────────────────────────────────────────┐
│                 AZURE GLOBAL INFRASTRUCTURE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  GEOGRAPHY (Geopolitical boundary)                              │
│  └── REGION (Data center cluster)                               │
│      └── AVAILABILITY ZONE (Isolated data center)               │
│                                                                  │
│  Example: Europe Geography                                       │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  North Europe Region (Ireland)                             │  │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐                   │  │
│  │  │  AZ 1   │  │  AZ 2   │  │  AZ 3   │                   │  │
│  │  │ (DC 1)  │  │ (DC 2)  │  │ (DC 3)  │                   │  │
│  │  └─────────┘  └─────────┘  └─────────┘                   │  │
│  │       ↑____________↑____________↑                         │  │
│  │              Low-latency network                          │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  Popular Regions:                                               │
│  • West Europe (Netherlands)                                    │
│  • North Europe (Ireland)                                       │
│  • Sweden Central (Gävle)                                       │
│  • UK South (London)                                            │
│  • East US / West US                                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Core Azure Services

| Kategori | Tjänster | Användning |
|----------|----------|------------|
| **Compute** | VMs, App Service, Functions, AKS | Kör applikationer |
| **Storage** | Blob, Files, Queues, Tables | Lagra data |
| **Database** | SQL Database, Cosmos DB, PostgreSQL | Relationell/NoSQL |
| **Networking** | VNet, Load Balancer, VPN Gateway | Nätverksinfrastruktur |
| **Identity** | Azure AD, RBAC | Autentisering/auktorisering |
| **DevOps** | Azure DevOps, Container Registry | CI/CD |
| **AI/ML** | Cognitive Services, Azure ML | Machine Learning |
| **Monitoring** | Azure Monitor, Log Analytics | Övervakning |

---

## 💻 Azure vs AWS vs GCP

| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| **Styrka** | Enterprise, Microsoft-integration | Market leader, most services | Data/ML, Kubernetes |
| **IaaS** | Virtual Machines | EC2 | Compute Engine |
| **PaaS** | App Service | Elastic Beanstalk | App Engine |
| **Serverless** | Functions | Lambda | Cloud Functions |
| **Containers** | AKS | EKS | GKE |
| **Storage** | Blob Storage | S3 | Cloud Storage |
| **Database** | Azure SQL, Cosmos DB | RDS, DynamoDB | Cloud SQL, Firestore |

---

## 💻 Skapa Azure-konto

```bash
# 1. Gå till https://azure.microsoft.com/free
# 2. Registrera med Microsoft-konto
# 3. Du får $200 kredit i 30 dagar + 12 månader gratistjänster

# Free tier inkluderar:
# - 750h B1s Linux VM (12 mån)
# - 750h B1s Windows VM (12 mån)
# - 5GB Blob Storage (12 mån)
# - Azure App Service (alltid gratis)
# - Azure Functions (1M requests/mån)
```

---

## ⚠️ Vanliga Kostnadsmisstag

### Misstag 1: Glömda resurser

```bash
# ❌ Glömt bort att stänga av VM
# → $100+/månad för en oanvänd VM

# ✅ Sätt budget-alerts
# Azure Portal → Cost Management → Budgets
```

### Misstag 2: Fel region

```bash
# ❌ Väljer region utan att tänka på kostnad
# → US-regioner ofta billigare än Europa

# ✅ Jämför priser
# https://azure.microsoft.com/pricing/calculator
```

---

## ✅ Sammanfattning

- **Azure** är enterprise-fokuserad molnplattform
- **IaaS/PaaS/SaaS** - olika ansvarsnivåer
- **Regioner & Zoner** för high availability
- **Free tier** för att lära sig
- **Sätt budget-alerts** för kostnadskontroll
""",
}


# ============================================================================
# NODE 2: RESOURCE MANAGEMENT
# ============================================================================

AZURE_NODE_2_RESOURCES = {
    "node_id": 2,
    "title": "Resource Groups & Management",
    "slug": "azure-resource-management",
    "description": "Hantera Azure-resurser med Resource Groups och Tags",
    "difficulty": "beginner",
    "estimated_minutes": 50,
    "xp_reward": 90,
    "topics_covered": [
        "resource groups", "azure resources", "tags", "locks",
        "management groups", "subscriptions", "arm templates"
    ],
    "content": """
# Resource Groups & Management

> *"A well-organized cloud is a manageable cloud."*

---

## 🎯 Why This Matters

Resource management är grunden för Azure:
- **Organisation** - gruppera relaterade resurser
- **Access Control** - sätt rättigheter på grupp-nivå
- **Cost Tracking** - följ kostnader per projekt
- **Lifecycle** - radera hela miljöer med ett kommando

---

## 🧠 Azure Resource Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                 AZURE RESOURCE HIERARCHY                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              Azure Active Directory (Tenant)             │    │
│  │  Identiteter, användare, grupper, service principals    │    │
│  └─────────────────────────────────────────────────────────┘    │
│                           │                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                Management Groups (Optional)              │    │
│  │  Gruppera subscriptions för policy och RBAC              │    │
│  └─────────────────────────────────────────────────────────┘    │
│                           │                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                     Subscriptions                        │    │
│  │  Faktureringsenheter, en per miljö eller avdelning       │    │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐     │    │
│  │  │ Dev Subscr.  │ │ Test Subscr. │ │ Prod Subscr. │     │    │
│  │  └──────────────┘ └──────────────┘ └──────────────┘     │    │
│  └─────────────────────────────────────────────────────────┘    │
│                           │                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   Resource Groups                        │    │
│  │  Logiska containrar för relaterade resurser              │    │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐           │    │
│  │  │ rg-web-dev │ │rg-api-dev  │ │ rg-db-dev  │           │    │
│  │  └────────────┘ └────────────┘ └────────────┘           │    │
│  └─────────────────────────────────────────────────────────┘    │
│                           │                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                      Resources                           │    │
│  │  VMs, Storage, Databases, App Services, etc.             │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Resource Groups

```bash
# Azure CLI - skapa resource group
az group create \\
    --name rg-myproject-dev \\
    --location northeurope \\
    --tags Environment=Development Project=MyProject Owner=team@company.com

# Lista resource groups
az group list --output table

# Visa resurser i en group
az resource list --resource-group rg-myproject-dev --output table

# Ta bort HELA resource group (alla resurser!)
az group delete --name rg-myproject-dev --yes --no-wait
```

---

## 💻 Naming Conventions

```
┌─────────────────────────────────────────────────────────────────┐
│             AZURE NAMING CONVENTION (Microsoft CAF)              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Format: {resource-type}-{workload}-{environment}-{region}-{#}  │
│                                                                  │
│  Examples:                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ Resource Group:    rg-webshop-prod-ne-001               │    │
│  │ Virtual Machine:   vm-webshop-prod-ne-001               │    │
│  │ Storage Account:   stwebshopprodne001 (no hyphens!)     │    │
│  │ App Service:       app-webshop-prod-ne-001              │    │
│  │ SQL Database:      sql-webshop-prod-ne-001              │    │
│  │ Key Vault:         kv-webshop-prod-ne-001               │    │
│  │ Virtual Network:   vnet-webshop-prod-ne-001             │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  Common Prefixes:                                                │
│  rg   = Resource Group     vm   = Virtual Machine               │
│  st   = Storage Account    sql  = SQL Database                  │
│  app  = App Service        func = Function App                  │
│  kv   = Key Vault          vnet = Virtual Network               │
│  nsg  = Network Security   pip  = Public IP                     │
│                                                                  │
│  Environment:                                                    │
│  dev = Development         test = Testing                       │
│  stg = Staging             prod = Production                    │
│                                                                  │
│  Region:                                                         │
│  ne = North Europe         we = West Europe                     │
│  eus = East US             wus = West US                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Tags

```bash
# Lägg till tags vid skapande
az group create \\
    --name rg-myproject-prod \\
    --location northeurope \\
    --tags \\
        Environment=Production \\
        Project=MyProject \\
        CostCenter=CC-123 \\
        Owner=team@company.com \\
        CreatedBy=terraform

# Uppdatera tags på befintlig resurs
az resource tag \\
    --tags Environment=Production CostCenter=CC-123 \\
    --ids /subscriptions/xxx/resourceGroups/rg-myproject/providers/...

# Filtrera resurser på tag
az resource list --tag Environment=Production --output table

# Visa kostnader per tag i Cost Management
# Azure Portal → Cost Management → Cost Analysis → Group by: Tag
```

---

## 💻 Resource Locks

```bash
# Skapa lock som förhindrar radering
az lock create \\
    --name DoNotDelete \\
    --resource-group rg-production \\
    --lock-type CanNotDelete \\
    --notes "Production environment - do not delete"

# Skapa ReadOnly lock (förhindrar ändringar)
az lock create \\
    --name ReadOnly \\
    --resource-group rg-production \\
    --lock-type ReadOnly

# Lista locks
az lock list --resource-group rg-production --output table

# Ta bort lock (krävs för att kunna radera)
az lock delete --name DoNotDelete --resource-group rg-production
```

---

## 💻 Best Practices

### Resource Group Design

```bash
# ✅ Gruppera efter livscykel
rg-webshop-frontend-prod    # Frontend-resurser
rg-webshop-backend-prod     # Backend-resurser
rg-webshop-shared-prod      # Delade resurser

# ✅ Gruppera efter miljö
rg-myapp-dev
rg-myapp-test
rg-myapp-prod

# ❌ Undvik att blanda miljöer
# rg-all-resources (blandar dev och prod!)
```

---

## ⚠️ Vanliga Misstag

### Misstag: Radera resource group med produktion

```bash
# ⚠️ Detta raderar ALLT i gruppen!
az group delete --name rg-production

# ✅ Använd locks för kritiska miljöer
az lock create --name critical --resource-group rg-production --lock-type CanNotDelete
```

---

## ✅ Sammanfattning

- **Resource Groups** grupperar relaterade resurser
- **Naming conventions** för tydlighet
- **Tags** för organisation och kostnadsspårning
- **Locks** skyddar mot oavsiktlig radering
- **Subscription-design** separerar miljöer
""",
}


# ============================================================================
# NODE 3: AZURE PORTAL & CLI
# ============================================================================

AZURE_NODE_3_PORTAL_CLI = {
    "node_id": 3,
    "title": "Azure Portal & CLI",
    "slug": "azure-portal-cli",
    "description": "Navigera Azure Portal och använda Azure CLI",
    "difficulty": "beginner",
    "estimated_minutes": 55,
    "xp_reward": 100,
    "topics_covered": [
        "azure portal", "azure cli", "cloud shell", "az commands",
        "powershell", "authentication", "scripting"
    ],
    "content": """
# Azure Portal & CLI

> *"The CLI is for automation, the portal is for exploration."*

---

## 🎯 Why This Matters

Flera sätt att hantera Azure:
- **Portal** - visuell, bra för utforskning
- **CLI** - scriptbar, snabb för repetitiva uppgifter
- **PowerShell** - för Windows-admins
- **ARM/Bicep** - Infrastructure as Code

---

## 🧠 Azure Management Tools

```
┌─────────────────────────────────────────────────────────────────┐
│                 AZURE MANAGEMENT TOOLS                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    AZURE PORTAL                           │   │
│  │  https://portal.azure.com                                 │   │
│  │  ✓ Visual interface                                       │   │
│  │  ✓ Best for exploration                                   │   │
│  │  ✓ Dashboards & monitoring                                │   │
│  │  ✗ Hard to automate                                       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                           │                                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                      AZURE CLI                            │   │
│  │  az <service> <command>                                   │   │
│  │  ✓ Cross-platform (Windows, Mac, Linux)                   │   │
│  │  ✓ Scriptable (bash, zsh)                                 │   │
│  │  ✓ JSON output for parsing                                │   │
│  │  ✓ Tab completion                                         │   │
│  └──────────────────────────────────────────────────────────┘   │
│                           │                                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                   AZURE POWERSHELL                        │   │
│  │  Connect-AzAccount / Get-AzResource                       │   │
│  │  ✓ Native PowerShell cmdlets                              │   │
│  │  ✓ Good for Windows admins                                │   │
│  │  ✓ Object-oriented output                                 │   │
│  └──────────────────────────────────────────────────────────┘   │
│                           │                                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    CLOUD SHELL                            │   │
│  │  shell.azure.com                                          │   │
│  │  ✓ Browser-based CLI                                      │   │
│  │  ✓ No installation needed                                 │   │
│  │  ✓ Pre-authenticated                                      │   │
│  │  ✓ Has az, kubectl, terraform, etc.                       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Azure CLI Installation

```bash
# macOS
brew install azure-cli

# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Windows (PowerShell as Admin)
winget install Microsoft.AzureCLI

# Docker
docker run -it mcr.microsoft.com/azure-cli

# Verifiera
az --version
```

---

## 💻 Azure CLI Basics

```bash
# Logga in
az login
# Öppnar webbläsare för autentisering

# Logga in med service principal (CI/CD)
az login --service-principal \\
    --username $AZURE_CLIENT_ID \\
    --password $AZURE_CLIENT_SECRET \\
    --tenant $AZURE_TENANT_ID

# Visa konto
az account show

# Lista subscriptions
az account list --output table

# Byt subscription
az account set --subscription "My Subscription Name"

# Visa aktuell subscription
az account show --query name -o tsv
```

---

## 💻 Vanliga az-kommandon

```bash
# ═══════════════════════════════════════════════════════════════
# RESOURCE GROUPS
# ═══════════════════════════════════════════════════════════════

# Skapa
az group create --name rg-demo --location northeurope

# Lista
az group list --output table

# Radera
az group delete --name rg-demo --yes

# ═══════════════════════════════════════════════════════════════
# VIRTUAL MACHINES
# ═══════════════════════════════════════════════════════════════

# Skapa VM
az vm create \\
    --resource-group rg-demo \\
    --name vm-demo \\
    --image Ubuntu2204 \\
    --admin-username azureuser \\
    --generate-ssh-keys \\
    --size Standard_B1s

# Lista VMs
az vm list --output table

# Starta/Stoppa
az vm start --resource-group rg-demo --name vm-demo
az vm stop --resource-group rg-demo --name vm-demo
az vm deallocate --resource-group rg-demo --name vm-demo  # Sparar pengar!

# Radera
az vm delete --resource-group rg-demo --name vm-demo --yes

# ═══════════════════════════════════════════════════════════════
# STORAGE
# ═══════════════════════════════════════════════════════════════

# Skapa storage account
az storage account create \\
    --name stdemo12345 \\
    --resource-group rg-demo \\
    --location northeurope \\
    --sku Standard_LRS

# Skapa container
az storage container create \\
    --name mycontainer \\
    --account-name stdemo12345

# Ladda upp fil
az storage blob upload \\
    --account-name stdemo12345 \\
    --container-name mycontainer \\
    --name myfile.txt \\
    --file ./local-file.txt
```

---

## 💻 Output Formats

```bash
# Table (human-readable)
az vm list --output table

# JSON (default, for parsing)
az vm list --output json

# YAML
az vm list --output yaml

# TSV (för scripting)
az vm list --query "[].name" --output tsv

# JMESPath queries
az vm show -g rg-demo -n vm-demo --query "{Name:name, OS:storageProfile.osDisk.osType}"

# Spara till variabel
VM_IP=$(az vm show -g rg-demo -n vm-demo --query publicIps -o tsv)
echo $VM_IP
```

---

## 💻 Cloud Shell

```bash
# Öppna i browser: shell.azure.com
# Eller via portal: Klicka på >_ ikonen

# Cloud Shell har:
# ✅ az (Azure CLI)
# ✅ kubectl
# ✅ terraform
# ✅ ansible
# ✅ git
# ✅ Persistent home directory (Azure Files)

# Ladda upp filer till Cloud Shell:
# Klicka på Upload/Download ikonen
```

---

## 💻 Hjälpsystem

```bash
# Generell hjälp
az --help

# Hjälp för specifik tjänst
az vm --help
az vm create --help

# Interaktiv läge (tab completion!)
az interactive

# Find command
az find "create vm"
```

---

## ⚠️ Vanliga Problem

### Problem 1: Fel subscription

```bash
# ❌ Skapar resurs i fel subscription
az vm create --resource-group rg-demo --name vm-demo ...

# ✅ Kontrollera först
az account show --query name
az account set --subscription "Correct Subscription"
```

### Problem 2: Glömd deallocate

```bash
# ❌ Stoppar VM men betalar fortfarande
az vm stop --resource-group rg-demo --name vm-demo

# ✅ Deallocate för att sluta betala
az vm deallocate --resource-group rg-demo --name vm-demo
```

---

## ✅ Sammanfattning

- **Portal** för utforskning, **CLI** för automation
- **az login** för att börja
- **JMESPath queries** för att extrahera data
- **Cloud Shell** när du inte har CLI lokalt
- **Deallocate** VMs för att spara pengar
""",
}


# ============================================================================
# NODE 4: SUBSCRIPTIONS & COST MANAGEMENT
# ============================================================================

AZURE_NODE_4_SUBSCRIPTIONS = {
    "node_id": 4,
    "title": "Subscriptions & Cost Management",
    "slug": "azure-subscriptions-cost",
    "description": "Hantera Azure-subscriptions och kontrollera kostnader",
    "difficulty": "beginner",
    "estimated_minutes": 50,
    "xp_reward": 90,
    "topics_covered": [
        "subscriptions", "billing", "cost management", "budgets",
        "cost analysis", "reserved instances", "azure advisor"
    ],
    "content": """
# Subscriptions & Cost Management

> *"The cloud is pay-as-you-go, not pay-and-forget."*

---

## 🎯 Why This Matters

Molnkostnader kan snabbt skena:
- **Oväntade räkningar** - resurser man glömt
- **Budget-överskriden** - saknar alerts
- **Fel storlekar** - over-provisioned VMs
- **Reservationer** - kan spara 40-70%

---

## 🧠 Subscription Strategy

```
┌─────────────────────────────────────────────────────────────────┐
│                 SUBSCRIPTION STRATEGIES                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  STRATEGY 1: Per Environment                                    │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  subscription-dev     subscription-test    subscription-prod │    │
│  │  ├── rg-app-dev      ├── rg-app-test     ├── rg-app-prod    │    │
│  │  └── rg-db-dev       └── rg-db-test      └── rg-db-prod     │    │
│  └─────────────────────────────────────────────────────────┘    │
│  ✅ Tydlig separation                                            │
│  ✅ Enkel kostnadsspårning per miljö                             │
│  ✅ Olika budgetar/policies per miljö                            │
│                                                                  │
│  STRATEGY 2: Per Department                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  subscription-it      subscription-marketing  subscription-hr │    │
│  │  ├── rg-dev          ├── rg-website         ├── rg-hr-sys   │    │
│  │  └── rg-prod         └── rg-campaigns       └── rg-payroll  │    │
│  └─────────────────────────────────────────────────────────┘    │
│  ✅ Tydlig kostnad per avdelning                                 │
│  ✅ Avdelningar kan ha egna budgetar                             │
│                                                                  │
│  STRATEGY 3: Hybrid (Recommended)                                │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Management Group: Company                               │    │
│  │  ├── MG: Production                                      │    │
│  │  │   ├── subscription-prod-eu                            │    │
│  │  │   └── subscription-prod-us                            │    │
│  │  └── MG: Non-Production                                  │    │
│  │      ├── subscription-dev                                │    │
│  │      └── subscription-test                               │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Subscription Management

```bash
# Lista alla subscriptions
az account list --output table

# Visa aktuell subscription
az account show

# Byt subscription
az account set --subscription "Subscription Name"
# eller med ID
az account set --subscription "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

# Skapa alias för snabbt byte (i .bashrc/.zshrc)
alias az-dev='az account set --subscription "Dev Subscription"'
alias az-prod='az account set --subscription "Prod Subscription"'

# Verifiera innan kritiska operationer
az account show --query "{Name:name, Id:id}" --output table
```

---

## 💻 Cost Management CLI

```bash
# Visa kostnad för aktuell månad
az consumption usage list \\
    --start-date 2024-12-01 \\
    --end-date 2024-12-31 \\
    --output table

# Gruppera kostnad per resource group
az consumption usage list \\
    --query "[].{ResourceGroup:instanceName, Cost:pretaxCost}" \\
    --output table

# Visa budgets
az consumption budget list --output table

# Skapa budget med alert
az consumption budget create \\
    --budget-name "Monthly-Budget" \\
    --amount 1000 \\
    --time-grain Monthly \\
    --category Cost \\
    --notifications "80:admin@company.com,90:admin@company.com,100:admin@company.com"
```

---

## 💻 Kostnadskontroll i Portal

```
┌─────────────────────────────────────────────────────────────────┐
│                    COST MANAGEMENT PORTAL                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Navigation: Cost Management + Billing                          │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  COST ANALYSIS                                           │    │
│  │  • Filtrera per tidperiod                                │    │
│  │  • Gruppera per resource group, tag, service             │    │
│  │  • Exportera till CSV                                    │    │
│  │  • Jämför med föregående period                          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  BUDGETS                                                 │    │
│  │  • Sätt månadsbudget                                     │    │
│  │  • Email-alerts vid 50%, 75%, 90%, 100%                  │    │
│  │  • Action Groups för automatisering                      │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  ADVISOR RECOMMENDATIONS                                 │    │
│  │  • Right-size VMs (mindre = billigare)                   │    │
│  │  • Reserved Instance recommendations                     │    │
│  │  • Oanvända resurser                                     │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Cost-Saving Strategies

### 1. Reserved Instances (RIs)

```bash
# Spara upp till 72% på VMs med 1-3 års åtagande

# Exempel: Standard_D4s_v3 VM
# Pay-as-you-go: ~$140/month
# 1-year RI:     ~$85/month (40% rabatt)
# 3-year RI:     ~$55/month (60% rabatt)

# Köp RI i Portal:
# Reservations → Add → Virtual Machine → Välj region, storlek, term
```

### 2. Azure Hybrid Benefit

```bash
# Använd befintliga Windows/SQL-licenser i Azure
# Spara upp till 40% på Windows VMs
# Spara upp till 55% på SQL Server

# Aktivera vid VM-skapande:
az vm create \\
    --resource-group rg-demo \\
    --name vm-demo \\
    --image Win2019Datacenter \\
    --license-type Windows_Server  # Hybrid Benefit
```

### 3. Auto-shutdown

```bash
# Stäng av dev-VMs på natten
az vm auto-shutdown \\
    --resource-group rg-dev \\
    --name vm-dev \\
    --time 1800 \\
    --timezone "W. Europe Standard Time"
```

### 4. Spot VMs

```bash
# Upp till 90% rabatt för interruptible workloads
az vm create \\
    --resource-group rg-demo \\
    --name vm-spot \\
    --image Ubuntu2204 \\
    --priority Spot \\
    --eviction-policy Deallocate \\
    --max-price 0.05  # Max pris per timme
```

---

## 💻 Budget Alert Setup

```bash
# Skapa action group för notifieringar
az monitor action-group create \\
    --name "CostAlerts" \\
    --resource-group rg-monitoring \\
    --short-name "CostAlerts" \\
    --email-receiver name="Admin" email-address="admin@company.com"

# Skapa budget med action group
# (Enklast via Portal för full funktionalitet)
```

---

## ⚠️ Vanliga Kostnadsmisstag

### Misstag 1: Oanvända resurser

```bash
# Hitta oanvända diskar
az disk list --query "[?diskState=='Unattached'].{Name:name,Size:diskSizeGb}" --output table

# Hitta stoppade VMs som fortfarande kostar
az vm list --query "[?powerState!='VM deallocated'].{Name:name,State:powerState}" --output table
```

### Misstag 2: Over-provisioned VMs

```bash
# Kontrollera CPU-användning
# Portal → VM → Metrics → CPU percentage
# Om < 20% genomsnitt → right-size till mindre VM
```

---

## ✅ Sammanfattning

- **Subscription-design** för kostnadskontroll
- **Budgets + alerts** förhindrar överraskningar
- **Reserved Instances** sparar 40-72%
- **Auto-shutdown** för dev-miljöer
- **Kontrollera oanvända resurser** regelbundet
""",
}


# Export all nodes from Block 1
BLOCK_1_NODES = [
    AZURE_NODE_1_INTRO,
    AZURE_NODE_2_RESOURCES,
    AZURE_NODE_3_PORTAL_CLI,
    AZURE_NODE_4_SUBSCRIPTIONS,
]
