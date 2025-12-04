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
    "content": r'''
# Ansible Roles

## Varför detta är kritiskt

> "En playbook är ett recept. En role är ett helt kök — organiserat, testbart, återanvändbart. När du har 50 playbooks med duplicerad kod har du problem. Med roles har du lösningen."

Roles transformerar Ansible från "scripts som kör tasks" till "infrastructure as code på enterprise-nivå".

**Problem med stora playbooks:**
- 2000+ rader i en fil
- Samma kod i flera playbooks
- Svårt att testa isolerat
- Nightmare att underhålla

**Med roles:**
- Modulär, organiserad kod
- Återanvänd över projekt
- Versionshantera separat
- Testa individuellt

---

## Role Anatomy

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          ROLE STRUCTURE                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  roles/                                                                 │
│  └── nginx/                        ← Role name                          │
│      │                                                                  │
│      ├── defaults/                 ← Default variables (LOWEST prio)    │
│      │   └── main.yml                                                   │
│      │                                                                  │
│      ├── vars/                     ← Role variables (HIGH prio)         │
│      │   └── main.yml                                                   │
│      │                                                                  │
│      ├── tasks/                    ← Main logic                         │
│      │   ├── main.yml              ← Entry point                        │
│      │   ├── install.yml                                                │
│      │   ├── configure.yml                                              │
│      │   └── service.yml                                                │
│      │                                                                  │
│      ├── handlers/                 ← Event handlers                     │
│      │   └── main.yml                                                   │
│      │                                                                  │
│      ├── templates/                ← Jinja2 templates                   │
│      │   ├── nginx.conf.j2                                              │
│      │   └── vhost.conf.j2                                              │
│      │                                                                  │
│      ├── files/                    ← Static files                       │
│      │   └── ssl/                                                       │
│      │                                                                  │
│      ├── meta/                     ← Dependencies & metadata            │
│      │   └── main.yml                                                   │
│      │                                                                  │
│      └── README.md                 ← Documentation                      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Directory Purpose

| Directory | Purpose | Priority |
|-----------|---------|----------|
| `defaults/` | Default variables användaren kan override | Lägst |
| `vars/` | Interna role-variabler | Hög |
| `tasks/` | Alla tasks | - |
| `handlers/` | Handlers för notify | - |
| `templates/` | Jinja2 templates (.j2) | - |
| `files/` | Statiska filer att kopiera | - |
| `meta/` | Dependencies och metadata | - |

---

## Skapa en Role

### ansible-galaxy init

```bash
# Skapa standardstruktur
ansible-galaxy init roles/nginx

# Output
roles/nginx/
├── README.md
├── defaults/
│   └── main.yml
├── files/
├── handlers/
│   └── main.yml
├── meta/
│   └── main.yml
├── tasks/
│   └── main.yml
├── templates/
├── tests/
│   ├── inventory
│   └── test.yml
└── vars/
    └── main.yml
```

### Manual Creation

```bash
mkdir -p roles/nginx/{tasks,handlers,templates,files,defaults,vars,meta}
```

---

## Complete Role Example

### defaults/main.yml

```yaml
---
# User-configurable defaults
nginx_user: www-data
nginx_worker_processes: auto
nginx_worker_connections: 1024

nginx_http_port: 80
nginx_https_port: 443
nginx_ssl_enabled: false

nginx_server_name: "{{ inventory_hostname }}"
nginx_root: /var/www/html

nginx_access_log: /var/log/nginx/access.log
nginx_error_log: /var/log/nginx/error.log

nginx_extra_packages: []
```

### vars/main.yml

```yaml
---
# Internal variables (don't override)
nginx_package_name: nginx
nginx_service_name: nginx
nginx_config_path: /etc/nginx
nginx_main_config: "{{ nginx_config_path }}/nginx.conf"
nginx_sites_available: "{{ nginx_config_path }}/sites-available"
nginx_sites_enabled: "{{ nginx_config_path }}/sites-enabled"
```

### tasks/main.yml

```yaml
---
# Entry point - includes other task files
- name: Include OS-specific variables
  include_vars: "{{ item }}"
  with_first_found:
    - "{{ ansible_distribution }}-{{ ansible_distribution_major_version }}.yml"
    - "{{ ansible_distribution }}.yml"
    - "{{ ansible_os_family }}.yml"
    - default.yml
  tags: always

- name: Install nginx
  include_tasks: install.yml
  tags: nginx_install

- name: Configure nginx
  include_tasks: configure.yml
  tags: nginx_config

- name: Manage nginx service
  include_tasks: service.yml
  tags: nginx_service
```

### tasks/install.yml

```yaml
---
- name: Install nginx package
  apt:
    name: "{{ nginx_package_name }}"
    state: present
    update_cache: true
    cache_valid_time: 3600
  when: ansible_os_family == "Debian"

- name: Install nginx package (RedHat)
  yum:
    name: "{{ nginx_package_name }}"
    state: present
  when: ansible_os_family == "RedHat"

- name: Install extra packages
  package:
    name: "{{ item }}"
    state: present
  loop: "{{ nginx_extra_packages }}"
  when: nginx_extra_packages | length > 0
```

### tasks/configure.yml

```yaml
---
- name: Ensure directories exist
  file:
    path: "{{ item }}"
    state: directory
    owner: root
    group: root
    mode: '0755'
  loop:
    - "{{ nginx_config_path }}"
    - "{{ nginx_sites_available }}"
    - "{{ nginx_sites_enabled }}"
    - "{{ nginx_root }}"

- name: Deploy main nginx configuration
  template:
    src: nginx.conf.j2
    dest: "{{ nginx_main_config }}"
    owner: root
    group: root
    mode: '0644'
    validate: 'nginx -t -c %s'
  notify: Reload nginx

- name: Deploy default site
  template:
    src: default-site.conf.j2
    dest: "{{ nginx_sites_available }}/default"
    owner: root
    group: root
    mode: '0644'
  notify: Reload nginx

- name: Enable default site
  file:
    src: "{{ nginx_sites_available }}/default"
    dest: "{{ nginx_sites_enabled }}/default"
    state: link
  notify: Reload nginx
```

### tasks/service.yml

```yaml
---
- name: Ensure nginx is started and enabled
  service:
    name: "{{ nginx_service_name }}"
    state: started
    enabled: true

- name: Verify nginx is responding
  uri:
    url: "http://localhost:{{ nginx_http_port }}"
    status_code: 200
  register: nginx_health
  retries: 5
  delay: 3
  until: nginx_health.status == 200
```

### handlers/main.yml

```yaml
---
- name: Restart nginx
  service:
    name: "{{ nginx_service_name }}"
    state: restarted

- name: Reload nginx
  service:
    name: "{{ nginx_service_name }}"
    state: reloaded

- name: Validate nginx config
  command: nginx -t
  changed_when: false
  listen: "Validate and reload nginx"

- name: Apply nginx config
  service:
    name: "{{ nginx_service_name }}"
    state: reloaded
  listen: "Validate and reload nginx"
```

### templates/nginx.conf.j2

```jinja2
# {{ ansible_managed }}
user {{ nginx_user }};
worker_processes {{ nginx_worker_processes }};
pid /run/nginx.pid;

events {
    worker_connections {{ nginx_worker_connections }};
    multi_accept on;
}

http {
    # Basic Settings
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging
    access_log {{ nginx_access_log }};
    error_log {{ nginx_error_log }};

    # Gzip
    gzip on;
    gzip_disable "msie6";

    # Virtual Host Configs
    include {{ nginx_sites_enabled }}/*;
}
```

### meta/main.yml

```yaml
---
galaxy_info:
  author: Your Name
  description: Nginx web server role
  license: MIT
  min_ansible_version: "2.10"

  platforms:
    - name: Ubuntu
      versions:
        - focal
        - jammy
    - name: Debian
      versions:
        - bullseye
        - bookworm
    - name: EL
      versions:
        - "8"
        - "9"

  galaxy_tags:
    - nginx
    - web
    - proxy

dependencies: []
```

---

## Using Roles

### Method 1: roles section

```yaml
---
- name: Configure webservers
  hosts: webservers
  become: true

  roles:
    - nginx                                   # Basic usage
    - { role: nginx, nginx_http_port: 8080 }  # With variables
    - role: app
      vars:
        app_port: 3000
      tags: app
```

### Method 2: include_role (dynamic)

```yaml
---
- name: Conditional role loading
  hosts: webservers

  tasks:
    - name: Include nginx role
      include_role:
        name: nginx
      vars:
        nginx_ssl_enabled: true
      when: "'webservers' in group_names"
```

### Method 3: import_role (static)

```yaml
---
- name: Static role import
  hosts: webservers

  tasks:
    - name: Import nginx role
      import_role:
        name: nginx
      tags: nginx  # Tags work with import
```

### include_role vs import_role

| Feature | include_role | import_role |
|---------|-------------|-------------|
| Timing | Runtime (dynamic) | Parse time (static) |
| Looping | ✓ Works with loop | ✗ No looping |
| Conditionals | Per-iteration | Whole role |
| Tags | Limited | Full support |
| Performance | Slower | Faster |

---

## Role Dependencies

```yaml
# roles/app/meta/main.yml
---
dependencies:
  - role: common

  - role: nginx
    vars:
      nginx_http_port: 80
      nginx_ssl_enabled: "{{ app_ssl_enabled | default(false) }}"

  - role: postgresql
    vars:
      postgresql_version: 14
    when: app_database == "postgres"
```

**Dependency order:** Dependencies run BEFORE the role itself.

---

## Practical Tips

### Tag Everything

```yaml
# tasks/main.yml
- include_tasks: install.yml
  tags: [nginx, nginx_install, install]

- include_tasks: configure.yml
  tags: [nginx, nginx_config, config]
```

```bash
# Run only config tasks
ansible-playbook site.yml --tags nginx_config
```

### Molecule Testing

```bash
# Install molecule
pip install molecule molecule-docker

# Initialize tests
cd roles/nginx
molecule init scenario

# Run tests
molecule test
```

---

## Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| `defaults/` | Variabler användaren kan override |
| `vars/` | Interna role-variabler |
| `tasks/` | Huvudlogik (main.yml = entry) |
| `handlers/` | Event handlers |
| `templates/` | Jinja2 filer |
| `meta/` | Dependencies |
| `include_role` | Dynamisk inkludering |
| `import_role` | Statisk inkludering |

---

## Nästa Steg

Nu kan du organisera kod i roles. Nästa: **Templates (Jinja2)** — dynamiska config-filer.
''',
}

NODE_10_TEMPLATES = {
    "node_id": 10,
    "title": "Templates (Jinja2)",
    "slug": "templates-jinja2",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "prerequisites": [9],
    "content": r'''
# Jinja2 Templates

## Varför detta är kritiskt

> "Statiska config-filer fungerar för EN server. Templates fungerar för 1000. Med Jinja2 genererar du unika configs för varje host, miljö och scenario."

Varje server har unik:
- Hostname, IP-adress
- CPU/RAM specifikationer
- Miljö (dev/staging/prod)
- Applikationsport

Templates tar EN fil och genererar hundratals anpassade versioner.

---

## Jinja2 Syntax

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        JINJA2 BASICS                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  {{ variable }}              Output variable value                      │
│  {% statement %}             Logic (if, for, etc)                       │
│  {# comment #}               Comments (not in output)                   │
│                                                                         │
│  {{ name }}                  → "web01"                                  │
│  {{ port | default(80) }}    → 80 (if port undefined)                  │
│  {% if ssl %}...{% endif %}  → Conditional content                      │
│  {% for x in list %}...{% endfor %}  → Loop                            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Variables

### Basic Variable Output

```jinja2
# /etc/myapp/config.yml.j2
server:
  name: {{ server_name }}
  port: {{ http_port }}
  host: {{ ansible_default_ipv4.address }}
  environment: {{ env }}
```

### Dictionary Access

```jinja2
# Dot notation
database:
  host: {{ database.host }}
  port: {{ database.port }}
  name: {{ database.name }}

# Bracket notation (required for keys with special chars)
api_key: {{ secrets['api-key'] }}
```

### Default Values

```jinja2
# If variable might not exist
port: {{ custom_port | default(8080) }}
log_level: {{ log_level | default('info') }}

# Default to another variable
backup_host: {{ backup_server | default(primary_server) }}

# Required (fail if undefined)
api_key: {{ api_key | mandatory }}
```

---

## Conditionals

### if/elif/else

```jinja2
{% if ssl_enabled %}
server {
    listen 443 ssl;
    ssl_certificate {{ ssl_cert_path }};
    ssl_certificate_key {{ ssl_key_path }};

    {% if ssl_dhparam %}
    ssl_dhparam {{ ssl_dhparam }};
    {% endif %}
}
{% else %}
server {
    listen 80;
}
{% endif %}
```

### Multiple Conditions

```jinja2
{% if env == 'production' %}
DEBUG = false
LOG_LEVEL = warn
{% elif env == 'staging' %}
DEBUG = true
LOG_LEVEL = info
{% else %}
DEBUG = true
LOG_LEVEL = debug
{% endif %}
```

### Inline Conditionals

```jinja2
# Ternary-style
debug: {{ 'true' if debug_enabled else 'false' }}

# In strings
connection: {{ 'https' if ssl_enabled else 'http' }}://{{ host }}:{{ port }}
```

### Testing Variables

```jinja2
{% if database is defined %}
DATABASE_URL = postgres://{{ database.host }}:{{ database.port }}/{{ database.name }}
{% endif %}

{% if users is not none and users | length > 0 %}
ADMIN_USERS = {{ users | join(',') }}
{% endif %}

{% if version is version('2.0', '>=') %}
# Use new config format
{% endif %}
```

---

## Loops

### Basic Loop

```jinja2
# /etc/hosts entries
{% for host in inventory_hosts %}
{{ hostvars[host].ansible_host }}    {{ host }}
{% endfor %}
```

### Loop with Index

```jinja2
# Numbered list
{% for user in users %}
{{ loop.index }}. {{ user.name }} ({{ user.email }})
{% endfor %}

# Loop variables:
# loop.index      → 1-indexed (1, 2, 3...)
# loop.index0     → 0-indexed (0, 1, 2...)
# loop.first      → True for first iteration
# loop.last       → True for last iteration
# loop.length     → Total items
```

### Loop with Dictionaries

```jinja2
# Environment variables
{% for key, value in env_vars.items() %}
export {{ key }}="{{ value }}"
{% endfor %}

# Server pool
upstream backend {
{% for server in backend_servers %}
    server {{ server.host }}:{{ server.port }} weight={{ server.weight | default(1) }};
{% endfor %}
}
```

### Loop Control

```jinja2
# Skip empty items
{% for item in items if item.enabled %}
{{ item.name }}
{% endfor %}

# Handle empty list
{% for host in hosts %}
{{ host }}
{% else %}
# No hosts configured
{% endfor %}
```

---

## Filters

### String Filters

```jinja2
{{ name | upper }}           → "MYAPP"
{{ name | lower }}           → "myapp"
{{ name | capitalize }}      → "Myapp"
{{ name | title }}           → "My App"
{{ text | trim }}            → Remove whitespace
{{ name | replace('_', '-') }} → "my-app"
{{ name | regex_replace('^web', 'srv') }}
```

### List Filters

```jinja2
{{ packages | join(', ') }}           → "nginx, curl, vim"
{{ packages | first }}                → "nginx"
{{ packages | last }}                 → "vim"
{{ packages | length }}               → 3
{{ packages | sort }}                 → Sorted list
{{ packages | unique }}               → Remove duplicates
{{ packages | reverse | list }}       → Reversed
{{ numbers | max }}                   → Maximum value
{{ numbers | min }}                   → Minimum value
{{ numbers | sum }}                   → Total
```

### Type Conversion

```jinja2
{{ "true" | bool }}                   → true
{{ "42" | int }}                      → 42
{{ 3.14 | string }}                   → "3.14"
{{ {'a': 1} | to_json }}              → '{"a": 1}'
{{ data | to_yaml }}                  → YAML format
{{ data | to_nice_json(indent=2) }}   → Pretty JSON
```

### Path Filters

```jinja2
{{ "/etc/nginx/nginx.conf" | basename }}    → "nginx.conf"
{{ "/etc/nginx/nginx.conf" | dirname }}     → "/etc/nginx"
{{ "config" | path_join("nginx.conf") }}    → "config/nginx.conf"
{{ path | expanduser }}                     → Expand ~
```

### Security Filters

```jinja2
# Password hashing
password: {{ raw_password | password_hash('sha512') }}

# URL encoding
url: https://api.example.com?q={{ query | urlencode }}

# Base64
encoded: {{ secret | b64encode }}
decoded: {{ encoded_data | b64decode }}
```

### Ansible-specific Filters

```jinja2
# IP address manipulation
{{ '192.168.1.0/24' | ipaddr('network') }}    → "192.168.1.0"
{{ '192.168.1.0/24' | ipaddr('netmask') }}    → "255.255.255.0"
{{ ansible_all_ipv4_addresses | ipaddr('192.168.0.0/16') }}

# Regex
{{ text | regex_search('version: (\d+\.\d+)', '\\1') }}
{{ items | select('match', '^web.*') | list }}
```

---

## Ansible Variables in Templates

### Facts

```jinja2
# System information
Hostname: {{ ansible_hostname }}
FQDN: {{ ansible_fqdn }}
OS: {{ ansible_distribution }} {{ ansible_distribution_version }}
Kernel: {{ ansible_kernel }}
Architecture: {{ ansible_architecture }}

# Hardware
CPUs: {{ ansible_processor_vcpus }}
Memory: {{ ansible_memtotal_mb }} MB
Memory (GB): {{ (ansible_memtotal_mb / 1024) | round(1) }} GB

# Network
IP: {{ ansible_default_ipv4.address }}
Gateway: {{ ansible_default_ipv4.gateway }}
Interface: {{ ansible_default_ipv4.interface }}
```

### Inventory Variables

```jinja2
# Group members
{% for host in groups['webservers'] %}
server {{ hostvars[host]['ansible_host'] }};
{% endfor %}

# Current host info
Server: {{ inventory_hostname }}
Group: {{ group_names | join(', ') }}
```

---

## Advanced Template Techniques

### Whitespace Control

```jinja2
{# Default: preserves whitespace #}
{% for item in items %}
- {{ item }}
{% endfor %}

{# Remove whitespace with - #}
{%- for item in items %}
- {{ item }}
{%- endfor %}
```

### Macros (Reusable Functions)

```jinja2
{% macro server_block(name, port, root) %}
server {
    listen {{ port }};
    server_name {{ name }};
    root {{ root }};

    location / {
        try_files $uri $uri/ =404;
    }
}
{% endmacro %}

# Use macro
{{ server_block('web01.example.com', 80, '/var/www/web01') }}
{{ server_block('web02.example.com', 80, '/var/www/web02') }}
```

### Set Variables in Template

```jinja2
{% set workers = ansible_processor_vcpus * 2 %}
{% set max_connections = workers * 1024 %}

worker_processes {{ workers }};
worker_connections {{ max_connections }};
```

---

## Complete Example: nginx.conf.j2

```jinja2
# {{ ansible_managed }}
# Generated on {{ ansible_date_time.iso8601 }}

user {{ nginx_user | default('www-data') }};
worker_processes {{ nginx_workers | default(ansible_processor_vcpus) }};
pid /run/nginx.pid;

events {
    worker_connections {{ nginx_connections | default(1024) }};
    multi_accept on;
}

http {
    # Basic settings
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout {{ nginx_keepalive | default(65) }};

    # Logging
    access_log {{ nginx_access_log | default('/var/log/nginx/access.log') }};
    error_log {{ nginx_error_log | default('/var/log/nginx/error.log') }};

    # Gzip
{% if nginx_gzip_enabled | default(true) %}
    gzip on;
    gzip_types text/plain application/json application/javascript text/css;
    gzip_min_length 1000;
{% endif %}

    # Upstream backends
{% if upstream_servers is defined and upstream_servers | length > 0 %}
    upstream backend {
{% for server in upstream_servers %}
        server {{ server.host }}:{{ server.port }}{% if server.weight is defined %} weight={{ server.weight }}{% endif %};
{% endfor %}
    }
{% endif %}

    # Virtual hosts
{% for vhost in virtual_hosts | default([]) %}
    server {
        listen {{ vhost.port | default(80) }}{% if vhost.ssl | default(false) %} ssl{% endif %};
        server_name {{ vhost.server_name }};
        root {{ vhost.root | default('/var/www/html') }};

{% if vhost.ssl | default(false) %}
        ssl_certificate {{ vhost.ssl_cert }};
        ssl_certificate_key {{ vhost.ssl_key }};
        ssl_protocols TLSv1.2 TLSv1.3;
{% endif %}

{% for location in vhost.locations | default([]) %}
        location {{ location.path }} {
{% if location.proxy_pass is defined %}
            proxy_pass {{ location.proxy_pass }};
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
{% else %}
            try_files $uri $uri/ =404;
{% endif %}
        }
{% endfor %}
    }

{% endfor %}
}
```

---

## Template Module Usage

```yaml
- name: Deploy nginx configuration
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
    backup: true
    validate: 'nginx -t -c %s'
  notify: Reload nginx
```

---

## Sammanfattning

| Feature | Syntax |
|---------|--------|
| Variable | `{{ var }}` |
| Conditional | `{% if %}...{% endif %}` |
| Loop | `{% for x in list %}...{% endfor %}` |
| Comment | `{# comment #}` |
| Filter | `{{ var \| filter }}` |
| Macro | `{% macro name() %}...{% endmacro %}` |

---

## Nästa Steg

Nu kan du skapa dynamiska config-filer. Nästa: **Ansible Galaxy** — community roles och collections.
''',
}

NODE_11_ANSIBLE_GALAXY = {
    "node_id": 11,
    "title": "Ansible Galaxy",
    "slug": "ansible-galaxy",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [9],
    "content": r'''
# Ansible Galaxy

## Varför detta är kritiskt

> "Varför skriva en nginx-role från scratch när 100+ redan finns? Galaxy ger dig tillgång till tusentals testade, community-driven roles. Arbeta smart, inte hårt."

**Galaxy ecosystem:**
- **3000+** community roles
- **500+** certified collections
- Versionshantering
- Dependencies-hantering
- Kvalitetsbetyg

---

## Galaxy Koncept

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         GALAXY ECOSYSTEM                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ROLES (Legacy)                    COLLECTIONS (Modern)                 │
│  ─────────────                     ──────────────────                   │
│  Single-purpose                    Multi-purpose                        │
│  Namespace.rolename                Namespace.collection                 │
│  galaxy.ansible.com                galaxy.ansible.com                   │
│                                                                         │
│  Example:                          Example:                             │
│  geerlingguy.docker                community.docker                     │
│  geerlingguy.nginx                 amazon.aws                           │
│                                    kubernetes.core                      │
│                                                                         │
│  COLLECTION INNEHÅLLER:                                                 │
│  ├── Roles                                                              │
│  ├── Modules                                                            │
│  ├── Plugins                                                            │
│  └── Playbooks                                                          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Installera Roles

### Från Galaxy

```bash
# Basic installation
ansible-galaxy install geerlingguy.docker

# Specifik version
ansible-galaxy install geerlingguy.docker,6.1.0

# Till specifik path
ansible-galaxy install geerlingguy.nginx -p ./roles/

# Lista installerade roles
ansible-galaxy list

# Remove role
ansible-galaxy remove geerlingguy.docker
```

### Från Git

```bash
# GitHub
ansible-galaxy install git+https://github.com/geerlingguy/ansible-role-docker.git

# Med version (tag/branch)
ansible-galaxy install git+https://github.com/org/repo.git,v1.2.0

# Private repo med SSH
ansible-galaxy install git+git@github.com:company/private-role.git
```

---

## Installera Collections

```bash
# Basic installation
ansible-galaxy collection install community.docker

# Specifik version
ansible-galaxy collection install community.docker:3.4.0

# Version range
ansible-galaxy collection install 'community.general:>=5.0.0,<6.0.0'

# Lista collections
ansible-galaxy collection list

# Visa collection info
ansible-galaxy collection list community.docker
```

---

## Requirements File

### requirements.yml

```yaml
---
# ROLES
roles:
  # From Galaxy
  - name: geerlingguy.docker
    version: 6.1.0

  - name: geerlingguy.nginx

  # From GitHub
  - name: custom_nginx
    src: git+https://github.com/company/ansible-role-nginx.git
    version: v2.0.0

  # From private Git
  - name: internal_role
    src: git@gitlab.company.com:ansible/internal-role.git
    scm: git
    version: main

# COLLECTIONS
collections:
  # From Galaxy
  - name: community.docker
    version: ">=3.0.0"

  - name: community.general
    version: ">=6.0.0"

  - name: amazon.aws
    version: 5.4.0

  - name: kubernetes.core

  # From Automation Hub (requires auth)
  - name: redhat.rhel_system_roles
    source: https://cloud.redhat.com/api/automation-hub/
```

### Installera från requirements

```bash
# Install both roles and collections
ansible-galaxy install -r requirements.yml

# Only roles
ansible-galaxy role install -r requirements.yml

# Only collections
ansible-galaxy collection install -r requirements.yml

# Force reinstall
ansible-galaxy install -r requirements.yml --force
```

---

## Använda Collections

### FQCN (Fully Qualified Collection Name)

```yaml
---
- name: Use collection modules
  hosts: all

  tasks:
    # FQCN format: namespace.collection.module
    - name: Create Docker container
      community.docker.docker_container:
        name: nginx
        image: nginx:latest
        state: started
        ports:
          - "80:80"

    - name: Create AWS S3 bucket
      amazon.aws.s3_bucket:
        name: my-bucket
        state: present
        region: eu-north-1

    - name: Apply Kubernetes manifest
      kubernetes.core.k8s:
        state: present
        definition:
          apiVersion: v1
          kind: Pod
          metadata:
            name: nginx
          spec:
            containers:
              - name: nginx
                image: nginx
```

### collections Keyword

```yaml
---
- name: With collections keyword
  hosts: all
  collections:
    - community.docker
    - amazon.aws

  tasks:
    # Nu kan du skippa namespace prefix
    - name: Create container
      docker_container:
        name: nginx
        image: nginx:latest

    - name: Create bucket
      s3_bucket:
        name: my-bucket
```

---

## Populära Collections

| Collection | Innehåll |
|------------|----------|
| `community.general` | 100+ utility modules |
| `community.docker` | Docker management |
| `community.mysql` | MySQL/MariaDB |
| `community.postgresql` | PostgreSQL |
| `amazon.aws` | AWS services |
| `google.cloud` | GCP services |
| `azure.azcollection` | Azure services |
| `kubernetes.core` | K8s management |
| `ansible.posix` | POSIX modules |
| `ansible.netcommon` | Network automation |

---

## Galaxy Role Quality

### Välja rätt role

```bash
# Sök roles
ansible-galaxy search nginx

# Visa role info
ansible-galaxy info geerlingguy.nginx
```

**Kvalitetskriterier:**
- ⭐ GitHub stars
- 📥 Download count
- 🔄 Recent updates
- 📝 Good documentation
- 🧪 CI/CD testing
- 🏷️ Proper versioning

### Rekommenderade författare

| Author | Specialitet |
|--------|-------------|
| `geerlingguy` | Infrastructure (nginx, docker, mysql) |
| `jdauphant` | Security |
| `dev-sec` | Hardening |
| `elastic` | ELK stack |
| `oefenweb` | Various services |

---

## Publicera egen Role

### meta/main.yml krav

```yaml
---
galaxy_info:
  author: your_name
  description: Brief description of the role
  company: Optional company name
  license: MIT

  min_ansible_version: "2.10"

  platforms:
    - name: Ubuntu
      versions:
        - focal
        - jammy
    - name: Debian
      versions:
        - bullseye
        - bookworm
    - name: EL
      versions:
        - "8"
        - "9"

  galaxy_tags:
    - nginx
    - webserver
    - proxy
    - load-balancer

dependencies: []
```

### Publicera

```bash
# Login med GitHub token
ansible-galaxy login --github-token YOUR_TOKEN

# Import role från GitHub
ansible-galaxy import your_username your_role_repo

# Role måste ha:
# - meta/main.yml med galaxy_info
# - README.md
# - GitHub releases/tags för versioner
```

---

## Collection Development

### Skapa collection

```bash
# Initialize
ansible-galaxy collection init my_namespace.my_collection

# Struktur
my_namespace/my_collection/
├── docs/
├── galaxy.yml
├── plugins/
│   ├── modules/
│   └── lookup/
├── roles/
└── README.md
```

### galaxy.yml

```yaml
namespace: my_namespace
name: my_collection
version: 1.0.0
readme: README.md
authors:
  - Your Name <email@example.com>
description: My custom collection
license_file: LICENSE
tags:
  - infrastructure
  - devops
dependencies:
  community.general: ">=5.0.0"
repository: https://github.com/you/collection
```

### Build och publicera

```bash
# Build
ansible-galaxy collection build

# Publish to Galaxy
ansible-galaxy collection publish my_namespace-my_collection-1.0.0.tar.gz

# Install local
ansible-galaxy collection install ./my_namespace-my_collection-1.0.0.tar.gz
```

---

## Best Practices

### requirements.yml i projekt

```yaml
# requirements.yml
---
collections:
  - name: community.docker
    version: ">=3.0.0,<4.0.0"  # Pin to major version
  - name: amazon.aws
    version: 5.4.0  # Pin exact for prod

roles:
  - name: geerlingguy.docker
    version: 6.1.0  # Always pin versions
```

### CI/CD Integration

```yaml
# .github/workflows/ansible.yml
- name: Install dependencies
  run: |
    ansible-galaxy collection install -r requirements.yml
    ansible-galaxy role install -r requirements.yml
```

---

## Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| Roles | Single-purpose automation |
| Collections | Multi-purpose packages |
| requirements.yml | Dependency management |
| FQCN | Full module path |
| Galaxy | Community hub |

---

## Nästa Steg

Nu kan du använda community-resurser. Nästa: **Ansible Vault** — kryptera känslig data.
''',
}

NODE_12_ANSIBLE_VAULT = {
    "node_id": 12,
    "title": "Ansible Vault",
    "slug": "ansible-vault",
    "estimated_minutes": 55,
    "xp_reward": 145,
    "prerequisites": [6],
    "content": r'''
# Ansible Vault

## Varför detta är kritiskt

> "Lösenord i plaintext = säkerhetsincident. Vault krypterar känslig data med AES256. Ingen ursäkt att ha secrets i klartext."

**Vault skyddar:**
- Lösenord
- API-nycklar
- SSL-certifikat
- Databas-credentials
- SSH-nycklar

---

## Vault Arkitektur

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        ANSIBLE VAULT FLOW                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   PLAINTEXT                 ENCRYPTION                VAULT FILE        │
│   ─────────                 ──────────                ──────────        │
│   db_password: secret123    ───────────►    $ANSIBLE_VAULT;1.2;AES256   │
│                                             6238...encrypted...data     │
│                                                                         │
│                                                                         │
│   DECRYPTION METHODS:                                                   │
│   ┌─────────────────┬────────────────────┬─────────────────────────┐    │
│   │ --ask-vault-pass│ --vault-password-  │ ANSIBLE_VAULT_PASSWORD_ │    │
│   │ (interactive)   │ file (automation)  │ FILE env var            │    │
│   └─────────────────┴────────────────────┴─────────────────────────┘    │
│                                                                         │
│   VAULT IDs:                                                            │
│   ├── dev@dev_vault_pass                                                │
│   ├── staging@staging_vault_pass                                        │
│   └── prod@prod_vault_pass                                              │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Skapa Vault-krypterade filer

### Ny krypterad fil

```bash
# Skapa med interaktiv prompt
ansible-vault create secrets.yml
# Öppnar $EDITOR för att skriva innehåll

# Med specifik vault-id
ansible-vault create --vault-id prod@prompt secrets_prod.yml

# Med password-file
ansible-vault create --vault-password-file .vault_pass secrets.yml
```

### Kryptera existerande fil

```bash
# Kryptera hela filen
ansible-vault encrypt vars/credentials.yml

# Output till ny fil
ansible-vault encrypt vars/plain.yml --output vars/encrypted.yml

# Kryptera med vault-id
ansible-vault encrypt --vault-id prod@prompt vars/prod_secrets.yml
```

---

## Hantera krypterade filer

### View & Edit

```bash
# Visa innehåll (utan att ändra)
ansible-vault view secrets.yml

# Redigera
ansible-vault edit secrets.yml

# Decrypt permanent
ansible-vault decrypt secrets.yml

# Rekey (ändra lösenord)
ansible-vault rekey secrets.yml
ansible-vault rekey --new-vault-id prod@prompt secrets.yml
```

### Verifiera

```bash
# Kontrollera om fil är krypterad
head -1 secrets.yml
# Output: $ANSIBLE_VAULT;1.2;AES256;...
```

---

## Encrypt String (inline)

### Enskilda värden

```bash
# Basic encryption
ansible-vault encrypt_string 'SuperSecret123!' --name 'db_password'

# Output:
db_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          62383433643765636530653964373136...

# Med vault-id
ansible-vault encrypt_string --vault-id prod@prompt 'secret' --name 'api_key'

# Från stdin (säkrare)
echo -n 'my_password' | ansible-vault encrypt_string --stdin-name 'password'
```

### Användning i vars

```yaml
# group_vars/production.yml
---
app_name: myapp
environment: production

# Encrypted inline
db_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          62383433643765636530653964373136396266343139373239653165313932
          6639363039653739376563653934616430626461333263320a366165363963
          39616634373536386564316434653337333735616664356566656630313962
          3663326334343062370a643234323731353931363765613030633233313763

api_key: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          ...encrypted...

# Plaintext values can coexist
log_level: info
```

---

## Köra Playbooks med Vault

### Interaktivt

```bash
# Fråga efter lösenord
ansible-playbook deploy.yml --ask-vault-pass

# Kort flag
ansible-playbook deploy.yml -J
```

### Med password-file

```bash
# Skapa password-fil
echo "YourVaultPassword" > .vault_pass
chmod 600 .vault_pass
echo ".vault_pass" >> .gitignore

# Använd vid körning
ansible-playbook deploy.yml --vault-password-file .vault_pass

# I ansible.cfg
[defaults]
vault_password_file = .vault_pass
```

### Environment Variable

```bash
# Set env var
export ANSIBLE_VAULT_PASSWORD_FILE=/path/to/.vault_pass

# Körs utan extra flags
ansible-playbook deploy.yml
```

---

## Multiple Vault IDs

### Scenario: Dev vs Prod secrets

```bash
# Skapa dev secrets
ansible-vault create --vault-id dev@.vault_pass_dev group_vars/dev/vault.yml

# Skapa prod secrets
ansible-vault create --vault-id prod@.vault_pass_prod group_vars/prod/vault.yml

# Edit med rätt id
ansible-vault edit --vault-id prod@.vault_pass_prod group_vars/prod/vault.yml
```

### Köra med multiple vaults

```bash
# Båda vault-ids
ansible-playbook site.yml \
  --vault-id dev@.vault_pass_dev \
  --vault-id prod@.vault_pass_prod

# ansible.cfg
[defaults]
vault_identity_list = dev@.vault_pass_dev, prod@.vault_pass_prod
```

---

## Projektstruktur med Vault

### Best Practice Layout

```
project/
├── ansible.cfg
├── .vault_pass              # ❌ ALDRIG I GIT
├── .gitignore               # Exkludera .vault_pass
├── inventory/
│   ├── production
│   └── staging
├── group_vars/
│   ├── all/
│   │   ├── vars.yml         # Ej krypterat
│   │   └── vault.yml        # Krypterat (secrets)
│   ├── production/
│   │   ├── vars.yml         # Environment-specific vars
│   │   └── vault.yml        # Environment-specific secrets
│   └── staging/
│       ├── vars.yml
│       └── vault.yml
├── playbooks/
└── roles/
```

### Separera vars och vault

```yaml
# group_vars/production/vars.yml (plaintext)
---
db_host: db.prod.example.com
db_port: 5432
db_name: production_db
db_user: app_user
# Reference vault variable
db_password: "{{ vault_db_password }}"

# group_vars/production/vault.yml (encrypted)
---
vault_db_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          ...

vault_api_key: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          ...

vault_ssl_private_key: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          ...
```

---

## CI/CD Integration

### GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Create vault password file
        run: echo "${{ secrets.ANSIBLE_VAULT_PASSWORD }}" > .vault_pass

      - name: Run playbook
        run: |
          ansible-playbook deploy.yml \
            --vault-password-file .vault_pass \
            -i inventory/production

      - name: Cleanup
        if: always()
        run: rm -f .vault_pass
```

### GitLab CI

```yaml
# .gitlab-ci.yml
deploy:
  stage: deploy
  script:
    - echo "$VAULT_PASSWORD" > .vault_pass
    - ansible-playbook deploy.yml --vault-password-file .vault_pass
  after_script:
    - rm -f .vault_pass
```

---

## Felsökning

| Problem | Lösning |
|---------|---------|
| `ERROR! Decryption failed` | Fel vault-lösenord |
| `no vault secrets found` | Glömt --ask-vault-pass |
| `ERROR! input is not vault encrypted` | Filen är inte krypterad |
| `vault password required` | Vault-ID mismatch |

### Debug commands

```bash
# Kontrollera encryption header
head -1 secrets.yml

# Verify vault-id
ansible-vault view --vault-id prod@prompt secrets.yml

# Test decryption
ansible-vault decrypt --output /dev/stdout secrets.yml
```

---

## Säkerhets Best Practices

### DO ✅

```bash
# Använd starka lösenord
openssl rand -base64 32 > .vault_pass

# Strikt permissions
chmod 600 .vault_pass

# Separata vault-ids per miljö
--vault-id dev@... --vault-id prod@...

# Använd vault för:
# - Lösenord
# - API-nycklar
# - Certifikat
# - SSH-nycklar
```

### DON'T ❌

```bash
# ALDRIG committa vault password
git add .vault_pass  # ABSOLUT FEL

# ALDRIG plaintext secrets
db_password: password123  # ALDRIG

# ALDRIG samma vault för alla miljöer
# (dev kan läsa prod secrets)
```

---

## Praktisk Övning

Implementera secrets-hantering:

```bash
# 1. Skapa vault password
openssl rand -base64 32 > .vault_pass
chmod 600 .vault_pass
echo ".vault_pass" >> .gitignore

# 2. Skapa krypterad secrets-fil
ansible-vault create --vault-password-file .vault_pass group_vars/all/vault.yml

# 3. Lägg till secrets
vault_db_password: SecurePass123!
vault_api_key: sk-abc123...

# 4. Referera i vars.yml
db_password: "{{ vault_db_password }}"

# 5. Kör playbook
ansible-playbook site.yml --vault-password-file .vault_pass
```

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `create` | Ny krypterad fil |
| `encrypt` | Kryptera existerande |
| `decrypt` | Permanent dekryptering |
| `edit` | Redigera krypterad |
| `view` | Visa utan ändring |
| `rekey` | Byt lösenord |
| `encrypt_string` | Inline encryption |

---

## Nästa Steg

Secrets är säkra. Nästa block: **Ansible Modules Deep Dive** — specifika moduler för verkliga uppgifter.
''',
}

ANSIBLE_BLOCK_3 = [
    NODE_09_ROLES,
    NODE_10_TEMPLATES,
    NODE_11_ANSIBLE_GALAXY,
    NODE_12_ANSIBLE_VAULT,
]
