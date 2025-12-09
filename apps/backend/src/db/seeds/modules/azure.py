"""
Azure Cloud Mastery Module
==========================

20 noder med svensk pedagogisk stil.
Komplett Azure-kunskap - från grunderna till enterprise.

Track: cloud
Difficulty: intermediate
Estimated Hours: 25
"""

MODULE = {
    "name": "Azure Cloud Mastery",
    "slug": "azure-mastery",
    "description": "Komplett Azure-kunskap - från cloud fundamentals till enterprise-arkitektur med naturlig svensk pedagogik",
    "track_slug": "cloud",
    "order_index": 24,
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "prerequisites": ["linux-mastery"],
    "icon": "☁️",
    "color": "#0078D4",
    "tasks": [
        # =====================================================================
        # NODE 1: Azure Fundamentals & Cloud Models
        # =====================================================================
        {
            "title": "Azure Fundamentals & Cloud Models",
            "slug": "azure-fundamentals-cloud-models",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Azure Fundamentals & Cloud Models

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Azure ar viktigt |
|----------|-------------------------|
| **Hybrid Cloud** | Koppla ihop on-prem med molnet |
| **Enterprise** | Active Directory-integration |
| **Microsoft-stack** | .NET, SQL Server, Windows |
| **Compliance** | GDPR-regioner i Sverige |
| **Skalning** | Global infrastruktur, 60+ regioner |

Som DevOps-ingenjor maste du forsta:

- **Cloud-modeller (IaaS/PaaS/SaaS)** sa du kan valja ratt tjanst
- **Azures globala infrastruktur** sa du kan optimera for latens och compliance
- **Skillnaden mellan Azure och andra moln** sa du kan argumentera for ratt plattform

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad ar Azure?

Microsoft Azure ar varldens nast storsta molnplattform (efter AWS). Det ar sarskilt starkt for:

- **Enterprise** - Tight integration med Active Directory
- **Hybrid Cloud** - Azure Arc, Azure Stack
- **Microsoft-produkter** - Office 365, Dynamics, Power Platform
- **Europa/Sverige** - Datacenter i Gavle (Sweden Central)

```
┌─────────────────────────────────────────────────────────────┐
│                    AZURE EKOSYSTEMET                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────────────────────────────────────────────┐  │
│   │                 AZURE PORTAL                         │  │
│   │              (portal.azure.com)                      │  │
│   └─────────────────────────────────────────────────────┘  │
│                          │                                  │
│          ┌───────────────┼───────────────┐                 │
│          ▼               ▼               ▼                 │
│   ┌───────────┐   ┌───────────┐   ┌───────────┐           │
│   │  Compute  │   │  Storage  │   │ Networking│           │
│   │ VMs, AKS  │   │ Blob,Files│   │ VNet, LB  │           │
│   └───────────┘   └───────────┘   └───────────┘           │
│          │               │               │                 │
│          └───────────────┼───────────────┘                 │
│                          ▼                                  │
│   ┌─────────────────────────────────────────────────────┐  │
│   │              AZURE RESOURCE MANAGER                  │  │
│   │           (Enhetligt API for alla resurser)          │  │
│   └─────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cloud Computing Models

```
┌─────────────────────────────────────────────────────────────┐
│              ANSVAR PER MODELL                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ON-PREM      IaaS        PaaS        SaaS                 │
│  ┌──────┐   ┌──────┐    ┌──────┐    ┌──────┐              │
│  │ App  │   │ App  │    │ App  │    │ App  │ ← Azure      │
│  │ Data │   │ Data │    │ Data │    │ Data │ ← Azure      │
│  │ RT   │   │ RT   │    │ RT   │ ←  │ RT   │ ← Azure      │
│  │ OS   │   │ OS   │ ←  │ OS   │ ←  │ OS   │ ← Azure      │
│  │ VM   │   │ VM   │ ←  │ VM   │ ←  │ VM   │ ← Azure      │
│  │ HW   │   │ HW   │ ←  │ HW   │ ←  │ HW   │ ← Azure      │
│  └──────┘   └──────┘    └──────┘    └──────┘              │
│                                                             │
│  Pil (←) = Azure ansvarar                                  │
└─────────────────────────────────────────────────────────────┘
```

### Jamforelsetabell

| Modell | Du ansvarar for | Azure ansvarar for | Exempel |
|--------|-----------------|-------------------|---------|
| **IaaS** | App, Data, Runtime, OS | VM, Natverk, Lagring | Azure VMs |
| **PaaS** | App, Data | Allt annat | App Service, Azure SQL |
| **SaaS** | Konfiguration | Hela stacken | Microsoft 365, Dynamics |

**Tumregel:** Borja med PaaS om mojligt - mindre underhall, snabbare deployment.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azures Globala Infrastruktur

```
┌─────────────────────────────────────────────────────────────┐
│                   AZURE HIERARKI                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │               GEOGRAPHY (Geografi)                   │   │
│  │            Europa, USA, Asien, etc.                  │   │
│  │         Data stannar inom geografin                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                          │                                  │
│           ┌──────────────┼──────────────┐                  │
│           ▼              ▼              ▼                  │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │   REGION    │ │   REGION    │ │   REGION    │          │
│  │   Sweden    │ │   North     │ │   West      │          │
│  │   Central   │ │   Europe    │ │   Europe    │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
│         │                                                   │
│    ┌────┼────┐                                             │
│    ▼    ▼    ▼                                             │
│  ┌───┐┌───┐┌───┐                                           │
│  │AZ1││AZ2││AZ3│  AVAILABILITY ZONES                       │
│  └───┘└───┘└───┘  (Separata datacenter)                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Regioner for Sverige

| Region | Plats | Latens fran SE | Anvandningsfall |
|--------|-------|----------------|-----------------|
| **Sweden Central** | Gavle | ~5ms | GDPR-kanslig data |
| **Sweden South** | Staffanstorp | ~10ms | DR-site |
| **North Europe** | Irland | ~30ms | Billigare, stort utbud |
| **West Europe** | Nederlanderna | ~25ms | Legacy-appar |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Azure CLI

### Installation och Login

| Kommando | Beskrivning |
|----------|-------------|
| `az login` | Logga in (oppnar webblasare) |
| `az account list` | Lista subscriptions |
| `az account set -s <id>` | Byt subscription |
| `az account show` | Visa aktiv subscription |

```bash
# Logga in pa Azure
az login
# Oppnar webblasare for autentisering

# Lista dina subscriptions
az account list --output table
# Name                State    IsDefault
# ------------------  -------  ---------
# Production          Enabled  True
# Development         Enabled  False

# Byt till annan subscription
az account set --subscription "Development"

# Verifiera
az account show --query name -o tsv
# Development
```

### Utforska regioner och resurser

```bash
# Lista alla tillgangliga regioner
az account list-locations --output table | head -20
# DisplayName      Name             RegionalDisplayName
# ---------------  ---------------  ----------------------
# Sweden Central   swedencentral    (Europe) Sweden Central
# North Europe     northeurope      (Europe) North Europe

# Lista resursgrupper
az group list --output table
# Name              Location       Status
# ----------------  -------------  --------
# rg-production     swedencentral  Succeeded
# rg-development    northeurope    Succeeded
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Azure vs AWS

| Koncept | Azure | AWS |
|---------|-------|-----|
| **Compute** | Virtual Machines | EC2 |
| **Serverless** | Azure Functions | Lambda |
| **Kubernetes** | AKS | EKS |
| **Object Storage** | Blob Storage | S3 |
| **SQL Database** | Azure SQL | RDS |
| **NoSQL** | Cosmos DB | DynamoDB |
| **Identitet** | Entra ID (Azure AD) | IAM |
| **CDN** | Azure CDN | CloudFront |
| **DNS** | Azure DNS | Route 53 |
| **VPN** | VPN Gateway | VPN Gateway |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `AuthorizationFailed` | Saknar rattigheter | Kolla RBAC-roller |
| `SubscriptionNotFound` | Fel subscription vald | `az account set -s <id>` |
| `ResourceNotFound` | Resursen finns inte | Kolla resursgrupp och namn |
| `QuotaExceeded` | Maxgrans uppnadd | Beggar quota-okning |
| `RegionNotAvailable` | Tjansten saknas i regionen | Valj annan region |

```bash
# Kolla dina tilldelade roller
az role assignment list --assignee $(az ad signed-in-user show --query id -o tsv) --output table

# Kolla quota for en region
az vm list-usage --location swedencentral --output table
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Cloud-modeller** | IaaS = du skoter OS, PaaS = bara kod, SaaS = anvand |
| **Regioner** | Sweden Central for GDPR, North Europe for kostnad |
| **Azure CLI** | `az login` + `az account set` for att komma igang |
| **ARM** | Alla resurser hanteras via Azure Resource Manager |
| **Entra ID** | Identitetshantering (tidigare Azure AD) |

**Kom ihag:**
- Borja alltid med `az login` och verifiera ratt subscription
- Valj region baserat pa compliance, latens och kostnad
- PaaS ar nastan alltid battre an IaaS for nya projekt
- Azure Portal ar bra for laring, CLI/Bicep for automation
"""
        },
        # =====================================================================
        # NODE 2: Resource Groups & Azure Resource Manager
        # =====================================================================
        {
            "title": "Resource Groups & Azure Resource Manager",
            "slug": "resource-groups-arm",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 75,
            "content": """# Resource Groups & Azure Resource Manager

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Resource Groups ar viktigt |
|----------|----------------------------------|
| **Organisation** | Gruppera relaterade resurser |
| **Kostnadskontroll** | Se kostnader per projekt |
| **Livscykelhantering** | Ta bort allt pa en gang |
| **RBAC** | Tilldela rattigheter per grupp |
| **Tagging** | Metadata for automation |

Som DevOps-ingenjor maste du forsta:

- **Hur resurser organiseras** sa du kan strukturera projekt ratt
- **ARM:s roll** sa du forstar hur Azure fungerar under huven
- **Best practices** sa du undviker kostnadsfallor och kaos

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure Resource Manager (ARM)

ARM ar Azures kontrollplan - ALLT gar genom ARM:

```
┌─────────────────────────────────────────────────────────────┐
│                    AZURE RESOURCE MANAGER                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ Portal  │ │  CLI    │ │PowerShell│ │  REST   │          │
│  │         │ │ az xxx  │ │ Az-xxx  │ │  API    │          │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘          │
│       │           │           │           │                │
│       └───────────┴─────┬─────┴───────────┘                │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              AZURE RESOURCE MANAGER                  │   │
│  │    • Autentisering (Entra ID)                       │   │
│  │    • Auktorisering (RBAC)                           │   │
│  │    • Validering                                      │   │
│  │    • Throttling                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│         ┌───────────────┼───────────────┐                  │
│         ▼               ▼               ▼                  │
│  ┌───────────┐   ┌───────────┐   ┌───────────┐            │
│  │  Compute  │   │  Storage  │   │ Networking│            │
│  │  Provider │   │  Provider │   │  Provider │            │
│  └───────────┘   └───────────┘   └───────────┘            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**ARM:s fordelar:**
- Deklarativ deployment (beskriv vad, inte hur)
- Idempotent (kor samma template flera ganger = samma resultat)
- Beroenden hanteras automatiskt
- Rollback vid fel

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Resource Groups

En Resource Group ar en logisk container for Azure-resurser:

```
┌─────────────────────────────────────────────────────────────┐
│                    SUBSCRIPTION                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           Resource Group: rg-webapp-prod             │   │
│  │           Location: swedencentral                    │   │
│  │           Tags: env=prod, team=backend               │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │   │
│  │  │App Svc  │ │SQL DB   │ │Storage  │ │Key Vault│   │   │
│  │  │webapp   │ │sqldb    │ │stgdata  │ │kv-secrets│   │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           Resource Group: rg-webapp-dev              │   │
│  │           Location: northeurope                      │   │
│  │           Tags: env=dev, team=backend                │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐               │   │
│  │  │App Svc  │ │SQL DB   │ │Storage  │               │   │
│  │  │webapp-d │ │sqldb-d  │ │stgdata-d│               │   │
│  │  └─────────┘ └─────────┘ └─────────┘               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Viktiga regler

| Regel | Beskrivning |
|-------|-------------|
| **En region per RG** | RG har en region (for metadata), resurser kan vara i olika |
| **Delad livscykel** | Ta bort RG = ta bort alla resurser i den |
| **RBAC-scope** | Rattigheter kan tilldelas pa RG-niva |
| **Tagging** | Tags arver inte automatiskt till resurser |
| **Max 800 resurser** | Per resurstyp per RG |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hantera Resource Groups med CLI

### Skapa och lista

| Kommando | Beskrivning |
|----------|-------------|
| `az group create` | Skapa ny resursgrupp |
| `az group list` | Lista alla resursgrupper |
| `az group show` | Visa detaljer |
| `az group delete` | Ta bort resursgrupp |

```bash
# Skapa en resursgrupp
az group create \\
  --name rg-webapp-prod \\
  --location swedencentral \\
  --tags env=prod team=backend project=webapp

# Output:
# {
#   "id": "/subscriptions/.../resourceGroups/rg-webapp-prod",
#   "location": "swedencentral",
#   "name": "rg-webapp-prod",
#   "properties": { "provisioningState": "Succeeded" },
#   "tags": { "env": "prod", "team": "backend", "project": "webapp" }
# }

# Lista alla resursgrupper
az group list --output table
# Name              Location       Status
# ----------------  -------------  ---------
# rg-webapp-prod    swedencentral  Succeeded
# rg-webapp-dev     northeurope    Succeeded

# Visa detaljer for en specifik grupp
az group show --name rg-webapp-prod --output yaml
```

### Hantera resurser i gruppen

```bash
# Lista alla resurser i en grupp
az resource list --resource-group rg-webapp-prod --output table
# Name       ResourceGroup    Location       Type
# ---------  ---------------  -------------  -------------------
# webapp     rg-webapp-prod   swedencentral  Microsoft.Web/sites
# sqldb      rg-webapp-prod   swedencentral  Microsoft.Sql/servers

# Flytta resurser mellan grupper
az resource move \\
  --destination-group rg-webapp-dev \\
  --ids /subscriptions/.../resourceGroups/rg-webapp-prod/providers/Microsoft.Web/sites/webapp
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Naming Conventions

En bra namnstandard ar kritisk for hanterbarhet:

```
┌─────────────────────────────────────────────────────────────┐
│               AZURE NAMING CONVENTION                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Format: {resurstyp}-{arbetsbelastning}-{miljo}-{region}   │
│                                                             │
│  Exempel:                                                   │
│  ─────────────────────────────────────────────────────────  │
│  rg-webapp-prod-swe     Resource Group                     │
│  app-api-prod-swe       App Service                        │
│  sql-webapp-prod-swe    SQL Server                         │
│  st-data-prod-swe       Storage Account                    │
│  kv-secrets-prod-swe    Key Vault                          │
│  vnet-main-prod-swe     Virtual Network                    │
│  vm-web01-prod-swe      Virtual Machine                    │
│                                                             │
│  Prefix per resurstyp:                                      │
│  ─────────────────────────────────────────────────────────  │
│  rg-    Resource Group                                      │
│  app-   App Service                                         │
│  func-  Function App                                        │
│  sql-   SQL Server                                          │
│  sqldb- SQL Database                                        │
│  st-    Storage Account (lowercase, no hyphens)            │
│  kv-    Key Vault                                          │
│  vnet-  Virtual Network                                    │
│  snet-  Subnet                                             │
│  nsg-   Network Security Group                             │
│  pip-   Public IP                                          │
│  nic-   Network Interface                                  │
│  vm-    Virtual Machine                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Tagging Strategy

Tags ar key-value par for metadata:

```bash
# Lagg till tags vid skapande
az group create \\
  --name rg-webapp-prod \\
  --location swedencentral \\
  --tags \\
    env=prod \\
    team=backend \\
    costcenter=12345 \\
    owner=devops@company.com \\
    created=$(date +%Y-%m-%d)

# Uppdatera tags pa befintlig resurs
az group update \\
  --name rg-webapp-prod \\
  --tags env=prod team=backend costcenter=12345

# Lista resurser med specifik tag
az resource list --tag env=prod --output table

# Kolla kostnader per tag (i portalen: Cost Management + Billing)
```

### Rekommenderade tags

| Tag | Syfte | Exempel |
|-----|-------|---------|
| **env** | Miljo | prod, staging, dev |
| **team** | Agande team | backend, platform |
| **costcenter** | Kostnadsallokering | 12345 |
| **owner** | Kontaktperson | devops@company.com |
| **project** | Projektnamn | webapp, dataplatform |
| **created** | Skapandedatum | 2024-01-15 |
| **expiry** | Nar ska den tas bort | 2024-12-31 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `ResourceGroupNotFound` | RG finns inte | Kolla namn och subscription |
| `ResourceGroupBeingDeleted` | RG haller pa att tas bort | Vanta eller skapa med nytt namn |
| `ScopeLocked` | Lock pa RG | Ta bort lock forst |
| `InvalidResourceGroup` | Ogiltigt namn | Bara alfanumeriska, bindestreck |
| `TooManyResourceGroups` | Quota | Max 980 RGs per subscription |

```bash
# Kolla om det finns locks
az lock list --resource-group rg-webapp-prod

# Ta bort en lock
az lock delete --name LockName --resource-group rg-webapp-prod

# Tvinga borttagning av RG (VARNING: tar bort allt!)
az group delete --name rg-webapp-dev --yes --no-wait
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **ARM** | Alla Azure-operationer gar genom ARM |
| **Resource Group** | Logisk container, dela livscykel |
| **Naming** | Konsekvent namnstandard ar kritisk |
| **Tags** | Metadata for kostnad, agare, miljo |
| **RBAC** | Tilldela rattigheter pa RG-niva |

**Kom ihag:**
- En resurs kan bara tillhora EN resursgrupp
- Ta bort en RG tar bort ALLA resurser i den
- RG location ar bara for metadata, resurser kan vara i andra regioner
- Anvand alltid tags for kostnadsspaning
- Las ner produktions-RGs med Resource Locks
"""
        },
        # =====================================================================
        # NODE 3: Azure Portal & CLI Deep Dive
        # =====================================================================
        {
            "title": "Azure Portal & CLI Deep Dive",
            "slug": "azure-portal-cli-deep-dive",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Azure Portal & CLI Deep Dive

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor CLI-kunskap ar viktigt |
|----------|------------------------------|
| **Automation** | Skripta repetitiva tasks |
| **CI/CD** | Deploya fran pipelines |
| **Felsökning** | Snabbare an portalen |
| **Reproducerbarhet** | Dela kommandon med teamet |
| **Scripting** | Bash/PowerShell-integration |

Som DevOps-ingenjor maste du forsta:

- **Nar du anvander Portal vs CLI** sa du valjer ratt verktyg
- **Output-formatering** sa du kan parsa data i scripts
- **JMESPath queries** sa du kan filtrera stora datamangder

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure Portal vs CLI vs PowerShell

```
┌─────────────────────────────────────────────────────────────┐
│              VERKTYG FOR AZURE                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  AZURE PORTAL (portal.azure.com)                     │   │
│  │  + Visuellt, bra for laring                         │   │
│  │  + Komplex konfiguration                            │   │
│  │  - Kan inte automatiseras                           │   │
│  │  - Langsamt for repetitiva tasks                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  AZURE CLI (az)                                      │   │
│  │  + Cross-platform (Win/Mac/Linux)                   │   │
│  │  + Bash-vanligt                                     │   │
│  │  + Bra for scripting                                │   │
│  │  - Syntaxen kan vara lang                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  AZURE POWERSHELL (Az module)                        │   │
│  │  + Kraftfull objekt-pipeline                        │   │
│  │  + Bra for Windows-admins                           │   │
│  │  - Verbose syntax                                   │   │
│  │  - Krav pa PowerShell Core for Linux               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Nar anvanda vad?

| Scenario | Rekommendation |
|----------|----------------|
| **Lara sig Azure** | Portal |
| **Engangskonfiguration** | Portal eller CLI |
| **Bash-scripts** | Azure CLI |
| **PowerShell-scripts** | Azure PowerShell |
| **CI/CD pipelines** | Azure CLI (mest portabelt) |
| **Terraform/Bicep** | Anvands bakom kulisserna |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure Cloud Shell

Cloud Shell ar en webbaserad terminal direkt i Azure Portal:

```
┌─────────────────────────────────────────────────────────────┐
│                   CLOUD SHELL                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Fordelar:                                                  │
│  ─────────────────────────────────────────────────────────  │
│  • Ingen installation - kors i webblasaren                 │
│  • Forauthenticerad - redan inloggad                       │
│  • Persistent storage - filer sparas mellan sessioner      │
│  • Forinstallerade verktyg (az, kubectl, terraform, git)   │
│  • Bash ELLER PowerShell                                   │
│                                                             │
│  Begransningar:                                             │
│  ─────────────────────────────────────────────────────────  │
│  • 20 min timeout vid inaktivitet                          │
│  • 5 GB persistent storage                                  │
│  • Inte for tunga workloads                                │
│                                                             │
│  Starta:                                                    │
│  ─────────────────────────────────────────────────────────  │
│  1. Ga till portal.azure.com                               │
│  2. Klicka pa >_ ikonen uppe till hoger                    │
│  3. Valj Bash eller PowerShell                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure CLI Output-formatering

### Output-format

| Format | Anvandning | Exempel |
|--------|------------|---------|
| `--output table` | Lasbar oversikt | `az group list -o table` |
| `--output json` | Default, parsning | `az group list -o json` |
| `--output yaml` | Lasbar struktur | `az group list -o yaml` |
| `--output tsv` | Scripting, inga headers | `az group list -o tsv` |
| `--output none` | Tysta kommandon | `az group create -o none` |

```bash
# Table - lasbar for manniskor
az group list --output table
# Name              Location       Status
# ----------------  -------------  ---------
# rg-webapp-prod    swedencentral  Succeeded
# rg-webapp-dev     northeurope    Succeeded

# JSON - for programmering
az group list --output json
# [{"name": "rg-webapp-prod", "location": "swedencentral"...}]

# TSV - for scripting (tab-separerat, inga headers)
az group list --query "[].name" --output tsv
# rg-webapp-prod
# rg-webapp-dev

# None - tysta output (for scripting)
az group create --name rg-test --location swedencentral --output none
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## JMESPath Queries

JMESPath ar ett kraftfullt query-sprak for JSON:

### Grundlaggande queries

| Query | Beskrivning |
|-------|-------------|
| `[].name` | Hamta alla namn |
| `[0]` | Forsta elementet |
| `[?name=='x']` | Filter pa varde |
| `{n:name, l:location}` | Valj specifika falt |
| `sort_by(@, &name)` | Sortera |
| `[].name | [0]` | Hamta forsta namnet |

```bash
# Hamta bara namn
az group list --query "[].name" -o tsv
# rg-webapp-prod
# rg-webapp-dev

# Filtrera pa location
az group list --query "[?location=='swedencentral'].name" -o tsv
# rg-webapp-prod

# Valj specifika falt med alias
az group list --query "[].{Namn:name, Region:location}" -o table
# Namn              Region
# ----------------  -------------
# rg-webapp-prod    swedencentral

# Sortera efter namn
az group list --query "sort_by([],&name)" -o table

# Rakna antal resurser
az resource list -g rg-webapp-prod --query "length(@)"
# 5
```

### Avancerade queries

```bash
# Hamta alla VMs som ar iggang
az vm list --query "[?powerState=='VM running'].name" -o tsv

# Hitta Storage Accounts over 100GB
az storage account list \\
  --query "[?primaryEndpoints.blob!=null].{Name:name,SKU:sku.name}" \\
  -o table

# Lista App Services med deras URL
az webapp list --query "[].{Name:name, URL:defaultHostName}" -o table

# Hamta subscription ID
SUB_ID=$(az account show --query id -o tsv)
echo $SUB_ID
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiska CLI-monster

### Login och konfiguration

```bash
# Interaktiv login (oppnar webblasare)
az login

# Service principal login (for CI/CD)
az login --service-principal \\
  --username $APP_ID \\
  --password $SECRET \\
  --tenant $TENANT_ID

# Lista och byt subscription
az account list -o table
az account set --subscription "Production"

# Satt default-varden
az configure --defaults location=swedencentral
az configure --defaults group=rg-webapp-prod
```

### Vanliga operationer

```bash
# Skapa resursgrupp
az group create --name rg-test --location swedencentral

# Lista resurser i grupp
az resource list -g rg-webapp-prod -o table

# Ta bort resursgrupp (och allt i den!)
az group delete --name rg-test --yes --no-wait

# Exportera som ARM-template
az group export --name rg-webapp-prod > template.json

# Visa aktivitetslogg
az monitor activity-log list -g rg-webapp-prod --max-events 10
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `az: command not found` | CLI inte installerat | `brew install azure-cli` |
| `AADSTS700016` | Fel tenant | Logga ut och in igen |
| `AuthenticationError` | Token utgangen | `az login` igen |
| `InvalidQueryArgument` | Fel JMESPath-syntax | Testa query pa jsonpath.com |
| `--output: error` | Ogiltigt format | Anvand table/json/yaml/tsv/none |

```bash
# Rensa credentials och logga in pa nytt
az logout
az account clear
az login

# Debug-lage for mer info
az group list --debug

# Kolla CLI-version
az version
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Portal** | Bra for laring och komplex konfiguration |
| **CLI** | Bast for automation och scripting |
| **Cloud Shell** | Snabbstart utan installation |
| **Output-format** | table for lasning, tsv for scripting |
| **JMESPath** | Kraftfull filtrering av JSON-data |

**Kom ihag:**
- Anvand alltid `--query` for att bara hamta det du behover
- `--output tsv` for scripting, `--output table` for lasning
- Cloud Shell ar forauthenticerad - perfekt for snabba tasks
- Satt defaults med `az configure` for att spara tid
"""
        },
        # =====================================================================
        # NODE 4: Subscriptions & Cost Management
        # =====================================================================
        {
            "title": "Subscriptions & Cost Management",
            "slug": "subscriptions-cost-management",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 75,
            "content": """# Subscriptions & Cost Management

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor kostnadskontroll ar viktigt |
|----------|-----------------------------------|
| **Budget** | Undvik overraskningar pa fakturan |
| **Optimering** | Minska onodiga kostnader |
| **Showback** | Visa kostnader per team/projekt |
| **Governance** | Satt granser per miljo |
| **Forecasting** | Planera framtida kostnader |

Som DevOps-ingenjor maste du forsta:

- **Subscription-hierarkin** sa du kan organisera resurser
- **Kostnadsmodeller** sa du kan valja ratt storlekar
- **Budgets och alerts** sa du undviker budgetsprackning

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure Hierarki

```
┌─────────────────────────────────────────────────────────────┐
│                    AZURE HIERARKI                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ENTRA ID TENANT (Azure AD)                          │   │
│  │  Din organisations identitet                         │   │
│  │  tenant-id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx    │   │
│  └─────────────────────────────────────────────────────┘   │
│                          │                                  │
│           ┌──────────────┼──────────────┐                  │
│           ▼              ▼              ▼                  │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │ Management  │ │ Management  │ │ Management  │          │
│  │   Group     │ │   Group     │ │   Group     │          │
│  │  (valfri)   │ │  (valfri)   │ │  (valfri)   │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
│           │                                                 │
│    ┌──────┼──────┐                                         │
│    ▼      ▼      ▼                                         │
│  ┌────┐┌────┐┌────┐                                        │
│  │Sub1││Sub2││Sub3│  SUBSCRIPTIONS                         │
│  │Prod││Dev ││Test│  (Faktureringsgransen)                 │
│  └────┘└────┘└────┘                                        │
│    │                                                        │
│    ├──> Resource Group 1                                   │
│    ├──> Resource Group 2                                   │
│    └──> Resource Group 3                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Niva-beskrivning

| Niva | Syfte | Exempel |
|------|-------|---------|
| **Tenant** | Identitetsgransen | Ditt foretag |
| **Management Group** | Gruppera subscriptions | Efter avdelning |
| **Subscription** | Fakturerings + resursgrans | Prod, Dev, Test |
| **Resource Group** | Logisk gruppering | Per applikation |
| **Resource** | Faktiska tjanster | VM, SQL, Storage |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Subscription-typer

| Typ | Syfte | Granser |
|-----|-------|---------|
| **Free** | Testning | $200 kredit, 12 man |
| **Pay-As-You-Go** | Standard | Betala for anvandning |
| **Enterprise Agreement** | Stora foretag | Rabatter, prepaid |
| **CSP** | Via partner | Partner fakturerar |
| **Dev/Test** | Utveckling | Rabatterade priser |

```bash
# Lista dina subscriptions
az account list --output table
# Name         State    IsDefault
# -----------  -------  ---------
# Production   Enabled  True
# Development  Enabled  False
# Testing      Enabled  False

# Byt aktiv subscription
az account set --subscription "Development"

# Visa aktuell
az account show --query "{Name:name,ID:id,State:state}" -o table
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure Pricing Model

```
┌─────────────────────────────────────────────────────────────┐
│               AZURE KOSTNADSMODELL                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  COMPUTE (VMs, App Service)                                 │
│  ─────────────────────────────────────────────────────────  │
│  Per timme/sekund baserat pa:                              │
│  • VM-storlek (vCPU, RAM)                                  │
│  • OS (Windows kostar mer an Linux)                        │
│  • Region (priser varierar)                                │
│                                                             │
│  STORAGE                                                    │
│  ─────────────────────────────────────────────────────────  │
│  • Per GB lagrat (Hot/Cool/Archive)                        │
│  • Per operation (reads/writes)                            │
│  • Egress (data ut fran Azure)                             │
│                                                             │
│  NETWORKING                                                 │
│  ─────────────────────────────────────────────────────────  │
│  • Ingress: GRATIS                                         │
│  • Egress: $0.05-0.12 per GB                               │
│  • VPN/ExpressRoute: Fast manadskostnad                    │
│                                                             │
│  DATABASE                                                   │
│  ─────────────────────────────────────────────────────────  │
│  • DTU-baserat (Azure SQL)                                 │
│  • vCore-baserat (Azure SQL)                               │
│  • RU/s (Cosmos DB)                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Kostnadsoptimeringstips

| Strategi | Besparing | Exempel |
|----------|-----------|---------|
| **Reserved Instances** | 40-72% | Commit 1-3 ar |
| **Spot VMs** | 60-90% | Avbrytbara workloads |
| **Auto-shutdown** | 100% under natter | Dev/test VMs |
| **Right-sizing** | 20-50% | Valj ratt VM-storlek |
| **Azure Hybrid Benefit** | 40% | Anvand befintliga licenser |
| **Dev/Test pricing** | 50% | Utvecklingsmiljoer |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cost Management + Billing

### Satta upp Budget

```bash
# Skapa en budget via CLI
az consumption budget create \\
  --budget-name "Monthly-Limit" \\
  --amount 1000 \\
  --time-grain Monthly \\
  --start-date 2024-01-01 \\
  --end-date 2024-12-31 \\
  --resource-group rg-webapp-prod

# Lista budgets
az consumption budget list -o table

# Visa aktuella kostnader
az consumption usage list \\
  --start-date 2024-01-01 \\
  --end-date 2024-01-31 \\
  --query "[].{Service:consumedService,Cost:pretaxCost}" \\
  -o table
```

### Cost Analysis i Portal

```
┌─────────────────────────────────────────────────────────────┐
│                COST ANALYSIS                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Ga till Cost Management + Billing                      │
│  2. Valj Cost Analysis                                     │
│  3. Filtrera efter:                                        │
│     • Subscription                                         │
│     • Resource Group                                       │
│     • Tag (t.ex. team=backend)                            │
│     • Tidsperiod                                           │
│                                                             │
│  Vyer:                                                      │
│  ─────────────────────────────────────────────────────────  │
│  • AccumulatedCost  - Total kostnad over tid               │
│  • DailyCost        - Daglig kostnad                       │
│  • CostByService    - Per tjanst                           │
│  • CostByResource   - Per resurs                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure Advisor

Azure Advisor ger rekommendationer for:

| Kategori | Exempel |
|----------|---------|
| **Cost** | Oanvanda resurser, right-sizing |
| **Security** | Saknade firewalls, MFA |
| **Reliability** | Saknad redundans |
| **Operational Excellence** | Diagnostik, monitoring |
| **Performance** | Flaskhalsar, caching |

```bash
# Hamta Advisor-rekommendationer
az advisor recommendation list --output table

# Filtrera pa kostnad
az advisor recommendation list \\
  --category Cost \\
  --output table

# Exempel-output:
# Category  Impact  Problem
# --------  ------  ------------------------------------------
# Cost      High    VM is underutilized (CPU < 5%)
# Cost      Medium  Unattached disk found
# Cost      Low     Consider Reserved Instances
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Quotas och Limits

```bash
# Kolla VM-quota for en region
az vm list-usage --location swedencentral -o table
# Name                             CurrentValue    Limit
# ------------------------------   ------------    -----
# Total Regional vCPUs             4               10
# Standard BS Family vCPUs         4               10
# Standard DSv3 Family vCPUs       0               10

# Kolla Storage Account quota
az storage account list --query "length(@)"
# 3 (max 250 per subscription)
```

### Vanliga limits

| Resurs | Default Limit |
|--------|---------------|
| **vCPUs per region** | 10-20 (hojas via support) |
| **Resource Groups** | 980 per subscription |
| **Storage Accounts** | 250 per subscription |
| **VNets per region** | 1000 |
| **NICs per VM** | Varierar per VM-storlek |
| **Public IPs** | 1000 per subscription |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `QuotaExceeded` | Resursgrans nadd | Beggar okning via Portal |
| `Budget exceeded` | Over budget | Analysera kostnader, optimera |
| `SubscriptionNotFound` | Fel sub vald | `az account set -s <id>` |
| `Billing error` | Betalningsproblem | Uppdatera betalningsmetod |

```bash
# Beggar quota-okning
# 1. Ga till Subscriptions > Usage + quotas
# 2. Valj resursen
# 3. Klicka "Request increase"

# Eller via CLI (oppnar support-arende)
az support tickets create \\
  --ticket-name "Quota increase" \\
  --description "Need more vCPUs in swedencentral" \\
  --problem-classification "/providers/Microsoft.Support/services/..."
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Hierarki** | Tenant > Management Groups > Subscriptions > RGs |
| **Subscription** | Fakturerings- och resursgrans |
| **Cost Management** | Analysera och optimera kostnader |
| **Budgets** | Satt granser och alerts |
| **Advisor** | Automatiska rekommendationer |

**Kom ihag:**
- Separata subscriptions for Prod/Dev/Test ar best practice
- Satt alltid upp budget-alerts innan du borjar
- Kolla Azure Advisor regelbundet for optimeringstips
- Reserved Instances sparar 40-72% for stabila workloads
- Tagga ALLT for kostnadsspaning per team/projekt
"""
        },
        # =====================================================================
        # NODE 5: Virtual Machines Fundamentals
        # =====================================================================
        {
            "title": "Virtual Machines Fundamentals",
            "slug": "virtual-machines-fundamentals",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 100,
            "content": """# Virtual Machines Fundamentals

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor VMs ar viktigt |
|----------|----------------------|
| **Legacy apps** | Appar som inte kan containeriseras |
| **Full kontroll** | Anpassade OS-konfigurationer |
| **Windows workloads** | SQL Server, .NET Framework |
| **Lift-and-shift** | Migrera fran on-prem |
| **CI/CD agents** | Self-hosted build agents |

Som DevOps-ingenjor maste du forsta:

- **VM-familjer** sa du valjer ratt storlek for workloaden
- **Diskkonfiguration** sa du optimerar prestanda och kostnad
- **Networking** sa VMs kan kommunicera sakert

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## VM-arkitektur

```
┌─────────────────────────────────────────────────────────────┐
│                    AZURE VM ARKITEKTUR                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  VIRTUAL MACHINE                     │   │
│  │  ┌─────────────┬─────────────┬─────────────────┐   │   │
│  │  │    vCPUs    │    Memory   │      GPU        │   │   │
│  │  │    2-416    │   1GB-12TB  │   (N-series)    │   │   │
│  │  └─────────────┴─────────────┴─────────────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
│                          │                                  │
│           ┌──────────────┼──────────────┐                  │
│           ▼              ▼              ▼                  │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │  OS Disk    │ │  Data Disk  │ │  Temp Disk  │          │
│  │  (required) │ │  (optional) │ │  (ephemeral)│          │
│  │  30-4095 GB │ │  Up to 64TB │ │  Local SSD  │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
│                          │                                  │
│                          ▼                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    NIC (Network)                     │   │
│  │  Private IP │ Public IP (opt) │ NSG (firewall)      │   │
│  └─────────────────────────────────────────────────────┘   │
│                          │                                  │
│                          ▼                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  VIRTUAL NETWORK                     │   │
│  │               Subnet: 10.0.0.0/24                   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## VM-familjer

| Serie | Syfte | Exempel | Anvandning |
|-------|-------|---------|------------|
| **B** | Burstable | B1s, B2ms | Dev/test, latt last |
| **D** | General purpose | D2s_v5, D4s_v5 | Webbservrar, databaser |
| **E** | Memory optimized | E4s_v5, E16s_v5 | In-memory caching |
| **F** | Compute optimized | F2s_v2, F8s_v2 | Batch, gaming |
| **L** | Storage optimized | L8s_v3, L16s_v3 | Big data, SQL |
| **N** | GPU | NC6, NV12 | ML, rendering |
| **M** | Memory intensive | M32ms, M128s | SAP HANA |

### Namnkonvention

```
┌─────────────────────────────────────────────────────────────┐
│           Standard_D4s_v5                                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Standard   = Storlekklass (Basic/Standard)               │
│   D          = Familj (General purpose)                    │
│   4          = vCPUs                                       │
│   s          = Premium Storage-kapabel                     │
│   _v5        = Generation                                  │
│                                                             │
│   Andra suffix:                                            │
│   a = AMD-processor                                        │
│   d = Lokal temp disk                                      │
│   i = Isolated (dedikerad host)                            │
│   m = Memory-intensive variant                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa VM med CLI

### Grundlaggande kommando

```bash
# Skapa en enkel Linux VM
az vm create \\
  --resource-group rg-webapp-prod \\
  --name vm-web01 \\
  --image Ubuntu2204 \\
  --size Standard_B2s \\
  --admin-username azureuser \\
  --generate-ssh-keys \\
  --public-ip-sku Standard

# Output:
# {
#   "publicIpAddress": "20.123.45.67",
#   "fqdns": "",
#   "privateIpAddress": "10.0.0.4"
# }

# SSH till VM
ssh azureuser@20.123.45.67
```

### Avancerad konfiguration

```bash
# VM med specifik konfiguration
az vm create \\
  --resource-group rg-webapp-prod \\
  --name vm-web01 \\
  --image Ubuntu2204 \\
  --size Standard_D2s_v5 \\
  --admin-username azureuser \\
  --ssh-key-values ~/.ssh/id_rsa.pub \\
  --vnet-name vnet-prod \\
  --subnet snet-web \\
  --nsg nsg-web \\
  --public-ip-address "" \\
  --os-disk-size-gb 64 \\
  --storage-sku Premium_LRS \\
  --zone 1 \\
  --tags env=prod team=web

# Lagg till data disk
az vm disk attach \\
  --resource-group rg-webapp-prod \\
  --vm-name vm-web01 \\
  --name disk-data01 \\
  --size-gb 256 \\
  --sku Premium_LRS \\
  --new
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Disktyper

| Disk | IOPS | Throughput | Anvandning |
|------|------|------------|------------|
| **Standard HDD** | 500 | 60 MB/s | Backup, dev/test |
| **Standard SSD** | 6000 | 750 MB/s | Webbservrar |
| **Premium SSD** | 20000 | 900 MB/s | Produktion |
| **Ultra Disk** | 160000 | 4000 MB/s | SAP, databaser |

```bash
# Lista tillgangliga disk-SKUs
az disk list-skus --location swedencentral -o table

# Skapa managed disk
az disk create \\
  --resource-group rg-webapp-prod \\
  --name disk-data01 \\
  --size-gb 256 \\
  --sku Premium_LRS

# Expandera disk (VM maste vara stoppad)
az disk update \\
  --resource-group rg-webapp-prod \\
  --name disk-data01 \\
  --size-gb 512
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hantera VMs

### Livscykelkommandon

| Kommando | Beskrivning | Fakturering |
|----------|-------------|-------------|
| `az vm start` | Starta VM | Borjar |
| `az vm stop` | Stoppa (behaller IP) | Fortsatter |
| `az vm deallocate` | Deallocate (frigir resurser) | Stoppar |
| `az vm restart` | Omstart | Fortsatter |
| `az vm delete` | Ta bort | Stoppar |

```bash
# Starta VM
az vm start --resource-group rg-webapp-prod --name vm-web01

# Stoppa (behaller allokering - kostar fortfarande!)
az vm stop --resource-group rg-webapp-prod --name vm-web01

# Deallocate (frigor resurser - slutar kosta)
az vm deallocate --resource-group rg-webapp-prod --name vm-web01

# Visa status
az vm get-instance-view \\
  --resource-group rg-webapp-prod \\
  --name vm-web01 \\
  --query "instanceView.statuses[1].displayStatus" -o tsv
# VM running / VM deallocated

# Lista alla VMs
az vm list -d -o table
# Name      ResourceGroup    PowerState      PublicIps
# --------  ---------------  --------------  -----------
# vm-web01  rg-webapp-prod   VM running      20.123.45.67
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Auto-shutdown

```bash
# Konfigurera auto-shutdown (sparar pengar for dev/test)
az vm auto-shutdown \\
  --resource-group rg-webapp-prod \\
  --name vm-web01 \\
  --time 1900 \\
  --email "devops@company.com"

# Visa auto-shutdown status
az vm show \\
  --resource-group rg-webapp-prod \\
  --name vm-web01 \\
  --query "diagnosticsProfile"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `QuotaExceeded` | vCPU-grans nadd | Beggar okning eller annan region |
| `SkuNotAvailable` | VM-storlek saknas | Valj annan storlek eller region |
| `AllocationFailed` | Ingen kapacitet | Annan storlek/region/zone |
| `OSProvisioningTimedOut` | VM startade inte | Kolla boot diagnostics |
| `NetworkInterfaceError` | Natverksproblem | Kolla NSG och VNet |

```bash
# Kolla boot diagnostics
az vm boot-diagnostics get-boot-log \\
  --resource-group rg-webapp-prod \\
  --name vm-web01

# Kolla serial console
az serial-console connect \\
  --resource-group rg-webapp-prod \\
  --name vm-web01
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **B-series** | Burstable, bra for dev/test |
| **D-series** | General purpose, vanligast |
| **Premium SSD** | Krav for produktion |
| **Deallocate** | Stoppa fakturering |
| **Auto-shutdown** | Spara pengar for dev/test |

**Kom ihag:**
- `az vm stop` frigir INTE resurser - anvand `az vm deallocate`
- Valj alltid Managed Disks over Unmanaged
- B-serien ar billig men begransad - inte for stabil last
- Satt alltid auto-shutdown pa dev/test VMs
- Premium SSD kravs for SLA
"""
        },
        # =====================================================================
        # NODE 6: VM Scale Sets & Availability
        # =====================================================================
        {
            "title": "VM Scale Sets & Availability",
            "slug": "vm-scale-sets-availability",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 100,
            "content": """# VM Scale Sets & Availability

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor HA ar viktigt |
|----------|---------------------|
| **SLA** | 99.95-99.99% tillganglighet |
| **Skalning** | Hantera trafikspikar |
| **Redundans** | Overleva datacenterfel |
| **Zero-downtime** | Uppdatera utan avbrott |
| **Kostnadsoptimering** | Skala ner vid lag last |

Som DevOps-ingenjor maste du forsta:

- **Availability Sets vs Zones** sa du valjer ratt redundansmodell
- **VM Scale Sets** sa du kan auto-skala
- **Load Balancer** sa du kan fordela trafik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Tillganglighetsmodeller

```
┌─────────────────────────────────────────────────────────────┐
│             AZURE AVAILABILITY OPTIONS                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  AVAILABILITY SET (inom ett datacenter)                    │
│  ─────────────────────────────────────────────────────────  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Datacenter                                          │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐              │   │
│  │  │ Rack 1  │ │ Rack 2  │ │ Rack 3  │              │   │
│  │  │ (FD 0)  │ │ (FD 1)  │ │ (FD 2)  │              │   │
│  │  │   VM1   │ │   VM2   │ │   VM3   │              │   │
│  │  └─────────┘ └─────────┘ └─────────┘              │   │
│  │  SLA: 99.95%                                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  AVAILABILITY ZONES (separata datacenter)                  │
│  ─────────────────────────────────────────────────────────  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐               │
│  │  AZ 1   │    │  AZ 2   │    │  AZ 3   │               │
│  │   VM1   │    │   VM2   │    │   VM3   │               │
│  │Datacenter│    │Datacenter│    │Datacenter│               │
│  └─────────┘    └─────────┘    └─────────┘               │
│  SLA: 99.99%                                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Jamforelse

| Egenskap | Availability Set | Availability Zones |
|----------|------------------|-------------------|
| **Skydd mot** | Rack/host-fel | Datacenter-fel |
| **SLA** | 99.95% | 99.99% |
| **Latens** | Minimal | Lan latens (1-2ms) |
| **Kostnad** | Ingen extra | Ingen extra (men egress) |
| **Regioner** | Alla | Utvalda regioner |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Availability Sets

```bash
# Skapa Availability Set
az vm availability-set create \\
  --resource-group rg-webapp-prod \\
  --name avset-web \\
  --platform-fault-domain-count 3 \\
  --platform-update-domain-count 5

# Skapa VM i Availability Set
az vm create \\
  --resource-group rg-webapp-prod \\
  --name vm-web01 \\
  --availability-set avset-web \\
  --image Ubuntu2204 \\
  --size Standard_D2s_v5

# Lista VMs i ett Availability Set
az vm availability-set list-sizes \\
  --resource-group rg-webapp-prod \\
  --name avset-web -o table
```

### Fault Domains vs Update Domains

| Koncept | Beskrivning | Default |
|---------|-------------|---------|
| **Fault Domain (FD)** | Fysisk rack-isolation | 3 |
| **Update Domain (UD)** | Logisk gruppering for underhall | 5 |

```
┌─────────────────────────────────────────────────────────────┐
│                  AVAILABILITY SET                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│           FD 0          FD 1          FD 2                 │
│         ┌─────┐       ┌─────┐       ┌─────┐               │
│  UD 0   │ VM1 │       │     │       │     │               │
│         └─────┘       └─────┘       └─────┘               │
│         ┌─────┐       ┌─────┐       ┌─────┐               │
│  UD 1   │     │       │ VM2 │       │     │               │
│         └─────┘       └─────┘       └─────┘               │
│         ┌─────┐       ┌─────┐       ┌─────┐               │
│  UD 2   │     │       │     │       │ VM3 │               │
│         └─────┘       └─────┘       └─────┘               │
│                                                             │
│  Azure uppdaterar EN UD i taget                            │
│  Om ett rack gar ner = bara EN FD paverkas                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## VM Scale Sets (VMSS)

VMSS ar den rekommenderade losningen for skalbar compute:

```
┌─────────────────────────────────────────────────────────────┐
│                    VM SCALE SET                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  LOAD BALANCER                       │   │
│  │              (Azure LB / App Gateway)                │   │
│  └─────────────────────────────────────────────────────┘   │
│                          │                                  │
│           ┌──────────────┼──────────────┐                  │
│           ▼              ▼              ▼                  │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │    VM 0     │ │    VM 1     │ │    VM 2     │          │
│  │  (Instance) │ │  (Instance) │ │  (Instance) │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
│                          │                                  │
│                          ▼                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  AUTOSCALE                           │   │
│  │  Min: 2 │ Max: 10 │ Scale on: CPU > 70%             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Skapa VMSS

```bash
# Skapa VMSS med autoscaling
az vmss create \\
  --resource-group rg-webapp-prod \\
  --name vmss-web \\
  --image Ubuntu2204 \\
  --vm-sku Standard_D2s_v5 \\
  --instance-count 2 \\
  --admin-username azureuser \\
  --generate-ssh-keys \\
  --zones 1 2 3 \\
  --load-balancer lb-web \\
  --upgrade-policy-mode Automatic

# Konfigurera autoscale
az monitor autoscale create \\
  --resource-group rg-webapp-prod \\
  --resource vmss-web \\
  --resource-type Microsoft.Compute/virtualMachineScaleSets \\
  --name autoscale-web \\
  --min-count 2 \\
  --max-count 10 \\
  --count 2

# Lagg till scale-out regel (CPU > 70%)
az monitor autoscale rule create \\
  --resource-group rg-webapp-prod \\
  --autoscale-name autoscale-web \\
  --condition "Percentage CPU > 70 avg 5m" \\
  --scale out 2

# Lagg till scale-in regel (CPU < 30%)
az monitor autoscale rule create \\
  --resource-group rg-webapp-prod \\
  --autoscale-name autoscale-web \\
  --condition "Percentage CPU < 30 avg 5m" \\
  --scale in 1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hantera VMSS

```bash
# Lista instanser
az vmss list-instances \\
  --resource-group rg-webapp-prod \\
  --name vmss-web -o table
# InstanceId  LatestModelApplied  ProvisioningState
# ----------  ------------------  -----------------
# 0           True                Succeeded
# 1           True                Succeeded

# Skala manuellt
az vmss scale \\
  --resource-group rg-webapp-prod \\
  --name vmss-web \\
  --new-capacity 5

# Uppdatera image
az vmss update \\
  --resource-group rg-webapp-prod \\
  --name vmss-web \\
  --set virtualMachineProfile.storageProfile.imageReference.version=latest

# Uppgradera instanser
az vmss update-instances \\
  --resource-group rg-webapp-prod \\
  --name vmss-web \\
  --instance-ids "*"

# Reimage (aterinstallera OS)
az vmss reimage \\
  --resource-group rg-webapp-prod \\
  --name vmss-web \\
  --instance-id 0
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Upgrade Policies

| Policy | Beskrivning | Anvandning |
|--------|-------------|------------|
| **Manual** | Du triggar uppgraderingar | Maximal kontroll |
| **Automatic** | Azure uppgraderar automatiskt | Stateless apps |
| **Rolling** | Uppgraderar i batchar | Minimal downtime |

```bash
# Satt Rolling upgrade policy
az vmss update \\
  --resource-group rg-webapp-prod \\
  --name vmss-web \\
  --set upgradePolicy.mode=Rolling \\
  --set upgradePolicy.rollingUpgradePolicy.maxBatchInstancePercent=20 \\
  --set upgradePolicy.rollingUpgradePolicy.pauseTimeBetweenBatches=PT5S
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure Load Balancer

```
┌─────────────────────────────────────────────────────────────┐
│              LOAD BALANCER TYPER                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BASIC (GRATIS)                    STANDARD                │
│  ─────────────────────────        ─────────────────────────│
│  • Max 300 instanser              • Max 1000 instanser     │
│  • Inget SLA                      • 99.99% SLA             │
│  • Ingen zone redundans           • Zone-redundant         │
│  • Oppet default                  • Stangd default (NSG)   │
│                                                             │
│  PUBLIC LB                         INTERNAL LB             │
│  ─────────────────────────        ─────────────────────────│
│  • Internet-facing                • VNet-intern            │
│  • Public IP                      • Private IP             │
│  • Webbtrafik                     • Databastrafik          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Skapa Standard Load Balancer
az network lb create \\
  --resource-group rg-webapp-prod \\
  --name lb-web \\
  --sku Standard \\
  --frontend-ip-name frontend \\
  --backend-pool-name backend \\
  --public-ip-address pip-lb

# Skapa health probe
az network lb probe create \\
  --resource-group rg-webapp-prod \\
  --lb-name lb-web \\
  --name probe-http \\
  --protocol Http \\
  --port 80 \\
  --path /health

# Skapa load balancing regel
az network lb rule create \\
  --resource-group rg-webapp-prod \\
  --lb-name lb-web \\
  --name rule-http \\
  --protocol Tcp \\
  --frontend-port 80 \\
  --backend-port 80 \\
  --frontend-ip-name frontend \\
  --backend-pool-name backend \\
  --probe-name probe-http
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `AllocationFailed` | Ingen kapacitet i vald AZ | Annan zone eller region |
| `OverconstrainedAllocation` | For strikt placering | Minska constraints |
| `VMSSInstanceNotFound` | Instans borttagen | Kolla autoscale-historik |
| `HealthProbeNoResponse` | Backend ar nere | Kolla NSG och app |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Availability Zones** | 99.99% SLA, skyddar mot datacenter-fel |
| **Availability Sets** | 99.95% SLA, skyddar mot rack-fel |
| **VMSS** | Auto-scaling, rolling upgrades |
| **Standard LB** | Zone-redundant, 99.99% SLA |
| **Health Probes** | Kritiskt for routing |

**Kom ihag:**
- Anvand alltid Availability Zones for produktion
- VMSS ar standard for skalbar compute
- Standard Load Balancer ar default (Basic fases ut)
- Konfigurera health probes - annars ingen failover
- Rolling upgrade policy for zero-downtime deploys
"""
        },
        # =====================================================================
        # NODE 7: Azure App Service
        # =====================================================================
        {
            "title": "Azure App Service",
            "slug": "azure-app-service",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 100,
            "content": """# Azure App Service

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor App Service ar viktigt |
|----------|------------------------------|
| **PaaS** | Ingen serverhantering |
| **CI/CD** | Inbyggd GitHub/Azure DevOps-integration |
| **Skalning** | Auto-scale utan infra-jobb |
| **SSL/TLS** | Gratis certifikat |
| **Slots** | Zero-downtime deployments |

Som DevOps-ingenjor maste du forsta:

- **App Service Plans** sa du valjer ratt kapacitet och kostnad
- **Deployment slots** sa du kan deploya utan downtime
- **Configuration** sa du hanterar miljoevariabler ratt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## App Service Arkitektur

```
┌─────────────────────────────────────────────────────────────┐
│                    APP SERVICE                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │               APP SERVICE PLAN                       │   │
│  │  (Underliggande compute - delade resurser)          │   │
│  │                                                      │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐           │   │
│  │  │  Web App │ │  Web App │ │  API App │           │   │
│  │  │ (Python) │ │  (Node)  │ │  (.NET)  │           │   │
│  │  └──────────┘ └──────────┘ └──────────┘           │   │
│  │                                                      │   │
│  │  Plan: P1v3 (2 vCPU, 8 GB RAM)                     │   │
│  │  Instances: 3                                       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  DEPLOYMENT SLOTS                                          │
│  ─────────────────────────────────────────────────────────  │
│  ┌───────────────┐    ┌───────────────┐                   │
│  │  Production   │◄──►│   Staging     │  (Swap)          │
│  │    Slot       │    │    Slot       │                   │
│  └───────────────┘    └───────────────┘                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## App Service Plans

| Tier | Syfte | Features | Kostnad |
|------|-------|----------|---------|
| **F1** | Free | 60 CPU min/dag, ingen SLA | Gratis |
| **B1** | Basic | Custom domain, SSL | ~$13/man |
| **S1** | Standard | Slots, auto-scale | ~$70/man |
| **P1v3** | Premium | VNet, mer kraft | ~$140/man |
| **I1v2** | Isolated | Dedikerad miljo | ~$300/man |

### Skapa App Service Plan

```bash
# Skapa App Service Plan
az appservice plan create \\
  --resource-group rg-webapp-prod \\
  --name plan-webapp \\
  --sku P1v3 \\
  --location swedencentral \\
  --is-linux

# Lista planer
az appservice plan list -o table

# Skala plan (antal instanser)
az appservice plan update \\
  --resource-group rg-webapp-prod \\
  --name plan-webapp \\
  --number-of-workers 3
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa Web App

```bash
# Skapa Web App (Python)
az webapp create \\
  --resource-group rg-webapp-prod \\
  --plan plan-webapp \\
  --name app-api-prod \\
  --runtime "PYTHON:3.11"

# Skapa Web App (Node.js)
az webapp create \\
  --resource-group rg-webapp-prod \\
  --plan plan-webapp \\
  --name app-frontend-prod \\
  --runtime "NODE:18-lts"

# Skapa Web App (Docker)
az webapp create \\
  --resource-group rg-webapp-prod \\
  --plan plan-webapp \\
  --name app-custom-prod \\
  --deployment-container-image-name nginx:latest

# Lista runtimes
az webapp list-runtimes --os-type linux
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Deployment-metoder

| Metod | Anvandning | Kommando |
|-------|------------|----------|
| **ZIP Deploy** | Enkel deploy | `az webapp deploy` |
| **Git** | Kontinuerlig | GitHub Actions |
| **Docker** | Containers | ACR integration |
| **FTP** | Legacy | Undvik |

### ZIP Deploy

```bash
# Deploya fran ZIP
az webapp deploy \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod \\
  --src-path ./dist.zip \\
  --type zip

# Deploya fran lokal mapp
cd myapp
zip -r ../deploy.zip .
az webapp deploy \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod \\
  --src-path ../deploy.zip
```

### GitHub Actions Deploy

```yaml
# .github/workflows/deploy.yml
name: Deploy to Azure
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: azure/webapps-deploy@v2
        with:
          app-name: app-api-prod
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
          package: .
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Deployment Slots

Slots ger zero-downtime deployments:

```
┌─────────────────────────────────────────────────────────────┐
│               DEPLOYMENT SLOT WORKFLOW                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Deploy till staging                                    │
│     ┌────────────┐                                         │
│     │  STAGING   │ ◄── Deploy ny version                  │
│     │  v2.0.0    │                                         │
│     └────────────┘                                         │
│                                                             │
│  2. Testa staging (samma URL)                              │
│     https://app-api-prod-staging.azurewebsites.net        │
│                                                             │
│  3. Swap slots                                              │
│     ┌────────────┐    ┌────────────┐                      │
│     │ PRODUCTION │◄──►│  STAGING   │                      │
│     │  v1.0.0    │    │  v2.0.0    │                      │
│     └────────────┘    └────────────┘                      │
│           │                  │                              │
│           ▼                  ▼                              │
│     ┌────────────┐    ┌────────────┐                      │
│     │ PRODUCTION │    │  STAGING   │                      │
│     │  v2.0.0    │    │  v1.0.0    │ (rollback ready)    │
│     └────────────┘    └────────────┘                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Skapa staging slot
az webapp deployment slot create \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod \\
  --slot staging

# Deploy till staging
az webapp deploy \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod \\
  --slot staging \\
  --src-path ./dist.zip

# Swap staging till produktion
az webapp deployment slot swap \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod \\
  --slot staging \\
  --target-slot production

# Rollback (swap tillbaka)
az webapp deployment slot swap \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod \\
  --slot production \\
  --target-slot staging
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Konfiguration

### App Settings (miljoevariabler)

```bash
# Satt miljoevariabler
az webapp config appsettings set \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod \\
  --settings \\
    DATABASE_URL="postgresql://..." \\
    REDIS_URL="redis://..." \\
    LOG_LEVEL="info"

# Lista settings
az webapp config appsettings list \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod -o table

# Ta bort setting
az webapp config appsettings delete \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod \\
  --setting-names OLD_SETTING
```

### Slot-sticky settings

```bash
# Markera setting som slot-sticky
# (stannar i sloten, foljer inte med vid swap)
az webapp config appsettings set \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod \\
  --slot staging \\
  --slot-settings \\
    LOG_LEVEL="debug" \\
    ENVIRONMENT="staging"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Autoscale

```bash
# Konfigurera autoscale
az monitor autoscale create \\
  --resource-group rg-webapp-prod \\
  --resource plan-webapp \\
  --resource-type Microsoft.Web/serverfarms \\
  --name autoscale-webapp \\
  --min-count 2 \\
  --max-count 10 \\
  --count 2

# Scale-out pa CPU
az monitor autoscale rule create \\
  --resource-group rg-webapp-prod \\
  --autoscale-name autoscale-webapp \\
  --condition "CpuPercentage > 70 avg 5m" \\
  --scale out 2

# Scale-in pa CPU
az monitor autoscale rule create \\
  --resource-group rg-webapp-prod \\
  --autoscale-name autoscale-webapp \\
  --condition "CpuPercentage < 30 avg 10m" \\
  --scale in 1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `503 Service Unavailable` | App kraschade | Kolla logs, oeka plan |
| `502 Bad Gateway` | Startup timeout | Oka startup timeout |
| `Application Error` | Kodfelfil | Kolla stderr logs |
| `Slot swap failed` | Config skillnad | Kolla sticky settings |

```bash
# Kolla logs
az webapp log tail \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod

# Kolla deployment logs
az webapp log deployment show \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod

# Starta om app
az webapp restart \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **App Service Plan** | Delar resurser mellan flera appar |
| **Slots** | Zero-downtime via swap |
| **App Settings** | Miljoevariabler, slot-sticky |
| **Autoscale** | Baserat pa CPU, requests |
| **ZIP Deploy** | Enklaste deployment-metoden |

**Kom ihag:**
- Anvand minst S1 for slots och autoscale
- Slot-sticky settings for miljospecifik config
- Testa alltid i staging innan swap
- Aktivera Application Insights for monitoring
- Premium tier kravs for VNet-integration
"""
        },
        # =====================================================================
        # NODE 8: Azure Functions & Serverless
        # =====================================================================
        {
            "title": "Azure Functions & Serverless",
            "slug": "azure-functions-serverless",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 100,
            "content": """# Azure Functions & Serverless

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Serverless ar viktigt |
|----------|------------------------------|
| **Kostnad** | Betala bara for exekvering |
| **Skalning** | Automatisk, oandlig skalning |
| **Event-driven** | Triggas av events |
| **Microservices** | Sma, fokuserade funktioner |
| **Integration** | Koppla ihop system |

Som DevOps-ingenjor maste du forsta:

- **Hosting plans** sa du valjer ratt modell
- **Triggers och bindings** sa du kan koppla ihop system
- **Cold start** sa du forstar latens-implikationer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Serverless Arkitektur

```
┌─────────────────────────────────────────────────────────────┐
│                  AZURE FUNCTIONS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TRIGGERS (vad startar funktionen)                         │
│  ─────────────────────────────────────────────────────────  │
│  HTTP Request ──┐                                          │
│  Timer (cron) ──┼──► ┌────────────────┐                   │
│  Queue message ─┤    │   FUNCTION     │                   │
│  Blob created ──┤    │   (din kod)    │                   │
│  Event Grid ────┤    │                │                   │
│  Cosmos change ─┘    └────────┬───────┘                   │
│                               │                            │
│  BINDINGS (input/output)      ▼                           │
│  ─────────────────────────────────────────────────────────  │
│                    ┌─────────────┐                         │
│                    │   OUTPUT    │                         │
│                    │ Queue/Blob/ │                         │
│                    │ Cosmos/HTTP │                         │
│                    └─────────────┘                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hosting Plans

| Plan | Skalning | Cold Start | Max Exekvering | Kostnad |
|------|----------|------------|----------------|---------|
| **Consumption** | Auto (0-200) | Ja | 5 min (default) | Per exekvering |
| **Premium** | Auto (1-100) | Nej | 60 min | Per sekund |
| **Dedicated** | Manual | Nej | Obegransad | Fast |

```
┌─────────────────────────────────────────────────────────────┐
│               HOSTING PLAN JAMFORELSE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CONSUMPTION (Serverless)                                  │
│  ─────────────────────────────────────────────────────────  │
│  + Betala bara for anvandning                              │
│  + Skalar till noll                                        │
│  - Cold start (1-3 sekunder)                               │
│  - Max 5 min timeout                                       │
│  Bast for: Sporadiska workloads, dev/test                 │
│                                                             │
│  PREMIUM (Serverless med alltid-varm)                      │
│  ─────────────────────────────────────────────────────────  │
│  + Ingen cold start                                        │
│  + VNet-integration                                        │
│  + Storre instanser                                        │
│  - Dyrare                                                   │
│  Bast for: Produktion, latens-kansliga appar              │
│                                                             │
│  DEDICATED (App Service Plan)                              │
│  ─────────────────────────────────────────────────────────  │
│  + Forutsagbar kostnad                                     │
│  + Delade resurser med Web Apps                            │
│  - Ingen auto-scale till noll                              │
│  Bast for: Befintlig App Service-infra                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa Function App

```bash
# Skapa Storage Account (kravs)
az storage account create \\
  --resource-group rg-webapp-prod \\
  --name stfuncprod \\
  --sku Standard_LRS

# Skapa Function App (Consumption)
az functionapp create \\
  --resource-group rg-webapp-prod \\
  --name func-api-prod \\
  --storage-account stfuncprod \\
  --consumption-plan-location swedencentral \\
  --runtime python \\
  --runtime-version 3.11 \\
  --functions-version 4 \\
  --os-type linux

# Skapa Function App (Premium)
az functionapp plan create \\
  --resource-group rg-webapp-prod \\
  --name plan-func-premium \\
  --sku EP1 \\
  --is-linux

az functionapp create \\
  --resource-group rg-webapp-prod \\
  --name func-api-premium \\
  --storage-account stfuncprod \\
  --plan plan-func-premium \\
  --runtime python \\
  --runtime-version 3.11 \\
  --functions-version 4
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Triggers

### HTTP Trigger

```python
# function_app.py
import azure.functions as func
import json

app = func.FunctionApp()

@app.route(route="hello", methods=["GET", "POST"])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name", "World")
    return func.HttpResponse(
        json.dumps({"message": f"Hello, {name}!"}),
        mimetype="application/json"
    )
```

### Timer Trigger (Cron)

```python
@app.timer_trigger(
    schedule="0 */5 * * * *",  # Var 5:e minut
    arg_name="timer"
)
def scheduled_cleanup(timer: func.TimerRequest):
    # Kor cleanup varje 5 minuter
    logging.info("Running scheduled cleanup...")
    cleanup_old_files()
```

### Queue Trigger

```python
@app.queue_trigger(
    queue_name="orders",
    connection="AzureWebJobsStorage",
    arg_name="msg"
)
def process_order(msg: func.QueueMessage):
    order = json.loads(msg.get_body().decode())
    logging.info(f"Processing order: {order['id']}")
    # Bearbeta order...
```

### Blob Trigger

```python
@app.blob_trigger(
    path="uploads/{name}",
    connection="AzureWebJobsStorage",
    arg_name="blob"
)
def process_upload(blob: func.InputStream):
    logging.info(f"Processing blob: {blob.name}")
    content = blob.read()
    # Bearbeta fil...
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Bindings

Bindings ar deklarativa kopplingar till andra tjanster:

```python
# Input binding - hamtar data
@app.route(route="user/{id}")
@app.cosmos_db_input(
    database_name="users",
    container_name="profiles",
    connection="CosmosConnection",
    id="{id}",
    partition_key="{id}",
    arg_name="user"
)
def get_user(req: func.HttpRequest, user: dict):
    return func.HttpResponse(json.dumps(user))

# Output binding - skriver data
@app.route(route="order", methods=["POST"])
@app.queue_output(
    queue_name="orders",
    connection="AzureWebJobsStorage",
    arg_name="msg"
)
def create_order(req: func.HttpRequest, msg: func.Out[str]):
    order = req.get_json()
    msg.set(json.dumps(order))  # Skickas till queue
    return func.HttpResponse("Order created")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Lokal utveckling

```bash
# Installera Azure Functions Core Tools
brew install azure-functions-core-tools@4

# Skapa nytt projekt
func init MyFunctionApp --python
cd MyFunctionApp

# Skapa ny funktion
func new --name hello --template "HTTP trigger"

# Kor lokalt
func start

# Testa
curl http://localhost:7071/api/hello?name=World
```

### Projektstruktur

```
MyFunctionApp/
├── function_app.py      # Huvudfil med alla funktioner
├── host.json            # Global konfiguration
├── local.settings.json  # Lokala miljoevariabler
└── requirements.txt     # Python dependencies
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Deploy

```bash
# Deploy fran lokal maskin
func azure functionapp publish func-api-prod

# Deploy via ZIP
az functionapp deployment source config-zip \\
  --resource-group rg-webapp-prod \\
  --name func-api-prod \\
  --src deploy.zip

# Konfigurera app settings
az functionapp config appsettings set \\
  --resource-group rg-webapp-prod \\
  --name func-api-prod \\
  --settings \\
    DATABASE_URL="postgresql://..." \\
    API_KEY="secret"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Durable Functions

For langt gande, komplexa workflows:

```python
import azure.durable_functions as df

# Orchestrator - koordinerar workflow
@app.orchestration_trigger(context_name="context")
def order_workflow(context: df.DurableOrchestrationContext):
    order = context.get_input()

    # Steg 1: Validera
    valid = yield context.call_activity("validate_order", order)

    # Steg 2: Bearbeta betalning
    payment = yield context.call_activity("process_payment", order)

    # Steg 3: Skicka bekraftelse
    yield context.call_activity("send_confirmation", order)

    return {"status": "completed", "order_id": order["id"]}

# Activity - gor det faktiska jobbet
@app.activity_trigger(input_name="order")
def validate_order(order: dict):
    # Validera order...
    return True

# HTTP trigger for att starta workflow
@app.route(route="order/start")
@app.durable_client_input(client_name="client")
async def start_order(req, client):
    order = req.get_json()
    instance_id = await client.start_new("order_workflow", None, order)
    return {"instance_id": instance_id}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `Timeout` | >5 min (Consumption) | Premium plan eller dela upp |
| `Cold start` | Ingen aktiv instans | Premium plan, warmup |
| `Out of memory` | For stor payload | Streama data, oka plan |
| `Storage connection failed` | Felaktig connection string | Kolla app settings |

```bash
# Kolla funktionsloggar
az functionapp log tail \\
  --resource-group rg-webapp-prod \\
  --name func-api-prod

# Kolla metriker
az monitor metrics list \\
  --resource func-api-prod \\
  --resource-type Microsoft.Web/sites \\
  --metric "FunctionExecutionCount"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Consumption** | Billigast, cold start, 5 min timeout |
| **Premium** | Ingen cold start, VNet, langre timeout |
| **Triggers** | HTTP, Timer, Queue, Blob, Cosmos, etc. |
| **Bindings** | Deklarativ dataatkomst |
| **Durable** | Langt gande workflows |

**Kom ihag:**
- Consumption ar perfekt for sporadiska workloads
- Premium for latens-kansliga produktionsappar
- Anvand bindings istallet for att skriva egen integrationskod
- Durable Functions for komplexa, langt gande processer
- Lokal utveckling med `func start` innan deploy
"""
        },
        # =====================================================================
        # NODE 9: Azure Storage - Blob & Files
        # =====================================================================
        {
            "title": "Azure Storage - Blob & Files",
            "slug": "azure-storage-blob-files",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 100,
            "content": """# Azure Storage - Blob & Files

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Storage ar viktigt |
|----------|--------------------------|
| **Backup** | Lagra backups kostnadseffektivt |
| **Static hosting** | Hosta statiska webbsidor |
| **Data lake** | Big data och analytics |
| **Fildelning** | SMB-shares for VMs |
| **Artifact storage** | CI/CD artifacts |

Som DevOps-ingenjor maste du forsta:

- **Storage-typer** sa du valjer ratt for anvandningsfallet
- **Access tiers** sa du optimerar kostnad
- **Security** sa du skyddar data korrekt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Storage Account Arkitektur

```
┌─────────────────────────────────────────────────────────────┐
│                   STORAGE ACCOUNT                           │
│               (stwebappprod)                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  BLOB STORAGE                                        │   │
│  │  Objektlagring for filer, bilder, backups           │   │
│  │  ┌──────────────┐  ┌──────────────┐                │   │
│  │  │ Container:   │  │ Container:   │                │   │
│  │  │ uploads      │  │ backups      │                │   │
│  │  │ ├── img1.jpg │  │ ├── db.bak   │                │   │
│  │  │ ├── img2.png │  │ └── logs.zip │                │   │
│  │  │ └── doc.pdf  │  │              │                │   │
│  │  └──────────────┘  └──────────────┘                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  FILE STORAGE                                        │   │
│  │  SMB-shares for VMs och lokala maskiner             │   │
│  │  ┌──────────────┐                                   │   │
│  │  │ Share:       │                                   │   │
│  │  │ config       │                                   │   │
│  │  │ ├── app.conf │                                   │   │
│  │  │ └── certs/   │                                   │   │
│  │  └──────────────┘                                   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  TABLE STORAGE (NoSQL key-value)                    │   │
│  │  QUEUE STORAGE (meddelandekoer)                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa Storage Account

```bash
# Skapa Storage Account
az storage account create \\
  --resource-group rg-webapp-prod \\
  --name stwebappprod \\
  --location swedencentral \\
  --sku Standard_LRS \\
  --kind StorageV2 \\
  --access-tier Hot

# Hamta connection string
az storage account show-connection-string \\
  --resource-group rg-webapp-prod \\
  --name stwebappprod \\
  --query connectionString -o tsv

# Hamta account key
az storage account keys list \\
  --resource-group rg-webapp-prod \\
  --name stwebappprod \\
  --query "[0].value" -o tsv
```

### SKU-typer

| SKU | Redundans | Anvandning |
|-----|-----------|------------|
| **Standard_LRS** | 3 kopior lokalt | Dev/test |
| **Standard_ZRS** | 3 kopior i 3 zoner | Produktion |
| **Standard_GRS** | 6 kopior (2 regioner) | DR-krav |
| **Premium_LRS** | SSD, 3 kopior | High performance |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Blob Storage

### Access Tiers

| Tier | Lagring | Access | Anvandning |
|------|---------|--------|------------|
| **Hot** | Hogst | Lagst | Aktiv data |
| **Cool** | Lagre | Hogre | Sallsynt access (30d) |
| **Archive** | Lagst | Hogst | Langtidslagring (180d) |

```bash
# Skapa container
az storage container create \\
  --account-name stwebappprod \\
  --name uploads \\
  --public-access off

# Ladda upp fil
az storage blob upload \\
  --account-name stwebappprod \\
  --container-name uploads \\
  --file ./image.jpg \\
  --name images/image.jpg

# Ladda upp mapp
az storage blob upload-batch \\
  --account-name stwebappprod \\
  --destination uploads \\
  --source ./local-folder

# Lista blobbar
az storage blob list \\
  --account-name stwebappprod \\
  --container-name uploads -o table

# Ladda ner fil
az storage blob download \\
  --account-name stwebappprod \\
  --container-name uploads \\
  --name images/image.jpg \\
  --file ./downloaded.jpg
```

### Access Tier hantering

```bash
# Andra tier for en blob
az storage blob set-tier \\
  --account-name stwebappprod \\
  --container-name backups \\
  --name old-backup.zip \\
  --tier Archive

# Satt lifecycle policy (automatisk tier-flytt)
az storage account management-policy create \\
  --account-name stwebappprod \\
  --policy @policy.json
```

```json
// policy.json - Flytta till Cool efter 30 dagar
{
  "rules": [{
    "name": "move-to-cool",
    "enabled": true,
    "type": "Lifecycle",
    "definition": {
      "filters": {"blobTypes": ["blockBlob"]},
      "actions": {
        "baseBlob": {
          "tierToCool": {"daysAfterModificationGreaterThan": 30},
          "tierToArchive": {"daysAfterModificationGreaterThan": 90}
        }
      }
    }
  }]
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## File Storage

Azure Files ar SMB-shares i molnet:

```bash
# Skapa file share
az storage share create \\
  --account-name stwebappprod \\
  --name config \\
  --quota 100

# Ladda upp fil
az storage file upload \\
  --account-name stwebappprod \\
  --share-name config \\
  --source ./app.conf

# Lista filer
az storage file list \\
  --account-name stwebappprod \\
  --share-name config -o table

# Montera pa Linux VM
sudo mount -t cifs \\
  //stwebappprod.file.core.windows.net/config \\
  /mnt/config \\
  -o vers=3.0,username=stwebappprod,password=<key>,dir_mode=0777
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Static Website Hosting

```bash
# Aktivera static website
az storage blob service-properties update \\
  --account-name stwebappprod \\
  --static-website \\
  --index-document index.html \\
  --404-document 404.html

# Ladda upp webbsida
az storage blob upload-batch \\
  --account-name stwebappprod \\
  --destination '$web' \\
  --source ./dist

# Hamta URL
az storage account show \\
  --name stwebappprod \\
  --query "primaryEndpoints.web" -o tsv
# https://stwebappprod.z1.web.core.windows.net/
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Saskerhet

### SAS Tokens (Shared Access Signature)

```bash
# Generera SAS for container (giltig 1 timme)
az storage container generate-sas \\
  --account-name stwebappprod \\
  --name uploads \\
  --permissions rwl \\
  --expiry $(date -u -v+1H '+%Y-%m-%dT%H:%MZ')

# Generera SAS for specifik blob
az storage blob generate-sas \\
  --account-name stwebappprod \\
  --container-name uploads \\
  --name images/photo.jpg \\
  --permissions r \\
  --expiry $(date -u -v+1H '+%Y-%m-%dT%H:%MZ') \\
  --full-uri

# Output: https://stwebappprod.blob.core.windows.net/uploads/images/photo.jpg?sv=...
```

### Private Endpoints

```bash
# Skapa Private Endpoint for Storage
az network private-endpoint create \\
  --resource-group rg-webapp-prod \\
  --name pe-storage \\
  --vnet-name vnet-prod \\
  --subnet snet-private \\
  --private-connection-resource-id $(az storage account show -n stwebappprod --query id -o tsv) \\
  --group-id blob \\
  --connection-name conn-blob
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## AzCopy

AzCopy ar ett snabbt verktyg for stora datamangder:

```bash
# Installera AzCopy
brew install azcopy

# Logga in
azcopy login

# Kopiera fil till blob
azcopy copy ./data.zip "https://stwebappprod.blob.core.windows.net/uploads/data.zip"

# Synka mapp med container
azcopy sync ./local-folder "https://stwebappprod.blob.core.windows.net/uploads" --recursive

# Kopiera mellan storage accounts
azcopy copy \\
  "https://source.blob.core.windows.net/container/*" \\
  "https://dest.blob.core.windows.net/container/"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `AuthorizationFailure` | Felaktig nyckel/SAS | Regenerera nyckel |
| `BlobNotFound` | Fel sokvag | Kolla container/blob-namn |
| `ContainerNotFound` | Container saknas | Skapa container forst |
| `PublicAccessNotPermitted` | Public access av | Anvand SAS eller private endpoint |
| `StorageAccountNotFound` | Fel kontonamn | Kolla stavning (lowercase) |

```bash
# Kolla storage-konto
az storage account show --name stwebappprod -o table

# Lista containers
az storage container list --account-name stwebappprod -o table

# Kolla ACL
az storage container show-permission \\
  --account-name stwebappprod \\
  --name uploads
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Blob** | Objektlagring for filer, bilder, backups |
| **Files** | SMB-shares for VMs |
| **Access Tiers** | Hot/Cool/Archive for kostnad |
| **SAS** | Tidsbegransad access utan delade nycklar |
| **AzCopy** | Snabb bulk-kopiering |

**Kom ihag:**
- Namn pa storage accounts maste vara globalt unika, lowercase
- ZRS for produktion, LRS for dev/test
- Anvand lifecycle policies for automatisk tier-flytt
- SAS tokens ar battre an delade nycklar
- Private endpoints for hog sakerhet
"""
        },
        # =====================================================================
        # NODE 10: Azure SQL & Database Services
        # =====================================================================
        {
            "title": "Azure SQL & Database Services",
            "slug": "azure-sql-database-services",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 100,
            "content": """# Azure SQL & Database Services

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Managed DB ar viktigt |
|----------|------------------------------|
| **Underhall** | Azure skoter patching, backups |
| **HA** | Inbyggd redundans och failover |
| **Skalning** | Dynamisk skalning utan downtime |
| **Sakerhet** | TDE, firewall, auditing |
| **Monitoring** | Inbyggd Query Performance |

Som DevOps-ingenjor maste du forsta:

- **Pricing models** sa du valjer ratt kapacitet
- **Backup/restore** sa du kan aterstalla data
- **Connectivity** sa appar kan koppla upp sakert

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure SQL Produkter

```
┌─────────────────────────────────────────────────────────────┐
│                   AZURE SQL FAMILY                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  AZURE SQL DATABASE (PaaS - mest anvand)                   │
│  ─────────────────────────────────────────────────────────  │
│  • Managed databas-tjanst                                  │
│  • Inget OS-ansvar                                         │
│  • Auto-tuning, intelligent insights                       │
│  Bast for: Nya appar, microservices                       │
│                                                             │
│  AZURE SQL MANAGED INSTANCE                                │
│  ─────────────────────────────────────────────────────────  │
│  • Nara 100% SQL Server-kompatibilitet                    │
│  • Cross-database queries                                  │
│  • SQL Agent, linked servers                               │
│  Bast for: Lift-and-shift fran on-prem                    │
│                                                             │
│  SQL SERVER ON VM (IaaS)                                   │
│  ─────────────────────────────────────────────────────────  │
│  • Full SQL Server                                         │
│  • Du skoter allt (OS, patching, backups)                 │
│  Bast for: Legacy-appar som kraver full kontroll          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure SQL Database

### Pricing Models

| Modell | Beskrivning | Anvandning |
|--------|-------------|------------|
| **DTU** | CPU+RAM+IO bundlat | Enkel, forutsagbar |
| **vCore** | Separat CPU/RAM | Flexibel, migration |
| **Serverless** | Auto-pause | Dev/test, sporadisk |
| **Hyperscale** | 100TB+, snabb scale | Enterprise |

### Skapa SQL Database

```bash
# Skapa SQL Server (logisk server)
az sql server create \\
  --resource-group rg-webapp-prod \\
  --name sql-webapp-prod \\
  --location swedencentral \\
  --admin-user sqladmin \\
  --admin-password 'ComplexP@ssw0rd!'

# Skapa databas (vCore)
az sql db create \\
  --resource-group rg-webapp-prod \\
  --server sql-webapp-prod \\
  --name db-webapp \\
  --edition GeneralPurpose \\
  --compute-model Provisioned \\
  --family Gen5 \\
  --capacity 2 \\
  --zone-redundant true

# Skapa databas (DTU - enklare)
az sql db create \\
  --resource-group rg-webapp-prod \\
  --server sql-webapp-prod \\
  --name db-webapp \\
  --edition Standard \\
  --capacity 20

# Skapa Serverless databas
az sql db create \\
  --resource-group rg-webapp-prod \\
  --server sql-webapp-prod \\
  --name db-dev \\
  --edition GeneralPurpose \\
  --compute-model Serverless \\
  --family Gen5 \\
  --min-capacity 0.5 \\
  --max-capacity 4 \\
  --auto-pause-delay 60
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Connectivity

### Firewall Rules

```bash
# Tillat Azure-tjanster
az sql server firewall-rule create \\
  --resource-group rg-webapp-prod \\
  --server sql-webapp-prod \\
  --name AllowAzureServices \\
  --start-ip-address 0.0.0.0 \\
  --end-ip-address 0.0.0.0

# Tillat specifik IP
az sql server firewall-rule create \\
  --resource-group rg-webapp-prod \\
  --server sql-webapp-prod \\
  --name AllowMyIP \\
  --start-ip-address 203.0.113.50 \\
  --end-ip-address 203.0.113.50

# Lista regler
az sql server firewall-rule list \\
  --resource-group rg-webapp-prod \\
  --server sql-webapp-prod -o table
```

### Connection String

```bash
# Hamta connection string
az sql db show-connection-string \\
  --server sql-webapp-prod \\
  --name db-webapp \\
  --client ado.net

# Output:
# Server=tcp:sql-webapp-prod.database.windows.net,1433;
# Database=db-webapp;
# User ID=<username>;
# Password=<password>;
# Encrypt=true;
```

### Private Endpoint

```bash
# Skapa Private Endpoint
az network private-endpoint create \\
  --resource-group rg-webapp-prod \\
  --name pe-sql \\
  --vnet-name vnet-prod \\
  --subnet snet-private \\
  --private-connection-resource-id $(az sql server show -g rg-webapp-prod -n sql-webapp-prod --query id -o tsv) \\
  --group-id sqlServer \\
  --connection-name conn-sql

# Inaktivera public access
az sql server update \\
  --resource-group rg-webapp-prod \\
  --name sql-webapp-prod \\
  --public-network-access Disabled
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Backup & Restore

Azure SQL har automatiska backups:

| Backup | Frekvens | Retention |
|--------|----------|-----------|
| **Full** | Veckovis | 7-35 dagar |
| **Differential** | Var 12-24h | 7-35 dagar |
| **Transaction log** | Var 5-10 min | 7-35 dagar |

```bash
# Satt backup retention
az sql db ltr-policy set \\
  --resource-group rg-webapp-prod \\
  --server sql-webapp-prod \\
  --database db-webapp \\
  --weekly-retention P4W \\
  --monthly-retention P12M \\
  --yearly-retention P5Y

# Point-in-time restore
az sql db restore \\
  --resource-group rg-webapp-prod \\
  --server sql-webapp-prod \\
  --name db-webapp-restored \\
  --dest-name db-webapp-restored \\
  --time "2024-01-15T10:30:00Z"

# Geo-restore (fran annan region)
az sql db restore \\
  --resource-group rg-webapp-dr \\
  --server sql-webapp-dr \\
  --name db-webapp \\
  --source-database-deletion-date "2024-01-15T10:30:00Z" \\
  --deleted-time "2024-01-15T10:30:00Z"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Monitoring & Performance

```bash
# Aktivera auditing
az sql server audit-policy update \\
  --resource-group rg-webapp-prod \\
  --name sql-webapp-prod \\
  --state Enabled \\
  --storage-account stauditlogs

# Aktivera threat detection
az sql db threat-policy update \\
  --resource-group rg-webapp-prod \\
  --server sql-webapp-prod \\
  --name db-webapp \\
  --state Enabled \\
  --email-addresses security@company.com

# Visa performance metriker
az sql db show \\
  --resource-group rg-webapp-prod \\
  --server sql-webapp-prod \\
  --name db-webapp \\
  --query "{DTU:currentServiceObjectiveName,Size:maxSizeBytes}" -o table
```

### Query Performance Insight

I Azure Portal:
1. Ga till din SQL Database
2. Valj "Query Performance Insight"
3. Se langsammaste queries
4. Fa index-rekommendationer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## High Availability

```
┌─────────────────────────────────────────────────────────────┐
│               AZURE SQL HA OPTIONS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ZONE REDUNDANT (inom region)                              │
│  ─────────────────────────────────────────────────────────  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐               │
│  │  AZ 1   │    │  AZ 2   │    │  AZ 3   │               │
│  │ Primary │───▶│ Replica │───▶│ Replica │               │
│  └─────────┘    └─────────┘    └─────────┘               │
│  SLA: 99.995%                                              │
│                                                             │
│  GEO-REPLICATION (mellan regioner)                         │
│  ─────────────────────────────────────────────────────────  │
│  ┌────────────────┐         ┌────────────────┐            │
│  │  Sweden Central │───────▶│  North Europe   │            │
│  │    Primary     │  Async  │   Secondary    │            │
│  └────────────────┘         └────────────────┘            │
│  RPO: ~5 sekunder                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Aktivera geo-replication
az sql db replica create \\
  --resource-group rg-webapp-dr \\
  --server sql-webapp-dr \\
  --name db-webapp \\
  --partner-resource-group rg-webapp-prod \\
  --partner-server sql-webapp-prod

# Failover till secondary
az sql db replica set-primary \\
  --resource-group rg-webapp-dr \\
  --server sql-webapp-dr \\
  --name db-webapp
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `Login failed` | Fel credentials | Kolla losenord |
| `Cannot connect` | Firewall | Lagg till IP-regel |
| `DTU limit reached` | For lag kapacitet | Skala upp |
| `Database is paused` | Serverless paus | Forsta request startar |
| `TDE encryption error` | Nyckelhantering | Kolla Key Vault |

```bash
# Kolla server-status
az sql server show \\
  --resource-group rg-webapp-prod \\
  --name sql-webapp-prod \\
  --query state -o tsv

# Kolla databas-status
az sql db show \\
  --resource-group rg-webapp-prod \\
  --server sql-webapp-prod \\
  --name db-webapp \\
  --query status -o tsv
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **DTU** | Enkelt, forutsagbart |
| **vCore** | Flexibelt, migration |
| **Serverless** | Auto-pause, dev/test |
| **Zone redundant** | 99.995% SLA |
| **Geo-replication** | DR, ~5s RPO |

**Kom ihag:**
- Skapa alltid firewall-regler eller private endpoints
- Serverless ar perfekt for dev/test med auto-pause
- Zone redundant kravs for kritiska workloads
- Aktivera auditing och threat detection
- Point-in-time restore funkar upp till retention-period
"""
        },
        # =====================================================================
        # NODE 11: Cosmos DB & NoSQL
        # =====================================================================
        {
            "title": "Cosmos DB & NoSQL",
            "slug": "cosmos-db-nosql",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 100,
            "content": """# Cosmos DB & NoSQL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Cosmos DB ar viktigt |
|----------|----------------------------|
| **Global** | Multi-region med single-digit latency |
| **Skalbarhet** | Oandlig horisontell skalning |
| **Flexibilitet** | Multipla API:er (SQL, MongoDB, etc.) |
| **Tillganglighet** | 99.999% SLA |
| **Serverless** | Betala-per-request for dev/test |

Som DevOps-ingenjor maste du forsta:

- **Request Units (RU)** sa du kan dimensionera ratt
- **Partition keys** sa du undviker hot partitions
- **Consistency levels** sa du forstar trade-offs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cosmos DB Arkitektur

```
┌─────────────────────────────────────────────────────────────┐
│                    COSMOS DB                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              COSMOS DB ACCOUNT                       │   │
│  │              (cosmos-webapp-prod)                    │   │
│  │                                                      │   │
│  │  API: SQL (Core)  │  MongoDB  │  Cassandra  │  ...  │   │
│  └─────────────────────────────────────────────────────┘   │
│                          │                                  │
│           ┌──────────────┼──────────────┐                  │
│           ▼              ▼              ▼                  │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │  DATABASE   │ │  DATABASE   │ │  DATABASE   │          │
│  │   users     │ │   orders    │ │   logs      │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
│           │                                                 │
│     ┌─────┼─────┐                                          │
│     ▼     ▼     ▼                                          │
│  ┌─────┐┌─────┐┌─────┐                                     │
│  │Cont.││Cont.││Cont.│  CONTAINERS                         │
│  │prof.││sess.││logs │  (Partitionerade)                   │
│  └─────┘└─────┘└─────┘                                     │
│                                                             │
│  GLOBAL DISTRIBUTION                                       │
│  ─────────────────────────────────────────────────────────  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐               │
│  │ Sweden  │◄──►│  West   │◄──►│  East   │               │
│  │ Central │    │ Europe  │    │  US     │               │
│  └─────────┘    └─────────┘    └─────────┘               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Request Units (RU)

RU ar Cosmos DBs valuta for throughput:

| Operation | Ungefarlig RU-kostnad |
|-----------|----------------------|
| **Read 1KB** | 1 RU |
| **Write 1KB** | 5 RU |
| **Query (enkel)** | 2-5 RU |
| **Query (komplex)** | 10-100+ RU |
| **Index update** | 5-10 RU |

```
┌─────────────────────────────────────────────────────────────┐
│               THROUGHPUT MODELLER                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PROVISIONED (Forutsagbar)                                 │
│  ─────────────────────────────────────────────────────────  │
│  • Satt RU/s i forvag (400-unlimited)                     │
│  • Betala per timme oavsett anvandning                     │
│  • Autoscale: 10-100% av max                              │
│  Bast for: Produktion med forutsagbar last                │
│                                                             │
│  SERVERLESS                                                │
│  ─────────────────────────────────────────────────────────  │
│  • Betala per request (RU)                                 │
│  • Ingen minsta kostnad                                    │
│  • Max 5000 RU/s burst                                     │
│  Bast for: Dev/test, sporadisk last                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa Cosmos DB

```bash
# Skapa Cosmos DB account (SQL API)
az cosmosdb create \\
  --resource-group rg-webapp-prod \\
  --name cosmos-webapp-prod \\
  --kind GlobalDocumentDB \\
  --locations regionName=swedencentral failoverPriority=0 \\
  --default-consistency-level Session \\
  --enable-automatic-failover true

# Skapa database
az cosmosdb sql database create \\
  --resource-group rg-webapp-prod \\
  --account-name cosmos-webapp-prod \\
  --name webapp

# Skapa container med partition key
az cosmosdb sql container create \\
  --resource-group rg-webapp-prod \\
  --account-name cosmos-webapp-prod \\
  --database-name webapp \\
  --name users \\
  --partition-key-path "/userId" \\
  --throughput 400

# Skapa serverless container
az cosmosdb sql container create \\
  --resource-group rg-webapp-prod \\
  --account-name cosmos-webapp-prod \\
  --database-name webapp \\
  --name logs \\
  --partition-key-path "/timestamp"
  # (Serverless satts pa konto-niva)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Partition Keys

Partition key ar det viktigaste beslutet i Cosmos DB:

```
┌─────────────────────────────────────────────────────────────┐
│                    PARTITION STRATEGY                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BRA PARTITION KEY                                         │
│  ─────────────────────────────────────────────────────────  │
│  • Hog kardinalitet (manga unika varden)                   │
│  • Anvands i de flesta queries                             │
│  • Jamn distribution av data                               │
│                                                             │
│  Exempel for Users:                                        │
│  ✓ /userId          (unikt per user)                       │
│  ✗ /country         (for fa varden = hot partition)        │
│  ✗ /createdAt       (tidsstampel = sequentiell writes)    │
│                                                             │
│  Exempel for Orders:                                       │
│  ✓ /customerId      (queries ar ofta per kund)             │
│  ✓ /orderId         (unikt)                                │
│  ✗ /status          (for fa varden)                        │
│                                                             │
│  HOT PARTITION (undvik!)                                   │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  Partition "SE":  ████████████████████  90% av trafik     │
│  Partition "US":  ██                    5%                 │
│  Partition "UK":  █                     5%                 │
│                                                             │
│  = Partition "SE" blir flaskhals                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Consistency Levels

| Niva | Beskrivning | Latens | Anvandning |
|------|-------------|--------|------------|
| **Strong** | Linearizable reads | Hogre | Finansiella system |
| **Bounded Staleness** | Max K versioner/T sek | Medel | Balans |
| **Session** | Read your writes | Lag | Default, mest anvand |
| **Consistent Prefix** | Aldrig out-of-order | Lag | Analytics |
| **Eventual** | Ingen garanti | Lagst | Counters, likes |

```bash
# Satt default consistency
az cosmosdb update \\
  --resource-group rg-webapp-prod \\
  --name cosmos-webapp-prod \\
  --default-consistency-level Session
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CRUD Operations

### Python SDK

```python
from azure.cosmos import CosmosClient, PartitionKey

# Anslut
client = CosmosClient(endpoint, credential)
database = client.get_database_client("webapp")
container = database.get_container_client("users")

# Create
user = {
    "id": "user-123",
    "userId": "user-123",
    "name": "Alice",
    "email": "alice@example.com"
}
container.create_item(user)

# Read
user = container.read_item(item="user-123", partition_key="user-123")

# Query
query = "SELECT * FROM c WHERE c.email = @email"
items = container.query_items(
    query=query,
    parameters=[{"name": "@email", "value": "alice@example.com"}],
    enable_cross_partition_query=True
)
for item in items:
    print(item)

# Update (replace)
user["name"] = "Alice Smith"
container.replace_item(item="user-123", body=user)

# Delete
container.delete_item(item="user-123", partition_key="user-123")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Global Distribution

```bash
# Lagg till region
az cosmosdb update \\
  --resource-group rg-webapp-prod \\
  --name cosmos-webapp-prod \\
  --locations regionName=swedencentral failoverPriority=0 \\
  --locations regionName=northeurope failoverPriority=1 \\
  --locations regionName=eastus failoverPriority=2

# Aktivera multi-region writes
az cosmosdb update \\
  --resource-group rg-webapp-prod \\
  --name cosmos-webapp-prod \\
  --enable-multiple-write-locations true
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `429 Too Many Requests` | RU limit nadd | Oka RU eller optimera queries |
| `Cross partition query` | Query utan partition key | Inkludera partition key |
| `Request rate large` | Hot partition | Andra partition key strategy |
| `DocumentClientException` | Felaktig query | Kolla syntax |

```bash
# Kolla RU-anvandning
az cosmosdb sql container throughput show \\
  --resource-group rg-webapp-prod \\
  --account-name cosmos-webapp-prod \\
  --database-name webapp \\
  --name users

# Oka throughput
az cosmosdb sql container throughput update \\
  --resource-group rg-webapp-prod \\
  --account-name cosmos-webapp-prod \\
  --database-name webapp \\
  --name users \\
  --throughput 1000
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **RU** | Cosmos DBs "valuta" - planera kapacitet |
| **Partition Key** | Viktigaste beslutet - valj noggrant |
| **Consistency** | Session ar default och racker for de flesta |
| **Global** | Multi-region med millisekund-latens |
| **Serverless** | Perfekt for dev/test |

**Kom ihag:**
- Partition key kan INTE andras efter skapande
- Cross-partition queries ar dyra - undvik om mojligt
- 429-errors betyder att du behover mer RU eller optimera
- Serverless har 5000 RU/s burst-limit
- Multi-region writes okar komplexitet (conflict resolution)
"""
        },
        # =====================================================================
        # NODE 12: Azure Cache for Redis
        # =====================================================================
        {
            "title": "Azure Cache for Redis",
            "slug": "azure-cache-redis",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "content": """# Azure Cache for Redis

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Redis ar viktigt |
|----------|------------------------|
| **Caching** | Minska databas-last |
| **Sessions** | Distribuerad session-hantering |
| **Pub/Sub** | Real-time messaging |
| **Rate Limiting** | API throttling |
| **Leaderboards** | Snabba sorted sets |

Som DevOps-ingenjor maste du forsta:

- **Tiers och storlekar** sa du valjer ratt kapacitet
- **Persistence** sa du forstar data-hållbarhet
- **Clustering** sa du kan skala horisontellt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure Redis Tiers

| Tier | RAM | Features | Anvandning |
|------|-----|----------|------------|
| **Basic** | 250MB-53GB | Ingen SLA, ingen replik | Dev/test |
| **Standard** | 250MB-53GB | 99.9% SLA, replikering | Produktion |
| **Premium** | 6GB-120GB | Clustering, VNet, geo-rep | Enterprise |
| **Enterprise** | 12GB-2TB | Redis Modules, 99.999% | Mission-critical |

```
┌─────────────────────────────────────────────────────────────┐
│               AZURE REDIS ARKITEKTUR                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BASIC (ingen HA)              STANDARD (HA)               │
│  ┌─────────────────┐          ┌─────────────────┐          │
│  │    Primary      │          │    Primary      │          │
│  │   (Single node) │          │       │         │          │
│  └─────────────────┘          │       ▼         │          │
│                               │    Replica      │          │
│                               └─────────────────┘          │
│                                                             │
│  PREMIUM (Clustering)                                      │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐                  │
│  │Shard 0│ │Shard 1│ │Shard 2│ │Shard 3│                  │
│  │ P + R │ │ P + R │ │ P + R │ │ P + R │                  │
│  └───────┘ └───────┘ └───────┘ └───────┘                  │
│  Max 10 shards = 10x kapacitet                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa Azure Redis

```bash
# Skapa Redis Cache (Standard)
az redis create \\
  --resource-group rg-webapp-prod \\
  --name redis-webapp-prod \\
  --location swedencentral \\
  --sku Standard \\
  --vm-size C1 \\
  --enable-non-ssl-port false

# Hamta anslutningsinformation
az redis show \\
  --resource-group rg-webapp-prod \\
  --name redis-webapp-prod \\
  --query "{Host:hostName,Port:sslPort}" -o table

# Hamta access keys
az redis list-keys \\
  --resource-group rg-webapp-prod \\
  --name redis-webapp-prod

# Skapa Premium med clustering
az redis create \\
  --resource-group rg-webapp-prod \\
  --name redis-webapp-premium \\
  --location swedencentral \\
  --sku Premium \\
  --vm-size P1 \\
  --shard-count 4
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Connection String

```
# Format:
redis-webapp-prod.redis.cache.windows.net:6380,password=<key>,ssl=True,abortConnect=False

# Python
redis://:<password>@redis-webapp-prod.redis.cache.windows.net:6380/0?ssl=true

# Environment variable
REDIS_URL=rediss://:<password>@redis-webapp-prod.redis.cache.windows.net:6380/0
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Anvandning med Python

```python
import redis
import json

# Anslut
r = redis.Redis(
    host='redis-webapp-prod.redis.cache.windows.net',
    port=6380,
    password='<access-key>',
    ssl=True
)

# ===============================
# CACHING
# ===============================

# Set med TTL (expiry)
r.setex('user:123', 3600, json.dumps({'name': 'Alice'}))

# Get
user_data = r.get('user:123')
if user_data:
    user = json.loads(user_data)

# Cache-aside pattern
def get_user(user_id):
    cache_key = f'user:{user_id}'
    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)

    # Miss - hamta fran databas
    user = db.get_user(user_id)
    r.setex(cache_key, 3600, json.dumps(user))
    return user

# ===============================
# SESSIONS
# ===============================

# Spara session
r.hset(f'session:{session_id}', mapping={
    'user_id': 123,
    'created_at': '2024-01-15T10:00:00',
    'ip': '192.168.1.1'
})
r.expire(f'session:{session_id}', 86400)  # 24h

# Hamta session
session = r.hgetall(f'session:{session_id}')

# ===============================
# RATE LIMITING
# ===============================

def rate_limit(user_id, limit=100, window=60):
    key = f'rate:{user_id}'
    current = r.incr(key)
    if current == 1:
        r.expire(key, window)
    return current <= limit
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pub/Sub

```python
# Publisher
r.publish('notifications', json.dumps({
    'type': 'order_completed',
    'order_id': 456
}))

# Subscriber
pubsub = r.pubsub()
pubsub.subscribe('notifications')

for message in pubsub.listen():
    if message['type'] == 'message':
        data = json.loads(message['data'])
        print(f"Received: {data}")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Persistence & Backup

### Data Persistence (Premium)

| Typ | Beskrivning | RPO |
|-----|-------------|-----|
| **RDB** | Snapshots | Konfigurerbart |
| **AOF** | Append-only log | ~1 sekund |

```bash
# Aktivera RDB persistence
az redis update \\
  --resource-group rg-webapp-prod \\
  --name redis-webapp-premium \\
  --set redisConfiguration.rdb-backup-enabled=true \\
  --set redisConfiguration.rdb-backup-frequency=60

# Exportera data till blob
az redis export \\
  --resource-group rg-webapp-prod \\
  --name redis-webapp-premium \\
  --prefix backup \\
  --container "https://stbackups.blob.core.windows.net/redis?<sas>"

# Importera data fran blob
az redis import \\
  --resource-group rg-webapp-prod \\
  --name redis-webapp-premium \\
  --files "https://stbackups.blob.core.windows.net/redis/backup.rdb?<sas>"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Monitoring

```bash
# Kolla cache-info
az redis show \\
  --resource-group rg-webapp-prod \\
  --name redis-webapp-prod \\
  --query "{Used:redisConfiguration.maxmemory-reserved,Clients:redisConfiguration.maxclients}" -o table

# Console (anslut direkt)
# I Azure Portal: Redis Cache > Console
> INFO
> DBSIZE
> KEYS *
> GET user:123
```

### Viktiga metriker

| Metrik | Beskrivning | Varning |
|--------|-------------|---------|
| **Cache Hits** | Traffar i cachen | Lag = dalig caching |
| **Cache Misses** | Missar | Hog = problem |
| **Server Load** | CPU-anvandning | >80% = skala |
| **Used Memory** | RAM-anvandning | >80% = skala |
| **Connected Clients** | Antal anslutningar | Max limit |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Best Practices

```
┌─────────────────────────────────────────────────────────────┐
│              REDIS BEST PRACTICES                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. ANVAND ALLTID SSL                                      │
│     Aldrig non-ssl-port i produktion                       │
│                                                             │
│  2. SATT TTL PA ALLT                                       │
│     Undvik memory-overflow                                  │
│                                                             │
│  3. ANVAND PIPELINES                                        │
│     Batcha kommandon for battre prestanda                  │
│                                                             │
│  4. VALJ RATT STORLEK                                       │
│     Storre cache = farre missar                            │
│                                                             │
│  5. OVERVAKA METRIKER                                       │
│     Hit ratio, memory, server load                         │
│                                                             │
│  6. CONNECTION POOLING                                      │
│     Ateranvand anslutningar                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `Connection refused` | SSL inte aktiverat | Anvand port 6380 + SSL |
| `OOM` | Slut pa minne | Skala upp eller satt TTL |
| `Too many connections` | Connection leak | Anvand pooling |
| `MOVED` | Clustering redirect | Anvand cluster-aware client |
| `Timeout` | Overbelastad | Skala upp, optimera queries |

```bash
# Kolla memory-anvandning
az redis show \\
  --resource-group rg-webapp-prod \\
  --name redis-webapp-prod \\
  --query "instances[0].isMaster"

# Forcera failover (testa HA)
az redis force-reboot \\
  --resource-group rg-webapp-prod \\
  --name redis-webapp-prod \\
  --reboot-type PrimaryNode
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Standard** | Produktion med replika |
| **Premium** | Clustering, VNet, persistence |
| **TTL** | Satt alltid expiry |
| **SSL** | Alltid port 6380 |
| **Monitoring** | Hit ratio ar viktigast |

**Kom ihag:**
- Basic ar BARA for dev/test (ingen SLA)
- Satt alltid TTL - annars fyller cachen
- Anvand connection pooling for bast prestanda
- Premium kravs for VNet-integration
- Overvaka hit ratio - under 90% = problem
"""
        },
        # =====================================================================
        # NODE 13: Azure DevOps & Pipelines
        # =====================================================================
        {
            "title": "Azure DevOps & Pipelines",
            "slug": "azure-devops-pipelines",
            "difficulty": "medium",
            "estimated_minutes": 60,
            "xp_reward": 125,
            "content": """# Azure DevOps & Pipelines

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Azure DevOps ar viktigt |
|----------|-------------------------------|
| **CI/CD** | Komplett pipeline-losning |
| **Repos** | Git hosting med PR-workflows |
| **Boards** | Agile project management |
| **Artifacts** | Package management |
| **Test Plans** | Test management |

Som DevOps-ingenjor maste du forsta:

- **YAML pipelines** sa du kan versionskontrollera CI/CD
- **Service connections** sa du kan deploya till Azure
- **Environments** sa du har kontroll over deployments

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure DevOps Oversikt

```
┌─────────────────────────────────────────────────────────────┐
│                   AZURE DEVOPS                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ORGANIZATION (dev.azure.com/myorg)                  │   │
│  │                                                      │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │  PROJECT (webapp)                            │   │   │
│  │  │                                              │   │   │
│  │  │  ┌──────────┐ ┌──────────┐ ┌──────────┐   │   │   │
│  │  │  │  Repos   │ │ Pipelines│ │  Boards  │   │   │   │
│  │  │  │   Git    │ │   CI/CD  │ │  Kanban  │   │   │   │
│  │  │  └──────────┘ └──────────┘ └──────────┘   │   │   │
│  │  │                                              │   │   │
│  │  │  ┌──────────┐ ┌──────────┐                 │   │   │
│  │  │  │Artifacts │ │Test Plans│                 │   │   │
│  │  │  │ NuGet,npm│ │  QA      │                 │   │   │
│  │  │  └──────────┘ └──────────┘                 │   │   │
│  │  │                                              │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## YAML Pipeline Basics

### Enkel CI Pipeline

```yaml
# azure-pipelines.yml
trigger:
  - main
  - develop

pool:
  vmImage: 'ubuntu-latest'

variables:
  pythonVersion: '3.11'

stages:
  - stage: Build
    jobs:
      - job: BuildJob
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: '$(pythonVersion)'

          - script: |
              python -m pip install --upgrade pip
              pip install -r requirements.txt
            displayName: 'Install dependencies'

          - script: |
              pip install pytest pytest-cov
              pytest --cov=src --cov-report=xml
            displayName: 'Run tests'

          - task: PublishCodeCoverageResults@1
            inputs:
              codeCoverageTool: Cobertura
              summaryFileLocation: 'coverage.xml'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Multi-Stage Pipeline

```yaml
trigger:
  - main

variables:
  - group: webapp-secrets  # Variable group
  - name: imageRepository
    value: 'webapp'
  - name: dockerfilePath
    value: 'Dockerfile'

stages:
  # ========================================
  # BUILD STAGE
  # ========================================
  - stage: Build
    jobs:
      - job: BuildAndPush
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: Docker@2
            displayName: 'Build and push image'
            inputs:
              containerRegistry: 'acr-connection'
              repository: '$(imageRepository)'
              command: 'buildAndPush'
              Dockerfile: '$(dockerfilePath)'
              tags: |
                $(Build.BuildId)
                latest

  # ========================================
  # DEPLOY TO STAGING
  # ========================================
  - stage: DeployStaging
    dependsOn: Build
    condition: succeeded()
    jobs:
      - deployment: DeployStaging
        environment: 'staging'
        pool:
          vmImage: 'ubuntu-latest'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebAppContainer@1
                  inputs:
                    azureSubscription: 'azure-connection'
                    appName: 'app-api-staging'
                    containers: 'myacr.azurecr.io/$(imageRepository):$(Build.BuildId)'

  # ========================================
  # DEPLOY TO PRODUCTION
  # ========================================
  - stage: DeployProduction
    dependsOn: DeployStaging
    condition: succeeded()
    jobs:
      - deployment: DeployProduction
        environment: 'production'  # Krav pa approval
        pool:
          vmImage: 'ubuntu-latest'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebAppContainer@1
                  inputs:
                    azureSubscription: 'azure-connection'
                    appName: 'app-api-prod'
                    containers: 'myacr.azurecr.io/$(imageRepository):$(Build.BuildId)'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Service Connections

Service connections kopplar Azure DevOps till Azure:

```
┌─────────────────────────────────────────────────────────────┐
│              SERVICE CONNECTIONS                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Project Settings > Service connections                    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  azure-connection                                    │   │
│  │  Type: Azure Resource Manager                        │   │
│  │  Scope: Subscription (Production)                    │   │
│  │  Auth: Service Principal (auto)                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  acr-connection                                      │   │
│  │  Type: Docker Registry                               │   │
│  │  Registry: myacr.azurecr.io                         │   │
│  │  Auth: Service Principal                            │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Environments & Approvals

```yaml
# Deployment med environment
- stage: DeployProduction
  jobs:
    - deployment: Deploy
      environment: 'production'  # Mappar till Environment i DevOps
      strategy:
        runOnce:
          deploy:
            steps:
              - script: echo "Deploying to production"
```

### Konfigurera Approvals i UI:
1. Pipelines > Environments > production
2. More actions > Approvals and checks
3. Add check > Approvals
4. Valj approvers

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Variable Groups & Secrets

```yaml
# Anvand variable group
variables:
  - group: 'webapp-prod-secrets'  # Defineras i Library
  - name: environment
    value: 'production'

steps:
  - script: |
      echo "Deploying to $(environment)"
      # $(DATABASE_URL) fran variable group
    env:
      DATABASE_URL: $(DATABASE_URL)  # Secret mappas
```

### Key Vault-integration

```yaml
variables:
  - group: 'keyvault-secrets'  # Linkad till Key Vault

# Eller direkt i pipeline:
steps:
  - task: AzureKeyVault@2
    inputs:
      azureSubscription: 'azure-connection'
      KeyVaultName: 'kv-webapp-prod'
      SecretsFilter: 'DATABASE-URL,API-KEY'
      RunAsPreJob: true
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Templates

### Ateranvandbara templates

```yaml
# templates/build-docker.yml
parameters:
  - name: imageName
    type: string
  - name: dockerfile
    type: string
    default: 'Dockerfile'

steps:
  - task: Docker@2
    inputs:
      containerRegistry: 'acr-connection'
      repository: '${{ parameters.imageName }}'
      command: 'buildAndPush'
      Dockerfile: '${{ parameters.dockerfile }}'
      tags: |
        $(Build.BuildId)
        latest
```

```yaml
# azure-pipelines.yml - Anvand template
stages:
  - stage: Build
    jobs:
      - job: BuildAPI
        steps:
          - template: templates/build-docker.yml
            parameters:
              imageName: 'api'
              dockerfile: 'apps/api/Dockerfile'

      - job: BuildWorker
        steps:
          - template: templates/build-docker.yml
            parameters:
              imageName: 'worker'
              dockerfile: 'apps/worker/Dockerfile'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Self-Hosted Agents

```bash
# Installera agent pa VM
mkdir myagent && cd myagent
curl -O https://vstsagentpackage.azureedge.net/agent/3.230.0/vsts-agent-linux-x64-3.230.0.tar.gz
tar zxvf vsts-agent-linux-x64-3.230.0.tar.gz

# Konfigurera
./config.sh \\
  --url https://dev.azure.com/myorg \\
  --auth pat \\
  --token <PAT> \\
  --pool mypool \\
  --agent myagent \\
  --work _work

# Kor som service
sudo ./svc.sh install
sudo ./svc.sh start
```

```yaml
# Anvand self-hosted pool
pool:
  name: 'mypool'
  demands:
    - docker
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `No hosted parallelism` | Free tier limit | Beggar free grant eller kok |
| `Service connection failed` | Permissions | Kolla SP-rattigheter |
| `Agent offline` | Agent ner | Starta om agent |
| `Variable not found` | Fel scope | Kolla variable group linking |
| `Deployment blocked` | Approval pending | Godkann i Environments |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **YAML** | Versionskontrollera pipelines |
| **Stages** | Build > Test > Deploy (Staging > Prod) |
| **Environments** | Approvals och gates |
| **Service Connections** | Koppla till Azure |
| **Templates** | Ateranvand pipeline-kod |

**Kom ihag:**
- YAML ar standard - undvik Classic pipelines
- Anvand environments for deployment-kontroll
- Variable groups for delade hemligheter
- Templates for DRY (Don't Repeat Yourself)
- Self-hosted agents for speciella krav
"""
        },
        # =====================================================================
        # NODE 14: Azure Container Registry (ACR)
        # =====================================================================
        {
            "title": "Azure Container Registry (ACR)",
            "slug": "azure-container-registry",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 100,
            "content": """# Azure Container Registry (ACR)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor ACR ar viktigt |
|----------|----------------------|
| **Container hosting** | Azure-native registry |
| **CI/CD** | Integrerar med Pipelines |
| **AKS** | Direkt integration |
| **Geo-replikering** | Global distribution |
| **Security** | Private endpoint support |

Som DevOps-ingenjor maste du forsta:

- **SKU-val** sa du valjer ratt kapacitet
- **ACR Tasks** sa du kan bygga i molnet
- **Authentication** sa du kan pusha/pulla sakernt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ACR Arkitektur

```
┌─────────────────────────────────────────────────────────────┐
│              AZURE CONTAINER REGISTRY                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  myacr.azurecr.io                                   │   │
│  │                                                      │   │
│  │  Repositories:                                       │   │
│  │  ├── webapp/api          (v1.0, v1.1, latest)       │   │
│  │  ├── webapp/frontend     (v1.0, latest)             │   │
│  │  ├── webapp/worker       (v1.0, v1.1, v1.2)        │   │
│  │  └── base/python         (3.11, 3.12)               │   │
│  │                                                      │   │
│  │  ┌─────────────────┐ ┌─────────────────┐           │   │
│  │  │  Geo-Replicas   │ │    Webhooks     │           │   │
│  │  │  westeurope     │ │  on push: CD    │           │   │
│  │  │  eastus         │ │  on delete      │           │   │
│  │  └─────────────────┘ └─────────────────┘           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Authentication:                                            │
│  ├── Admin user (ej rekommenderat)                         │
│  ├── Service Principal                                      │
│  ├── Managed Identity                                       │
│  └── Token (repository-scoped)                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## SKU-jamforelse

| Feature | Basic | Standard | Premium |
|---------|-------|----------|---------|
| **Storage** | 10 GB | 100 GB | 500 GB |
| **Throughput** | Low | Medium | High |
| **Geo-replication** | Nej | Nej | Ja |
| **Private Link** | Nej | Nej | Ja |
| **Content Trust** | Nej | Nej | Ja |
| **Pris** | ca 5 USD/man | ca 20 USD/man | ca 50 USD/man |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa och Konfigurera ACR

### Med Azure CLI

```bash
# Skapa ACR
az acr create \\
  --resource-group rg-webapp-prod \\
  --name myacr \\
  --sku Premium \\
  --location westeurope \\
  --admin-enabled false

# Visa login server
az acr show --name myacr --query loginServer -o tsv
# Output: myacr.azurecr.io

# Aktivera geo-replikering (Premium)
az acr replication create \\
  --registry myacr \\
  --location eastus

# Lista replicas
az acr replication list --registry myacr -o table
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Authentication

### 1. Azure CLI Login

```bash
# Logga in med Azure AD
az acr login --name myacr

# Bakom kulisserna:
# 1. Az CLI hamtar OAuth token
# 2. Token skickas till Docker config
```

### 2. Service Principal

```bash
# Skapa Service Principal med pull-access
ACR_ID=$(az acr show --name myacr --query id -o tsv)

az ad sp create-for-rbac \\
  --name sp-acr-pull \\
  --scopes $ACR_ID \\
  --role acrpull

# Output:
# {
#   "appId": "xxxx-xxxx-xxxx",
#   "password": "secret",
#   "tenant": "yyyy-yyyy-yyyy"
# }

# Anvand i Docker login
docker login myacr.azurecr.io \\
  --username <appId> \\
  --password <password>
```

### 3. Managed Identity (AKS)

```bash
# AKS med managed identity till ACR
az aks update \\
  --resource-group rg-webapp-prod \\
  --name aks-webapp \\
  --attach-acr myacr

# Verifierar att AKS kubelet identity har AcrPull
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Push och Pull Images

### Bygga och Pusha

```bash
# Bygg lokalt
docker build -t myapp:v1.0 .

# Tagga for ACR
docker tag myapp:v1.0 myacr.azurecr.io/webapp/api:v1.0
docker tag myapp:v1.0 myacr.azurecr.io/webapp/api:latest

# Pusha till ACR
docker push myacr.azurecr.io/webapp/api:v1.0
docker push myacr.azurecr.io/webapp/api:latest
```

### Lista Images

```bash
# Lista repositories
az acr repository list --name myacr -o table

# Lista tags for en repository
az acr repository show-tags \\
  --name myacr \\
  --repository webapp/api \\
  -o table

# Visa manifest
az acr manifest list-metadata \\
  --registry myacr \\
  --name webapp/api
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ACR Tasks - Cloud Build

```bash
# Snabb build i molnet
az acr build \\
  --registry myacr \\
  --image webapp/api:v1.0 \\
  --file Dockerfile \\
  .

# Multi-arch build
az acr build \\
  --registry myacr \\
  --image webapp/api:v1.0 \\
  --platform linux/amd64,linux/arm64 \\
  .
```

### Task med Trigger

```yaml
# acr-task.yaml
version: v1.1.0
steps:
  - build: -t {{.Run.Registry}}/webapp/api:{{.Run.ID}} -f Dockerfile .
  - push: ["{{.Run.Registry}}/webapp/api:{{.Run.ID}}"]
```

```bash
# Skapa task med Git trigger
az acr task create \\
  --registry myacr \\
  --name build-api \\
  --image webapp/api:{{.Run.ID}} \\
  --context https://github.com/myorg/webapp.git \\
  --file Dockerfile \\
  --git-access-token <PAT> \\
  --commit-trigger-enabled true

# Lista task runs
az acr task list-runs --registry myacr -o table
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure DevOps Integration

```yaml
# azure-pipelines.yml
trigger:
  - main

variables:
  acrName: 'myacr'
  imageName: 'webapp/api'

stages:
  - stage: Build
    jobs:
      - job: BuildAndPush
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: Docker@2
            displayName: 'Build and push to ACR'
            inputs:
              containerRegistry: 'acr-service-connection'
              repository: '$(imageName)'
              command: 'buildAndPush'
              Dockerfile: 'Dockerfile'
              tags: |
                $(Build.BuildId)
                latest
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Security Best Practices

### Private Endpoint (Premium)

```bash
# Skapa Private Endpoint
az network private-endpoint create \\
  --name pe-acr \\
  --resource-group rg-webapp-prod \\
  --vnet-name vnet-webapp \\
  --subnet subnet-private-endpoints \\
  --private-connection-resource-id $(az acr show --name myacr --query id -o tsv) \\
  --group-id registry \\
  --connection-name acr-connection

# Inaktivera public access
az acr update --name myacr --public-network-enabled false
```

### Image Scanning

```bash
# Microsoft Defender for Containers skannar automatiskt
# Se resultat:
az acr repository show \\
  --name myacr \\
  --repository webapp/api \\
  --detail
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Image Cleanup

```bash
# Ta bort gamla tags
az acr repository delete \\
  --name myacr \\
  --image webapp/api:old-tag \\
  --yes

# Purge policy (behall senaste 10)
az acr run \\
  --cmd "acr purge --filter 'webapp/api:.*' --ago 30d --keep 10" \\
  --registry myacr \\
  /dev/null

# Schedule cleanup task
az acr task create \\
  --name cleanup \\
  --registry myacr \\
  --cmd "acr purge --filter 'webapp/*:.*' --ago 30d --keep 5" \\
  --schedule "0 0 * * *" \\
  --context /dev/null
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - ACR Kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `az acr login` | Logga in till ACR |
| `az acr build` | Bygg image i molnet |
| `az acr repository list` | Lista repos |
| `az acr repository show-tags` | Lista tags |
| `az acr task create` | Skapa build task |
| `az acr task run` | Kor task manuellt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `unauthorized: authentication required` | Ej inloggad | `az acr login --name myacr` |
| `denied: requested access denied` | Fel permissions | Kolla RBAC-roll |
| `context deadline exceeded` | Image for stor | Oka timeout eller minska image |
| `manifest unknown` | Tag finns ej | Kolla tag-namn |
| `quota exceeded` | Storage fullt | Rensa gamla images |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Premium** | For geo-rep och private link |
| **Managed Identity** | Basta auth for AKS |
| **ACR Tasks** | Bygg i molnet utan lokal Docker |
| **Purge** | Automatisk cleanup av gamla images |
| **Private Endpoint** | Sakerhet i produktion |

**Kom ihag:**
- Undvik admin user - anvand Service Principal eller MI
- Premium SKU for enterprise (geo-rep, private link)
- ACR Tasks for CI utan self-hosted runners
- Schemalagd cleanup for att spara lagring
- Attach ACR till AKS med managed identity
"""
        },
        # =====================================================================
        # NODE 15: Infrastructure as Code - Bicep
        # =====================================================================
        {
            "title": "Infrastructure as Code - Bicep",
            "slug": "iac-bicep",
            "difficulty": "hard",
            "estimated_minutes": 65,
            "xp_reward": 150,
            "content": """# Infrastructure as Code - Bicep

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Bicep ar viktigt |
|----------|------------------------|
| **IaC** | Deklarativ Azure-infrastruktur |
| **ARM-ersattare** | Enklare an ARM JSON |
| **Moduler** | Atervandbara komponenter |
| **Type-safe** | Validering i editorn |
| **Native** | Forsta-klass Azure-stod |

Som DevOps-ingenjor maste du forsta:

- **Bicep-syntax** sa du kan skriva Azure IaC
- **Moduler** sa du strukturerar stora deployments
- **Parameters** sa du kan ateranvanda over miljoer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Bicep vs ARM vs Terraform

```
┌─────────────────────────────────────────────────────────────┐
│                    IAC-JAMFORELSE                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ARM Template (JSON)                                 │   │
│  │  - Verbose, svar att lasa                           │   │
│  │  - Ingen modulstod                                  │   │
│  │  - Azure-native                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                    │                                        │
│                    ▼ Kompilerar till                       │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Bicep                                               │   │
│  │  + Ren, lasbar syntax                               │   │
│  │  + Moduler och loops                                │   │
│  │  + Type-checking                                     │   │
│  │  + Azure-native (Microsoft)                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Terraform (HCL)                                     │   │
│  │  + Multi-cloud                                       │   │
│  │  + Stor community                                    │   │
│  │  - Separat state-hantering                          │   │
│  │  - Provider-lag for nya features                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Bicep Grundlaggande Syntax

### Enkel resurs

```bicep
// main.bicep

// Parameters
param location string = resourceGroup().location
param environment string = 'prod'
param appName string

// Variables
var storageAccountName = 'st${appName}${environment}'

// Resource: Storage Account
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
    supportsHttpsTrafficOnly: true
  }

  // Nested resource
  resource blobService 'blobServices' = {
    name: 'default'
    resource container 'containers' = {
      name: 'data'
      properties: {
        publicAccess: 'None'
      }
    }
  }
}

// Outputs
output storageAccountId string = storageAccount.id
output blobEndpoint string = storageAccount.properties.primaryEndpoints.blob
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Deploying Bicep

### Med Azure CLI

```bash
# Deploya till resource group
az deployment group create \\
  --resource-group rg-webapp-prod \\
  --template-file main.bicep \\
  --parameters appName=webapp environment=prod

# Deploya till subscription
az deployment sub create \\
  --location westeurope \\
  --template-file main.bicep \\
  --parameters @parameters.prod.json

# What-if (dry run)
az deployment group what-if \\
  --resource-group rg-webapp-prod \\
  --template-file main.bicep \\
  --parameters appName=webapp
```

### Parameter-fil

```json
// parameters.prod.json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "appName": {
      "value": "webapp"
    },
    "environment": {
      "value": "prod"
    },
    "skuName": {
      "value": "P1v3"
    }
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Moduler

### Strukturera med moduler

```
infra/
├── main.bicep
├── parameters.prod.json
├── parameters.staging.json
└── modules/
    ├── storage.bicep
    ├── appservice.bicep
    ├── database.bicep
    └── keyvault.bicep
```

### Module: storage.bicep

```bicep
// modules/storage.bicep
param location string
param name string
param sku string = 'Standard_LRS'

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: name
  location: location
  sku: {
    name: sku
  }
  kind: 'StorageV2'
  properties: {
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
  }
}

output id string = storageAccount.id
output name string = storageAccount.name
output primaryEndpoint string = storageAccount.properties.primaryEndpoints.blob
```

### Main som anvandar moduler

```bicep
// main.bicep
param location string = resourceGroup().location
param environment string
param appName string

// Deploy storage via module
module storage 'modules/storage.bicep' = {
  name: 'storageDeployment'
  params: {
    location: location
    name: 'st${appName}${environment}'
    sku: environment == 'prod' ? 'Standard_GRS' : 'Standard_LRS'
  }
}

// Deploy App Service via module
module appService 'modules/appservice.bicep' = {
  name: 'appServiceDeployment'
  params: {
    location: location
    appName: appName
    environment: environment
    storageAccountName: storage.outputs.name  // Reference output
  }
}

output storageEndpoint string = storage.outputs.primaryEndpoint
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Loops och Conditions

### Loops

```bicep
// Array parameter
param storageAccounts array = [
  { name: 'logs', sku: 'Standard_LRS' }
  { name: 'data', sku: 'Standard_GRS' }
  { name: 'backups', sku: 'Standard_GRS' }
]

// Loop over array
resource storage 'Microsoft.Storage/storageAccounts@2023-01-01' = [for account in storageAccounts: {
  name: 'st${account.name}${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: account.sku
  }
  kind: 'StorageV2'
}]

// Index-based loop
resource containers 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = [for (name, i) in containerNames: {
  name: '${storageAccount.name}/default/${name}'
  properties: {
    publicAccess: 'None'
  }
}]
```

### Conditions

```bicep
param deployRedis bool = false
param environment string

// Conditional deployment
resource redis 'Microsoft.Cache/redis@2023-04-01' = if (deployRedis) {
  name: 'redis-${environment}'
  location: location
  properties: {
    sku: {
      name: 'Standard'
      family: 'C'
      capacity: 1
    }
  }
}

// Conditional property
resource appService 'Microsoft.Web/sites@2022-09-01' = {
  name: 'app-${environment}'
  location: location
  properties: {
    httpsOnly: true
    siteConfig: {
      alwaysOn: environment == 'prod' ? true : false
      minTlsVersion: '1.2'
    }
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Komplett Exempel - Web App med SQL

```bicep
// main.bicep - Full web application stack
@description('Application name')
param appName string

@description('Environment')
@allowed(['dev', 'staging', 'prod'])
param environment string

@description('Location')
param location string = resourceGroup().location

@secure()
@description('SQL Admin Password')
param sqlAdminPassword string

// Variables
var appServicePlanName = 'asp-${appName}-${environment}'
var webAppName = 'app-${appName}-${environment}'
var sqlServerName = 'sql-${appName}-${environment}'
var sqlDbName = 'sqldb-${appName}'

// App Service Plan
resource appServicePlan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: environment == 'prod' ? 'P1v3' : 'B1'
    tier: environment == 'prod' ? 'PremiumV3' : 'Basic'
  }
  kind: 'linux'
  properties: {
    reserved: true
  }
}

// Web App
resource webApp 'Microsoft.Web/sites@2022-09-01' = {
  name: webAppName
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    httpsOnly: true
    siteConfig: {
      linuxFxVersion: 'PYTHON|3.11'
      alwaysOn: environment == 'prod'
      minTlsVersion: '1.2'
      appSettings: [
        {
          name: 'DATABASE_URL'
          value: 'Server=${sqlServer.properties.fullyQualifiedDomainName};Database=${sqlDbName};'
        }
        {
          name: 'ENVIRONMENT'
          value: environment
        }
      ]
    }
  }
}

// SQL Server
resource sqlServer 'Microsoft.Sql/servers@2022-05-01-preview' = {
  name: sqlServerName
  location: location
  properties: {
    administratorLogin: 'sqladmin'
    administratorLoginPassword: sqlAdminPassword
    minimalTlsVersion: '1.2'
  }
}

// SQL Database
resource sqlDb 'Microsoft.Sql/servers/databases@2022-05-01-preview' = {
  parent: sqlServer
  name: sqlDbName
  location: location
  sku: {
    name: environment == 'prod' ? 'S2' : 'Basic'
    tier: environment == 'prod' ? 'Standard' : 'Basic'
  }
}

// Allow Azure services
resource sqlFirewall 'Microsoft.Sql/servers/firewallRules@2022-05-01-preview' = {
  parent: sqlServer
  name: 'AllowAzureServices'
  properties: {
    startIpAddress: '0.0.0.0'
    endIpAddress: '0.0.0.0'
  }
}

// Outputs
output webAppUrl string = 'https://${webApp.properties.defaultHostName}'
output sqlServerFqdn string = sqlServer.properties.fullyQualifiedDomainName
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CI/CD Pipeline med Bicep

```yaml
# azure-pipelines.yml
trigger:
  paths:
    include:
      - infra/**

variables:
  - group: azure-credentials
  - name: resourceGroup
    value: 'rg-webapp-$(environment)'

stages:
  - stage: Validate
    jobs:
      - job: ValidateBicep
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: AzureCLI@2
            displayName: 'Validate Bicep'
            inputs:
              azureSubscription: 'azure-connection'
              scriptType: 'bash'
              scriptLocation: 'inlineScript'
              inlineScript: |
                az bicep build --file infra/main.bicep
                az deployment group validate \\
                  --resource-group $(resourceGroup) \\
                  --template-file infra/main.bicep \\
                  --parameters @infra/parameters.$(environment).json

  - stage: Preview
    jobs:
      - job: WhatIf
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: AzureCLI@2
            displayName: 'What-If Preview'
            inputs:
              azureSubscription: 'azure-connection'
              scriptType: 'bash'
              scriptLocation: 'inlineScript'
              inlineScript: |
                az deployment group what-if \\
                  --resource-group $(resourceGroup) \\
                  --template-file infra/main.bicep \\
                  --parameters @infra/parameters.$(environment).json

  - stage: Deploy
    jobs:
      - deployment: DeployInfra
        environment: '$(environment)'
        pool:
          vmImage: 'ubuntu-latest'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureCLI@2
                  displayName: 'Deploy Bicep'
                  inputs:
                    azureSubscription: 'azure-connection'
                    scriptType: 'bash'
                    scriptLocation: 'inlineScript'
                    inlineScript: |
                      az deployment group create \\
                        --resource-group $(resourceGroup) \\
                        --template-file infra/main.bicep \\
                        --parameters @infra/parameters.$(environment).json
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Bicep CLI Kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `az bicep build -f main.bicep` | Kompilera till ARM |
| `az bicep decompile -f template.json` | Konvertera ARM till Bicep |
| `az bicep format -f main.bicep` | Formatera Bicep-fil |
| `az bicep lint -f main.bicep` | Linta for fel |
| `az bicep version` | Visa Bicep-version |
| `az bicep upgrade` | Uppgradera Bicep |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `Resource type not found` | Fel API-version | Uppdatera @version |
| `Duplicate resource` | Samma namn | Anvand uniqueString() |
| `Circular dependency` | Moduler refererar varandra | Omstrukturera |
| `Parameter missing` | Obligatorisk param | Lagg till i parameters-fil |
| `What-if shows delete` | Resurser utanfor template | Anvand complete mode forsiktigt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Bicep > ARM** | Mycket enklare syntax |
| **Moduler** | Dela upp och ateranvand |
| **What-if** | Alltid forhandsvisa |
| **Parameters** | Separata filer per miljo |
| **Native** | Inget state att hantera |

**Kom ihag:**
- Bicep kompilerar till ARM - Azure-native
- Moduler for struktur och ateranvandning
- What-if i pipelines fore deploy
- Versionskontrollera all infrastruktur
- Bicep VS Code extension for IntelliSense
"""
        },
        # =====================================================================
        # NODE 16: Azure Pipelines Advanced
        # =====================================================================
        {
            "title": "Azure Pipelines Advanced",
            "slug": "azure-pipelines-advanced",
            "difficulty": "hard",
            "estimated_minutes": 65,
            "xp_reward": 150,
            "content": """# Azure Pipelines Advanced

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Advanced Pipelines ar viktigt |
|----------|-------------------------------------|
| **Komplexa deployments** | Multi-stage, multi-environment |
| **Sakerhet** | Gates, approvals, compliance |
| **Skalbarhet** | Matrix builds, parallelism |
| **Integration** | Third-party services |
| **Enterprise** | Governance och audit |

Som DevOps-ingenjor maste du forsta:

- **Deployment strategies** sa du kan rulla ut sakert
- **Gates & Checks** sa du uppfyller compliance
- **Matrix builds** sa du testar pa flera plattformar

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Deployment Strategies

```
┌─────────────────────────────────────────────────────────────┐
│              DEPLOYMENT STRATEGIES                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  RunOnce              Rolling               Canary          │
│  ┌─────┐             ┌─────┐              ┌─────┐          │
│  │ 100%│             │ 25% │──┐           │ 10% │          │
│  │ NEW │             │ NEW │  │           │ NEW │          │
│  └─────┘             └─────┘  │           └─────┘          │
│     │                   │     │              │              │
│     ▼                   ▼     ▼              ▼              │
│  Alla                 25%   50%   75%     Monitor          │
│  samtidigt            │      │      │     metriker         │
│                       ▼      ▼      ▼        │              │
│                     Gradvis utrullning    ┌──┴──┐          │
│                                           OK?  Nej         │
│                                           │     │          │
│                                        100%  Rollback      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Rolling Deployment

```yaml
stages:
  - stage: DeployProduction
    jobs:
      - deployment: DeployWeb
        environment: 'production'
        pool:
          vmImage: 'ubuntu-latest'
        strategy:
          rolling:
            maxParallel: 2  # 2 targets at a time
            preDeploy:
              steps:
                - script: echo "Preparing deployment"
                  displayName: 'Pre-deploy checks'
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: 'azure-connection'
                    appName: '$(webAppName)'
                    package: '$(Pipeline.Workspace)/drop/*.zip'
            routeTraffic:
              steps:
                - script: echo "Routing traffic"
                  displayName: 'Route traffic'
            postRouteTraffic:
              steps:
                - script: |
                    # Smoke tests
                    curl -f https://$(webAppName).azurewebsites.net/health
                  displayName: 'Health check'
            on:
              failure:
                steps:
                  - script: echo "Deployment failed - initiating rollback"
                    displayName: 'Rollback notification'
              success:
                steps:
                  - script: echo "Deployment successful"
                    displayName: 'Success notification'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Canary Deployment

```yaml
stages:
  - stage: CanaryDeploy
    jobs:
      - deployment: DeployCanary
        environment: 'production'
        strategy:
          canary:
            increments: [10, 25, 50]  # Gradvis okning
            preDeploy:
              steps:
                - script: echo "Deploying to $(strategy.increment)% of targets"
            deploy:
              steps:
                - task: AzureAppServiceSettings@1
                  inputs:
                    azureSubscription: 'azure-connection'
                    appName: '$(webAppName)'
                    resourceGroupName: '$(resourceGroup)'
                    slotName: 'canary'
            routeTraffic:
              steps:
                - task: AzureAppServiceManage@0
                  inputs:
                    azureSubscription: 'azure-connection'
                    action: 'Start Azure App Service'
                    WebAppName: '$(webAppName)'
                    SpecifySlotOrASE: true
                    ResourceGroupName: '$(resourceGroup)'
                    Slot: 'canary'
            postRouteTraffic:
              steps:
                - task: AzureCLI@2
                  displayName: 'Monitor Canary Metrics'
                  inputs:
                    azureSubscription: 'azure-connection'
                    scriptType: 'bash'
                    scriptLocation: 'inlineScript'
                    inlineScript: |
                      # Vanta och kontrollera metrics
                      sleep 300  # 5 min
                      # Hamta error rate fran App Insights
                      ERROR_RATE=$(az monitor app-insights query \\
                        --app $(appInsightsName) \\
                        --analytics-query "requests | where success == false | count" \\
                        --query "tables[0].rows[0][0]" -o tsv)

                      if [ "$ERROR_RATE" -gt 5 ]; then
                        echo "##vso[task.complete result=Failed;]High error rate detected"
                        exit 1
                      fi
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Matrix Builds

```yaml
# Testa pa flera versioner/plattformar
stages:
  - stage: Test
    jobs:
      - job: TestMatrix
        strategy:
          matrix:
            Python39_Ubuntu:
              pythonVersion: '3.9'
              vmImage: 'ubuntu-latest'
            Python310_Ubuntu:
              pythonVersion: '3.10'
              vmImage: 'ubuntu-latest'
            Python311_Ubuntu:
              pythonVersion: '3.11'
              vmImage: 'ubuntu-latest'
            Python311_Windows:
              pythonVersion: '3.11'
              vmImage: 'windows-latest'
          maxParallel: 4

        pool:
          vmImage: $(vmImage)

        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: '$(pythonVersion)'

          - script: |
              python -m pip install -r requirements.txt
              pytest tests/ -v --junitxml=results.xml
            displayName: 'Run tests on $(pythonVersion) - $(vmImage)'

          - task: PublishTestResults@2
            inputs:
              testResultsFormat: 'JUnit'
              testResultsFiles: 'results.xml'
              testRunTitle: 'Python $(pythonVersion) - $(vmImage)'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Environment Gates & Checks

### Approval Gates

```yaml
# I Azure DevOps UI: Environments > production > Approvals and checks

# Pipeline refererar environment
- stage: Production
  jobs:
    - deployment: Deploy
      environment: 'production'  # Krav pa approval
```

### Business Hours Gate

```yaml
# Konfigurera i UI:
# Environments > production > Approvals and checks > Business Hours

# Tillater deploy endast:
# - Mandag-Fredag
# - 09:00 - 17:00 (lokal tid)
# - Exkluderar helgdagar
```

### Azure Monitor Gate

```yaml
# Invoke Azure Function gate
# Konfigurera i UI med:
# - Function URL
# - Function Key
# - Success criteria
```

### Manual Validation

```yaml
stages:
  - stage: PreProduction
    jobs:
      - job: ManualValidation
        pool: server  # Agentless job
        steps:
          - task: ManualValidation@0
            inputs:
              notifyUsers: 'devops-team@company.com'
              instructions: |
                Validera staging-miljon:
                - Kolla https://staging.app.com
                - Verifiera nya features
                - Kontrollera logs
              onTimeout: 'reject'
              timeoutInMinutes: 1440  # 24 timmar
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Conditional Execution

```yaml
stages:
  - stage: Build
    jobs:
      - job: BuildApp
        steps:
          - script: echo "Building..."

  # Deploya staging endast pa develop
  - stage: DeployStaging
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/develop'))
    jobs:
      - deployment: Deploy
        environment: 'staging'

  # Deploya prod endast pa main + manuell trigger
  - stage: DeployProduction
    condition: |
      and(
        succeeded(),
        eq(variables['Build.SourceBranch'], 'refs/heads/main'),
        eq(variables['Build.Reason'], 'Manual')
      )
    jobs:
      - deployment: Deploy
        environment: 'production'

  # Alltid kor cleanup, aven vid failure
  - stage: Cleanup
    condition: always()
    jobs:
      - job: CleanupResources
        steps:
          - script: echo "Cleaning up..."
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Reusable Templates

### Extends Template

```yaml
# templates/pipeline-template.yml
parameters:
  - name: environment
    type: string
  - name: dependsOn
    type: object
    default: []

stages:
  - stage: Deploy_${{ parameters.environment }}
    dependsOn: ${{ parameters.dependsOn }}
    jobs:
      - deployment: Deploy
        environment: ${{ parameters.environment }}
        strategy:
          runOnce:
            deploy:
              steps:
                - template: steps/deploy-steps.yml
                  parameters:
                    environment: ${{ parameters.environment }}
```

```yaml
# azure-pipelines.yml
trigger:
  - main

extends:
  template: templates/pipeline-base.yml
  parameters:
    buildConfiguration: 'Release'
    runTests: true
    environments:
      - name: 'staging'
        dependsOn: Build
      - name: 'production'
        dependsOn: staging
```

### Step Templates

```yaml
# templates/steps/deploy-steps.yml
parameters:
  - name: environment
    type: string

steps:
  - task: AzureCLI@2
    displayName: 'Deploy to ${{ parameters.environment }}'
    inputs:
      azureSubscription: 'azure-${{ parameters.environment }}'
      scriptType: 'bash'
      scriptLocation: 'inlineScript'
      inlineScript: |
        az webapp deployment source config-zip \\
          --resource-group rg-app-${{ parameters.environment }} \\
          --name app-${{ parameters.environment }} \\
          --src $(Pipeline.Workspace)/drop/app.zip

  - script: |
      curl -f https://app-${{ parameters.environment }}.azurewebsites.net/health
    displayName: 'Health Check'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pipeline Caching

```yaml
variables:
  npm_config_cache: $(Pipeline.Workspace)/.npm
  pip_cache_dir: $(Pipeline.Workspace)/.pip

steps:
  # NPM Cache
  - task: Cache@2
    inputs:
      key: 'npm | "$(Agent.OS)" | package-lock.json'
      restoreKeys: |
        npm | "$(Agent.OS)"
      path: $(npm_config_cache)
    displayName: 'Cache npm'

  # Pip Cache
  - task: Cache@2
    inputs:
      key: 'pip | "$(Agent.OS)" | requirements.txt'
      restoreKeys: |
        pip | "$(Agent.OS)"
      path: $(pip_cache_dir)
    displayName: 'Cache pip'

  # Docker Layer Cache
  - task: Cache@2
    inputs:
      key: 'docker | "$(Agent.OS)" | Dockerfile'
      path: $(Pipeline.Workspace)/docker-cache
      restoreKeys: |
        docker | "$(Agent.OS)"
    displayName: 'Cache Docker layers'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Service Hooks & Integrations

```yaml
# Slack notification
- task: SlackNotification@2
  inputs:
    connectionType: 'serviceEndpoint'
    serviceEndpoint: 'slack-webhook'
    message: |
      Deployment to $(environment) completed!
      Build: $(Build.BuildNumber)
      Status: $(Agent.JobStatus)

# Teams notification
- task: InvokeRESTAPI@1
  inputs:
    connectionType: 'connectedServiceName'
    serviceConnection: 'teams-webhook'
    method: 'POST'
    body: |
      {
        "@type": "MessageCard",
        "summary": "Deployment Status",
        "sections": [{
          "facts": [
            {"name": "Environment", "value": "$(environment)"},
            {"name": "Status", "value": "$(Agent.JobStatus)"}
          ]
        }]
      }

# GitHub Status
- task: GitHubComment@0
  inputs:
    gitHubConnection: 'github-connection'
    repositoryName: '$(Build.Repository.Name)'
    comment: 'Deployed to $(environment) successfully!'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `No agents in pool` | Alla upptagna/offline | Oka pool eller vanta |
| `Approval timeout` | Ingen godkande | Oka timeout eller notifiera |
| `Cache miss` | Key andrad | Kolla cache key |
| `Matrix too large` | For manga kombinationer | Begransa matrix |
| `Template not found` | Fel path | Kolla relativ sokvag |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Strategies** | Rolling/Canary for saker deploy |
| **Gates** | Automatic quality checks |
| **Matrix** | Parallell testning |
| **Templates** | DRY - ateranvand |
| **Caching** | Snabbare builds |

**Kom ihag:**
- Canary for kritiska produktions-deployments
- Gates for automatic compliance
- Matrix for cross-platform testing
- Templates for konsistens over team
- Cache dependencies for snabbare pipelines
"""
        },
        # =====================================================================
        # NODE 17: Entra ID & Identity Management
        # =====================================================================
        {
            "title": "Entra ID & Identity Management",
            "slug": "entra-id-identity",
            "difficulty": "hard",
            "estimated_minutes": 60,
            "xp_reward": 150,
            "content": """# Entra ID & Identity Management

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Entra ID ar viktigt |
|----------|---------------------------|
| **Authentication** | Centraliserad identitet |
| **Authorization** | RBAC for Azure-resurser |
| **SSO** | Single Sign-On for appar |
| **Managed Identity** | Passwordless for services |
| **Compliance** | Audit och governance |

Som DevOps-ingenjor maste du forsta:

- **Service Principals** sa appar kan autentisera
- **Managed Identity** sa du slipper hantera hemligheter
- **RBAC** sa du ger ratt access till ratt resurser

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Entra ID Oversikt

```
┌─────────────────────────────────────────────────────────────┐
│                    MICROSOFT ENTRA ID                       │
│              (tidigare Azure Active Directory)              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  TENANT (company.onmicrosoft.com)                   │   │
│  │                                                      │   │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │   │
│  │  │    Users     │ │    Groups    │ │ Applications │ │   │
│  │  │  john@co.se  │ │  DevOps-team │ │  webapp-api  │ │   │
│  │  │  jane@co.se  │ │  Developers  │ │  ci-pipeline │ │   │
│  │  └──────────────┘ └──────────────┘ └──────────────┘ │   │
│  │                                                      │   │
│  │  ┌──────────────┐ ┌──────────────┐                 │   │
│  │  │   Service    │ │   Managed    │                 │   │
│  │  │  Principals  │ │  Identities  │                 │   │
│  │  │  sp-deploy   │ │  mi-webapp   │                 │   │
│  │  └──────────────┘ └──────────────┘                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Service Principal

### Skapa Service Principal

```bash
# Skapa SP med Contributor pa subscription
az ad sp create-for-rbac \\
  --name sp-devops-deploy \\
  --role Contributor \\
  --scopes /subscriptions/<subscription-id>

# Output:
# {
#   "appId": "xxxx-xxxx-xxxx-xxxx",      # Client ID
#   "displayName": "sp-devops-deploy",
#   "password": "secret",                  # Client Secret
#   "tenant": "yyyy-yyyy-yyyy-yyyy"        # Tenant ID
# }

# Skapa med specifik scope
az ad sp create-for-rbac \\
  --name sp-webapp-deploy \\
  --role Contributor \\
  --scopes /subscriptions/<sub>/resourceGroups/rg-webapp-prod

# Lista SPs
az ad sp list --display-name sp-devops --output table
```

### Anvanda SP for login

```bash
# Login med SP (CI/CD)
az login --service-principal \\
  --username <appId> \\
  --password <password> \\
  --tenant <tenantId>

# Verifiera
az account show
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Managed Identity

```
┌─────────────────────────────────────────────────────────────┐
│              MANAGED IDENTITY FLOW                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐          ┌─────────────┐                  │
│  │   Web App   │          │   Entra ID  │                  │
│  │  (med MI)   │──Token──▶│             │                  │
│  └─────────────┘  request └─────────────┘                  │
│         │                        │                          │
│         │                        │ Token                    │
│         │                        ▼                          │
│         │              ┌─────────────────┐                 │
│         │              │  Access Token   │                 │
│         │              │  (1h giltig)    │                 │
│         │              └─────────────────┘                 │
│         │                        │                          │
│         ▼                        ▼                          │
│  ┌─────────────┐    Token  ┌─────────────┐                 │
│  │  Key Vault  │◀──────────│   Web App   │                 │
│  │  SQL DB     │           │             │                 │
│  │  Storage    │           │             │                 │
│  └─────────────┘           └─────────────┘                 │
│                                                             │
│  Inga credentials att hantera!                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### System-Assigned Managed Identity

```bash
# Aktivera pa Web App
az webapp identity assign \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod

# Output:
# {
#   "principalId": "xxxx-xxxx-xxxx",  # Object ID
#   "tenantId": "yyyy-yyyy-yyyy",
#   "type": "SystemAssigned"
# }

# Ge MI access till Key Vault
az keyvault set-policy \\
  --name kv-webapp-prod \\
  --object-id <principalId> \\
  --secret-permissions get list

# Ge MI access till Storage
az role assignment create \\
  --assignee <principalId> \\
  --role "Storage Blob Data Reader" \\
  --scope /subscriptions/<sub>/resourceGroups/rg-webapp-prod/providers/Microsoft.Storage/storageAccounts/stwebapp
```

### User-Assigned Managed Identity

```bash
# Skapa User-Assigned MI (kan delas mellan resurser)
az identity create \\
  --resource-group rg-webapp-prod \\
  --name mi-webapp-shared

# Tilldela till Web App
az webapp identity assign \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod \\
  --identities /subscriptions/<sub>/resourceGroups/rg-webapp-prod/providers/Microsoft.ManagedIdentity/userAssignedIdentities/mi-webapp-shared
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## RBAC - Role-Based Access Control

### Built-in Roles

| Roll | Beskrivning |
|------|-------------|
| **Owner** | Full access + kan tilldela roller |
| **Contributor** | Full access, ej rollhantering |
| **Reader** | Lasrattigheter |
| **User Access Admin** | Hantera anvandare |

### DevOps-relevanta roller

| Roll | Anvandning |
|------|------------|
| **AcrPush** | Push till Container Registry |
| **AcrPull** | Pull fran Container Registry |
| **Key Vault Secrets User** | Lasa secrets |
| **Storage Blob Data Contributor** | Skriva till Blob |
| **Website Contributor** | Hantera Web Apps |

### Tilldela roller

```bash
# Ge SP Contributor pa resource group
az role assignment create \\
  --assignee <appId-or-objectId> \\
  --role "Contributor" \\
  --scope /subscriptions/<sub>/resourceGroups/rg-webapp-prod

# Ge grupp Reader pa subscription
az role assignment create \\
  --assignee-object-id <group-object-id> \\
  --assignee-principal-type Group \\
  --role "Reader" \\
  --scope /subscriptions/<sub>

# Lista role assignments
az role assignment list \\
  --resource-group rg-webapp-prod \\
  --output table
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## App Registration

### Skapa App Registration for API

```bash
# Skapa app registration
az ad app create \\
  --display-name "WebApp API" \\
  --sign-in-audience AzureADMyOrg

# Lagg till API scope
az ad app update \\
  --id <app-id> \\
  --identifier-uris "api://webapp-api"

# Skapa client secret
az ad app credential reset \\
  --id <app-id> \\
  --display-name "CI/CD Secret" \\
  --years 1
```

### Python-kod med Managed Identity

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient

# DefaultAzureCredential provar (i ordning):
# 1. Environment variables
# 2. Managed Identity
# 3. Azure CLI
# 4. Azure PowerShell

credential = DefaultAzureCredential()

# Key Vault access
kv_url = "https://kv-webapp-prod.vault.azure.net/"
secret_client = SecretClient(vault_url=kv_url, credential=credential)
db_password = secret_client.get_secret("database-password").value

# Blob Storage access
blob_url = "https://stwebapp.blob.core.windows.net/"
blob_client = BlobServiceClient(account_url=blob_url, credential=credential)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Workload Identity Federation

For GitHub Actions utan secrets:

```bash
# Skapa federated credential
az ad app federated-credential create \\
  --id <app-id> \\
  --parameters '{
    "name": "github-main",
    "issuer": "https://token.actions.githubusercontent.com",
    "subject": "repo:myorg/myrepo:ref:refs/heads/main",
    "audiences": ["api://AzureADTokenExchange"]
  }'
```

```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: azure/login@v1
        with:
          client-id: ${{ secrets.AZURE_CLIENT_ID }}
          tenant-id: ${{ secrets.AZURE_TENANT_ID }}
          subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}

      - name: Deploy
        run: |
          az webapp deployment source config-zip ...
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Conditional Access (Premium)

```
┌─────────────────────────────────────────────────────────────┐
│              CONDITIONAL ACCESS POLICY                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  IF (Assignments):                                          │
│  ├── Users: DevOps-team                                    │
│  ├── Apps: Azure Portal, Azure CLI                         │
│  └── Conditions:                                            │
│       ├── Location: Outside corporate network              │
│       └── Device: Not compliant                            │
│                                                             │
│  THEN (Access controls):                                    │
│  ├── Grant: Require MFA                                    │
│  └── Session: Sign-in frequency 4 hours                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Identity Kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `az ad sp create-for-rbac` | Skapa Service Principal |
| `az webapp identity assign` | Aktivera Managed Identity |
| `az role assignment create` | Tilldela RBAC-roll |
| `az keyvault set-policy` | Ge KV access |
| `az ad app create` | Skapa App Registration |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `AADSTS700016` | App finns ej | Kolla app-id och tenant |
| `Forbidden` | Saknar RBAC-roll | Tilldela ratt roll |
| `Managed Identity not found` | MI ej aktiverad | `az webapp identity assign` |
| `Secret expired` | SP secret utgangen | Rotera credential |
| `Token expired` | Gammal token | Re-authenticate |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Managed Identity** | Forstahandsval - inga secrets |
| **Service Principal** | For CI/CD och externa system |
| **RBAC** | Least privilege - minsta nodvandiga |
| **Federation** | GitHub/GitLab utan secrets |
| **DefaultAzureCredential** | Fungerar overallt |

**Kom ihag:**
- Managed Identity framfor Service Principal
- Aldrig hardkoda credentials
- Rotera SP secrets regelbundet
- Anvand grupper for RBAC
- Workload Identity Federation for GitHub Actions
"""
        },
        # =====================================================================
        # NODE 18: Azure Key Vault & Secrets
        # =====================================================================
        {
            "title": "Azure Key Vault & Secrets",
            "slug": "azure-key-vault-secrets",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 125,
            "content": """# Azure Key Vault & Secrets

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Key Vault ar viktigt |
|----------|----------------------------|
| **Secrets** | Centraliserad hemlighetshantering |
| **Keys** | Krypteringsnycklar |
| **Certificates** | SSL/TLS-certifikat |
| **Rotation** | Automatisk rotation |
| **Audit** | Logging av all access |

Som DevOps-ingenjor maste du forsta:

- **Access policies** sa du kan ge ratt permissions
- **Secret rotation** sa hemligheter byts automatiskt
- **Integration** sa appar kan hamta secrets sakert

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Vault Oversikt

```
┌─────────────────────────────────────────────────────────────┐
│                    AZURE KEY VAULT                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  kv-webapp-prod                                      │   │
│  │                                                      │   │
│  │  Secrets:                                            │   │
│  │  ├── database-connection-string                      │   │
│  │  ├── api-key-sendgrid                               │   │
│  │  ├── jwt-secret                                      │   │
│  │  └── storage-account-key                            │   │
│  │                                                      │   │
│  │  Keys:                                               │   │
│  │  ├── encryption-key (RSA 2048)                      │   │
│  │  └── signing-key (EC P-256)                         │   │
│  │                                                      │   │
│  │  Certificates:                                       │   │
│  │  ├── wildcard-cert (*.webapp.com)                   │   │
│  │  └── api-client-cert                                │   │
│  │                                                      │   │
│  │  Access Policies:                                    │   │
│  │  ├── DevOps-team: Get, List secrets                 │   │
│  │  ├── app-api-prod (MI): Get secrets                 │   │
│  │  └── sp-deploy: Get, Set secrets                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa Key Vault

```bash
# Skapa Key Vault
az keyvault create \\
  --name kv-webapp-prod \\
  --resource-group rg-webapp-prod \\
  --location westeurope \\
  --sku standard \\
  --enable-rbac-authorization false  # Anvander access policies

# Med RBAC (rekommenderat for nya)
az keyvault create \\
  --name kv-webapp-prod \\
  --resource-group rg-webapp-prod \\
  --location westeurope \\
  --sku premium \\
  --enable-rbac-authorization true

# Aktivera soft-delete och purge protection
az keyvault update \\
  --name kv-webapp-prod \\
  --enable-soft-delete true \\
  --enable-purge-protection true
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Secrets Management

### Skapa och Lasa Secrets

```bash
# Skapa secret
az keyvault secret set \\
  --vault-name kv-webapp-prod \\
  --name "database-password" \\
  --value "SuperSecret123!"

# Skapa secret fran fil
az keyvault secret set \\
  --vault-name kv-webapp-prod \\
  --name "ssl-cert-private" \\
  --file ./private-key.pem

# Lasa secret
az keyvault secret show \\
  --vault-name kv-webapp-prod \\
  --name "database-password" \\
  --query "value" -o tsv

# Lista secrets
az keyvault secret list \\
  --vault-name kv-webapp-prod \\
  --output table

# Ta bort secret (soft delete)
az keyvault secret delete \\
  --vault-name kv-webapp-prod \\
  --name "old-secret"

# Aterstall deleted secret
az keyvault secret recover \\
  --vault-name kv-webapp-prod \\
  --name "old-secret"
```

### Secret Versions

```bash
# Lista versioner
az keyvault secret list-versions \\
  --vault-name kv-webapp-prod \\
  --name "database-password" \\
  --output table

# Hamta specifik version
az keyvault secret show \\
  --vault-name kv-webapp-prod \\
  --name "database-password" \\
  --version "abc123def456"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Access Policies vs RBAC

### Access Policies

```bash
# Ge anvandare access
az keyvault set-policy \\
  --name kv-webapp-prod \\
  --upn john@company.com \\
  --secret-permissions get list

# Ge Managed Identity access
az keyvault set-policy \\
  --name kv-webapp-prod \\
  --object-id <managed-identity-object-id> \\
  --secret-permissions get

# Ge Service Principal full access
az keyvault set-policy \\
  --name kv-webapp-prod \\
  --spn <app-id> \\
  --secret-permissions get list set delete \\
  --key-permissions get list create \\
  --certificate-permissions get list
```

### RBAC (Modern)

```bash
# Key Vault Secrets User - lasa secrets
az role assignment create \\
  --assignee <principal-id> \\
  --role "Key Vault Secrets User" \\
  --scope /subscriptions/<sub>/resourceGroups/rg-webapp-prod/providers/Microsoft.KeyVault/vaults/kv-webapp-prod

# Key Vault Administrator - full access
az role assignment create \\
  --assignee <principal-id> \\
  --role "Key Vault Administrator" \\
  --scope /subscriptions/<sub>/resourceGroups/rg-webapp-prod/providers/Microsoft.KeyVault/vaults/kv-webapp-prod
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Python Integration

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Skapa client med Managed Identity / CLI / env vars
credential = DefaultAzureCredential()
vault_url = "https://kv-webapp-prod.vault.azure.net/"
client = SecretClient(vault_url=vault_url, credential=credential)

# Hamta secret
db_password = client.get_secret("database-password")
print(f"Secret value: {db_password.value}")

# Hamta flera secrets
secrets_to_fetch = ["database-password", "api-key", "jwt-secret"]
config = {}
for name in secrets_to_fetch:
    secret = client.get_secret(name)
    config[name] = secret.value

# Skapa/uppdatera secret
client.set_secret("new-secret", "new-value")

# Lista secrets (endast namn, ej varden)
secrets = client.list_properties_of_secrets()
for secret in secrets:
    print(f"Secret: {secret.name}, Updated: {secret.updated_on}")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## App Service Integration

### Key Vault References

```bash
# Aktivera Managed Identity pa App Service
az webapp identity assign \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod

# Ge MI access till Key Vault
az keyvault set-policy \\
  --name kv-webapp-prod \\
  --object-id <principalId> \\
  --secret-permissions get

# Konfigurera app setting med KV reference
az webapp config appsettings set \\
  --resource-group rg-webapp-prod \\
  --name app-api-prod \\
  --settings DATABASE_PASSWORD="@Microsoft.KeyVault(VaultName=kv-webapp-prod;SecretName=database-password)"
```

### Bicep med Key Vault

```bicep
// Key Vault reference i Bicep
resource webApp 'Microsoft.Web/sites@2022-09-01' = {
  name: 'app-api-prod'
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    siteConfig: {
      appSettings: [
        {
          name: 'DATABASE_PASSWORD'
          value: '@Microsoft.KeyVault(VaultName=${keyVault.name};SecretName=database-password)'
        }
      ]
    }
  }
}

// Key Vault access policy
resource kvAccessPolicy 'Microsoft.KeyVault/vaults/accessPolicies@2022-07-01' = {
  parent: keyVault
  name: 'add'
  properties: {
    accessPolicies: [
      {
        tenantId: tenant().tenantId
        objectId: webApp.identity.principalId
        permissions: {
          secrets: ['get']
        }
      }
    ]
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure DevOps Integration

```yaml
# azure-pipelines.yml
variables:
  - group: 'keyvault-secrets'  # Linkad till Key Vault

# Eller direkt i pipeline:
steps:
  - task: AzureKeyVault@2
    displayName: 'Fetch secrets from Key Vault'
    inputs:
      azureSubscription: 'azure-connection'
      KeyVaultName: 'kv-webapp-prod'
      SecretsFilter: 'database-password,api-key,jwt-secret'
      RunAsPreJob: true

  - script: |
      echo "Using secrets in deployment..."
      # Secrets ar tillgangliga som pipeline variables
      # $(database-password), $(api-key), $(jwt-secret)
    env:
      DB_PASS: $(database-password)  # Mappa till env var
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Secret Rotation

### Automatisk rotation med Event Grid

```bash
# Skapa Event Grid subscription for expiring secrets
az eventgrid event-subscription create \\
  --name secret-expiring-handler \\
  --source-resource-id /subscriptions/<sub>/resourceGroups/rg-webapp-prod/providers/Microsoft.KeyVault/vaults/kv-webapp-prod \\
  --endpoint <function-app-url> \\
  --included-event-types Microsoft.KeyVault.SecretNearExpiry
```

```python
# Azure Function for rotation
import azure.functions as func
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def rotate_secret(event: func.EventGridEvent):
    secret_name = event.data['ObjectName']
    vault_url = event.data['VaultName']

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=f"https://{vault_url}.vault.azure.net/",
                          credential=credential)

    # Generera nytt varde
    new_value = generate_new_secret()

    # Uppdatera secret
    client.set_secret(secret_name, new_value)

    # Uppdatera beroende system (t.ex. databas)
    update_database_password(new_value)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Private Endpoint

```bash
# Skapa Private Endpoint
az network private-endpoint create \\
  --name pe-keyvault \\
  --resource-group rg-webapp-prod \\
  --vnet-name vnet-webapp \\
  --subnet subnet-private-endpoints \\
  --private-connection-resource-id $(az keyvault show --name kv-webapp-prod --query id -o tsv) \\
  --group-id vault \\
  --connection-name keyvault-connection

# Inaktivera public access
az keyvault update \\
  --name kv-webapp-prod \\
  --public-network-access Disabled
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Key Vault Kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `az keyvault create` | Skapa Key Vault |
| `az keyvault secret set` | Skapa/uppdatera secret |
| `az keyvault secret show` | Visa secret |
| `az keyvault secret list` | Lista secrets |
| `az keyvault set-policy` | Ge access |
| `az keyvault secret delete` | Soft-delete secret |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `Forbidden` | Saknar access policy | Lagg till policy/RBAC |
| `SecretNotFound` | Fel namn eller deleted | Kolla namn, aterstall |
| `Vault not found` | Fel DNS/private endpoint | Kolla neverks-config |
| `Access denied` | Firewall blockerar | Lagg till IP/VNet |
| `SecretDisabled` | Secret inaktiverad | Aktivera igen |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Centralisera** | Alla secrets i Key Vault |
| **Managed Identity** | Basta sattet att ge access |
| **KV References** | App Settings direkt fran KV |
| **Rotation** | Automatisera med Event Grid |
| **Private Endpoint** | Ingen public access i prod |

**Kom ihag:**
- Aldrig hardkoda secrets i kod
- Anvand Key Vault references i App Settings
- Managed Identity framfor access policies
- Soft-delete och purge protection i prod
- Private Endpoint for sakerhet
"""
        },
        # =====================================================================
        # NODE 19: Azure Defender & Security
        # =====================================================================
        {
            "title": "Azure Defender & Security",
            "slug": "azure-defender-security",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 150,
            "content": """# Azure Defender & Security

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Security ar viktigt |
|----------|---------------------------|
| **Compliance** | Uppfyll regler och standarder |
| **Threat detection** | Upptack attacker |
| **Vulnerability** | Hitta sarbarheter |
| **Data protection** | Skydda kanslig data |
| **Audit** | Sparbarhet och logging |

Som DevOps-ingenjor maste du forsta:

- **Microsoft Defender** sa du har threat protection
- **Security Center** sa du har oversikt
- **Network Security** sa du begransar trafik

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Microsoft Defender for Cloud

```
┌─────────────────────────────────────────────────────────────┐
│            MICROSOFT DEFENDER FOR CLOUD                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  SECURITY POSTURE                                    │   │
│  │                                                      │   │
│  │  Secure Score: 67/100                               │   │
│  │  ████████████████░░░░░░░░                           │   │
│  │                                                      │   │
│  │  Recommendations:                                    │   │
│  │  ├── [High] Enable MFA for accounts                 │   │
│  │  ├── [High] Encrypt storage at rest                 │   │
│  │  ├── [Medium] Enable diagnostic logs               │   │
│  │  └── [Low] Add resource tags                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  WORKLOAD PROTECTIONS                                │   │
│  │                                                      │   │
│  │  ├── Defender for Servers         [Enabled]        │   │
│  │  ├── Defender for Containers      [Enabled]        │   │
│  │  ├── Defender for App Service     [Enabled]        │   │
│  │  ├── Defender for Storage         [Enabled]        │   │
│  │  ├── Defender for SQL             [Enabled]        │   │
│  │  └── Defender for Key Vault       [Enabled]        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Aktivera Defender

```bash
# Aktivera Defender for Servers
az security pricing create \\
  --name VirtualMachines \\
  --tier Standard

# Aktivera Defender for Containers
az security pricing create \\
  --name Containers \\
  --tier Standard

# Aktivera Defender for App Service
az security pricing create \\
  --name AppServices \\
  --tier Standard

# Aktivera Defender for Storage
az security pricing create \\
  --name StorageAccounts \\
  --tier Standard

# Aktivera Defender for SQL
az security pricing create \\
  --name SqlServers \\
  --tier Standard

# Lista alla pricing tiers
az security pricing list --output table
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Network Security Groups (NSG)

### Skapa NSG

```bash
# Skapa NSG
az network nsg create \\
  --resource-group rg-webapp-prod \\
  --name nsg-webapp

# Tillat HTTPS inbound
az network nsg rule create \\
  --resource-group rg-webapp-prod \\
  --nsg-name nsg-webapp \\
  --name AllowHTTPS \\
  --priority 100 \\
  --direction Inbound \\
  --access Allow \\
  --protocol Tcp \\
  --destination-port-ranges 443

# Neka all annan inbound (implicit men explicit ar tydligare)
az network nsg rule create \\
  --resource-group rg-webapp-prod \\
  --nsg-name nsg-webapp \\
  --name DenyAllInbound \\
  --priority 4096 \\
  --direction Inbound \\
  --access Deny \\
  --protocol '*' \\
  --destination-port-ranges '*'

# Tillat outbound till specifika IPs
az network nsg rule create \\
  --resource-group rg-webapp-prod \\
  --nsg-name nsg-webapp \\
  --name AllowDBOutbound \\
  --priority 100 \\
  --direction Outbound \\
  --access Allow \\
  --protocol Tcp \\
  --destination-address-prefixes 10.0.2.0/24 \\
  --destination-port-ranges 5432

# Associera NSG med subnet
az network vnet subnet update \\
  --resource-group rg-webapp-prod \\
  --vnet-name vnet-webapp \\
  --name subnet-apps \\
  --network-security-group nsg-webapp
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Web Application Firewall (WAF)

```bash
# Skapa WAF Policy
az network application-gateway waf-policy create \\
  --name waf-policy-webapp \\
  --resource-group rg-webapp-prod \\
  --type OWASP \\
  --version 3.2

# Konfigurera managed rules
az network application-gateway waf-policy managed-rule rule-set add \\
  --policy-name waf-policy-webapp \\
  --resource-group rg-webapp-prod \\
  --type OWASP \\
  --version 3.2

# Custom rule - block specifika IPs
az network application-gateway waf-policy custom-rule create \\
  --policy-name waf-policy-webapp \\
  --resource-group rg-webapp-prod \\
  --name BlockBadIPs \\
  --priority 1 \\
  --rule-type MatchRule \\
  --action Block

# Lista WAF logs
az monitor activity-log list \\
  --resource-group rg-webapp-prod \\
  --query "[?contains(operationName.value, 'WAF')]"
```

### WAF pa Azure Front Door

```bicep
// Bicep for Front Door med WAF
resource frontDoor 'Microsoft.Cdn/profiles@2023-05-01' = {
  name: 'fd-webapp-prod'
  location: 'global'
  sku: {
    name: 'Premium_AzureFrontDoor'
  }
}

resource wafPolicy 'Microsoft.Network/FrontDoorWebApplicationFirewallPolicies@2022-05-01' = {
  name: 'waf-fd-webapp'
  location: 'global'
  properties: {
    policySettings: {
      mode: 'Prevention'
      enabledState: 'Enabled'
    }
    managedRules: {
      managedRuleSets: [
        {
          ruleSetType: 'Microsoft_DefaultRuleSet'
          ruleSetVersion: '2.1'
        }
        {
          ruleSetType: 'Microsoft_BotManagerRuleSet'
          ruleSetVersion: '1.0'
        }
      ]
    }
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Private Endpoints

```
┌─────────────────────────────────────────────────────────────┐
│              PRIVATE ENDPOINT ARCHITECTURE                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────────┐                 ┌───────────────┐       │
│  │    VNet       │                 │   PaaS        │       │
│  │  10.0.0.0/16  │                 │   Services    │       │
│  │               │                 │               │       │
│  │  ┌─────────┐  │  Private Link   │  ┌─────────┐ │       │
│  │  │ App     │──┼────────────────▶│  │ SQL DB  │ │       │
│  │  │ Service │  │  10.0.1.5       │  │         │ │       │
│  │  └─────────┘  │                 │  └─────────┘ │       │
│  │               │                 │               │       │
│  │  ┌─────────┐  │  Private Link   │  ┌─────────┐ │       │
│  │  │ Private │──┼────────────────▶│  │ Storage │ │       │
│  │  │Endpoint │  │  10.0.1.6       │  │ Account │ │       │
│  │  └─────────┘  │                 │  └─────────┘ │       │
│  │               │                 │               │       │
│  └───────────────┘                 └───────────────┘       │
│                                                             │
│  Trafik stannar inom Azure backbone - aldrig internet      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Skapa Private Endpoint for SQL
az network private-endpoint create \\
  --name pe-sql \\
  --resource-group rg-webapp-prod \\
  --vnet-name vnet-webapp \\
  --subnet subnet-private-endpoints \\
  --private-connection-resource-id $(az sql server show --name sql-webapp-prod --resource-group rg-webapp-prod --query id -o tsv) \\
  --group-id sqlServer \\
  --connection-name sql-connection

# Skapa Private DNS Zone
az network private-dns zone create \\
  --resource-group rg-webapp-prod \\
  --name privatelink.database.windows.net

# Linka DNS zone till VNet
az network private-dns link vnet create \\
  --resource-group rg-webapp-prod \\
  --zone-name privatelink.database.windows.net \\
  --name sql-dns-link \\
  --virtual-network vnet-webapp \\
  --registration-enabled false
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Container Security

### Defender for Containers

```bash
# Aktivera vulnerability scanning for ACR
az security pricing create \\
  --name ContainerRegistry \\
  --tier Standard

# Visa skanningsresultat
az security sub-assessment list \\
  --assessed-resource-id /subscriptions/<sub>/resourceGroups/rg-webapp-prod/providers/Microsoft.ContainerRegistry/registries/myacr
```

### AKS Security

```bash
# Aktivera Defender for AKS
az aks update \\
  --resource-group rg-webapp-prod \\
  --name aks-webapp \\
  --enable-defender

# Aktivera Azure Policy for AKS
az aks enable-addons \\
  --resource-group rg-webapp-prod \\
  --name aks-webapp \\
  --addons azure-policy

# Network Policy (Calico)
az aks update \\
  --resource-group rg-webapp-prod \\
  --name aks-webapp \\
  --network-policy calico
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Security Logging

### Diagnostic Settings

```bash
# Skicka logs till Log Analytics
az monitor diagnostic-settings create \\
  --name diag-keyvault \\
  --resource /subscriptions/<sub>/resourceGroups/rg-webapp-prod/providers/Microsoft.KeyVault/vaults/kv-webapp-prod \\
  --workspace /subscriptions/<sub>/resourceGroups/rg-webapp-prod/providers/Microsoft.OperationalInsights/workspaces/log-webapp-prod \\
  --logs '[{"category":"AuditEvent","enabled":true}]'

# NSG Flow Logs
az network watcher flow-log create \\
  --resource-group rg-webapp-prod \\
  --name nsg-flowlog \\
  --nsg nsg-webapp \\
  --storage-account stwebapplogsprod \\
  --workspace log-webapp-prod \\
  --enabled true \\
  --traffic-analytics true
```

### KQL Queries for Security

```kql
// Failed login attempts
SigninLogs
| where ResultType != 0
| summarize FailedAttempts = count() by UserPrincipalName, IPAddress
| where FailedAttempts > 5
| order by FailedAttempts desc

// Key Vault access
AzureDiagnostics
| where ResourceType == "VAULTS"
| where OperationName == "SecretGet"
| summarize count() by CallerIPAddress, identity_claim_upn_s
| order by count_ desc

// Suspicious network traffic
AzureNetworkAnalytics_CL
| where FlowStatus_s == "D"  // Denied
| summarize count() by SrcIP_s, DestPort_d
| where count_ > 100
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `NSG blocking traffic` | For restriktiva regler | Kolla NSG flow logs |
| `Private endpoint not resolving` | DNS-fel | Kolla private DNS zone |
| `WAF blocking legit traffic` | False positive | Lagg till exclusion |
| `Defender alerts` | Potential threat | Utred och atgarda |
| `Secure score low` | Recommendations ej fixade | Prioritera high-severity |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Defender** | Aktivera for alla workloads |
| **Private Endpoints** | Ingen public access i prod |
| **NSG** | Defense in depth |
| **WAF** | Skydda webappar |
| **Logging** | Centralisera till Log Analytics |

**Kom ihag:**
- Defender for Cloud for sakerhetsoversikt
- Private Endpoints for alla PaaS-tjanster
- NSG pa varje subnet
- WAF framfor alla publika webappar
- Aktivera alla diagnostic logs
"""
        },
        # =====================================================================
        # NODE 20: Azure Governance & Policy
        # =====================================================================
        {
            "title": "Azure Governance & Policy",
            "slug": "azure-governance-policy",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 150,
            "content": """# Azure Governance & Policy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Governance ar viktigt |
|----------|------------------------------|
| **Compliance** | Uppfyll regulatoriska krav |
| **Standardisering** | Konsistenta resurser |
| **Kostnadskontroll** | Forhindra overforbrukning |
| **Sakerhet** | Framtvinga best practices |
| **Audit** | Sparbarhet |

Som DevOps-ingenjor maste du forsta:

- **Azure Policy** sa du kan framtvinga regler
- **Blueprints** sa du kan deploya kompletta miljoer
- **Management Groups** sa du kan strukturera subscriptions

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Governance Hierarki

```
┌─────────────────────────────────────────────────────────────┐
│                    GOVERNANCE HIERARCHY                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                   ┌─────────────────┐                      │
│                   │  Tenant Root    │                      │
│                   │  Management     │                      │
│                   │  Group          │                      │
│                   └────────┬────────┘                      │
│                            │                                │
│         ┌──────────────────┼──────────────────┐            │
│         │                  │                  │            │
│  ┌──────▼─────┐    ┌──────▼─────┐    ┌──────▼─────┐      │
│  │ Production │    │   Dev/Test │    │  Sandbox   │      │
│  │     MG     │    │     MG     │    │     MG     │      │
│  └──────┬─────┘    └──────┬─────┘    └──────┬─────┘      │
│         │                  │                  │            │
│  ┌──────▼─────┐    ┌──────▼─────┐    ┌──────▼─────┐      │
│  │Subscription│    │Subscription│    │Subscription│      │
│  │  prod-001  │    │  dev-001   │    │  sandbox   │      │
│  └──────┬─────┘    └──────┬─────┘    └────────────┘      │
│         │                  │                               │
│  ┌──────▼─────────────────▼─────┐                         │
│  │     Resource Groups          │                         │
│  │  ├── rg-webapp-prod          │                         │
│  │  ├── rg-data-prod            │                         │
│  │  └── rg-network-prod         │                         │
│  └──────────────────────────────┘                         │
│                                                             │
│  Policy arv:  Tenant → MG → Sub → RG → Resource           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure Policy

### Policy Effects

| Effect | Beskrivning |
|--------|-------------|
| **Deny** | Blockera operation |
| **Audit** | Logga men tillat |
| **Append** | Lagg till properties |
| **Modify** | Andra properties |
| **DeployIfNotExists** | Auto-deploya |
| **AuditIfNotExists** | Auditera om saknas |

### Skapa och Tilldela Policy

```bash
# Lista inbyggda policies
az policy definition list --query "[?policyType=='BuiltIn']" --output table

# Tilldela inbyggd policy - Require tags
az policy assignment create \\
  --name "require-env-tag" \\
  --display-name "Require Environment Tag" \\
  --scope /subscriptions/<sub> \\
  --policy "/providers/Microsoft.Authorization/policyDefinitions/871b6d14-10aa-478d-b590-94f262ecfa99" \\
  --params '{"tagName":{"value":"Environment"}}'

# Tilldela policy pa resource group
az policy assignment create \\
  --name "allowed-locations" \\
  --display-name "Allowed Locations - West Europe" \\
  --scope /subscriptions/<sub>/resourceGroups/rg-webapp-prod \\
  --policy "/providers/Microsoft.Authorization/policyDefinitions/e56962a6-4747-49cd-b67b-bf8b01975c4c" \\
  --params '{"listOfAllowedLocations":{"value":["westeurope","northeurope"]}}'
```

### Custom Policy Definition

```json
{
  "mode": "Indexed",
  "policyRule": {
    "if": {
      "allOf": [
        {
          "field": "type",
          "equals": "Microsoft.Storage/storageAccounts"
        },
        {
          "field": "Microsoft.Storage/storageAccounts/allowBlobPublicAccess",
          "notEquals": false
        }
      ]
    },
    "then": {
      "effect": "deny"
    }
  },
  "parameters": {}
}
```

```bash
# Skapa custom policy
az policy definition create \\
  --name "deny-public-blob" \\
  --display-name "Deny Public Blob Access" \\
  --description "Prevents storage accounts with public blob access" \\
  --rules @policy-rule.json \\
  --mode Indexed
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Policy Initiatives

```bash
# Skapa initiative (policy set)
az policy set-definition create \\
  --name "security-baseline" \\
  --display-name "Security Baseline" \\
  --definitions '[
    {"policyDefinitionId": "/providers/Microsoft.Authorization/policyDefinitions/404c3081-a854-4457-ae30-26a93ef643f9"},
    {"policyDefinitionId": "/providers/Microsoft.Authorization/policyDefinitions/0961003e-5a0a-4549-abde-af6a37f2724d"},
    {"policyDefinitionId": "/providers/Microsoft.Authorization/policyDefinitions/2a1a9cdf-e04d-429a-8416-3bfb72a1b26f"}
  ]'

# Tilldela initiative
az policy assignment create \\
  --name "security-baseline" \\
  --display-name "Apply Security Baseline" \\
  --scope /subscriptions/<sub> \\
  --policy-set-definition "security-baseline"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Management Groups

```bash
# Skapa management group
az account management-group create \\
  --name "mg-production" \\
  --display-name "Production"

# Skapa child management group
az account management-group create \\
  --name "mg-prod-europe" \\
  --display-name "Production Europe" \\
  --parent "mg-production"

# Flytta subscription till management group
az account management-group subscription add \\
  --name "mg-production" \\
  --subscription <subscription-id>

# Lista hierarki
az account management-group list --output table

# Tilldela policy pa MG-niva
az policy assignment create \\
  --name "require-tags-mg" \\
  --scope /providers/Microsoft.Management/managementGroups/mg-production \\
  --policy "/providers/Microsoft.Authorization/policyDefinitions/871b6d14-10aa-478d-b590-94f262ecfa99"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Resource Locks

```bash
# Skapa CanNotDelete lock
az lock create \\
  --name "prod-lock" \\
  --resource-group rg-webapp-prod \\
  --lock-type CanNotDelete \\
  --notes "Prevent accidental deletion"

# Skapa ReadOnly lock
az lock create \\
  --name "readonly-lock" \\
  --resource-group rg-webapp-prod \\
  --lock-type ReadOnly \\
  --notes "Prevent any changes"

# Lista locks
az lock list --resource-group rg-webapp-prod --output table

# Ta bort lock (kravs fore deletion)
az lock delete \\
  --name "prod-lock" \\
  --resource-group rg-webapp-prod
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Tagging Strategy

```bash
# Obligatoriska tags
az policy assignment create \\
  --name "require-mandatory-tags" \\
  --policy "require-tag" \\
  --params '{
    "tagName": {"value": "CostCenter"},
    "tagValue": {"value": ""}
  }'

# Auto-apply tags med policy (Modify effect)
az policy definition create \\
  --name "inherit-tag-from-rg" \\
  --display-name "Inherit Environment tag from RG" \\
  --mode "Indexed" \\
  --rules '{
    "if": {
      "allOf": [
        {"field": "tags[Environment]", "exists": "false"},
        {"value": "[resourceGroup().tags[Environment]]", "notEquals": ""}
      ]
    },
    "then": {
      "effect": "modify",
      "details": {
        "roleDefinitionIds": ["/providers/Microsoft.Authorization/roleDefinitions/b24988ac-6180-42a0-ab88-20f7382dd24c"],
        "operations": [{
          "operation": "add",
          "field": "tags[Environment]",
          "value": "[resourceGroup().tags[Environment]]"
        }]
      }
    }
  }'
```

### Rekommenderad Tagging

| Tag | Exempel | Syfte |
|-----|---------|-------|
| **Environment** | prod, staging, dev | Miljoidentifiering |
| **CostCenter** | IT-001, Sales-002 | Kostnadsallokering |
| **Owner** | devops-team | Ansvarig |
| **Application** | webapp-api | Applikation |
| **CreatedBy** | terraform, manual | Skapelsesatt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cost Management

```bash
# Skapa budget
az consumption budget create \\
  --budget-name "monthly-prod-budget" \\
  --amount 5000 \\
  --time-grain Monthly \\
  --start-date 2024-01-01 \\
  --end-date 2024-12-31 \\
  --resource-group rg-webapp-prod \\
  --notifications '{
    "notification1": {
      "enabled": true,
      "operator": "GreaterThan",
      "threshold": 80,
      "contactEmails": ["devops@company.com"],
      "contactRoles": ["Owner"]
    }
  }'

# Visa aktuell kostnad
az consumption usage list \\
  --start-date 2024-01-01 \\
  --end-date 2024-01-31 \\
  --query "[].{Resource:instanceName, Cost:pretaxCost}" \\
  --output table
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Compliance & Regulatory

### Compliance Dashboard

```bash
# Lista compliance states
az policy state list \\
  --resource-group rg-webapp-prod \\
  --query "[?complianceState=='NonCompliant']" \\
  --output table

# Trigga policy evaluation
az policy state trigger-scan \\
  --resource-group rg-webapp-prod

# Export compliance report
az policy state list \\
  --filter "complianceState eq 'NonCompliant'" \\
  --output json > compliance-report.json
```

### Regulatory Compliance Initiatives

| Initiative | Beskrivning |
|------------|-------------|
| **CIS Microsoft Azure** | CIS Benchmark |
| **ISO 27001** | Information security |
| **SOC 2** | Service organization |
| **GDPR** | Data protection |
| **PCI DSS** | Payment card |

```bash
# Tilldela compliance initiative
az policy assignment create \\
  --name "cis-benchmark" \\
  --display-name "CIS Microsoft Azure Foundations" \\
  --scope /subscriptions/<sub> \\
  --policy-set-definition "/providers/Microsoft.Authorization/policySetDefinitions/612b5213-9160-4969-8578-1518bd2a000c"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Governance Kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `az policy definition list` | Lista policies |
| `az policy assignment create` | Tilldela policy |
| `az policy state list` | Visa compliance |
| `az lock create` | Skapa resource lock |
| `az account management-group` | Hantera MG |
| `az consumption budget` | Skapa budget |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `Policy denied` | Bryter mot policy | Fix compliance issue |
| `Lock preventing change` | Resource lock | Ta bort lock temporart |
| `Non-compliant resources` | Existerande resurser | Remediate manuellt |
| `Budget exceeded` | For hog forbrukning | Skala ner eller oka budget |
| `Tag missing` | Policy ej tilldelad | Tilldela tag policy |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Policy** | Framtvinga compliance |
| **Management Groups** | Strukturera subscriptions |
| **Tags** | Obligatoriska for kostnad/agare |
| **Locks** | Skydda kritiska resurser |
| **Budgets** | Undvik overskridanden |

**Kom ihag:**
- Policy pa MG-niva for bred tillämpning
- Deny policies for kritiska regler
- Audit policies for gradvis implementering
- Tags ar grunden for kostnadskontroll
- Locks pa produktionsresurser
"""
        },
    ]
}
