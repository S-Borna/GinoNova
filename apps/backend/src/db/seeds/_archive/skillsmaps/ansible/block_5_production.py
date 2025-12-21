# =============================================================================
# BLOCK 5: PRODUCTION & BEST PRACTICES (Noder 17-20)
# =============================================================================

NODE_17_TESTING_ANSIBLE = {
    "node_id": 17,
    "title": "Testing Ansible",
    "slug": "testing-ansible",
    "estimated_minutes": 60,
    "xp_reward": 155,
    "prerequisites": [9],
    "content": r'''
# Testing Ansible

## Varför detta är kritiskt

> "Untested automation = automated disasters. Molecule, ansible-lint, och check mode säkerställer att dina playbooks fungerar INNAN de når produktion."

**Testing pyramid:**
- **Linting** — Statisk kodanalys
- **Check mode** — Dry run simulation
- **Molecule** — Full integration testing
- **Testinfra** — Python assertions

---

## Testing Pyramid

```
+-------------------------------------------------------------------------+
|                    ANSIBLE TESTING PYRAMID                              |
+-------------------------------------------------------------------------+
|                                                                         |
|                          +---------+                                    |
|                          | E2E     |  <- Full stack testing              |
|                         ╱| Tests   |╲   (Production-like)               |
|                        ╱ +---------+ ╲                                  |
|                       ╱               ╲                                 |
|                      ╱  +-----------+  ╲                                |
|                     ╱   | Molecule  |   ╲ <- Integration tests           |
|                    ╱    | + Verify  |    ╲  (Containers)                |
|                   ╱     +-----------+     ╲                             |
|                  ╱                         ╲                            |
|                 ╱    +-----------------+    ╲                           |
|                ╱     | Check Mode      |     ╲ <- Dry run                |
|               ╱      | (--check --diff)|      ╲ (Simulation)            |
|              ╱       +-----------------+       ╲                        |
|             ╱                                   ╲                       |
|            ╱      +-----------------------+      ╲                      |
|           ╱       | Lint + Syntax Check   |       ╲ <- Static analysis   |
|          ╱        | (ansible-lint, yamllint)       ╲ (Fast feedback)    |
|         ╱---------+-----------------------+---------╲                   |
|                                                                         |
|  TESTING STAGES:                                                        |
|  ---------------                                                        |
|  1. Developer runs lint locally (pre-commit)                            |
|  2. CI runs full test suite on PR                                       |
|  3. Check mode validates against staging                                |
|  4. Molecule tests run in containers                                    |
|  5. E2E tests validate full deployment                                  |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Syntax Check & Linting

### Basic Syntax Validation

```bash
# Check YAML syntax
ansible-playbook site.yml --syntax-check

# Check all playbooks
find . -name "*.yml" -exec ansible-playbook {} --syntax-check \;

# Validate with verbose
ansible-playbook site.yml --syntax-check -v
```

### ansible-lint

```bash
# Install
pip install ansible-lint yamllint

# Run linter
ansible-lint site.yml
ansible-lint roles/
ansible-lint .  # Current directory

# Specific rules
ansible-lint --list-rules

# Skip rules
ansible-lint -x no-changed-when,command-instead-of-shell
```

### ansible-lint Configuration

```yaml
# .ansible-lint
---
profile: production

warn_list:
  - experimental
  - no-changed-when

skip_list:
  - meta-no-info
  - role-name

exclude_paths:
  - .cache/
  - .git/
  - tests/output/

mock_modules:
  - custom_module

mock_roles:
  - geerlingguy.docker

enable_list:
  - no-log-password
  - no-same-owner
```

### yamllint Configuration

```yaml
# .yamllint
---
extends: default

rules:
  line-length:
    max: 120
    level: warning
  truthy:
    allowed-values: ['true', 'false', 'yes', 'no']
  comments:
    min-spaces-from-content: 1
  indentation:
    spaces: 2
    indent-sequences: consistent
```

### Pre-commit Integration

```yaml
# .pre-commit-config.yaml
---
repos:
  - repo: https://github.com/ansible/ansible-lint
    rev: v6.17.0
    hooks:
      - id: ansible-lint
        args: []
        additional_dependencies:
          - ansible-core>=2.14

  - repo: https://github.com/adrienverge/yamllint
    rev: v1.32.0
    hooks:
      - id: yamllint
        args: [-c=.yamllint]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
        args: [--allow-multiple-documents]
```

```bash
# Install pre-commit
pip install pre-commit
pre-commit install

# Run manually
pre-commit run --all-files
```

---

## Check Mode (Dry Run)

### Basic Usage

```bash
# Simulate changes
ansible-playbook site.yml --check

# With diff to see changes
ansible-playbook site.yml --check --diff

# Limit to specific hosts
ansible-playbook site.yml --check --limit webservers

# Combine with verbose
ansible-playbook site.yml --check --diff -v
```

### Check Mode in Tasks

```yaml
---
- name: Configuration with check mode handling
  hosts: webservers
  tasks:
    # Always runs, even in check mode
    - name: Gather system info
      command: uname -a
      check_mode: false
      register: system_info
      changed_when: false

    # Skipped in check mode
    - name: Download large file
      get_url:
        url: https://example.com/big-file.tar.gz
        dest: /tmp/big-file.tar.gz
      when: not ansible_check_mode

    # Proper check mode support
    - name: Deploy configuration
      template:
        src: app.conf.j2
        dest: /etc/app/app.conf
      check_mode: true
      register: config_check
      diff: true

    - name: Show what would change
      debug:
        var: config_check.diff
      when: config_check.changed
```

### Register Check Results

```yaml
- name: Validate before apply
  hosts: all
  tasks:
    - name: Check nginx config
      command: nginx -t
      check_mode: false  # Always run
      changed_when: false
      register: nginx_check
      failed_when: nginx_check.rc != 0

    - name: Dry run database migration
      command: flask db upgrade --sql
      args:
        chdir: /opt/app
      check_mode: false
      register: migration_sql
      changed_when: false

    - name: Show migration SQL
      debug:
        var: migration_sql.stdout_lines
```

---

## Molecule Testing

### Installation

```bash
# Core + Docker driver
pip install molecule molecule-docker

# Additional drivers
pip install molecule-vagrant
pip install molecule-podman
pip install molecule-ec2
```

### Initialize Molecule

```bash
# Add to existing role
cd roles/nginx
molecule init scenario -d docker

# Created structure:
roles/nginx/
+-- defaults/
+-- handlers/
+-- tasks/
+-- templates/
+-- vars/
+-- molecule/
    +-- default/
        +-- molecule.yml
        +-- converge.yml
        +-- verify.yml
        +-- prepare.yml
```

### molecule.yml Configuration

```yaml
# molecule/default/molecule.yml
---
dependency:
  name: galaxy
  options:
    requirements-file: requirements.yml

driver:
  name: docker

platforms:
  - name: ubuntu-22
    image: ubuntu:22.04
    pre_build_image: true
    privileged: true
    command: /lib/systemd/systemd
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:rw
    cgroupns_mode: host

  - name: debian-12
    image: debian:12
    pre_build_image: true
    privileged: true
    command: /lib/systemd/systemd

  - name: rocky-9
    image: rockylinux:9
    pre_build_image: true
    privileged: true
    command: /usr/sbin/init

provisioner:
  name: ansible
  playbooks:
    prepare: prepare.yml
    converge: converge.yml
    verify: verify.yml
  inventory:
    group_vars:
      all:
        nginx_worker_processes: 2
        nginx_port: 80
  config_options:
    defaults:
      gathering: smart
      fact_caching: jsonfile
      fact_caching_connection: /tmp/molecule_facts

verifier:
  name: ansible

lint: |
  set -e
  yamllint .
  ansible-lint

scenario:
  name: default
  test_sequence:
    - dependency
    - lint
    - cleanup
    - destroy
    - syntax
    - create
    - prepare
    - converge
    - idempotence
    - side_effect
    - verify
    - cleanup
    - destroy
```

### Converge Playbook

```yaml
# molecule/default/converge.yml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  pre_tasks:
    - name: Update apt cache (Debian)
      apt:
        update_cache: true
        cache_valid_time: 3600
      when: ansible_os_family == 'Debian'

  roles:
    - role: nginx
      vars:
        nginx_worker_processes: auto
        nginx_port: 80
        nginx_sites:
          - name: default
            server_name: localhost
            root: /var/www/html
```

### Verify Playbook

```yaml
# molecule/default/verify.yml
---
- name: Verify
  hosts: all
  gather_facts: false
  become: true

  tasks:
    - name: Check nginx is installed
      ansible.builtin.package:
        name: nginx
        state: present
      check_mode: true
      register: nginx_installed
      failed_when: nginx_installed.changed

    - name: Get nginx version
      ansible.builtin.command: nginx -v
      register: nginx_version
      changed_when: false
      failed_when: nginx_version.rc != 0

    - name: Check nginx is running
      ansible.builtin.service:
        name: nginx
        state: started
      check_mode: true
      register: nginx_running
      failed_when: nginx_running.changed

    - name: Check nginx is enabled
      ansible.builtin.service:
        name: nginx
        enabled: true
      check_mode: true
      register: nginx_enabled
      failed_when: nginx_enabled.changed

    - name: Check nginx is listening on port 80
      ansible.builtin.wait_for:
        port: 80
        timeout: 5
      register: nginx_listening

    - name: Test HTTP response
      ansible.builtin.uri:
        url: http://localhost
        return_content: true
        status_code: 200
      register: http_response

    - name: Verify response content
      ansible.builtin.assert:
        that:
          - "'Welcome' in http_response.content or 'nginx' in http_response.content"
        fail_msg: "Unexpected HTTP response"
        success_msg: "HTTP response verified"

    - name: Check config file exists
      ansible.builtin.stat:
        path: /etc/nginx/nginx.conf
      register: nginx_conf
      failed_when: not nginx_conf.stat.exists

    - name: Validate nginx configuration
      ansible.builtin.command: nginx -t
      register: nginx_valid
      changed_when: false
      failed_when: nginx_valid.rc != 0

    - name: Print test summary
      ansible.builtin.debug:
        msg:
          - "✅ Nginx version: {{ nginx_version.stderr }}"
          - "✅ Nginx is running and enabled"
          - "✅ Listening on port 80"
          - "✅ Configuration is valid"
```

### Molecule Commands

```bash
# Full test cycle
molecule test

# Step-by-step debugging
molecule create       # Create containers
molecule list         # List instances
molecule prepare      # Run prepare playbook
molecule converge     # Run converge playbook
molecule idempotence  # Run converge twice (check idempotence)
molecule verify       # Run verify playbook
molecule login        # SSH into container
molecule destroy      # Clean up

# Run on specific platform
molecule converge -- --limit ubuntu-22

# Debug mode
molecule --debug test

# Keep containers after failure
molecule test --destroy never
```

---

## Testinfra (Python Testing)

### Setup

```bash
pip install testinfra pytest
```

### Test File

```python
# molecule/default/tests/test_nginx.py
import pytest


def test_nginx_package_installed(host):
    """Test nginx package is installed"""
    nginx = host.package("nginx")
    assert nginx.is_installed


def test_nginx_service_running(host):
    """Test nginx service is running and enabled"""
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled


def test_nginx_listening_http(host):
    """Test nginx is listening on port 80"""
    socket = host.socket("tcp://0.0.0.0:80")
    assert socket.is_listening


def test_nginx_config_valid(host):
    """Test nginx configuration is valid"""
    cmd = host.run("nginx -t")
    assert cmd.rc == 0


def test_nginx_config_file(host):
    """Test nginx config file exists with correct permissions"""
    config = host.file("/etc/nginx/nginx.conf")
    assert config.exists
    assert config.is_file
    assert config.user == "root"
    assert config.group == "root"
    assert config.mode == 0o644


def test_nginx_http_response(host):
    """Test nginx returns HTTP 200"""
    cmd = host.run("curl -s -o /dev/null -w '%{http_code}' http://localhost")
    assert cmd.stdout == "200"


@pytest.mark.parametrize("directory", [
    "/var/www/html",
    "/var/log/nginx",
    "/etc/nginx/conf.d",
])
def test_nginx_directories(host, directory):
    """Test nginx directories exist"""
    dir_obj = host.file(directory)
    assert dir_obj.exists
    assert dir_obj.is_directory


def test_nginx_worker_processes(host):
    """Test nginx has correct number of workers"""
    cmd = host.run("grep -c 'nginx: worker' /proc/*/status 2>/dev/null | wc -l")
    # Should have at least 1 worker
    assert int(cmd.stdout.strip()) >= 1
```

### Run Testinfra

```bash
# Via Molecule
molecule verify

# Directly with pytest
pytest molecule/default/tests/ -v
```

---

## Assert Module

### Inline Assertions

```yaml
---
- name: Validate deployment
  hosts: webservers
  tasks:
    - name: Check application health
      uri:
        url: http://localhost:8080/health
        return_content: true
      register: health_check

    - name: Assert application is healthy
      assert:
        that:
          - health_check.status == 200
          - health_check.json.status == 'healthy'
          - health_check.json.database == 'connected'
        fail_msg: "Application health check failed!"
        success_msg: "Application is healthy"

    - name: Check disk space
      shell: df -h / | tail -1 | awk '{print $5}' | tr -d '%'
      register: disk_usage
      changed_when: false

    - name: Assert sufficient disk space
      assert:
        that:
          - disk_usage.stdout | int < 85
        fail_msg: "Disk usage is {{ disk_usage.stdout }}% - too high!"
        success_msg: "Disk usage OK: {{ disk_usage.stdout }}%"
```

---

## Testing Summary

| Tool | Purpose | Speed |
|------|---------|-------|
| `--syntax-check` | YAML syntax | Fast |
| `ansible-lint` | Best practices | Fast |
| `--check --diff` | Dry run | Medium |
| `Molecule` | Full integration | Slow |
| `Testinfra` | Python assertions | Medium |

---

## Nästa Steg

Testing bemästrat. Nästa: **CI/CD Integration** — automatisera Ansible i pipelines.
''',
}

NODE_18_CICD_ANSIBLE = {
    "node_id": 18,
    "title": "CI/CD Integration",
    "slug": "cicd-ansible",
    "estimated_minutes": 60,
    "xp_reward": 160,
    "prerequisites": [17],
    "content": r'''
# CI/CD med Ansible

## Varför detta är kritiskt

> "Manuella Ansible-körningar = risk för mänskliga misstag. CI/CD automatiserar lint, test, och deployment med full audit trail."

**CI/CD Benefits:**
- Automatiserad testing före deploy
- Reproducerbara deployments
- Audit trail för alla ändringar
- Rollback-möjligheter
- Separation of duties

---

## CI/CD Pipeline Architecture

```
+-------------------------------------------------------------------------+
|                    ANSIBLE CI/CD PIPELINE                               |
+-------------------------------------------------------------------------+
|                                                                         |
|  GIT REPOSITORY                                                         |
|  --------------                                                         |
|       |                                                                 |
|       ▼                                                                 |
|  +-----------------------------------------------------------------+    |
|  |                    CI PIPELINE (PR/Merge)                       |    |
|  +---------+------------+-------------+------------+--------------+    |
|  |  Lint   |  Syntax    |  Unit Tests |  Molecule  |  Security    |    |
|  |         |  Check     |  (pytest)   |  Tests     |  Scan        |    |
|  +----+----+-----+------+------+------+-----+------+------+-------+    |
|       |          |             |            |             |            |
|       +----------+-------------+------------+-------------+            |
|                              |                                          |
|                              ▼ (if all pass)                            |
|  +-----------------------------------------------------------------+    |
|  |                    CD PIPELINE (main branch)                    |    |
|  +-------------+--------------+----------------+------------------+    |
|  |   Deploy    |   Deploy     |   Deploy       |   Smoke Tests    |    |
|  |   Staging   |   Canary     |   Production   |   + Verify       |    |
|  |             |   (10%)      |   (Rolling)    |                  |    |
|  +------+------+-------+------+--------+-------+---------+--------+    |
|         |              |               |                 |             |
|         ▼              ▼               ▼                 ▼             |
|  +-----------+  +-----------+  +---------------+  +--------------+     |
|  | Staging   |  |  Canary   |  |  Production   |  |  Monitoring  |     |
|  | Servers   |  |  Servers  |  |  Servers      |  |  Dashboard   |     |
|  +-----------+  +-----------+  +---------------+  +--------------+     |
|                                                                         |
|  SECRETS MANAGEMENT:                                                    |
|  +-- CI/CD Variables (encrypted)                                        |
|  +-- Vault integration                                                  |
|  +-- Ansible Vault passwords                                            |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## GitHub Actions

### Complete CI/CD Workflow

```yaml
# .github/workflows/ansible.yml
---
name: Ansible CI/CD

on:
  push:
    branches: [main, develop]
    paths:
      - 'ansible/**'
      - '.github/workflows/ansible.yml'
  pull_request:
    branches: [main]
    paths:
      - 'ansible/**'

env:
  ANSIBLE_FORCE_COLOR: true
  ANSIBLE_HOST_KEY_CHECKING: 'false'
  PY_COLORS: '1'

jobs:
  lint:
    name: Lint
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          pip install ansible-core ansible-lint yamllint

      - name: Run yamllint
        run: yamllint -c .yamllint ansible/
        continue-on-error: false

      - name: Run ansible-lint
        run: ansible-lint ansible/
        continue-on-error: false

      - name: Syntax check playbooks
        run: |
          for playbook in ansible/playbooks/*.yml; do
            ansible-playbook "$playbook" --syntax-check
          done

  molecule:
    name: Molecule Tests
    runs-on: ubuntu-latest
    needs: lint
    strategy:
      fail-fast: false
      matrix:
        role:
          - nginx
          - postgresql
          - app
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install ansible-core molecule molecule-docker pytest-testinfra

      - name: Run Molecule
        run: molecule test
        working-directory: ansible/roles/${{ matrix.role }}
        env:
          MOLECULE_DISTRO: ubuntu2204

  security-scan:
    name: Security Scan
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'config'
          scan-ref: 'ansible/'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'

  deploy-staging:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    needs: [lint, molecule]
    if: github.ref == 'refs/heads/develop'
    environment:
      name: staging
      url: https://staging.example.com
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Ansible
        run: |
          pip install ansible-core boto3
          ansible-galaxy collection install -r ansible/requirements.yml

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-north-1

      - name: Create vault password file
        run: |
          echo "${{ secrets.ANSIBLE_VAULT_PASSWORD }}" > .vault_pass
          chmod 600 .vault_pass

      - name: Run playbook
        run: |
          ansible-playbook ansible/playbooks/site.yml \
            -i ansible/inventory/staging/aws_ec2.yml \
            --vault-password-file .vault_pass \
            -e "env=staging version=${{ github.sha }}"

      - name: Verify deployment
        run: |
          curl -f https://staging.example.com/health || exit 1

      - name: Cleanup
        if: always()
        run: rm -f .vault_pass

  deploy-production:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: [lint, molecule, security-scan]
    if: github.ref == 'refs/heads/main'
    environment:
      name: production
      url: https://example.com
    concurrency:
      group: production-deploy
      cancel-in-progress: false
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Ansible
        run: |
          pip install ansible-core boto3
          ansible-galaxy collection install -r ansible/requirements.yml

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-north-1

      - name: Create vault password file
        run: |
          echo "${{ secrets.ANSIBLE_VAULT_PASSWORD }}" > .vault_pass
          chmod 600 .vault_pass

      - name: Run playbook (Rolling)
        run: |
          ansible-playbook ansible/playbooks/site.yml \
            -i ansible/inventory/production/aws_ec2.yml \
            --vault-password-file .vault_pass \
            -e "env=production version=${{ github.sha }}" \
            -e "serial=2"

      - name: Smoke tests
        run: |
          ./scripts/smoke-tests.sh production

      - name: Notify success
        if: success()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "✅ Production deployment successful",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Production Deploy*\nVersion: `${{ github.sha }}`\nBy: ${{ github.actor }}"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}

      - name: Cleanup
        if: always()
        run: rm -f .vault_pass
```

---

## GitLab CI

### Complete Pipeline

```yaml
# .gitlab-ci.yml
---
stages:
  - lint
  - test
  - deploy-staging
  - deploy-production

variables:
  ANSIBLE_FORCE_COLOR: "true"
  ANSIBLE_HOST_KEY_CHECKING: "false"
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

cache:
  paths:
    - .cache/pip

.ansible-base:
  image: python:3.11
  before_script:
    - pip install ansible-core ansible-lint molecule molecule-docker
    - ansible-galaxy collection install -r ansible/requirements.yml

lint:
  stage: lint
  extends: .ansible-base
  script:
    - yamllint ansible/
    - ansible-lint ansible/
    - |
      for playbook in ansible/playbooks/*.yml; do
        ansible-playbook "$playbook" --syntax-check
      done
  rules:
    - changes:
        - ansible/**/*

molecule:
  stage: test
  extends: .ansible-base
  services:
    - docker:24-dind
  variables:
    DOCKER_HOST: tcp://docker:2375
  parallel:
    matrix:
      - ROLE: [nginx, postgresql, app]
  script:
    - cd ansible/roles/$ROLE
    - molecule test
  rules:
    - changes:
        - ansible/roles/**/*

deploy-staging:
  stage: deploy-staging
  extends: .ansible-base
  script:
    - echo "$VAULT_PASSWORD" > .vault_pass
    - |
      ansible-playbook ansible/playbooks/site.yml \
        -i ansible/inventory/staging \
        --vault-password-file .vault_pass \
        -e "env=staging version=$CI_COMMIT_SHA"
    - rm -f .vault_pass
  environment:
    name: staging
    url: https://staging.example.com
  rules:
    - if: $CI_COMMIT_BRANCH == "develop"

deploy-production:
  stage: deploy-production
  extends: .ansible-base
  script:
    - echo "$VAULT_PASSWORD" > .vault_pass
    - |
      ansible-playbook ansible/playbooks/site.yml \
        -i ansible/inventory/production \
        --vault-password-file .vault_pass \
        -e "env=production version=$CI_COMMIT_SHA"
    - rm -f .vault_pass
  environment:
    name: production
    url: https://example.com
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
      when: manual
  allow_failure: false
```

---

## Ansible Tower / AWX

### Job Templates

```yaml
# AWX Job Template Configuration
name: Deploy Application
job_type: run
inventory: Production Inventory
project: My Ansible Project
playbook: playbooks/deploy.yml
credentials:
  - SSH Private Key
  - Vault Password
extra_vars:
  env: production
limit: webservers
verbosity: 1
job_tags: deploy
skip_tags: backup
become_enabled: true
concurrent_jobs_enabled: false
```

### Workflow Templates

```yaml
# AWX Workflow (CI/CD Pipeline)
name: Production Deployment Pipeline

nodes:
  - name: Lint and Syntax Check
    job_template: Lint Playbooks
    success_nodes:
      - Run Molecule Tests
    failure_nodes:
      - Notify Failure

  - name: Run Molecule Tests
    job_template: Molecule Tests
    success_nodes:
      - Deploy to Staging
    failure_nodes:
      - Notify Failure

  - name: Deploy to Staging
    job_template: Deploy Staging
    success_nodes:
      - Staging Smoke Tests
    failure_nodes:
      - Notify Failure

  - name: Staging Smoke Tests
    job_template: Smoke Tests
    extra_vars:
      target: staging
    success_nodes:
      - Approval Gate
    failure_nodes:
      - Notify Failure

  - name: Approval Gate
    approval_node: true
    success_nodes:
      - Deploy to Production

  - name: Deploy to Production
    job_template: Deploy Production
    success_nodes:
      - Production Smoke Tests
    failure_nodes:
      - Rollback Production

  - name: Production Smoke Tests
    job_template: Smoke Tests
    extra_vars:
      target: production
    failure_nodes:
      - Rollback Production

  - name: Rollback Production
    job_template: Rollback
    always_nodes:
      - Notify Failure

  - name: Notify Failure
    job_template: Slack Notification
    extra_vars:
      status: failed
```

---

## Dynamic Inventory in CI

### AWS EC2 Dynamic Inventory

```yaml
# ansible/inventory/production/aws_ec2.yml
---
plugin: amazon.aws.aws_ec2
regions:
  - eu-north-1
filters:
  tag:Environment: production
  instance-state-name: running
keyed_groups:
  - key: tags.Role
    prefix: role
  - key: tags.Application
    prefix: app
compose:
  ansible_host: private_ip_address
  ansible_user: "'ubuntu'"
hostnames:
  - tag:Name
  - private-dns-name
```

### CI Configuration for AWS

```yaml
# GitHub Actions AWS setup
- name: Configure AWS credentials
  uses: aws-actions/configure-aws-credentials@v4
  with:
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: eu-north-1

- name: Test dynamic inventory
  run: |
    ansible-inventory -i ansible/inventory/production/aws_ec2.yml --graph
```

---

## Secrets Management

### GitHub Secrets Structure

```
Repository Secrets:
+-- AWS_ACCESS_KEY_ID
+-- AWS_SECRET_ACCESS_KEY
+-- ANSIBLE_VAULT_PASSWORD
+-- SSH_PRIVATE_KEY
+-- SLACK_WEBHOOK

Environment Secrets (staging):
+-- DB_PASSWORD
+-- API_KEY

Environment Secrets (production):
+-- DB_PASSWORD
+-- API_KEY
```

### Using Secrets in Playbooks

```yaml
# In CI, create temporary files
- name: Setup SSH key
  run: |
    mkdir -p ~/.ssh
    echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_rsa
    chmod 600 ~/.ssh/id_rsa
    ssh-keyscan -H your-server.com >> ~/.ssh/known_hosts

- name: Create vault password
  run: |
    echo "${{ secrets.ANSIBLE_VAULT_PASSWORD }}" > .vault_pass
    chmod 600 .vault_pass

- name: Cleanup (always run)
  if: always()
  run: |
    rm -f ~/.ssh/id_rsa
    rm -f .vault_pass
```

---

## Rollback Strategy

### Automated Rollback

```yaml
# playbooks/rollback.yml
---
- name: Rollback deployment
  hosts: "{{ target_hosts }}"
  vars:
    rollback_version: "{{ previous_version | default(lookup('file', '/opt/app/.previous_version')) }}"

  tasks:
    - name: Stop current version
      systemd:
        name: myapp
        state: stopped

    - name: Switch to previous version
      file:
        src: "/opt/app/releases/{{ rollback_version }}"
        dest: /opt/app/current
        state: link
        force: true

    - name: Start application
      systemd:
        name: myapp
        state: started

    - name: Verify rollback
      uri:
        url: http://localhost:8080/health
        status_code: 200
      retries: 5
      delay: 10
```

---

## Platform Comparison

| Platform | Pros | Cons |
|----------|------|------|
| GitHub Actions | Native Git integration | Limited runners |
| GitLab CI | Built-in CD features | Self-hosted complexity |
| AWX/Tower | GUI, RBAC, scheduling | Resource intensive |
| Jenkins | Highly flexible | Complex setup |

---

## Sammanfattning

| Stage | Tools |
|-------|-------|
| Lint | ansible-lint, yamllint |
| Test | Molecule, pytest |
| Deploy | ansible-playbook |
| Orchestration | AWX, GitHub Actions |
| Secrets | Vault, CI secrets |

---

## Nästa Steg

CI/CD pipeline klar. Nästa: **Best Practices** — produktion-redo mönster.
''',
}

NODE_19_BEST_PRACTICES = {
    "node_id": 19,
    "title": "Ansible Best Practices",
    "slug": "best-practices",
    "estimated_minutes": 60,
    "xp_reward": 165,
    "prerequisites": [9, 12],
    "content": r'''
# Ansible Best Practices

## Varför detta är kritiskt

> "Best practices är skillnaden mellan Ansible som 'fungerar' och Ansible som är underhållbart, skalbart, och säkert i produktion."

**Best Practice områden:**
- **Structure** — Projektlayout och organisation
- **Security** — Secrets och access control
- **Performance** — Optimering och caching
- **Maintainability** — Naming och dokumentation

---

## Project Structure

```
+-------------------------------------------------------------------------+
|                    RECOMMENDED PROJECT STRUCTURE                        |
+-------------------------------------------------------------------------+
|                                                                         |
|  ansible/                                                               |
|  +-- ansible.cfg              <- Global Ansible configuration            |
|  +-- requirements.yml         <- Galaxy dependencies                     |
|  +-- .ansible-lint            <- Linting rules                           |
|  +-- .yamllint                <- YAML linting rules                      |
|  |                                                                      |
|  +-- inventories/             <- Environment-specific inventories        |
|  |   +-- production/                                                    |
|  |   |   +-- hosts.yml        <- Static inventory                        |
|  |   |   +-- aws_ec2.yml      <- Dynamic inventory                       |
|  |   |   +-- group_vars/      <- Environment-specific vars               |
|  |   |   |   +-- all.yml                                                |
|  |   |   |   +-- all/                                                   |
|  |   |   |   |   +-- vars.yml                                           |
|  |   |   |   |   +-- vault.yml <- Encrypted secrets                      |
|  |   |   |   +-- webservers.yml                                         |
|  |   |   +-- host_vars/       <- Host-specific vars                      |
|  |   |       +-- web01.yml                                              |
|  |   +-- staging/                                                       |
|  |       +-- ...                                                        |
|  |                                                                      |
|  +-- playbooks/               <- Playbook files                          |
|  |   +-- site.yml             <- Master playbook                         |
|  |   +-- webservers.yml                                                 |
|  |   +-- databases.yml                                                  |
|  |   +-- deploy.yml                                                     |
|  |                                                                      |
|  +-- roles/                   <- Reusable roles                          |
|  |   +-- common/                                                        |
|  |   |   +-- defaults/                                                  |
|  |   |   +-- handlers/                                                  |
|  |   |   +-- tasks/                                                     |
|  |   |   +-- templates/                                                 |
|  |   |   +-- files/                                                     |
|  |   |   +-- vars/                                                      |
|  |   |   +-- meta/                                                      |
|  |   |   +-- molecule/        <- Tests                                   |
|  |   +-- nginx/                                                         |
|  |   +-- postgresql/                                                    |
|  |                                                                      |
|  +-- library/                 <- Custom modules                          |
|  +-- filter_plugins/          <- Custom filters                          |
|  +-- callback_plugins/        <- Custom callbacks                        |
|                                                                         |
+-------------------------------------------------------------------------+
```

### ansible.cfg

```ini
# ansible.cfg
[defaults]
# Inventory
inventory = inventories/production

# Roles
roles_path = roles:~/.ansible/roles:/usr/share/ansible/roles

# Performance
forks = 20
gathering = smart
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_facts
fact_caching_timeout = 86400

# Output
stdout_callback = yaml
callback_whitelist = timer, profile_tasks

# Security
host_key_checking = False
retry_files_enabled = False

# Logging
log_path = /var/log/ansible/ansible.log

[privilege_escalation]
become = True
become_method = sudo
become_user = root
become_ask_pass = False

[ssh_connection]
pipelining = True
control_path = /tmp/ansible-%%h-%%p-%%r
ssh_args = -o ControlMaster=auto -o ControlPersist=60s

[inventory]
enable_plugins = yaml, ini, auto, host_list, aws_ec2
```

---

## Naming Conventions

### Files and Directories

```
# Roles: lowercase, underscore separated
roles/
+-- web_server/          ✅ Good
+-- db_backup/           ✅ Good
+-- WebServer/           ❌ Bad (PascalCase)
+-- web-server/          ❌ Bad (hyphens)

# Playbooks: descriptive, verb-noun
playbooks/
+-- deploy_application.yml    ✅ Good
+-- configure_webservers.yml  ✅ Good
+-- setup.yml                 ❌ Bad (not descriptive)
+-- do_stuff.yml              ❌ Bad (vague)
```

### Variables

```yaml
# Use component prefix
nginx_port: 80
nginx_worker_processes: auto
nginx_sites: []

postgresql_version: "15"
postgresql_max_connections: 100
postgresql_data_directory: /var/lib/postgresql

# Use vault_ prefix for secrets
vault_db_password: "{{ lookup('vault', 'secret/db') }}"
vault_api_key: "encrypted_value"

# Reference in regular vars
db_password: "{{ vault_db_password }}"
```

### Tasks

```yaml
# Start with action verb, be descriptive
tasks:
  # ✅ Good task names
  - name: Install nginx package
  - name: Configure nginx main config file
  - name: Create nginx site configuration
  - name: Enable and start nginx service
  - name: Verify nginx is responding on port 80

  # ❌ Bad task names
  - name: nginx              # Not descriptive
  - name: Install stuff      # Vague
  - name: Do the thing       # Meaningless
  - name: Step 1             # Not descriptive
```

---

## Idempotency Rules

### DO: Use Modules

```yaml
# ✅ Idempotent - uses apt module
- name: Ensure nginx is installed
  ansible.builtin.apt:
    name: nginx
    state: present
    update_cache: true

# ✅ Idempotent - uses file module
- name: Ensure directory exists
  ansible.builtin.file:
    path: /opt/app
    state: directory
    mode: '0755'

# ✅ Idempotent - uses user module
- name: Ensure deploy user exists
  ansible.builtin.user:
    name: deploy
    state: present
    groups: docker
```

### DON'T: Use Shell Without Guards

```yaml
# ❌ Not idempotent - always runs
- name: Install nginx
  ansible.builtin.shell: apt-get install -y nginx

# ✅ Idempotent with creates/removes
- name: Run migration
  ansible.builtin.shell: python manage.py migrate
  args:
    chdir: /opt/app
    creates: /opt/app/.migrated

# ✅ Idempotent with changed_when
- name: Check for updates
  ansible.builtin.command: apt list --upgradable
  register: updates
  changed_when: false

# ✅ Idempotent with check
- name: Initialize database (only if not exists)
  ansible.builtin.shell: |
    psql -c "SELECT 1 FROM pg_database WHERE datname='mydb'" | grep -q 1 || \
    createdb mydb
  changed_when: false
```

---

## Variable Hierarchy

```
+-------------------------------------------------------------------------+
|                    VARIABLE PRECEDENCE (Low to High)                    |
+-------------------------------------------------------------------------+
|                                                                         |
|  1.  command line values (for example, -u my_user)                      |
|  2.  role defaults (defined in role/defaults/main.yml)                  |
|  3.  inventory file or script group vars                                |
|  4.  inventory group_vars/all                                           |
|  5.  playbook group_vars/all                                            |
|  6.  inventory group_vars/*                                             |
|  7.  playbook group_vars/*                                              |
|  8.  inventory file or script host vars                                 |
|  9.  inventory host_vars/*                                              |
|  10. playbook host_vars/*                                               |
|  11. host facts / cached set_facts                                      |
|  12. play vars                                                          |
|  13. play vars_prompt                                                   |
|  14. play vars_files                                                    |
|  15. role vars (defined in role/vars/main.yml)                          |
|  16. block vars (only for tasks in block)                               |
|  17. task vars (only for the task)                                      |
|  18. include_vars                                                       |
|  19. set_facts / registered vars                                        |
|  20. role (and include_role) params                                     |
|  21. include params                                                     |
|  22. extra vars (for example, -e "user=admin")          <- HIGHEST       |
|                                                                         |
|  BEST PRACTICE:                                                         |
|  +-- defaults/main.yml  -> Sane defaults (can be overridden)             |
|  +-- vars/main.yml      -> Role-internal vars (rarely override)          |
|  +-- group_vars/        -> Environment-specific values                   |
|                                                                         |
+-------------------------------------------------------------------------+
```

### Variable Organization

```yaml
# roles/nginx/defaults/main.yml - Overridable defaults
nginx_port: 80
nginx_worker_processes: auto
nginx_user: www-data
nginx_sites: []
nginx_ssl_enabled: false

# roles/nginx/vars/main.yml - Internal constants
_nginx_packages:
  Debian: [nginx, nginx-extras]
  RedHat: [nginx]
_nginx_service: nginx
_nginx_config_dir: /etc/nginx

# inventories/production/group_vars/webservers.yml
nginx_port: 443
nginx_ssl_enabled: true
nginx_worker_processes: 4
nginx_sites:
  - name: api
    server_name: api.example.com
    upstream: app_backend
```

---

## Tag Strategy

### Consistent Tagging

```yaml
# roles/nginx/tasks/main.yml
---
- name: Install nginx packages
  ansible.builtin.apt:
    name: "{{ nginx_packages }}"
    state: present
  tags:
    - install
    - packages
    - nginx

- name: Configure nginx main config
  ansible.builtin.template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  tags:
    - configure
    - nginx
  notify: Reload nginx

- name: Configure nginx sites
  ansible.builtin.template:
    src: site.conf.j2
    dest: "/etc/nginx/sites-available/{{ item.name }}.conf"
  loop: "{{ nginx_sites }}"
  tags:
    - configure
    - nginx
    - sites

- name: Enable nginx service
  ansible.builtin.systemd:
    name: nginx
    enabled: true
    state: started
  tags:
    - service
    - nginx
```

### Tag Usage

```bash
# Run only specific tags
ansible-playbook site.yml --tags "configure"
ansible-playbook site.yml --tags "nginx,postgresql"

# Skip specific tags
ansible-playbook site.yml --skip-tags "install"

# List available tags
ansible-playbook site.yml --list-tags

# Common tag patterns
--tags install      # Only installation tasks
--tags configure    # Only configuration tasks
--tags service      # Only service management
--tags deploy       # Only deployment tasks
```

---

## Handler Best Practices

### Validate Before Restart

```yaml
# roles/nginx/handlers/main.yml
---
- name: Validate nginx config
  ansible.builtin.command: nginx -t
  listen: Reload nginx
  changed_when: false

- name: Reload nginx service
  ansible.builtin.systemd:
    name: nginx
    state: reloaded
  listen: Reload nginx

# Handler chain: validate -> reload
# If validate fails, reload won't run
```

### Named Handler Groups

```yaml
# handlers/main.yml
---
- name: Restart full stack
  ansible.builtin.debug:
    msg: "Restarting full stack"
  listen: restart stack
  changed_when: true

- name: Restart nginx
  ansible.builtin.systemd:
    name: nginx
    state: restarted
  listen: restart stack

- name: Restart application
  ansible.builtin.systemd:
    name: myapp
    state: restarted
  listen: restart stack

# Usage in tasks:
# notify: restart stack
```

---

## Security Best Practices

### Secrets Management

```yaml
# ✅ DO: Use Vault for secrets
vault_db_password: !vault |
  $ANSIBLE_VAULT;1.1;AES256
  ...

# ✅ DO: Reference vault vars
db_password: "{{ vault_db_password }}"

# ✅ DO: Use no_log for sensitive tasks
- name: Set database password
  postgresql_user:
    name: app
    password: "{{ vault_db_password }}"
  no_log: true

# ❌ DON'T: Plaintext secrets
db_password: "supersecret123"
```

### Minimal Privileges

```yaml
# ✅ DO: Only become when needed
- name: Read user config
  ansible.builtin.slurp:
    src: ~/.config/app.conf
  # No become - runs as connecting user

- name: Install system package
  ansible.builtin.apt:
    name: nginx
  become: true  # Explicit escalation

# ✅ DO: Use specific become_user
- name: Run as postgres
  postgresql_db:
    name: mydb
  become: true
  become_user: postgres
```

---

## Performance Optimization

### Fact Caching

```ini
# ansible.cfg
[defaults]
gathering = smart
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_facts
fact_caching_timeout = 86400
```

### Parallel Execution

```yaml
# Increase forks
# ansible.cfg
[defaults]
forks = 30

# Strategy for fast execution
- hosts: all
  strategy: free  # Tasks run as fast as possible
```

### Limit Fact Gathering

```yaml
# Disable if not needed
- hosts: webservers
  gather_facts: false
  tasks:
    - name: Deploy static files
      ansible.builtin.copy:
        src: dist/
        dest: /var/www/html/

# Gather only what you need
- hosts: all
  gather_facts: true
  gather_subset:
    - "!all"
    - "!min"
    - network
    - hardware
```

---

## Best Practices Checklist

| Category | Practice | Priority |
|----------|----------|----------|
| **Structure** | Standard directory layout | High |
| **Structure** | One role per component | High |
| **Naming** | Descriptive task names | High |
| **Naming** | Component-prefixed vars | Medium |
| **Security** | Vault for all secrets | Critical |
| **Security** | no_log for sensitive data | Critical |
| **Testing** | Molecule for all roles | High |
| **Testing** | ansible-lint in CI | High |
| **Idempotency** | Use modules over shell | High |
| **Idempotency** | changed_when for commands | Medium |
| **Performance** | Enable fact caching | Medium |
| **Docs** | README for every role | Medium |

---

## Sammanfattning

| Area | Key Points |
|------|------------|
| Structure | Consistent layout, environments separate |
| Naming | Descriptive, prefixed, lowercase |
| Security | Vault everything, no_log |
| Performance | Caching, parallelism |
| Testing | Lint, Molecule, CI |

---

## Nästa Steg

Best practices etablerade. Nästa: **Real-World Patterns** — production deployment strategies.
''',
}

NODE_20_REALWORLD_PATTERNS = {
    "node_id": 20,
    "title": "Real-World Patterns",
    "slug": "realworld-patterns",
    "estimated_minutes": 65,
    "xp_reward": 180,
    "prerequisites": [19],
    "content": r'''
# Real-World Ansible Patterns

## Varför detta är kritiskt

> "Teori är en sak, produktion en annan. Dessa patterns är battle-tested i miljoner deployments. Lär dig av andras misstag."

**Deployment strategies:**
- **Rolling** — Zero-downtime updates
- **Blue/Green** — Instant rollback
- **Canary** — Risk mitigation
- **Feature flags** — Gradual rollout

---

## Deployment Pattern Overview

```
+-------------------------------------------------------------------------+
|                    DEPLOYMENT STRATEGIES                                |
+-------------------------------------------------------------------------+
|                                                                         |
|  ROLLING DEPLOYMENT                                                     |
|  ------------------                                                     |
|  +-----+  +-----+  +-----+  +-----+  +-----+                           |
|  | v1  |  | v1  |  | v1  |  | v1  |  | v1  |  <- Start                  |
|  +-----+  +-----+  +-----+  +-----+  +-----+                           |
|     ↓                                                                   |
|  +-----+  +-----+  +-----+  +-----+  +-----+                           |
|  | v2  |  | v2  |  | v1  |  | v1  |  | v1  |  <- 2 at a time           |
|  +-----+  +-----+  +-----+  +-----+  +-----+                           |
|                       ↓                                                 |
|  +-----+  +-----+  +-----+  +-----+  +-----+                           |
|  | v2  |  | v2  |  | v2  |  | v2  |  | v2  |  <- Complete               |
|  +-----+  +-----+  +-----+  +-----+  +-----+                           |
|                                                                         |
|  BLUE/GREEN DEPLOYMENT                                                  |
|  ---------------------                                                  |
|  +-----------------+     +-----------------+                           |
|  |   BLUE (v1)     | <--  |   Load          |  <- Traffic to Blue       |
|  |   [Active]      |     |   Balancer      |                           |
|  +-----------------+     +-----------------+                           |
|  +-----------------+           |                                       |
|  |   GREEN (v2)    | <----------+            <- Deploy to Green          |
|  |   [Standby]     |     Switch traffic     <- Test, then switch       |
|  +-----------------+                                                    |
|                                                                         |
|  CANARY DEPLOYMENT                                                      |
|  -----------------                                                      |
|  +---------------------------------------+                             |
|  |             PRODUCTION (v1)           | <- 90% traffic               |
|  |  +-----+ +-----+ +-----+ +-----+     |                             |
|  |  | v1  | | v1  | | v1  | | v1  |     |                             |
|  +---------------------------------------+                             |
|  +---------------+                                                      |
|  |  CANARY (v2)  | <- 10% traffic, monitor                              |
|  |  +-----+      |                                                      |
|  |  | v2  |      |  If OK -> Roll out to all                            |
|  +---------------+  If BAD -> Roll back                                  |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## Rolling Deployment

### With Load Balancer Integration

```yaml
# playbooks/rolling_deploy.yml
---
- name: Rolling deployment with zero downtime
  hosts: webservers
  serial: 2  # Deploy to 2 hosts at a time
  max_fail_percentage: 25  # Fail if > 25% hosts fail
  any_errors_fatal: false

  vars:
    app_version: "{{ version | default('latest') }}"
    health_check_url: "http://{{ inventory_hostname }}:8080/health"
    lb_api_url: "http://lb.internal:8080/api"

  pre_tasks:
    - name: Drain connections from load balancer
      ansible.builtin.uri:
        url: "{{ lb_api_url }}/pools/webservers/members/{{ inventory_hostname }}"
        method: PUT
        body_format: json
        body:
          admin_state: "drain"
        headers:
          Authorization: "Bearer {{ lb_api_token }}"
      delegate_to: localhost

    - name: Wait for active connections to finish
      ansible.builtin.uri:
        url: "{{ lb_api_url }}/pools/webservers/members/{{ inventory_hostname }}/stats"
        method: GET
        headers:
          Authorization: "Bearer {{ lb_api_token }}"
      register: member_stats
      delegate_to: localhost
      until: member_stats.json.active_connections == 0
      retries: 30
      delay: 10

  roles:
    - role: deploy_application
      vars:
        app_version: "{{ version }}"

  post_tasks:
    - name: Verify application health
      ansible.builtin.uri:
        url: "{{ health_check_url }}"
        method: GET
        status_code: 200
        return_content: true
      register: health_result
      retries: 10
      delay: 5
      until: health_result.status == 200

    - name: Verify application version
      ansible.builtin.uri:
        url: "http://{{ inventory_hostname }}:8080/version"
        method: GET
      register: version_check
      failed_when: version_check.json.version != app_version

    - name: Re-enable in load balancer
      ansible.builtin.uri:
        url: "{{ lb_api_url }}/pools/webservers/members/{{ inventory_hostname }}"
        method: PUT
        body_format: json
        body:
          admin_state: "enable"
        headers:
          Authorization: "Bearer {{ lb_api_token }}"
      delegate_to: localhost

    - name: Wait for load balancer health check
      ansible.builtin.uri:
        url: "{{ lb_api_url }}/pools/webservers/members/{{ inventory_hostname }}/stats"
        method: GET
        headers:
          Authorization: "Bearer {{ lb_api_token }}"
      register: lb_health
      delegate_to: localhost
      until: lb_health.json.health_status == "healthy"
      retries: 12
      delay: 5
```

### Serial Strategies

```yaml
# Fixed number
serial: 2  # 2 hosts at a time

# Percentage
serial: "25%"  # 25% of hosts at a time

# Progressive
serial:
  - 1       # First, deploy to 1 host (canary)
  - 5       # Then 5 hosts
  - "25%"   # Then 25% of remaining
  - "50%"   # Then 50% of remaining
  - "100%"  # Then all remaining
```

---

## Blue/Green Deployment

### Implementation

```yaml
# playbooks/blue_green_deploy.yml
---
- name: Blue/Green Deployment
  hosts: localhost
  gather_facts: false

  vars:
    active_file: /opt/deploy/active_color
    colors: [blue, green]

  tasks:
    - name: Get current active color
      ansible.builtin.slurp:
        src: "{{ active_file }}"
      register: active_content
      failed_when: false

    - name: Set active and inactive colors
      ansible.builtin.set_fact:
        active_color: "{{ (active_content.content | b64decode | trim) if active_content.content is defined else 'blue' }}"

    - name: Set deploy color (inactive)
      ansible.builtin.set_fact:
        deploy_color: "{{ 'green' if active_color == 'blue' else 'blue' }}"

    - name: Display deployment info
      ansible.builtin.debug:
        msg: |
          Current active: {{ active_color }}
          Deploying to: {{ deploy_color }}
          Version: {{ version }}

- name: Deploy to inactive environment
  hosts: "{{ hostvars['localhost']['deploy_color'] }}_servers"
  become: true

  roles:
    - role: deploy_application
      vars:
        app_version: "{{ version }}"

- name: Verify inactive environment
  hosts: "{{ hostvars['localhost']['deploy_color'] }}_servers"
  tasks:
    - name: Health check
      ansible.builtin.uri:
        url: "http://{{ inventory_hostname }}:8080/health"
        status_code: 200
      retries: 10
      delay: 5

    - name: Run smoke tests
      ansible.builtin.command: /opt/scripts/smoke_tests.sh
      delegate_to: localhost
      run_once: true

- name: Switch traffic
  hosts: load_balancers
  become: true

  vars:
    deploy_color: "{{ hostvars['localhost']['deploy_color'] }}"

  tasks:
    - name: Update nginx upstream
      ansible.builtin.template:
        src: nginx_upstream.j2
        dest: /etc/nginx/conf.d/upstream.conf
      notify: Reload nginx

    - name: Verify traffic switched
      ansible.builtin.uri:
        url: http://localhost/version
        return_content: true
      register: version_check
      until: version_check.json.environment == deploy_color
      retries: 10
      delay: 5

  handlers:
    - name: Reload nginx
      ansible.builtin.systemd:
        name: nginx
        state: reloaded

- name: Update active color
  hosts: localhost
  tasks:
    - name: Record new active color
      ansible.builtin.copy:
        content: "{{ deploy_color }}"
        dest: "{{ active_file }}"

    - name: Notify success
      community.general.slack:
        token: "{{ slack_token }}"
        channel: "#deployments"
        msg: "✅ Blue/Green switch complete: {{ deploy_color }} is now active"
```

### Rollback

```yaml
# playbooks/blue_green_rollback.yml
---
- name: Rollback to previous color
  hosts: localhost
  tasks:
    - name: Get current active color
      ansible.builtin.slurp:
        src: /opt/deploy/active_color
      register: active_content

    - name: Set rollback color
      ansible.builtin.set_fact:
        rollback_color: "{{ 'blue' if (active_content.content | b64decode | trim) == 'green' else 'green' }}"

- name: Switch traffic back
  hosts: load_balancers
  become: true
  tasks:
    - name: Update nginx upstream to rollback color
      ansible.builtin.template:
        src: nginx_upstream.j2
        dest: /etc/nginx/conf.d/upstream.conf
      vars:
        active_servers: "{{ groups[hostvars['localhost']['rollback_color'] + '_servers'] }}"
      notify: Reload nginx

  handlers:
    - name: Reload nginx
      ansible.builtin.systemd:
        name: nginx
        state: reloaded

- name: Update active color
  hosts: localhost
  tasks:
    - name: Record rollback color as active
      ansible.builtin.copy:
        content: "{{ rollback_color }}"
        dest: /opt/deploy/active_color
```

---

## Canary Deployment

### Progressive Rollout

```yaml
# playbooks/canary_deploy.yml
---
- name: Canary Deployment - Phase 1 (10%)
  hosts: canary_servers
  serial: 1

  vars:
    app_version: "{{ version }}"
    canary_percentage: 10

  roles:
    - role: deploy_application

  post_tasks:
    - name: Configure canary traffic weight
      ansible.builtin.uri:
        url: "http://lb.internal:8080/api/routing"
        method: PUT
        body_format: json
        body:
          canary_weight: "{{ canary_percentage }}"
        headers:
          Authorization: "Bearer {{ lb_token }}"
      delegate_to: localhost
      run_once: true

- name: Monitor canary metrics
  hosts: localhost
  tasks:
    - name: Wait for metrics stabilization
      ansible.builtin.pause:
        minutes: 10
        prompt: "Monitoring canary for 10 minutes..."

    - name: Check error rate
      ansible.builtin.uri:
        url: "http://prometheus:9090/api/v1/query"
        method: GET
        body_format: json
        body:
          query: 'sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))'
      register: error_rate

    - name: Validate error rate
      ansible.builtin.assert:
        that:
          - error_rate.json.data.result[0].value[1] | float < 0.01
        fail_msg: "Error rate {{ error_rate.json.data.result[0].value[1] }} exceeds 1% threshold"
        success_msg: "Error rate OK: {{ error_rate.json.data.result[0].value[1] }}"

    - name: Check latency
      ansible.builtin.uri:
        url: "http://prometheus:9090/api/v1/query"
        method: GET
        body_format: json
        body:
          query: 'histogram_quantile(0.99, http_request_duration_seconds_bucket)'
      register: latency_p99

    - name: Validate latency
      ansible.builtin.assert:
        that:
          - latency_p99.json.data.result[0].value[1] | float < 0.5
        fail_msg: "P99 latency {{ latency_p99.json.data.result[0].value[1] }}s exceeds 500ms threshold"

- name: Canary Deployment - Full Rollout
  hosts: production_servers:!canary_servers
  serial: "25%"

  roles:
    - role: deploy_application
      vars:
        app_version: "{{ version }}"

  post_tasks:
    - name: Remove canary routing
      ansible.builtin.uri:
        url: "http://lb.internal:8080/api/routing"
        method: PUT
        body_format: json
        body:
          canary_weight: 0
        headers:
          Authorization: "Bearer {{ lb_token }}"
      delegate_to: localhost
      run_once: true
      when: inventory_hostname == ansible_play_hosts[-1]
```

---

## Database Migrations

### Safe Migration Pattern

```yaml
# playbooks/database_migrate.yml
---
- name: Database Migration
  hosts: db_primary
  become: true
  become_user: postgres

  vars:
    backup_path: "/backup/pre_migration_{{ ansible_date_time.iso8601_basic_short }}.sql"

  tasks:
    - name: Create pre-migration backup
      ansible.builtin.shell: |
        pg_dump {{ db_name }} | gzip > {{ backup_path }}.gz
      args:
        creates: "{{ backup_path }}.gz"

    - name: Verify backup
      ansible.builtin.stat:
        path: "{{ backup_path }}.gz"
      register: backup_file
      failed_when: not backup_file.stat.exists or backup_file.stat.size < 1000

    - name: Generate migration SQL (dry run)
      ansible.builtin.command: |
        alembic upgrade head --sql
      args:
        chdir: /opt/app
      register: migration_sql
      changed_when: false

    - name: Display migration SQL
      ansible.builtin.debug:
        var: migration_sql.stdout_lines

    - name: Confirm migration
      ansible.builtin.pause:
        prompt: "Review migration SQL above. Press enter to continue or Ctrl+C to abort"
      when: not auto_approve | default(false)

    - name: Run migrations
      ansible.builtin.command: |
        alembic upgrade head
      args:
        chdir: /opt/app
      register: migration_result

    - name: Verify migration
      ansible.builtin.command: |
        alembic current
      args:
        chdir: /opt/app
      register: current_revision
      changed_when: false

    - name: Verify application connectivity
      ansible.builtin.uri:
        url: "http://{{ app_host }}:8080/health"
        status_code: 200
      retries: 5
      delay: 10

  handlers:
    - name: Rollback migration
      ansible.builtin.shell: |
        psql {{ db_name }} < <(gunzip -c {{ backup_path }}.gz)
      args:
        executable: /bin/bash
      listen: Rollback database
```

---

## Secrets Rotation

### Automated Rotation

```yaml
# playbooks/rotate_secrets.yml
---
- name: Rotate application secrets
  hosts: localhost
  gather_facts: false

  vars:
    rotation_date: "{{ ansible_date_time.date }}"

  tasks:
    - name: Generate new database password
      ansible.builtin.set_fact:
        new_db_password: "{{ lookup('password', '/dev/null length=32 chars=ascii_letters,digits') }}"

    - name: Generate new API key
      ansible.builtin.set_fact:
        new_api_key: "{{ lookup('password', '/dev/null length=64 chars=ascii_letters,digits') }}"

- name: Update database password
  hosts: db_primary
  become: true
  become_user: postgres

  tasks:
    - name: Update database user password
      community.postgresql.postgresql_user:
        name: app_user
        password: "{{ hostvars['localhost']['new_db_password'] }}"
        state: present

- name: Update application servers
  hosts: app_servers
  serial: 1

  tasks:
    - name: Update application config
      ansible.builtin.template:
        src: app.env.j2
        dest: /opt/app/.env
        mode: '0600'
      vars:
        db_password: "{{ hostvars['localhost']['new_db_password'] }}"
        api_key: "{{ hostvars['localhost']['new_api_key'] }}"
      notify: Restart application

    - name: Verify application health
      ansible.builtin.uri:
        url: http://{{ inventory_hostname }}:8080/health
        status_code: 200
      retries: 10
      delay: 5

  handlers:
    - name: Restart application
      ansible.builtin.systemd:
        name: myapp
        state: restarted

- name: Update secrets in Vault
  hosts: localhost
  tasks:
    - name: Store new secrets in Vault
      community.hashi_vault.vault_write:
        url: "{{ vault_url }}"
        token: "{{ vault_token }}"
        path: secret/data/app/credentials
        data:
          data:
            db_password: "{{ new_db_password }}"
            api_key: "{{ new_api_key }}"
            rotated_at: "{{ rotation_date }}"

    - name: Notify rotation complete
      community.general.slack:
        token: "{{ slack_token }}"
        channel: "#security"
        msg: "🔐 Secrets rotated successfully for {{ env }} environment"
```

---

## Pattern Summary

| Pattern | Use Case | Risk Level |
|---------|----------|------------|
| Rolling | Regular updates | Low |
| Blue/Green | Critical apps | Very Low |
| Canary | New features | Low |
| Feature Flags | Gradual rollout | Very Low |
| DB Migration | Schema changes | Medium |
| Secrets Rotation | Security | Medium |

---

## 🎉 Grattis!

Du har slutfört **Ansible Mastery SkillsMap**!

**Du har lärt dig:**
- ✅ Ansible fundamentals och YAML
- ✅ Inventory management och playbooks
- ✅ Variables, templates, och Jinja2
- ✅ Roles och Galaxy
- ✅ Vault för secrets
- ✅ Cloud och container automation
- ✅ Custom modules och plugins
- ✅ Testing med Molecule
- ✅ CI/CD integration
- ✅ Production deployment patterns

---

## Nästa Steg

**Rekommenderade SkillsMaps:**
- **Terraform** -> Infrastructure as Code
- **Kubernetes** -> Container orchestration
- **CI/CD Pipelines** -> GitHub Actions, GitLab CI
- **Monitoring** -> Prometheus, Grafana
''',
}

ANSIBLE_BLOCK_5 = [
    NODE_17_TESTING_ANSIBLE,
    NODE_18_CICD_ANSIBLE,
    NODE_19_BEST_PRACTICES,
    NODE_20_REALWORLD_PATTERNS,
]
