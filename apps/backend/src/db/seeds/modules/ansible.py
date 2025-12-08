"""
Ansible Mastery Module
======================

Komplett kurs i Configuration Management med Ansible.
Följer Linux-mallen: Svenska, pedagogiskt, bash-kommentarer på varje rad.

20 noder från grundläggande till avancerat.
"""

MODULE = {
    "name": "Ansible Mastery",
    "slug": "ansible-mastery",
    "description": "Automatisera konfiguration och deployment med Ansible",
    "track_slug": "infrastructure",
    "order_index": 8,
    "difficulty": "intermediate",
    "estimated_hours": 20,
    "prerequisites": ["linux-mastery"],
    "icon": "⚙️",
    "color": "#EE0000",
    "tasks": [
        {
            "title": "Introduction to Ansible",
            "slug": "introduction-to-ansible",
            "difficulty": "beginner",
            "content": '''# Introduction to Ansible

Ansible ar den ledande agentlosa automatiseringsplattformen for konfigurationshantering. Istallet for att manuellt SSH:a till servrar och kora kommandon, definierar du onskat tillstand i YAML-filer och lat Ansible gora jobbet.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Installation

| Distribution | Kommando |
|--------------|----------|
| macOS | `brew install ansible` |
| Ubuntu/Debian | `sudo apt install ansible -y` |
| RHEL/CentOS | `sudo dnf install ansible -y` |
| pip (alla) | `pip3 install ansible ansible-lint` |

```bash
# Verifiera installation
ansible --version                    # visa Ansible-version
ansible-playbook --version           # visa playbook-version
which ansible                        # visa installationssokväg
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Ansible Arkitektur

```
┌─────────────────────────────────────────────────────────────────┐
│                    ANSIBLE ARKITEKTUR                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────────┐                                             │
│   │ KONTROLLNOD  │  (Ansible installerat har)                  │
│   │  - Playbooks │                                             │
│   │  - Inventory │                                             │
│   │  - Roles     │                                             │
│   └──────┬───────┘                                             │
│          │ SSH                                                  │
│          │ (ingen agent!)                                       │
│          ▼                                                      │
│   ┌──────────────┬──────────────┬──────────────┐               │
│   │   Server 1   │   Server 2   │   Server 3   │               │
│   │  (managed)   │  (managed)   │  (managed)   │               │
│   └──────────────┴──────────────┴──────────────┘               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Ansible vs Andra Verktyg

| Egenskap | Ansible | Chef | Puppet | Salt |
|----------|---------|------|--------|------|
| Agent | Nej | Ja | Ja | Ja/Nej |
| Sprak | YAML | Ruby | DSL | YAML |
| Push/Pull | Push | Pull | Pull | Bada |
| Inlarning | Enkel | Svar | Medel | Medel |
| SSH | Ja | Nej | Nej | Valfri |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Inventory Grunderna

```ini
# inventory.ini - Lista over servrar
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Ad-hoc Kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `ansible all -m ping` | Testa anslutning till alla |
| `ansible webservers -a "uptime"` | Kor kommando pa grupp |
| `ansible all -m setup` | Samla fakta om servrar |
| `ansible all -m copy -a "src=X dest=Y"` | Kopiera fil |
| `ansible all -m apt -a "name=nginx" -b` | Installera paket |

```bash
# Praktiska exempel
ansible all -i inventory.ini -m ping           # testa SSH
ansible webservers -i inventory.ini -a "df -h" # diskutrymme
ansible all -m setup -a "filter=ansible_os*"   # OS-info
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Forsta Playbook

```yaml
# playbook.yml
---
- name: Configure web servers          # play-namn
  hosts: webservers                    # malgrupp
  become: yes                          # sudo

  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
        cache_valid_time: 3600

    - name: Install nginx
      apt:
        name: nginx
        state: present

    - name: Start nginx service
      service:
        name: nginx
        state: started
        enabled: yes
```

```bash
# Kor playbook
ansible-playbook -i inventory.ini playbook.yml

# Dry-run (check mode)
ansible-playbook -i inventory.ini playbook.yml --check

# Verbose
ansible-playbook playbook.yml -v      # mer info
ansible-playbook playbook.yml -vvv    # debug
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Agentlost | Kommunicerar via SSH, ingen agent pa servrar |
| Idempotent | Sakert att kora om, andrar bara vad som behovs |
| YAML | Playbooks skrivs i lattlast YAML-syntax |
| Inventory | Definerar servrar och grupper |
| Check mode | --check for dry-run innan skarpt |

**Kom ihag:**
- Ansible kraver endast SSH-access och Python pa malet
- Playbooks ar deklarativa - beskriv onskat tillstand
- Ad-hoc for snabba engangsjobb, playbooks for repeterbart
- Anvand -v/-vv/-vvv for felsökning
- inventory.yml ar mer flexibelt an .ini-format
''',
        },
        {
            "title": "Inventory Management",
            "slug": "inventory-management",
            "difficulty": "beginner",
            "content": '''# Inventory Management

Inventory ar Ansibles karta over din infrastruktur - vilka servrar finns, hur grupperas de, och vilka variabler galler. En valsstrukturerad inventory ar nyckeln till skalbar automation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Inventory Typer

| Typ | Format | Anvandning |
|-----|--------|------------|
| Static INI | `.ini` | Enkel, lattlast |
| Static YAML | `.yml` | Mer flexibel, hierarkisk |
| Dynamic | Python/Plugin | Cloud, auto-discovery |
| Directory | Mapp-struktur | Stora miljoer |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Inventory Struktur

```
┌─────────────────────────────────────────────────────────────────┐
│                    INVENTORY HIERARKI                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   all (implicit grupp)                                         │
│    ├── production          (children-grupp)                    │
│    │    ├── webservers                                         │
│    │    │    ├── web1.example.com                              │
│    │    │    └── web2.example.com                              │
│    │    └── dbservers                                          │
│    │         └── db1.example.com                               │
│    └── staging                                                 │
│         └── staging.example.com                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Static INI Inventory

```ini
# inventory/hosts.ini

# Enskilda servrar
server1.example.com
192.168.1.50

# Grupper
[webservers]
web1.example.com
web2.example.com
web[3:5].example.com          # web3, web4, web5

[dbservers]
db1.example.com

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## YAML Inventory (Rekommenderat)

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

    staging:
      hosts:
        staging.example.com:
          ansible_host: 10.0.0.50
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Directory Layout (Skalbar)

```
inventory/
├── production/
│   ├── hosts.yml              # servrar
│   ├── group_vars/
│   │   ├── all.yml            # alla prod-servrar
│   │   ├── webservers.yml     # webserver-specifikt
│   │   └── dbservers.yml      # db-specifikt
│   └── host_vars/
│       └── web1.example.com.yml
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dynamic Inventory (Cloud)

```yaml
# inventory/aws_ec2.yml
---
plugin: amazon.aws.aws_ec2
regions:
  - eu-north-1

filters:
  tag:Environment:
    - production
  instance-state-name: running

keyed_groups:
  - key: tags.Role
    prefix: role
  - key: placement.availability_zone
    prefix: az

compose:
  ansible_host: private_ip_address
```

```bash
# Installera och testa
ansible-galaxy collection install amazon.aws
ansible-inventory -i inventory/aws_ec2.yml --graph
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Inventory Kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `ansible-inventory --list` | Lista alla hosts som JSON |
| `ansible-inventory --graph` | Visa som trad-graf |
| `ansible-inventory --host X` | Visa variabler for host |
| `ansible all --list-hosts` | Lista hosts i grupp |

```bash
# Praktiska exempel
ansible-inventory -i inventory/ --graph
ansible-inventory -i inventory/ --host web1.example.com
ansible webservers -i inventory/ --list-hosts
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| INI vs YAML | YAML mer flexibelt, INI enklare |
| group_vars | Variabler per grupp i egen fil |
| host_vars | Variabler per host i egen fil |
| Dynamic | Plugins for AWS, Azure, GCP |
| --graph | Visualisera inventory-struktur |

**Kom ihag:**
- Anvand YAML-format for komplexa miljoer
- group_vars/all.yml for gemensamma variabler
- Dynamisk inventory for cloud-miljoer
- Kombinera flera inventory med -i flagga
- ansible-inventory --graph for att verifiera struktur
''',
        },
        {
            "title": "Playbook Fundamentals",
            "slug": "playbook-fundamentals",
            "difficulty": "beginner",
            "content": '''# Playbook Fundamentals

Playbooks ar hjartat i Ansible - YAML-filer som definierar onskat tillstand for din infrastruktur. En playbook innehaller plays, som i sin tur innehaller tasks som utfor det faktiska arbetet.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Playbook Struktur

```
┌─────────────────────────────────────────────────────────────────┐
│                      PLAYBOOK ANATOMI                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   playbook.yml                                                 │
│   ├── Play 1: "Configure webservers"                           │
│   │    ├── hosts: webservers                                   │
│   │    ├── vars: {...}                                         │
│   │    ├── tasks:                                              │
│   │    │    ├── Task 1: Install nginx                          │
│   │    │    ├── Task 2: Copy config                            │
│   │    │    └── Task 3: Start service                          │
│   │    └── handlers:                                           │
│   │         └── Restart nginx                                  │
│   │                                                             │
│   └── Play 2: "Configure dbservers"                            │
│        ├── hosts: dbservers                                    │
│        └── tasks: [...]                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Playbook

```yaml
# site.yml
---
- name: Configure web servers          # play-namn
  hosts: webservers                    # malgrupp fran inventory
  become: yes                          # kor som sudo
  gather_facts: yes                    # samla systeminfo

  vars:
    http_port: 80
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
      notify: Restart nginx            # trigga handler vid andring

  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Task Syntax

| Element | Beskrivning |
|---------|-------------|
| `name:` | Beskrivande namn (visas vid korning) |
| `module:` | Ansible-modul att anvanda |
| `when:` | Villkor for exekvering |
| `loop:` | Iterera over lista |
| `register:` | Spara output i variabel |
| `notify:` | Trigga handler vid andring |
| `ignore_errors:` | Fortsatt vid fel |
| `changed_when:` | Anpassad changed-logik |

```yaml
tasks:
  # Task med villkor
  - name: Install on Ubuntu only
    apt:
      name: nginx
      state: present
    when: ansible_distribution == "Ubuntu"

  # Task med loop
  - name: Install packages
    apt:
      name: "{{ item }}"
      state: present
    loop:
      - nginx
      - curl
      - vim

  # Task med register
  - name: Check file
    stat:
      path: /etc/myapp.conf
    register: config_file

  - name: Create if missing
    template:
      src: myapp.conf.j2
      dest: /etc/myapp.conf
    when: not config_file.stat.exists
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Handlers

```
┌─────────────────────────────────────────────────────────────────┐
│                    HANDLER FLODE                                │
│                                                                 │
│   Task: Copy config ──► notify: Restart nginx                  │
│                              │                                  │
│                              ▼                                  │
│   (Alla tasks kors forst)                                      │
│                              │                                  │
│                              ▼                                  │
│   Handler: Restart nginx ──► Kors EN gang i slutet             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

```yaml
handlers:
  - name: Restart nginx
    service:
      name: nginx
      state: restarted

  - name: Reload nginx
    service:
      name: nginx
      state: reloaded

tasks:
  - name: Update config
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify: Restart nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Play Options

| Option | Beskrivning |
|--------|-------------|
| `hosts:` | Malgrupp fran inventory |
| `become: yes` | Kor som sudo |
| `become_user:` | Vilken user att bli |
| `gather_facts:` | Samla systeminfo (default: yes) |
| `serial:` | Antal hosts at gangen |
| `max_fail_percentage:` | Avbryt om X% failar |
| `any_errors_fatal:` | Avbryt vid forsta fel |

```yaml
- name: Rolling deployment
  hosts: webservers
  become: yes
  serial: 2                    # 2 hosts at gangen
  max_fail_percentage: 25      # max 25% far faila

  pre_tasks:
    - name: Disable in LB
      # ...

  roles:
    - nginx

  tasks:
    - name: Deploy app
      # ...

  post_tasks:
    - name: Enable in LB
      # ...
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Block Error Handling

```yaml
tasks:
  - name: Handle errors
    block:
      - name: Risky operation
        command: /opt/deploy.sh

      - name: Another risky task
        service:
          name: myapp
          state: started

    rescue:
      - name: On failure
        debug:
          msg: "Deploy failed, rolling back"

      - name: Rollback
        command: /opt/rollback.sh

    always:
      - name: Cleanup
        file:
          path: /tmp/deploy_temp
          state: absent
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kora Playbooks

| Kommando | Beskrivning |
|----------|-------------|
| `ansible-playbook site.yml` | Kor playbook |
| `ansible-playbook site.yml --check` | Dry-run |
| `ansible-playbook site.yml --diff` | Visa andringar |
| `ansible-playbook site.yml -v` | Verbose |
| `ansible-playbook site.yml --limit web1` | Begransat till host |
| `ansible-playbook site.yml --tags deploy` | Endast taggade tasks |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Plays | Malgrupp + tasks tillsammans |
| Tasks | Individuella steg med modules |
| Handlers | Kors endast vid notify + i slutet |
| Blocks | Error handling med rescue/always |
| Serial | Rolling deployments |

**Kom ihag:**
- En playbook kan ha flera plays
- Handlers kors bara om task faktiskt andrar nagot
- Anvand --check for dry-run innan skarpt
- block/rescue/always for felhantering
- serial for sakra rolling deployments
''',
        },
        {
            "title": "Variables & Facts",
            "slug": "variables-facts",
            "difficulty": "beginner",
            "content": '''# Variables & Facts

Variabler gor dina playbooks dynamiska och ateranvandbara. Istallet for hardkodade varden kan samma playbook konfigurera utveckling, staging och produktion. Facts ar systeminfo som Ansible automatiskt samlar in fran varje host.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Variabel Prioritet (Lagst till Hogst)

```
┌─────────────────────────────────────────────────────────────────┐
│                 VARIABEL PRECEDENS                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   1. Role defaults         (lagst)                             │
│   2. Inventory group_vars                                      │
│   3. Inventory host_vars                                       │
│   4. Playbook vars                                             │
│   5. Role vars                                                 │
│   6. Block vars                                                │
│   7. Task vars                                                 │
│   8. Extra vars (-e)       (hogst)                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Definiera Variabler

| Plats | Fil | Scope |
|-------|-----|-------|
| Playbook | `vars:` i playbook | Per play |
| Vars file | `vars_files:` | Inkluderad fil |
| Group vars | `group_vars/gruppnamn.yml` | Per grupp |
| Host vars | `host_vars/hostname.yml` | Per host |
| Extra vars | `-e "key=value"` | Korning |

```yaml
# I playbook
- name: Configure servers
  hosts: webservers

  vars:
    http_port: 80
    app_name: myapp
    packages:
      - nginx
      - curl

  vars_files:
    - vars/common.yml
    - "vars/{{ env }}.yml"

  tasks:
    - name: Show config
      debug:
        msg: "Port: {{ http_port }}"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Extra Vars (Kommandorad)

| Kommando | Beskrivning |
|----------|-------------|
| `-e "var=value"` | Enkel variabel |
| `-e '{"key": "val"}'` | JSON |
| `-e "@vars.yml"` | Fran YAML-fil |
| `-e "@vars.json"` | Fran JSON-fil |

```bash
# Extra vars har hogst prioritet
ansible-playbook site.yml -e "env=production"
ansible-playbook site.yml -e "http_port=8080 debug=true"
ansible-playbook site.yml -e "@secrets.yml"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Ansible Facts

| Fact | Beskrivning |
|------|-------------|
| `ansible_distribution` | OS (Ubuntu, CentOS) |
| `ansible_distribution_version` | OS version |
| `ansible_os_family` | Debian, RedHat, etc |
| `ansible_default_ipv4.address` | Primar IP |
| `ansible_memtotal_mb` | Total RAM i MB |
| `ansible_processor_cores` | CPU-karnor |
| `ansible_hostname` | Hostname |

```yaml
- name: Use facts
  hosts: all
  gather_facts: yes

  tasks:
    - name: Show OS info
      debug:
        msg: "{{ ansible_distribution }} {{ ansible_distribution_version }}"

    - name: Install on Debian
      apt:
        name: nginx
      when: ansible_os_family == "Debian"

    - name: Install on RedHat
      yum:
        name: nginx
      when: ansible_os_family == "RedHat"
```

```bash
# Visa alla facts
ansible hostname -m setup

# Filtrera facts
ansible hostname -m setup -a "filter=ansible_distribution*"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Register och set_fact

```yaml
tasks:
  # Register sparar task output
  - name: Get date
    command: date +%Y-%m-%d
    register: current_date
    changed_when: false

  - name: Show result
    debug:
      msg: "Date: {{ current_date.stdout }}"

  # set_fact skapar nya variabler
  - name: Create variable
    set_fact:
      deploy_date: "{{ current_date.stdout }}"
      deploy_env: "{{ 'prod' if env == 'production' else 'dev' }}"

  - name: Use new fact
    debug:
      msg: "Deployed on {{ deploy_date }} to {{ deploy_env }}"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Jinja2 Filters

| Filter | Exempel | Resultat |
|--------|---------|----------|
| `upper` | `{{ name \\| upper }}` | NAME |
| `lower` | `{{ name \\| lower }}` | name |
| `default` | `{{ x \\| default('val') }}` | fallback |
| `first` | `{{ list \\| first }}` | forsta element |
| `join` | `{{ list \\| join(',') }}` | a,b,c |
| `to_json` | `{{ dict \\| to_json }}` | JSON-strang |
| `basename` | `{{ path \\| basename }}` | filnamn |

```yaml
tasks:
  - name: Filter examples
    debug:
      msg: |
        Default: {{ undefined_var | default('fallback') }}
        Upper: {{ name | upper }}
        Join: {{ packages | join(', ') }}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Custom Facts

```ini
# /etc/ansible/facts.d/custom.fact (pa malserver)
[general]
app_version=1.2.3
environment=production
```

```yaml
# Anvand i playbook
- name: Use custom fact
  debug:
    msg: "Version: {{ ansible_local.custom.general.app_version }}"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Precedens | Extra vars (-e) har hogst prioritet |
| Facts | Automatisk systeminfo via gather_facts |
| Register | Spara task-output i variabel |
| set_fact | Skapa nya runtime-variabler |
| Filters | Transformera varden med Jinja2 |

**Kom ihag:**
- Anvand group_vars/ for miljoseparation
- Extra vars overridar allt annat
- gather_facts: no for snabbare korning om ej behovs
- register + when for villkorlig logik
- default-filter undviker undefined errors
''',
        },
        {
            "title": "Modules & Plugins",
            "slug": "modules-plugins",
            "difficulty": "beginner",
            "content": '''# Modules & Plugins

Modules ar Ansibles byggblock - over 3000 inbyggda modules som var och en gor en specifik uppgift. Alla modules ar idempotenta vilket betyder att de ar sakra att kora flera ganger utan oonskat resultat.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Module Kategorier

| Kategori | Exempel | Anvandning |
|----------|---------|------------|
| System | user, group, service | Anvandare, tjanster |
| Files | copy, template, file | Filhantering |
| Packaging | apt, yum, pip | Paketinstallation |
| Cloud | aws_*, azure_*, gcp_* | Cloud-resurser |
| Network | ios_*, nxos_* | Natverksutrustning |
| Database | postgresql_*, mysql_* | Databashantering |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## System Modules

| Module | Beskrivning |
|--------|-------------|
| `user` | Hantera anvandare |
| `group` | Hantera grupper |
| `service` | Starta/stoppa tjanster |
| `systemd` | Systemd-specifika operationer |
| `cron` | Cron-jobb |
| `authorized_key` | SSH-nycklar |

```yaml
tasks:
  - name: Create user
    user:
      name: deploy
      state: present
      groups: sudo,www-data
      shell: /bin/bash
      create_home: yes

  - name: Manage service
    service:
      name: nginx
      state: started
      enabled: yes
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## File Modules

| Module | Beskrivning |
|--------|-------------|
| `copy` | Kopiera fil till remote |
| `template` | Rendera Jinja2 template |
| `file` | Skapa filer/kataloger/symlinks |
| `lineinfile` | Andra rad i fil |
| `blockinfile` | Lagg till block i fil |
| `fetch` | Hamta fil fran remote |

```yaml
tasks:
  - name: Copy file
    copy:
      src: files/config.txt
      dest: /etc/myapp/config.txt
      owner: root
      mode: '0644'

  - name: Create directory
    file:
      path: /var/www/myapp
      state: directory
      mode: '0755'

  - name: Deploy template
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
      validate: nginx -t -c %s
    notify: Restart nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Package Modules

| Module | Distribution |
|--------|--------------|
| `apt` | Debian/Ubuntu |
| `yum` | RHEL/CentOS 7 |
| `dnf` | RHEL/CentOS 8+ |
| `package` | Cross-platform |
| `pip` | Python packages |
| `npm` | Node.js packages |

```yaml
tasks:
  # Debian/Ubuntu
  - name: Install nginx
    apt:
      name: nginx
      state: present
      update_cache: yes

  # Cross-platform
  - name: Install git
    package:
      name: git
      state: present

  # Python
  - name: Install flask
    pip:
      name: flask
      virtualenv: /opt/venv
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Command Modules

| Module | Shell | Beskrivning |
|--------|-------|-------------|
| `command` | Nej | Sakrare, ingen shell |
| `shell` | Ja | Stoder pipes, redirects |
| `raw` | Nej | Direkt SSH, ingen Python |
| `script` | - | Kor lokalt script remote |

```yaml
tasks:
  # Command (sakrare)
  - name: Run command
    command: /opt/script.sh --arg value
    args:
      creates: /opt/done.txt

  # Shell (stoder pipes)
  - name: Run shell
    shell: cat /etc/passwd | grep deploy
    args:
      creates: /tmp/output.txt

  # Raw (ingen Python pa remote)
  - name: Bootstrap Python
    raw: apt-get install -y python3
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Lookup Plugins

| Plugin | Anvandning |
|--------|------------|
| `file` | Las filinnehall |
| `env` | Miljovariabel |
| `password` | Generera losenord |
| `pipe` | Kor kommando |
| `aws_ssm` | AWS SSM parameter |

```yaml
tasks:
  - name: Read file
    debug:
      msg: "{{ lookup('file', '/etc/hostname') }}"

  - name: Get env
    debug:
      msg: "{{ lookup('env', 'HOME') }}"

  - name: Generate password
    debug:
      msg: "{{ lookup('password', '/dev/null length=16') }}"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Module Dokumentation

| Kommando | Beskrivning |
|----------|-------------|
| `ansible-doc -l` | Lista alla modules |
| `ansible-doc apt` | Full dokumentation |
| `ansible-doc -s apt` | Kort syntax |
| `ansible-doc -t lookup -l` | Lista lookup plugins |

```bash
# Hitta modules
ansible-doc -l | grep aws
ansible-doc -l | grep file

# Visa dokumentation
ansible-doc apt
ansible-doc -s template
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Idempotent | Modules ar sakra att kora om |
| state | present/absent/latest for tillstand |
| validate | Validera config innan apply |
| creates | Skippa task om fil finns |
| ansible-doc | Inbyggd dokumentation |

**Kom ihag:**
- Anvand command over shell nar mojligt (sakrare)
- template for dynamiska config-filer
- validate-parameter for att undvika trasig config
- Lookup plugins for dynamiska varden
- ansible-doc for att lara dig nya modules
''',
        },
        {
            "title": "Templates & Jinja2",
            "slug": "templates-jinja2",
            "difficulty": "intermediate",
            "content": '''# Templates & Jinja2

Templates gor dina konfigurationsfiler dynamiska. Istallet for att ha olika config-filer for varje miljo, skapar du EN template som renderas med ratt variabler vid deployment. Jinja2 ar templating-motorn som driver detta.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Jinja2 Syntax Oversikt

| Syntax | Anvandning |
|--------|------------|
| `{{ variabel }}` | Skriv ut variabel |
| `{% if %}` | Villkor |
| `{% for %}` | Loopar |
| `{# kommentar #}` | Kommentar (renderas ej) |
| `\\| filter` | Transformera varde |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Template Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    TEMPLATE RENDERING                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   nginx.conf.j2          vars:                 nginx.conf       │
│   ┌─────────────┐       http_port: 80         ┌─────────────┐  │
│   │ listen      │  ──►  server: web1     ──►  │ listen 80;  │  │
│   │ {{ port }}; │       env: prod             │ server web1 │  │
│   └─────────────┘                             └─────────────┘  │
│                                                                 │
│       Template    +    Variabler    =    Renderad fil          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Template

```jinja2
{# templates/nginx.conf.j2 #}
# Generated by Ansible - DO NOT EDIT

user {{ nginx_user | default('www-data') }};
worker_processes {{ nginx_workers | default('auto') }};

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
# Anvand i playbook
- name: Deploy config
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
  vars:
    http_port: 80
    server_name: example.com
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Villkor (if/elif/else)

```jinja2
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

# Med is defined
{% if db_replica is defined and db_replica %}
REPLICA_URL = {{ db_replica_url }}
{% endif %}

# Kortform
STATUS = {{ 'enabled' if feature_on else 'disabled' }}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Loopar (for)

```jinja2
# Enkel loop
{% for server in app_servers %}
server {{ server }};
{% endfor %}

# Med loop-variabler
{% for item in items %}
{{ loop.index }}. {{ item }}{% if not loop.last %},{% endif %}
{% endfor %}

# Loop over dict
{% for key, value in config.items() %}
{{ key }} = {{ value }}
{% endfor %}
```

| Loop-variabel | Beskrivning |
|---------------|-------------|
| `loop.index` | Iteration (1-indexed) |
| `loop.index0` | Iteration (0-indexed) |
| `loop.first` | True om forsta |
| `loop.last` | True om sista |
| `loop.length` | Total antal |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga Filters

| Filter | Exempel | Resultat |
|--------|---------|----------|
| `default` | `{{ x \\| default('val') }}` | Fallback |
| `upper` | `{{ name \\| upper }}` | UPPERCASE |
| `lower` | `{{ name \\| lower }}` | lowercase |
| `join` | `{{ list \\| join(',') }}` | a,b,c |
| `to_json` | `{{ dict \\| to_json }}` | JSON |
| `to_nice_yaml` | `{{ dict \\| to_nice_yaml }}` | YAML |
| `replace` | `{{ s \\| replace(' ','-') }}` | Ersatt |
| `regex_replace` | Regex-ersattning | Pattern |

```jinja2
# Praktiska exempel
PORT = {{ port | default(8080) }}
NAME = {{ app | upper }}
SERVERS = {{ servers | join(', ') }}
CONFIG = {{ settings | to_nice_yaml }}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Template Validering

```yaml
tasks:
  - name: Deploy nginx (med validering)
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
      validate: nginx -t -c %s       # %s = temp-fil

  - name: Deploy sudoers
    template:
      src: sudoers.j2
      dest: /etc/sudoers.d/app
      validate: visudo -cf %s
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Whitespace Control

```jinja2
# Problem: extra radbrytningar
{% for item in items %}
{{ item }}
{% endfor %}

# Losning: - tar bort whitespace
{%- for item in items -%}
{{ item }}
{%- endfor -%}

# Eller anvand join
{{ items | join(', ') }}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| {{ }} | Variabel-output |
| {% %} | Logik (if, for) |
| Filters | Transformera med \\| |
| default | Undvik undefined errors |
| validate | Testa config innan apply |

**Kom ihag:**
- Anvand default-filter for att undvika errors
- validate-parameter for kritiska config-filer
- {# kommentar #} renderas INTE i output
- -% tar bort whitespace
- loop.last for att undvika trailing comma
''',
        },
        {
            "title": "Roles",
            "slug": "roles",
            "difficulty": "intermediate",
            "content": '''# Roles

Roles ar satt att organisera Ansible-kod i ateranvandbara, testbara och delbara komponenter. Istallet for en stor playbook med all logik, bryter du ut funktionalitet i roller som nginx, postgresql, eller deploy - var och en med standardiserad katalogstruktur.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Role Katalogstruktur

```
roles/nginx/
├── defaults/
│   └── main.yml          # Default-variabler (lagst prio)
├── vars/
│   └── main.yml          # Role-variabler (hog prio)
├── tasks/
│   └── main.yml          # Huvudsakliga tasks
├── handlers/
│   └── main.yml          # Handlers
├── templates/
│   └── nginx.conf.j2     # Jinja2 templates
├── files/
│   └── ssl.crt           # Statiska filer
├── meta/
│   └── main.yml          # Dependencies, metadata
└── README.md
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Role Kataloger

| Katalog | Syfte |
|---------|-------|
| `defaults/` | Default-variabler (kan overridas) |
| `vars/` | Fasta variabler (hog prioritet) |
| `tasks/` | Huvudlogiken |
| `handlers/` | Handlers (restart, reload) |
| `templates/` | Jinja2-templates |
| `files/` | Statiska filer att kopiera |
| `meta/` | Dependencies och metadata |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa en Role

```bash
# Skapa role-struktur
ansible-galaxy role init nginx
```

```yaml
# roles/nginx/defaults/main.yml
---
nginx_port: 80
nginx_worker_processes: auto
nginx_sites: []
```

```yaml
# roles/nginx/tasks/main.yml
---
- name: Install nginx
  apt:
    name: nginx
    state: present

- name: Deploy config
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    validate: nginx -t -c %s
  notify: Restart nginx

- name: Ensure running
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Anvanda Roles

```yaml
# site.yml
---
- name: Configure servers
  hosts: webservers
  become: yes

  roles:
    # Enkel
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
      tags: [web, nginx]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## include_role vs roles

| Metod | Nar |
|-------|-----|
| `roles:` | Statisk, kors fore tasks |
| `include_role:` | Dynamisk, inuti tasks |
| `import_role:` | Statisk, inuti tasks |

```yaml
tasks:
  - name: Apply role dynamically
    include_role:
      name: nginx
    when: setup_nginx | default(false)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Role Dependencies

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

```
┌─────────────────────────────────────────────────────────────────┐
│                  DEPENDENCY ORDNING                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   webapp (main role)                                           │
│      │                                                          │
│      ├──► common    (kors forst)                               │
│      ├──► nginx     (kors andra)                               │
│      ├──► nodejs    (kors tredje)                              │
│      └──► webapp tasks (kors sist)                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## OS-specifika Tasks

```yaml
# roles/nginx/tasks/main.yml
---
- name: Include OS-specific vars
  include_vars: "{{ ansible_os_family | lower }}.yml"

- name: Include OS-specific tasks
  include_tasks: "{{ ansible_os_family | lower }}.yml"
```

```yaml
# roles/nginx/tasks/debian.yml
- name: Install nginx (Debian)
  apt:
    name: nginx

# roles/nginx/tasks/redhat.yml
- name: Install nginx (RedHat)
  yum:
    name: nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| defaults/ | Overskrivbara standardvarden |
| vars/ | Fasta role-variabler |
| handlers/ | Kors vid notify |
| meta/ | Dependencies pa andra roles |
| include_tasks | OS-specifik logik |

**Kom ihag:**
- ansible-galaxy role init skapar strukturen
- defaults/ for varden anvandare kan andra
- vars/ for fasta role-installningar
- meta/main.yml for dependencies
- Testa roles separat innan anvandning
''',
        },
        {
            "title": "Ansible Galaxy",
            "slug": "ansible-galaxy",
            "difficulty": "intermediate",
            "content": '''
# Ansible Galaxy

Ansible Galaxy ar det officiella paketsystemet for Ansible - en central hubb dar du hittar tusentals fardiga roles och collections skapade av communityn och foretag. Istallet for att skriva allt fran grunden kan du atervanda beprovat innehall och fokusera pa det som ar unikt for din infrastruktur.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Galaxy Koncept

| Typ | Beskrivning | Exempel |
|-----|-------------|---------|
| Role | Enskilt atervandbart paket | geerlingguy.nginx |
| Collection | Bundle av roles, modules, plugins | community.general |
| FQCN | Fully Qualified Collection Name | amazon.aws.ec2_instance |
| requirements.yml | Beroendefil | Versionshantering |

```
┌─────────────────────────────────────────────────────────────────┐
│                    ANSIBLE GALAXY                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   galaxy.ansible.com                                           │
│         │                                                       │
│         ├──► Roles       (enskilda paket)                      │
│         │      └── geerlingguy.nginx                           │
│         │      └── geerlingguy.docker                          │
│         │                                                       │
│         └──► Collections (bundlade paket)                      │
│                └── community.general                           │
│                └── amazon.aws                                  │
│                └── azure.azcollection                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Galaxy Kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `ansible-galaxy search nginx` | Sok efter roles |
| `ansible-galaxy info ROLE` | Visa role-detaljer |
| `ansible-galaxy install ROLE` | Installera role |
| `ansible-galaxy collection install COL` | Installera collection |
| `ansible-galaxy role list` | Lista installerade roles |
| `ansible-galaxy collection list` | Lista collections |

```bash
# Sok och installera roles
ansible-galaxy search nginx
ansible-galaxy search nginx --platforms Ubuntu
ansible-galaxy info geerlingguy.nginx

# Installera role
ansible-galaxy install geerlingguy.nginx
ansible-galaxy install geerlingguy.nginx,3.1.0       # Specifik version
ansible-galaxy install geerlingguy.nginx -p roles/   # Till mapp

# Installera collections
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install azure.azcollection
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Requirements File

```yaml
# requirements.yml - Definiera alla beroenden
---
roles:
  - name: geerlingguy.nginx
    version: "3.1.0"

  - name: geerlingguy.postgresql
    version: "3.4.0"

  - name: geerlingguy.docker

  # Fran git
  - name: custom-role
    src: git+https://github.com/company/ansible-role.git
    version: v1.2.0

collections:
  - name: community.general
    version: ">=6.0.0"

  - name: amazon.aws
    version: "6.5.0"

  - name: community.docker
```

```bash
# Installera fran requirements.yml
ansible-galaxy install -r requirements.yml
ansible-galaxy collection install -r requirements.yml

# Force reinstall
ansible-galaxy install -r requirements.yml --force

# Till specifik mapp
ansible-galaxy install -r requirements.yml -p ./roles
ansible-galaxy collection install -r requirements.yml -p ./collections
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Anvanda Collections

```yaml
# playbook.yml - Anvand collection modules
---
- name: Deploy to AWS
  hosts: localhost
  connection: local

  collections:
    - amazon.aws                       # Gor alla modules tillgangliga

  tasks:
    - name: Create S3 bucket
      s3_bucket:                       # Utan FQCN
        name: my-bucket
        state: present

    # Med FQCN (Fully Qualified Collection Name)
    - name: Create EC2 instance
      amazon.aws.ec2_instance:
        name: web-server
        instance_type: t3.micro
        image_id: ami-12345678
```

| Metod | Syntax | Fordel |
|-------|--------|--------|
| collections: | `s3_bucket:` | Kortare syntax |
| FQCN | `amazon.aws.ec2_instance:` | Tydlig kalla |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa Egen Role

```bash
# Initiera ny role
ansible-galaxy role init my_company.webserver
```

```
my_company.webserver/
├── README.md                  # Dokumentation
├── meta/
│   └── main.yml               # Galaxy metadata
├── defaults/
│   └── main.yml               # Overskrivbara varden
├── tasks/
│   └── main.yml               # Huvudlogik
├── handlers/
│   └── main.yml               # Handlers
└── templates/                 # Jinja2-templates
```

```yaml
# meta/main.yml - Galaxy metadata
---
galaxy_info:
  role_name: webserver
  namespace: my_company
  author: Your Name
  description: Configure webserver with nginx
  license: MIT
  min_ansible_version: "2.14"

  platforms:
    - name: Ubuntu
      versions:
        - jammy
        - focal

  galaxy_tags:
    - web
    - nginx

dependencies:
  - geerlingguy.nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa Egen Collection

```bash
# Skapa collection-struktur
ansible-galaxy collection init my_company.infrastructure
```

```
my_company/infrastructure/
├── README.md
├── galaxy.yml                 # Collection metadata
├── plugins/
│   ├── modules/               # Custom modules
│   ├── lookup/                # Lookup plugins
│   └── filter/                # Filter plugins
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
description: Infrastructure automation
license:
  - MIT
dependencies:
  community.general: ">=6.0.0"
```

```bash
# Bygg och publicera
ansible-galaxy collection build
ansible-galaxy collection publish my_company-infrastructure-1.0.0.tar.gz --token TOKEN
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Private Galaxy

```bash
# Anvand privat Galaxy-server
ansible-galaxy collection install my_collection \\
  --server https://galaxy.internal.company.com
```

```ini
# ansible.cfg
[galaxy]
server_list = private_galaxy, galaxy

[galaxy_server.private_galaxy]
url = https://galaxy.internal.company.com/api/
token = YOUR_TOKEN

[galaxy_server.galaxy]
url = https://galaxy.ansible.com/
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Version Constraints

| Syntax | Betydelse |
|--------|-----------|
| `"6.5.0"` | Exakt version |
| `">=6.0.0"` | Minst version |
| `">=6.0.0,<7.0.0"` | Range |
| `"*"` | Senaste |

```yaml
# requirements.yml
collections:
  - name: community.general
    version: ">=6.0.0,<7.0.0"

  - name: amazon.aws
    version: "6.5.0"

roles:
  - name: geerlingguy.nginx
    version: ">=3.0.0"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Galaxy | Central hubb for roles/collections |
| requirements.yml | Versionerade beroenden |
| Collection | Bundle av roles, modules, plugins |
| FQCN | Fully Qualified Collection Name |
| ansible-galaxy | CLI for sokning/installation |

**Kom ihag:**
- Anvand Galaxy istallet for att skriva allt sjalv
- requirements.yml for reproducerbarhet
- FQCN ger tydlig module-kalla
- Versionera alltid dina beroenden
- Skapa egna roles for intern ateranvandning
''',
        },
        {
            "title": "Conditionals & Loops",
            "slug": "conditionals-loops",
            "difficulty": "intermediate",
            "content": '''
# Conditionals & Loops

Villkor och loopar ar kraftfulla konstruktioner som gor dina playbooks dynamiska och flexibla. Med when-satser kan du anpassa tasks efter OS, miljo eller variabelvarden. Loopar lat dig iterera over listor och dictionaries for att hantera multipla resurser elegant utan upprepning.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Villkors- och Loop-typer

| Typ | Syfte | Exempel |
|-----|-------|---------|
| `when` | Kor task om villkor ar sant | `when: ansible_os_family == "Debian"` |
| `loop` | Iterera over lista | `loop: [nginx, curl, vim]` |
| `until` | Retry tills villkor | `until: result.status == 200` |
| `loop_control` | Kontrollera loop-beteende | `index_var`, `label` |

```
┌─────────────────────────────────────────────────────────────────┐
│              CONDITIONAL & LOOP FLOW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   when: condition                                               │
│      └──► TRUE  ──► Task kors                                  │
│      └──► FALSE ──► Task skippas                               │
│                                                                 │
│   loop: [a, b, c]                                              │
│      └──► item=a ──► Task kors                                 │
│      └──► item=b ──► Task kors                                 │
│      └──► item=c ──► Task kors                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## When Conditionals

```yaml
tasks:
  # Enkel condition
  - name: Install on Ubuntu
    apt:
      name: nginx
    when: ansible_distribution == "Ubuntu"

  # Multiple conditions (AND)
  - name: Install on Ubuntu 22.04
    apt:
      name: nginx
    when:
      - ansible_distribution == "Ubuntu"
      - ansible_distribution_version == "22.04"

  # OR condition
  - name: Install on Debian family
    apt:
      name: nginx
    when: ansible_distribution == "Ubuntu" or ansible_distribution == "Debian"

  # Anvand facts
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

| Operator | Beskrivning | Exempel |
|----------|-------------|---------|
| `==` | Lika med | `when: var == "value"` |
| `!=` | Inte lika | `when: var != "value"` |
| `>`, `<` | Storre/mindre | `when: count > 5` |
| `in` | Innehaller | `when: "'error' in output"` |
| `is defined` | Existerar | `when: var is defined` |
| `and`, `or` | Logiska | `when: a and b` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Register och Conditionals

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Loop Basics

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

  # Loop med label (for output)
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

| loop_control | Beskrivning |
|--------------|-------------|
| `index_var` | Variabel for loop-index (0-baserat) |
| `label` | Vad som visas i output |
| `pause` | Sekunder mellan iterationer |
| `extended` | Extra loop-info (first, last, etc) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dictionary Loops

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
  # Loop over dict med dict2items
  - name: Create users from dict
    user:
      name: "{{ item.key }}"
      groups: "{{ item.value.groups }}"
      shell: "{{ item.value.shell }}"
    loop: "{{ users | dict2items }}"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Nested Loops

```yaml
vars:
  environments: [dev, staging, prod]
  services: [web, api, worker]

tasks:
  # Product - alla kombinationer
  - name: Create service directories
    file:
      path: "/opt/{{ item.0 }}/{{ item.1 }}"
      state: directory
    loop: "{{ environments | product(services) | list }}"
    # Skapar: dev/web, dev/api, dev/worker, staging/web, etc.

  # Subelements - for nested lists
  - name: Create user SSH keys
    authorized_key:
      user: "{{ item.0.name }}"
      key: "{{ item.1 }}"
    loop: "{{ users | subelements('ssh_keys') }}"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Until Loops (Retry)

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
    delay: 10                    # Sekunder mellan forsok

  # Wait for deployment
  - name: Wait for replicas
    command: kubectl get deployment myapp -o jsonpath='{.status.availableReplicas}'
    register: replicas
    until: replicas.stdout | int >= 3
    retries: 60
    delay: 5
```

| Parameter | Beskrivning | Default |
|-----------|-------------|---------|
| `until` | Villkor som maste vara sant | - |
| `retries` | Max antal forsok | 3 |
| `delay` | Sekunder mellan forsok | 5 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Loop med Conditionals

```yaml
tasks:
  # Filter i loop
  - name: Install only enabled services
    apt:
      name: "{{ item.name }}"
    loop: "{{ services }}"
    when: item.enabled | default(true)

  # Skip vissa items
  - name: Create users except admin
    user:
      name: "{{ item }}"
    loop: [alice, bob, admin]
    when: item != 'admin'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Block Conditionals

```yaml
tasks:
  - name: Production-only configuration
    block:
      - name: Install monitoring agent
        apt:
          name: datadog-agent

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| when | Conditional execution baserat pa villkor |
| loop | Iterera over listor (ersatter with_*) |
| loop_control | Index, label, pause for loops |
| until | Retry-logik med retries/delay |
| block + when | Applicera villkor pa flera tasks |

**Kom ihag:**
- when utvarderats for varje host separat
- loop: med dict2items for dictionaries
- Kombinera loop och when for filtrering
- until ar perfekt for wait-scenarios
- Block gor villkor pa grupper av tasks
''',
        },
        {
            "title": "Error Handling",
            "slug": "error-handling",
            "difficulty": "intermediate",
            "content": '''
# Error Handling

Fel ar oundvikliga i distribuerade system - servrar kan vara otillgangliga, tjanster kan krascha, och kommandon kan misslyckas. Ansible erbjuder kraftfulla verktyg for att hantera dessa situationer graciost, fran att ignorera icke-kritiska fel till komplett rollback-logik med block/rescue/always.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Felhanteringsverktyg

| Verktyg | Beskrivning | Anvandning |
|---------|-------------|------------|
| `ignore_errors` | Fortsatt vid fel | Icke-kritiska tasks |
| `failed_when` | Custom failure-villkor | Specifik fellogik |
| `changed_when` | Custom change-detection | Idempotens |
| `block/rescue/always` | Try/catch/finally | Rollback-logik |
| `any_errors_fatal` | Stoppa allt vid fel | Kritiska tasks |
| `assert` | Validera forutsattningar | Pre-flight checks |

```
┌─────────────────────────────────────────────────────────────────┐
│                    ERROR HANDLING FLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Task kors                                                     │
│      │                                                          │
│      ├── SUCCESS ──► Nasta task                                │
│      │                                                          │
│      └── FAILURE                                                │
│             │                                                   │
│             ├── ignore_errors: yes ──► Fortsatt               │
│             ├── block/rescue ──► Kor rescue-tasks              │
│             └── default ──► Stoppa playbook                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ignore_errors

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
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## failed_when och changed_when

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
    failed_when: false

  # Command som aldrig andrar
  - name: Get current version
    command: cat /etc/version
    register: version
    changed_when: false

  # Custom change detection
  - name: Update configuration
    command: /opt/update-config.sh
    register: update_result
    changed_when: "'Updated' in update_result.stdout"
```

| Direktiv | Varde | Effekt |
|----------|-------|--------|
| `failed_when: false` | Alltid | Misslyckas aldrig |
| `failed_when: rc != 0` | Villkor | Custom fel-villkor |
| `changed_when: false` | Alltid | Rapporterar aldrig changed |
| `changed_when: "'x' in out"` | Villkor | Changed vid match |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## block/rescue/always

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

    always:
      - name: Cleanup temp files
        file:
          path: /tmp/deploy
          state: absent

      - name: Record deployment attempt
        lineinfile:
          path: /var/log/deployments.log
          line: "{{ ansible_date_time.iso8601 }} - Deployment completed"
```

| Block | Beskrivning |
|-------|-------------|
| `block:` | Huvudsakliga tasks (try) |
| `rescue:` | Kors om block misslyckas (catch) |
| `always:` | Kors alltid (finally) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## any_errors_fatal

```yaml
# Stoppa vid forsta fel
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## assert och fail

```yaml
tasks:
  # Validera forutsattningar
  - name: Verify prerequisites
    assert:
      that:
        - ansible_memtotal_mb >= 2048
        - ansible_processor_vcpus >= 2
        - ansible_distribution == "Ubuntu"
      fail_msg: "Server does not meet minimum requirements"
      success_msg: "All prerequisites met"

  # Villkorlig fail
  - name: Check environment
    fail:
      msg: "Cannot deploy to production on Friday!"
    when:
      - environment == 'production'
      - ansible_date_time.weekday == 'Friday'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## max_fail_percentage

```yaml
# Tillat viss andel failures
- name: Rolling update
  hosts: webservers
  serial: 5                     # 5 hosts at gangen
  max_fail_percentage: 20       # Max 20% far faila

  tasks:
    - name: Deploy and restart
      copy:
        src: app.tar.gz
        dest: /opt/app.tar.gz
      notify: Restart app
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| ignore_errors | Fortsatt vid icke-kritiska fel |
| failed_when | Definiera egna failure-villkor |
| changed_when | Kontrollera change-rapportering |
| block/rescue/always | Strukturerad felhantering med rollback |
| any_errors_fatal | Stoppa allt vid forsta fel |
| assert | Validera prerequisites |

**Kom ihag:**
- Anvand ignore_errors sparsamt - doljer problem
- block/rescue ar perfekt for deployment med rollback
- always kors oavsett - bra for cleanup
- assert i borjan validerar forutsattningar
- max_fail_percentage for rolling updates
''',
        },
        {
            "title": "Vault & Secrets",
            "slug": "vault-secrets",
            "difficulty": "intermediate",
            "content": '''
# Vault & Secrets

Hemlig data som losenord, API-nycklar och certifikat maste skyddas - de far aldrig ligga i klartext i version control. Ansible Vault erbjuder AES256-kryptering som lat dig lagra kanslig data sakert medan den fortfarande ar anvandbar i dina playbooks.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vault Kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `ansible-vault create FILE` | Skapa ny krypterad fil |
| `ansible-vault edit FILE` | Redigera krypterad fil |
| `ansible-vault view FILE` | Visa innehall |
| `ansible-vault encrypt FILE` | Kryptera befintlig fil |
| `ansible-vault decrypt FILE` | Dekryptera fil |
| `ansible-vault rekey FILE` | Andra losenord |
| `ansible-vault encrypt_string` | Kryptera enskilt varde |

```bash
# Grundlaggande vault-operationer
ansible-vault create secrets.yml
ansible-vault edit secrets.yml
ansible-vault view secrets.yml
ansible-vault encrypt vars/secrets.yml
ansible-vault decrypt vars/secrets.yml
ansible-vault rekey secrets.yml
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vault i Playbook

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
    - vars/secrets.yml        # Krypterad fil

  tasks:
    - name: Configure database
      template:
        src: database.conf.j2
        dest: /etc/app/database.conf
      vars:
        password: "{{ db_password }}"
```

```bash
# Kor med vault password
ansible-playbook playbook.yml --ask-vault-pass
ansible-playbook playbook.yml --vault-password-file ~/.vault_pass
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kryptera Enskilda Varden

```bash
# Kryptera en strang
ansible-vault encrypt_string 'supersecret' --name 'db_password'

# Output:
# db_password: !vault |
#           $ANSIBLE_VAULT;1.1;AES256
#           61626364...
```

```yaml
# vars/main.yml - Okrypterad fil med krypterat varde
---
app_name: myapp
environment: production

# Krypterat varde inline
db_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          61626364656667686970...

# Okrypterade varden
db_host: localhost
db_port: 5432
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Multipla Vault-losenord

```bash
# Vault ID for olika miljoer
ansible-vault create --vault-id dev@prompt secrets_dev.yml
ansible-vault create --vault-id prod@prompt secrets_prod.yml
ansible-vault create --vault-id prod@/path/to/prod_pass secrets_prod.yml

# Kor med multipla vault IDs
ansible-playbook playbook.yml \\
  --vault-id dev@prompt \\
  --vault-id prod@~/.vault_prod
```

| Vault ID Source | Syntax | Beskrivning |
|-----------------|--------|-------------|
| Prompt | `dev@prompt` | Fraga efter losenord |
| Fil | `prod@~/.vault_pass` | Las fran fil |
| Script | `prod@./get_pass.py` | Kor script |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vault Password File

```bash
# Skapa password-fil
echo 'mysecretpassword' > ~/.vault_pass
chmod 600 ~/.vault_pass
```

```ini
# ansible.cfg
[defaults]
vault_password_file = ~/.vault_pass
```

```python
#!/usr/bin/env python3
# vault_pass_script.py - Hamta fran extern kalla
import subprocess

# Hamta fran 1Password
result = subprocess.run(
    ['op', 'read', 'op://Vault/AnsibleVault/password'],
    capture_output=True, text=True
)
print(result.stdout.strip())
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Best Practices Struktur

```
group_vars/
├── all/
│   ├── vars.yml         # Okrypterade variabler
│   └── vault.yml        # Krypterade variabler
├── production/
│   ├── vars.yml
│   └── vault.yml
└── staging/
    ├── vars.yml
    └── vault.yml
```

```yaml
# group_vars/production/vault.yml (krypterad)
---
vault_db_password: supersecret
vault_api_key: abc123xyz
```

```yaml
# group_vars/production/vars.yml (okrypterad)
---
environment: production
db_host: db.prod.example.com
# Referera vault-variabler
db_password: "{{ vault_db_password }}"
api_key: "{{ vault_api_key }}"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Externa Secret Managers

| Provider | Lookup Plugin |
|----------|---------------|
| HashiCorp Vault | `hashi_vault` |
| AWS Secrets Manager | `amazon.aws.aws_secret` |
| Azure Key Vault | `azure.azcollection.azure_keyvault_secret` |

```yaml
# Hamta fran HashiCorp Vault
- name: Get secret
  set_fact:
    db_password: "{{ lookup('hashi_vault', 'secret/data/myapp:db_password') }}"

# Hamta fran AWS Secrets Manager
- name: Get AWS secret
  set_fact:
    db_password: "{{ lookup('amazon.aws.aws_secret', 'myapp/db_password') }}"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| ansible-vault | Krypterar med AES256 |
| encrypt_string | Kryptera enskilda varden inline |
| Vault IDs | Multipla losenord for olika miljoer |
| vault_ prefix | Konvention for krypterade variabler |
| External secrets | HashiCorp, AWS, Azure integration |

**Kom ihag:**
- Aldrig lagra secrets i klartext i git
- Anvand vault_password_file i ansible.cfg
- Separera vault.yml fran vars.yml
- vault_ prefix gor det tydligt vad som ar krypterat
- For enterprise: overväg externa secret managers
''',
        },
        {
            "title": "Ansible in CI/CD",
            "slug": "ansible-cicd",
            "difficulty": "advanced",
            "content": '''
# Ansible in CI/CD

Att integrera Ansible i CI/CD-pipelines automatiserar hela deployment-processen - fran kodandring till produktion. Varje commit kan trigga linting, tester och deployment till ratt miljo, vilket ger snabbare leveranser och konsistenta deployments med full audit trail.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CI/CD Pipeline Steg

| Steg | Verktyg | Syfte |
|------|---------|-------|
| Lint | ansible-lint, yamllint | Kodkvalitet |
| Syntax | --syntax-check | Validerering |
| Test | Molecule | Integration testing |
| Deploy Staging | ansible-playbook | Testa i staging |
| Approve | Manual gate | Kvalitetssakring |
| Deploy Prod | ansible-playbook | Produktion |

```
┌─────────────────────────────────────────────────────────────────┐
│                    CI/CD PIPELINE FLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Push/PR ──► Lint ──► Test ──► Deploy Staging                 │
│                                      │                          │
│                                      ▼                          │
│                              Manual Approve                     │
│                                      │                          │
│                                      ▼                          │
│                              Deploy Production                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install ansible ansible-lint yamllint

      - name: YAML Lint
        run: yamllint .

      - name: Ansible Lint
        run: ansible-lint

      - name: Syntax check
        run: ansible-playbook site.yml --syntax-check

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Molecule
        run: pip install molecule molecule-docker ansible

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
      - run: pip install ansible

      - name: Setup SSH
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_KEY }}" > ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa

      - name: Deploy
        run: ansible-playbook -i inventory/staging site.yml
        env:
          ANSIBLE_VAULT_PASSWORD: ${{ secrets.VAULT_PASS }}

  deploy-production:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - run: pip install ansible
      - name: Deploy
        run: |
          ansible-playbook -i inventory/production site.yml \\
            --vault-password-file <(echo "${{ secrets.VAULT_PASS }}")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
    - apk add python3 py3-pip
    - pip install molecule molecule-docker ansible
  script:
    - cd roles/webserver && molecule test

deploy-staging:
  stage: deploy
  environment: staging
  only: [develop]
  script:
    - pip install ansible
    - ansible-playbook -i inventory/staging site.yml

deploy-production:
  stage: deploy
  environment: production
  only: [main]
  when: manual              # Manuell approve
  script:
    - ansible-playbook -i inventory/production site.yml
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Ansible-lint Konfiguration

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

use_default_rules: true
```

| Profile | Strikthet |
|---------|----------|
| min | Minimal |
| basic | Grundlaggande |
| moderate | Medelstark |
| safety | Fokus pa sakerhet |
| shared | For delade roles |
| production | Strikt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Molecule i CI/CD

```yaml
# molecule/default/molecule.yml
---
driver:
  name: docker
platforms:
  - name: ubuntu-22
    image: geerlingguy/docker-ubuntu2204-ansible
    pre_build_image: true
    privileged: true
    command: /lib/systemd/systemd

provisioner:
  name: ansible
  playbooks:
    converge: converge.yml
    verify: verify.yml

scenario:
  test_sequence:
    - lint
    - destroy
    - create
    - converge
    - idempotence
    - verify
    - destroy
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## AWX / Ansible Tower

```yaml
# Skapa job template via API
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
```

```bash
# Trigger AWX job fran CI/CD
curl -X POST \\
  -H "Authorization: Bearer $AWX_TOKEN" \\
  -d '{"extra_vars": {"version": "1.2.3"}}' \\
  "https://awx.example.com/api/v2/job_templates/123/launch/"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Lint | ansible-lint i varje pipeline |
| Molecule | Testa roles i containers |
| Environments | Staging fore production |
| Manual gates | Approve innan prod-deploy |
| Secrets | Vault-losenord som CI/CD secrets |
| AWX/Tower | Enterprise orchestration |

**Kom ihag:**
- Lint och syntax-check pa varje commit
- Molecule testar roles isolerat
- Separata environments med approval gates
- Vault-losenord som CI/CD secrets (aldrig i kod)
- AWX/Tower for visuell orchestration
''',
        },
        {
            "title": "Dynamic Inventory",
            "slug": "dynamic-inventory",
            "difficulty": "advanced",
            "content": '''
# Dynamic Inventory

I molnmiljoer ar infrastrukturen i konstant forandring - servrar skapas och tas bort, auto-scaling andrar antal instanser, och IP-adresser byts ut. Dynamic inventory loser detta genom att fraga cloud-APIs i realtid och alltid ge dig en aktuell bild av din infrastruktur.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dynamic Inventory Koncept

| Koncept | Beskrivning |
|---------|-------------|
| Plugin | Inbyggd integration (AWS, Azure, GCP) |
| Script | Custom inventory via Python/Bash |
| keyed_groups | Automatiska grupper fran tags |
| compose | Definiera host-variabler |
| filters | Filtrera vilka hosts som inkluderas |

```
┌─────────────────────────────────────────────────────────────────┐
│                 DYNAMIC INVENTORY FLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ansible-playbook -i aws_ec2.yml site.yml                     │
│         │                                                       │
│         ▼                                                       │
│   Plugin fragar AWS API                                        │
│         │                                                       │
│         ▼                                                       │
│   Returnerar JSON med hosts                                    │
│         │                                                       │
│         ▼                                                       │
│   Ansible kor playbook mot aktuella hosts                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## AWS EC2 Plugin

```yaml
# inventory/aws_ec2.yml
---
plugin: amazon.aws.aws_ec2

regions:
  - eu-north-1
  - eu-west-1

filters:
  instance-state-name: running
  tag:Environment:
    - production
    - staging

keyed_groups:
  - key: tags.Environment
    prefix: env
  - key: tags.Role
    prefix: role
  - key: placement.availability_zone
    prefix: az

groups:
  webservers: "'web' in tags.Role"
  production: "tags.Environment == 'production'"

compose:
  ansible_host: private_ip_address
  ansible_user: "'ubuntu'"

hostnames:
  - tag:Name
  - private-ip-address
```

```bash
# Installera och testa
ansible-galaxy collection install amazon.aws
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=...

ansible-inventory -i inventory/aws_ec2.yml --graph
ansible-inventory -i inventory/aws_ec2.yml --list
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Azure Plugin

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

hostvar_expressions:
  ansible_host: private_ipv4_addresses[0]
  ansible_user: "'azureuser'"

exclude_host_filters:
  - powerstate != 'running'
```

```bash
ansible-galaxy collection install azure.azcollection
az login
ansible-inventory -i inventory/azure_rm.yml --graph
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GCP Plugin

```yaml
# inventory/gcp.yml
---
plugin: google.cloud.gcp_compute

projects:
  - my-gcp-project

regions:
  - europe-north1

filters:
  - status = RUNNING

keyed_groups:
  - key: labels.environment
    prefix: env
  - key: labels.role
    prefix: role

compose:
  ansible_host: networkInterfaces[0].networkIP
  ansible_user: "'ubuntu'"
```

```bash
ansible-galaxy collection install google.cloud
export GCP_SERVICE_ACCOUNT_FILE=/path/to/sa.json
ansible-inventory -i inventory/gcp.yml --graph
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Custom Dynamic Inventory

```python
#!/usr/bin/env python3
# inventory/custom_inventory.py
import json
import argparse
import requests

def get_inventory():
    response = requests.get(
        'https://cmdb.internal/api/servers',
        headers={'Authorization': 'Bearer TOKEN'}
    )
    servers = response.json()

    inventory = {
        '_meta': {'hostvars': {}},
        'all': {'children': ['webservers', 'dbservers']},
        'webservers': {'hosts': []},
        'dbservers': {'hosts': []}
    }

    for server in servers:
        hostname = server['hostname']
        group = 'webservers' if server['role'] == 'web' else 'dbservers'
        inventory[group]['hosts'].append(hostname)
        inventory['_meta']['hostvars'][hostname] = {
            'ansible_host': server['ip_address'],
            'ansible_user': 'deploy'
        }
    return inventory

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--host', type=str)
    args = parser.parse_args()

    if args.list:
        print(json.dumps(get_inventory(), indent=2))
```

```bash
chmod +x inventory/custom_inventory.py
./inventory/custom_inventory.py --list
ansible-playbook -i inventory/custom_inventory.py site.yml
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kombinera Inventory Sources

```
inventory/
├── static_hosts.yml      # Statiska hosts
├── aws_ec2.yml           # AWS EC2
├── azure_rm.yml          # Azure VMs
└── group_vars/
    └── all.yml
```

```bash
# Ansible laser alla filer i mappen
ansible-playbook -i inventory/ site.yml
```

```ini
# ansible.cfg
[defaults]
inventory = ./inventory
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Dynamic inventory | Realtidsdata fran cloud APIs |
| keyed_groups | Automatiska grupper fran tags/labels |
| compose | Definiera ansible_host, ansible_user |
| Custom scripts | Python for interna system |
| Kombinera | Statisk + dynamisk i samma mapp |

**Kom ihag:**
- Plugins finns for AWS, Azure, GCP, K8s
- keyed_groups skapar grupper automatiskt fran tags
- compose satter host-variabler
- Custom scripts maste stodja --list och --host
- Kombinera flera sources i en inventory-mapp
''',
        },
        {
            "title": "Performance Tuning",
            "slug": "performance-tuning",
            "difficulty": "advanced",
            "content": '''
# Performance Tuning

Nar du hanterar hundratals eller tusentals servrar blir prestanda kritiskt. En playbook som tar 30 minuter kan optimeras till 5 minuter med ratt installningar - forks, pipelining, fact caching och effektiva playbook-monster gor enorm skillnad.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Optimeringsomraden

| Omrade | Teknik | Effekt |
|--------|--------|--------|
| Parallellism | forks | Fler hosts samtidigt |
| SSH | pipelining | Minskar overhead |
| Facts | caching | Undviker upprepning |
| Tasks | async | Langvariga i bakgrund |
| Strategy | free/mitogen | Snabbare exekvering |

```
┌─────────────────────────────────────────────────────────────────┐
│              PERFORMANCE OPTIMIZATION                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Default (forks=5)          Optimized (forks=50)              │
│   ─────────────────          ────────────────────              │
│   Host1 ──────►              Host1-50 ──────►                  │
│   Host2 ──────►                   │                            │
│   Host3 ──────►              Host51-100 ─────►                 │
│   Host4 ──────►                                                │
│   Host5 ──────►              2-7x snabbare med Mitogen         │
│   (vantar...)                                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Tuning

```ini
# ansible.cfg
[defaults]
forks = 50                    # Parallella anslutningar (default: 5)
host_key_checking = False     # Skippa host key verify
gathering = smart             # Cache facts
callback_whitelist = profile_tasks, timer

[ssh_connection]
pipelining = True             # STOR skillnad!
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
transfer_method = piped
```

| Installning | Default | Rekommenderat | Effekt |
|-------------|---------|---------------|--------|
| forks | 5 | 25-50 | Fler parallella hosts |
| pipelining | False | True | 2x snabbare |
| gathering | implicit | smart | Cache facts |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Fact Caching

```ini
# ansible.cfg
[defaults]
gathering = smart
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_facts_cache
fact_caching_timeout = 86400      # 24 timmar

# Eller Redis for team
fact_caching = redis
fact_caching_connection = localhost:6379:0
```

```yaml
# Skippa facts om inte nodvandigt
- name: Quick deployment
  hosts: webservers
  gather_facts: no

  tasks:
    - name: Deploy app
      copy:
        src: app.tar.gz
        dest: /opt/
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pipelining

```ini
# ansible.cfg
[ssh_connection]
pipelining = True
```

```bash
# Kraver pa malservrar (sudoers):
# Defaults !requiretty
# deploy ALL=(ALL) NOPASSWD: ALL
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Async Tasks

```yaml
tasks:
  # Kor asynkront
  - name: Long running task
    command: /opt/long-script.sh
    async: 3600              # Max runtime
    poll: 0                  # Vanta inte
    register: long_task

  # Fortsatt med annat
  - name: Do other things
    apt:
      name: nginx

  # Kolla status senare
  - name: Check on long task
    async_status:
      jid: "{{ long_task.ansible_job_id }}"
    register: job_result
    until: job_result.finished
    retries: 60
    delay: 60
```

| Parameter | Beskrivning |
|-----------|-------------|
| async | Max koretid i sekunder |
| poll: 0 | Fire-and-forget |
| async_status | Kolla jobb-status |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Strategy

```yaml
# Free strategy - hosts vantar inte pa varandra
- name: Deploy
  hosts: webservers
  strategy: free

  tasks:
    - apt:
        name: nginx
```

| Strategy | Beskrivning |
|----------|-------------|
| linear | Default, alla hosts per task |
| free | Hosts kor sa fort de kan |
| mitogen_linear | 2-7x snabbare |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Playbook Optimering

```yaml
# INEFFEKTIVT - flera apt-anrop
- apt: name=nginx state=present
- apt: name=curl state=present
- apt: name=vim state=present

# EFFEKTIVT - ett anrop
- name: Install packages
  apt:
    name: [nginx, curl, vim]
    state: present
```

```yaml
# Handlers - restart EN gang
tasks:
  - template: src=1.conf.j2 dest=/etc/1.conf
    notify: Restart app
  - template: src=2.conf.j2 dest=/etc/2.conf
    notify: Restart app

handlers:
  - name: Restart app
    service: name=app state=restarted
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Serial (Rolling Deploy)

```yaml
- name: Rolling update
  hosts: webservers
  serial: 5              # 5 hosts at gangen
  # serial: "20%"        # 20% at gangen
  # serial: [1, 5, "100%"]  # Canary

  tasks:
    - include_tasks: deploy.yml
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Profiling

```ini
# ansible.cfg
[defaults]
callback_whitelist = profile_tasks, timer
```

```
# Output visar tid per task:
apt ----------------------- 45.23s
template ------------------ 12.45s
service ------------------- 3.21s
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| forks | Oka parallellism (25-50) |
| pipelining | True minskar SSH overhead |
| Fact caching | smart + jsonfile/redis |
| async | Langvariga tasks i bakgrund |
| Batching | Samla paket i en apt-task |
| serial | Rolling deploy for sakerhet |

**Kom ihag:**
- forks=50 och pipelining=True forst
- gather_facts: no om du inte behover facts
- Batcha paketinstallationer
- Anvand handlers istallet for multipla restarts
- profile_tasks visar var tiden gar
''',
        },
        {
            "title": "Testing with Molecule",
            "slug": "testing-molecule",
            "difficulty": "advanced",
            "content": '''
# Testing with Molecule

Ansible-kod behover testas precis som all annan kod. Molecule ar standardverktyget for att testa Ansible roles - det skapar isolerade testmiljoer i Docker-containers, kor dina playbooks, verifierar resultatet och sakerstaller idempotens.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Installation

```bash
# Installera Molecule med Docker driver
pip install molecule molecule-docker

# Verifiera
molecule --version
```

| Driver | Anvandning |
|--------|------------|
| docker | Snabbast, vanligast |
| podman | Docker-alternativ |
| vagrant | VMs for full systemtest |
| ec2 | AWS-instanser |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Molecule Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                  MOLECULE TEST SEQUENCE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   lint ──► destroy ──► create ──► converge                     │
│                                      │                          │
│                                      ▼                          │
│                              idempotence                        │
│                                      │                          │
│                                      ▼                          │
│                              verify ──► destroy                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Steg | Beskrivning |
|------|-------------|
| lint | Validera YAML och Ansible syntax |
| destroy | Ta bort eventuella gamla containers |
| create | Skapa testcontainers |
| converge | Kor playbook/role |
| idempotence | Kor igen - ska inte andra nagot |
| verify | Verifiera att allt fungerar |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Initiera Molecule

```bash
cd roles/webserver
molecule init scenario -d docker
```

```
roles/webserver/
└── molecule/
    └── default/
        ├── converge.yml      # Kor rolen
        ├── molecule.yml      # Konfiguration
        └── verify.yml        # Testa resultat
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## molecule.yml Konfiguration

```yaml
# molecule/default/molecule.yml
---
driver:
  name: docker

platforms:
  - name: ubuntu-22
    image: geerlingguy/docker-ubuntu2204-ansible
    pre_build_image: true
    privileged: true
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
    - lint
    - destroy
    - create
    - converge
    - idempotence
    - verify
    - destroy
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## converge.yml och verify.yml

```yaml
# converge.yml - Kor rolen
---
- name: Converge
  hosts: all
  become: yes

  roles:
    - role: webserver
      vars:
        nginx_port: 8080
```

```yaml
# verify.yml - Verifiera resultat
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

    - name: Check nginx responds
      uri:
        url: http://localhost:8080
        status_code: 200
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Molecule Kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `molecule test` | Kor alla steg |
| `molecule create` | Skapa containers |
| `molecule converge` | Kor playbook |
| `molecule idempotence` | Testa idempotens |
| `molecule verify` | Kor verifiering |
| `molecule login` | SSH till container |
| `molecule destroy` | Ta bort containers |
| `molecule list` | Lista status |

```bash
# Vanligt workflow under utveckling
molecule create
molecule converge
molecule login          # Debugga
molecule converge       # Testa igen
molecule verify
molecule destroy
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Multiple Scenarios

```bash
molecule init scenario --scenario-name ubuntu-only -d docker
molecule init scenario --scenario-name integration -d vagrant
```

```
molecule/
├── default/
│   └── molecule.yml
├── ubuntu-only/
│   └── molecule.yml
└── integration/
    └── molecule.yml
```

```bash
molecule test -s ubuntu-only
molecule converge -s integration
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CI/CD Integration

```yaml
# .github/workflows/molecule.yml
name: Molecule Test
on: [push, pull_request]

jobs:
  molecule:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        distro: [ubuntu2204, debian12]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install molecule molecule-docker ansible
      - run: molecule test
        env:
          MOLECULE_DISTRO: ${{ matrix.distro }}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| Molecule | Standard for Ansible role testing |
| converge.yml | Kor rolen mot testcontainers |
| verify.yml | Validera resultat med assert |
| idempotence | Kor 2x - ska vara identiskt |
| Scenarios | Olika testmiljoer (OS, drivers) |

**Kom ihag:**
- molecule test kor alla steg automatiskt
- converge + login ar bra for debugging
- Idempotens ar kritiskt - inga andringar vid andra korning
- Multipla scenarios for olika OS/miljoer
- Integrera i CI/CD for automatisk testning
''',
        },
        {
            "title": "Callback Plugins",
            "slug": "callback-plugins",
            "difficulty": "advanced",
            "content": '''
# Callback Plugins

Callback plugins lat dig utoka Ansibles beteende genom att haka pa events under korningen. Du kan anvanda inbyggda callbacks for profiling och JSON-output, eller skapa egna for att skicka notifikationer till Slack, logga till externa system eller integrera med monitoring-verktyg.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Callback Typer

| Typ | Beskrivning | Exempel |
|-----|-------------|--------|
| stdout | Andrar output-format | yaml, json, minimal |
| notification | Skickar events externt | Slack, email |
| aggregate | Samlar statistik | profile_tasks |

```
┌─────────────────────────────────────────────────────────────────┐
│                   CALLBACK EVENTS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   playbook_on_start                                            │
│         │                                                       │
│         ▼                                                       │
│   play_on_start ──► task_on_start ──► runner_on_ok            │
│                                    └─► runner_on_failed         │
│         │                                                       │
│         ▼                                                       │
│   playbook_on_stats                                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Inbyggda Callbacks

```ini
# ansible.cfg
[defaults]
# Aktivera flera callbacks
callbacks_enabled = profile_tasks, timer, json

# Stdout callback (en at gangen)
stdout_callback = yaml
```

| Callback | Beskrivning |
|----------|-------------|
| default | Standard output |
| yaml | YAML-formaterad output |
| json | JSON for parsing |
| minimal | Minimal output |
| profile_tasks | Tid per task |
| profile_roles | Tid per role |
| timer | Total koretid |

```bash
# Lista alla callbacks
ansible-doc -t callback -l

# Visa dokumentation
ansible-doc -t callback profile_tasks
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Profile Callbacks

```ini
# ansible.cfg
[defaults]
callbacks_enabled = profile_tasks, timer
```

```
# Output med profile_tasks:
TASK [Install nginx] ************************
ok: [web1]

Tuesday 05 December 2024 (0:00:45.123)
===============================================
Install nginx -------------------- 45.12s
Start service -------------------- 2.34s
-----------------------------------------------
Total ---------------------------- 47.46s
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## JSON Callback

```bash
# JSON output for parsing
ANSIBLE_STDOUT_CALLBACK=json ansible-playbook site.yml

# Eller spara till fil
ansible-playbook site.yml --stdout-callback json > output.json
```

```json
{
  "plays": [{
    "play": {"name": "Configure servers"},
    "tasks": [{
      "task": {"name": "Install nginx"},
      "hosts": {
        "web1": {"changed": true}
      }
    }]
  }],
  "stats": {
    "web1": {"changed": 5, "ok": 10, "failures": 0}
  }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Custom Callback Plugin

```python
# callback_plugins/notify_slack.py
from ansible.plugins.callback import CallbackBase
import requests

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'notify_slack'
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self):
        super().__init__()
        self.webhook_url = None

    def set_options(self, **kwargs):
        super().set_options(**kwargs)
        self.webhook_url = self.get_option('webhook_url')

    def v2_playbook_on_stats(self, stats):
        hosts = stats.processed.keys()
        summary = {'ok': 0, 'failures': 0}

        for host in hosts:
            s = stats.summarize(host)
            summary['ok'] += s['ok']
            summary['failures'] += s['failures']

        color = 'good' if summary['failures'] == 0 else 'danger'
        payload = {
            'attachments': [{
                'color': color,
                'title': 'Ansible Playbook',
                'text': f"OK: {summary['ok']}, Failures: {summary['failures']}"
            }]
        }

        if self.webhook_url:
            requests.post(self.webhook_url, json=payload)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Aktivera Custom Callback

```ini
# ansible.cfg
[defaults]
callback_plugins = ./callback_plugins
callbacks_enabled = notify_slack

[callback_notify_slack]
webhook_url = https://hooks.slack.com/services/XXX/YYY
```

```bash
# Eller med environment
export SLACK_WEBHOOK_URL=https://hooks.slack.com/...
ansible-playbook site.yml
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Callback Events

| Event | Metod | Nar |
|-------|-------|-----|
| Playbook start | `v2_playbook_on_start` | Borjan |
| Play start | `v2_playbook_on_play_start` | Varje play |
| Task start | `v2_playbook_on_task_start` | Varje task |
| Success | `v2_runner_on_ok` | Task OK |
| Failure | `v2_runner_on_failed` | Task misslyckades |
| Stats | `v2_playbook_on_stats` | Slut med statistik |

```python
class CallbackModule(CallbackBase):
    def v2_playbook_on_start(self, playbook):
        # Playbook startar
        pass

    def v2_runner_on_ok(self, result):
        # Task lyckades
        host = result._host.name
        task = result._task.name

    def v2_runner_on_failed(self, result, ignore_errors=False):
        # Task misslyckades
        pass
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Beskrivning |
|---------|-------------|
| stdout_callback | Andrar output-format (yaml, json) |
| callbacks_enabled | Aktivera multipla callbacks |
| profile_tasks | Performance debugging |
| Custom callbacks | Integration med externa system |
| Events | Haka pa playbook/task events |

**Kom ihag:**
- profile_tasks visar var tiden gar
- JSON callback for maskinlasbar output
- Custom callbacks for Slack/Teams notifikationer
- Flera callbacks kan vara aktiva samtidigt
- stdout_callback kan bara vara en at gangen
''',
        },
        {
            "title": "Ansible for Windows",
            "slug": "ansible-windows",
            "difficulty": "advanced",
            "content": '''
# Ansible for Windows

Ansible ar inte bara for Linux - Windows-hantering ar en kritisk del av enterprise automation. Hybrid-miljoer med bade Linux och Windows ar standard idag, och Ansible ger dig ett enhetligt satt att automatisera bada plattformar med samma playbooks och workflows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Windows Connection Architecture

```
+-------------------+       WinRM/HTTPS        +-------------------+
|  Control Node     |------------------------->|  Windows Host     |
|  (Linux)          |       Port 5986          |                   |
|                   |                          |                   |
|  ansible-playbook |       NTLM/Kerberos      |  PowerShell       |
|  win_* modules    |       Authentication     |  Execution        |
+-------------------+                          +-------------------+
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Viktiga Windows Modules

| Module | Anvandning |
|--------|------------|
| win_feature | Installera Windows features/roles |
| win_service | Hantera Windows services |
| win_package | Installera MSI/EXE paket |
| win_chocolatey | Pakethantering via Chocolatey |
| win_copy | Kopiera filer till Windows |
| win_template | Jinja2 templates till Windows |
| win_regedit | Hantera Windows Registry |
| win_shell | Kora PowerShell kommandon |
| win_updates | Windows Update hantering |
| win_domain_membership | Join/leave AD domain |
| win_iis_* | IIS webbserver hantering |
| win_dsc | PowerShell DSC integration |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| WinRM | Windows motsvarighet till SSH, port 5986 for HTTPS |
| win_* modules | Windows-specifik automation med PowerShell backend |
| Chocolatey | Pakethantering for Windows via win_chocolatey |
| DSC integration | PowerShell Desired State Configuration via win_dsc |
| AD automation | Domain join, users, groups med dedikerade modules |
| IIS hantering | win_iis_website, win_iis_webapppool for webbservrar |

**Kom ihag:**
- WinRM maste konfigureras pa Windows-hosten forst
- HTTPS (port 5986) ar rekommenderat for produktion
- NTLM eller Kerberos for authentication
- win_* modules motsvarar Linux modules men for Windows
- pywinrm maste installeras pa control node
''',
        },
        {
            "title": "Ansible AWX",
            "slug": "ansible-awx",
            "difficulty": "advanced",
            "content": '''
# Ansible AWX

AWX ar den oppna kallkods-versionen av Red Hat Ansible Tower - en kraftfull plattform som ger dig visuell hantering, schemaläggning och API-access for dina Ansible automationer. For team och enterprise ar AWX det som gor Ansible till en skalbar automation platform.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## AWX Architecture Overview

```
+------------------+     +------------------+     +------------------+
|   Web Browser    |     |   CI/CD System   |     |   Custom Apps    |
+--------+---------+     +--------+---------+     +--------+---------+
         |                        |                        |
         v                        v                        v
+--------+------------------------+------------------------+---------+
|                           AWX REST API                             |
+--------------------------------------------------------------------+
|  Job Templates  |  Workflows  |  Inventories  |  Credentials       |
+--------------------------------------------------------------------+
|                       Execution Engine                             |
|    +------------+  +------------+  +------------+                  |
|    | ansible-   |  | ansible-   |  | ansible-   |                  |
|    | playbook   |  | playbook   |  | playbook   |                  |
|    +------------+  +------------+  +------------+                  |
+--------------------------------------------------------------------+
         |                    |                     |
         v                    v                     v
    +---------+         +---------+          +---------+
    |  Linux  |         | Windows |          |  Cloud  |
    |  Hosts  |         |  Hosts  |          |   VMs   |
    +---------+         +---------+          +---------+
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## AWX Komponenter

| Komponent | Beskrivning |
|-----------|-------------|
| Job Templates | Forutdefinierade playbook-korningar med parametrar |
| Workflows | Koppla ihop flera job templates i sekvens/parallell |
| Inventories | Dynamisk eller statisk host-hantering |
| Credentials | Sakert lagrade nycklar och losenord |
| Projects | Git repos med playbooks synkade automatiskt |
| Schedules | Cron-liknande schemaläggning av jobs |
| RBAC | Role-based access control for team |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| AWX | Open source version av Ansible Tower med Web UI |
| Job Templates | Forutdefinierade playbook-korningar med parametrar |
| Workflows | Koppla ihop jobs i sekvens eller parallellt |
| REST API | Programmatisk access for CI/CD integration |
| Inventory Sources | Dynamisk sync fran AWS, GCP, VMware etc |
| Credentials | Centraliserad och sakert lagrad credential management |

**Kom ihag:**
- Docker eller Kubernetes for AWX installation
- awx.awx collection for programmatisk hantering
- REST API for integration med CI/CD pipelines
- Inventory sources synkar automatiskt vid job launch
- RBAC ger granular access control for team
''',
        },
        {
            "title": "Security Best Practices",
            "slug": "security-best-practices",
            "difficulty": "advanced",
            "content": '''
# Security Best Practices

Med stor makt kommer stort ansvar - Ansible har tillgang till alla servrar och hanterar kansliga credentials. Sakerhetsmisstag kan fa katastrofala konsekvenser. Denna nod gar igenom hur du bygger in sakerhet fran borjan och foljer best practices for enterprise-automation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Security Checklist

```
+------------------------------------------------------------------+
|                    ANSIBLE SECURITY LAYERS                       |
+------------------------------------------------------------------+
|  1. Credentials     | Vault, no plaintext, rotate regularly     |
|  2. SSH Hardening   | Key-only auth, dedicated users            |
|  3. Least Privilege | Minimal sudo, specific commands           |
|  4. Audit Logging   | Track all changes, who did what           |
|  5. Secret Scanning | CI/CD checks for exposed secrets          |
|  6. Network         | Bastion hosts, encrypted connections      |
+------------------------------------------------------------------+
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Security Practices Oversikt

| Omrade | Best Practice |
|--------|---------------|
| Vault | Separata losenord per miljo (prod/dev/staging) |
| SSH | Key-only auth, dedicated deploy user |
| Become | Begransad sudo, specifika kommandon |
| Logging | no_log: true for kanslig data |
| Audit | Custom callbacks for compliance |
| CI/CD | Secret scanning i pipelines |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Vault | Separata losenord per miljo, krypterade secrets |
| no_log | Dolj kanslig output i ansible logs |
| Deploy user | Dedikerad anvandare med minimal sudo-rattigheter |
| Audit callback | Custom plugin for compliance logging |
| Secret scanning | Automatisk check i CI/CD for lakta secrets |
| SSH hardening | Key-only auth, disable root login |

**Kom ihag:**
- Aldrig credentials i plaintext, alltid Vault
- no_log: true pa alla tasks med kanslig data
- Dedicerad deploy user med begransad sudo
- Audit trail ar krav for enterprise compliance
- Secret scanning i varje pull request
''',
        },
        {
            "title": "Enterprise Patterns",
            "slug": "enterprise-patterns",
            "difficulty": "advanced",
            "content": '''
# Enterprise Patterns

Nar Ansible skalar fran ett litet team till enterprise med tusentals servrar och multipla team kravs helt nya patterns. Denna nod gar igenom beproade metoder for repository-struktur, multi-team workflows, self-service automation och compliance - allt som kravs for att Ansible ska fungera i stor skala.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Enterprise Patterns Overview

```
+--------------------------------------------------------------------+
|                   ENTERPRISE ANSIBLE ARCHITECTURE                  |
+--------------------------------------------------------------------+
|                                                                    |
|  +----------------+     +----------------+     +----------------+  |
|  |  Dev Team      |     |  SRE Team      |     |  Security Team |  |
|  |  /staging/     |     |  /production/  |     |  /security/    |  |
|  +-------+--------+     +-------+--------+     +-------+--------+  |
|          |                      |                      |           |
|          v                      v                      v           |
|  +-------+----------------------+----------------------+--------+  |
|  |              Git Repository (CODEOWNERS)                     |  |
|  |  /roles/  /playbooks/  /inventory/  /collections/            |  |
|  +-------+----------------------+----------------------+--------+  |
|          |                      |                      |           |
|          v                      v                      v           |
|  +-------+--------+     +-------+--------+     +-------+--------+  |
|  |  AWX Staging   |     |  AWX Prod      |     |  Compliance    |  |
|  |  Self-Service  |     |  Controlled    |     |  Automation    |  |
|  +----------------+     +----------------+     +----------------+  |
|                                                                    |
+--------------------------------------------------------------------+
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Enterprise Patterns Checklist

| Pattern | Beskrivning |
|---------|-------------|
| Monorepo | En repository for all automation med tydlig struktur |
| CODEOWNERS | Team-ansvar for specifika mappar kravs review |
| Self-Service | AWX surveys lar anvandare deploya utan CLI |
| Canary Deploy | Rulla ut gradvis: 1 server, 25%, sedan 100% |
| Compliance | Automatiska audits och rapporter som kod |
| GitOps | Deklarativ automation synkad fran Git |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| Monorepo | En repo for all automation med roles/playbooks/inventory |
| CODEOWNERS | GitHub/GitLab file som kraver team-review for specifika mappar |
| Self-Service | AWX surveys lar anvandare deploya utan terminal |
| Canary | serial: [1, "25%", "100%"] for gradvis utrullning |
| Compliance | Automatiska CIS benchmark checks som playbooks |
| GitOps | ArgoCD + Kubernetes Job for kontinuerlig sync |

**Kom ihag:**
- Monorepo struktur med tydlig separation av concerns
- CODEOWNERS skapar automatisk review gate per team
- AWX surveys ger self-service for developers
- Canary deployments minimerar risk vid utrullning
- Compliance automation ar krav for enterprise
''',
        },
    ],
}
