"""
Azure Cloud SkillsMap - Block 3: Storage & Databases
Nodes 9-12: Blob Storage, Azure SQL, Cosmos DB, Caching
"""

from typing import Any

# ============================================================================
# NODE 9: AZURE BLOB STORAGE
# ============================================================================

AZURE_NODE_9_BLOB = {
    "node_id": 9,
    "title": "Azure Blob Storage",
    "slug": "azure-blob-storage",
    "description": "Lagra ostrukturerad data i Blob Storage",
    "difficulty": "intermediate",
    "estimated_minutes": 55,
    "xp_reward": 100,
    "topics_covered": [
        "blob storage", "containers", "access tiers", "lifecycle",
        "sas tokens", "static websites", "cdn"
    ],
    "content": """
# Azure Blob Storage

> *"Blob Storage is where the world's data lives."*

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Problem utan Blob Storage | Losning med Blob Storage |
|----------|---------------------------|--------------------------|
| Backup pipeline | Lokal lagring begransad och riskabel | Oandlig skalbar cloud storage |
| Static content | CDN konfiguration komplex | Inbyggd static website hosting |
| Log aggregation | Loggar sprids over servrar | Centraliserad log storage |
| Cost optimization | Samma pris for alla data | Auto-tiering (Hot/Cool/Archive) |

------------------------------------------------------------

## Blob Storage Hierarchy

```
+-----------------------------------------------------------------+
|                 BLOB STORAGE HIERARCHY                           |
+-----------------------------------------------------------------+
|                                                                  |
|  Storage Account: stmyapp123                                    |
|  +-- Container: images                                          |
|      +-- 2024/                                                  |
|      |   +-- 01/                                                |
|      |   |   +-- photo1.jpg        <- Blob                       |
|      |   |   +-- photo2.jpg                                     |
|      |   +-- 02/                                                |
|      |       +-- photo3.jpg                                     |
|      +-- thumbnails/                                            |
|          +-- photo1_thumb.jpg                                   |
|                                                                  |
|  BLOB TYPES:                                                    |
|  +---------------------------------------------------------+    |
|  | Block Blob  | Page Blob    | Append Blob                |    |
|  | - Images    | - VHD disks  | - Log files                |    |
|  | - Videos    | - Random I/O | - Append-only              |    |
|  | - Backups   |              | - Audit trails             |    |
|  | - Up to 4.7TB| - Up to 8TB | - Up to 195GB             |    |
|  +---------------------------------------------------------+    |
|                                                                  |
|  ACCESS TIERS:                                                  |
|  +---------------------------------------------------------+    |
|  | Hot       | Cool      | Cold       | Archive           |    |
|  | Frequent  | Infrequent| Rare       | Long-term         |    |
|  | $0.02/GB  | $0.01/GB  | $0.004/GB  | $0.001/GB         |    |
|  | Low access| Higher    | Higher     | Rehydration       |    |
|  | cost      | access    | access     | required          |    |
|  +---------------------------------------------------------+    |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Skapa Storage Account

```bash
# Skapa Storage Account
az storage account create \\
    --name stmyapp123 \\
    --resource-group rg-demo \\
    --location northeurope \\
    --sku Standard_LRS \\
    --kind StorageV2 \\
    --access-tier Hot

# Skapa container
az storage container create \\
    --name images \\
    --account-name stmyapp123 \\
    --public-access off

# Visa access keys
az storage account keys list \\
    --account-name stmyapp123 \\
    --resource-group rg-demo
```

------------------------------------------------------------

## Upload/Download Blobs

```bash
# Upload fil
az storage blob upload \\
    --account-name stmyapp123 \\
    --container-name images \\
    --name photos/2024/photo1.jpg \\
    --file ./photo1.jpg \\
    --auth-mode login

# Upload mapp (batch)
az storage blob upload-batch \\
    --account-name stmyapp123 \\
    --destination images \\
    --source ./local-folder \\
    --pattern "*.jpg"

# Download fil
az storage blob download \\
    --account-name stmyapp123 \\
    --container-name images \\
    --name photos/2024/photo1.jpg \\
    --file ./downloaded.jpg

# Lista blobs
az storage blob list \\
    --account-name stmyapp123 \\
    --container-name images \\
    --output table

# Radera blob
az storage blob delete \\
    --account-name stmyapp123 \\
    --container-name images \\
    --name photos/old-photo.jpg
```

------------------------------------------------------------

## SAS Tokens (Shared Access Signatures)

```bash
# Generera SAS token för container (tidsbegränsad åtkomst)
az storage container generate-sas \\
    --account-name stmyapp123 \\
    --name images \\
    --permissions rl \\
    --expiry 2024-12-31T23:59:59Z \\
    --output tsv

# Generera SAS för specifik blob
az storage blob generate-sas \\
    --account-name stmyapp123 \\
    --container-name images \\
    --name photos/secret.jpg \\
    --permissions r \\
    --expiry 2024-12-07T12:00:00Z \\
    --full-uri

# Resultat: URL med SAS token för säker delning
# https://stmyapp123.blob.core.windows.net/images/photos/secret.jpg?sv=...&sig=...
```

------------------------------------------------------------

## Lifecycle Management

```bash
# Skapa lifecycle policy (JSON)
cat << 'EOF' > lifecycle-policy.json
{
  "rules": [
    {
      "name": "move-to-cool-after-30-days",
      "enabled": true,
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["logs/"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": { "daysAfterModificationGreaterThan": 30 },
            "tierToArchive": { "daysAfterModificationGreaterThan": 90 },
            "delete": { "daysAfterModificationGreaterThan": 365 }
          }
        }
      }
    }
  ]
}
EOF

# Applicera policy
az storage account management-policy create \\
    --account-name stmyapp123 \\
    --resource-group rg-demo \\
    --policy @lifecycle-policy.json
```

------------------------------------------------------------

## Static Website Hosting

```bash
# Aktivera static website
az storage blob service-properties update \\
    --account-name stmyapp123 \\
    --static-website \\
    --index-document index.html \\
    --404-document 404.html

# Upload website files
az storage blob upload-batch \\
    --account-name stmyapp123 \\
    --destination '$web' \\
    --source ./dist

# Visa URL
az storage account show \\
    --name stmyapp123 \\
    --query "primaryEndpoints.web" \\
    --output tsv

# Resultat: https://stmyapp123.z16.web.core.windows.net/
```

------------------------------------------------------------

## SDK Usage (Python)

```python
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential

# Anslut med managed identity
credential = DefaultAzureCredential()
blob_service = BlobServiceClient(
    account_url="https://stmyapp123.blob.core.windows.net",
    credential=credential
)

# Upload
container = blob_service.get_container_client("images")
with open("photo.jpg", "rb") as data:
    container.upload_blob(name="photos/photo.jpg", data=data, overwrite=True)

# Download
blob = container.get_blob_client("photos/photo.jpg")
with open("downloaded.jpg", "wb") as f:
    f.write(blob.download_blob().readall())

# Lista blobs
for blob in container.list_blobs(name_starts_with="photos/"):
    print(f"{blob.name}: {blob.size} bytes")
```

------------------------------------------------------------

## Vanliga Problem

### Problem 1: Access Denied

```bash
# Kontrollera att RBAC är konfigurerad
az role assignment create \\
    --role "Storage Blob Data Contributor" \\
    --assignee "user@company.com" \\
    --scope "/subscriptions/.../resourceGroups/rg-demo/providers/Microsoft.Storage/storageAccounts/stmyapp123"
```

------------------------------------------------------------

## Key Takeaways

| Begrepp | Beskrivning |
|---------|-------------|
| Block Blobs | Anvand for de flesta scenarier (bilder, videos, backups) |
| Access tiers | Hot/Cool/Archive optimerar kostnad automatiskt |
| Lifecycle policies | Automatiserar tiering och radering |
| SAS tokens | Tidsbegransad delning utan att ge access keys |
| Static websites | Enkel hosting direkt fran Blob Storage |

**Kom ihag:**
- Valj ratt access tier baserat pa hur ofta data accessas
- Anvand SAS tokens istallet for att dela access keys
- Satt upp lifecycle policies for att spara pengar
- Block Blobs ar nastan alltid ratt val
""",
}


# ============================================================================
# NODE 10: AZURE SQL DATABASE
# ============================================================================

AZURE_NODE_10_SQL = {
    "node_id": 10,
    "title": "Azure SQL Database",
    "slug": "azure-sql-database",
    "description": "Managed relational database i Azure",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 110,
    "topics_covered": [
        "azure sql", "elastic pools", "serverless", "geo-replication",
        "backup", "security", "performance tuning"
    ],
    "content": """
# Azure SQL Database

> *"Your database, managed by Microsoft."*

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Problem utan Azure SQL | Losning med Azure SQL |
|----------|------------------------|------------------------|
| Databashantering | Patching, backups, HA manuellt | Fully managed av Microsoft |
| Skalning | Provisionera ny server, migrera | Andras med ett kommando |
| Disaster recovery | Komplex replikering | Inbyggd geo-replication |
| Dev/test kostnader | Betala for idle servrar | Serverless auto-pause |

------------------------------------------------------------

## Azure SQL Options

```
+-----------------------------------------------------------------+
|                    AZURE SQL OPTIONS                             |
+-----------------------------------------------------------------+
|                                                                  |
|  +------------------------------------------------------------+ |
|  | AZURE SQL DATABASE (PaaS - Single Database)                 | |
|  | • Enklast att använda                                       | |
|  | • Per-databas prissättning                                  | |
|  | • Serverless option (auto-pause)                            | |
|  | Use case: Nya appar, microservices                          | |
|  +------------------------------------------------------------+ |
|                                                                  |
|  +------------------------------------------------------------+ |
|  | ELASTIC POOL                                                | |
|  | • Dela resurser mellan databaser                            | |
|  | • Kostnadseffektivt för SaaS                                | |
|  | Use case: Multi-tenant apps                                 | |
|  +------------------------------------------------------------+ |
|                                                                  |
|  +------------------------------------------------------------+ |
|  | AZURE SQL MANAGED INSTANCE                                  | |
|  | • Närmast on-prem SQL Server                                | |
|  | • Cross-database queries, SQL Agent                         | |
|  | • VNet-native                                               | |
|  | Use case: Lift-and-shift migration                          | |
|  +------------------------------------------------------------+ |
|                                                                  |
|  +------------------------------------------------------------+ |
|  | SQL SERVER ON AZURE VM (IaaS)                               | |
|  | • Full kontroll över OS och SQL                             | |
|  | • Du hanterar patching och backups                          | |
|  | Use case: Legacy apps, specifika krav                       | |
|  +------------------------------------------------------------+ |
|                                                                  |
|  PRICING TIERS:                                                 |
|  +---------------------------------------------------------+    |
|  | DTU (Basic/Std/Prem) | vCore (Gen Purpose/Business Crit)|    |
|  | - Bundled resources  | - Separate CPU/Storage            |    |
|  | - Enklare prissätt   | - Mer flexibel                    |    |
|  | - Från ~$5/mån       | - Från ~$30/mån                   |    |
|  +---------------------------------------------------------+    |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Skapa SQL Database

```bash
# Skapa SQL Server (logical server)
az sql server create \\
    --name sqlserver-myapp \\
    --resource-group rg-demo \\
    --location northeurope \\
    --admin-user sqladmin \\
    --admin-password "SecureP@ssw0rd123!"

# Skapa databas (DTU model)
az sql db create \\
    --name mydb \\
    --resource-group rg-demo \\
    --server sqlserver-myapp \\
    --service-objective S0

# Skapa databas (vCore model)
az sql db create \\
    --name mydb-vcore \\
    --resource-group rg-demo \\
    --server sqlserver-myapp \\
    --edition GeneralPurpose \\
    --compute-model Provisioned \\
    --family Gen5 \\
    --capacity 2

# Skapa serverless databas (auto-pause!)
az sql db create \\
    --name mydb-serverless \\
    --resource-group rg-demo \\
    --server sqlserver-myapp \\
    --edition GeneralPurpose \\
    --compute-model Serverless \\
    --family Gen5 \\
    --min-capacity 0.5 \\
    --max-capacity 4 \\
    --auto-pause-delay 60  # minuter
```

------------------------------------------------------------

## Firewall & Security

```bash
# Tillåt Azure services
az sql server firewall-rule create \\
    --name AllowAzureServices \\
    --resource-group rg-demo \\
    --server sqlserver-myapp \\
    --start-ip-address 0.0.0.0 \\
    --end-ip-address 0.0.0.0

# Tillåt din IP
az sql server firewall-rule create \\
    --name AllowMyIP \\
    --resource-group rg-demo \\
    --server sqlserver-myapp \\
    --start-ip-address "203.0.113.45" \\
    --end-ip-address "203.0.113.45"

# Aktivera Azure AD authentication
az sql server ad-admin create \\
    --resource-group rg-demo \\
    --server sqlserver-myapp \\
    --display-name "DBA Team" \\
    --object-id "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
```

------------------------------------------------------------

## Connection Strings

```bash
# Visa connection string
az sql db show-connection-string \\
    --client ado.net \\
    --name mydb \\
    --server sqlserver-myapp

# .NET connection string
"Server=tcp:sqlserver-myapp.database.windows.net,1433;Initial Catalog=mydb;Persist Security Info=False;User ID=sqladmin;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"

# Med Managed Identity (recommended)
"Server=tcp:sqlserver-myapp.database.windows.net,1433;Initial Catalog=mydb;Authentication=Active Directory Default;"
```

------------------------------------------------------------

## Geo-Replication & Failover

```bash
# Skapa geo-replica (läs-replica i annan region)
az sql db replica create \\
    --name mydb \\
    --resource-group rg-demo \\
    --server sqlserver-myapp \\
    --partner-resource-group rg-demo-secondary \\
    --partner-server sqlserver-myapp-secondary

# Skapa failover group
az sql failover-group create \\
    --name fg-myapp \\
    --resource-group rg-demo \\
    --server sqlserver-myapp \\
    --partner-server sqlserver-myapp-secondary \\
    --partner-resource-group rg-demo-secondary \\
    --add-db mydb \\
    --failover-policy Automatic \\
    --grace-period 1
```

------------------------------------------------------------

## Backup & Restore

```bash
# Azure SQL har automatisk backup:
# - Full backup: weekly
# - Differential: every 12 hours
# - Transaction log: every 5-10 minutes

# Retention: 7-35 dagar (LTR up to 10 years)

# Point-in-time restore
az sql db restore \\
    --resource-group rg-demo \\
    --server sqlserver-myapp \\
    --name mydb-restored \\
    --source-database mydb \\
    --time "2024-12-06T10:00:00Z"

# Geo-restore (från annan region vid disaster)
az sql db restore \\
    --resource-group rg-demo \\
    --server sqlserver-recovery \\
    --name mydb-georestored \\
    --source-database mydb \\
    --source-server sqlserver-myapp \\
    --geo-backup
```

------------------------------------------------------------

## Performance Monitoring

```bash
# Query Performance Insight (i Portal)
# Portal -> SQL Database -> Query Performance Insight

# Intelligent Insights
az sql db show \\
    --name mydb \\
    --resource-group rg-demo \\
    --server sqlserver-myapp \\
    --query "currentServiceObjectiveName"

# Visa metrics
az monitor metrics list \\
    --resource "/subscriptions/.../resourceGroups/rg-demo/providers/Microsoft.Sql/servers/sqlserver-myapp/databases/mydb" \\
    --metric "cpu_percent,storage_percent,dtu_used" \\
    --interval PT1H
```

------------------------------------------------------------

## Vanliga Problem

### Problem 1: "Cannot connect to SQL Server"

```bash
# Kontrollera firewall
az sql server firewall-rule list --resource-group rg-demo --server sqlserver-myapp

# Kontrollera att port 1433 är öppen
telnet sqlserver-myapp.database.windows.net 1433
```

------------------------------------------------------------

## Key Takeaways

| Begrepp | Beskrivning |
|---------|-------------|
| Single Database | Bast for nya appar och microservices |
| Elastic Pool | Kostnadseffektivt for SaaS med flera databaser |
| Serverless | Sparar pengar pa dev/test med auto-pause |
| Geo-replication | Las-replika i annan region for DR |
| PITR | Point-in-time restore fran automatiska backups |

**Kom ihag:**
- Anvand Serverless for dev/test miljoer
- Satt upp Elastic Pool om du har flera databaser
- Aktivera Azure AD authentication istallet for SQL auth
- Geo-replication ar basta DR-losningen
""",
}


# ============================================================================
# NODE 11: AZURE COSMOS DB
# ============================================================================

AZURE_NODE_11_COSMOS = {
    "node_id": 11,
    "title": "Azure Cosmos DB",
    "slug": "azure-cosmos-db",
    "description": "Globally distributed NoSQL database",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 110,
    "topics_covered": [
        "cosmos db", "nosql", "partitioning", "consistency levels",
        "request units", "global distribution", "apis"
    ],
    "content": """
# Azure Cosmos DB

> *"Single-digit millisecond latency, anywhere in the world."*

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Problem utan Cosmos DB | Losning med Cosmos DB |
|----------|------------------------|------------------------|
| Global app | Hog latency for avlagsna users | Multi-region writes, laga ms |
| Schema evolution | Migreringar nar schema andras | Schemalost (NoSQL) |
| Varying workloads | Over/under-provisioning | Autoscale RU |
| Multi-API stod | Migrera fran MongoDB/Cassandra | Native API-stod |

------------------------------------------------------------

## Cosmos DB Architecture

```
+-----------------------------------------------------------------+
|                    COSMOS DB ARCHITECTURE                        |
+-----------------------------------------------------------------+
|                                                                  |
|  +------------------------------------------------------------+ |
|  |                   COSMOS DB ACCOUNT                         | |
|  |  +------------------------------------------------------+  | |
|  |  |                    DATABASE                           |  | |
|  |  |  +-------------------------------------------------+ |  | |
|  |  |  |              CONTAINER                          | |  | |
|  |  |  |  +---------+ +---------+ +---------+          | |  | |
|  |  |  |  |  Item   | |  Item   | |  Item   |          | |  | |
|  |  |  |  | (JSON)  | | (JSON)  | | (JSON)  |          | |  | |
|  |  |  |  +---------+ +---------+ +---------+          | |  | |
|  |  |  |       ↓           ↓           ↓                | |  | |
|  |  |  |  PARTITION KEY (e.g., userId)                  | |  | |
|  |  |  |  +---------+ +---------+ +---------+          | |  | |
|  |  |  |  |Partition| |Partition| |Partition|          | |  | |
|  |  |  |  |   A     | |   B     | |   C     |          | |  | |
|  |  |  |  +---------+ +---------+ +---------+          | |  | |
|  |  |  +-------------------------------------------------+ |  | |
|  |  +------------------------------------------------------+  | |
|  +------------------------------------------------------------+ |
|                                                                  |
|  CONSISTENCY LEVELS:                                            |
|  +---------------------------------------------------------+    |
|  | Strong -> Bounded Staleness -> Session -> Consistent Prefix |    |
|  |        -> Eventual                                        |    |
|  |                                                          |    |
|  | More consistency <---------------------> More performance  |    |
|  | Higher latency   <---------------------> Lower latency     |    |
|  +---------------------------------------------------------+    |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Skapa Cosmos DB

```bash
# Skapa Cosmos DB account
az cosmosdb create \\
    --name cosmos-myapp \\
    --resource-group rg-demo \\
    --locations regionName=northeurope failoverPriority=0 \\
    --default-consistency-level Session \\
    --enable-automatic-failover true

# Skapa databas
az cosmosdb sql database create \\
    --account-name cosmos-myapp \\
    --resource-group rg-demo \\
    --name mydb

# Skapa container med partition key
az cosmosdb sql container create \\
    --account-name cosmos-myapp \\
    --resource-group rg-demo \\
    --database-name mydb \\
    --name users \\
    --partition-key-path "/userId" \\
    --throughput 400

# Skapa container med autoscale
az cosmosdb sql container create \\
    --account-name cosmos-myapp \\
    --resource-group rg-demo \\
    --database-name mydb \\
    --name orders \\
    --partition-key-path "/customerId" \\
    --max-throughput 4000  # Auto-scales 400-4000 RU
```

------------------------------------------------------------

## Request Units (RU)

```
+-----------------------------------------------------------------+
|                    REQUEST UNITS (RU)                            |
+-----------------------------------------------------------------+
|                                                                  |
|  RU = Valutan för Cosmos DB throughput                          |
|                                                                  |
|  OPERATION                              COST                     |
|  ---------------------------------------------                  |
|  Read 1KB item by ID & partition key    ~1 RU                   |
|  Read 1KB item by query                 ~3 RU                   |
|  Write 1KB item                         ~5 RU                   |
|  Delete 1KB item                        ~5 RU                   |
|  Query with filter (depends)            ~10-100+ RU             |
|                                                                  |
|  PRICING (Sweden Central):                                       |
|  Provisioned: 400 RU = ~$24/month                               |
|  Autoscale:   Min 400, Max 4000 = ~$28/month (for 400 avg)      |
|  Serverless:  Per request ($0.25 per 1M RU)                     |
|                                                                  |
|  ⚠️ COST TRAP:                                                   |
|  Dålig partition key -> cross-partition queries -> höga RU costs  |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## CRUD Operations (Python SDK)

```python
from azure.cosmos import CosmosClient, PartitionKey
from azure.identity import DefaultAzureCredential

# Anslut
endpoint = "https://cosmos-myapp.documents.azure.com:443/"
credential = DefaultAzureCredential()
client = CosmosClient(endpoint, credential)

database = client.get_database_client("mydb")
container = database.get_container_client("users")

# Create
user = {
    "id": "user-123",
    "userId": "user-123",  # Partition key
    "name": "John Doe",
    "email": "john@example.com"
}
container.create_item(body=user)

# Read (by ID + partition key = 1 RU!)
user = container.read_item(item="user-123", partition_key="user-123")

# Query (högre RU cost)
query = "SELECT * FROM c WHERE c.name = @name"
items = container.query_items(
    query=query,
    parameters=[{"name": "@name", "value": "John Doe"}],
    enable_cross_partition_query=True  # ⚠️ Expensive!
)
for item in items:
    print(item)

# Update (upsert)
user["email"] = "john.doe@example.com"
container.upsert_item(body=user)

# Delete
container.delete_item(item="user-123", partition_key="user-123")
```

------------------------------------------------------------

## Partition Key Design

```python
# ✅ GOOD partition keys:
# - userId for user data
# - customerId for orders
# - deviceId for IoT data
# - tenantId for SaaS apps

# ❌ BAD partition keys:
# - country (low cardinality, hot partitions)
# - status (e.g., "active"/"inactive")
# - date only (without other fields)

# Example: E-commerce orders
{
    "id": "order-12345",
    "customerId": "cust-789",  # <- Partition key
    "orderDate": "2024-12-07",
    "items": [...],
    "total": 99.99
}

# Query within partition (efficient):
container.query_items(
    query="SELECT * FROM c WHERE c.orderDate > @date",
    partition_key="cust-789"  # <- Locked to one partition!
)
```

------------------------------------------------------------

## Global Distribution

```bash
# Lägg till region
az cosmosdb update \\
    --name cosmos-myapp \\
    --resource-group rg-demo \\
    --locations regionName=northeurope failoverPriority=0 \\
    --locations regionName=westeurope failoverPriority=1

# Aktivera multi-region writes
az cosmosdb update \\
    --name cosmos-myapp \\
    --resource-group rg-demo \\
    --enable-multiple-write-locations true

# Manuell failover
az cosmosdb failover-priority-change \\
    --name cosmos-myapp \\
    --resource-group rg-demo \\
    --failover-policies "westeurope=0" "northeurope=1"
```

------------------------------------------------------------

## Vanliga Problem

### Problem 1: Hoga RU costs

```python
# ❌ Cross-partition query
container.query_items(
    query="SELECT * FROM c WHERE c.email = @email",
    enable_cross_partition_query=True  # Skannar ALLA partitioner!
)

# ✅ Inkludera partition key
container.query_items(
    query="SELECT * FROM c WHERE c.email = @email",
    partition_key="user-123"  # Skannar endast EN partition
)
```

------------------------------------------------------------

## Key Takeaways

| Begrepp | Beskrivning |
|---------|-------------|
| Partition key | Viktigaste designbeslutet - valj noggrant |
| Request Units | Throughput-valutan - 1 RU = 1 read av 1KB |
| Consistency levels | Session ar bast for de flesta use cases |
| Global distribution | Multi-region for lag latency overallt |
| Autoscale | Dynamisk skalning for variabel workload |

**Kom ihag:**
- Partition key kan INTE andras efter container skapats
- Undvik cross-partition queries (dyra i RU)
- Anvand read_item() med partition key for 1 RU reads
- Session consistency ar default och rekommenderat
""",
}


# ============================================================================
# NODE 12: AZURE CACHE FOR REDIS
# ============================================================================

AZURE_NODE_12_CACHE = {
    "node_id": 12,
    "title": "Azure Cache for Redis",
    "slug": "azure-redis-cache",
    "description": "High-performance caching med Redis",
    "difficulty": "intermediate",
    "estimated_minutes": 50,
    "xp_reward": 90,
    "topics_covered": [
        "redis", "caching", "session state", "pub/sub",
        "clustering", "data persistence", "cache patterns"
    ],
    "content": """
# Azure Cache for Redis

> *"The fastest way to speed up your app is to not hit the database."*

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Problem utan Redis | Losning med Redis |
|----------|-------------------|-------------------|
| Databas-load | Varje request slar DB | Cache vanliga queries |
| Session state | Sticky sessions, single point of failure | Distribuerad session store |
| Real-time features | Polling, hog latency | Pub/Sub, microsekunder |
| Rate limiting | Komplex implementation | Atomic INCR med TTL |

------------------------------------------------------------

## Caching Architecture

```
+-----------------------------------------------------------------+
|                    CACHING ARCHITECTURE                          |
+-----------------------------------------------------------------+
|                                                                  |
|  Without Cache:                                                 |
|  +--------+        +----------+        +----------+            |
|  | Client | ----->  |   App    | ----->  | Database |            |
|  +--------+        +----------+        +----------+            |
|                        |                    |                   |
|                    50ms total           50ms query              |
|                                                                  |
|  With Cache (Cache Hit):                                        |
|  +--------+        +----------+        +----------+            |
|  | Client | ----->  |   App    | - X -  | Database |            |
|  +--------+        +----------+        +----------+            |
|                        |                                        |
|                    +----------+                                 |
|                    |  Redis   |                                 |
|                    +----------+                                 |
|                        |                                        |
|                    2ms total (25x faster!)                      |
|                                                                  |
|  TIERS:                                                         |
|  +---------------------------------------------------------+    |
|  | Basic      | Standard   | Premium      | Enterprise    |    |
|  | - No SLA   | - 99.9%    | - Clustering | - 99.999%     |    |
|  | - Dev/test | - Replicas | - VNet       | - Active-geo  |    |
|  | - 250MB+   | - HA       | - Zones      | - Redis Modules|   |
|  +---------------------------------------------------------+    |
|                                                                  |
+-----------------------------------------------------------------+
```

------------------------------------------------------------

## Skapa Redis Cache

```bash
# Skapa Redis Cache (Standard tier)
az redis create \\
    --name redis-myapp \\
    --resource-group rg-demo \\
    --location northeurope \\
    --sku Standard \\
    --vm-size c1

# Premium med clustering
az redis create \\
    --name redis-premium \\
    --resource-group rg-demo \\
    --location northeurope \\
    --sku Premium \\
    --vm-size p1 \\
    --shard-count 3 \\
    --zones 1 2 3

# Visa access keys
az redis list-keys \\
    --name redis-myapp \\
    --resource-group rg-demo

# Visa connection info
az redis show \\
    --name redis-myapp \\
    --resource-group rg-demo \\
    --query "{Host:hostName,Port:sslPort}"
```

------------------------------------------------------------

## Python Usage

```python
import redis
import json

# Anslut till Azure Redis
r = redis.Redis(
    host='redis-myapp.redis.cache.windows.net',
    port=6380,
    password='your-access-key',
    ssl=True,
    decode_responses=True
)

# ========================================
# Basic Operations
# ========================================

# Set med TTL (Time To Live)
r.setex("user:123", 3600, json.dumps({"name": "John", "email": "john@example.com"}))

# Get
user_data = r.get("user:123")
if user_data:
    user = json.loads(user_data)

# Delete
r.delete("user:123")

# ========================================
# Cache-Aside Pattern
# ========================================

def get_user(user_id: str):
    cache_key = f"user:{user_id}"

    # 1. Kolla cache först
    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)

    # 2. Cache miss -> hämta från databas
    user = db.query_user(user_id)

    # 3. Spara i cache (1 timme TTL)
    r.setex(cache_key, 3600, json.dumps(user))

    return user

# ========================================
# Session Management
# ========================================

def create_session(user_id: str) -> str:
    session_id = str(uuid.uuid4())
    session_data = {"user_id": user_id, "created": datetime.utcnow().isoformat()}

    # Session expires efter 24 timmar
    r.setex(f"session:{session_id}", 86400, json.dumps(session_data))

    return session_id

def validate_session(session_id: str):
    session_data = r.get(f"session:{session_id}")
    if not session_data:
        return None

    # Förnya TTL vid access
    r.expire(f"session:{session_id}", 86400)

    return json.loads(session_data)
```

------------------------------------------------------------

## Common Patterns

```python
# ========================================
# Leaderboard (Sorted Set)
# ========================================

# Lägg till poäng
r.zadd("leaderboard:daily", {"player1": 1000, "player2": 850, "player3": 920})

# Topp 10
top_players = r.zrevrange("leaderboard:daily", 0, 9, withscores=True)
# [('player1', 1000.0), ('player3', 920.0), ('player2', 850.0)]

# Rank för specifik spelare
rank = r.zrevrank("leaderboard:daily", "player2")  # 2 (0-indexed)

# ========================================
# Rate Limiting
# ========================================

def check_rate_limit(user_id: str, max_requests: int = 100, window_seconds: int = 60):
    key = f"ratelimit:{user_id}"

    current = r.incr(key)
    if current == 1:
        r.expire(key, window_seconds)

    if current > max_requests:
        ttl = r.ttl(key)
        raise RateLimitExceeded(f"Too many requests. Try again in {ttl} seconds.")

    return True

# ========================================
# Pub/Sub (Real-time notifications)
# ========================================

# Publisher
def publish_notification(channel: str, message: dict):
    r.publish(channel, json.dumps(message))

publish_notification("notifications:user123", {"type": "order_shipped", "order_id": "456"})

# Subscriber (i separat process)
pubsub = r.pubsub()
pubsub.subscribe("notifications:user123")

for message in pubsub.listen():
    if message["type"] == "message":
        data = json.loads(message["data"])
        print(f"Received: {data}")
```

------------------------------------------------------------

## .NET Integration

```csharp
// StackExchange.Redis
var redis = ConnectionMultiplexer.Connect("redis-myapp.redis.cache.windows.net:6380,password=xxx,ssl=True");
var db = redis.GetDatabase();

// Set
await db.StringSetAsync("key", "value", TimeSpan.FromHours(1));

// Get
var value = await db.StringGetAsync("key");

// Distributed Cache (Microsoft.Extensions.Caching.StackExchangeRedis)
builder.Services.AddStackExchangeRedisCache(options =>
{
    options.Configuration = "redis-myapp.redis.cache.windows.net:6380,password=xxx,ssl=True";
    options.InstanceName = "MyApp:";
});
```

------------------------------------------------------------

## Vanliga Problem

### Problem 1: Cache Stampede

```python
# ❌ Alla requests slår databasen när cache expirerar
def get_popular_item(item_id):
    cached = r.get(f"item:{item_id}")
    if not cached:
        item = db.get_item(item_id)  # 1000 requests samtidigt!
        r.setex(f"item:{item_id}", 3600, json.dumps(item))
    return json.loads(cached)

# ✅ Locking/mutex pattern
def get_popular_item_safe(item_id):
    cache_key = f"item:{item_id}"
    lock_key = f"lock:item:{item_id}"

    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)

    # Försök ta lock
    if r.setnx(lock_key, "1"):
        r.expire(lock_key, 10)  # Lock timeout
        try:
            item = db.get_item(item_id)
            r.setex(cache_key, 3600, json.dumps(item))
            return item
        finally:
            r.delete(lock_key)
    else:
        # Vänta och försök igen
        time.sleep(0.1)
        return get_popular_item_safe(item_id)
```

------------------------------------------------------------

## Key Takeaways

| Begrepp | Beskrivning |
|---------|-------------|
| Cache-Aside | Kolla cache forst, hamta fran DB vid miss |
| TTL | Time To Live forhindrar stale data |
| Sorted Sets | Perfekt for leaderboards och rankings |
| Pub/Sub | Real-time notifications och events |
| Rate limiting | Atomic INCR med EXPIRE for throttling |

**Kom ihag:**
- Satt alltid TTL pa cached data
- Anvand locking/mutex for att undvika cache stampede
- Standard tier for produktion (har replikas)
- Premium for clustering och VNet-integration
""",
}


# Export all nodes from Block 3
BLOCK_3_NODES = [
    AZURE_NODE_9_BLOB,
    AZURE_NODE_10_SQL,
    AZURE_NODE_11_COSMOS,
    AZURE_NODE_12_CACHE,
]
