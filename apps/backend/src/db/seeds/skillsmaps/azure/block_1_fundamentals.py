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
    "description": "Forsta Microsoft Azure och cloud computing koncept",
    "difficulty": "beginner",
    "estimated_minutes": 45,
    "xp_reward": 80,
    "topics_covered": [
        "azure overview", "cloud computing", "regions", "availability zones",
        "iaas", "paas", "saas", "azure services"
    ],
    "content": """# Introduction to Azure

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Azure ar viktigt |
|----------|------------------------|
| **Multi-cloud strategi** | Azure ar #2 globalt - maste kunna |
| **Enterprise-integration** | Active Directory, Office 365, Teams |
| **Hybrid-scenarios** | Azure Arc for on-prem + cloud |
| **CI/CD pipelines** | Azure DevOps ar industristandard |
| **Certifieringar** | AZ-900, AZ-104, AZ-400 efterfragas |

Microsoft Azure ar varldens nast storsta molnplattform:

- **200+ tjanster** - compute, storage, AI, IoT och mer
- **60+ regioner** - global tackning
- **Enterprise-fokus** - stark integration med Microsoft-produkter

------------------------------------------------------------

## Cloud Computing Models

```
+-----------------------------------------------------------------+
|              CLOUD COMPUTING MODELS                              |
+-----------------------------------------------------------------+
|                                                                  |
|   ON-PREMISES        IaaS           PaaS           SaaS         |
|  +-----------+   +-----------+  +-----------+  +-----------+   |
|  |Application|   |Application|  |Application|  |Application|   |
|  +-----------+   +-----------+  +-----------+  +-----------+   |
|  |  Runtime  |   |  Runtime  |  |  Runtime  |  |  Runtime  |   |
|  +-----------+   +-----------+  +-----------+  +-----------+   |
|  |    OS     |   |    OS     |  |    OS     |  |    OS     |   |
|  +-----------+   +-----------+  +-----------+  +-----------+   |
|  |   VMs     |   |   VMs     |  |   VMs     |  |   VMs     |   |
|  +-----------+   +-----------+  +-----------+  +-----------+   |
|  |  Storage  |   |  Storage  |  |  Storage  |  |  Storage  |   |
|  +-----------+   +-----------+  +-----------+  +-----------+   |
|  | Network   |   | Network   |  | Network   |  | Network   |   |
|  +-----------+   +-----------+  +-----------+  +-----------+   |
|       |               |              |              |            |
|    DU HANTERAR    DU/AZURE       AZURE          AZURE           |
|     ALLT          DELAR         HANTERAR       HANTERAR         |
|                                                                  |
|  Exempel:        Exempel:       Exempel:       Exempel:         |
|  Ditt            Azure VMs      App Service    Microsoft 365    |
|  serverrum       Azure Storage  Functions      Dynamics 365     |
|                                 AKS            Power BI         |
+-----------------------------------------------------------------+
```

### Ansvarsfordelning

| Modell | Du hanterar | Azure hanterar |
|--------|-------------|----------------|
| **On-Prem** | Allt | Inget |
| **IaaS** | OS, Runtime, App | Natverk, Storage, VMs |
| **PaaS** | App, Data | Allt annat |
| **SaaS** | Inget | Allt |

------------------------------------------------------------

## Azure Global Infrastructure

```
+-----------------------------------------------------------------+
|                 AZURE GLOBAL INFRASTRUCTURE                      |
+-----------------------------------------------------------------+
|                                                                  |
|  GEOGRAPHY (Geopolitisk grans)                                  |
|  +-- REGION (Datacenter-kluster)                                |
|      +-- AVAILABILITY ZONE (Isolerat datacenter)                |
|                                                                  |
|  Exempel: Europe Geography                                       |
|  +-----------------------------------------------------------+  |
|  |  North Europe Region (Ireland)                             |  |
|  |  +---------+  +---------+  +---------+                   |  |
|  |  |  AZ 1   |  |  AZ 2   |  |  AZ 3   |                   |  |
|  |  | (DC 1)  |  | (DC 2)  |  | (DC 3)  |                   |  |
|  |  +---------+  +---------+  +---------+                   |  |
|  |       +----------+----------+                             |  |
|  |           Low-latency network                             |  |
|  +-----------------------------------------------------------+  |
|                                                                  |
|  Populara regioner:                                             |
|  • West Europe (Netherlands) - Lagst latens fran Sverige        |
|  • North Europe (Ireland) - Billigare                           |
|  • Sweden Central (Gavle) - Data residency                      |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Core Azure Services

| Kategori | Tjanster | Anvandning |
|----------|----------|------------|
| **Compute** | VMs, App Service, Functions, AKS | Kor applikationer |
| **Storage** | Blob, Files, Queues, Tables | Lagra data |
| **Database** | SQL Database, Cosmos DB, PostgreSQL | Relationell/NoSQL |
| **Networking** | VNet, Load Balancer, VPN Gateway | Natverksinfrastruktur |
| **Identity** | Azure AD, RBAC | Autentisering/auktorisering |
| **DevOps** | Azure DevOps, Container Registry | CI/CD |
| **AI/ML** | Cognitive Services, Azure ML | Machine Learning |
| **Monitoring** | Azure Monitor, Log Analytics | Overvakning |

------------------------------------------------------------

## Azure vs AWS vs GCP

| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| **Styrka** | Enterprise, MS-integration | Market leader | Data/ML, K8s |
| **IaaS** | Virtual Machines | EC2 | Compute Engine |
| **PaaS** | App Service | Elastic Beanstalk | App Engine |
| **Serverless** | Functions | Lambda | Cloud Functions |
| **Containers** | AKS | EKS | GKE |
| **Storage** | Blob Storage | S3 | Cloud Storage |
| **Database** | Azure SQL, Cosmos DB | RDS, DynamoDB | Cloud SQL |

------------------------------------------------------------

## Skapa Azure-konto

```bash
# 1. Ga till https://azure.microsoft.com/free
# 2. Registrera med Microsoft-konto
# 3. Du far $200 kredit i 30 dagar + 12 manader gratistjanster

# Free tier inkluderar:
# - 750h B1s Linux VM (12 man)
# - 750h B1s Windows VM (12 man)
# - 5GB Blob Storage (12 man)
# - Azure App Service (alltid gratis)
# - Azure Functions (1M requests/man)
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Glomda resurser | VM kostar aven stoppad | Deallocate eller radera |
| Fel region | Hogre kostnad | Jamfor priser i calculator |
| Ingen budget-alert | Ovantad rakring | Satt upp i Cost Management |
| Over-provisioned | For stor VM | Right-size enligt Advisor |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Azure** | Enterprise-fokuserad molnplattform, #2 globalt |
| **IaaS/PaaS/SaaS** | Olika ansvarsnivder - valj ratt modell |
| **Regioner & Zoner** | Valj region nara anvandare, zoner for HA |
| **Free tier** | $200 kredit + 12 man gratis for att lara sig |

**Kom ihag:**
- Azure ar starkt integrerat med **Microsoft-produkter** (AD, Office, Teams)
- **Regioner** paverkar bade **latens och kostnad**
- Satt **alltid budget-alerts** innan du borjar experimentera
- **AZ-900** ar en bra start-certifiering
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
    "content": """# Resource Groups & Management

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Resource Management ar viktigt |
|----------|--------------------------------------|
| **Organisation** | Gruppera relaterade resurser logiskt |
| **Access Control** | Satt rattigheter pa grupp-niva med RBAC |
| **Cost Tracking** | Folj kostnader per projekt/team/miljo |
| **Lifecycle** | Radera hela miljoer med ett kommando |
| **Automation** | Terraform/ARM arbetar med resource groups |

Resource management ar grunden for all Azure-hantering.

------------------------------------------------------------

## Azure Resource Hierarchy

```
+-----------------------------------------------------------------+
|                 AZURE RESOURCE HIERARCHY                         |
+-----------------------------------------------------------------+
|                                                                  |
|  +---------------------------------------------------------+    |
|  |              Azure Active Directory (Tenant)             |    |
|  |  Identiteter, anvandare, grupper, service principals    |    |
|  +---------------------------------------------------------+    |
|                           |                                      |
|  +---------------------------------------------------------+    |
|  |                Management Groups (Valfritt)              |    |
|  |  Gruppera subscriptions for policy och RBAC              |    |
|  +---------------------------------------------------------+    |
|                           |                                      |
|  +---------------------------------------------------------+    |
|  |                     Subscriptions                        |    |
|  |  Faktureringsenheter, en per miljo eller avdelning       |    |
|  |  +--------------+ +--------------+ +--------------+     |    |
|  |  | Dev Subscr.  | | Test Subscr. | | Prod Subscr. |     |    |
|  |  +--------------+ +--------------+ +--------------+     |    |
|  +---------------------------------------------------------+    |
|                           |                                      |
|  +---------------------------------------------------------+    |
|  |                   Resource Groups                        |    |
|  |  Logiska containrar for relaterade resurser              |    |
|  |  +------------+ +------------+ +------------+           |    |
|  |  | rg-web-dev | |rg-api-dev  | | rg-db-dev  |           |    |
|  |  +------------+ +------------+ +------------+           |    |
|  +---------------------------------------------------------+    |
|                           |                                      |
|  +---------------------------------------------------------+    |
|  |                      Resources                           |    |
|  |  VMs, Storage, Databases, App Services, etc.             |    |
|  +---------------------------------------------------------+    |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Resource Group Kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `az group create` | Skapa resource group |
| `az group list` | Lista alla resource groups |
| `az resource list -g <name>` | Lista resurser i grupp |
| `az group delete` | Radera grupp och ALLA resurser |

```bash
# Skapa resource group med tags
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

------------------------------------------------------------

## Naming Conventions

```
+-----------------------------------------------------------------+
|             AZURE NAMING CONVENTION (Microsoft CAF)              |
+-----------------------------------------------------------------+
|                                                                  |
|  Format: {resource-type}-{workload}-{environment}-{region}-{#}  |
|                                                                  |
|  Exempel:                                                        |
|  +---------------------------------------------------------+    |
|  | Resource Group:    rg-webshop-prod-ne-001               |    |
|  | Virtual Machine:   vm-webshop-prod-ne-001               |    |
|  | Storage Account:   stwebshopprodne001 (inga bindestreck!)|    |
|  | App Service:       app-webshop-prod-ne-001              |    |
|  | SQL Database:      sql-webshop-prod-ne-001              |    |
|  | Key Vault:         kv-webshop-prod-ne-001               |    |
|  | Virtual Network:   vnet-webshop-prod-ne-001             |    |
|  +---------------------------------------------------------+    |
|                                                                  |
|  Vanliga prefix:                                                 |
|  rg   = Resource Group     vm   = Virtual Machine               |
|  st   = Storage Account    sql  = SQL Database                  |
|  app  = App Service        func = Function App                  |
|  kv   = Key Vault          vnet = Virtual Network               |
|  nsg  = Network Security   pip  = Public IP                     |
|                                                                  |
|  Environment:                                                    |
|  dev = Development         test = Testing                       |
|  stg = Staging             prod = Production                    |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Tags

| Kommando | Beskrivning |
|----------|-------------|
| `--tags Key=Value` | Lagg till vid skapande |
| `az resource tag` | Uppdatera tags |
| `az resource list --tag` | Filtrera pa tag |

```bash
# Lagg till tags vid skapande
az group create \\
    --name rg-myproject-prod \\
    --location northeurope \\
    --tags \\
        Environment=Production \\
        Project=MyProject \\
        CostCenter=CC-123 \\
        Owner=team@company.com \\
        CreatedBy=terraform

# Filtrera resurser pa tag
az resource list --tag Environment=Production --output table

# Visa kostnader per tag i Cost Management
# Azure Portal -> Cost Management -> Cost Analysis -> Group by: Tag
```

### Rekommenderade Tags

| Tag | Syfte | Exempel |
|-----|-------|---------|
| **Environment** | Miljo | Production, Development |
| **Project** | Projekt | WebShop, API |
| **CostCenter** | Fakturering | CC-123 |
| **Owner** | Ansvarig | team@company.com |
| **CreatedBy** | Skapad av | terraform, manual |

------------------------------------------------------------

## Resource Locks

```bash
# Skapa lock som forhindrar radering
az lock create \\
    --name DoNotDelete \\
    --resource-group rg-production \\
    --lock-type CanNotDelete \\
    --notes "Production environment - do not delete"

# Skapa ReadOnly lock (forhindrar andringar)
az lock create \\
    --name ReadOnly \\
    --resource-group rg-production \\
    --lock-type ReadOnly

# Lista locks
az lock list --resource-group rg-production --output table

# Ta bort lock (kravs for att kunna radera)
az lock delete --name DoNotDelete --resource-group rg-production
```

### Lock-typer

| Lock-typ | Forhindrar | Anvandning |
|----------|------------|------------|
| **CanNotDelete** | Radering | Skydda produktion |
| **ReadOnly** | Alla andringar | Kritiska resurser |

------------------------------------------------------------

## Best Practices for Resource Groups

```
+-----------------------------------------------------------------+
|                 RESOURCE GROUP DESIGN                            |
+-----------------------------------------------------------------+
|                                                                  |
|  RATT: Gruppera efter livscykel                                 |
|  -----------------------------------------------------          |
|  rg-webshop-frontend-prod    # Frontend-resurser                |
|  rg-webshop-backend-prod     # Backend-resurser                 |
|  rg-webshop-shared-prod      # Delade resurser                  |
|                                                                  |
|  RATT: Gruppera efter miljo                                     |
|  -----------------------------------------------------          |
|  rg-myapp-dev                                                   |
|  rg-myapp-test                                                  |
|  rg-myapp-prod                                                  |
|                                                                  |
|  FEL: Blanda miljoer                                            |
|  -----------------------------------------------------          |
|  rg-all-resources (blandar dev och prod!)                       |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Raderar produktion | Inget lock | Skapa CanNotDelete lock |
| Hittar inte resurs | Fel subscription | `az account set` |
| Kan inte radera | Lock finns | Ta bort lock forst |
| Kostnad oorganiserad | Inga tags | Implementera tagging policy |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Resource Groups** | Logiska containrar - gruppera efter livscykel |
| **Naming Convention** | Konsekvent namngivning sparar tid |
| **Tags** | Organisation och kostnadssparning |
| **Locks** | Skydda kritiska miljoer fran misstag |

**Kom ihag:**
- En resurs kan **bara finnas i en** resource group
- Resource groups har **en region** men resurser kan vara i olika
- **Radering av grupp = radering av ALLT** i gruppen
- Anvand **locks pa produktion** - alltid
""",
}


# ============================================================================
# NODE 3: AZURE PORTAL & CLI
# ============================================================================

AZURE_NODE_3_PORTAL_CLI = {
    "node_id": 3,
    "title": "Azure Portal & CLI",
    "slug": "azure-portal-cli",
    "description": "Navigera Azure Portal och anvanda Azure CLI",
    "difficulty": "beginner",
    "estimated_minutes": 55,
    "xp_reward": 100,
    "topics_covered": [
        "azure portal", "azure cli", "cloud shell", "az commands",
        "powershell", "authentication", "scripting"
    ],
    "content": """# Azure Portal & CLI

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor CLI ar viktigt |
|----------|----------------------|
| **Automation** | Skripta repetitiva uppgifter |
| **CI/CD** | Deploya fran pipelines |
| **Reproducerbarhet** | Samma kommando = samma resultat |
| **Hastighet** | CLI ar snabbare an portal for erfarna |
| **Dokumentation** | Kommandon ar sjalvdokumenterande |

Flera satt att hantera Azure - valj ratt verktyg for uppgiften.

------------------------------------------------------------

## Azure Management Tools

```
+-----------------------------------------------------------------+
|                 AZURE MANAGEMENT TOOLS                           |
+-----------------------------------------------------------------+
|                                                                  |
|  +----------------------------------------------------------+   |
|  |                    AZURE PORTAL                           |   |
|  |  https://portal.azure.com                                 |   |
|  |  + Visuellt interface                                     |   |
|  |  + Bast for utforskning                                   |   |
|  |  + Dashboards & monitoring                                |   |
|  |  - Svart att automatisera                                 |   |
|  +----------------------------------------------------------+   |
|                           |                                      |
|  +----------------------------------------------------------+   |
|  |                      AZURE CLI                            |   |
|  |  az <service> <command>                                   |   |
|  |  + Cross-platform (Windows, Mac, Linux)                   |   |
|  |  + Scriptbar (bash, zsh)                                  |   |
|  |  + JSON output for parsing                                |   |
|  |  + Tab completion                                         |   |
|  +----------------------------------------------------------+   |
|                           |                                      |
|  +----------------------------------------------------------+   |
|  |                   AZURE POWERSHELL                        |   |
|  |  Connect-AzAccount / Get-AzResource                       |   |
|  |  + Nativa PowerShell cmdlets                              |   |
|  |  + Bra for Windows-admins                                 |   |
|  |  + Objekt-orienterad output                               |   |
|  +----------------------------------------------------------+   |
|                           |                                      |
|  +----------------------------------------------------------+   |
|  |                    CLOUD SHELL                            |   |
|  |  shell.azure.com                                          |   |
|  |  + Browserbased CLI                                       |   |
|  |  + Ingen installation                                     |   |
|  |  + For-autentiserad                                       |   |
|  |  + Har az, kubectl, terraform, etc.                       |   |
|  +----------------------------------------------------------+   |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Azure CLI Installation

| Plattform | Kommando |
|-----------|----------|
| **macOS** | `brew install azure-cli` |
| **Ubuntu/Debian** | `curl -sL https://aka.ms/InstallAzureCLIDeb \\| sudo bash` |
| **Windows** | `winget install Microsoft.AzureCLI` |
| **Docker** | `docker run -it mcr.microsoft.com/azure-cli` |

```bash
# macOS
brew install azure-cli

# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Verifiera
az --version
```

------------------------------------------------------------

## Azure CLI Basics

| Kommando | Beskrivning |
|----------|-------------|
| `az login` | Logga in (oppnar webblasare) |
| `az account show` | Visa aktuellt konto |
| `az account list` | Lista subscriptions |
| `az account set --subscription` | Byt subscription |

```bash
# Logga in
az login
# Oppnar webblasare for autentisering

# Logga in med service principal (CI/CD)
az login --service-principal \\
    --username $AZURE_CLIENT_ID \\
    --password $AZURE_CLIENT_SECRET \\
    --tenant $AZURE_TENANT_ID

# Visa aktuell subscription
az account show --query name -o tsv

# Lista subscriptions
az account list --output table

# Byt subscription
az account set --subscription "My Subscription Name"
```

------------------------------------------------------------

## Vanliga az-kommandon

### Resource Groups

| Kommando | Beskrivning |
|----------|-------------|
| `az group create` | Skapa resource group |
| `az group list` | Lista grupper |
| `az group delete` | Radera grupp |

```bash
# Skapa
az group create --name rg-demo --location northeurope

# Lista
az group list --output table

# Radera
az group delete --name rg-demo --yes
```

### Virtual Machines

| Kommando | Beskrivning |
|----------|-------------|
| `az vm create` | Skapa VM |
| `az vm list` | Lista VMs |
| `az vm start/stop` | Starta/stoppa |
| `az vm deallocate` | Deallocate (sparar pengar!) |

```bash
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
```

### Storage

```bash
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

------------------------------------------------------------

## Output Formats

| Format | Flagga | Anvandning |
|--------|--------|------------|
| **Table** | `--output table` | Lasbar for manniskor |
| **JSON** | `--output json` | Parsing, default |
| **TSV** | `--output tsv` | Scripting |
| **YAML** | `--output yaml` | Konfiguration |

```bash
# Table (human-readable)
az vm list --output table

# JSON (default, for parsing)
az vm list --output json

# TSV (for scripting)
az vm list --query "[].name" --output tsv

# JMESPath queries
az vm show -g rg-demo -n vm-demo \\
    --query "{Name:name, OS:storageProfile.osDisk.osType}"

# Spara till variabel
VM_IP=$(az vm show -g rg-demo -n vm-demo --query publicIps -o tsv)
echo $VM_IP
```

------------------------------------------------------------

## Cloud Shell

```
+-----------------------------------------------------------------+
|                       CLOUD SHELL                                |
+-----------------------------------------------------------------+
|                                                                  |
|  URL: shell.azure.com                                           |
|  Eller: Portal -> klicka pa >_ ikonen                           |
|                                                                  |
|  Forinstallerat:                                                |
|  +---------------------------------------------------------+    |
|  |  az          - Azure CLI                                |    |
|  |  kubectl     - Kubernetes CLI                           |    |
|  |  terraform   - Infrastructure as Code                   |    |
|  |  ansible     - Configuration Management                 |    |
|  |  git         - Version Control                          |    |
|  |  code        - VS Code (editor)                         |    |
|  +---------------------------------------------------------+    |
|                                                                  |
|  + Persistent home directory (Azure Files)                      |
|  + For-autentiserad med ditt konto                              |
|  + 5GB lagring inkluderat                                       |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Hjalpsystem

| Kommando | Beskrivning |
|----------|-------------|
| `az --help` | Generell hjalp |
| `az vm --help` | Hjalp for service |
| `az vm create --help` | Hjalp for kommando |
| `az interactive` | Interaktivt lage |
| `az find "create vm"` | Sok kommando |

```bash
# Generell hjalp
az --help

# Hjalp for specifik tjanst
az vm --help
az vm create --help

# Interaktiv lage (tab completion!)
az interactive

# Hitta kommando
az find "create vm"
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Fel subscription | Standard vald | `az account set --subscription` |
| VM kostar trots stopp | Ej deallocate | `az vm deallocate` |
| Command not found | CLI ej installerad | Installera az CLI |
| Unauthorized | Token expired | `az login` igen |

```bash
# Kontrollera subscription innan kritiska operationer
az account show --query name

# Deallocate for att sluta betala
az vm deallocate --resource-group rg-demo --name vm-demo
```

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Portal** | For utforskning och dashboards |
| **CLI** | For automation och scripting |
| **Cloud Shell** | Nar du inte har CLI lokalt |
| **JMESPath** | Queries for att extrahera data |

**Kom ihag:**
- **Portal for utforskning**, CLI for automation
- `az login` for att borja, `az account set` for att byta subscription
- **Deallocate** VMs for att spara pengar (stop racker inte!)
- Anvand **--output table** for lasbarhet, **tsv** for scripting
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
    "content": """# Subscriptions & Cost Management

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Cost Management ar viktigt |
|----------|----------------------------------|
| **Budget-kontroll** | Forhindra ovantade rakningar |
| **Kostnadsoptimering** | Right-size resurser, spara pengar |
| **Showback/Chargeback** | Visa kostnader per team/projekt |
| **Forecasting** | Planera framtida kostnader |
| **FinOps** | Kombinera Dev + Finance + Ops |

Molnkostnader kan snabbt skena utan kontroll.

------------------------------------------------------------

## Subscription Strategies

```
+-----------------------------------------------------------------+
|                 SUBSCRIPTION STRATEGIES                          |
+-----------------------------------------------------------------+
|                                                                  |
|  STRATEGI 1: Per Miljo                                          |
|  +---------------------------------------------------------+    |
|  |  subscription-dev    subscription-test   subscription-prod   |
|  |  +-- rg-app-dev     +-- rg-app-test     +-- rg-app-prod     |
|  |  +-- rg-db-dev      +-- rg-db-test      +-- rg-db-prod      |
|  +---------------------------------------------------------+    |
|  + Tydlig separation mellan miljoer                             |
|  + Enkel kostnadssparning per miljo                             |
|  + Olika budgetar/policies per miljo                            |
|                                                                  |
|  STRATEGI 2: Per Avdelning                                      |
|  +---------------------------------------------------------+    |
|  |  subscription-it     subscription-marketing  subscription-hr |
|  |  +-- rg-dev         +-- rg-website          +-- rg-hr-sys   |
|  |  +-- rg-prod        +-- rg-campaigns        +-- rg-payroll  |
|  +---------------------------------------------------------+    |
|  + Tydlig kostnad per avdelning                                 |
|  + Avdelningar kan ha egna budgetar                             |
|                                                                  |
|  STRATEGI 3: Hybrid (Rekommenderas)                             |
|  +---------------------------------------------------------+    |
|  |  Management Group: Company                               |    |
|  |  +-- MG: Production                                      |    |
|  |  |   +-- subscription-prod-eu                            |    |
|  |  |   +-- subscription-prod-us                            |    |
|  |  +-- MG: Non-Production                                  |    |
|  |      +-- subscription-dev                                |    |
|  |      +-- subscription-test                               |    |
|  +---------------------------------------------------------+    |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Subscription Management

| Kommando | Beskrivning |
|----------|-------------|
| `az account list` | Lista subscriptions |
| `az account show` | Visa aktuell |
| `az account set` | Byt subscription |

```bash
# Lista alla subscriptions
az account list --output table

# Visa aktuell subscription
az account show

# Byt subscription
az account set --subscription "Subscription Name"
# eller med ID
az account set --subscription "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

# Skapa alias for snabbt byte (i .bashrc/.zshrc)
alias az-dev='az account set --subscription "Dev Subscription"'
alias az-prod='az account set --subscription "Prod Subscription"'

# Verifiera innan kritiska operationer
az account show --query "{Name:name, Id:id}" --output table
```

------------------------------------------------------------

## Cost Management i Portal

```
+-----------------------------------------------------------------+
|                    COST MANAGEMENT PORTAL                        |
+-----------------------------------------------------------------+
|                                                                  |
|  Navigation: Cost Management + Billing                          |
|                                                                  |
|  +---------------------------------------------------------+    |
|  |  COST ANALYSIS                                           |    |
|  |  - Filtrera per tidperiod                                |    |
|  |  - Gruppera per resource group, tag, service             |    |
|  |  - Exportera till CSV                                    |    |
|  |  - Jamfor med foregaende period                          |    |
|  +---------------------------------------------------------+    |
|                                                                  |
|  +---------------------------------------------------------+    |
|  |  BUDGETS                                                 |    |
|  |  - Satt manadsbudget                                     |    |
|  |  - Email-alerts vid 50%, 75%, 90%, 100%                  |    |
|  |  - Action Groups for automatisering                      |    |
|  +---------------------------------------------------------+    |
|                                                                  |
|  +---------------------------------------------------------+    |
|  |  ADVISOR RECOMMENDATIONS                                 |    |
|  |  - Right-size VMs (mindre = billigare)                   |    |
|  |  - Reserved Instance recommendations                     |    |
|  |  - Oanvanda resurser                                     |    |
|  +---------------------------------------------------------+    |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Cost-Saving Strategies

### 1. Reserved Instances (RIs)

| Term | Rabatt | Anvandning |
|------|--------|------------|
| **Pay-as-you-go** | 0% | Test, kortvarig |
| **1-year RI** | ~40% | Stabil workload |
| **3-year RI** | ~60-72% | Produktion |

```bash
# Exempel: Standard_D4s_v3 VM
# Pay-as-you-go: ~$140/month
# 1-year RI:     ~$85/month (40% rabatt)
# 3-year RI:     ~$55/month (60% rabatt)

# Kop RI i Portal:
# Reservations -> Add -> Virtual Machine -> Valj region, storlek, term
```

### 2. Azure Hybrid Benefit

```bash
# Anvand befintliga Windows/SQL-licenser i Azure
# Spara upp till 40% pa Windows VMs
# Spara upp till 55% pa SQL Server

# Aktivera vid VM-skapande:
az vm create \\
    --resource-group rg-demo \\
    --name vm-demo \\
    --image Win2019Datacenter \\
    --license-type Windows_Server  # Hybrid Benefit
```

### 3. Auto-shutdown

```bash
# Stang av dev-VMs pa natten
az vm auto-shutdown \\
    --resource-group rg-dev \\
    --name vm-dev \\
    --time 1800 \\
    --timezone "W. Europe Standard Time"
```

### 4. Spot VMs

```bash
# Upp till 90% rabatt for interruptible workloads
az vm create \\
    --resource-group rg-demo \\
    --name vm-spot \\
    --image Ubuntu2204 \\
    --priority Spot \\
    --eviction-policy Deallocate \\
    --max-price 0.05  # Max pris per timme
```

------------------------------------------------------------

## Hitta oanvanda resurser

```bash
# Hitta oanvanda diskar
az disk list \\
    --query "[?diskState=='Unattached'].{Name:name,Size:diskSizeGb}" \\
    --output table

# Hitta stoppade VMs som fortfarande kostar
az vm list \\
    --query "[?powerState!='VM deallocated'].{Name:name,State:powerState}" \\
    --output table

# Hitta gamla snapshots
az snapshot list \\
    --query "[?timeCreated<'2024-01-01'].{Name:name,Created:timeCreated}" \\
    --output table
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Ovantad hog rakning | Glomda resurser | Satt budget alerts |
| VM kostar trots stangd | Stop != Deallocate | Anvand deallocate |
| Storage kostar mycket | Gamla snapshots | Rensa regelbundet |
| Over-provisioned | For stor VM | Folj Advisor recommendations |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Subscription-design** | Separera miljoer for kostnadskontroll |
| **Budgets + alerts** | Forhindrar overraskningar |
| **Reserved Instances** | Spara 40-72% pa stabila workloads |
| **Auto-shutdown** | Stang av dev-miljoer pa natten |

**Kom ihag:**
- Satt **alltid budget-alerts** innan du borjar
- **Deallocate** VMs istallet for bara stop
- **Reserved Instances** for produktion (40-72% rabatt)
- **Kontrollera Advisor** regelbundet for recommendations
""",
}


# Export all nodes from Block 1
BLOCK_1_NODES = [
    AZURE_NODE_1_INTRO,
    AZURE_NODE_2_RESOURCES,
    AZURE_NODE_3_PORTAL_CLI,
    AZURE_NODE_4_SUBSCRIPTIONS,
]
