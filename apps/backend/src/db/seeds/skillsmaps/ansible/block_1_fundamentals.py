# =============================================================================
# BLOCK 1: ANSIBLE FUNDAMENTALS (Noder 1-4)
# =============================================================================

NODE_01_ANSIBLE_INTRO = {
    "node_id": 1,
    "title": "Ansible Introduktion",
    "slug": "ansible-intro",
    "estimated_minutes": 45,
    "xp_reward": 100,
    "prerequisites": [],
    "content": '''
# Ansible Introduktion

Agentless automation för configuration management.

## Varför Ansible?

| Funktion | Fördel |
|----------|--------|
| Agentless | Ingen agent på managed nodes |
| SSH-baserat | Använder befintlig SSH |
| YAML | Läsbar syntax |
| Idempotent | Säkra upprepade körningar |
| Push-based | Du styr när det körs |

## Installation

```bash
# macOS
brew install ansible

# Ubuntu/Debian
sudo apt update
sudo apt install ansible

# pip (alla plattformar)
pip install ansible

# Verifiera
ansible --version
```

## Arkitektur

```
┌─────────────────┐
│  Control Node   │  ← Ansible installerat här
│  (din laptop)   │
└────────┬────────┘
         │ SSH
    ┌────┴────┬────────┬────────┐
    ▼         ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│ web01 │ │ web02 │ │ db01  │ │ cache │
└───────┘ └───────┘ └───────┘ └───────┘
         Managed Nodes (ingen agent)
```

## Första Kommandot

```bash
# Testa anslutning
ansible all -i "192.168.1.10," -m ping

# Med inventory-fil
ansible all -i inventory.ini -m ping
```

**Nästa steg:** Node 2 - Inventory
''',
}

NODE_02_INVENTORY = {
    "node_id": 2,
    "title": "Inventory",
    "slug": "inventory",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "prerequisites": [1],
    "content": '''
# Ansible Inventory

Definiera dina managed nodes.

## INI Format

```ini
# inventory.ini
[webservers]
web01.example.com
web02.example.com ansible_host=192.168.1.11

[databases]
db01.example.com ansible_port=2222
db02.example.com

[production:children]
webservers
databases

[webservers:vars]
http_port=80
```

## YAML Format

```yaml
# inventory.yml
all:
  children:
    webservers:
      hosts:
        web01:
          ansible_host: 192.168.1.10
        web02:
          ansible_host: 192.168.1.11
      vars:
        http_port: 80
    databases:
      hosts:
        db01:
          ansible_host: 192.168.1.20
```

## Inventory Variables

```ini
[webservers]
web01 ansible_host=192.168.1.10 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/web.pem

[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

## Dynamisk Inventory

```bash
# AWS EC2
ansible-inventory -i aws_ec2.yml --list

# Script
chmod +x inventory.py
ansible all -i inventory.py -m ping
```

## Kommandon

```bash
# Lista hosts
ansible-inventory -i inventory.ini --list

# Visa grafer
ansible-inventory -i inventory.ini --graph

# Testa specifik grupp
ansible webservers -i inventory.ini -m ping
```

| Pattern | Matchar |
|---------|---------|
| all | Alla hosts |
| webservers | Grupp |
| web01 | Specifik host |
| web* | Wildcard |
| webservers:&databases | Intersection |
| webservers:!db01 | Exkludera |

**Nästa steg:** Node 3 - Ad-hoc Commands
''',
}

NODE_03_ADHOC_COMMANDS = {
    "node_id": 3,
    "title": "Ad-hoc Commands",
    "slug": "adhoc-commands",
    "estimated_minutes": 45,
    "xp_reward": 110,
    "prerequisites": [2],
    "content": '''
# Ad-hoc Commands

Snabba one-liners utan playbooks.

## Syntax

```bash
ansible <pattern> -i <inventory> -m <module> -a "<arguments>"
```

## Vanliga Modules

```bash
# Ping (connectivity test)
ansible all -m ping

# Shell command
ansible webservers -m shell -a "uptime"

# Command (säkrare, ingen shell)
ansible webservers -m command -a "df -h"

# Copy fil
ansible webservers -m copy -a "src=app.conf dest=/etc/app.conf"

# Installera paket
ansible webservers -m apt -a "name=nginx state=present" --become

# Starta service
ansible webservers -m service -a "name=nginx state=started" --become

# Skapa användare
ansible all -m user -a "name=deploy state=present" --become
```

## Privilege Escalation

```bash
# Kör som root
ansible webservers -m apt -a "name=nginx state=present" --become

# Specifik användare
ansible webservers -m command -a "whoami" --become --become-user=postgres
```

## Parallelism

```bash
# Kör på 5 hosts samtidigt (default: 5)
ansible all -m ping -f 10

# En i taget
ansible all -m command -a "reboot" -f 1 --become
```

## Output Formats

```bash
# JSON output
ansible all -m setup -o

# Verbose
ansible all -m ping -v
ansible all -m ping -vvv  # Mer debug
```

## Praktiska Exempel

```bash
# Samla fakta
ansible webservers -m setup

# Filtrera fakta
ansible webservers -m setup -a "filter=ansible_distribution*"

# Kör script
ansible webservers -m script -a "/path/to/script.sh"

# Synka directory
ansible webservers -m synchronize -a "src=/local/path dest=/remote/path"
```

| Module | Användning |
|--------|-----------|
| ping | Testa anslutning |
| command | Kör kommando (utan shell) |
| shell | Kör kommando (med shell) |
| copy | Kopiera filer |
| apt/yum | Pakethantering |
| service | Hantera tjänster |
| user | Hantera användare |
| file | Filer och directories |

**Nästa steg:** Node 4 - YAML & Playbook Basics
''',
}

NODE_04_YAML_BASICS = {
    "node_id": 4,
    "title": "YAML & Playbook Basics",
    "slug": "yaml-basics",
    "estimated_minutes": 50,
    "xp_reward": 125,
    "prerequisites": [3],
    "content": '''
# YAML & Playbook Basics

YAML-syntax och din första playbook.

## YAML Syntax

```yaml
# Sträng
name: webserver

# Nummer
port: 80

# Boolean
enabled: true

# Lista
packages:
  - nginx
  - curl
  - vim

# Dictionary
server:
  name: web01
  ip: 192.168.1.10
  port: 80

# Lista av dictionaries
users:
  - name: alice
    role: admin
  - name: bob
    role: developer
```

## Första Playbook

```yaml
# site.yml
---
- name: Configure webservers
  hosts: webservers
  become: true

  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: true

    - name: Start nginx
      service:
        name: nginx
        state: started
        enabled: true

    - name: Copy index page
      copy:
        src: files/index.html
        dest: /var/www/html/index.html
        owner: www-data
        mode: '0644'
```

## Kör Playbook

```bash
# Basic
ansible-playbook -i inventory.ini site.yml

# Dry-run (check mode)
ansible-playbook -i inventory.ini site.yml --check

# Visa diff
ansible-playbook -i inventory.ini site.yml --diff

# Verbose
ansible-playbook -i inventory.ini site.yml -v

# Limit hosts
ansible-playbook -i inventory.ini site.yml --limit web01
```

## Playbook Struktur

```yaml
---
# Play 1
- name: Configure web tier
  hosts: webservers
  become: true
  vars:
    http_port: 80
  tasks:
    - name: Task 1
      # ...

# Play 2
- name: Configure db tier
  hosts: databases
  become: true
  tasks:
    - name: Task 1
      # ...
```

## Task Keywords

```yaml
tasks:
  - name: Install package
    apt:
      name: nginx
      state: present
    become: true
    when: ansible_os_family == "Debian"
    tags:
      - packages
      - nginx
    register: install_result
    notify: Restart nginx
```

| Keyword | Betydelse |
|---------|-----------|
| name | Beskrivning |
| become | Privilege escalation |
| when | Villkor |
| tags | Taggning |
| register | Spara resultat |
| notify | Trigga handler |

**Nästa steg:** Node 5 - Tasks & Modules
''',
}

ANSIBLE_BLOCK_1 = [
    NODE_01_ANSIBLE_INTRO,
    NODE_02_INVENTORY,
    NODE_03_ADHOC_COMMANDS,
    NODE_04_YAML_BASICS,
]
