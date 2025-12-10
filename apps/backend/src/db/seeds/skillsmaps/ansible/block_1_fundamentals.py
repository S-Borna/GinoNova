# =============================================================================
# BLOCK 1: ANSIBLE FUNDAMENTALS (Noder 1-4)
# =============================================================================

NODE_01_ANSIBLE_INTRO = {
    "node_id": 1,
    "title": "Ansible Introduktion",
    "slug": "ansible-intro",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "prerequisites": [],
    "content": r'''
# Ansible Introduktion

## Varför detta är kritiskt

> "Du har 50 servrar som behöver en säkerhetsuppdatering. NU. SSH:a in på varje? Nej. Med Ansible gör du det på 30 sekunder med ett kommando. Det är skillnaden mellan att jobba hårt och att jobba smart."

Tänk dig: Det är måndag morgon. En kritisk CVE har släppts. Din säkerhetsavdelning kräver att alla servrar patchas inom 2 timmar. Du har 200 servrar.

**Utan Ansible:**
- SSH till varje server manuellt
- Kör samma kommandon 200 gånger
- Hoppas du inte gör misstag
- 8+ timmar av monotont arbete

**Med Ansible:**
```bash
ansible all -m apt -a "name=openssl state=latest" --become
```
- Klart på 5 minuter
- Konsekvent på alla servrar
- Loggat och spårbart

---

## Vad är Ansible?

Ansible är ett **agentless configuration management och automation-verktyg** skapat av Michael DeHaan 2012 (nu ägt av Red Hat).

```
+-------------------------------------------------------------------------+
|                     ANSIBLE VS ANDRA VERKTYG                            |
+-------------------------------------------------------------------------+
|                                                                         |
|   ANSIBLE          PUPPET           CHEF            SALTSTACK           |
|   --------         ------           ----            ---------           |
|   Agentless        Agent            Agent           Agent/Agentless     |
|   Push-based       Pull-based       Pull-based      Push/Pull           |
|   YAML             DSL              Ruby DSL        YAML                |
|   SSH              HTTPS            HTTPS           ZeroMQ              |
|   Simple           Complex          Complex         Medium              |
|                                                                         |
+-------------------------------------------------------------------------+
```

### Ansibles Kärnkoncept

| Koncept | Beskrivning | Exempel |
|---------|-------------|---------|
| **Agentless** | Ingen mjukvara på målservrar | Bara SSH och Python |
| **Idempotent** | Samma resultat oavsett antal körningar | `state: present` |
| **Push-based** | Du initierar från control node | `ansible-playbook deploy.yml` |
| **YAML** | Human-readable syntax | Ingen DSL att lära sig |
| **Modules** | Färdiga byggblock | 3000+ inbyggda moduler |

---

## Arkitektur Deep Dive

```
+-------------------------------------------------------------------------+
|                         ANSIBLE ARKITEKTUR                              |
+-------------------------------------------------------------------------+
|                                                                         |
|  +-------------------------------------+                                |
|  |         CONTROL NODE                |                                |
|  |  +-----------------------------+    |                                |
|  |  |  ansible / ansible-playbook |    |                                |
|  |  +--------------+--------------+    |                                |
|  |                 |                   |                                |
|  |  +--------------+--------------+    |                                |
|  |  |      INVENTORY              |    |                                |
|  |  |  [webservers]               |    |                                |
|  |  |  web01.example.com          |    |                                |
|  |  |  web02.example.com          |    |                                |
|  |  +--------------+--------------+    |                                |
|  |                 |                   |                                |
|  |  +--------------+--------------+    |                                |
|  |  |      PLAYBOOKS              |    |                                |
|  |  |  - tasks                    |    |                                |
|  |  |  - handlers                 |    |                                |
|  |  |  - roles                    |    |                                |
|  |  +-----------------------------+    |                                |
|  +-----------------+-------------------+                                |
|                    |                                                    |
|                    | SSH (port 22)                                      |
|                    |                                                    |
|     +--------------+--------------+--------------+                      |
|     ▼              ▼              ▼              ▼                      |
|  +------+      +------+      +------+      +------+                     |
|  |web01 |      |web02 |      | db01 |      |cache |                     |
|  |      |      |      |      |      |      |      |                     |
|  |Python|      |Python|      |Python|      |Python|                     |
|  +------+      +------+      +------+      +------+                     |
|           MANAGED NODES (Ingen Ansible-agent!)                          |
|                                                                         |
+-------------------------------------------------------------------------+
```

### Krav på Control Node

| Komponent | Krav |
|-----------|------|
| OS | Linux, macOS, WSL (EJ native Windows) |
| Python | 3.8+ |
| SSH | OpenSSH client |
| Ansible | 2.9+ (rekommenderat: senaste) |

### Krav på Managed Nodes

| Komponent | Krav |
|-----------|------|
| SSH | sshd körande |
| Python | 2.7 eller 3.5+ (de flesta moduler) |
| Användare | SSH-access med sudo (för become) |

---

## Installation

### macOS

```bash
# Via Homebrew (rekommenderat)
brew install ansible

# Verifiera
ansible --version
# ansible [core 2.15.0]
#   python version = 3.11.4
```

### Ubuntu/Debian

```bash
# Via apt (äldre version)
sudo apt update
sudo apt install ansible

# Via PPA (senaste version)
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible
```

### RHEL/CentOS

```bash
# RHEL 8+
sudo dnf install ansible

# Med EPEL
sudo yum install epel-release
sudo yum install ansible
```

### Python pip (Alla plattformar)

```bash
# Skapa virtual environment (best practice)
python3 -m venv ~/.ansible-venv
source ~/.ansible-venv/bin/activate

# Installera
pip install ansible

# Eller specifik version
pip install ansible==2.15.0

# Med extra collections
pip install ansible[azure]  # För Azure-moduler
```

### Verifiering

```bash
# Version
ansible --version

# Hitta config
ansible --version | grep "config file"

# Lista installerade collections
ansible-galaxy collection list

# Testa lokal körning
ansible localhost -m ping
# localhost | SUCCESS => {
#     "changed": false,
#     "ping": "pong"
# }
```

---

## Konfiguration

### ansible.cfg

Ansible söker config i denna ordning:
1. `ANSIBLE_CONFIG` (environment variable)
2. `./ansible.cfg` (current directory)
3. `~/.ansible.cfg` (home directory)
4. `/etc/ansible/ansible.cfg` (global)

```ini
# ansible.cfg
[defaults]
inventory = ./inventory.ini
remote_user = ubuntu
host_key_checking = False
retry_files_enabled = False
stdout_callback = yaml

[privilege_escalation]
become = True
become_method = sudo
become_user = root
become_ask_pass = False

[ssh_connection]
pipelining = True
control_path = /tmp/ansible-ssh-%%h-%%p-%%r
```

### Viktiga Inställningar

| Setting | Default | Rekommenderat | Beskrivning |
|---------|---------|---------------|-------------|
| `host_key_checking` | True | False (dev) | SSH fingerprint check |
| `pipelining` | False | True | Snabbare exekvering |
| `forks` | 5 | 20-50 | Parallella connections |
| `timeout` | 10 | 30 | SSH timeout i sekunder |
| `retry_files_enabled` | True | False | Skapa .retry filer |

---

## Ditt Första Ansible-kommando

### Ad-hoc kommando

```bash
# Syntax
ansible <hosts> -i <inventory> -m <module> -a "<arguments>"

# Ping alla hosts i inventory
ansible all -i inventory.ini -m ping

# Kör shell-kommando
ansible webservers -i inventory.ini -m shell -a "uptime"

# Med inline inventory (notera kommat!)
ansible all -i "192.168.1.10," -m ping
```

### Praktiskt Exempel

```bash
# 1. Skapa inventory
cat > inventory.ini << 'EOF'
[local]
localhost ansible_connection=local
EOF

# 2. Testa ping
ansible local -i inventory.ini -m ping

# 3. Samla fakta
ansible local -i inventory.ini -m setup | head -50

# 4. Kör kommando
ansible local -i inventory.ini -m shell -a "df -h"
```

---

## Felsökning

### Vanliga Problem

| Problem | Orsak | Lösning |
|---------|-------|---------|
| `Permission denied` | SSH-nyckel saknas | `ssh-copy-id user@host` |
| `No hosts matched` | Fel inventory | Kolla `-i` flaggan |
| `Python not found` | Python saknas på target | Installera Python |
| `unreachable` | SSH-problem | Testa `ssh user@host` först |

### Debug-kommandon

```bash
# Verbose output (-v, -vv, -vvv, -vvvv)
ansible all -m ping -vvv

# Testa SSH manuellt
ssh -o BatchMode=yes user@host 'echo ok'

# Lista hosts i inventory
ansible-inventory -i inventory.ini --list

# Visa host-variabler
ansible-inventory -i inventory.ini --host web01
```

---

## Praktisk Övning

### Övning 1: Sätt upp din miljö

```bash
# 1. Installera Ansible
pip install ansible

# 2. Skapa projektstruktur
mkdir -p ~/ansible-lab
cd ~/ansible-lab

# 3. Skapa ansible.cfg
cat > ansible.cfg << 'EOF'
[defaults]
inventory = inventory.ini
host_key_checking = False
EOF

# 4. Skapa inventory
cat > inventory.ini << 'EOF'
[local]
localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3
EOF

# 5. Testa
ansible local -m ping
ansible local -m setup -a "filter=ansible_distribution*"
ansible local -m shell -a "whoami && pwd"
```

### Övning 2: Multi-host Setup (om du har fler maskiner)

```bash
# inventory.ini
[webservers]
web01 ansible_host=192.168.1.10
web02 ansible_host=192.168.1.11

[databases]
db01 ansible_host=192.168.1.20

[all:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/id_rsa
```

---

## Sammanfattning

| Koncept | Vad du lärt dig |
|---------|-----------------|
| Agentless | Ansible behöver ingen agent på målservrar |
| SSH-baserat | Använder standard SSH för kommunikation |
| Idempotent | Säkert att köra samma sak flera gånger |
| Control Node | Där Ansible körs (din maskin) |
| Managed Nodes | Servrar du hanterar |
| Inventory | Lista över dina servrar |
| Modules | Byggblock för tasks (ping, shell, apt, etc) |

---

## Nästa Steg

Du kan nu installera och konfigurera Ansible. I nästa modul lär du dig **Inventory** — hur du organiserar och grupperar dina servrar för effektiv hantering.

> 💡 **Pro Tip:** Skapa alltid en `ansible.cfg` i ditt projektroot. Det gör dina kommandon kortare och projektet portabelt.
''',
}

NODE_02_INVENTORY = {
    "node_id": 2,
    "title": "Inventory Hantering",
    "slug": "inventory",
    "estimated_minutes": 60,
    "xp_reward": 120,
    "prerequisites": [1],
    "content": r'''
# Inventory Hantering

## Varför detta är kritiskt

> "Din inventory är kartan över din infrastruktur. Med fel karta hamnar du fel. Med rätt karta kan du navigera var som helst."

Scenario: Du är ansvarig för 3 miljöer - development, staging, production. Varje miljö har webservrar, databaser, och cache-servrar. Totalt 45 servrar. Utan strukturerad inventory blir det kaos.

**Med smart inventory:**
```bash
# Patcha bara produktion-webbservrar
ansible prod_webservers -m apt -a "name=nginx state=latest"

# Kör på alla databaser utom prod
ansible 'databases:!prod_databases' -m shell -a "pg_dump..."
```

---

## Inventory Koncept

```
+-------------------------------------------------------------------------+
|                        INVENTORY HIERARCHY                              |
+-------------------------------------------------------------------------+
|                                                                         |
|                              ALL                                        |
|                               |                                         |
|         +---------------------+---------------------+                   |
|         |                     |                     |                   |
|    +----+----+          +----+----+          +----+----+               |
|    |   DEV   |          | STAGING |          |  PROD   |               |
|    +----+----+          +----+----+          +----+----+               |
|         |                    |                    |                    |
|    +----+----+          +----+----+          +----+----+               |
|    |    |    |          |    |    |          |    |    |               |
|   web  db  cache       web  db  cache       web  db  cache             |
|                                                                         |
|  Grupper kan ha children (nested groups)                               |
|  Hosts kan vara i flera grupper                                        |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## INI Format (Klassiskt)

```ini
# inventory.ini - Fullständigt exempel

# ==========================================
# INDIVIDUAL HOSTS
# ==========================================
jumpbox ansible_host=10.0.0.1 ansible_user=admin

# ==========================================
# WEBSERVERS
# ==========================================
[webservers]
web01.example.com
web02.example.com
web03.example.com ansible_host=192.168.1.13

# Med ranges (web01 till web10)
web[01:10].example.com

# Alfabetiska ranges
web-[a:f].example.com

# ==========================================
# DATABASES
# ==========================================
[databases]
db01.example.com ansible_port=2222
db02.example.com

# ==========================================
# CACHES
# ==========================================
[caches]
redis01 ansible_host=192.168.1.30
redis02 ansible_host=192.168.1.31

# ==========================================
# GRUPPVARIABLER
# ==========================================
[webservers:vars]
ansible_user=www-data
http_port=80
max_connections=1000

[databases:vars]
ansible_user=postgres
db_port=5432

# ==========================================
# NESTED GROUPS (Children)
# ==========================================
[production:children]
webservers
databases
caches

[production:vars]
env=production
monitoring=enabled

# ==========================================
# ALLA HOSTS - GLOBALA VARIABLER
# ==========================================
[all:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/id_rsa
ansible_python_interpreter=/usr/bin/python3
```

---

## YAML Format (Rekommenderat)

```yaml
# inventory.yml
all:
  vars:
    ansible_user: ubuntu
    ansible_python_interpreter: /usr/bin/python3

  children:
    # ==========================================
    # PRODUKTION
    # ==========================================
    production:
      vars:
        env: production
        monitoring: enabled

      children:
        prod_webservers:
          hosts:
            web01:
              ansible_host: 10.0.1.10
              nginx_worker_processes: 4
            web02:
              ansible_host: 10.0.1.11
              nginx_worker_processes: 4
            web03:
              ansible_host: 10.0.1.12
              nginx_worker_processes: 8  # Mer kraft

        prod_databases:
          hosts:
            db01:
              ansible_host: 10.0.1.20
              role: primary
              max_connections: 500
            db02:
              ansible_host: 10.0.1.21
              role: replica
              max_connections: 200

        prod_caches:
          hosts:
            redis01:
              ansible_host: 10.0.1.30
              redis_maxmemory: 4gb

    # ==========================================
    # STAGING
    # ==========================================
    staging:
      vars:
        env: staging
        monitoring: disabled

      children:
        stag_webservers:
          hosts:
            stag-web01:
              ansible_host: 10.0.2.10
        stag_databases:
          hosts:
            stag-db01:
              ansible_host: 10.0.2.20

    # ==========================================
    # SPECIAL GROUPS
    # ==========================================
    loadbalancers:
      hosts:
        lb01:
          ansible_host: 10.0.0.5
          vip: 10.0.0.100
```

---

## Host Patterns

| Pattern | Beskrivning | Exempel |
|---------|-------------|---------|
| `all` | Alla hosts | `ansible all -m ping` |
| `*` | Wildcard | `ansible "*.example.com" -m ping` |
| `group1:group2` | Union (OR) | `ansible "web:db" -m ping` |
| `group1:&group2` | Intersection (AND) | `ansible "prod:&webservers"` |
| `group1:!group2` | Exclude (NOT) | `ansible "all:!databases"` |
| `~regex` | Regex match | `ansible "~web[0-9]+" -m ping` |
| `host1,host2` | Explicit hosts | `ansible "web01,web02" -m ping` |

### Kombinerade Patterns

```bash
# Alla webservrar i produktion
ansible 'production:&webservers' -m ping

# Alla hosts utom databaser och caches
ansible 'all:!databases:!caches' -m ping

# Produktion webservrar ELLER staging databaser
ansible 'prod_webservers:stag_databases' -m ping

# Regex: alla som börjar med "web"
ansible '~^web.*' -m ping

# Subscript: första 5 webservrarna
ansible 'webservers[0:4]' -m ping
```

---

## Inventory Variables

### Var definieras variabler?

```
+-------------------------------------------------------------------------+
|                    VARIABEL PRECEDENCE (lägst -> högst)                  |
+-------------------------------------------------------------------------+
|                                                                         |
|  1. all group_vars                     group_vars/all.yml               |
|  2. parent group_vars                  group_vars/production.yml        |
|  3. child group_vars                   group_vars/webservers.yml        |
|  4. host_vars                          host_vars/web01.yml              |
|  5. inventory file vars                [webservers:vars]                |
|  6. play vars                          vars: i playbook                 |
|  7. include_vars                       dynamiskt laddade                |
|  8. set_facts / registered vars        runtime                          |
|  9. extra vars (-e)                    ansible-playbook -e "var=val"    |
|                                                                         |
|  HÖGRE NUMMER = ÖVERSKRIVER LÄGRE                                       |
|                                                                         |
+-------------------------------------------------------------------------+
```

### group_vars och host_vars

```bash
# Projektstruktur
ansible-project/
+-- inventory.yml
+-- playbook.yml
+-- group_vars/
|   +-- all.yml              # Gäller ALLA hosts
|   +-- production.yml       # Gäller production-gruppen
|   +-- webservers.yml       # Gäller webservers-gruppen
+-- host_vars/
    +-- web01.yml            # Specifikt för web01
    +-- db01.yml             # Specifikt för db01
```

```yaml
# group_vars/all.yml
---
ntp_server: time.google.com
dns_servers:
  - 8.8.8.8
  - 8.8.4.4
ssh_port: 22

# group_vars/production.yml
---
env: production
monitoring_enabled: true
log_level: warn

# group_vars/webservers.yml
---
nginx_worker_processes: auto
nginx_worker_connections: 1024
ssl_certificate: /etc/ssl/certs/prod.crt

# host_vars/web01.yml
---
nginx_worker_processes: 8  # Överskriver webservers.yml
backup_enabled: true
```

---

## Dynamisk Inventory

### Varför dynamisk inventory?

| Statisk | Dynamisk |
|---------|----------|
| Manuellt underhållen fil | Auto-genererad från källa |
| Bra för < 50 hosts | Skalbar till tusentals |
| Risk för att bli utdaterad | Alltid aktuell |
| Enkel setup | Kräver script/plugin |

### AWS EC2 Exempel

```yaml
# aws_ec2.yml (inventory plugin)
plugin: amazon.aws.aws_ec2
regions:
  - eu-north-1
  - eu-west-1

filters:
  instance-state-name: running
  "tag:Environment": production

keyed_groups:
  - key: tags.Environment
    prefix: env
  - key: instance_type
    prefix: type
  - key: placement.availability_zone
    prefix: az

compose:
  ansible_host: public_ip_address
```

```bash
# Använd dynamisk inventory
ansible-inventory -i aws_ec2.yml --graph

# Kör playbook
ansible-playbook -i aws_ec2.yml deploy.yml
```

### Custom Script

```python
#!/usr/bin/env python3
# inventory.py

import json

def main():
    inventory = {
        "webservers": {
            "hosts": ["web01", "web02"],
            "vars": {
                "http_port": 80
            }
        },
        "_meta": {
            "hostvars": {
                "web01": {"ansible_host": "192.168.1.10"},
                "web02": {"ansible_host": "192.168.1.11"}
            }
        }
    }
    print(json.dumps(inventory))

if __name__ == "__main__":
    main()
```

```bash
chmod +x inventory.py
ansible-inventory -i inventory.py --list
```

---

## Felsökning

### Debug-kommandon

```bash
# Lista alla hosts
ansible-inventory -i inventory.yml --list

# Grafisk vy
ansible-inventory -i inventory.yml --graph

# Visa specifik host
ansible-inventory -i inventory.yml --host web01

# Verifiera syntax
ansible-inventory -i inventory.yml --list > /dev/null && echo "OK"

# Testa pattern
ansible "webservers:&production" --list-hosts
```

### Vanliga Problem

| Problem | Orsak | Lösning |
|---------|-------|---------|
| `No hosts matched` | Fel pattern/gruppnamn | Kör `--list-hosts` |
| Variable undefined | Fel i precedence | Kolla var variabeln definieras |
| Duplicate host | Samma host i flera filer | Konsolidera inventory |
| YAML parse error | Indenteringsfel | Validera med `yamllint` |

---

## Praktisk Övning

### Övning: Multi-Environment Inventory

```bash
# 1. Skapa projektstruktur
mkdir -p ~/ansible-inventory-lab/{group_vars,host_vars}
cd ~/ansible-inventory-lab

# 2. Skapa inventory
cat > inventory.yml << 'EOF'
all:
  children:
    production:
      children:
        prod_web:
          hosts:
            prod-web01:
              ansible_host: localhost
              ansible_connection: local
    staging:
      children:
        stag_web:
          hosts:
            stag-web01:
              ansible_host: localhost
              ansible_connection: local
EOF

# 3. Skapa group_vars
cat > group_vars/all.yml << 'EOF'
company: DevOpsHub
deploy_user: deploy
EOF

cat > group_vars/production.yml << 'EOF'
env: production
debug_mode: false
EOF

cat > group_vars/staging.yml << 'EOF'
env: staging
debug_mode: true
EOF

# 4. Testa
ansible-inventory -i inventory.yml --graph
ansible production -i inventory.yml --list-hosts
ansible staging -i inventory.yml -m debug -a "var=env"
```

---

## Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| INI vs YAML | Båda fungerar, YAML är mer flexibelt |
| Groups | Organisera hosts logiskt |
| Children | Nested groups för hierarki |
| Patterns | Kraftfulla sätt att välja hosts |
| group_vars | Variabler per grupp |
| host_vars | Variabler per host |
| Dynamisk | Auto-genererad från cloud/CMDB |

---

## Nästa Steg

Nu kan du organisera din infrastruktur. Nästa modul: **Ad-hoc Commands** — köra snabba one-liners mot dina servrar.
''',
}

NODE_03_ADHOC_COMMANDS = {
    "node_id": 3,
    "title": "Ad-hoc Commands",
    "slug": "adhoc-commands",
    "estimated_minutes": 60,
    "xp_reward": 110,
    "prerequisites": [2],
    "content": r'''
# Ad-hoc Commands

## Varför detta är kritiskt

> "Du får ett samtal kl 03:00. 'Alla webservrar är nere!' Med ad-hoc commands kan du diagnostisera och fixa problemet på minuter — utan att öppna en enda fil."

Ad-hoc commands är Ansible's **emergency toolkit**. När du inte har tid att skriva en playbook, när du behöver snabb information från 100 servrar, när du måste agera NU.

**Verkliga scenarier:**
- "Vilka servrar har mindre än 10% diskutrymme kvar?"
- "Starta om nginx på alla webservrar"
- "Vad är uptimen på alla databaser?"
- "Installera en critical security patch på 50 servrar — nu"

---

## Syntax och Struktur

```
+-------------------------------------------------------------------------+
|                       AD-HOC COMMAND ANATOMY                            |
+-------------------------------------------------------------------------+
|                                                                         |
|  ansible  webservers  -i inventory.yml  -m apt  -a "name=nginx"  -b    |
|     |         |              |            |           |            |    |
|     |         |              |            |           |            |    |
|  Command   Pattern       Inventory     Module    Arguments      Become  |
|                                                                         |
|  REQUIRED: ansible <pattern> -m <module>                               |
|  OPTIONAL: -i, -a, -b, -u, -f, -v                                     |
|                                                                         |
+-------------------------------------------------------------------------+
```

### Alla Flaggor

| Flagga | Lång form | Beskrivning | Exempel |
|--------|-----------|-------------|---------|
| `-i` | `--inventory` | Inventory-fil | `-i prod.yml` |
| `-m` | `--module-name` | Modul att köra | `-m ping` |
| `-a` | `--args` | Modul-argument | `-a "name=nginx"` |
| `-b` | `--become` | Kör som root (sudo) | `-b` |
| `-K` | `--ask-become-pass` | Fråga efter sudo-lösen | `-K` |
| `-u` | `--user` | SSH-användare | `-u ubuntu` |
| `-k` | `--ask-pass` | Fråga efter SSH-lösen | `-k` |
| `-f` | `--forks` | Parallelism | `-f 20` |
| `-v` | `--verbose` | Debug output | `-vvv` |
| `-C` | `--check` | Dry-run | `-C` |
| `-D` | `--diff` | Visa ändringar | `-D` |
| `-e` | `--extra-vars` | Extra variabler | `-e "env=prod"` |
| `-l` | `--limit` | Begränsa hosts | `-l web01` |
| `-t` | `--timeout` | SSH timeout | `-t 30` |

---

## Essential Modules

### 1. Connectivity & Info

```bash
# Testa anslutning
ansible all -m ping

# Samla ALLA fakta om hosts
ansible webservers -m setup

# Filtrera specifika fakta
ansible webservers -m setup -a "filter=ansible_distribution*"
ansible webservers -m setup -a "filter=ansible_memory_mb"
ansible webservers -m setup -a "filter=ansible_processor*"

# Visa enbart IPv4-adresser
ansible all -m setup -a "filter=ansible_default_ipv4"
```

### 2. Shell & Command

```bash
# command - SÄKRARE, ingen shell-expansion
ansible webservers -m command -a "uptime"
ansible webservers -m command -a "df -h"
ansible webservers -m command -a "free -m"

# shell - full shell med pipes, redirects etc
ansible webservers -m shell -a "ps aux | grep nginx | wc -l"
ansible webservers -m shell -a "cat /var/log/nginx/error.log | tail -20"
ansible webservers -m shell -a "du -sh /var/log/* | sort -h | tail -10"

# raw - ingen Python krävs på target
ansible webservers -m raw -a "cat /etc/os-release"
```

**Command vs Shell:**

| Aspekt | command | shell |
|--------|---------|-------|
| Shell expansion | Nej | Ja |
| Pipes | Nej | Ja |
| Redirects | Nej | Ja |
| Säkerhet | Högre | Lägre |
| Environment vars | Begränsad | Full |

### 3. Package Management

```bash
# APT (Debian/Ubuntu)
ansible webservers -m apt -a "name=nginx state=present" -b
ansible webservers -m apt -a "name=nginx state=latest" -b
ansible webservers -m apt -a "name=nginx state=absent" -b
ansible webservers -m apt -a "update_cache=yes" -b
ansible webservers -m apt -a "upgrade=dist" -b

# YUM/DNF (RHEL/CentOS)
ansible webservers -m yum -a "name=httpd state=present" -b
ansible webservers -m dnf -a "name=httpd state=latest" -b

# Package (auto-detect)
ansible webservers -m package -a "name=git state=present" -b

# Pip (Python)
ansible webservers -m pip -a "name=flask state=present"
ansible webservers -m pip -a "name=flask version=2.0.0"
```

### 4. Service Management

```bash
# Systemd
ansible webservers -m systemd -a "name=nginx state=started" -b
ansible webservers -m systemd -a "name=nginx state=stopped" -b
ansible webservers -m systemd -a "name=nginx state=restarted" -b
ansible webservers -m systemd -a "name=nginx enabled=yes" -b
ansible webservers -m systemd -a "daemon_reload=yes" -b

# Service (generic)
ansible webservers -m service -a "name=nginx state=reloaded" -b

# Visa status
ansible webservers -m shell -a "systemctl status nginx" -b
```

### 5. File Operations

```bash
# Kopiera fil
ansible webservers -m copy -a "src=/local/file.txt dest=/remote/file.txt"
ansible webservers -m copy -a "src=/local/file.txt dest=/etc/app/config mode=0644 owner=root" -b

# Kopiera innehåll direkt
ansible webservers -m copy -a "content='Hello World' dest=/tmp/hello.txt"

# Skapa directory
ansible webservers -m file -a "path=/opt/myapp state=directory mode=0755" -b

# Skapa symlink
ansible webservers -m file -a "src=/opt/app/current dest=/opt/app/latest state=link"

# Ta bort fil/directory
ansible webservers -m file -a "path=/tmp/old state=absent"

# Ändra permissions
ansible webservers -m file -a "path=/var/log/app mode=0640 owner=app group=app" -b

# Template
ansible webservers -m template -a "src=nginx.conf.j2 dest=/etc/nginx/nginx.conf" -b
```

### 6. User & Group Management

```bash
# Skapa användare
ansible all -m user -a "name=deploy state=present shell=/bin/bash" -b

# Med SSH-nyckel
ansible all -m authorized_key -a "user=deploy key='ssh-rsa AAAA...'" -b

# Med grupp
ansible all -m user -a "name=deploy groups=sudo,docker append=yes" -b

# Skapa grupp
ansible all -m group -a "name=developers state=present" -b

# Ta bort användare
ansible all -m user -a "name=olduser state=absent remove=yes" -b
```

---

## Privilege Escalation

```
+-------------------------------------------------------------------------+
|                     PRIVILEGE ESCALATION FLOW                           |
+-------------------------------------------------------------------------+
|                                                                         |
|  SSH Login (ubuntu)                                                     |
|       |                                                                 |
|       |  --become                                                       |
|       ▼                                                                 |
|  sudo su (root)     <- default become_method                            |
|       |                                                                 |
|       |  --become-user=postgres                                         |
|       ▼                                                                 |
|  sudo -u postgres   <- specifik användare                               |
|                                                                         |
+-------------------------------------------------------------------------+
```

```bash
# Som root
ansible webservers -m apt -a "name=nginx state=present" -b

# Som specifik användare
ansible databases -m shell -a "psql -c 'SELECT version();'" -b --become-user=postgres

# Med sudo-lösenord
ansible webservers -m apt -a "name=nginx state=present" -b -K

# Olika become_method
ansible webservers -m command -a "id" --become --become-method=su
```

---

## Parallelism & Performance

```bash
# Default: 5 parallella hosts
ansible all -m ping

# Öka till 20 parallella
ansible all -m ping -f 20

# En i taget (för riskabla operationer)
ansible webservers -m service -a "name=app state=restarted" -f 1 -b

# Med procent (30% av hosts åt gången)
# Kräver playbook, men bra att veta
```

**Rekommendationer:**

| Scenario | Forks |
|----------|-------|
| Ping/status check | 50-100 |
| Paketinstallation | 10-20 |
| Service restart | 1-5 |
| Reboot | 1 |
| Säkerhetsuppdatering | 20-50 |

---

## Practical Scenarios

### Scenario 1: Emergency Diagnostics

```bash
# Kl 03:00 - "Allt är långsamt!"

# 1. Kolla load average
ansible all -m shell -a "uptime" -f 50

# 2. Kolla diskutrymme
ansible all -m shell -a "df -h | grep -E '^/dev'" -f 50

# 3. Kolla minne
ansible all -m shell -a "free -m | grep Mem" -f 50

# 4. Hitta stora logfiler
ansible all -m shell -a "find /var/log -size +100M -type f 2>/dev/null" -f 50 -b

# 5. Kolla processer
ansible all -m shell -a "ps aux --sort=-%mem | head -10" -f 50
```

### Scenario 2: Mass Update

```bash
# CVE-2024-XXXX - Critical OpenSSL vulnerability

# 1. Kolla nuvarande version
ansible all -m shell -a "openssl version" -f 50

# 2. Update cache
ansible all -m apt -a "update_cache=yes" -f 20 -b

# 3. Installera patch
ansible all -m apt -a "name=openssl state=latest" -f 20 -b

# 4. Verifiera
ansible all -m shell -a "openssl version" -f 50
```

### Scenario 3: User Management

```bash
# Ny utvecklare börjar

# 1. Skapa användare på alla servrar
ansible all -m user -a "name=newdev shell=/bin/bash createhome=yes" -b

# 2. Lägg till SSH-nyckel
ansible all -m authorized_key -a "user=newdev key='ssh-rsa AAAA...'" -b

# 3. Lägg till i grupper
ansible all -m user -a "name=newdev groups=developers,docker append=yes" -b

# 4. Verifiera
ansible all -m shell -a "id newdev"
```

---

## Felsökning

### Debug Levels

```bash
-v      # Basic
-vv     # Mer detaljer
-vvv    # SSH debugging
-vvvv   # Full connection debug
```

### Vanliga Problem

| Problem | Kommando | Lösning |
|---------|----------|---------|
| SSH timeout | `-t 30` | Öka timeout |
| Permission denied | `-b -K` | Använd become + lösen |
| Module not found | `ansible-doc -l \| grep X` | Kolla modulnamn |
| Host unreachable | `ansible host -m ping -vvv` | Debug SSH |

---

## Praktisk Övning

```bash
# 1. Setup
mkdir ~/adhoc-lab && cd ~/adhoc-lab

cat > inventory.ini << 'EOF'
[local]
localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3
EOF

# 2. Basic tests
ansible local -m ping
ansible local -m setup -a "filter=ansible_distribution*"

# 3. Shell vs Command
ansible local -m command -a "echo hello"
ansible local -m shell -a "echo $HOME"  # Shell expansion

# 4. File operations
ansible local -m file -a "path=/tmp/test_dir state=directory mode=0755"
ansible local -m copy -a "content='Ansible test' dest=/tmp/test_file.txt"
ansible local -m file -a "path=/tmp/test_dir state=absent"

# 5. System info
ansible local -m shell -a "df -h"
ansible local -m shell -a "free -m"
ansible local -m shell -a "uptime"
```

---

## Sammanfattning

| Modul | Användning |
|-------|------------|
| `ping` | Connectivity test |
| `setup` | Samla fakta |
| `command` | Säkra kommandon |
| `shell` | Kommandon med shell |
| `copy` | Kopiera filer |
| `file` | Skapa/ta bort filer |
| `apt/yum` | Pakethantering |
| `service/systemd` | Tjänsthantering |
| `user` | Användarhantering |

---

## Nästa Steg

Nu kan du köra snabba operationer på dina servrar. Nästa modul: **YAML & Playbook Basics** — strukturerade, repeterbar automation.
''',
}

NODE_04_YAML_BASICS = {
    "node_id": 4,
    "title": "YAML & Playbook Basics",
    "slug": "yaml-basics",
    "estimated_minutes": 60,
    "xp_reward": 125,
    "prerequisites": [3],
    "content": r'''
# YAML & Playbook Basics

## Varför detta är kritiskt

> "Ad-hoc commands är för akutlägen. Playbooks är för allt annat. En playbook är skillnaden mellan att göra något en gång och att göra det på rätt sätt för alltid."

Tänk dig: Du har manuellt konfigurerat din webserver perfekt. Två månader senare kraschar servern. Kan du återskapa samma setup? Med en playbook: ja, på 5 minuter. Utan: timmar av trial and error.

**Playbooks ger dig:**
- Dokumentation av din infrastruktur
- Repeterbarhet - samma resultat varje gång
- Versionshantering - spåra ändringar i Git
- Delbarhet - teamet kan använda samma automation

---

## YAML Fundamentals

YAML = YAML Ain't Markup Language. Det är ett data-serialiseringsformat designat för att vara läsbart av människor.

```
+-------------------------------------------------------------------------+
|                           YAML REGLER                                   |
+-------------------------------------------------------------------------+
|                                                                         |
|  1. Indentering med SPACES (aldrig TAB!)                               |
|  2. 2 spaces är standard i Ansible                                      |
|  3. Case sensitive                                                      |
|  4. Listor börjar med -                                                |
|  5. Key-value med :                                                     |
|  6. Kommentarer med #                                                   |
|                                                                         |
+-------------------------------------------------------------------------+
```

### Data Types

```yaml
# ==========================================
# STRINGS
# ==========================================
# Enkla strängar (quotes optional)
name: webserver
full_name: "Web Server 01"
description: 'A production web server'

# Multiline string (behåll newlines)
message: |
  Rad 1
  Rad 2
  Rad 3

# Multiline string (fold till en rad)
message: >
  Detta blir
  en lång
  rad

# ==========================================
# NUMBERS
# ==========================================
port: 80
price: 19.99
hex: 0x1A
octal: 0o755

# ==========================================
# BOOLEANS
# ==========================================
enabled: true
disabled: false
# OBS: yes/no fungerar men true/false är bättre

# ==========================================
# NULL
# ==========================================
empty_value: null
also_null: ~

# ==========================================
# LISTS (Arrays)
# ==========================================
# Block format
packages:
  - nginx
  - curl
  - vim
  - htop

# Inline format
packages: [nginx, curl, vim, htop]

# ==========================================
# DICTIONARIES (Maps)
# ==========================================
# Block format
server:
  name: web01
  ip: 192.168.1.10
  port: 80
  enabled: true

# Inline format
server: {name: web01, ip: 192.168.1.10, port: 80}

# ==========================================
# NESTED STRUCTURES
# ==========================================
servers:
  - name: web01
    ip: 192.168.1.10
    services:
      - nginx
      - php-fpm
    settings:
      max_connections: 1000
      timeout: 30

  - name: web02
    ip: 192.168.1.11
    services:
      - nginx
    settings:
      max_connections: 500
      timeout: 60
```

---

## Playbook Struktur

```
+-------------------------------------------------------------------------+
|                        PLAYBOOK ANATOMY                                 |
+-------------------------------------------------------------------------+
|                                                                         |
|   playbook.yml                                                          |
|   |                                                                     |
|   +-- PLAY 1 ------------------------------------------                |
|   |   +-- name: Configure webservers                                   |
|   |   +-- hosts: webservers                                            |
|   |   +-- become: true                                                 |
|   |   +-- vars:                                                        |
|   |   |   +-- http_port: 80                                           |
|   |   |                                                                |
|   |   +-- tasks:                                                       |
|   |       +-- Task 1: Install nginx                                    |
|   |       +-- Task 2: Copy config                                      |
|   |       +-- Task 3: Start service                                    |
|   |                                                                     |
|   +-- PLAY 2 ------------------------------------------                |
|       +-- name: Configure databases                                    |
|       +-- hosts: databases                                             |
|       +-- tasks:                                                       |
|           +-- ...                                                      |
|                                                                         |
|   En playbook kan ha FLERA plays                                       |
|   Varje play körs mot en grupp hosts                                   |
|                                                                         |
+-------------------------------------------------------------------------+
```

### Komplett Playbook Exempel

```yaml
---
# ==========================================
# PLAY 1: WEBSERVER CONFIGURATION
# ==========================================
- name: Configure webservers
  hosts: webservers
  become: true
  gather_facts: true

  vars:
    http_port: 80
    https_port: 443
    server_name: "{{ inventory_hostname }}"
    packages:
      - nginx
      - curl
      - certbot

  tasks:
    # ------------------------------------------
    # TASK 1: Installera paket
    # ------------------------------------------
    - name: Install required packages
      apt:
        name: "{{ packages }}"
        state: present
        update_cache: true
      tags:
        - packages
        - setup

    # ------------------------------------------
    # TASK 2: Kopiera nginx config
    # ------------------------------------------
    - name: Deploy nginx configuration
      template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/nginx.conf
        owner: root
        group: root
        mode: '0644'
        backup: true
      notify: Restart nginx
      tags:
        - config

    # ------------------------------------------
    # TASK 3: Skapa web root
    # ------------------------------------------
    - name: Create web root directory
      file:
        path: /var/www/{{ server_name }}
        state: directory
        owner: www-data
        group: www-data
        mode: '0755'
      tags:
        - setup

    # ------------------------------------------
    # TASK 4: Deploy index page
    # ------------------------------------------
    - name: Copy index.html
      copy:
        src: files/index.html
        dest: /var/www/{{ server_name }}/index.html
        owner: www-data
        group: www-data
        mode: '0644'
      tags:
        - deploy

    # ------------------------------------------
    # TASK 5: Ensure nginx is running
    # ------------------------------------------
    - name: Start and enable nginx
      service:
        name: nginx
        state: started
        enabled: true
      tags:
        - service

  # ------------------------------------------
  # HANDLERS
  # ------------------------------------------
  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted

# ==========================================
# PLAY 2: DATABASE CONFIGURATION
# ==========================================
- name: Configure databases
  hosts: databases
  become: true

  tasks:
    - name: Install PostgreSQL
      apt:
        name: postgresql
        state: present
```

---

## Play Keywords

| Keyword | Beskrivning | Exempel |
|---------|-------------|---------|
| `name` | Beskrivning av play | `name: Configure web` |
| `hosts` | Målgrupp från inventory | `hosts: webservers` |
| `become` | Kör som root | `become: true` |
| `become_user` | Specifik användare | `become_user: postgres` |
| `gather_facts` | Samla systeminfo | `gather_facts: true` |
| `vars` | Variabler för play | `vars: {...}` |
| `vars_files` | Läs variabler från fil | `vars_files: [secrets.yml]` |
| `tasks` | Lista av tasks | `tasks: [...]` |
| `handlers` | Triggered tasks | `handlers: [...]` |
| `pre_tasks` | Körs före tasks | `pre_tasks: [...]` |
| `post_tasks` | Körs efter tasks | `post_tasks: [...]` |
| `roles` | Inkludera roles | `roles: [nginx]` |
| `tags` | Tagga hela play | `tags: [setup]` |
| `serial` | Antal hosts åt gången | `serial: 2` |
| `max_fail_percentage` | Tolerans för fel | `max_fail_percentage: 25` |

---

## Task Keywords

| Keyword | Beskrivning | Exempel |
|---------|-------------|---------|
| `name` | Beskrivning | `name: Install nginx` |
| `MODULE` | Modulen att köra | `apt:`, `copy:`, `service:` |
| `become` | Överskrid play-become | `become: false` |
| `when` | Villkor för körning | `when: ansible_os == 'Ubuntu'` |
| `loop` | Loopa över lista | `loop: [a, b, c]` |
| `register` | Spara output | `register: result` |
| `notify` | Triggra handler | `notify: Restart nginx` |
| `tags` | Tagga task | `tags: [config]` |
| `ignore_errors` | Fortsätt vid fel | `ignore_errors: true` |
| `changed_when` | Överskrid changed | `changed_when: false` |
| `failed_when` | Överskrid failed | `failed_when: "'error' in result"` |
| `delegate_to` | Kör på annan host | `delegate_to: localhost` |
| `run_once` | Kör bara en gång | `run_once: true` |
| `block` | Gruppera tasks | `block: [...]` |
| `rescue` | Error handling | `rescue: [...]` |
| `always` | Körs alltid | `always: [...]` |

---

## Köra Playbooks

```bash
# Basic körning
ansible-playbook -i inventory.yml playbook.yml

# Dry-run (check mode)
ansible-playbook playbook.yml --check

# Visa ändringar (diff)
ansible-playbook playbook.yml --diff

# Check + Diff (vanligast)
ansible-playbook playbook.yml --check --diff

# Verbose output
ansible-playbook playbook.yml -v      # Basic
ansible-playbook playbook.yml -vv     # Mer info
ansible-playbook playbook.yml -vvv    # SSH debug
ansible-playbook playbook.yml -vvvv   # Full debug

# Begränsa hosts
ansible-playbook playbook.yml --limit web01
ansible-playbook playbook.yml --limit 'webservers:!web03'

# Starta från specifik task
ansible-playbook playbook.yml --start-at-task="Copy config"

# Kör bara specifika tags
ansible-playbook playbook.yml --tags "config,deploy"
ansible-playbook playbook.yml --skip-tags "setup"

# Lista tasks utan att köra
ansible-playbook playbook.yml --list-tasks

# Lista hosts utan att köra
ansible-playbook playbook.yml --list-hosts

# Step-by-step (fråga före varje task)
ansible-playbook playbook.yml --step

# Extra variabler
ansible-playbook playbook.yml -e "env=production version=1.2.3"
ansible-playbook playbook.yml -e "@vars.json"
```

---

## Handlers

Handlers körs bara om en task har `changed` status och alla handlers körs i slutet av play:en.

```yaml
tasks:
  - name: Copy nginx config
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify:
      - Reload nginx
      - Clear cache

  - name: Copy SSL certificate
    copy:
      src: ssl/cert.pem
      dest: /etc/ssl/cert.pem
    notify: Reload nginx

handlers:
  - name: Reload nginx
    service:
      name: nginx
      state: reloaded

  - name: Clear cache
    file:
      path: /var/cache/nginx
      state: absent
```

---

## Felsökning

### YAML Validation

```bash
# Syntax check
ansible-playbook playbook.yml --syntax-check

# Lint (kräver ansible-lint)
pip install ansible-lint
ansible-lint playbook.yml

# YAML validation
python -c "import yaml; yaml.safe_load(open('playbook.yml'))"
```

### Vanliga YAML-fel

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `mapping values not allowed` | Saknas space efter `:` | `name: value` |
| `could not find expected ':'` | Fel indentering | Kolla spaces |
| `found character that cannot start` | TAB istället för space | Använd spaces |
| `did not find expected key` | Inkonsekvent indentering | Samma antal spaces |
| `block sequence entries` | Lista i fel kontext | Kolla strukturen |

---

## Praktisk Övning

```bash
# 1. Setup
mkdir -p ~/playbook-lab/{files,templates}
cd ~/playbook-lab

# 2. Skapa inventory
cat > inventory.yml << 'EOF'
all:
  children:
    local:
      hosts:
        localhost:
          ansible_connection: local
          ansible_python_interpreter: /usr/bin/python3
EOF

# 3. Skapa en fil att kopiera
echo "<h1>Hello from Ansible!</h1>" > files/index.html

# 4. Skapa playbook
cat > site.yml << 'EOF'
---
- name: My first playbook
  hosts: local
  become: false

  vars:
    app_name: myapp
    app_port: 8080

  tasks:
    - name: Show hostname
      debug:
        msg: "Running on {{ inventory_hostname }}"

    - name: Show variables
      debug:
        msg: "App: {{ app_name }} on port {{ app_port }}"

    - name: Create app directory
      file:
        path: "/tmp/{{ app_name }}"
        state: directory
        mode: '0755'

    - name: Copy index file
      copy:
        src: files/index.html
        dest: "/tmp/{{ app_name }}/index.html"
        mode: '0644'

    - name: Verify file exists
      stat:
        path: "/tmp/{{ app_name }}/index.html"
      register: index_file

    - name: Show file info
      debug:
        msg: "File size: {{ index_file.stat.size }} bytes"
      when: index_file.stat.exists
EOF

# 5. Syntax check
ansible-playbook site.yml --syntax-check

# 6. Dry-run
ansible-playbook -i inventory.yml site.yml --check --diff

# 7. Execute
ansible-playbook -i inventory.yml site.yml

# 8. Verify
ls -la /tmp/myapp/
cat /tmp/myapp/index.html
```

---

## Sammanfattning

| Koncept | Vad du lärt dig |
|---------|-----------------|
| YAML | Data-format med key:value och listor |
| Playbook | Fil med en eller flera plays |
| Play | Körs mot en grupp hosts |
| Task | En operation (modul + argument) |
| Handler | Körs vid ändringar (notify) |
| Tags | Selektiv körning |
| Check mode | Dry-run utan ändringar |

---

## Nästa Steg

Nu kan du skriva och köra playbooks. Nästa modul: **Variables & Facts** — dynamisk konfiguration och systeminfo.
''',
}

ANSIBLE_BLOCK_1 = [
    NODE_01_ANSIBLE_INTRO,
    NODE_02_INVENTORY,
    NODE_03_ADHOC_COMMANDS,
    NODE_04_YAML_BASICS,
]
