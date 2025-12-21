"""
Azure Cloud Mastery - Camp DevOps format
20 noder med å/ä/ö bevarade.
"""

MODULE = {
    "name": "Azure Cloud Mastery",
    "slug": "azure-mastery-v2",
    "description": "Praktisk Azure för DevOps: identitet, nätverk, compute, IaC, säkerhet och drift",
    "track_slug": "cloud",
    "order_index": 200,
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "prerequisites": ["linux-mastery"],
    "icon": "☁️",
    "color": "#0078D4",
    "tasks": [
        {
            "title": "Azure Fundamentals & Architecture",
            "slug": "azure-fundamentals-architecture",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Azure Fundamentals & Architecture

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför Azure är viktigt |
|----------|-------------------------|
| **Hybrid/enterprise** | Vanligt val för organisationer med Microsoft-stack |
| **Identity-first** | Entra ID (Azure AD) styr åtkomst och policy överallt |
| **Governance** | Policy, budget och compliance sätts centralt via ARM |
| **Plattform för DevOps** | Azure DevOps/GitHub + AKS + ACR ger hel kedja |

Du behöver förstå:

- **Kontrollplanet (ARM)** som alla verktyg använder
- **Regionala resurser och zoner** för tillgänglighet och latency
- **Prenumerationer och management groups** för isolation och billing

------------------------------------------------------------

## Huvudinnehåll

+-------------------------------------------------------------+
|                    Azure Resource Model                     |
+-------------------------------------------------------------+
| Management Group -> Subscription -> Resource Group -> Resource |
|               Region/Zoner sätter HA och latency            |
+-------------------------------------------------------------+

| Princip | Förklaring |
|---------|------------|
| **ARM** | Deklarativt API och kontrollplan som alla klienter använder |
| **Resource Group** | Livscykel- och åtkomstgräns för resurser |
| **Region & AZ** | Region = geoplats, AZ = datacenter-zon för HA |
| **Tags** | Nyckel/värde för kost, ägare, miljö |
| **RBAC** | Rollbaserad åtkomst via Entra ID |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az account show` | Visa aktiv prenumeration |
| `az account set --subscription <id>` | Byt prenumeration |
| `az group create -n rg-demo -l westeurope` | Skapa resource group |
| `az resource list --tag env=dev` | Lista resurser efter tag |
| `az deployment group create ...` | Deploya ARM/Bicep till RG |

------------------------------------------------------------

## Praktiska exempel

```bash
# Logga in och välj prenumeration
az login
az account set --subscription "$SUB"

# Skapa en resursgrupp med taggar
az group create \
  --name rg-app-dev \
  --location westeurope \
  --tags env=dev owner=platform

# Lista resurser i gruppen
az resource list --resource-group rg-app-dev --output table
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **ARM** | Kontrollplanen alla verktyg använder |
| **Resource Group** | Samlar resurser med gemensam livscykel |
| **Taggar** | Gör kost, ägare och miljö spårbara |
| **Region/Zon** | Plats och tillgänglighetsnivå |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `AuthorizationFailed` | Fel roll eller scope | Kontrollera RBAC och byt konto/prenumeration |
| `RequestDisallowedByPolicy` | Policy blockerar resurs | Läs `policyDefinitionDisplayName`, justera resurs eller ansök om undantag |
| `LocationNotAvailableForResourceType` | Tjänst ej i regionen | Välj annan region eller SKU |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **ARM är navet** | All åtkomst och IaC går via ARM |
| **Strukturera rätt** | MG/Subscription/RG bestämmer åtkomst och kost |
| **Tagga tidigt** | Taggar behövs för kost, ägande och policy |
| **Regionval** | Påverkar latency, HA och tjänstetillgänglighet |
""",
        },
        {
            "title": "Resource Groups & RBAC grunder",
            "slug": "azure-resource-groups-rbac",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Resource Groups & RBAC

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|--------|
| **Isolera miljöer** | RG som livscykelgräns för dev/test/prod |
| **Åtkomstkontroll** | RBAC per RG för team och tjänster |
| **IaC** | All provisioning adresserar RG |

------------------------------------------------------------

## Huvudinnehåll

+-------------------------------------------------------------+
| Resource Group -> Innehåller resurser, tags, åtkomst         |
| RBAC -> Roll + principal + scope                             |
+-------------------------------------------------------------+

| Princip | Förklaring |
|---------|------------|
| **Scope** | MG -> Sub -> RG -> Resurs |
| **Built-in roles** | Reader, Contributor, Owner |
| **Custom roles** | Egen JSON-definition |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az group create -n rg-app -l westeurope` | Skapa RG |
| `az role assignment create --assignee ... --role Reader --scope ...` | Tilldela roll |
| `az role definition list` | Visa inbyggda roller |

------------------------------------------------------------

## Praktiska exempel

```bash
az group create -n rg-api-dev -l westeurope --tags env=dev owner=platform
az role assignment create \
  --assignee user@company.com \
  --role Reader \
  --scope /subscriptions/$SUB/resourceGroups/rg-api-dev
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Scope** | Var rollen gäller |
| **Role Definition** | Behörigheter |
| **Role Assignment** | Knyt identitet till roll |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `AuthorizationFailed` | Fel scope | Sätt korrekt subscription/RG |
| `Insufficient privileges` | Identitet saknar rätt roll | Tilldela minst Contributor där det behövs |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Scope styr** | Tilldela på minsta nödvändiga nivå |
| **Tagga RG** | Kost och ägande spåras här |
| **RBAC före access** | Skapa roller innan deploy |
""",
        },
        {
            "title": "Governance: Policy & Management Groups",
            "slug": "azure-governance-policy",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Governance: Policy & Management Groups

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Guardrails i CI/CD** | Policy stoppar fel resurstyper/regioner |
| **Compliance** | ISO/SOC kräver kontroller och evidens |
| **Skalbar styrning** | Management groups sätter standard över subscriptions |

------------------------------------------------------------

## Huvudinnehåll

| Komponent | Beskrivning |
|-----------|-------------|
| **Management Group** | Hierarki ovanför subscriptions |
| **Policy** | Deklarativt regelverk (deny, audit, append, deployIfNotExists) |
| **Initiative** | Samling av policies |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az policy definition list` | Visa policies |
| `az policy assignment create ...` | Tilldela policy |
| `az account management-group create ...` | Skapa MG |

------------------------------------------------------------

## Praktiska exempel

```bash
az account management-group create --name mg-landingzones
az policy assignment create \
  --name require-tags \
  --scope /subscriptions/$SUB/resourceGroups/rg-app-dev \
  --policy "$(az policy definition list --query \"[?contains(displayName,'Inherit a tag')].name\" -o tsv)" \
  --params '{"tagName":{"value":"env"}}'
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Policy** | Regel som utvärderas vid deploy och efteråt |
| **Initiative** | Policy-samling för ett mål |
| **Management Group** | Organiserar subscriptions |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `RequestDisallowedByPolicy` | Policy blockerar resurs | Läs `policyDefinitionDisplayName` och justera resurs eller undantag |
| `AssignmentDenied` | Fel scope eller roll | Se till att du har `Owner`/`Contributor` på scope |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Policy före drift** | Sätt guardrails innan du provisionerar |
| **Hierarki** | MG -> Subscription -> RG ger kontroll per nivå |
| **Tag enforcement** | Gör kost och ägande spårbart |
""",
        },
        {
            "title": "Identitet: Entra ID och Service Principals",
            "slug": "azure-identity-entra",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Identitet: Entra ID och Service Principals

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|--------|
| **CI/CD** | Service principals för pipelines och IaC |
| **Zero trust** | MFA/Conditional Access styr åtkomst |
| **RBAC** | All access kopplas mot Entra-principals |

------------------------------------------------------------

## Huvudinnehåll

| Begrepp | Förklaring |
|---------|------------|
| **User/Group** | Mänskliga identiteter |
| **Service Principal** | App-identitet för automation |
| **Managed Identity** | Id för Azure-resurser |
| **App Registration** | Definierar SPN och API-behörigheter |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az ad sp create-for-rbac ...` | Skapa service principal |
| `az identity create ...` | Skapa managed identity |
| `az role assignment create ...` | Tilldela roll till SPN/MI |

------------------------------------------------------------

## Praktiska exempel

```bash
# Skapa service principal för IaC
az ad sp create-for-rbac \
  --name spn-iac \
  --role Contributor \
  --scopes /subscriptions/$SUB/resourceGroups/rg-app-dev \
  --sdk-auth > spn-iac.json

# Skapa user-assigned managed identity
az identity create \
  --name mi-aks \
  --resource-group rg-app-dev \
  --location westeurope
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **SPN** | Icke-mänsklig identitet för appar |
| **Managed Identity** | Automatiskt roterade hemligheter |
| **Conditional Access** | Policys för inloggning |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `AADSTS700016` | App ej registrerad | Skapa app registration eller kontrollera namn |
| `Insufficient privileges to complete the operation` | Saknar Directory.ReadWrite | Be admin om rätt behörighet |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Identitet först** | All åtkomst går via Entra ID |
| **Använd MI** | Slipp hantera hemligheter manuellt |
| **Minsta behörighet** | Tilldela roller på rätt scope |
""",
        },
        {
            "title": "Nätverk: VNet, Subnets, Peering, Private Endpoints",
            "slug": "azure-networking-basics",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Nätverk: VNet, Subnets, Peering, Private Endpoints

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Säkra tjänster** | Private endpoints stänger publikt ingress |
| **Hybrid** | VPN/ExpressRoute kräver rätt adressplan |
| **Kubernetes** | AKS och ACR behöver nätverksdesign |

------------------------------------------------------------

## Huvudinnehåll

| Begrepp | Beskrivning |
|---------|------------|
| **VNet** | Isolerat nät i Azure |
| **Subnet** | Uppdelning av VNet för segmentering |
| **NSG** | Brandväggsregler per subnet/nic |
| **Peering** | Länka två VNets med privat routing |
| **Private Endpoint** | Privat åtkomst till PaaS-tjänst |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az network vnet create ...` | Skapa VNet och subnet |
| `az network vnet peering create ...` | Skapa peering |
| `az network private-endpoint create ...` | Skapa private endpoint |

------------------------------------------------------------

## Praktiska exempel

```bash
# Skapa VNet med två subnät
az network vnet create \
  --name vnet-app \
  --resource-group rg-app-dev \
  --address-prefix 10.10.0.0/16 \
  --subnet-name snet-app \
  --subnet-prefix 10.10.1.0/24

# Peering mellan hub och spoke
az network vnet peering create \
  --name hub-to-app \
  --resource-group rg-hub \
  --vnet-name vnet-hub \
  --remote-vnet /subscriptions/$SUB/resourceGroups/rg-app-dev/providers/Microsoft.Network/virtualNetworks/vnet-app \
  --allow-vnet-access
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **NSG** | L4 brandvägg |
| **UDR** | Custom routes |
| **Private DNS** | Namn för privata endpoints |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `AddressPrefixConflict` | Överlappande CIDR | Planera IP-plan och undvik overlap |
| `PeeringFailed` | Ej tillåten kombination | Kontrollera allow-forwarded/allow-gateway |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Planera IP** | Starta med adressplan för hub/spoke |
| **Privat åtkomst** | Använd private endpoints för PaaS |
| **NSG + UDR** | Styr trafik och segmentera |
""",
        },
        {
            "title": "Hybridkoppling: VPN, ExpressRoute, Private DNS",
            "slug": "azure-hybrid-connectivity",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Hybridkoppling: VPN, ExpressRoute, Private DNS

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Hybrid appar** | On-prem behöver prata med Azure-resurser |
| **Säkra vägar** | Undvik publik exponering |
| **DNS** | Namnupplösning krävs för privata endpoints |

------------------------------------------------------------

## Huvudinnehåll

| Komponent | Beskrivning |
|-----------|-------------|
| **Site-to-Site VPN** | IPSec-tunnel via internet |
| **ExpressRoute** | Privat krets med SLA |
| **Private DNS Zones** | Hanterar namn för privata endpoints |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az network vnet-gateway create ...` | Skapa VPN-gateway |
| `az network vpn-connection create ...` | Skapa tunnel |
| `az network private-dns zone create ...` | Private DNS zon |

------------------------------------------------------------

## Praktiska exempel

```bash
# Private DNS zone för storage
az network private-dns zone create \
  --resource-group rg-hub \
  --name privatelink.blob.core.windows.net

# Länka zon till VNet
az network private-dns link vnet create \
  --resource-group rg-hub \
  --zone-name privatelink.blob.core.windows.net \
  --name link-hub \
  --virtual-network /subscriptions/$SUB/resourceGroups/rg-hub/providers/Microsoft.Network/virtualNetworks/vnet-hub \
  --registration-enabled false
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **VPN Gateway** | Krypterad tunnel |
| **ExpressRoute** | Privat linje med SLA |
| **Private DNS** | Namn för privata endpoints |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `GatewayNotFound` | Ingen gateway i VNet | Skapa gateway-subnet och gateway |
| DNS-resolver löser ej namn | Private DNS ej länkat | Länka zon till VNet |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Privat först** | Stäng publika endpoints där det går |
| **DNS är kritiskt** | Länka Private DNS till alla VNets |
| **SLA** | ExpressRoute för stabilitet och låg latency |
""",
        },
        {
            "title": "Compute: VM och Scale Sets",
            "slug": "azure-compute-vm-vmss",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Compute: VM och Scale Sets

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Lyfta & skifta** | Många appar börjar som VM |
| **Autoskalning** | VMSS ger elasticitet |
| **Image-hygien** | Golden images med Packer |

------------------------------------------------------------

## Huvudinnehåll

| Begrepp | Förklaring |
|---------|------------|
| **VM** | Virtuell server |
| **VMSS** | Autoskalande uppsättning |
| **Images** | Marketplace, Shared Image Gallery |
| **Extensions** | CustomScript/AMA/DependencyAgent |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az vm create ...` | Skapa VM |
| `az vmss create ...` | Skapa VM scale set |
| `az sig image-definition create ...` | Image Gallery definition |

------------------------------------------------------------

## Praktiska exempel

```bash
# Skapa VM
az vm create \
  --resource-group rg-app-dev \
  --name vm-api \
  --image Ubuntu2204 \
  --size Standard_B2ms \
  --vnet-name vnet-app \
  --subnet snet-app \
  --generate-ssh-keys

# Skapa VMSS med autoscale
az vmss create \
  --resource-group rg-app-dev \
  --name vmss-web \
  --image Ubuntu2204 \
  --upgrade-policy-mode automatic \
  --instance-count 2 \
  --vm-sku Standard_B2ms
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **VMSS** | Autoskalning av VM |
| **SIG** | Shared Image Gallery |
| **Extensions** | Efterkonfig av VM |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `AllocationFailed` | SKU ej tillgänglig i zon | Byt zon/SKU |
| Provisioning timeout | CustomScript fel | Kolla extension-loggar |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Automatisera** | Använd cloud-init/Extensions för idempotent setup |
| **Image-hygien** | SIG + Packer för reproducerbara baser |
| **Autoskalning** | VMSS med metriker eller schema |
""",
        },
        {
            "title": "Storage: Blob, File, Lifecycle",
            "slug": "azure-storage-blob-file",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 60,
            "content": """# Storage: Blob, File, Lifecycle

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Stateful tjänster** | Lagring av artefakter/loggar |
| **Backup** | Säkra data över tid |
| **Kost** | Tiering spar pengar |

------------------------------------------------------------

## Huvudinnehåll

| Tjänst | Användning |
|--------|------------|
| **Blob** | Objektlagring, versioner, immutability |
| **File** | SMB/NFS shares |
| **Lifecycle** | Flytta data mellan hot/cool/archive |
| **SAS** | Delad åtkomsttoken |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az storage account create ...` | Skapa lagringskonto |
| `az storage blob upload ...` | Ladda upp blob |
| `az storage share-rm create ...` | Skapa fileshare |

------------------------------------------------------------

## Praktiska exempel

```bash
az storage account create \
  --name saappdev$RANDOM \
  --resource-group rg-app-dev \
  --sku Standard_LRS \
  --kind StorageV2 \
  --https-only true

az storage container create --account-name saappdev --name artifacts --auth-mode login
az storage blob upload --account-name saappdev --container-name artifacts --name app.tar.gz --file app.tar.gz --auth-mode login
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **SAS** | Tidsbegränsad åtkomsttoken |
| **Immutability** | Skydd mot radering/ändring |
| **Lifecycle** | Automatiskt tier-byte |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `AuthorizationPermissionMismatch` | Fel auth-läge | Använd `--auth-mode login` eller SAS |
| NFS mount misslyckas | Fel subnet eller protokoll | Aktivera NFS och tillåt subnet i nätverk |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Rätt konto-typ** | Premium för IOPS, Standard för billig volym |
| **Säker åtkomst** | Private endpoints + SAS |
| **Livscykel** | Tiera data för kostoptimering |
""",
        },
        {
            "title": "Data: SQL, PostgreSQL, Backup",
            "slug": "azure-data-services",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Data: SQL, PostgreSQL, Backup

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **PaaS databaser** | Mindre drift, mer fokus på schema |
| **Säkerhet** | Private endpoints + audit |
| **Backup/DR** | Geo-redundans och PITR |

------------------------------------------------------------

## Huvudinnehåll

| Tjänst | Användning |
|--------|------------|
| **Azure SQL DB** | Relations-PaaS, autoskalning |
| **SQL MI** | Nära SQL Server-kompatibilitet |
| **PostgreSQL Flexible** | OSS-PaaS med AZ-stöd |
| **Backup** | PITR och geo-restore |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az sql server create ...` | Skapa SQL server |
| `az sql db create ...` | Skapa databasen |
| `az postgres flexible-server create ...` | Skapa Postgres |

------------------------------------------------------------

## Praktiska exempel

```bash
az sql server create \
  --name sql-app-dev \
  --resource-group rg-app-dev \
  --location westeurope \
  --admin-user sqladmin \
  --admin-password "P@ssw0rd!"

az sql db create \
  --name appdb \
  --resource-group rg-app-dev \
  --server sql-app-dev \
  --compute-model Serverless \
  --edition GeneralPurpose \
  --family Gen5 \
  --capacity 2
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **DTU/vCore** | Prestandamodeller |
| **PITR** | Point-in-time-restore |
| **Geo-redundans** | Kopia i annan region |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `Firewall rule not found` | IP blockerad | Lägg till VNet/firewall-regel |
| Timeout mot DB | Ingen private endpoint/DNS | Lägg till PE + Private DNS |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Privat åtkomst** | Använd private endpoints + DNS |
| **Backup** | Ställ in retention och testa restore |
| **Skalning** | Välj rätt compute-modell (serverless/elastic) |
""",
        },
        {
            "title": "Säkerhet: Key Vault och hemligheter",
            "slug": "azure-security-keyvault",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 60,
            "content": """# Säkerhet: Key Vault och hemligheter

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **CI/CD** | Hemligheter för deployments |
| **Runtime** | Appar behöver nycklar/certs säkert |
| **Rotation** | Automatiskt byte av nycklar/certs |

------------------------------------------------------------

## Huvudinnehåll

| Begrepp | Förklaring |
|---------|------------|
| **Vault** | Lagrar secrets, keys, certs |
| **Access policy/RBAC** | Styr åtkomst |
| **Managed Identity** | Hämtar secrets utan lösen |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az keyvault create ...` | Skapa vault |
| `az keyvault secret set ...` | Sätt secret |
| `az keyvault secret show ...` | Läs secret |

------------------------------------------------------------

## Praktiska exempel

```bash
az keyvault create --name kv-app-dev --resource-group rg-app-dev --location westeurope
az keyvault secret set --vault-name kv-app-dev --name db-password --value "P@ssw0rd!"

# Ge MI åtkomst
az keyvault set-policy \
  --name kv-app-dev \
  --object-id $(az identity show -g rg-app-dev -n mi-aks --query principalId -o tsv) \
  --secret-permissions get list
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Secret** | Nyckel/värde |
| **Access Policy** | Rättigheter på vault |
| **Private Endpoint** | Privat åtkomst |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `Forbidden` | Saknar rätt policy/RBAC | Lägg till MI/SPN med rättigheter |
| DNS-resolver når ej vault | Ingen private DNS | Lägg till privatelink.vaultcore.azure.net |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Aldrig plaintext** | Använd vault för alla hemligheter |
| **MI** | Slipp hantera hemligheter i kod |
| **Privat åtkomst** | PE + DNS ger zero trust |
""",
        },
        {
            "title": "Container Registry (ACR) och bilder",
            "slug": "azure-acr-container-images",
            "difficulty": "medium",
            "estimated_minutes": 35,
            "xp_reward": 60,
            "content": """# Container Registry (ACR) och bilder

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Supply chain** | Kontrollera bilder och signering |
| **AKS/Apps** | ACR som privat registry |
| **CI/CD** | Push/pull med token/MI |

------------------------------------------------------------

## Huvudinnehåll

| Begrepp | Förklaring |
|---------|------------|
| **ACR SKU** | Basic/Standard/Premium (geo-repl) |
| **Tasks** | Inbyggda bygg/scan-jobb |
| **Content Trust** | Signering |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az acr create ...` | Skapa registry |
| `az acr login ...` | Logga in |
| `az acr task create ...` | Bygg/scan |

------------------------------------------------------------

## Praktiska exempel

```bash
az acr create --name acrappdev --resource-group rg-app-dev --sku Standard
az acr login --name acrappdev

# Bygg och push med ACR Tasks
az acr build --registry acrappdev --image api:1.0 .
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **ACR Tasks** | CI i registry |
| **Admin user** | Undvik i produktion, använd MI |
| **Private Link** | Privat åtkomst |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `DENIED: client unauthorized` | Saknar rätt roll | Tilldela `AcrPull`/`AcrPush` |
| Pull timeout från AKS | Saknar PE/DNS | Lägg till private endpoint och DNS |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Äg dina bilder** | ACR + signering |
| **Minsta åtkomst** | AcrPull/AcrPush per workload |
| **Privat trafik** | Private Link + DNS |
""",
        },
        {
            "title": "AKS grunder",
            "slug": "azure-aks-basics",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# AKS grunder

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Containerplattform** | Standard för mikrotjänster |
| **GitOps** | Integrerar med Flux/Argo |
| **Nätverk/säkerhet** | Kräver rätt design med PE/NSG |

------------------------------------------------------------

## Huvudinnehåll

| Begrepp | Förklaring |
|---------|------------|
| **Nodepool** | VMSS-baserade noder |
| **CNI** | Azure CNI (VNet integrerat) |
| **Ingress** | NGINX/App Gateway Ingress Controller |
| **AAD integration** | RBAC mot Entra |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az aks create ...` | Skapa AKS |
| `az aks get-credentials ...` | Hämta kubeconfig |
| `az aks nodepool add ...` | Lägg till pool |

------------------------------------------------------------

## Praktiska exempel

```bash
az aks create \
  --resource-group rg-app-dev \
  --name aks-app \
  --node-count 2 \
  --node-vm-size Standard_DS2_v2 \
  --network-plugin azure \
  --enable-managed-identity \
  --attach-acr acrappdev

az aks get-credentials --resource-group rg-app-dev --name aks-app
kubectl get nodes
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **CNI** | Nätmodell, pods får VNet-IP |
| **Nodepool** | VMSS-grupp |
| **AGIC** | App Gateway Ingress Controller |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| Pod IP tar slut | För liten subnet | Planera större prefix |
| `ImagePullBackOff` | Saknar ACR-rätt | `--attach-acr` eller MI med AcrPull |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Planera IP** | VNet/CNI kräver adressutrymme |
| **Integrera ACR** | Sätt pull-rättigheter från start |
| **RBAC** | Använd AAD-RBAC i klustret |
""",
        },
        {
            "title": "Pipelines: Azure DevOps och GitHub Actions",
            "slug": "azure-pipelines-ci-cd",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Pipelines: Azure DevOps och GitHub Actions

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **CI/CD** | Bygg, testa, deploya till Azure |
| **Service Principals** | Säker auth mot Azure |
| **Miljöer** | Gates och approvals |

------------------------------------------------------------

## Huvudinnehåll

| Begrepp | Förklaring |
|---------|------------|
| **ADO Pipelines** | YAML-baserad automation |
| **GitHub Actions** | Workflows i repo |
| **Service Connection** | SPN + rättigheter |
| **Self-hosted runner** | Behövs för privata nät |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az devops service-endpoint azurerm create ...` | Skapa service connection |
| `az pipelines create ...` | Skapa pipeline |

------------------------------------------------------------

## Praktiska exempel

```yaml
# .github/workflows/deploy.yaml
name: Deploy
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}
      - run: az deployment group create --resource-group rg-app-dev --template-file main.bicep
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Service Connection** | SPN för pipelines |
| **Secrets store** | GitHub Secrets/ADO Library |
| **Gates** | Approvals/checks |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `invalid_client` vid login | Fel klientid/hemlighet | Regenerera SPN-sekret |
| Timeout mot privata resurser | Runner saknar nätåtkomst | Använd self-hosted runner i VNet |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Automatisera allt** | Kodad pipeline + IaC |
| **Säkra secrets** | I Key Vault + pipeline integration |
| **Miljö-gates** | Stoppa fel deployer till prod |
""",
        },
        {
            "title": "IaC: Bicep",
            "slug": "azure-iac-bicep",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# IaC: Bicep

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **ARM-native** | Bicep kompilerar till ARM |
| **Snabb feedback** | Bra språkstöd och linters |
| **Moduler** | Återanvändbara block |

------------------------------------------------------------

## Huvudinnehåll

| Begrepp | Förklaring |
|---------|------------|
| **Parameter** | Inputvärden |
| **Output** | Returnerar värden till pipeline |
| **Module** | Återanvändbart Bicep-block |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az bicep build --file main.bicep` | Kompilera |
| `az deployment group create ...` | Deploya |

------------------------------------------------------------

## Praktiska exempel

```bicep
// main.bicep
param location string = resourceGroup().location
resource rgSa 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: 'saapp${uniqueString(resourceGroup().id)}'
  location: location
  kind: 'StorageV2'
  sku: { name: 'Standard_LRS' }
}
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **what-if** | Visa plan före deploy |
| **modules** | Återanvändbarhet |
| **targetScope** | rg/subscription |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `BCP`-fel | Syntaxfel | Kör `az bicep build` lokalt |
| `DeploymentFailed` | Policy blockerar | Läs errorDetails och justera |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Declarativt** | Lätt att granska och versionera |
| **what-if** | Få plan innan ändring |
| **Moduler** | Skapa bibliotek för teamet |
""",
        },
        {
            "title": "IaC: Terraform i Azure",
            "slug": "azure-iac-terraform",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# IaC: Terraform i Azure

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Multi-cloud** | Samma verktyg för flera moln |
| **State** | Lagra i remote backend |
| **Moduler** | Återanvändbar kod |

------------------------------------------------------------

## Huvudinnehåll

| Begrepp | Förklaring |
|---------|------------|
| **Backend** | Ex. azurerm med storage + SAS |
| **Provider** | azurerm-versioner |
| **Module** | Återanvändbar Terraform-kod |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `terraform init` | Initiera backend |
| `terraform plan` | Planera |
| `terraform apply` | Köra |

------------------------------------------------------------

## Praktiska exempel

```hcl
# backend
terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tfstate"
    storage_account_name = "satfstate"
    container_name       = "tfstate"
    key                  = "app.tfstate"
  }
}

provider "azurerm" {
  features {}
}
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **State lock** | Hindrar race conditions |
| **Workspace** | Isolera miljöer |
| **Vars** | Använd tfvars + Key Vault |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `Error acquiring state lock` | Lås kvar | Släpp lås i storage eller vänta |
| `ExpiredToken` | Kortlivad token | Logga in igen eller använd federated identity |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Remote state** | Lagra säkert i storage med lås |
| **Versionera provider** | Lås versioner för reproducibilitet |
| **Automatisera** | Kör i pipeline med SPN/Workload Identity |
""",
        },
        {
            "title": "Observability: Monitor, Log Analytics, App Insights",
            "slug": "azure-observability",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Observability: Monitor, Log Analytics, App Insights

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Incidenthantering** | Samla loggar och metriker |
| **SLO/SLA** | Mäta latency och fel |
| **Kost** | Optimera resurser via metriker |

------------------------------------------------------------

## Huvudinnehåll

| Komponent | Beskrivning |
|-----------|-------------|
| **Log Analytics** | Kusto-baserad loggsamling |
| **Application Insights** | APM för appar |
| **Alerts** | Regler + action groups |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az monitor log-analytics workspace create ...` | Skapa LA |
| `az monitor app-insights component create ...` | Skapa App Insights |
| `az monitor metrics alert create ...` | Skapa alert |

------------------------------------------------------------

## Praktiska exempel

```bash
az monitor log-analytics workspace create --resource-group rg-app-dev --workspace-name law-app-dev
az monitor app-insights component create --app appinsights-dev --location westeurope --resource-group rg-app-dev --workspace law-app-dev

# Alert på CPU > 80%
az monitor metrics alert create \
  --name cpu-high \
  --resource-group rg-app-dev \
  --scopes $(az vm show -g rg-app-dev -n vm-api --query id -o tsv) \
  --condition "max Percentage CPU > 80" \
  --window-size 5m
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **KQL** | Frågespråk för Log Analytics |
| **Action Group** | Mottagare (mail/webhook/ITSM) |
| **Diagnostic settings** | Skicka loggar till LA/Event Hub/Storage |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| Inga loggar i LA | Diagnostic settings saknas | Aktivera per resurs |
| Dubbelbilling | Både App Insights klassisk + workspace | Använd workspace-läget |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Central loggning** | Skicka allt till LA |
| **Alert hygiene** | Få signal, inte brus |
| **Bygg dashboards** | KQL + workbooks för team |
""",
        },
        {
            "title": "Kost och budget",
            "slug": "azure-cost-management",
            "difficulty": "easy",
            "estimated_minutes": 30,
            "xp_reward": 55,
            "content": """# Kost och budget

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Finops** | DevOps ansvarar för kostdisciplin |
| **Miljöer** | Dev vs prod kräver olika policys |
| **Autoskalning** | Undvik överprovisionering |

------------------------------------------------------------

## Huvudinnehåll

| Begrepp | Förklaring |
|---------|------------|
| **Budget** | Larm vid kostnadstak |
| **Cost Alerts** | Mail/webhook vid tröskel |
| **Tags** | Kostallokering |
| **Reservations** | Rabatt på långvarig användning |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az consumption budget create ...` | Skapa budget |
| `az tag create/update` | Hantera taggar |

------------------------------------------------------------

## Praktiska exempel

```bash
az consumption budget create \
  --amount 500 \
  --category cost \
  --name dev-budget \
  --time-grain monthly \
  --subscription $SUB \
  --notifications '{"Ops":{"enabled":true,"operator":"GreaterThan","threshold":80,"contactEmails":["finops@company.com"]}}'
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Budget** | Trigger vid nivå |
| **Reservation** | Rabatt på VM/DB vid commitment |
| **Spot** | Billigare, avbrytbar compute |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| Budget triggar ej | Notifier saknas | Lägg till mail/webhook |
| Svår kostspårning | Taggar saknas | Enforce tag-policy |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Tagga allt** | Kostspårning kräver taggar |
| **Budgetlarm** | Undvik överraskningar |
| **Rätt SKU** | Anpassa storlek och reservera |
""",
        },
        {
            "title": "Serverless: Functions och Event Grid",
            "slug": "azure-serverless-functions",
            "difficulty": "medium",
            "estimated_minutes": 35,
            "xp_reward": 60,
            "content": """# Serverless: Functions och Event Grid

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Event-driven** | Koppla ihop PaaS-tjänster |
| **Kosteffektivt** | Betala per körning |
| **Snabbt att skeppa** | Minimal infrastruktur |

------------------------------------------------------------

## Huvudinnehåll

| Begrepp | Förklaring |
|---------|------------|
| **Function App** | Värd för functions |
| **Triggers** | HTTP, Timer, Queue, Event Grid |
| **Consumption/Plan** | Skala vid behov |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az functionapp create ...` | Skapa function app |
| `func new` | Skapa function lokalt |
| `az eventgrid event-subscription create ...` | Koppla event |

------------------------------------------------------------

## Praktiska exempel

```bash
# Skapa storage och function app
az storage account create --name safunc$RANDOM --resource-group rg-app-dev --sku Standard_LRS --kind StorageV2
az functionapp create \
  --name fa-webhook \
  --resource-group rg-app-dev \
  --storage-account safunc$RANDOM \
  --consumption-plan-location westeurope \
  --runtime python
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Cold start** | Första körning kan vara långsam |
| **Bindings** | Kopplingar till köer/lagring |
| **Durable** | Orchestreringar |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `Storage account not found` | Fel namn/region | Kontrollera existens |
| Timeout i HTTP-funktion | För lång körning | Använd Premium/isolated eller kö-trigger |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Event-driven** | Koppla PaaS via Event Grid |
| **Kost** | Betala per körning, men övervaka kallstart |
| **Säkerhet** | Använd private endpoints och Key Vault |
""",
        },
        {
            "title": "Messaging: Service Bus och Event Hubs",
            "slug": "azure-messaging",
            "difficulty": "medium",
            "estimated_minutes": 35,
            "xp_reward": 60,
            "content": """# Messaging: Service Bus och Event Hubs

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Löskoppling** | Köer/ämnen isolerar tjänster |
| **Observability** | Event flöden för analys |
| **Backpressure** | Hantera spikes |

------------------------------------------------------------

## Huvudinnehåll

| Tjänst | Användning |
|--------|------------|
| **Service Bus** | Köer/Topics, transaktioner |
| **Event Hubs** | Hög throughput event-streaming |
| **Shared Access Policy** | Nycklar per klient |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az servicebus namespace create ...` | Skapa SB |
| `az eventhubs namespace create ...` | Skapa EH |
| `az eventhubs eventhub create ...` | Skapa hub |

------------------------------------------------------------

## Praktiska exempel

```bash
az servicebus namespace create --resource-group rg-app-dev --name sb-app-dev --location westeurope --sku Standard
az servicebus queue create --resource-group rg-app-dev --namespace-name sb-app-dev --name orders

az eventhubs namespace create --resource-group rg-app-dev --name eh-telemetry --location westeurope --sku Standard
az eventhubs eventhub create --resource-group rg-app-dev --namespace-name eh-telemetry --name telemetry --partition-count 4
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Queue/Topic** | Punkt-till-punkt vs pub/sub |
| **SAS** | Nyckel per policy |
| **Capture** | Skriv EH-data till Blob |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `Unauthorized` | Fel SAS/policy | Skapa nyckel och ge rätt policy |
| Droppade meddelanden | Ingen DLQ-hantering | Aktivera och övervaka DLQ |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Välj rätt** | Service Bus för affärshändelser, Event Hubs för telemetri |
| **Säkerhet** | SAS per klient + rotation |
| **Observability** | Capture + metrics för flöden |
""",
        },
        {
            "title": "Backup och Disaster Recovery",
            "slug": "azure-backup-dr",
            "difficulty": "medium",
            "estimated_minutes": 35,
            "xp_reward": 60,
            "content": """# Backup och Disaster Recovery

------------------------------------------------------------

## Varför viktigt för DevOps?

| Scenario | Varför |
|----------|-------|
| **Affärskrav** | RPO/RTO krav |
| **Skydd mot fel** | Regionavbrott |
| **Compliance** | Bevisa backuper och tester |

------------------------------------------------------------

## Huvudinnehåll

| Komponent | Beskrivning |
|-----------|-------------|
| **Recovery Services Vault** | Hanterar backuper |
| **Backup Policy** | Frekvens och retention |
| **ASR** | Site Recovery för VMs |

------------------------------------------------------------

## Kommandon/Syntax

| Kommando | Beskrivning |
|----------|-------------|
| `az backup vault create ...` | Skapa vault |
| `az backup protection enable-for-vm ...` | Aktivera backup |
| `az backup restore restore-disks ...` | Återställ |

------------------------------------------------------------

## Praktiska exempel

```bash
az backup vault create --resource-group rg-app-dev --name rsv-app-dev --location westeurope
az backup protection enable-for-vm --resource-group rg-app-dev --vault-name rsv-app-dev --vm vm-api --policy-name DefaultPolicy
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **RPO/RTO** | Återställningsmål |
| **Vault** | Håller backupdata |
| **ASR** | Replikering till sekundär region |

------------------------------------------------------------

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| Backup misslyckas | Agent/extension fel | Kontrollera extension-loggar |
| Restore saknar nät | VNet ej specificerat | Ange nät vid restore |

------------------------------------------------------------

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Testa restore** | Bevisa att backup funkar |
| **Policy per workload** | Anpassa retention |
| **Geo-resiliens** | ASR eller GRS beroende på krav |
""",
        },
    ],
}
