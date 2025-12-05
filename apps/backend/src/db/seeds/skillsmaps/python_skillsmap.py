# -*- coding: utf-8 -*-
"""
Python SkillsMap - 20 Consolidated Nodes (DevOps Focus)
Version: 1.0
Date: 2025-12-01

Pedagogical Style: Akhilesh (Intro -> Concept -> Code -> Pro Tips -> Task)
Focus: Python for DevOps, Automation, and Cloud
"""

from typing import Literal, List, Dict, Any

DifficultyLevel = Literal["beginner", "intermediate", "advanced", "expert"]


# =============================================================================
# PYTHON SKILLSMAP METADATA
# =============================================================================

PYTHON_SKILLSMAP_INFO = {
    "name": "Python for DevOps",
    "slug": "python-devops",
    "description": "Master Python for automation, scripting, and cloud infrastructure",
    "total_nodes": 20,
    "estimated_hours": 35,
    "difficulty_range": "beginner to advanced",
    "focus": "DevOps, Automation, Cloud SDKs",
}


# =============================================================================
# NODE 1: PYTHON BASICS
# =============================================================================

NODE_01_PYTHON_BASICS = {
    "node_id": 1,
    "title": "Python Fundamentals",
    "slug": "python-basics",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 70,
    "topics_covered": [
        "variables", "data types", "strings", "numbers",
        "booleans", "type conversion", "print", "input"
    ],
    "content": r"""# 🐍 Python Fundamentals

## Varför detta är viktigt

Som DevOps-ingenjör är Python ditt viktigaste verktyg. Ansible är skrivet i Python. AWS Lambda älskar Python. Kubernetes operators använder Python. Terraform providers byggs med Python. Det är läsbart, kraftfullt och finns överallt i DevOps-världen.

## Vad du kommer lära dig

- Förstå Pythons grundläggande syntax och datatyper
- Konfigurera Python-miljöer för DevOps-arbete
- Implementera variabler, strings och numbers korrekt
- Behärska type conversion och namnkonventioner

---

## 📚 Varför Python för DevOps?

> "Python is the Swiss Army knife of DevOps. Ansible is Python. AWS Lambda loves Python. Kubernetes operators use Python. It's readable, powerful, and everywhere."

```
┌────────────────────────────────────────────────────────────────────────┐
│                    PYTHON I DEVOPS-EKOSYSTEMET                         │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐       │
│   │ Ansible  │    │   AWS    │    │ Kubernetes│   │ Terraform│       │
│   │  YAML+   │    │  Lambda  │    │ Operators │   │ Providers│       │
│   │ Python   │    │  Python  │    │  Python   │   │  Python  │       │
│   └────┬─────┘    └────┬─────┘    └────┬─────┘    └────┬─────┘       │
│        │               │               │               │              │
│        └───────────────┴───────┬───────┴───────────────┘              │
│                                │                                       │
│                    ┌───────────▼───────────┐                          │
│                    │      PYTHON CORE      │                          │
│                    │   (Your Foundation)   │                          │
│                    └───────────────────────┘                          │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Installation & Setup

```bash
# Kolla version
python3 --version

# Skapa virtual environment (best practice!)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Kor Python interaktivt
python3

# Kor script
python3 script.py
```

---

## Variabler

Variabler lagrar data. Ingen typdeklaration behovs.

```python
# Strings (text)
name = "DevOps Engineer"
server = 'prod-server-01'

# Numbers
port = 8080           # int (heltal)
cpu_usage = 75.5      # float (decimaltal)

# Booleans
is_running = True
is_failed = False

# None (inget varde)
result = None
```

### Namnkonventioner

```python
# snake_case for variabler och funktioner (Python-standard)
server_name = "web-01"
max_retries = 3

# SCREAMING_SNAKE_CASE for konstanter
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
```

---

## Datatyper

### Strings

```python
# Skapa strings
name = "nginx"
path = '/var/log/nginx'
multiline = '''
Detta ar
flera rader
'''

# String operations
server = "prod-web-01"
print(server.upper())        # PROD-WEB-01
print(server.lower())        # prod-web-01
print(server.replace("-", "_"))  # prod_web_01
print(len(server))           # 11

# Slicing
print(server[0])             # p (forsta tecknet)
print(server[-1])            # 1 (sista tecknet)
print(server[0:4])           # prod (index 0-3)
print(server[5:])            # web-01 (fran index 5)

# f-strings (formaterade strings) - ANVAND DESSA!
host = "192.168.1.10"
port = 22
print(f"Connecting to {host}:{port}")
# Connecting to 192.168.1.10:22

# Med expressions
cpu = 85.7
print(f"CPU: {cpu:.1f}%")    # CPU: 85.7%
print(f"Status: {'HIGH' if cpu > 80 else 'OK'}")
```

### Numbers

```python
# Integers
count = 42
port = 8080
max_pods = 100

# Floats
cpu_percent = 75.5
memory_gb = 16.0

# Operationer
total = 10 + 5      # 15
diff = 10 - 5       # 5
product = 10 * 5    # 50
quotient = 10 / 3   # 3.333...
floor_div = 10 // 3 # 3 (heltalsdivision)
remainder = 10 % 3  # 1 (modulo)
power = 2 ** 10     # 1024

# Jamforelser
print(10 > 5)       # True
print(10 == 10)     # True
print(10 != 5)      # True
print(10 >= 10)     # True
```

### Booleans

```python
is_running = True
is_failed = False

# Logiska operatorer
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Vanligt i DevOps:
health_check_passed = True
enough_memory = True
can_deploy = health_check_passed and enough_memory
```

---

## Type Conversion

```python
# String -> Number
port_str = "8080"
port = int(port_str)      # 8080

# Number -> String
count = 42
count_str = str(count)    # "42"

# String -> Float
cpu = float("75.5")       # 75.5

# Kolla typ
print(type(port))         # <class 'int'>
print(type("hello"))      # <class 'str'>

# isinstance() - battre for typkontroll
if isinstance(port, int):
    print("Port is an integer")
```

---

## Praktiska Ovningar

### Ovning 1: Server Info

```python
# Skapa variabler for en server
hostname = "prod-web-01"
ip_address = "192.168.1.100"
port = 443
is_https = True
cpu_usage = 67.8

# Skriv ut info
print(f"Server: {hostname}")
print(f"Address: {ip_address}:{port}")
print(f"HTTPS: {is_https}")
print(f"CPU: {cpu_usage}%")
```

### Ovning 2: Berakningar

```python
# Memory calculation
total_memory_gb = 16
used_memory_gb = 12.5
free_memory_gb = total_memory_gb - used_memory_gb
usage_percent = (used_memory_gb / total_memory_gb) * 100

print(f"Memory: {used_memory_gb}/{total_memory_gb} GB")
print(f"Usage: {usage_percent:.1f}%")
print(f"Free: {free_memory_gb} GB")
```

---

## Sammanfattning

| Koncept | Exempel |
|---------|---------|
| String | `name = "nginx"` |
| Integer | `port = 8080` |
| Float | `cpu = 75.5` |
| Boolean | `is_running = True` |
| f-string | `f"Port: {port}"` |
| Type check | `isinstance(x, int)` |

---

## ✅ Praktisk Övning

### Uppgift
Skapa ett script som definierar serverinformation och beräknar resursanvändning.

### Steg-för-steg

1. Skapa en fil `server_info.py`:
```python
# server_info.py
hostname = "prod-web-01"
ip_address = "192.168.1.100"
port = 443
is_https = True
total_memory_gb = 16
used_memory_gb = 12.5
```

2. Lägg till beräkningar:
```python
free_memory_gb = total_memory_gb - used_memory_gb
usage_percent = (used_memory_gb / total_memory_gb) * 100
```

3. Skriv ut formaterad output:
```python
print(f"Server: {hostname}")
print(f"Address: {ip_address}:{port}")
print(f"Memory Usage: {usage_percent:.1f}%")
```

### Verifiera
Kör scriptet:
```bash
python3 server_info.py
```

Du bör se:
```
Server: prod-web-01
Address: 192.168.1.100:443
Memory Usage: 78.1%
```

### Vanliga problem

**Problem:** `SyntaxError: invalid syntax`
**Lösning:** Kontrollera att alla parenteser och citattecken är korrekt stängda.

**Problem:** `NameError: name 'x' is not defined`
**Lösning:** Du använder en variabel innan den deklarerats.

---

## 🎯 Sammanfattning

I denna task har du lärt dig:
- ✅ Pythons grundläggande datatyper: strings, integers, floats, booleans
- ✅ Hur man deklarerar variabler utan typangivelse
- ✅ f-strings för formaterad output
- ✅ Type conversion mellan olika datatyper
- ✅ Python-namnkonventioner (snake_case)

### Nästa steg
I nästa task lär du dig om **Collections** - listor, dictionaries och sets för att hantera flera datapunkter.
"""
}


# =============================================================================
# NODE 2: COLLECTIONS
# =============================================================================

NODE_02_COLLECTIONS = {
    "node_id": 2,
    "title": "Collections: Lists, Dicts, Sets",
    "slug": "collections",
    "difficulty": "beginner",
    "estimated_minutes": 65,
    "xp_reward": 80,
    "topics_covered": [
        "lists", "dictionaries", "sets", "tuples",
        "indexing", "slicing", "methods", "comprehensions"
    ],
    "content": r"""# 🗂️ Collections: Lists, Dicts, Sets

## Varför detta är viktigt

Som DevOps-ingenjör hanterar du ständigt MÅNGA saker - servrar, containers, configs, användare. Collections är hur du organiserar och manipulerar dem effektivt i Python.

## Vad du kommer lära dig

- Förstå skillnaden mellan lists, dicts, sets och tuples
- Implementera indexering och slicing för dataåtkomst
- Använda list/dict comprehensions för effektiv kod
- Välja rätt collection-typ för olika användningsfall

---

## 📚 Lists (Listor)

Ordnade, andringsbara samlingar.

```python
# Skapa lista
servers = ["web-01", "web-02", "web-03"]
ports = [80, 443, 8080]
mixed = ["nginx", 80, True, 3.14]  # Olika typer OK

# Tom lista
empty = []
also_empty = list()

# Atkomst via index (0-baserat)
print(servers[0])     # web-01
print(servers[-1])    # web-03 (sista)
print(servers[1:3])   # ['web-02', 'web-03']

# Andra element
servers[0] = "web-primary"

# Langd
print(len(servers))   # 3
```

### List Methods

```python
servers = ["web-01", "web-02"]

# Lagg till
servers.append("web-03")           # Sist
servers.insert(0, "web-00")        # Pa index 0
servers.extend(["db-01", "db-02"]) # Lagg till flera

# Ta bort
servers.remove("web-00")           # By value
del servers[0]                     # By index
last = servers.pop()               # Ta bort & returnera sista
servers.clear()                    # Ta bort alla

# Sok
servers = ["web-01", "web-02", "web-03"]
print("web-02" in servers)         # True
print(servers.index("web-02"))     # 1
print(servers.count("web-01"))     # 1

# Sortera
servers.sort()                     # Pa plats
servers.sort(reverse=True)         # Omvand
sorted_list = sorted(servers)      # Ny lista
servers.reverse()                  # Vand ordning
```

### List Comprehensions (VIKTIGT!)

Kompakt satt att skapa listor.

```python
# Gammal stil
squares = []
for i in range(5):
    squares.append(i ** 2)

# List comprehension - samma resultat
squares = [i ** 2 for i in range(5)]
# [0, 1, 4, 9, 16]

# Med villkor
servers = ["web-01", "db-01", "web-02", "cache-01"]
web_servers = [s for s in servers if s.startswith("web")]
# ['web-01', 'web-02']

# DevOps-exempel: Generera hostnames
hosts = [f"node-{i:02d}" for i in range(1, 6)]
# ['node-01', 'node-02', 'node-03', 'node-04', 'node-05']

# Transformera
upper_servers = [s.upper() for s in servers]
```

---

## Dictionaries (Dicts)

Key-value par. **Extremt vanligt i DevOps** (configs, JSON, etc.)

```python
# Skapa dict
server = {
    "hostname": "web-01",
    "ip": "192.168.1.10",
    "port": 80,
    "is_active": True
}

# Atkomst
print(server["hostname"])         # web-01
print(server.get("hostname"))     # web-01
print(server.get("missing", "N/A"))  # N/A (default)

# Andra / Lagg till
server["port"] = 443
server["ssl"] = True

# Ta bort
del server["ssl"]
port = server.pop("port")         # Ta bort & returnera
```

### Dict Methods

```python
server = {"hostname": "web-01", "ip": "192.168.1.10"}

# Keys, values, items
print(server.keys())      # dict_keys(['hostname', 'ip'])
print(server.values())    # dict_values(['web-01', '192.168.1.10'])
print(server.items())     # dict_items([('hostname', 'web-01'), ...])

# Kolla om key finns
if "hostname" in server:
    print("Has hostname")

# Uppdatera med annan dict
server.update({"port": 80, "ssl": True})

# Kopiera
server_copy = server.copy()
```

### Nested Dicts (vanligt!)

```python
infrastructure = {
    "production": {
        "web": ["web-01", "web-02"],
        "db": ["db-01"]
    },
    "staging": {
        "web": ["staging-web-01"],
        "db": ["staging-db-01"]
    }
}

# Atkomst
print(infrastructure["production"]["web"][0])  # web-01

# Safe access
prod_web = infrastructure.get("production", {}).get("web", [])
```

### Dict Comprehensions

```python
# Skapa dict fran lista
servers = ["web-01", "web-02", "web-03"]
server_ports = {s: 80 for s in servers}
# {'web-01': 80, 'web-02': 80, 'web-03': 80}

# Med index
server_ids = {s: i for i, s in enumerate(servers)}
# {'web-01': 0, 'web-02': 1, 'web-03': 2}

# Filtrera dict
all_servers = {"web-01": "running", "web-02": "stopped", "db-01": "running"}
running = {k: v for k, v in all_servers.items() if v == "running"}
```

---

## Sets

Unika varden, oordnade. Bra for att hitta duplikater.

```python
# Skapa set
ips = {"192.168.1.1", "192.168.1.2", "192.168.1.1"}
print(ips)  # {'192.168.1.1', '192.168.1.2'} - dubletten borta!

# Set operations
a = {"web-01", "web-02", "web-03"}
b = {"web-02", "web-03", "web-04"}

print(a | b)    # Union: alla
print(a & b)    # Intersection: gemensamma
print(a - b)    # Difference: i a men inte b

# Praktiskt: hitta nya/borttagna servrar
old_servers = {"web-01", "web-02", "web-03"}
new_servers = {"web-02", "web-03", "web-04"}

added = new_servers - old_servers    # {'web-04'}
removed = old_servers - new_servers  # {'web-01'}
```

---

## Tuples

Som listor, men **immutable** (kan inte andras).

```python
# Skapa tuple
coordinates = (10, 20)
rgb = (255, 128, 0)

# Atkomst (som lista)
print(coordinates[0])  # 10

# Kan INTE andras
# coordinates[0] = 15  # TypeError!

# Tuple unpacking
x, y = coordinates
print(x, y)  # 10 20

# Vanligt: returnera flera varden
def get_server_info():
    return "web-01", "192.168.1.10", 80

hostname, ip, port = get_server_info()
```

---

## Sammanfattning

| Typ | Syntax | Anvandning |
|-----|--------|------------|
| List | `[1, 2, 3]` | Ordnad, andringsbar |
| Dict | `{"key": "val"}` | Key-value, configs |
| Set | `{1, 2, 3}` | Unika varden |
| Tuple | `(1, 2, 3)` | Immutable lista |

---

## Nasta Steg

Du kan nu hantera data i collections. Nasta node: **Control Flow** - if, loops och logik.
"""
}


# =============================================================================
# NODE 3: CONTROL FLOW
# =============================================================================

NODE_03_CONTROL_FLOW = {
    "node_id": 3,
    "title": "Control Flow: If, Loops, Logic",
    "slug": "control-flow",
    "difficulty": "beginner",
    "estimated_minutes": 55,
    "xp_reward": 75,
    "topics_covered": [
        "if", "elif", "else", "for", "while",
        "break", "continue", "pass", "match"
    ],
    "content": r"""# 🔄 Control Flow: If, Loops, Logic

## Varför detta är viktigt

Som DevOps-ingenjör är automation logik. IF server är nere, THEN starta om. FOR varje container, kolla status. Control flow är hjärnan i dina scripts och avgör hur dina automationer beter sig.

## Vad du kommer lära dig

- Förstå if/elif/else för villkorlig logik
- Implementera for- och while-loopar för iteration
- Använda break, continue och pass för loop-kontroll
- Kombinera logiska operatorer för komplexa villkor

---

## 📚 If-satser

```python
cpu_usage = 85

if cpu_usage > 90:
    print("CRITICAL: CPU overbelastad!")
elif cpu_usage > 70:
    print("WARNING: Hog CPU-anvandning")
else:
    print("OK: CPU normal")
```

### Jamforelseoperatorer

```python
x = 10

x == 10    # Lika med
x != 5     # Inte lika med
x > 5      # Storre an
x < 20     # Mindre an
x >= 10    # Storre eller lika
x <= 10    # Mindre eller lika
```

### Logiska operatorer

```python
is_running = True
has_memory = True
is_healthy = False

# and - bada maste vara True
if is_running and has_memory:
    print("Server OK")

# or - minst en maste vara True
if is_running or is_healthy:
    print("Nagon check passerade")

# not - inverterar
if not is_healthy:
    print("Server ar ohalsosam")

# Kombinera
if is_running and has_memory and not is_healthy:
    print("Kors men ohalsosam - undersok!")
```

### Membership & Identity

```python
# in - finns i collection
servers = ["web-01", "web-02"]
if "web-01" in servers:
    print("web-01 finns")

# not in
if "db-01" not in servers:
    print("db-01 saknas")

# is - samma objekt (identity)
x = None
if x is None:
    print("x ar None")
```

### Ternary Operator (one-liner)

```python
status = "running"
emoji = "[OK]" if status == "running" else "[FAIL]"
print(f"Status: {emoji}")
```

---

## For-loopar

Iterera over collections.

```python
# Lista
servers = ["web-01", "web-02", "web-03"]
for server in servers:
    print(f"Checking {server}...")

# Dict
config = {"port": 80, "ssl": True}
for key, value in config.items():
    print(f"{key}: {value}")

# Range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (steg 2)
    print(i)

# Enumerate (index + varde)
for i, server in enumerate(servers):
    print(f"{i}: {server}")
# 0: web-01
# 1: web-02
# 2: web-03
```

### Nested Loops

```python
environments = ["prod", "staging"]
servers = ["web", "db"]

for env in environments:
    for server in servers:
        print(f"{env}-{server}")
# prod-web, prod-db, staging-web, staging-db
```

---

## While-loopar

Kor sa lange villkor ar True.

```python
# Retry-pattern
retries = 0
max_retries = 3

while retries < max_retries:
    print(f"Attempt {retries + 1}")
    # ... forsok nagot
    success = False  # simulera
    if success:
        break
    retries += 1
else:
    print("Alla forsok misslyckades")
```

---

## Break, Continue, Pass

```python
servers = ["web-01", "db-01", "web-02", "cache-01"]

# break - avbryt loop
for server in servers:
    if server.startswith("db"):
        print(f"Found database: {server}")
        break

# continue - hoppa till nasta iteration
for server in servers:
    if server.startswith("cache"):
        continue  # Skippa cache-servrar
    print(f"Processing: {server}")

# pass - gor ingenting (placeholder)
for server in servers:
    if server.startswith("web"):
        pass  # TODO: implementera senare
    else:
        print(f"Non-web: {server}")
```

---

## Match Statement (Python 3.10+)

```python
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")
```

---

## Praktisk Ovning: Health Check

```python
servers = [
    {"name": "web-01", "status": "running", "cpu": 45},
    {"name": "web-02", "status": "running", "cpu": 92},
    {"name": "db-01", "status": "stopped", "cpu": 0},
]

for server in servers:
    name = server["name"]

    if server["status"] != "running":
        print(f"[FAIL] {name}: NOT RUNNING")
        continue

    cpu = server["cpu"]
    if cpu > 90:
        print(f"[CRIT] {name}: CPU {cpu}%")
    elif cpu > 70:
        print(f"[WARN] {name}: CPU {cpu}%")
    else:
        print(f"[OK] {name}: CPU {cpu}%")
```

---

## 🎯 Sammanfattning

I denna task har du lärt dig:
- ✅ If/elif/else för villkorlig logik
- ✅ For-loopar för iteration över collections
- ✅ While-loopar för villkorsbaserad iteration
- ✅ Break och continue för loop-kontroll
- ✅ Enumerate för index + värde

| Syntax | Användning |
|--------|------------|
| `if/elif/else` | Villkor |
| `for x in list` | Iteration |
| `while condition` | Loop tills False |
| `break` | Avbryt loop |
| `continue` | Nästa iteration |
| `enumerate()` | Index + värde |

### Nästa steg
I nästa task lär du dig om **Functions** - hur du strukturerar återanvändbar kod.
"""
}


# =============================================================================
# NODE 4: FUNCTIONS
# =============================================================================

NODE_04_FUNCTIONS = {
    "node_id": 4,
    "title": "Functions & Arguments",
    "slug": "functions",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 80,
    "topics_covered": [
        "def", "arguments", "return", "default values",
        "*args", "**kwargs", "lambda", "docstrings"
    ],
    "content": r"""# 🔧 Functions & Arguments

## Varför detta är viktigt

Som DevOps-ingenjör följer du DRY-principen (Don't Repeat Yourself). Funktioner låter dig skriva kod en gång och använda den överallt. En bra deploy-funktion kan användas för alla dina projekt.

## Vad du kommer lära dig

- Förstå funktionsdefinitioner och anrop
- Implementera olika argument-typer (*args, **kwargs)
- Använda return-värden och default-parametrar
- Skriva docstrings för dokumentation

---

## 📚 Grundläggande Funktioner

```python
# Definiera funktion
def greet():
    print("Hello, DevOps!")

# Anropa
greet()  # Hello, DevOps!

# Med parameter
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Engineer")  # Hello, Engineer!

# Med return
def add(a, b):
    return a + b

result = add(5, 3)  # 8
```

---

## Arguments

### Positional Arguments

```python
def deploy(environment, version):
    print(f"Deploying v{version} to {environment}")

deploy("production", "1.2.3")
# Deploying v1.2.3 to production
```

### Keyword Arguments

```python
# Explicit namngivning
deploy(version="1.2.3", environment="production")
# Ordning spelar ingen roll med keywords

# Blanda (positional forst!)
deploy("staging", version="1.2.3")
```

### Default Values

```python
def deploy(environment, version="latest", dry_run=False):
    if dry_run:
        print(f"[DRY RUN] Would deploy v{version} to {environment}")
    else:
        print(f"Deploying v{version} to {environment}")

deploy("production")                    # Anvander defaults
deploy("production", "1.2.3")          # Override version
deploy("production", dry_run=True)     # Bara dry_run
```

### *args (Variable Positional)

```python
def restart_servers(*servers):
    for server in servers:
        print(f"Restarting {server}...")

restart_servers("web-01")
restart_servers("web-01", "web-02", "web-03")

# servers blir en tuple
```

### **kwargs (Variable Keyword)

```python
def create_config(**settings):
    for key, value in settings.items():
        print(f"{key} = {value}")

create_config(port=8080, debug=True, log_level="INFO")

# settings blir en dict
```

---

## Return Values

```python
# Returnera ett varde
def get_status(server):
    return "running"

# Returnera flera (tuple)
def get_server_info(name):
    return name, "192.168.1.10", 80

hostname, ip, port = get_server_info("web-01")

# Returnera dict (vanligt!)
def check_health(server):
    return {
        "server": server,
        "status": "healthy",
        "cpu": 45,
        "memory": 60
    }

result = check_health("web-01")
print(result["status"])  # healthy
```

---

## Lambda (Anonymous Functions)

Korta engangsfunktioner.

```python
# Normal funktion
def square(x):
    return x ** 2

# Lambda
square = lambda x: x ** 2

# Vanligt med sort/filter/map
servers = ["web-01", "db-01", "web-02"]

# Sortera pa sista tecknet
sorted_servers = sorted(servers, key=lambda s: s[-1])

# Filtrera
web_only = list(filter(lambda s: s.startswith("web"), servers))

# Transformera
upper = list(map(lambda s: s.upper(), servers))
```

---

## Type Hints

```python
from typing import List, Dict, Optional

def get_servers(environment: str) -> List[str]:
    return ["web-01", "web-02"]

def get_config(key: str, default: Optional[str] = None) -> str:
    configs = {"port": "8080"}
    return configs.get(key, default)

def process_servers(servers: List[Dict[str, str]]) -> None:
    for server in servers:
        print(server["name"])
```

---

## Praktisk Ovning: Health Check Function

```python
def check_server_health(server: dict) -> dict:
    name = server.get("name", "unknown")
    cpu = server.get("cpu", 0)

    if cpu > 90:
        return {"status": "critical", "message": f"{name}: CPU {cpu}%"}
    elif cpu > 70:
        return {"status": "warning", "message": f"{name}: CPU {cpu}%"}
    else:
        return {"status": "ok", "message": f"{name}: healthy"}

# Test
server = {"name": "web-01", "cpu": 85}
result = check_server_health(server)
print(result)
```

---

## Sammanfattning

| Koncept | Exempel |
|---------|---------|
| Basic function | `def func():` |
| With args | `def func(a, b):` |
| Default value | `def func(x=10):` |
| *args | `def func(*args):` |
| **kwargs | `def func(**kwargs):` |
| Return | `return value` |
| Lambda | `lambda x: x * 2` |
| Type hints | `def func(x: int) -> str:` |
"""
}


# =============================================================================
# NODE 5: FILE I/O
# =============================================================================

NODE_05_FILE_IO = {
    "node_id": 5,
    "title": "File I/O Operations",
    "slug": "file-io",
    "difficulty": "beginner",
    "estimated_minutes": 50,
    "xp_reward": 75,
    "topics_covered": [
        "open", "read", "write", "with statement",
        "pathlib", "file modes", "binary files"
    ],
    "content": r"""# 📁 File I/O Operations

## Varför detta är viktigt

Som DevOps-ingenjör jobbar du ständigt med filer: config files, log files, YAML, JSON, scripts. Du måste kunna läsa, skriva och manipulera filer effektivt för att automatisera konfigurationshantering.

## Vad du kommer lära dig

- Förstå filläsning och -skrivning med open()
- Implementera with-statement för säker filhantering
- Använda pathlib för modern path-hantering
- Hantera olika filformat och binärfiler

---

## 📚 Läsa Filer

### Grundläggande

```python
# Oppna och las
file = open("config.txt", "r")
content = file.read()
file.close()

# BATTRE: with statement (stanger automatiskt)
with open("config.txt", "r") as file:
    content = file.read()

print(content)
```

### Olika satt att lasa

```python
with open("servers.txt", "r") as f:
    # Las allt
    all_content = f.read()

    # Las en rad
    first_line = f.readline()

    # Las alla rader som lista
    lines = f.readlines()

    # Iterera rad for rad (minneseffektivt)
    for line in f:
        print(line.strip())  # strip() tar bort newlines
```

---

## Skriva Filer

```python
# Skriv (overskriver)
with open("output.txt", "w") as f:
    f.write("Hello, DevOps!\n")
    f.write("Second line\n")

# Append (lagg till)
with open("log.txt", "a") as f:
    f.write("New log entry\n")

# Skriv flera rader
lines = ["server1", "server2", "server3"]
with open("servers.txt", "w") as f:
    f.writelines([line + "\n" for line in lines])
```

---

## File Modes

| Mode | Beskrivning |
|------|-------------|
| `r` | Read (default) |
| `w` | Write (overskriver) |
| `a` | Append |
| `x` | Create (fail om finns) |
| `b` | Binary mode |
| `+` | Read and write |

```python
# Binart lage (for bilder, etc)
with open("image.png", "rb") as f:
    data = f.read()

# Read + Write
with open("config.txt", "r+") as f:
    content = f.read()
    f.write("Appended text")
```

---

## pathlib (Modern approach)

```python
from pathlib import Path

# Skapa Path-objekt
config_path = Path("/etc/nginx/nginx.conf")
home = Path.home()
current = Path.cwd()

# Kolla om finns
if config_path.exists():
    print("Config exists")

if config_path.is_file():
    print("It's a file")

if config_path.is_dir():
    print("It's a directory")

# Las fil
content = config_path.read_text()
data = config_path.read_bytes()

# Skriv fil
Path("output.txt").write_text("Hello!")

# Path-manipulation
logs = Path("/var/log")
nginx_log = logs / "nginx" / "access.log"  # Snygg join!

# Lista filer
for file in Path(".").glob("*.py"):
    print(file.name)

# Rekursiv glob
for file in Path(".").rglob("*.yaml"):
    print(file)
```

---

## Praktiska Exempel

### Config Parser

```python
def load_config(filepath):
    config = {}
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config

# config.txt:
# port=8080
# debug=true

config = load_config("config.txt")
print(config)  # {'port': '8080', 'debug': 'true'}
```

### Log Writer

```python
from datetime import datetime

def log_message(message, filepath="app.log"):
    timestamp = datetime.now().isoformat()
    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

log_message("Server started")
log_message("Connection received")
```

---

## Sammanfattning

| Operation | Kod |
|-----------|-----|
| Read file | `open(f, "r").read()` |
| Write file | `open(f, "w").write()` |
| Append | `open(f, "a").write()` |
| Path exists | `Path(f).exists()` |
| Read with pathlib | `Path(f).read_text()` |
"""
}


# =============================================================================
# NODE 6: ERROR HANDLING
# =============================================================================

NODE_06_ERROR_HANDLING = {
    "node_id": 6,
    "title": "Error Handling & Exceptions",
    "slug": "error-handling",
    "difficulty": "intermediate",
    "estimated_minutes": 45,
    "xp_reward": 75,
    "topics_covered": [
        "try", "except", "finally", "raise",
        "custom exceptions", "exception types"
    ],
    "content": r"""# ⚠️ Error Handling & Exceptions

## Varför detta är viktigt

I produktion går saker fel - nätverk timeout, filer saknas, servrar svarar inte. Din kod måste hantera det gracefullt istället för att krascha och ta ner hela systemet.

## Vad du kommer lära dig

- Förstå try/except/finally för felhantering
- Implementera specifika exception-typer
- Skapa egna custom exceptions
- Använda raise för att propagera fel

---

## 📚 Try / Except

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Kan inte dividera med noll!")

# Fanga alla fel (anvand sparsamt)
try:
    risky_operation()
except Exception as e:
    print(f"Nagot gick fel: {e}")
```

### Flera Exception Types

```python
try:
    file = open("missing.txt")
    data = file.read()
    number = int(data)
except FileNotFoundError:
    print("Filen finns inte")
except ValueError:
    print("Kunde inte konvertera till nummer")
except Exception as e:
    print(f"Okant fel: {e}")
```

---

## Finally

Kors ALLTID, oavsett om fel uppstod.

```python
try:
    file = open("data.txt")
    process(file)
except FileNotFoundError:
    print("Fil saknas")
finally:
    file.close()  # Stanger alltid

# Battre: anvand with
with open("data.txt") as f:
    process(f)  # Stanger automatiskt
```

---

## Raise

Kasta egna fel.

```python
def deploy(environment):
    if environment not in ["prod", "staging", "dev"]:
        raise ValueError(f"Invalid environment: {environment}")
    print(f"Deploying to {environment}")

try:
    deploy("invalid")
except ValueError as e:
    print(f"Error: {e}")
```

---

## Vanliga Exception Types

| Exception | Nar |
|-----------|-----|
| `ValueError` | Fel varde |
| `TypeError` | Fel typ |
| `FileNotFoundError` | Fil saknas |
| `KeyError` | Dict-key saknas |
| `IndexError` | List index out of range |
| `ConnectionError` | Natverksfel |
| `TimeoutError` | Timeout |

---

## Praktiskt: Retry Pattern

```python
import time

def retry(func, max_attempts=3, delay=1):
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
                time.sleep(delay)
            else:
                raise

# Anvandning
def unstable_api_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("API timeout")
    return {"status": "ok"}

try:
    result = retry(unstable_api_call, max_attempts=5)
    print(f"Success: {result}")
except ConnectionError:
    print("All retries failed")
```

---

## Sammanfattning

| Syntax | Anvandning |
|--------|------------|
| `try/except` | Fanga fel |
| `except Type as e` | Specifikt fel |
| `finally` | Kors alltid |
| `raise` | Kasta fel |
"""
}


# =============================================================================
# ALL NODES COLLECTION
# =============================================================================

PYTHON_SKILLSMAP_NODES: List[Dict[str, Any]] = [
    NODE_01_PYTHON_BASICS,
    NODE_02_COLLECTIONS,
    NODE_03_CONTROL_FLOW,
    NODE_04_FUNCTIONS,
    NODE_05_FILE_IO,
    NODE_06_ERROR_HANDLING,
]

# =============================================================================
# NODE 7: OOP BASICS - Classes, Objects, Inheritance
# =============================================================================

NODE_07_OOP_BASICS: Dict[str, Any] = {
    "id": "python_oop_basics",
    "title": "OOP Basics",
    "description": "Classes, objects, inheritance och encapsulation",
    "icon": "🏛️",
    "difficulty": 3,
    "estimated_time_minutes": 45,
    "prerequisites": ["python_functions", "python_error_handling"],
    "skills_taught": [
        "Classes och objects",
        "__init__ constructor",
        "Instance och class attributes",
        "Inheritance och super()",
        "Magic methods",
        "Property decorators"
    ],
    "real_world_context": "Som DevOps bygger du Ansible-liknande inventory-klasser, boto3-wrappers och API-clients som återanvändbara objekt.",
    "content": """# 🏛️ OOP Basics - Objektorienterad Python för DevOps

## Varför detta är viktigt

Som DevOps-ingenjör behöver du bygga återanvändbara komponenter: AWS/Azure/GCP clients, server inventory management, configuration builders. OOP ger dig strukturen för att skapa maintainable kod.

## Vad du kommer lära dig

- Förstå classes och objects i Python
- Implementera __init__ constructor och attributes
- Använda inheritance och super() för kodåteranvändning
- Skapa property decorators och magic methods

---

## 📚 Din Första Klass

```python
class Server:
    '''Representerar en server i infrastructure.'''

    def __init__(self, hostname: str, ip: str, role: str = "web"):
        self.hostname = hostname
        self.ip = ip
        self.role = role
        self.status = "stopped"

    def start(self):
        '''Starta servern.'''
        self.status = "running"
        print(f"Starting {self.hostname}...")

    def stop(self):
        '''Stoppa servern.'''
        self.status = "stopped"
        print(f"Stopping {self.hostname}...")

    def __str__(self):
        return f"Server({self.hostname}, {self.ip}, {self.status})"

    def __repr__(self):
        return f"Server('{self.hostname}', '{self.ip}', role='{self.role}')"


# Anvandning
web1 = Server("web-01", "10.0.0.10", "web")
web1.start()
print(web1)  # Server(web-01, 10.0.0.10, running)
```

---

## 2. Class vs Instance Attributes

```python
class Container:
    '''Docker container model.'''

    # Class attribute - delas av alla instanser
    runtime = "docker"
    container_count = 0

    def __init__(self, name: str, image: str):
        # Instance attributes - unika per instans
        self.name = name
        self.image = image
        self.container_id = None

        # Uppdatera class attribute
        Container.container_count += 1

    @classmethod
    def get_count(cls):
        '''Returnera antal containers.'''
        return cls.container_count

    @staticmethod
    def is_valid_name(name: str) -> bool:
        '''Validera container name.'''
        import re
        return bool(re.match(r'^[a-z0-9][a-z0-9_.-]*$', name))


# Anvandning
c1 = Container("nginx-01", "nginx:latest")
c2 = Container("redis-cache", "redis:alpine")

print(Container.get_count())  # 2
print(Container.is_valid_name("my-app"))  # True
```

---

## 3. Inheritance - Arvning

```python
class CloudResource:
    '''Base class for cloud resources.'''

    def __init__(self, name: str, region: str):
        self.name = name
        self.region = region
        self.tags = {}
        self.created_at = None

    def tag(self, key: str, value: str):
        self.tags[key] = value

    def describe(self) -> dict:
        return {
            "name": self.name,
            "region": self.region,
            "tags": self.tags
        }


class EC2Instance(CloudResource):
    '''AWS EC2 Instance.'''

    def __init__(self, name: str, region: str, instance_type: str):
        # Anropa parent __init__
        super().__init__(name, region)
        self.instance_type = instance_type
        self.state = "stopped"
        self.instance_id = None

    def start(self):
        self.state = "running"
        print(f"Starting EC2 instance {self.name}...")

    def describe(self) -> dict:
        # Utoka parent-metoden
        info = super().describe()
        info.update({
            "instance_type": self.instance_type,
            "state": self.state,
            "instance_id": self.instance_id
        })
        return info


class S3Bucket(CloudResource):
    '''AWS S3 Bucket.'''

    def __init__(self, name: str, region: str):
        super().__init__(name, region)
        self.versioning = False
        self.objects = []

    def enable_versioning(self):
        self.versioning = True

    def put_object(self, key: str, content: str):
        self.objects.append({"key": key, "size": len(content)})


# Polymorfism i aktion
resources = [
    EC2Instance("web-server", "eu-north-1", "t3.micro"),
    S3Bucket("my-bucket", "eu-north-1"),
]

for resource in resources:
    resource.tag("Environment", "production")
    print(resource.describe())
```

---

## 4. Property Decorators

```python
class KubernetesDeployment:
    '''K8s Deployment model med validation.'''

    def __init__(self, name: str, image: str, replicas: int = 1):
        self.name = name
        self._image = image
        self._replicas = replicas

    @property
    def replicas(self) -> int:
        '''Getter for replicas.'''
        return self._replicas

    @replicas.setter
    def replicas(self, value: int):
        '''Setter med validation.'''
        if not isinstance(value, int) or value < 0:
            raise ValueError("Replicas must be non-negative integer")
        if value > 100:
            raise ValueError("Max 100 replicas allowed")
        self._replicas = value

    @property
    def image(self) -> str:
        return self._image

    @image.setter
    def image(self, value: str):
        if ":" not in value:
            value = f"{value}:latest"
        self._image = value

    @property
    def manifest(self) -> dict:
        '''Read-only property for K8s manifest.'''
        return {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {"name": self.name},
            "spec": {
                "replicas": self.replicas,
                "template": {
                    "spec": {
                        "containers": [{"name": self.name, "image": self.image}]
                    }
                }
            }
        }


# Anvandning
deploy = KubernetesDeployment("nginx", "nginx")
deploy.replicas = 3
deploy.image = "nginx"  # Blir nginx:latest

print(deploy.manifest)
```

---

## 5. Magic Methods (Dunder Methods)

```python
class ServerInventory:
    '''Custom container for servers.'''

    def __init__(self):
        self._servers = {}

    def __len__(self):
        '''len(inventory)'''
        return len(self._servers)

    def __getitem__(self, hostname: str):
        '''inventory["web-01"]'''
        return self._servers[hostname]

    def __setitem__(self, hostname: str, server):
        '''inventory["web-01"] = server'''
        self._servers[hostname] = server

    def __delitem__(self, hostname: str):
        '''del inventory["web-01"]'''
        del self._servers[hostname]

    def __contains__(self, hostname: str):
        '''if "web-01" in inventory'''
        return hostname in self._servers

    def __iter__(self):
        '''for server in inventory'''
        return iter(self._servers.values())

    def __repr__(self):
        return f"ServerInventory({len(self)} servers)"


# Anvandning
inventory = ServerInventory()
inventory["web-01"] = Server("web-01", "10.0.0.1")
inventory["web-02"] = Server("web-02", "10.0.0.2")

print(len(inventory))         # 2
print("web-01" in inventory)  # True

for server in inventory:
    print(server)
```

---

## 6. Dataclasses - Modern Python OOP

```python
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class ContainerSpec:
    '''Container specification using dataclass.'''
    name: str
    image: str
    cpu: str = "100m"
    memory: str = "128Mi"
    ports: List[int] = field(default_factory=list)
    env_vars: dict = field(default_factory=dict)
    created: datetime = field(default_factory=datetime.now)

    def to_yaml(self) -> str:
        '''Convert to YAML-like string.'''
        return f'''
containers:
- name: {self.name}
  image: {self.image}
  resources:
    limits:
      cpu: {self.cpu}
      memory: {self.memory}
  ports:
{self._format_ports()}
'''.strip()

    def _format_ports(self) -> str:
        if not self.ports:
            return "    []"
        lines = [f"    - containerPort: {p}" for p in self.ports]
        return "\\n".join(lines)


# Dataclasses ger automatiskt:
# - __init__ baserat pa falt
# - __repr__
# - __eq__ for jamforelser

nginx = ContainerSpec(
    name="nginx",
    image="nginx:1.21",
    ports=[80, 443],
    env_vars={"ENV": "production"}
)

print(nginx)
# ContainerSpec(name='nginx', image='nginx:1.21', ...)
```

---

## 7. Praktiskt Exempel: Infrastructure Builder

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class NetworkConfig:
    vpc_cidr: str = "10.0.0.0/16"
    subnets: List[str] = field(default_factory=lambda: ["10.0.1.0/24", "10.0.2.0/24"])


@dataclass
class InstanceConfig:
    instance_type: str = "t3.micro"
    ami: str = "ami-12345678"
    key_name: str = "my-key"


class InfrastructureBuilder:
    '''Builder pattern for infrastructure.'''

    def __init__(self, name: str):
        self.name = name
        self.network = NetworkConfig()
        self.instances = []
        self.security_groups = []

    def with_network(self, vpc_cidr: str, subnets: List[str] = None):
        '''Configure network.'''
        self.network.vpc_cidr = vpc_cidr
        if subnets:
            self.network.subnets = subnets
        return self  # For chaining

    def add_instance(self, name: str, **kwargs):
        '''Add an instance.'''
        config = InstanceConfig(**kwargs) if kwargs else InstanceConfig()
        self.instances.append({"name": name, "config": config})
        return self

    def add_security_group(self, name: str, rules: List[Dict]):
        '''Add a security group.'''
        self.security_groups.append({"name": name, "rules": rules})
        return self

    def build(self) -> Dict[str, Any]:
        '''Build infrastructure spec.'''
        return {
            "name": self.name,
            "network": {
                "vpc_cidr": self.network.vpc_cidr,
                "subnets": self.network.subnets
            },
            "instances": self.instances,
            "security_groups": self.security_groups
        }


# Builder pattern med method chaining
infra = (
    InfrastructureBuilder("production")
    .with_network("10.0.0.0/16", ["10.0.1.0/24", "10.0.2.0/24"])
    .add_instance("web-01", instance_type="t3.small")
    .add_instance("web-02", instance_type="t3.small")
    .add_security_group("web-sg", [{"port": 80, "cidr": "0.0.0.0/0"}])
    .build()
)

print(infra)
```

---

## Ovning: Bygg en Service Mesh Model

Skapa klasser for:
1. `Service` - namn, port, endpoints
2. `LoadBalancer` - namn, services, algorithm
3. `ServiceMesh` - services, load_balancers, add_service(), route()

```python
# Din losning har:

class Service:
    def __init__(self, name: str, port: int):
        self.name = name
        self.port = port
        self.endpoints = []

    def add_endpoint(self, ip: str):
        self.endpoints.append(ip)


class LoadBalancer:
    def __init__(self, name: str, algorithm: str = "round_robin"):
        self.name = name
        self.algorithm = algorithm
        self.services = []

    def add_service(self, service: Service):
        self.services.append(service)


class ServiceMesh:
    def __init__(self):
        self.services = {}
        self.load_balancers = {}

    def register_service(self, service: Service):
        self.services[service.name] = service

    def add_load_balancer(self, lb: LoadBalancer):
        self.load_balancers[lb.name] = lb
```

---

## Sammanfattning

| Koncept | Anvandning |
|---------|------------|
| `class` | Definiera ny typ |
| `__init__` | Constructor |
| `self` | Referens till instans |
| `super()` | Anropa parent-klass |
| `@property` | Getter/setter |
| `@classmethod` | Metod pa klassen |
| `@staticmethod` | Statisk funktion |
| `@dataclass` | Modern OOP shorthand |
"""
}


# =============================================================================
# NODE 8: OS & SYSTEM INTERACTION
# =============================================================================

NODE_08_OS_SYSTEM: Dict[str, Any] = {
    "id": "python_os_system",
    "title": "OS & System Interaction",
    "description": "Arbeta med filer, paths, environment och system",
    "icon": "🖥️",
    "difficulty": 3,
    "estimated_time_minutes": 35,
    "prerequisites": ["python_file_io"],
    "skills_taught": [
        "os module basics",
        "pathlib for modern paths",
        "Environment variables",
        "System information",
        "shutil for file operations"
    ],
    "real_world_context": "Varje DevOps-script behover hantera paths, environment variables och systeminfo. Detta ar karnkunskap.",
    "content": """# 🖥️ OS & System Interaction

## Varför detta är viktigt

Varje DevOps-script behöver hantera paths, environment variables och systeminformation. Detta är kärnkunskap för all automation och scripting.

## Vad du kommer lära dig

- Förstå os-modulen för systeminteraktion
- Implementera pathlib för modern path-hantering
- Använda environment variables säkert
- Hämta systeminformation programmatiskt

---

## 📚 pathlib - Modern Path Handling

`pathlib` är det moderna sättet att hantera filepaths:

```python
from pathlib import Path


# Skapa paths
home = Path.home()
current = Path.cwd()
config_dir = Path("/etc/nginx")

# Path operations
app_dir = Path("/opt/myapp")
config_file = app_dir / "config" / "app.yaml"  # Snyggt!

print(config_file)  # /opt/myapp/config/app.yaml


# Path properties
path = Path("/var/log/nginx/access.log")

print(path.name)      # access.log
print(path.stem)      # access
print(path.suffix)    # .log
print(path.parent)    # /var/log/nginx
print(path.parts)     # ('/', 'var', 'log', 'nginx', 'access.log')


# Kontrollera existens och typ
path = Path("/etc/passwd")
print(path.exists())     # True
print(path.is_file())    # True
print(path.is_dir())     # False


# Lista filer
log_dir = Path("/var/log")
for log_file in log_dir.glob("*.log"):
    print(log_file)

# Rekursivt
for py_file in Path(".").rglob("*.py"):
    print(py_file)


# Skapa directories
new_dir = Path("/tmp/myapp/logs")
new_dir.mkdir(parents=True, exist_ok=True)


# Lasa/skriva filer
config_path = Path("config.yaml")
content = config_path.read_text()
config_path.write_text("key: value")
```

---

## 2. os Module

```python
import os


# Environment variables
home = os.environ.get("HOME")
path = os.environ.get("PATH", "/usr/bin")

# Satt environment
os.environ["MY_VAR"] = "value"


# Arbeta med directories
os.getcwd()           # Current directory
os.chdir("/tmp")      # Byt directory
os.listdir("/etc")    # Lista filer


# Fil-information
info = os.stat("/etc/passwd")
print(info.st_size)    # Storlek i bytes
print(info.st_mtime)   # Modification time
print(info.st_mode)    # Permissions


# Skapa/ta bort
os.makedirs("/tmp/a/b/c", exist_ok=True)  # mkdir -p
os.remove("file.txt")                      # rm
os.rmdir("empty_dir")                      # rmdir


# Walk directory tree
for root, dirs, files in os.walk("/var/log"):
    for file in files:
        if file.endswith(".log"):
            print(os.path.join(root, file))
```

---

## 3. Environment Variable Management

```python
import os
from pathlib import Path
from typing import Dict, Any


def load_env_file(path: str) -> Dict[str, str]:
    '''Load .env file into dict.'''
    env_vars = {}
    env_path = Path(path)

    if not env_path.exists():
        return env_vars

    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            # Remove quotes
            value = value.strip("\"'")
            env_vars[key.strip()] = value

    return env_vars


def get_config() -> Dict[str, Any]:
    '''Get configuration from environment.'''
    return {
        "debug": os.environ.get("DEBUG", "false").lower() == "true",
        "database_url": os.environ.get("DATABASE_URL"),
        "redis_host": os.environ.get("REDIS_HOST", "localhost"),
        "redis_port": int(os.environ.get("REDIS_PORT", "6379")),
        "log_level": os.environ.get("LOG_LEVEL", "INFO"),
    }


# Ladda .env och applicera
env_vars = load_env_file(".env")
os.environ.update(env_vars)

config = get_config()
print(config)
```

---

## 4. shutil - High-Level File Operations

```python
import shutil
from pathlib import Path


# Kopiera fil
shutil.copy("source.txt", "dest.txt")           # Behall permissions
shutil.copy2("source.txt", "dest.txt")          # Behall metadata


# Kopiera directory
shutil.copytree("src_dir", "dst_dir")
shutil.copytree("src", "dst", dirs_exist_ok=True)  # Overwrite OK


# Flytta/rename
shutil.move("old.txt", "new.txt")
shutil.move("file.txt", "/new/location/file.txt")


# Ta bort directory med innehall
shutil.rmtree("/tmp/myapp", ignore_errors=True)


# Disk usage
usage = shutil.disk_usage("/")
print(f"Total: {usage.total // (2**30)} GB")
print(f"Used: {usage.used // (2**30)} GB")
print(f"Free: {usage.free // (2**30)} GB")


# Skapa arkiv
shutil.make_archive("backup", "gztar", "/var/log/myapp")
# Skapar backup.tar.gz
```

---

## 5. platform - System Information

```python
import platform


# OS info
print(platform.system())        # Linux, Darwin, Windows
print(platform.release())       # 5.4.0-42-generic
print(platform.version())       # #46-Ubuntu SMP Fri Jul 10
print(platform.machine())       # x86_64, arm64


# Python info
print(platform.python_version())      # 3.11.4
print(platform.python_implementation()) # CPython


# Komplett info
print(platform.platform())
# Linux-5.4.0-42-generic-x86_64-with-glibc2.31


# Exempel: Platform-specific code
if platform.system() == "Windows":
    config_path = Path(os.environ["APPDATA"]) / "myapp"
elif platform.system() == "Darwin":
    config_path = Path.home() / "Library" / "Application Support" / "myapp"
else:  # Linux
    config_path = Path.home() / ".config" / "myapp"
```

---

## 6. Praktiskt Exempel: DevOps Utility Functions

```python
import os
import shutil
import platform
from pathlib import Path
from datetime import datetime


def get_system_info() -> dict:
    '''Samla system information.'''
    return {
        "os": platform.system(),
        "os_version": platform.release(),
        "hostname": platform.node(),
        "machine": platform.machine(),
        "python_version": platform.python_version(),
        "user": os.environ.get("USER", os.environ.get("USERNAME")),
        "home": str(Path.home()),
        "cwd": str(Path.cwd()),
    }


def ensure_directory(path: str, clean: bool = False) -> Path:
    '''Ensure directory exists, optionally clean it.'''
    dir_path = Path(path)

    if clean and dir_path.exists():
        shutil.rmtree(dir_path)

    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def backup_file(source: str, backup_dir: str = "/tmp/backups") -> Path:
    '''Backup file with timestamp.'''
    source_path = Path(source)
    if not source_path.exists():
        raise FileNotFoundError(f"{source} not found")

    backup_path = Path(backup_dir)
    backup_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{source_path.stem}_{timestamp}{source_path.suffix}"
    dest = backup_path / backup_name

    shutil.copy2(source_path, dest)
    return dest


def find_large_files(directory: str, min_size_mb: int = 100) -> list:
    '''Find files larger than min_size_mb.'''
    large_files = []
    min_bytes = min_size_mb * 1024 * 1024

    for path in Path(directory).rglob("*"):
        if path.is_file():
            try:
                if path.stat().st_size > min_bytes:
                    large_files.append({
                        "path": str(path),
                        "size_mb": path.stat().st_size / (1024 * 1024)
                    })
            except PermissionError:
                continue

    return sorted(large_files, key=lambda x: x["size_mb"], reverse=True)


# Anvandning
info = get_system_info()
print(f"Running on {info['os']} as {info['user']}")

work_dir = ensure_directory("/tmp/work", clean=True)
print(f"Working directory: {work_dir}")
```

---

## Sammanfattning

| Module | Anvandning |
|--------|------------|
| `pathlib.Path` | Modern path handling |
| `os.environ` | Environment variables |
| `os.walk` | Directory traversal |
| `shutil.copy/move` | File operations |
| `shutil.rmtree` | Remove directory tree |
| `platform` | System information |
"""
}


# =============================================================================
# NODE 9: SUBPROCESS & SHELL COMMANDS
# =============================================================================

NODE_09_SUBPROCESS: Dict[str, Any] = {
    "id": "python_subprocess",
    "title": "Subprocess & Shell Commands",
    "description": "Kör externa kommandon och script frän Python",
    "icon": "⚡",
    "difficulty": 3,
    "estimated_time_minutes": 40,
    "prerequisites": ["python_os_system", "python_error_handling"],
    "skills_taught": [
        "subprocess.run() basics",
        "Capturing output",
        "Error handling",
        "Pipes och redirects",
        "Timeout och signals",
        "Security best practices"
    ],
    "real_world_context": "Som DevOps kör du konstant shell commands: git, docker, kubectl, terraform. subprocess är bryggan mellan Python och shell.",
    "content": """# ⚡ Subprocess & Shell Commands

## Varför detta är viktigt

Som DevOps-ingenjör kör du konstant shell commands: git, docker, kubectl, terraform. subprocess är bryggan mellan Python och shell - det låter dig automatisera allt.

## Vad du kommer lära dig

- Förstå subprocess.run() för shell-kommandon
- Implementera input/output-hantering
- Använda timeout och error handling
- Följa security best practices

---

## 📚 subprocess.run() - Basics

```python
import subprocess


# Enklaste sattet
result = subprocess.run(["ls", "-la"])
print(f"Exit code: {result.returncode}")


# Fanga output
result = subprocess.run(
    ["ls", "-la"],
    capture_output=True,  # Fanga stdout/stderr
    text=True              # Som string, inte bytes
)

print(result.stdout)
print(result.stderr)
print(result.returncode)


# Equivalent till capture_output=True:
result = subprocess.run(
    ["ls", "-la"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
```

---

## 2. Error Handling

```python
import subprocess


# check=True kastar exception pa fel
try:
    result = subprocess.run(
        ["ls", "/nonexistent"],
        capture_output=True,
        text=True,
        check=True  # Raise CalledProcessError if returncode != 0
    )
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}")
    print(f"stderr: {e.stderr}")


# Timeout
try:
    result = subprocess.run(
        ["sleep", "10"],
        timeout=5  # Sekunder
    )
except subprocess.TimeoutExpired:
    print("Command timed out!")


# Kombinerat
def run_command(cmd: list, timeout: int = 30) -> str:
    '''Run command with error handling.'''
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            timeout=timeout
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Command failed: {e.stderr}")
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"Command timed out after {timeout}s")
```

---

## 3. Shell Mode (Varsamt!)

```python
import subprocess


# shell=True - kor via shell
# VARNING: Saker risk med user input!
result = subprocess.run(
    "ls -la | grep .py",  # String, inte lista
    shell=True,
    capture_output=True,
    text=True
)


# FARLIGT - command injection!
user_input = "file.txt; rm -rf /"  # Malicious input
subprocess.run(f"cat {user_input}", shell=True)  # DON'T DO THIS!


# SAKERT - anvand lista utan shell=True
filename = "file.txt; rm -rf /"  # Input fran user
subprocess.run(["cat", filename])  # Sakert - behandlas som filnamn
```

---

## 4. Input till Process

```python
import subprocess


# Skicka data via stdin
result = subprocess.run(
    ["grep", "error"],
    input="line1\\nerror found\\nline3",
    capture_output=True,
    text=True
)
print(result.stdout)  # error found


# Pipe till process
log_content = Path("/var/log/syslog").read_text()
result = subprocess.run(
    ["grep", "-c", "error"],
    input=log_content,
    capture_output=True,
    text=True
)
print(f"Errors found: {result.stdout.strip()}")
```

---

## 5. DevOps Command Wrappers

```python
import subprocess
from typing import Optional


class CommandRunner:
    '''Safe command runner with logging.'''

    def __init__(self, dry_run: bool = False, verbose: bool = True):
        self.dry_run = dry_run
        self.verbose = verbose

    def run(self, cmd: list, check: bool = True,
            timeout: int = 300) -> subprocess.CompletedProcess:
        '''Run command with standardized handling.'''
        cmd_str = " ".join(cmd)

        if self.verbose:
            print(f"$ {cmd_str}")

        if self.dry_run:
            print(f"[DRY RUN] Would execute: {cmd_str}")
            return subprocess.CompletedProcess(cmd, 0, "", "")

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=check,
                timeout=timeout
            )

            if self.verbose and result.stdout:
                print(result.stdout)

            return result

        except subprocess.CalledProcessError as e:
            print(f"ERROR: {e.stderr}")
            raise


# Git wrapper
def git_status(repo_path: str = ".") -> str:
    result = subprocess.run(
        ["git", "-C", repo_path, "status", "--porcelain"],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout


def git_commit(message: str, repo_path: str = ".") -> None:
    subprocess.run(
        ["git", "-C", repo_path, "add", "-A"],
        check=True
    )
    subprocess.run(
        ["git", "-C", repo_path, "commit", "-m", message],
        check=True
    )


# Docker wrapper
def docker_ps() -> list:
    result = subprocess.run(
        ["docker", "ps", "--format", "{{.ID}}\\t{{.Names}}\\t{{.Status}}"],
        capture_output=True,
        text=True,
        check=True
    )
    containers = []
    for line in result.stdout.strip().split("\\n"):
        if line:
            id_, name, status = line.split("\\t")
            containers.append({"id": id_, "name": name, "status": status})
    return containers


def docker_logs(container: str, tail: int = 100) -> str:
    result = subprocess.run(
        ["docker", "logs", "--tail", str(tail), container],
        capture_output=True,
        text=True
    )
    return result.stdout + result.stderr
```

---

## 6. Kubectl Wrapper

```python
import subprocess
import json
from typing import List, Dict, Any


class Kubectl:
    '''Kubernetes kubectl wrapper.'''

    def __init__(self, context: str = None, namespace: str = "default"):
        self.context = context
        self.namespace = namespace

    def _build_command(self, *args) -> List[str]:
        cmd = ["kubectl"]
        if self.context:
            cmd.extend(["--context", self.context])
        cmd.extend(["-n", self.namespace])
        cmd.extend(args)
        return cmd

    def _run(self, *args, json_output: bool = False) -> Any:
        cmd = self._build_command(*args)
        if json_output:
            cmd.extend(["-o", "json"])

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )

        if json_output:
            return json.loads(result.stdout)
        return result.stdout

    def get_pods(self) -> List[Dict]:
        '''Get all pods in namespace.'''
        data = self._run("get", "pods", json_output=True)
        return data.get("items", [])

    def get_pod_logs(self, pod_name: str, tail: int = 100) -> str:
        '''Get pod logs.'''
        return self._run("logs", pod_name, "--tail", str(tail))

    def apply(self, manifest_path: str) -> str:
        '''Apply manifest.'''
        return self._run("apply", "-f", manifest_path)

    def delete(self, resource_type: str, name: str) -> str:
        '''Delete resource.'''
        return self._run("delete", resource_type, name)


# Anvandning
k8s = Kubectl(namespace="production")
pods = k8s.get_pods()
for pod in pods:
    name = pod["metadata"]["name"]
    status = pod["status"]["phase"]
    print(f"{name}: {status}")
```

---

## 7. Async Subprocess (for Advanced)

```python
import asyncio


async def run_command_async(cmd: list) -> str:
    '''Run command asynchronously.'''
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        raise RuntimeError(f"Command failed: {stderr.decode()}")

    return stdout.decode()


async def run_multiple_commands():
    '''Run multiple commands in parallel.'''
    commands = [
        ["kubectl", "get", "pods"],
        ["docker", "ps"],
        ["git", "status"],
    ]

    tasks = [run_command_async(cmd) for cmd in commands]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for cmd, result in zip(commands, results):
        if isinstance(result, Exception):
            print(f"{cmd[0]} failed: {result}")
        else:
            print(f"{cmd[0]} output: {result[:100]}...")


# Kor async
asyncio.run(run_multiple_commands())
```

---

## Security Best Practices

1. **Aldrig** använd `shell=True` med user input
2. Använd listor `["cmd", "arg"]` istället för strängar
3. Validera och sanitera alla inputs
4. Använd absoluta paths för kommandon
5. Sätt timeouts för att undvika hängande processer
6. Fånga och logga errors ordentligt

---

## Sammanfattning

| Funktion | Anvandning |
|----------|------------|
| `subprocess.run()` | Kor command och vanta |
| `capture_output=True` | Fanga stdout/stderr |
| `text=True` | Output som string |
| `check=True` | Raise pa fel |
| `timeout=N` | Max tid i sekunder |
| `shell=True` | Kor via shell (farligt!) |
| `input="data"` | Skicka till stdin |
"""
}


# =============================================================================
# NODE 10: JSON & YAML
# =============================================================================

NODE_10_JSON_YAML: Dict[str, Any] = {
    "id": "python_json_yaml",
    "title": "JSON & YAML",
    "description": "Arbeta med JSON och YAML - DevOps dataformat",
    "icon": "📋",
    "difficulty": 2,
    "estimated_time_minutes": 30,
    "prerequisites": ["python_file_io", "python_collections"],
    "skills_taught": [
        "JSON parsing och serialization",
        "YAML parsing med PyYAML",
        "Config file handling",
        "Nested data structures",
        "Schema validation"
    ],
    "real_world_context": "JSON och YAML är överallt i DevOps: Kubernetes manifests, Ansible playbooks, Terraform configs, API responses.",
    "content": """# 📋 JSON & YAML - DevOps Data Formats

## Varför detta är viktigt

JSON och YAML är överallt i DevOps: Kubernetes manifests, Ansible playbooks, Terraform configs, API responses. Du måste kunna läsa, skriva och manipulera dessa format effektivt.

## Vad du kommer lära dig

- Förstå JSON parsing och serialization
- Implementera YAML-hantering med PyYAML
- Hantera nested data structures
- Validera config-filer

---

## 📚 JSON Basics

```python
import json
from pathlib import Path


# Python dict till JSON string
data = {
    "name": "web-server",
    "port": 8080,
    "debug": True,
    "tags": ["production", "critical"]
}

json_string = json.dumps(data)
print(json_string)
# {"name": "web-server", "port": 8080, "debug": true, "tags": ["production", "critical"]}


# Pretty print
json_pretty = json.dumps(data, indent=2)
print(json_pretty)


# JSON string till Python dict
json_input = '{"name": "api", "version": "1.0"}'
parsed = json.loads(json_input)
print(parsed["name"])  # api


# Skriva till fil
with open("config.json", "w") as f:
    json.dump(data, f, indent=2)

# Eller med pathlib
Path("config.json").write_text(json.dumps(data, indent=2))


# Lasa fran fil
with open("config.json") as f:
    config = json.load(f)

# Eller
config = json.loads(Path("config.json").read_text())
```

---

## 2. JSON Best Practices

```python
import json
from datetime import datetime
from pathlib import Path


# Custom encoder for special types
class DevOpsEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Path):
            return str(obj)
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return super().default(obj)


# Anvandning
data = {
    "created": datetime.now(),
    "config_path": Path("/etc/app/config.yaml"),
}

json_string = json.dumps(data, cls=DevOpsEncoder, indent=2)
print(json_string)


# Safe JSON loading
def load_json_safe(path: str, default: dict = None) -> dict:
    '''Load JSON file safely with default.'''
    try:
        return json.loads(Path(path).read_text())
    except FileNotFoundError:
        return default or {}
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {path}: {e}")
        return default or {}


config = load_json_safe("config.json", {"debug": False})
```

---

## 3. YAML Basics

Installera: `pip install pyyaml`

```python
import yaml
from pathlib import Path


# Python dict till YAML
data = {
    "apiVersion": "v1",
    "kind": "ConfigMap",
    "metadata": {
        "name": "app-config",
        "namespace": "default"
    },
    "data": {
        "DATABASE_URL": "postgres://localhost/db",
        "DEBUG": "false"
    }
}

yaml_string = yaml.dump(data, default_flow_style=False)
print(yaml_string)
# apiVersion: v1
# kind: ConfigMap
# metadata:
#   name: app-config
#   namespace: default
# data:
#   DATABASE_URL: postgres://localhost/db
#   DEBUG: 'false'


# YAML till Python
yaml_input = '''
name: my-app
version: 1.0.0
dependencies:
  - flask
  - redis
  - celery
'''

parsed = yaml.safe_load(yaml_input)
print(parsed["dependencies"])  # ['flask', 'redis', 'celery']


# Multipla YAML documents
multi_yaml = '''
---
name: service-a
port: 8080
---
name: service-b
port: 8081
'''

documents = list(yaml.safe_load_all(multi_yaml))
for doc in documents:
    print(doc["name"])
```

---

## 4. Kubernetes YAML Handling

```python
import yaml
from pathlib import Path
from typing import List, Dict, Any


def load_k8s_manifests(path: str) -> List[Dict]:
    '''Load Kubernetes manifests from file or directory.'''
    p = Path(path)
    manifests = []

    if p.is_file():
        with open(p) as f:
            for doc in yaml.safe_load_all(f):
                if doc:  # Skip empty documents
                    manifests.append(doc)
    elif p.is_dir():
        for yaml_file in p.glob("*.yaml"):
            manifests.extend(load_k8s_manifests(str(yaml_file)))

    return manifests


def filter_by_kind(manifests: List[Dict], kind: str) -> List[Dict]:
    '''Filter manifests by Kubernetes kind.'''
    return [m for m in manifests if m.get("kind") == kind]


def generate_deployment(name: str, image: str, replicas: int = 1) -> Dict:
    '''Generate a Kubernetes Deployment manifest.'''
    return {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "name": name,
            "labels": {"app": name}
        },
        "spec": {
            "replicas": replicas,
            "selector": {
                "matchLabels": {"app": name}
            },
            "template": {
                "metadata": {
                    "labels": {"app": name}
                },
                "spec": {
                    "containers": [{
                        "name": name,
                        "image": image,
                        "ports": [{"containerPort": 80}]
                    }]
                }
            }
        }
    }


# Anvandning
deploy = generate_deployment("nginx", "nginx:1.21", replicas=3)
yaml_output = yaml.dump(deploy, default_flow_style=False)
Path("deployment.yaml").write_text(yaml_output)
```

---

## 5. Config File Handler

```python
import json
import yaml
from pathlib import Path
from typing import Dict, Any


class ConfigLoader:
    '''Universal config loader for JSON and YAML.'''

    @staticmethod
    def load(path: str) -> Dict[str, Any]:
        '''Load config file, auto-detect format.'''
        p = Path(path)
        content = p.read_text()

        if p.suffix in [".yaml", ".yml"]:
            return yaml.safe_load(content)
        elif p.suffix == ".json":
            return json.loads(content)
        else:
            # Try YAML first (superset of JSON)
            try:
                return yaml.safe_load(content)
            except yaml.YAMLError:
                return json.loads(content)

    @staticmethod
    def save(path: str, data: Dict[str, Any], format: str = None):
        '''Save config file.'''
        p = Path(path)

        if format is None:
            format = "yaml" if p.suffix in [".yaml", ".yml"] else "json"

        if format == "yaml":
            content = yaml.dump(data, default_flow_style=False)
        else:
            content = json.dumps(data, indent=2)

        p.write_text(content)

    @staticmethod
    def merge(base: Dict, override: Dict) -> Dict:
        '''Deep merge two configs.'''
        result = base.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = ConfigLoader.merge(result[key], value)
            else:
                result[key] = value
        return result


# Anvandning
base_config = ConfigLoader.load("config/base.yaml")
env_config = ConfigLoader.load("config/production.yaml")

final_config = ConfigLoader.merge(base_config, env_config)
ConfigLoader.save("config/compiled.yaml", final_config)
```

---

## 6. Ansible Inventory Parser

```python
import yaml
from pathlib import Path
from typing import Dict, List


def parse_ansible_inventory(path: str) -> Dict:
    '''Parse Ansible YAML inventory.'''
    inventory = yaml.safe_load(Path(path).read_text())

    result = {
        "all_hosts": [],
        "groups": {}
    }

    def process_group(name: str, data: Dict):
        if not isinstance(data, dict):
            return

        hosts = data.get("hosts", {})
        for host, vars in (hosts or {}).items():
            result["all_hosts"].append(host)
            if name not in result["groups"]:
                result["groups"][name] = []
            result["groups"][name].append({
                "host": host,
                "vars": vars or {}
            })

        children = data.get("children", {})
        for child_name, child_data in (children or {}).items():
            process_group(child_name, child_data)

    for group_name, group_data in inventory.items():
        process_group(group_name, group_data)

    return result


# Exempel inventory.yaml:
# all:
#   children:
#     webservers:
#       hosts:
#         web1:
#           ansible_host: 10.0.0.1
#         web2:
#           ansible_host: 10.0.0.2

inv = parse_ansible_inventory("inventory.yaml")
print(f"Total hosts: {len(inv['all_hosts'])}")
print(f"Groups: {list(inv['groups'].keys())}")
```

---

## Sammanfattning

| Funktion | Modul | Anvandning |
|----------|-------|------------|
| `json.dumps()` | json | Dict till JSON string |
| `json.loads()` | json | JSON string till dict |
| `json.dump()` | json | Skriv till fil |
| `json.load()` | json | Las fran fil |
| `yaml.dump()` | pyyaml | Dict till YAML |
| `yaml.safe_load()` | pyyaml | YAML till dict |
| `yaml.safe_load_all()` | pyyaml | Multi-doc YAML |
"""
}


# Add nodes to list
PYTHON_SKILLSMAP_NODES.extend([
    NODE_07_OOP_BASICS,
    NODE_08_OS_SYSTEM,
    NODE_09_SUBPROCESS,
    NODE_10_JSON_YAML,
])


# =============================================================================
# NODE 11: HTTP & APIs (requests library)
# =============================================================================

NODE_11_HTTP_APIS: Dict[str, Any] = {
    "id": "python_http_apis",
    "title": "HTTP & APIs",
    "description": "Arbeta med REST APIs och HTTP requests",
    "icon": "🌐",
    "difficulty": 3,
    "estimated_time_minutes": 40,
    "prerequisites": ["python_json_yaml", "python_error_handling"],
    "skills_taught": [
        "requests library",
        "GET, POST, PUT, DELETE",
        "Authentication methods",
        "Error handling",
        "Session management",
        "API wrappers"
    ],
    "real_world_context": "APIs är livsnerven i DevOps: GitHub API, AWS API, Slack webhooks, PagerDuty, monitoring endpoints.",
    "content": """# 🌐 HTTP & APIs med Python

## Varför detta är viktigt

APIs är livsnerven i DevOps: GitHub API, AWS API, Slack webhooks, PagerDuty, monitoring endpoints. Du behöver kunna kommunicera med alla dessa tjänster programmatiskt.

## Vad du kommer lära dig

- Förstå requests library för HTTP
- Implementera GET, POST, PUT, DELETE
- Hantera authentication och sessions
- Bygga API wrappers

---

## 📚 Installation

Installera: `pip install requests`

## 1. Requests Basics

```python
import requests


# GET request
response = requests.get("https://api.github.com/users/octocat")

print(response.status_code)  # 200
print(response.headers["content-type"])  # application/json
print(response.json())  # Parsed JSON som dict


# Med query parameters
response = requests.get(
    "https://api.github.com/search/repositories",
    params={
        "q": "kubernetes language:python",
        "sort": "stars",
        "per_page": 10
    }
)

repos = response.json()["items"]
for repo in repos:
    print(f"{repo['name']}: {repo['stargazers_count']} stars")


# POST request
response = requests.post(
    "https://httpbin.org/post",
    json={
        "name": "deployment",
        "version": "1.0"
    }
)
print(response.json())


# PUT request
response = requests.put(
    "https://api.example.com/resource/123",
    json={"status": "active"}
)


# DELETE request
response = requests.delete("https://api.example.com/resource/123")
```

---

## 2. Headers och Authentication

```python
import requests


# Custom headers
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Accept": "application/vnd.github.v3+json",
    "X-Custom-Header": "value"
}

response = requests.get(
    "https://api.github.com/user",
    headers=headers
)


# Basic Auth
response = requests.get(
    "https://api.example.com/data",
    auth=("username", "password")
)


# Token Auth (Bearer)
token = "ghp_xxxxxxxxxxxx"
response = requests.get(
    "https://api.github.com/user/repos",
    headers={"Authorization": f"token {token}"}
)
```

---

## 3. Error Handling

```python
import requests
from requests.exceptions import RequestException, Timeout, HTTPError


def api_request(url: str, method: str = "GET", **kwargs) -> dict:
    '''Make API request with error handling.'''
    try:
        response = requests.request(
            method,
            url,
            timeout=30,
            **kwargs
        )
        response.raise_for_status()  # Raise HTTPError for 4xx/5xx
        return response.json()

    except Timeout:
        raise RuntimeError(f"Request timed out: {url}")

    except HTTPError as e:
        if e.response.status_code == 404:
            raise RuntimeError(f"Resource not found: {url}")
        elif e.response.status_code == 401:
            raise RuntimeError("Authentication failed")
        elif e.response.status_code == 403:
            raise RuntimeError("Access forbidden - check permissions")
        elif e.response.status_code >= 500:
            raise RuntimeError(f"Server error: {e.response.status_code}")
        else:
            raise RuntimeError(f"HTTP error {e.response.status_code}")

    except RequestException as e:
        raise RuntimeError(f"Request failed: {e}")


# Anvandning
try:
    data = api_request("https://api.github.com/users/octocat")
    print(data["login"])
except RuntimeError as e:
    print(f"Error: {e}")
```

---

## 4. Sessions for Reuse

```python
import requests


# Session bevarar cookies och settings
session = requests.Session()
session.headers.update({
    "Authorization": "Bearer TOKEN",
    "Accept": "application/json"
})

# Alla requests anvander samma settings
response1 = session.get("https://api.example.com/user")
response2 = session.get("https://api.example.com/repos")
response3 = session.post("https://api.example.com/data", json={"key": "value"})

# Stang session
session.close()


# Som context manager
with requests.Session() as session:
    session.headers["Authorization"] = "Bearer TOKEN"
    response = session.get("https://api.example.com/data")
```

---

## 5. GitHub API Wrapper

```python
import requests
from typing import List, Dict, Optional


class GitHubAPI:
    '''GitHub API wrapper.'''

    BASE_URL = "https://api.github.com"

    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        })

    def _request(self, method: str, endpoint: str, **kwargs) -> dict:
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.request(method, url, timeout=30, **kwargs)
        response.raise_for_status()
        return response.json() if response.text else {}

    def get_user(self) -> dict:
        '''Get authenticated user.'''
        return self._request("GET", "/user")

    def list_repos(self, username: str = None) -> List[dict]:
        '''List repositories.'''
        endpoint = f"/users/{username}/repos" if username else "/user/repos"
        return self._request("GET", endpoint, params={"per_page": 100})

    def create_repo(self, name: str, private: bool = False) -> dict:
        '''Create a new repository.'''
        return self._request("POST", "/user/repos", json={
            "name": name,
            "private": private
        })

    def create_issue(self, owner: str, repo: str, title: str, body: str = "") -> dict:
        '''Create an issue.'''
        return self._request("POST", f"/repos/{owner}/{repo}/issues", json={
            "title": title,
            "body": body
        })

    def get_workflows(self, owner: str, repo: str) -> List[dict]:
        '''Get GitHub Actions workflows.'''
        data = self._request("GET", f"/repos/{owner}/{repo}/actions/workflows")
        return data.get("workflows", [])

    def trigger_workflow(self, owner: str, repo: str, workflow_id: str, ref: str = "main"):
        '''Trigger a workflow.'''
        self._request(
            "POST",
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches",
            json={"ref": ref}
        )


# Anvandning
github = GitHubAPI("ghp_xxxxxxxxxxxx")
user = github.get_user()
print(f"Logged in as: {user['login']}")

repos = github.list_repos()
for repo in repos[:5]:
    print(f"  - {repo['name']}")
```

---

## 6. Slack Webhook

```python
import requests
from typing import List, Dict, Optional


class SlackNotifier:
    '''Send messages to Slack.'''

    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send(self, text: str, blocks: List[Dict] = None) -> bool:
        '''Send message to Slack.'''
        payload = {"text": text}
        if blocks:
            payload["blocks"] = blocks

        response = requests.post(
            self.webhook_url,
            json=payload,
            timeout=10
        )
        return response.status_code == 200

    def send_deployment(self, service: str, version: str, env: str, status: str):
        '''Send deployment notification.'''
        color = "#36a64f" if status == "success" else "#ff0000"
        emoji = ":white_check_mark:" if status == "success" else ":x:"

        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{emoji} *Deployment {status.upper()}*"
                }
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*Service:*\\n{service}"},
                    {"type": "mrkdwn", "text": f"*Version:*\\n{version}"},
                    {"type": "mrkdwn", "text": f"*Environment:*\\n{env}"},
                    {"type": "mrkdwn", "text": f"*Status:*\\n{status}"}
                ]
            }
        ]

        return self.send(f"Deployment {status}: {service} v{version}", blocks)


# Anvandning
slack = SlackNotifier("https://hooks.slack.com/services/xxx/yyy/zzz")
slack.send_deployment("api-service", "1.2.3", "production", "success")
```

---

## 7. Retry Logic

```python
import requests
import time
from functools import wraps


def retry(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    '''Decorator for retrying failed requests.'''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            current_delay = delay

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    last_error = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed, retrying in {current_delay}s...")
                        time.sleep(current_delay)
                        current_delay *= backoff

            raise last_error
        return wrapper
    return decorator


@retry(max_attempts=3, delay=1.0)
def fetch_data(url: str) -> dict:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


# Anvandning
data = fetch_data("https://api.example.com/data")
```

---

## Sammanfattning

| Metod | Anvandning |
|-------|------------|
| `requests.get()` | Hamta data |
| `requests.post()` | Skicka data |
| `requests.put()` | Uppdatera data |
| `requests.delete()` | Ta bort data |
| `response.json()` | Parsa JSON response |
| `response.raise_for_status()` | Kasta exception pa fel |
| `requests.Session()` | Bevara state mellan requests |
"""
}


# =============================================================================
# NODE 12: VIRTUAL ENVIRONMENTS
# =============================================================================

NODE_12_VENV: Dict[str, Any] = {
    "id": "python_venv",
    "title": "Virtual Environments",
    "description": "Isolera Python-projekt med venv och pip",
    "icon": "📦",
    "difficulty": 2,
    "estimated_time_minutes": 25,
    "prerequisites": ["python_os_system"],
    "skills_taught": [
        "venv creation",
        "pip och requirements.txt",
        "pyproject.toml",
        "Dependency management",
        "Multiple Python versions"
    ],
    "real_world_context": "Varje Python-projekt behöver isolerade dependencies. venv är grundläggande för reproduzerbara builds.",
    "content": """# 📦 Virtual Environments

## Varför detta är viktigt

Varje Python-projekt behöver isolerade dependencies. venv är grundläggande för reproduzerbara builds och förhindrar "works on my machine"-problem.

## Vad du kommer lära dig

- Förstå varför virtual environments behövs
- Skapa och aktivera venv korrekt
- Hantera requirements.txt
- Använda pip freeze och pip install

---

## 📚 Skapa och Använda venv

```bash
# Skapa virtual environment
python3 -m venv .venv

# Aktivera (Linux/macOS)
source .venv/bin/activate

# Aktivera (Windows)
.\\.venv\\Scripts\\activate

# Kontrollera aktiv Python
which python
# /path/to/project/.venv/bin/python

# Installera packages
pip install requests flask redis

# Se installerade packages
pip list

# Avaktivera
deactivate
```

---

## 3. requirements.txt

```bash
# Exportera aktuella dependencies
pip freeze > requirements.txt

# Installera fran requirements.txt
pip install -r requirements.txt
```

**requirements.txt format:**

```text
# Production dependencies
flask==2.3.0
redis>=4.0,<5.0
requests~=2.28  # ~= betyder compatible version

# Development dependencies kan vara i separat fil
# requirements-dev.txt
-r requirements.txt  # Inkludera production deps
pytest>=7.0
black
mypy
```

---

## 4. pyproject.toml (Modern Standard)

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my-devops-tool"
version = "1.0.0"
description = "A DevOps automation tool"
requires-python = ">=3.9"
dependencies = [
    "requests>=2.28",
    "pyyaml>=6.0",
    "click>=8.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black",
    "mypy",
]

[project.scripts]
mytool = "my_devops_tool.cli:main"
```

```bash
# Installera med pip
pip install -e .          # Installera i editable mode
pip install -e ".[dev]"   # Med dev dependencies
```

---

## 5. Python Script for venv Management

```python
import subprocess
import sys
from pathlib import Path
from typing import List


def create_venv(path: str = ".venv") -> Path:
    '''Create a virtual environment.'''
    venv_path = Path(path)
    subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
    print(f"Created venv at {venv_path.absolute()}")
    return venv_path


def get_pip_path(venv_path: str = ".venv") -> Path:
    '''Get pip executable path in venv.'''
    venv = Path(venv_path)
    if sys.platform == "win32":
        return venv / "Scripts" / "pip.exe"
    return venv / "bin" / "pip"


def install_packages(packages: List[str], venv_path: str = ".venv"):
    '''Install packages in venv.'''
    pip = get_pip_path(venv_path)
    subprocess.run([str(pip), "install"] + packages, check=True)


def install_requirements(req_file: str = "requirements.txt", venv_path: str = ".venv"):
    '''Install from requirements file.'''
    pip = get_pip_path(venv_path)
    subprocess.run([str(pip), "install", "-r", req_file], check=True)


def export_requirements(output: str = "requirements.txt", venv_path: str = ".venv"):
    '''Export installed packages to requirements.txt.'''
    pip = get_pip_path(venv_path)
    result = subprocess.run(
        [str(pip), "freeze"],
        capture_output=True,
        text=True,
        check=True
    )
    Path(output).write_text(result.stdout)
    print(f"Exported to {output}")


# Anvandning
if __name__ == "__main__":
    create_venv(".venv")
    install_packages(["requests", "flask", "redis"])
    export_requirements()
```

---

## 6. Makefile for venv Automation

```makefile
.PHONY: venv install install-dev clean test

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

venv:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

install: venv
	$(PIP) install -r requirements.txt

install-dev: install
	$(PIP) install -r requirements-dev.txt

clean:
	rm -rf $(VENV)
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

test: install-dev
	$(PYTHON) -m pytest tests/

freeze:
	$(PIP) freeze > requirements.txt
```

---

## 7. Docker + venv Best Practices

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Skapa venv i container
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Installera dependencies forst (for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera kod
COPY . .

CMD ["python", "main.py"]
```

---

## 8. pyenv for Multiple Python Versions

```bash
# Installera pyenv (macOS)
brew install pyenv

# Installera Python version
pyenv install 3.11.4

# Satt lokal version for projekt
cd my-project
pyenv local 3.11.4  # Skapar .python-version

# Skapa venv med specifik version
python -m venv .venv
```

---

## Tips

1. **Aldrig** installera packages globalt (utan sudo pip)
2. Lagg `.venv/` i `.gitignore`
3. Commita `requirements.txt` eller `pyproject.toml`
4. Anvand `pip-tools` for advanced dependency management
5. Overväg `poetry` eller `pdm` for moderna projekt

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `python -m venv .venv` | Skapa venv |
| `source .venv/bin/activate` | Aktivera |
| `pip install -r requirements.txt` | Installera deps |
| `pip freeze > requirements.txt` | Exportera deps |
| `deactivate` | Avaktivera venv |
"""
}


# =============================================================================
# NODE 13: CLI TOOLS (argparse, click)
# =============================================================================

NODE_13_CLI_TOOLS: Dict[str, Any] = {
    "id": "python_cli_tools",
    "title": "CLI Tools",
    "description": "Bygg command-line tools med argparse och click",
    "icon": "💻",
    "difficulty": 3,
    "estimated_time_minutes": 40,
    "prerequisites": ["python_functions", "python_file_io"],
    "skills_taught": [
        "argparse basics",
        "Subcommands",
        "Click framework",
        "Environment variables",
        "Output formatting",
        "Exit codes"
    ],
    "real_world_context": "Varje DevOps-verktyg ar en CLI: kubectl, docker, terraform. Lär dig bygga professionella CLI-verktyg.",
    "content": """# 🖥️ CLI Tools med Python

## Varför detta är viktigt

Varje DevOps-verktyg är en CLI: kubectl, docker, terraform. Att kunna bygga professionella CLI-verktyg låter dig automatisera och standardisera arbetsflöden i ditt team.

## Vad du kommer lära dig

- Förstå argparse för argument-parsing
- Implementera subcommands som kubectl/git
- Använda Click framework för avancerade CLI
- Hantera exit codes korrekt

---

## 📚 argparse Basics

```python
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="DevOps deployment tool",
        epilog="Example: deploy.py --env production --version 1.2.3"
    )

    # Required argument
    parser.add_argument(
        "service",
        help="Service name to deploy"
    )

    # Optional arguments
    parser.add_argument(
        "-e", "--env",
        choices=["dev", "staging", "production"],
        default="dev",
        help="Target environment (default: dev)"
    )

    parser.add_argument(
        "-v", "--version",
        required=True,
        help="Version to deploy"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without executing"
    )

    parser.add_argument(
        "--replicas",
        type=int,
        default=2,
        help="Number of replicas (default: 2)"
    )

    args = parser.parse_args()

    print(f"Deploying {args.service} v{args.version} to {args.env}")
    print(f"Replicas: {args.replicas}")
    print(f"Dry run: {args.dry_run}")


if __name__ == "__main__":
    main()
```

**Anvandning:**
```bash
python deploy.py myapp -v 1.0.0 --env production --replicas 3
python deploy.py myapp -v 1.0.0 --dry-run
python deploy.py --help
```

---

## 2. Subcommands

```python
import argparse


def cmd_deploy(args):
    print(f"Deploying {args.service} v{args.version}")


def cmd_rollback(args):
    print(f"Rolling back {args.service} to {args.revision}")


def cmd_status(args):
    print(f"Status of {args.service}")


def main():
    parser = argparse.ArgumentParser(description="Kubernetes deployment tool")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # deploy command
    deploy_parser = subparsers.add_parser("deploy", help="Deploy a service")
    deploy_parser.add_argument("service", help="Service name")
    deploy_parser.add_argument("-v", "--version", required=True)
    deploy_parser.set_defaults(func=cmd_deploy)

    # rollback command
    rollback_parser = subparsers.add_parser("rollback", help="Rollback a deployment")
    rollback_parser.add_argument("service", help="Service name")
    rollback_parser.add_argument("-r", "--revision", type=int, default=1)
    rollback_parser.set_defaults(func=cmd_rollback)

    # status command
    status_parser = subparsers.add_parser("status", help="Check service status")
    status_parser.add_argument("service", help="Service name")
    status_parser.set_defaults(func=cmd_status)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```

---

## 3. Click Framework (Recommended)

Installera: `pip install click`

```python
import click


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
@click.pass_context
def cli(ctx, verbose):
    '''DevOps deployment tool.'''
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose


@cli.command()
@click.argument("service")
@click.option("--version", "-v", required=True, help="Version to deploy")
@click.option("--env", "-e",
              type=click.Choice(["dev", "staging", "prod"]),
              default="dev",
              help="Target environment")
@click.option("--replicas", "-r", type=int, default=2, help="Number of replicas")
@click.option("--dry-run", is_flag=True, help="Show what would be done")
@click.pass_context
def deploy(ctx, service, version, env, replicas, dry_run):
    '''Deploy a service.'''
    if ctx.obj["verbose"]:
        click.echo("Verbose mode enabled")

    click.echo(f"Deploying {service} v{version} to {env}")
    click.echo(f"Replicas: {replicas}")

    if dry_run:
        click.secho("DRY RUN - no changes made", fg="yellow")
        return

    # Simulate deployment
    with click.progressbar(range(10), label="Deploying") as bar:
        import time
        for _ in bar:
            time.sleep(0.1)

    click.secho(f"✓ Deployed successfully!", fg="green")


@cli.command()
@click.argument("service")
@click.option("--revision", "-r", type=int, default=1)
def rollback(service, revision):
    '''Rollback to previous revision.'''
    if click.confirm(f"Rollback {service} to revision {revision}?"):
        click.echo(f"Rolling back {service}...")
        click.secho("✓ Rollback complete", fg="green")
    else:
        click.echo("Cancelled")


@cli.command()
@click.argument("service")
def status(service):
    '''Check service status.'''
    click.echo(f"Service: {service}")
    click.echo(f"Status: Running")
    click.echo(f"Replicas: 3/3 ready")


if __name__ == "__main__":
    cli(obj={})
```

---

## 4. Rich Output (Colored, Tables)

```python
import click
from typing import List, Dict


def print_table(headers: List[str], rows: List[List[str]]):
    '''Print a formatted table.'''
    # Calculate column widths
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    # Print header
    header_line = " | ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
    click.echo(header_line)
    click.echo("-" * len(header_line))

    # Print rows
    for row in rows:
        row_line = " | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row))
        click.echo(row_line)


@click.command()
def pods():
    '''List Kubernetes pods.'''
    headers = ["NAME", "STATUS", "RESTARTS", "AGE"]
    rows = [
        ["nginx-abc123", click.style("Running", fg="green"), "0", "2d"],
        ["redis-xyz789", click.style("Running", fg="green"), "1", "5d"],
        ["api-def456", click.style("Pending", fg="yellow"), "0", "1m"],
    ]
    print_table(headers, rows)


# Med rich library for snyggare output
# pip install rich

from rich.console import Console
from rich.table import Table

console = Console()


def list_pods_rich():
    table = Table(title="Kubernetes Pods")
    table.add_column("Name", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Restarts", justify="right")
    table.add_column("Age")

    table.add_row("nginx-abc123", "Running", "0", "2d")
    table.add_row("redis-xyz789", "Running", "1", "5d")
    table.add_row("api-def456", "[yellow]Pending[/yellow]", "0", "1m")

    console.print(table)
```

---

## 5. Environment Variables & Config

```python
import os
import click


@click.command()
@click.option("--api-key",
              envvar="API_KEY",  # Fallback till env var
              help="API key (or set API_KEY env var)")
@click.option("--endpoint",
              envvar="API_ENDPOINT",
              default="https://api.example.com",
              help="API endpoint")
def main(api_key, endpoint):
    '''CLI tool with env var support.'''
    if not api_key:
        raise click.ClickException("API key required. Set --api-key or API_KEY env var")

    click.echo(f"Using endpoint: {endpoint}")
    click.echo(f"API key: {api_key[:4]}****")


# Anvandning:
# export API_KEY=secret123
# python tool.py
# eller
# python tool.py --api-key secret123
```

---

## 6. Exit Codes

```python
import sys
import click


EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_USAGE = 2


@click.command()
@click.argument("action", type=click.Choice(["check", "deploy"]))
def main(action):
    try:
        if action == "check":
            # Simulera check
            click.echo("All checks passed")
            sys.exit(EXIT_SUCCESS)

        elif action == "deploy":
            # Simulera deployment failure
            raise RuntimeError("Deployment failed: timeout")

    except RuntimeError as e:
        click.secho(f"Error: {e}", fg="red", err=True)
        sys.exit(EXIT_ERROR)

    except click.UsageError:
        sys.exit(EXIT_USAGE)


# Exit codes ar viktiga for scripting:
# $ python deploy.py check && echo "Success" || echo "Failed"
```

---

## 7. Komplett Exempel: k8s-tool

```python
#!/usr/bin/env python3
'''
Kubernetes deployment tool.
'''
import click
import subprocess
import json
from pathlib import Path


@click.group()
@click.option("--kubeconfig", envvar="KUBECONFIG",
              default="~/.kube/config", help="Kubeconfig path")
@click.option("--namespace", "-n", default="default", help="Kubernetes namespace")
@click.pass_context
def cli(ctx, kubeconfig, namespace):
    '''Kubernetes deployment tool.'''
    ctx.ensure_object(dict)
    ctx.obj["kubeconfig"] = Path(kubeconfig).expanduser()
    ctx.obj["namespace"] = namespace


@cli.command()
@click.pass_context
def pods(ctx):
    '''List pods.'''
    ns = ctx.obj["namespace"]
    result = subprocess.run(
        ["kubectl", "-n", ns, "get", "pods", "-o", "json"],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        click.secho(f"Error: {result.stderr}", fg="red")
        return

    data = json.loads(result.stdout)
    for pod in data.get("items", []):
        name = pod["metadata"]["name"]
        status = pod["status"]["phase"]
        color = "green" if status == "Running" else "yellow"
        click.echo(f"  {name}: ", nl=False)
        click.secho(status, fg=color)


@cli.command()
@click.argument("manifest", type=click.Path(exists=True))
@click.option("--dry-run", is_flag=True)
@click.pass_context
def apply(ctx, manifest, dry_run):
    '''Apply manifest.'''
    ns = ctx.obj["namespace"]
    cmd = ["kubectl", "-n", ns, "apply", "-f", manifest]

    if dry_run:
        cmd.append("--dry-run=client")

    click.echo(f"$ {' '.join(cmd)}")
    subprocess.run(cmd)


if __name__ == "__main__":
    cli()
```

---

## Sammanfattning

| Feature | argparse | click |
|---------|----------|-------|
| Subcommands | Manual setup | `@click.group()` |
| Type validation | `type=int` | `type=int` |
| Choices | `choices=[]` | `type=click.Choice()` |
| Environment vars | Manual | `envvar="VAR"` |
| Colors | Manual | `click.secho()` |
| Confirmation | Manual | `click.confirm()` |
| Progress | Manual | `click.progressbar()` |
"""
}


# =============================================================================
# NODE 14: REGEX & TEXT PROCESSING
# =============================================================================

NODE_14_REGEX: Dict[str, Any] = {
    "id": "python_regex",
    "title": "Regex & Text Processing",
    "description": "Sök och manipulera text med regular expressions",
    "icon": "🔍",
    "difficulty": 4,
    "estimated_time_minutes": 45,
    "prerequisites": ["python_basics", "python_file_io"],
    "skills_taught": [
        "Regex syntax",
        "re module",
        "Pattern matching",
        "Search and replace",
        "Groups and captures",
        "Log parsing"
    ],
    "real_world_context": "Regex är essentiellt för log-parsning, config-manipulation och validering i DevOps.",
    "content": """# 🔍 Regex & Text Processing

## Varför detta är viktigt

Regex är essentiellt för log-parsning, config-manipulation och validering i DevOps. Du behöver kunna extrahera data från loggar, validera input och transformera text.

## Vad du kommer lära dig

- Förstå regex syntax och patterns
- Implementera re-modulen för sökning
- Använda groups och captures
- Parsa loggar och extrahera data

---

## 📚 Regex Basics

```python
import re


# Match - matcha fran borjan
pattern = r"^error"
text = "error: file not found"
match = re.match(pattern, text, re.IGNORECASE)
if match:
    print(f"Found: {match.group()}")


# Search - hitta var som helst
text = "Server started at 10:30:45"
match = re.search(r"\\d{2}:\\d{2}:\\d{2}", text)
if match:
    print(f"Time: {match.group()}")  # 10:30:45


# Findall - hitta alla matchningar
log = "IPs: 192.168.1.1, 10.0.0.5, 172.16.0.1"
ips = re.findall(r"\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}", log)
print(ips)  # ['192.168.1.1', '10.0.0.5', '172.16.0.1']


# Sub - ersatt
text = "Error: Connection failed"
clean = re.sub(r"Error:\\s*", "", text)
print(clean)  # Connection failed
```

---

## 2. Regex Syntax Cheat Sheet

```python
# Tecken
# .     - Vilket tecken som helst (utom newline)
# \\d    - Siffra [0-9]
# \\D    - Inte siffra
# \\w    - Word character [a-zA-Z0-9_]
# \\W    - Inte word character
# \\s    - Whitespace (space, tab, newline)
# \\S    - Inte whitespace

# Kvantifierare
# *     - 0 eller fler
# +     - 1 eller fler
# ?     - 0 eller 1
# {n}   - Exakt n ganger
# {n,m} - Mellan n och m ganger
# {n,}  - Minst n ganger

# Positioner
# ^     - Borjan av strang/rad
# $     - Slutet av strang/rad
# \\b    - Word boundary

# Grupper
# ()    - Capture group
# (?:)  - Non-capture group
# (?P<name>) - Named group
# |     - Alternation (eller)

# Teckenklasser
# [abc]   - a, b, eller c
# [^abc]  - Inte a, b, eller c
# [a-z]   - a till z
# [0-9]   - 0 till 9
```

---

## 3. Groups och Captures

```python
import re


# Capture groups
log_line = '2024-01-15 10:30:45 ERROR [api] Connection failed'
pattern = r'(\\d{4}-\\d{2}-\\d{2}) (\\d{2}:\\d{2}:\\d{2}) (\\w+) \\[(\\w+)\\] (.+)'

match = re.match(pattern, log_line)
if match:
    date = match.group(1)      # 2024-01-15
    time = match.group(2)      # 10:30:45
    level = match.group(3)     # ERROR
    service = match.group(4)   # api
    message = match.group(5)   # Connection failed

    print(f"{level} in {service}: {message}")


# Named groups
pattern = r'(?P<date>\\d{4}-\\d{2}-\\d{2}) (?P<time>\\d{2}:\\d{2}:\\d{2}) (?P<level>\\w+)'
match = re.match(pattern, log_line)
if match:
    print(match.group("level"))  # ERROR
    print(match.groupdict())     # {'date': '2024-01-15', 'time': '10:30:45', 'level': 'ERROR'}
```

---

## 4. Log Parsing

```python
import re
from typing import List, Dict, Optional
from collections import Counter


def parse_nginx_log(line: str) -> Optional[Dict]:
    '''Parse NGINX access log line.'''
    # Format: IP - - [timestamp] "method path protocol" status size
    pattern = r'(\\d+\\.\\d+\\.\\d+\\.\\d+) - - \\[(.+?)\\] "([A-Z]+) (.+?) HTTP/\\d\\.\\d" (\\d+) (\\d+)'

    match = re.match(pattern, line)
    if not match:
        return None

    return {
        "ip": match.group(1),
        "timestamp": match.group(2),
        "method": match.group(3),
        "path": match.group(4),
        "status": int(match.group(5)),
        "size": int(match.group(6))
    }


def analyze_logs(log_file: str) -> Dict:
    '''Analyze NGINX logs.'''
    status_counts = Counter()
    path_counts = Counter()
    ips = Counter()
    errors = []

    with open(log_file) as f:
        for line in f:
            parsed = parse_nginx_log(line)
            if not parsed:
                continue

            status_counts[parsed["status"]] += 1
            path_counts[parsed["path"]] += 1
            ips[parsed["ip"]] += 1

            if parsed["status"] >= 400:
                errors.append(parsed)

    return {
        "total_requests": sum(status_counts.values()),
        "status_codes": dict(status_counts),
        "top_paths": path_counts.most_common(10),
        "top_ips": ips.most_common(10),
        "errors": errors[:100]
    }


# Anvandning
# stats = analyze_logs("/var/log/nginx/access.log")
# print(f"Total: {stats['total_requests']}")
# print(f"Errors: {stats['status_codes'].get(500, 0)}")
```

---

## 5. Config File Parsing

```python
import re
from pathlib import Path
from typing import Dict


def parse_env_file(path: str) -> Dict[str, str]:
    '''Parse .env file.'''
    env = {}
    content = Path(path).read_text()

    # Pattern: KEY=value eller KEY="quoted value"
    pattern = r'^([A-Z_][A-Z0-9_]*)=[\"\\'']?([^\"\\''\\n]*)[\"\\'']?$'

    for match in re.finditer(pattern, content, re.MULTILINE):
        key, value = match.groups()
        env[key] = value

    return env


def parse_ini_file(path: str) -> Dict[str, Dict[str, str]]:
    '''Parse simple INI file.'''
    sections = {}
    current_section = "default"

    content = Path(path).read_text()

    for line in content.splitlines():
        line = line.strip()

        # Skip empty lines and comments
        if not line or line.startswith(("#", ";")):
            continue

        # Section header
        section_match = re.match(r'^\\[([^\\]]+)\\]$', line)
        if section_match:
            current_section = section_match.group(1)
            sections[current_section] = {}
            continue

        # Key-value pair
        kv_match = re.match(r'^([^=]+)=(.*)$', line)
        if kv_match:
            key, value = kv_match.groups()
            if current_section not in sections:
                sections[current_section] = {}
            sections[current_section][key.strip()] = value.strip()

    return sections


# Anvandning
env = parse_env_file(".env")
print(env.get("DATABASE_URL"))

config = parse_ini_file("config.ini")
print(config["database"]["host"])
```

---

## 6. Text Extraction

```python
import re


def extract_ips(text: str) -> list:
    '''Extract all IP addresses.'''
    pattern = r'\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b'
    return re.findall(pattern, text)


def extract_emails(text: str) -> list:
    '''Extract email addresses.'''
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)


def extract_urls(text: str) -> list:
    '''Extract URLs.'''
    pattern = r'https?://[^\\s<>"{}|\\\\^`\\[\\]]+'
    return re.findall(pattern, text)


def extract_docker_images(dockerfile: str) -> list:
    '''Extract FROM images in Dockerfile.'''
    pattern = r'^FROM\\s+([^\\s]+)'
    return re.findall(pattern, dockerfile, re.MULTILINE)


def extract_k8s_images(manifest: str) -> list:
    '''Extract container images from K8s manifest.'''
    pattern = r'image:\\s*["\\'']?([^"\\''\\s]+)["\\'']?'
    return re.findall(pattern, manifest)


# Anvandning
log = '''
Server 192.168.1.1 connected
Email: admin@example.com
See https://kubernetes.io for docs
'''

print(extract_ips(log))     # ['192.168.1.1']
print(extract_emails(log))  # ['admin@example.com']
print(extract_urls(log))    # ['https://kubernetes.io']
```

---

## 7. Search and Replace

```python
import re
from pathlib import Path


def update_version_in_file(file_path: str, new_version: str):
    '''Update version number in file.'''
    content = Path(file_path).read_text()

    # Pattern for semver
    pattern = r'version["\\'']?:\\s*["\\'']?(\\d+\\.\\d+\\.\\d+)["\\'']?'

    updated = re.sub(
        pattern,
        f'version: "{new_version}"',
        content
    )

    Path(file_path).write_text(updated)


def mask_secrets(text: str) -> str:
    '''Mask sensitive data in logs.'''
    # Mask API keys
    text = re.sub(r'(api[_-]?key[=:])\\s*["\\'']?[\\w-]+["\\'']?',
                  r'\\1****', text, flags=re.IGNORECASE)

    # Mask passwords
    text = re.sub(r'(password[=:])\\s*["\\'']?[^\\s"\\'']+["\\'']?',
                  r'\\1****', text, flags=re.IGNORECASE)

    # Mask tokens
    text = re.sub(r'(token[=:])\\s*["\\'']?[\\w.-]+["\\'']?',
                  r'\\1****', text, flags=re.IGNORECASE)

    return text


# Anvandning
config = '''
api_key: sk-abc123xyz
password: supersecret
token: ghp_xxxxxxxxxxxx
'''

print(mask_secrets(config))
# api_key:****
# password:****
# token:****
```

---

## 8. Compiled Patterns (Performance)

```python
import re


# Kompilera pattern for battre performance vid upprepade anvandningar
IP_PATTERN = re.compile(r'\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b')
LOG_PATTERN = re.compile(
    r'(?P<timestamp>\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2})\\s+'
    r'(?P<level>\\w+)\\s+'
    r'\\[(?P<service>[^\\]]+)\\]\\s+'
    r'(?P<message>.+)'
)


def process_logs(lines):
    '''Process log lines with compiled patterns.'''
    for line in lines:
        match = LOG_PATTERN.match(line)
        if match:
            yield match.groupdict()


# Anvandning
logs = [
    "2024-01-15T10:30:45 ERROR [api] Connection failed",
    "2024-01-15T10:30:46 INFO [api] Retrying...",
]

for entry in process_logs(logs):
    print(f"{entry['level']}: {entry['message']}")
```

---

## Sammanfattning

| Funktion | Anvandning |
|----------|------------|
| `re.match()` | Matcha fran borjan |
| `re.search()` | Hitta forsta forekomst |
| `re.findall()` | Hitta alla forekomster |
| `re.sub()` | Ersatt matchningar |
| `re.split()` | Splitta pa pattern |
| `re.compile()` | Kompilera for performance |
| `match.group()` | Hamta capture group |
| `match.groupdict()` | Hamta named groups |
"""
}


# Add nodes 11-14
PYTHON_SKILLSMAP_NODES.extend([
    NODE_11_HTTP_APIS,
    NODE_12_VENV,
    NODE_13_CLI_TOOLS,
    NODE_14_REGEX,
])


# =============================================================================
# NODE 15: LOGGING
# =============================================================================

NODE_15_LOGGING: Dict[str, Any] = {
    "id": "python_logging",
    "title": "Logging & Debugging",
    "description": "Professionell logging for production-redo scripts",
    "icon": "📝",
    "difficulty": 3,
    "estimated_time_minutes": 35,
    "prerequisites": ["python_file_io", "python_error_handling"],
    "skills_taught": [
        "logging module basics",
        "Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
        "Formatters och handlers",
        "File och console logging",
        "Structured logging",
        "Log rotation"
    ],
    "real_world_context": "Print() ar for amatorer. Professionella DevOps-scripts anvander logging for traceability och debugging i produktion.",
    "content": '''# 📝 Logging & Debugging - Professionell Logging

## Varför detta är viktigt

print() är för amatörer. Professionella DevOps-scripts använder logging för traceability och debugging i produktion. Utan ordentlig logging är felsökning en mardröm.

## Vad du kommer lära dig

- Förstå logging module och levels
- Implementera formatters och handlers
- Konfigurera file och console logging
- Använda structured logging för ELK/CloudWatch

---

## 📚 Basic Logging

```python
import logging

# Konfigurera basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Anvand olika levels
logger.debug("Debug info - for development")
logger.info("Server started on port 8080")
logger.warning("Disk space running low")
logger.error("Failed to connect to database")
logger.critical("System is shutting down!")
```

---

## 2. Log Levels

| Level | Varde | Anvandning |
|-------|-------|------------|
| DEBUG | 10 | Detaljerad info for debugging |
| INFO | 20 | Bekraftar att saker fungerar |
| WARNING | 30 | Nagot ovantatt men ej kritiskt |
| ERROR | 40 | Allvarligt fel, funktion misslyckades |
| CRITICAL | 50 | Mycket allvarligt, program kan inte fortsatta |

```python
# Satt level - allt under ignoreras
logging.basicConfig(level=logging.WARNING)

logger.debug("Syns inte")
logger.info("Syns inte")
logger.warning("Syns!")
```

---

## 3. Logga till Fil

```python
import logging
from logging.handlers import RotatingFileHandler


def setup_logger(name: str, log_file: str = "app.log"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)

    # File handler med rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10_000_000,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(file_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# Anvandning
logger = setup_logger("myapp")
logger.info("Application started")
```

---

## 4. Structured Logging (JSON)

```python
import logging
import json
from datetime import datetime


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }

        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_record)


# Anvandning
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger = logging.getLogger("json_logger")
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("User logged in", extra={"user_id": 123})
# {"timestamp": "2024-01-15T10:30:00", "level": "INFO", ...}
```

---

## 5. Praktisk DevOps Logger

```python
import logging
import sys
from pathlib import Path


def get_devops_logger(
    name: str = "devops",
    log_dir: str = "/var/log/devops"
) -> logging.Logger:
    """
    Production-ready logger for DevOps scripts.
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger  # Already configured

    logger.setLevel(logging.DEBUG)

    # Ensure log directory exists
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    # Console: INFO and above
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter(
        '[%(levelname)s] %(message)s'
    ))

    # File: All levels
    from logging.handlers import TimedRotatingFileHandler
    file_handler = TimedRotatingFileHandler(
        f"{log_dir}/{name}.log",
        when="midnight",
        interval=1,
        backupCount=30
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'
    ))

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger


# Anvandning
log = get_devops_logger("deploy")
log.info("Starting deployment...")
log.debug("Config loaded: %s", config)
log.error("Deployment failed: %s", error)
```

---

## 6. Exception Logging

```python
import logging

logger = logging.getLogger(__name__)

def risky_operation():
    try:
        result = 10 / 0
    except Exception:
        # exc_info=True inkluderar full traceback
        logger.exception("Operation failed")
        raise


# Eller manuellt
try:
    risky_operation()
except Exception as e:
    logger.error("Error: %s", e, exc_info=True)
```

---

## Sammanfattning

| Koncept | Anvandning |
|---------|------------|
| `logging.basicConfig()` | Snabb setup |
| `logger.info()` | Normal info |
| `logger.exception()` | Fel med traceback |
| `RotatingFileHandler` | Auto-rotation |
| `JSONFormatter` | Structured logs |
'''
}


# =============================================================================
# NODE 16: TESTING WITH PYTEST
# =============================================================================

NODE_16_TESTING: Dict[str, Any] = {
    "id": "python_testing",
    "title": "Testing with pytest",
    "description": "Skriv och kor tester for din kod",
    "icon": "🧪",
    "difficulty": 3,
    "estimated_time_minutes": 45,
    "prerequisites": ["python_functions", "python_oop_basics"],
    "skills_taught": [
        "pytest basics",
        "Test functions och assertions",
        "Fixtures",
        "Parametrized tests",
        "Mocking",
        "Test coverage"
    ],
    "real_world_context": "Tester ar inte optional i DevOps. CI/CD pipelines kor tester automatiskt. Ingen merge utan grona tester.",
    "content": '''# 🧪 Testing med pytest - Professionell Testning

## Varför detta är kritiskt
> "Ingen seriös DevOps-pipeline accepterar kod utan tester. pytest är Python-världens teststandard - automatiska tester är skillnaden mellan 'det fungerade på min maskin' och produktionsredo kod."

## Vad du kommer lära dig
- ✅ pytest basics och test discovery
- ✅ Assertions och fixtures
- ✅ Parametrized tests för edge cases
- ✅ Mocking och patching
- ✅ Test coverage mätning

---

## Varför Testa?

- Fånga buggar INNAN produktion
- Dokumenterar hur kod ska fungera
- Möjliggör refactoring utan rädsla
- CI/CD krav - inga tester = ingen deploy

---

## 1. Installation

```bash
pip install pytest pytest-cov
```

---

## 2. Din Forsta Test

```python
# test_calculator.py

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)
```

Kor tester:
```bash
pytest test_calculator.py -v
```

---

## 3. Assertions

```python
import pytest

def test_assertions():
    # Equality
    assert 1 + 1 == 2

    # Boolean
    assert True
    assert not False

    # Membership
    assert "a" in "abc"
    assert 1 in [1, 2, 3]

    # Type
    assert isinstance([], list)

    # Exceptions
    with pytest.raises(ValueError):
        int("not a number")

    with pytest.raises(ZeroDivisionError):
        1 / 0
```

---

## 4. Fixtures - Setup och Teardown

```python
import pytest


@pytest.fixture
def sample_server():
    """Create a sample server for tests."""
    return {
        "hostname": "web-01",
        "ip": "192.168.1.10",
        "port": 80,
        "status": "running"
    }


@pytest.fixture
def server_list():
    """Create multiple servers."""
    return [
        {"hostname": "web-01", "status": "running"},
        {"hostname": "web-02", "status": "stopped"},
        {"hostname": "db-01", "status": "running"},
    ]


def test_server_hostname(sample_server):
    assert sample_server["hostname"] == "web-01"


def test_running_servers(server_list):
    running = [s for s in server_list if s["status"] == "running"]
    assert len(running) == 2
```

---

## 5. Fixture med Cleanup

```python
import pytest
from pathlib import Path


@pytest.fixture
def temp_config_file(tmp_path):
    """Create temporary config file."""
    config_file = tmp_path / "config.yaml"
    config_file.write_text("port: 8080\\ndebug: true")
    yield config_file
    # Cleanup sker automatiskt med tmp_path


@pytest.fixture
def database_connection():
    """Setup and teardown database."""
    # Setup
    conn = create_connection()
    conn.execute("CREATE TABLE test (id INT)")

    yield conn

    # Teardown
    conn.execute("DROP TABLE test")
    conn.close()
```

---

## 6. Parametrized Tests

```python
import pytest


def is_valid_port(port: int) -> bool:
    return 1 <= port <= 65535


@pytest.mark.parametrize("port,expected", [
    (80, True),
    (443, True),
    (8080, True),
    (0, False),
    (-1, False),
    (65536, False),
    (65535, True),
])
def test_is_valid_port(port, expected):
    assert is_valid_port(port) == expected


@pytest.mark.parametrize("hostname", [
    "web-01",
    "db-primary",
    "cache-node-1",
])
def test_hostname_format(hostname):
    assert "-" in hostname
    assert hostname.islower() or hostname[0].isalpha()
```

---

## 7. Mocking

```python
from unittest.mock import Mock, patch, MagicMock


def get_server_status(hostname: str) -> str:
    # Anropar extern API
    import requests
    response = requests.get(f"http://api/servers/{hostname}")
    return response.json()["status"]


def test_get_server_status_mock():
    with patch('requests.get') as mock_get:
        # Konfigurera mock
        mock_get.return_value.json.return_value = {"status": "running"}

        # Test
        status = get_server_status("web-01")

        assert status == "running"
        mock_get.assert_called_once_with("http://api/servers/web-01")


@patch('os.environ.get')
def test_config_from_env(mock_env):
    mock_env.return_value = "production"

    from myapp import get_environment
    assert get_environment() == "production"
```

---

## 8. Test Organization

```
tests/
    __init__.py
    conftest.py          # Shared fixtures
    test_servers.py
    test_deployments.py
    integration/
        test_api.py
```

```python
# conftest.py - Shared fixtures
import pytest

@pytest.fixture(scope="session")
def api_client():
    """Shared across all tests in session."""
    return APIClient()

@pytest.fixture(scope="module")
def database():
    """Shared across tests in same module."""
    return Database()
```

---

## 9. Running Tests

```bash
# Alla tester
pytest

# Verbose output
pytest -v

# Specifik fil
pytest tests/test_servers.py

# Specifik test
pytest tests/test_servers.py::test_server_status

# Med coverage
pytest --cov=myapp --cov-report=html

# Stoppa vid forsta fel
pytest -x

# Kör senast failade
pytest --lf
```

---

## Sammanfattning

| Koncept | Syntax |
|---------|--------|
| Test function | `def test_name():` |
| Assert | `assert x == y` |
| Fixture | `@pytest.fixture` |
| Parametrize | `@pytest.mark.parametrize` |
| Mock | `@patch('module.func')` |
| Exception | `pytest.raises(Error)` |
'''
}


# =============================================================================
# NODE 17: ASYNC PYTHON
# =============================================================================

NODE_17_ASYNC: Dict[str, Any] = {
    "id": "python_async",
    "title": "Async Python",
    "description": "Asynkron programmering med asyncio",
    "icon": "⚡",
    "difficulty": 4,
    "estimated_time_minutes": 50,
    "prerequisites": ["python_functions", "python_http_apis"],
    "skills_taught": [
        "async/await syntax",
        "asyncio basics",
        "Concurrent HTTP requests",
        "async context managers",
        "Task management",
        "aiohttp for async HTTP"
    ],
    "real_world_context": "Nar du behover gora 100 API-anrop ar sync alldeles for langsamt. Async later dig gora dem parallellt.",
    "content": '''# ⚡ Async Python - Parallell Execution

## Varför detta är viktigt
> "När du behöver göra 100 API-anrop, hämta data från flera microservices, eller hantera tusentals samtidiga connections - async är skillnaden mellan sekunder och minuter. Det är grundläggande för moderna Python-backends."

## Vad du kommer lära dig
- ✅ async/await syntax och coroutines
- ✅ asyncio event loop
- ✅ Concurrent HTTP med aiohttp
- ✅ Task management och gather
- ✅ Async context managers

---

## Varför Async?

Sync (vanlig) kod väntar på varje operation:
- API call 1: 500ms
- API call 2: 500ms
- API call 3: 500ms
- Total: 1500ms

Async kör parallellt:
- Alla 3 calls samtidigt: ~500ms total!

---

## 1. Grundläggande Syntax

```python
import asyncio


# Definiera async function
async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(1)  # Simulera IO
    print("Done!")
    return {"data": "value"}


# Kör async function
async def main():
    result = await fetch_data()
    print(result)


# Entry point
asyncio.run(main())
```

---

## 2. Parallel Execution

```python
import asyncio


async def check_server(hostname: str) -> dict:
    print(f"Checking {hostname}...")
    await asyncio.sleep(1)  # Simulera nätverksanrop
    return {"hostname": hostname, "status": "running"}


async def main():
    # Sekventiellt (långsamt)
    result1 = await check_server("web-01")
    result2 = await check_server("web-02")
    # Total: 2 sekunder

    # Parallellt (snabbt!)
    results = await asyncio.gather(
        check_server("web-01"),
        check_server("web-02"),
        check_server("web-03"),
    )
    # Total: ~1 sekund
    print(results)


asyncio.run(main())
```

---

## 3. aiohttp - Async HTTP

```python
import asyncio
import aiohttp


async def fetch_url(session, url: str) -> dict:
    async with session.get(url) as response:
        return {
            "url": url,
            "status": response.status,
            "data": await response.text()
        }


async def fetch_all_urls(urls: list) -> list:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results


async def main():
    urls = [
        "https://api.github.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts/1"
    ]

    results = await fetch_all_urls(urls)
    for result in results:
        print(f"{result['url']}: {result['status']}")


asyncio.run(main())
```

---

## 4. Async Context Managers

```python
import asyncio
import aiofiles


async def read_file_async(path: str) -> str:
    async with aiofiles.open(path, 'r') as f:
        content = await f.read()
    return content


async def write_file_async(path: str, content: str):
    async with aiofiles.open(path, 'w') as f:
        await f.write(content)


async def main():
    await write_file_async("test.txt", "Hello Async!")
    content = await read_file_async("test.txt")
    print(content)
```

---

## 5. Task Management

```python
import asyncio


async def long_running_task(name: str, duration: int):
    print(f"Task {name} starting...")
    await asyncio.sleep(duration)
    print(f"Task {name} completed!")
    return f"Result from {name}"


async def main():
    # Skapa tasks
    task1 = asyncio.create_task(long_running_task("A", 2))
    task2 = asyncio.create_task(long_running_task("B", 1))

    # Vänta på båda
    results = await asyncio.gather(task1, task2)
    print(results)

    # Med timeout
    try:
        result = await asyncio.wait_for(
            long_running_task("C", 5),
            timeout=2.0
        )
    except asyncio.TimeoutError:
        print("Task timed out!")


asyncio.run(main())
```

---

## 6. Praktiskt Exempel: Parallel Server Check

```python
import asyncio
import aiohttp
from dataclasses import dataclass
from typing import List


@dataclass
class ServerStatus:
    hostname: str
    url: str
    status: str
    response_time_ms: float


async def check_server(
    session: aiohttp.ClientSession,
    hostname: str,
    url: str
) -> ServerStatus:
    import time
    start = time.time()

    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as resp:
            elapsed = (time.time() - start) * 1000
            status = "healthy" if resp.status == 200 else "unhealthy"
            return ServerStatus(hostname, url, status, elapsed)
    except Exception as e:
        elapsed = (time.time() - start) * 1000
        return ServerStatus(hostname, url, f"error: {e}", elapsed)


async def check_all_servers(servers: List[dict]) -> List[ServerStatus]:
    async with aiohttp.ClientSession() as session:
        tasks = [
            check_server(session, s["hostname"], s["url"])
            for s in servers
        ]
        return await asyncio.gather(*tasks)


async def main():
    servers = [
        {"hostname": "web-01", "url": "https://google.com"},
        {"hostname": "web-02", "url": "https://github.com"},
        {"hostname": "api-01", "url": "https://api.github.com"},
    ]

    print("Checking servers...")
    results = await check_all_servers(servers)

    for r in results:
        print(f"{r.hostname}: {r.status} ({r.response_time_ms:.0f}ms)")


asyncio.run(main())
```

---

## Sammanfattning

| Koncept | Syntax |
|---------|--------|
| Async function | `async def func():` |
| Await | `await async_func()` |
| Run | `asyncio.run(main())` |
| Parallel | `asyncio.gather(*tasks)` |
| Timeout | `asyncio.wait_for(coro, timeout=5)` |
| HTTP | `aiohttp.ClientSession()` |
'''
}


# =============================================================================
# NODE 18: DECORATORS
# =============================================================================

NODE_18_DECORATORS: Dict[str, Any] = {
    "id": "python_decorators",
    "title": "Decorators",
    "description": "Funktions- och klassdecorators",
    "icon": "🎀",
    "difficulty": 4,
    "estimated_time_minutes": 40,
    "prerequisites": ["python_functions", "python_oop_basics"],
    "skills_taught": [
        "Function decorators",
        "Decorators med argument",
        "Class decorators",
        "functools.wraps",
        "Praktiska decorators (retry, timer, cache)"
    ],
    "real_world_context": "Decorators ar Python-magi som later dig lägga till funktionalitet utan att ändra kod. @retry, @cache, @authenticate - kraftfulla patterns.",
    "content": '''# 🎀 Decorators - Python Magi

## Varför detta är viktigt
> "Decorators är meta-programmering som låter dig modifiera funktioners beteende utan att röra originalkoden. @retry för resiliens, @cache för prestanda, @authenticate för säkerhet - de bästa Python-kodbaserna använder decorators överallt."

## Vad du kommer lära dig
- ✅ Function decorators grunderna
- ✅ Decorators med argument
- ✅ functools.wraps för metadata
- ✅ Praktiska decorators (retry, timer, cache)
- ✅ Class decorators och metaklasser

---

## Vad är en Decorator?

En decorator är en funktion som tar en funktion och returnerar en ny funktion med extra funktionalitet.

```python
@my_decorator
def my_function():
    pass

# Är samma som:
my_function = my_decorator(my_function)
```

---

## 1. Enkel Decorator

```python
from functools import wraps


def log_call(func):
    """Logga varje funktionsanrop."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b


add(2, 3)
# Calling add...
# add returned 5
```

---

## 2. Timer Decorator

```python
import time
from functools import wraps


def timer(func):
    """Mät exekveringstid."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.3f}s")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)
    return "done"


slow_function()
# slow_function took 1.001s
```

---

## 3. Retry Decorator

```python
import time
from functools import wraps


def retry(max_attempts: int = 3, delay: float = 1.0):
    """Retry decorator med konfigurerbart antal försök."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


@retry(max_attempts=5, delay=2.0)
def unreliable_api_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("API timeout")
    return {"status": "ok"}


result = unreliable_api_call()
```

---

## 4. Cache Decorator

```python
from functools import wraps, lru_cache


def simple_cache(func):
    """Enkel memoization cache."""
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@simple_cache
def expensive_calculation(n):
    print(f"Calculating for {n}...")
    return n ** 2


expensive_calculation(5)  # Calculating...
expensive_calculation(5)  # Cache hit!


# Eller anvand inbyggda lru_cache
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## 5. Authentication Decorator

```python
from functools import wraps


def require_auth(func):
    """Kräv autentisering."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Simulera auth check
        user = kwargs.get('user') or (args[0] if args else None)
        if not user or not user.get('authenticated'):
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    return wrapper


def require_role(role: str):
    """Kräv specifik roll."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = kwargs.get('user') or (args[0] if args else None)
            if not user or role not in user.get('roles', []):
                raise PermissionError(f"Role '{role}' required")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@require_auth
@require_role("admin")
def delete_server(user, server_id):
    return f"Server {server_id} deleted by {user['name']}"


admin_user = {"name": "admin", "authenticated": True, "roles": ["admin"]}
delete_server(admin_user, "web-01")
```

---

## 6. Class-based Decorator

```python
class CountCalls:
    """Räkna antal anrop."""

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello(name):
    return f"Hello, {name}!"


say_hello("Alice")  # say_hello called 1 times
say_hello("Bob")    # say_hello called 2 times
```

---

## 7. Praktiskt: Rate Limiter

```python
import time
from functools import wraps
from collections import defaultdict


def rate_limit(calls: int, period: float):
    """Begränsa antal anrop per tidsperiod."""
    call_times = defaultdict(list)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            key = func.__name__

            # Ta bort gamla anrop
            call_times[key] = [
                t for t in call_times[key]
                if now - t < period
            ]

            if len(call_times[key]) >= calls:
                wait = period - (now - call_times[key][0])
                raise Exception(f"Rate limited. Wait {wait:.1f}s")

            call_times[key].append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@rate_limit(calls=3, period=10.0)
def api_call():
    return "API response"


for i in range(5):
    try:
        print(api_call())
    except Exception as e:
        print(e)
```

---

## Sammanfattning

| Pattern | Användning |
|---------|------------|
| `@timer` | Mät tid |
| `@retry(n)` | Retry vid fel |
| `@lru_cache` | Cacha resultat |
| `@require_auth` | Kräv login |
| `@rate_limit` | Begränsa anrop |
'''
}


# =============================================================================
# NODE 19: TYPE HINTS
# =============================================================================

NODE_19_TYPE_HINTS: Dict[str, Any] = {
    "id": "python_type_hints",
    "title": "Type Hints & Mypy",
    "description": "Statisk typning i Python",
    "icon": "🏷️",
    "difficulty": 3,
    "estimated_time_minutes": 35,
    "prerequisites": ["python_functions", "python_oop_basics"],
    "skills_taught": [
        "Basic type hints",
        "typing module",
        "Generic types",
        "Optional och Union",
        "TypedDict",
        "Mypy for type checking"
    ],
    "real_world_context": "Type hints gor din kod sjalvdokumenterande och fangar buggar innan runtime. Stora projekt kraver det.",
    "content": '''# 🏷️ Type Hints & Mypy - Statisk Typning

## Varför detta är viktigt
> "I stora Python-projekt är type hints inte optional - de fångar buggar INNAN runtime, ger IDE superkrafter med autocomplete, och gör koden självdokumenterande. Mypy i CI/CD garanterar typkorrekthet."

## Vad du kommer lära dig
- ✅ Basic type hints för variabler och funktioner
- ✅ typing module (List, Dict, Optional, Union)
- ✅ Generic types och TypeVar
- ✅ TypedDict och dataclasses
- ✅ Mypy för statisk analys i CI/CD

---

## Varför Type Hints?

- Dokumentation i koden
- IDE autocomplete
- Fånga buggar före runtime
- Refactoring-säkerhet

---

## 1. Basic Type Hints

```python
# Variabler
name: str = "DevOps"
port: int = 8080
is_active: bool = True
cpu_usage: float = 75.5


# Funktioner
def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def process() -> None:
    print("Processing...")
```

---

## 2. Collections

```python
from typing import List, Dict, Set, Tuple


# List av strings
servers: List[str] = ["web-01", "web-02"]

# Dict med string keys och int values
ports: Dict[str, int] = {"http": 80, "https": 443}

# Set av integers
unique_ids: Set[int] = {1, 2, 3}

# Tuple (fixed length)
coordinate: Tuple[float, float] = (10.5, 20.3)

# Tuple med variabel langd
args: Tuple[int, ...] = (1, 2, 3, 4, 5)


# Python 3.9+ kan anvanda built-in types direkt:
servers: list[str] = ["web-01", "web-02"]
ports: dict[str, int] = {"http": 80}
```

---

## 3. Optional och Union

```python
from typing import Optional, Union


# Optional - kan vara None
def find_server(name: str) -> Optional[dict]:
    servers = {"web-01": {"ip": "10.0.0.1"}}
    return servers.get(name)  # Returnerar dict eller None


# Union - flera mojliga typer
def parse_port(value: Union[str, int]) -> int:
    if isinstance(value, str):
        return int(value)
    return value


# Python 3.10+ syntax:
def parse_port(value: str | int) -> int:
    ...


def find_server(name: str) -> dict | None:
    ...
```

---

## 4. Type Aliases

```python
from typing import Dict, List, TypeAlias


# Skapa alias for komplexa typer
ServerConfig: TypeAlias = Dict[str, Union[str, int, bool]]
ServerList: TypeAlias = List[ServerConfig]


def get_servers() -> ServerList:
    return [
        {"hostname": "web-01", "port": 80, "ssl": True},
        {"hostname": "web-02", "port": 80, "ssl": False},
    ]


def update_server(config: ServerConfig) -> bool:
    # ...
    return True
```

---

## 5. TypedDict

```python
from typing import TypedDict, Required, NotRequired


class ServerConfig(TypedDict):
    hostname: str
    ip: str
    port: int
    ssl: NotRequired[bool]  # Optional field


class DeploymentConfig(TypedDict, total=False):
    # Alla falt ar optional med total=False
    environment: str
    replicas: int
    image: str


def deploy(config: DeploymentConfig) -> None:
    env = config.get("environment", "production")
    replicas = config.get("replicas", 1)
    print(f"Deploying to {env} with {replicas} replicas")


# Anvandning
server: ServerConfig = {
    "hostname": "web-01",
    "ip": "10.0.0.1",
    "port": 80
}
```

---

## 6. Callable

```python
from typing import Callable


# Funktion som tar en funktion
def retry(
    func: Callable[..., str],
    attempts: int = 3
) -> str:
    for _ in range(attempts):
        try:
            return func()
        except Exception:
            pass
    raise RuntimeError("All retries failed")


# Specifik signatur
Handler = Callable[[str, int], bool]


def register_handler(name: str, handler: Handler) -> None:
    # handler tar (str, int) och returnerar bool
    pass
```

---

## 7. Generics

```python
from typing import TypeVar, Generic, List


T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]


# Anvandning
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)

str_stack: Stack[str] = Stack()
str_stack.push("hello")
```

---

## 8. Mypy - Type Checker

```bash
# Installation
pip install mypy

# Kor type check
mypy script.py

# Strict mode
mypy --strict script.py

# Ignorera specifika errors
mypy --ignore-missing-imports script.py
```

```python
# mypy.ini eller pyproject.toml
[mypy]
python_version = 3.11
warn_return_any = True
warn_unused_ignores = True
disallow_untyped_defs = True
```

---

## 9. Praktiskt Exempel

```python
from typing import TypedDict, Optional, List
from dataclasses import dataclass


class ServerSpec(TypedDict):
    hostname: str
    ip: str
    port: int
    tags: List[str]


@dataclass
class HealthCheck:
    server: str
    status: str
    response_time_ms: float
    error: Optional[str] = None


def check_servers(
    servers: List[ServerSpec],
    timeout: float = 5.0
) -> List[HealthCheck]:
    results: List[HealthCheck] = []

    for server in servers:
        # Type-safe access
        hostname: str = server["hostname"]
        ip: str = server["ip"]

        result = HealthCheck(
            server=hostname,
            status="healthy",
            response_time_ms=100.0
        )
        results.append(result)

    return results
```

---

## Sammanfattning

| Type | Syntax |
|------|--------|
| Basic | `x: int = 5` |
| List | `List[str]` eller `list[str]` |
| Dict | `Dict[str, int]` |
| Optional | `Optional[str]` eller `str \\| None` |
| Union | `Union[str, int]` eller `str \\| int` |
| TypedDict | `class Config(TypedDict):` |
| Generic | `class Box(Generic[T]):` |
'''
}


# =============================================================================
# NODE 20: PACKAGING & DISTRIBUTION
# =============================================================================

NODE_20_PACKAGING: Dict[str, Any] = {
    "id": "python_packaging",
    "title": "Packaging & Distribution",
    "description": "Skapa och distribuera Python-paket",
    "icon": "📦",
    "difficulty": 4,
    "estimated_time_minutes": 45,
    "prerequisites": ["python_venv", "python_cli_tools"],
    "skills_taught": [
        "pyproject.toml",
        "Package structure",
        "Entry points",
        "Build och publish",
        "Poetry vs pip",
        "Private PyPI"
    ],
    "real_world_context": "Dela dina DevOps-verktyg med teamet eller varlden. Gor dem pip-installerbara.",
    "content": '''# 📦 Packaging & Distribution - Dela Dina Verktyg

## Varför detta är viktigt
> "De bästa DevOps-teamen bygger återanvändbara verktyg. Med proper packaging kan alla i teamet `pip install your-tool` och få samma funktionalitet. Private PyPI låter er dela internt utan att publicera till världen."

## Vad du kommer lära dig
- ✅ pyproject.toml - modern packaging
- ✅ Package structure och namespace
- ✅ Entry points för CLI-verktyg
- ✅ Build, publish och versioning
- ✅ Poetry vs pip och private PyPI

---

## Varför Paketera?

- Dela kod med teamet
- Versionhantering
- `pip install` dina verktyg
- Reproducerbar setup

---

## 1. Package Structure

```
my-devops-tool/
├── pyproject.toml          # Modern config (ersätter setup.py)
├── README.md
├── LICENSE
├── src/
│   └── devops_tool/
│       ├── __init__.py
│       ├── cli.py
│       ├── utils.py
│       └── config.py
└── tests/
    ├── __init__.py
    └── test_utils.py
```

---

## 2. pyproject.toml

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "devops-tool"
version = "1.0.0"
description = "DevOps automation toolkit"
readme = "README.md"
license = "MIT"
requires-python = ">=3.9"
authors = [
    { name = "Your Name", email = "you@example.com" }
]
keywords = ["devops", "automation", "cli"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.11",
]

dependencies = [
    "click>=8.0",
    "requests>=2.28",
    "pyyaml>=6.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "mypy>=1.0",
    "black>=23.0",
]

[project.scripts]
devops-tool = "devops_tool.cli:main"

[project.urls]
Homepage = "https://github.com/you/devops-tool"
Documentation = "https://devops-tool.readthedocs.io"
```

---

## 3. Package Code

```python
# src/devops_tool/__init__.py
"""DevOps automation toolkit."""

__version__ = "1.0.0"

from .utils import check_server, deploy
from .config import load_config

__all__ = ["check_server", "deploy", "load_config", "__version__"]
```

```python
# src/devops_tool/cli.py
import click
from . import check_server, __version__


@click.group()
@click.version_option(__version__)
def main():
    """DevOps automation CLI."""
    pass


@main.command()
@click.argument("hostname")
def check(hostname: str):
    """Check server health."""
    result = check_server(hostname)
    click.echo(f"Status: {result['status']}")


@main.command()
@click.argument("environment")
@click.option("--dry-run", is_flag=True)
def deploy(environment: str, dry_run: bool):
    """Deploy to environment."""
    if dry_run:
        click.echo(f"Would deploy to {environment}")
    else:
        click.echo(f"Deploying to {environment}...")


if __name__ == "__main__":
    main()
```

---

## 4. Build Package

```bash
# Installera build tools
pip install build twine

# Bygg package
python -m build

# Resultat:
# dist/
#   devops_tool-1.0.0-py3-none-any.whl
#   devops_tool-1.0.0.tar.gz
```

---

## 5. Install Locally

```bash
# Editable install (for development)
pip install -e .

# Med dev dependencies
pip install -e ".[dev]"

# Nu kan du anvanda:
devops-tool --version
devops-tool check web-01
```

---

## 6. Publish to PyPI

```bash
# Skapa konto pa pypi.org och testpypi.org

# Test upload forst
twine upload --repository testpypi dist/*

# Riktigt upload
twine upload dist/*

# Nu kan alla installera:
pip install devops-tool
```

---

## 7. Poetry Alternative

```bash
# Installera Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Skapa nytt projekt
poetry new my-tool
cd my-tool

# Lagg till dependencies
poetry add click requests
poetry add --group dev pytest mypy

# Bygg
poetry build

# Publicera
poetry publish
```

```toml
# pyproject.toml med Poetry
[tool.poetry]
name = "my-tool"
version = "1.0.0"
description = "My awesome tool"
authors = ["You <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
click = "^8.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0"

[tool.poetry.scripts]
my-tool = "my_tool.cli:main"
```

---

## 8. Private PyPI

```bash
# Enkelt: Anvand devpi
pip install devpi-server devpi-client

# Starta server
devpi-server --start --init

# Skapa user och index
devpi use http://localhost:3141
devpi user -c myuser password=secret
devpi login myuser
devpi index -c dev

# Upload till privat index
devpi upload dist/*

# Installera fran privat
pip install --index-url http://localhost:3141/myuser/dev devops-tool
```

---

## 9. GitHub Release

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Build
        run: |
          pip install build
          python -m build

      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          password: ${{ secrets.PYPI_API_TOKEN }}
```

---

## Sammanfattning

| Steg | Kommando |
|------|----------|
| Build | `python -m build` |
| Local install | `pip install -e .` |
| Publish | `twine upload dist/*` |
| Poetry build | `poetry build` |
| Poetry publish | `poetry publish` |
'''
}


# =============================================================================
# ADD FINAL NODES TO COLLECTION
# =============================================================================

PYTHON_SKILLSMAP_NODES.extend([
    NODE_15_LOGGING,
    NODE_16_TESTING,
    NODE_17_ASYNC,
    NODE_18_DECORATORS,
    NODE_19_TYPE_HINTS,
    NODE_20_PACKAGING,
])


# =============================================================================
# HELPER FUNCTION
# =============================================================================

def get_python_skillsmap_summary() -> Dict[str, Any]:
    """Return summary of Python SkillsMap progress."""
    total_nodes = 20
    completed_nodes = len(PYTHON_SKILLSMAP_NODES)
    return {
        "name": PYTHON_SKILLSMAP_INFO["name"],
        "total_nodes": total_nodes,
        "completed_nodes": completed_nodes,
        "progress_percent": (completed_nodes / total_nodes) * 100,
        "remaining_nodes": total_nodes - completed_nodes,
    }


if __name__ == "__main__":
    summary = get_python_skillsmap_summary()
    print(f"Python SkillsMap: {summary['completed_nodes']}/{summary['total_nodes']} nodes")
    print(f"Progress: {summary['progress_percent']:.0f}%")
