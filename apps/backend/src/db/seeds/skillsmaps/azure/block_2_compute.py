"""
Azure Cloud SkillsMap - Block 2: Compute & Networking
Nodes 5-8: Virtual Machines, App Service, Azure Functions, Virtual Networks
"""

from typing import Any

# ============================================================================
# NODE 5: AZURE VIRTUAL MACHINES
# ============================================================================

AZURE_NODE_5_VMS = {
    "node_id": 5,
    "title": "Azure Virtual Machines",
    "slug": "azure-virtual-machines",
    "description": "Skapa och hantera Azure VMs",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 110,
    "topics_covered": [
        "virtual machines", "vm sizes", "images", "disks",
        "availability sets", "scale sets", "vm extensions"
    ],
    "content": """# Azure Virtual Machines

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor VMs ar viktigt |
|----------|----------------------|
| **Full kontroll** | Hantera OS, middleware, applikationer |
| **Legacy-appar** | Kor applikationer som inte passar PaaS |
| **Custom images** | Skapa gyllene images for snabb deploy |
| **Hybrid** | Migrera fran on-prem till cloud |
| **HA/DR** | Availability Sets/Zones for redundans |

Azure VMs ar IaaS-grunden - full kontroll over compute.

------------------------------------------------------------

## VM Size Families

```
+-----------------------------------------------------------------+
|                    AZURE VM SIZE FAMILIES                        |
+-----------------------------------------------------------------+
|                                                                  |
|  FAMILY    ANVANDNING              EXEMPEL          vCPU  RAM   |
|  -----------------------------------------------------------    |
|  B-series  Burstable, dev/test     Standard_B2s      2    4GB   |
|            (ekonomisk, variabel CPU)                            |
|                                                                  |
|  D-series  General purpose         Standard_D4s_v5   4   16GB   |
|            (balanserad compute)                                 |
|                                                                  |
|  E-series  Memory optimized        Standard_E4s_v5   4   32GB   |
|            (databaser, caching)                                 |
|                                                                  |
|  F-series  Compute optimized       Standard_F4s_v2   4    8GB   |
|            (batch, gaming, analytics)                           |
|                                                                  |
|  N-series  GPU                     Standard_NC6      6   56GB   |
|            (ML, rendering, HPC)    (+ GPU)                      |
|                                                                  |
|  L-series  Storage optimized       Standard_L8s_v2   8   64GB   |
|            (big data, SQL, NoSQL)  (+ NVMe)                     |
|                                                                  |
+-----------------------------------------------------------------+
```

### Naming Convention

```
Standard_D4as_v5
|       |||   |
|       |||   +-- Version (nyare = battre)
|       ||+-- Special: s=SSD, r=RDMA, a=AMD
|       |+-- CPU count
|       +-- Family
+-- Tier (Basic/Standard)
```

------------------------------------------------------------

## Skapa VM med CLI

| Kommando | Beskrivning |
|----------|-------------|
| `az vm create` | Skapa VM |
| `az vm list` | Lista VMs |
| `az vm start/stop` | Starta/stoppa |
| `az vm deallocate` | Deallocate (sparar pengar) |
| `az vm resize` | Andra storlek |

```bash
# Skapa enkel Linux VM
az vm create \\
    --resource-group rg-demo \\
    --name vm-linux-01 \\
    --image Ubuntu2204 \\
    --size Standard_B2s \\
    --admin-username azureuser \\
    --generate-ssh-keys \\
    --public-ip-sku Standard

# Skapa Windows VM
az vm create \\
    --resource-group rg-demo \\
    --name vm-windows-01 \\
    --image Win2022Datacenter \\
    --size Standard_D2s_v5 \\
    --admin-username azureadmin \\
    --admin-password "SecureP@ssw0rd123!"

# Med managed disk och zones
az vm create \\
    --resource-group rg-demo \\
    --name vm-prod-01 \\
    --image Ubuntu2204 \\
    --size Standard_D4s_v5 \\
    --zone 1 \\
    --os-disk-size-gb 128 \\
    --data-disk-sizes-gb 256 \\
    --storage-sku Premium_LRS \\
    --nsg-rule SSH
```

------------------------------------------------------------

## VM Lifecycle

```bash
# Start VM
az vm start --resource-group rg-demo --name vm-linux-01

# Stop VM (fortfarande fakturering for storage!)
az vm stop --resource-group rg-demo --name vm-linux-01

# Deallocate (ingen compute-kostnad)
az vm deallocate --resource-group rg-demo --name vm-linux-01

# Restart
az vm restart --resource-group rg-demo --name vm-linux-01

# Resize VM
az vm resize --resource-group rg-demo --name vm-linux-01 --size Standard_D4s_v5

# Delete VM
az vm delete --resource-group rg-demo --name vm-linux-01 --yes
```

### Stop vs Deallocate

| Operation | Compute-kostnad | Storage-kostnad | Public IP |
|-----------|-----------------|-----------------|-----------|
| **Stop** | Ja (betalar!) | Ja | Behalles |
| **Deallocate** | Nej | Ja | Kan frigoras |

------------------------------------------------------------

## VM Disks

```bash
# Skapa och koppla datadisk
az vm disk attach \\
    --resource-group rg-demo \\
    --vm-name vm-linux-01 \\
    --name datadisk01 \\
    --new \\
    --size-gb 256 \\
    --sku Premium_LRS

# Inuti VM: formatera och mounta
sudo mkfs.ext4 /dev/sdc
sudo mkdir /data
sudo mount /dev/sdc /data

# Persistent mount (fstab)
echo '/dev/sdc /data ext4 defaults,nofail 0 0' | sudo tee -a /etc/fstab
```

### Disk-typer

| Typ | IOPS | Anvandning |
|-----|------|------------|
| **Standard HDD** | 500 | Backup, dev |
| **Standard SSD** | 6000 | Web servers |
| **Premium SSD** | 20000 | Databaser, produktion |
| **Ultra Disk** | 160000 | Mission-critical |

------------------------------------------------------------

## High Availability

```
+-----------------------------------------------------------------+
|                    VM HIGH AVAILABILITY                          |
+-----------------------------------------------------------------+
|                                                                  |
|  AVAILABILITY SETS (99.95% SLA)                                 |
|  +---------------------------------------------------------+    |
|  |  Fault Domain 0       Fault Domain 1       Fault Domain 2|    |
|  |  +---------+         +---------+          +---------+   |    |
|  |  |   VM1   |         |   VM2   |          |   VM3   |   |    |
|  |  +---------+         +---------+          +---------+   |    |
|  |  (Same rack)         (Different rack)     (Different)   |    |
|  +---------------------------------------------------------+    |
|                                                                  |
|  AVAILABILITY ZONES (99.99% SLA)                                |
|  +---------------------------------------------------------+    |
|  |    Zone 1             Zone 2               Zone 3       |    |
|  |  +---------+        +---------+          +---------+   |    |
|  |  |   VM1   |        |   VM2   |          |   VM3   |   |    |
|  |  +---------+        +---------+          +---------+   |    |
|  |  (Datacenter 1)     (Datacenter 2)       (Datacenter 3)|    |
|  +---------------------------------------------------------+    |
|                                                                  |
+-----------------------------------------------------------------+
```

| Strategi | SLA | Skyddar mot |
|----------|-----|-------------|
| **Single VM (Premium)** | 99.9% | - |
| **Availability Set** | 99.95% | Rack-fel |
| **Availability Zone** | 99.99% | Datacenter-fel |

------------------------------------------------------------

## VM Extensions

```bash
# Installera Azure Monitor agent
az vm extension set \\
    --resource-group rg-demo \\
    --vm-name vm-linux-01 \\
    --name AzureMonitorLinuxAgent \\
    --publisher Microsoft.Azure.Monitor

# Custom script extension
az vm extension set \\
    --resource-group rg-demo \\
    --vm-name vm-linux-01 \\
    --name customScript \\
    --publisher Microsoft.Azure.Extensions \\
    --settings '{"commandToExecute":"apt-get update && apt-get install -y nginx"}'
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| VM fastnar i "Creating" | Quota | `az vm list-usage --location` |
| Kan inte SSH | NSG blockerar | Lagg till port 22 i NSG |
| VM stoppad men kostar | Stop != Deallocate | Anvand `az vm deallocate` |
| Kan inte resize | Size ej tillganglig | Deallocate forst |

```bash
# Kontrollera quota
az vm list-usage --location northeurope --output table

# Kontrollera NSG-regler
az network nsg rule list \\
    --resource-group rg-demo \\
    --nsg-name vm-linux-01-nsg \\
    --output table
```

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Size Family** | Valj ratt family for workload (B=dev, D=general) |
| **Deallocate** | Stoppa betalning - inte bara stop |
| **Premium SSD** | For produktion och databaser |
| **Availability Zones** | 99.99% SLA - sprida over datacenter |

**Kom ihag:**
- **B-series** for dev/test (billig, burstable)
- **Deallocate** for att sluta betala compute
- **Premium SSD** for produktions-workloads
- **Availability Zones** for hogsta SLA
""",
}


# ============================================================================
# NODE 6: AZURE APP SERVICE
# ============================================================================

AZURE_NODE_6_APP_SERVICE = {
    "node_id": 6,
    "title": "Azure App Service",
    "slug": "azure-app-service",
    "description": "Deploya webbappar med PaaS",
    "difficulty": "intermediate",
    "estimated_minutes": 55,
    "xp_reward": 100,
    "topics_covered": [
        "app service", "app service plan", "deployment slots",
        "scaling", "custom domains", "ssl certificates"
    ],
    "content": """# Azure App Service

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor App Service ar viktigt |
|----------|------------------------------|
| **Ingen infrastruktur** | Azure skoter OS, patching, scaling |
| **Multi-language** | .NET, Node, Python, Java, PHP |
| **CI/CD built-in** | GitHub Actions, Azure DevOps |
| **Zero-downtime deploys** | Deployment slots for swapping |
| **Auto-scale** | Skala baserat pa trafik |

App Service ar Azures PaaS for webappar - fokusera pa kod.

------------------------------------------------------------

## App Service Architecture

```
+-----------------------------------------------------------------+
|                  APP SERVICE ARCHITECTURE                        |
+-----------------------------------------------------------------+
|                                                                  |
|  +-----------------------------------------------------------+  |
|  |                   APP SERVICE PLAN                         |  |
|  |  (Definierar compute-resurser: CPU, RAM, features)         |  |
|  |                                                             |  |
|  |  +-------------+ +-------------+ +-------------+          |  |
|  |  |  Web App 1  | |  Web App 2  | |  Web App 3  |          |  |
|  |  |   (API)     | |  (Frontend) | |  (Admin)    |          |  |
|  |  +-------------+ +-------------+ +-------------+          |  |
|  |                                                             |  |
|  +-----------------------------------------------------------+  |
|                                                                  |
|  TIERS:                                                         |
|  +----------------------------------------------------------+   |
|  | Free/Shared  | Basic        | Standard     | Premium     |   |
|  | - Dev/Test   | - Dedicated  | - Slots      | - More scale|   |
|  | - No SLA     | - Custom DNS | - Auto-scale | - Traffic   |   |
|  | - 1GB RAM    | - SSL        | - Daily backup|  Manager   |   |
|  +----------------------------------------------------------+   |
|                                                                  |
+-----------------------------------------------------------------+
```

### App Service Plan Tiers

| Tier | Anvandning | Features |
|------|------------|----------|
| **Free/Shared** | Dev/test | Ingen SLA, delad |
| **Basic** | Latt produktion | Custom DNS, SSL |
| **Standard** | Produktion | Slots, auto-scale, backup |
| **Premium** | Hog trafik | Mer scale, Traffic Manager |

------------------------------------------------------------

## Skapa App Service

| Kommando | Beskrivning |
|----------|-------------|
| `az appservice plan create` | Skapa plan |
| `az webapp create` | Skapa web app |
| `az webapp list` | Lista appar |
| `az webapp deployment` | Deploy |

```bash
# Skapa App Service Plan
az appservice plan create \\
    --name asp-myapp \\
    --resource-group rg-demo \\
    --location northeurope \\
    --sku B1 \\
    --is-linux

# Skapa Web App (Node.js)
az webapp create \\
    --name myapp-unique-123 \\
    --resource-group rg-demo \\
    --plan asp-myapp \\
    --runtime "NODE:18-lts"

# Skapa Web App (Python)
az webapp create \\
    --name myapp-python-123 \\
    --resource-group rg-demo \\
    --plan asp-myapp \\
    --runtime "PYTHON:3.11"

# Skapa Web App (.NET)
az webapp create \\
    --name myapp-dotnet-123 \\
    --resource-group rg-demo \\
    --plan asp-myapp \\
    --runtime "DOTNETCORE:8.0"
```

------------------------------------------------------------

## Deployment Methods

| Metod | Anvandning | Komplexitet |
|-------|------------|-------------|
| **ZIP Deploy** | Enkel, snabb | Lag |
| **Git Deploy** | Local git push | Medel |
| **GitHub Actions** | CI/CD (rekommenderas) | Medel |
| **Container** | Docker images | Hog |

```bash
# 1. ZIP Deploy (enklast)
az webapp deployment source config-zip \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --src app.zip

# 2. Git Deploy
az webapp deployment source config-local-git \\
    --resource-group rg-demo \\
    --name myapp-unique-123

git remote add azure https://myapp-unique-123.scm.azurewebsites.net/myapp-unique-123.git
git push azure main

# 3. GitHub Actions (recommended)
az webapp deployment github-actions add \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --repo "username/repo" \\
    --branch main

# 4. Container Deploy
az webapp create \\
    --resource-group rg-demo \\
    --plan asp-myapp \\
    --name myapp-container-123 \\
    --deployment-container-image-name myregistry.azurecr.io/myapp:latest
```

------------------------------------------------------------

## App Settings & Connection Strings

```bash
# Satt app settings (environment variables)
az webapp config appsettings set \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --settings \\
        NODE_ENV=production \\
        API_KEY=@Microsoft.KeyVault(VaultName=mykv;SecretName=api-key)

# Satt connection string
az webapp config connection-string set \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --connection-string-type SQLAzure \\
    --settings \\
        DefaultConnection="Server=myserver.database.windows.net;..."

# Visa settings
az webapp config appsettings list \\
    --resource-group rg-demo \\
    --name myapp-unique-123
```

------------------------------------------------------------

## Deployment Slots

```
+-----------------------------------------------------------------+
|                    DEPLOYMENT SLOTS                              |
+-----------------------------------------------------------------+
|                                                                  |
|  1. Deploy till staging                                         |
|  +-----------------+    +-----------------+                    |
|  |   PRODUCTION    |    |    STAGING      |                    |
|  |   (v1.0)        |    |    (v2.0)       |  <-- ny version    |
|  +-----------------+    +-----------------+                    |
|                                                                  |
|  2. Testa staging                                               |
|     https://myapp-staging.azurewebsites.net                     |
|                                                                  |
|  3. SWAP! (zero downtime)                                       |
|  +-----------------+    +-----------------+                    |
|  |   PRODUCTION    |<-->|    STAGING      |                    |
|  |   (v2.0)        |    |    (v1.0)       |  <-- rollback!     |
|  +-----------------+    +-----------------+                    |
|                                                                  |
+-----------------------------------------------------------------+
```

```bash
# Skapa staging slot
az webapp deployment slot create \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --slot staging

# Deploya till staging
az webapp deployment source config-zip \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --slot staging \\
    --src app.zip

# Swap staging -> production (zero downtime!)
az webapp deployment slot swap \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --slot staging \\
    --target-slot production
```

------------------------------------------------------------

## Custom Domain & SSL

```bash
# Lagg till custom domain
az webapp config hostname add \\
    --resource-group rg-demo \\
    --webapp-name myapp-unique-123 \\
    --hostname www.example.com

# Managed SSL (gratis!)
az webapp config ssl create \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --hostname www.example.com

# Bind SSL
az webapp config ssl bind \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --certificate-thumbprint <thumbprint> \\
    --ssl-type SNI
```

------------------------------------------------------------

## Scaling

```bash
# Manual scale (fler instances)
az appservice plan update \\
    --resource-group rg-demo \\
    --name asp-myapp \\
    --number-of-workers 3

# Scale up (storre VM)
az appservice plan update \\
    --resource-group rg-demo \\
    --name asp-myapp \\
    --sku P1v2

# Auto-scale (baserat pa CPU)
az monitor autoscale create \\
    --resource-group rg-demo \\
    --resource asp-myapp \\
    --resource-type Microsoft.Web/serverFarms \\
    --name autoscale-myapp \\
    --min-count 1 \\
    --max-count 10 \\
    --count 2
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Site cannot be reached | App crashar | Kolla logs |
| 502 Bad Gateway | Startup timeout | Oka startup time |
| Slow cold start | App Service Plan | Anvand Always On |
| SSL error | Cert ej bundet | Bind SSL cert |

```bash
# Visa logs
az webapp log tail \\
    --resource-group rg-demo \\
    --name myapp-unique-123

# Aktivera logging
az webapp log config \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --application-logging filesystem \\
    --detailed-error-messages true
```

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **App Service Plan** | Bestammer resurser och pris |
| **Deployment Slots** | Zero-downtime deploys och rollback |
| **Managed SSL** | Gratis SSL-certifikat |
| **Auto-scale** | Skala baserat pa CPU/minne/requests |

**Kom ihag:**
- **Standard tier** kravs for deployment slots
- **GitHub Actions** ar basta satt for CI/CD
- **Managed SSL** ar gratis och automatisk
- **Always On** forhindrar cold starts
""",
}


# ============================================================================
# NODE 7: AZURE FUNCTIONS
# ============================================================================

AZURE_NODE_7_FUNCTIONS = {
    "node_id": 7,
    "title": "Azure Functions",
    "slug": "azure-functions",
    "description": "Serverless compute med Azure Functions",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 110,
    "topics_covered": [
        "azure functions", "serverless", "triggers", "bindings",
        "durable functions", "consumption plan", "premium plan"
    ],
    "content": """# Azure Functions

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Serverless ar viktigt |
|----------|------------------------------|
| **Event-driven** | Reagera pa events utan server |
| **Cost-effective** | Betala endast for exekvering |
| **Auto-scale** | 0 till 1000+ instances automatiskt |
| **Microservices** | Sma, fokuserade funktioner |
| **Integration** | Triggers fran 100+ Azure-tjanster |

Serverless = fokusera pa kod, inte infrastruktur.

------------------------------------------------------------

## Azure Functions Architecture

```
+-----------------------------------------------------------------+
|                    AZURE FUNCTIONS                               |
+-----------------------------------------------------------------+
|                                                                  |
|  TRIGGERS (Vad startar funktionen?)                             |
|  +---------------------------------------------------------+    |
|  | HTTP     | Timer    | Blob     | Queue   | Event Hub  |    |
|  | request  | cron     | storage  | message | stream     |    |
|  +---------------------------------------------------------+    |
|                           |                                      |
|                           v                                      |
|  +---------------------------------------------------------+    |
|  |                   DIN FUNKTION                           |    |
|  |              (C#, JavaScript, Python, Java)              |    |
|  +---------------------------------------------------------+    |
|                           |                                      |
|                           v                                      |
|  BINDINGS (Input/Output)                                        |
|  +---------------------------------------------------------+    |
|  | Cosmos DB | SQL    | Blob    | Queue   | SendGrid     |    |
|  | Table     | Event  | SignalR | Twilio  | Service Bus  |    |
|  +---------------------------------------------------------+    |
|                                                                  |
+-----------------------------------------------------------------+
```

### Hosting Plans

| Plan | Beskrivning | Cold Start | Max tid |
|------|-------------|------------|---------|
| **Consumption** | Pay-per-execution | Ja (1-2s) | 5-10 min |
| **Premium** | Pre-warmed instances | Nej | Unlimited |
| **Dedicated** | App Service Plan | Nej | Unlimited |

------------------------------------------------------------

## Skapa Function App

```bash
# Skapa Storage Account (kravs for Functions)
az storage account create \\
    --name stfuncmyapp123 \\
    --resource-group rg-demo \\
    --location northeurope \\
    --sku Standard_LRS

# Skapa Function App (Consumption plan)
az functionapp create \\
    --name func-myapp-123 \\
    --resource-group rg-demo \\
    --storage-account stfuncmyapp123 \\
    --consumption-plan-location northeurope \\
    --runtime node \\
    --runtime-version 18 \\
    --functions-version 4

# Skapa Function App (Premium plan)
az functionapp plan create \\
    --name plan-func-premium \\
    --resource-group rg-demo \\
    --location northeurope \\
    --sku EP1

az functionapp create \\
    --name func-premium-123 \\
    --resource-group rg-demo \\
    --storage-account stfuncmyapp123 \\
    --plan plan-func-premium \\
    --runtime python \\
    --runtime-version 3.11
```

------------------------------------------------------------

## Trigger Types

| Trigger | Anvandning | Exempel |
|---------|------------|---------|
| **HTTP** | REST API, webhooks | API endpoints |
| **Timer** | Schemalagda jobb | Daglig cleanup |
| **Blob** | Fil uppladdad | Bildprocessning |
| **Queue** | Meddelande i ko | Asynkron processing |
| **Event Hub** | Event streaming | IoT data |
| **Cosmos DB** | Dokument andrat | Change feed |

### HTTP Trigger (JavaScript)

```javascript
// HttpTrigger/index.js
module.exports = async function (context, req) {
    const name = req.query.name || req.body?.name || 'World';

    context.res = {
        status: 200,
        body: { message: `Hello, ${name}!` }
    };
};

// function.json
{
    "bindings": [
        {
            "authLevel": "function",
            "type": "httpTrigger",
            "direction": "in",
            "name": "req",
            "methods": ["get", "post"]
        },
        {
            "type": "http",
            "direction": "out",
            "name": "res"
        }
    ]
}
```

### Timer Trigger (Python)

```python
# TimerTrigger/__init__.py
import azure.functions as func
import logging

def main(mytimer: func.TimerRequest) -> None:
    if mytimer.past_due:
        logging.warning('Timer is running late!')

    logging.info('Timer trigger executed!')
    # Din logik har - cleanup, rapporter, etc.

# function.json - var 5:e minut
{
    "bindings": [
        {
            "name": "mytimer",
            "type": "timerTrigger",
            "direction": "in",
            "schedule": "0 */5 * * * *"
        }
    ]
}
```

------------------------------------------------------------

## Local Development

```bash
# Installera Azure Functions Core Tools
brew install azure-functions-core-tools@4  # macOS
npm install -g azure-functions-core-tools@4  # npm

# Skapa nytt projekt
func init MyFunctionProject --worker-runtime python
cd MyFunctionProject

# Skapa ny function
func new --name HttpExample --template "HTTP trigger"

# Kor lokalt
func start

# Test
curl http://localhost:7071/api/HttpExample?name=Azure
```

------------------------------------------------------------

## Deployment

```bash
# Deploy fran lokal maskin
func azure functionapp publish func-myapp-123

# Satt app settings
az functionapp config appsettings set \\
    --name func-myapp-123 \\
    --resource-group rg-demo \\
    --settings \\
        DATABASE_URL="postgresql://..." \\
        API_KEY="@Microsoft.KeyVault(VaultName=mykv;SecretName=api-key)"
```

### local.settings.json

```json
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "python",
        "DATABASE_URL": "postgresql://localhost/mydb"
    }
}
```

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Cold start slow | Consumption plan | Premium plan eller keep-alive |
| Function timeout | Max 5 min | Premium plan for langre |
| Out of memory | For lite minne | Oka memory i plan |
| Binding error | Fel connection string | Kolla app settings |

```bash
# Visa logs
az functionapp logs show \\
    --name func-myapp-123 \\
    --resource-group rg-demo

# Stream logs
func azure functionapp logstream func-myapp-123
```

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Triggers** | Vad som startar funktionen |
| **Bindings** | Deklarativ input/output |
| **Consumption** | Pay-per-use, cold starts |
| **Premium** | Pre-warmed, VNet, unlimited time |

**Kom ihag:**
- **Consumption** for sporadisk anvandning (billigast)
- **Premium** for produktion (inga cold starts)
- **Core Tools** for lokal utveckling
- **Triggers + Bindings** = deklarativ integration
""",
}


# ============================================================================
# NODE 8: AZURE VIRTUAL NETWORK
# ============================================================================

AZURE_NODE_8_VNET = {
    "node_id": 8,
    "title": "Azure Virtual Network",
    "slug": "azure-virtual-network",
    "description": "Natverksarkitektur i Azure",
    "difficulty": "intermediate",
    "estimated_minutes": 65,
    "xp_reward": 120,
    "topics_covered": [
        "virtual network", "subnets", "nsg", "load balancer",
        "vpn gateway", "peering", "private endpoints"
    ],
    "content": """# Azure Virtual Network

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor VNet ar viktigt |
|----------|------------------------|
| **Isolation** | Separera workloads fran varandra |
| **Security** | Kontrollera trafikflode med NSG |
| **Connectivity** | Koppla ihop resurser sakkert |
| **Hybrid** | Anslut till on-prem med VPN/ExpressRoute |
| **Compliance** | Data stannar i privat natverk |

Natverk ar grunden for all sakerhet i Azure.

------------------------------------------------------------

## VNet Architecture

```
+-----------------------------------------------------------------+
|                    AZURE VNET ARCHITECTURE                       |
+-----------------------------------------------------------------+
|                                                                  |
|  Virtual Network: vnet-myapp (10.0.0.0/16)                      |
|  +---------------------------------------------------------+    |
|  |                                                          |    |
|  |  Subnet: snet-web (10.0.1.0/24)                         |    |
|  |  +---------+ +---------+ +---------+                   |    |
|  |  |  VM-1   | |  VM-2   | |  VM-3   |  <--- NSG-web     |    |
|  |  | .1.4    | | .1.5    | | .1.6    |                   |    |
|  |  +---------+ +---------+ +---------+                   |    |
|  |                      ^                                   |    |
|  |              Load Balancer                               |    |
|  |                      ^                                   |    |
|  |              Public IP                                   |    |
|  |                                                          |    |
|  |  Subnet: snet-app (10.0.2.0/24)                         |    |
|  |  +---------+ +---------+                               |    |
|  |  |  VM-4   | |  VM-5   |  <--- NSG-app                 |    |
|  |  | .2.4    | | .2.5    |  (Ingen public IP!)           |    |
|  |  +---------+ +---------+                               |    |
|  |                      |                                   |    |
|  |                      v                                   |    |
|  |  Subnet: snet-db (10.0.3.0/24)                          |    |
|  |  +---------+                                            |    |
|  |  | SQL DB  |  <--- Private Endpoint                     |    |
|  |  +---------+       (Ingen public access!)               |    |
|  |                                                          |    |
|  +---------------------------------------------------------+    |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Skapa Virtual Network

| Kommando | Beskrivning |
|----------|-------------|
| `az network vnet create` | Skapa VNet |
| `az network vnet subnet create` | Skapa subnet |
| `az network vnet list` | Lista VNets |

```bash
# Skapa VNet
az network vnet create \\
    --resource-group rg-demo \\
    --name vnet-myapp \\
    --address-prefix 10.0.0.0/16 \\
    --location northeurope

# Skapa subnets
az network vnet subnet create \\
    --resource-group rg-demo \\
    --vnet-name vnet-myapp \\
    --name snet-web \\
    --address-prefix 10.0.1.0/24

az network vnet subnet create \\
    --resource-group rg-demo \\
    --vnet-name vnet-myapp \\
    --name snet-app \\
    --address-prefix 10.0.2.0/24

az network vnet subnet create \\
    --resource-group rg-demo \\
    --vnet-name vnet-myapp \\
    --name snet-db \\
    --address-prefix 10.0.3.0/24
```

------------------------------------------------------------

## Network Security Groups (NSG)

```
+-----------------------------------------------------------------+
|                    NSG REGLER                                    |
+-----------------------------------------------------------------+
|                                                                  |
|  Priority  Namn           Port   Kaella        Action           |
|  -----------------------------------------------------------    |
|  100       AllowHTTP      80     Internet      Allow            |
|  110       AllowHTTPS     443    Internet      Allow            |
|  120       AllowSSH       22     MyIP          Allow            |
|  4096      DenyAll        *      *             Deny             |
|                                                                  |
|  Lagre priority = hogre prioritet (100 kors fore 200)           |
|                                                                  |
+-----------------------------------------------------------------+
```

```bash
# Skapa NSG
az network nsg create \\
    --resource-group rg-demo \\
    --name nsg-web

# Tillat HTTP/HTTPS fran internet
az network nsg rule create \\
    --resource-group rg-demo \\
    --nsg-name nsg-web \\
    --name AllowHTTP \\
    --priority 100 \\
    --source-address-prefixes Internet \\
    --destination-port-ranges 80 443 \\
    --access Allow \\
    --protocol Tcp \\
    --direction Inbound

# Tillat SSH endast fran specifik IP
az network nsg rule create \\
    --resource-group rg-demo \\
    --nsg-name nsg-web \\
    --name AllowSSH \\
    --priority 110 \\
    --source-address-prefixes "203.0.113.0/24" \\
    --destination-port-ranges 22 \\
    --access Allow \\
    --protocol Tcp \\
    --direction Inbound

# Koppla NSG till subnet
az network vnet subnet update \\
    --resource-group rg-demo \\
    --vnet-name vnet-myapp \\
    --name snet-web \\
    --network-security-group nsg-web
```

------------------------------------------------------------

## Load Balancer

```bash
# Skapa public IP for LB
az network public-ip create \\
    --resource-group rg-demo \\
    --name pip-lb \\
    --sku Standard \\
    --allocation-method Static

# Skapa Load Balancer
az network lb create \\
    --resource-group rg-demo \\
    --name lb-web \\
    --sku Standard \\
    --public-ip-address pip-lb \\
    --frontend-ip-name fe-web \\
    --backend-pool-name be-pool

# Skapa health probe
az network lb probe create \\
    --resource-group rg-demo \\
    --lb-name lb-web \\
    --name hp-http \\
    --protocol Http \\
    --port 80 \\
    --path /health

# Skapa load balancing rule
az network lb rule create \\
    --resource-group rg-demo \\
    --lb-name lb-web \\
    --name rule-http \\
    --protocol Tcp \\
    --frontend-port 80 \\
    --backend-port 80 \\
    --frontend-ip-name fe-web \\
    --backend-pool-name be-pool \\
    --probe-name hp-http
```

------------------------------------------------------------

## VNet Peering

```
+-----------------------------------------------------------------+
|                    VNET PEERING                                  |
+-----------------------------------------------------------------+
|                                                                  |
|  VNet-A (10.0.0.0/16)         VNet-B (10.1.0.0/16)             |
|  +-----------------+          +-----------------+              |
|  |                 |  <---->  |                 |              |
|  |   Production    |  Peering |   Shared Svcs   |              |
|  |                 |          |                 |              |
|  +-----------------+          +-----------------+              |
|                                                                  |
|  + Privat trafik over Microsoft backbone                        |
|  + Lag latens, hog bandbredd                                    |
|  + Kravs fran bada sidor                                        |
|                                                                  |
+-----------------------------------------------------------------+
```

```bash
# Peera tva VNets (kravs tva kommandon - bada riktningar)
# VNet A -> VNet B
az network vnet peering create \\
    --resource-group rg-demo \\
    --name peer-vnetA-to-vnetB \\
    --vnet-name vnet-A \\
    --remote-vnet /subscriptions/.../vnet-B \\
    --allow-vnet-access

# VNet B -> VNet A
az network vnet peering create \\
    --resource-group rg-demo \\
    --name peer-vnetB-to-vnetA \\
    --vnet-name vnet-B \\
    --remote-vnet /subscriptions/.../vnet-A \\
    --allow-vnet-access
```

------------------------------------------------------------

## Private Endpoints

```bash
# Skapa Private Endpoint for Azure SQL
az network private-endpoint create \\
    --resource-group rg-demo \\
    --name pe-sql \\
    --vnet-name vnet-myapp \\
    --subnet snet-db \\
    --private-connection-resource-id "/subscriptions/.../Microsoft.Sql/servers/mysqlserver" \\
    --group-id sqlServer \\
    --connection-name pe-sql-connection

# Nu kan SQL nas via privat IP (10.0.3.x) istallet for public endpoint
```

### Private Endpoint vs Service Endpoint

| Feature | Private Endpoint | Service Endpoint |
|---------|------------------|------------------|
| **IP** | Privat IP i VNet | Public IP med VNet-rule |
| **DNS** | Kravs privat DNS | Ingen andring |
| **Kostnad** | Per endpoint | Gratis |
| **On-prem** | Fungerar | Fungerar ej |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| VMs kan inte na internet | Ingen route | Kontrollera UDR |
| NSG blockerar trafik | Fel regel | `az network nic show-effective-nsg` |
| Peering fungerar ej | Bara en riktning | Skapa bada riktningar |
| Private Endpoint DNS | Fel DNS | Konfigurera Private DNS Zone |

```bash
# Visa effektiva NSG-regler for VM
az network nic show-effective-nsg \\
    --resource-group rg-demo \\
    --name vm-web-01-nic

# Lista VNet peerings
az network vnet peering list \\
    --resource-group rg-demo \\
    --vnet-name vnet-myapp
```

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **VNet** | Isolerar resurser i privat natverk |
| **Subnets** | Segmenterar trafik inom VNet |
| **NSG** | Kontrollerar vad som tillats in/ut |
| **Private Endpoints** | Eliminerar public access till PaaS |

**Kom ihag:**
- **NSG pa subnet**, inte bara pa NIC
- **Private Endpoints** for databaser och storage
- **VNet Peering** kravs fran **bada sidor**
- **Planera IP-adresser** innan du bygger (svart att andra)
""",
}


# Export all nodes from Block 2
BLOCK_2_NODES = [
    AZURE_NODE_5_VMS,
    AZURE_NODE_6_APP_SERVICE,
    AZURE_NODE_7_FUNCTIONS,
    AZURE_NODE_8_VNET,
]
