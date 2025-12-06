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
    "content": """
# Azure Virtual Machines

> *"VMs give you full control - but with great power comes great responsibility."*

---

## 🎯 Why This Matters

Azure VMs är IaaS-grunden:
- **Full kontroll** - OS, middleware, applikationer
- **Flexibilitet** - Windows, Linux, custom images
- **Integration** - med Azure-tjänster
- **Skalbarhet** - Scale Sets för auto-scaling

---

## 🧠 VM Size Families

```
┌─────────────────────────────────────────────────────────────────┐
│                    AZURE VM SIZE FAMILIES                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  FAMILY    USE CASE                  EXAMPLE          vCPU  RAM │
│  ────────────────────────────────────────────────────────────── │
│  B-series  Burstable, dev/test       Standard_B2s      2    4GB │
│            (ekonomisk, variabel CPU)                            │
│                                                                  │
│  D-series  General purpose           Standard_D4s_v5   4   16GB │
│            (balanserad compute)                                 │
│                                                                  │
│  E-series  Memory optimized          Standard_E4s_v5   4   32GB │
│            (databaser, caching)                                 │
│                                                                  │
│  F-series  Compute optimized         Standard_F4s_v2   4    8GB │
│            (batch, gaming, analytics)                           │
│                                                                  │
│  N-series  GPU                       Standard_NC6      6   56GB │
│            (ML, rendering, HPC)      (+ GPU)                    │
│                                                                  │
│  L-series  Storage optimized         Standard_L8s_v2   8   64GB │
│            (big data, SQL, NoSQL)    (+ NVMe)                   │
│                                                                  │
│  NAMING CONVENTION:                                              │
│  Standard_D4as_v5                                                │
│  │       │││   │                                                 │
│  │       │││   └── Version                                       │
│  │       ││└── Special: s=SSD, r=RDMA, a=AMD                     │
│  │       │└── CPU count                                          │
│  │       └── Family                                              │
│  └── Tier (Basic/Standard)                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Skapa VM med CLI

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

---

## 💻 VM Lifecycle

```bash
# Start VM
az vm start --resource-group rg-demo --name vm-linux-01

# Stop VM (still billing for storage!)
az vm stop --resource-group rg-demo --name vm-linux-01

# Deallocate (no compute charges)
az vm deallocate --resource-group rg-demo --name vm-linux-01

# Restart
az vm restart --resource-group rg-demo --name vm-linux-01

# Resize VM
az vm resize --resource-group rg-demo --name vm-linux-01 --size Standard_D4s_v5

# Delete VM
az vm delete --resource-group rg-demo --name vm-linux-01 --yes
```

---

## 💻 VM Disks

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

---

## 💻 VM Extensions

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

---

## 💻 High Availability

```
┌─────────────────────────────────────────────────────────────────┐
│                    VM HIGH AVAILABILITY                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  AVAILABILITY SETS (99.95% SLA)                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Fault Domain 0       Fault Domain 1       Fault Domain 2│    │
│  │  ┌─────────┐         ┌─────────┐          ┌─────────┐   │    │
│  │  │   VM1   │         │   VM2   │          │   VM3   │   │    │
│  │  └─────────┘         └─────────┘          └─────────┘   │    │
│  │  (Same rack)         (Different rack)     (Different)   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  AVAILABILITY ZONES (99.99% SLA)                                │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │    Zone 1             Zone 2               Zone 3       │    │
│  │  ┌─────────┐        ┌─────────┐          ┌─────────┐   │    │
│  │  │   VM1   │        │   VM2   │          │   VM3   │   │    │
│  │  └─────────┘        └─────────┘          └─────────┘   │    │
│  │  (Datacenter 1)     (Datacenter 2)       (Datacenter 3)│    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Vanliga Problem

### Problem 1: VM fastnar i "Creating"

```bash
# Kontrollera quota
az vm list-usage --location northeurope --output table

# Begär quota-ökning i Portal
# Subscriptions → Usage + quotas → Request increase
```

### Problem 2: Kan inte SSH

```bash
# Kontrollera NSG-regler
az network nsg rule list --resource-group rg-demo --nsg-name vm-linux-01-nsg --output table

# Lägg till SSH-regel
az network nsg rule create \\
    --resource-group rg-demo \\
    --nsg-name vm-linux-01-nsg \\
    --name AllowSSH \\
    --priority 1000 \\
    --access Allow \\
    --source-address-prefixes "YOUR_IP" \\
    --destination-port-ranges 22
```

---

## ✅ Sammanfattning

- **Välj rätt size family** för workload
- **Deallocate** för att stoppa betalning
- **Premium SSD** för produktion
- **Availability Zones** för 99.99% SLA
- **Extensions** för automation
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
    "content": """
# Azure App Service

> *"Focus on your code, let Azure handle the infrastructure."*

---

## 🎯 Why This Matters

App Service är Azures PaaS för webappar:
- **Ingen infrastruktur** - Azure sköter OS, patching
- **Multi-language** - .NET, Node, Python, Java, PHP
- **CI/CD built-in** - GitHub Actions, Azure DevOps
- **Scaling** - auto-scale baserat på trafik

---

## 🧠 App Service Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  APP SERVICE ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                   APP SERVICE PLAN                         │  │
│  │  (Defines compute resources: CPU, RAM, features)           │  │
│  │                                                             │  │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │  │
│  │  │  Web App 1  │ │  Web App 2  │ │  Web App 3  │          │  │
│  │  │   (API)     │ │  (Frontend) │ │  (Admin)    │          │  │
│  │  └─────────────┘ └─────────────┘ └─────────────┘          │  │
│  │                                                             │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  TIERS:                                                         │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Free/Shared  │ Basic        │ Standard     │ Premium     │   │
│  │ - Dev/Test   │ - Dedicated  │ - Slots      │ - More scale│   │
│  │ - No SLA     │ - Custom DNS │ - Auto-scale │ - Traffic   │   │
│  │ - 1GB RAM    │ - SSL        │ - Daily backup│  Manager   │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Skapa App Service

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

---

## 💻 Deployment Methods

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

# Push to Azure remote
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

---

## 💻 App Settings & Connection Strings

```bash
# Sätt app settings (environment variables)
az webapp config appsettings set \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --settings \\
        NODE_ENV=production \\
        API_KEY=@Microsoft.KeyVault(VaultName=mykv;SecretName=api-key)

# Sätt connection string
az webapp config connection-string set \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --connection-string-type SQLAzure \\
    --settings \\
        DefaultConnection="Server=myserver.database.windows.net;Database=mydb;..."

# Visa settings
az webapp config appsettings list --resource-group rg-demo --name myapp-unique-123
```

---

## 💻 Deployment Slots

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

# Swap staging → production (zero downtime!)
az webapp deployment slot swap \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --slot staging \\
    --target-slot production
```

---

## 💻 Custom Domain & SSL

```bash
# Lägg till custom domain
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

---

## 💻 Scaling

```bash
# Manual scale (fler instances)
az appservice plan update \\
    --resource-group rg-demo \\
    --name asp-myapp \\
    --number-of-workers 3

# Scale up (större VM)
az appservice plan update \\
    --resource-group rg-demo \\
    --name asp-myapp \\
    --sku P1v2

# Auto-scale (baserat på CPU)
az monitor autoscale create \\
    --resource-group rg-demo \\
    --resource asp-myapp \\
    --resource-type Microsoft.Web/serverFarms \\
    --name autoscale-myapp \\
    --min-count 1 \\
    --max-count 10 \\
    --count 2
```

---

## ⚠️ Vanliga Problem

### Problem 1: "Site cannot be reached"

```bash
# Kontrollera logs
az webapp log tail --resource-group rg-demo --name myapp-unique-123

# Aktivera logging
az webapp log config \\
    --resource-group rg-demo \\
    --name myapp-unique-123 \\
    --application-logging filesystem \\
    --detailed-error-messages true
```

---

## ✅ Sammanfattning

- **App Service Plan** bestämmer resurser
- **Deployment Slots** för zero-downtime deploys
- **Managed SSL** är gratis
- **Auto-scale** baserat på metrics
- **GitHub Actions** för CI/CD
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
    "content": """
# Azure Functions

> *"Run code when you need it, pay only for what you use."*

---

## 🎯 Why This Matters

Serverless computing:
- **Ingen server-hantering** - fokusera på kod
- **Event-driven** - reagera på triggers
- **Auto-scale** - 0 till 1000+ instances
- **Pay-per-execution** - ingen baseline-kostnad

---

## 🧠 Azure Functions Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    AZURE FUNCTIONS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  TRIGGERS (Vad startar funktionen?)                             │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ HTTP     │ Timer    │ Blob     │ Queue   │ Event Hub  │    │
│  │ request  │ cron     │ storage  │ message │ stream     │    │
│  └─────────────────────────────────────────────────────────┘    │
│                           │                                      │
│                           ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   YOUR FUNCTION                          │    │
│  │              (C#, JavaScript, Python, Java)              │    │
│  └─────────────────────────────────────────────────────────┘    │
│                           │                                      │
│                           ▼                                      │
│  BINDINGS (Input/Output)                                        │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ Cosmos DB │ SQL    │ Blob    │ Queue   │ SendGrid     │    │
│  │ Table     │ Event  │ SignalR │ Twilio  │ Service Bus  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  HOSTING PLANS:                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Consumption │ Premium       │ Dedicated (App Service)   │   │
│  │ - Pay/exec  │ - Pre-warmed  │ - Always running          │   │
│  │ - Cold start│ - VNet        │ - No cold start           │   │
│  │ - 5min max  │ - Unlimited   │ - Predictable cost        │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Skapa Function App

```bash
# Skapa Storage Account (required for Functions)
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

---

## 💻 Function Code Examples

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
    # Din logik här - cleanup, rapporter, etc.

# function.json
{
    "bindings": [
        {
            "name": "mytimer",
            "type": "timerTrigger",
            "direction": "in",
            "schedule": "0 */5 * * * *"  // Var 5:e minut
        }
    ]
}
```

### Blob Trigger with Output Binding

```python
# BlobProcessor/__init__.py
import azure.functions as func
from PIL import Image
import io

def main(inputblob: func.InputStream, outputblob: func.Out[bytes]) -> None:
    # Läs bild
    image = Image.open(inputblob)

    # Resize
    thumbnail = image.resize((150, 150))

    # Spara som output
    buffer = io.BytesIO()
    thumbnail.save(buffer, format='JPEG')
    outputblob.set(buffer.getvalue())

# function.json
{
    "bindings": [
        {
            "name": "inputblob",
            "type": "blobTrigger",
            "direction": "in",
            "path": "images/{name}",
            "connection": "AzureWebJobsStorage"
        },
        {
            "name": "outputblob",
            "type": "blob",
            "direction": "out",
            "path": "thumbnails/{name}",
            "connection": "AzureWebJobsStorage"
        }
    ]
}
```

---

## 💻 Local Development

```bash
# Installera Azure Functions Core Tools
brew install azure-functions-core-tools@4  # macOS
npm install -g azure-functions-core-tools@4  # npm

# Skapa nytt projekt
func init MyFunctionProject --worker-runtime python
cd MyFunctionProject

# Skapa ny function
func new --name HttpExample --template "HTTP trigger"

# Kör lokalt
func start

# Test
curl http://localhost:7071/api/HttpExample?name=Azure
```

---

## 💻 Deployment

```bash
# Deploy från lokal maskin
func azure functionapp publish func-myapp-123

# GitHub Actions deployment
# .github/workflows/deploy.yml
# name: Deploy to Azure Functions
# on:
#   push:
#     branches: [main]
# jobs:
#   deploy:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v3
#       - uses: Azure/functions-action@v1
#         with:
#           app-name: func-myapp-123
#           publish-profile: ${{ secrets.AZURE_FUNCTIONAPP_PUBLISH_PROFILE }}
```

---

## 💻 Environment Variables

```bash
# Sätt app settings
az functionapp config appsettings set \\
    --name func-myapp-123 \\
    --resource-group rg-demo \\
    --settings \\
        DATABASE_URL="postgresql://..." \\
        API_KEY="@Microsoft.KeyVault(VaultName=mykv;SecretName=api-key)"

# Local settings (local.settings.json)
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "python",
        "DATABASE_URL": "postgresql://localhost/mydb"
    }
}
```

---

## ⚠️ Vanliga Problem

### Problem 1: Cold Start

```bash
# Consumption plan har cold starts (1-2 sekunder)

# Lösningar:
# 1. Premium plan (pre-warmed instances)
# 2. Dedicated plan (always running)
# 3. Minimera dependencies för snabbare startup
```

### Problem 2: Timeout

```bash
# Consumption: max 5 min (default) / 10 min (max)
# Premium/Dedicated: unlimited

# För längre jobb: använd Durable Functions
```

---

## ✅ Sammanfattning

- **Triggers** startar funktioner
- **Bindings** kopplar input/output
- **Consumption** för sporadisk användning
- **Premium** för produktion utan cold starts
- **Core Tools** för lokal utveckling
""",
}


# ============================================================================
# NODE 8: AZURE VIRTUAL NETWORK
# ============================================================================

AZURE_NODE_8_VNET = {
    "node_id": 8,
    "title": "Azure Virtual Network",
    "slug": "azure-virtual-network",
    "description": "Nätverksarkitektur i Azure",
    "difficulty": "intermediate",
    "estimated_minutes": 65,
    "xp_reward": 120,
    "topics_covered": [
        "virtual network", "subnets", "nsg", "load balancer",
        "vpn gateway", "peering", "private endpoints"
    ],
    "content": """
# Azure Virtual Network

> *"A well-designed network is the foundation of security."*

---

## 🎯 Why This Matters

Nätverk är grunden för allt i Azure:
- **Isolation** - separera workloads
- **Security** - kontrollera trafikflöde
- **Connectivity** - koppla ihop resurser
- **Hybrid** - anslut till on-premises

---

## 🧠 VNet Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    AZURE VNET ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Virtual Network: vnet-myapp (10.0.0.0/16)                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                                                          │    │
│  │  Subnet: snet-web (10.0.1.0/24)                         │    │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐                   │    │
│  │  │  VM-1   │ │  VM-2   │ │  VM-3   │  ←─── NSG-web     │    │
│  │  │ .1.4    │ │ .1.5    │ │ .1.6    │                   │    │
│  │  └─────────┘ └─────────┘ └─────────┘                   │    │
│  │                      ↑                                   │    │
│  │              Load Balancer                               │    │
│  │                      ↑                                   │    │
│  │              Public IP                                   │    │
│  │                                                          │    │
│  │  Subnet: snet-app (10.0.2.0/24)                         │    │
│  │  ┌─────────┐ ┌─────────┐                               │    │
│  │  │  VM-4   │ │  VM-5   │  ←─── NSG-app                 │    │
│  │  │ .2.4    │ │ .2.5    │  (No public IP!)              │    │
│  │  └─────────┘ └─────────┘                               │    │
│  │                      │                                   │    │
│  │                      ▼                                   │    │
│  │  Subnet: snet-db (10.0.3.0/24)                          │    │
│  │  ┌─────────┐                                            │    │
│  │  │ SQL DB  │  ←─── Private Endpoint                     │    │
│  │  └─────────┘       (No public access!)                  │    │
│  │                                                          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Skapa Virtual Network

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

---

## 💻 Network Security Groups (NSG)

```bash
# Skapa NSG
az network nsg create \\
    --resource-group rg-demo \\
    --name nsg-web

# Tillåt HTTP/HTTPS från internet
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

# Tillåt SSH endast från specifik IP
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

# Neka allt annat (implicit, men explicit är tydligare)
az network nsg rule create \\
    --resource-group rg-demo \\
    --nsg-name nsg-web \\
    --name DenyAll \\
    --priority 4096 \\
    --source-address-prefixes "*" \\
    --destination-port-ranges "*" \\
    --access Deny \\
    --protocol "*" \\
    --direction Inbound

# Koppla NSG till subnet
az network vnet subnet update \\
    --resource-group rg-demo \\
    --vnet-name vnet-myapp \\
    --name snet-web \\
    --network-security-group nsg-web
```

---

## 💻 Load Balancer

```bash
# Skapa public IP för LB
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

# Lägg till VM till backend pool
az network nic ip-config address-pool add \\
    --resource-group rg-demo \\
    --nic-name vm-web-01-nic \\
    --ip-config-name ipconfig1 \\
    --lb-name lb-web \\
    --address-pool be-pool
```

---

## 💻 VNet Peering

```bash
# Peera två VNets (kräver två kommandon)
# VNet A → VNet B
az network vnet peering create \\
    --resource-group rg-demo \\
    --name peer-vnetA-to-vnetB \\
    --vnet-name vnet-A \\
    --remote-vnet /subscriptions/.../resourceGroups/.../providers/Microsoft.Network/virtualNetworks/vnet-B \\
    --allow-vnet-access

# VNet B → VNet A
az network vnet peering create \\
    --resource-group rg-demo \\
    --name peer-vnetB-to-vnetA \\
    --vnet-name vnet-B \\
    --remote-vnet /subscriptions/.../resourceGroups/.../providers/Microsoft.Network/virtualNetworks/vnet-A \\
    --allow-vnet-access
```

---

## 💻 Private Endpoints

```bash
# Skapa Private Endpoint för Azure SQL
az network private-endpoint create \\
    --resource-group rg-demo \\
    --name pe-sql \\
    --vnet-name vnet-myapp \\
    --subnet snet-db \\
    --private-connection-resource-id "/subscriptions/.../resourceGroups/.../providers/Microsoft.Sql/servers/mysqlserver" \\
    --group-id sqlServer \\
    --connection-name pe-sql-connection

# Nu kan SQL nås via privat IP (10.0.3.x) istället för public endpoint
```

---

## ⚠️ Vanliga Problem

### Problem 1: VMs kan inte nå internet

```bash
# Kontrollera att subnet har route till internet
# Standard: Azure tillhandahåller default route

# Om du har UDR (User Defined Route), kontrollera:
az network route-table route list --resource-group rg-demo --route-table-name rt-custom
```

### Problem 2: NSG blockerar trafik

```bash
# Visa effektiva NSG-regler för VM
az network nic show-effective-nsg \\
    --resource-group rg-demo \\
    --name vm-web-01-nic

# Kontrollera NSG flow logs
# Portal → NSG → Diagnostic settings → Enable flow logs
```

---

## ✅ Sammanfattning

- **VNet** isolerar dina resurser
- **Subnets** segmenterar trafik
- **NSGs** kontrollerar vad som tillåts
- **Load Balancer** distribuerar trafik
- **Private Endpoints** eliminerar public access
""",
}


# Export all nodes from Block 2
BLOCK_2_NODES = [
    AZURE_NODE_5_VMS,
    AZURE_NODE_6_APP_SERVICE,
    AZURE_NODE_7_FUNCTIONS,
    AZURE_NODE_8_VNET,
]
