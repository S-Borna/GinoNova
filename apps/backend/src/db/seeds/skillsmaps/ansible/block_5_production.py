# =============================================================================
# BLOCK 5: PRODUCTION & BEST PRACTICES (Noder 17-20)
# =============================================================================

NODE_17_TESTING_ANSIBLE = {
    "node_id": 17,
    "title": "Testing Ansible",
    "slug": "testing-ansible",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [9],
    "content": '''
# Testing Ansible

Testa dina playbooks och roles.

## Syntax Check

```bash
# Validate syntax
ansible-playbook site.yml --syntax-check

# Lint with ansible-lint
pip install ansible-lint
ansible-lint site.yml
ansible-lint roles/
```

## Check Mode (Dry Run)

```bash
# Simulate changes
ansible-playbook site.yml --check

# With diff
ansible-playbook site.yml --check --diff
```

## Molecule

```bash
# Installera
pip install molecule molecule-docker

# Skapa test för role
cd roles/nginx
molecule init scenario -d docker

# Struktur
roles/nginx/
├── molecule/
│   └── default/
│       ├── molecule.yml
│       ├── converge.yml
│       └── verify.yml
```

```yaml
# molecule/default/molecule.yml
dependency:
  name: galaxy
driver:
  name: docker
platforms:
  - name: ubuntu
    image: ubuntu:22.04
    pre_build_image: true
provisioner:
  name: ansible
verifier:
  name: ansible
```

```yaml
# molecule/default/converge.yml
---
- name: Converge
  hosts: all
  become: true
  roles:
    - role: nginx
```

```yaml
# molecule/default/verify.yml
---
- name: Verify
  hosts: all
  tasks:
    - name: Check nginx is installed
      command: nginx -v
      register: nginx_version
      changed_when: false

    - name: Check nginx is running
      service:
        name: nginx
        state: started
      check_mode: true
      register: nginx_service

    - name: Assert nginx is running
      assert:
        that:
          - nginx_service is not changed
```

## Molecule Commands

```bash
# Full test cycle
molecule test

# Steg för steg
molecule create     # Skapa containers
molecule converge   # Kör playbook
molecule verify     # Kör tester
molecule destroy    # Städa upp

# Login för debug
molecule login
```

## Assert i Playbooks

```yaml
- name: Verify application
  hosts: webservers
  tasks:
    - name: Check HTTP response
      uri:
        url: http://localhost
        status_code: 200
      register: http_result

    - name: Assert response
      assert:
        that:
          - http_result.status == 200
          - "'Welcome' in http_result.content"
        fail_msg: "Application not responding correctly"
        success_msg: "Application is healthy"
```

## Testinfra (Python)

```python
# tests/test_nginx.py
def test_nginx_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

def test_nginx_listening(host):
    socket = host.socket("tcp://0.0.0.0:80")
    assert socket.is_listening
```

| Tool | Syfte |
|------|-------|
| --syntax-check | YAML syntax |
| ansible-lint | Best practices |
| --check | Dry run |
| Molecule | Full testing |
| Testinfra | Python assertions |

**Nästa steg:** Node 18 - CI/CD Integration
''',
}

NODE_18_CICD_ANSIBLE = {
    "node_id": 18,
    "title": "CI/CD Integration",
    "slug": "cicd-ansible",
    "estimated_minutes": 55,
    "xp_reward": 155,
    "prerequisites": [17],
    "content": '''
# CI/CD med Ansible

Automatisera Ansible i pipelines.

## GitHub Actions

```yaml
# .github/workflows/ansible.yml
name: Ansible CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install ansible ansible-lint

      - name: Run ansible-lint
        run: ansible-lint

  molecule:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install molecule molecule-docker ansible

      - name: Run Molecule tests
        run: molecule test
        working-directory: roles/nginx

  deploy:
    needs: [lint, molecule]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5

      - name: Install Ansible
        run: pip install ansible

      - name: Run playbook
        run: |
          ansible-playbook -i inventory/prod site.yml
        env:
          ANSIBLE_VAULT_PASSWORD: ${{ secrets.VAULT_PASSWORD }}
          ANSIBLE_HOST_KEY_CHECKING: 'false'
```

## GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - lint
  - test
  - deploy

lint:
  stage: lint
  image: python:3.11
  script:
    - pip install ansible-lint
    - ansible-lint

molecule:
  stage: test
  image: docker:latest
  services:
    - docker:dind
  script:
    - pip install molecule molecule-docker ansible
    - molecule test
  only:
    - merge_requests

deploy:
  stage: deploy
  image: python:3.11
  script:
    - pip install ansible
    - ansible-playbook -i inventory/prod site.yml
  only:
    - main
  when: manual
```

## Ansible Tower / AWX

```yaml
# Job Template i AWX
# - Inventory: Production
# - Playbook: site.yml
# - Credentials: SSH Key, Vault Password
# - Extra Variables: env=production
```

## Semaphore

```bash
# Open source Ansible UI
docker run -d -p 3000:3000 \
  -v /opt/semaphore:/etc/semaphore \
  semaphoreui/semaphore:latest
```

## Dynamic Inventory i CI

```yaml
# aws_ec2.yml för CI
plugin: amazon.aws.aws_ec2
regions:
  - eu-north-1
filters:
  tag:Environment: "{{ lookup('env', 'DEPLOY_ENV') }}"
```

```yaml
# GitHub Actions med AWS
- name: Configure AWS
  uses: aws-actions/configure-aws-credentials@v4
  with:
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: eu-north-1

- name: Run playbook
  run: |
    ansible-playbook -i aws_ec2.yml site.yml
```

| Platform | Verktyg |
|----------|---------|
| GitHub | GitHub Actions |
| GitLab | GitLab CI |
| Jenkins | Ansible Plugin |
| Self-hosted | AWX/Semaphore |

**Nästa steg:** Node 19 - Best Practices
''',
}

NODE_19_BEST_PRACTICES = {
    "node_id": 19,
    "title": "Ansible Best Practices",
    "slug": "best-practices",
    "estimated_minutes": 55,
    "xp_reward": 160,
    "prerequisites": [9, 12],
    "content": '''
# Ansible Best Practices

Produktion-redo Ansible.

## Directory Layout

```
ansible/
├── ansible.cfg
├── inventory/
│   ├── production/
│   │   ├── hosts.yml
│   │   ├── group_vars/
│   │   │   ├── all.yml
│   │   │   └── webservers.yml
│   │   └── host_vars/
│   └── staging/
├── playbooks/
│   ├── site.yml
│   ├── webservers.yml
│   └── databases.yml
├── roles/
│   ├── common/
│   ├── nginx/
│   └── postgres/
├── group_vars/
│   └── all/
│       ├── vars.yml
│       └── vault.yml
└── requirements.yml
```

## ansible.cfg

```ini
[defaults]
inventory = inventory/production
roles_path = roles
host_key_checking = False
retry_files_enabled = False
gathering = smart
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_facts
fact_caching_timeout = 86400

[privilege_escalation]
become = True
become_method = sudo
become_user = root

[ssh_connection]
pipelining = True
control_path = /tmp/ansible-%%h-%%p-%%r
```

## Naming Conventions

```yaml
# Roles: lowercase, underscore
roles/
  web_server/
  db_backup/

# Variables: lowercase, underscore
http_port: 80
db_admin_user: admin

# Tasks: Descriptive, start with verb
- name: Install nginx packages
- name: Configure nginx main config
- name: Start nginx service
```

## Idempotency

```yaml
# ✅ Bra - idempotent
- name: Ensure nginx is installed
  apt:
    name: nginx
    state: present

# ❌ Dåligt - ej idempotent
- name: Install nginx
  command: apt-get install nginx
```

## Tag Strategy

```yaml
# Konsekvent taggning
tasks:
  - name: Install packages
    apt:
      name: nginx
    tags:
      - install
      - packages
      - nginx

  - name: Configure nginx
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    tags:
      - configure
      - nginx
```

```bash
# Kör specifika tags
ansible-playbook site.yml --tags "configure"
ansible-playbook site.yml --skip-tags "install"
```

## Variable Naming

```yaml
# Prefix med role/component
nginx_port: 80
nginx_worker_processes: auto
postgres_version: 14
postgres_max_connections: 100

# Vault-prefix för secrets
vault_db_password: secret123
vault_api_key: abc123
```

## Handler Best Practices

```yaml
# Validera innan restart
handlers:
  - name: Validate nginx config
    command: nginx -t
    changed_when: false
    listen: Restart nginx

  - name: Restart nginx service
    service:
      name: nginx
      state: restarted
    listen: Restart nginx
```

## Checklist

| Practice | Implementation |
|----------|----------------|
| Version control | Git för allt |
| Vault för secrets | Aldrig plaintext |
| Idempotent tasks | Använd modules |
| Descriptive names | Verb + objekt |
| Test med Molecule | Innan merge |
| Lint med ansible-lint | I CI |
| Tags | För selektiv körning |
| Group/host vars | Separera data |

**Nästa steg:** Node 20 - Real-World Patterns
''',
}

NODE_20_REALWORLD_PATTERNS = {
    "node_id": 20,
    "title": "Real-World Patterns",
    "slug": "realworld-patterns",
    "estimated_minutes": 60,
    "xp_reward": 175,
    "prerequisites": [19],
    "content": '''
# Real-World Ansible Patterns

Production-proven patterns.

## Rolling Deployments

```yaml
- name: Rolling deployment
  hosts: webservers
  serial: 2  # 2 hosts at a time
  max_fail_percentage: 25

  pre_tasks:
    - name: Remove from load balancer
      uri:
        url: "http://lb.example.com/api/remove/{{ inventory_hostname }}"
        method: POST

  roles:
    - role: deploy_app

  post_tasks:
    - name: Verify app health
      uri:
        url: "http://{{ inventory_hostname }}:8080/health"
        status_code: 200
      retries: 10
      delay: 5

    - name: Add back to load balancer
      uri:
        url: "http://lb.example.com/api/add/{{ inventory_hostname }}"
        method: POST
```

## Blue/Green Deployment

```yaml
- name: Blue/Green deployment
  hosts: localhost
  vars:
    active_color: "{{ lookup('file', '/opt/deploy/active_color') }}"
    deploy_color: "{{ 'green' if active_color == 'blue' else 'blue' }}"

  tasks:
    - name: Deploy to inactive environment
      include_role:
        name: deploy_app
      vars:
        target_hosts: "{{ groups[deploy_color] }}"

    - name: Switch traffic
      template:
        src: nginx_upstream.j2
        dest: /etc/nginx/upstream.conf
      vars:
        active_servers: "{{ groups[deploy_color] }}"
      delegate_to: load_balancer

    - name: Update active color
      copy:
        content: "{{ deploy_color }}"
        dest: /opt/deploy/active_color
```

## Canary Releases

```yaml
- name: Canary deployment
  hosts: webservers
  tasks:
    - name: Deploy to canary (10%)
      include_role:
        name: deploy_app
      when: "'canary' in group_names"

    - name: Wait for monitoring
      pause:
        minutes: 10
      when: "'canary' in group_names"

    - name: Check metrics
      uri:
        url: "http://prometheus/api/v1/query?query=error_rate"
      register: metrics
      failed_when: metrics.json.data.result[0].value[1] | float > 0.01

    - name: Deploy to remaining
      include_role:
        name: deploy_app
      when: "'canary' not in group_names"
```

## Environment Promotion

```yaml
# deploy.yml
- name: Deploy to environment
  hosts: "{{ env }}_servers"
  vars_files:
    - "vars/{{ env }}.yml"
    - "vars/{{ env }}_vault.yml"
  roles:
    - common
    - app
```

```bash
# Usage
ansible-playbook deploy.yml -e env=staging
ansible-playbook deploy.yml -e env=production
```

## Database Migrations

```yaml
- name: Database migration
  hosts: db_primary
  tasks:
    - name: Backup database
      command: pg_dump mydb > /backup/pre_migration.sql

    - name: Run migrations
      command: flask db upgrade
      args:
        chdir: /opt/app
      register: migration
      notify: Notify on failure

    - name: Verify migration
      command: flask db current
      register: db_version

  handlers:
    - name: Notify on failure
      slack:
        token: "{{ slack_token }}"
        channel: '#deployments'
        msg: "Migration failed: {{ migration.stderr }}"
      when: migration.failed
```

## Secrets Rotation

```yaml
- name: Rotate secrets
  hosts: app_servers
  vars:
    new_password: "{{ lookup('password', '/dev/null length=32') }}"

  tasks:
    - name: Update database password
      postgresql_user:
        name: app_user
        password: "{{ new_password }}"
      delegate_to: db_primary

    - name: Update app config
      template:
        src: app.conf.j2
        dest: /etc/app/config
      notify: Restart app

    - name: Update Vault
      community.hashi_vault.vault_write:
        path: secret/app/db_password
        data:
          value: "{{ new_password }}"
```

## Pattern Summary

| Pattern | Use Case |
|---------|----------|
| Rolling | Zero-downtime updates |
| Blue/Green | Instant rollback |
| Canary | Risk mitigation |
| Promotion | Environment progression |
| Migration | Database changes |

**🎉 Grattis! Du har slutfört Ansible Mastery SkillsMap!**

**Nästa steg:** Terraform SkillsMap → Infrastructure as Code
''',
}

ANSIBLE_BLOCK_5 = [
    NODE_17_TESTING_ANSIBLE,
    NODE_18_CICD_ANSIBLE,
    NODE_19_BEST_PRACTICES,
    NODE_20_REALWORLD_PATTERNS,
]
