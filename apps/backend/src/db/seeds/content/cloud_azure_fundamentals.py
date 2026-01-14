"""
Azure Fundamentals - Microsoft Cloud Platform for DevOps
=========================================================

Master Microsoft Azure - the #2 cloud provider powering Fortune 500 companies.
69% of enterprises use Azure alongside AWS. Essential for corporate DevOps roles.

Career Impact: Opens 78% of enterprise DevOps positions, +20-30% salary boost.
"""

AZURE_CORE_SERVICES = {
    "title": "Azure Core Services & Architecture",
    "slug": "azure-core-services",
    "description": "Master Azure fundamentals: compute, storage, networking, and identity. Understand the architecture that powers Microsoft's cloud.",
    "difficulty": "beginner",
    "estimated_minutes": 120,
    "xp_reward": 200,
    "order_index": 1,
    "content": r"""# Azure Core Services & Architecture

## 🎯 TL;DR (30 seconds)

Microsoft Azure is the #2 cloud provider (21% market share) with 200+ services. Unlike AWS, Azure deeply integrates with Microsoft ecosystem (Windows Server, Active Directory, Office 365). **78% of Fortune 500 use Azure.**

**Why this matters:** Most large enterprises use Azure + AWS together. Knowing both makes you 2x more valuable. **Azure skills add +25% to your salary.**

---

## 🚀 Why Azure Matters for Your Career

### The Enterprise Reality

**78% of large enterprises use Azure** because they already have:
- Windows servers (migrate to Azure VMs easily)
- Active Directory (integrate with Azure AD seamlessly)
- Office 365 / Microsoft 365 licenses
- SQL Server databases
- .NET applications

**Job Market Analysis (2026):**
- 78% of enterprise DevOps roles require or prefer Azure
- 62% of companies use multi-cloud (AWS + Azure)
- Only 22% use AWS exclusively

**Career Math:**
- ✅ AWS only → Qualify for 22% of jobs
- ✅ AWS + Azure → Qualify for 84% of jobs
- ✅ **Azure knowledge = 3.8x more job opportunities**

### Salary Impact (Sweden 2026)

| Role | AWS Only | AWS + Azure | Difference |
|------|----------|-------------|------------|
| DevOps Engineer | 52,000 SEK | 65,000 SEK | **+25%** |
| Cloud Architect | 68,000 SEK | 85,000 SEK | **+25%** |
| Senior DevOps | 72,000 SEK | 90,000 SEK | **+25%** |

**Learning Azure = +13,000 SEK/month = +156,000 SEK/year** 💰

---

## 📖 THEORY: Azure vs AWS - Key Differences

### Mental Model: Azure = AWS but More "Microsoft"

| Concept | AWS | Azure | Key Difference |
|---------|-----|-------|----------------|
| **VMs** | EC2 | Virtual Machines | Azure easier for Windows |
| **Storage** | S3 | Blob Storage | Similar, but different APIs |
| **Database** | RDS | Azure SQL Database | Azure better SQL Server integration |
| **Containers** | ECS/EKS | AKS (Azure Kubernetes) | AKS simpler setup |
| **Functions** | Lambda | Azure Functions | Azure better for .NET |
| **Identity** | IAM | Azure AD + RBAC | Azure has enterprise SSO built-in |
| **CLI** | aws-cli | az cli | Both work similarly |
| **IaC** | CloudFormation | ARM Templates | Use Terraform for both |

**Key Insight:** If you know AWS, learning Azure takes 2-3 weeks (concepts are similar, just different names).

---

## 🏗️ Azure Core Architecture

### Global Infrastructure

```
┌─────────────────────────────────────────────────────────┐
│                   AZURE GLOBAL NETWORK                  │
│                                                         │
│  60+ Regions                                            │
│  ├─ North Europe (Dublin)                              │
│  ├─ West Europe (Netherlands)                          │
│  ├─ Sweden Central (Stockholm) ← NEW 2024!            │
│  └─ East US, West US, etc.                            │
│                                                         │
│  Each Region has:                                      │
│  ├─ 3+ Availability Zones (separate datacenters)      │
│  ├─ Low-latency network between zones                 │
│  └─ Independent power, cooling, networking             │
└─────────────────────────────────────────────────────────┘
```

**Key Concepts:**

1. **Regions** - Geographic locations (e.g., "Sweden Central")
2. **Availability Zones** - Separate datacenters within a region
3. **Resource Groups** - Logical containers for resources (unique to Azure!)
4. **Subscriptions** - Billing boundary

---

## 💻 HANDS-ON: Your First Azure Resources

### Step 1: Install Azure CLI

```bash
# macOS
brew update && brew install azure-cli

# Linux
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Windows (PowerShell as Admin)
Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi
Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'

# Verify installation
az --version

# Output:
# azure-cli 2.56.0
```

---

### Step 2: Login to Azure

```bash
# Login (opens browser)
az login

# You'll see your subscriptions:
# [
#   {
#     "cloudName": "AzureCloud",
#     "id": "12345678-1234-1234-1234-123456789012",
#     "name": "Pay-As-You-Go",
#     "state": "Enabled",
#     "isDefault": true
#   }
# ]

# Set default subscription (if you have multiple)
az account set --subscription "Pay-As-You-Go"

# Verify current subscription
az account show
```

---

### Step 3: Create a Resource Group

**Resource Groups = Logical containers** (like folders for your cloud resources)

```bash
# Create resource group in Sweden Central
az group create \
  --name rg-devopshub-dev \
  --location swedencentral

# Output:
# {
#   "id": "/subscriptions/.../resourceGroups/rg-devopshub-dev",
#   "location": "swedencentral",
#   "name": "rg-devopshub-dev",
#   "properties": {
#     "provisioningState": "Succeeded"
#   }
# }

# List all resource groups
az group list --output table

# Output:
# Name               Location       Status
# -----------------  -------------  ---------
# rg-devopshub-dev   swedencentral  Succeeded
```

**🎯 Pro Tip:** Use naming conventions:
- `rg-` = resource group
- `vm-` = virtual machine
- `st-` = storage account
- Environment suffix: `-dev`, `-staging`, `-prod`

---

### Step 4: Create Storage Account (Like S3)

```bash
# Storage account names must be globally unique, lowercase, no hyphens
STORAGE_NAME="stdevopshub$RANDOM"

az storage account create \
  --name $STORAGE_NAME \
  --resource-group rg-devopshub-dev \
  --location swedencentral \
  --sku Standard_LRS \
  --kind StorageV2

# Output shows creation details...

# Get storage account key
STORAGE_KEY=$(az storage account keys list \
  --account-name $STORAGE_NAME \
  --resource-group rg-devopshub-dev \
  --query '[0].value' \
  --output tsv)

echo "Storage account: $STORAGE_NAME"
echo "Storage key: $STORAGE_KEY"
```

---

### Step 5: Create a Blob Container & Upload File

```bash
# Create container (like S3 bucket)
az storage container create \
  --name backups \
  --account-name $STORAGE_NAME \
  --account-key $STORAGE_KEY

# Create test file
echo "Hello from Azure!" > test.txt

# Upload file
az storage blob upload \
  --account-name $STORAGE_NAME \
  --account-key $STORAGE_KEY \
  --container-name backups \
  --name test.txt \
  --file test.txt

# List blobs
az storage blob list \
  --account-name $STORAGE_NAME \
  --account-key $STORAGE_KEY \
  --container-name backups \
  --output table

# Output:
# Name      Blob Type    Length    Content Type
# --------  -----------  --------  --------------
# test.txt  BlockBlob    18        application/octet-stream

# Download file
az storage blob download \
  --account-name $STORAGE_NAME \
  --account-key $STORAGE_KEY \
  --container-name backups \
  --name test.txt \
  --file downloaded.txt

cat downloaded.txt
# Output: Hello from Azure!
```

---

### Step 6: Create a Linux VM

```bash
# Create VM
az vm create \
  --resource-group rg-devopshub-dev \
  --name vm-web-dev \
  --image Ubuntu2204 \
  --size Standard_B1s \
  --admin-username azureuser \
  --generate-ssh-keys \
  --public-ip-sku Standard

# Output shows VM details including public IP...

# Get VM public IP
VM_IP=$(az vm list-ip-addresses \
  --resource-group rg-devopshub-dev \
  --name vm-web-dev \
  --query '[0].virtualMachine.network.publicIpAddresses[0].ipAddress' \
  --output tsv)

echo "VM IP: $VM_IP"

# SSH into VM
ssh azureuser@$VM_IP

# You're now in the VM! Install nginx:
sudo apt update
sudo apt install -y nginx
sudo systemctl start nginx

# Exit VM
exit

# Open port 80 for web traffic
az vm open-port \
  --resource-group rg-devopshub-dev \
  --name vm-web-dev \
  --port 80

# Test nginx
curl http://$VM_IP
# You'll see nginx welcome page!
```

🎉 **You just created a web server in Azure!**

---

### Step 7: Create Azure Kubernetes Service (AKS)

```bash
# Create AKS cluster (takes 5-10 minutes)
az aks create \
  --resource-group rg-devopshub-dev \
  --name aks-devopshub-dev \
  --node-count 2 \
  --node-vm-size Standard_B2s \
  --generate-ssh-keys \
  --enable-managed-identity

# Get credentials for kubectl
az aks get-credentials \
  --resource-group rg-devopshub-dev \
  --name aks-devopshub-dev

# Verify connection
kubectl get nodes

# Output:
# NAME                                STATUS   ROLES   AGE   VERSION
# aks-nodepool1-12345678-vmss000000   Ready    agent   2m    v1.28.3
# aks-nodepool1-12345678-vmss000001   Ready    agent   2m    v1.28.3

# Deploy nginx to AKS
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=LoadBalancer

# Get external IP (wait 1-2 minutes)
kubectl get service nginx --watch

# When EXTERNAL-IP shows (not <pending>), test it:
curl http://<EXTERNAL-IP>
```

---

### Step 8: Clean Up (Avoid Charges!)

```bash
# Delete entire resource group (deletes everything inside)
az group delete \
  --name rg-devopshub-dev \
  --yes \
  --no-wait

# Verify deletion
az group list --output table
# rg-devopshub-dev should be gone
```

**💡 Pro Tip:** Always delete resource groups when done learning! Azure charges by the hour.

---

## 🧠 Azure Core Services (Master These)

### 1. Compute Services

| Service | Use Case | AWS Equivalent |
|---------|----------|----------------|
| **Virtual Machines** | Full control VMs | EC2 |
| **App Service** | Web apps (PaaS) | Elastic Beanstalk |
| **AKS** | Kubernetes | EKS |
| **Azure Functions** | Serverless | Lambda |
| **Container Instances** | Simple containers | Fargate |
| **Batch** | Large-scale compute | Batch |

**Interview Answer:**
> "For compute, I choose based on control needs: VMs for full control, App Service for simple web apps, AKS for microservices, and Functions for event-driven workloads."

---

### 2. Storage Services

| Service | Use Case | AWS Equivalent |
|---------|----------|----------------|
| **Blob Storage** | Object storage | S3 |
| **File Storage** | SMB file shares | EFS |
| **Disk Storage** | VM disks | EBS |
| **Queue Storage** | Message queues | SQS |
| **Table Storage** | NoSQL key-value | DynamoDB |

**Interview Answer:**
> "Blob Storage for large files and backups, File Storage for shared file systems across VMs, Queue Storage for async processing, and Managed Disks for VM persistent storage."

---

### 3. Database Services

| Service | Use Case | AWS Equivalent |
|---------|----------|----------------|
| **Azure SQL Database** | SQL Server (PaaS) | RDS SQL Server |
| **Cosmos DB** | Multi-model NoSQL | DynamoDB |
| **Database for PostgreSQL** | PostgreSQL (PaaS) | RDS PostgreSQL |
| **Database for MySQL** | MySQL (PaaS) | RDS MySQL |
| **Redis Cache** | In-memory cache | ElastiCache |

**Why Azure SQL is Special:**
- Better SQL Server integration than AWS
- Built-in high availability
- Automatic backups
- No server management needed

---

### 4. Networking Services

| Service | Use Case | AWS Equivalent |
|---------|----------|----------------|
| **Virtual Network (VNet)** | Private network | VPC |
| **Load Balancer** | Layer 4 load balancing | ELB/NLB |
| **Application Gateway** | Layer 7 load balancing | ALB |
| **VPN Gateway** | Site-to-site VPN | VPN Gateway |
| **ExpressRoute** | Private connection to Azure | Direct Connect |
| **Traffic Manager** | Global DNS load balancing | Route 53 |

---

### 5. Identity & Security

**Azure Active Directory (Azure AD / Entra ID)**
- **Single Sign-On** for all Azure services
- **Multi-Factor Authentication** built-in
- **Integrates with on-premises AD** (hybrid identity)
- **Role-Based Access Control (RBAC)**

```bash
# Grant user access to resource group
az role assignment create \
  --assignee user@company.com \
  --role Contributor \
  --resource-group rg-devopshub-dev

# Built-in roles:
# - Owner: Full access
# - Contributor: Manage resources but not access
# - Reader: Read-only
# - Custom roles: Define your own
```

---

## 💼 Interview Preparation

### Question 1: Architecture

**Interviewer:** "How would you design a highly available web application in Azure?"

✅ **Strong Answer:**
> "I'd use a multi-zone architecture: Deploy App Service or AKS across availability zones with Azure Front Door for global load balancing and DDoS protection. Use Azure SQL with zone-redundant configuration for the database, and Blob Storage with GRS replication for static assets. Implement Azure Monitor for observability and Application Insights for application performance. For CI/CD, use Azure DevOps or GitHub Actions with deployment slots for blue-green deployments."

**Why this impresses:** Shows knowledge of HA, security, monitoring, and deployment strategies.

---

### Question 2: Cost Optimization

**Interviewer:** "How do you optimize Azure costs?"

✅ **Strong Answer:**
> "Several strategies: 1) Reserved Instances for predictable workloads (up to 72% savings). 2) Auto-scaling to match demand - scale down non-prod environments at night. 3) Use B-series VMs for variable workloads. 4) Set budget alerts with Azure Cost Management. 5) Delete unused resources using Azure Advisor recommendations. 6) Use Blob Storage lifecycle policies to move old data to cool/archive tiers. 7) Tag resources by cost center for chargeback."

**Why this impresses:** Cost optimization is critical for senior roles.

---

### Question 3: Security

**Interviewer:** "How do you secure Azure resources?"

✅ **Strong Answer:**
> "Security in layers: 1) Azure AD with MFA for identity. 2) RBAC for least-privilege access. 3) Network Security Groups for firewall rules. 4) Azure Key Vault for secrets management - never hardcode credentials. 5) Enable Azure Defender (Security Center) for threat detection. 6) Private Endpoints to keep traffic off public internet. 7) Azure Policy to enforce standards. 8) Regular vulnerability scanning with Azure Security Center. 9) Audit logs with Azure Monitor."

**Why this impresses:** Security is top priority in 2026.

---

### Question 4: Disaster Recovery

**Interviewer:** "How do you implement disaster recovery in Azure?"

✅ **Strong Answer:**
> "Depends on RTO/RPO requirements. For critical systems: 1) Azure Site Recovery for VM replication to secondary region. 2) Geo-redundant storage (GRS) for Blob Storage. 3) Azure SQL with active geo-replication. 4) Azure Traffic Manager or Front Door for automatic failover. 5) Regular DR drills to verify RPO/RTO. 6) Infrastructure as Code (Terraform) so we can rebuild in any region. For less critical: Azure Backup with cross-region restore."

**Why this impresses:** DR is often tested in interviews.

---

## 🎯 Common Azure Commands (Memorize These!)

### Resource Management

```bash
# List all resources
az resource list --output table

# List by resource group
az resource list --resource-group rg-devopshub-dev --output table

# Get resource details
az resource show --ids /subscriptions/.../resourceGroups/rg.../providers/Microsoft.Compute/virtualMachines/vm-web

# Delete resource
az resource delete --ids <resource-id>

# Tag resources
az resource tag --tags Environment=Dev CostCenter=Engineering --ids <resource-id>
```

### Monitoring & Troubleshooting

```bash
# View activity log
az monitor activity-log list --resource-group rg-devopshub-dev

# View metrics
az monitor metrics list --resource <resource-id> --metric-names "Percentage CPU"

# Create alert
az monitor metrics alert create \
  --name cpu-alert \
  --resource-group rg-devopshub-dev \
  --scopes <resource-id> \
  --condition "avg Percentage CPU > 80" \
  --description "Alert when CPU > 80%"
```

---

## 📚 Flashcards

**Q: What's a Resource Group?**
A: Logical container for Azure resources. Lifecycle management - delete RG = delete all resources.

**Q: What's the difference between Blob Storage and File Storage?**
A: Blob = object storage (REST API, like S3). File = SMB file shares (mount like network drive).

**Q: What are Availability Zones?**
A: Physically separate datacenters within a region (independent power, cooling, networking).

**Q: What's the Azure equivalent of AWS IAM?**
A: Azure AD (Entra ID) for identity + RBAC for permissions.

**Q: What's the Azure equivalent of EC2?**
A: Azure Virtual Machines.

**Q: What's the Azure equivalent of S3?**
A: Azure Blob Storage.

**Q: What's AKS?**
A: Azure Kubernetes Service - managed Kubernetes.

**Q: How do you secure secrets in Azure?**
A: Azure Key Vault - centralized secrets management.

**Q: What's Azure CLI command structure?**
A: `az <service> <command> --parameters`

**Q: How do you estimate Azure costs?**
A: Azure Pricing Calculator (https://azure.microsoft.com/pricing/calculator/)

---

## 🎓 Quiz

### Question 1: Architecture

**You need to deploy a .NET web app. Which service should you use?**

A) Virtual Machines
B) App Service ✅
C) Container Instances
D) Azure Functions

**Explanation:** App Service is purpose-built for web apps, provides auto-scaling, deployment slots, and excellent .NET support.

---

### Question 2: Storage

**Which storage type should you use for VM boot disks?**

A) Blob Storage
B) File Storage
C) Managed Disks ✅
D) Queue Storage

**Explanation:** Managed Disks are designed for VM disks with automatic replication and snapshots.

---

### Question 3: Security

**You want to store database passwords securely. Where should they go?**

A) Environment variables in VM
B) Configuration file in Blob Storage
C) Azure Key Vault ✅
D) Azure Table Storage

**Explanation:** Key Vault is designed for secrets management with encryption, access policies, and audit logs.

---

## 🏆 Portfolio Project: Multi-Tier Web App

**Build this for your GitHub:**

Deploy a production-ready web application:
- **Frontend**: React (App Service or Static Web Apps)
- **Backend**: Node.js API (App Service with auto-scaling)
- **Database**: Azure SQL Database (zone-redundant)
- **Cache**: Azure Redis Cache
- **Storage**: Blob Storage for user uploads
- **CDN**: Azure CDN for static assets
- **Monitoring**: Application Insights
- **CI/CD**: GitHub Actions with deployment slots

**Infrastructure as Code:**
```hcl
# Use Terraform to define everything
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── networking.tf
├── compute.tf
└── database.tf
```

**Why this impresses:**
- ✅ Multi-tier architecture
- ✅ High availability
- ✅ Infrastructure as Code
- ✅ CI/CD pipeline
- ✅ Monitoring & observability
- ✅ Security best practices

---

## ⚠️ Common Mistakes (Avoid These!)

### ❌ Mistake 1: Not Using Resource Groups Properly

```bash
# DON'T: Mix dev/prod in same resource group
az group create --name my-resources --location swedencentral
```

**Fix:**
```bash
# DO: Separate by environment and team
az group create --name rg-web-dev --location swedencentral
az group create --name rg-web-prod --location swedencentral
az group create --name rg-data-dev --location swedencentral
```

---

### ❌ Mistake 2: Using Public IPs Unnecessarily

```bash
# DON'T: Every VM with public IP
az vm create --name vm1 --public-ip-address vm1-ip
```

**Fix:**
```bash
# DO: Use bastion host or VPN for access
az network bastion create --name bastion --resource-group rg-dev --vnet-name vnet-dev
```

---

### ❌ Mistake 3: Not Setting Cost Alerts

**Fix:**
```bash
# Set budget alert
az consumption budget create \
  --amount 500 \
  --budget-name monthly-budget \
  --time-period-start 2026-01-01 \
  --time-period-end 2027-01-01 \
  --threshold 80
```

---

## 📈 Next Steps

### After This Module:
1. **Azure DevOps Pipelines** - CI/CD automation
2. **Azure Monitor & Log Analytics** - Observability
3. **Azure Security** - Advanced security patterns
4. **Terraform on Azure** - Infrastructure as Code

### Certifications Worth Getting:
- **AZ-900** - Azure Fundamentals (entry-level, 2-3 weeks)
- **AZ-104** - Azure Administrator (intermediate, 1-2 months)
- **AZ-305** - Azure Solutions Architect (advanced, 2-3 months)

---

## 🌟 Module Summary

✅ **Hands-on experience** - Created VMs, storage, AKS
✅ **CLI proficiency** - Mastered az commands
✅ **Architecture knowledge** - Understand Azure services
✅ **Cost awareness** - Know how to optimize
✅ **Security mindset** - Key Vault, RBAC, Network Security
✅ **Interview ready** - Can answer technical questions
✅ **Multi-cloud** - Understand Azure vs AWS differences

**Job market impact:** Opens 78% of enterprise DevOps roles
**Salary boost:** +20-30% with Azure + AWS
**Time to complete:** 2 hours

---

**Module completed!** 🎉

**Next recommended:** Google Cloud Platform (GCP) - Complete the multi-cloud trifecta!
"""
}

MODULE = {
    "id": "cloud-azure-fundamentals",
    "slug": "cloud-azure-fundamentals",
    "title": "Azure Fundamentals",
    "description": "Master Microsoft Azure - the #2 cloud provider. 78% of enterprises use Azure. Opens enterprise DevOps roles. +25% salary boost.",
    "icon": "☁️",
    "category": "cloud",
    "difficulty": "beginner",
    "estimated_hours": 8,
    "tasks": [AZURE_CORE_SERVICES],
}
