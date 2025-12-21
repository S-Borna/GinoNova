"""
Azure Cloud SkillsMap - Block 5: Security & Governance
Nodes 17-20: Entra ID, Key Vault, Defender for Cloud, Governance
"""

from typing import Any

# ============================================================================
# NODE 17: AZURE ENTRA ID (FORMERLY AZURE AD)
# ============================================================================

AZURE_NODE_17_ENTRA = {
    "node_id": 17,
    "title": "Azure Entra ID",
    "slug": "azure-entra-id",
    "description": "Identity och access management i Azure",
    "difficulty": "intermediate",
    "estimated_minutes": 65,
    "xp_reward": 120,
    "topics_covered": [
        "azure ad", "entra id", "authentication", "authorization",
        "service principals", "managed identity", "rbac"
    ],
    "content": """
# Azure Entra ID (Azure Active Directory)

> *"Identity is the new perimeter."*

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Problem utan Entra ID | Losning med Entra ID |
|----------|----------------------|----------------------|
| CI/CD auth | Hardkodade credentials | Service Principals med RBAC |
| App secrets | Losenord i kod | Managed Identity (no secrets!) |
| Access control | Alla har samma access | Finkornig RBAC |
| Audit | Ingen sparbarhet | Full audit trail |

------------------------------------------------------------

## Identity Concepts

```
+-----------------------------------------------------------------+
|                    AZURE ENTRA ID                                |
+-----------------------------------------------------------------+
|                                                                  |
|  IDENTITY TYPES:                                                |
|  +---------------------------------------------------------+    |
|  |                                                          |    |
|  |  USER                SERVICE           MANAGED           |    |
|  |  IDENTITY            PRINCIPAL         IDENTITY          |    |
|  |  +-----+            +-----+           +-----+           |    |
|  |  | 👤  |            | 🤖  |           | 🔐  |           |    |
|  |  +-----+            +-----+           +-----+           |    |
|  |  Human user         App/service       Azure resource    |    |
|  |  Interactive        Client ID +       Auto-managed      |    |
|  |  login              Secret/Cert       No credentials    |    |
|  |                                                          |    |
|  +---------------------------------------------------------+    |
|                                                                  |
|  AUTHENTICATION FLOW:                                           |
|  +---------------------------------------------------------+    |
|  |                                                          |    |
|  |  Client -> Entra ID -> Token -> Resource (Graph, Azure)    |    |
|  |                                                          |    |
|  |  OAuth 2.0 / OpenID Connect flows:                      |    |
|  |  - Authorization Code (web apps)                        |    |
|  |  - Client Credentials (service-to-service)              |    |
|  |  - Device Code (CLI/IoT)                                |    |
|  |  - Implicit (deprecated)                                |    |
|  |                                                          |    |
|  +---------------------------------------------------------+    |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Service Principal

```bash
# Skapa Service Principal (för CI/CD, scripts etc.)
az ad sp create-for-rbac \\
    --name "sp-myapp-cicd" \\
    --role "Contributor" \\
    --scopes /subscriptions/xxx/resourceGroups/rg-myapp

# Output:
# {
#   "appId": "xxx",          <- Client ID
#   "password": "xxx",       <- Client Secret (visa bara EN gång!)
#   "tenant": "xxx"          <- Tenant ID
# }

# Logga in med Service Principal
az login --service-principal \\
    --username <appId> \\
    --password <password> \\
    --tenant <tenant>

# Lista service principals
az ad sp list --display-name "sp-myapp" --output table

# Rotera credentials
az ad sp credential reset --id <appId>
```

------------------------------------------------------------

## Managed Identity

```bash
# Managed Identity = Azure hanterar credentials åt dig!
# Två typer:
# 1. System-assigned - skapas/tas bort med resursen
# 2. User-assigned - separat resurs, kan delas

# Aktivera System-assigned på VM
az vm identity assign \\
    --name vm-myapp \\
    --resource-group rg-demo

# Aktivera System-assigned på App Service
az webapp identity assign \\
    --name app-myapp \\
    --resource-group rg-demo

# Skapa User-assigned Managed Identity
az identity create \\
    --name id-myapp \\
    --resource-group rg-demo

# Tilldela User-assigned till VM
az vm identity assign \\
    --name vm-myapp \\
    --resource-group rg-demo \\
    --identities /subscriptions/xxx/resourceGroups/rg-demo/providers/Microsoft.ManagedIdentity/userAssignedIdentities/id-myapp
```

------------------------------------------------------------

## Anvanda Managed Identity

```python
# Python: Azure SDK med Managed Identity
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# DefaultAzureCredential försöker:
# 1. Environment variables (Service Principal)
# 2. Managed Identity
# 3. Azure CLI
# 4. VS Code
credential = DefaultAzureCredential()

# Anslut till Storage med Managed Identity
blob_service = BlobServiceClient(
    account_url="https://mystorageaccount.blob.core.windows.net",
    credential=credential
)

# Ingen connection string eller API keys behövs!
containers = blob_service.list_containers()
for container in containers:
    print(container.name)
```

```csharp
// C#: Azure SDK med Managed Identity
using Azure.Identity;
using Azure.Storage.Blobs;

var credential = new DefaultAzureCredential();
var blobServiceClient = new BlobServiceClient(
    new Uri("https://mystorageaccount.blob.core.windows.net"),
    credential);

await foreach (var container in blobServiceClient.GetBlobContainersAsync())
{
    Console.WriteLine(container.Name);
}
```

------------------------------------------------------------

## RBAC (Role-Based Access Control)

```bash
# RBAC = Vem (Identity) får göra vad (Role) var (Scope)

# Lista inbyggda roller
az role definition list --output table

# Vanliga roller:
# - Owner: full access + kan ge tillgång
# - Contributor: full access, men kan inte ge tillgång
# - Reader: bara läsa
# - User Access Administrator: hantera access

# Tilldela roll till användare
az role assignment create \\
    --role "Contributor" \\
    --assignee "user@company.com" \\
    --scope /subscriptions/xxx/resourceGroups/rg-demo

# Tilldela roll till Managed Identity
az role assignment create \\
    --role "Storage Blob Data Contributor" \\
    --assignee-object-id $(az webapp identity show --name app-myapp --resource-group rg-demo --query principalId -o tsv) \\
    --scope /subscriptions/xxx/resourceGroups/rg-demo/providers/Microsoft.Storage/storageAccounts/mystorageaccount

# Lista role assignments
az role assignment list \\
    --resource-group rg-demo \\
    --output table
```

------------------------------------------------------------

## Conditional Access

```bash
# Conditional Access policies (via Portal eller Graph API)
# Exempel på policy:
# IF: User från extern plats
# AND: Accessing Azure Portal
# THEN: Kräv MFA

# Vanliga villkor:
# - Plats (IP-range, namngivna platser)
# - Enhet (compliant, hybrid-joined)
# - Applikation (specifika appar)
# - Risk level (sign-in risk, user risk)

# Vanliga kontroller:
# - Block access
# - Require MFA
# - Require compliant device
# - Require approved client app
```

------------------------------------------------------------

## App Registration

```bash
# Registrera app i Entra ID (för OAuth)
az ad app create \\
    --display-name "MyWebApp" \\
    --sign-in-audience "AzureADMyOrg" \\
    --web-redirect-uris "https://myapp.com/auth/callback"

# Lägg till API permissions
az ad app permission add \\
    --id <app-id> \\
    --api 00000003-0000-0000-c000-000000000000 \\  # Microsoft Graph
    --api-permissions e1fe6dd8-ba31-4d61-89e7-88639da4683d=Scope  # User.Read

# Grant admin consent
az ad app permission admin-consent --id <app-id>
```

------------------------------------------------------------

## Vanliga Problem

### Problem 1: "AADSTS700016: Application not found"

```bash
# Kontrollera att app finns i rätt tenant
az ad app show --id <app-id>

# Kontrollera Sign-in audience
# - AzureADMyOrg: bara din tenant
# - AzureADMultipleOrgs: alla Azure AD tenants
# - AzureADandPersonalMicrosoftAccount: alla + personliga
```

------------------------------------------------------------

## Key Takeaways

| Begrepp | Beskrivning |
|---------|-------------|
| Service Principal | For CI/CD och automation (Client ID + Secret) |
| Managed Identity | Basta praxis - Azure hanterar credentials |
| RBAC | Finkornig access control (Role + Scope) |
| Conditional Access | Policy-baserad access (MFA, device compliance) |
| DefaultAzureCredential | SDK-klass som provar alla auth-metoder |

**Kom ihag:**
- Anvand Managed Identity istallet for Service Principal nar mojligt
- Folj principen om minsta behorighet (least privilege)
- RBAC-roller propagerar nedat i scope-hierarkin
- DefaultAzureCredential fungerar bade lokalt och i Azure
""",
}


# ============================================================================
# NODE 18: AZURE KEY VAULT
# ============================================================================

AZURE_NODE_18_KEYVAULT = {
    "node_id": 18,
    "title": "Azure Key Vault",
    "slug": "azure-key-vault",
    "description": "Säker lagring av hemligheter, nycklar och certifikat",
    "difficulty": "intermediate",
    "estimated_minutes": 55,
    "xp_reward": 110,
    "topics_covered": [
        "key vault", "secrets", "keys", "certificates",
        "access policies", "rbac", "integration"
    ],
    "content": """
# Azure Key Vault

> *"Never store secrets in code. Ever."*

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Problem utan Key Vault | Losning med Key Vault |
|----------|------------------------|------------------------|
| Secrets i kod | Credentials i Git-historik | Centraliserad secrets store |
| Rotation | Manuell uppdatering overallt | Automatisk rotation |
| Audit | Ingen sparbarhet | Full access logging |
| Compliance | Svar att bevisa kontroll | RBAC + HSM-stod |

------------------------------------------------------------

## Key Vault Architecture

```
+-----------------------------------------------------------------+
|                    AZURE KEY VAULT                               |
+-----------------------------------------------------------------+
|                                                                  |
|  KEY VAULT: kv-myapp                                            |
|  +----------------------------------------------------------+   |
|  |                                                           |   |
|  |  SECRETS                 KEYS                CERTS       |   |
|  |  +-------------+        +-------------+     +---------+ |   |
|  |  | db-password |        | encryption- |     | ssl-cert| |   |
|  |  | api-key     |        | key         |     | sign-   | |   |
|  |  | conn-string |        | signing-key |     | cert    | |   |
|  |  +-------------+        +-------------+     +---------+ |   |
|  |                                                           |   |
|  +----------------------------------------------------------+   |
|                                                                  |
|  ACCESS CONTROL:                                                |
|  +----------------------------------------------------------+   |
|  |                                                           |   |
|  |  Option 1: Access Policies (vault-level)                 |   |
|  |  +-- User A: Get, List secrets                          |   |
|  |  +-- App B: Get secrets, Sign with keys                 |   |
|  |                                                           |   |
|  |  Option 2: RBAC (Azure RBAC, recommended)               |   |
|  |  +-- Key Vault Secrets User (read secrets)              |   |
|  |  +-- Key Vault Secrets Officer (manage secrets)         |   |
|  |  +-- Key Vault Administrator (full access)              |   |
|  |                                                           |   |
|  +----------------------------------------------------------+   |
|                                                                  |
|  TIERS:                                                         |
|  - Standard: Software-backed keys                               |
|  - Premium: HSM-backed keys (FIPS 140-2 Level 2)               |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Skapa Key Vault

```bash
# Skapa Key Vault
az keyvault create \\
    --name kv-myapp-unique123 \\
    --resource-group rg-demo \\
    --location northeurope \\
    --enable-rbac-authorization true  # Rekommenderat!

# Med soft-delete och purge protection
az keyvault create \\
    --name kv-myapp-prod \\
    --resource-group rg-demo \\
    --location northeurope \\
    --enable-rbac-authorization true \\
    --enable-soft-delete true \\
    --retention-days 90 \\
    --enable-purge-protection true
```

------------------------------------------------------------

## Hantera Secrets

```bash
# Skapa secret
az keyvault secret set \\
    --vault-name kv-myapp \\
    --name "db-password" \\
    --value "SuperSecretP@ssword123"

# Hämta secret
az keyvault secret show \\
    --vault-name kv-myapp \\
    --name "db-password" \\
    --query value -o tsv

# Lista secrets
az keyvault secret list --vault-name kv-myapp --output table

# Uppdatera secret (ny version skapas)
az keyvault secret set \\
    --vault-name kv-myapp \\
    --name "db-password" \\
    --value "NewP@ssword456"

# Lista versioner av en secret
az keyvault secret list-versions \\
    --vault-name kv-myapp \\
    --name "db-password" \\
    --output table

# Hämta specifik version
az keyvault secret show \\
    --vault-name kv-myapp \\
    --name "db-password" \\
    --version "abc123..."

# Soft-delete secret
az keyvault secret delete \\
    --vault-name kv-myapp \\
    --name "db-password"

# Recover deleted secret
az keyvault secret recover \\
    --vault-name kv-myapp \\
    --name "db-password"
```

------------------------------------------------------------

## Access med RBAC

```bash
# Ge app/user access till secrets
az role assignment create \\
    --role "Key Vault Secrets User" \\
    --assignee <principal-id> \\
    --scope /subscriptions/xxx/resourceGroups/rg-demo/providers/Microsoft.KeyVault/vaults/kv-myapp

# Vanliga Key Vault roller:
# - Key Vault Administrator: full access
# - Key Vault Secrets Officer: manage secrets
# - Key Vault Secrets User: read secrets
# - Key Vault Certificates Officer: manage certs
# - Key Vault Crypto Officer: manage keys
# - Key Vault Reader: read metadata only
```

------------------------------------------------------------

## Anvanda i Kod

```python
# Python: Hämta secrets med Managed Identity
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()
client = SecretClient(
    vault_url="https://kv-myapp.vault.azure.net/",
    credential=credential
)

# Hämta secret
db_password = client.get_secret("db-password")
print(f"Password: {db_password.value}")

# Skapa/uppdatera secret
client.set_secret("new-secret", "secret-value")

# Lista secrets
for secret in client.list_properties_of_secrets():
    print(f"Secret: {secret.name}")
```

```csharp
// C#: Hämta secrets
using Azure.Identity;
using Azure.Security.KeyVault.Secrets;

var client = new SecretClient(
    new Uri("https://kv-myapp.vault.azure.net/"),
    new DefaultAzureCredential());

KeyVaultSecret secret = await client.GetSecretAsync("db-password");
Console.WriteLine($"Password: {secret.Value}");
```

------------------------------------------------------------

## Integration med App Service

```bash
# Referera Key Vault secret i App Settings
# Format: @Microsoft.KeyVault(SecretUri=https://kv-myapp.vault.azure.net/secrets/db-password/)

az webapp config appsettings set \\
    --name app-myapp \\
    --resource-group rg-demo \\
    --settings DB_PASSWORD="@Microsoft.KeyVault(VaultName=kv-myapp;SecretName=db-password)"

# App Service Managed Identity måste ha "Key Vault Secrets User" roll!
```

------------------------------------------------------------

## Integration med Azure DevOps

```yaml
# azure-pipelines.yml
# Koppla Key Vault till Variable Group

# 1. Project Settings -> Library -> Variable group
# 2. "Link secrets from an Azure key vault"
# 3. Välj Service Connection och Key Vault
# 4. Authorize och välj secrets

variables:
  - group: 'kv-secrets'  # Linked till Key Vault

steps:
  - script: |
      echo "Using secret in pipeline"
      # $(db-password) är automatiskt maskad i logs
    env:
      DB_PASSWORD: $(db-password)
```

------------------------------------------------------------

## Private Endpoint

```bash
# Disable public access
az keyvault update \\
    --name kv-myapp \\
    --public-network-access Disabled

# Skapa private endpoint
az network private-endpoint create \\
    --name pe-keyvault \\
    --resource-group rg-demo \\
    --vnet-name vnet-myapp \\
    --subnet snet-private \\
    --private-connection-resource-id $(az keyvault show --name kv-myapp --query id -o tsv) \\
    --group-id vault \\
    --connection-name kv-connection
```

------------------------------------------------------------

## Vanliga Problem

### Problem 1: "Access denied" trots RBAC

```bash
# RBAC propagerar inte omedelbart
# Vänta 5-10 minuter eller:
az role assignment list \\
    --assignee <principal-id> \\
    --scope /subscriptions/xxx/.../kv-myapp

# Kontrollera att RBAC är aktiverat
az keyvault show --name kv-myapp --query properties.enableRbacAuthorization
```

------------------------------------------------------------

## Key Takeaways

| Begrepp | Beskrivning |
|---------|-------------|
| Key Vault | Centraliserad secrets, keys, certificates |
| RBAC | Rekommenderat over Access Policies |
| Managed Identity | Basta satt att accessa fran Azure-resurser |
| Key Vault Reference | App Service kan hamta direkt fran KV |
| Soft-delete | Skyddar mot oavsiktlig radering |

**Kom ihag:**
- Aktivera RBAC istallet for Access Policies pa nya vaults
- Anvand @Microsoft.KeyVault() i App Service settings
- Aktivera soft-delete och purge protection for prod
- RBAC-roller kan ta 5-10 minuter att propagera
""",
}


# ============================================================================
# NODE 19: MICROSOFT DEFENDER FOR CLOUD
# ============================================================================

AZURE_NODE_19_DEFENDER = {
    "node_id": 19,
    "title": "Microsoft Defender for Cloud",
    "slug": "azure-defender-cloud",
    "description": "Cloud security posture management och threat protection",
    "difficulty": "advanced",
    "estimated_minutes": 60,
    "xp_reward": 115,
    "topics_covered": [
        "defender for cloud", "security center", "secure score",
        "recommendations", "alerts", "compliance"
    ],
    "content": """
# Microsoft Defender for Cloud

> *"Security that keeps pace with your cloud."*

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Problem utan Defender | Losning med Defender |
|----------|----------------------|----------------------|
| Security posture | Ingen overblick | Secure Score dashboard |
| Misconfiguration | Upptacks vid breach | Proaktiva recommendations |
| Compliance | Manuell audit | Automatiserad compliance check |
| Threat detection | Reaktiv hantering | Real-time alerts |

------------------------------------------------------------

## Defender Architecture

```
+-----------------------------------------------------------------+
|               MICROSOFT DEFENDER FOR CLOUD                       |
+-----------------------------------------------------------------+
|                                                                  |
|  FREE TIER (CSPM Basic):                                        |
|  +----------------------------------------------------------+   |
|  | • Secure Score                                            |   |
|  | • Security recommendations                                |   |
|  | • Azure security best practices                          |   |
|  | • Basic asset inventory                                  |   |
|  +----------------------------------------------------------+   |
|                                                                  |
|  PAID PLANS (CWPP):                                             |
|  +----------------------------------------------------------+   |
|  |                                                           |   |
|  |  Defender for:                                           |   |
|  |  +-------------+ +-------------+ +-------------+        |   |
|  |  |   Servers   | |    SQL      | | Containers  |        |   |
|  |  |   ~$15/mo   | |   ~$15/mo   | |  ~$7/node   |        |   |
|  |  +-------------+ +-------------+ +-------------+        |   |
|  |  +-------------+ +-------------+ +-------------+        |   |
|  |  |   Storage   | | App Service | |  Key Vault  |        |   |
|  |  |  ~$0.02/10k | |  ~$15/inst  | | ~$0.02/10k  |        |   |
|  |  +-------------+ +-------------+ +-------------+        |   |
|  |                                                           |   |
|  |  Features:                                               |   |
|  |  • Just-In-Time VM access                               |   |
|  |  • Adaptive application controls                        |   |
|  |  • File integrity monitoring                            |   |
|  |  • Vulnerability assessment                             |   |
|  |  • Security alerts                                      |   |
|  |                                                           |   |
|  +----------------------------------------------------------+   |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Aktivera Defender

```bash
# Visa pricing tiers
az security pricing list --output table

# Aktivera Defender for Servers
az security pricing create \\
    --name VirtualMachines \\
    --tier Standard

# Aktivera Defender for SQL
az security pricing create \\
    --name SqlServers \\
    --tier Standard

# Aktivera Defender for Containers
az security pricing create \\
    --name Containers \\
    --tier Standard

# Aktivera Defender for Storage
az security pricing create \\
    --name StorageAccounts \\
    --tier Standard

# Visa alla aktiva planer
az security pricing list --query "[?pricingTier=='Standard']" --output table
```

------------------------------------------------------------

## Secure Score

```bash
# Visa Secure Score
az security secure-score list --output table

# Visa score controls
az security secure-score-control list --output table

# Vanliga förbättringsområden:
# - Enable MFA
# - Encrypt data at rest
# - Enable Azure Defender
# - Restrict network access
# - Enable audit logs
```

------------------------------------------------------------

## Security Recommendations

```bash
# Lista alla rekommendationer
az security recommendation list --output table

# Filtrera på severity
az security recommendation list \\
    --query "[?severity=='High']" \\
    --output table

# Exempel på High severity recommendations:
# - "Storage account should use private link"
# - "SQL databases should have vulnerability findings resolved"
# - "VMs should encrypt temp disks and caches"
# - "MFA should be enabled on accounts with owner permissions"
```

------------------------------------------------------------

## Security Alerts

```bash
# Lista security alerts
az security alert list --output table

# Filtrera aktiva alerts
az security alert list \\
    --query "[?status=='Active']" \\
    --output table

# Alert severities:
# - High: Omedelbar action
# - Medium: Snart action
# - Low: Informational

# Dismiss alert
az security alert update \\
    --name <alert-name> \\
    --location <location> \\
    --status "Dismissed"
```

------------------------------------------------------------

## Just-In-Time (JIT) VM Access

```bash
# JIT = temporär port-öppning för SSH/RDP

# Aktivera JIT på VM
az security jit-policy create \\
    --name "jit-vm-myapp" \\
    --resource-group rg-demo \\
    --location northeurope \\
    --virtual-machines '[{
        "id": "/subscriptions/xxx/.../vm-myapp",
        "ports": [{
            "number": 22,
            "protocol": "TCP",
            "allowedSourceAddressPrefix": "*",
            "maxRequestAccessDuration": "PT3H"
        }]
    }]'

# Begär JIT access
az security jit-policy initiate \\
    --name "jit-vm-myapp" \\
    --resource-group rg-demo \\
    --location northeurope \\
    --virtual-machines '[{
        "id": "/subscriptions/xxx/.../vm-myapp",
        "ports": [{
            "number": 22,
            "allowedSourceAddressPrefix": "1.2.3.4",
            "endTimeUtc": "2024-01-01T12:00:00Z"
        }]
    }]'
```

------------------------------------------------------------

## Compliance

```bash
# Lista regulatory compliance standards
az security regulatory-compliance-standards list --output table

# Visa compliance status för specifik standard
az security regulatory-compliance-controls list \\
    --standard-name "Azure-CIS-1.1.0" \\
    --output table

# Built-in standards:
# - Azure CIS
# - NIST SP 800-53
# - ISO 27001
# - PCI-DSS
# - SOC 2
# - HIPAA
```

------------------------------------------------------------

## Export till SIEM

```bash
# Continuous export till Log Analytics
az security automation create \\
    --name "export-to-law" \\
    --resource-group rg-demo \\
    --location northeurope \\
    --scopes "/subscriptions/xxx" \\
    --sources '[{
        "eventSource": "Alerts",
        "ruleSets": []
    }]' \\
    --actions '[{
        "logAnalyticsResourceId": "/subscriptions/xxx/.../law-security",
        "actionType": "LogAnalytics"
    }]'

# Queries i Log Analytics:
# SecurityAlert
# | where TimeGenerated > ago(7d)
# | summarize count() by AlertSeverity
```

------------------------------------------------------------

## Vanliga Problem

### Problem 1: "Secure Score didn't update"

```bash
# Score uppdateras var 24:e timme
# Recommendations kan ta längre tid att refresha

# Tvinga rescan (via Portal):
# Defender for Cloud -> Recommendations -> Refresh
```

------------------------------------------------------------

## Key Takeaways

| Begrepp | Beskrivning |
|---------|-------------|
| Secure Score | Mal pa din sakerhetspostyr (0-100%) |
| Recommendations | Atgardsforslag for att forbattra score |
| Alerts | Real-time notifiering om hot |
| JIT Access | Temporar port-oppning for SSH/RDP |
| Compliance | Automatiserad kontroll mot standards |

**Kom ihag:**
- Free tier ger Secure Score och recommendations
- Paid tier (Defender plans) ger threat protection
- JIT Access eliminerar behovet av oppna management-portar
- Exportera alerts till SIEM for centraliserad overvakning
""",
}


# ============================================================================
# NODE 20: AZURE GOVERNANCE
# ============================================================================

AZURE_NODE_20_GOVERNANCE = {
    "node_id": 20,
    "title": "Azure Governance",
    "slug": "azure-governance",
    "description": "Policy, Blueprints och Cost Management",
    "difficulty": "advanced",
    "estimated_minutes": 55,
    "xp_reward": 110,
    "topics_covered": [
        "azure policy", "blueprints", "management groups",
        "cost management", "tags", "resource locks"
    ],
    "content": """
# Azure Governance

> *"Control without constraints, compliance without complexity."*

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Problem utan Governance | Losning med Governance |
|----------|------------------------|------------------------|
| Compliance | Manuell kontroll | Azure Policy tvingar standarder |
| Kostnader | Ingen budget-kontroll | Budgets med auto-alerts |
| Standardisering | Varje team gor olika | Blueprints for consistency |
| Oavsiktlig radering | Kritiska resurser raderas | Resource Locks |

------------------------------------------------------------

## Governance Hierarchy

```
+-----------------------------------------------------------------+
|                    AZURE GOVERNANCE HIERARCHY                    |
+-----------------------------------------------------------------+
|                                                                  |
|                     +------------------+                        |
|                     |   ROOT TENANT    |                        |
|                     |  (Entra ID)      |                        |
|                     +--------+---------+                        |
|                              |                                   |
|                     +--------▼---------+                        |
|                     | MANAGEMENT GROUP | <- Policies apply here  |
|                     |   (Organization) |                        |
|                     +--------+---------+                        |
|                              |                                   |
|            +-----------------+-----------------+                |
|            |                 |                 |                |
|   +--------▼-------+ +------▼------+ +-------▼------+         |
|   | MANAGEMENT     | | MANAGEMENT  | | MANAGEMENT   |         |
|   | GROUP (Dev)    | | GROUP (Prod)| | GROUP (Shared)|         |
|   +-------+--------+ +------+------+ +------+-------+         |
|           |                 |               |                   |
|   +-------▼--------+ +-----▼-----+  +-----▼-----+             |
|   | SUBSCRIPTION   | |SUBSCRIPTION|  |SUBSCRIPTION|             |
|   | (Dev-Team-A)   | | (Prod)     |  | (Networking)|             |
|   +-------+--------+ +-----+-----+  +-----+-----+             |
|           |                |              |                     |
|   +-------▼--------+ +-----▼-----+  +-----▼-----+             |
|   |RESOURCE GROUPS | |  RGs      |  |   RGs     |             |
|   +----------------+ +-----------+  +-----------+             |
|                                                                  |
|  POLICY INHERITANCE: Top -> Down (Management Group -> Sub -> RG)  |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Azure Policy

```bash
# Lista built-in policies
az policy definition list --query "[?policyType=='BuiltIn']" --output table | head -20

# Vanliga policies:
# - "Allowed locations"
# - "Require tag on resources"
# - "Deny public IP addresses"
# - "Storage accounts should use private link"
# - "Kubernetes cluster should not allow privileged containers"

# Skapa policy assignment
az policy assignment create \\
    --name "require-tags" \\
    --display-name "Require Environment Tag" \\
    --policy "/providers/Microsoft.Authorization/policyDefinitions/871b6d14-10aa-478d-b590-94f262ecfa99" \\
    --scope "/subscriptions/xxx" \\
    --params '{ "tagName": { "value": "Environment" } }'

# Enforce mode (audit vs deny)
# - Disabled: ingen effekt
# - DoNotEnforce: audit only (Default)
# - Default: deny non-compliant

az policy assignment create \\
    --name "deny-public-ips" \\
    --policy "xxx" \\
    --scope "/subscriptions/xxx" \\
    --enforcement-mode Default  # Deny!
```

------------------------------------------------------------

## Custom Policy

```json
// custom-policy-deny-public-storage.json
{
  "mode": "All",
  "policyRule": {
    "if": {
      "allOf": [
        {
          "field": "type",
          "equals": "Microsoft.Storage/storageAccounts"
        },
        {
          "field": "Microsoft.Storage/storageAccounts/allowBlobPublicAccess",
          "equals": true
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
# Skapa custom policy definition
az policy definition create \\
    --name "deny-public-blob" \\
    --display-name "Deny Public Blob Access" \\
    --description "Prevents storage accounts from allowing public blob access" \\
    --rules custom-policy-deny-public-storage.json \\
    --mode All

# Assign custom policy
az policy assignment create \\
    --name "deny-public-blob-assignment" \\
    --policy "deny-public-blob" \\
    --scope "/subscriptions/xxx"
```

------------------------------------------------------------

## Management Groups

```bash
# Skapa management group hierarchy
az account management-group create --name "mg-organization"
az account management-group create --name "mg-production" --parent "mg-organization"
az account management-group create --name "mg-development" --parent "mg-organization"

# Flytta subscription till management group
az account management-group subscription add \\
    --name "mg-production" \\
    --subscription "xxx-subscription-id"

# Assign policy på management group level
az policy assignment create \\
    --name "org-wide-tags" \\
    --policy "xxx" \\
    --scope "/providers/Microsoft.Management/managementGroups/mg-organization"

# Nu gäller policyn för ALLA subscriptions under mg-organization!
```

------------------------------------------------------------

## Resource Locks

```bash
# Prevent accidental deletion
az lock create \\
    --name "no-delete" \\
    --resource-group rg-production \\
    --lock-type CanNotDelete

# Prevent all changes (read-only)
az lock create \\
    --name "read-only" \\
    --resource-group rg-production \\
    --lock-type ReadOnly

# Lock på specifik resurs
az lock create \\
    --name "protect-db" \\
    --resource-group rg-production \\
    --resource-type "Microsoft.Sql/servers" \\
    --resource "sql-production" \\
    --lock-type CanNotDelete

# Lista locks
az lock list --resource-group rg-production --output table

# Ta bort lock (krävs för att radera resursen)
az lock delete --name "no-delete" --resource-group rg-production
```

------------------------------------------------------------

## Cost Management

```bash
# Visa current spend
az consumption usage list \\
    --query "[].{Resource:instanceName, Cost:pretaxCost}" \\
    --output table

# Skapa budget
az consumption budget create \\
    --budget-name "monthly-budget" \\
    --amount 1000 \\
    --time-grain Monthly \\
    --time-period "Start=2024-01-01,End=2024-12-31" \\
    --resource-group rg-demo \\
    --category Cost

# Budget med notifications
az consumption budget create \\
    --budget-name "team-a-budget" \\
    --amount 500 \\
    --time-grain Monthly \\
    --notifications '[{
        "enabled": true,
        "operator": "GreaterThan",
        "threshold": 80,
        "contactEmails": ["admin@company.com"],
        "thresholdType": "Actual"
    }]'
```

------------------------------------------------------------

## Tags

```bash
# Tagging strategy
# - Environment: dev, test, prod
# - CostCenter: 123, 456
# - Owner: team@company.com
# - Project: project-name

# Tagga resurs
az resource tag \\
    --tags Environment=prod CostCenter=123 Owner=devops@company.com \\
    --resource-group rg-demo \\
    --name app-myapp \\
    --resource-type "Microsoft.Web/sites"

# Tagga resource group
az group update \\
    --name rg-demo \\
    --tags Environment=prod CostCenter=123

# Inherit tags med policy
# Built-in policy: "Inherit a tag from the resource group"
az policy assignment create \\
    --name "inherit-environment-tag" \\
    --policy "cd3aa116-8754-49c9-a813-ad46512ece54" \\
    --scope "/subscriptions/xxx" \\
    --params '{ "tagName": { "value": "Environment" } }'
```

------------------------------------------------------------

## Azure Blueprints (Preview)

```bash
# Blueprints = template för hela miljöer
# Innehåller: Policies + RBAC + ARM templates

# Skapa blueprint (via Portal rekommenderat)
# 1. All services -> Blueprints -> Create blueprint
# 2. Lägg till artifacts: Policy, Role assignment, ARM template
# 3. Publish blueprint
# 4. Assign blueprint till subscription

# CLI (limited support)
az blueprint create \\
    --name "compliant-environment" \\
    --description "Compliant dev environment" \\
    --management-group "mg-organization"
```

------------------------------------------------------------

## Vanliga Problem

### Problem 1: "Policy blocks deployment"

```bash
# Check compliance status
az policy state list \\
    --resource-group rg-demo \\
    --query "[?complianceState=='NonCompliant']" \\
    --output table

# Exemption för specifik resurs
az policy exemption create \\
    --name "temp-exemption" \\
    --policy-assignment "xxx" \\
    --exemption-category Waiver \\
    --scope "/subscriptions/xxx/resourceGroups/rg-demo"
```

------------------------------------------------------------

## Key Takeaways

| Begrepp | Beskrivning |
|---------|-------------|
| Management Groups | Hierarkisk access over subscriptions |
| Azure Policy | Tvinga compliance (audit eller deny) |
| Resource Locks | Skydda mot oavsiktlig radering/andring |
| Cost Management | Budgets med automatiska alerts |
| Tags | Organisera och spara kostnader |

**Kom ihag:**
- Policies arver nedat i scope-hierarkin
- Anvand Audit-mode forst, sedan Deny
- Resource Locks maste tas bort innan resurs kan raderas
- Tagga ALLA resurser for kostnadsrapportering
""",
}


# Export all nodes from Block 5
BLOCK_5_NODES = [
    AZURE_NODE_17_ENTRA,
    AZURE_NODE_18_KEYVAULT,
    AZURE_NODE_19_DEFENDER,
    AZURE_NODE_20_GOVERNANCE,
]
