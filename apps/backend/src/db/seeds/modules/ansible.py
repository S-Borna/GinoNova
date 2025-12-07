"""
Ansible Mastery Module
======================

Komplett kurs i Configuration Management med Ansible.
Följer Linux-mallen: Svenska, pedagogiskt, bash-kommentarer på varje rad.

20 noder från grundläggande till avancerat.
"""

MODULE = {
    "slug": "ansible-mastery",
    "title": "Ansible Mastery",
    "description": "Automatisera konfiguration och deployment med Ansible",
    "icon": "settings",
    "category": "infrastructure",
    "order": 8,
    "tasks": [
        {
            "title": "Introduction to Ansible",
            "slug": "introduction-to-ansible",
            "difficulty": "beginner",
            "content": '''
# Introduction to Ansible

## Varför behöver du kunna detta?

Manuell serverkonfiguration är:

- Tidskrävande och felbenägen
- Svår att replikera exakt
- Omöjlig att versionskontrollera
- Källa till konfigurationsdrift

Ansible automatiserar allt detta med enkel YAML-syntax.

---

## Så fungerar det

Ansible är agentlöst:

1. Kontrollnod har Ansible installerat
2. Ansluter till målservrar via SSH
3. Kör tasks definierade i playbooks
4. Idempotent - säkert att köra om

Ingen agent behövs på målservrar!

---

## Installation

```bash
# macOS med Homebrew
brew install ansible                 # Installera Ansible

# Ubuntu/Debian
sudo apt update                      # Uppdatera paketlista
sudo apt install ansible -y          # Installera Ansible

# Med pip (alla plattformar)
pip3 install ansible                 # Installera via pip
pip3 install ansible-lint            # Installera linter

# Verifiera installation
ansible --version                    # Visa version
ansible-playbook --version           # Visa playbook version
```

---

## Första inventory

```ini
# inventory.ini - Lista över servrar

[webservers]
web1.example.com
web2.example.com ansible_host=192.168.1.10

[dbservers]
db1.example.com ansible_port=2222

[all:vars]
ansible_user=deploy
ansible_ssh_private_key_file=~/.ssh/deploy_key
```

```yaml
# inventory.yml - YAML-format (rekommenderat)
all:
  children:
    webservers:
      hosts:
        web1.example.com:
        web2.example.com:
          ansible_host: 192.168.1.10
    dbservers:
      hosts:
        db1.example.com:
          ansible_port: 2222
  vars:
    ansible_user: deploy
```

---

## Ad-hoc kommandon

```bash
# Testa anslutning
ansible all -i inventory.ini -m ping       # Ping alla servrar

# Kör kommando
ansible webservers -i inventory.ini -a "uptime"  # Kör uptime

# Installera paket
ansible webservers -i inventory.ini -m apt -a "name=nginx state=present" --become

# Kopiera fil
ansible all -i inventory.ini -m copy -a "src=/local/file dest=/remote/path"

# Samla fakta
ansible web1.example.com -i inventory.ini -m setup  # Alla fakta
ansible web1.example.com -i inventory.ini -m setup -a "filter=ansible_distribution*"
```

---

## Första playbook

```yaml
# playbook.yml - Installera och starta nginx
---
- name: Configure web servers          # Play-namn
  hosts: webservers                    # Målgrupp från inventory
  become: yes                          # Kör som root (sudo)

  tasks:
    - name: Update apt cache           # Task-namn
      apt:
        update_cache: yes              # apt update
        cache_valid_time: 3600         # Cache giltig i 1 timme

    - name: Install nginx
      apt:
        name: nginx                    # Paketnamn
        state: present                 # Säkerställ installerat

    - name: Start nginx service
      service:
        name: nginx                    # Tjänstnamn
        state: started                 # Säkerställ startad
        enabled: yes                   # Starta vid boot
```

```bash
# Kör playbook
ansible-playbook -i inventory.ini playbook.yml

# Dry-run (check mode)
ansible-playbook -i inventory.ini playbook.yml --check

# Verbose output
ansible-playbook -i inventory.ini playbook.yml -v   # Mer info
ansible-playbook -i inventory.ini playbook.yml -vvv # Debug
```

---

## Key Takeaways

1. Ansible är agentlöst - kommunicerar via SSH
2. Inventory definierar servrar och grupper
3. Playbooks är YAML-filer med tasks
4. Idempotent - säkert att köra flera gånger
5. `--check` för dry-run innan apply
''',
        },
        {
            "title": "Inventory Management",
            "slug": "inventory-management",
            "difficulty": "beginner",
            "content": '''
# Inventory Management

## Varför behöver du kunna detta?

Inventory är Ansibles karta över infrastrukturen:

- Vilka servrar finns?
- Hur grupperas de?
- Vilka variabler gäller?
- Hur når vi dem?

Rätt inventory-struktur förenklar allt.

---

## Så fungerar det

Inventory kan vara:

1. Statisk fil (INI eller YAML)
2. Dynamisk (script eller plugin)
3. Kombinationer av båda
4. Flera inventory-källor

---

## Static inventory

```ini
# inventory/hosts.ini

# Enskilda servrar
server1.example.com
192.168.1.50

# Grupper med hakparenteser
[webservers]
web1.example.com
web2.example.com
web[3:5].example.com      # web3, web4, web5

[dbservers]
db1.example.com
db2.example.com

# Gruppvariabler
[webservers:vars]
http_port=80
max_clients=200

# Grupp av grupper
[production:children]
webservers
dbservers

# Globala variabler
[all:vars]
ansible_user=deploy
ansible_python_interpreter=/usr/bin/python3
```

---

## YAML inventory

```yaml
# inventory/hosts.yml
all:
  vars:
    ansible_user: deploy
    ansible_python_interpreter: /usr/bin/python3

  children:
    production:
      children:
        webservers:
          hosts:
            web1.example.com:
              http_port: 80
            web2.example.com:
              http_port: 8080
          vars:
            max_clients: 200

        dbservers:
          hosts:
            db1.example.com:
              db_port: 5432
            db2.example.com:
              db_port: 5432
              is_replica: true

    staging:
      hosts:
        staging.example.com:
          ansible_host: 10.0.0.50
```

---

## Directory layout

```bash
# Rekommenderad struktur
inventory/
├── production/
│   ├── hosts.yml           # Production servrar
│   ├── group_vars/
│   │   ├── all.yml         # Alla production-servrar
│   │   ├── webservers.yml  # Webserver-specifikt
│   │   └── dbservers.yml   # Database-specifikt
│   └── host_vars/
│       ├── web1.example.com.yml
│       └── db1.example.com.yml
└── staging/
    ├── hosts.yml
    └── group_vars/
        └── all.yml
```

```yaml
# inventory/production/group_vars/webservers.yml
---
nginx_worker_processes: auto
nginx_worker_connections: 1024
ssl_certificate: /etc/ssl/certs/prod.crt
```

```yaml
# inventory/production/host_vars/web1.example.com.yml
---
is_primary: true
custom_config: specific_to_this_host
```

---

## Dynamic inventory

```python
#!/usr/bin/env python3
# inventory/dynamic.py - Enkel dynamisk inventory

import json

inventory = {
    "webservers": {
        "hosts": ["web1.example.com", "web2.example.com"],
        "vars": {
            "http_port": 80
        }
    },
    "dbservers": {
        "hosts": ["db1.example.com"]
    },
    "_meta": {
        "hostvars": {
            "web1.example.com": {
                "ansible_host": "192.168.1.10"
            }
        }
    }
}

print(json.dumps(inventory))
```

```bash
# Gör körbar och testa
chmod +x inventory/dynamic.py
./inventory/dynamic.py               # Visa JSON output
ansible-inventory -i inventory/dynamic.py --list  # Verifiera
```

---

## AWS dynamic inventory

```yaml
# inventory/aws_ec2.yml
---
plugin: amazon.aws.aws_ec2
regions:
  - eu-north-1
  - eu-west-1

filters:
  tag:Environment:
    - production
  instance-state-name: running

keyed_groups:
  - key: tags.Role
    prefix: role
  - key: placement.availability_zone
    prefix: az

hostnames:
  - private-ip-address
  - tag:Name

compose:
  ansible_host: private_ip_address
```

```bash
# Installera AWS collection
ansible-galaxy collection install amazon.aws

# Testa inventory
ansible-inventory -i inventory/aws_ec2.yml --graph
ansible-inventory -i inventory/aws_ec2.yml --list
```

---

## Inventory plugins

```yaml
# ansible.cfg - Aktivera plugins
[inventory]
enable_plugins = host_list, script, auto, yaml, ini, aws_ec2, azure_rm

[defaults]
inventory = ./inventory
```

```bash
# Lista tillgängliga plugins
ansible-doc -t inventory -l

# Dokumentation för specifik plugin
ansible-doc -t inventory aws_ec2
```

---

## Inventory commands

```bash
# Lista alla hosts
ansible-inventory -i inventory/ --list

# Visa som graf
ansible-inventory -i inventory/ --graph

# Visa specifik host
ansible-inventory -i inventory/ --host web1.example.com

# Kombinera flera inventory
ansible-playbook -i inventory/production -i inventory/staging playbook.yml
```

---

## Key Takeaways

1. Inventory kan vara statisk (INI/YAML) eller dynamisk
2. group_vars/ och host_vars/ för strukturerade variabler
3. Dynamisk inventory för cloud-miljöer
4. `ansible-inventory --graph` för visualisering
5. Flera inventory-källor kan kombineras
''',
        },
        {
            "title": "Playbook Fundamentals",
            "slug": "playbook-fundamentals",
            "difficulty": "beginner",
            "content": '''
# Playbook Fundamentals

## Varför behöver du kunna detta?

Playbooks är Ansibles hjärta:

- Definierar önskat tillstånd
- Dokumenterar infrastruktur som kod
- Reproducerbara deployments
- Versionskontrollerbara

Rätt playbookstruktur = underhållbar automation.

---

## Så fungerar det

En playbook innehåller:

1. **Plays** - målgrupp + tasks
2. **Tasks** - individuella steg
3. **Modules** - Ansibles byggblock
4. **Handlers** - trigger-baserade tasks

---

## Playbook struktur

```yaml
# site.yml - Komplett playbook
---
# Play 1: Konfigurera webservrar
- name: Configure web servers
  hosts: webservers                    # Målgrupp
  become: yes                          # Sudo
  gather_facts: yes                    # Samla systeminfo

  vars:
    http_port: 80                      # Play-variabler
    doc_root: /var/www/html

  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present

    - name: Copy nginx config
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: Restart nginx            # Trigga handler

  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted

# Play 2: Konfigurera databaser
- name: Configure database servers
  hosts: dbservers
  become: yes

  tasks:
    - name: Install PostgreSQL
      apt:
        name: postgresql
        state: present
```

---

## Task syntax

```yaml
tasks:
  # Enkel task
  - name: Install package
    apt:
      name: nginx
      state: present

  # Task med loop
  - name: Install multiple packages
    apt:
      name: "{{ item }}"
      state: present
    loop:
      - nginx
      - curl
      - vim

  # Task med villkor
  - name: Install on Ubuntu only
    apt:
      name: ubuntu-specific-package
      state: present
    when: ansible_distribution == "Ubuntu"

  # Task med register
  - name: Check if file exists
    stat:
      path: /etc/myapp.conf
    register: config_file

  - name: Create config if missing
    template:
      src: myapp.conf.j2
      dest: /etc/myapp.conf
    when: not config_file.stat.exists

  # Task med ignore_errors
  - name: Try something that might fail
    command: /opt/script.sh
    ignore_errors: yes
    register: script_result

  # Task med changed_when
  - name: Run command
    command: /opt/update.sh
    changed_when: "'Updated' in command_result.stdout"
    register: command_result
```

---

## Handlers

```yaml
# Handlers körs endast om notified
handlers:
  - name: Restart nginx
    service:
      name: nginx
      state: restarted

  - name: Reload nginx
    service:
      name: nginx
      state: reloaded

  - name: Restart multiple services
    service:
      name: "{{ item }}"
      state: restarted
    loop:
      - nginx
      - php-fpm

tasks:
  - name: Update nginx config
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify:
      - Restart nginx              # Triggar handler

  - name: Update PHP config
    template:
      src: php.ini.j2
      dest: /etc/php/8.1/fpm/php.ini
    notify:
      - Restart multiple services
```

---

## Play options

```yaml
---
- name: Configure servers
  hosts: all
  become: yes                          # Sudo för alla tasks
  become_user: root                    # Vilken user
  gather_facts: yes                    # Samla fakta (default: yes)
  serial: 2                            # Kör på 2 hosts åt gången
  max_fail_percentage: 25              # Avbryt om >25% failar
  any_errors_fatal: true               # Avbryt vid första fel

  environment:
    http_proxy: http://proxy:8080

  vars_files:
    - vars/common.yml
    - "vars/{{ env }}.yml"

  pre_tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

  roles:
    - common
    - nginx

  tasks:
    - name: Final configuration
      debug:
        msg: "All done!"

  post_tasks:
    - name: Cleanup
      file:
        path: /tmp/ansible_temp
        state: absent
```

---

## Blocks och error handling

```yaml
tasks:
  - name: Handle errors gracefully
    block:
      - name: Attempt risky operation
        command: /opt/risky_script.sh

      - name: Another risky task
        service:
          name: myapp
          state: started

    rescue:
      - name: Run on failure
        debug:
          msg: "Something failed, running recovery"

      - name: Rollback changes
        command: /opt/rollback.sh

    always:
      - name: Always run this
        debug:
          msg: "Cleanup regardless of success/failure"
```

---

## Key Takeaways

1. Playbooks innehåller plays med tasks
2. Tasks använder modules för att göra arbetet
3. Handlers körs endast när de notifieras
4. Blocks ger error handling med rescue/always
5. `gather_facts` ger systeminfo för villkor
''',
        },
        {
            "title": "Variables & Facts",
            "slug": "variables-facts",
            "difficulty": "beginner",
            "content": '''
# Variables & Facts

## Varför behöver du kunna detta?

Variabler gör playbooks flexibla:

- Samma playbook för olika miljöer
- Konfigurerbar utan kodändringar
- Återanvändbar kod
- Separation av data och logik

Facts ger automatisk systeminformation.

---

## Så fungerar det

Variabelkällor (prioritetsordning, lägst till högst):

1. Role defaults
2. Inventory vars
3. Playbook vars
4. Role vars
5. Extra vars (kommandorad)

---

## Definiera variabler

```yaml
# I playbook
---
- name: Configure servers
  hosts: webservers

  vars:
    http_port: 80
    app_name: myapp
    packages:
      - nginx
      - curl
    config:
      max_connections: 100
      timeout: 30

  tasks:
    - name: Install packages
      apt:
        name: "{{ packages }}"
        state: present

    - name: Show config
      debug:
        msg: "Port: {{ http_port }}, App: {{ app_name }}"
```

```yaml
# I separat fil (vars/main.yml)
---
http_port: 80
app_name: myapp

database:
  host: localhost
  port: 5432
  name: myapp_db
```

```yaml
# Inkludera i playbook
- name: Configure servers
  hosts: all

  vars_files:
    - vars/common.yml
    - "vars/{{ env }}.yml"           # Dynamiskt baserat på env
```

---

## Variabel precedens

```bash
# Kommandoradsvariabler har högst prioritet
ansible-playbook site.yml -e "http_port=8080"
ansible-playbook site.yml --extra-vars "http_port=8080"
ansible-playbook site.yml -e "@vars.json"  # Från JSON-fil
ansible-playbook site.yml -e "@vars.yml"   # Från YAML-fil
```

```yaml
# Inventory-variabler
# inventory/group_vars/webservers.yml
---
http_port: 80
nginx_workers: 4

# inventory/host_vars/web1.example.com.yml
---
is_primary: true
http_port: 8080                        # Override för denna host
```

---

## Ansible Facts

```yaml
# Facts samlas automatiskt
- name: Show facts
  hosts: all
  gather_facts: yes                    # Default: yes

  tasks:
    - name: Show OS
      debug:
        msg: "OS: {{ ansible_distribution }} {{ ansible_distribution_version }}"

    - name: Show IP
      debug:
        msg: "IP: {{ ansible_default_ipv4.address }}"

    - name: Show memory
      debug:
        msg: "Memory: {{ ansible_memtotal_mb }} MB"

    - name: Conditional on OS
      apt:
        name: nginx
        state: present
      when: ansible_os_family == "Debian"

    - name: Conditional on OS (RedHat)
      yum:
        name: nginx
        state: present
      when: ansible_os_family == "RedHat"
```

```bash
# Visa alla facts
ansible hostname -m setup

# Filtrera facts
ansible hostname -m setup -a "filter=ansible_distribution*"
ansible hostname -m setup -a "filter=ansible_memory_mb"
```

---

## Custom facts

```bash
# Skapa custom fact på målserver
# /etc/ansible/facts.d/custom.fact
```

```ini
[general]
app_version=1.2.3
environment=production

[database]
host=localhost
port=5432
```

```yaml
# Använd i playbook
- name: Use custom facts
  hosts: all

  tasks:
    - name: Show custom fact
      debug:
        msg: "App version: {{ ansible_local.custom.general.app_version }}"
```

---

## Register och set_fact

```yaml
tasks:
  # Register sparar task-output
  - name: Get current date
    command: date +%Y-%m-%d
    register: current_date
    changed_when: false

  - name: Show date
    debug:
      msg: "Date: {{ current_date.stdout }}"

  # set_fact skapar nya variabler
  - name: Set deployment date
    set_fact:
      deploy_date: "{{ current_date.stdout }}"
      deploy_time: "{{ ansible_date_time.iso8601 }}"

  - name: Use new fact
    debug:
      msg: "Deployed on {{ deploy_date }}"

  # Kombinera facts
  - name: Build connection string
    set_fact:
      db_connection: "postgresql://{{ db_user }}:{{ db_pass }}@{{ db_host }}:{{ db_port }}/{{ db_name }}"

  # Conditionally set fact
  - name: Set environment-specific values
    set_fact:
      log_level: "{{ 'DEBUG' if env == 'development' else 'INFO' }}"
```

---

## Variabel filters

```yaml
tasks:
  - name: String manipulation
    debug:
      msg: |
        Upper: {{ name | upper }}
        Lower: {{ name | lower }}
        Title: {{ name | title }}
        Default: {{ undefined_var | default('fallback') }}

  - name: List operations
    debug:
      msg: |
        First: {{ my_list | first }}
        Last: {{ my_list | last }}
        Length: {{ my_list | length }}
        Joined: {{ my_list | join(', ') }}
        Unique: {{ my_list | unique }}

  - name: JSON/YAML
    debug:
      msg: |
        To JSON: {{ my_dict | to_json }}
        To YAML: {{ my_dict | to_yaml }}

  - name: Path operations
    debug:
      msg: |
        Basename: {{ '/path/to/file.txt' | basename }}
        Dirname: {{ '/path/to/file.txt' | dirname }}
        Expanduser: {{ '~/.ssh' | expanduser }}
```

---

## Key Takeaways

1. Variabler definieras på flera ställen med olika prioritet
2. Extra vars (-e) har högst prioritet
3. Facts samlas automatiskt med gather_facts
4. set_fact skapar runtime-variabler
5. Filters transformerar variabelvärden
''',
        },
        {
            "title": "Modules & Plugins",
            "slug": "modules-plugins",
            "difficulty": "beginner",
            "content": '''
# Modules & Plugins

## Varför behöver du kunna detta?

Modules är Ansibles byggblock:

- 3000+ inbyggda modules
- Varje module gör en specifik sak
- Idempotent - säkra att köra om
- Dokumenterade och testade

Rätt module = rätt verktyg för jobbet.

---

## Så fungerar det

Modules kategoriseras efter funktion:

- **System** - användare, grupper, tjänster
- **Files** - kopiera, template, permissions
- **Packaging** - apt, yum, pip
- **Cloud** - aws, azure, gcp
- **Network** - routers, switches

---

## Vanliga system-modules

```yaml
tasks:
  # User management
  - name: Create user
    user:
      name: deploy                     # Användarnamn
      state: present                   # Skapa om inte finns
      groups: sudo,www-data            # Gruppmedlemskap
      shell: /bin/bash                 # Shell
      create_home: yes                 # Skapa hemkatalog

  - name: Add SSH key
    authorized_key:
      user: deploy
      key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
      state: present

  # Group management
  - name: Create group
    group:
      name: appgroup
      state: present
      gid: 1500

  # Service management
  - name: Ensure nginx is running
    service:
      name: nginx
      state: started                   # started/stopped/restarted
      enabled: yes                     # Start vid boot

  # Systemd specifikt
  - name: Manage systemd service
    systemd:
      name: myapp
      state: started
      daemon_reload: yes               # Ladda om systemd config
```

---

## File modules

```yaml
tasks:
  # Kopiera fil
  - name: Copy file
    copy:
      src: files/config.txt            # Lokal fil
      dest: /etc/myapp/config.txt      # Remote destination
      owner: root
      group: root
      mode: '0644'                     # Permissions

  # Skapa katalog
  - name: Create directory
    file:
      path: /var/www/myapp
      state: directory
      owner: www-data
      group: www-data
      mode: '0755'

  # Skapa symlink
  - name: Create symlink
    file:
      src: /var/www/myapp/current
      dest: /var/www/html
      state: link

  # Ta bort fil
  - name: Remove file
    file:
      path: /tmp/obsolete.txt
      state: absent

  # Template med Jinja2
  - name: Deploy config from template
    template:
      src: templates/nginx.conf.j2
      dest: /etc/nginx/nginx.conf
      owner: root
      group: root
      mode: '0644'
      validate: nginx -t -c %s         # Validera innan apply
    notify: Restart nginx
```

---

## Package modules

```yaml
tasks:
  # APT (Debian/Ubuntu)
  - name: Install package
    apt:
      name: nginx
      state: present                   # present/absent/latest
      update_cache: yes                # apt update först

  - name: Install multiple packages
    apt:
      name:
        - nginx
        - curl
        - vim
      state: present

  # YUM/DNF (RedHat/CentOS)
  - name: Install with yum
    yum:
      name: httpd
      state: present

  # Package (cross-platform)
  - name: Install generically
    package:
      name: git
      state: present

  # Pip (Python)
  - name: Install Python package
    pip:
      name: flask
      state: present
      virtualenv: /opt/myapp/venv      # Optional venv

  # NPM (Node.js)
  - name: Install npm package
    npm:
      name: pm2
      global: yes
      state: present
```

---

## Command modules

```yaml
tasks:
  # Shell - kör via shell (stöder pipes, redirects)
  - name: Run shell command
    shell: cat /etc/passwd | grep deploy > /tmp/user.txt
    args:
      creates: /tmp/user.txt           # Skippa om filen finns

  # Command - kör utan shell (säkrare)
  - name: Run command
    command: /opt/script.sh --arg1 value
    args:
      chdir: /opt                      # Arbetskatalog
      creates: /opt/output.txt         # Skippa om finns
    register: script_result
    changed_when: "'Changed' in script_result.stdout"

  # Raw - direkt SSH (ingen Python på remote)
  - name: Raw command
    raw: apt-get install -y python3
    when: ansible_python_interpreter is not defined

  # Script - kopiera och kör lokalt script
  - name: Run local script on remote
    script: scripts/setup.sh
    args:
      creates: /opt/setup_done
```

---

## Lookup plugins

```yaml
tasks:
  # Läs fil
  - name: Read file content
    debug:
      msg: "{{ lookup('file', '/etc/hostname') }}"

  # Environment variable
  - name: Get env var
    debug:
      msg: "Home: {{ lookup('env', 'HOME') }}"

  # Password generation
  - name: Generate password
    debug:
      msg: "{{ lookup('password', '/dev/null length=16 chars=ascii_letters,digits') }}"

  # Read from URL
  - name: Fetch URL
    debug:
      msg: "{{ lookup('url', 'https://api.example.com/config') }}"

  # AWS SSM Parameter
  - name: Get SSM parameter
    debug:
      msg: "{{ lookup('amazon.aws.aws_ssm', 'my-param', region='eu-north-1') }}"
```

---

## Module dokumentation

```bash
# Lista alla modules
ansible-doc -l                         # Alla modules
ansible-doc -l | grep aws              # Filtrera

# Visa dokumentation
ansible-doc apt                        # Full dokumentation
ansible-doc -s apt                     # Kort syntax-exempel

# Lista plugins
ansible-doc -t lookup -l               # Lookup plugins
ansible-doc -t callback -l             # Callback plugins
ansible-doc -t connection -l           # Connection plugins
```

---

## Key Takeaways

1. Modules är idempotenta - säkra att köra om
2. Använd rätt module för rätt jobb
3. `state: present/absent` för att skapa/ta bort
4. Lookup plugins för dynamiska värden
5. `ansible-doc` för dokumentation
''',
        },
        {
            "title": "Templates & Jinja2",
            "slug": "templates-jinja2",
            "difficulty": "intermediate",
            "content": '''
# Templates & Jinja2

## Varför behöver du kunna detta?

Templates gör konfiguration dynamisk:

- Generera config-filer med variabler
- Logik i templates (loopar, villkor)
- Återanvändbar konfiguration
- Miljöspecifika värden

Jinja2 är Ansibles templating-motor.

---

## Så fungerar det

1. Skapa `.j2` template-fil
2. Använd `template` module i playbook
3. Ansible renderar med variabler
4. Resultat kopieras till destination

---

## Grundläggande syntax

```jinja2
{# templates/nginx.conf.j2 #}
{# Detta är en Jinja2-kommentar #}

# Nginx configuration for {{ app_name }}
# Generated by Ansible - DO NOT EDIT MANUALLY

user {{ nginx_user | default('www-data') }};
worker_processes {{ nginx_workers | default('auto') }};

events {
    worker_connections {{ worker_connections | default(1024) }};
}

http {
    server {
        listen {{ http_port }};
        server_name {{ server_name }};
        root {{ doc_root }};

        location / {
            proxy_pass http://{{ backend_host }}:{{ backend_port }};
        }
    }
}
```

```yaml
# I playbook
- name: Deploy nginx config
  template:
    src: templates/nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  vars:
    app_name: myapp
    http_port: 80
    server_name: example.com
    doc_root: /var/www/html
    backend_host: 127.0.0.1
    backend_port: 8080
```

---

## Villkor i templates

```jinja2
{# templates/app.conf.j2 #}

{% if environment == 'production' %}
DEBUG = false
LOG_LEVEL = WARNING
{% elif environment == 'staging' %}
DEBUG = true
LOG_LEVEL = INFO
{% else %}
DEBUG = true
LOG_LEVEL = DEBUG
{% endif %}

# Database configuration
{% if db_replica is defined and db_replica %}
DATABASE_URL = {{ db_primary_url }}
DATABASE_REPLICA_URL = {{ db_replica_url }}
{% else %}
DATABASE_URL = {{ db_primary_url }}
{% endif %}

# Optional features
{% if enable_cache | default(false) %}
CACHE_BACKEND = redis
CACHE_URL = {{ cache_url }}
{% endif %}
```

---

## Loopar i templates

```jinja2
{# templates/hosts.j2 #}
# /etc/hosts - Generated by Ansible

127.0.0.1   localhost
::1         localhost

# Application servers
{% for host in app_servers %}
{{ hostvars[host].ansible_host }}   {{ host }}
{% endfor %}

# Database servers
{% for host in groups['dbservers'] %}
{{ hostvars[host].ansible_default_ipv4.address }}   {{ host }} {{ host.split('.')[0] }}
{% endfor %}
```

```jinja2
{# templates/vhosts.conf.j2 #}
# Virtual hosts configuration

{% for vhost in virtual_hosts %}
<VirtualHost *:{{ vhost.port | default(80) }}>
    ServerName {{ vhost.name }}
    DocumentRoot {{ vhost.root }}

    {% if vhost.aliases is defined %}
    {% for alias in vhost.aliases %}
    ServerAlias {{ alias }}
    {% endfor %}
    {% endif %}

    {% if vhost.ssl | default(false) %}
    SSLEngine on
    SSLCertificateFile {{ vhost.ssl_cert }}
    SSLCertificateKeyFile {{ vhost.ssl_key }}
    {% endif %}
</VirtualHost>

{% endfor %}
```

---

## Filters i templates

```jinja2
{# templates/config.j2 #}

# String filters
APP_NAME = {{ app_name | upper }}
SLUG = {{ app_name | lower | replace(' ', '-') }}
TRUNCATED = {{ description | truncate(50) }}

# Default values
PORT = {{ port | default(8080) }}
TIMEOUT = {{ timeout | default(30) }}

# JSON/YAML output
CONFIG_JSON = '{{ config_dict | to_json }}'
CONFIG_YAML = |
{{ config_dict | to_nice_yaml(indent=2) | indent(2) }}

# List operations
SERVERS = {{ server_list | join(',') }}
FIRST = {{ items | first }}
LAST = {{ items | last }}
COUNT = {{ items | length }}

# Math
MEMORY_GB = {{ ansible_memtotal_mb / 1024 | round(1) }}
WORKERS = {{ ansible_processor_vcpus | int * 2 }}

# Conditional
STATUS = {{ 'enabled' if feature_enabled else 'disabled' }}
```

---

## Whitespace control

```jinja2
{# Utan kontroll - extra radbrytningar #}
{% for item in items %}
{{ item }}
{% endfor %}

{# Med whitespace control #}
{% for item in items -%}
{{ item }}
{%- endfor %}

{# Resultat: item1item2item3 (ingen whitespace) #}

{# Bättre kontroll #}
{% for item in items %}
{{ item }}{% if not loop.last %},{% endif %}
{% endfor %}

{# Eller använd join filter #}
{{ items | join(', ') }}
```

---

## Template validation

```yaml
tasks:
  - name: Deploy nginx config with validation
    template:
      src: templates/nginx.conf.j2
      dest: /etc/nginx/nginx.conf
      validate: nginx -t -c %s         # %s ersätts med temp-fil

  - name: Deploy sudoers with validation
    template:
      src: templates/sudoers.j2
      dest: /etc/sudoers.d/app
      validate: visudo -cf %s

  - name: Deploy Apache config
    template:
      src: templates/httpd.conf.j2
      dest: /etc/httpd/conf/httpd.conf
      validate: apachectl -t -f %s
```

---

## Template inheritance

```jinja2
{# templates/base.conf.j2 #}
# Base configuration
{% block header %}
# Default header
{% endblock %}

{% block main %}
# Main content goes here
{% endblock %}

{% block footer %}
# Generated by Ansible
{% endblock %}
```

```jinja2
{# templates/app.conf.j2 #}
{% extends "base.conf.j2" %}

{% block header %}
# Application: {{ app_name }}
# Environment: {{ environment }}
{% endblock %}

{% block main %}
DATABASE_URL = {{ db_url }}
REDIS_URL = {{ redis_url }}
{% endblock %}
```

---

## Key Takeaways

1. Templates använder Jinja2-syntax
2. `{{ variable }}` för värden
3. `{% if/for %}` för logik
4. Filters transformerar data
5. `validate` säkerställer korrekt syntax
''',
        },
        {
            "title": "Roles",
            "slug": "roles",
            "difficulty": "intermediate",
            "content": '''
# Roles

## Varför behöver du kunna detta?

Roles organiserar Ansible-kod:

- Återanvändbar och delbar
- Standardiserad struktur
- Enkel att testa
- Separat utveckling

En role = en specifik funktion (nginx, postgresql, etc.).

---

## Så fungerar det

En role har en definierad katalogstruktur:

1. `tasks/` - huvudsakliga tasks
2. `handlers/` - handlers
3. `templates/` - Jinja2 templates
4. `files/` - statiska filer
5. `vars/` - variabler
6. `defaults/` - default-värden

---

## Role-struktur

```bash
# Skapa role med ansible-galaxy
ansible-galaxy role init nginx

# Resulterande struktur
roles/nginx/
├── README.md
├── defaults/
│   └── main.yml              # Default-variabler (lägst prioritet)
├── files/
│   └── ssl.crt               # Statiska filer
├── handlers/
│   └── main.yml              # Handlers
├── meta/
│   └── main.yml              # Role metadata och dependencies
├── tasks/
│   └── main.yml              # Huvudsakliga tasks
├── templates/
│   └── nginx.conf.j2         # Jinja2 templates
├── tests/
│   ├── inventory
│   └── test.yml
└── vars/
    └── main.yml              # Role-variabler (hög prioritet)
```

---

## Skapa en role

```yaml
# roles/nginx/defaults/main.yml
---
nginx_port: 80
nginx_worker_processes: auto
nginx_worker_connections: 1024
nginx_sites: []
```

```yaml
# roles/nginx/tasks/main.yml
---
- name: Install nginx
  apt:
    name: nginx
    state: present
    update_cache: yes

- name: Create sites directory
  file:
    path: /etc/nginx/sites-available
    state: directory
    mode: '0755'

- name: Deploy nginx config
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    validate: nginx -t -c %s
  notify: Restart nginx

- name: Deploy site configs
  template:
    src: site.conf.j2
    dest: "/etc/nginx/sites-available/{{ item.name }}.conf"
  loop: "{{ nginx_sites }}"
  notify: Reload nginx

- name: Enable sites
  file:
    src: "/etc/nginx/sites-available/{{ item.name }}.conf"
    dest: "/etc/nginx/sites-enabled/{{ item.name }}.conf"
    state: link
  loop: "{{ nginx_sites }}"
  notify: Reload nginx

- name: Ensure nginx is running
  service:
    name: nginx
    state: started
    enabled: yes
```

```yaml
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
```

---

## Använda roles

```yaml
# site.yml - Använd roles i playbook
---
- name: Configure web servers
  hosts: webservers
  become: yes

  roles:
    # Enkel användning
    - nginx

    # Med variabler
    - role: nginx
      vars:
        nginx_port: 8080

    # Med villkor
    - role: nginx
      when: ansible_os_family == "Debian"

    # Med tags
    - role: nginx
      tags:
        - web
        - nginx
```

```yaml
# Alternativ syntax med tasks
- name: Configure servers
  hosts: all
  become: yes

  tasks:
    - name: Apply common role
      include_role:
        name: common

    - name: Apply nginx role conditionally
      include_role:
        name: nginx
      when: "'webservers' in group_names"
```

---

## Role dependencies

```yaml
# roles/webapp/meta/main.yml
---
dependencies:
  - role: common

  - role: nginx
    vars:
      nginx_port: 80

  - role: nodejs
    vars:
      nodejs_version: "18.x"
```

```yaml
# roles/common/meta/main.yml
---
galaxy_info:
  author: your_name
  description: Common server setup
  company: Your Company
  license: MIT
  min_ansible_version: "2.14"
  platforms:
    - name: Ubuntu
      versions:
        - jammy
        - focal
  galaxy_tags:
    - system
    - common
```

---

## Task includes

```yaml
# roles/nginx/tasks/main.yml
---
- name: Include OS-specific vars
  include_vars: "{{ ansible_os_family | lower }}.yml"

- name: Include OS-specific tasks
  include_tasks: "{{ ansible_os_family | lower }}.yml"

- name: Include common tasks
  include_tasks: configure.yml

- name: Include SSL tasks if enabled
  include_tasks: ssl.yml
  when: nginx_ssl_enabled | default(false)
```

```yaml
# roles/nginx/tasks/debian.yml
---
- name: Install nginx (Debian)
  apt:
    name: nginx
    state: present
```

```yaml
# roles/nginx/tasks/redhat.yml
---
- name: Install nginx (RedHat)
  yum:
    name: nginx
    state: present
```

---

## Role testing

```yaml
# roles/nginx/tests/test.yml
---
- name: Test nginx role
  hosts: localhost
  connection: local
  become: yes

  vars:
    nginx_sites:
      - name: test
        server_name: test.local
        root: /var/www/test

  roles:
    - nginx

  post_tasks:
    - name: Verify nginx is running
      command: systemctl is-active nginx
      changed_when: false

    - name: Verify nginx config
      command: nginx -t
      changed_when: false
```

```bash
# Kör test
cd roles/nginx
ansible-playbook tests/test.yml -i tests/inventory
```

---

## Key Takeaways

1. Roles organiserar kod i standardiserad struktur
2. `defaults/` för överskrivbara standardvärden
3. `include_tasks` för konditionell inkludering
4. `meta/main.yml` för dependencies
5. `ansible-galaxy role init` skapar struktur
''',
        },
        {
            "title": "Ansible Galaxy",
            "slug": "ansible-galaxy",
            "difficulty": "intermediate",
            "content": '''
# Ansible Galaxy

## Varför behöver du kunna detta?

Ansible Galaxy är Ansibles pakethanterare:

- Tusentals färdiga roles och collections
- Dela dina egna roles
- Versionerade beroenden
- Spar utvecklingstid

Återuppfinn inte hjulet - använd Galaxy.

---

## Så fungerar det

Galaxy innehåller:

1. **Roles** - återanvändbara rollpaket
2. **Collections** - bundlade roles, modules, plugins
3. **CLI** - ansible-galaxy kommando

---

## Söka och installera

```bash
# Sök roles
ansible-galaxy search nginx
ansible-galaxy search nginx --platforms Ubuntu

# Visa role-info
ansible-galaxy info geerlingguy.nginx

# Installera role
ansible-galaxy install geerlingguy.nginx
ansible-galaxy install geerlingguy.nginx,3.1.0       # Specifik version
ansible-galaxy install geerlingguy.nginx -p roles/   # Till specifik sökväg

# Installera collection
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install azure.azcollection
```

---

## Requirements file

```yaml
# requirements.yml - Definiera beroenden
---
roles:
  - name: geerlingguy.nginx
    version: "3.1.0"

  - name: geerlingguy.postgresql
    version: "3.4.0"

  - name: geerlingguy.docker

  # Från git
  - name: custom-role
    src: git+https://github.com/company/ansible-role.git
    version: v1.2.0

  # Från tar.gz
  - name: custom-role-tar
    src: https://example.com/role.tar.gz

collections:
  - name: community.general
    version: ">=6.0.0"

  - name: amazon.aws
    version: "6.5.0"

  - name: community.docker
```

```bash
# Installera allt från requirements
ansible-galaxy install -r requirements.yml
ansible-galaxy collection install -r requirements.yml

# Force reinstall
ansible-galaxy install -r requirements.yml --force

# Installera till specifik sökväg
ansible-galaxy install -r requirements.yml -p ./roles
ansible-galaxy collection install -r requirements.yml -p ./collections
```

---

## Använda collections

```yaml
# playbook.yml - Använd collection modules
---
- name: Deploy to AWS
  hosts: localhost
  connection: local

  collections:
    - amazon.aws                       # Gör alla modules tillgängliga

  tasks:
    - name: Create S3 bucket
      s3_bucket:                       # Utan FQCN
        name: my-bucket
        state: present

    # Eller med FQCN (Fully Qualified Collection Name)
    - name: Create EC2 instance
      amazon.aws.ec2_instance:
        name: web-server
        instance_type: t3.micro
        image_id: ami-12345678
```

```yaml
# Alternativt i ansible.cfg
[defaults]
collections_paths = ./collections:~/.ansible/collections:/usr/share/ansible/collections
```

---

## Skapa egen role för Galaxy

```bash
# Initiera ny role
ansible-galaxy role init my_company.webserver

# Struktur
my_company.webserver/
├── README.md                         # Dokumentation
├── meta/
│   └── main.yml                      # Galaxy metadata
├── defaults/
│   └── main.yml
├── tasks/
│   └── main.yml
└── ...
```

```yaml
# meta/main.yml - Galaxy metadata
---
galaxy_info:
  role_name: webserver
  namespace: my_company
  author: Your Name
  description: Configure webserver with nginx
  company: My Company
  license: MIT
  min_ansible_version: "2.14"

  platforms:
    - name: Ubuntu
      versions:
        - jammy
        - focal
    - name: Debian
      versions:
        - bullseye

  galaxy_tags:
    - web
    - nginx
    - proxy

dependencies:
  - geerlingguy.nginx
```

---

## Skapa egen collection

```bash
# Skapa collection-struktur
ansible-galaxy collection init my_company.infrastructure

# Struktur
my_company/infrastructure/
├── README.md
├── galaxy.yml                        # Collection metadata
├── plugins/
│   ├── modules/                      # Custom modules
│   ├── lookup/                       # Custom lookup plugins
│   └── filter/                       # Custom filter plugins
├── roles/
│   ├── webserver/
│   └── database/
└── playbooks/
```

```yaml
# galaxy.yml
---
namespace: my_company
name: infrastructure
version: 1.0.0
readme: README.md
authors:
  - Your Name <you@example.com>
description: Infrastructure automation for My Company
license:
  - MIT
tags:
  - infrastructure
  - devops
dependencies:
  community.general: ">=6.0.0"
repository: https://github.com/my-company/ansible-infrastructure
```

```bash
# Bygg collection
ansible-galaxy collection build

# Publicera till Galaxy
ansible-galaxy collection publish my_company-infrastructure-1.0.0.tar.gz --token YOUR_API_TOKEN
```

---

## Private Galaxy / Automation Hub

```bash
# Använd privat Galaxy-server
ansible-galaxy collection install my_collection \
  --server https://galaxy.internal.company.com

# Konfigurera i ansible.cfg
[galaxy]
server_list = private_galaxy, galaxy

[galaxy_server.private_galaxy]
url = https://galaxy.internal.company.com/api/
token = YOUR_TOKEN

[galaxy_server.galaxy]
url = https://galaxy.ansible.com/
```

---

## Version management

```yaml
# requirements.yml - Version constraints
---
collections:
  - name: community.general
    version: ">=6.0.0,<7.0.0"         # Range

  - name: amazon.aws
    version: "6.5.0"                  # Exakt version

  - name: community.docker
    version: "*"                      # Senaste

roles:
  - name: geerlingguy.nginx
    version: ">=3.0.0"
```

```bash
# Lista installerade
ansible-galaxy role list
ansible-galaxy collection list

# Visa installerad version
ansible-galaxy collection list community.general
```

---

## Key Takeaways

1. Galaxy har tusentals färdiga roles och collections
2. `requirements.yml` för versionerade beroenden
3. Collections buntar roles, modules, plugins
4. FQCN för tydlig module-referens
5. Skapa och dela egna roles/collections
''',
        },
        {
            "title": "Conditionals & Loops",
            "slug": "conditionals-loops",
            "difficulty": "intermediate",
            "content": '''
# Conditionals & Loops

## Varför behöver du kunna detta?

Villkor och loopar gör playbooks flexibla:

- Anpassa efter OS och miljö
- Iterera över listor och dictionaries
- Dynamiskt antal resurser
- Conditional task execution

Kraftfulla konstruktioner för komplex automation.

---

## Så fungerar det

- `when` - kör task om villkor är sant
- `loop` - iterera över lista
- `with_*` - legacy loop-syntax
- Kombinera för komplex logik

---

## When conditionals

```yaml
tasks:
  # Enkel condition
  - name: Install on Ubuntu
    apt:
      name: nginx
      state: present
    when: ansible_distribution == "Ubuntu"

  # Multiple conditions (AND)
  - name: Install on Ubuntu 22.04
    apt:
      name: nginx
      state: present
    when:
      - ansible_distribution == "Ubuntu"
      - ansible_distribution_version == "22.04"

  # OR condition
  - name: Install on Debian family
    apt:
      name: nginx
      state: present
    when: ansible_distribution == "Ubuntu" or ansible_distribution == "Debian"

  # Använd facts
  - name: Configure for high memory
    template:
      src: high_memory.conf.j2
      dest: /etc/app.conf
    when: ansible_memtotal_mb > 8192

  # Variabel exists
  - name: Configure if defined
    template:
      src: custom.conf.j2
      dest: /etc/custom.conf
    when: custom_config is defined

  # Boolean test
  - name: Configure SSL
    include_tasks: ssl.yml
    when: ssl_enabled | default(false) | bool
```

---

## Register och conditionals

```yaml
tasks:
  - name: Check if file exists
    stat:
      path: /etc/myapp.conf
    register: config_file

  - name: Create config if missing
    template:
      src: myapp.conf.j2
      dest: /etc/myapp.conf
    when: not config_file.stat.exists

  - name: Check service status
    command: systemctl is-active myapp
    register: service_status
    failed_when: false
    changed_when: false

  - name: Start service if not running
    service:
      name: myapp
      state: started
    when: service_status.rc != 0

  - name: Check version
    command: myapp --version
    register: version_output
    changed_when: false

  - name: Upgrade if old version
    apt:
      name: myapp
      state: latest
    when: "'1.0' in version_output.stdout"
```

---

## Loop basics

```yaml
tasks:
  # Enkel loop
  - name: Install packages
    apt:
      name: "{{ item }}"
      state: present
    loop:
      - nginx
      - curl
      - vim

  # Loop med index
  - name: Create users
    user:
      name: "{{ item }}"
      uid: "{{ 1000 + index }}"
    loop:
      - alice
      - bob
      - charlie
    loop_control:
      index_var: index

  # Loop med label (för output)
  - name: Create users with details
    user:
      name: "{{ item.name }}"
      groups: "{{ item.groups }}"
    loop:
      - { name: alice, groups: sudo }
      - { name: bob, groups: www-data }
    loop_control:
      label: "{{ item.name }}"
```

---

## Dictionary loops

```yaml
vars:
  users:
    alice:
      groups: sudo
      shell: /bin/bash
    bob:
      groups: www-data
      shell: /bin/sh

tasks:
  # Loop över dict
  - name: Create users from dict
    user:
      name: "{{ item.key }}"
      groups: "{{ item.value.groups }}"
      shell: "{{ item.value.shell }}"
    loop: "{{ users | dict2items }}"

  # Nested dict
  - name: Show user info
    debug:
      msg: "User {{ item.key }} has groups {{ item.value.groups }}"
    loop: "{{ users | dict2items }}"
```

---

## Nested loops

```yaml
vars:
  environments:
    - dev
    - staging
    - prod
  services:
    - web
    - api
    - worker

tasks:
  # Product (alla kombinationer)
  - name: Create service directories
    file:
      path: "/opt/{{ item.0 }}/{{ item.1 }}"
      state: directory
    loop: "{{ environments | product(services) | list }}"

  # Subelements
  - name: Create user SSH keys
    authorized_key:
      user: "{{ item.0.name }}"
      key: "{{ item.1 }}"
    loop: "{{ users | subelements('ssh_keys') }}"

vars:
  users:
    - name: alice
      ssh_keys:
        - "ssh-rsa AAAA... alice@laptop"
        - "ssh-rsa BBBB... alice@desktop"
    - name: bob
      ssh_keys:
        - "ssh-rsa CCCC... bob@laptop"
```

---

## Until loops

```yaml
tasks:
  # Retry tills success
  - name: Wait for service to start
    uri:
      url: http://localhost:8080/health
      status_code: 200
    register: result
    until: result.status == 200
    retries: 30
    delay: 10                          # Sekunder mellan försök

  # Wait for file
  - name: Wait for lock file to disappear
    wait_for:
      path: /var/lock/myapp.lock
      state: absent
    timeout: 300

  # Custom condition
  - name: Wait for deployment
    command: kubectl get deployment myapp -o jsonpath='{.status.availableReplicas}'
    register: replicas
    until: replicas.stdout | int >= 3
    retries: 60
    delay: 5
```

---

## Loop with conditionals

```yaml
tasks:
  # Filter i loop
  - name: Install only enabled services
    apt:
      name: "{{ item.name }}"
      state: present
    loop: "{{ services }}"
    when: item.enabled | default(true)

  # Skip vissa items
  - name: Create users except admin
    user:
      name: "{{ item }}"
    loop:
      - alice
      - bob
      - admin
    when: item != 'admin'

  # Complex condition
  - name: Configure production services
    template:
      src: "{{ item.template }}"
      dest: "{{ item.dest }}"
    loop: "{{ services }}"
    when:
      - item.environment == 'production'
      - item.enabled | default(false)
```

---

## Block conditionals

```yaml
tasks:
  - name: Production-only configuration
    block:
      - name: Install monitoring agent
        apt:
          name: datadog-agent
          state: present

      - name: Configure monitoring
        template:
          src: datadog.yaml.j2
          dest: /etc/datadog-agent/datadog.yaml

      - name: Start monitoring
        service:
          name: datadog-agent
          state: started
    when: environment == 'production'
```

---

## Key Takeaways

1. `when` för conditional execution
2. `loop` ersätter gamla `with_*` syntax
3. `loop_control` för index och labels
4. `until` för retry-logik
5. Kombinera conditionals och loops
''',
        },
        {
            "title": "Error Handling",
            "slug": "error-handling",
            "difficulty": "intermediate",
            "content": '''
# Error Handling

## Varför behöver du kunna detta?

Fel händer - Ansible måste hantera dem:

- Graceful degradation
- Rollback vid misslyckande
- Fortsätt trots icke-kritiska fel
- Korrekt felrapportering

Robust automation kräver felhantering.

---

## Så fungerar det

Ansible erbjuder:

1. `ignore_errors` - fortsätt vid fel
2. `failed_when` - custom failure condition
3. `block/rescue/always` - try/catch/finally
4. `any_errors_fatal` - stoppa allt vid fel

---

## Ignore errors

```yaml
tasks:
  # Ignorera fel helt
  - name: Try to stop old service
    service:
      name: old-service
      state: stopped
    ignore_errors: yes

  # Ignorera och spara resultat
  - name: Check optional service
    command: systemctl status optional-service
    register: optional_status
    ignore_errors: yes

  - name: Configure if service exists
    template:
      src: optional.conf.j2
      dest: /etc/optional.conf
    when: optional_status.rc == 0

  # Ignorera unreachable hosts
  - name: Deploy to all hosts
    hosts: all
    ignore_unreachable: yes
    tasks:
      - name: Deploy app
        copy:
          src: app.tar.gz
          dest: /opt/app.tar.gz
```

---

## Failed_when

```yaml
tasks:
  # Custom failure condition
  - name: Run script
    command: /opt/deploy.sh
    register: deploy_result
    failed_when:
      - deploy_result.rc != 0
      - "'CRITICAL' in deploy_result.stderr"

  # Never fail
  - name: Check something
    command: /opt/check.sh
    register: check_result
    failed_when: false

  # Fail on specific output
  - name: Verify configuration
    command: /opt/verify.sh
    register: verify_result
    failed_when: "'ERROR' in verify_result.stdout"

  # Complex condition
  - name: Database migration
    command: /opt/migrate.sh
    register: migrate_result
    failed_when: >
      migrate_result.rc != 0 and
      'Already migrated' not in migrate_result.stdout
```

---

## Changed_when

```yaml
tasks:
  # Command som aldrig ändrar
  - name: Get current version
    command: cat /etc/version
    register: version
    changed_when: false

  # Custom change detection
  - name: Update configuration
    command: /opt/update-config.sh
    register: update_result
    changed_when: "'Updated' in update_result.stdout"

  # Alltid changed
  - name: Touch deploy marker
    command: touch /var/deploy_timestamp
    changed_when: true

  # Complex condition
  - name: Run migration
    command: /opt/migrate.sh
    register: migrate
    changed_when: "'Applied' in migrate.stdout"
    failed_when: "'ERROR' in migrate.stderr"
```

---

## Block/rescue/always

```yaml
tasks:
  - name: Handle deployment with recovery
    block:
      - name: Stop service
        service:
          name: myapp
          state: stopped

      - name: Deploy new version
        unarchive:
          src: app-v2.tar.gz
          dest: /opt/myapp
          remote_src: no

      - name: Run migrations
        command: /opt/myapp/migrate.sh

      - name: Start service
        service:
          name: myapp
          state: started

    rescue:
      - name: Log failure
        debug:
          msg: "Deployment failed, rolling back"

      - name: Rollback to previous version
        command: /opt/myapp/rollback.sh

      - name: Start service with old version
        service:
          name: myapp
          state: started

      - name: Send alert
        uri:
          url: https://alerts.example.com/webhook
          method: POST
          body_format: json
          body:
            message: "Deployment failed on {{ inventory_hostname }}"

    always:
      - name: Cleanup temp files
        file:
          path: /tmp/deploy
          state: absent

      - name: Record deployment attempt
        lineinfile:
          path: /var/log/deployments.log
          line: "{{ ansible_date_time.iso8601 }} - Deployment attempt completed"
```

---

## Any_errors_fatal

```yaml
# Stoppa vid första fel
- name: Critical deployment
  hosts: webservers
  any_errors_fatal: true

  tasks:
    - name: Check disk space
      command: df -h /
      register: disk_check
      failed_when: "'100%' in disk_check.stdout"

    - name: Deploy application
      copy:
        src: app.tar.gz
        dest: /opt/
```

```yaml
# Fail fast på specifika tasks
- name: Mixed criticality
  hosts: all

  tasks:
    - name: Critical check
      command: /opt/critical-check.sh
      any_errors_fatal: true

    - name: Non-critical task
      command: /opt/optional.sh
      ignore_errors: yes
```

---

## Assert och fail

```yaml
tasks:
  # Assert conditions
  - name: Verify prerequisites
    assert:
      that:
        - ansible_memtotal_mb >= 2048
        - ansible_processor_vcpus >= 2
        - ansible_distribution == "Ubuntu"
      fail_msg: "Server does not meet minimum requirements"
      success_msg: "All prerequisites met"

  # Conditional fail
  - name: Check environment
    fail:
      msg: "Cannot deploy to production on Friday!"
    when:
      - environment == 'production'
      - ansible_date_time.weekday == 'Friday'

  # Fail with details
  - name: Validate config
    assert:
      that:
        - db_host is defined
        - db_port | int > 0
        - db_name | length > 0
      fail_msg: |
        Database configuration invalid:
        - db_host: {{ db_host | default('NOT SET') }}
        - db_port: {{ db_port | default('NOT SET') }}
        - db_name: {{ db_name | default('NOT SET') }}
```

---

## Max_fail_percentage

```yaml
# Tillåt viss andel failures
- name: Rolling update
  hosts: webservers
  serial: 5                            # 5 hosts åt gången
  max_fail_percentage: 20              # Max 20% får faila

  tasks:
    - name: Deploy
      copy:
        src: app.tar.gz
        dest: /opt/app.tar.gz

    - name: Restart
      service:
        name: myapp
        state: restarted
```

---

## Key Takeaways

1. `ignore_errors` för icke-kritiska tasks
2. `failed_when` för custom failure conditions
3. `block/rescue/always` för strukturerad felhantering
4. `any_errors_fatal` stoppar allt vid första fel
5. `assert` validerar förutsättningar
''',
        },
        {
            "title": "Vault & Secrets",
            "slug": "vault-secrets",
            "difficulty": "intermediate",
            "content": '''
# Vault & Secrets

## Varför behöver du kunna detta?

Secrets måste skyddas:

- Lösenord
- API-nycklar
- Certifikat
- Databaskredentialer

Ansible Vault krypterar känslig data.

---

## Så fungerar det

Ansible Vault:

1. Krypterar filer med AES256
2. Stöd för flera vault-lösenord
3. Integrerat i playbook-körning
4. Versionskontrollvänligt

---

## Grundläggande vault

```bash
# Skapa krypterad fil
ansible-vault create secrets.yml

# Redigera krypterad fil
ansible-vault edit secrets.yml

# Visa innehåll
ansible-vault view secrets.yml

# Kryptera befintlig fil
ansible-vault encrypt vars/secrets.yml

# Dekryptera fil
ansible-vault decrypt vars/secrets.yml

# Ändra lösenord
ansible-vault rekey secrets.yml
```

---

## Vault i playbook

```yaml
# vars/secrets.yml (krypterad)
---
db_password: supersecret123
api_key: abc123xyz
ssl_private_key: |
  -----BEGIN PRIVATE KEY-----
  MIIEvgIBADANBg...
  -----END PRIVATE KEY-----
```

```yaml
# playbook.yml
---
- name: Deploy with secrets
  hosts: webservers
  become: yes

  vars_files:
    - vars/common.yml
    - vars/secrets.yml              # Krypterad fil

  tasks:
    - name: Configure database
      template:
        src: database.conf.j2
        dest: /etc/app/database.conf
      vars:
        password: "{{ db_password }}"
```

```bash
# Kör med vault password
ansible-playbook playbook.yml --ask-vault-pass
ansible-playbook playbook.yml --vault-password-file ~/.vault_pass
```

---

## Kryptera enskilda värden

```bash
# Kryptera en sträng
ansible-vault encrypt_string 'supersecret' --name 'db_password'

# Output:
# db_password: !vault |
#           $ANSIBLE_VAULT;1.1;AES256
#           61626364...
```

```yaml
# Använd i vars-fil (okrypterad fil med krypterat värde)
# vars/main.yml
---
app_name: myapp
environment: production

# Krypterat värde
db_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          61626364656667686970...

# Okrypterade värden
db_host: localhost
db_port: 5432
```

---

## Multipla vault-lösenord

```bash
# Vault ID för olika miljöer
ansible-vault create --vault-id dev@prompt secrets_dev.yml
ansible-vault create --vault-id prod@prompt secrets_prod.yml
ansible-vault create --vault-id prod@/path/to/prod_pass secrets_prod.yml

# Kör med multipla vault IDs
ansible-playbook playbook.yml \
  --vault-id dev@prompt \
  --vault-id prod@~/.vault_prod
```

```yaml
# Krypterade värden med vault ID
db_password: !vault |
          $ANSIBLE_VAULT;1.2;AES256;prod
          61626364...
```

---

## Vault password file

```bash
# Skapa password-fil
echo 'mysecretpassword' > ~/.vault_pass
chmod 600 ~/.vault_pass

# Konfigurera i ansible.cfg
[defaults]
vault_password_file = ~/.vault_pass
```

```python
#!/usr/bin/env python3
# vault_pass_script.py - Hämta från extern källa
import subprocess
import sys

# Hämta från 1Password
result = subprocess.run(
    ['op', 'read', 'op://Vault/AnsibleVault/password'],
    capture_output=True,
    text=True
)
print(result.stdout.strip())
```

```bash
chmod +x vault_pass_script.py
ansible-playbook playbook.yml --vault-password-file ./vault_pass_script.py
```

---

## Best practices struktur

```bash
# Separera krypterat från okrypterat
group_vars/
├── all/
│   ├── vars.yml              # Okrypterade variabler
│   └── vault.yml             # Krypterade variabler
├── production/
│   ├── vars.yml
│   └── vault.yml
└── staging/
    ├── vars.yml
    └── vault.yml
```

```yaml
# group_vars/production/vars.yml (okrypterad)
---
environment: production
db_host: db.prod.example.com
db_name: app_production
log_level: WARNING
```

```yaml
# group_vars/production/vault.yml (krypterad)
---
vault_db_password: supersecret
vault_api_key: abc123xyz
vault_ssl_key: |
  -----BEGIN PRIVATE KEY-----
  ...
```

```yaml
# Referera vault-variabler
# group_vars/production/vars.yml
---
db_password: "{{ vault_db_password }}"
api_key: "{{ vault_api_key }}"
```

---

## External secrets

```yaml
# Hämta från HashiCorp Vault
- name: Get secret from HashiCorp Vault
  set_fact:
    db_password: "{{ lookup('hashi_vault', 'secret/data/myapp:db_password') }}"

# Hämta från AWS Secrets Manager
- name: Get secret from AWS
  set_fact:
    db_password: "{{ lookup('amazon.aws.aws_secret', 'myapp/db_password') }}"

# Hämta från Azure Key Vault
- name: Get secret from Azure
  set_fact:
    db_password: "{{ lookup('azure.azcollection.azure_keyvault_secret', 'db-password', vault_url='https://myvault.vault.azure.net') }}"
```

---

## Key Takeaways

1. `ansible-vault` krypterar med AES256
2. Kryptera hela filer eller enskilda värden
3. Vault IDs för multipla lösenord
4. Separera vault-variabler med `vault_` prefix
5. Externa secret managers för enterprise
''',
        },
        {
            "title": "Ansible in CI/CD",
            "slug": "ansible-cicd",
            "difficulty": "advanced",
            "content": '''
# Ansible in CI/CD

## Varför behöver du kunna detta?

Ansible i pipelines:

- Automatisk deployment vid merge
- Testning av playbooks
- Consistent miljöer
- Audit trail

GitOps med Ansible.

---

## Så fungerar det

CI/CD med Ansible:

1. Lint och syntax-check
2. Molecule testing
3. Deploy till staging
4. Approval gates
5. Deploy till production

---

## GitHub Actions

```yaml
# .github/workflows/ansible.yml
name: Ansible CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

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
          pip install ansible ansible-lint yamllint

      - name: YAML Lint
        run: yamllint .

      - name: Ansible Lint
        run: ansible-lint

      - name: Syntax check
        run: |
          ansible-playbook site.yml --syntax-check

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Molecule
        run: |
          pip install molecule molecule-docker ansible

      - name: Run Molecule tests
        run: |
          cd roles/webserver
          molecule test

  deploy-staging:
    needs: test
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment: staging

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Ansible
        run: pip install ansible

      - name: Setup SSH key
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa
          ssh-keyscan -H ${{ secrets.STAGING_HOST }} >> ~/.ssh/known_hosts

      - name: Deploy to staging
        run: |
          ansible-playbook -i inventory/staging site.yml
        env:
          ANSIBLE_VAULT_PASSWORD: ${{ secrets.VAULT_PASSWORD }}

  deploy-production:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/checkout@v4

      - name: Install Ansible
        run: pip install ansible

      - name: Setup SSH
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.PROD_SSH_KEY }}" > ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa

      - name: Deploy to production
        run: |
          ansible-playbook -i inventory/production site.yml \
            --vault-password-file <(echo "${{ secrets.VAULT_PASSWORD }}")
```

---

## GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - lint
  - test
  - deploy

variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

cache:
  paths:
    - .cache/pip/

lint:
  stage: lint
  image: python:3.11
  script:
    - pip install ansible ansible-lint yamllint
    - yamllint .
    - ansible-lint
    - ansible-playbook site.yml --syntax-check

molecule-test:
  stage: test
  image: docker:latest
  services:
    - docker:dind
  before_script:
    - apk add --no-cache python3 py3-pip
    - pip install molecule molecule-docker ansible
  script:
    - cd roles/webserver
    - molecule test

deploy-staging:
  stage: deploy
  image: python:3.11
  environment:
    name: staging
  only:
    - develop
  before_script:
    - pip install ansible
    - mkdir -p ~/.ssh
    - echo "$SSH_PRIVATE_KEY" > ~/.ssh/id_rsa
    - chmod 600 ~/.ssh/id_rsa
  script:
    - ansible-playbook -i inventory/staging site.yml
  variables:
    ANSIBLE_HOST_KEY_CHECKING: "false"

deploy-production:
  stage: deploy
  image: python:3.11
  environment:
    name: production
  only:
    - main
  when: manual                         # Manuell approve
  script:
    - pip install ansible
    - ansible-playbook -i inventory/production site.yml
```

---

## Ansible-lint config

```yaml
# .ansible-lint
---
profile: production

exclude_paths:
  - .cache/
  - .github/
  - molecule/

skip_list:
  - yaml[line-length]
  - name[casing]

warn_list:
  - experimental

enable_list:
  - no-same-owner

offline: false

use_default_rules: true
```

---

## Molecule testing

```yaml
# roles/webserver/molecule/default/molecule.yml
---
dependency:
  name: galaxy
driver:
  name: docker
platforms:
  - name: ubuntu-22
    image: geerlingguy/docker-ubuntu2204-ansible
    pre_build_image: true
    privileged: true
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:rw
    command: /lib/systemd/systemd

  - name: debian-12
    image: geerlingguy/docker-debian12-ansible
    pre_build_image: true
    privileged: true
    command: /lib/systemd/systemd

provisioner:
  name: ansible
  playbooks:
    converge: converge.yml
    verify: verify.yml

verifier:
  name: ansible

scenario:
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
    - verify
    - cleanup
    - destroy
```

```yaml
# molecule/default/converge.yml
---
- name: Converge
  hosts: all
  become: yes

  roles:
    - webserver
```

```yaml
# molecule/default/verify.yml
---
- name: Verify
  hosts: all
  gather_facts: false

  tasks:
    - name: Check nginx is running
      command: systemctl is-active nginx
      changed_when: false

    - name: Check nginx responds
      uri:
        url: http://localhost
        status_code: 200
```

---

## AWX / Ansible Tower

```yaml
# AWX job template config (via API)
- name: Create job template
  awx.awx.job_template:
    name: "Deploy Web Application"
    organization: "My Org"
    project: "Infrastructure"
    playbook: "site.yml"
    inventory: "Production"
    credentials:
      - "SSH Key"
      - "Vault Password"
    extra_vars:
      environment: production
    ask_variables_on_launch: yes
```

```bash
# Trigger AWX job från CI/CD
curl -X POST \
  -H "Authorization: Bearer $AWX_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"extra_vars": {"version": "1.2.3"}}' \
  "https://awx.example.com/api/v2/job_templates/123/launch/"
```

---

## Key Takeaways

1. Lint och syntax-check i varje pipeline
2. Molecule för integration testing
3. Separata environments med approval gates
4. Vault-lösenord som CI/CD secrets
5. AWX/Tower för enterprise orchestration
''',
        },
        {
            "title": "Dynamic Inventory",
            "slug": "dynamic-inventory",
            "difficulty": "advanced",
            "content": '''
# Dynamic Inventory

## Varför behöver du kunna detta?

Cloud-infrastruktur är dynamisk:

- Servrar skapas och tas bort
- Auto-scaling ändrar antal instanser
- IP-adresser ändras
- Statisk inventory blir snabbt inaktuell

Dynamisk inventory synkar automatiskt.

---

## Så fungerar det

Dynamisk inventory:

1. Plugin/script frågar cloud API
2. Returnerar aktuell infrastruktur som JSON
3. Ansible använder för targeting
4. Realtidsdata vid varje körning

---

## AWS EC2 plugin

```yaml
# inventory/aws_ec2.yml
---
plugin: amazon.aws.aws_ec2

regions:
  - eu-north-1
  - eu-west-1

# Filtrera instanser
filters:
  instance-state-name: running
  tag:Environment:
    - production
    - staging

# Skapa grupper baserat på tags
keyed_groups:
  - key: tags.Environment
    prefix: env
    separator: "_"
  - key: tags.Role
    prefix: role
  - key: placement.availability_zone
    prefix: az
  - key: instance_type
    prefix: type

# Grupperingar
groups:
  webservers: "'web' in tags.Role"
  dbservers: "'db' in tags.Role"
  production: "tags.Environment == 'production'"

# Host variabler
compose:
  ansible_host: private_ip_address
  ansible_user: "'ubuntu'"
  instance_id: instance_id
  ec2_region: placement.region

# Hostnames
hostnames:
  - tag:Name
  - private-ip-address
  - instance-id
```

```bash
# Installera AWS collection
ansible-galaxy collection install amazon.aws

# Konfigurera AWS credentials
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

# Testa inventory
ansible-inventory -i inventory/aws_ec2.yml --graph
ansible-inventory -i inventory/aws_ec2.yml --list

# Använd i playbook
ansible-playbook -i inventory/aws_ec2.yml site.yml
```

---

## Azure plugin

```yaml
# inventory/azure_rm.yml
---
plugin: azure.azcollection.azure_rm

auth_source: auto

include_vm_resource_groups:
  - production-rg
  - staging-rg

keyed_groups:
  - key: tags.Environment
    prefix: env
  - key: tags.Role
    prefix: role
  - key: location
    prefix: location

conditional_groups:
  webservers: "'web' in tags.Role"
  linux: "os_profile.system == 'Linux'"

hostvar_expressions:
  ansible_host: private_ipv4_addresses[0]
  ansible_user: "'azureuser'"

exclude_host_filters:
  - powerstate != 'running'
```

```bash
# Installera Azure collection
ansible-galaxy collection install azure.azcollection
pip install azure-identity azure-mgmt-compute azure-mgmt-network

# Autentisera
az login

# Testa
ansible-inventory -i inventory/azure_rm.yml --graph
```

---

## GCP plugin

```yaml
# inventory/gcp.yml
---
plugin: google.cloud.gcp_compute

projects:
  - my-gcp-project

regions:
  - europe-north1
  - europe-west1

filters:
  - status = RUNNING

keyed_groups:
  - key: labels.environment
    prefix: env
  - key: labels.role
    prefix: role
  - key: zone
    prefix: zone

groups:
  webservers: "'web' in labels.role"

compose:
  ansible_host: networkInterfaces[0].networkIP
  ansible_user: "'ubuntu'"

hostnames:
  - name
  - public_ip
  - private_ip
```

```bash
# Installera GCP collection
ansible-galaxy collection install google.cloud

# Autentisera
export GCP_SERVICE_ACCOUNT_FILE=/path/to/service-account.json

# Eller
gcloud auth application-default login

ansible-inventory -i inventory/gcp.yml --graph
```

---

## Kubernetes plugin

```yaml
# inventory/k8s.yml
---
plugin: kubernetes.core.k8s

connections:
  - kubeconfig: ~/.kube/config
    context: production

namespaces:
  - default
  - production

# Gruppera pods
keyed_groups:
  - key: labels.app
    prefix: app
  - key: labels.environment
    prefix: env
  - key: namespace
    prefix: ns

compose:
  ansible_host: status.podIP
  ansible_connection: "'kubectl'"
```

---

## Custom dynamic inventory

```python
#!/usr/bin/env python3
# inventory/custom_inventory.py

import json
import argparse
import requests

def get_inventory():
    # Hämta data från intern CMDB
    response = requests.get(
        'https://cmdb.internal/api/servers',
        headers={'Authorization': 'Bearer TOKEN'}
    )
    servers = response.json()

    inventory = {
        '_meta': {
            'hostvars': {}
        },
        'all': {
            'children': ['webservers', 'dbservers']
        },
        'webservers': {
            'hosts': []
        },
        'dbservers': {
            'hosts': []
        }
    }

    for server in servers:
        hostname = server['hostname']
        role = server['role']

        # Lägg till i rätt grupp
        if role == 'web':
            inventory['webservers']['hosts'].append(hostname)
        elif role == 'db':
            inventory['dbservers']['hosts'].append(hostname)

        # Host-variabler
        inventory['_meta']['hostvars'][hostname] = {
            'ansible_host': server['ip_address'],
            'ansible_user': server.get('ssh_user', 'deploy'),
            'server_id': server['id'],
            'environment': server['environment']
        }

    return inventory

def get_host(hostname):
    # Hämta specifik host
    response = requests.get(
        f'https://cmdb.internal/api/servers/{hostname}'
    )
    return response.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--host', type=str)
    args = parser.parse_args()

    if args.list:
        print(json.dumps(get_inventory(), indent=2))
    elif args.host:
        print(json.dumps(get_host(args.host), indent=2))
```

```bash
# Gör körbar
chmod +x inventory/custom_inventory.py

# Testa
./inventory/custom_inventory.py --list
./inventory/custom_inventory.py --host web1.example.com

# Använd
ansible-playbook -i inventory/custom_inventory.py site.yml
```

---

## Kombinera inventory sources

```bash
# Directory med flera sources
inventory/
├── static_hosts.yml          # Statiska hosts
├── aws_ec2.yml               # AWS EC2
├── azure_rm.yml              # Azure VMs
└── group_vars/
    └── all.yml

# Ansible läser alla filer
ansible-playbook -i inventory/ site.yml
```

```ini
# ansible.cfg
[defaults]
inventory = ./inventory
```

---

## Key Takeaways

1. Dynamic inventory synkar med cloud APIs
2. `keyed_groups` skapar automatiska grupper
3. `compose` definierar host-variabler
4. Custom scripts för interna system
5. Kombinera statisk och dynamisk inventory
''',
        },
        {
            "title": "Performance Tuning",
            "slug": "performance-tuning",
            "difficulty": "advanced",
            "content": '''
# Performance Tuning

## Varför behöver du kunna detta?

Ansible kan vara långsamt:

- Hundratals servrar
- Många tasks
- Stora filer
- SSH overhead

Optimering gör stor skillnad.

---

## Så fungerar det

Prestandaoptimering:

1. Parallellism (forks)
2. Pipelining
3. Caching
4. Effektiva playbooks
5. Mitogen acceleration

---

## Grundläggande tuning

```ini
# ansible.cfg
[defaults]
# Parallella anslutningar
forks = 50                             # Default: 5

# Snabbare SSH
host_key_checking = False              # Skippa host key verify
gathering = smart                      # Cache facts

# Callback för timing
callback_whitelist = profile_tasks, timer

[ssh_connection]
# SSH pipelining (stor skillnad!)
pipelining = True

# Multiplexing
ssh_args = -o ControlMaster=auto -o ControlPersist=60s -o PreferSharedKey=yes

# Snabbare transfer
transfer_method = piped
```

---

## Fact caching

```ini
# ansible.cfg
[defaults]
gathering = smart                      # Samla bara om cache saknas
fact_caching = jsonfile                # Cache backend
fact_caching_connection = /tmp/ansible_facts_cache
fact_caching_timeout = 86400           # 24 timmar

# Eller Redis
fact_caching = redis
fact_caching_connection = localhost:6379:0
fact_caching_prefix = ansible_facts_
```

```yaml
# Manuellt kontrollera facts
- name: Deploy without facts
  hosts: webservers
  gather_facts: no                     # Skippa om inte behövs

  tasks:
    - name: Explicit fact gathering
      setup:
        gather_subset:
          - network
          - hardware
      when: need_facts | default(false)
```

---

## Pipelining

```ini
# ansible.cfg
[ssh_connection]
pipelining = True
```

```bash
# Kräver på målservrar:
# /etc/sudoers måste ha:
# Defaults !requiretty

# Eller för specifik user:
# deploy ALL=(ALL) NOPASSWD: ALL
# Defaults:deploy !requiretty
```

---

## Async tasks

```yaml
tasks:
  # Kör asynkront (fire and forget)
  - name: Long running task
    command: /opt/long-script.sh
    async: 3600                        # Max runtime (sekunder)
    poll: 0                            # Vänta inte på resultat
    register: long_task

  # Fortsätt med annat
  - name: Do other things
    apt:
      name: nginx
      state: present

  # Kolla status senare
  - name: Check on long task
    async_status:
      jid: "{{ long_task.ansible_job_id }}"
    register: job_result
    until: job_result.finished
    retries: 60
    delay: 60
```

---

## Free strategy

```yaml
# Default: linear (väntar på alla hosts per task)
# Free: hosts kör så fort de kan

- name: Deploy with free strategy
  hosts: webservers
  strategy: free                       # Vänta inte på långsamma hosts

  tasks:
    - name: Install packages
      apt:
        name: nginx
        state: present
```

---

## Mitogen acceleration

```bash
# Installera Mitogen
pip install mitogen

# Aktivera i ansible.cfg
[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear
```

```ini
# ansible.cfg med Mitogen
[defaults]
strategy_plugins = ~/.local/lib/python3.11/site-packages/ansible_mitogen/plugins/strategy
strategy = mitogen_linear

# Mitogen-specifik config
[mitogen]
# Aktivera för specifika connections
host_key_checking = False
```

---

## Playbook optimization

```yaml
# Samla tasks av samma typ
tasks:
  # INEFFEKTIVT - flera apt-calls
  - apt: name=nginx state=present
  - apt: name=curl state=present
  - apt: name=vim state=present

  # EFFEKTIVT - en apt-call
  - name: Install all packages
    apt:
      name:
        - nginx
        - curl
        - vim
      state: present
      update_cache: yes
```

```yaml
# Använd handlers istället för restart i varje task
tasks:
  - name: Update config 1
    template: src=1.conf.j2 dest=/etc/app/1.conf
    notify: Restart app

  - name: Update config 2
    template: src=2.conf.j2 dest=/etc/app/2.conf
    notify: Restart app

handlers:
  - name: Restart app
    service: name=app state=restarted
    # Körs EN gång, inte två
```

---

## Serial och batch

```yaml
# Rolling deployment
- name: Rolling update
  hosts: webservers
  serial: 5                            # 5 hosts åt gången
  # eller
  serial: "20%"                        # 20% åt gången
  # eller
  serial:
    - 1                                # Först 1 (canary)
    - 5                                # Sen 5
    - "100%"                           # Sen resten

  tasks:
    - name: Deploy
      include_tasks: deploy.yml
```

---

## Profiling

```bash
# Aktivera profiling
export ANSIBLE_CALLBACK_WHITELIST=profile_tasks

# Eller i ansible.cfg
[defaults]
callback_whitelist = profile_tasks, timer

# Kör och se timing
ansible-playbook site.yml

# Output visar tid per task:
# PLAY RECAP
# Tuesday 05 December 2024  15:30:00 +0000 (0:00:02.123)
# ===============================================
# apt ------------------------------------------ 45.23s
# template ------------------------------------- 12.45s
# service -------------------------------------- 3.21s
```

---

## Key Takeaways

1. `forks` ökar parallellism
2. `pipelining = True` minskar SSH overhead
3. Fact caching undviker upprepade insamlingar
4. `async` för långvariga tasks
5. Mitogen kan ge 2-7x snabbare körning
''',
        },
        {
            "title": "Testing with Molecule",
            "slug": "testing-molecule",
            "difficulty": "advanced",
            "content": '''
# Testing with Molecule

## Varför behöver du kunna detta?

Ansible-kod behöver testas:

- Fånga buggar innan produktion
- Säkerställ idempotens
- Testa på flera OS
- Automatisera i CI/CD

Molecule är standard för Ansible testing.

---

## Så fungerar det

Molecule workflow:

1. Skapa test-container/VM
2. Kör playbook (converge)
3. Testa idempotens
4. Verifiera resultat
5. Städa upp

---

## Installation

```bash
# Installera Molecule
pip install molecule

# Med Docker driver (vanligast)
pip install molecule molecule-docker

# Med andra drivers
pip install molecule-vagrant
pip install molecule-ec2
pip install molecule-podman

# Verifiera
molecule --version
```

---

## Initiera Molecule

```bash
# I befintlig role
cd roles/webserver
molecule init scenario -d docker

# Skapar struktur:
roles/webserver/
├── molecule/
│   └── default/
│       ├── converge.yml
│       ├── molecule.yml
│       └── verify.yml
```

---

## Molecule configuration

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
    image: geerlingguy/docker-ubuntu2204-ansible
    pre_build_image: true
    privileged: true
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:rw
    cgroupns_mode: host
    command: /lib/systemd/systemd

  - name: debian-12
    image: geerlingguy/docker-debian12-ansible
    pre_build_image: true
    privileged: true
    command: /lib/systemd/systemd

  - name: rockylinux-9
    image: geerlingguy/docker-rockylinux9-ansible
    pre_build_image: true
    privileged: true
    command: /lib/systemd/systemd

provisioner:
  name: ansible
  inventory:
    host_vars:
      ubuntu-22:
        ansible_python_interpreter: /usr/bin/python3
  playbooks:
    converge: converge.yml
    verify: verify.yml
  config_options:
    defaults:
      callbacks_enabled: profile_tasks

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
    - verify
    - cleanup
    - destroy
```

---

## Converge playbook

```yaml
# molecule/default/converge.yml
---
- name: Converge
  hosts: all
  become: yes

  vars:
    nginx_port: 8080
    nginx_sites:
      - name: test
        server_name: test.local
        root: /var/www/test

  pre_tasks:
    - name: Update apt cache (Debian)
      apt:
        update_cache: yes
      when: ansible_os_family == "Debian"

  roles:
    - role: webserver
```

---

## Verify playbook

```yaml
# molecule/default/verify.yml
---
- name: Verify
  hosts: all
  gather_facts: yes

  tasks:
    - name: Gather service facts
      service_facts:

    - name: Assert nginx is running
      assert:
        that:
          - ansible_facts.services['nginx.service'].state == 'running'
        fail_msg: "nginx is not running"
        success_msg: "nginx is running"

    - name: Check nginx responds on port 8080
      uri:
        url: http://localhost:8080
        status_code: 200
      register: nginx_response

    - name: Assert nginx response
      assert:
        that:
          - nginx_response.status == 200

    - name: Check config file exists
      stat:
        path: /etc/nginx/sites-enabled/test.conf
      register: config_file

    - name: Assert config exists
      assert:
        that:
          - config_file.stat.exists
          - config_file.stat.isreg

    - name: Verify nginx config syntax
      command: nginx -t
      changed_when: false
```

---

## Molecule commands

```bash
# Fullständigt test (alla steg)
molecule test

# Skapa containers
molecule create

# Kör converge
molecule converge

# Testa idempotens
molecule idempotence

# Kör verify
molecule verify

# Logga in på container
molecule login
molecule login -h ubuntu-22           # Specifik host

# Städa upp
molecule destroy

# Lista status
molecule list

# Debug
molecule --debug test
```

---

## Prepare playbook

```yaml
# molecule/default/prepare.yml
# Körs före converge för test-setup
---
- name: Prepare
  hosts: all
  become: yes

  tasks:
    - name: Install test dependencies
      apt:
        name:
          - curl
          - netcat-openbsd
        state: present
      when: ansible_os_family == "Debian"

    - name: Create test user
      user:
        name: testuser
        state: present
```

---

## Multiple scenarios

```bash
# Skapa flera scenarios
molecule init scenario --scenario-name ubuntu-only -d docker
molecule init scenario --scenario-name integration -d vagrant

# Struktur:
molecule/
├── default/
│   ├── molecule.yml
│   ├── converge.yml
│   └── verify.yml
├── ubuntu-only/
│   ├── molecule.yml
│   ├── converge.yml
│   └── verify.yml
└── integration/
    ├── molecule.yml
    └── converge.yml
```

```bash
# Kör specifik scenario
molecule test -s ubuntu-only
molecule converge -s integration
```

---

## CI/CD integration

```yaml
# .github/workflows/molecule.yml
name: Molecule Test

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  molecule:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        distro:
          - ubuntu2204
          - debian12
          - rockylinux9

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install molecule molecule-docker ansible ansible-lint

      - name: Run Molecule tests
        run: molecule test
        env:
          MOLECULE_DISTRO: ${{ matrix.distro }}
```

---

## Key Takeaways

1. Molecule testar roles i isolerade containers
2. `converge.yml` kör rolen
3. `verify.yml` validerar resultat
4. `idempotence` säkerställer repeat-safety
5. Multiple scenarios för olika test-cases
''',
        },
        {
            "title": "Callback Plugins",
            "slug": "callback-plugins",
            "difficulty": "advanced",
            "content": '''
# Callback Plugins

## Varför behöver du kunna detta?

Callback plugins utökar Ansibles output:

- Anpassad logging
- Integration med externa system
- Performance profiling
- Custom notifications

Utöka Ansible efter dina behov.

---

## Så fungerar det

Callbacks triggas vid events:

1. Playbook start/end
2. Play start/end
3. Task start/end
4. Host success/failure
5. Stats

---

## Inbyggda callbacks

```ini
# ansible.cfg
[defaults]
# Aktivera flera callbacks
callbacks_enabled = profile_tasks, timer, json

# Stdout callback (en i taget)
stdout_callback = yaml
# Alternativ: default, minimal, dense, json, yaml
```

```bash
# Lista tillgängliga callbacks
ansible-doc -t callback -l

# Visa dokumentation
ansible-doc -t callback profile_tasks
ansible-doc -t callback json
```

---

## Profile callbacks

```ini
# ansible.cfg - Performance profiling
[defaults]
callbacks_enabled = profile_tasks, profile_roles, timer

# profile_tasks: Tid per task
# profile_roles: Tid per role
# timer: Total tid
```

```bash
# Output med profile_tasks:
# TASK [Install nginx] **************************
# ok: [web1] => (item=nginx)
# ok: [web1] => (item=curl)
#
# Tuesday 05 December 2024  10:30:00 +0000 (0:00:45.123)
# ===============================================
# Install nginx -------------------------------- 45.12s
# Start service -------------------------------- 2.34s
# -----------------------------------------------
# Total ---------------------------------------- 47.46s
```

---

## JSON callback

```bash
# JSON output för parsing
ANSIBLE_STDOUT_CALLBACK=json ansible-playbook site.yml

# Eller
ansible-playbook site.yml --stdout-callback json > output.json
```

```json
{
    "plays": [{
        "play": {
            "name": "Configure servers"
        },
        "tasks": [{
            "task": {
                "name": "Install nginx"
            },
            "hosts": {
                "web1": {
                    "changed": true,
                    "msg": "Package installed"
                }
            }
        }]
    }],
    "stats": {
        "web1": {
            "changed": 5,
            "failures": 0,
            "ok": 10
        }
    }
}
```

---

## Custom callback plugin

```python
# callback_plugins/notify_slack.py

from ansible.plugins.callback import CallbackBase
import requests
import json

DOCUMENTATION = """
callback: notify_slack
type: notification
short_description: Send notifications to Slack
description:
    - This callback sends play results to Slack
requirements:
    - requests
options:
    webhook_url:
        description: Slack webhook URL
        env:
            - name: SLACK_WEBHOOK_URL
        ini:
            - section: callback_notify_slack
              key: webhook_url
"""

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'notify_slack'
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self):
        super().__init__()
        self.webhook_url = None
        self.playbook_name = None
        self.results = []

    def set_options(self, task_keys=None, var_options=None, direct=None):
        super().set_options(task_keys=task_keys, var_options=var_options, direct=direct)
        self.webhook_url = self.get_option('webhook_url')

    def v2_playbook_on_start(self, playbook):
        self.playbook_name = playbook._file_name

    def v2_playbook_on_stats(self, stats):
        hosts = sorted(stats.processed.keys())

        summary = {
            'ok': 0,
            'changed': 0,
            'failures': 0,
            'unreachable': 0
        }

        for host in hosts:
            s = stats.summarize(host)
            summary['ok'] += s['ok']
            summary['changed'] += s['changed']
            summary['failures'] += s['failures']
            summary['unreachable'] += s['unreachable']

        # Skicka till Slack
        color = 'good' if summary['failures'] == 0 else 'danger'

        payload = {
            'attachments': [{
                'color': color,
                'title': f'Ansible: {self.playbook_name}',
                'fields': [
                    {'title': 'OK', 'value': summary['ok'], 'short': True},
                    {'title': 'Changed', 'value': summary['changed'], 'short': True},
                    {'title': 'Failures', 'value': summary['failures'], 'short': True},
                    {'title': 'Unreachable', 'value': summary['unreachable'], 'short': True}
                ]
            }]
        }

        if self.webhook_url:
            requests.post(self.webhook_url, json=payload)
```

---

## Aktivera custom callback

```ini
# ansible.cfg
[defaults]
callback_plugins = ./callback_plugins
callbacks_enabled = notify_slack

[callback_notify_slack]
webhook_url = https://hooks.slack.com/services/XXX/YYY/ZZZ
```

```bash
# Eller med environment variable
export SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXX/YYY/ZZZ
ansible-playbook site.yml
```

---

## Callback events

```python
# Tillgängliga callback-metoder
class CallbackModule(CallbackBase):

    # Playbook events
    def v2_playbook_on_start(self, playbook):
        pass

    def v2_playbook_on_play_start(self, play):
        pass

    def v2_playbook_on_stats(self, stats):
        pass

    # Task events
    def v2_playbook_on_task_start(self, task, is_conditional):
        pass

    def v2_runner_on_ok(self, result):
        pass

    def v2_runner_on_failed(self, result, ignore_errors=False):
        pass

    def v2_runner_on_skipped(self, result):
        pass

    def v2_runner_on_unreachable(self, result):
        pass

    # Handler events
    def v2_playbook_on_handler_task_start(self, task):
        pass
```

---

## Log callback

```python
# callback_plugins/log_plays.py
import os
import datetime
from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'log_plays'
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self):
        super().__init__()
        self.log_file = os.getenv('ANSIBLE_LOG_FILE', '/var/log/ansible/plays.log')

    def log(self, message):
        timestamp = datetime.datetime.now().isoformat()
        with open(self.log_file, 'a') as f:
            f.write(f"{timestamp} - {message}\n")

    def v2_playbook_on_start(self, playbook):
        self.log(f"PLAYBOOK START: {playbook._file_name}")

    def v2_runner_on_ok(self, result):
        self.log(f"OK: {result._host.name} - {result._task.name}")

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.log(f"FAILED: {result._host.name} - {result._task.name}")
```

---

## Key Takeaways

1. Callbacks utökar Ansibles output
2. `profile_tasks` för performance debugging
3. Custom callbacks för integration
4. Flera callbacks kan vara aktiva samtidigt
5. `stdout_callback` för output-format
''',
        },
        {
            "title": "Ansible for Windows",
            "slug": "ansible-windows",
            "difficulty": "advanced",
            "content": '''
# Ansible for Windows

## Varför behöver du kunna detta?

Windows är vanligt i enterprise:

- Active Directory
- IIS och .NET
- SQL Server
- Hybrid-miljöer

Ansible kan hantera Windows lika bra som Linux.

---

## Så fungerar det

Windows-hantering via:

1. WinRM (Windows Remote Management)
2. PowerShell modules
3. Dedicated Windows modules
4. Credentials och Kerberos

---

## WinRM setup

```powershell
# På Windows-servern (kör som admin)
# Aktivera WinRM
winrm quickconfig -q

# Konfigurera för Ansible
winrm set winrm/config/service/auth '@{Basic="true"}'
winrm set winrm/config/service '@{AllowUnencrypted="true"}'

# För HTTPS (rekommenderat)
$cert = New-SelfSignedCertificate -DnsName $(hostname) -CertStoreLocation Cert:\LocalMachine\My
winrm create winrm/config/Listener?Address=*+Transport=HTTPS "@{Hostname=`"$(hostname)`"; CertificateThumbprint=`"$($cert.Thumbprint)`"}"

# Öppna brandvägg
netsh advfirewall firewall add rule name="WinRM HTTPS" dir=in localport=5986 protocol=TCP action=allow

# Verifiera
winrm enumerate winrm/config/listener
```

---

## Inventory för Windows

```yaml
# inventory/windows.yml
---
all:
  children:
    windows:
      hosts:
        win-server1:
          ansible_host: 192.168.1.100
        win-server2:
          ansible_host: 192.168.1.101
      vars:
        ansible_user: Administrator
        ansible_password: "{{ vault_win_password }}"
        ansible_connection: winrm
        ansible_winrm_transport: ntlm
        ansible_winrm_server_cert_validation: ignore
        ansible_port: 5986
```

```ini
# Alternativ inventory (INI)
[windows]
win-server1 ansible_host=192.168.1.100
win-server2 ansible_host=192.168.1.101

[windows:vars]
ansible_user=Administrator
ansible_connection=winrm
ansible_winrm_transport=ntlm
ansible_port=5986
```

---

## Python dependencies

```bash
# Installera pywinrm
pip install pywinrm
pip install pywinrm[credssp]          # För CredSSP auth
pip install pywinrm[kerberos]         # För Kerberos auth

# Kerberos kräver också
# Ubuntu/Debian:
sudo apt install krb5-user python3-kerberos
# macOS:
brew install krb5
```

---

## Windows modules

```yaml
# windows_setup.yml
---
- name: Configure Windows Servers
  hosts: windows
  gather_facts: yes

  tasks:
    # Installera features
    - name: Install IIS
      win_feature:
        name: Web-Server
        include_sub_features: yes
        include_management_tools: yes
        state: present

    # Hantera Windows-tjänster
    - name: Ensure IIS is running
      win_service:
        name: W3SVC
        state: started
        start_mode: auto

    # Installera programvara via Chocolatey
    - name: Install Chocolatey
      win_chocolatey:
        name: chocolatey
        state: present

    - name: Install software
      win_chocolatey:
        name:
          - git
          - notepadplusplus
          - 7zip
        state: present

    # Kopiera filer
    - name: Copy configuration file
      win_copy:
        src: files/web.config
        dest: C:\inetpub\wwwroot\web.config

    # Hantera registry
    - name: Set registry value
      win_regedit:
        path: HKLM:\SOFTWARE\MyApp
        name: InstallPath
        data: C:\Program Files\MyApp
        type: string

    # Kör PowerShell
    - name: Run PowerShell script
      win_shell: |
        Get-Service | Where-Object {$_.Status -eq "Running"}
      register: running_services

    - name: Show services
      debug:
        var: running_services.stdout_lines
```

---

## Windows updates

```yaml
tasks:
  # Hantera Windows Updates
  - name: Install all critical updates
    win_updates:
      category_names:
        - SecurityUpdates
        - CriticalUpdates
      state: installed
      reboot: yes
      reboot_timeout: 3600
    register: update_result

  - name: Reboot if required
    win_reboot:
      reboot_timeout: 600
    when: update_result.reboot_required
```

---

## AD och domän

```yaml
tasks:
  # Gå med i domän
  - name: Join domain
    win_domain_membership:
      dns_domain_name: example.com
      domain_admin_user: admin@example.com
      domain_admin_password: "{{ domain_password }}"
      state: domain
    register: domain_join

  - name: Reboot after domain join
    win_reboot:
    when: domain_join.reboot_required

  # Skapa AD-användare
  - name: Create AD user
    win_domain_user:
      name: johndoe
      password: "{{ user_password }}"
      state: present
      path: OU=Users,DC=example,DC=com
      groups:
        - Domain Users
        - Developers

  # Skapa AD-grupp
  - name: Create AD group
    win_domain_group:
      name: Developers
      scope: global
      path: OU=Groups,DC=example,DC=com
      state: present
```

---

## IIS management

```yaml
tasks:
  # Skapa application pool
  - name: Create app pool
    win_iis_webapppool:
      name: MyAppPool
      state: started
      attributes:
        managedRuntimeVersion: v4.0
        managedPipelineMode: Integrated

  # Skapa webbsite
  - name: Create website
    win_iis_website:
      name: MyWebsite
      state: started
      port: 80
      ip: '*'
      hostname: www.example.com
      application_pool: MyAppPool
      physical_path: C:\inetpub\wwwroot\mysite

  # Skapa virtual directory
  - name: Create virtual directory
    win_iis_virtualdirectory:
      name: api
      site: MyWebsite
      physical_path: C:\inetpub\wwwroot\api
```

---

## DSC integration

```yaml
tasks:
  # Kör DSC configuration
  - name: Apply DSC configuration
    win_dsc:
      resource_name: WindowsFeature
      Name: Web-Server
      Ensure: Present

  # Custom DSC resource
  - name: Configure with DSC
    win_dsc:
      resource_name: File
      DestinationPath: C:\Temp\test.txt
      Contents: "Hello from DSC"
      Ensure: Present
```

---

## Key Takeaways

1. WinRM måste konfigureras på Windows-servrar
2. `pywinrm` Python-paket krävs
3. Windows-specifika modules (`win_*`)
4. Chocolatey för pakethantering
5. DSC-integration för komplexa konfigurationer
''',
        },
        {
            "title": "Ansible AWX",
            "slug": "ansible-awx",
            "difficulty": "advanced",
            "content": '''
# Ansible AWX

## Varför behöver du kunna detta?

AWX är Ansibles web UI och API:

- Visuell job scheduling
- Role-based access control
- Audit logging
- REST API
- Inventory sync

Enterprise-ready automation platform.

---

## Så fungerar det

AWX components:

1. Web UI för management
2. REST API för integration
3. Job templates och workflows
4. Inventory sources
5. Credential management

---

## Installation med Docker

```bash
# Klona AWX operator
git clone https://github.com/ansible/awx-operator.git
cd awx-operator

# Installera med Kubernetes (minikube)
minikube start --cpus=4 --memory=8g
make deploy

# Skapa AWX instance
cat <<EOF | kubectl apply -f -
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx
spec:
  service_type: nodeport
  postgres_storage_requirements:
    requests:
      storage: 8Gi
EOF

# Hämta admin password
kubectl get secret awx-admin-password -o jsonpath="{.data.password}" | base64 --decode
```

---

## Docker Compose setup

```yaml
# docker-compose.yml
version: '3'
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: awx
      POSTGRES_PASSWORD: awxpass
      POSTGRES_DB: awx
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7

  awx-web:
    image: quay.io/ansible/awx:latest
    depends_on:
      - postgres
      - redis
    ports:
      - "8080:8052"
    environment:
      DATABASE_USER: awx
      DATABASE_PASSWORD: awxpass
      DATABASE_NAME: awx
      DATABASE_HOST: postgres

  awx-task:
    image: quay.io/ansible/awx:latest
    depends_on:
      - awx-web
    command: launch_awx_task.sh

volumes:
  postgres_data:
```

---

## Job Templates

```yaml
# Via AWX Collection
- name: Create job template
  awx.awx.job_template:
    name: "Deploy Web Application"
    organization: "Default"
    project: "Infrastructure"
    playbook: "site.yml"
    inventory: "Production"
    credentials:
      - "SSH Key"
      - "Vault Password"
    extra_vars:
      environment: production
    job_type: run
    ask_variables_on_launch: yes
    survey_enabled: yes
    survey_spec:
      name: "Deployment Survey"
      description: "Variables for deployment"
      spec:
        - question_name: "Version"
          variable: "app_version"
          type: "text"
          required: true
          default: "latest"
```

---

## Workflows

```yaml
# Skapa workflow template
- name: Create workflow
  awx.awx.workflow_job_template:
    name: "Full Deployment"
    organization: "Default"
    survey_enabled: no

- name: Add workflow nodes
  awx.awx.workflow_job_template_node:
    workflow_job_template: "Full Deployment"
    identifier: "deploy-staging"
    unified_job_template: "Deploy Web Application"
    extra_data:
      environment: staging

- name: Add success node
  awx.awx.workflow_job_template_node:
    workflow_job_template: "Full Deployment"
    identifier: "deploy-production"
    unified_job_template: "Deploy Web Application"
    extra_data:
      environment: production

- name: Link nodes
  awx.awx.workflow_job_template_node:
    workflow_job_template: "Full Deployment"
    identifier: "deploy-production"
    success_nodes:
      - "deploy-staging"
```

---

## REST API

```bash
# Autentisering
export AWX_HOST=https://awx.example.com
export AWX_TOKEN=your-api-token

# Lista job templates
curl -H "Authorization: Bearer $AWX_TOKEN" \
  "$AWX_HOST/api/v2/job_templates/"

# Starta job
curl -X POST \
  -H "Authorization: Bearer $AWX_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"extra_vars": {"version": "1.2.3"}}' \
  "$AWX_HOST/api/v2/job_templates/5/launch/"

# Hämta job status
curl -H "Authorization: Bearer $AWX_TOKEN" \
  "$AWX_HOST/api/v2/jobs/123/"
```

```python
# Python client
import requests

class AWXClient:
    def __init__(self, host, token):
        self.host = host
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

    def launch_job(self, template_id, extra_vars=None):
        url = f'{self.host}/api/v2/job_templates/{template_id}/launch/'
        data = {'extra_vars': extra_vars or {}}
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

    def get_job_status(self, job_id):
        url = f'{self.host}/api/v2/jobs/{job_id}/'
        response = requests.get(url, headers=self.headers)
        return response.json()

# Användning
client = AWXClient('https://awx.example.com', 'token')
job = client.launch_job(5, {'version': '1.2.3'})
print(f"Job ID: {job['id']}")
```

---

## Inventory sources

```yaml
# Sync från AWS
- name: Create AWS inventory source
  awx.awx.inventory_source:
    name: "AWS EC2"
    inventory: "Production"
    source: ec2
    credential: "AWS Credentials"
    source_vars:
      regions:
        - eu-north-1
      filters:
        tag:Environment: production
    update_on_launch: yes
    overwrite: yes

# Sync från Git
- name: Create SCM inventory source
  awx.awx.inventory_source:
    name: "Git Inventory"
    inventory: "Production"
    source: scm
    source_project: "Infrastructure"
    source_path: "inventory/production/"
```

---

## Credentials

```yaml
# Skapa credentials
- name: Create SSH credential
  awx.awx.credential:
    name: "Production SSH Key"
    organization: "Default"
    credential_type: "Machine"
    inputs:
      username: deploy
      ssh_key_data: "{{ lookup('file', '~/.ssh/deploy_key') }}"
      become_method: sudo

- name: Create Vault credential
  awx.awx.credential:
    name: "Ansible Vault"
    organization: "Default"
    credential_type: "Vault"
    inputs:
      vault_password: "{{ vault_password }}"

- name: Create AWS credential
  awx.awx.credential:
    name: "AWS Credentials"
    organization: "Default"
    credential_type: "Amazon Web Services"
    inputs:
      username: "{{ aws_access_key }}"
      password: "{{ aws_secret_key }}"
```

---

## Schedules

```yaml
# Scheduled jobs
- name: Create schedule
  awx.awx.schedule:
    name: "Nightly Backup"
    unified_job_template: "Backup Job Template"
    rrule: "DTSTART:20240101T000000Z RRULE:FREQ=DAILY;INTERVAL=1"
    enabled: yes
```

---

## Key Takeaways

1. AWX ger web UI och API för Ansible
2. Job templates och workflows för orchestration
3. REST API för CI/CD integration
4. Inventory sources synkar dynamiskt
5. Centraliserad credential management
''',
        },
        {
            "title": "Security Best Practices",
            "slug": "security-best-practices",
            "difficulty": "advanced",
            "content": '''
# Security Best Practices

## Varför behöver du kunna detta?

Ansible har stor makt - och ansvar:

- Tillgång till alla servrar
- Hanterar känsliga credentials
- Kan ändra säkerhetskonfigurationer
- Audit-krav i enterprise

Säkerhet måste byggas in från början.

---

## Så fungerar det

Säkerhetsområden:

1. Credential management
2. SSH härdning
3. Playbook security
4. Audit och logging
5. Network security

---

## Vault best practices

```bash
# Använd separata vault-lösenord per miljö
ansible-vault create --vault-id prod@prompt secrets_prod.yml
ansible-vault create --vault-id dev@prompt secrets_dev.yml

# Separera vault-variabler
group_vars/
├── production/
│   ├── vars.yml              # Inga secrets
│   └── vault.yml             # Alla secrets
```

```yaml
# Namnkonvention för vault-variabler
# group_vars/production/vault.yml
---
vault_db_password: supersecret
vault_api_key: abc123xyz

# group_vars/production/vars.yml - referera med tydliga namn
db_password: "{{ vault_db_password }}"
```

---

## SSH härdning

```yaml
# Skapa dedikerad deploy-användare
- name: Create deploy user
  user:
    name: deploy
    groups: sudo
    shell: /bin/bash
    create_home: yes

- name: Set up authorized key
  authorized_key:
    user: deploy
    key: "{{ lookup('file', 'files/deploy_key.pub') }}"
    exclusive: yes                     # Ta bort andra nycklar

- name: Disable password authentication
  lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^#?PasswordAuthentication'
    line: 'PasswordAuthentication no'
  notify: Restart sshd

- name: Disable root login
  lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^#?PermitRootLogin'
    line: 'PermitRootLogin no'
  notify: Restart sshd
```

---

## Become security

```yaml
# Begränsa sudo-rättigheter
- name: Configure sudo for deploy user
  copy:
    dest: /etc/sudoers.d/deploy
    content: |
      # Deploy user kan bara köra specifika kommandon
      deploy ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart myapp
      deploy ALL=(ALL) NOPASSWD: /usr/bin/apt-get update
      deploy ALL=(ALL) NOPASSWD: /usr/bin/apt-get install *
    mode: '0440'
    validate: visudo -cf %s
```

```ini
# ansible.cfg - Kräv become password
[privilege_escalation]
become_ask_pass = True
```

---

## No_log för känslig data

```yaml
tasks:
  # Dölj känslig output
  - name: Set database password
    mysql_user:
      name: app
      password: "{{ db_password }}"
    no_log: true                       # Dölj i logs

  - name: Debug sensitive data
    debug:
      var: api_response
    no_log: "{{ hide_sensitive | default(true) }}"

  # Dölj i hela blocken
  - name: Handle secrets
    block:
      - name: Fetch API token
        uri:
          url: https://api.example.com/token
          body:
            username: "{{ api_user }}"
            password: "{{ api_pass }}"
        register: token_response
    no_log: true
```

---

## Begränsa module-användning

```ini
# ansible.cfg
[inventory]
# Inaktivera osäkra inventory-plugins
enable_plugins = yaml, ini, host_list

[defaults]
# Begränsa modul-sökvägar
library = ./library:/usr/share/ansible/plugins/modules

# Blockera shell/command för audit
# (implementera via callback eller policy)
```

```yaml
# Använd specifika modules istället för shell/command
tasks:
  # DÅLIGT - ospecifikt
  - name: Install package
    shell: apt-get install -y nginx

  # BRA - idempotent och loggbart
  - name: Install package
    apt:
      name: nginx
      state: present
```

---

## Audit logging

```python
# callback_plugins/audit_log.py
import json
import datetime
from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'audit_log'
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self):
        super().__init__()
        self.audit_log = '/var/log/ansible/audit.json'

    def log_event(self, event_type, data):
        event = {
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'type': event_type,
            'data': data
        }
        with open(self.audit_log, 'a') as f:
            f.write(json.dumps(event) + '\n')

    def v2_playbook_on_start(self, playbook):
        self.log_event('playbook_start', {
            'playbook': playbook._file_name,
            'user': os.getenv('USER')
        })

    def v2_runner_on_ok(self, result):
        self.log_event('task_ok', {
            'host': result._host.name,
            'task': result._task.name,
            'changed': result._result.get('changed', False)
        })

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.log_event('task_failed', {
            'host': result._host.name,
            'task': result._task.name,
            'error': str(result._result.get('msg', ''))
        })
```

---

## Network security

```ini
# ansible.cfg
[ssh_connection]
# Kräv host key verification
host_key_checking = True

# Använd stark kryptering
ssh_args = -o KexAlgorithms=curve25519-sha256 -o Ciphers=chacha20-poly1305@openssh.com
```

```yaml
# Använd bastion/jump host
# inventory/hosts.yml
all:
  vars:
    ansible_ssh_common_args: '-o ProxyJump=bastion.example.com'

  children:
    internal:
      hosts:
        internal-server:
          ansible_host: 10.0.1.100
```

---

## Secret scanning

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  secrets-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Detect secrets
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./

      - name: Check for unencrypted vaults
        run: |
          # Hitta YAML-filer med misstänkta secrets
          grep -r "password:" --include="*.yml" --include="*.yaml" | \
            grep -v "vault.yml" | \
            grep -v "!vault" && exit 1 || exit 0
```

---

## Key Takeaways

1. Vault med separata lösenord per miljö
2. `no_log: true` för känslig data
3. Dedikerade deploy-användare med begränsad sudo
4. Audit logging med custom callback
5. Secret scanning i CI/CD
''',
        },
        {
            "title": "Enterprise Patterns",
            "slug": "enterprise-patterns",
            "difficulty": "advanced",
            "content": '''
# Enterprise Patterns

## Varför behöver du kunna detta?

Enterprise-skala kräver:

- Skalbarhet över tusentals servrar
- Multi-team samarbete
- Compliance och governance
- Self-service automation

Patterns som fungerar i stor skala.

---

## Så fungerar det

Enterprise patterns:

1. Repository struktur
2. Role-based access
3. Self-service portaler
4. Compliance automation
5. Multi-tenant arkitektur

---

## Monorepo struktur

```bash
# Enterprise repository layout
ansible-infrastructure/
├── ansible.cfg
├── requirements.yml               # Galaxy dependencies
├── inventory/
│   ├── production/
│   │   ├── hosts.yml
│   │   ├── group_vars/
│   │   │   ├── all/
│   │   │   │   ├── vars.yml
│   │   │   │   └── vault.yml
│   │   │   └── webservers/
│   │   └── host_vars/
│   └── staging/
├── playbooks/
│   ├── site.yml                   # Main entry point
│   ├── webservers.yml
│   ├── databases.yml
│   └── maintenance/
│       ├── patching.yml
│       └── backup.yml
├── roles/
│   ├── common/
│   ├── webserver/
│   ├── database/
│   └── security/
├── collections/
│   └── requirements.yml
├── plugins/
│   ├── callback/
│   ├── filter/
│   └── lookup/
├── files/
├── templates/
└── tests/
    └── molecule/
```

---

## Multi-team workflow

```yaml
# CODEOWNERS - GitHub/GitLab
# Kräv review från rätt team

# Infrastructure team äger roles
/roles/ @infrastructure-team

# Security team måste granska säkerhetsändringar
/roles/security/ @security-team
/playbooks/*security* @security-team

# Miljö-specifikt
/inventory/production/ @sre-team
/inventory/staging/ @dev-team
```

```yaml
# .github/workflows/ansible-pr.yml
name: Ansible PR Checks

on:
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Lint
        run: ansible-lint

  security-review:
    runs-on: ubuntu-latest
    if: contains(github.event.pull_request.labels.*.name, 'security')
    steps:
      - name: Require security team approval
        uses: actions/github-script@v7
        with:
          script: |
            const reviews = await github.rest.pulls.listReviews({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.payload.pull_request.number
            });
            const securityApproved = reviews.data.some(
              r => r.state === 'APPROVED' &&
              securityTeamMembers.includes(r.user.login)
            );
            if (!securityApproved) {
              core.setFailed('Security team approval required');
            }
```

---

## Self-service med AWX

```yaml
# Survey-driven deployment
- name: Create self-service job template
  awx.awx.job_template:
    name: "Deploy Application"
    organization: "Default"
    project: "Infrastructure"
    playbook: "deploy.yml"
    inventory: "All Environments"
    survey_enabled: yes
    survey_spec:
      name: "Deployment Options"
      spec:
        - question_name: "Environment"
          variable: "target_environment"
          type: "multiplechoice"
          choices:
            - "staging"
            - "production"
          required: true

        - question_name: "Application Version"
          variable: "app_version"
          type: "text"
          required: true
          default: "latest"

        - question_name: "Rolling Update Batch Size"
          variable: "serial_count"
          type: "integer"
          min: 1
          max: 10
          default: 2

# RBAC - Developers kan deploy till staging
- name: Grant staging access
  awx.awx.role:
    user: developer-team
    role: execute
    job_templates:
      - "Deploy Application"
    workflows:
      - "Staging Pipeline"
```

---

## Compliance automation

```yaml
# CIS Benchmark compliance check
---
- name: CIS Compliance Audit
  hosts: all
  become: yes
  gather_facts: yes

  tasks:
    - name: Check SSH config compliance
      assert:
        that:
          - "'PermitRootLogin no' in ssh_config.stdout"
          - "'PasswordAuthentication no' in ssh_config.stdout"
        fail_msg: "SSH configuration non-compliant"
      vars:
        ssh_config: "{{ lookup('file', '/etc/ssh/sshd_config') }}"
      register: ssh_compliance
      ignore_errors: yes

    - name: Check filesystem permissions
      stat:
        path: "{{ item }}"
      register: file_perms
      loop:
        - /etc/passwd
        - /etc/shadow
        - /etc/group

    - name: Assert secure permissions
      assert:
        that:
          - item.stat.mode == '0644' or item.stat.mode == '0640' or item.stat.mode == '0600'
        fail_msg: "{{ item.item }} has insecure permissions: {{ item.stat.mode }}"
      loop: "{{ file_perms.results }}"
      ignore_errors: yes

    - name: Generate compliance report
      template:
        src: compliance_report.j2
        dest: "/var/log/compliance/{{ inventory_hostname }}_{{ ansible_date_time.date }}.json"
      delegate_to: localhost
```

---

## Canary deployments

```yaml
# canary_deploy.yml
---
- name: Canary Deployment
  hosts: webservers
  serial:
    - 1                                # Första: 1 server (canary)
    - "25%"                            # Sedan: 25%
    - "100%"                           # Slutligen: resten
  max_fail_percentage: 0               # Nolltolerans för fel

  pre_tasks:
    - name: Verify health before deployment
      uri:
        url: "http://{{ inventory_hostname }}/health"
        status_code: 200
      delegate_to: localhost

  roles:
    - deploy

  post_tasks:
    - name: Wait for service to stabilize
      wait_for:
        host: "{{ inventory_hostname }}"
        port: 8080
        state: started
        delay: 10
        timeout: 60

    - name: Verify health after deployment
      uri:
        url: "http://{{ inventory_hostname }}/health"
        status_code: 200
      register: health_check
      retries: 5
      delay: 10
      until: health_check.status == 200
      delegate_to: localhost

    - name: Run smoke tests
      command: /opt/tests/smoke_test.sh
      delegate_to: localhost

    - name: Pause for manual verification (canary)
      pause:
        prompt: "Canary deployed. Check metrics. Press enter to continue or Ctrl+C to abort."
      when: ansible_play_batch | first == inventory_hostname
```

---

## Config management database

```yaml
# Synka med CMDB efter ändringar
- name: Update CMDB
  hosts: all
  gather_facts: yes

  post_tasks:
    - name: Update CMDB entry
      uri:
        url: "https://cmdb.internal/api/servers/{{ inventory_hostname }}"
        method: PUT
        headers:
          Authorization: "Bearer {{ cmdb_token }}"
        body_format: json
        body:
          hostname: "{{ inventory_hostname }}"
          ip_address: "{{ ansible_default_ipv4.address }}"
          os: "{{ ansible_distribution }} {{ ansible_distribution_version }}"
          kernel: "{{ ansible_kernel }}"
          memory_mb: "{{ ansible_memtotal_mb }}"
          cpu_cores: "{{ ansible_processor_vcpus }}"
          last_updated: "{{ ansible_date_time.iso8601 }}"
          managed_by: ansible
      delegate_to: localhost
```

---

## GitOps med Ansible

```yaml
# ArgoCD + Ansible för GitOps
# .argocd/config.yml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: infrastructure-ansible
spec:
  project: default
  source:
    repoURL: https://github.com/company/ansible-infrastructure
    targetRevision: main
    path: .
  destination:
    server: https://kubernetes.default.svc
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

```yaml
# Kubernetes Job för Ansible
apiVersion: batch/v1
kind: Job
metadata:
  name: ansible-deploy
spec:
  template:
    spec:
      containers:
        - name: ansible
          image: willhallonline/ansible:latest
          command:
            - ansible-playbook
            - -i
            - inventory/production
            - site.yml
          volumeMounts:
            - name: ssh-key
              mountPath: /root/.ssh
              readOnly: true
      volumes:
        - name: ssh-key
          secret:
            secretName: ansible-ssh-key
      restartPolicy: OnFailure
```

---

## Key Takeaways

1. Monorepo med tydlig struktur
2. CODEOWNERS för team-ansvar
3. Self-service via AWX surveys
4. Compliance som kod
5. GitOps för deklarativ automation
''',
        },
    ],
}
