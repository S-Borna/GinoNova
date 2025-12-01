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
    "content": r"""# Python Fundamentals

## Varfor Python for DevOps?

> "Python is the Swiss Army knife of DevOps. Ansible is Python. AWS Lambda loves Python. Kubernetes operators use Python. It's readable, powerful, and everywhere."

---

## Installation & Setup

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

## Nasta Steg

Du har nu grunderna. Nasta node: **Collections** - listor, dictionaries och sets.
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
    "content": r"""# Collections: Lists, Dicts, Sets

## Varfor detta ar kritiskt

> "DevOps handlar om att hantera MANGA saker - servrar, containers, configs. Collections ar hur du organiserar dem i Python."

---

## Lists (Listor)

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
    "content": r"""# Control Flow: If, Loops, Logic

## Varfor detta ar kritiskt

> "Automation ar logik. IF server ar nere, THEN starta om. FOR varje container, kolla status. Control flow ar hjarnan i dina scripts."

---

## If-satser

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

## Sammanfattning

| Syntax | Anvandning |
|--------|------------|
| `if/elif/else` | Villkor |
| `for x in list` | Iteration |
| `while condition` | Loop tills False |
| `break` | Avbryt loop |
| `continue` | Nasta iteration |
| `enumerate()` | Index + varde |
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
    "content": r"""# Functions & Arguments

## Varfor detta ar kritiskt

> "DRY - Don't Repeat Yourself. Funktioner ar hur du skriver kod en gang och anvander overallt. En bra deploy-funktion kan anvandas for alla dina projekt."

---

## Grundlaggande Funktioner

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
    "content": r"""# File I/O Operations

## Varfor detta ar kritiskt

> "DevOps = filer. Config files, log files, YAML, JSON, scripts. Du maste kunna lasa, skriva och manipulera filer effektivt."

---

## Lasa Filer

### Grundlaggande

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
    "content": r"""# Error Handling & Exceptions

## Varfor detta ar kritiskt

> "I produktion gar saker fel. Natverk timeout. Filer saknas. Servers svarar inte. Din kod maste hantera det gracefullt istallet for att krascha."

---

## Try / Except

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
    # More nodes to be added...
]


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
