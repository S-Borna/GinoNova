"""
Ansible Automation - Agentless Configuration Management
========================================================

Master Ansible - the #1 automation tool for servers and cloud infrastructure.
Agentless, simple YAML, powers Red Hat, NASA, and thousands of companies.

Career Impact: 72% of DevOps jobs require Ansible. +15-20% salary boost.
"""

ANSIBLE_FUNDAMENTALS = {
    "title": "Ansible Automation Fundamentals",
    "slug": "ansible-fundamentals",
    "description": "Master Ansible playbooks, roles, and automation. Learn the #1 configuration management tool - agentless, YAML-based, and battle-tested.",
    "difficulty": "intermediate",
    "estimated_minutes": 120,
    "xp_reward": 200,
    "order_index": 1,
    "content": r"""# Ansible Automation Fundamentals

## 🎯 TL;DR (30 seconds)

Ansible automates server configuration, application deployment, and cloud provisioning using simple YAML files. **Agentless** (no software to install on servers) and **idempotent** (safe to run multiple times).

**Why this matters:** 72% of DevOps jobs require Ansible. It's the easiest automation tool to learn. **Ansible skills add +18% to your salary.**

---

## 🚀 Why Ansible Matters for Your Career

### The Automation Reality

**Manual server management doesn't scale:**
- 1 server → SSH and configure manually (30 min)
- 10 servers → 5 hours of repetitive work
- 100 servers → IMPOSSIBLE without automation
- 1000 servers → Ansible deploys in 10 minutes

**Market Dominance:**
- 72% of DevOps job postings mention Ansible
- Red Hat (IBM) pays $150 million for Ansible (2015)
- Used by: NASA, BMW, Apple, Cisco, Walmart, JPMorgan

**Ansible vs Competitors:**
- **Ansible**: 72% adoption (easiest to learn)
- **Chef**: 15% adoption (complex Ruby DSL)
- **Puppet**: 18% adoption (complex Puppet language)
- **SaltStack**: 8% adoption (Python-based)

**Why Ansible Won:**
1. **Agentless** - No agents to install (SSH/WinRM only)
2. **YAML** - Easy to read and write
3. **Idempotent** - Safe to run multiple times
4. **Large ecosystem** - 3000+ modules for everything

### Salary Impact (Sweden 2026)

| Role | Without Ansible | With Ansible | Difference |
|------|-----------------|--------------|------------|
| Junior DevOps | 42,000 SEK | 50,000 SEK | **+19%** |
| DevOps Engineer | 55,000 SEK | 65,000 SEK | **+18%** |
| Senior DevOps | 70,000 SEK | 82,000 SEK | **+17%** |

**Learning Ansible = +10,000 SEK/month = +120,000 SEK/year** 💰

---

## 📖 THEORY: How Ansible Works

### The Mental Model

```
┌─────────────────────────────────────────────────────┐
│              Your Laptop (Control Node)             │
│                                                     │
│  1. Write playbook.yml (what you want)            │
│  2. Run: ansible-playbook playbook.yml            │
│  3. Ansible connects via SSH                       │
└─────────────────────────────────────────────────────┘
              │ SSH │ SSH │ SSH
              ↓     ↓     ↓
    ┌────────┐ ┌────────┐ ┌────────┐
    │Server 1│ │Server 2│ │Server 3│
    │        │ │        │ │        │
    │ Nginx  │ │ Nginx  │ │ Nginx  │
    │installed│ │installed│ │installed│
    └────────┘ └────────┘ └────────┘
```

**Key Concepts:**

1. **Control Node** - Your laptop (where you run Ansible)
2. **Managed Nodes** - Servers you configure (no agent needed!)
3. **Inventory** - List of servers to manage
4. **Playbook** - YAML file describing desired state
5. **Modules** - Reusable units (apt, yum, copy, user, etc.)
6. **Roles** - Organized collection of playbooks/tasks
7. **Idempotent** - Running twice = same result (safe!)

---

### Ansible vs Shell Scripts

**❌ Shell Script (Imperative):**
```bash
#!/bin/bash
# Install nginx
apt-get update
apt-get install -y nginx

# Start nginx
systemctl start nginx
systemctl enable nginx

# What if nginx is already installed? Script fails!
# What if it's a RedHat system? (uses yum, not apt)
# What if systemd doesn't exist? (uses init)
```

**✅ Ansible (Declarative):**
```yaml
- name: Install and start nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes

    - name: Ensure nginx is running
      service:
        name: nginx
        state: started
        enabled: yes

# ✅ Idempotent - safe to run multiple times
# ✅ Cross-platform - works on Ubuntu, Debian, RedHat (different module)
# ✅ Readable - anyone can understand YAML
# ✅ Error handling - built-in
```

---

## 💻 HANDS-ON: Your First Ansible Playbook

### Step 1: Install Ansible

```bash
# macOS
brew install ansible

# Ubuntu/Debian
sudo apt update
sudo apt install -y ansible

# RedHat/CentOS
sudo yum install -y ansible

# Via pip (any OS)
pip3 install ansible

# Verify installation
ansible --version

# Output:
# ansible [core 2.16.2]
#   python version = 3.11.6
```

---

### Step 2: Create Inventory File

**Inventory = List of servers to manage**

```bash
mkdir ansible-demo && cd ansible-demo

# Create inventory file
cat > inventory.ini << 'EOF'
[webservers]
web1 ansible_host=192.168.1.10 ansible_user=ubuntu
web2 ansible_host=192.168.1.11 ansible_user=ubuntu

[databases]
db1 ansible_host=192.168.1.20 ansible_user=ubuntu

[production:children]
webservers
databases

[production:vars]
ansible_ssh_private_key_file=~/.ssh/id_rsa
ansible_python_interpreter=/usr/bin/python3
EOF
```

**Testing with localhost (no servers needed):**

```bash
# Create local inventory
cat > inventory-local.ini << 'EOF'
[local]
localhost ansible_connection=local
EOF
```

---

### Step 3: Test Connection

```bash
# Ping all hosts (uses SSH)
ansible all -i inventory-local.ini -m ping

# Output:
# localhost | SUCCESS => {
#     "changed": false,
#     "ping": "pong"
# }

# Run ad-hoc command
ansible all -i inventory-local.ini -m shell -a "uptime"

# Output:
# localhost | SUCCESS | rc=0 >>
#  10:23:45 up 5 days, 2:15, 3 users, load average: 0.52, 0.58, 0.59
```

🎉 **Ansible is working!**

---

### Step 4: Your First Playbook

```bash
# Create playbook
cat > webserver.yml << 'EOF'
---
- name: Configure web servers
  hosts: local
  become: yes  # Run as sudo
  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
        cache_valid_time: 3600
      when: ansible_os_family == "Debian"

    - name: Install nginx
      apt:
        name: nginx
        state: present
      when: ansible_os_family == "Debian"

    - name: Install nginx (RedHat)
      yum:
        name: nginx
        state: present
      when: ansible_os_family == "RedHat"

    - name: Start and enable nginx
      service:
        name: nginx
        state: started
        enabled: yes

    - name: Create custom index.html
      copy:
        content: |
          <html>
          <body>
            <h1>Deployed with Ansible!</h1>
            <p>Server: {{ ansible_hostname }}</p>
            <p>IP: {{ ansible_default_ipv4.address }}</p>
          </body>
          </html>
        dest: /var/www/html/index.html
        owner: www-data
        group: www-data
        mode: '0644'

    - name: Ensure nginx is running
      service:
        name: nginx
        state: started

    - name: Open firewall for HTTP
      ufw:
        rule: allow
        port: '80'
        proto: tcp
      when: ansible_os_family == "Debian"
EOF

# Run playbook
ansible-playbook -i inventory-local.ini webserver.yml

# Output shows each task:
# PLAY [Configure web servers] ************
# TASK [Gathering Facts] ******************
# ok: [localhost]
# TASK [Update apt cache] *****************
# changed: [localhost]
# TASK [Install nginx] ********************
# changed: [localhost]
# ...
# PLAY RECAP *****************************
# localhost: ok=6 changed=4 unreachable=0 failed=0
```

---

### Step 5: Check Idempotency

```bash
# Run again (should show "changed=0")
ansible-playbook -i inventory-local.ini webserver.yml

# Output:
# PLAY RECAP *****************************
# localhost: ok=6 changed=0 unreachable=0 failed=0
# ✅ "changed=0" means idempotent!

# Test nginx
curl http://localhost

# Output: <h1>Deployed with Ansible!</h1> ...
```

---

## 🏗️ Ansible Roles (Best Practice)

**Roles = Organized, reusable playbooks**

### Create Role Structure

```bash
# Create role
ansible-galaxy init roles/nginx

# Structure created:
# roles/nginx/
# ├── tasks/         # Main tasks
# ├── handlers/      # Event handlers (restart services)
# ├── templates/     # Jinja2 templates
# ├── files/         # Static files
# ├── vars/          # Variables
# ├── defaults/      # Default variables
# └── meta/          # Role dependencies
```

---

### Example: Nginx Role

```bash
# roles/nginx/tasks/main.yml
cat > roles/nginx/tasks/main.yml << 'EOF'
---
- name: Install nginx
  apt:
    name: nginx
    state: present
    update_cache: yes

- name: Copy nginx config
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
  notify: Restart nginx

- name: Ensure nginx is running
  service:
    name: nginx
    state: started
    enabled: yes
EOF

# roles/nginx/handlers/main.yml
cat > roles/nginx/handlers/main.yml << 'EOF'
---
- name: Restart nginx
  service:
    name: nginx
    state: restarted
EOF

# roles/nginx/templates/nginx.conf.j2
cat > roles/nginx/templates/nginx.conf.j2 << 'EOF'
user www-data;
worker_processes {{ ansible_processor_vcpus }};
pid /run/nginx.pid;

events {
    worker_connections 1024;
}

http {
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    server {
        listen 80;
        server_name {{ ansible_hostname }};

        location / {
            root /var/www/html;
            index index.html;
        }
    }
}
EOF

# Use role in playbook
cat > site.yml << 'EOF'
---
- name: Configure web servers
  hosts: local
  become: yes
  roles:
    - nginx
EOF

# Run
ansible-playbook -i inventory-local.ini site.yml
```

---

## 🧠 Essential Ansible Modules

### File Operations

```yaml
# Copy file
- name: Copy config file
  copy:
    src: files/app.conf
    dest: /etc/app/app.conf
    owner: root
    mode: '0644'

# Template (Jinja2 with variables)
- name: Create config from template
  template:
    src: templates/config.j2
    dest: /etc/app/config.ini

# Download file
- name: Download binary
  get_url:
    url: https://example.com/app.tar.gz
    dest: /tmp/app.tar.gz
    checksum: sha256:abc123...

# Create directory
- name: Create app directory
  file:
    path: /opt/myapp
    state: directory
    owner: app
    group: app
    mode: '0755'
```

---

### Package Management

```yaml
# APT (Debian/Ubuntu)
- name: Install packages
  apt:
    name:
      - nginx
      - postgresql
      - redis-server
    state: present
    update_cache: yes

# YUM (RedHat/CentOS)
- name: Install packages (RedHat)
  yum:
    name:
      - nginx
      - postgresql
      - redis
    state: present

# Cross-platform
- name: Install package (any OS)
  package:
    name: nginx
    state: present
```

---

### Service Management

```yaml
# Start/stop/restart
- name: Ensure nginx is running
  service:
    name: nginx
    state: started
    enabled: yes

# Restart
- name: Restart nginx
  service:
    name: nginx
    state: restarted

# Reload config
- name: Reload nginx config
  service:
    name: nginx
    state: reloaded
```

---

### User Management

```yaml
# Create user
- name: Create app user
  user:
    name: appuser
    shell: /bin/bash
    groups: docker,sudo
    append: yes
    create_home: yes

# Add SSH key
- name: Add SSH key
  authorized_key:
    user: appuser
    key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
```

---

### Git Operations

```yaml
# Clone repository
- name: Clone application repo
  git:
    repo: https://github.com/company/app.git
    dest: /opt/app
    version: main
    force: yes
```

---

### Docker Operations

```yaml
# Install Docker
- name: Install Docker
  apt:
    name: docker.io
    state: present

# Run container
- name: Run nginx container
  docker_container:
    name: nginx
    image: nginx:latest
    state: started
    ports:
      - "80:80"
    volumes:
      - /data/nginx:/usr/share/nginx/html
```

---

## 💼 Interview Preparation

### Question 1: Idempotency

**Interviewer:** "What does idempotent mean in Ansible?"

✅ **Strong Answer:**
> "Idempotent means running a playbook multiple times produces the same result as running it once. Ansible achieves this by checking current state before making changes. For example, the 'apt' module checks if a package is installed before attempting installation. This makes Ansible safe to run repeatedly without side effects - critical for automation. Non-idempotent operations (like 'shell' module) should be avoided or made idempotent with 'creates' or 'unless' parameters."

**Why this impresses:** Shows deep understanding of core concept.

---

### Question 2: Handlers

**Interviewer:** "What are handlers in Ansible and when do you use them?"

✅ **Strong Answer:**
> "Handlers are tasks that run only when notified by another task that changed state. Common use case: restart a service after changing its config file. Handlers run at the end of a playbook (not immediately) and only once even if notified multiple times. Example: if you update nginx config, mysql config, and systemd service file, each task notifies 'restart services' handler, but services restart only once at the end. This prevents unnecessary restarts and reduces downtime."

**Why this impresses:** Explains the "why" and "when."

---

### Question 3: Playbook vs Role

**Interviewer:** "When would you use a role instead of a playbook?"

✅ **Strong Answer:**
> "Roles are for reusable, organized code. Use roles when: 1) You need to reuse logic across multiple playbooks (DRY principle). 2) You want to share with others (Ansible Galaxy). 3) Complex setup with many tasks (roles organize tasks, handlers, templates, vars). Use simple playbooks for: 1) Quick one-off tasks. 2) Orchestration that combines multiple roles. 3) Project-specific logic. In production, I always use roles for anything I'll deploy more than once - web servers, databases, monitoring agents."

**Why this impresses:** Practical experience.

---

### Question 4: Ansible vs Terraform

**Interviewer:** "When do you use Ansible vs Terraform?"

✅ **Strong Answer:**
> "Terraform is for infrastructure provisioning (creating VMs, networks, cloud resources) using declarative state. Ansible is for configuration management (installing software, configuring services) using procedural tasks. In practice: 1) Terraform creates infrastructure. 2) Terraform outputs IPs to Ansible inventory. 3) Ansible configures servers. They complement each other. Terraform could do configuration (with provisioners) but Ansible is better at it. Ansible could provision infrastructure (with cloud modules) but Terraform is better at it. Use both together."

**Why this impresses:** Knows tool boundaries.

---

## 🎯 Real-World Ansible Patterns

### Pattern 1: Dynamic Inventory (EC2)

```bash
# Install AWS dynamic inventory
wget https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py
chmod +x ec2.py

# Configure AWS credentials
export AWS_ACCESS_KEY_ID=xxx
export AWS_SECRET_ACCESS_KEY=xxx

# Use dynamic inventory (auto-discovers EC2 instances)
ansible-playbook -i ec2.py site.yml

# Group by tags automatically!
# [tag_Environment_production]
# [tag_Role_webserver]
```

---

### Pattern 2: Secrets with Ansible Vault

```bash
# Create encrypted file
ansible-vault create secrets.yml

# Enter password, then:
db_password: super_secret_password
api_key: abc123xyz

# Use in playbook
- name: Deploy app
  hosts: webservers
  vars_files:
    - secrets.yml
  tasks:
    - name: Configure app
      template:
        src: config.j2
        dest: /etc/app/config.ini

# config.j2:
# [database]
# password={{ db_password }}

# Run with vault password
ansible-playbook site.yml --ask-vault-pass
```

---

### Pattern 3: Rolling Updates (Zero Downtime)

```yaml
- name: Rolling update web servers
  hosts: webservers
  serial: 2  # Update 2 servers at a time

  tasks:
    - name: Remove from load balancer
      haproxy:
        state: disabled
        backend: webapp
        host: "{{ inventory_hostname }}"
      delegate_to: "{{ item }}"
      loop: "{{ groups['loadbalancers'] }}"

    - name: Update application
      git:
        repo: https://github.com/company/app.git
        dest: /opt/app
        version: "{{ app_version }}"

    - name: Restart app
      service:
        name: webapp
        state: restarted

    - name: Wait for app to start
      wait_for:
        port: 8080
        delay: 5
        timeout: 60

    - name: Add back to load balancer
      haproxy:
        state: enabled
        backend: webapp
        host: "{{ inventory_hostname }}"
      delegate_to: "{{ item }}"
      loop: "{{ groups['loadbalancers'] }}"
```

---

## 📚 Flashcards

**Q: What is Ansible?**
A: Agentless configuration management tool using YAML playbooks and SSH.

**Q: What's an inventory?**
A: List of servers to manage (can be static file or dynamic script).

**Q: What's a playbook?**
A: YAML file that describes desired state of servers.

**Q: What's a role?**
A: Organized collection of tasks, handlers, templates for reusability.

**Q: What does idempotent mean?**
A: Running multiple times = same result. Safe to repeat.

**Q: What's a handler?**
A: Task that runs only when notified by changed task (usually restarts services).

**Q: What's ansible-vault?**
A: Encrypts sensitive data in playbooks (passwords, keys).

**Q: How does Ansible connect to servers?**
A: SSH (Linux) or WinRM (Windows). No agent needed.

**Q: What's the difference between Ansible and Terraform?**
A: Terraform = provision infrastructure. Ansible = configure servers.

**Q: What's Ansible Galaxy?**
A: Repository of community roles (like npm for Ansible).

---

## 🎓 Quiz

### Question 1: Idempotency

**Which task is NOT idempotent?**

A) `apt: name=nginx state=present`
B) `service: name=nginx state=started`
C) `shell: echo "test" >> /tmp/file.txt` ✅
D) `copy: src=file.txt dest=/tmp/file.txt`

**Explanation:** The shell command appends to file every time. Others check state first.

---

### Question 2: Handlers

**When do handlers run?**

A) Immediately when notified
B) At the end of the playbook ✅
C) Before tasks
D) In parallel with tasks

**Explanation:** Handlers run at the end, once, even if notified multiple times.

---

## 🏆 Portfolio Project: Full Stack Deployment

**Build this for your GitHub:**

```
ansible-webapp-deployment/
├── inventory/
│   ├── production
│   └── staging
├── roles/
│   ├── common/        # Base setup (users, SSH)
│   ├── nginx/         # Web server
│   ├── postgresql/    # Database
│   ├── redis/         # Cache
│   └── webapp/        # Application
├── playbooks/
│   ├── site.yml       # Main playbook
│   ├── deploy.yml     # Deploy updates
│   └── rollback.yml   # Rollback
├── group_vars/
│   ├── all.yml
│   ├── production.yml
│   └── staging.yml
└── README.md
```

**Why this impresses:**
- ✅ Production-ready structure
- ✅ Multiple environments
- ✅ Organized roles
- ✅ Deployment automation
- ✅ Rollback capability

---

## 🌟 Module Summary

✅ **Hands-on playbooks** - Deployed nginx, apps
✅ **Roles mastery** - Organized reusable code
✅ **Best practices** - Idempotency, handlers, vault
✅ **Real-world patterns** - Rolling updates, dynamic inventory
✅ **Interview ready** - Can explain concepts clearly
✅ **Portfolio project** - Full deployment automation

**Job market impact:** Opens 72% of DevOps roles
**Salary boost:** +15-20%
**Time to complete:** 2 hours

---

**Module completed!** 🎉

**Next recommended:** Terraform for Infrastructure as Code - perfect complement to Ansible!
"""
}

MODULE = {
    "id": "config-ansible-automation",
    "slug": "config-ansible-automation",
    "title": "Ansible Automation",
    "description": "Master Ansible - #1 automation tool. Agentless, YAML-based configuration management. 72% of DevOps jobs require it. +18% salary boost.",
    "icon": "🤖",
    "category": "configuration-management",
    "difficulty": "intermediate",
    "estimated_hours": 8,
    "tasks": [ANSIBLE_FUNDAMENTALS],
}
