# =============================================================================
# BLOCK 2: PLAYBOOKS (Noder 5-8)
# =============================================================================

NODE_05_TASKS_MODULES = {
    "node_id": 5,
    "title": "Tasks & Modules",
    "slug": "tasks-modules",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": [4],
    "content": '''
# Tasks & Modules

Ansible modules är verktyg för automation.

## Task Syntax

```yaml
tasks:
  - name: Beskrivande namn
    module_name:
      param1: value1
      param2: value2
```

## Vanliga Modules

### Package Management

```yaml
# apt (Debian/Ubuntu)
- name: Install packages
  apt:
    name:
      - nginx
      - curl
      - git
    state: present
    update_cache: true

# yum (RHEL/CentOS)
- name: Install packages
  yum:
    name: httpd
    state: latest

# package (auto-detect)
- name: Install package
  package:
    name: vim
    state: present
```

### File Operations

```yaml
# Copy file
- name: Copy config
  copy:
    src: nginx.conf
    dest: /etc/nginx/nginx.conf
    owner: root
    mode: '0644'
    backup: true

# Create directory
- name: Create app directory
  file:
    path: /opt/myapp
    state: directory
    owner: deploy
    mode: '0755'

# Template
- name: Deploy config from template
  template:
    src: app.conf.j2
    dest: /etc/app/config.conf

# Download file
- name: Download binary
  get_url:
    url: https://example.com/app.tar.gz
    dest: /tmp/app.tar.gz
    checksum: sha256:abc123...
```

### Service Management

```yaml
- name: Start and enable nginx
  service:
    name: nginx
    state: started
    enabled: true

# Systemd specific
- name: Restart app
  systemd:
    name: myapp
    state: restarted
    daemon_reload: true
```

### User Management

```yaml
- name: Create user
  user:
    name: deploy
    groups: sudo,docker
    shell: /bin/bash
    create_home: true

- name: Add SSH key
  authorized_key:
    user: deploy
    key: "{{ lookup('file', 'id_rsa.pub') }}"
```

## Registering Results

```yaml
- name: Check if file exists
  stat:
    path: /etc/app.conf
  register: config_file

- name: Create config if missing
  copy:
    src: app.conf
    dest: /etc/app.conf
  when: not config_file.stat.exists
```

| Module | Syfte |
|--------|-------|
| apt/yum | Paket |
| copy | Kopiera filer |
| template | Jinja2 templates |
| file | Filer/dirs |
| service | Tjänster |
| user | Användare |
| command | Kör kommando |
| shell | Shell-kommando |

**Nästa steg:** Node 6 - Variables
''',
}

NODE_06_VARIABLES = {
    "node_id": 6,
    "title": "Variables",
    "slug": "variables",
    "estimated_minutes": 55,
    "xp_reward": 145,
    "prerequisites": [5],
    "content": '''
# Ansible Variables

Parametrisera dina playbooks.

## Definiera Variables

### I Playbook

```yaml
- name: Configure web
  hosts: webservers
  vars:
    http_port: 80
    app_name: myapp
    packages:
      - nginx
      - curl
```

### I Separat Fil

```yaml
# vars/main.yml
http_port: 80
app_name: myapp
db_host: localhost
```

```yaml
# playbook
- name: Configure
  hosts: all
  vars_files:
    - vars/main.yml
    - vars/secrets.yml
```

### I Inventory

```ini
[webservers:vars]
http_port=80
app_env=production
```

### Host/Group Vars

```
inventory/
├── hosts.ini
├── group_vars/
│   ├── all.yml
│   ├── webservers.yml
│   └── databases.yml
└── host_vars/
    ├── web01.yml
    └── db01.yml
```

## Använda Variables

```yaml
tasks:
  - name: Install package
    apt:
      name: "{{ app_name }}"

  - name: Deploy config
    template:
      src: app.conf.j2
      dest: "/etc/{{ app_name }}/config.conf"

  - name: Debug
    debug:
      msg: "Port is {{ http_port }}"
```

## Variable Precedence (låg → hög)

1. Role defaults
2. Inventory vars
3. Playbook vars
4. Role vars
5. Block vars
6. Task vars
7. Extra vars (-e)

```bash
# Highest priority
ansible-playbook site.yml -e "http_port=8080"
```

## Special Variables (Facts)

```yaml
- name: Show OS
  debug:
    msg: "OS: {{ ansible_distribution }} {{ ansible_distribution_version }}"

- name: Show IP
  debug:
    msg: "IP: {{ ansible_default_ipv4.address }}"

- name: Show hostname
  debug:
    msg: "Host: {{ inventory_hostname }}"
```

## Registered Variables

```yaml
- name: Get uptime
  command: uptime
  register: uptime_result

- name: Show uptime
  debug:
    msg: "{{ uptime_result.stdout }}"
```

| Scope | Exempel |
|-------|---------|
| Play | vars: i playbook |
| Host | host_vars/ |
| Group | group_vars/ |
| Global | all.yml |
| Runtime | -e "var=value" |

**Nästa steg:** Node 7 - Handlers
''',
}

NODE_07_HANDLERS = {
    "node_id": 7,
    "title": "Handlers",
    "slug": "handlers",
    "estimated_minutes": 45,
    "xp_reward": 125,
    "prerequisites": [6],
    "content": '''
# Handlers

Tasks som körs vid changes.

## Basic Handler

```yaml
- name: Configure nginx
  hosts: webservers
  become: true

  tasks:
    - name: Update nginx config
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: Restart nginx

    - name: Update site config
      template:
        src: site.conf.j2
        dest: /etc/nginx/sites-available/default
      notify: Restart nginx

  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted
```

## Viktigt om Handlers

```yaml
# Handlers körs:
# 1. Endast om task ändrar något (changed)
# 2. I slutet av play (inte direkt)
# 3. Bara EN gång (även om notified flera gånger)
```

## Flush Handlers

```yaml
tasks:
  - name: Update config
    copy:
      src: app.conf
      dest: /etc/app.conf
    notify: Restart app

  # Kör handlers NU (inte i slutet)
  - name: Force handler run
    meta: flush_handlers

  - name: Verify app is running
    uri:
      url: http://localhost:8080/health
```

## Multiple Handlers

```yaml
tasks:
  - name: Update nginx.conf
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify:
      - Validate nginx config
      - Restart nginx

handlers:
  - name: Validate nginx config
    command: nginx -t
    changed_when: false

  - name: Restart nginx
    service:
      name: nginx
      state: restarted
```

## Handler Listen

```yaml
tasks:
  - name: Update config
    copy:
      src: app.conf
      dest: /etc/app.conf
    notify: Restart stack

handlers:
  - name: Restart app
    service:
      name: myapp
      state: restarted
    listen: Restart stack

  - name: Restart worker
    service:
      name: worker
      state: restarted
    listen: Restart stack
```

## Handler i Roles

```
roles/nginx/
├── tasks/main.yml
└── handlers/main.yml  ← Handlers här
```

```yaml
# roles/nginx/handlers/main.yml
- name: Restart nginx
  service:
    name: nginx
    state: restarted

- name: Reload nginx
  service:
    name: nginx
    state: reloaded
```

| Koncept | Beteende |
|---------|----------|
| notify | Triggar handler |
| changed | Endast vid ändring |
| flush_handlers | Kör direkt |
| listen | Gruppera handlers |

**Nästa steg:** Node 8 - Conditionals & Loops
''',
}

NODE_08_CONDITIONALS_LOOPS = {
    "node_id": 8,
    "title": "Conditionals & Loops",
    "slug": "conditionals-loops",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "prerequisites": [7],
    "content": '''
# Conditionals & Loops

Kontrollflöde i playbooks.

## When Conditionals

```yaml
tasks:
  # String comparison
  - name: Install on Debian
    apt:
      name: nginx
    when: ansible_os_family == "Debian"

  # Boolean
  - name: Start if enabled
    service:
      name: nginx
      state: started
    when: nginx_enabled

  # Registered variable
  - name: Check config
    command: nginx -t
    register: nginx_test

  - name: Restart nginx
    service:
      name: nginx
      state: restarted
    when: nginx_test.rc == 0

  # Multiple conditions (AND)
  - name: Production Debian only
    apt:
      name: nginx
    when:
      - ansible_os_family == "Debian"
      - app_env == "production"

  # OR condition
  - name: RedHat or Debian
    package:
      name: nginx
    when: ansible_os_family == "Debian" or ansible_os_family == "RedHat"
```

## Loops

```yaml
# Simple loop
- name: Install packages
  apt:
    name: "{{ item }}"
    state: present
  loop:
    - nginx
    - curl
    - git

# Loop with dict
- name: Create users
  user:
    name: "{{ item.name }}"
    groups: "{{ item.groups }}"
  loop:
    - { name: alice, groups: sudo }
    - { name: bob, groups: developers }

# Loop over variable
- name: Install packages
  apt:
    name: "{{ item }}"
  loop: "{{ packages }}"
```

## Loop Controls

```yaml
# With index
- name: Create files
  file:
    path: "/tmp/file{{ idx }}"
    state: touch
  loop:
    - one
    - two
    - three
  loop_control:
    index_var: idx

# Custom label
- name: Create users
  user:
    name: "{{ item.name }}"
  loop: "{{ users }}"
  loop_control:
    label: "{{ item.name }}"

# Pause between iterations
- name: Restart services
  service:
    name: "{{ item }}"
    state: restarted
  loop: "{{ services }}"
  loop_control:
    pause: 5
```

## Combining When + Loop

```yaml
- name: Install only missing packages
  apt:
    name: "{{ item }}"
  loop: "{{ packages }}"
  when: item not in ansible_facts.packages
```

## Block

```yaml
- name: Handle web setup
  block:
    - name: Install nginx
      apt:
        name: nginx

    - name: Start nginx
      service:
        name: nginx
        state: started
  when: install_web
  become: true
```

## Error Handling

```yaml
- block:
    - name: Risky operation
      command: /might/fail
  rescue:
    - name: Handle failure
      debug:
        msg: "Operation failed, cleaning up"
  always:
    - name: Always run
      debug:
        msg: "Cleanup complete"
```

| Konstruktion | Användning |
|--------------|-----------|
| when | Villkorlig körning |
| loop | Iterera över lista |
| block | Gruppera tasks |
| rescue | Felhantering |
| always | Kör alltid |

**Nästa steg:** Node 9 - Roles
''',
}

ANSIBLE_BLOCK_2 = [
    NODE_05_TASKS_MODULES,
    NODE_06_VARIABLES,
    NODE_07_HANDLERS,
    NODE_08_CONDITIONALS_LOOPS,
]
