"""
Google Cloud Platform (GCP) Fundamentals
=========================================

Master Google Cloud - the #3 cloud provider built on Google's infrastructure.
Powers YouTube, Gmail, Search. Best for data analytics & machine learning.

Career Impact: Opens 45% of cloud roles, especially at startups. +20% salary.
"""

GCP_CORE_SERVICES = {
    "title": "GCP Core Services & Architecture",
    "slug": "gcp-core-services",
    "description": "Master Google Cloud Platform: compute, storage, networking, and BigQuery. Learn the infrastructure behind Google Search and YouTube.",
    "difficulty": "beginner",
    "estimated_minutes": 120,
    "xp_reward": 200,
    "order_index": 1,
    "content": r"""# Google Cloud Platform Core Services

## 🎯 TL;DR (30 seconds)

Google Cloud Platform (GCP) is the #3 cloud provider (10% market share) running on the same infrastructure as Google Search, YouTube, and Gmail. **Best-in-class for data analytics (BigQuery), Kubernetes (GKE invented K8s), and ML/AI.**

**Why this matters:** Startups and data-driven companies prefer GCP. Learning all three clouds (AWS + Azure + GCP) makes you **irreplaceable**. **Multi-cloud engineers earn 40% more.**

---

## 🚀 Why GCP Matters for Your Career

### The Startup & Data Science Reality

**Who uses GCP:**
- **Startups** (45% of Y Combinator companies use GCP)
- **Data-driven companies** (Spotify, Twitter, Snapchat)
- **E-commerce** (eBay, Target, Home Depot)
- **Gaming** (Nintendo, Ubisoft)

**Why GCP?**
1. **Best data analytics** - BigQuery is unmatched
2. **Best Kubernetes** - Google invented Kubernetes
3. **Cheapest pricing** - Automatic sustained use discounts
4. **Best ML/AI** - TensorFlow, Vertex AI, TPUs
5. **Developer-friendly** - Simplest APIs

**Job Market Analysis (2026):**
- 45% of cloud-native startups use GCP
- 67% of data engineering roles prefer GCP (BigQuery)
- 89% of ML engineering roles use GCP (Vertex AI, TPUs)

**Career Positioning:**
- ✅ AWS only → "Just another AWS person"
- ✅ AWS + Azure → "Enterprise ready"
- ✅ AWS + Azure + GCP → **"Multi-cloud expert" (40% higher salary)**

### Salary Impact (Sweden 2026)

| Role | Single Cloud | Multi-Cloud (AWS+Azure+GCP) | Difference |
|------|--------------|----------------------------|------------|
| DevOps Engineer | 55,000 SEK | 72,000 SEK | **+31%** |
| Cloud Architect | 70,000 SEK | 95,000 SEK | **+36%** |
| Data Engineer | 60,000 SEK | 82,000 SEK | **+37%** |

**Learning GCP = +17,000 SEK/month = +204,000 SEK/year** 💰

---

## 📖 THEORY: GCP vs AWS vs Azure

### Mental Model: GCP = AWS but Simpler & Data-Focused

| Concept | AWS | Azure | GCP | Why GCP Different |
|---------|-----|-------|-----|-------------------|
| **VMs** | EC2 | Virtual Machines | Compute Engine | Cheaper with sustained use |
| **Storage** | S3 | Blob Storage | Cloud Storage | Same concepts |
| **Database** | RDS | Azure SQL | Cloud SQL | Simpler setup |
| **NoSQL** | DynamoDB | Cosmos DB | Firestore | Better for mobile apps |
| **Kubernetes** | EKS | AKS | **GKE** | **Best K8s (Google invented it!)** |
| **Serverless** | Lambda | Functions | Cloud Functions | Similar |
| **Data Warehouse** | Redshift | Synapse | **BigQuery** | **Serverless, query petabytes instantly** |
| **ML Platform** | SageMaker | ML Studio | **Vertex AI** | **Best for TensorFlow** |
| **Identity** | IAM | Azure AD | IAM | Similar to AWS |
| **CLI** | aws | az | gcloud | Most developer-friendly |

**Key Insights:**
1. **Easier to learn than AWS** - Fewer services, simpler naming
2. **Better for data** - BigQuery alone is worth learning GCP
3. **Better for K8s** - GKE is the gold standard
4. **Cheaper** - Automatic discounts (no upfront commitment)

---

## 🏗️ GCP Core Architecture

### Global Infrastructure

```
┌──────────────────────────────────────────────────────────┐
│                 GOOGLE CLOUD GLOBAL NETWORK               │
│                                                          │
│  35+ Regions, 100+ Zones                                 │
│  ├─ europe-north1 (Finland)                             │
│  ├─ europe-west1 (Belgium)                              │
│  ├─ us-central1 (Iowa)                                  │
│  └─ asia-southeast1 (Singapore)                         │
│                                                          │
│  Each Region has:                                       │
│  ├─ 3+ Zones (independent datacenters)                  │
│  ├─ Private fiber network                               │
│  └─ Same network as YouTube/Gmail (99.99% uptime)      │
└──────────────────────────────────────────────────────────┘
```

**Key Difference from AWS/Azure:**
- **Projects** instead of accounts (better organization)
- **No separate networking charge** (data transfer within region is free!)
- **Global load balancing** built-in (no extra cost)

---

## 💻 HANDS-ON: Your First GCP Resources

### Step 1: Install Google Cloud SDK

```bash
# macOS
brew install --cask google-cloud-sdk

# Linux
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Windows (PowerShell)
(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
& $env:Temp\GoogleCloudSDKInstaller.exe

# Verify installation
gcloud --version

# Output:
# Google Cloud SDK 461.0.0
```

---

### Step 2: Initialize & Login

```bash
# Initialize (interactive setup)
gcloud init

# Or login separately
gcloud auth login

# Browser opens, you authenticate...

# List your projects
gcloud projects list

# Create new project
gcloud projects create devopshub-learning-$(date +%s) --name="DevOpsHub Learning"

# Set default project
PROJECT_ID="devopshub-learning-xxxxx"  # Use your project ID
gcloud config set project $PROJECT_ID

# Enable billing (required for most services)
# Note: This requires billing account ID from console
gcloud beta billing projects link $PROJECT_ID --billing-account=XXXXXX-XXXXXX-XXXXXX
```

---

### Step 3: Create Storage Bucket (Like S3)

```bash
# Enable Cloud Storage API
gcloud services enable storage.googleapis.com

# Create bucket (globally unique name)
BUCKET_NAME="devopshub-storage-$(date +%s)"
gcloud storage buckets create gs://$BUCKET_NAME \
  --location=europe-north1 \
  --uniform-bucket-level-access

# Output:
# Creating gs://devopshub-storage-xxxxx/...

# Upload file
echo "Hello from GCP!" > test.txt
gcloud storage cp test.txt gs://$BUCKET_NAME/

# List files
gcloud storage ls gs://$BUCKET_NAME/

# Output:
# gs://devopshub-storage-xxxxx/test.txt

# Download file
gcloud storage cp gs://$BUCKET_NAME/test.txt downloaded.txt

# Make file public (for static hosting)
gcloud storage objects update gs://$BUCKET_NAME/test.txt --add-acl-grant=entity=allUsers,role=READER

# Get public URL
echo "https://storage.googleapis.com/$BUCKET_NAME/test.txt"
```

---

### Step 4: Create Compute Engine VM

```bash
# Enable Compute Engine API
gcloud services enable compute.googleapis.com

# Create VM
gcloud compute instances create vm-web-dev \
  --zone=europe-north1-a \
  --machine-type=e2-micro \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --tags=http-server \
  --metadata=startup-script='#!/bin/bash
apt-get update
apt-get install -y nginx
systemctl start nginx'

# Output shows VM details...

# Create firewall rule for HTTP
gcloud compute firewall-rules create allow-http \
  --allow tcp:80 \
  --target-tags http-server \
  --description="Allow HTTP traffic"

# Get VM external IP
VM_IP=$(gcloud compute instances describe vm-web-dev \
  --zone=europe-north1-a \
  --format='get(networkInterfaces[0].accessConfigs[0].natIP)')

echo "VM IP: $VM_IP"

# Wait 30 seconds for nginx to start, then test
sleep 30
curl http://$VM_IP

# You'll see nginx welcome page!

# SSH into VM
gcloud compute ssh vm-web-dev --zone=europe-north1-a
```

🎉 **You created a web server in GCP!**

---

### Step 5: Create Google Kubernetes Engine (GKE) Cluster

```bash
# Enable GKE API
gcloud services enable container.googleapis.com

# Create GKE cluster (takes 3-5 minutes)
gcloud container clusters create gke-devopshub \
  --zone=europe-north1-a \
  --num-nodes=2 \
  --machine-type=e2-medium \
  --enable-autoscaling \
  --min-nodes=1 \
  --max-nodes=5

# Get credentials for kubectl
gcloud container clusters get-credentials gke-devopshub --zone=europe-north1-a

# Verify
kubectl get nodes

# Output:
# NAME                                          STATUS   ROLES    AGE   VERSION
# gke-gke-devopshub-default-pool-xxx-xxx        Ready    <none>   2m    v1.28.3-gke.1234
# gke-gke-devopshub-default-pool-xxx-yyy        Ready    <none>   2m    v1.28.3-gke.1234

# Deploy nginx
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=LoadBalancer

# Get external IP (wait 1-2 minutes)
kubectl get service nginx --watch

# When EXTERNAL-IP shows, test:
curl http://<EXTERNAL-IP>
```

---

### Step 6: BigQuery - Query Petabytes of Data

**BigQuery = Serverless data warehouse (no servers to manage!)**

```bash
# Enable BigQuery API
gcloud services enable bigquery.googleapis.com

# Query public dataset (Stack Overflow data!)
bq query --use_legacy_sql=false '
SELECT
  tags,
  COUNT(*) as question_count
FROM `bigquery-public-data.stackoverflow.posts_questions`
WHERE EXTRACT(YEAR FROM creation_date) = 2024
  AND tags LIKE "%kubernetes%"
GROUP BY tags
ORDER BY question_count DESC
LIMIT 10
'

# Output shows top Kubernetes questions!
# This queried BILLIONS of rows in seconds - no infrastructure needed!

# Create your own dataset
bq mk --dataset $PROJECT_ID:devops_metrics

# Create table
bq mk --table $PROJECT_ID:devops_metrics.deployments \
  deployment_id:STRING,timestamp:TIMESTAMP,service:STRING,status:STRING,duration_seconds:INTEGER

# Insert data
echo '{"deployment_id":"deploy-001","timestamp":"2026-01-13T10:00:00","service":"api","status":"success","duration_seconds":45}' | \
  bq insert $PROJECT_ID:devops_metrics.deployments

# Query your data
bq query --use_legacy_sql=false "
SELECT * FROM \`$PROJECT_ID.devops_metrics.deployments\`
"
```

**🔥 This is GCP's killer feature!** Query petabytes without managing servers.

---

### Step 7: Cloud Functions (Serverless)

```bash
# Enable Cloud Functions API
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable cloudbuild.googleapis.com

# Create simple function
mkdir hello-function && cd hello-function

# Create function code
cat > main.py << 'EOF'
def hello_world(request):
    name = request.args.get('name', 'World')
    return f'Hello {name} from GCP Cloud Functions!'
EOF

# Create requirements.txt
cat > requirements.txt << 'EOF'
functions-framework==3.*
EOF

# Deploy function
gcloud functions deploy hello-world \
  --runtime=python311 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point=hello_world \
  --region=europe-north1

# Test function
FUNCTION_URL=$(gcloud functions describe hello-world --region=europe-north1 --format='value(serviceConfig.uri)')

curl "$FUNCTION_URL?name=DevOps"

# Output: Hello DevOps from GCP Cloud Functions!

cd ..
```

---

### Step 8: Clean Up (Avoid Charges!)

```bash
# Delete GKE cluster
gcloud container clusters delete gke-devopshub --zone=europe-north1-a --quiet

# Delete VM
gcloud compute instances delete vm-web-dev --zone=europe-north1-a --quiet

# Delete firewall rule
gcloud compute firewall-rules delete allow-http --quiet

# Delete Cloud Function
gcloud functions delete hello-world --region=europe-north1 --quiet

# Delete storage bucket
gcloud storage rm --recursive gs://$BUCKET_NAME

# Delete BigQuery dataset
bq rm -r -f $PROJECT_ID:devops_metrics

# Delete project (nuclear option - deletes EVERYTHING)
# gcloud projects delete $PROJECT_ID
```

---

## 🧠 GCP Core Services (Master These)

### 1. Compute Services

| Service | Use Case | AWS Equivalent | When to Use |
|---------|----------|----------------|-------------|
| **Compute Engine** | VMs | EC2 | Full control needed |
| **App Engine** | Web apps (PaaS) | Elastic Beanstalk | Quick deployments |
| **GKE** | Kubernetes | EKS | **Best K8s experience** |
| **Cloud Functions** | Serverless | Lambda | Event-driven |
| **Cloud Run** | Containers (serverless) | Fargate | **Easiest container deployment** |

**Interview Answer:**
> "GKE for microservices (best K8s), Cloud Run for containerized apps without managing clusters, Compute Engine for legacy apps needing VMs, and Cloud Functions for simple event-driven tasks."

---

### 2. Storage Services

| Service | Use Case | AWS Equivalent |
|---------|----------|----------------|
| **Cloud Storage** | Object storage | S3 |
| **Persistent Disk** | VM disks | EBS |
| **Filestore** | NFS file shares | EFS |

**Storage Classes:**
- **Standard** - Hot data (frequently accessed)
- **Nearline** - Accessed once/month (backups)
- **Coldline** - Accessed once/quarter (archives)
- **Archive** - Accessed once/year (long-term)

**Auto-tiering saves money!**

---

### 3. Database Services

| Service | Use Case | AWS Equivalent | Why Choose GCP |
|---------|----------|----------------|----------------|
| **Cloud SQL** | PostgreSQL/MySQL | RDS | Simpler than AWS |
| **Cloud Spanner** | Global SQL | Aurora Global | **Globally distributed** |
| **Firestore** | NoSQL documents | DynamoDB | Better mobile apps |
| **Bigtable** | Wide-column NoSQL | DynamoDB | **Powers Google Search** |
| **BigQuery** | Data warehouse | Redshift | **Serverless, instant queries** |
| **Memorystore** | Redis/Memcached | ElastiCache | Managed cache |

**BigQuery is the killer app** - no other cloud has anything this good!

---

### 4. Networking Services

| Service | Use Case | AWS Equivalent |
|---------|----------|----------------|
| **VPC** | Private network | VPC |
| **Cloud Load Balancing** | Global LB | ELB + Route53 |
| **Cloud CDN** | Content delivery | CloudFront |
| **Cloud Armor** | DDoS protection | Shield |
| **Cloud VPN** | Site-to-site VPN | VPN Gateway |
| **Cloud Interconnect** | Private connection | Direct Connect |

**GCP Advantage:** Global load balancing is built-in and simpler than AWS.

---

### 5. Identity & Security

**Cloud IAM (Identity and Access Management)**

```bash
# Grant user access to project
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="user:engineer@company.com" \
  --role="roles/editor"

# Built-in roles:
# - roles/owner: Full control
# - roles/editor: Can modify resources
# - roles/viewer: Read-only
# - Custom roles: Define your own

# Service accounts (for apps, not humans)
gcloud iam service-accounts create app-backend \
  --display-name="Backend Application"

# Grant service account access to bucket
gcloud storage buckets add-iam-policy-binding gs://$BUCKET_NAME \
  --member="serviceAccount:app-backend@$PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
```

**Secret Manager (like AWS Secrets Manager)**

```bash
# Enable Secret Manager
gcloud services enable secretmanager.googleapis.com

# Create secret
echo -n "super-secret-password" | \
  gcloud secrets create db-password --data-file=-

# Access secret
gcloud secrets versions access latest --secret=db-password

# Output: super-secret-password
```

---

## 💼 Interview Preparation

### Question 1: When to Use GCP vs AWS

**Interviewer:** "When would you choose GCP over AWS?"

✅ **Strong Answer:**
> "I'd choose GCP for: 1) Data analytics projects - BigQuery is unmatched for ad-hoc analysis of large datasets. 2) Kubernetes workloads - GKE is the best managed K8s with autopilot mode. 3) Machine learning - Vertex AI and TPUs are superior for TensorFlow workloads. 4) Cost optimization - GCP's sustained use discounts are automatic (no upfront commitment like AWS Reserved Instances). 5) Startups - simpler pricing and fewer services to learn. That said, I'd choose AWS for enterprise with existing AWS footprint, or when ecosystem maturity matters (more third-party integrations)."

**Why this impresses:** Shows you understand trade-offs, not just features.

---

### Question 2: BigQuery Architecture

**Interviewer:** "Explain how BigQuery can query petabytes so fast."

✅ **Strong Answer:**
> "BigQuery separates storage and compute (unlike traditional databases). Data is stored in Google's Colossus filesystem in columnar format. When you query, BigQuery spins up thousands of workers in parallel across Google's network. It uses a distributed execution tree - the root node aggregates results from thousands of leaf nodes reading data. Because storage is columnar, it only reads columns you query (not entire rows). Plus, Google's network is incredibly fast. You're essentially renting Google Search's infrastructure for your queries."

**Why this impresses:** Deep understanding of architecture.

---

### Question 3: GKE Autopilot vs Standard

**Interviewer:** "What's the difference between GKE Autopilot and Standard?"

✅ **Strong Answer:**
> "GKE Standard is like traditional K8s - you manage node pools, scaling, upgrades, and security. GKE Autopilot is fully managed - Google handles nodes, you just deploy pods. Autopilot pros: less operational burden, automatic security best practices, cost optimization (pay per pod, not per node). Cons: less control, can't use DaemonSets or privileged containers. I'd use Autopilot for most apps (95% of use cases), and Standard only when needing custom node configurations, GPUs, or specific kernel modules."

**Why this impresses:** Knows the trade-offs.

---

### Question 4: GCP Cost Optimization

**Interviewer:** "How do you optimize GCP costs?"

✅ **Strong Answer:**
> "GCP has automatic optimizations that AWS doesn't: 1) Sustained use discounts - automatic up to 30% off for consistent usage. 2) Committed use discounts - 1 or 3 year commitments for 50-70% off. 3) Preemptible VMs - 80% cheaper for fault-tolerant workloads. 4) GKE Autopilot - pay per pod, not node (can save 40%). 5) BigQuery - only pay for data scanned (partition tables by date, use clustering). 6) Storage lifecycle policies - auto-move old data to Nearline/Coldline. 7) Use Cloud Run instead of GKE for variable traffic (scales to zero). 8) Set budget alerts and quotas."

**Why this impresses:** Cost optimization is critical.

---

## 🎯 Common GCP Commands (Memorize These!)

### Project Management

```bash
# List projects
gcloud projects list

# Switch project
gcloud config set project PROJECT_ID

# Current config
gcloud config list

# View all APIs enabled
gcloud services list

# Enable an API
gcloud services enable compute.googleapis.com
```

### Compute

```bash
# List VMs
gcloud compute instances list

# Start/stop VM
gcloud compute instances start VM_NAME --zone=ZONE
gcloud compute instances stop VM_NAME --zone=ZONE

# SSH to VM
gcloud compute ssh VM_NAME --zone=ZONE

# List firewall rules
gcloud compute firewall-rules list
```

### Kubernetes

```bash
# List clusters
gcloud container clusters list

# Get credentials
gcloud container clusters get-credentials CLUSTER_NAME --zone=ZONE

# Resize cluster
gcloud container clusters resize CLUSTER_NAME --num-nodes=5 --zone=ZONE
```

### Storage

```bash
# List buckets
gcloud storage ls

# Copy files
gcloud storage cp file.txt gs://bucket-name/
gcloud storage cp gs://bucket-name/file.txt ./

# Sync directories
gcloud storage rsync local-dir gs://bucket-name/remote-dir
```

---

## 📚 Flashcards

**Q: What's GCP's biggest advantage over AWS?**
A: BigQuery (serverless data warehouse) and GKE (best Kubernetes).

**Q: What's a GCP Project?**
A: Organizational unit that contains resources (like AWS account).

**Q: What's the GCP equivalent of S3?**
A: Cloud Storage.

**Q: What's the GCP equivalent of EC2?**
A: Compute Engine.

**Q: What's the GCP equivalent of Lambda?**
A: Cloud Functions (or Cloud Run for containers).

**Q: What's BigQuery?**
A: Serverless data warehouse - query petabytes without managing infrastructure.

**Q: What's Cloud Run?**
A: Serverless containers - deploy any container without managing servers.

**Q: What's GKE Autopilot?**
A: Fully managed Kubernetes - Google manages nodes, you deploy pods.

**Q: What are preemptible VMs?**
A: 80% cheaper VMs that can be terminated anytime (for fault-tolerant workloads).

**Q: What are sustained use discounts?**
A: Automatic discounts (up to 30%) for consistent VM usage - no commitment needed.

---

## 🎓 Quiz

### Question 1: Services

**You need to run a containerized app that scales to zero when not used. Which service?**

A) GKE
B) Compute Engine
C) Cloud Run ✅
D) Cloud Functions

**Explanation:** Cloud Run runs containers, scales to zero, and is fully serverless. Perfect for variable traffic.

---

### Question 2: Data

**You need to analyze 5 TB of logs daily. Which service?**

A) Cloud SQL
B) BigQuery ✅
C) Firestore
D) Cloud Storage

**Explanation:** BigQuery is designed for analytics on large datasets. Can query terabytes in seconds.

---

### Question 3: Cost

**Which GCP feature automatically reduces costs without commitment?**

A) Committed use discounts
B) Preemptible VMs
C) Sustained use discounts ✅
D) Budget alerts

**Explanation:** Sustained use discounts are automatic - up to 30% off for consistent usage.

---

## 🏆 Portfolio Project: Data Pipeline

**Build this for your GitHub:**

**Real-time data pipeline:**
1. **Ingest**: Cloud Functions triggered by Cloud Storage uploads
2. **Process**: Dataflow (Apache Beam) for transformations
3. **Store**: BigQuery for analytics
4. **Visualize**: Looker Studio (free!) for dashboards
5. **Orchestrate**: Cloud Composer (managed Airflow)
6. **Monitor**: Cloud Monitoring & Logging

**Tech Stack:**
```
GCS Bucket (CSV uploads)
  ↓
Cloud Function (trigger)
  ↓
Pub/Sub (message queue)
  ↓
Dataflow (processing)
  ↓
BigQuery (storage)
  ↓
Looker Studio (dashboards)
```

**Why this impresses:**
- ✅ Real-world data engineering
- ✅ Serverless architecture
- ✅ Event-driven design
- ✅ BigQuery expertise
- ✅ Monitoring included

---

## ⚠️ Common Mistakes

### ❌ Mistake 1: Not Using Service Accounts

```bash
# DON'T: Use personal account in code
gcloud auth login
# Then hardcode credentials
```

**Fix:**
```bash
# DO: Use service accounts
gcloud iam service-accounts create my-app
gcloud iam service-accounts keys create key.json --iam-account=my-app@project.iam.gserviceaccount.com
export GOOGLE_APPLICATION_CREDENTIALS="key.json"
```

---

### ❌ Mistake 2: Not Partitioning BigQuery Tables

```sql
-- DON'T: Scan entire table every query (expensive!)
SELECT * FROM logs WHERE date = '2026-01-13'
```

**Fix:**
```sql
-- DO: Partition by date
CREATE TABLE logs (
  date DATE,
  message STRING
)
PARTITION BY date;

-- Queries now only scan relevant partitions (much cheaper!)
```

---

## 📈 Next Steps

### After This Module:
1. **BigQuery Advanced** - Optimize queries, ML in SQL
2. **GKE Deep Dive** - Autopilot, multi-cluster, service mesh
3. **Cloud Run Patterns** - Microservices architecture
4. **Data Engineering on GCP** - Dataflow, Pub/Sub, Composer

### Certifications:
- **Cloud Digital Leader** - Business-focused (easy)
- **Associate Cloud Engineer** - Most popular (2-3 months)
- **Professional Cloud Architect** - Advanced (3-4 months)

---

## 🌟 Module Summary

✅ **Multi-cloud expertise** - AWS + Azure + GCP = Irreplaceable
✅ **BigQuery hands-on** - Queried public datasets
✅ **GKE deployed** - Best Kubernetes experience
✅ **Cloud Run** - Serverless containers
✅ **Cost optimization** - Sustained use discounts
✅ **Data pipeline** - Real-world project ready

**Job market impact:** Opens startup & data-focused roles
**Salary boost:** +20% on top of AWS/Azure skills
**Time to complete:** 2 hours

---

**Module completed!** 🎉

**You now know all 3 major clouds! This makes you a multi-cloud expert.** 🏆

**Next recommended:** Multi-Cloud Architecture - Learn to design across clouds!
"""
}

MODULE = {
    "id": "cloud-gcp-fundamentals",
    "slug": "cloud-gcp-fundamentals",
    "title": "Google Cloud Platform (GCP)",
    "description": "Master Google Cloud - powers YouTube, Gmail. Best for data analytics (BigQuery) and Kubernetes (GKE). Opens startup roles. +20% salary.",
    "icon": "☁️",
    "category": "cloud",
    "difficulty": "beginner",
    "estimated_hours": 8,
    "tasks": [GCP_CORE_SERVICES],
}
