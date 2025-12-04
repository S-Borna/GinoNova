# =============================================================================
# BLOCK 4: MODULES & COLLECTIONS (Noder 13-16)
# =============================================================================

NODE_13_CORE_MODULES = {
    "node_id": 13,
    "title": "Core Modules Deep Dive",
    "slug": "core-modules",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "prerequisites": [5],
    "content": r'''
# Core Modules Deep Dive

## Varför detta är kritiskt

> "Ansible har 3000+ modules. Du behöver djup kunskap i ~50 som täcker 90% av use cases. Dessa är dina dagliga verktyg."

**Core module-kategorier:**
- **Files**: copy, template, file, lineinfile
- **Commands**: command, shell, script, raw
- **System**: systemd, cron, user, group
- **Packages**: apt, yum, dnf, pip
- **Network**: uri, get_url, firewalld

---

## Module Arkitektur

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       ANSIBLE MODULE EXECUTION                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  CONTROL NODE                          TARGET NODE                      │
│  ────────────                          ───────────                      │
│  ┌──────────────┐                      ┌──────────────────────────┐     │
│  │ Playbook     │                      │ 1. Module transferred    │     │
│  │   ↓          │      SSH/WinRM       │ 2. Arguments passed      │     │
│  │ Task         │  ─────────────────►  │ 3. Module executes       │     │
│  │   ↓          │                      │ 4. JSON result returned  │     │
│  │ Module       │  ◄─────────────────  │ 5. Cleanup               │     │
│  └──────────────┘                      └──────────────────────────┘     │
│                                                                         │
│  MODULE TYPES:                                                          │
│  ├── Python modules (most)  → Requires Python on target                 │
│  ├── Binary modules         → Platform-specific                         │
│  └── Raw/Script             → No Python needed                          │
│                                                                         │
│  RETURN VALUES:                                                         │
│  {                                                                      │
│    "changed": true/false,   ← Idempotency indicator                     │
│    "msg": "Human readable", ← Status message                            │
│    "rc": 0,                 ← Return code (commands)                    │
│    "stdout": "...",         ← Command output                            │
│    "failed": false          ← Success/failure                           │
│  }                                                                      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## File Modules

### file - Manage files and directories

```yaml
---
# File management tasks
- name: Create directory with specific permissions
  ansible.builtin.file:
    path: /opt/app/data
    state: directory
    owner: deploy
    group: deploy
    mode: '0755'
    recurse: true

- name: Create empty file (touch)
  ansible.builtin.file:
    path: /opt/app/logs/app.log
    state: touch
    owner: deploy
    mode: '0644'
    modification_time: preserve
    access_time: preserve

- name: Create symbolic link
  ansible.builtin.file:
    src: /opt/app/releases/v1.2.3
    dest: /opt/app/current
    state: link
    force: true

- name: Create hard link
  ansible.builtin.file:
    src: /etc/resolv.conf
    dest: /opt/app/resolv.conf
    state: hard

- name: Remove file
  ansible.builtin.file:
    path: /tmp/old_file.txt
    state: absent

- name: Set complex permissions
  ansible.builtin.file:
    path: /var/www
    state: directory
    owner: www-data
    group: www-data
    mode: u=rwX,g=rX,o=rX
    recurse: true
```

### copy - Copy files to remote

```yaml
- name: Copy file with owner and permissions
  ansible.builtin.copy:
    src: files/app.conf
    dest: /etc/app/app.conf
    owner: root
    group: root
    mode: '0644'
    backup: true
    validate: /usr/bin/nginx -t -c %s

- name: Copy content directly
  ansible.builtin.copy:
    content: |
      # Application config
      APP_NAME={{ app_name }}
      ENVIRONMENT={{ env }}
      DEBUG={{ debug_mode }}
    dest: /opt/app/.env
    mode: '0600'

- name: Copy directory recursively
  ansible.builtin.copy:
    src: configs/
    dest: /etc/app/
    directory_mode: '0755'
```

### lineinfile - Manage single lines

```yaml
- name: Ensure line present
  ansible.builtin.lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^PermitRootLogin'
    line: 'PermitRootLogin no'
    backup: true
    validate: '/usr/sbin/sshd -t -f %s'

- name: Add line after pattern
  ansible.builtin.lineinfile:
    path: /etc/hosts
    insertafter: '^127\.0\.0\.1'
    line: '192.168.1.100 app.local'

- name: Add line before pattern
  ansible.builtin.lineinfile:
    path: /etc/sudoers
    insertbefore: '^#includedir'
    line: 'deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart app'
    validate: '/usr/sbin/visudo -cf %s'

- name: Remove line
  ansible.builtin.lineinfile:
    path: /etc/hosts
    regexp: '^192\.168\.1\.100'
    state: absent

- name: Create if not exist, add to end
  ansible.builtin.lineinfile:
    path: /opt/app/config.txt
    line: 'LAST_UPDATED={{ ansible_date_time.iso8601 }}'
    create: true
```

### blockinfile - Manage text blocks

```yaml
- name: Add upstream block to nginx
  ansible.builtin.blockinfile:
    path: /etc/nginx/nginx.conf
    marker: "# {mark} ANSIBLE MANAGED - APP UPSTREAM"
    insertbefore: "^http {"
    block: |
      upstream app_backend {
          least_conn;
          server 127.0.0.1:8001 weight=3;
          server 127.0.0.1:8002 weight=2;
          server 127.0.0.1:8003 backup;
          keepalive 32;
      }
    backup: true
    validate: /usr/sbin/nginx -t -c %s

- name: Add SSH authorized key
  ansible.builtin.blockinfile:
    path: /home/deploy/.ssh/authorized_keys
    marker: "# {mark} KEY FOR {{ item.name }}"
    block: "{{ item.key }}"
    create: true
    mode: '0600'
    owner: deploy
  loop:
    - { name: 'ci_deploy', key: 'ssh-rsa AAAA...' }
    - { name: 'admin', key: 'ssh-rsa BBBB...' }
```

---

## Command Modules

### command vs shell vs raw

```
┌────────────────────────────────────────────────────────────────────────┐
│                    COMMAND MODULE COMPARISON                           │
├─────────────┬──────────────┬──────────────┬────────────────────────────┤
│ Feature     │ command      │ shell        │ raw                        │
├─────────────┼──────────────┼──────────────┼────────────────────────────┤
│ Shell       │ ❌ No        │ ✅ Yes       │ ✅ Yes                     │
│ Pipes       │ ❌ No        │ ✅ Yes       │ ✅ Yes                     │
│ Redirects   │ ❌ No        │ ✅ Yes       │ ✅ Yes                     │
│ Variables   │ ❌ No        │ ✅ Yes       │ ✅ Yes                     │
│ Python req  │ ✅ Yes       │ ✅ Yes       │ ❌ No                      │
│ Security    │ ✅ Safer     │ ⚠️ Riskier   │ ⚠️ Riskier                 │
│ Idempotent  │ With creates │ With creates │ ❌ Never                   │
└─────────────┴──────────────┴──────────────┴────────────────────────────┘
```

### command - Execute without shell

```yaml
- name: Run command safely
  ansible.builtin.command:
    cmd: /opt/scripts/deploy.sh --version {{ version }}
    chdir: /opt/app
    creates: /opt/app/.deployed-{{ version }}
  register: deploy_result
  changed_when: "'deployed' in deploy_result.stdout"

- name: Run with argument list (safer)
  ansible.builtin.command:
    argv:
      - /usr/bin/docker
      - exec
      - mycontainer
      - /app/healthcheck.sh
  register: health

- name: Conditional execution
  ansible.builtin.command:
    cmd: /opt/scripts/migrate.sh
    chdir: /opt/app
  when: run_migrations | default(false)
  changed_when: false
```

### shell - Execute with shell features

```yaml
- name: Use pipes and redirects
  ansible.builtin.shell: |
    cat /var/log/nginx/access.log \
      | grep "$(date +%Y-%m-%d)" \
      | grep -E "5[0-9]{2}" \
      | wc -l
  register: error_count
  changed_when: false

- name: Multiple commands
  ansible.builtin.shell: |
    set -euo pipefail
    cd /opt/app
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate --noinput
  args:
    executable: /bin/bash
  environment:
    DJANGO_SETTINGS_MODULE: config.production

- name: Process substitution
  ansible.builtin.shell: >
    diff <(systemctl list-units --state=running)
         <(cat /opt/expected_services.txt) || true
  args:
    executable: /bin/bash
  register: service_diff
  changed_when: false
```

### script - Run local script remotely

```yaml
- name: Execute local script on remote
  ansible.builtin.script:
    cmd: scripts/setup_app.sh --env production
    creates: /opt/app/.setup_complete
  register: script_result

- name: Execute with specific interpreter
  ansible.builtin.script:
    cmd: scripts/configure.py
    executable: /usr/bin/python3
  args:
    chdir: /opt/app
```

### raw - Without Python

```yaml
- name: Bootstrap Python (before Ansible can work)
  ansible.builtin.raw: |
    apt-get update && apt-get install -y python3
  when: ansible_python_interpreter is not defined
  changed_when: true

- name: Quick network test
  ansible.builtin.raw: ping -c 1 google.com
  register: ping_result
  failed_when: false
```

---

## System Modules

### systemd - Service management

```yaml
- name: Full service management
  ansible.builtin.systemd:
    name: nginx
    state: restarted
    enabled: true
    daemon_reload: true
    scope: system

- name: Stop and disable
  ansible.builtin.systemd:
    name: apache2
    state: stopped
    enabled: false
    masked: true

- name: Just reload config
  ansible.builtin.systemd:
    name: nginx
    state: reloaded
```

### user & group

```yaml
- name: Create system group
  ansible.builtin.group:
    name: appgroup
    gid: 1500
    system: true
    state: present

- name: Create application user
  ansible.builtin.user:
    name: appuser
    uid: 1500
    group: appgroup
    groups:
      - docker
      - sudo
    shell: /bin/bash
    home: /home/appuser
    create_home: true
    generate_ssh_key: true
    ssh_key_bits: 4096
    ssh_key_file: .ssh/id_ed25519
    ssh_key_type: ed25519
    state: present
    password: "{{ user_password | password_hash('sha512', 'mysecretsalt') }}"
    update_password: on_create

- name: Remove user completely
  ansible.builtin.user:
    name: olduser
    state: absent
    remove: true
    force: true
```

### cron - Schedule tasks

```yaml
- name: Add cron job with all options
  ansible.builtin.cron:
    name: "Database backup"
    minute: "0"
    hour: "2"
    day: "*"
    month: "*"
    weekday: "1-5"
    job: "/opt/scripts/backup.sh >> /var/log/backup.log 2>&1"
    user: postgres
    state: present

- name: Add environment variable
  ansible.builtin.cron:
    name: PATH
    env: true
    job: /usr/local/bin:/usr/bin
    user: deploy

- name: Special time syntax
  ansible.builtin.cron:
    name: "Reboot cleanup"
    special_time: reboot
    job: "/opt/scripts/cleanup_temp.sh"

# special_time options: reboot, yearly, annually, monthly, weekly, daily, hourly
```

---

## Package Modules

### apt - Debian/Ubuntu

```yaml
- name: Update cache and install packages
  ansible.builtin.apt:
    name:
      - nginx
      - python3-pip
      - git
      - curl
    state: present
    update_cache: true
    cache_valid_time: 3600

- name: Install specific version
  ansible.builtin.apt:
    name: nginx=1.18.0-0ubuntu1
    state: present

- name: Upgrade all packages
  ansible.builtin.apt:
    upgrade: dist
    update_cache: true
    autoremove: true
    autoclean: true

- name: Add repository and install
  block:
    - name: Add GPG key
      ansible.builtin.apt_key:
        url: https://packages.grafana.com/gpg.key
        state: present

    - name: Add repository
      ansible.builtin.apt_repository:
        repo: deb https://packages.grafana.com/oss/deb stable main
        state: present
        filename: grafana

    - name: Install Grafana
      ansible.builtin.apt:
        name: grafana
        update_cache: true
```

### pip - Python packages

```yaml
- name: Install in virtualenv
  ansible.builtin.pip:
    name:
      - flask>=2.0
      - gunicorn
      - redis
    virtualenv: /opt/app/venv
    virtualenv_command: python3 -m venv
    state: present

- name: Install from requirements
  ansible.builtin.pip:
    requirements: /opt/app/requirements.txt
    virtualenv: /opt/app/venv
    extra_args: --no-cache-dir

- name: Install editable package
  ansible.builtin.pip:
    name: /opt/app
    editable: true
    virtualenv: /opt/app/venv
```

---

## Network Modules

### uri - HTTP requests

```yaml
- name: GET request
  ansible.builtin.uri:
    url: https://api.example.com/health
    method: GET
    return_content: true
    status_code: 200
    timeout: 30
  register: health_check

- name: POST with authentication
  ansible.builtin.uri:
    url: https://api.example.com/deploy
    method: POST
    headers:
      Authorization: "Bearer {{ api_token }}"
      Content-Type: application/json
    body_format: json
    body:
      version: "{{ version }}"
      environment: "{{ env }}"
    status_code:
      - 200
      - 201
  register: deploy_response

- name: Wait for service ready
  ansible.builtin.uri:
    url: http://localhost:8080/ready
    status_code: 200
  register: result
  until: result.status == 200
  retries: 30
  delay: 10
```

### get_url - Download files

```yaml
- name: Download with checksum verification
  ansible.builtin.get_url:
    url: https://releases.hashicorp.com/terraform/1.5.0/terraform_1.5.0_linux_amd64.zip
    dest: /tmp/terraform.zip
    checksum: sha256:c0d5a1f1c8e1d5f4d1e2f5b1a2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e
    mode: '0644'
    timeout: 60
    force: false
```

---

## Module Quick Reference

| Module | Use Case | Key Parameters |
|--------|----------|----------------|
| `file` | Files/dirs/links | path, state, mode |
| `copy` | Transfer files | src, dest, content |
| `template` | Jinja2 files | src, dest, vars |
| `lineinfile` | Single lines | path, regexp, line |
| `blockinfile` | Text blocks | path, block, marker |
| `command` | Safe execution | cmd, creates, chdir |
| `shell` | Shell features | cmd, executable |
| `systemd` | Services | name, state, enabled |
| `user` | User accounts | name, groups, home |
| `apt` | Debian packages | name, state, update_cache |
| `pip` | Python packages | name, virtualenv |
| `uri` | HTTP requests | url, method, body |

---

## Praktisk Övning

Implementera komplett server setup:

```yaml
---
- name: Complete server provisioning
  hosts: webservers
  become: true

  vars:
    app_user: deploy
    app_dir: /opt/myapp

  tasks:
    - name: Create app user
      user:
        name: "{{ app_user }}"
        groups: docker

    - name: Setup directories
      file:
        path: "{{ item }}"
        state: directory
        owner: "{{ app_user }}"
      loop:
        - "{{ app_dir }}"
        - "{{ app_dir }}/logs"

    - name: Install packages
      apt:
        name: [nginx, python3-pip]
        update_cache: true

    - name: Configure nginx
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: restart nginx

  handlers:
    - name: restart nginx
      systemd:
        name: nginx
        state: restarted
```

---

## Sammanfattning

| Kategori | Viktiga Modules |
|----------|-----------------|
| Files | file, copy, template, lineinfile |
| Commands | command, shell, script |
| System | systemd, user, group, cron |
| Packages | apt, yum, pip |
| Network | uri, get_url |

---

## Nästa Steg

Core modules bemästrade. Nästa: **Cloud Modules** — AWS, Azure, GCP automation.
''',
}

NODE_14_CLOUD_MODULES = {
    "node_id": 14,
    "title": "Cloud Modules",
    "slug": "cloud-modules",
    "estimated_minutes": 60,
    "xp_reward": 155,
    "prerequisites": [13],
    "content": r'''
# Cloud Modules

## Varför detta är kritiskt

> "Manuella klick i AWS Console = kaos. Cloud modules ger dig reproducerbar, versionshanterad infrastruktur. Infrastructure as Code på riktigt."

**Cloud collections:**
- **amazon.aws** — EC2, S3, RDS, Lambda, etc.
- **azure.azcollection** — VMs, Storage, AKS, etc.
- **google.cloud** — GCE, GKE, Cloud Storage, etc.
- **community.digitalocean** — Droplets, Spaces, etc.

---

## Cloud Automation Arkitektur

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ANSIBLE CLOUD AUTOMATION                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  CONTROL NODE                        CLOUD PROVIDERS                    │
│  ────────────                        ───────────────                    │
│  ┌──────────────┐                    ┌─────────────────┐                │
│  │ Playbook     │                    │      AWS        │                │
│  │  ↓           │                    │    ┌─────┐      │                │
│  │ Cloud Module │ ──── API Calls ──► │    │ EC2 │      │                │
│  │  ↓           │                    │    │ S3  │      │                │
│  │ localhost    │                    │    │ RDS │      │                │
│  └──────────────┘                    └─────────────────┘                │
│        │                             ┌─────────────────┐                │
│        │                             │     Azure       │                │
│        └──── API Calls ────────────► │    ┌─────┐      │                │
│                                      │    │ VMs │      │                │
│                                      │    │ AKS │      │                │
│                                      └─────────────────┘                │
│                                                                         │
│  AUTHENTICATION METHODS:                                                │
│  ├── Environment Variables (AWS_ACCESS_KEY_ID)                          │
│  ├── IAM Roles (EC2 Instance Profiles)                                  │
│  ├── Credential Files (~/.aws/credentials)                              │
│  └── Service Account JSON (GCP)                                         │
│                                                                         │
│  DYNAMIC INVENTORY:                                                     │
│  ├── aws_ec2           → Auto-discover EC2 instances                    │
│  ├── azure_rm          → Auto-discover Azure VMs                        │
│  └── gcp_compute       → Auto-discover GCE instances                    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## AWS Setup

### Installation

```bash
# Collection
ansible-galaxy collection install amazon.aws

# Python dependencies
pip install boto3 botocore
```

### Authentication

```bash
# Option 1: Environment variables
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_REGION=eu-north-1

# Option 2: Credential file (~/.aws/credentials)
[default]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

# Option 3: IAM Instance Profile (on EC2)
# No configuration needed - auto-detected
```

---

## AWS EC2 Management

### Launch Instances

```yaml
---
- name: AWS Infrastructure
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    region: eu-north-1
    instance_type: t3.micro
    ami_id: ami-0fe8bec493a81c7da  # Ubuntu 22.04

  tasks:
    - name: Create security group
      amazon.aws.ec2_security_group:
        name: web-sg
        description: Web server security group
        region: "{{ region }}"
        vpc_id: vpc-123456789
        rules:
          - proto: tcp
            ports: 22
            cidr_ip: 10.0.0.0/8
            rule_desc: SSH from internal
          - proto: tcp
            ports: 80
            cidr_ip: 0.0.0.0/0
            rule_desc: HTTP from anywhere
          - proto: tcp
            ports: 443
            cidr_ip: 0.0.0.0/0
            rule_desc: HTTPS from anywhere
        rules_egress:
          - proto: all
            cidr_ip: 0.0.0.0/0
        tags:
          Environment: production
          ManagedBy: ansible
      register: sg

    - name: Launch EC2 instances
      amazon.aws.ec2_instance:
        name: "web-{{ item }}"
        instance_type: "{{ instance_type }}"
        image_id: "{{ ami_id }}"
        region: "{{ region }}"
        key_name: deploy-key
        vpc_subnet_id: subnet-123456789
        security_group: "{{ sg.group_id }}"
        network:
          assign_public_ip: true
        volumes:
          - device_name: /dev/sda1
            ebs:
              volume_size: 30
              volume_type: gp3
              delete_on_termination: true
        instance_initiated_shutdown_behavior: stop
        wait: true
        state: running
        tags:
          Environment: production
          Role: webserver
          ManagedBy: ansible
      loop:
        - "01"
        - "02"
        - "03"
      register: ec2_instances

    - name: Wait for SSH
      ansible.builtin.wait_for:
        host: "{{ item.instances[0].public_ip_address }}"
        port: 22
        delay: 10
        timeout: 300
      loop: "{{ ec2_instances.results }}"
```

### S3 Bucket Management

```yaml
- name: Create S3 bucket with lifecycle
  amazon.aws.s3_bucket:
    name: mycompany-backups-{{ env }}
    region: "{{ region }}"
    state: present
    versioning: true
    encryption: AES256
    public_access:
      block_public_acls: true
      block_public_policy: true
      ignore_public_acls: true
      restrict_public_buckets: true
    tags:
      Environment: "{{ env }}"

- name: Configure lifecycle rules
  amazon.aws.s3_lifecycle:
    name: mycompany-backups-{{ env }}
    rules:
      - id: expire-old-versions
        status: enabled
        noncurrent_version_expiration_days: 30
      - id: transition-to-glacier
        prefix: archives/
        status: enabled
        transitions:
          - days: 90
            storage_class: GLACIER

- name: Upload file to S3
  amazon.aws.s3_object:
    bucket: mycompany-backups-{{ env }}
    object: backups/db-{{ ansible_date_time.date }}.sql.gz
    src: /tmp/backup.sql.gz
    mode: put
    encryption: aws:kms
```

### RDS Database

```yaml
- name: Create RDS PostgreSQL
  amazon.aws.rds_instance:
    id: myapp-db-{{ env }}
    state: present
    engine: postgres
    engine_version: "15.3"
    db_instance_class: db.t3.medium
    allocated_storage: 100
    storage_type: gp3
    storage_encrypted: true
    master_username: "{{ db_master_user }}"
    master_user_password: "{{ db_master_password }}"
    db_name: myapp
    vpc_security_group_ids:
      - "{{ db_sg.group_id }}"
    db_subnet_group_name: my-db-subnet-group
    multi_az: "{{ env == 'production' }}"
    backup_retention_period: 7
    preferred_backup_window: "03:00-04:00"
    auto_minor_version_upgrade: true
    tags:
      Environment: "{{ env }}"
  register: rds_result

- name: Wait for RDS available
  amazon.aws.rds_instance_info:
    db_instance_identifier: myapp-db-{{ env }}
  register: rds_info
  until: rds_info.instances[0].db_instance_status == 'available'
  retries: 30
  delay: 60
```

---

## AWS Dynamic Inventory

### aws_ec2.yml

```yaml
---
plugin: amazon.aws.aws_ec2

regions:
  - eu-north-1
  - eu-west-1

filters:
  tag:Environment:
    - production
    - staging
  instance-state-name: running

keyed_groups:
  # Group by Environment tag
  - key: tags.Environment
    prefix: env
    separator: "_"
  # Group by Role tag
  - key: tags.Role
    prefix: role
    separator: "_"
  # Group by instance type
  - key: instance_type
    prefix: type
    separator: "_"
  # Group by region
  - key: placement.region
    prefix: region

compose:
  # Use public IP for ansible_host
  ansible_host: public_ip_address | default(private_ip_address)
  # Set SSH user based on AMI
  ansible_user: "'ubuntu'"

hostnames:
  - tag:Name
  - dns-name
  - private-ip-address
```

### Usage

```bash
# Test inventory
ansible-inventory -i aws_ec2.yml --graph

# Output:
# @all:
#   |--@env_production:
#   |  |--web-01
#   |  |--web-02
#   |--@role_webserver:
#   |  |--web-01
#   |  |--web-02

# Run against dynamic inventory
ansible-playbook -i aws_ec2.yml deploy.yml
```

---

## Azure Setup

### Installation

```bash
ansible-galaxy collection install azure.azcollection
pip install azure-identity azure-mgmt-compute azure-mgmt-network azure-mgmt-resource
```

### Authentication

```bash
# Service Principal
export AZURE_SUBSCRIPTION_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
export AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
export AZURE_SECRET=your-secret
export AZURE_TENANT=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

### Azure VM Deployment

```yaml
---
- name: Azure Infrastructure
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    resource_group: myapp-rg
    location: northeurope

  tasks:
    - name: Create resource group
      azure.azcollection.azure_rm_resourcegroup:
        name: "{{ resource_group }}"
        location: "{{ location }}"
        tags:
          Environment: production

    - name: Create virtual network
      azure.azcollection.azure_rm_virtualnetwork:
        resource_group: "{{ resource_group }}"
        name: myapp-vnet
        address_prefixes: "10.0.0.0/16"

    - name: Create subnet
      azure.azcollection.azure_rm_subnet:
        resource_group: "{{ resource_group }}"
        virtual_network: myapp-vnet
        name: web-subnet
        address_prefix: "10.0.1.0/24"

    - name: Create NSG
      azure.azcollection.azure_rm_securitygroup:
        resource_group: "{{ resource_group }}"
        name: web-nsg
        rules:
          - name: SSH
            protocol: Tcp
            destination_port_range: 22
            access: Allow
            priority: 1000
            direction: Inbound
          - name: HTTP
            protocol: Tcp
            destination_port_range: 80
            access: Allow
            priority: 1001
            direction: Inbound

    - name: Create VM
      azure.azcollection.azure_rm_virtualmachine:
        resource_group: "{{ resource_group }}"
        name: web-vm-01
        vm_size: Standard_B2s
        admin_username: azureuser
        ssh_password_enabled: false
        ssh_public_keys:
          - path: /home/azureuser/.ssh/authorized_keys
            key_data: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
        network_interfaces: web-vm-01-nic
        image:
          offer: 0001-com-ubuntu-server-jammy
          publisher: Canonical
          sku: 22_04-lts
          version: latest
        managed_disk_type: Standard_LRS
        tags:
          Environment: production
```

---

## GCP Setup

### Installation

```bash
ansible-galaxy collection install google.cloud
pip install google-auth requests
```

### GCP Instance

```yaml
---
- name: GCP Infrastructure
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    project: my-gcp-project
    zone: europe-north1-a

  tasks:
    - name: Create VPC network
      google.cloud.gcp_compute_network:
        name: myapp-network
        auto_create_subnetworks: false
        project: "{{ project }}"
        auth_kind: serviceaccount
        service_account_file: /path/to/sa.json
      register: network

    - name: Create subnet
      google.cloud.gcp_compute_subnetwork:
        name: web-subnet
        network: "{{ network }}"
        ip_cidr_range: 10.0.1.0/24
        region: europe-north1
        project: "{{ project }}"
        auth_kind: serviceaccount
        service_account_file: /path/to/sa.json

    - name: Create firewall rule
      google.cloud.gcp_compute_firewall:
        name: allow-web
        network: "{{ network }}"
        allowed:
          - ip_protocol: tcp
            ports:
              - "80"
              - "443"
              - "22"
        source_ranges:
          - 0.0.0.0/0
        project: "{{ project }}"
        auth_kind: serviceaccount
        service_account_file: /path/to/sa.json

    - name: Create instance
      google.cloud.gcp_compute_instance:
        name: web-instance-01
        machine_type: e2-medium
        zone: "{{ zone }}"
        project: "{{ project }}"
        auth_kind: serviceaccount
        service_account_file: /path/to/sa.json
        disks:
          - auto_delete: true
            boot: true
            initialize_params:
              source_image: projects/ubuntu-os-cloud/global/images/family/ubuntu-2204-lts
              disk_size_gb: 30
              disk_type: pd-standard
        network_interfaces:
          - network: "{{ network }}"
            subnetwork: "{{ subnet }}"
            access_configs:
              - name: External NAT
                type: ONE_TO_ONE_NAT
        labels:
          environment: production
        tags:
          items:
            - web
            - production
      register: instance
```

---

## Cloud Module Comparison

| Feature | AWS | Azure | GCP |
|---------|-----|-------|-----|
| Collection | amazon.aws | azure.azcollection | google.cloud |
| Auth | IAM/Keys | Service Principal | Service Account |
| Dynamic Inv | aws_ec2 | azure_rm | gcp_compute |
| VM Module | ec2_instance | azure_rm_virtualmachine | gcp_compute_instance |
| Storage | s3_bucket | azure_rm_storageaccount | gcp_storage_bucket |

---

## Best Practices

### DO ✅

```yaml
# Always use dynamic inventory
# Always tag resources
# Use IAM roles over access keys
# Encrypt sensitive data
# Use idempotent operations
```

### DON'T ❌

```yaml
# Never hardcode credentials
# Never skip tagging
# Don't create resources without cleanup plans
```

---

## Sammanfattning

| Cloud | Setup | Key Modules |
|-------|-------|-------------|
| AWS | amazon.aws + boto3 | ec2_instance, s3_bucket, rds_instance |
| Azure | azure.azcollection | azure_rm_virtualmachine |
| GCP | google.cloud | gcp_compute_instance |

---

## Nästa Steg

Cloud bemästrat. Nästa: **Container Modules** — Docker och Kubernetes automation.
''',
}

NODE_15_CONTAINER_MODULES = {
    "node_id": 15,
    "title": "Container Modules",
    "slug": "container-modules",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "prerequisites": [13],
    "content": r'''
# Container Modules

## Varför detta är kritiskt

> "Containers är standard. Docker CLI är bra för ad-hoc, men Ansible ger dig reproducerbar, deklarativ container-hantering. Kombinera IaC med containers."

**Container collections:**
- **community.docker** — Docker containers, images, networks
- **kubernetes.core** — K8s resources, deployments
- **community.kubernetes** — Extended K8s support

---

## Container Automation Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ANSIBLE CONTAINER AUTOMATION                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ANSIBLE PLAYBOOK                                                       │
│  ─────────────────                                                      │
│                                                                         │
│  ┌─────────────┐    ┌──────────────────────────────────────────────┐    │
│  │ docker_image│───►│ Pull/Build Images                            │    │
│  └─────────────┘    └──────────────────────────────────────────────┘    │
│         │                                                               │
│         ▼                                                               │
│  ┌───────────────┐  ┌──────────────────────────────────────────────┐    │
│  │docker_network │─►│ Create Networks (bridge, overlay)            │    │
│  └───────────────┘  └──────────────────────────────────────────────┘    │
│         │                                                               │
│         ▼                                                               │
│  ┌───────────────┐  ┌──────────────────────────────────────────────┐    │
│  │ docker_volume │─►│ Create Persistent Volumes                    │    │
│  └───────────────┘  └──────────────────────────────────────────────┘    │
│         │                                                               │
│         ▼                                                               │
│  ┌─────────────────┐┌──────────────────────────────────────────────┐    │
│  │docker_container ││ Run Containers with configs                  │    │
│  └─────────────────┘└──────────────────────────────────────────────┘    │
│         │                                                               │
│         ▼                                                               │
│  ┌─────────────────┐┌──────────────────────────────────────────────┐    │
│  │docker_compose_v2││ Multi-container apps with Compose            │    │
│  └─────────────────┘└──────────────────────────────────────────────┘    │
│                                                                         │
│  KUBERNETES FLOW:                                                       │
│  ┌────────┐  ┌────────────┐  ┌────────┐  ┌─────────────────────────┐    │
│  │ k8s    │─►│ Deployment │─►│Service │─►│ Ingress/ConfigMaps/etc │    │
│  └────────┘  └────────────┘  └────────┘  └─────────────────────────┘    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Docker Setup

### Installation

```bash
# Collection
ansible-galaxy collection install community.docker

# Python SDK (på control node OCH target om delegating)
pip install docker docker-compose
```

### Docker Connection

```yaml
# ansible.cfg
[defaults]
# För remote Docker hosts
host_key_checking = False

# Eller kör mot Docker socket direkt
[all:vars]
ansible_connection=docker
```

---

## Docker Image Management

### Pull Images

```yaml
---
- name: Docker Image Management
  hosts: docker_hosts
  become: true

  tasks:
    - name: Pull specific image version
      community.docker.docker_image:
        name: nginx
        tag: "1.25-alpine"
        source: pull
        force_source: "{{ force_pull | default(false) }}"

    - name: Pull multiple images
      community.docker.docker_image:
        name: "{{ item.name }}"
        tag: "{{ item.tag }}"
        source: pull
      loop:
        - { name: nginx, tag: "1.25-alpine" }
        - { name: redis, tag: "7-alpine" }
        - { name: postgres, tag: "15-alpine" }

    - name: Pull from private registry
      community.docker.docker_image:
        name: registry.company.com/myapp
        tag: "{{ version }}"
        source: pull
      environment:
        DOCKER_CONFIG: /root/.docker
```

### Build Images

```yaml
- name: Build application image
  community.docker.docker_image:
    name: myapp
    tag: "{{ git_sha }}"
    source: build
    build:
      path: /opt/app
      dockerfile: Dockerfile
      pull: true
      nocache: "{{ nocache | default(false) }}"
      args:
        APP_VERSION: "{{ version }}"
        BUILD_DATE: "{{ ansible_date_time.iso8601 }}"
      target: production
    push: false
  register: build_result

- name: Tag and push to registry
  community.docker.docker_image:
    name: myapp
    tag: "{{ git_sha }}"
    repository: registry.company.com/myapp
    push: true
    source: local
  when: build_result.changed

- name: Cleanup old images
  community.docker.docker_prune:
    images: true
    images_filters:
      dangling: true
    containers: true
    containers_filters:
      until: 24h
```

---

## Docker Container Management

### Run Containers

```yaml
---
- name: Container Deployment
  hosts: docker_hosts
  become: true

  vars:
    app_name: myapp
    app_port: 8080

  tasks:
    - name: Create application network
      community.docker.docker_network:
        name: "{{ app_name }}_network"
        driver: bridge
        ipam_config:
          - subnet: 172.28.0.0/16
            gateway: 172.28.0.1

    - name: Create data volume
      community.docker.docker_volume:
        name: "{{ app_name }}_data"
        driver: local
        driver_options:
          type: none
          device: /opt/{{ app_name }}/data
          o: bind

    - name: Run PostgreSQL container
      community.docker.docker_container:
        name: "{{ app_name }}_db"
        image: postgres:15-alpine
        state: started
        restart_policy: unless-stopped
        networks:
          - name: "{{ app_name }}_network"
            aliases:
              - db
              - postgres
        volumes:
          - "{{ app_name }}_data:/var/lib/postgresql/data"
        env:
          POSTGRES_DB: "{{ db_name }}"
          POSTGRES_USER: "{{ db_user }}"
          POSTGRES_PASSWORD: "{{ db_password }}"
        healthcheck:
          test: ["CMD-SHELL", "pg_isready -U {{ db_user }}"]
          interval: 10s
          timeout: 5s
          retries: 5
          start_period: 30s
        log_driver: json-file
        log_options:
          max-size: "10m"
          max-file: "3"

    - name: Run Redis container
      community.docker.docker_container:
        name: "{{ app_name }}_redis"
        image: redis:7-alpine
        state: started
        restart_policy: unless-stopped
        networks:
          - name: "{{ app_name }}_network"
            aliases:
              - redis
              - cache
        command: redis-server --appendonly yes
        volumes:
          - redis_data:/data
        memory: 512m
        memory_swap: 512m

    - name: Run application container
      community.docker.docker_container:
        name: "{{ app_name }}_web"
        image: "myapp:{{ version }}"
        state: started
        restart_policy: unless-stopped
        pull: true
        recreate: "{{ force_recreate | default(false) }}"
        networks:
          - name: "{{ app_name }}_network"
        ports:
          - "{{ app_port }}:8080"
          - "127.0.0.1:9090:9090"  # Metrics only on localhost
        volumes:
          - /opt/{{ app_name }}/config:/app/config:ro
          - /opt/{{ app_name }}/logs:/app/logs
        env:
          DATABASE_URL: "postgres://{{ db_user }}:{{ db_password }}@db:5432/{{ db_name }}"
          REDIS_URL: "redis://redis:6379/0"
          LOG_LEVEL: "{{ log_level | default('info') }}"
          SECRET_KEY: "{{ secret_key }}"
        labels:
          traefik.enable: "true"
          traefik.http.routers.myapp.rule: "Host(`{{ domain }}`)"
        healthcheck:
          test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
          interval: 30s
          timeout: 10s
          retries: 3
        comparisons:
          image: strict
          env: strict
          volumes: allow_more_present
      register: container_result

    - name: Wait for container healthy
      community.docker.docker_container_info:
        name: "{{ app_name }}_web"
      register: container_info
      until: container_info.container.State.Health.Status == "healthy"
      retries: 12
      delay: 10
      when: container_result.changed
```

### Container Operations

```yaml
- name: Stop container gracefully
  community.docker.docker_container:
    name: myapp_web
    state: stopped
    stop_timeout: 30

- name: Remove container and volumes
  community.docker.docker_container:
    name: myapp_web
    state: absent
    keep_volumes: false

- name: Execute command in container
  community.docker.docker_container_exec:
    container: myapp_web
    command: /bin/sh -c "python manage.py migrate"
    chdir: /app
  register: migrate_result

- name: Copy file to container
  community.docker.docker_container_copy_into:
    container: myapp_web
    path: /app/config/override.yml
    content: |
      debug: true
      log_level: debug
```

---

## Docker Compose

### Deploy Compose Stack

```yaml
- name: Deploy with Docker Compose
  community.docker.docker_compose_v2:
    project_src: /opt/app
    project_name: myapp
    state: present
    pull: always
    remove_orphans: true
    env_files:
      - .env.production
  register: compose_result

- name: Compose with inline definition
  community.docker.docker_compose_v2:
    project_name: monitoring
    definition:
      version: "3.8"
      services:
        prometheus:
          image: prom/prometheus:latest
          ports:
            - "9090:9090"
          volumes:
            - prometheus_data:/prometheus
            - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
        grafana:
          image: grafana/grafana:latest
          ports:
            - "3000:3000"
          volumes:
            - grafana_data:/var/lib/grafana
          depends_on:
            - prometheus
      volumes:
        prometheus_data:
        grafana_data:
    state: present

- name: Scale service
  community.docker.docker_compose_v2:
    project_src: /opt/app
    scale:
      web: 3
      worker: 2
```

---

## Kubernetes Modules

### Installation

```bash
ansible-galaxy collection install kubernetes.core
pip install kubernetes
```

### Authentication

```yaml
# Use kubeconfig
- hosts: localhost
  vars:
    kubeconfig: ~/.kube/config

# Or in-cluster (ServiceAccount)
- hosts: localhost
  environment:
    K8S_AUTH_IN_CLUSTER: "true"
```

### Deploy Resources

```yaml
---
- name: Kubernetes Deployment
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    namespace: production
    app_name: myapp
    replicas: 3

  tasks:
    - name: Create namespace
      kubernetes.core.k8s:
        state: present
        definition:
          apiVersion: v1
          kind: Namespace
          metadata:
            name: "{{ namespace }}"
            labels:
              environment: production

    - name: Create ConfigMap
      kubernetes.core.k8s:
        state: present
        definition:
          apiVersion: v1
          kind: ConfigMap
          metadata:
            name: "{{ app_name }}-config"
            namespace: "{{ namespace }}"
          data:
            LOG_LEVEL: info
            API_URL: https://api.example.com

    - name: Create Secret
      kubernetes.core.k8s:
        state: present
        definition:
          apiVersion: v1
          kind: Secret
          metadata:
            name: "{{ app_name }}-secrets"
            namespace: "{{ namespace }}"
          type: Opaque
          stringData:
            DATABASE_URL: "{{ db_url }}"
            API_KEY: "{{ api_key }}"

    - name: Create Deployment
      kubernetes.core.k8s:
        state: present
        definition:
          apiVersion: apps/v1
          kind: Deployment
          metadata:
            name: "{{ app_name }}"
            namespace: "{{ namespace }}"
            labels:
              app: "{{ app_name }}"
          spec:
            replicas: "{{ replicas }}"
            selector:
              matchLabels:
                app: "{{ app_name }}"
            strategy:
              type: RollingUpdate
              rollingUpdate:
                maxSurge: 1
                maxUnavailable: 0
            template:
              metadata:
                labels:
                  app: "{{ app_name }}"
              spec:
                containers:
                  - name: "{{ app_name }}"
                    image: "myregistry/{{ app_name }}:{{ version }}"
                    ports:
                      - containerPort: 8080
                    envFrom:
                      - configMapRef:
                          name: "{{ app_name }}-config"
                      - secretRef:
                          name: "{{ app_name }}-secrets"
                    resources:
                      requests:
                        memory: "256Mi"
                        cpu: "100m"
                      limits:
                        memory: "512Mi"
                        cpu: "500m"
                    livenessProbe:
                      httpGet:
                        path: /health
                        port: 8080
                      initialDelaySeconds: 30
                      periodSeconds: 10
                    readinessProbe:
                      httpGet:
                        path: /ready
                        port: 8080
                      initialDelaySeconds: 5
                      periodSeconds: 5

    - name: Create Service
      kubernetes.core.k8s:
        state: present
        definition:
          apiVersion: v1
          kind: Service
          metadata:
            name: "{{ app_name }}"
            namespace: "{{ namespace }}"
          spec:
            selector:
              app: "{{ app_name }}"
            ports:
              - port: 80
                targetPort: 8080
            type: ClusterIP

    - name: Create Ingress
      kubernetes.core.k8s:
        state: present
        definition:
          apiVersion: networking.k8s.io/v1
          kind: Ingress
          metadata:
            name: "{{ app_name }}"
            namespace: "{{ namespace }}"
            annotations:
              kubernetes.io/ingress.class: nginx
              cert-manager.io/cluster-issuer: letsencrypt-prod
          spec:
            tls:
              - hosts:
                  - "{{ domain }}"
                secretName: "{{ app_name }}-tls"
            rules:
              - host: "{{ domain }}"
                http:
                  paths:
                    - path: /
                      pathType: Prefix
                      backend:
                        service:
                          name: "{{ app_name }}"
                          port:
                            number: 80

    - name: Wait for deployment ready
      kubernetes.core.k8s_info:
        api_version: apps/v1
        kind: Deployment
        name: "{{ app_name }}"
        namespace: "{{ namespace }}"
      register: deployment
      until: deployment.resources[0].status.readyReplicas == replicas
      retries: 30
      delay: 10
```

### Helm Charts

```yaml
- name: Add Helm repo
  kubernetes.core.helm_repository:
    name: bitnami
    repo_url: https://charts.bitnami.com/bitnami

- name: Deploy with Helm
  kubernetes.core.helm:
    name: nginx
    chart_ref: bitnami/nginx
    release_namespace: web
    create_namespace: true
    values:
      replicaCount: 3
      service:
        type: LoadBalancer
      resources:
        requests:
          memory: 128Mi
          cpu: 100m
    wait: true
    timeout: 10m
```

---

## Module Reference

| Module | Purpose |
|--------|---------|
| `docker_image` | Build/pull images |
| `docker_container` | Run containers |
| `docker_network` | Manage networks |
| `docker_volume` | Manage volumes |
| `docker_compose_v2` | Deploy stacks |
| `k8s` | K8s resources |
| `k8s_info` | Query K8s |
| `helm` | Helm deployments |

---

## Sammanfattning

| Platform | Collection | Key Modules |
|----------|------------|-------------|
| Docker | community.docker | docker_container, docker_image |
| Kubernetes | kubernetes.core | k8s, helm |
| Compose | community.docker | docker_compose_v2 |

---

## Nästa Steg

Container automation klar. Nästa: **Custom Modules** — bygg egna Ansible-moduler.
''',
}


NODE_16_CUSTOM_MODULES = {
    "node_id": 16,
    "title": "Custom Modules & Plugins",
    "slug": "custom-modules",
    "estimated_minutes": 65,
    "xp_reward": 165,
    "prerequisites": [13],
    "content": r"""
# Custom Modules & Plugins

## Varför detta är kritiskt

> "Ansible har 3000+ moduler, men inte alltid precis vad du behöver. Custom modules låter dig integrera med vilken API eller system som helst. Din kreativitet är gränsen."

**Custom extension types:**
- **Modules** — Nya tasks/actions
- **Filters** — Data transformation
- **Lookups** — External data retrieval
- **Callbacks** — Output/logging customization
- **Connection plugins** — Custom transport

---

## Plugin Arkitektur

```
+-------------------------------------------------------------------------+
|                    ANSIBLE PLUGIN ARCHITECTURE                          |
+-------------------------------------------------------------------------+
|                                                                         |
|  PROJECT STRUCTURE:                                                     |
|  myproject/                                                             |
|  +-- ansible.cfg                                                        |
|  +-- playbook.yml                                                       |
|  +-- library/              <- MODULES (task actions)                    |
|  |   +-- my_api.py                                                      |
|  +-- filter_plugins/       <- FILTERS (data transforms)                 |
|  |   +-- my_filters.py                                                  |
|  +-- lookup_plugins/       <- LOOKUPS (external data)                   |
|  |   +-- my_lookup.py                                                   |
|  +-- callback_plugins/     <- CALLBACKS (output format)                 |
|  |   +-- my_callback.py                                                 |
|  +-- module_utils/         <- SHARED CODE (between modules)             |
|      +-- my_utils.py                                                    |
|                                                                         |
|  MODULE EXECUTION:                                                      |
|  Task -> Module Transferred -> Target Execution -> JSON Result          |
+-------------------------------------------------------------------------+
```

---

## Custom Module Basics

### Minimal Module Structure

```python
#!/usr/bin/python
# library/hello_world.py

from ansible.module_utils.basic import AnsibleModule

# DOCUMENTATION - Triple-quoted YAML string describing the module
# EXAMPLES - Triple-quoted YAML with usage examples
# RETURN - Triple-quoted YAML describing return values

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type="str", required=True),
            greeting=dict(type="str", default="Hello"),
        ),
        supports_check_mode=True
    )

    name = module.params["name"]
    greeting = module.params["greeting"]

    if module.check_mode:
        module.exit_json(changed=False, message=f"Would say: {greeting}, {name}!")

    message = f"{greeting}, {name}!"
    module.exit_json(changed=False, message=message)

if __name__ == "__main__":
    main()
```

### Documentation Strings

Ansible modules use three special variables for documentation:

```yaml
# DOCUMENTATION format:
---
module: hello_world
short_description: A simple hello world module
description:
  - Demonstrates basic Ansible module structure
options:
  name:
    description: Name to greet
    required: true
    type: str
  greeting:
    description: Custom greeting
    default: "Hello"
    type: str
author:
  - Your Name (@github_handle)

# EXAMPLES format:
- name: Say hello
  hello_world:
    name: World

- name: Custom greeting
  hello_world:
    name: Ansible
    greeting: "Greetings"

# RETURN format:
message:
  description: The greeting message
  type: str
  returned: always
  sample: "Hello, World!"
```

### Usage

```yaml
---
- hosts: localhost
  gather_facts: false
  tasks:
    - name: Test custom module
      hello_world:
        name: DevOps Engineer
        greeting: "Welcome"
      register: result

    - debug:
        var: result.message
        # Output: "Welcome, DevOps Engineer!"
```

---

## API Integration Module

### REST API Module Pattern

```python
#!/usr/bin/python
# library/api_resource.py

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
import json


def api_request(module, method, url, data=None):
    headers = {
        "Authorization": f"Bearer {module.params['api_token']}",
        "Content-Type": "application/json"
    }

    body = json.dumps(data) if data else None
    response, info = fetch_url(module, url, headers=headers,
                                method=method, data=body, timeout=30)

    if info["status"] == -1:
        module.fail_json(msg=f"Connection error: {info['msg']}")

    if response:
        body = response.read()
        return info["status"], json.loads(body) if body else {}
    return info["status"], {}


def main():
    module = AnsibleModule(
        argument_spec=dict(
            api_url=dict(type="str", required=True),
            api_token=dict(type="str", required=True, no_log=True),
            resource_type=dict(type="str", required=True),
            resource_id=dict(type="str", required=False),
            state=dict(type="str", default="present",
                      choices=["present", "absent"]),
            data=dict(type="dict", required=False, default={}),
        ),
        supports_check_mode=True,
    )

    base_url = module.params["api_url"].rstrip("/")
    resource_type = module.params["resource_type"]
    resource_id = module.params.get("resource_id")
    state = module.params["state"]
    data = module.params["data"]

    result = {"changed": False, "resource": None}

    if state == "absent" and resource_id:
        url = f"{base_url}/{resource_type}/{resource_id}"
        status, _ = api_request(module, "DELETE", url)
        if status in [200, 204]:
            result["changed"] = True
    elif state == "present":
        url = f"{base_url}/{resource_type}"
        status, response = api_request(module, "POST", url, data)
        if status in [200, 201]:
            result["changed"] = True
            result["resource"] = response

    module.exit_json(**result)


if __name__ == "__main__":
    main()
```

### Usage

```yaml
- name: Create resource
  api_resource:
    api_url: https://api.example.com
    api_token: "{{ vault_api_token }}"
    resource_type: users
    state: present
    data:
      name: John Doe
      email: john@example.com
  register: result

- name: Delete resource
  api_resource:
    api_url: https://api.example.com
    api_token: "{{ vault_api_token }}"
    resource_type: users
    resource_id: "12345"
    state: absent
```

---

## Custom Filter Plugins

### Filter Plugin Structure

```python
# filter_plugins/my_filters.py

import re
import hashlib

def to_slug(value):
    value = str(value).lower()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"[-\s]+", "-", value)
    return value.strip("-")

def hash_password(value, algorithm="sha256"):
    h = hashlib.new(algorithm)
    h.update(value.encode("utf-8"))
    return h.hexdigest()

def format_bytes(value, precision=2):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if abs(value) < 1024.0:
            return f"{value:.{precision}f} {unit}"
        value /= 1024.0
    return f"{value:.{precision}f} PB"

def mask_secret(value, show_chars=4):
    if len(value) <= show_chars * 2:
        return "*" * len(value)
    return value[:show_chars] + "*" * (len(value) - show_chars * 2) + value[-show_chars:]


class FilterModule:
    def filters(self):
        return {
            "to_slug": to_slug,
            "hash_password": hash_password,
            "format_bytes": format_bytes,
            "mask_secret": mask_secret,
        }
```

### Using Custom Filters

```yaml
---
- hosts: localhost
  vars:
    title: "My Awesome Blog Post!"
    password: "supersecret123"
    file_size: 15728640
    api_key: "sk-abc123456789xyz"

  tasks:
    - name: Demo filters
      debug:
        msg:
          - "Slug: {{ title | to_slug }}"
          # Output: "my-awesome-blog-post"

          - "Hash: {{ password | hash_password }}"
          # Output: sha256 hash

          - "Size: {{ file_size | format_bytes }}"
          # Output: "15.00 MB"

          - "Masked: {{ api_key | mask_secret }}"
          # Output: "sk-a*********xyz"
```

---

## Custom Lookup Plugins

### Lookup Plugin Structure

```python
# lookup_plugins/vault_secret.py

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError
import requests


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        self.set_options(var_options=variables, direct=kwargs)

        vault_addr = self.get_option("vault_addr") or "http://127.0.0.1:8200"
        vault_token = self.get_option("vault_token")

        if not vault_token:
            raise AnsibleError("vault_token is required")

        results = []

        for term in terms:
            url = f"{vault_addr}/v1/{term}"
            headers = {"X-Vault-Token": vault_token}

            try:
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                data = response.json()
                results.append(data.get("data", {}).get("data", {}))
            except requests.RequestException as e:
                raise AnsibleError(f"Vault lookup failed: {e}")

        return results
```

### Using Lookups

```yaml
- name: Get database password from Vault
  set_fact:
    db_secrets: "{{ lookup('vault_secret', 'secret/data/myapp/database') }}"

- name: Use the secret
  debug:
    msg: "DB Password: {{ db_secrets.password }}"
```

---

## Testing Custom Modules

### Unit Testing Pattern

```python
# tests/test_api_resource.py

import pytest
from unittest.mock import patch, MagicMock
import json
import sys
sys.path.insert(0, "library")

from api_resource import main


@pytest.fixture
def module_args():
    return {
        "api_url": "https://api.example.com",
        "api_token": "test-token",
        "resource_type": "users",
        "state": "present",
        "data": {"name": "Test User"}
    }


def test_create_resource(module_args):
    with patch("api_resource.AnsibleModule") as mock_module:
        mock_instance = MagicMock()
        mock_instance.params = module_args
        mock_instance.check_mode = False
        mock_module.return_value = mock_instance

        with patch("api_resource.fetch_url") as mock_fetch:
            mock_response = MagicMock()
            mock_response.read.return_value = json.dumps(
                {"id": "123", "name": "Test User"}
            ).encode()
            mock_fetch.return_value = (mock_response, {"status": 201})

            main()

            mock_instance.exit_json.assert_called_once()
            call_args = mock_instance.exit_json.call_args
            assert call_args[1]["changed"] == True
```

### Running Tests

```bash
# Run module directly for debugging
python library/api_resource.py /tmp/args.json

# Run pytest
pytest tests/ -v
```

---

## Collection Distribution

### Collection Structure

```
my_namespace/
  my_collection/
    galaxy.yml
    README.md
    plugins/
      modules/
        api_resource.py
      filter/
        my_filters.py
      lookup/
        vault_secret.py
    roles/
```

### galaxy.yml

```yaml
namespace: my_namespace
name: my_collection
version: 1.0.0
readme: README.md
authors:
  - Your Name <you@example.com>
description: Custom Ansible collection
dependencies: {}
tags:
  - api
  - automation
```

### Build and Publish

```bash
# Build collection
ansible-galaxy collection build

# Publish to Galaxy
ansible-galaxy collection publish \
  my_namespace-my_collection-1.0.0.tar.gz \
  --api-key YOUR_KEY

# Install from Galaxy
ansible-galaxy collection install my_namespace.my_collection
```

---

## Plugin Quick Reference

| Plugin Type | Location | Purpose | Example |
|-------------|----------|---------|---------|
| Modules | library/ | Task actions | api_resource |
| Filters | filter_plugins/ | Transform data | to_slug |
| Lookups | lookup_plugins/ | Fetch external data | vault_secret |
| Callbacks | callback_plugins/ | Custom output | json_logger |
| Connection | connection_plugins/ | Transport | custom_ssh |

---

## Best Practices

### DO

- Use AnsibleModule for argument parsing
- Support check_mode for dry-run
- Return changed=True only when state changes
- Use no_log=True for sensitive parameters
- Include DOCUMENTATION, EXAMPLES, RETURN

### DON'T

- Print to stdout (use module.exit_json)
- Ignore exceptions (handle gracefully)
- Hardcode credentials
- Skip idempotency checks

---

## Praktisk Övning

Bygg en custom module som hanterar en extern API:

1. Skapa `library/my_api.py` med argument_spec
2. Implementera CRUD operations
3. Lägg till filter i `filter_plugins/`
4. Skriv tester i `tests/`
5. Paketera som collection

---

## Sammanfattning

| Concept | Implementation |
|---------|----------------|
| Module | AnsibleModule + main() |
| Filter | FilterModule.filters() dict |
| Lookup | LookupModule.run() method |
| Testing | pytest + mock AnsibleModule |
| Distribution | ansible-galaxy collection |

---

## Nästa Steg

Custom plugins mastered. Nästa block: **Production Ansible** — testing, CI/CD, best practices.
""",
}

ANSIBLE_BLOCK_4 = [
    NODE_13_CORE_MODULES,
    NODE_14_CLOUD_MODULES,
    NODE_15_CONTAINER_MODULES,
    NODE_16_CUSTOM_MODULES,
]
