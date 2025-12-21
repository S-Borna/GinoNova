# -*- coding: utf-8 -*-
"""
Python for DevOps - Docker-style V3 Format
Version: 3.0
Converted: 2025-12-09

Format: NODE_CONTENT_TEMPLATE.md (Swedish, no emojis, ASCII diagrams)
"""

MODULE = {
    "name": "Python for DevOps",
    "slug": "python-devops",
    "description": "Bemästra Python för automation, scripting och molninfrastruktur. Lär dig skriva effektiva DevOps-verktyg med Python.",
    "track_slug": "skillsmaps",
    "order_index": 2,
    "difficulty": "intermediate",
    "estimated_hours": 35,
    "prerequisites": ["linux-fundamentals"],
    "icon": "python",
    "color": "#3776AB",
    "tasks": [
        # =====================================================================
        # NODE 1: Python Fundamentals
        # =====================================================================
        {
            "title": "Python Fundamentals",
            "slug": "python-fundamentals",
            "difficulty": "beginner",
            "estimated_minutes": 60,
            "xp_reward": 70,
            "content": """# Python Fundamentals

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Python ar viktigt |
|----------|-------------------------|
| **Automation** | Skriv scripts for repetitiva tasks |
| **Ansible** | Helt byggt pa Python |
| **AWS Lambda** | Forstahandssprak for serverless |
| **Kubernetes** | Operators och controllers |
| **CI/CD** | Bygg custom tools och integrationer |

Som DevOps-ingenjor maste du forsta:

- **Grundlaggande syntax** sa du kan lasa och skriva scripts
- **Variabler och typer** sa du hanterar data korrekt
- **Virtual environments** sa du isolerar dependencies

------------------------------------------------------------

## Python i DevOps-ekosystemet

```
+-------------------------------------------------------------+
|                PYTHON I DEVOPS                              |
+-------------------------------------------------------------+
|                                                             |
|  +----------+  +----------+  +----------+  +----------+   |
|  | Ansible  |  |  AWS     |  |Kubernetes|  | Terraform|   |
|  | YAML +   |  |  Lambda  |  | Operators|  | Providers|   |
|  | Python   |  |  Python  |  |  Python  |  |  Python  |   |
|  +----+-----+  +----+-----+  +----+-----+  +----+-----+   |
|       |             |             |             |          |
|       +-------------+------+------+-------------+          |
|                            |                               |
|                 +----------▼----------+                    |
|                 |    PYTHON CORE      |                    |
|                 |  (Din grund)        |                    |
|                 +---------------------+                    |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Installation och Setup

```bash
# Kontrollera version
python3 --version
# Python 3.11.x

# Skapa virtual environment (best practice)
python3 -m venv venv

# Aktivera (Linux/Mac)
source venv/bin/activate

# Aktivera (Windows)
venv\\Scripts\\activate

# Verifiera aktivering
which python
# /path/to/venv/bin/python

# Avaktivera
deactivate
```

------------------------------------------------------------

## Variabler och Datatyper

### Grundlaggande typer

```python
# Strings (text)
hostname = "prod-server-01"
environment = 'production'

# Numbers
port = 8080              # int (heltal)
cpu_usage = 75.5         # float (decimaltal)
max_connections = 1000   # int

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
deployment_count = 5

# SCREAMING_SNAKE_CASE for konstanter
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

# Undvik:
# - camelCase (Java/JavaScript-stil)
# - namn som borjar med siffra
# - reserverade ord (class, def, return, etc.)
```

------------------------------------------------------------

## Strings

### Skapa och manipulera

```python
# Skapa strings
name = "nginx"
path = '/var/log/nginx'

# Multi-line strings
config = \"\"\"
server {
    listen 80;
    server_name example.com;
}
\"\"\"

# f-strings (formaterade strings) - REKOMMENDERAT
server = "web-01"
port = 8080
url = f"http://{server}:{port}"
# "http://web-01:8080"

# String-metoder
filename = "access.log"
print(filename.upper())         # "ACCESS.LOG"
print(filename.replace(".", "_"))  # "access_log"
print(filename.split("."))      # ["access", "log"]
print(filename.endswith(".log"))  # True
```

### Praktiska string-operationer

```python
# Bygga filvagar
base_path = "/var/log"
app_name = "myapp"
log_file = f"{base_path}/{app_name}/app.log"

# Ta bort whitespace
user_input = "  prod-server  \\n"
clean_input = user_input.strip()  # "prod-server"

# Kontrollera innehall
hostname = "prod-web-01"
if hostname.startswith("prod-"):
    print("Production server detected")

# Splitta och joina
servers = "web-01,web-02,web-03"
server_list = servers.split(",")  # ["web-01", "web-02", "web-03"]
rejoined = "-".join(server_list)  # "web-01-web-02-web-03"
```

------------------------------------------------------------

## Numbers och Berakningar

```python
# Grundlaggande aritmetik
total = 10 + 5      # 15
diff = 10 - 5       # 5
product = 10 * 5    # 50
quotient = 10 / 3   # 3.333...
integer_div = 10 // 3  # 3 (heltalsdivision)
remainder = 10 % 3  # 1 (modulo)
power = 2 ** 10     # 1024

# Praktiskt: Minnesberakning
total_memory_gb = 16
used_memory_gb = 12.5
free_memory_gb = total_memory_gb - used_memory_gb
usage_percent = (used_memory_gb / total_memory_gb) * 100

print(f"Memory: {used_memory_gb}/{total_memory_gb} GB")
print(f"Usage: {usage_percent:.1f}%")  # "Usage: 78.1%"

# Avrundning
cpu = 67.89
print(round(cpu, 1))  # 67.9
print(int(cpu))       # 67 (trunkerar)
```

------------------------------------------------------------

## Booleans och Jamforelser

```python
# Booleans
is_running = True
is_failed = False

# Jamforelser
print(10 > 5)       # True
print(10 == 10)     # True
print(10 != 5)      # True
print(10 >= 10)     # True

# Logiska operatorer
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Praktiskt DevOps-exempel
health_check_passed = True
enough_memory = True
within_maintenance_window = False

can_deploy = health_check_passed and enough_memory
should_skip = not within_maintenance_window

if can_deploy and should_skip:
    print("Ready for deployment")
```

------------------------------------------------------------

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

# Praktiskt: Environment variables ar alltid strings
import os
timeout_str = os.environ.get("TIMEOUT", "30")
timeout = int(timeout_str)  # Konvertera till int for anvandning
```

------------------------------------------------------------

## Snabbreferens - Grundlaggande Syntax

| Koncept | Exempel |
|---------|---------|
| String | `name = "nginx"` |
| Integer | `port = 8080` |
| Float | `cpu = 75.5` |
| Boolean | `is_running = True` |
| f-string | `f"Port: {port}"` |
| Type check | `isinstance(x, int)` |
| Konvertera | `int("8080")` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `NameError: name 'x' is not defined` | Variabel finns ej | Definiera fore anvandning |
| `TypeError: can only concatenate str` | Blandar typer | Anvand f-string eller str() |
| `SyntaxError: invalid syntax` | Felaktig syntax | Kolla parenteser, kolon |
| `IndentationError` | Fel indentering | Anvand 4 spaces konsekvent |
| `ValueError: invalid literal` | Kan ej konvertera | Validera input forst |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **snake_case** | Standard for Python-variabler |
| **f-strings** | Basta sattet att formatera text |
| **Virtual env** | Alltid anvand for projekt |
| **Typer** | str, int, float, bool, None |
| **isinstance()** | Battre an type() for kontroll |

**Kom ihag:**
- Alltid skapa virtual environment for projekt
- Anvand f-strings istallet for + for stringar
- Python ar dynamiskt typat men typer spelar roll
- Indentering ar syntax, inte bara stil
- Variabler behover inte deklareras med typ
"""
        },
        # =====================================================================
        # NODE 2: Collections - Lists, Dicts, Sets
        # =====================================================================
        {
            "title": "Collections - Lists, Dicts, Sets",
            "slug": "python-collections",
            "difficulty": "beginner",
            "estimated_minutes": 55,
            "xp_reward": 75,
            "content": """# Collections - Lists, Dicts, Sets

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Collections ar viktigt |
|----------|------------------------------|
| **Server lists** | Hantera fleet av servrar |
| **Config data** | Key-value pairs for settings |
| **Inventory** | Ansible inventory ar dicts |
| **Unique items** | Sets for deduplikering |
| **Data processing** | Batch-operationer |

Som DevOps-ingenjor maste du forsta:

- **Lists** sa du kan hantera ordnade sekvenser
- **Dicts** sa du kan lagra key-value data
- **Sets** sa du kan hitta unika varden

------------------------------------------------------------

## Collection Types Oversikt

```
+-------------------------------------------------------------+
|                 PYTHON COLLECTIONS                          |
+-------------------------------------------------------------+
|                                                             |
|  LIST (ordnad, mutabel)                                    |
|  +-----+-----+-----+-----+-----+                          |
|  |  0  |  1  |  2  |  3  |  4  |  <- index                |
|  |web-1|web-2|web-3|db-1 |db-2 |                          |
|  +-----+-----+-----+-----+-----+                          |
|                                                             |
|  DICT (key-value, mutabel)                                 |
|  +--------------------------------------+                  |
|  | "hostname" -> "prod-web-01"          |                  |
|  | "port"     -> 8080                   |                  |
|  | "env"      -> "production"           |                  |
|  +--------------------------------------+                  |
|                                                             |
|  SET (unika varden, oordnad)                               |
|  +-----------------------------+                           |
|  | { "us-east", "eu-west",     |                           |
|  |   "ap-south" }              |  <- inga dubletter       |
|  +-----------------------------+                           |
|                                                             |
|  TUPLE (ordnad, IMMUTABEL)                                 |
|  +-----+-----+-----+                                       |
|  | "192.168.1.1" | 22 | "ssh" |  <- kan ej andras        |
|  +-----+-----+-----+                                       |
|                                                             |
+-------------------------------------------------------------+
```

------------------------------------------------------------

## Lists

### Skapa och komma at element

```python
# Skapa list
servers = ["web-01", "web-02", "web-03"]
ports = [80, 443, 8080, 3000]
mixed = ["nginx", 80, True, 3.14]  # Kan blanda typer

# Indexering (0-baserad)
first = servers[0]    # "web-01"
last = servers[-1]    # "web-03"
second_last = servers[-2]  # "web-02"

# Slicing
first_two = servers[0:2]   # ["web-01", "web-02"]
all_but_first = servers[1:]  # ["web-02", "web-03"]
every_other = ports[::2]   # [80, 8080]
```

### Modifiera lists

```python
servers = ["web-01", "web-02"]

# Lagg till element
servers.append("web-03")           # Lagg till sist
servers.insert(0, "lb-01")         # Lagg till forst
servers.extend(["db-01", "db-02"]) # Lagg till flera

# Ta bort element
servers.remove("web-01")  # Ta bort specifikt varde
last = servers.pop()      # Ta bort och returnera sista
first = servers.pop(0)    # Ta bort och returnera forsta
del servers[1]            # Ta bort via index

# Uppdatera
servers[0] = "new-server"

# Sortera
servers.sort()                # Sortera in-place
sorted_servers = sorted(servers)  # Ny sorterad lista
servers.reverse()             # Vand ordning
```

### List comprehensions

```python
# Traditionell loop
ports = []
for i in range(5):
    ports.append(8080 + i)
# [8080, 8081, 8082, 8083, 8084]

# List comprehension (Pythonic!)
ports = [8080 + i for i in range(5)]

# Med villkor
servers = ["web-01", "web-02", "db-01", "db-02"]
web_servers = [s for s in servers if s.startswith("web-")]
# ["web-01", "web-02"]

# Transformera
upper_servers = [s.upper() for s in servers]
# ["WEB-01", "WEB-02", "DB-01", "DB-02"]
```

------------------------------------------------------------

## Dictionaries

### Skapa och komma at

```python
# Skapa dict
server = {
    "hostname": "prod-web-01",
    "ip": "192.168.1.100",
    "port": 8080,
    "is_active": True
}

# Komma at varden
hostname = server["hostname"]      # KeyError om saknas
port = server.get("port")          # None om saknas
timeout = server.get("timeout", 30)  # Default om saknas

# Kolla om nyckel finns
if "ip" in server:
    print(f"IP: {server['ip']}")

# Alla nycklar, varden, par
keys = server.keys()       # dict_keys([...])
values = server.values()   # dict_values([...])
items = server.items()     # dict_items([(k, v), ...])
```

### Modifiera dicts

```python
server = {"hostname": "web-01", "port": 8080}

# Lagg till/uppdatera
server["ip"] = "192.168.1.100"     # Lagg till ny nyckel
server["port"] = 443               # Uppdatera existerande
server.update({"env": "prod", "region": "eu-west"})

# Ta bort
del server["port"]                 # Ta bort nyckel
port = server.pop("port", None)    # Ta bort och returnera

# Nested dicts
config = {
    "database": {
        "host": "db.example.com",
        "port": 5432,
        "credentials": {
            "user": "admin",
            "password": "secret"
        }
    },
    "cache": {
        "host": "redis.example.com",
        "port": 6379
    }
}

# Komma at nested
db_host = config["database"]["host"]
db_user = config["database"]["credentials"]["user"]

# Sakert satt med get
db_port = config.get("database", {}).get("port", 5432)
```

### Dict comprehensions

```python
# Skapa dict fran listor
servers = ["web-01", "web-02", "web-03"]
server_ports = {s: 8080 for s in servers}
# {"web-01": 8080, "web-02": 8080, "web-03": 8080}

# Med index
server_ports = {s: 8080 + i for i, s in enumerate(servers)}
# {"web-01": 8080, "web-02": 8081, "web-03": 8082}

# Filtrera dict
config = {"DEBUG": True, "PORT": 8080, "HOST": "0.0.0.0"}
string_values = {k: v for k, v in config.items() if isinstance(v, str)}
# {"HOST": "0.0.0.0"}
```

------------------------------------------------------------

## Sets

### Grundlaggande operationer

```python
# Skapa set
regions = {"us-east", "eu-west", "ap-south"}
more_regions = set(["us-east", "us-west"])  # Fran lista

# Inga dubletter
tags = {"web", "prod", "web", "critical"}
# {"web", "prod", "critical"} - "web" bara en gang

# Lagg till/ta bort
regions.add("ap-north")
regions.remove("eu-west")    # KeyError om saknas
regions.discard("eu-west")   # Tyst om saknas

# Kolla medlemskap (SNABBT - O(1))
if "us-east" in regions:
    print("US East is available")
```

### Set-operationer

```python
prod_servers = {"web-01", "web-02", "db-01"}
monitored = {"web-01", "db-01", "cache-01"}

# Union - alla unika
all_servers = prod_servers | monitored
# {"web-01", "web-02", "db-01", "cache-01"}

# Intersection - gemensamma
both = prod_servers & monitored
# {"web-01", "db-01"}

# Difference - finns i forsta men inte andra
unmonitored = prod_servers - monitored
# {"web-02"}

# Symmetric difference - finns i en men inte bada
exclusive = prod_servers ^ monitored
# {"web-02", "cache-01"}
```

### Praktiskt: Hitta skillnader

```python
# Hitta nya/borttagna servrar
old_inventory = {"web-01", "web-02", "db-01"}
new_inventory = {"web-01", "web-03", "db-01"}

added = new_inventory - old_inventory    # {"web-03"}
removed = old_inventory - new_inventory  # {"web-02"}
unchanged = old_inventory & new_inventory  # {"web-01", "db-01"}

print(f"Added: {added}")
print(f"Removed: {removed}")
```

------------------------------------------------------------

## Tuples

```python
# Immutabel (kan ej andras)
server_info = ("192.168.1.100", 22, "ssh")

# Unpacking
ip, port, protocol = server_info

# Anvands ofta for:
# - Dictionary keys (lists kan ej vara keys)
# - Returnera flera varden fran funktion
# - Data som inte ska andras

# Som dict key
connections = {}
connections[("192.168.1.100", 22)] = "active"
connections[("192.168.1.101", 443)] = "idle"

# Named tuples (battre alternativ)
from collections import namedtuple

Server = namedtuple("Server", ["hostname", "ip", "port"])
web = Server("web-01", "192.168.1.100", 8080)
print(web.hostname)  # "web-01"
print(web.port)      # 8080
```

------------------------------------------------------------

## Iteration

```python
# Iterera over list
servers = ["web-01", "web-02", "web-03"]
for server in servers:
    print(f"Checking {server}")

# Med index (enumerate)
for i, server in enumerate(servers):
    print(f"{i}: {server}")

# Iterera over dict
config = {"host": "localhost", "port": 8080}

for key in config:
    print(f"{key}: {config[key]}")

for key, value in config.items():  # Battre!
    print(f"{key}: {value}")

# Iterera over set
regions = {"us-east", "eu-west"}
for region in regions:
    print(f"Deploying to {region}")

# Zip - kombinera listor
hosts = ["web-01", "web-02"]
ips = ["192.168.1.1", "192.168.1.2"]
for host, ip in zip(hosts, ips):
    print(f"{host}: {ip}")
```

------------------------------------------------------------

## Snabbreferens - Collections

| Operation | List | Dict | Set |
|-----------|------|------|-----|
| Skapa | `[]` | `{}` | `set()` |
| Lagg till | `append()` | `d[k]=v` | `add()` |
| Ta bort | `remove()` | `del d[k]` | `discard()` |
| Kolla | `in` | `in` (keys) | `in` |
| Langd | `len()` | `len()` | `len()` |
| Ordnad | Ja | Ja (3.7+) | Nej |
| Dubletter | Ja | Keys unika | Nej |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `IndexError` | Index utanfor range | Kolla langd forst |
| `KeyError` | Nyckel finns ej | Anvand `.get()` |
| `TypeError: unhashable` | List som dict key | Anvand tuple |
| Tom iteration | Tom collection | Kolla `if collection:` |
| Modify during iteration | Andrar under loop | Iterera over kopia |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **List** | Ordnad, mutabel, index-baserad |
| **Dict** | Key-value, snabb lookup |
| **Set** | Unika varden, matematiska operationer |
| **Comprehensions** | Pythonic satt att skapa |
| **get()** | Sakrare an direkt access |

**Kom ihag:**
- List for ordnade sekvenser med dubletter
- Dict for key-value mapping
- Set for unika varden och membership testing
- Comprehensions ar snabbare och mer lasbara
- Anvand .get() for sakerare dict-access
"""
        },
        # =====================================================================
        # NODE 3: Control Flow
        # =====================================================================
        {
            "title": "Control Flow",
            "slug": "python-control-flow",
            "difficulty": "beginner",
            "estimated_minutes": 50,
            "xp_reward": 70,
            "content": """# Control Flow

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Control Flow ar viktigt |
|----------|-------------------------------|
| **Health checks** | If/else for status |
| **Batch operations** | Loops over servers |
| **Retry logic** | While for forsok |
| **Error handling** | Conditional responses |
| **Config validation** | Multiple conditions |

Som DevOps-ingenjor maste du forsta:

- **if/elif/else** sa du kan gora beslut
- **for/while** sa du kan iterera
- **break/continue** sa du kontrollerar loopar

------------------------------------------------------------

## If/Elif/Else

### Grundlaggande syntax

```python
# Enkel if
cpu_usage = 85
if cpu_usage > 80:
    print("WARNING: High CPU usage!")

# If-else
is_healthy = True
if is_healthy:
    print("Service is running")
else:
    print("Service is down!")

# If-elif-else
status_code = 503

if status_code == 200:
    print("OK")
elif status_code == 404:
    print("Not Found")
elif status_code >= 500:
    print("Server Error")
else:
    print(f"Unknown status: {status_code}")
```

### Jamforelseoperatorer

```python
# Jamforelser
x == y    # Lika med
x != y    # Inte lika med
x > y     # Storre an
x < y     # Mindre an
x >= y    # Storre eller lika
x <= y    # Mindre eller lika

# Logiska operatorer
and       # Bada maste vara True
or        # Minst en maste vara True
not       # Inverterar

# Praktiskt exempel
memory_ok = memory_used < 90
cpu_ok = cpu_usage < 80
disk_ok = disk_usage < 85

if memory_ok and cpu_ok and disk_ok:
    print("System healthy")
elif not memory_ok:
    print("Memory warning")
elif not cpu_ok:
    print("CPU warning")
```

### Truthy och Falsy

```python
# Falsy varden (evalueras som False)
# - None
# - False
# - 0, 0.0
# - "" (tom string)
# - [], {}, set() (tomma collections)

# Truthy (allt annat)

# Praktiskt
servers = []
if servers:
    print("Processing servers")
else:
    print("No servers to process")

# Samma som:
if len(servers) > 0:
    print("Processing servers")

# None-check
result = get_server_status()
if result is None:
    print("No result")
elif result:
    print(f"Status: {result}")
```

------------------------------------------------------------

## For Loops

### Iterera over collections

```python
# Lista
servers = ["web-01", "web-02", "web-03"]
for server in servers:
    print(f"Deploying to {server}")

# Dict
config = {"host": "localhost", "port": 8080, "debug": True}
for key, value in config.items():
    print(f"{key} = {value}")

# Range
for i in range(5):       # 0, 1, 2, 3, 4
    print(f"Attempt {i + 1}")

for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(f"Server-{i}")

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

### Enumerate och Zip

```python
# Enumerate - ger index
servers = ["web-01", "web-02", "web-03"]
for index, server in enumerate(servers):
    print(f"{index}: {server}")
# 0: web-01
# 1: web-02
# 2: web-03

# Starta fran annat index
for index, server in enumerate(servers, start=1):
    print(f"Server {index}: {server}")

# Zip - kombinera listor
hostnames = ["web-01", "web-02"]
ips = ["192.168.1.1", "192.168.1.2"]
ports = [8080, 8081]

for hostname, ip, port in zip(hostnames, ips, ports):
    print(f"{hostname}: {ip}:{port}")
```

------------------------------------------------------------

## While Loops

### Grundlaggande while

```python
# Rakna ner
countdown = 5
while countdown > 0:
    print(f"T-{countdown}")
    countdown -= 1
print("Liftoff!")

# Retry logic
import time

max_retries = 3
attempt = 0
success = False

while attempt < max_retries and not success:
    attempt += 1
    print(f"Attempt {attempt}/{max_retries}")

    # Simulera anrop
    success = check_service_health()

    if not success and attempt < max_retries:
        print("Retrying in 5 seconds...")
        time.sleep(5)

if success:
    print("Service is healthy")
else:
    print("Service failed after all retries")
```

### Infinite loops med break

```python
# Polling loop
while True:
    status = get_deployment_status()

    if status == "completed":
        print("Deployment finished!")
        break
    elif status == "failed":
        print("Deployment failed!")
        break
    else:
        print(f"Status: {status}...")
        time.sleep(10)
```

------------------------------------------------------------

## Break, Continue, Else

### Break - avbryt loop

```python
servers = ["web-01", "web-02", "db-01", "web-03"]

# Hitta forsta databasserver
for server in servers:
    if server.startswith("db-"):
        print(f"Found database: {server}")
        break
    print(f"Checking {server}...")
```

### Continue - hoppa till nasta iteration

```python
servers = ["web-01", "", "web-02", None, "web-03"]

for server in servers:
    # Skippa tomma/None
    if not server:
        continue

    print(f"Deploying to {server}")
```

### Else pa loops

```python
# Else kors om loopen INTE avbryts med break
servers = ["web-01", "web-02", "web-03"]
target = "db-01"

for server in servers:
    if server == target:
        print(f"Found {target}")
        break
else:
    # Kors om break INTE anropades
    print(f"{target} not found in server list")
```

------------------------------------------------------------

## Praktiska Patterns

### Health Check Loop

```python
def check_all_services():
    services = {
        "api": "http://localhost:8080/health",
        "db": "localhost:5432",
        "cache": "localhost:6379"
    }

    all_healthy = True

    for name, endpoint in services.items():
        status = check_health(endpoint)

        if status == "healthy":
            print(f"[OK] {name}")
        else:
            print(f"[FAIL] {name}: {status}")
            all_healthy = False

    return all_healthy
```

### Retry with Exponential Backoff

```python
import time

def retry_with_backoff(func, max_retries=5, base_delay=1):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise  # Sista forsoket - kasta exception

            delay = base_delay * (2 ** attempt)  # 1, 2, 4, 8, 16
            print(f"Attempt {attempt + 1} failed: {e}")
            print(f"Retrying in {delay}s...")
            time.sleep(delay)
```

### Batch Processing

```python
def process_in_batches(items, batch_size=10):
    total = len(items)
    processed = 0

    for i in range(0, total, batch_size):
        batch = items[i:i + batch_size]

        for item in batch:
            process_item(item)
            processed += 1

        print(f"Progress: {processed}/{total} ({processed/total*100:.1f}%)")
```

------------------------------------------------------------

## Ternary Operator

```python
# Enkel conditional assignment
status = "running" if is_active else "stopped"

# Equivalent till:
if is_active:
    status = "running"
else:
    status = "stopped"

# Praktiskt
log_level = "DEBUG" if debug_mode else "INFO"
port = int(port_str) if port_str else 8080
servers = server_list if server_list else ["localhost"]
```

------------------------------------------------------------

## Snabbreferens - Control Flow

| Konstruktion | Anvandning |
|--------------|------------|
| `if/elif/else` | Villkorlig exekvering |
| `for x in y` | Iterera over collection |
| `while cond` | Loop tills villkor falskt |
| `break` | Avbryt loop |
| `continue` | Hoppa till nasta iteration |
| `else` pa loop | Kors om ingen break |
| `x if c else y` | Ternary operator |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Infinite loop | Villkor aldrig falskt | Kolla break/update |
| Off-by-one | Fel range | range(1, n+1) |
| Modify during loop | Andrar list i loop | Iterera over kopia |
| Wrong indentation | Fel block | Konsekvent 4 spaces |
| Missing colon | Glom : efter if/for | Lagg till : |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Truthiness** | Tomma varden ar Falsy |
| **enumerate** | Battre an manuellt index |
| **zip** | Kombinera parallella listor |
| **break/continue** | Kontrollera loop flow |
| **else pa loop** | Nyttigt for "not found" |

**Kom ihag:**
- Anvand `for` nar du vet antalet iterationer
- Anvand `while` for okant antal eller polling
- `enumerate()` istallet for `range(len(x))`
- Ternary for enkla villkorliga assignments
- Undvik att modifiera lista medan du itererar
"""
        },
        # =====================================================================
        # NODE 4: Functions
        # =====================================================================
        {
            "title": "Functions",
            "slug": "python-functions",
            "difficulty": "beginner",
            "estimated_minutes": 55,
            "xp_reward": 75,
            "content": """# Functions

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Functions ar viktigt |
|----------|----------------------------|
| **Ateranvandning** | Skriv en gang, anvand overallt |
| **Testbarhet** | Isolerade enheter att testa |
| **Lashbarhet** | Klar struktur i kod |
| **Modularitet** | Byggblock for storre system |
| **Abstraktion** | Dolj komplexitet |

Som DevOps-ingenjor maste du forsta:

- **def** sa du kan definiera funktioner
- **Parametrar** sa du kan gora flexibla funktioner
- **Return** sa du kan returnera varden
- **Args/kwargs** sa du hanterar dynamiska argument

------------------------------------------------------------

## Definiera Functions

### Grundlaggande syntax

```python
# Enkel funktion
def greet():
    print("Hello, DevOps!")

# Anropa
greet()  # "Hello, DevOps!"

# Med parametrar
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")  # "Hello, Alice!"

# Med return
def get_server_url(host, port):
    return f"http://{host}:{port}"

url = get_server_url("localhost", 8080)
print(url)  # "http://localhost:8080"
```

### Multipla return-varden

```python
def get_server_status(server):
    # Simulerad logik
    is_healthy = True
    response_time = 45
    error_count = 0

    return is_healthy, response_time, error_count

# Unpacking
healthy, latency, errors = get_server_status("web-01")
print(f"Healthy: {healthy}, Latency: {latency}ms")

# Returnera som dict (battre for manga varden)
def get_server_metrics(server):
    return {
        "healthy": True,
        "cpu": 45.5,
        "memory": 62.3,
        "connections": 150
    }

metrics = get_server_metrics("web-01")
print(f"CPU: {metrics['cpu']}%")
```

------------------------------------------------------------

## Parametrar

### Default Parameters

```python
def deploy(service, environment="staging", replicas=1):
    print(f"Deploying {service} to {environment} with {replicas} replicas")

deploy("api")                           # api, staging, 1
deploy("api", "production")             # api, production, 1
deploy("api", "production", 3)          # api, production, 3
deploy("api", replicas=5)               # api, staging, 5
```

### Keyword Arguments

```python
def create_server(hostname, ip, port=22, env="dev"):
    return {
        "hostname": hostname,
        "ip": ip,
        "port": port,
        "env": env
    }

# Positional
server = create_server("web-01", "192.168.1.1")

# Keyword (mer lasbart)
server = create_server(
    hostname="web-01",
    ip="192.168.1.1",
    port=8080,
    env="prod"
)

# Blanda (positional forst!)
server = create_server("web-01", "192.168.1.1", env="prod")
```

### *args och **kwargs

```python
# *args - godtyckligt antal positionella argument
def deploy_services(*services):
    for service in services:
        print(f"Deploying {service}")

deploy_services("api", "worker", "scheduler")

# **kwargs - godtyckligt antal keyword arguments
def create_config(**settings):
    config = {}
    for key, value in settings.items():
        config[key.upper()] = value
    return config

config = create_config(host="localhost", port=8080, debug=True)
# {"HOST": "localhost", "PORT": 8080, "DEBUG": True}

# Kombinera
def setup_deployment(name, *servers, **options):
    print(f"Deployment: {name}")
    print(f"Servers: {servers}")
    print(f"Options: {options}")

setup_deployment(
    "web-app",
    "web-01", "web-02", "web-03",
    env="prod",
    replicas=3
)
```

------------------------------------------------------------

## Docstrings

```python
def check_service_health(host, port, timeout=5):
    \"\"\"
    Check if a service is responding on the given host and port.

    Args:
        host: The hostname or IP address to check.
        port: The port number to connect to.
        timeout: Connection timeout in seconds (default: 5).

    Returns:
        dict: A dictionary containing:
            - healthy (bool): Whether the service is responding
            - response_time (float): Response time in milliseconds
            - error (str|None): Error message if unhealthy

    Raises:
        ValueError: If port is not in valid range.

    Example:
        >>> result = check_service_health("localhost", 8080)
        >>> if result["healthy"]:
        ...     print(f"Service up, latency: {result['response_time']}ms")
    \"\"\"
    if not 1 <= port <= 65535:
        raise ValueError(f"Invalid port: {port}")

    # Implementation...
    return {"healthy": True, "response_time": 15.3, "error": None}

# Visa docstring
help(check_service_health)
print(check_service_health.__doc__)
```

------------------------------------------------------------

## Lambda Functions

```python
# Kortform for enkla funktioner
square = lambda x: x ** 2
print(square(5))  # 25

# Anvandning med sort
servers = [
    {"name": "web-01", "cpu": 45},
    {"name": "web-02", "cpu": 78},
    {"name": "web-03", "cpu": 23}
]

# Sortera efter CPU
sorted_servers = sorted(servers, key=lambda s: s["cpu"])

# Sortera efter namn
sorted_servers = sorted(servers, key=lambda s: s["name"])

# Med filter
healthy = list(filter(lambda s: s["cpu"] < 80, servers))

# Med map
names = list(map(lambda s: s["name"], servers))
# ["web-01", "web-02", "web-03"]
```

------------------------------------------------------------

## Scope

```python
# Global scope
API_URL = "https://api.example.com"  # Global

def make_request():
    # Lokal scope
    endpoint = "/health"  # Lokal
    return f"{API_URL}{endpoint}"  # Kan lasa global

# Modifiera global (undvik om mojligt!)
request_count = 0

def make_request():
    global request_count
    request_count += 1
    # ...

# Battre: returnera nytt varde
def make_request(count):
    return count + 1

request_count = make_request(request_count)
```

------------------------------------------------------------

## Praktiska DevOps Functions

### Health Check Function

```python
import requests
from typing import Dict, Any

def check_health(url: str, timeout: int = 5) -> Dict[str, Any]:
    \"\"\"Check health of an HTTP endpoint.\"\"\"
    try:
        response = requests.get(f"{url}/health", timeout=timeout)
        return {
            "healthy": response.status_code == 200,
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds() * 1000
        }
    except requests.RequestException as e:
        return {
            "healthy": False,
            "status_code": None,
            "error": str(e)
        }
```

### Retry Function

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1, backoff=2):
    \"\"\"Decorator for retry logic with exponential backoff.\"\"\"
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def call_api(endpoint):
    # API call that might fail
    pass
```

### Config Builder

```python
def build_config(
    app_name: str,
    env: str = "dev",
    **overrides
) -> dict:
    \"\"\"Build application configuration.\"\"\"
    defaults = {
        "dev": {
            "debug": True,
            "log_level": "DEBUG",
            "replicas": 1
        },
        "staging": {
            "debug": False,
            "log_level": "INFO",
            "replicas": 2
        },
        "prod": {
            "debug": False,
            "log_level": "WARNING",
            "replicas": 3
        }
    }

    config = {
        "app_name": app_name,
        "environment": env,
        **defaults.get(env, defaults["dev"]),
        **overrides  # Override defaults
    }

    return config

# Anvandning
config = build_config("my-api", "prod", replicas=5, custom_setting="value")
```

------------------------------------------------------------

## Snabbreferens - Functions

| Koncept | Exempel |
|---------|---------|
| Definiera | `def func():` |
| Parametrar | `def func(a, b):` |
| Default | `def func(a=1):` |
| Return | `return value` |
| *args | `def func(*args):` |
| **kwargs | `def func(**kwargs):` |
| Lambda | `lambda x: x * 2` |
| Docstring | `\"\"\"Description\"\"\"` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Mutable default | `def f(x=[]):` | Anvand `x=None` |
| Missing return | Glom return | Explicit return |
| Wrong arg order | Pos efter keyword | Pos forst |
| Scope confusion | Modifiera global | Anvand return |
| Recursion limit | For djup rekursion | Iterativ losning |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Docstrings** | Dokumentera alltid |
| **Default params** | Gor flexibla funktioner |
| **kwargs** | For config-liknande input |
| **Single responsibility** | En funktion = en uppgift |
| **Return early** | Undvik djup nesting |

**Kom ihag:**
- Undvik mutable defaults (`def f(x=[]):`)
- Anvand keyword args for tydlighet
- Skriv docstrings for publika funktioner
- Hog cohesion - en funktion gor en sak
- Return tidigt for att undvika djup nesting
"""
        },
        # =====================================================================
        # NODE 5: File I/O
        # =====================================================================
        {
            "title": "File I/O",
            "slug": "python-file-io",
            "difficulty": "beginner",
            "estimated_minutes": 50,
            "xp_reward": 70,
            "content": """# File I/O

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor File I/O ar viktigt |
|----------|---------------------------|
| **Config files** | Lasa/skriva YAML, JSON |
| **Log parsing** | Analysera loggfiler |
| **Reports** | Generera deployment reports |
| **Inventory** | Hantera server-listor |
| **Backup scripts** | Kopiera och arkivera |

Som DevOps-ingenjor maste du forsta:

- **open()** sa du kan oppna filer
- **with statement** sa resurser stangs korrekt
- **pathlib** sa du hanterar sokvagar portabelt

------------------------------------------------------------

## Lasa Filer

### Grundlaggande lasning

```python
# Med with (rekommenderat - stangs automatiskt)
with open("servers.txt", "r") as f:
    content = f.read()  # Hela filen som en string
print(content)

# Lasa rad for rad
with open("servers.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip() tar bort newline

# Lasa alla rader till lista
with open("servers.txt", "r") as f:
    lines = f.readlines()
    # ["web-01\\n", "web-02\\n", "web-03\\n"]

# Batter: List comprehension med strip
with open("servers.txt", "r") as f:
    servers = [line.strip() for line in f]
    # ["web-01", "web-02", "web-03"]
```

### Hantera encoding

```python
# Explicit encoding (rekommenderat)
with open("config.txt", "r", encoding="utf-8") as f:
    content = f.read()

# For filer med annan encoding
with open("legacy.txt", "r", encoding="latin-1") as f:
    content = f.read()
```

------------------------------------------------------------

## Skriva Filer

### Grundlaggande skrivning

```python
# Skriv (ersatt innehall)
with open("output.txt", "w") as f:
    f.write("Server report\\n")
    f.write("=============\\n")

# Lagg till (append)
with open("log.txt", "a") as f:
    f.write("2024-01-15 10:30:00 - Deployment started\\n")

# Skriv flera rader
lines = ["web-01", "web-02", "web-03"]
with open("servers.txt", "w") as f:
    for server in lines:
        f.write(f"{server}\\n")

# Eller med writelines
with open("servers.txt", "w") as f:
    f.writelines(f"{s}\\n" for s in lines)
```

### File Modes

| Mode | Beskrivning |
|------|-------------|
| `r` | Read (default) |
| `w` | Write (ersatter) |
| `a` | Append |
| `r+` | Read and write |
| `b` | Binary mode |
| `x` | Exclusive create |

```python
# Binary mode (for bilder, etc)
with open("image.png", "rb") as f:
    data = f.read()

# Exclusive create (error om finns)
try:
    with open("new_file.txt", "x") as f:
        f.write("New content")
except FileExistsError:
    print("File already exists!")
```

------------------------------------------------------------

## Pathlib (Modern Python)

```python
from pathlib import Path

# Skapa path
config_path = Path("/etc/nginx/nginx.conf")
log_dir = Path("/var/log/myapp")

# Egenskaper
print(config_path.name)      # "nginx.conf"
print(config_path.stem)      # "nginx"
print(config_path.suffix)    # ".conf"
print(config_path.parent)    # Path("/etc/nginx")

# Bygga paths (cross-platform)
base = Path("/var/log")
app_log = base / "myapp" / "app.log"
# Path("/var/log/myapp/app.log")

# Kolla existens
if config_path.exists():
    print("Config found")

if log_dir.is_dir():
    print("Log directory exists")

if config_path.is_file():
    print("Is a file")
```

### Pathlib for File I/O

```python
from pathlib import Path

path = Path("servers.txt")

# Lasa
content = path.read_text(encoding="utf-8")
binary = path.read_bytes()

# Skriv
path.write_text("web-01\\nweb-02\\n", encoding="utf-8")
path.write_bytes(binary_data)

# Kombinera med open
with path.open("r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### Katalogoperationer

```python
from pathlib import Path

log_dir = Path("/var/log/myapp")

# Skapa katalog
log_dir.mkdir(parents=True, exist_ok=True)

# Lista filer
for file in log_dir.iterdir():
    print(file.name)

# Glob patterns
for log_file in log_dir.glob("*.log"):
    print(log_file)

# Rekursiv glob
for py_file in Path(".").rglob("*.py"):
    print(py_file)

# Ta bort
empty_file = Path("temp.txt")
empty_file.unlink(missing_ok=True)  # Ta bort fil

empty_dir = Path("temp_dir")
empty_dir.rmdir()  # Endast tom katalog
```

------------------------------------------------------------

## Praktiska Exempel

### Log Parser

```python
from pathlib import Path
from collections import Counter

def parse_access_log(log_path):
    \"\"\"Parse nginx access log and count status codes.\"\"\"
    status_counts = Counter()

    with open(log_path, "r") as f:
        for line in f:
            # Format: IP - - [date] "request" status size
            parts = line.split()
            if len(parts) >= 9:
                status_code = parts[8]
                status_counts[status_code] += 1

    return status_counts

# Anvandning
counts = parse_access_log("/var/log/nginx/access.log")
for status, count in counts.most_common(10):
    print(f"{status}: {count}")
```

### Config File Manager

```python
from pathlib import Path

def backup_config(config_path, backup_dir):
    \"\"\"Backup a config file with timestamp.\"\"\"
    from datetime import datetime

    config = Path(config_path)
    backup = Path(backup_dir)

    if not config.exists():
        raise FileNotFoundError(f"Config not found: {config}")

    backup.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{config.stem}_{timestamp}{config.suffix}"
    backup_path = backup / backup_name

    backup_path.write_bytes(config.read_bytes())

    return backup_path

# Anvandning
backup = backup_config(
    "/etc/nginx/nginx.conf",
    "/backup/nginx"
)
print(f"Backup created: {backup}")
```

### Server Inventory

```python
from pathlib import Path

def load_inventory(path):
    \"\"\"Load server inventory from file.\"\"\"
    inventory = {"web": [], "db": [], "cache": []}

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if line.startswith("web-"):
                inventory["web"].append(line)
            elif line.startswith("db-"):
                inventory["db"].append(line)
            elif line.startswith("cache-"):
                inventory["cache"].append(line)

    return inventory

def save_inventory(inventory, path):
    \"\"\"Save server inventory to file.\"\"\"
    with open(path, "w") as f:
        f.write("# Server Inventory\\n\\n")
        for category, servers in inventory.items():
            f.write(f"# {category.upper()}\\n")
            for server in servers:
                f.write(f"{server}\\n")
            f.write("\\n")
```

------------------------------------------------------------

## Tempfiler

```python
import tempfile
from pathlib import Path

# Tempfil som auto-raderas
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
    f.write("Temporary content")
    temp_path = f.name

print(f"Temp file: {temp_path}")
Path(temp_path).unlink()  # Radera manuellt

# Tempkatalog
with tempfile.TemporaryDirectory() as tmpdir:
    temp_file = Path(tmpdir) / "data.txt"
    temp_file.write_text("Data")
    # Katalog och innehall raderas automatiskt

# For deployment scripts
def deploy_with_temp_config(config_data):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml") as f:
        f.write(config_data)
        f.flush()
        # Anvand temp config
        run_deployment(f.name)
```

------------------------------------------------------------

## Snabbreferens - File I/O

| Operation | Kod |
|-----------|-----|
| Lasa | `path.read_text()` |
| Skriv | `path.write_text()` |
| Finns? | `path.exists()` |
| Katalog? | `path.is_dir()` |
| Skapa dir | `path.mkdir(parents=True)` |
| Lista | `path.iterdir()` |
| Glob | `path.glob("*.log")` |
| Parent | `path.parent` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `FileNotFoundError` | Fil finns ej | Kolla `path.exists()` |
| `PermissionError` | Saknar rattigheter | Kolla chmod/chown |
| `UnicodeDecodeError` | Fel encoding | Ange ratt encoding |
| `IsADirectoryError` | Oppnar dir som fil | Kolla `is_file()` |
| File not closed | Glom stanga | Anvand `with` |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **with** | Alltid for fil-operationer |
| **pathlib** | Modern, cross-platform paths |
| **encoding** | Ange alltid utf-8 |
| **exists()** | Kolla fore lasning |
| **parents=True** | Skapa hela sokvagen |

**Kom ihag:**
- Alltid anvand `with` for automatisk stangning
- Pathlib ar battre an os.path
- Ange encoding explicit
- Kolla om fil/katalog finns fore operation
- Anvand tempfile for temporara filer
"""
        },
        # =====================================================================
        # NODE 6: Error Handling
        # =====================================================================
        {
            "title": "Error Handling",
            "slug": "python-error-handling",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Error Handling

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Error Handling ar viktigt |
|----------|----------------------------------|
| **Resilience** | Scripts ska ej krascha |
| **Debugging** | Tydliga felmeddelanden |
| **Retry logic** | Hantera transient failures |
| **Graceful degradation** | Fortsatt aven vid problem |
| **Audit** | Logga fel for analys |

Som DevOps-ingenjor maste du forsta:

- **try/except** sa du kan fanga fel
- **Exception types** sa du hanterar ratt fel
- **raise** sa du kan skapa egna fel
- **finally** sa cleanup alltid sker

------------------------------------------------------------

## Try/Except Grunderna

### Grundlaggande syntax

```python
# Enkel try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Fanga exception-objekt
try:
    file = open("nonexistent.txt")
except FileNotFoundError as e:
    print(f"Error: {e}")
    # Error: [Errno 2] No such file or directory: 'nonexistent.txt'

# Flera except-block
try:
    data = get_server_data(server)
    port = int(data["port"])
except KeyError:
    print("Missing port in config")
except ValueError:
    print("Invalid port number")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Exception Hierarki

```
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- Exception
    +-- StopIteration
    +-- ArithmeticError
    |   +-- ZeroDivisionError
    |   +-- OverflowError
    +-- LookupError
    |   +-- KeyError
    |   +-- IndexError
    +-- OSError
    |   +-- FileNotFoundError
    |   +-- PermissionError
    |   +-- ConnectionError
    +-- ValueError
    +-- TypeError
    +-- RuntimeError
```

------------------------------------------------------------

## Else och Finally

```python
try:
    file = open("config.txt")
    data = file.read()
except FileNotFoundError:
    print("Config not found, using defaults")
    data = "default config"
else:
    # Kors ENDAST om inget exception
    print("Config loaded successfully")
finally:
    # Kors ALLTID
    print("Cleanup complete")

# Praktiskt exempel
def process_deployment_file(path):
    file = None
    try:
        file = open(path)
        config = parse_config(file.read())
        validate_config(config)
        return config
    except FileNotFoundError:
        raise DeploymentError(f"Config file not found: {path}")
    except ValidationError as e:
        raise DeploymentError(f"Invalid config: {e}")
    finally:
        if file:
            file.close()
```

------------------------------------------------------------

## Raise Exceptions

### Kasta exceptions

```python
def deploy_service(name, replicas):
    if not name:
        raise ValueError("Service name cannot be empty")

    if replicas < 1:
        raise ValueError(f"Replicas must be >= 1, got {replicas}")

    if replicas > 100:
        raise ValueError(f"Too many replicas: {replicas} (max 100)")

    # Deploy logic...

# Re-raise med context
try:
    deploy_service("api", 0)
except ValueError as e:
    logger.error(f"Deployment failed: {e}")
    raise  # Re-raise samma exception
```

### Custom Exceptions

```python
class DeploymentError(Exception):
    \"\"\"Base exception for deployment errors.\"\"\"
    pass

class ConfigurationError(DeploymentError):
    \"\"\"Raised when configuration is invalid.\"\"\"
    pass

class ServiceUnavailableError(DeploymentError):
    \"\"\"Raised when a service is not responding.\"\"\"
    def __init__(self, service_name, message=None):
        self.service_name = service_name
        self.message = message or f"Service {service_name} is unavailable"
        super().__init__(self.message)

# Anvandning
def check_service(name):
    if not ping_service(name):
        raise ServiceUnavailableError(name)

try:
    check_service("api")
except ServiceUnavailableError as e:
    print(f"Service {e.service_name} is down")
    send_alert(e.message)
```

------------------------------------------------------------

## Context Managers

```python
# with-statement for automatisk cleanup
with open("file.txt") as f:
    data = f.read()
# Filen stangs automatiskt, aven vid exception

# Skapa egen context manager
from contextlib import contextmanager

@contextmanager
def deployment_lock(service_name):
    \"\"\"Acquire deployment lock for a service.\"\"\"
    lock_file = f"/var/lock/{service_name}.lock"
    try:
        acquire_lock(lock_file)
        print(f"Lock acquired for {service_name}")
        yield
    except Exception as e:
        print(f"Deployment failed: {e}")
        raise
    finally:
        release_lock(lock_file)
        print(f"Lock released for {service_name}")

# Anvandning
with deployment_lock("api"):
    deploy_service("api")
```

------------------------------------------------------------

## Praktiska Patterns

### Retry Pattern

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    \"\"\"Decorator for retry logic with exponential backoff.\"\"\"
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed: {e}")
                        print(f"Retrying in {current_delay}s...")
                        time.sleep(current_delay)
                        current_delay *= backoff

            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1, exceptions=(ConnectionError, TimeoutError))
def call_api(endpoint):
    response = requests.get(endpoint, timeout=5)
    response.raise_for_status()
    return response.json()
```

### Fallback Pattern

```python
def get_config_value(key, fallback=None):
    \"\"\"Get config value with multiple fallback sources.\"\"\"
    # Try environment variable
    try:
        import os
        value = os.environ[key]
        if value:
            return value
    except KeyError:
        pass

    # Try config file
    try:
        with open("/etc/myapp/config.json") as f:
            config = json.load(f)
            return config[key]
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        pass

    # Try default config
    defaults = {"PORT": "8080", "HOST": "localhost"}
    if key in defaults:
        return defaults[key]

    # Return fallback
    if fallback is not None:
        return fallback

    raise ConfigurationError(f"No value found for {key}")
```

### Graceful Degradation

```python
def get_server_metrics(servers):
    \"\"\"Get metrics from all servers, continue on errors.\"\"\"
    results = {}
    errors = []

    for server in servers:
        try:
            metrics = fetch_metrics(server)
            results[server] = metrics
        except ConnectionError as e:
            errors.append({"server": server, "error": str(e)})
            results[server] = None  # Mark as unavailable
        except Exception as e:
            errors.append({"server": server, "error": str(e)})
            results[server] = None

    if errors:
        print(f"Warning: {len(errors)} servers failed")
        for err in errors:
            print(f"  - {err['server']}: {err['error']}")

    return results, errors
```

------------------------------------------------------------

## Logging Errors

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def deploy_service(service_name):
    logger.info(f"Starting deployment of {service_name}")

    try:
        pull_image(service_name)
        start_container(service_name)
        health_check(service_name)
        logger.info(f"Deployment of {service_name} successful")
    except ImageNotFoundError as e:
        logger.error(f"Image not found: {e}")
        raise
    except HealthCheckError as e:
        logger.warning(f"Health check failed: {e}")
        rollback(service_name)
        raise
    except Exception as e:
        logger.exception(f"Unexpected error deploying {service_name}")
        # exception() loggar full traceback
        raise
```

------------------------------------------------------------

## Snabbreferens - Exceptions

| Exception | Nar den kastas |
|-----------|----------------|
| `ValueError` | Fel varde |
| `TypeError` | Fel typ |
| `KeyError` | Dict key finns ej |
| `IndexError` | List index out of range |
| `FileNotFoundError` | Fil finns ej |
| `PermissionError` | Saknar rattigheter |
| `ConnectionError` | Natverksfel |
| `TimeoutError` | Timeout |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Broad except | `except:` fangar allt | Specifika exceptions |
| Silent failure | Exception ignoreras | Logga eller re-raise |
| Lost traceback | `raise e` istallet for `raise` | Anvand bara `raise` |
| Unhandled | Inget except-block | Lagg till error handling |
| Wrong order | General fore specifik | Specifik forst |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Specifika except** | Fanga ratt exception |
| **finally** | Cleanup ska alltid ske |
| **Custom exceptions** | Tydligare felhantering |
| **Logging** | Alltid logga errors |
| **Retry** | For transient failures |

**Kom ihag:**
- Undvik `except:` utan exception typ
- Anvand `raise` utan argument for re-raise
- Custom exceptions gor kod tydligare
- finally kors alltid, aven vid return
- Logga exceptions for debugging
"""
        },
        # =====================================================================
        # NODE 7: Object-Oriented Programming
        # =====================================================================
        {
            "title": "Object-Oriented Programming",
            "slug": "python-oop",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 90,
            "content": """# Object-Oriented Programming

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor OOP ar viktigt |
|----------|----------------------|
| **SDK:er** | Alla cloud SDK:er ar OOP |
| **Abstraktion** | Model komplexa system |
| **Plugins** | Utokningsbar arkitektur |
| **Testing** | Mocking och dependency injection |
| **Ansible modules** | Bygger pa klasser |

Som DevOps-ingenjor maste du forsta:

- **Classes** sa du kan modellera resurser
- **Inheritance** sa du kan utoka funktionalitet
- **Methods** sa du kan definiera beteenden

------------------------------------------------------------

## Classes och Objects

### Grundlaggande class

```python
class Server:
    \"\"\"Represents a server in the infrastructure.\"\"\"

    def __init__(self, hostname, ip, port=22):
        \"\"\"Initialize server with connection details.\"\"\"
        self.hostname = hostname
        self.ip = ip
        self.port = port
        self.status = "unknown"

    def connect(self):
        \"\"\"Establish connection to server.\"\"\"
        print(f"Connecting to {self.hostname} ({self.ip}:{self.port})")
        self.status = "connected"

    def disconnect(self):
        \"\"\"Close connection to server.\"\"\"
        print(f"Disconnecting from {self.hostname}")
        self.status = "disconnected"

    def __str__(self):
        \"\"\"String representation.\"\"\"
        return f"Server({self.hostname}, {self.ip})"

    def __repr__(self):
        \"\"\"Debug representation.\"\"\"
        return f"Server(hostname='{self.hostname}', ip='{self.ip}', port={self.port})"

# Anvandning
web = Server("web-01", "192.168.1.100", 8080)
print(web.hostname)  # "web-01"
web.connect()        # "Connecting to web-01 (192.168.1.100:8080)"
print(web)           # "Server(web-01, 192.168.1.100)"
```

### Class Attributes vs Instance Attributes

```python
class Server:
    # Class attribute - delad mellan alla instanser
    default_port = 22
    all_servers = []

    def __init__(self, hostname, ip):
        # Instance attributes - unika per instans
        self.hostname = hostname
        self.ip = ip
        self.port = Server.default_port
        Server.all_servers.append(self)

    @classmethod
    def get_all_servers(cls):
        return cls.all_servers

    @classmethod
    def from_string(cls, server_string):
        \"\"\"Create server from string format 'hostname:ip'.\"\"\"
        hostname, ip = server_string.split(":")
        return cls(hostname, ip)

# Anvandning
web1 = Server("web-01", "192.168.1.1")
web2 = Server("web-02", "192.168.1.2")

print(Server.all_servers)  # [Server(...), Server(...)]
db = Server.from_string("db-01:192.168.1.10")
```

------------------------------------------------------------

## Inheritance

```python
class Server:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

    def connect(self):
        print(f"Connecting to {self.hostname}")

    def get_info(self):
        return {"hostname": self.hostname, "ip": self.ip}

class WebServer(Server):
    def __init__(self, hostname, ip, port=80):
        super().__init__(hostname, ip)  # Anropa parent __init__
        self.port = port

    def get_url(self):
        return f"http://{self.ip}:{self.port}"

    def get_info(self):
        info = super().get_info()  # Anropa parent metod
        info["port"] = self.port
        info["type"] = "web"
        return info

class DatabaseServer(Server):
    def __init__(self, hostname, ip, engine="postgresql"):
        super().__init__(hostname, ip)
        self.engine = engine

    def get_connection_string(self):
        return f"{self.engine}://{self.ip}:5432"

    def get_info(self):
        info = super().get_info()
        info["engine"] = self.engine
        info["type"] = "database"
        return info

# Anvandning
web = WebServer("web-01", "192.168.1.1", 8080)
db = DatabaseServer("db-01", "192.168.1.10", "mysql")

print(web.get_url())  # "http://192.168.1.1:8080"
print(db.get_connection_string())  # "mysql://192.168.1.10:5432"

# Polymorfism
servers = [web, db]
for server in servers:
    print(server.get_info())
```

------------------------------------------------------------

## Properties

```python
class Container:
    def __init__(self, name, image):
        self._name = name
        self._image = image
        self._status = "created"

    @property
    def name(self):
        \"\"\"Get container name (read-only).\"\"\"
        return self._name

    @property
    def status(self):
        \"\"\"Get container status.\"\"\"
        return self._status

    @status.setter
    def status(self, value):
        \"\"\"Set container status with validation.\"\"\"
        valid_statuses = ["created", "running", "stopped", "error"]
        if value not in valid_statuses:
            raise ValueError(f"Invalid status: {value}")
        self._status = value

    @property
    def is_running(self):
        \"\"\"Check if container is running (computed property).\"\"\"
        return self._status == "running"

# Anvandning
container = Container("web", "nginx:latest")
print(container.name)    # "web" (getter)
container.status = "running"  # setter
print(container.is_running)   # True

container.status = "invalid"  # ValueError
```

------------------------------------------------------------

## Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Server:
    hostname: str
    ip: str
    port: int = 22
    tags: List[str] = field(default_factory=list)
    status: str = "unknown"

    def connect(self):
        print(f"Connecting to {self.hostname}")
        self.status = "connected"

# Skapar automatiskt __init__, __repr__, __eq__
web = Server("web-01", "192.168.1.1", 8080)
print(web)
# Server(hostname='web-01', ip='192.168.1.1', port=8080, tags=[], status='unknown')

# Jamforelse fungerar
web2 = Server("web-01", "192.168.1.1", 8080)
print(web == web2)  # True

@dataclass
class Deployment:
    name: str
    replicas: int
    image: str
    env: dict = field(default_factory=dict)

    def scale(self, replicas: int):
        self.replicas = replicas

    @property
    def resource_name(self):
        return f"deployment/{self.name}"

deploy = Deployment("api", 3, "myapp:latest")
deploy.scale(5)
```

------------------------------------------------------------

## Abstract Base Classes

```python
from abc import ABC, abstractmethod

class CloudProvider(ABC):
    \"\"\"Abstract base class for cloud providers.\"\"\"

    def __init__(self, region):
        self.region = region

    @abstractmethod
    def create_vm(self, name, size):
        \"\"\"Create a virtual machine.\"\"\"
        pass

    @abstractmethod
    def delete_vm(self, name):
        \"\"\"Delete a virtual machine.\"\"\"
        pass

    def list_vms(self):
        \"\"\"Default implementation.\"\"\"
        print(f"Listing VMs in {self.region}")

class AWSProvider(CloudProvider):
    def create_vm(self, name, size):
        print(f"Creating EC2 instance {name} ({size}) in {self.region}")
        return {"id": f"i-{name}", "type": "ec2"}

    def delete_vm(self, name):
        print(f"Terminating EC2 instance {name}")

class AzureProvider(CloudProvider):
    def create_vm(self, name, size):
        print(f"Creating Azure VM {name} ({size}) in {self.region}")
        return {"id": f"vm-{name}", "type": "azure_vm"}

    def delete_vm(self, name):
        print(f"Deleting Azure VM {name}")

# Kan inte instansiera abstrakt klass
# provider = CloudProvider("us-east-1")  # TypeError

# Men kan instansiera konkreta implementationer
aws = AWSProvider("us-east-1")
azure = AzureProvider("westeurope")

# Polymorfism
providers = [aws, azure]
for provider in providers:
    provider.create_vm("web-01", "medium")
```

------------------------------------------------------------

## Praktiskt Exempel: Resource Manager

```python
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from abc import ABC, abstractmethod

@dataclass
class Resource:
    name: str
    resource_type: str
    status: str = "pending"
    metadata: Dict = field(default_factory=dict)

class ResourceManager(ABC):
    def __init__(self):
        self.resources: Dict[str, Resource] = {}

    @abstractmethod
    def create(self, name: str, **kwargs) -> Resource:
        pass

    @abstractmethod
    def delete(self, name: str) -> bool:
        pass

    def get(self, name: str) -> Optional[Resource]:
        return self.resources.get(name)

    def list_all(self) -> List[Resource]:
        return list(self.resources.values())

class ContainerManager(ResourceManager):
    def __init__(self, docker_client):
        super().__init__()
        self.docker = docker_client

    def create(self, name: str, image: str, **kwargs) -> Resource:
        container = self.docker.containers.run(
            image,
            name=name,
            detach=True,
            **kwargs
        )
        resource = Resource(
            name=name,
            resource_type="container",
            status="running",
            metadata={"image": image, "id": container.id}
        )
        self.resources[name] = resource
        return resource

    def delete(self, name: str) -> bool:
        if name not in self.resources:
            return False

        resource = self.resources[name]
        container = self.docker.containers.get(resource.metadata["id"])
        container.stop()
        container.remove()
        del self.resources[name]
        return True
```

------------------------------------------------------------

## Snabbreferens - OOP

| Koncept | Syntax |
|---------|--------|
| Class | `class MyClass:` |
| Constructor | `def __init__(self):` |
| Instance method | `def method(self):` |
| Class method | `@classmethod` |
| Static method | `@staticmethod` |
| Property | `@property` |
| Inheritance | `class Child(Parent):` |
| Super | `super().__init__()` |
| Abstract | `from abc import ABC` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Missing self | Glom self i metod | Lagg till self |
| Mutable default | `def __init__(self, x=[]):` | Anvand None |
| Not calling super | Glom anropa parent | `super().__init__()` |
| Circular import | Classes importerar varandra | Refaktorera |
| Wrong inheritance | Fel parent | Kolla hierarki |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **dataclass** | Anvand for enkel data |
| **Properties** | For validering och computed |
| **ABC** | For interface-kontrakt |
| **Composition** | Ofta battre an inheritance |
| **super()** | Alltid anropa for init |

**Kom ihag:**
- Dataclasses for enkla data-klasser
- Properties for kontrollerad access
- Composition over inheritance
- ABC for abstrakta granssnitt
- super() i subclass __init__
"""
        },
        # =====================================================================
        # NODE 8: OS & System Interaction
        # =====================================================================
        {
            "title": "OS & System Interaction",
            "slug": "python-os-system",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 85,
            "content": """# OS & System Interaction

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor os-modulen ar viktig |
|----------|----------------------------|
| **Environment** | Lasa/satta env vars |
| **Filoperation** | Hantera filer programmatiskt |
| **Systeminfo** | Hamta hostname, CPU, disk |
| **Paths** | Plattformsoberoende sokvagar |
| **Process** | Hantera processer och PIDs |

Som DevOps-ingenjor maste du forsta:

- **os** och **sys** for systeminteraktion
- **platform** for plattformsinformation
- **shutil** for filoperationer

------------------------------------------------------------

## Environment Variables

```python
import os

# Lasa environment variables
home = os.environ.get("HOME")
api_key = os.environ.get("API_KEY", "default-key")

# Kontrollera om den finns
if "DATABASE_URL" in os.environ:
    db_url = os.environ["DATABASE_URL"]
else:
    db_url = "sqlite:///local.db"

# Satta environment variable (for child processes)
os.environ["MY_APP_ENV"] = "production"

# Alla environment variables
for key, value in os.environ.items():
    if key.startswith("AWS_"):
        print(f"{key}={value[:10]}...")

# Expandera variabler i strang
path = os.path.expandvars("$HOME/config/$USER")
```

### Praktisk Config Class

```python
import os

class Config:
    \"\"\"Configuration from environment.\"\"\"

    # Required
    DATABASE_URL = os.environ["DATABASE_URL"]
    SECRET_KEY = os.environ["SECRET_KEY"]

    # Optional med defaults
    DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    PORT = int(os.environ.get("PORT", 8000))
    WORKERS = int(os.environ.get("WORKERS", 4))

    # Computed
    @property
    def is_production(self):
        return os.environ.get("ENV") == "production"
```

------------------------------------------------------------

## Filsystem med os

```python
import os
from pathlib import Path

# Aktuell katalog
cwd = os.getcwd()
os.chdir("/tmp")

# Lista filer
files = os.listdir(".")
files = os.listdir("/etc")

# Skapa kataloger
os.mkdir("single_dir")           # En niva
os.makedirs("path/to/deep/dir", exist_ok=True)  # Rekursivt

# Ta bort
os.remove("file.txt")            # Ta bort fil
os.rmdir("empty_dir")            # Ta bort tom katalog

# Byt namn / flytta
os.rename("old.txt", "new.txt")

# Kontrollera existens
os.path.exists("/etc/hosts")     # True
os.path.isfile("/etc/hosts")     # True
os.path.isdir("/etc")            # True

# Sokvagshanter
full_path = os.path.join("/var", "log", "app.log")
dirname = os.path.dirname("/var/log/app.log")    # "/var/log"
basename = os.path.basename("/var/log/app.log")  # "app.log"
name, ext = os.path.splitext("app.log")          # ("app", ".log")

# Absolut sokvag
abs_path = os.path.abspath("./config.yaml")
```

------------------------------------------------------------

## os.walk - Traversera kataloger

```python
import os

# Traversera hela katalogtradet
for root, dirs, files in os.walk("/var/log"):
    # root = aktuell katalog
    # dirs = subkataloger
    # files = filer i denna katalog

    for filename in files:
        if filename.endswith(".log"):
            full_path = os.path.join(root, filename)
            size = os.path.getsize(full_path)
            print(f"{full_path}: {size} bytes")

# Hitta alla Python-filer
def find_python_files(directory):
    python_files = []
    for root, dirs, files in os.walk(directory):
        # Hoppa over hidden och venv
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "venv"]

        for f in files:
            if f.endswith(".py"):
                python_files.append(os.path.join(root, f))
    return python_files

# Storlek pa katalog
def get_dir_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            if os.path.exists(fp):
                total += os.path.getsize(fp)
    return total
```

------------------------------------------------------------

## shutil - Filoperationer

```python
import shutil

# Kopiera filer
shutil.copy("source.txt", "dest.txt")        # Kopiera fil
shutil.copy2("source.txt", "dest.txt")       # Behall metadata
shutil.copyfile("src.txt", "dst.txt")        # Bara innehall

# Kopiera kataloger
shutil.copytree("src_dir", "dst_dir")
shutil.copytree("src", "dst", dirs_exist_ok=True)  # Python 3.8+

# Ta bort katalog med innehall
shutil.rmtree("/tmp/mydir")
shutil.rmtree("/tmp/mydir", ignore_errors=True)

# Flytta
shutil.move("old_location", "new_location")

# Diskutrymme
total, used, free = shutil.disk_usage("/")
print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")

# Arkiv
shutil.make_archive("backup", "zip", "/var/log")     # backup.zip
shutil.make_archive("backup", "gztar", "/var/log")   # backup.tar.gz
shutil.unpack_archive("backup.zip", "extracted/")
```

------------------------------------------------------------

## sys - Interpreter Info

```python
import sys

# Python version
print(sys.version)            # "3.11.0 ..."
print(sys.version_info)       # (3, 11, 0, 'final', 0)
print(sys.version_info.major) # 3

# Sokvagar
print(sys.executable)         # "/usr/bin/python3"
print(sys.prefix)             # "/usr" eller venv path
print(sys.path)               # Lista av import-sokvagar

# Argument
print(sys.argv)               # ["script.py", "arg1", "arg2"]

# Exit
sys.exit(0)                   # Lyckad exit
sys.exit(1)                   # Felaktig exit
sys.exit("Error message")     # Print och exit med 1

# Platform
print(sys.platform)           # "linux", "darwin", "win32"

# stdin, stdout, stderr
sys.stdout.write("Hello\\n")
sys.stderr.write("Error\\n")
```

------------------------------------------------------------

## platform - Systeminformation

```python
import platform

# OS info
print(platform.system())       # "Linux", "Darwin", "Windows"
print(platform.release())      # "5.15.0-1022-aws"
print(platform.version())      # "#23-Ubuntu SMP..."
print(platform.machine())      # "x86_64", "arm64"
print(platform.node())         # hostname

# Python
print(platform.python_version())  # "3.11.0"

# Full info
print(platform.uname())
# uname_result(system='Linux', node='server01', ...)

# Praktisk anvandning
if platform.system() == "Linux":
    config_path = "/etc/myapp"
elif platform.system() == "Darwin":
    config_path = "/usr/local/etc/myapp"
else:
    config_path = "C:\\\\ProgramData\\\\myapp"
```

------------------------------------------------------------

## Praktiskt Exempel: System Info Script

```python
import os
import sys
import platform
import shutil

def get_system_info():
    \"\"\"Gather comprehensive system information.\"\"\"

    info = {
        "hostname": platform.node(),
        "os": platform.system(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "python_executable": sys.executable,
    }

    # Disk usage
    try:
        total, used, free = shutil.disk_usage("/")
        info["disk"] = {
            "total_gb": round(total / (2**30), 2),
            "used_gb": round(used / (2**30), 2),
            "free_gb": round(free / (2**30), 2),
            "used_percent": round(used / total * 100, 1)
        }
    except Exception as e:
        info["disk"] = {"error": str(e)}

    # Environment
    info["environment"] = {
        "user": os.environ.get("USER", "unknown"),
        "home": os.environ.get("HOME", "unknown"),
        "shell": os.environ.get("SHELL", "unknown"),
        "path_entries": len(os.environ.get("PATH", "").split(":")),
    }

    return info

if __name__ == "__main__":
    import json
    info = get_system_info()
    print(json.dumps(info, indent=2))
```

------------------------------------------------------------

## Snabbreferens - OS & System

| Uppgift | Modul / Funktion |
|---------|------------------|
| Env vars | `os.environ` |
| Lista filer | `os.listdir()` |
| Skapa katalog | `os.makedirs()` |
| Sokvagar | `os.path.join()` |
| Traversera | `os.walk()` |
| Kopiera | `shutil.copy()` |
| Ta bort dir | `shutil.rmtree()` |
| Diskutrymme | `shutil.disk_usage()` |
| Python version | `sys.version_info` |
| Plattform | `platform.system()` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| FileNotFoundError | Fil/katalog saknas | Kolla med exists() |
| PermissionError | Ingen behorighet | sudo eller chown |
| OSError | Diverse OS-fel | Try/except |
| KeyError environ | Env var saknas | Anvand .get() |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **os.environ** | Alltid .get() med default |
| **pathlib** | Modernt alternativ till os.path |
| **shutil** | For kopiera, flytta, ta bort |
| **platform** | For plattformsspecifik logik |
| **sys.exit** | Exit med ratt kod |

**Kom ihag:**
- Anvand os.environ.get() med defaults
- os.makedirs() med exist_ok=True
- shutil for bulk-operationer
- Kolla platform.system() for OS-specifik kod
- sys.exit(0) for success, sys.exit(1) for failure
"""
        },
        # =====================================================================
        # NODE 9: Subprocess & Shell Commands
        # =====================================================================
        {
            "title": "Subprocess & Shell Commands",
            "slug": "python-subprocess",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Subprocess & Shell Commands

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor subprocess ar viktigt |
|----------|------------------------------|
| **Automation** | Kor shell-kommandon fran Python |
| **System admin** | Hantera servrar programmatiskt |
| **CI/CD** | Exekvera build-steg |
| **Migration** | Wrapper for legacy scripts |
| **Integration** | Anropa externa verktyg |

Som DevOps-ingenjor maste du forsta:

- **subprocess.run()** for att kora kommandon
- **Output capture** for att fanga resultat
- **Error handling** for att hantera misslyckanden

------------------------------------------------------------

## subprocess.run() - Grundlaggande

```python
import subprocess

# Enklaste formen
result = subprocess.run(["ls", "-la"])
print(f"Return code: {result.returncode}")

# Med output capture
result = subprocess.run(
    ["ls", "-la"],
    capture_output=True,  # Fanga stdout och stderr
    text=True             # Returnera str istallet for bytes
)

print(result.stdout)      # Standard output
print(result.stderr)      # Standard error
print(result.returncode)  # Exit code (0 = success)

# Kolla om kommandot lyckades
if result.returncode == 0:
    print("Success!")
else:
    print(f"Failed: {result.stderr}")
```

### check=True for automatisk felhantering

```python
import subprocess

try:
    # check=True kastar exception om returncode != 0
    result = subprocess.run(
        ["git", "status"],
        capture_output=True,
        text=True,
        check=True
    )
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Command failed with code {e.returncode}")
    print(f"Error: {e.stderr}")
```

------------------------------------------------------------

## Shell Commands

```python
import subprocess

# Med shell=True (VAR FORSIKTIG!)
result = subprocess.run(
    "echo $HOME && ls | head -5",
    shell=True,
    capture_output=True,
    text=True
)

# Shell pipes och redirects
result = subprocess.run(
    "cat /etc/passwd | grep root | wc -l",
    shell=True,
    capture_output=True,
    text=True
)
print(result.stdout.strip())

# VARNING: Undvik shell=True med user input!
# Detta ar OSAKER:
# user_input = "; rm -rf /"
# subprocess.run(f"echo {user_input}", shell=True)  # FARLIGT!

# Saker variant utan shell:
subprocess.run(["echo", user_input])  # SAKERT
```

------------------------------------------------------------

## Pipes mellan processer

```python
import subprocess

# Pipe mellan tva processer
# ps aux | grep python
ps = subprocess.Popen(
    ["ps", "aux"],
    stdout=subprocess.PIPE
)

grep = subprocess.Popen(
    ["grep", "python"],
    stdin=ps.stdout,
    stdout=subprocess.PIPE,
    text=True
)

ps.stdout.close()  # Allow ps to receive SIGPIPE
output, _ = grep.communicate()
print(output)

# Enklare: Anvand shell (men mindre sakert)
result = subprocess.run(
    "ps aux | grep python | grep -v grep",
    shell=True,
    capture_output=True,
    text=True
)
print(result.stdout)
```

------------------------------------------------------------

## Timeout och Environment

```python
import subprocess
import os

# Med timeout
try:
    result = subprocess.run(
        ["sleep", "10"],
        timeout=5  # Timeout efter 5 sekunder
    )
except subprocess.TimeoutExpired:
    print("Command timed out!")

# Med custom environment
my_env = os.environ.copy()
my_env["API_KEY"] = "secret123"
my_env["DEBUG"] = "true"

result = subprocess.run(
    ["python", "script.py"],
    env=my_env,
    capture_output=True,
    text=True
)

# Med working directory
result = subprocess.run(
    ["npm", "install"],
    cwd="/path/to/project",
    capture_output=True,
    text=True
)
```

------------------------------------------------------------

## Input till processer

```python
import subprocess

# Skicka input till process
result = subprocess.run(
    ["python", "-c", "name = input('Name: '); print(f'Hello {name}')"],
    input="DevOps\\n",
    capture_output=True,
    text=True
)
print(result.stdout)  # "Name: Hello DevOps"

# Interaktiv process med Popen
process = subprocess.Popen(
    ["cat"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate(input="Hello World\\n")
print(stdout)  # "Hello World"
```

------------------------------------------------------------

## Praktiskt Exempel: DevOps Utilities

```python
import subprocess
from typing import Tuple, Optional

def run_command(
    cmd: list,
    cwd: Optional[str] = None,
    timeout: int = 60,
    check: bool = True
) -> Tuple[str, str, int]:
    \"\"\"Run a command and return (stdout, stderr, returncode).\"\"\"
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            timeout=timeout,
            capture_output=True,
            text=True,
            check=check
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired as e:
        return "", f"Timeout after {timeout}s", -1
    except subprocess.CalledProcessError as e:
        return e.stdout or "", e.stderr or "", e.returncode

def get_git_info(repo_path: str) -> dict:
    \"\"\"Get git repository information.\"\"\"
    info = {}

    # Current branch
    stdout, _, _ = run_command(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=repo_path
    )
    info["branch"] = stdout.strip()

    # Latest commit
    stdout, _, _ = run_command(
        ["git", "log", "-1", "--format=%H %s"],
        cwd=repo_path
    )
    parts = stdout.strip().split(" ", 1)
    info["commit_hash"] = parts[0][:8]
    info["commit_msg"] = parts[1] if len(parts) > 1 else ""

    # Status
    stdout, _, _ = run_command(
        ["git", "status", "--porcelain"],
        cwd=repo_path
    )
    info["changed_files"] = len(stdout.strip().split("\\n")) if stdout.strip() else 0

    return info

def docker_command(action: str, container: str) -> bool:
    \"\"\"Run docker command (start/stop/restart).\"\"\"
    valid_actions = ["start", "stop", "restart"]
    if action not in valid_actions:
        raise ValueError(f"Invalid action: {action}")

    stdout, stderr, code = run_command(
        ["docker", action, container],
        check=False
    )

    if code == 0:
        print(f"Successfully {action}ed {container}")
        return True
    else:
        print(f"Failed to {action} {container}: {stderr}")
        return False

# Anvandning
if __name__ == "__main__":
    info = get_git_info(".")
    print(f"Branch: {info['branch']}")
    print(f"Commit: {info['commit_hash']} - {info['commit_msg']}")
```

------------------------------------------------------------

## Snabbreferens - subprocess

| Uppgift | Kod |
|---------|-----|
| Enkel korning | `subprocess.run(["cmd", "arg"])` |
| Fanga output | `capture_output=True, text=True` |
| Kolla fel | `check=True` |
| Timeout | `timeout=30` |
| Working dir | `cwd="/path"` |
| Environment | `env=my_env` |
| Input | `input="data"` |
| Shell | `shell=True` (undvik om mojligt) |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| FileNotFoundError | Kommando finns ej | Kolla PATH |
| CalledProcessError | Kommando failed | check=False eller try/except |
| TimeoutExpired | For langsamt | Oka timeout |
| Shell injection | User input i shell | Undvik shell=True |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **subprocess.run()** | Anvand alltid denna |
| **Lista format** | `["cmd", "arg"]` ar sakrare an shell |
| **capture_output** | For att fanga resultat |
| **check=True** | Kasta exception vid fel |
| **Undvik shell=True** | Sakerhetsproblem |

**Kom ihag:**
- Foredra subprocess.run() over os.system()
- Anvand listor `["cmd", "arg"]` inte strangar
- capture_output=True, text=True for output
- check=True kastar exception vid fel
- Undvik shell=True med user input
"""
        },
        # =====================================================================
        # NODE 10: JSON & YAML Handling
        # =====================================================================
        {
            "title": "JSON & YAML Handling",
            "slug": "python-json-yaml",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# JSON & YAML Handling

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor JSON/YAML ar viktigt |
|----------|----------------------------|
| **Config** | Kubernetes, Docker Compose, Ansible |
| **API** | Request/response format |
| **State** | Terraform state files |
| **CI/CD** | Pipeline definitions |
| **IaC** | CloudFormation, ARM templates |

Som DevOps-ingenjor maste du forsta:

- **JSON** for API-kommunikation
- **YAML** for konfigurationsfiler
- **Konvertering** mellan formaten

------------------------------------------------------------

## JSON - Grundlaggande

```python
import json

# Python dict till JSON string
data = {
    "name": "web-server",
    "port": 8080,
    "enabled": True,
    "tags": ["production", "frontend"]
}

json_string = json.dumps(data)
print(json_string)
# {"name": "web-server", "port": 8080, "enabled": true, "tags": ["production", "frontend"]}

# Med formattering
json_pretty = json.dumps(data, indent=2)
print(json_pretty)

# JSON string till Python dict
json_input = '{"name": "api", "port": 3000}'
config = json.loads(json_input)
print(config["name"])  # "api"
```

### Filer

```python
import json
from pathlib import Path

# Skriv till fil
config = {"database": "postgres", "host": "localhost"}

with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

# Las fran fil
with open("config.json", "r") as f:
    config = json.load(f)

# Med pathlib
config_path = Path("config.json")
config = json.loads(config_path.read_text())
config_path.write_text(json.dumps(config, indent=2))
```

------------------------------------------------------------

## JSON - Avancerat

```python
import json
from datetime import datetime
from dataclasses import dataclass, asdict

# Custom encoder for datetime
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {"event": "deploy", "timestamp": datetime.now()}
json_string = json.dumps(data, cls=DateTimeEncoder)
print(json_string)

# Custom decoder
def datetime_decoder(dct):
    for key, value in dct.items():
        if isinstance(value, str):
            try:
                dct[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return dct

parsed = json.loads(json_string, object_hook=datetime_decoder)

# Dataclass serialization
@dataclass
class Server:
    name: str
    ip: str
    port: int = 22

server = Server("web-01", "192.168.1.1", 8080)
json_data = json.dumps(asdict(server), indent=2)
```

------------------------------------------------------------

## YAML - Grundlaggande

```python
import yaml  # pip install pyyaml

# YAML string till Python
yaml_string = '''
name: web-server
port: 8080
enabled: true
tags:
  - production
  - frontend
database:
  host: localhost
  port: 5432
'''

data = yaml.safe_load(yaml_string)
print(data["database"]["host"])  # "localhost"

# Python till YAML string
config = {
    "apiVersion": "v1",
    "kind": "Service",
    "metadata": {"name": "my-service"}
}

yaml_output = yaml.dump(config, default_flow_style=False)
print(yaml_output)
```

### YAML Filer

```python
import yaml
from pathlib import Path

# Las YAML fil
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Skriv YAML fil
with open("config.yaml", "w") as f:
    yaml.dump(config, f, default_flow_style=False)

# Las flera dokument fran samma fil
yaml_multi = '''
---
name: server1
---
name: server2
'''

for doc in yaml.safe_load_all(yaml_multi):
    print(doc["name"])

# Med pathlib
config_path = Path("k8s/deployment.yaml")
deployment = yaml.safe_load(config_path.read_text())
```

------------------------------------------------------------

## YAML - Avancerat

```python
import yaml

# Preserve order (Python 3.7+ dicts ar ordnade)
config = yaml.safe_load('''
first: 1
second: 2
third: 3
''')

# Custom representer
def str_representer(dumper, data):
    if '\\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_representer)

# Multiline strings
data = {
    "script": '''#!/bin/bash
echo "Hello"
echo "World"
'''
}
print(yaml.dump(data))
# script: |
#   #!/bin/bash
#   echo "Hello"
#   echo "World"

# Anchors och aliases
yaml_anchors = '''
defaults: &defaults
  adapter: postgres
  host: localhost

development:
  <<: *defaults
  database: dev_db

production:
  <<: *defaults
  database: prod_db
'''

config = yaml.safe_load(yaml_anchors)
print(config["production"]["host"])  # "localhost"
```

------------------------------------------------------------

## Praktiskt Exempel: Config Manager

```python
import json
import yaml
from pathlib import Path
from typing import Any, Dict

class ConfigManager:
    \"\"\"Manage JSON and YAML configuration files.\"\"\"

    def __init__(self, config_dir: str = "."):
        self.config_dir = Path(config_dir)

    def load(self, filename: str) -> Dict[str, Any]:
        \"\"\"Load config file (auto-detect format).\"\"\"
        path = self.config_dir / filename
        content = path.read_text()

        if filename.endswith(".json"):
            return json.loads(content)
        elif filename.endswith((".yaml", ".yml")):
            return yaml.safe_load(content)
        else:
            raise ValueError(f"Unknown format: {filename}")

    def save(self, filename: str, data: Dict[str, Any]) -> None:
        \"\"\"Save config file (auto-detect format).\"\"\"
        path = self.config_dir / filename

        if filename.endswith(".json"):
            content = json.dumps(data, indent=2)
        elif filename.endswith((".yaml", ".yml")):
            content = yaml.dump(data, default_flow_style=False)
        else:
            raise ValueError(f"Unknown format: {filename}")

        path.write_text(content)

    def convert(self, source: str, target: str) -> None:
        \"\"\"Convert between JSON and YAML.\"\"\"
        data = self.load(source)
        self.save(target, data)

# Anvandning
manager = ConfigManager("./configs")

# Las olika format
app_config = manager.load("app.yaml")
db_config = manager.load("database.json")

# Konvertera
manager.convert("kubernetes.yaml", "kubernetes.json")
```

------------------------------------------------------------

## Snabbreferens - JSON & YAML

| Uppgift | JSON | YAML |
|---------|------|------|
| String -> Dict | `json.loads(s)` | `yaml.safe_load(s)` |
| Dict -> String | `json.dumps(d)` | `yaml.dump(d)` |
| Las fil | `json.load(f)` | `yaml.safe_load(f)` |
| Skriv fil | `json.dump(d, f)` | `yaml.dump(d, f)` |
| Pretty print | `indent=2` | `default_flow_style=False` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| JSONDecodeError | Ogiltig JSON | Validera med jsonlint |
| YAMLError | Ogiltig YAML | Kolla indentation |
| UnicodeDecodeError | Fel encoding | encoding="utf-8" |
| KeyError | Nyckel saknas | Anvand .get() |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **json** | Inbyggd modul |
| **yaml** | Kraver pip install pyyaml |
| **safe_load** | Anvand ALLTID istallet for load |
| **indent** | For lasbar output |
| **dumps/loads** | String, dump/load = fil |

**Kom ihag:**
- JSON for API, YAML for config
- Anvand yaml.safe_load() (sakerhet)
- json.dumps(indent=2) for lasbar JSON
- Hantera encoding: open(f, encoding="utf-8")
- Validera innan parsing
"""
        },
        # =====================================================================
        # NODE 11: HTTP & REST APIs
        # =====================================================================
        {
            "title": "HTTP & REST APIs",
            "slug": "python-http-apis",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# HTTP & REST APIs

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor HTTP ar viktigt |
|----------|------------------------|
| **Cloud APIs** | AWS, Azure, GCP |
| **Monitoring** | Prometheus, Datadog |
| **Webhooks** | GitHub, Slack |
| **Automation** | REST endpoints |
| **Health checks** | Service status |

Som DevOps-ingenjor maste du forsta:

- **requests** for HTTP-anrop
- **REST** metoder (GET, POST, PUT, DELETE)
- **Authentication** och headers

------------------------------------------------------------

## requests - Grundlaggande

```python
import requests  # pip install requests

# GET request
response = requests.get("https://api.github.com/users/torvalds")

print(response.status_code)   # 200
print(response.headers)       # Response headers
print(response.text)          # Raw text
print(response.json())        # Parse JSON response

# Kolla om request lyckades
if response.ok:  # status_code < 400
    data = response.json()
    print(f"Name: {data['name']}")
else:
    print(f"Error: {response.status_code}")

# Query parameters
params = {"q": "python", "sort": "stars"}
response = requests.get("https://api.github.com/search/repositories", params=params)
```

### POST Request

```python
import requests

# POST med JSON data
data = {
    "name": "web-server",
    "image": "nginx:latest",
    "port": 80
}

response = requests.post(
    "https://api.example.com/containers",
    json=data  # Automatiskt Content-Type: application/json
)

# POST med form data
response = requests.post(
    "https://api.example.com/login",
    data={"username": "admin", "password": "secret"}
)

# PUT (update)
response = requests.put(
    "https://api.example.com/containers/123",
    json={"port": 8080}
)

# DELETE
response = requests.delete("https://api.example.com/containers/123")
```

------------------------------------------------------------

## Headers och Authentication

```python
import requests
import os

# Custom headers
headers = {
    "Authorization": f"Bearer {os.environ['API_TOKEN']}",
    "Content-Type": "application/json",
    "User-Agent": "DevOps-Script/1.0"
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers
)

# Basic Auth
response = requests.get(
    "https://api.example.com/secure",
    auth=("username", "password")
)

# Bearer Token (GitHub style)
token = os.environ.get("GITHUB_TOKEN")
headers = {"Authorization": f"token {token}"}
response = requests.get(
    "https://api.github.com/user/repos",
    headers=headers
)

# API Key
response = requests.get(
    "https://api.example.com/data",
    headers={"X-API-Key": os.environ["API_KEY"]}
)
```

------------------------------------------------------------

## Timeout och Error Handling

```python
import requests
from requests.exceptions import (
    RequestException,
    Timeout,
    ConnectionError,
    HTTPError
)

def safe_request(url, method="GET", **kwargs):
    \"\"\"Make HTTP request with error handling.\"\"\"
    try:
        response = requests.request(
            method,
            url,
            timeout=30,  # Alltid satt timeout!
            **kwargs
        )
        response.raise_for_status()  # Kasta exception for 4xx/5xx
        return response

    except Timeout:
        print(f"Request to {url} timed out")
        return None
    except ConnectionError:
        print(f"Could not connect to {url}")
        return None
    except HTTPError as e:
        print(f"HTTP error: {e.response.status_code}")
        return None
    except RequestException as e:
        print(f"Request failed: {e}")
        return None

# Anvandning
response = safe_request("https://api.example.com/health")
if response:
    print(response.json())
```

------------------------------------------------------------

## Sessions och Connection Pooling

```python
import requests

# Session for att ateranvanda connections
session = requests.Session()

# Satt default headers for alla requests
session.headers.update({
    "Authorization": "Bearer token123",
    "User-Agent": "DevOps-Script/1.0"
})

# Alla requests anvander samma session
response1 = session.get("https://api.example.com/users")
response2 = session.get("https://api.example.com/repos")
response3 = session.post("https://api.example.com/deploy", json={"env": "prod"})

# Session med context manager
with requests.Session() as s:
    s.auth = ("user", "pass")
    response = s.get("https://api.example.com/data")

# Retries med urllib3
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504]
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)
```

------------------------------------------------------------

## Praktiskt Exempel: API Client

```python
import requests
import os
from typing import Dict, List, Optional

class GitHubClient:
    \"\"\"GitHub API client for DevOps automation.\"\"\"

    BASE_URL = "https://api.github.com"

    def __init__(self, token: Optional[str] = None):
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "DevOps-Automation"
        })

        if token:
            self.session.headers["Authorization"] = f"token {token}"

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
        \"\"\"Make API request with error handling.\"\"\"
        url = f"{self.BASE_URL}{endpoint}"

        response = self.session.request(method, url, timeout=30, **kwargs)
        response.raise_for_status()

        return response.json() if response.text else {}

    def get_repo(self, owner: str, repo: str) -> Dict:
        \"\"\"Get repository information.\"\"\"
        return self._request("GET", f"/repos/{owner}/{repo}")

    def list_branches(self, owner: str, repo: str) -> List[Dict]:
        \"\"\"List repository branches.\"\"\"
        return self._request("GET", f"/repos/{owner}/{repo}/branches")

    def create_issue(self, owner: str, repo: str, title: str, body: str) -> Dict:
        \"\"\"Create a new issue.\"\"\"
        return self._request(
            "POST",
            f"/repos/{owner}/{repo}/issues",
            json={"title": title, "body": body}
        )

    def trigger_workflow(self, owner: str, repo: str, workflow: str, ref: str = "main") -> bool:
        \"\"\"Trigger a GitHub Actions workflow.\"\"\"
        try:
            self._request(
                "POST",
                f"/repos/{owner}/{repo}/actions/workflows/{workflow}/dispatches",
                json={"ref": ref}
            )
            return True
        except requests.HTTPError:
            return False

# Anvandning
if __name__ == "__main__":
    client = GitHubClient(os.environ.get("GITHUB_TOKEN"))

    # Hamta repo info
    repo = client.get_repo("python", "cpython")
    print(f"Stars: {repo['stargazers_count']}")

    # Lista branches
    branches = client.list_branches("python", "cpython")
    for branch in branches[:5]:
        print(f"- {branch['name']}")
```

------------------------------------------------------------

## Health Check Script

```python
import requests
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List

def check_endpoint(url: str, timeout: int = 5) -> Dict:
    \"\"\"Check if endpoint is healthy.\"\"\"
    try:
        response = requests.get(url, timeout=timeout)
        return {
            "url": url,
            "status": "healthy" if response.ok else "unhealthy",
            "code": response.status_code,
            "latency_ms": response.elapsed.total_seconds() * 1000
        }
    except requests.RequestException as e:
        return {
            "url": url,
            "status": "unreachable",
            "error": str(e)
        }

def health_check(endpoints: List[str]) -> List[Dict]:
    \"\"\"Check multiple endpoints in parallel.\"\"\"
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(check_endpoint, endpoints))
    return results

# Anvandning
endpoints = [
    "https://api.example.com/health",
    "https://db.example.com/health",
    "https://cache.example.com/health"
]

results = health_check(endpoints)
for r in results:
    print(f"{r['url']}: {r['status']}")
```

------------------------------------------------------------

## Snabbreferens - HTTP & REST

| Uppgift | Kod |
|---------|-----|
| GET | `requests.get(url)` |
| POST JSON | `requests.post(url, json=data)` |
| Headers | `headers={"Auth": "token"}` |
| Timeout | `timeout=30` |
| Status check | `response.ok` |
| Parse JSON | `response.json()` |
| Error check | `response.raise_for_status()` |
| Session | `requests.Session()` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Timeout | For lang responstid | Oka timeout |
| 401 Unauthorized | Fel credentials | Kontrollera token |
| 403 Forbidden | Saknar behorighet | Kolla permissions |
| 429 Too Many | Rate limiting | Implementera backoff |
| ConnectionError | Natverk/DNS | Kolla URL |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **timeout** | ALLTID satt timeout |
| **Session** | Ateranvand connections |
| **raise_for_status()** | Kasta exception for errors |
| **json=** | Auto Content-Type |
| **Retries** | Implementera for resilience |

**Kom ihag:**
- Alltid satt timeout (default ar ingen!)
- Anvand Session for flera requests
- raise_for_status() for error handling
- json= istallet for manuell serialisering
- Lagra aldrig tokens i kod
"""
        },
        # =====================================================================
        # NODE 12: AWS SDK (Boto3)
        # =====================================================================
        {
            "title": "AWS SDK (Boto3)",
            "slug": "python-boto3",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 100,
            "content": """# AWS SDK (Boto3)

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Boto3 ar viktigt |
|----------|------------------------|
| **IaC** | Programmera AWS-resurser |
| **Automation** | Skript for EC2, S3, Lambda |
| **Cost** | Stang av oanvanda resurser |
| **Backup** | Automatisera snapshots |
| **Monitoring** | CloudWatch integration |

Som DevOps-ingenjor maste du forsta:

- **Clients** for low-level API
- **Resources** for high-level OOP
- **Sessions** for credentials

------------------------------------------------------------

## Setup och Credentials

```python
import boto3

# Boto3 soker credentials i denna ordning:
# 1. Explicit i kod (UNDVIK!)
# 2. Environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
# 3. ~/.aws/credentials
# 4. IAM role (pa EC2/Lambda)

# Default session (anvander credentials fran env/file/role)
s3 = boto3.client("s3")
ec2 = boto3.resource("ec2")

# Med explicit region
s3 = boto3.client("s3", region_name="eu-west-1")

# Med profil fran ~/.aws/credentials
session = boto3.Session(profile_name="production")
s3 = session.client("s3")

# Environment variables (rekommenderat for CI/CD)
# export AWS_ACCESS_KEY_ID="..."
# export AWS_SECRET_ACCESS_KEY="..."
# export AWS_DEFAULT_REGION="eu-west-1"
```

------------------------------------------------------------

## S3 - Simple Storage Service

```python
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3")

# Lista buckets
response = s3.list_buckets()
for bucket in response["Buckets"]:
    print(bucket["Name"])

# Upload fil
s3.upload_file("local_file.txt", "my-bucket", "remote/path/file.txt")

# Download fil
s3.download_file("my-bucket", "remote/path/file.txt", "local_file.txt")

# Upload med content
s3.put_object(
    Bucket="my-bucket",
    Key="config/app.json",
    Body='{"version": "1.0"}',
    ContentType="application/json"
)

# Las innehall
response = s3.get_object(Bucket="my-bucket", Key="config/app.json")
content = response["Body"].read().decode("utf-8")

# Lista objekt
response = s3.list_objects_v2(Bucket="my-bucket", Prefix="logs/")
for obj in response.get("Contents", []):
    print(f"{obj['Key']}: {obj['Size']} bytes")

# Radera
s3.delete_object(Bucket="my-bucket", Key="old_file.txt")
```

### S3 Resource (high-level)

```python
import boto3

s3 = boto3.resource("s3")

# Bucket objekt
bucket = s3.Bucket("my-bucket")

# Lista alla objekt
for obj in bucket.objects.all():
    print(obj.key)

# Filtrera pa prefix
for obj in bucket.objects.filter(Prefix="logs/2024/"):
    print(obj.key)

# Upload
bucket.upload_file("local.txt", "remote.txt")

# Download
bucket.download_file("remote.txt", "local.txt")
```

------------------------------------------------------------

## EC2 - Elastic Compute Cloud

```python
import boto3

ec2_client = boto3.client("ec2")
ec2_resource = boto3.resource("ec2")

# Lista instanser
response = ec2_client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(f"{instance['InstanceId']}: {instance['State']['Name']}")

# Med Resource
for instance in ec2_resource.instances.all():
    print(f"{instance.id}: {instance.state['Name']}")

# Filtrera pa tags
instances = ec2_resource.instances.filter(
    Filters=[
        {"Name": "tag:Environment", "Values": ["production"]},
        {"Name": "instance-state-name", "Values": ["running"]}
    ]
)

# Starta/stoppa instanser
ec2_client.start_instances(InstanceIds=["i-1234567890abcdef0"])
ec2_client.stop_instances(InstanceIds=["i-1234567890abcdef0"])

# Skapa instans
instances = ec2_resource.create_instances(
    ImageId="ami-0123456789abcdef0",
    MinCount=1,
    MaxCount=1,
    InstanceType="t3.micro",
    KeyName="my-key",
    TagSpecifications=[{
        "ResourceType": "instance",
        "Tags": [
            {"Key": "Name", "Value": "web-server"},
            {"Key": "Environment", "Value": "production"}
        ]
    }]
)
print(f"Created: {instances[0].id}")
```

------------------------------------------------------------

## Lambda och CloudWatch

```python
import boto3
import json

# Lambda
lambda_client = boto3.client("lambda")

# Invoke Lambda function
response = lambda_client.invoke(
    FunctionName="my-function",
    InvocationType="RequestResponse",
    Payload=json.dumps({"key": "value"})
)

result = json.loads(response["Payload"].read())
print(result)

# CloudWatch Logs
logs = boto3.client("logs")

# Lista log groups
response = logs.describe_log_groups(logGroupNamePrefix="/aws/lambda/")
for group in response["logGroups"]:
    print(group["logGroupName"])

# Hamta logs
response = logs.get_log_events(
    logGroupName="/aws/lambda/my-function",
    logStreamName="2024/01/15/[$LATEST]abc123",
    limit=100
)

for event in response["events"]:
    print(event["message"])

# CloudWatch Metrics
cloudwatch = boto3.client("cloudwatch")

cloudwatch.put_metric_data(
    Namespace="MyApp",
    MetricData=[{
        "MetricName": "DeployCount",
        "Value": 1,
        "Unit": "Count"
    }]
)
```

------------------------------------------------------------

## Praktiskt Exempel: EC2 Manager

```python
import boto3
from typing import List, Dict, Optional
from botocore.exceptions import ClientError

class EC2Manager:
    \"\"\"Manage EC2 instances for DevOps automation.\"\"\"

    def __init__(self, region: str = "eu-west-1"):
        self.ec2 = boto3.resource("ec2", region_name=region)
        self.client = boto3.client("ec2", region_name=region)

    def get_instances_by_tag(self, tag_name: str, tag_value: str) -> List:
        \"\"\"Get instances by tag.\"\"\"
        return list(self.ec2.instances.filter(
            Filters=[
                {"Name": f"tag:{tag_name}", "Values": [tag_value]},
                {"Name": "instance-state-name", "Values": ["running", "stopped"]}
            ]
        ))

    def stop_by_environment(self, env: str) -> int:
        \"\"\"Stop all instances in an environment.\"\"\"
        instances = self.get_instances_by_tag("Environment", env)
        running = [i for i in instances if i.state["Name"] == "running"]

        if running:
            ids = [i.id for i in running]
            self.client.stop_instances(InstanceIds=ids)
            print(f"Stopping {len(ids)} instances")
            return len(ids)
        return 0

    def start_by_environment(self, env: str) -> int:
        \"\"\"Start all instances in an environment.\"\"\"
        instances = self.get_instances_by_tag("Environment", env)
        stopped = [i for i in instances if i.state["Name"] == "stopped"]

        if stopped:
            ids = [i.id for i in stopped]
            self.client.start_instances(InstanceIds=ids)
            print(f"Starting {len(ids)} instances")
            return len(ids)
        return 0

    def list_instances(self, environment: Optional[str] = None) -> List[Dict]:
        \"\"\"List all instances with details.\"\"\"
        filters = []
        if environment:
            filters.append({"Name": "tag:Environment", "Values": [environment]})

        instances = self.ec2.instances.filter(Filters=filters)

        result = []
        for i in instances:
            name = ""
            env = ""
            for tag in (i.tags or []):
                if tag["Key"] == "Name":
                    name = tag["Value"]
                if tag["Key"] == "Environment":
                    env = tag["Value"]

            result.append({
                "id": i.id,
                "name": name,
                "environment": env,
                "type": i.instance_type,
                "state": i.state["Name"],
                "ip": i.public_ip_address
            })

        return result

# Anvandning
if __name__ == "__main__":
    manager = EC2Manager()

    # Lista alla prod-instanser
    for instance in manager.list_instances("production"):
        print(f"{instance['name']}: {instance['state']}")

    # Stang ner dev-miljon (t.ex. pa natten)
    manager.stop_by_environment("development")
```

------------------------------------------------------------

## Snabbreferens - Boto3

| Service | Client | Resource |
|---------|--------|----------|
| S3 | `boto3.client("s3")` | `boto3.resource("s3")` |
| EC2 | `boto3.client("ec2")` | `boto3.resource("ec2")` |
| Lambda | `boto3.client("lambda")` | - |
| CloudWatch | `boto3.client("cloudwatch")` | - |
| IAM | `boto3.client("iam")` | `boto3.resource("iam")` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| NoCredentialsError | Inga credentials | Konfigurera AWS CLI |
| AccessDenied | Saknar behorighet | Kolla IAM policy |
| InvalidParameterValue | Fel region/ami | Verifiera resurser |
| ClientError | API fel | Kolla exception.response |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Client** | Low-level, alla operationer |
| **Resource** | High-level, OOP-stil |
| **Session** | For multipla profiler |
| **Paginering** | Anvand paginators |
| **Credentials** | Aldrig i kod! |

**Kom ihag:**
- Anvand IAM roles pa EC2/Lambda
- Resource for enklare kod
- Client for full kontroll
- Hantera ClientError
- Paginera stora resultat
"""
        },
        # =====================================================================
        # NODE 13: Azure SDK
        # =====================================================================
        {
            "title": "Azure SDK",
            "slug": "python-azure-sdk",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Azure SDK

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Azure SDK ar viktigt |
|----------|----------------------------|
| **IaC** | Programmera Azure-resurser |
| **Automation** | Skript for VMs, Storage, AKS |
| **Integration** | DevOps pipelines |
| **Management** | Resource management |
| **Monitoring** | Azure Monitor |

Som DevOps-ingenjor maste du forsta:

- **azure-identity** for autentisering
- **Management clients** for resurser
- **DefaultAzureCredential** for enkel auth

------------------------------------------------------------

## Installation och Setup

```bash
# Installera core-paket
pip install azure-identity azure-mgmt-resource azure-mgmt-compute azure-mgmt-storage

# Alla Azure SDK-paket foljer detta monster:
# azure-mgmt-<service>  (management/control plane)
# azure-<service>       (data plane)
```

```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# DefaultAzureCredential provar flera autentiseringsmetoder:
# 1. Environment variables (AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID)
# 2. Managed Identity (pa Azure VMs/Functions)
# 3. Azure CLI (az login)
# 4. Visual Studio Code
# 5. Azure PowerShell

credential = DefaultAzureCredential()

# Hamta subscription ID
subscription_id = "your-subscription-id"
# Eller fran environment:
# subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
```

------------------------------------------------------------

## Resource Management

```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import os

credential = DefaultAzureCredential()
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

resource_client = ResourceManagementClient(credential, subscription_id)

# Lista resource groups
for rg in resource_client.resource_groups.list():
    print(f"{rg.name} ({rg.location})")

# Skapa resource group
rg_result = resource_client.resource_groups.create_or_update(
    "my-devops-rg",
    {"location": "westeurope", "tags": {"environment": "dev"}}
)
print(f"Created: {rg_result.name}")

# Lista resurser i en resource group
for resource in resource_client.resources.list_by_resource_group("my-devops-rg"):
    print(f"  {resource.type}: {resource.name}")

# Radera resource group
delete_async = resource_client.resource_groups.begin_delete("my-devops-rg")
delete_async.wait()  # Vanta pa completion
```

------------------------------------------------------------

## Virtual Machines

```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
import os

credential = DefaultAzureCredential()
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

compute_client = ComputeManagementClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)

# Lista VMs
for vm in compute_client.virtual_machines.list_all():
    print(f"{vm.name}: {vm.location}")

# Lista VMs i en resource group
for vm in compute_client.virtual_machines.list("my-rg"):
    # Hamta power state (krava separat call)
    instance_view = compute_client.virtual_machines.instance_view("my-rg", vm.name)
    power_state = "unknown"
    for status in instance_view.statuses:
        if status.code.startswith("PowerState/"):
            power_state = status.code.split("/")[1]
    print(f"{vm.name}: {power_state}")

# Starta VM
async_start = compute_client.virtual_machines.begin_start("my-rg", "my-vm")
async_start.wait()

# Stoppa VM
async_stop = compute_client.virtual_machines.begin_deallocate("my-rg", "my-vm")
async_stop.wait()

# Restart VM
async_restart = compute_client.virtual_machines.begin_restart("my-rg", "my-vm")
async_restart.wait()
```

------------------------------------------------------------

## Blob Storage

```python
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient
import os

# Med connection string (fran portal)
connection_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
blob_service = BlobServiceClient.from_connection_string(connection_string)

# Med DefaultAzureCredential
account_url = "https://mystorageaccount.blob.core.windows.net"
blob_service = BlobServiceClient(account_url, credential=DefaultAzureCredential())

# Lista containers
for container in blob_service.list_containers():
    print(container["name"])

# Skapa container
container_client = blob_service.create_container("my-container")

# Upload blob
blob_client = blob_service.get_blob_client("my-container", "config/app.json")
with open("app.json", "rb") as f:
    blob_client.upload_blob(f, overwrite=True)

# Download blob
with open("downloaded.json", "wb") as f:
    blob_data = blob_client.download_blob()
    blob_data.readinto(f)

# Las blob som string
blob_client = blob_service.get_blob_client("my-container", "config/app.json")
content = blob_client.download_blob().readall().decode("utf-8")

# Lista blobs i container
container_client = blob_service.get_container_client("my-container")
for blob in container_client.list_blobs(name_starts_with="logs/"):
    print(f"{blob.name}: {blob.size} bytes")

# Radera blob
blob_client.delete_blob()
```

------------------------------------------------------------

## Praktiskt Exempel: Azure Resource Manager

```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from typing import List, Dict, Optional
import os

class AzureManager:
    \"\"\"Manage Azure resources for DevOps automation.\"\"\"

    def __init__(self):
        self.credential = DefaultAzureCredential()
        self.subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

        self.resource_client = ResourceManagementClient(
            self.credential, self.subscription_id
        )
        self.compute_client = ComputeManagementClient(
            self.credential, self.subscription_id
        )

    def list_resource_groups(self, tag_filter: Optional[Dict] = None) -> List[Dict]:
        \"\"\"List resource groups, optionally filtered by tags.\"\"\"
        result = []
        for rg in self.resource_client.resource_groups.list():
            if tag_filter:
                if not rg.tags:
                    continue
                if not all(rg.tags.get(k) == v for k, v in tag_filter.items()):
                    continue

            result.append({
                "name": rg.name,
                "location": rg.location,
                "tags": rg.tags or {}
            })
        return result

    def list_vms_in_rg(self, resource_group: str) -> List[Dict]:
        \"\"\"List VMs in a resource group with power state.\"\"\"
        result = []
        for vm in self.compute_client.virtual_machines.list(resource_group):
            # Get power state
            instance_view = self.compute_client.virtual_machines.instance_view(
                resource_group, vm.name
            )
            power_state = "unknown"
            for status in instance_view.statuses:
                if status.code.startswith("PowerState/"):
                    power_state = status.code.split("/")[1]
                    break

            result.append({
                "name": vm.name,
                "size": vm.hardware_profile.vm_size,
                "state": power_state,
                "location": vm.location
            })
        return result

    def stop_vms_in_rg(self, resource_group: str) -> int:
        \"\"\"Stop all running VMs in a resource group.\"\"\"
        stopped = 0
        for vm in self.list_vms_in_rg(resource_group):
            if vm["state"] == "running":
                print(f"Stopping {vm['name']}...")
                async_op = self.compute_client.virtual_machines.begin_deallocate(
                    resource_group, vm["name"]
                )
                async_op.wait()
                stopped += 1
        return stopped

    def start_vms_in_rg(self, resource_group: str) -> int:
        \"\"\"Start all stopped VMs in a resource group.\"\"\"
        started = 0
        for vm in self.list_vms_in_rg(resource_group):
            if vm["state"] == "deallocated":
                print(f"Starting {vm['name']}...")
                async_op = self.compute_client.virtual_machines.begin_start(
                    resource_group, vm["name"]
                )
                async_op.wait()
                started += 1
        return started

# Anvandning
if __name__ == "__main__":
    manager = AzureManager()

    # Lista dev resource groups
    dev_rgs = manager.list_resource_groups({"environment": "development"})
    for rg in dev_rgs:
        print(f"\\n{rg['name']}:")
        for vm in manager.list_vms_in_rg(rg["name"]):
            print(f"  {vm['name']}: {vm['state']}")
```

------------------------------------------------------------

## Snabbreferens - Azure SDK

| Service | Paket | Client |
|---------|-------|--------|
| Resources | azure-mgmt-resource | ResourceManagementClient |
| Compute | azure-mgmt-compute | ComputeManagementClient |
| Storage | azure-storage-blob | BlobServiceClient |
| Network | azure-mgmt-network | NetworkManagementClient |
| KeyVault | azure-keyvault-secrets | SecretClient |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| AuthenticationError | Fel credentials | az login eller env vars |
| ResourceNotFoundError | Resurs saknas | Verifiera namn och RG |
| ClientAuthenticationError | RBAC permission | Kolla role assignments |
| HttpResponseError | API error | Kolla error.message |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **DefaultAzureCredential** | Anvand alltid for enkel auth |
| **begin_** | Async operationer |
| **wait()** | Vanta pa async completion |
| **Managed Identity** | Best practice i Azure |
| **RBAC** | Minsta nodvandiga behorighet |

**Kom ihag:**
- DefaultAzureCredential for alla miljoer
- begin_* metoder ar asynkrona
- Anropa .wait() om du behover resultatet
- Anvand Managed Identity i Azure
- Tagga resurser for organisering
"""
        },
        # =====================================================================
        # NODE 14: Docker SDK
        # =====================================================================
        {
            "title": "Docker SDK",
            "slug": "python-docker-sdk",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker SDK

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Docker SDK ar viktigt |
|----------|------------------------------|
| **Automation** | Programmera container lifecycle |
| **CI/CD** | Build och push images |
| **Testing** | Starta test-containers |
| **Orchestration** | Hantera containers programmatiskt |
| **Monitoring** | Hamta container stats |

Som DevOps-ingenjor maste du forsta:

- **docker** Python-biblioteket
- **Container** och **Image** management
- **Volumes** och **Networks**

------------------------------------------------------------

## Installation och Setup

```bash
pip install docker
```

```python
import docker

# Anslut till Docker daemon
client = docker.from_env()  # Anvander DOCKER_HOST eller /var/run/docker.sock

# Verifiera anslutning
print(client.version())
print(client.ping())

# Med explicit URL
# client = docker.DockerClient(base_url="unix:///var/run/docker.sock")
# client = docker.DockerClient(base_url="tcp://localhost:2375")
```

------------------------------------------------------------

## Container Management

```python
import docker

client = docker.from_env()

# Kor en container
container = client.containers.run(
    "nginx:alpine",
    detach=True,
    name="web-server",
    ports={"80/tcp": 8080}
)
print(f"Started: {container.id[:12]}")

# Lista containers
for container in client.containers.list():
    print(f"{container.name}: {container.status}")

# Lista alla (inkl. stoppade)
for container in client.containers.list(all=True):
    print(f"{container.name}: {container.status}")

# Hamta specifik container
container = client.containers.get("web-server")

# Container operationer
container.stop()
container.start()
container.restart()
container.pause()
container.unpause()

# Kor kommando i container
result = container.exec_run("cat /etc/nginx/nginx.conf")
print(result.output.decode())

# Hamta logs
logs = container.logs(tail=100)
print(logs.decode())

# Stream logs
for log in container.logs(stream=True, follow=True):
    print(log.decode(), end="")

# Ta bort container
container.stop()
container.remove()
# Eller force remove
container.remove(force=True)
```

------------------------------------------------------------

## Image Management

```python
import docker

client = docker.from_env()

# Lista images
for image in client.images.list():
    tags = image.tags[0] if image.tags else "<none>"
    print(f"{tags}: {image.id[:12]}")

# Pull image
image = client.images.pull("python", tag="3.11-slim")
print(f"Pulled: {image.tags}")

# Build image
image, logs = client.images.build(
    path="./app",
    tag="myapp:latest",
    dockerfile="Dockerfile"
)
for log in logs:
    if "stream" in log:
        print(log["stream"], end="")

# Push image (kraver login)
client.login(username="user", password="pass", registry="registry.example.com")
client.images.push("registry.example.com/myapp:latest")

# Tag image
image = client.images.get("myapp:latest")
image.tag("registry.example.com/myapp", tag="v1.0.0")

# Ta bort image
client.images.remove("myapp:old")
# Eller
image.remove()

# Prune oanvanda images
client.images.prune()
```

------------------------------------------------------------

## Volumes och Networks

```python
import docker

client = docker.from_env()

# Skapa volume
volume = client.volumes.create(name="app-data")

# Lista volumes
for vol in client.volumes.list():
    print(vol.name)

# Anvand volume i container
container = client.containers.run(
    "postgres:15",
    detach=True,
    name="db",
    volumes={"app-data": {"bind": "/var/lib/postgresql/data", "mode": "rw"}},
    environment={"POSTGRES_PASSWORD": "secret"}
)

# Skapa network
network = client.networks.create("app-network", driver="bridge")

# Lista networks
for net in client.networks.list():
    print(net.name)

# Anslut container till network
network.connect("web-server")

# Container med network
container = client.containers.run(
    "nginx",
    detach=True,
    network="app-network"
)

# Prune
client.volumes.prune()
client.networks.prune()
```

------------------------------------------------------------

## Container Stats och Health

```python
import docker

client = docker.from_env()

container = client.containers.get("web-server")

# Hamta stats (snapshot)
stats = container.stats(stream=False)
print(f"CPU: {stats['cpu_stats']}")
print(f"Memory: {stats['memory_stats']}")

# Stream stats
for stats in container.stats(stream=True, decode=True):
    cpu_percent = calculate_cpu_percent(stats)
    mem_usage = stats["memory_stats"]["usage"]
    print(f"CPU: {cpu_percent:.2f}%, MEM: {mem_usage / 1024 / 1024:.2f}MB")

def calculate_cpu_percent(stats):
    \"\"\"Calculate CPU percentage from stats.\"\"\"
    cpu_delta = stats["cpu_stats"]["cpu_usage"]["total_usage"] - \\
                stats["precpu_stats"]["cpu_usage"]["total_usage"]
    system_delta = stats["cpu_stats"]["system_cpu_usage"] - \\
                   stats["precpu_stats"]["system_cpu_usage"]

    if system_delta > 0:
        cpu_count = len(stats["cpu_stats"]["cpu_usage"].get("percpu_usage", [1]))
        return (cpu_delta / system_delta) * cpu_count * 100.0
    return 0.0

# Inspect container
info = container.attrs
print(f"State: {info['State']['Status']}")
print(f"IP: {info['NetworkSettings']['IPAddress']}")
```

------------------------------------------------------------

## Praktiskt Exempel: Container Manager

```python
import docker
from typing import List, Dict, Optional
from docker.errors import NotFound, APIError

class ContainerManager:
    \"\"\"Manage Docker containers for DevOps automation.\"\"\"

    def __init__(self):
        self.client = docker.from_env()

    def run_container(
        self,
        image: str,
        name: str,
        ports: Optional[Dict] = None,
        env: Optional[Dict] = None,
        volumes: Optional[Dict] = None
    ):
        \"\"\"Run a new container.\"\"\"
        # Ta bort om finns
        try:
            old = self.client.containers.get(name)
            old.remove(force=True)
        except NotFound:
            pass

        container = self.client.containers.run(
            image,
            name=name,
            detach=True,
            ports=ports or {},
            environment=env or {},
            volumes=volumes or {}
        )
        return container

    def list_containers(self, label: Optional[str] = None) -> List[Dict]:
        \"\"\"List containers with optional label filter.\"\"\"
        filters = {}
        if label:
            filters["label"] = label

        result = []
        for c in self.client.containers.list(all=True, filters=filters):
            result.append({
                "id": c.id[:12],
                "name": c.name,
                "image": c.image.tags[0] if c.image.tags else "none",
                "status": c.status,
                "ports": c.ports
            })
        return result

    def cleanup_stopped(self) -> int:
        \"\"\"Remove all stopped containers.\"\"\"
        removed = 0
        for c in self.client.containers.list(all=True):
            if c.status == "exited":
                c.remove()
                removed += 1
        return removed

    def get_logs(self, name: str, lines: int = 100) -> str:
        \"\"\"Get container logs.\"\"\"
        try:
            container = self.client.containers.get(name)
            return container.logs(tail=lines).decode()
        except NotFound:
            return f"Container {name} not found"

    def deploy_stack(self, services: List[Dict]):
        \"\"\"Deploy a stack of services.\"\"\"
        # Skapa network
        try:
            network = self.client.networks.create("app-net", driver="bridge")
        except APIError:
            network = self.client.networks.get("app-net")

        containers = []
        for svc in services:
            container = self.run_container(
                image=svc["image"],
                name=svc["name"],
                ports=svc.get("ports"),
                env=svc.get("env")
            )
            network.connect(container)
            containers.append(container)

        return containers

# Anvandning
if __name__ == "__main__":
    manager = ContainerManager()

    # Deploy services
    services = [
        {
            "name": "redis",
            "image": "redis:alpine",
            "ports": {"6379/tcp": 6379}
        },
        {
            "name": "api",
            "image": "myapp:latest",
            "ports": {"8000/tcp": 8000},
            "env": {"REDIS_HOST": "redis"}
        }
    ]

    containers = manager.deploy_stack(services)
    for c in containers:
        print(f"Started: {c.name}")
```

------------------------------------------------------------

## Snabbreferens - Docker SDK

| Uppgift | Kod |
|---------|-----|
| Connect | `docker.from_env()` |
| Run | `client.containers.run(image, detach=True)` |
| List | `client.containers.list()` |
| Stop | `container.stop()` |
| Remove | `container.remove()` |
| Logs | `container.logs()` |
| Pull | `client.images.pull(image)` |
| Build | `client.images.build(path=".")` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| NotFound | Container/image finns ej | Kolla namn |
| APIError | Docker daemon error | Verifiera daemon |
| ImageNotFound | Image finns ej lokalt | pull forst |
| PermissionError | Ingen docker-access | Lagg till user i docker-grupp |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **from_env()** | Automatisk connection |
| **detach=True** | Kor i bakgrund |
| **list(all=True)** | Inkluderar stoppade |
| **remove(force=True)** | Tvinga bort |
| **logs(stream=True)** | For realtid |

**Kom ihag:**
- docker.from_env() for automatisk setup
- detach=True for bakgrundskorning
- Hantera NotFound exception
- Prune for att rensa gamla resurser
- Anvand networks for container-kommunikation
"""
        },
        # =====================================================================
        # NODE 15: Logging & Monitoring
        # =====================================================================
        {
            "title": "Logging & Monitoring",
            "slug": "python-logging",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Logging & Monitoring

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor loggning ar viktigt |
|----------|---------------------------|
| **Debugging** | Spara fel for analys |
| **Audit** | Spara handelser |
| **Metrics** | Samla in data |
| **Alerting** | Trigga vid problem |
| **Compliance** | Kraver loggning |

Som DevOps-ingenjor maste du forsta:

- **logging** module for strukturerad loggning
- **Log levels** for filtrering
- **Handlers** for olika destinations

------------------------------------------------------------

## Grundlaggande logging

```python
import logging

# Enklaste setup
logging.basicConfig(level=logging.INFO)
logging.info("Application started")

# Konfigurera format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Log levels (i stigande ordning)
logging.debug("Debug message")     # 10 - Detaljerad info
logging.info("Info message")       # 20 - Generell info
logging.warning("Warning message") # 30 - Varning
logging.error("Error message")     # 40 - Fel
logging.critical("Critical!")      # 50 - Kritiskt fel

# Med variabler
server = "web-01"
port = 8080
logging.info(f"Server {server} started on port {port}")

# Med exception info
try:
    result = 1 / 0
except Exception:
    logging.error("Division failed", exc_info=True)
```

------------------------------------------------------------

## Logger per modul

```python
import logging

# Skapa logger for denna modul
logger = logging.getLogger(__name__)

# I modul/script:
def process_file(filename):
    logger.info(f"Processing {filename}")
    try:
        # ... process
        logger.debug(f"Processed {filename} successfully")
    except Exception as e:
        logger.error(f"Failed to process {filename}: {e}")
        raise

# Konfigurera root logger i main
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Satt niva per logger
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
```

------------------------------------------------------------

## Handlers - Logga till olika destinations

```python
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)

# File handler med rotation pa storlek
file_handler = RotatingFileHandler(
    "app.log",
    maxBytes=10*1024*1024,  # 10MB
    backupCount=5
)
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

# Tidsbaserad rotation
time_handler = TimedRotatingFileHandler(
    "app.log",
    when="midnight",
    interval=1,
    backupCount=30
)

# Anvandning
logger.info("This goes to console and file")
logger.debug("This only goes to file")
```

------------------------------------------------------------

## JSON Logging

```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    \"\"\"Format logs as JSON for log aggregation.\"\"\"

    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }

        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)

        # Lagg till extra fields
        for key, value in record.__dict__.items():
            if key not in ["msg", "args", "exc_info", "exc_text", "stack_info",
                          "name", "levelno", "levelname", "pathname", "filename",
                          "module", "funcName", "lineno", "created", "msecs",
                          "relativeCreated", "thread", "threadName", "processName",
                          "process", "message"]:
                log_entry[key] = value

        return json.dumps(log_entry)

# Setup
logger = logging.getLogger("myapp")
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Anvandning med extra fields
logger.info("User logged in", extra={"user_id": "123", "ip": "192.168.1.1"})

# Output:
# {"timestamp": "2024-01-15T10:30:00", "level": "INFO", "logger": "myapp",
#  "message": "User logged in", "user_id": "123", "ip": "192.168.1.1", ...}
```

------------------------------------------------------------

## Structured Logging med structlog

```python
# pip install structlog
import structlog

# Konfigurera structlog
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.add_log_level,
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.BoundLogger,
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
)

logger = structlog.get_logger()

# Anvandning
logger.info("server_started", host="0.0.0.0", port=8080)
# {"timestamp": "2024-01-15T10:30:00", "level": "info",
#  "event": "server_started", "host": "0.0.0.0", "port": 8080}

# Bind context
logger = logger.bind(request_id="abc123")
logger.info("request_received", path="/api/users")
# Alla logs inkluderar nu request_id

# Med exception
try:
    raise ValueError("Invalid input")
except Exception:
    logger.exception("request_failed")
```

------------------------------------------------------------

## Praktiskt Exempel: Logger Setup

```python
import logging
import sys
import os
from logging.handlers import RotatingFileHandler
import json
from datetime import datetime

def setup_logging(
    name: str,
    level: str = "INFO",
    log_file: str = None,
    json_format: bool = False
):
    \"\"\"Configure logging for application.\"\"\"

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))

    # Remove existing handlers
    logger.handlers = []

    # Formatter
    if json_format:
        class JSONFormatter(logging.Formatter):
            def format(self, record):
                return json.dumps({
                    "timestamp": datetime.utcnow().isoformat(),
                    "level": record.levelname,
                    "logger": record.name,
                    "message": record.getMessage(),
                    "module": record.module
                })
        formatter = JSONFormatter()
    else:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

    # Console handler
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    logger.addHandler(console)

    # File handler
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=10*1024*1024,
            backupCount=5
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

# Anvandning
if __name__ == "__main__":
    # Development
    logger = setup_logging("myapp", level="DEBUG")

    # Production med JSON
    logger = setup_logging(
        "myapp",
        level=os.environ.get("LOG_LEVEL", "INFO"),
        log_file="/var/log/myapp/app.log",
        json_format=True
    )

    logger.info("Application started")
```

------------------------------------------------------------

## Snabbreferens - Logging

| Uppgift | Kod |
|---------|-----|
| Basic setup | `logging.basicConfig(level=logging.INFO)` |
| Get logger | `logger = logging.getLogger(__name__)` |
| Log levels | DEBUG, INFO, WARNING, ERROR, CRITICAL |
| File handler | `RotatingFileHandler(file, maxBytes, backupCount)` |
| Exception | `logger.error("msg", exc_info=True)` |
| Extra data | `logger.info("msg", extra={"key": "value"})` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| No output | Fel level | Sank level |
| Duplicate logs | Flera handlers | Clear handlers |
| Missing exc | Ingen exc_info | Lagg till exc_info=True |
| Fil error | Permission | Kolla rattigheter |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **__name__** | Anvand for logger name |
| **Levels** | Anvand ratt level |
| **Rotation** | Alltid for filer |
| **JSON** | For log aggregation |
| **exc_info** | For exceptions |

**Kom ihag:**
- logging.getLogger(__name__) per modul
- Anvand ratt log level
- RotatingFileHandler for filloggar
- JSON format for ELK/Splunk
- exc_info=True for stack traces
"""
        },
        # =====================================================================
        # NODE 16: Testing with Pytest
        # =====================================================================
        {
            "title": "Testing with Pytest",
            "slug": "python-testing",
            "difficulty": "intermediate",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Testing with Pytest

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor testing ar viktigt |
|----------|--------------------------|
| **CI/CD** | Automatiska tester i pipeline |
| **Kvalitet** | Sakerstall funktionalitet |
| **Refactoring** | Trygg kodandring |
| **Documentation** | Tester visar anvandning |
| **Regression** | Fanga buggar tidigt |

Som DevOps-ingenjor maste du forsta:

- **pytest** for att skriva och kora tester
- **Fixtures** for setup/teardown
- **Mocking** for externa beroenden

------------------------------------------------------------

## Grundlaggande pytest

```bash
pip install pytest
```

```python
# tests/test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_add_strings():
    assert add("hello", " world") == "hello world"
```

```bash
# Kor tester
pytest                      # Alla tester
pytest tests/test_math.py   # Specifik fil
pytest -v                   # Verbose output
pytest -k "add"             # Filter pa namn
pytest --tb=short           # Kortare traceback
```

------------------------------------------------------------

## Test Classes och Organization

```python
# tests/test_server.py
import pytest

class TestServer:
    \"\"\"Test server functionality.\"\"\"

    def test_start(self):
        server = Server("localhost", 8080)
        assert server.start() == True

    def test_stop(self):
        server = Server("localhost", 8080)
        server.start()
        assert server.stop() == True

    def test_invalid_port(self):
        with pytest.raises(ValueError):
            Server("localhost", -1)

class TestConnection:
    def test_connect(self):
        conn = Connection("192.168.1.1")
        assert conn.status == "connected"
```

### Projekt struktur

```
project/
+-- src/
|   +-- myapp/
|       +-- __init__.py
|       +-- server.py
+-- tests/
|   +-- __init__.py
|   +-- conftest.py        # Shared fixtures
|   +-- test_server.py
|   +-- test_connection.py
+-- pyproject.toml
+-- pytest.ini
```

------------------------------------------------------------

## Fixtures

```python
# tests/conftest.py
import pytest
import tempfile
import os

@pytest.fixture
def temp_file():
    \"\"\"Create a temporary file for testing.\"\"\"
    fd, path = tempfile.mkstemp()
    os.write(fd, b"test content")
    os.close(fd)
    yield path  # Test kors har
    os.unlink(path)  # Cleanup

@pytest.fixture
def config():
    \"\"\"Provide test configuration.\"\"\"
    return {
        "host": "localhost",
        "port": 8080,
        "debug": True
    }

@pytest.fixture(scope="session")
def database():
    \"\"\"Setup database connection once per test session.\"\"\"
    db = Database("test.db")
    db.connect()
    yield db
    db.close()

# Anvandning i test
def test_read_file(temp_file):
    with open(temp_file) as f:
        assert f.read() == "test content"

def test_server_config(config):
    server = Server(**config)
    assert server.port == 8080
```

### Fixture Scopes

```python
@pytest.fixture(scope="function")   # Default - per test
@pytest.fixture(scope="class")      # Per test class
@pytest.fixture(scope="module")     # Per test file
@pytest.fixture(scope="session")    # Per pytest session
```

------------------------------------------------------------

## Parametriserade tester

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (-2, 4),
])
def test_square(input, expected):
    assert input ** 2 == expected

@pytest.mark.parametrize("filename,valid", [
    ("config.yaml", True),
    ("config.yml", True),
    ("config.json", False),
    ("config", False),
])
def test_is_yaml_file(filename, valid):
    assert is_yaml_file(filename) == valid

# Multipla parametrar
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_multiply(x, y):
    # Testar alla kombinationer: (1,10), (1,20), (2,10), (2,20), (3,10), (3,20)
    assert x * y == x * y
```

------------------------------------------------------------

## Mocking

```python
from unittest.mock import Mock, patch, MagicMock
import pytest

# Mock objekt
def test_api_call():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "ok"}

    # Ersatt requests.get
    with patch("requests.get", return_value=mock_response):
        result = check_api_health("http://api.example.com")
        assert result == True

# Mock som decorator
@patch("myapp.database.connect")
def test_with_mock_db(mock_connect):
    mock_connect.return_value = Mock(connected=True)

    app = Application()
    assert app.is_connected() == True
    mock_connect.assert_called_once()

# Mock context manager
def test_file_read():
    mock_open = mock_open(read_data="config data")

    with patch("builtins.open", mock_open):
        result = read_config("config.yaml")
        assert result == "config data"

# Mock environment variables
@patch.dict("os.environ", {"API_KEY": "test-key"})
def test_api_key():
    import os
    assert os.environ["API_KEY"] == "test-key"
```

------------------------------------------------------------

## Markers och Skip

```python
import pytest

@pytest.mark.slow
def test_large_dataset():
    # Lang test
    pass

@pytest.mark.integration
def test_database_connection():
    # Kraver extern databas
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_new_feature():
    pass

@pytest.mark.skipif(
    os.environ.get("CI") != "true",
    reason="Only run in CI"
)
def test_ci_only():
    pass

@pytest.mark.xfail(reason="Known bug #123")
def test_known_failure():
    assert False  # Forvantas misslyckas

# pytest.ini eller pyproject.toml
# [pytest]
# markers =
#     slow: marks tests as slow
#     integration: integration tests
```

```bash
# Kor endast specifika markers
pytest -m slow
pytest -m "not slow"
pytest -m "integration and not slow"
```

------------------------------------------------------------

## Praktiskt Exempel: Testing en Server

```python
# src/server.py
class Server:
    def __init__(self, host, port):
        if port < 0 or port > 65535:
            raise ValueError("Invalid port")
        self.host = host
        self.port = port
        self.running = False

    def start(self):
        self.running = True
        return True

    def stop(self):
        self.running = False
        return True

# tests/conftest.py
import pytest
from server import Server

@pytest.fixture
def server():
    s = Server("localhost", 8080)
    yield s
    if s.running:
        s.stop()

# tests/test_server.py
import pytest
from server import Server

class TestServer:
    def test_create_server(self):
        s = Server("localhost", 8080)
        assert s.host == "localhost"
        assert s.port == 8080
        assert s.running == False

    def test_invalid_port(self):
        with pytest.raises(ValueError):
            Server("localhost", -1)

    def test_start_server(self, server):
        assert server.start() == True
        assert server.running == True

    def test_stop_server(self, server):
        server.start()
        assert server.stop() == True
        assert server.running == False

    @pytest.mark.parametrize("port", [0, 80, 443, 8080, 65535])
    def test_valid_ports(self, port):
        s = Server("localhost", port)
        assert s.port == port

    @pytest.mark.parametrize("port", [-1, 65536, 100000])
    def test_invalid_ports(self, port):
        with pytest.raises(ValueError):
            Server("localhost", port)
```

------------------------------------------------------------

## pytest.ini / pyproject.toml

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v --tb=short
markers =
    slow: slow running tests
    integration: integration tests
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
addopts = "-v --tb=short --cov=src"
markers = [
    "slow: slow running tests",
    "integration: integration tests"
]
```

------------------------------------------------------------

## Snabbreferens - pytest

| Uppgift | Kod |
|---------|-----|
| Run tests | `pytest` |
| Verbose | `pytest -v` |
| Filter | `pytest -k "test_name"` |
| Marker | `pytest -m slow` |
| Coverage | `pytest --cov=src` |
| Stop on fail | `pytest -x` |
| Last failed | `pytest --lf` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Not found | Fel filnamn | test_*.py |
| Import error | Path problem | Lagg till __init__.py |
| Fixture not found | Fel scope | Kolla conftest.py |
| Mock not applied | Fel path | Mock where used |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Fixtures** | For setup/teardown |
| **Parametrize** | For multipla inputs |
| **Mock** | For externa beroenden |
| **Markers** | For att kategorisera |
| **conftest.py** | For delade fixtures |

**Kom ihag:**
- Namnge filer test_*.py
- Anvand fixtures for setup
- Mock externa services
- pytest -v for detaljerad output
- Coverage for att mata tackning
"""
        },
        # =====================================================================
        # NODE 17: Async Programming
        # =====================================================================
        {
            "title": "Async Programming",
            "slug": "python-async",
            "difficulty": "advanced",
            "estimated_minutes": 60,
            "xp_reward": 100,
            "content": """# Async Programming

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor async ar viktigt |
|----------|------------------------|
| **API servers** | Hantera manga requests |
| **Monitoring** | Parallell datainsamling |
| **Automation** | Parallella tasks |
| **Webhooks** | Icke-blockerande |
| **Chat/Bots** | Real-time kommunikation |

Som DevOps-ingenjor maste du forsta:

- **async/await** syntax
- **asyncio** event loop
- **Concurrent** execution

------------------------------------------------------------

## Grundlaggande async/await

```python
import asyncio

# Async funktion (coroutine)
async def fetch_data(url):
    print(f"Fetching {url}")
    await asyncio.sleep(1)  # Simulera I/O
    return f"Data from {url}"

# Kora async funktion
async def main():
    result = await fetch_data("http://api.example.com")
    print(result)

# Entry point
asyncio.run(main())

# Eller i existing event loop
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
```

### Grundlaggande monster

```python
import asyncio

async def process_item(item):
    \"\"\"Process a single item asynchronously.\"\"\"
    print(f"Processing {item}")
    await asyncio.sleep(0.5)  # Simulera I/O
    return f"Processed {item}"

async def main():
    items = ["a", "b", "c", "d", "e"]

    # Sekventiell (langsam)
    results = []
    for item in items:
        result = await process_item(item)
        results.append(result)

    print(results)

asyncio.run(main())  # Tar 2.5 sekunder
```

------------------------------------------------------------

## Parallell korning med gather

```python
import asyncio

async def fetch_url(url):
    print(f"Fetching {url}")
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    urls = [
        "http://api1.example.com",
        "http://api2.example.com",
        "http://api3.example.com"
    ]

    # Parallell - alla startar samtidigt!
    results = await asyncio.gather(
        fetch_url(urls[0]),
        fetch_url(urls[1]),
        fetch_url(urls[2])
    )

    print(results)

asyncio.run(main())  # Tar ca 1 sekund (inte 3!)

# Med lista
async def main():
    urls = ["http://api1.com", "http://api2.com", "http://api3.com"]

    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)

    return results
```

### gather med error handling

```python
import asyncio

async def risky_operation(n):
    if n == 2:
        raise ValueError("Error on item 2")
    await asyncio.sleep(0.5)
    return f"Result {n}"

async def main():
    # return_exceptions=True returnerar exceptions istallet for att kasta
    results = await asyncio.gather(
        risky_operation(1),
        risky_operation(2),
        risky_operation(3),
        return_exceptions=True
    )

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i} failed: {result}")
        else:
            print(f"Task {i}: {result}")

asyncio.run(main())
```

------------------------------------------------------------

## Tasks och create_task

```python
import asyncio

async def background_task(name):
    while True:
        print(f"{name}: running")
        await asyncio.sleep(1)

async def main():
    # Skapa task som kors i bakgrunden
    task = asyncio.create_task(background_task("monitor"))

    # Gor annat arbete
    await asyncio.sleep(3)

    # Avbryt bakgrundstask
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task cancelled")

asyncio.run(main())

# Vanta pa tasks
async def main():
    task1 = asyncio.create_task(fetch_data("url1"))
    task2 = asyncio.create_task(fetch_data("url2"))

    # Gor annat medan tasks kors
    print("Tasks started...")

    # Vanta pa resultat
    result1 = await task1
    result2 = await task2
```

------------------------------------------------------------

## Timeout och Semaphores

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(10)
    return "Done"

async def main():
    # Med timeout
    try:
        result = await asyncio.wait_for(
            slow_operation(),
            timeout=2.0
        )
    except asyncio.TimeoutError:
        print("Operation timed out!")

asyncio.run(main())

# Semaphore for att begansa parallellitet
async def fetch_with_limit(url, semaphore):
    async with semaphore:
        print(f"Fetching {url}")
        await asyncio.sleep(1)
        return f"Data from {url}"

async def main():
    # Max 3 parallella requests
    semaphore = asyncio.Semaphore(3)

    urls = [f"http://api{i}.com" for i in range(10)]
    tasks = [fetch_with_limit(url, semaphore) for url in urls]

    results = await asyncio.gather(*tasks)
    print(results)
```

------------------------------------------------------------

## aiohttp for async HTTP

```python
import asyncio
import aiohttp  # pip install aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        # Parallella requests
        tasks = [
            fetch(session, "https://api.github.com/users/torvalds"),
            fetch(session, "https://api.github.com/users/gvanrossum"),
            fetch(session, "https://api.github.com/users/kennethreitz")
        ]

        results = await asyncio.gather(*tasks)

        for result in results:
            print(f"{result['login']}: {result['public_repos']} repos")

asyncio.run(main())
```

------------------------------------------------------------

## Praktiskt Exempel: Async Health Checker

```python
import asyncio
import aiohttp
from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime

@dataclass
class HealthResult:
    url: str
    status: str
    latency_ms: float
    timestamp: str

async def check_endpoint(
    session: aiohttp.ClientSession,
    url: str,
    timeout: int = 5
) -> HealthResult:
    \"\"\"Check health of a single endpoint.\"\"\"
    start = asyncio.get_event_loop().time()

    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as resp:
            latency = (asyncio.get_event_loop().time() - start) * 1000
            status = "healthy" if resp.status < 400 else "unhealthy"

            return HealthResult(
                url=url,
                status=status,
                latency_ms=round(latency, 2),
                timestamp=datetime.utcnow().isoformat()
            )
    except asyncio.TimeoutError:
        return HealthResult(url=url, status="timeout", latency_ms=-1,
                          timestamp=datetime.utcnow().isoformat())
    except Exception as e:
        return HealthResult(url=url, status=f"error: {str(e)}", latency_ms=-1,
                          timestamp=datetime.utcnow().isoformat())

async def health_check(endpoints: List[str], concurrency: int = 10) -> List[HealthResult]:
    \"\"\"Check multiple endpoints with controlled concurrency.\"\"\"
    semaphore = asyncio.Semaphore(concurrency)

    async def check_with_limit(session, url):
        async with semaphore:
            return await check_endpoint(session, url)

    async with aiohttp.ClientSession() as session:
        tasks = [check_with_limit(session, url) for url in endpoints]
        results = await asyncio.gather(*tasks)

    return results

async def main():
    endpoints = [
        "https://api.github.com",
        "https://google.com",
        "https://httpbin.org/status/500",
        "https://nonexistent.example.com"
    ]

    results = await health_check(endpoints)

    for r in results:
        print(f"{r.url}: {r.status} ({r.latency_ms}ms)")

if __name__ == "__main__":
    asyncio.run(main())
```

------------------------------------------------------------

## Snabbreferens - Async

| Uppgift | Kod |
|---------|-----|
| Definiera | `async def func():` |
| Anropa | `await func()` |
| Kora | `asyncio.run(main())` |
| Parallell | `asyncio.gather(*tasks)` |
| Task | `asyncio.create_task(coro)` |
| Timeout | `asyncio.wait_for(coro, timeout=5)` |
| Semaphore | `asyncio.Semaphore(n)` |
| Sleep | `await asyncio.sleep(1)` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Never awaited | Glomt await | Lagg till await |
| Event loop running | Nested run | Anvand create_task |
| Blocking call | Sync I/O i async | Anvand async bibliotek |
| Task cancelled | Timeout/cancel | Hantera CancelledError |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **async/await** | For icke-blockerande kod |
| **gather** | For parallell korning |
| **Semaphore** | Begransar parallellitet |
| **aiohttp** | Async HTTP requests |
| **Timeout** | Alltid satt timeout |

**Kom ihag:**
- await for att pausa och vanta
- gather for parallell exekvering
- Semaphore for rate limiting
- Anvand aiohttp istallet for requests
- Hantera timeouts och cancellation
"""
        },
        # =====================================================================
        # NODE 18: Decorators & Context Managers
        # =====================================================================
        {
            "title": "Decorators & Context Managers",
            "slug": "python-decorators",
            "difficulty": "advanced",
            "estimated_minutes": 50,
            "xp_reward": 95,
            "content": """# Decorators & Context Managers

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor decorators ar viktiga |
|----------|------------------------------|
| **Logging** | Automatisk loggning |
| **Timing** | Mata exekveringstid |
| **Retry** | Automatisk retry-logik |
| **Caching** | Memoization |
| **Auth** | Authentication/authorization |

Som DevOps-ingenjor maste du forsta:

- **Decorators** for att utoka funktioner
- **Context managers** for resource management
- **functools** for decorator-verktyg

------------------------------------------------------------

## Decorators - Grundlaggande

```python
import functools

# Enkel decorator
def log_call(func):
    @functools.wraps(func)  # Behall original metadata
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

# Samma som: add = log_call(add)
result = add(2, 3)
# Output:
# Calling add
# add returned 5
```

### Timer decorator

```python
import functools
import time

def timer(func):
    \"\"\"Measure function execution time.\"\"\"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

slow_function()  # "slow_function took 1.0012 seconds"
```

------------------------------------------------------------

## Decorators med argument

```python
import functools
import time

def retry(max_attempts=3, delay=1):
    \"\"\"Retry decorator with configurable attempts.\"\"\"
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def unreliable_api_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("API unavailable")
    return "Success!"

# Anvandning
result = unreliable_api_call()
```

### Decorator med eller utan argument

```python
import functools

def cache(func=None, *, maxsize=128):
    \"\"\"Cache decorator that works with or without arguments.\"\"\"
    def decorator(fn):
        @functools.wraps(fn)
        @functools.lru_cache(maxsize=maxsize)
        def wrapper(*args):
            return fn(*args)
        return wrapper

    if func is not None:
        return decorator(func)
    return decorator

# Utan argument
@cache
def fetch_data(url):
    return requests.get(url).json()

# Med argument
@cache(maxsize=256)
def fetch_user(user_id):
    return db.get_user(user_id)
```

------------------------------------------------------------

## Context Managers - Grundlaggande

```python
# Anvandning
with open("file.txt") as f:
    content = f.read()
# Filen stangs automatiskt

# Skapa egen context manager med class
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False  # False = propagera exceptions

# Anvandning
with Timer() as t:
    time.sleep(1)
print(f"Operation took {t.elapsed:.4f}s")
```

### Med @contextmanager decorator

```python
from contextlib import contextmanager
import os

@contextmanager
def change_dir(path):
    \"\"\"Temporarily change directory.\"\"\"
    old_dir = os.getcwd()
    try:
        os.chdir(path)
        yield  # Kod i with-blocket kors har
    finally:
        os.chdir(old_dir)

# Anvandning
with change_dir("/tmp"):
    print(os.getcwd())  # /tmp
print(os.getcwd())  # Original directory

@contextmanager
def database_transaction(conn):
    \"\"\"Handle database transaction.\"\"\"
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise

# Anvandning
with database_transaction(db_conn) as conn:
    conn.execute("INSERT ...")
    conn.execute("UPDATE ...")
# Auto-commit or rollback
```

------------------------------------------------------------

## Praktiska DevOps Decorators

```python
import functools
import time
import logging

logger = logging.getLogger(__name__)

def log_execution(func):
    \"\"\"Log function execution with timing.\"\"\"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Starting {func.__name__}")
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            logger.info(f"Completed {func.__name__} in {elapsed:.2f}s")
            return result
        except Exception as e:
            logger.error(f"Failed {func.__name__}: {e}")
            raise
    return wrapper

def require_env(*env_vars):
    \"\"\"Ensure required environment variables exist.\"\"\"
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            missing = [v for v in env_vars if v not in os.environ]
            if missing:
                raise EnvironmentError(f"Missing env vars: {missing}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def deprecated(message=""):
    \"\"\"Mark function as deprecated.\"\"\"
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import warnings
            warnings.warn(
                f"{func.__name__} is deprecated. {message}",
                DeprecationWarning,
                stacklevel=2
            )
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Anvandning
@log_execution
@require_env("DATABASE_URL", "API_KEY")
def deploy_application():
    \"\"\"Deploy the application.\"\"\"
    pass

@deprecated("Use new_function instead")
def old_function():
    pass
```

------------------------------------------------------------

## Praktiska Context Managers

```python
from contextlib import contextmanager
import tempfile
import shutil
import os

@contextmanager
def temp_directory():
    \"\"\"Create and cleanup temporary directory.\"\"\"
    path = tempfile.mkdtemp()
    try:
        yield path
    finally:
        shutil.rmtree(path, ignore_errors=True)

@contextmanager
def env_override(**env_vars):
    \"\"\"Temporarily override environment variables.\"\"\"
    old_values = {}
    for key, value in env_vars.items():
        old_values[key] = os.environ.get(key)
        os.environ[key] = value
    try:
        yield
    finally:
        for key, old_value in old_values.items():
            if old_value is None:
                del os.environ[key]
            else:
                os.environ[key] = old_value

@contextmanager
def ssh_connection(host, user):
    \"\"\"Manage SSH connection lifecycle.\"\"\"
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, username=user)
        yield client
    finally:
        client.close()

# Anvandning
with temp_directory() as tmpdir:
    # Arbeta med temp-filer
    pass
# Katalog ar automatiskt borttagen

with env_override(DEBUG="true", LOG_LEVEL="DEBUG"):
    # Korande med overridden env
    pass
# Ursprungliga varden aterstalds
```

------------------------------------------------------------

## Snabbreferens - Decorators & Context Managers

| Uppgift | Kod |
|---------|-----|
| Simple decorator | `def deco(func): ... return wrapper` |
| With args | `def deco(arg): def inner(func): ...` |
| Preserve metadata | `@functools.wraps(func)` |
| Context class | `__enter__`, `__exit__` |
| Context func | `@contextmanager` |
| Built-in cache | `@functools.lru_cache` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Lost metadata | Inget wraps | @functools.wraps |
| Wrong return | Return saknas | return func() |
| Exit not called | Exception | finally: block |
| Nested issue | Decorator order | Kolla ordning |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **@functools.wraps** | Alltid anvand |
| **@contextmanager** | Enklare an class |
| **Retry** | Vanlig DevOps-pattern |
| **Timer** | For performance |
| **finally** | Garanterad cleanup |

**Kom ihag:**
- @functools.wraps for att behalla metadata
- @contextmanager for enkla context managers
- finally for garanterad cleanup
- Decorators exekverar inifrån och ut
- Context managers for resource management
"""
        },
        # =====================================================================
        # NODE 19: Type Hints & Mypy
        # =====================================================================
        {
            "title": "Type Hints & Mypy",
            "slug": "python-type-hints",
            "difficulty": "advanced",
            "estimated_minutes": 45,
            "xp_reward": 85,
            "content": """# Type Hints & Mypy

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor type hints ar viktiga |
|----------|------------------------------|
| **IDE** | Battre autocomplete |
| **Dokumentation** | Sjalvdokumenterande kod |
| **Buggar** | Fanga fel tidigt |
| **Refactoring** | Tryggare andringar |
| **CI/CD** | Statisk analys i pipeline |

Som DevOps-ingenjor maste du forsta:

- **Type hints** syntax
- **typing** modulen
- **mypy** for statisk analys

------------------------------------------------------------

## Grundlaggande Type Hints

```python
# Variabler
name: str = "web-server"
port: int = 8080
enabled: bool = True
ratio: float = 0.95

# Funktioner
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

def process() -> None:
    print("Processing...")

# Default-varden
def create_server(host: str, port: int = 8080) -> dict:
    return {"host": host, "port": port}
```

------------------------------------------------------------

## Collections

```python
from typing import List, Dict, Set, Tuple

# Listor
servers: List[str] = ["web-01", "web-02"]
ports: List[int] = [80, 443, 8080]

# Dictionaries
config: Dict[str, str] = {"host": "localhost"}
server_ports: Dict[str, int] = {"web": 80, "api": 8080}

# Sets
tags: Set[str] = {"production", "frontend"}

# Tuples
endpoint: Tuple[str, int] = ("localhost", 8080)
# Fixed length tuple
rgb: Tuple[int, int, int] = (255, 128, 0)
# Variable length
args: Tuple[str, ...] = ("a", "b", "c")

# Python 3.9+ - built-in generics
servers: list[str] = ["web-01", "web-02"]
config: dict[str, str] = {"host": "localhost"}
```

------------------------------------------------------------

## Optional och Union

```python
from typing import Optional, Union

# Optional - kan vara None
def find_server(name: str) -> Optional[dict]:
    \"\"\"Returns server dict or None if not found.\"\"\"
    servers = {"web": {"port": 80}}
    return servers.get(name)

# Union - flera mojliga typer
def process(value: Union[str, int]) -> str:
    return str(value)

# Python 3.10+ - pipe syntax
def process(value: str | int) -> str:
    return str(value)

def get_port(default: int | None = None) -> int | None:
    return os.environ.get("PORT") or default
```

------------------------------------------------------------

## Callable och TypeVar

```python
from typing import Callable, TypeVar

# Callable - funktioner som parametrar
def retry(func: Callable[[], str], attempts: int = 3) -> str:
    for _ in range(attempts):
        try:
            return func()
        except Exception:
            continue
    raise Exception("All retries failed")

# Med argument
Handler = Callable[[str, int], bool]

def process(handler: Handler) -> None:
    result = handler("data", 42)

# TypeVar - generiska typer
T = TypeVar("T")

def first(items: List[T]) -> T:
    return items[0]

# first(["a", "b"]) returnerar str
# first([1, 2, 3]) returnerar int
```

------------------------------------------------------------

## TypedDict och dataclass

```python
from typing import TypedDict
from dataclasses import dataclass

# TypedDict for dict-struktur
class ServerConfig(TypedDict):
    host: str
    port: int
    enabled: bool

config: ServerConfig = {
    "host": "localhost",
    "port": 8080,
    "enabled": True
}

# Med optional fields
class ServerConfig(TypedDict, total=False):
    host: str
    port: int
    ssl: bool  # Optional

# Dataclass med types
@dataclass
class Server:
    hostname: str
    ip: str
    port: int = 22
    tags: List[str] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []

server = Server("web-01", "192.168.1.1", 8080)
```

------------------------------------------------------------

## Literal och Final

```python
from typing import Literal, Final

# Literal - specifika varden
Environment = Literal["development", "staging", "production"]

def deploy(env: Environment) -> None:
    print(f"Deploying to {env}")

deploy("production")  # OK
deploy("test")        # Type error!

# Final - konstanter
MAX_RETRIES: Final = 3
API_URL: Final[str] = "https://api.example.com"

# Kan inte reassign
MAX_RETRIES = 5  # Type error!

# Kombinera
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]
DEFAULT_LEVEL: Final[LogLevel] = "INFO"
```

------------------------------------------------------------

## Mypy - Statisk typkontroll

```bash
# Installation
pip install mypy

# Kor mypy
mypy script.py
mypy src/

# Med konfiguration
mypy --strict src/
mypy --ignore-missing-imports src/
```

### mypy.ini eller pyproject.toml

```ini
# mypy.ini
[mypy]
python_version = 3.11
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
ignore_missing_imports = True

[mypy-tests.*]
disallow_untyped_defs = False
```

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.11"
warn_return_any = true
disallow_untyped_defs = true
ignore_missing_imports = true
```

------------------------------------------------------------

## Praktiskt Exempel: Typed DevOps Code

```python
from typing import List, Dict, Optional, TypedDict
from dataclasses import dataclass, field

class ServerConfig(TypedDict):
    hostname: str
    ip: str
    port: int

@dataclass
class DeployResult:
    success: bool
    message: str
    duration_seconds: float
    servers: List[str] = field(default_factory=list)

class ServerManager:
    def __init__(self) -> None:
        self.servers: Dict[str, ServerConfig] = {}

    def add_server(self, name: str, config: ServerConfig) -> None:
        self.servers[name] = config

    def get_server(self, name: str) -> Optional[ServerConfig]:
        return self.servers.get(name)

    def list_servers(self) -> List[str]:
        return list(self.servers.keys())

    def deploy(
        self,
        servers: List[str],
        environment: str
    ) -> DeployResult:
        \"\"\"Deploy to specified servers.\"\"\"
        deployed: List[str] = []

        for name in servers:
            server = self.get_server(name)
            if server:
                print(f"Deploying to {server['hostname']}")
                deployed.append(name)

        return DeployResult(
            success=len(deployed) == len(servers),
            message=f"Deployed to {len(deployed)}/{len(servers)} servers",
            duration_seconds=1.5,
            servers=deployed
        )

# Anvandning
manager = ServerManager()
manager.add_server("web", {"hostname": "web-01", "ip": "192.168.1.1", "port": 8080})

result = manager.deploy(["web"], "production")
print(result.message)
```

------------------------------------------------------------

## Snabbreferens - Type Hints

| Type | Syntax |
|------|--------|
| String | `str` |
| Integer | `int` |
| Float | `float` |
| Boolean | `bool` |
| None | `None` |
| List | `List[str]` / `list[str]` |
| Dict | `Dict[str, int]` / `dict[str, int]` |
| Optional | `Optional[str]` / `str \\| None` |
| Union | `Union[str, int]` / `str \\| int` |
| Callable | `Callable[[int], str]` |
| Any | `Any` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Missing import | Glomt import | from typing import ... |
| Incompatible | Fel typ | Fixa typen eller cast |
| Missing return | Saknar return type | Lagg till -> Type |
| Generic needed | List utan type | List[str] |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **Optional** | For None-varden |
| **TypedDict** | For dict-struktur |
| **dataclass** | For data objects |
| **mypy** | For statisk analys |
| **-> None** | For void-funktioner |

**Kom ihag:**
- Optional[X] = X eller None
- Python 3.10+ stodjer | syntax
- mypy i CI/CD pipeline
- TypedDict for dict-schemas
- dataclass for struct-liknande klasser
"""
        },
        # =====================================================================
        # NODE 20: Packaging & Distribution
        # =====================================================================
        {
            "title": "Packaging & Distribution",
            "slug": "python-packaging",
            "difficulty": "advanced",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Packaging & Distribution

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor packaging ar viktigt |
|----------|----------------------------|
| **Distribution** | Dela verktyg i teamet |
| **Version** | Spara releases |
| **Dependencies** | Hantera beroenden |
| **CI/CD** | Bygg och publicera paket |
| **Internal tools** | Privata PyPI-servrar |

Som DevOps-ingenjor maste du forsta:

- **pyproject.toml** for modern packaging
- **pip** och **wheel** for distribution
- **Private PyPI** for interna paket

------------------------------------------------------------

## Projekt struktur

```
mypackage/
+-- pyproject.toml          # Huvudkonfiguration
+-- README.md
+-- LICENSE
+-- src/
|   +-- mypackage/
|       +-- __init__.py
|       +-- core.py
|       +-- utils.py
+-- tests/
|   +-- __init__.py
|   +-- test_core.py
+-- scripts/
    +-- cli.py
```

### __init__.py

```python
# src/mypackage/__init__.py
\"\"\"DevOps automation toolkit.\"\"\"

__version__ = "1.0.0"

from .core import Server, deploy
from .utils import load_config

__all__ = ["Server", "deploy", "load_config"]
```

------------------------------------------------------------

## pyproject.toml

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "devops-toolkit"
version = "1.0.0"
description = "DevOps automation tools"
readme = "README.md"
license = {text = "MIT"}
authors = [
    {name = "DevOps Team", email = "devops@example.com"}
]
requires-python = ">=3.9"
classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
keywords = ["devops", "automation", "deployment"]

dependencies = [
    "requests>=2.28.0",
    "pyyaml>=6.0",
    "click>=8.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "mypy>=1.0",
    "black>=23.0",
]
aws = [
    "boto3>=1.28",
]
azure = [
    "azure-identity>=1.12",
    "azure-mgmt-compute>=30.0",
]

[project.scripts]
devops-cli = "mypackage.cli:main"

[project.urls]
Homepage = "https://github.com/company/devops-toolkit"
Documentation = "https://devops-toolkit.readthedocs.io"
Repository = "https://github.com/company/devops-toolkit"

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-data]
mypackage = ["py.typed", "data/*.yaml"]
```

------------------------------------------------------------

## Bygga och installera

```bash
# Installera build-verktyg
pip install build twine

# Bygg paket
python -m build

# Resultat i dist/
# dist/
#   devops_toolkit-1.0.0-py3-none-any.whl
#   devops_toolkit-1.0.0.tar.gz

# Installera lokalt for utveckling
pip install -e .

# Med optional dependencies
pip install -e ".[dev,aws]"

# Installera fran wheel
pip install dist/devops_toolkit-1.0.0-py3-none-any.whl
```

------------------------------------------------------------

## CLI Entry Points

```python
# src/mypackage/cli.py
import click

@click.group()
@click.version_option()
def main():
    \"\"\"DevOps automation CLI.\"\"\"
    pass

@main.command()
@click.argument("environment")
@click.option("--dry-run", is_flag=True)
def deploy(environment: str, dry_run: bool):
    \"\"\"Deploy to an environment.\"\"\"
    if dry_run:
        click.echo(f"Would deploy to {environment}")
    else:
        click.echo(f"Deploying to {environment}...")

@main.command()
@click.option("--all", is_flag=True, help="Show all servers")
def status(all: bool):
    \"\"\"Show server status.\"\"\"
    click.echo("Server status:")
    # ...

if __name__ == "__main__":
    main()
```

```bash
# Efter installation
devops-cli --version
devops-cli deploy production
devops-cli deploy staging --dry-run
devops-cli status --all
```

------------------------------------------------------------

## Publicering till PyPI

```bash
# Test pa TestPyPI forst
twine upload --repository testpypi dist/*

# Installera fran TestPyPI
pip install --index-url https://test.pypi.org/simple/ devops-toolkit

# Publicera till PyPI
twine upload dist/*

# Med API token (rekommenderat)
# Skapa ~/.pypirc
# [pypi]
# username = __token__
# password = pypi-xxxx...

# Eller med environment variable
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-xxxx...
twine upload dist/*
```

------------------------------------------------------------

## Private PyPI Server

```bash
# Anvand privat index
pip install --index-url https://pypi.company.com/simple/ mypackage

# Bade privat och offentlig
pip install --extra-index-url https://pypi.company.com/simple/ mypackage

# I pip.conf
# [global]
# extra-index-url = https://pypi.company.com/simple/
```

### requirements.txt med privat index

```text
--extra-index-url https://pypi.company.com/simple/

requests>=2.28.0
pyyaml>=6.0
company-internal-lib>=1.0.0
```

------------------------------------------------------------

## Version Management

```python
# src/mypackage/__init__.py
__version__ = "1.0.0"

# Hamta version programmatiskt
from importlib.metadata import version

def get_version():
    return version("devops-toolkit")
```

### Semantic Versioning

```
MAJOR.MINOR.PATCH

1.0.0 - Initial release
1.0.1 - Bug fix
1.1.0 - New feature (backward compatible)
2.0.0 - Breaking change
```

### Automatisk versioning med git tags

```bash
# Tag release
git tag v1.0.0
git push origin v1.0.0

# I CI/CD - hamta version fran tag
VERSION=$(git describe --tags --abbrev=0)
```

------------------------------------------------------------

## CI/CD Pipeline for Publishing

```yaml
# .github/workflows/publish.yml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install build twine

      - name: Build package
        run: python -m build

      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

------------------------------------------------------------

## Praktisk Checklista

```
[ ] pyproject.toml konfigurerad
[ ] src/ layout anvands
[ ] __init__.py med __version__
[ ] README.md med dokumentation
[ ] LICENSE fil
[ ] tests/ med pytest
[ ] Entry points for CLI
[ ] .gitignore (dist/, *.egg-info/)
[ ] CI/CD pipeline for test och publish
[ ] Version uppdaterad innan release
```

------------------------------------------------------------

## Snabbreferens - Packaging

| Uppgift | Kommando |
|---------|----------|
| Bygg | `python -m build` |
| Dev install | `pip install -e .` |
| Upload test | `twine upload --repository testpypi dist/*` |
| Upload prod | `twine upload dist/*` |
| Check | `twine check dist/*` |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Package not found | Fel packages.find | Kolla src/ layout |
| Version exists | Redan publicerad | Bump version |
| Invalid metadata | pyproject.toml fel | Validera med twine check |
| Import error | Circular import | Refaktorera imports |

------------------------------------------------------------

## Key Takeaways

| Punkt | Beskrivning |
|-------|-------------|
| **pyproject.toml** | Modern standard |
| **src/ layout** | Recommended |
| **pip install -e .** | For development |
| **twine** | For upload |
| **Semantic versioning** | MAJOR.MINOR.PATCH |

**Kom ihag:**
- pyproject.toml ar modern standard
- src/ layout forhindrar import-problem
- pip install -e . for development
- Testa pa TestPyPI forst
- Anvand API tokens, aldrig losenord
"""
        },
    ]
}
