# =============================================================================
# BLOCK 3: ADVANCED PLAYBOOKS (Noder 9-12)
# =============================================================================

NODE_09_ROLES = {
    "node_id": 9,
    "title": "Roles",
    "slug": "roles",
    "estimated_minutes": 60,
    "xp_reward": 160,
    "prerequisites": [8],
    "content": '''
# Ansible Roles

Återanvändbar, modulär Ansible-kod.

## Role Struktur

```
roles/
└── nginx/
    ├── defaults/      # Default variables (lowest priority)
    │   └── main.yml
    ├── files/         # Static files
    ├── handlers/      # Handlers
    │   └── main.yml
    ├── meta/          # Role metadata & dependencies
    │   └── main.yml
    ├── tasks/         # Tasks
    │   └── main.yml
    ├── templates/     # Jinja2 templates
    ├── tests/         # Test playbooks
    └── vars/          # Variables (high priority)
        └── main.yml
```

## Skapa Role

```bash
# Ansible Galaxy init
ansible-galaxy init roles/nginx

# Manuellt
mkdir -p roles/nginx/{tasks,handlers,templates,files,defaults,vars,meta}
```

## Exempel Role

```yaml
# roles/nginx/defaults/main.yml
nginx_port: 80
nginx_worker_processes: auto

# roles/nginx/tasks/main.yml
---
- name: Install nginx
  apt:
    name: nginx
    state: present
    update_cache: true

- name: Deploy nginx.conf
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  notify: Restart nginx

- name: Start nginx
  service:
    name: nginx
    state: started
    enabled: true

# roles/nginx/handlers/main.yml
---
- name: Restart nginx
  service:
    name: nginx
    state: restarted

- name: Reload nginx
  service:
    name: nginx
    state: reloaded

# roles/nginx/templates/nginx.conf.j2
worker_processes {{ nginx_worker_processes }};

events {
    worker_connections 1024;
}

http {
    server {
        listen {{ nginx_port }};
    }
}
```

## Använda Roles

```yaml
# Method 1: roles section
- hosts: webservers
  roles:
    - nginx
    - { role: app, app_port: 8080 }

# Method 2: include_role
- hosts: webservers
  tasks:
    - name: Setup nginx
      include_role:
        name: nginx
      vars:
        nginx_port: 8080

# Method 3: import_role (static)
- hosts: webservers
  tasks:
    - import_role:
        name: nginx
```

## Role Dependencies

```yaml
# roles/app/meta/main.yml
dependencies:
  - role: nginx
  - role: postgres
    vars:
      postgres_version: 14
```

| Directory | Syfte |
|-----------|-------|
| tasks/ | Huvudlogik |
| handlers/ | Notified tasks |
| defaults/ | Default vars |
| vars/ | Role vars |
| templates/ | Jinja2 |
| files/ | Statiska filer |
| meta/ | Dependencies |

**Nästa steg:** Node 10 - Templates (Jinja2)
''',
}

NODE_10_TEMPLATES = {
    "node_id": 10,
    "title": "Templates (Jinja2)",
    "slug": "templates-jinja2",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [9],
    "content": '''
# Jinja2 Templates

Dynamiska config-filer.

## Grundläggande Syntax

```jinja
{# Detta är en kommentar #}

{{ variable }}              {# Output variable #}
{% if condition %}         {# Logic #}
{% endif %}
```

## Variables

```jinja
# nginx.conf.j2
server {
    listen {{ http_port }};
    server_name {{ server_name }};

    location / {
        proxy_pass http://{{ app_host }}:{{ app_port }};
    }
}
```

## Conditionals

```jinja
{% if ssl_enabled %}
server {
    listen 443 ssl;
    ssl_certificate {{ ssl_cert_path }};
    ssl_certificate_key {{ ssl_key_path }};
}
{% else %}
server {
    listen 80;
}
{% endif %}
```

## Loops

```jinja
# hosts.j2
{% for host in webservers %}
{{ host.ip }}    {{ host.name }}
{% endfor %}

# Med index
{% for user in users %}
{{ loop.index }}. {{ user.name }}
{% endfor %}
```

## Filters

```jinja
{{ name | upper }}                 {# UPPERCASE #}
{{ name | lower }}                 {# lowercase #}
{{ name | capitalize }}            {# Capitalize #}
{{ list | join(', ') }}           {# Join list #}
{{ value | default('fallback') }} {# Default value #}
{{ password | password_hash('sha512') }}  {# Hash #}
{{ data | to_nice_json }}         {# Pretty JSON #}
{{ data | to_nice_yaml }}         {# Pretty YAML #}
{{ path | basename }}             {# Filename #}
{{ path | dirname }}              {# Directory #}
```

## Ansible-specifika

```jinja
{# Host facts #}
IP: {{ ansible_default_ipv4.address }}
OS: {{ ansible_distribution }}

{# Inventory #}
{% for host in groups['webservers'] %}
{{ hostvars[host]['ansible_host'] }}
{% endfor %}
```

## Avancerade Templates

```jinja
# app.conf.j2
{% set default_port = 8080 %}

[server]
port = {{ app_port | default(default_port) }}
workers = {{ ansible_processor_vcpus }}
debug = {{ 'true' if debug_mode else 'false' }}

[database]
{% if db_type == 'postgres' %}
driver = postgresql
port = 5432
{% elif db_type == 'mysql' %}
driver = mysql
port = 3306
{% endif %}
host = {{ db_host }}
name = {{ db_name }}

[servers]
{% for server in app_servers %}
server_{{ loop.index }} = {{ server.host }}:{{ server.port }}
{% endfor %}
```

## Template Task

```yaml
- name: Deploy config
  template:
    src: app.conf.j2
    dest: /etc/myapp/config.conf
    owner: root
    group: root
    mode: '0644'
    validate: '/usr/bin/myapp --check %s'
  notify: Restart app
```

| Filter | Funktion |
|--------|----------|
| default() | Fallback-värde |
| join() | Slå ihop lista |
| upper/lower | Case |
| to_json | JSON output |
| regex_replace | Regex |

**Nästa steg:** Node 11 - Ansible Galaxy
''',
}

NODE_11_ANSIBLE_GALAXY = {
    "node_id": 11,
    "title": "Ansible Galaxy",
    "slug": "ansible-galaxy",
    "estimated_minutes": 45,
    "xp_reward": 130,
    "prerequisites": [9],
    "content": '''
# Ansible Galaxy

Community roles och collections.

## Installera Roles

```bash
# Från Galaxy
ansible-galaxy install geerlingguy.docker
ansible-galaxy install geerlingguy.nginx

# Specifik version
ansible-galaxy install geerlingguy.docker,6.0.0

# Från GitHub
ansible-galaxy install git+https://github.com/user/repo.git

# Lista installerade
ansible-galaxy list
```

## Requirements File

```yaml
# requirements.yml
roles:
  - name: geerlingguy.docker
    version: 6.0.0
  - name: geerlingguy.nginx
  - name: custom_role
    src: git+https://github.com/org/role.git
    version: v1.0.0

collections:
  - name: community.general
    version: ">=5.0.0"
  - name: amazon.aws
```

```bash
# Installera allt
ansible-galaxy install -r requirements.yml
ansible-galaxy collection install -r requirements.yml
```

## Collections

```bash
# Installera collection
ansible-galaxy collection install community.docker
ansible-galaxy collection install amazon.aws

# Lista collections
ansible-galaxy collection list
```

## Använda Collections

```yaml
# FQCN (Fully Qualified Collection Name)
- name: Create Docker container
  community.docker.docker_container:
    name: nginx
    image: nginx:latest

# Eller med collections keyword
- hosts: all
  collections:
    - community.docker
  tasks:
    - name: Create container
      docker_container:
        name: nginx
```

## Publicera Role

```bash
# Login
ansible-galaxy login

# Import från GitHub
ansible-galaxy import username repo_name

# Role måste ha:
# - meta/main.yml med galaxy_info
# - README.md
# - Taggade releases
```

## meta/main.yml

```yaml
galaxy_info:
  author: your_name
  description: Role description
  license: MIT
  min_ansible_version: "2.9"
  platforms:
    - name: Ubuntu
      versions:
        - focal
        - jammy
  galaxy_tags:
    - nginx
    - webserver

dependencies:
  - role: common
```

| Kommando | Funktion |
|----------|----------|
| install | Installera role/collection |
| list | Lista installerade |
| search | Sök på Galaxy |
| init | Skapa role-struktur |
| import | Publicera role |

**Nästa steg:** Node 12 - Ansible Vault
''',
}

NODE_12_ANSIBLE_VAULT = {
    "node_id": 12,
    "title": "Ansible Vault",
    "slug": "ansible-vault",
    "estimated_minutes": 50,
    "xp_reward": 145,
    "prerequisites": [6],
    "content": '''
# Ansible Vault

Kryptera känslig data.

## Skapa Krypterad Fil

```bash
# Skapa ny
ansible-vault create secrets.yml

# Kryptera befintlig
ansible-vault encrypt vars/passwords.yml

# Visa innehåll
ansible-vault view secrets.yml

# Redigera
ansible-vault edit secrets.yml

# Dekryptera
ansible-vault decrypt secrets.yml

# Byt lösenord
ansible-vault rekey secrets.yml
```

## Krypterad Fil

```yaml
# secrets.yml (efter encrypt)
$ANSIBLE_VAULT;1.1;AES256
34623462346234623462346234623462346234623462
62346234623462346234623462346234623462346234
```

## Använda Vault

```yaml
# playbook.yml
- hosts: all
  vars_files:
    - vars/common.yml
    - vars/secrets.yml  # Krypterad fil
  tasks:
    - name: Configure database
      template:
        src: db.conf.j2
        dest: /etc/app/db.conf
      vars:
        db_password: "{{ vault_db_password }}"
```

```bash
# Kör med password prompt
ansible-playbook site.yml --ask-vault-pass

# Med password-fil
ansible-playbook site.yml --vault-password-file ~/.vault_pass

# Environment variable
export ANSIBLE_VAULT_PASSWORD_FILE=~/.vault_pass
ansible-playbook site.yml
```

## Kryptera Enskilda Värden

```bash
# String
ansible-vault encrypt_string 'supersecret' --name 'db_password'

# Output
db_password: !vault |
  $ANSIBLE_VAULT;1.1;AES256
  62346234623462346234623462346234...
```

```yaml
# Använd direkt i vars
vars:
  db_password: !vault |
    $ANSIBLE_VAULT;1.1;AES256
    62346234623462346234623462346234...
```

## Multiple Vault IDs

```bash
# Skapa med ID
ansible-vault create --vault-id prod@prompt secrets_prod.yml
ansible-vault create --vault-id dev@~/.dev_pass secrets_dev.yml

# Kör med multiple vaults
ansible-playbook site.yml \
  --vault-id dev@~/.dev_pass \
  --vault-id prod@prompt
```

## Best Practices

```yaml
# Separera secrets
group_vars/
├── all/
│   ├── vars.yml      # Normala variabler
│   └── vault.yml     # Krypterade (prefix: vault_)

# vars.yml
db_user: "{{ vault_db_user }}"
db_password: "{{ vault_db_password }}"

# vault.yml (krypterad)
vault_db_user: admin
vault_db_password: supersecret
```

| Kommando | Funktion |
|----------|----------|
| create | Ny krypterad fil |
| encrypt | Kryptera fil |
| decrypt | Dekryptera |
| edit | Redigera |
| view | Visa innehåll |
| rekey | Byt lösenord |

**Nästa steg:** Node 13 - Core Modules
''',
}

ANSIBLE_BLOCK_3 = [
    NODE_09_ROLES,
    NODE_10_TEMPLATES,
    NODE_11_ANSIBLE_GALAXY,
    NODE_12_ANSIBLE_VAULT,
]
