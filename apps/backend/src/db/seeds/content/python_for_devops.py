"""
Python for DevOps - Automation & Scripting
==========================================

Master Python for DevOps tasks - automate AWS, parse logs, build CLIs,
interact with APIs. Python is the #1 DevOps scripting language (used by 92% of teams).
"""

PYTHON_FUNDAMENTALS_DEVOPS = {
    "title": "Python for DevOps - Automation Essentials",
    "slug": "python-devops-essentials",
    "description": "Learn Python specifically for DevOps: AWS automation with boto3, log parsing, API interactions, CLI tools, and infrastructure automation.",
    "difficulty": "intermediate",
    "estimated_minutes": 90,
    "xp_reward": 150,
    "order_index": 1,
    "content": r"""# Python for DevOps - Automation Essentials

## 🎯 TL;DR (30 seconds)

Python is THE scripting language for DevOps. Automate AWS with boto3, parse logs with regex,
interact with APIs, build CLI tools. 92% of DevOps teams use Python daily.

**Why this matters:** Bash gets you 70% of the way. Python handles the complex 30% that makes you irreplaceable.

---

## 🚀 Why Python for DevOps?

### Job Market Reality

**Language Usage in DevOps (2026):**
- Python: 92% of teams
- Bash: 88% of teams
- Go: 35% of teams
- Ruby: 12% of teams

**Why Python dominates:**
✅ boto3 for AWS automation (official SDK)
✅ Rich ecosystem (requests, paramiko, fabric)
✅ Easy to read and maintain
✅ Great for both scripts and complex tools
✅ Huge community (StackOverflow solutions for everything)

---

## 📖 THEORY: Python vs Bash for DevOps

### When to Use Bash
✅ Simple file operations
✅ Chaining CLI tools together
✅ System administration tasks
✅ Quick one-liners

### When to Use Python
✅ AWS/Azure/GCP automation
✅ Complex log parsing
✅ API interactions (REST, GraphQL)
✅ Data transformation (JSON, YAML, CSV)
✅ Error handling and retry logic
✅ Building CLI tools (Click, Typer)

**Rule of thumb:** If your Bash script is >50 lines, rewrite it in Python.

---

## 🛠️ HANDS-ON: AWS Automation with boto3

### Setup

**Install boto3:**
```bash
pip install boto3
```

**AWS credentials (if not configured):**
```bash
aws configure
# Or export in script:
# export AWS_ACCESS_KEY_ID="xxx"
# export AWS_SECRET_ACCESS_KEY="xxx"
```

---

### Example 1: List All EC2 Instances

```python
#!/usr/bin/env python3
import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='eu-north-1')

# Get all instances
response = ec2.describe_instances()

print("EC2 Instances:")
print("-" * 80)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        instance_type = instance['InstanceType']

        # Get name tag
        name = "No Name"
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    name = tag['Value']

        print(f"ID: {instance_id}")
        print(f"  Name: {name}")
        print(f"  Type: {instance_type}")
        print(f"  State: {state}")
        print()
```

**Run:**
```bash
python3 list_ec2.py
```

**Output:**
```
EC2 Instances:
--------------------------------------------------------------------------------
ID: i-0123456789abcdef0
  Name: web-server-prod
  Type: t2.medium
  State: running

ID: i-0987654321fedcba0
  Name: db-server-prod
  Type: t2.large
  State: stopped
```

---

### Example 2: Automated Backup - Stop/Start Instances by Tag

```python
#!/usr/bin/env python3
'''
Stop all EC2 instances tagged 'Environment=development' to save costs
Run this at night, start them in the morning
'''
import boto3
import sys

def stop_dev_instances():
    ec2 = boto3.client('ec2', region_name='eu-north-1')

    # Find instances with Environment=development tag
    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Environment', 'Values': ['development']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    if not instance_ids:
        print("No running development instances found")
        return

    print(f"Stopping {len(instance_ids)} development instances...")
    ec2.stop_instances(InstanceIds=instance_ids)

    print("✅ Stopped instances:")
    for instance_id in instance_ids:
        print(f"  - {instance_id}")

def start_dev_instances():
    ec2 = boto3.client('ec2', region_name='eu-north-1')

    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Environment', 'Values': ['development']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    if not instance_ids:
        print("No stopped development instances found")
        return

    print(f"Starting {len(instance_ids)} development instances...")
    ec2.start_instances(InstanceIds=instance_ids)

    print("✅ Started instances:")
    for instance_id in instance_ids:
        print(f"  - {instance_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ['stop', 'start']:
        print("Usage: python3 manage_dev_instances.py [stop|start]")
        sys.exit(1)

    action = sys.argv[1]
    if action == 'stop':
        stop_dev_instances()
    else:
        start_dev_instances()
```

**Usage:**
```bash
# Stop all dev instances at night (save money!)
python3 manage_dev_instances.py stop

# Start them in the morning
python3 manage_dev_instances.py start
```

**Cost savings:** Stopping 5 t2.medium instances for 12 hours/day saves ~$50/month!

---

### Example 3: S3 Backup Script

```python
#!/usr/bin/env python3
'''
Backup local directory to S3 with timestamp
'''
import boto3
import os
from datetime import datetime

def backup_to_s3(local_dir, bucket_name):
    s3 = boto3.client('s3')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    print(f"Backing up {local_dir} to s3://{bucket_name}/backup_{timestamp}/")

    uploaded = 0
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_dir)
            s3_path = f"backup_{timestamp}/{relative_path}"

            try:
                s3.upload_file(local_path, bucket_name, s3_path)
                print(f"✅ Uploaded: {relative_path}")
                uploaded += 1
            except Exception as e:
                print(f"❌ Failed to upload {relative_path}: {e}")

    print(f"\n🎉 Backup complete! Uploaded {uploaded} files")

if __name__ == "__main__":
    backup_to_s3("/var/www/html", "my-backups-bucket")
```

---

## 🎓 Advanced: Building a CLI Tool with Click

**Install Click:**
```bash
pip install click
```

**Create `devops-cli.py`:**
```python
#!/usr/bin/env python3
import click
import boto3

@click.group()
def cli():
    '''DevOps CLI Tool - Manage AWS resources'''
    pass

@cli.command()
@click.option('--region', default='eu-north-1', help='AWS region')
def list_ec2(region):
    '''List all EC2 instances'''
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            click.echo(f"{instance['InstanceId']} - {instance['State']['Name']}")

@cli.command()
@click.argument('instance_id')
def stop_instance(instance_id):
    '''Stop an EC2 instance'''
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=[instance_id])
    click.echo(f"✅ Stopping {instance_id}")

@cli.command()
@click.option('--bucket', required=True, help='S3 bucket name')
def list_s3(bucket):
    '''List objects in S3 bucket'''
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket)

    if 'Contents' in response:
        for obj in response['Contents']:
            click.echo(f"{obj['Key']} - {obj['Size']} bytes")
    else:
        click.echo("Bucket is empty")

if __name__ == '__main__':
    cli()
```

**Make executable:**
```bash
chmod +x devops-cli.py
```

**Use it:**
```bash
./devops-cli.py list-ec2
./devops-cli.py stop-instance i-0123456789abcdef0
./devops-cli.py list-s3 --bucket my-bucket
```

---

## 📚 Essential Python Libraries for DevOps

### 1. **boto3** - AWS SDK
```python
import boto3
ec2 = boto3.client('ec2')
s3 = boto3.resource('s3')
```

### 2. **requests** - HTTP/API calls
```python
import requests
response = requests.get('https://api.github.com/repos/kubernetes/kubernetes')
data = response.json()
```

### 3. **paramiko** - SSH automation
```python
import paramiko
ssh = paramiko.SSHClient()
ssh.connect('server.com', username='admin', password='xxx')
stdin, stdout, stderr = ssh.exec_command('uptime')
```

### 4. **fabric** - Remote task automation
```python
from fabric import Connection
c = Connection('server.com')
result = c.run('uname -a')
```

### 5. **click/typer** - CLI tools
```python
import click

@click.command()
@click.option('--count', default=1)
def hello(count):
    for _ in range(count):
        click.echo('Hello!')
```

---

## 🎓 Quiz

### Question 1

**When should you use Python instead of Bash?**

A) Quick file operations
B) Complex AWS automation with error handling
C) Chaining grep, awk, sed
D) Simple system administration

**Answer:** B ✅

**Explanation:** Python excels at complex tasks with error handling. Bash is better for simple CLI chaining.

---

### Question 2

**What is boto3?**

A) Python web framework
B) AWS SDK for Python
C) Container orchestration tool
D) SSH library

**Answer:** B ✅

---

## 🌟 Why This Module is Powerful

✅ **AWS automation** - Control cloud infrastructure from scripts
✅ **Real-world examples** - Production-ready code you can use today
✅ **Cost savings** - Stop dev instances script saves $50+/month
✅ **Interview ready** - Can explain Python vs Bash tradeoffs
✅ **CLI tools** - Build professional DevOps utilities

**Time to complete:** 1.5 hours
**Practical value:** Immediate - use scripts today
**Job requirement:** 92% of DevOps teams

---

**Module completed!** 🎉

**Next:** Advanced Python for DevOps - async/await, multiprocessing, monitoring
"""
}

# Export as MODULE dict
MODULE = {
    "id": "python-for-devops",
    "slug": "python-for-devops",
    "title": "Python for DevOps",
    "description": "Master Python for DevOps automation: AWS boto3, log parsing, API interactions, CLI tools. Used by 92% of DevOps teams daily.",
    "icon": "🐍",
    "category": "tools",
    "difficulty": "rookie",
    "estimated_hours": 6,
    "tasks": [PYTHON_FUNDAMENTALS_DEVOPS],
}
