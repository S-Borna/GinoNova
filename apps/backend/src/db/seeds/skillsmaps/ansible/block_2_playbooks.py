# =============================================================================
# BLOCK 2: PLAYBOOKS (Noder 5-8)
# =============================================================================

NODE_05_TASKS_MODULES = {
    "node_id": 5,
    "title": "Tasks & Modules",
    "slug": "tasks-modules",
    "estimated_minutes": 60,
    "xp_reward": 140,
    "prerequisites": [4],
    "content": r'''
# Tasks & Modules

## Varför detta är kritiskt

> "En task är en atomär handling - installera ett paket, skapa en fil, starta en tjänst. Modules är verktygen som utför dessa handlingar. Bemästra dem och du bemästrar Ansible."

Ansible har över **3000 moduler** för allt från att installera paket till att konfigurera Kubernetes-kluster. Men du behöver bara cirka 20-30 för 90% av alla uppgifter.

---

## Task Anatomy

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          TASK STRUKTUR                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  - name: Install nginx                    ← BESKRIVNING (viktigt!)      │
│    apt:                                   ← MODUL                       │
│      name: nginx                          ← MODUL-PARAMETER             │
│      state: present                       ← MODUL-PARAMETER             │
│    become: true                           ← TASK KEYWORD                │
│    when: ansible_os_family == "Debian"    ← VILLKOR                     │
│    tags:                                  ← TAGGAR                      │
│      - packages                                                         │
│      - nginx                                                            │
│    register: nginx_install                ← SPARA RESULTAT              │
│    notify: Restart nginx                  ← TRIGGA HANDLER              │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Package Management Modules

### apt (Debian/Ubuntu)

```yaml
# Installera ett paket
- name: Install nginx
  apt:
    name: nginx
    state: present

# Installera flera paket
- name: Install web stack
  apt:
    name:
      - nginx
      - php-fpm
      - php-mysql
      - certbot
    state: present
    update_cache: true
    cache_valid_time: 3600  # Cache i 1 timme

# Installera specifik version
- name: Install specific version
  apt:
    name: nginx=1.18.0-0ubuntu1
    state: present

# Uppgradera alla paket
- name: Full system upgrade
  apt:
    upgrade: dist
    update_cache: true

# Ta bort paket (med dependencies)
- name: Remove package completely
  apt:
    name: apache2
    state: absent
    purge: true
    autoremove: true

# Installera .deb fil
- name: Install local package
  apt:
    deb: /tmp/package.deb
```

### yum/dnf (RHEL/CentOS)

```yaml
# YUM (CentOS 7)
- name: Install httpd
  yum:
    name: httpd
    state: latest

# DNF (CentOS 8+, Fedora)
- name: Install httpd
  dnf:
    name:
      - httpd
      - mod_ssl
    state: present

# Med EPEL repository
- name: Enable EPEL and install
  yum:
    name: epel-release
    state: present

- name: Install from EPEL
  yum:
    name: htop
    state: present
```

### package (Cross-platform)

```yaml
# Auto-detect pakethanterare
- name: Install vim
  package:
    name: vim
    state: present
```

| Parameter | Värden | Beskrivning |
|-----------|--------|-------------|
| `name` | paketnamn | Ett eller flera paket |
| `state` | present/absent/latest | Önskat tillstånd |
| `update_cache` | true/false | Uppdatera cache först |
| `cache_valid_time` | sekunder | Cache TTL |
| `purge` | true/false | Ta bort config-filer |

---

## File Management Modules

### copy

```yaml
# Kopiera fil från control node
- name: Copy nginx config
  copy:
    src: files/nginx.conf
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
    backup: true  # Skapa backup före överskrivning

# Kopiera med innehåll direkt
- name: Create motd
  copy:
    content: |
      ==============================
      Welcome to {{ inventory_hostname }}
      Environment: {{ env }}
      ==============================
    dest: /etc/motd
    mode: '0644'

# Kopiera directory
- name: Copy entire config directory
  copy:
    src: configs/
    dest: /etc/myapp/
    owner: app
    mode: '0755'
    directory_mode: '0755'
```

### template

```yaml
# Jinja2 template
- name: Deploy nginx config from template
  template:
    src: templates/nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
    validate: 'nginx -t -c %s'  # Validera innan deploy
  notify: Reload nginx
```

```jinja2
# templates/nginx.conf.j2
worker_processes {{ ansible_processor_vcpus }};

http {
    server {
        listen {{ http_port }};
        server_name {{ server_name }};
        root {{ web_root }};

        {% for location in locations %}
        location {{ location.path }} {
            proxy_pass {{ location.backend }};
        }
        {% endfor %}
    }
}
```

### file

```yaml
# Skapa directory
- name: Create app directories
  file:
    path: "{{ item }}"
    state: directory
    owner: app
    group: app
    mode: '0755'
  loop:
    - /opt/myapp
    - /opt/myapp/logs
    - /opt/myapp/data
    - /opt/myapp/config

# Skapa symlink
- name: Create symlink to current version
  file:
    src: /opt/myapp/releases/v1.2.3
    dest: /opt/myapp/current
    state: link

# Ta bort fil/directory
- name: Remove old logs
  file:
    path: /var/log/myapp/old
    state: absent

# Ändra permissions
- name: Set permissions on sensitive file
  file:
    path: /etc/myapp/secrets.yml
    mode: '0600'
    owner: root

# Skapa tom fil (touch)
- name: Create marker file
  file:
    path: /tmp/ansible_was_here
    state: touch
    mode: '0644'
```

### lineinfile & blockinfile

```yaml
# Lägg till/ändra en rad
- name: Ensure sudo without password for deploy
  lineinfile:
    path: /etc/sudoers
    line: 'deploy ALL=(ALL) NOPASSWD: ALL'
    validate: 'visudo -cf %s'

# Ersätt rad baserat på regex
- name: Update sshd config
  lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^#?PermitRootLogin'
    line: 'PermitRootLogin no'
  notify: Restart sshd

# Lägg till block av rader
- name: Add custom hosts
  blockinfile:
    path: /etc/hosts
    block: |
      192.168.1.10 web01
      192.168.1.11 web02
      192.168.1.20 db01
    marker: "# {mark} ANSIBLE MANAGED - Custom hosts"
```

---

## Service Management Modules

### service & systemd

```yaml
# Generic service module
- name: Ensure nginx is running
  service:
    name: nginx
    state: started
    enabled: true

# Systemd-specifik (mer kontroll)
- name: Restart app with systemd
  systemd:
    name: myapp
    state: restarted
    daemon_reload: true  # Om unit file ändrats
    enabled: true

# Systemd states
- name: Various service states
  systemd:
    name: nginx
    state: "{{ item }}"
  loop:
    - started   # Starta om inte igång
    - stopped   # Stoppa
    - restarted # Alltid restart
    - reloaded  # Reload config
```

| State | Beskrivning |
|-------|-------------|
| `started` | Starta om ej igång |
| `stopped` | Stoppa tjänsten |
| `restarted` | Stoppa + starta |
| `reloaded` | Ladda om config |

---

## User & Group Modules

```yaml
# Skapa användare
- name: Create application user
  user:
    name: deploy
    comment: "Deployment user"
    groups: sudo,docker
    append: true  # Behåll befintliga grupper
    shell: /bin/bash
    create_home: true
    home: /home/deploy
    password: "{{ 'secret' | password_hash('sha512') }}"

# Skapa systemanvändare (ingen login)
- name: Create service account
  user:
    name: myapp
    system: true
    shell: /usr/sbin/nologin
    create_home: false

# Ta bort användare
- name: Remove old user
  user:
    name: olduser
    state: absent
    remove: true  # Ta bort home directory

# SSH authorized_key
- name: Deploy SSH key
  authorized_key:
    user: deploy
    state: present
    key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"

# Skapa grupp
- name: Create developers group
  group:
    name: developers
    gid: 1500
    state: present
```

---

## Command & Shell Modules

### När ska du använda vad?

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    COMMAND vs SHELL vs RAW                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  COMMAND (säkrast)                                                      │
│  ├── Kör utan shell                                                     │
│  ├── Ingen pipe/redirect                                                │
│  └── Ingen env vars expansion                                           │
│                                                                         │
│  SHELL (flexibelt)                                                      │
│  ├── Full shell (/bin/sh)                                              │
│  ├── Pipes, redirects                                                   │
│  └── Variabel expansion                                                 │
│                                                                         │
│  RAW (minimalt)                                                         │
│  ├── Ingen Python krävs på target                                       │
│  └── Bootstrap-situationer                                              │
│                                                                         │
│  SCRIPT (skicka och kör)                                               │
│  ├── Kopiera lokalt script                                             │
│  └── Kör på remote                                                      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

```yaml
# Command - enkla kommandon
- name: Check disk space
  command: df -h /
  register: disk_result
  changed_when: false  # Rapportera aldrig changed

# Shell - behöver pipes/redirects
- name: Find large log files
  shell: find /var/log -type f -size +100M | head -10
  register: large_logs

# Med environment variables
- name: Run with env
  shell: echo $MY_VAR
  environment:
    MY_VAR: "hello"

# Kör bara om fil saknas
- name: Initialize database
  command: /opt/app/init-db.sh
  args:
    creates: /opt/app/.db_initialized

# Kör bara om fil finns
- name: Remove temp files
  command: rm -rf /tmp/myapp/*
  args:
    removes: /tmp/myapp

# Script module
- name: Run local script on remote
  script: scripts/setup.sh arg1 arg2
  args:
    creates: /opt/app/.setup_complete
```

---

## Network Modules

### get_url

```yaml
# Ladda ner fil
- name: Download application
  get_url:
    url: https://releases.example.com/app-v1.2.3.tar.gz
    dest: /tmp/app.tar.gz
    checksum: sha256:a1b2c3d4...
    mode: '0644'
    timeout: 30

# Med authentication
- name: Download from private repo
  get_url:
    url: https://private.repo/file.tar.gz
    dest: /tmp/file.tar.gz
    url_username: user
    url_password: "{{ repo_password }}"
```

### uri (HTTP requests)

```yaml
# Health check
- name: Check application health
  uri:
    url: http://localhost:8080/health
    method: GET
    status_code: 200
    timeout: 5
  register: health_check
  retries: 5
  delay: 10
  until: health_check.status == 200

# POST request
- name: Create resource via API
  uri:
    url: https://api.example.com/users
    method: POST
    body_format: json
    body:
      name: "{{ user_name }}"
      email: "{{ user_email }}"
    headers:
      Authorization: "Bearer {{ api_token }}"
    status_code: 201
```

---

## Practical Example: Full Web Server Setup

```yaml
---
- name: Configure production web server
  hosts: webservers
  become: true

  vars:
    app_name: myapp
    app_user: deploy
    app_port: 8080

  tasks:
    - name: Update apt cache
      apt:
        update_cache: true
        cache_valid_time: 3600
      tags: packages

    - name: Install required packages
      apt:
        name:
          - nginx
          - python3
          - python3-pip
          - supervisor
        state: present
      tags: packages

    - name: Create application user
      user:
        name: "{{ app_user }}"
        system: true
        shell: /bin/bash
        home: "/home/{{ app_user }}"
        create_home: true
      tags: setup

    - name: Create application directories
      file:
        path: "{{ item }}"
        state: directory
        owner: "{{ app_user }}"
        mode: '0755'
      loop:
        - /opt/{{ app_name }}
        - /opt/{{ app_name }}/releases
        - /opt/{{ app_name }}/shared
        - /var/log/{{ app_name }}
      tags: setup

    - name: Deploy nginx configuration
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/sites-available/{{ app_name }}
        mode: '0644'
      notify: Reload nginx
      tags: config

    - name: Enable site
      file:
        src: /etc/nginx/sites-available/{{ app_name }}
        dest: /etc/nginx/sites-enabled/{{ app_name }}
        state: link
      notify: Reload nginx
      tags: config

    - name: Ensure nginx is running
      service:
        name: nginx
        state: started
        enabled: true
      tags: service

  handlers:
    - name: Reload nginx
      service:
        name: nginx
        state: reloaded
```

---

## Sammanfattning

| Modul | Användning |
|-------|------------|
| `apt/yum/package` | Pakethantering |
| `copy` | Kopiera filer |
| `template` | Jinja2 templates |
| `file` | Skapa/ta bort filer/dirs |
| `lineinfile` | Ändra enskilda rader |
| `service/systemd` | Tjänsthantering |
| `user/group` | Användarhantering |
| `command/shell` | Köra kommandon |
| `get_url/uri` | HTTP-operationer |

---

## Nästa Steg

Du kan nu använda de viktigaste modulerna. Nästa: **Variables** — gör dina playbooks dynamiska och återanvändbara.
''',
}

NODE_06_VARIABLES = {
    "node_id": 6,
    "title": "Variables & Facts",
    "slug": "variables",
    "estimated_minutes": 60,
    "xp_reward": 145,
    "prerequisites": [5],
    "content": r'''
# Variables & Facts

## Varför detta är kritiskt

> "Hardcoded värden = teknisk skuld. Variabler = flexibilitet. Samma playbook kan deploya till dev, staging och production genom att bara ändra variabler."

Tänk dig: Du har samma applikation som ska köras i 3 miljöer med olika databaslösenord, portar och domännamn. Med variabler skriver du playbooken EN gång.

---

## Variable Typer och Scope

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      VARIABLE PRECEDENCE                                │
│                    (Lägst till Högst Prioritet)                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  1.  role defaults              roles/x/defaults/main.yml               │
│  2.  inventory file vars        [group:vars] i inventory                │
│  3.  inventory group_vars/all   group_vars/all.yml                      │
│  4.  inventory group_vars/*     group_vars/webservers.yml               │
│  5.  inventory host_vars/*      host_vars/web01.yml                     │
│  6.  play vars                  vars: i playbook                        │
│  7.  play vars_prompt           interaktiv input                        │
│  8.  play vars_files            vars_files: [vars.yml]                  │
│  9.  role vars                  roles/x/vars/main.yml                   │
│  10. block vars                 vars: i block                           │
│  11. task vars                  vars: i task                            │
│  12. include_vars               dynamiskt inkluderade                   │
│  13. set_facts/registered       runtime-genererade                      │
│  14. extra vars (-e)            HÖGST PRIORITET                         │
│                                                                         │
│  REGEL: Mer specifik = högre prioritet                                  │
│  REGEL: -e överskriver ALLT                                            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Definiera Variables

### I Playbook (play vars)

```yaml
---
- name: Configure application
  hosts: webservers

  vars:
    # Enkla variabler
    app_name: myapp
    http_port: 80
    enable_ssl: true

    # Lista
    packages:
      - nginx
      - python3
      - supervisor

    # Dictionary
    database:
      host: db.example.com
      port: 5432
      name: production_db
      user: app_user

    # Nested structures
    environments:
      production:
        debug: false
        log_level: warn
      staging:
        debug: true
        log_level: debug
```

### I Separata Filer (vars_files)

```yaml
# vars/common.yml
app_name: myapp
company: DevOpsHub

# vars/production.yml
env: production
debug: false
db_host: prod-db.internal

# vars/secrets.yml (kryptera med ansible-vault!)
db_password: supersecret123
api_key: abc123xyz
```

```yaml
# playbook.yml
---
- name: Deploy application
  hosts: webservers
  vars_files:
    - vars/common.yml
    - "vars/{{ env }}.yml"
    - vars/secrets.yml
```

### I Inventory (group_vars & host_vars)

```
project/
├── inventory.yml
├── group_vars/
│   ├── all.yml                 # Gäller ALLA hosts
│   ├── webservers.yml          # Gäller webservers-gruppen
│   ├── databases.yml           # Gäller databases-gruppen
│   └── production/             # Directory = samma som fil
│       ├── vars.yml
│       └── vault.yml           # Krypterade secrets
└── host_vars/
    ├── web01.yml               # Endast för web01
    └── db01.yml                # Endast för db01
```

```yaml
# group_vars/all.yml
---
ntp_server: time.google.com
dns_servers:
  - 8.8.8.8
  - 8.8.4.4
timezone: Europe/Stockholm
ssh_port: 22

# group_vars/webservers.yml
---
nginx_worker_processes: auto
nginx_worker_connections: 1024
nginx_keepalive_timeout: 65
ssl_protocols: "TLSv1.2 TLSv1.3"

# host_vars/web01.yml
---
nginx_worker_processes: 4  # Överskriver webservers.yml
primary_server: true
```

---

## Använda Variables

### Basic Syntax

```yaml
tasks:
  # Enkel variabel
  - name: Install application
    apt:
      name: "{{ app_name }}"
      state: present

  # Variabel i sträng
  - name: Create config path
    file:
      path: "/etc/{{ app_name }}/config"
      state: directory

  # Dictionary access
  - name: Connect to database
    postgresql_db:
      name: "{{ database.name }}"
      login_host: "{{ database.host }}"
      login_user: "{{ database.user }}"

  # Lista iteration
  - name: Install packages
    apt:
      name: "{{ item }}"
    loop: "{{ packages }}"
```

### Default Values

```yaml
# Om variabeln inte finns, använd default
- name: Set port
  debug:
    msg: "Port: {{ http_port | default(80) }}"

# Fail om variabeln saknas
- name: Require variable
  debug:
    msg: "API key: {{ api_key | mandatory }}"

# Kontrollera om variabel finns
- name: Conditional task
  debug:
    msg: "Using custom port"
  when: custom_port is defined
```

### Jinja2 Filters

```yaml
tasks:
  # String manipulation
  - debug:
      msg: "{{ app_name | upper }}"           # MYAPP
  - debug:
      msg: "{{ app_name | capitalize }}"      # Myapp
  - debug:
      msg: "{{ 'hello world' | replace(' ', '_') }}"  # hello_world

  # Lista operationer
  - debug:
      msg: "{{ packages | join(', ') }}"      # nginx, python3
  - debug:
      msg: "{{ packages | first }}"           # nginx
  - debug:
      msg: "{{ packages | length }}"          # 3

  # JSON/YAML
  - debug:
      msg: "{{ database | to_json }}"
  - debug:
      msg: "{{ database | to_yaml }}"

  # Path manipulation
  - debug:
      msg: "{{ '/etc/nginx/nginx.conf' | basename }}"    # nginx.conf
  - debug:
      msg: "{{ '/etc/nginx/nginx.conf' | dirname }}"     # /etc/nginx

  # Hashing
  - debug:
      msg: "{{ 'password' | password_hash('sha512') }}"
```

---

## Ansible Facts

Facts är systeminfo som Ansible samlar automatiskt vid start.

```yaml
# Visa alla facts
- name: Gather facts
  setup:

- name: Show all facts
  debug:
    var: ansible_facts

# Vanliga facts
- name: Show common facts
  debug:
    msg: |
      Hostname: {{ ansible_hostname }}
      FQDN: {{ ansible_fqdn }}
      OS: {{ ansible_distribution }} {{ ansible_distribution_version }}
      OS Family: {{ ansible_os_family }}
      Kernel: {{ ansible_kernel }}
      Architecture: {{ ansible_architecture }}
      CPUs: {{ ansible_processor_vcpus }}
      Memory: {{ ansible_memtotal_mb }} MB
      IPv4: {{ ansible_default_ipv4.address }}
      Python: {{ ansible_python_version }}
```

### Custom Facts

```bash
# På managed node: /etc/ansible/facts.d/custom.fact
#!/bin/bash
echo '{"app_version": "1.2.3", "deployed_by": "ansible"}'
```

```yaml
# Läs custom fact
- name: Show custom fact
  debug:
    msg: "App version: {{ ansible_local.custom.app_version }}"
```

### Stäng av fact gathering (snabbare)

```yaml
---
- name: Fast playbook
  hosts: webservers
  gather_facts: false  # Skippa facts

  tasks:
    - name: Quick task
      ping:
```

---

## Registered Variables

```yaml
tasks:
  - name: Check if config exists
    stat:
      path: /etc/myapp/config.yml
    register: config_file

  - name: Show result structure
    debug:
      var: config_file

  - name: Use result
    copy:
      src: config.yml
      dest: /etc/myapp/config.yml
    when: not config_file.stat.exists

  # Command output
  - name: Get application version
    command: /opt/app/bin/app --version
    register: app_version
    changed_when: false

  - name: Show version
    debug:
      msg: "Version: {{ app_version.stdout }}"

  # Fail based on output
  - name: Check database connection
    command: pg_isready -h {{ db_host }}
    register: db_check
    failed_when: db_check.rc != 0
```

---

## set_fact Module

```yaml
tasks:
  - name: Set simple fact
    set_fact:
      deployment_time: "{{ ansible_date_time.iso8601 }}"

  - name: Calculate value
    set_fact:
      memory_threshold: "{{ (ansible_memtotal_mb * 0.8) | int }}"

  - name: Combine facts
    set_fact:
      server_info:
        hostname: "{{ ansible_hostname }}"
        ip: "{{ ansible_default_ipv4.address }}"
        env: "{{ env }}"

  - name: Build URL
    set_fact:
      api_url: "https://{{ ansible_fqdn }}:{{ api_port }}/api/v1"
```

---

## Extra Variables (-e)

```bash
# Single variable
ansible-playbook deploy.yml -e "version=1.2.3"

# Multiple variables
ansible-playbook deploy.yml -e "env=production version=1.2.3 debug=false"

# JSON format
ansible-playbook deploy.yml -e '{"env": "production", "users": ["alice", "bob"]}'

# From file
ansible-playbook deploy.yml -e "@vars/production.yml"

# Override anything (highest priority!)
ansible-playbook deploy.yml -e "http_port=8080"
```

---

## Environment Variables

```yaml
tasks:
  # Set environment for task
  - name: Run with custom environment
    command: /opt/app/run.sh
    environment:
      APP_ENV: production
      DATABASE_URL: "postgres://{{ db_user }}:{{ db_pass }}@{{ db_host }}/{{ db_name }}"
      API_KEY: "{{ api_key }}"

  # Read system environment
  - name: Get PATH
    debug:
      msg: "{{ lookup('env', 'PATH') }}"
```

---

## Practical Example: Multi-Environment Setup

```yaml
# inventory/production/hosts.yml
all:
  children:
    webservers:
      hosts:
        prod-web01:
        prod-web02:
    databases:
      hosts:
        prod-db01:

# inventory/production/group_vars/all.yml
env: production
domain: example.com
ssl_enabled: true
log_level: warn

# inventory/staging/group_vars/all.yml
env: staging
domain: staging.example.com
ssl_enabled: false
log_level: debug

# deploy.yml
---
- name: Deploy application
  hosts: webservers

  vars:
    app_name: myapp
    config_file: "/etc/{{ app_name }}/config.yml"

  tasks:
    - name: Deploy config
      template:
        src: config.yml.j2
        dest: "{{ config_file }}"
      vars:
        full_domain: "{{ app_name }}.{{ domain }}"
```

```bash
# Deploy to staging
ansible-playbook -i inventory/staging deploy.yml

# Deploy to production
ansible-playbook -i inventory/production deploy.yml

# Override for testing
ansible-playbook -i inventory/production deploy.yml -e "ssl_enabled=false"
```

---

## Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| `vars:` | Variabler i playbook |
| `vars_files:` | Ladda från filer |
| `group_vars/` | Variabler per grupp |
| `host_vars/` | Variabler per host |
| `ansible_facts` | Automatisk systeminfo |
| `register` | Spara task-resultat |
| `set_fact` | Skapa nya variabler |
| `-e` | Högsta prioritet |

---

## Nästa Steg

Nu kan du parametrisera dina playbooks. Nästa: **Handlers** — tasks som körs vid ändringar.
''',
}

NODE_07_HANDLERS = {
    "node_id": 7,
    "title": "Handlers",
    "slug": "handlers",
    "estimated_minutes": 50,
    "xp_reward": 125,
    "prerequisites": [6],
    "content": r'''
# Handlers

## Varför detta är kritiskt

> "Du uppdaterar nginx.conf. Nginx fortsätter köra med gamla config. Problem? Ja. Lösning: Handlers — tasks som triggas vid ändringar och kör automatiskt restart/reload."

Utan handlers måste du antingen:
1. Alltid restarta tjänster (onödigt, orsakar downtime)
2. Manuellt avgöra om restart behövs (felbenäget)

Med handlers: Ansible vet när config ändrades och restartar automatiskt — men BARA då.

---

## Handler Koncept

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        HANDLER FLOW                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   TASK 1: Copy nginx.conf                                              │
│   ├── Result: CHANGED ✓                                                │
│   └── notify: "Restart nginx"  ────────────────────────┐               │
│                                                         │               │
│   TASK 2: Copy site config                              │               │
│   ├── Result: OK (no change)                            │               │
│   └── notify: "Restart nginx" (inte triggrad)           │               │
│                                                         │               │
│   TASK 3: Copy SSL cert                                 │               │
│   ├── Result: CHANGED ✓                                │               │
│   └── notify: "Restart nginx"  ─────────────────────────┤               │
│                                                         │               │
│   ════════════════════════════════════════════════════════              │
│                    END OF PLAY                          │               │
│   ════════════════════════════════════════════════════════              │
│                                                         │               │
│   HANDLERS RUN:                                         │               │
│   └── "Restart nginx" ◄────────────────────────────────┘               │
│       (körs EN gång, även om notified flera gånger)                    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Viktiga regler:**
1. Handlers körs BARA om task har `changed` status
2. Handlers körs i SLUTET av play (inte direkt)
3. En handler körs BARA EN gång (även om notified flera gånger)
4. Handlers körs i ordningen de DEFINIERAS (inte notify-ordning)

---

## Basic Handler Syntax

```yaml
---
- name: Configure nginx
  hosts: webservers
  become: true

  tasks:
    - name: Copy main nginx config
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
        mode: '0644'
      notify: Restart nginx      # ← Notify handler

    - name: Copy site configuration
      template:
        src: site.conf.j2
        dest: /etc/nginx/sites-available/mysite
        mode: '0644'
      notify: Reload nginx       # ← Annan handler (reload räcker)

    - name: Enable site
      file:
        src: /etc/nginx/sites-available/mysite
        dest: /etc/nginx/sites-enabled/mysite
        state: link
      notify: Reload nginx

  handlers:                       # ← Definieras i slutet
    - name: Restart nginx
      service:
        name: nginx
        state: restarted

    - name: Reload nginx
      service:
        name: nginx
        state: reloaded
```

---

## Restart vs Reload

| Operation | När använda | Downtime |
|-----------|-------------|----------|
| `restart` | Binär ändring, stora config-ändringar | Ja (kort) |
| `reload` | Config-ändringar som stöds av reload | Nej |

```yaml
handlers:
  # Restart = stoppa + starta (kort downtime)
  - name: Restart nginx
    service:
      name: nginx
      state: restarted

  # Reload = ladda om config utan att stoppa
  - name: Reload nginx
    service:
      name: nginx
      state: reloaded
```

**Best Practice:** Använd `reload` när möjligt, `restart` när nödvändigt.

---

## Notify Multiple Handlers

```yaml
tasks:
  - name: Update application config
    template:
      src: app.conf.j2
      dest: /etc/myapp/config.yml
    notify:
      - Validate config         # Körs först
      - Restart application     # Körs sen
      - Clear cache             # Körs sist

handlers:
  - name: Validate config
    command: /opt/myapp/bin/validate-config
    changed_when: false

  - name: Restart application
    systemd:
      name: myapp
      state: restarted

  - name: Clear cache
    file:
      path: /var/cache/myapp
      state: absent
```

---

## Handler Listen (Gruppera handlers)

Ibland vill du att EN notify triggar FLERA handlers:

```yaml
tasks:
  - name: Deploy new application version
    unarchive:
      src: "releases/app-{{ version }}.tar.gz"
      dest: /opt/myapp/releases/
    notify: Restart application stack  # EN notify

handlers:
  # Alla dessa lyssnar på samma notify
  - name: Restart application
    systemd:
      name: myapp
      state: restarted
    listen: Restart application stack

  - name: Restart workers
    systemd:
      name: myapp-worker
      state: restarted
    listen: Restart application stack

  - name: Restart scheduler
    systemd:
      name: myapp-scheduler
      state: restarted
    listen: Restart application stack

  - name: Clear application cache
    command: /opt/myapp/bin/clear-cache
    listen: Restart application stack
```

---

## Flush Handlers (Kör direkt)

Normalt körs handlers i slutet av play. Ibland behöver du att de körs DIREKT:

```yaml
tasks:
  - name: Install nginx
    apt:
      name: nginx
      state: present
    notify: Start nginx

  - name: Copy nginx config
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify: Restart nginx

  # FLUSH - kör alla pending handlers NU
  - name: Ensure nginx is running before health check
    meta: flush_handlers

  # Denna task kräver att nginx är igång
  - name: Verify nginx is responding
    uri:
      url: http://localhost/health
      status_code: 200
    retries: 5
    delay: 2

  - name: Continue with other tasks
    debug:
      msg: "Nginx is healthy, continuing..."

handlers:
  - name: Start nginx
    service:
      name: nginx
      state: started

  - name: Restart nginx
    service:
      name: nginx
      state: restarted
```

---

## Handlers med Villkor

```yaml
handlers:
  # Restart bara på Debian-system
  - name: Restart nginx
    service:
      name: nginx
      state: restarted
    when: ansible_os_family == "Debian"

  # Använd olika kommandon beroende på init-system
  - name: Restart app
    command: "{{ 'systemctl restart myapp' if ansible_service_mgr == 'systemd' else 'service myapp restart' }}"
```

---

## Handler Validation Pattern

Validera config INNAN restart:

```yaml
tasks:
  - name: Deploy nginx config
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify:
      - Validate nginx config
      - Reload nginx

handlers:
  - name: Validate nginx config
    command: nginx -t
    changed_when: false
    # Om detta failar, körs INTE "Reload nginx"

  - name: Reload nginx
    service:
      name: nginx
      state: reloaded
```

---

## Handlers i Roles

```
roles/
└── nginx/
    ├── tasks/
    │   └── main.yml
    ├── handlers/
    │   └── main.yml      ← Handlers definieras här
    └── templates/
        └── nginx.conf.j2
```

```yaml
# roles/nginx/handlers/main.yml
---
- name: Restart nginx
  service:
    name: nginx
    state: restarted
  become: true

- name: Reload nginx
  service:
    name: nginx
    state: reloaded
  become: true

# Dessa kan notifyas från tasks i rollen
```

---

## Debug och Felsökning

```yaml
# Visa när handlers triggades
- name: Debug handler trigger
  debug:
    msg: "Config changed, nginx will be restarted"
  changed_when: true
  notify: Restart nginx

# Tvinga handler att alltid köras
- name: Force restart
  debug:
    msg: "Forcing nginx restart"
  changed_when: true
  notify: Restart nginx
  tags: force_restart
```

```bash
# Kör bara tasks med specific tag
ansible-playbook site.yml --tags force_restart
```

---

## Praktiskt Exempel: Full Application Deploy

```yaml
---
- name: Deploy web application
  hosts: webservers
  become: true

  vars:
    app_name: myapp
    app_version: "{{ version | default('1.0.0') }}"

  tasks:
    - name: Create application directories
      file:
        path: "{{ item }}"
        state: directory
        owner: www-data
        mode: '0755'
      loop:
        - /opt/{{ app_name }}
        - /opt/{{ app_name }}/releases
        - /opt/{{ app_name }}/shared

    - name: Download application release
      get_url:
        url: "https://releases.example.com/{{ app_name }}-{{ app_version }}.tar.gz"
        dest: /tmp/{{ app_name }}-{{ app_version }}.tar.gz

    - name: Extract release
      unarchive:
        src: /tmp/{{ app_name }}-{{ app_version }}.tar.gz
        dest: /opt/{{ app_name }}/releases/
        remote_src: true
      notify:
        - Update symlink
        - Restart application

    - name: Deploy application config
      template:
        src: config.yml.j2
        dest: /opt/{{ app_name }}/shared/config.yml
      notify: Restart application

    - name: Deploy nginx vhost
      template:
        src: nginx-vhost.conf.j2
        dest: /etc/nginx/sites-available/{{ app_name }}
      notify: Reload nginx

    - name: Enable nginx vhost
      file:
        src: /etc/nginx/sites-available/{{ app_name }}
        dest: /etc/nginx/sites-enabled/{{ app_name }}
        state: link
      notify: Reload nginx

    # Flush handlers innan health check
    - meta: flush_handlers

    - name: Verify application health
      uri:
        url: http://localhost/health
        status_code: 200
      retries: 10
      delay: 3

  handlers:
    - name: Update symlink
      file:
        src: /opt/{{ app_name }}/releases/{{ app_version }}
        dest: /opt/{{ app_name }}/current
        state: link

    - name: Restart application
      systemd:
        name: "{{ app_name }}"
        state: restarted
        daemon_reload: true

    - name: Reload nginx
      service:
        name: nginx
        state: reloaded
```

---

## Sammanfattning

| Koncept | Beteende |
|---------|----------|
| `notify` | Trigger handler vid `changed` |
| Handler timing | Körs i slutet av play |
| Deduplication | En handler körs bara en gång |
| `listen` | Gruppera flera handlers |
| `flush_handlers` | Kör handlers direkt |
| Ordning | Handlers körs i definition-ordning |

---

## Nästa Steg

Nu kan du hantera konfigurationsändringar smart. Nästa: **Conditionals & Loops** — kontrollflöde och iteration.
''',
}

NODE_08_CONDITIONALS_LOOPS = {
    "node_id": 8,
    "title": "Conditionals & Loops",
    "slug": "conditionals-loops",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "prerequisites": [7],
    "content": r'''
# Conditionals & Loops

## Varför detta är kritiskt

> "Varje server är unik — olika OS, olika roller, olika miljöer. Conditionals låter dig hantera denna komplexitet. Loops låter dig skala utan att upprepa dig."

Utan conditionals och loops måste du skriva:
- En playbook för Debian, en för RHEL
- 100 tasks för att skapa 100 användare
- Separata filer för dev/staging/prod

Med dem: EN playbook hanterar allt.

---

## When Conditionals

### Basic Syntax

```yaml
tasks:
  # Enkel jämförelse
  - name: Install on Debian
    apt:
      name: nginx
      state: present
    when: ansible_os_family == "Debian"

  - name: Install on RedHat
    yum:
      name: nginx
      state: present
    when: ansible_os_family == "RedHat"

  # Boolean
  - name: Enable debug logging
    template:
      src: debug-config.yml.j2
      dest: /etc/myapp/config.yml
    when: debug_enabled

  # Negation
  - name: Skip in production
    debug:
      msg: "Running test data generator"
    when: not production_mode
```

### Operatorer

| Operator | Beskrivning | Exempel |
|----------|-------------|---------|
| `==` | Lika med | `when: env == "production"` |
| `!=` | Inte lika med | `when: env != "development"` |
| `>`, `<` | Större/mindre | `when: ansible_memtotal_mb > 4096` |
| `>=`, `<=` | Större/mindre eller lika | `when: version >= "2.0"` |
| `in` | Finns i lista | `when: inventory_hostname in groups['webservers']` |
| `not in` | Finns inte i | `when: "'admin' not in user_groups"` |
| `is defined` | Variabel existerar | `when: custom_port is defined` |
| `is not defined` | Variabel saknas | `when: legacy_mode is not defined` |

### Multiple Conditions

```yaml
tasks:
  # AND (alla måste vara sanna) - lista format
  - name: Production Debian webserver
    apt:
      name: nginx
      state: latest
    when:
      - ansible_os_family == "Debian"
      - env == "production"
      - "'webservers' in group_names"

  # OR (minst en måste vara sann)
  - name: Install on Debian or Ubuntu
    apt:
      name: nginx
    when: ansible_distribution == "Debian" or ansible_distribution == "Ubuntu"

  # Kombinerat
  - name: Complex condition
    debug:
      msg: "Special case"
    when: >
      (ansible_os_family == "Debian" and ansible_distribution_major_version | int >= 10)
      or
      (ansible_os_family == "RedHat" and ansible_distribution_major_version | int >= 8)
```

### Registered Variables i Conditions

```yaml
tasks:
  - name: Check if app is installed
    stat:
      path: /opt/myapp/bin/app
    register: app_binary

  - name: Install app if missing
    get_url:
      url: https://releases.example.com/app.tar.gz
      dest: /tmp/app.tar.gz
    when: not app_binary.stat.exists

  # Command return code
  - name: Check database connection
    command: pg_isready -h {{ db_host }}
    register: db_check
    changed_when: false
    failed_when: false  # Fortsätt även om det failar

  - name: Report database status
    debug:
      msg: "Database is {{ 'UP' if db_check.rc == 0 else 'DOWN' }}"

  - name: Initialize database
    command: /opt/app/bin/init-db
    when: db_check.rc == 0
```

---

## Loops

### Basic Loop

```yaml
tasks:
  # Loop över lista
  - name: Install packages
    apt:
      name: "{{ item }}"
      state: present
    loop:
      - nginx
      - curl
      - git
      - htop

  # Loop över variabel
  - name: Install all required packages
    apt:
      name: "{{ item }}"
      state: present
    loop: "{{ required_packages }}"
```

### Loop med Dictionaries

```yaml
tasks:
  # Lista av dicts
  - name: Create users
    user:
      name: "{{ item.name }}"
      groups: "{{ item.groups }}"
      shell: "{{ item.shell | default('/bin/bash') }}"
    loop:
      - { name: alice, groups: 'sudo,docker', shell: '/bin/zsh' }
      - { name: bob, groups: 'developers' }
      - { name: charlie, groups: 'developers,qa' }

  # Från variabel
  - name: Create service accounts
    user:
      name: "{{ item.name }}"
      system: true
      shell: /usr/sbin/nologin
    loop: "{{ service_accounts }}"
```

### Dict2items

```yaml
vars:
  dns_records:
    web01: 192.168.1.10
    web02: 192.168.1.11
    db01: 192.168.1.20

tasks:
  - name: Update /etc/hosts
    lineinfile:
      path: /etc/hosts
      line: "{{ item.value }} {{ item.key }}"
    loop: "{{ dns_records | dict2items }}"
    # Ger: [{"key": "web01", "value": "192.168.1.10"}, ...]
```

### Loop Control

```yaml
tasks:
  # Med index
  - name: Create numbered files
    file:
      path: "/tmp/file_{{ idx }}"
      state: touch
    loop:
      - alpha
      - beta
      - gamma
    loop_control:
      index_var: idx
    # Skapar: file_0, file_1, file_2

  # Custom label (snyggare output)
  - name: Configure virtual hosts
    template:
      src: vhost.conf.j2
      dest: "/etc/nginx/sites-available/{{ item.domain }}"
    loop: "{{ virtual_hosts }}"
    loop_control:
      label: "{{ item.domain }}"
    # Output visar bara domänen, inte hela dict

  # Paus mellan iterationer
  - name: Rolling restart
    systemd:
      name: myapp
      state: restarted
    loop: "{{ groups['webservers'] }}"
    loop_control:
      pause: 30  # 30 sekunder mellan varje

  # Extended loop info
  - name: Progress indicator
    debug:
      msg: "Processing {{ item }} ({{ ansible_loop.index }}/{{ ansible_loop.length }})"
    loop: "{{ items }}"
    loop_control:
      extended: true
```

### Nested Loops

```yaml
tasks:
  # Product av två listor
  - name: Create user directories
    file:
      path: "/home/{{ item.0 }}/{{ item.1 }}"
      state: directory
    loop: "{{ users | product(directories) | list }}"

  vars:
    users:
      - alice
      - bob
    directories:
      - documents
      - downloads
      - projects
    # Skapar: /home/alice/documents, /home/alice/downloads, ...
```

---

## Combining When + Loop

```yaml
tasks:
  # Condition evalueras per iteration
  - name: Start critical services only
    service:
      name: "{{ item }}"
      state: started
    loop: "{{ services }}"
    when: item in critical_services

  # Registrera resultat från loop
  - name: Check config files
    stat:
      path: "/etc/{{ item }}/config.yml"
    loop:
      - app1
      - app2
      - app3
    register: config_checks

  - name: Show missing configs
    debug:
      msg: "Missing: {{ item.item }}"
    loop: "{{ config_checks.results }}"
    when: not item.stat.exists
```

---

## Block

Gruppera tasks med gemensamma villkor:

```yaml
tasks:
  - name: Web server setup
    block:
      - name: Install nginx
        apt:
          name: nginx
          state: present

      - name: Copy nginx config
        template:
          src: nginx.conf.j2
          dest: /etc/nginx/nginx.conf

      - name: Start nginx
        service:
          name: nginx
          state: started
          enabled: true
    when: "'webservers' in group_names"
    become: true
    tags: webserver
```

### Error Handling med Block

```yaml
tasks:
  - name: Risky deployment
    block:
      - name: Stop application
        systemd:
          name: myapp
          state: stopped

      - name: Deploy new version
        unarchive:
          src: "releases/{{ version }}.tar.gz"
          dest: /opt/myapp/

      - name: Run migrations
        command: /opt/myapp/bin/migrate

      - name: Start application
        systemd:
          name: myapp
          state: started

    rescue:
      # Körs om något i block failar
      - name: Log failure
        debug:
          msg: "Deployment failed, rolling back..."

      - name: Restore previous version
        command: /opt/myapp/bin/rollback

      - name: Start previous version
        systemd:
          name: myapp
          state: started

      - name: Notify on failure
        slack:
          token: "{{ slack_token }}"
          msg: "Deploy of {{ version }} failed on {{ inventory_hostname }}"

    always:
      # Körs ALLTID, oavsett success/failure
      - name: Clean up temp files
        file:
          path: /tmp/deploy-{{ version }}
          state: absent

      - name: Update deployment log
        lineinfile:
          path: /var/log/deployments.log
          line: "{{ ansible_date_time.iso8601 }} - {{ version }} - {{ 'SUCCESS' if ansible_failed_task is not defined else 'FAILED' }}"
```

---

## Until (Retry Loop)

```yaml
tasks:
  # Vänta tills service är redo
  - name: Wait for application to start
    uri:
      url: http://localhost:8080/health
      status_code: 200
    register: health_result
    until: health_result.status == 200
    retries: 30
    delay: 5
    # Försöker var 5:e sekund i max 150 sekunder

  # Vänta på fil
  - name: Wait for config to be generated
    stat:
      path: /etc/myapp/generated-config.yml
    register: config_file
    until: config_file.stat.exists
    retries: 10
    delay: 3

  # Vänta på process
  - name: Wait for database migrations
    command: pgrep -f "db-migrate"
    register: migrate_running
    until: migrate_running.rc != 0  # rc != 0 = processen finns inte
    retries: 60
    delay: 10
    changed_when: false
    failed_when: false
```

---

## Praktiskt Exempel: Multi-Platform Setup

```yaml
---
- name: Setup development environment
  hosts: all
  become: true

  vars:
    common_packages:
      - git
      - curl
      - vim
      - htop

    users:
      - name: developer
        groups: ['sudo', 'docker']
        ssh_key: "ssh-rsa AAAA..."
      - name: deploy
        groups: ['sudo']
        ssh_key: "ssh-rsa BBBB..."

  tasks:
    # Platform-specific package installation
    - name: Install packages on Debian
      apt:
        name: "{{ common_packages + ['build-essential'] }}"
        state: present
        update_cache: true
      when: ansible_os_family == "Debian"

    - name: Install packages on RedHat
      yum:
        name: "{{ common_packages + ['gcc', 'make'] }}"
        state: present
      when: ansible_os_family == "RedHat"

    # User setup with loop
    - name: Create users
      user:
        name: "{{ item.name }}"
        groups: "{{ item.groups | join(',') }}"
        append: true
        shell: /bin/bash
      loop: "{{ users }}"

    - name: Add SSH keys
      authorized_key:
        user: "{{ item.name }}"
        key: "{{ item.ssh_key }}"
      loop: "{{ users }}"
      when: item.ssh_key is defined

    # Environment-specific config
    - name: Production security hardening
      block:
        - name: Disable root login
          lineinfile:
            path: /etc/ssh/sshd_config
            regexp: '^PermitRootLogin'
            line: 'PermitRootLogin no'
          notify: Restart sshd

        - name: Set password policies
          copy:
            src: pam-password-policy
            dest: /etc/pam.d/common-password
      when: env == "production"

  handlers:
    - name: Restart sshd
      service:
        name: sshd
        state: restarted
```

---

## Sammanfattning

| Konstruktion | Användning |
|--------------|-----------|
| `when` | Villkorlig körning |
| `loop` | Iterera över lista |
| `loop_control` | Index, label, pause |
| `block` | Gruppera tasks |
| `rescue` | Error handling |
| `always` | Körs alltid |
| `until` | Retry med villkor |

---

## Nästa Steg

Nu kan du skriva intelligenta playbooks som anpassar sig. Nästa: **Roles** — organisera och återanvänd din automation.
''',
}

ANSIBLE_BLOCK_2 = [
    NODE_05_TASKS_MODULES,
    NODE_06_VARIABLES,
    NODE_07_HANDLERS,
    NODE_08_CONDITIONALS_LOOPS,
]
