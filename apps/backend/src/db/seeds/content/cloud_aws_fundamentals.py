"""
AWS Cloud Fundamentals - Essential Cloud Skills for DevOps
==========================================================

Master Amazon Web Services basics - required in 85% of DevOps jobs.
Understanding cloud infrastructure is no longer optional.

MODULES:
1. Cloud Concepts & AWS Account Setup
2. EC2 - Virtual Servers in the Cloud
3. S3 - Object Storage & Static Hosting
4. VPC - Network Architecture in AWS
5. IAM - Identity & Access Management
6. RDS - Managed Databases
7. CloudWatch - Monitoring & Logging
8. Cost Optimization & Well-Architected Framework

Learn enough to pass interviews and work with production AWS infrastructure.
"""

# =============================================================================
# MODULE 1: CLOUD CONCEPTS & AWS BASICS
# =============================================================================

CLOUD_CONCEPTS_AWS = {
    "title": "Cloud Concepts & AWS Fundamentals",
    "slug": "cloud-aws-basics",
    "description": "Understand cloud computing fundamentals and AWS core services. Learn why companies migrate to cloud and how AWS became the industry standard.",
    "difficulty": "beginner",
    "estimated_minutes": 90,
    "xp_reward": 150,
    "order_index": 1,
    "content": r"""# Cloud Concepts & AWS Fundamentals

## 🎯 TL;DR (30 seconds)

Cloud computing means renting computers/storage/databases instead of buying physical servers. AWS is the biggest cloud provider (32% market share). Instead of spending $50,000 upfront for servers, you pay $500/month and scale instantly.

**Why this matters:** 85% of DevOps jobs require AWS/Azure/GCP. Learning AWS is the fastest path to cloud skills.

---

## 🚀 Career Impact

**Job Market Reality (2026):**
- 85% of DevOps roles require cloud experience
- 45% specifically mention AWS (more than Azure or GCP)
- "Cloud experience" in job posting = +20-30% higher salary

**Interview Question You WILL Hear:**
> "Have you worked with AWS? Which services?"

**Without AWS knowledge:** Eliminated from 85% of job opportunities
**With AWS basics:** Qualify for cloud-focused roles

**Salary Impact (Sweden 2026):**
| Role | No Cloud | With AWS | Difference |
|------|----------|----------|------------|
| Junior DevOps | 38,000 SEK | 46,000 SEK | **+21%** |
| Mid DevOps | 48,000 SEK | 58,000 SEK | **+21%** |
| Senior DevOps | 60,000 SEK | 72,000 SEK | **+20%** |

---

## 📖 THEORY: What is Cloud Computing?

### The Traditional Way (On-Premise)

**How companies used to run websites (pre-2006):**

```
Company needs a website:
1. Buy physical servers ($50,000+)
2. Buy networking equipment ($20,000+)
3. Rent datacenter space ($5,000/month)
4. Hire 24/7 operations team ($500,000/year)
5. Plan capacity for peak load (Black Friday)
6. 90% of servers idle most of the time
7. Wait 6 months for procurement
8. Total cost: $1M+ upfront + $500k/year ongoing
```

**Problems:**
- ❌ Huge upfront cost
- ❌ Slow (6 months to get new servers)
- ❌ Wasteful (servers idle 90% of time)
- ❌ Risky (what if you scale wrong?)
- ❌ Complex (need ops team 24/7)

---

### The Cloud Way

**How companies run websites today:**

```
Company needs a website:
1. Create AWS account (5 minutes, $0)
2. Launch EC2 instance (2 minutes, $50/month)
3. Traffic spikes? Auto-scale to 100 servers (5 minutes)
4. Traffic drops? Scale back to 2 servers automatically
5. Pay only for what you use
6. AWS handles hardware/networking/datacenter
7. Total cost: $0 upfront + $500/month (scales with usage)
```

**Benefits:**
- ✅ No upfront cost (pay-as-you-go)
- ✅ Fast (spin up servers in minutes)
- ✅ Efficient (pay only for what you use)
- ✅ Flexible (scale up/down instantly)
- ✅ Managed (AWS handles infrastructure)

---

### Mental Model: Cloud = Renting vs Buying

**Traditional IT:** Buying a car
- Huge upfront cost ($30,000)
- You maintain it (oil changes, repairs)
- Sits in garage 95% of time (wasteful)
- Hard to upgrade (stuck with it)

**Cloud Computing:** Uber/Taxi
- No upfront cost ($0)
- Pay per ride ($10-50)
- Someone else maintains the car
- Use different cars for different needs
- Only pay when you actually need transport

**Cloud = Uber for computers** 🚗→☁️

---

## 🏗️ AWS Core Services (The Big 6)

### 1. EC2 (Elastic Compute Cloud) - Virtual Servers

**What:** Rent virtual machines in the cloud

**Real-world use:**
- Run your web application
- Run your API servers
- Run batch processing jobs
- Replace physical servers

**Cost:** $0.01-$0.50 per hour (depending on size)

**Interview Answer:**
> "EC2 provides resizable compute capacity. I use it to run application servers, can scale from 1 to 100 instances automatically based on load."

---

### 2. S3 (Simple Storage Service) - Object Storage

**What:** Unlimited storage for files

**Real-world use:**
- Store user uploads (images, videos)
- Host static websites (HTML, CSS, JS)
- Store backups
- Data lakes for analytics

**Cost:** $0.023 per GB per month (dirt cheap!)

**Interview Answer:**
> "S3 is object storage with 99.999999999% durability. I use it for storing application assets, backups, and hosting static websites with CloudFront."

---

### 3. RDS (Relational Database Service) - Managed Databases

**What:** Fully managed PostgreSQL, MySQL, etc.

**Real-world use:**
- Application database (without managing servers)
- Automatic backups
- Auto-scaling storage
- Multi-AZ for high availability

**Cost:** $0.017-$0.50 per hour

**Interview Answer:**
> "RDS manages database operations like backups, patching, and failover. I use it instead of self-hosting PostgreSQL because AWS handles maintenance and provides better uptime."

---

### 4. VPC (Virtual Private Cloud) - Network Isolation

**What:** Your own private network in AWS

**Real-world use:**
- Isolate resources from internet
- Control network traffic with security groups
- Create public and private subnets
- Connect to on-premise datacenters

**Cost:** Free (pay for traffic)

**Interview Answer:**
> "VPC lets me create isolated networks with subnets, route tables, and security groups. I design VPCs with public subnets for load balancers and private subnets for databases."

---

### 5. IAM (Identity & Access Management) - Security

**What:** Control who can access what in AWS

**Real-world use:**
- Create users with specific permissions
- Use roles for EC2 instances
- Enforce least privilege
- MFA for sensitive operations

**Cost:** Free

**Interview Answer:**
> "IAM manages authentication and authorization. I use IAM roles for EC2 instances instead of hardcoding credentials, and enforce MFA for production access."

---

### 6. CloudWatch - Monitoring & Logging

**What:** Monitor AWS resources and applications

**Real-world use:**
- Collect logs from applications
- Set alarms (CPU > 80% → Alert)
- Create dashboards
- Trigger auto-scaling

**Cost:** Free tier covers most use cases

**Interview Answer:**
> "CloudWatch aggregates logs and metrics from all AWS services. I use it to set alarms for application errors and infrastructure issues, and create dashboards for monitoring."

---

## 💻 HANDS-ON: Your First AWS Infrastructure

### Step 1: Create AWS Account

```
1. Go to aws.amazon.com
2. Click "Create an AWS Account"
3. Enter email and password
4. Add payment method (won't charge unless you exceed free tier)
5. Verify identity
6. Select Basic Plan (free)

⚠️ IMPORTANT: Enable MFA (multi-factor authentication) immediately!
```

**Free Tier Includes:**
- 750 hours/month of EC2 t2.micro (12 months)
- 5 GB of S3 storage (12 months)
- 750 hours/month of RDS db.t2.micro (12 months)
- 10 GB of CloudWatch logs (always free)

**Cost control:**
- Set up billing alerts ($10, $50, $100)
- Use Cost Explorer
- Enable AWS Budgets

---

### Step 2: Launch Your First EC2 Instance

**Using AWS Console:**

```
1. Navigate to EC2 Dashboard
2. Click "Launch Instance"

3. Name: my-first-server

4. Choose AMI (Operating System):
   - Select: Ubuntu Server 22.04 LTS (Free tier eligible)

5. Choose Instance Type:
   - Select: t2.micro (Free tier eligible - 1 vCPU, 1 GB RAM)

6. Key pair:
   - Create new key pair → Name: my-aws-key
   - Download my-aws-key.pem (SAVE THIS!)

7. Network settings:
   - Allow SSH traffic from: My IP
   - Allow HTTP traffic from internet ✅

8. Configure storage:
   - 8 GB GP3 (default is fine)

9. Launch Instance

Wait 30 seconds → Instance is running! 🎉
```

---

### Step 3: Connect to Your Server

```bash
# Make key file read-only (required)
chmod 400 my-aws-key.pem

# Get instance public IP from AWS console
# Example: 13.51.234.123

# SSH into your server
ssh -i my-aws-key.pem ubuntu@13.51.234.123

# You're now in your AWS server! 🚀

# Try some commands
whoami  # ubuntu
uname -a  # Linux info
df -h  # Disk space
free -h  # Memory

# Update packages
sudo apt update
sudo apt upgrade -y

# Install nginx
sudo apt install nginx -y

# Check if nginx is running
sudo systemctl status nginx

# Your server is now accessible at http://13.51.234.123
# Open in browser - you'll see "Welcome to nginx"
```

**Congratulations!** You've deployed a web server to AWS! 🎉

---

### Step 4: Host a Static Website on S3

```bash
# Install AWS CLI on your laptop
# macOS:
brew install awscli

# Linux:
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Windows:
# Download and run AWS CLI installer from aws.amazon.com

# Configure AWS CLI
aws configure
# AWS Access Key ID: [from IAM console]
# AWS Secret Access Key: [from IAM console]
# Default region name: eu-north-1
# Default output format: json
```

**Create S3 bucket and upload website:**

```bash
# Create a simple website
mkdir my-website
cd my-website

cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>My AWS Website</title>
</head>
<body>
    <h1>🚀 Hello from AWS S3!</h1>
    <p>This website is hosted on Amazon S3.</p>
</body>
</html>
EOF

# Create S3 bucket (must be globally unique name)
aws s3 mb s3://my-devops-website-12345

# Upload website
aws s3 sync . s3://my-devops-website-12345 --acl public-read

# Configure bucket for static website hosting
aws s3 website s3://my-devops-website-12345 \
  --index-document index.html

# Your website is live at:
# http://my-devops-website-12345.s3-website.eu-north-1.amazonaws.com
```

**Result:** You've hosted a website on AWS for ~$0.50/month! 🎉

---

## 🧠 Core AWS Concepts (Must Know for Interviews)

### 1. Regions and Availability Zones

**Region:** Geographic area (e.g., eu-north-1 = Stockholm)
- AWS has 32 regions worldwide
- Each region is isolated (outage in US doesn't affect Europe)
- Lower latency if close to users

**Availability Zone (AZ):** Datacenter within a region
- Each region has 2-6 AZs
- AZs are isolated (separate power, networking)
- Spread resources across AZs for high availability

**Interview Answer:**
> "I deploy applications across multiple AZs for high availability. If one AZ fails, the other continues serving traffic. For example, I'd put load balancer in 2 AZs, app servers in 2 AZs, and use Multi-AZ RDS."

---

### 2. Shared Responsibility Model

**AWS Responsible For:**
- ✅ Hardware (servers, networking, datacenters)
- ✅ Hypervisor (virtualization layer)
- ✅ Physical security
- ✅ Global infrastructure

**You Responsible For:**
- ✅ Operating system patches
- ✅ Application code
- ✅ Data encryption
- ✅ IAM (access control)
- ✅ Network configuration (security groups)

**Interview Answer:**
> "AWS handles 'security OF the cloud' (hardware, datacenters). I handle 'security IN the cloud' (patching, IAM, encryption, firewall rules)."

---

### 3. Pay-As-You-Go Pricing

**Billing Models:**

1. **On-Demand:** Pay by hour/second
   - Most flexible
   - Most expensive
   - Use for: Unpredictable workloads

2. **Reserved Instances:** 1 or 3-year commitment
   - 30-60% cheaper
   - Use for: Steady-state workloads (production databases)

3. **Spot Instances:** Bid on unused capacity
   - Up to 90% cheaper
   - Can be terminated anytime
   - Use for: Batch jobs, CI/CD workers

4. **Savings Plans:** Flexible commitment
   - 20-40% cheaper
   - Use for: Growing applications

**Interview Answer:**
> "I use Reserved Instances for baseline capacity (databases, always-on services), Spot Instances for CI/CD and batch processing, and On-Demand for variable load. This typically saves 40-60% compared to all On-Demand."

---

## 💼 Interview Preparation

### Question 1: Architecture Design

**Interviewer:** "Design a highly available web application architecture on AWS."

❌ **Weak Answer:**
> "Put an EC2 instance with a database..."

✅ **Strong Answer:**
> "I'd design a multi-tier, multi-AZ architecture:
>
> **Frontend Layer:**
> - CloudFront (CDN) for static assets
> - S3 for static website hosting
> - Route 53 for DNS
>
> **Application Layer:**
> - Application Load Balancer (in 2 AZs)
> - Auto Scaling Group (min 2, max 10 instances across 2 AZs)
> - EC2 instances running application
>
> **Data Layer:**
> - RDS PostgreSQL (Multi-AZ for automatic failover)
> - ElastiCache Redis (2 nodes in 2 AZs)
> - S3 for user uploads
>
> **Monitoring:**
> - CloudWatch for logs and metrics
> - SNS for alerting
> - CloudWatch alarms for CPU, memory, error rates
>
> This design provides high availability (survives AZ failure), auto-scaling (handles traffic spikes), and cost efficiency (scales down during low traffic).
>
> I'd deploy with Terraform for infrastructure as code."

**Why this impresses:** Demonstrates architecture thinking, not just tool knowledge.

---

### Question 2: Cost Optimization

**Interviewer:** "Your AWS bill is $10,000/month. How would you reduce it?"

❌ **Weak Answer:**
> "I'd use smaller instances?"

✅ **Strong Answer:**
> "I'd do a systematic cost analysis:
>
> **1. Identify top costs:**
> - Use Cost Explorer to see spend by service
> - Usually EC2, RDS, data transfer are biggest
>
> **2. Right-size instances:**
> - Check CloudWatch metrics for CPU/memory utilization
> - If <30% utilized → Downsize instance type
> - Potential savings: 30-50%
>
> **3. Use Reserved Instances:**
> - For steady workloads (databases, always-on services)
> - 1-year commitment saves 30-40%
>
> **4. Use Spot Instances:**
> - For CI/CD, batch jobs, non-critical workloads
> - Saves up to 90%
>
> **5. Optimize storage:**
> - Move infrequent data to S3 Glacier
> - Enable S3 Intelligent-Tiering
> - Delete unused EBS volumes and snapshots
>
> **6. Review data transfer:**
> - Use CloudFront to reduce data transfer costs
> - Keep traffic within same region when possible
>
> **7. Auto-scaling:**
> - Scale down during nights/weekends
> - Use scheduled scaling for predictable patterns
>
> Typically can reduce costs by 40-60% with these optimizations."

**Why this impresses:** Shows cost awareness and systematic approach.

---

## 🎯 Portfolio Project

**Build this for interviews:**

**3-Tier Web Application on AWS**

```
Architecture:
- Route 53 DNS
- CloudFront CDN
- S3 for static assets
- Application Load Balancer (2 AZs)
- Auto Scaling Group (EC2 instances)
- RDS PostgreSQL (Multi-AZ)
- ElastiCache Redis
- VPC with public/private subnets
- CloudWatch monitoring and alarms

Deployment:
- Infrastructure as Code (Terraform)
- CI/CD pipeline (GitHub Actions)
- Blue-green deployment
- Automatic rollbacks

Documentation:
- Architecture diagram
- Cost breakdown ($50-200/month)
- Disaster recovery plan
- Monitoring strategy
```

**Why this impresses:**
- ✅ Production-ready architecture
- ✅ High availability (Multi-AZ)
- ✅ Auto-scaling (handles traffic spikes)
- ✅ Security (VPC, private subnets)
- ✅ Monitoring (CloudWatch)
- ✅ IaC (Terraform)

---

## ⚠️ Common Mistakes

### ❌ Mistake 1: Leaving Resources Running

```
You spin up 10 EC2 instances for testing.
You forget to terminate them.
They run for 30 days.
Bill: $1,000+ 😱
```

**Fix:**
- Always terminate test instances
- Use tags: `Environment: test`, `AutoShutdown: true`
- Set up AWS Instance Scheduler (auto-shuts down dev/test)
- Enable billing alerts

---

### ❌ Mistake 2: Hardcoded Credentials

```python
# DON'T DO THIS!
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
```

**Fix:**
```python
# Use IAM roles (best)
# EC2 instance with IAM role automatically has credentials

# Or use AWS CLI with configured credentials
import boto3
s3 = boto3.client('s3')  # Uses ~/.aws/credentials
```

---

### ❌ Mistake 3: Open Security Groups

```
Security Group Rule:
Type: SSH
Source: 0.0.0.0/0  # ANYONE IN THE WORLD CAN SSH! 🚨
```

**Fix:**
```
Security Group Rule:
Type: SSH
Source: My IP (123.45.67.89/32)  # Only you

Or use AWS Systems Manager Session Manager (no SSH port open!)
```

---

## 📚 Flashcards

**Q: What is AWS EC2?**
A: Elastic Compute Cloud - virtual servers in the cloud. Pay by hour, scale up/down instantly.

**Q: What is AWS S3?**
A: Simple Storage Service - object storage with 99.999999999% durability. Unlimited storage, pay per GB.

**Q: What is a Region?**
A: Geographic area with multiple Availability Zones (datacenters). Example: eu-north-1 (Stockholm).

**Q: What is an Availability Zone?**
A: Isolated datacenter within a region. Each AZ has separate power/networking.

**Q: What is IAM?**
A: Identity and Access Management - controls who can access what in AWS.

**Q: What is VPC?**
A: Virtual Private Cloud - your own isolated network in AWS with subnets, route tables, security groups.

**Q: What is RDS?**
A: Relational Database Service - managed PostgreSQL, MySQL, etc. AWS handles backups and maintenance.

**Q: What's the difference between On-Demand and Reserved Instances?**
A: On-Demand = pay by hour, flexible. Reserved = 1-3 year commitment, 30-60% cheaper.

---

## 🎓 Quiz

### Question 1: Scenario

You need to store 10 TB of files that are accessed once per month. What's the most cost-effective solution?

A) EC2 instance with 10 TB EBS volume
B) S3 Standard
C) S3 Glacier ✅
D) EBS snapshots

**Explanation:** S3 Glacier is designed for archival storage (infrequent access) and costs $0.004/GB vs $0.023/GB for S3 Standard. For 10 TB, saves $190/month.

---

### Question 2: High Availability

Your application must survive an Availability Zone failure. What should you do?

A) Deploy in one AZ with backups
B) Deploy across multiple regions
C) Deploy across multiple AZs in same region ✅
D) Use Spot Instances

**Explanation:** Multiple AZs provide HA within a region. Multiple regions is overkill for AZ failure and more expensive.

---

### Question 3: Security

How should an EC2 instance access S3 securely?

A) Hardcode AWS credentials in code
B) Store credentials in environment variables
C) Use IAM role attached to EC2 instance ✅
D) Use root account credentials

**Explanation:** IAM roles provide temporary credentials automatically rotated by AWS. No hardcoded secrets needed.

---

## 📈 Next Steps

After mastering AWS basics:

1. **Module 2:** EC2 Deep Dive (instance types, Auto Scaling, Load Balancers)
2. **Module 3:** S3 Advanced (versioning, lifecycle policies, CloudFront)
3. **Module 4:** VPC Networking (subnets, route tables, NAT gateways)
4. **Module 5:** IAM Security Best Practices
5. **Module 6:** RDS and Database Management
6. **Module 7:** CloudWatch Monitoring
7. **Module 8:** Cost Optimization Strategies

---

## 🌟 Why This Module Prepares You for Jobs

✅ **Hands-on experience** - You've launched real AWS resources
✅ **Interview-ready** - You know common questions & strong answers
✅ **Architecture knowledge** - You understand multi-tier design
✅ **Cost awareness** - You know how to optimize AWS bills
✅ **Security basics** - You know IAM, security groups, VPCs
✅ **Portfolio project** - You have a production-ready architecture

**Time to complete:** 1.5-2 hours
**Job market impact:** Opens 85% of DevOps roles requiring cloud
**Salary boost:** +20-30% on average

---

**Module completed!** 🎉

**Next:** Module 2 - EC2 Deep Dive (Auto Scaling, Load Balancing)

**Free Tier Warning:** Don't forget to terminate EC2 instances when done practicing!
"""
}

# Export modules
AWS_MODULES = [
    CLOUD_CONCEPTS_AWS,
    # More modules...
]

# MODULE export för kompatibilitet med systemet
MODULE = {
    "name": "AWS Cloud Fundamentals",
    "slug": "aws-cloud-fundamentals",
    "description": "Learn AWS cloud computing - required in 85% of DevOps jobs. Master EC2, S3, RDS, VPC, IAM, and CloudWatch with hands-on exercises.",
    "icon": "☁️",
    "order_index": 12,
    "category": "devops",
    "difficulty": "beginner",
    "estimated_hours": 6,
    "tasks": AWS_MODULES
}
