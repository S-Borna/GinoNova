"""
Shell/Bash SkillsMap — Complete Bash Mastery for DevOps
========================================================

20 nodes covering everything from basics to production-ready scripting.
Akhilesh-style pedagogy: Hook → Concept → Commands → Pro Tips → Hands-on Task

Block 1 (Nodes 1-5): Fundamentals
Block 2 (Nodes 6-10): I/O & Text Processing
Block 3 (Nodes 11-15): Advanced Techniques
Block 4 (Nodes 16-20): Production Patterns
"""

from typing import Any

# ============================================================================
# BLOCK 1: BASH FUNDAMENTALS (Nodes 1-5)
# ============================================================================

BASH_NODE_01_INTRODUCTION = {
    "id": "bash-01-introduction",
    "title": "Bash Introduction & Script Execution",
    "description": "Master the foundation of shell scripting — from shebang to execution",
    "content": """
# Bash Introduction & Script Execution

> *"The shell is your gateway to Unix power. Master it, and you control the machine."*

---

## 🎯 Why This Matters

Every DevOps engineer spends **hours in the terminal**. Whether you're automating deployments, processing logs, or managing servers — Bash is your primary tool. Understanding how scripts execute is fundamental to writing reliable automation.

**Real scenario:** A deployment script fails silently at 3 AM. Without understanding execution flow, you're debugging blind.

---

## 🧠 Core Concepts

### What is Bash?

**Bash** (Bourne Again SHell) is:
- A **command interpreter** that reads and executes commands
- A **programming language** for automation
- The **default shell** on most Linux distributions and macOS

```bash
# Check your current shell
echo $SHELL

# Check Bash version
bash --version
```

### The Shebang Line

The **shebang** (`#!`) tells the system which interpreter to use:

```bash
#!/bin/bash
# This script will be executed by Bash

#!/usr/bin/env bash
# More portable — finds bash in PATH (recommended)

#!/bin/sh
# POSIX shell — more portable but fewer features
```

**Why `#!/usr/bin/env bash`?**
- Bash might be at `/bin/bash`, `/usr/local/bin/bash`, or elsewhere
- `env` searches PATH and finds the right one
- Essential for cross-platform scripts

### Script Execution Methods

```bash
# Method 1: Direct execution (requires execute permission)
chmod +x script.sh
./script.sh

# Method 2: Explicit interpreter (no permission needed)
bash script.sh

# Method 3: Source (runs in current shell, shares variables)
source script.sh
. script.sh  # Shorthand
```

**Critical difference:**
- `./script.sh` — Runs in a **subshell** (isolated)
- `source script.sh` — Runs in **current shell** (affects your environment)

### Script Structure Best Practice

```bash
#!/usr/bin/env bash
#
# Script: deploy.sh
# Description: Deploy application to production
# Author: Your Name
# Date: 2025-12-03
# Version: 1.0.0
#

set -euo pipefail  # Strict mode (explained later)

# Constants
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly LOG_FILE="/var/log/deploy.log"

# Functions
main() {
    echo "Starting deployment..."
    # Your logic here
}

# Entry point
main "$@"
```

---

## 💻 Essential Commands

```bash
# Create a script
cat > hello.sh << 'EOF'
#!/usr/bin/env bash
echo "Hello, DevOps!"
EOF

# Make executable
chmod +x hello.sh

# Run it
./hello.sh

# Check which shell interprets a script
head -1 script.sh

# Find all bash scripts in a directory
find . -name "*.sh" -type f

# Check script syntax without running
bash -n script.sh

# Debug mode (print commands as executed)
bash -x script.sh
```

---

## 🔥 Pro Tips

### 1. Always Use Strict Mode
```bash
set -euo pipefail
# -e: Exit on error
# -u: Error on undefined variables
# -o pipefail: Catch pipe failures
```

### 2. Get Script Directory Reliably
```bash
# Works even when called from another directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
```

### 3. Use Meaningful Exit Codes
```bash
exit 0  # Success
exit 1  # General error
exit 2  # Misuse of command
exit 126  # Permission denied
exit 127  # Command not found
```

### 4. Make Scripts Self-Documenting
```bash
#!/usr/bin/env bash
#
# Usage: ./script.sh [options] <argument>
#
# Options:
#   -h, --help     Show this help
#   -v, --verbose  Enable verbose output
#   -d, --dry-run  Show what would be done
#
```

---

## ⚠️ Common Pitfalls

| Mistake | Problem | Solution |
|---------|---------|----------|
| `#!/bin/bash` on macOS | macOS has old Bash (3.2) | Use `#!/usr/bin/env bash` |
| Missing shebang | Script may run with wrong interpreter | Always include shebang |
| `source` vs `./` confusion | Variables leak or don't persist | Understand the difference |
| Forgetting `chmod +x` | "Permission denied" error | Always set execute permission |

---

## 🛠️ Hands-on Exercise

### Task: Create a Self-Documenting Script Template

Create a reusable script template that includes:
1. Proper shebang with env
2. Header documentation
3. Strict mode
4. Script directory detection
5. Help function
6. Main entry point

**Expected output structure:**
```bash
#!/usr/bin/env bash
# [Your template here]

show_help() { ... }
main() { ... }
main "$@"
```

**Bonus:** Make your template generate new scripts from itself!

---

## 📚 Deep Dive Resources

- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/)
- [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
- [ShellCheck Wiki](https://www.shellcheck.net/wiki/)
""",
    "xp_reward": 150,
    "estimated_time": "45 minutes",
    "difficulty": "beginner",
    "order_index": 1,
    "tags": ["bash", "shell", "scripting", "fundamentals", "shebang"],
}

BASH_NODE_02_VARIABLES = {
    "id": "bash-02-variables",
    "title": "Variables & Quoting Mastery",
    "description": "Understand variable types, scoping, and the critical art of quoting",
    "content": """
# Variables & Quoting Mastery

> *"In Bash, quoting isn't optional — it's the difference between a working script and a catastrophe."*

---

## 🎯 Why This Matters

**The horror story:** A developer ran `rm -rf $DIR/` where `$DIR` was unset. The command became `rm -rf /` and wiped the server. Understanding variables and quoting prevents disasters.

---

## 🧠 Core Concepts

### Variable Types

```bash
# 1. User Variables (lowercase by convention)
name="DevOps"
count=42

# 2. Environment Variables (UPPERCASE by convention)
export PATH="/usr/local/bin:$PATH"
export DEPLOY_ENV="production"

# 3. Special Variables (built-in)
echo $?   # Exit status of last command
echo $$   # Current script's PID
echo $!   # PID of last background process
echo $#   # Number of arguments
echo $@   # All arguments (as separate words)
echo $*   # All arguments (as single word)
echo $0   # Script name
echo $1   # First argument
```

### Variable Assignment Rules

```bash
# ✅ Correct — no spaces around =
name="value"

# ❌ Wrong — spaces cause errors
name = "value"   # Tries to run 'name' as command
name= "value"    # Sets empty variable, runs 'value'

# Assign command output
current_date=$(date +%Y-%m-%d)
current_date=`date +%Y-%m-%d`  # Old style, avoid

# Assign with default
name=${name:-"default"}  # Use default if unset or empty
name=${name:="default"}  # Set AND use default if unset
```

### The Quoting Trinity

| Quote Type | Behavior | Use Case |
|------------|----------|----------|
| `"double"` | Expands variables, preserves spaces | Most common |
| `'single'` | Literal string, no expansion | Regex, special chars |
| `$'...'` | Interprets escape sequences | Newlines, tabs |
| `` `...` `` | Command substitution (old) | Avoid — use `$()` |

```bash
name="World"

# Double quotes — variable expansion
echo "Hello, $name"        # Hello, World

# Single quotes — literal
echo 'Hello, $name'        # Hello, $name

# ANSI-C quoting — escape sequences
echo $'Line1\\nLine2'      # Line1
                           # Line2

# Command substitution
echo "Today is $(date)"    # Today is Tue Dec 3 ...
```

### Why Quoting Matters

```bash
# The disaster scenario
file="my important file.txt"

# ❌ Without quotes — 3 separate arguments
rm $file           # rm: cannot remove 'my': No such file
                   # rm: cannot remove 'important': No such file
                   # rm: cannot remove 'file.txt': No such file

# ✅ With quotes — single argument
rm "$file"         # Correctly removes "my important file.txt"
```

### Variable Expansion

```bash
name="bash"

# Basic
echo $name           # bash
echo ${name}         # bash (explicit form)

# Length
echo ${#name}        # 4

# Substring
echo ${name:0:2}     # ba (from pos 0, length 2)
echo ${name:2}       # sh (from pos 2 to end)

# Default values
echo ${var:-default}   # "default" if var unset/empty
echo ${var:=default}   # Set var to "default" if unset/empty
echo ${var:+alternate} # "alternate" if var IS set
echo ${var:?error}     # Exit with error if unset/empty

# Substitution
file="document.txt"
echo ${file%.txt}      # document (remove suffix)
echo ${file#doc}       # ument.txt (remove prefix)
echo ${file/txt/pdf}   # document.pdf (replace)
echo ${file//o/O}      # dOcument.txt (replace all)
```

### Read-Only Variables

```bash
# Constants that can't be changed
readonly PI=3.14159
declare -r MAX_RETRIES=3

PI=3.14  # Error: PI: readonly variable
```

---

## 💻 Essential Commands

```bash
# List all environment variables
env
printenv

# Export variable to child processes
export MY_VAR="value"

# Remove variable
unset MY_VAR

# Check if variable is set
if [[ -v MY_VAR ]]; then
    echo "MY_VAR is set"
fi

# Check if variable is empty
if [[ -z "$MY_VAR" ]]; then
    echo "MY_VAR is empty or unset"
fi

# Check if variable is non-empty
if [[ -n "$MY_VAR" ]]; then
    echo "MY_VAR has a value"
fi
```

---

## 🔥 Pro Tips

### 1. Always Quote Variables
```bash
# Even when you think it's safe
echo "$variable"
rm "$file"
cd "$directory"
```

### 2. Use `${var}` for Clarity
```bash
# Ambiguous
echo "$namefiles"  # Is it $name + "files" or $namefiles?

# Clear
echo "${name}files"  # $name followed by "files"
```

### 3. Protect Against Unset Variables
```bash
set -u  # Exit on undefined variable

# Or use defaults
file="${1:-default.txt}"
```

### 4. Use Lowercase for Local Variables
```bash
# Convention: UPPERCASE for environment, lowercase for local
export DATABASE_URL="postgres://..."
local_counter=0
```

---

## ⚠️ Common Pitfalls

| Mistake | Problem | Solution |
|---------|---------|----------|
| `var= value` | Space after `=` | No spaces: `var=value` |
| `$var` in `[[ ]]` | Word splitting | Quote: `"$var"` |
| `export var=val` | Some shells don't support | `var=val; export var` |
| Using `$$` wrong | Gets shell PID, not script | Use `$BASHPID` for subshell |

---

## 🛠️ Hands-on Exercise

### Task: Build a Configuration Loader

Create a script that:
1. Loads configuration from a file or environment
2. Uses default values for missing config
3. Validates required variables
4. Demonstrates proper quoting with filenames containing spaces

```bash
# config.env
DB_HOST=localhost
DB_PORT=5432
# DB_PASSWORD not set — should use default or error

# Your script should:
# - Source config.env if it exists
# - Use defaults: DB_HOST=${DB_HOST:-localhost}
# - Error if required vars missing (like DB_PASSWORD)
# - Handle file paths with spaces
```

**Test with:** Create a file named "my config.env" (with space) and load it correctly.

---

## 📚 Deep Dive Resources

- [Bash Parameter Expansion](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)
- [Quotes and Escaping](https://mywiki.wooledge.org/Quotes)
- [BashFAQ: Quoting](https://mywiki.wooledge.org/BashFAQ/073)
""",
    "xp_reward": 175,
    "estimated_time": "50 minutes",
    "difficulty": "beginner",
    "order_index": 2,
    "tags": ["bash", "variables", "quoting", "environment", "expansion"],
}

BASH_NODE_03_CONTROL_STRUCTURES = {
    "id": "bash-03-control-structures",
    "title": "Control Structures — Conditionals",
    "description": "Master if/elif/else, case statements, and test expressions",
    "content": """
# Control Structures — Conditionals

> *"Code that can't make decisions is just a list of commands. Conditionals give your scripts intelligence."*

---

## 🎯 Why This Matters

Every automation script needs to make decisions:
- Is the server reachable?
- Did the deployment succeed?
- Is the disk usage too high?

Mastering conditionals is essential for writing scripts that **respond** to real-world conditions.

---

## 🧠 Core Concepts

### The If Statement

```bash
# Basic syntax
if condition; then
    commands
fi

# With else
if condition; then
    commands
else
    other_commands
fi

# With elif
if condition1; then
    commands1
elif condition2; then
    commands2
else
    default_commands
fi
```

### Test Commands: `[ ]` vs `[[ ]]`

```bash
# Old style: [ ] (POSIX compatible)
if [ "$name" = "admin" ]; then
    echo "Welcome, admin"
fi

# Modern style: [[ ]] (Bash-specific, recommended)
if [[ "$name" == "admin" ]]; then
    echo "Welcome, admin"
fi
```

**Why prefer `[[ ]]`?**
| Feature | `[ ]` | `[[ ]]` |
|---------|-------|---------|
| Word splitting | Yes (dangerous) | No (safe) |
| Pattern matching | No | Yes (`==`, `!=`) |
| Regex matching | No | Yes (`=~`) |
| Logical operators | `-a`, `-o` | `&&`, `||` |
| Quoting required | Always | Sometimes optional |

### String Comparisons

```bash
# Equality
[[ "$str" == "value" ]]    # Equal
[[ "$str" != "value" ]]    # Not equal

# Empty/non-empty
[[ -z "$str" ]]            # True if empty
[[ -n "$str" ]]            # True if not empty

# Pattern matching (glob)
[[ "$file" == *.txt ]]     # Ends with .txt
[[ "$name" == admin* ]]    # Starts with admin

# Regex matching
[[ "$email" =~ ^[a-z]+@[a-z]+\\.[a-z]+$ ]]
```

### Numeric Comparisons

```bash
# Integer comparisons (use these in [[ ]])
[[ $a -eq $b ]]    # Equal
[[ $a -ne $b ]]    # Not equal
[[ $a -lt $b ]]    # Less than
[[ $a -le $b ]]    # Less than or equal
[[ $a -gt $b ]]    # Greater than
[[ $a -ge $b ]]    # Greater than or equal

# Arithmetic context (alternative)
(( a == b ))       # Equal
(( a != b ))       # Not equal
(( a < b ))        # Less than
(( a <= b ))       # Less than or equal
(( a > b ))        # Greater than
(( a >= b ))       # Greater than or equal
```

### File Tests

```bash
# Existence
[[ -e "$file" ]]    # Exists (any type)
[[ -f "$file" ]]    # Exists and is regular file
[[ -d "$path" ]]    # Exists and is directory
[[ -L "$link" ]]    # Exists and is symlink

# Permissions
[[ -r "$file" ]]    # Readable
[[ -w "$file" ]]    # Writable
[[ -x "$file" ]]    # Executable

# Size
[[ -s "$file" ]]    # Exists and not empty

# Comparisons
[[ "$f1" -nt "$f2" ]]  # f1 newer than f2
[[ "$f1" -ot "$f2" ]]  # f1 older than f2
```

### Logical Operators

```bash
# AND
[[ condition1 && condition2 ]]
[[ -f "$file" && -r "$file" ]]

# OR
[[ condition1 || condition2 ]]
[[ -z "$name" || "$name" == "default" ]]

# NOT
[[ ! condition ]]
[[ ! -d "$dir" ]]

# Combining
[[ (-f "$f" && -r "$f") || "$force" == "true" ]]
```

### Case Statements

```bash
case "$variable" in
    pattern1)
        commands
        ;;
    pattern2|pattern3)
        commands
        ;;
    *)
        default_commands
        ;;
esac

# Real example
case "$1" in
    start)
        start_service
        ;;
    stop)
        stop_service
        ;;
    restart)
        stop_service
        start_service
        ;;
    status)
        show_status
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac
```

### Case with Patterns

```bash
case "$filename" in
    *.tar.gz|*.tgz)
        tar -xzf "$filename"
        ;;
    *.tar.bz2)
        tar -xjf "$filename"
        ;;
    *.zip)
        unzip "$filename"
        ;;
    *.txt|*.log)
        cat "$filename"
        ;;
    *)
        echo "Unknown file type"
        ;;
esac
```

---

## 💻 Essential Commands

```bash
# One-liner if
[[ -f "$file" ]] && echo "File exists"
[[ -f "$file" ]] || echo "File missing"

# Ternary-like pattern
result=$([[ "$condition" ]] && echo "yes" || echo "no")

# Check command success
if command; then
    echo "Command succeeded"
fi

if grep -q "pattern" file.txt; then
    echo "Pattern found"
fi

# Check exit code
command
if [[ $? -eq 0 ]]; then
    echo "Success"
fi
```

---

## 🔥 Pro Tips

### 1. Use `[[` for Safety
```bash
# Even with unquoted variables, [[ is safer
name=""
[[ $name == "" ]]  # Works fine
[ $name == "" ]    # Error: too many arguments
```

### 2. Test Exit Codes Directly
```bash
# ❌ Verbose
if [[ $? -eq 0 ]]; then
    echo "Success"
fi

# ✅ Direct
if command; then
    echo "Success"
fi
```

### 3. Use `-v` to Check If Variable Is Set
```bash
# Bash 4.2+
if [[ -v OPTIONAL_VAR ]]; then
    echo "OPTIONAL_VAR is set (even if empty)"
fi
```

### 4. Arithmetic in Conditions
```bash
# Clean numeric comparisons
if (( count > 10 && count < 100 )); then
    echo "Count is between 10 and 100"
fi
```

---

## ⚠️ Common Pitfalls

| Mistake | Problem | Solution |
|---------|---------|----------|
| `if [ $var = "x" ]` | Fails if var is empty | Use `[[ "$var" == "x" ]]` |
| `if [ $a > $b ]` | `>` is redirection! | Use `-gt` or `(( ))` |
| Space after `[` | `[` is a command | `[ condition ]` needs spaces |
| `=` vs `==` | `=` is POSIX, `==` is Bash | Use `==` in `[[ ]]` |

---

## 🛠️ Hands-on Exercise

### Task: Build a System Health Checker

Create a script that checks:
1. Disk usage (alert if > 80%)
2. Memory usage (alert if > 90%)
3. Service status (check if nginx/apache running)
4. File age (alert if log file older than 24h)

```bash
# Expected output:
# [OK] Disk usage: 45%
# [WARN] Memory usage: 92%
# [OK] nginx is running
# [FAIL] Log file is 3 days old

# Use:
# - Numeric comparisons for percentages
# - File tests for existence
# - Command success checks for services
# - Case statement for output formatting
```

---

## 📚 Deep Dive Resources

- [Bash Conditional Expressions](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html)
- [Test Constructs](https://tldp.org/LDP/abs/html/testconstructs.html)
- [BashFAQ: Test and Conditionals](https://mywiki.wooledge.org/BashFAQ/031)
""",
    "xp_reward": 200,
    "estimated_time": "55 minutes",
    "difficulty": "intermediate",
    "order_index": 3,
    "tags": ["bash", "conditionals", "if", "case", "test", "control-flow"],
}

BASH_NODE_04_LOOPS = {
    "id": "bash-04-loops",
    "title": "Loops — Iteration Mastery",
    "description": "Master for, while, until loops and loop control",
    "content": """
# Loops — Iteration Mastery

> *"Automation is repetition without fatigue. Loops are your tireless workers."*

---

## 🎯 Why This Matters

DevOps work is inherently repetitive:
- Process 1000 log files
- Check status of 50 servers
- Retry a failing deployment 5 times
- Wait for a resource to become available

Loops transform hours of manual work into seconds of script execution.

---

## 🧠 Core Concepts

### The For Loop

```bash
# Iterate over a list
for item in item1 item2 item3; do
    echo "$item"
done

# Iterate over files
for file in *.txt; do
    echo "Processing: $file"
done

# Iterate over command output
for user in $(cat users.txt); do
    echo "User: $user"
done

# C-style for loop
for ((i=0; i<10; i++)); do
    echo "Count: $i"
done

# Range (Bash 3+)
for i in {1..10}; do
    echo "Number: $i"
done

# Range with step
for i in {0..100..10}; do
    echo "Tens: $i"  # 0, 10, 20, ...
done
```

### The While Loop

```bash
# Basic while
counter=0
while [[ $counter -lt 5 ]]; do
    echo "Counter: $counter"
    ((counter++))
done

# Read file line by line (CORRECT way)
while IFS= read -r line; do
    echo "Line: $line"
done < file.txt

# Infinite loop with break
while true; do
    if condition; then
        break
    fi
    sleep 1
done

# Read from command
while IFS= read -r line; do
    echo "$line"
done < <(command)
```

### The Until Loop

```bash
# Run until condition is true (opposite of while)
counter=0
until [[ $counter -ge 5 ]]; do
    echo "Counter: $counter"
    ((counter++))
done

# Wait for service
until curl -s http://localhost:8080/health > /dev/null; do
    echo "Waiting for service..."
    sleep 2
done
echo "Service is up!"
```

### Loop Control

```bash
# break — exit loop immediately
for i in {1..10}; do
    if [[ $i -eq 5 ]]; then
        break
    fi
    echo "$i"
done
# Output: 1 2 3 4

# continue — skip to next iteration
for i in {1..5}; do
    if [[ $i -eq 3 ]]; then
        continue
    fi
    echo "$i"
done
# Output: 1 2 4 5

# break N — break out of N nested loops
for i in {1..3}; do
    for j in {1..3}; do
        if [[ $j -eq 2 ]]; then
            break 2  # Break both loops
        fi
        echo "$i-$j"
    done
done
```

### Iterating Over Arrays

```bash
# Indexed array
servers=("web01" "web02" "db01" "cache01")

for server in "${servers[@]}"; do
    echo "Pinging: $server"
done

# With index
for i in "${!servers[@]}"; do
    echo "Server $i: ${servers[$i]}"
done

# Associative array (Bash 4+)
declare -A config=(
    [host]="localhost"
    [port]="5432"
    [user]="admin"
)

for key in "${!config[@]}"; do
    echo "$key = ${config[$key]}"
done
```

### Looping Over Files Safely

```bash
# ❌ Dangerous — breaks on spaces/special chars
for file in $(ls *.txt); do
    echo "$file"
done

# ✅ Safe — handles all filenames
for file in *.txt; do
    [[ -e "$file" ]] || continue  # Skip if no match
    echo "$file"
done

# ✅ Even safer — null-delimited
while IFS= read -r -d '' file; do
    echo "$file"
done < <(find . -name "*.txt" -print0)
```

---

## 💻 Essential Patterns

### Retry Pattern
```bash
max_retries=5
retry_count=0

while [[ $retry_count -lt $max_retries ]]; do
    if command; then
        echo "Success!"
        break
    fi
    ((retry_count++))
    echo "Retry $retry_count/$max_retries..."
    sleep $((retry_count * 2))  # Exponential backoff
done

if [[ $retry_count -eq $max_retries ]]; then
    echo "Failed after $max_retries attempts"
    exit 1
fi
```

### Progress Indicator
```bash
files=(*.log)
total=${#files[@]}
current=0

for file in "${files[@]}"; do
    ((current++))
    echo -ne "Processing: $current/$total\\r"
    process_file "$file"
done
echo -e "\\nDone!"
```

### Parallel Processing (Simple)
```bash
# Process in background, limit concurrency
max_jobs=4
job_count=0

for file in *.txt; do
    process_file "$file" &
    ((job_count++))

    if [[ $job_count -ge $max_jobs ]]; then
        wait -n  # Wait for any job to finish (Bash 4.3+)
        ((job_count--))
    fi
done
wait  # Wait for remaining jobs
```

### Batch Processing
```bash
# Process items in batches
items=({1..100})
batch_size=10

for ((i=0; i<${#items[@]}; i+=batch_size)); do
    batch=("${items[@]:i:batch_size}")
    echo "Processing batch: ${batch[*]}"
done
```

---

## 🔥 Pro Tips

### 1. Use `while read` for Files, Not `for`
```bash
# ❌ Word splitting issues
for line in $(cat file.txt); do
    echo "$line"
done

# ✅ Preserves lines correctly
while IFS= read -r line; do
    echo "$line"
done < file.txt
```

### 2. Process Substitution for Command Output
```bash
# Read from command output
while IFS= read -r line; do
    echo "$line"
done < <(find . -name "*.sh")
```

### 3. Loop Variable Scope
```bash
# Variables from while loop persist
last_line=""
while IFS= read -r line; do
    last_line="$line"
done < file.txt
echo "Last: $last_line"  # Works!

# BUT piped while runs in subshell
cat file.txt | while IFS= read -r line; do
    last_line="$line"
done
echo "Last: $last_line"  # Empty! (subshell)
```

### 4. Avoid Infinite Loops
```bash
# Always have an exit condition
timeout=60
elapsed=0

while ! service_ready; do
    if [[ $elapsed -ge $timeout ]]; then
        echo "Timeout waiting for service"
        exit 1
    fi
    sleep 1
    ((elapsed++))
done
```

---

## ⚠️ Common Pitfalls

| Mistake | Problem | Solution |
|---------|---------|----------|
| `for f in $(ls)` | Word splitting | `for f in *` |
| Piped while | Subshell loses variables | Use `< <(command)` |
| `for i in {1..$n}` | Brace expansion before variable | Use C-style: `for ((i=1; i<=n; i++))` |
| No `[[ -e "$f" ]]` check | Glob expands to literal if no match | Add existence check |

---

## 🛠️ Hands-on Exercise

### Task: Build a Log Processor

Create a script that:
1. Finds all `.log` files in `/var/log` (or current dir for testing)
2. Processes each file:
   - Count lines with "ERROR"
   - Count lines with "WARN"
   - Get file size
3. Shows progress (X/Y files processed)
4. Outputs summary table
5. Retries failed operations up to 3 times

```bash
# Expected output:
# Processing logs... [1/5]
# Processing logs... [2/5]
# ...
#
# Summary:
# FILE                 ERRORS  WARNINGS  SIZE
# app.log              15      42        1.2MB
# system.log           3       18        456KB
# ...
#
# Total: 5 files, 18 errors, 60 warnings
```

---

## 📚 Deep Dive Resources

- [Bash Loops](https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html)
- [BashFAQ: Process Lines](https://mywiki.wooledge.org/BashFAQ/001)
- [Wooledge: Don't Read Lines With For](https://mywiki.wooledge.org/DontReadLinesWithFor)
""",
    "xp_reward": 200,
    "estimated_time": "55 minutes",
    "difficulty": "intermediate",
    "order_index": 4,
    "tags": ["bash", "loops", "for", "while", "until", "iteration"],
}

BASH_NODE_05_FUNCTIONS = {
    "id": "bash-05-functions",
    "title": "Functions — Modular Scripting",
    "description": "Build reusable, maintainable code with functions",
    "content": """
# Functions — Modular Scripting

> *"A 1000-line script is a nightmare. 50 well-named functions are a toolkit."*

---

## 🎯 Why This Matters

Production scripts grow. Without functions:
- Code gets duplicated
- Changes require editing multiple places
- Testing becomes impossible
- Debugging is a nightmare

Functions transform scripts into maintainable, testable, reusable code.

---

## 🧠 Core Concepts

### Function Definition

```bash
# Style 1: Modern (recommended)
function_name() {
    commands
}

# Style 2: With 'function' keyword
function function_name {
    commands
}

# Style 3: One-liner
greet() { echo "Hello, $1!"; }
```

### Calling Functions

```bash
# Define
say_hello() {
    echo "Hello!"
}

# Call (no parentheses!)
say_hello

# With arguments
greet() {
    echo "Hello, $1!"
}

greet "DevOps"  # Hello, DevOps!
```

### Function Arguments

```bash
# Arguments are positional: $1, $2, $3, ...
create_user() {
    local username="$1"
    local email="$2"
    local role="${3:-user}"  # Default value

    echo "Creating user: $username"
    echo "Email: $email"
    echo "Role: $role"
}

create_user "john" "john@example.com" "admin"
create_user "jane" "jane@example.com"  # role defaults to "user"

# All arguments
process_files() {
    echo "Processing ${#} files..."
    for file in "$@"; do
        echo "  - $file"
    done
}

process_files file1.txt file2.txt file3.txt
```

### Return Values

```bash
# Return status (0-255)
is_valid_ip() {
    local ip="$1"
    if [[ "$ip" =~ ^[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+$ ]]; then
        return 0  # Success (true)
    else
        return 1  # Failure (false)
    fi
}

if is_valid_ip "192.168.1.1"; then
    echo "Valid IP"
fi

# Return data via stdout
get_timestamp() {
    date +%Y%m%d_%H%M%S
}

timestamp=$(get_timestamp)
echo "Timestamp: $timestamp"

# Return multiple values
get_user_info() {
    echo "john"      # Line 1: username
    echo "John Doe"  # Line 2: full name
    echo "admin"     # Line 3: role
}

# Capture multiple values
{
    read -r username
    read -r fullname
    read -r role
} < <(get_user_info)

echo "User: $username ($fullname) - $role"
```

### Local Variables

```bash
# Without local — variable pollutes global scope
bad_function() {
    result="I'm global now!"
}

bad_function
echo "$result"  # "I'm global now!" — leaked!

# With local — variable stays in function
good_function() {
    local result="I'm local!"
    echo "$result"
}

good_function
echo "$result"  # Empty — properly scoped
```

### Function Libraries

```bash
# lib/logging.sh
log_info() {
    echo "[INFO] $(date +%H:%M:%S) $*"
}

log_error() {
    echo "[ERROR] $(date +%H:%M:%S) $*" >&2
}

log_debug() {
    [[ "${DEBUG:-}" == "true" ]] && echo "[DEBUG] $(date +%H:%M:%S) $*"
}

# main.sh
source lib/logging.sh

log_info "Starting deployment"
log_error "Something went wrong"
DEBUG=true log_debug "Verbose output"
```

### Advanced Patterns

```bash
# Function with named parameters (using arrays)
deploy() {
    local -A args=(
        [env]="staging"
        [version]="latest"
        [dry_run]="false"
    )

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --env=*) args[env]="${1#*=}" ;;
            --version=*) args[version]="${1#*=}" ;;
            --dry-run) args[dry_run]="true" ;;
        esac
        shift
    done

    echo "Deploying version ${args[version]} to ${args[env]}"
    [[ "${args[dry_run]}" == "true" ]] && echo "(dry run)"
}

deploy --env=production --version=1.2.3 --dry-run

# Higher-order function (function that takes function)
retry() {
    local max_attempts="$1"
    local cmd="$2"
    shift 2

    local attempt=1
    until "$cmd" "$@"; do
        if [[ $attempt -ge $max_attempts ]]; then
            return 1
        fi
        echo "Attempt $attempt failed, retrying..."
        ((attempt++))
        sleep 1
    done
}

check_server() {
    curl -s "$1" > /dev/null
}

retry 5 check_server "http://localhost:8080"
```

---

## 💻 Essential Commands

```bash
# List all functions
declare -F

# Show function definition
declare -f function_name

# Export function for subshells
export -f function_name

# Unset function
unset -f function_name

# Check if function exists
if declare -f my_function > /dev/null; then
    echo "Function exists"
fi
```

---

## 🔥 Pro Tips

### 1. Always Use `local`
```bash
process_data() {
    local input="$1"
    local result=""
    # ... process ...
    echo "$result"
}
```

### 2. Validate Arguments
```bash
create_backup() {
    local source="${1:?Source directory required}"
    local dest="${2:?Destination required}"

    [[ -d "$source" ]] || { echo "Source not found"; return 1; }
    # ...
}
```

### 3. Document Functions
```bash
# Create a user account
#
# Usage: create_user <username> <email> [role]
#
# Arguments:
#   username  - Login name (required)
#   email     - Email address (required)
#   role      - User role (default: user)
#
# Returns:
#   0 on success, 1 on failure
#
create_user() {
    local username="${1:?Username required}"
    local email="${2:?Email required}"
    local role="${3:-user}"
    # ...
}
```

### 4. Use Meaningful Return Codes
```bash
readonly E_SUCCESS=0
readonly E_INVALID_ARG=1
readonly E_NOT_FOUND=2
readonly E_PERMISSION=3

find_user() {
    local username="$1"

    [[ -z "$username" ]] && return $E_INVALID_ARG

    if grep -q "^$username:" /etc/passwd; then
        return $E_SUCCESS
    else
        return $E_NOT_FOUND
    fi
}
```

---

## ⚠️ Common Pitfalls

| Mistake | Problem | Solution |
|---------|---------|----------|
| Missing `local` | Variables leak globally | Always use `local` |
| `return` vs `exit` | `exit` terminates script | Use `return` in functions |
| Calling with `()` | `func()` redefines function! | Call as `func` |
| Quoting `$@` | Word splitting | Use `"$@"` |

---

## 🛠️ Hands-on Exercise

### Task: Build a Logging Library

Create `lib/logger.sh` with:

1. **Log levels:** DEBUG, INFO, WARN, ERROR, FATAL
2. **Functions:**
   - `log_debug`, `log_info`, `log_warn`, `log_error`, `log_fatal`
   - `set_log_level` — control verbosity
   - `set_log_file` — redirect to file
3. **Features:**
   - Colored output (green=INFO, yellow=WARN, red=ERROR)
   - Timestamp in each message
   - Function name and line number in DEBUG
   - `log_fatal` should exit script

```bash
# Usage example:
source lib/logger.sh

set_log_level INFO
set_log_file "/var/log/myapp.log"

log_info "Application starting"
log_debug "This won't show (level is INFO)"
log_error "Something went wrong"
log_fatal "Critical failure"  # Exits script
```

---

## 📚 Deep Dive Resources

- [Bash Functions](https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html)
- [BashFAQ: Functions](https://mywiki.wooledge.org/BashFAQ/024)
- [Google Shell Style Guide: Functions](https://google.github.io/styleguide/shellguide.html#s7-naming-conventions)
""",
    "xp_reward": 200,
    "estimated_time": "60 minutes",
    "difficulty": "intermediate",
    "order_index": 5,
    "tags": ["bash", "functions", "modular", "libraries", "scope"],
}


# ============================================================================
# BLOCK 2: I/O & TEXT PROCESSING (Nodes 6-10)
# ============================================================================

BASH_NODE_06_REDIRECTION = {
    "id": "bash-06-redirection",
    "title": "Input/Output Redirection",
    "description": "Master stdin, stdout, stderr and the power of pipes",
    "content": """
# Input/Output Redirection

> *"In Unix, everything is a file — including your input and output streams."*

---

## 🎯 Why This Matters

Redirection is what makes Unix powerful. It lets you:
- Chain commands together
- Process data without temporary files
- Log output and errors separately
- Build complex pipelines from simple tools

---

## 🧠 Core Concepts

### The Three Standard Streams

| Stream | File Descriptor | Default | Purpose |
|--------|-----------------|---------|---------|
| stdin | 0 | Keyboard | Input |
| stdout | 1 | Terminal | Normal output |
| stderr | 2 | Terminal | Error messages |

### Output Redirection

```bash
# Redirect stdout to file (overwrite)
command > file.txt
echo "Hello" > output.txt

# Redirect stdout to file (append)
command >> file.txt
echo "World" >> output.txt

# Redirect stderr to file
command 2> errors.txt

# Redirect both stdout and stderr
command > output.txt 2> errors.txt

# Redirect both to same file
command > all.txt 2>&1
command &> all.txt  # Bash shorthand

# Discard output
command > /dev/null
command 2> /dev/null
command &> /dev/null  # Discard all
```

### Input Redirection

```bash
# Read from file
command < input.txt
sort < names.txt

# Combine input and output
sort < unsorted.txt > sorted.txt
```

### Pipes

```bash
# Send stdout of cmd1 to stdin of cmd2
cmd1 | cmd2

# Chain multiple commands
cat log.txt | grep ERROR | sort | uniq -c

# Common patterns
ps aux | grep nginx
ls -la | head -10
history | tail -20
```

### File Descriptor Manipulation

```bash
# Duplicate file descriptors
exec 3>&1  # Save stdout to fd 3
exec 1>file.txt  # Redirect stdout to file
echo "To file"
exec 1>&3  # Restore stdout
echo "To terminal"

# Close file descriptor
exec 3>&-
```

---

## 💻 Essential Patterns

```bash
# Separate stdout and stderr
./script.sh > output.log 2> error.log

# Stderr to stdout, then both to file
./script.sh 2>&1 | tee all.log

# Process stderr only
./script.sh 2>&1 >/dev/null | grep "ERROR"

# Swap stdout and stderr
./script.sh 3>&1 1>&2 2>&3
```

---

## 🔥 Pro Tips

### 1. Use `tee` for Logging + Display
```bash
command | tee output.log  # Show AND save
command | tee -a output.log  # Append
```

### 2. PIPESTATUS for Pipeline Errors
```bash
cmd1 | cmd2 | cmd3
echo "${PIPESTATUS[@]}"  # Exit codes of all commands
```

---

## 🛠️ Hands-on Exercise

Create a log analyzer that:
1. Reads from stdin or file
2. Separates errors to `errors.log`
3. Shows summary to terminal
4. Saves full output to `full.log`
""",
    "xp_reward": 175,
    "estimated_time": "45 minutes",
    "difficulty": "intermediate",
    "order_index": 6,
    "tags": ["bash", "redirection", "pipes", "stdin", "stdout", "stderr"],
}

BASH_NODE_07_HERE_DOCS = {
    "id": "bash-07-here-docs",
    "title": "Here Documents & Here Strings",
    "description": "Multi-line input and inline document generation",
    "content": """
# Here Documents & Here Strings

> *"When echo isn't enough, here documents let you embed entire files in your scripts."*

---

## 🎯 Why This Matters

Here documents are essential for:
- Generating config files dynamically
- Embedding SQL queries in scripts
- Creating multi-line messages
- SSH command execution

---

## 🧠 Core Concepts

### Here Documents

```bash
# Basic syntax
cat << EOF
This is a multi-line
document that will be
sent to cat's stdin.
EOF

# With variable expansion
name="DevOps"
cat << EOF
Hello, $name!
Today is $(date)
EOF

# Without variable expansion (quoted delimiter)
cat << 'EOF'
Variables like $name won't expand
Commands like $(date) won't run
EOF

# Indented (use <<- with tabs)
if true; then
    cat <<- EOF
	This text can be indented
	with tabs (not spaces)
	EOF
fi
```

### Here Strings

```bash
# Single line input
grep "pattern" <<< "search in this string"

# Variable as input
data="line1
line2
line3"
wc -l <<< "$data"

# Command substitution
bc <<< "2 + 2"
```

### Practical Examples

```bash
# Generate config file
cat > /etc/app.conf << EOF
host=$DB_HOST
port=$DB_PORT
user=$DB_USER
EOF

# MySQL query
mysql -u root << EOF
CREATE DATABASE myapp;
GRANT ALL ON myapp.* TO 'appuser'@'localhost';
EOF

# SSH remote commands
ssh user@server << 'EOF'
cd /app
git pull
./restart.sh
EOF
```

---

## 🔥 Pro Tips

### 1. Use for Multi-line Variables
```bash
read -r -d '' USAGE << 'EOF'
Usage: script.sh [options]
  -h  Show help
  -v  Verbose mode
EOF
echo "$USAGE"
```

### 2. Combine with Redirection
```bash
cat << EOF > config.yml
server:
  host: localhost
  port: 8080
EOF
```

---

## 🛠️ Hands-on Exercise

Create a script that generates:
1. An nginx config file
2. A systemd service file
3. A Docker compose file

All using here documents with variable substitution.
""",
    "xp_reward": 150,
    "estimated_time": "35 minutes",
    "difficulty": "intermediate",
    "order_index": 7,
    "tags": ["bash", "here-document", "here-string", "templating"],
}

BASH_NODE_08_STRINGS = {
    "id": "bash-08-strings",
    "title": "String Manipulation",
    "description": "Substring extraction, replacement, and case conversion",
    "content": """
# String Manipulation

> *"Bash string operations eliminate the need for sed and awk in 80% of cases."*

---

## 🎯 Why This Matters

Parsing filenames, extracting data, formatting output — string manipulation is everywhere in DevOps scripting.

---

## 🧠 Core Concepts

### String Length

```bash
str="Hello, World!"
echo ${#str}  # 13
```

### Substring Extraction

```bash
str="Hello, World!"

# From position (0-indexed)
echo ${str:0:5}   # Hello
echo ${str:7}     # World!
echo ${str: -6}   # World! (note space before -)
echo ${str: -6:5} # World
```

### Search and Replace

```bash
file="document.txt"

# Remove shortest match from start
echo ${file#*.}    # txt

# Remove longest match from start
echo ${file##*.}   # txt (same here)

# Remove shortest match from end
echo ${file%.*}    # document

# Remove longest match from end
echo ${file%%.*}   # document (same here)

# Replace first occurrence
str="hello hello"
echo ${str/hello/hi}   # hi hello

# Replace all occurrences
echo ${str//hello/hi}  # hi hi

# Replace at start
echo ${str/#hello/hi}  # hi hello

# Replace at end
echo ${str/%hello/hi}  # hello hi
```

### Case Conversion (Bash 4+)

```bash
str="Hello World"

# Lowercase
echo ${str,,}   # hello world
echo ${str,}    # hello World (first char only)

# Uppercase
echo ${str^^}   # HELLO WORLD
echo ${str^}    # Hello World (first char only)
```

### Default Values

```bash
# Use default if unset/empty
echo ${var:-default}

# Set and use default
echo ${var:=default}

# Error if unset
echo ${var:?Variable required}

# Use alternate if set
echo ${var:+alternate}
```

---

## 💻 Essential Patterns

```bash
# Extract filename from path
path="/var/log/app.log"
filename=${path##*/}  # app.log
dirname=${path%/*}    # /var/log

# Change file extension
file="data.txt"
echo ${file%.txt}.csv  # data.csv

# Extract between delimiters
str="[INFO] Message here"
temp=${str#*] }  # Message here
```

---

## 🛠️ Hands-on Exercise

Create functions for:
1. `basename` replacement
2. `dirname` replacement
3. Extension changer
4. Slug generator (lowercase, replace spaces with dashes)
""",
    "xp_reward": 175,
    "estimated_time": "45 minutes",
    "difficulty": "intermediate",
    "order_index": 8,
    "tags": ["bash", "strings", "manipulation", "substring", "replace"],
}

BASH_NODE_09_ARRAYS = {
    "id": "bash-09-arrays",
    "title": "Arrays — Indexed & Associative",
    "description": "Store and manipulate collections of data",
    "content": """
# Arrays — Indexed & Associative

> *"When you need more than one value, arrays are your friend."*

---

## 🎯 Why This Matters

Arrays let you:
- Store lists of servers, files, or options
- Process batch operations
- Build configuration structures
- Return multiple values from functions

---

## 🧠 Core Concepts

### Indexed Arrays

```bash
# Declaration
servers=("web01" "web02" "db01")
declare -a servers=("web01" "web02" "db01")

# Access elements
echo ${servers[0]}   # web01
echo ${servers[1]}   # web02
echo ${servers[-1]}  # db01 (last element, Bash 4.3+)

# All elements
echo ${servers[@]}   # web01 web02 db01
echo ${servers[*]}   # web01 web02 db01

# Length
echo ${#servers[@]}  # 3

# Indices
echo ${!servers[@]}  # 0 1 2

# Add elements
servers+=("cache01")
servers[10]="monitor"  # Sparse array OK

# Remove element
unset servers[1]
```

### Associative Arrays (Bash 4+)

```bash
# Must declare first
declare -A config

# Assignment
config[host]="localhost"
config[port]="5432"
config[user]="admin"

# Or inline
declare -A config=(
    [host]="localhost"
    [port]="5432"
    [user]="admin"
)

# Access
echo ${config[host]}

# All keys
echo ${!config[@]}  # host port user

# All values
echo ${config[@]}

# Check if key exists
if [[ -v config[host] ]]; then
    echo "Host is set"
fi
```

### Iteration

```bash
# Indexed array
for server in "${servers[@]}"; do
    echo "Server: $server"
done

# With index
for i in "${!servers[@]}"; do
    echo "$i: ${servers[$i]}"
done

# Associative array
for key in "${!config[@]}"; do
    echo "$key = ${config[$key]}"
done
```

### Array Operations

```bash
# Slice
arr=(a b c d e)
echo ${arr[@]:1:3}  # b c d

# Copy
new_arr=("${arr[@]}")

# Merge
combined=("${arr1[@]}" "${arr2[@]}")

# Search
if [[ " ${arr[*]} " =~ " value " ]]; then
    echo "Found"
fi
```

---

## 🔥 Pro Tips

### 1. Quote Array Expansions
```bash
# ✅ Preserves elements with spaces
for item in "${array[@]}"; do

# ❌ Word splitting breaks items
for item in ${array[@]}; do
```

### 2. Read File into Array
```bash
mapfile -t lines < file.txt
# or
readarray -t lines < file.txt
```

---

## 🛠️ Hands-on Exercise

Build a server inventory system:
1. Store servers in an array
2. Store config per server (associative array)
3. Functions: add_server, remove_server, list_servers
4. Iterate and check status of each
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "intermediate",
    "order_index": 9,
    "tags": ["bash", "arrays", "indexed", "associative", "collections"],
}

BASH_NODE_10_REGEX = {
    "id": "bash-10-regex",
    "title": "Regular Expressions in Bash",
    "description": "Pattern matching with =~ operator and grep integration",
    "content": """
# Regular Expressions in Bash

> *"Regex is the Swiss Army knife of text processing. Master it once, use it everywhere."*

---

## 🎯 Why This Matters

Regular expressions are essential for:
- Validating input (emails, IPs, dates)
- Extracting data from logs
- Parsing structured text
- Search and replace operations

---

## 🧠 Core Concepts

### The =~ Operator

```bash
# Basic matching
if [[ "$string" =~ pattern ]]; then
    echo "Match!"
fi

# Email validation
email="user@example.com"
pattern='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
if [[ "$email" =~ $pattern ]]; then
    echo "Valid email"
fi

# IP address
ip="192.168.1.1"
pattern='^[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+$'
if [[ "$ip" =~ $pattern ]]; then
    echo "Looks like an IP"
fi
```

### Capture Groups

```bash
# BASH_REMATCH contains matches
str="Error: code 404 at line 25"

pattern='code ([0-9]+) at line ([0-9]+)'
if [[ "$str" =~ $pattern ]]; then
    echo "Full match: ${BASH_REMATCH[0]}"
    echo "Error code: ${BASH_REMATCH[1]}"  # 404
    echo "Line: ${BASH_REMATCH[2]}"        # 25
fi
```

### Common Patterns

```bash
# Date (YYYY-MM-DD)
pattern='^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
[[ "$date" =~ $pattern ]]

# Semantic version
pattern='^v?([0-9]+)\\.([0-9]+)\\.([0-9]+)$'
[[ "$ver" =~ $pattern ]]

# UUID
pattern='^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
[[ "$id" =~ $pattern ]]

# URL
pattern='^https?://[a-zA-Z0-9.-]+(/.*)?$'
[[ "$url" =~ $pattern ]]
```

### Regex with grep

```bash
# Basic regex
grep "pattern" file.txt

# Extended regex (-E)
grep -E "error|warning|critical" log.txt

# Case insensitive
grep -i "error" log.txt

# Only matching part
grep -oE '[0-9]+' file.txt

# Count matches
grep -c "pattern" file.txt

# With line numbers
grep -n "pattern" file.txt
```

### Practical Examples

```bash
# Extract all IPs from log
grep -oE '[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}' access.log

# Find all email addresses
grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}' file.txt

# Match log timestamps
grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}' app.log
```

---

## 🔥 Pro Tips

### 1. Store Regex in Variable
```bash
# Avoids quoting issues
pattern='^[0-9]+$'
if [[ "$input" =~ $pattern ]]; then
    echo "Is a number"
fi
```

### 2. Negate Match
```bash
if [[ ! "$str" =~ pattern ]]; then
    echo "Does not match"
fi
```

---

## 🛠️ Hands-on Exercise

Create a log parser that:
1. Validates log format
2. Extracts timestamp, level, message
3. Filters by log level
4. Counts occurrences per hour
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "intermediate",
    "order_index": 10,
    "tags": ["bash", "regex", "pattern-matching", "grep", "validation"],
}


# ============================================================================
# BLOCK 4: ADVANCED TECHNIQUES (Nodes 11-13)
# ============================================================================

BASH_NODE_11_ERROR_HANDLING = {
    "id": "bash-11-error-handling",
    "title": "Error Handling & Exit Codes",
    "description": "Build robust scripts that handle failures gracefully",
    "content": """
# Error Handling & Exit Codes

> *"A script that ignores errors is a time bomb waiting to explode."*

---

## 🎯 Why This Matters

Production scripts face failures:
- Network timeouts
- Missing files
- Permission denied
- Full disks

Without proper error handling, scripts fail silently or cause cascading damage.

---

## 🧠 Core Concepts

### Exit Codes

```bash
# Every command returns an exit code
command
echo $?  # 0 = success, non-zero = failure

# Standard exit codes
# 0   - Success
# 1   - General error
# 2   - Misuse of command
# 126 - Permission denied
# 127 - Command not found
# 128 - Invalid exit argument
# 130 - Ctrl+C
# 137 - SIGKILL (kill -9)

# Set your own exit code
exit 0    # Success
exit 1    # Error
```

### Strict Mode

```bash
#!/usr/bin/env bash
set -euo pipefail

# -e  Exit immediately on error
# -u  Treat unset variables as error
# -o pipefail  Pipeline fails if any command fails

# More options
set -E  # ERR trap inherited by functions
set -x  # Debug mode (print commands)
```

### The trap Command

```bash
# Run cleanup on exit
cleanup() {
    rm -f "$temp_file"
    echo "Cleaned up"
}
trap cleanup EXIT

# Handle specific signals
trap 'echo "Interrupted!"' INT
trap 'echo "Terminated!"' TERM

# Handle errors
trap 'echo "Error on line $LINENO"' ERR

# Comprehensive error handler
error_handler() {
    local exit_code=$?
    local line_no=$1
    echo "Error $exit_code at line $line_no"
    exit $exit_code
}
trap 'error_handler $LINENO' ERR
```

### Error Checking Patterns

```bash
# Check command success
if ! command; then
    echo "Command failed"
    exit 1
fi

# Or with ||
command || { echo "Failed"; exit 1; }

# Check file exists
[[ -f "$file" ]] || { echo "File not found: $file"; exit 1; }

# Validate variables
: "${REQUIRED_VAR:?Variable REQUIRED_VAR is not set}"
```

### Try-Catch Pattern

```bash
# Bash doesn't have try-catch, but we can simulate
try() {
    set +e
    "$@"
    local exit_code=$?
    set -e
    return $exit_code
}

if try risky_command; then
    echo "Success"
else
    echo "Failed with code $?"
fi
```

---

## 💻 Essential Patterns

```bash
# Cleanup temporary files
temp_file=$(mktemp)
trap 'rm -f "$temp_file"' EXIT

# Log errors to file
exec 2> >(tee -a error.log >&2)

# Retry with backoff
retry() {
    local max=5 delay=1
    local i
    for ((i=1; i<=max; i++)); do
        if "$@"; then return 0; fi
        echo "Attempt $i failed, waiting ${delay}s..."
        sleep $delay
        ((delay*=2))
    done
    return 1
}
```

---

## 🔥 Pro Tips

### 1. Always Use Strict Mode
```bash
set -euo pipefail
```

### 2. Create Error Function
```bash
die() {
    echo "ERROR: $*" >&2
    exit 1
}
```

### 3. Check Dependencies Early
```bash
for cmd in curl jq docker; do
    command -v "$cmd" >/dev/null || die "$cmd required"
done
```

---

## 🛠️ Hands-on Exercise

Create a deployment script with:
1. Strict mode enabled
2. Cleanup trap for temp files
3. Error handler with line numbers
4. Dependency check at start
5. Retry logic for network operations
""",
    "xp_reward": 225,
    "estimated_time": "55 minutes",
    "difficulty": "intermediate",
    "order_index": 11,
    "tags": ["bash", "error-handling", "exit-codes", "trap", "robust"],
}

BASH_NODE_12_DEBUGGING = {
    "id": "bash-12-debugging",
    "title": "Debugging Bash Scripts",
    "description": "Tools and techniques to find and fix script bugs",
    "content": """
# Debugging Bash Scripts

> *"The best debugger is a clear head and well-placed echo statements... but bash has better tools."*

---

## 🎯 Why This Matters

Complex scripts fail in subtle ways. Debugging skills help you:
- Find bugs quickly
- Understand script flow
- Trace variable changes
- Identify performance issues

---

## 🧠 Core Concepts

### Debug Mode (set -x)

```bash
# Enable debug output
set -x  # Print each command before execution

# Disable debug output
set +x

# Run script in debug mode
bash -x script.sh

# Debug specific section
set -x
problematic_code
set +x
```

### Custom Debug Output

```bash
# PS4 controls debug prefix
export PS4='+ ${BASH_SOURCE}:${LINENO}: ${FUNCNAME[0]:+${FUNCNAME[0]}(): }'

# Now debug shows file:line:function
bash -x script.sh
# Output: + script.sh:10: main(): some_command
```

### Debug Logging

```bash
# Debug function
DEBUG=${DEBUG:-false}

debug() {
    [[ "$DEBUG" == true ]] && echo "[DEBUG] $*" >&2
}

# Usage
DEBUG=true ./script.sh

debug "Variable x = $x"
debug "Entering function process_file"
```

### Verbose Mode

```bash
# Different from debug - shows what's happening
set -v  # Print lines as read

# Combine for maximum info
set -xv
```

### Using printf for Debugging

```bash
# Better than echo for debugging
printf "Variable: [%s]\\n" "$var"
printf "Array: [%s]\\n" "${array[@]}"

# Show hidden characters
printf "%q\\n" "$string_with_special_chars"

# Hex dump
echo -n "$var" | xxd
```

### Shellcheck

```bash
# Static analysis tool
shellcheck script.sh

# Integrate with editor
# Shows warnings like:
# SC2086: Double quote to prevent globbing
# SC2046: Quote to prevent word splitting
```

### Breakpoint Debugging

```bash
# Pause execution
read -p "Press Enter to continue..."

# Conditional breakpoint
if [[ "$DEBUG_BREAK" == true ]]; then
    echo "Breakpoint: x=$x, y=$y"
    read -p "Continue?"
fi

# Interactive debugging
trap 'read -p "[$BASH_SOURCE:$LINENO] $BASH_COMMAND?"' DEBUG
```

---

## 💻 Essential Patterns

```bash
# Log function with levels
log() {
    local level=$1; shift
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] [$level] $*" >&2
}

log INFO "Starting process"
log ERROR "Something went wrong"

# Trace function calls
trace_call() {
    echo "TRACE: ${FUNCNAME[1]} called from ${FUNCNAME[2]:-main}"
}

# Memory usage
debug_memory() {
    ps -o rss= -p $$
}
```

---

## 🔥 Pro Tips

### 1. Use Shellcheck Always
```bash
# Add to your workflow
shellcheck *.sh
```

### 2. Debug Subshells
```bash
# Subshells inherit -x
set -x
(
    subshell_command  # This is traced too
)
```

### 3. Debug Specific Functions
```bash
my_function() {
    local debug_this=true
    [[ "$debug_this" == true ]] && set -x
    # function code
    [[ "$debug_this" == true ]] && set +x
}
```

---

## 🛠️ Hands-on Exercise

Create a debug toolkit:
1. Debug logging with levels
2. Custom PS4 with timestamps
3. Function tracer
4. Variable inspector
5. Performance timer
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "intermediate",
    "order_index": 12,
    "tags": ["bash", "debugging", "troubleshooting", "shellcheck", "trace"],
}

BASH_NODE_13_ARGUMENTS = {
    "id": "bash-13-arguments",
    "title": "Script Arguments & getopts",
    "description": "Parse command-line arguments like a pro",
    "content": """
# Script Arguments & getopts

> *"A script without argument handling is a script you'll rewrite next week."*

---

## 🎯 Why This Matters

Good CLI design makes scripts:
- User-friendly
- Self-documenting
- Flexible and reusable
- Professional

---

## 🧠 Core Concepts

### Positional Arguments

```bash
# Access arguments
echo "Script: $0"
echo "First arg: $1"
echo "Second arg: $2"
echo "All args: $@"
echo "Arg count: $#"

# Shift arguments
shift     # Remove $1, $2 becomes $1
shift 2   # Remove first 2 arguments
```

### Basic Argument Parsing

```bash
#!/usr/bin/env bash

# Simple pattern
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            show_help
            exit 0
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -f|--file)
            FILE="$2"
            shift 2
            ;;
        --)
            shift
            break
            ;;
        -*)
            echo "Unknown option: $1"
            exit 1
            ;;
        *)
            ARGS+=("$1")
            shift
            ;;
    esac
done
```

### getopts (Built-in)

```bash
#!/usr/bin/env bash

usage() {
    echo "Usage: $0 [-h] [-v] [-f file] [-n count] arg1 [arg2...]"
}

# Options: h=help, v=verbose, f:=file (requires arg), n:=number
while getopts ":hvf:n:" opt; do
    case $opt in
        h)
            usage
            exit 0
            ;;
        v)
            VERBOSE=true
            ;;
        f)
            FILE="$OPTARG"
            ;;
        n)
            COUNT="$OPTARG"
            ;;
        \\?)
            echo "Invalid option: -$OPTARG"
            exit 1
            ;;
        :)
            echo "Option -$OPTARG requires an argument"
            exit 1
            ;;
    esac
done

# Shift past options
shift $((OPTIND - 1))

# Remaining args in $@
echo "Remaining args: $@"
```

### Long Options Pattern

```bash
# getopts doesn't support long options natively
# Use this pattern:

while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            usage; exit 0 ;;
        -v|--verbose)
            VERBOSE=true; shift ;;
        -f|--file)
            FILE="${2:?--file requires argument}"; shift 2 ;;
        --file=*)
            FILE="${1#*=}"; shift ;;
        --)
            shift; break ;;
        -*)
            die "Unknown option: $1" ;;
        *)
            break ;;
    esac
done
```

### Validation

```bash
# Required argument
[[ -z "$FILE" ]] && die "Error: --file is required"

# File must exist
[[ -f "$FILE" ]] || die "File not found: $FILE"

# Must be a number
[[ "$COUNT" =~ ^[0-9]+$ ]] || die "Count must be a number"

# Must be in allowed values
case "$ENV" in
    dev|staging|prod) ;;
    *) die "Invalid environment: $ENV" ;;
esac
```

---

## 💻 Complete Example

```bash
#!/usr/bin/env bash
set -euo pipefail

readonly SCRIPT_NAME=$(basename "$0")
readonly VERSION="1.0.0"

# Defaults
VERBOSE=false
DRY_RUN=false
OUTPUT_DIR="./output"

usage() {
    cat << EOF
$SCRIPT_NAME v$VERSION - Process files

Usage: $SCRIPT_NAME [OPTIONS] <input-file>

Options:
    -h, --help          Show this help
    -v, --verbose       Enable verbose output
    -n, --dry-run       Show what would be done
    -o, --output DIR    Output directory (default: $OUTPUT_DIR)
    --version           Show version

Examples:
    $SCRIPT_NAME -v data.csv
    $SCRIPT_NAME --output=/tmp data.csv
EOF
}

die() { echo "Error: $*" >&2; exit 1; }

parse_args() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -h|--help) usage; exit 0 ;;
            --version) echo "$VERSION"; exit 0 ;;
            -v|--verbose) VERBOSE=true; shift ;;
            -n|--dry-run) DRY_RUN=true; shift ;;
            -o|--output) OUTPUT_DIR="$2"; shift 2 ;;
            --output=*) OUTPUT_DIR="${1#*=}"; shift ;;
            --) shift; break ;;
            -*) die "Unknown option: $1" ;;
            *) break ;;
        esac
    done

    # Remaining args
    INPUT_FILE="${1:-}"
    [[ -z "$INPUT_FILE" ]] && die "Input file required"
    [[ -f "$INPUT_FILE" ]] || die "File not found: $INPUT_FILE"
}

main() {
    parse_args "$@"

    [[ "$VERBOSE" == true ]] && echo "Processing $INPUT_FILE..."
    [[ "$DRY_RUN" == true ]] && echo "[DRY RUN]"

    # Your logic here
}

main "$@"
```

---

## 🔥 Pro Tips

### 1. Provide Good Help
```bash
# Always include examples
# Show defaults
# Document all options
```

### 2. Support Both Short and Long
```bash
-v|--verbose)
-f|--file)
```

### 3. Handle `--` Separator
```bash
# Allows: script.sh -- -file-starting-with-dash
```

---

## 🛠️ Hands-on Exercise

Build a `backup.sh` script:
1. Required: source directory
2. Optional: --dest, --compress, --exclude
3. Flags: --verbose, --dry-run
4. Validate all inputs
5. Show usage with examples
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "intermediate",
    "order_index": 13,
    "tags": ["bash", "arguments", "getopts", "cli", "parsing"],
}


# ============================================================================
# BLOCK 5: SIGNALS & ADVANCED I/O (Nodes 14-16)
# ============================================================================

BASH_NODE_14_SIGNALS = {
    "id": "bash-14-signals",
    "title": "Signals & Traps",
    "description": "Handle interrupts and implement graceful shutdowns",
    "content": """
# Signals & Traps

> *"A professional script doesn't just crash — it cleans up after itself."*

---

## 🎯 Why This Matters

Long-running scripts need to:
- Handle Ctrl+C gracefully
- Clean up temp files on exit
- Release locks and resources
- Restart services safely

---

## 🧠 Core Concepts

### Common Signals

| Signal | Number | Default | Use Case |
|--------|--------|---------|----------|
| SIGHUP | 1 | Terminate | Terminal closed |
| SIGINT | 2 | Terminate | Ctrl+C |
| SIGQUIT | 3 | Core dump | Ctrl+\\\\ |
| SIGTERM | 15 | Terminate | Polite kill |
| SIGKILL | 9 | Terminate | Force kill (can't trap) |
| SIGUSR1 | 10 | Terminate | User-defined |
| SIGUSR2 | 12 | Terminate | User-defined |

### trap Syntax

```bash
# Basic trap
trap 'commands' SIGNAL

# Trap multiple signals
trap 'cleanup' EXIT INT TERM

# Ignore signal
trap '' INT

# Reset to default
trap - INT

# Show current traps
trap -p
```

### Cleanup Pattern

```bash
#!/usr/bin/env bash
set -euo pipefail

# Create temp file
TEMP_FILE=$(mktemp)
LOCK_FILE="/var/run/myapp.lock"

cleanup() {
    local exit_code=$?
    echo "Cleaning up..."
    rm -f "$TEMP_FILE"
    rm -f "$LOCK_FILE"
    exit $exit_code
}

trap cleanup EXIT

# Script logic here
echo "Working..."
sleep 100
```

### Graceful Shutdown

```bash
#!/usr/bin/env bash

SHUTDOWN=false

shutdown_handler() {
    echo "Shutdown requested..."
    SHUTDOWN=true
}

trap shutdown_handler SIGTERM SIGINT

# Main loop
while [[ "$SHUTDOWN" == false ]]; do
    echo "Processing..."
    sleep 1
done

echo "Graceful shutdown complete"
```

### Signal Handlers

```bash
# Reload config on SIGHUP
reload_config() {
    echo "Reloading config..."
    source /etc/myapp/config
}
trap reload_config HUP

# Toggle debug on SIGUSR1
toggle_debug() {
    DEBUG=$((1 - DEBUG))
    echo "Debug: $DEBUG"
}
trap toggle_debug USR1

# Send signal
kill -USR1 $PID
```

---

## 💻 Essential Patterns

```bash
# Prevent double cleanup
CLEANED_UP=false
cleanup() {
    [[ "$CLEANED_UP" == true ]] && return
    CLEANED_UP=true
    # actual cleanup
}

# Lock file with cleanup
acquire_lock() {
    exec 200>"$LOCK_FILE"
    flock -n 200 || die "Already running"
    trap 'rm -f "$LOCK_FILE"' EXIT
}

# Timeout with trap
timeout_handler() {
    die "Operation timed out"
}
trap timeout_handler ALRM
(sleep 30; kill -ALRM $$) &
timeout_pid=$!
# operation
kill $timeout_pid 2>/dev/null
```

---

## 🔥 Pro Tips

### 1. EXIT Catches Everything
```bash
# EXIT runs on normal exit, error, or signal
trap cleanup EXIT
```

### 2. Use Functions in Traps
```bash
# ✅ Better
trap cleanup EXIT

# ❌ Harder to maintain
trap 'rm -f $f1; rm -f $f2; echo done' EXIT
```

---

## 🛠️ Hands-on Exercise

Create a daemon script:
1. Write PID file on start
2. Handle SIGTERM for shutdown
3. Reload config on SIGHUP
4. Clean up on any exit
5. Prevent multiple instances
""",
    "xp_reward": 225,
    "estimated_time": "55 minutes",
    "difficulty": "advanced",
    "order_index": 14,
    "tags": ["bash", "signals", "trap", "cleanup", "graceful-shutdown"],
}

BASH_NODE_15_PROCESS_SUBSTITUTION = {
    "id": "bash-15-process-substitution",
    "title": "Process Substitution",
    "description": "Connect commands without intermediate files",
    "content": """
# Process Substitution

> *"Pipes are great. Process substitution is pipes on steroids."*

---

## 🎯 Why This Matters

Process substitution lets you:
- Compare command outputs directly
- Use multiple inputs without temp files
- Feed data to commands expecting files
- Build complex data pipelines

---

## 🧠 Core Concepts

### Syntax

```bash
# Output as file
<(command)  # Read from command output as if it were a file

# Input as file
>(command)  # Write to command input as if it were a file

# They create special file descriptors
echo <(ls)  # /dev/fd/63 (example)
```

### Reading from Process Substitution

```bash
# Compare two commands
diff <(ls dir1) <(ls dir2)

# Compare sorted files
diff <(sort file1) <(sort file2)

# Read multiple files
paste <(cut -f1 data.tsv) <(cut -f3 data.tsv)

# Join command outputs
join <(sort file1) <(sort file2)
```

### Writing to Process Substitution

```bash
# Tee to multiple destinations
echo "log message" | tee >(logger) >(cat >> file.log)

# Process and save simultaneously
some_command | tee >(gzip > output.gz) | head

# Send to multiple processors
cat data.txt | tee >(grep ERROR > errors.txt) >(grep WARN > warnings.txt) > /dev/null
```

### While Loop Without Subshell

```bash
# ❌ Problem: pipe creates subshell
cat file | while read line; do
    count=$((count + 1))
done
echo $count  # Empty! Variable lost

# ✅ Solution: process substitution
while read -r line; do
    count=$((count + 1))
done < <(cat file)
echo $count  # Works!
```

### Complex Pipelines

```bash
# Diff remote files
diff <(ssh server1 'cat /etc/config') <(ssh server2 'cat /etc/config')

# Parallel downloads comparison
diff <(curl -s url1 | jq .) <(curl -s url2 | jq .)

# Multiple transformations
paste <(awk '{print $1}' data.txt) \\
      <(awk '{print $2}' data.txt | tr '[:lower:]' '[:upper:]')
```

---

## 💻 Essential Patterns

```bash
# Source from command
source <(curl -s https://example.com/script.sh)

# Here doc in process substitution
cat <(cat << 'EOF'
line 1
line 2
EOF
)

# Check if files differ
if diff <(sort a.txt) <(sort b.txt) >/dev/null; then
    echo "Files are identical"
fi

# Feed to command expecting filename
wc -l <(find . -name "*.sh")
```

---

## 🔥 Pro Tips

### 1. Combine with Named Pipes
```bash
mkfifo mypipe
process1 > mypipe &
process2 < mypipe
```

### 2. Debug with tee
```bash
cmd1 | tee >(cat >&2) | cmd2  # Show intermediate
```

---

## 🛠️ Hands-on Exercise

Build a log analyzer:
1. Compare today vs yesterday logs
2. Extract unique errors from both
3. Show entries only in today's log
4. All without temp files
""",
    "xp_reward": 200,
    "estimated_time": "45 minutes",
    "difficulty": "advanced",
    "order_index": 15,
    "tags": ["bash", "process-substitution", "pipes", "advanced-io"],
}

BASH_NODE_16_CRON = {
    "id": "bash-16-cron",
    "title": "Cron & Scheduling",
    "description": "Automate recurring tasks with cron and systemd timers",
    "content": """
# Cron & Scheduling

> *"The best automation runs while you sleep."*

---

## 🎯 Why This Matters

DevOps relies on scheduled tasks:
- Backups at midnight
- Log rotation weekly
- Health checks every minute
- Reports every morning

---

## 🧠 Core Concepts

### Cron Syntax

```
# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday = 0)
# │ │ │ │ │
# * * * * * command

# Examples
0 * * * *     # Every hour
*/5 * * * *   # Every 5 minutes
0 2 * * *     # Daily at 2 AM
0 0 * * 0     # Weekly on Sunday
0 0 1 * *     # Monthly on 1st
```

### Managing Crontab

```bash
# Edit your crontab
crontab -e

# List your crontab
crontab -l

# Remove crontab
crontab -r

# Edit another user's crontab (root)
crontab -u username -e
```

### Cron Best Practices

```bash
# Always use absolute paths
0 2 * * * /usr/local/bin/backup.sh

# Set PATH at top of crontab
PATH=/usr/local/bin:/usr/bin:/bin

# Capture output
0 2 * * * /path/to/script.sh >> /var/log/script.log 2>&1

# Use MAILTO for errors
MAILTO=admin@example.com
0 2 * * * /path/to/script.sh

# Lock to prevent overlap
0 * * * * flock -n /tmp/job.lock /path/to/script.sh
```

### Scripts for Cron

```bash
#!/usr/bin/env bash
# cron-safe script

set -euo pipefail

# Log file
LOG_FILE="/var/log/myjob.log"
exec >> "$LOG_FILE" 2>&1

# Timestamp
echo "=== $(date) ==="

# Set environment (cron has minimal env)
source /etc/environment

# Your logic
echo "Running job..."
```

### Systemd Timers (Modern Alternative)

```bash
# /etc/systemd/system/backup.service
[Unit]
Description=Backup Service

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh

# /etc/systemd/system/backup.timer
[Unit]
Description=Daily Backup

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target

# Enable and start
systemctl enable backup.timer
systemctl start backup.timer

# List timers
systemctl list-timers
```

---

## 💻 Essential Patterns

```bash
# Prevent overlapping runs
flock -n /tmp/job.lock /path/to/script.sh

# Timeout protection
timeout 3600 /path/to/script.sh

# Email on failure
0 2 * * * /path/to/script.sh || mail -s "Job failed" admin@example.com

# Random delay (spread load)
0 2 * * * sleep $((RANDOM \\% 300)); /path/to/script.sh
```

---

## 🔥 Pro Tips

### 1. Test Cron Commands
```bash
# Simulate cron environment
env -i /bin/bash --noprofile --norc -c 'your_command'
```

### 2. Use Cron Wrappers
```bash
#!/usr/bin/env bash
# Wrapper adds logging, locking, notifications
exec &>> /var/log/cron-wrapper.log
flock -n /tmp/job.lock "$@" || exit 0
```

---

## 🛠️ Hands-on Exercise

Set up automated maintenance:
1. Daily backup at 2 AM
2. Hourly log rotation
3. Weekly cleanup of /tmp
4. Monitor with email alerts
5. Include overlap prevention
""",
    "xp_reward": 200,
    "estimated_time": "50 minutes",
    "difficulty": "intermediate",
    "order_index": 16,
    "tags": ["bash", "cron", "scheduling", "systemd", "automation"],
}


# ============================================================================
# BLOCK 6: PRODUCTION PATTERNS (Nodes 17-19)
# ============================================================================

BASH_NODE_17_SECURITY = {
    "id": "bash-17-security",
    "title": "Security Best Practices",
    "description": "Write secure scripts that don't compromise your systems",
    "content": """
# Security Best Practices

> *"A script with root access is a loaded gun. Handle with care."*

---

## 🎯 Why This Matters

Scripts often:
- Run with elevated privileges
- Handle sensitive data
- Process untrusted input
- Access critical systems

One vulnerability can compromise everything.

---

## 🧠 Core Concepts

### Input Validation

```bash
# Never trust user input
filename="$1"

# ❌ Dangerous: command injection
cat $filename
rm $filename

# ✅ Safe: validate and quote
[[ "$filename" =~ ^[a-zA-Z0-9._-]+$ ]] || die "Invalid filename"
[[ -f "$filename" ]] || die "File not found"
cat -- "$filename"
```

### Prevent Command Injection

```bash
# ❌ Vulnerable to injection
user_input="hello; rm -rf /"
eval "echo $user_input"

# ✅ Safe: use arrays for commands
cmd=("echo" "$user_input")
"${cmd[@]}"

# ❌ Dangerous
mysql -e "SELECT * FROM users WHERE name='$input'"

# ✅ Safer: parameterized
mysql -e "SELECT * FROM users WHERE name=?" -- "$input"
```

### Secure File Operations

```bash
# Use mktemp for temp files
temp_file=$(mktemp)
trap 'rm -f "$temp_file"' EXIT

# Set restrictive permissions
umask 077  # Only owner can read/write

# Avoid symlink attacks
[[ -L "$file" ]] && die "Symlink not allowed"

# Safe directory creation
mkdir -p "$dir"
chmod 700 "$dir"
```

### Sensitive Data Handling

```bash
# ❌ Password in command line (visible in ps)
mysql --password="secret" ...

# ✅ Use environment or file
export MYSQL_PWD="$secret"
mysql ...

# ✅ Or config file
mysql --defaults-file=/root/.my.cnf

# Clear sensitive variables
unset password
secret=""
```

### Privilege Management

```bash
# Drop privileges when possible
if [[ $EUID -eq 0 ]]; then
    su -c "less_privileged_command" nobody
fi

# Request sudo only when needed
if [[ $EUID -ne 0 ]]; then
    exec sudo "$0" "$@"
fi

# Validate sudo is available
sudo -n true 2>/dev/null || die "Sudo required"
```

### Safe PATH Handling

```bash
# ❌ Dangerous: relative paths
./bin/mycommand
bin/mycommand

# ✅ Safe: absolute paths
/usr/local/bin/mycommand

# ✅ Restrict PATH
export PATH="/usr/local/bin:/usr/bin:/bin"
```

---

## 💻 Essential Patterns

```bash
# Validate integer
is_int() {
    [[ "$1" =~ ^-?[0-9]+$ ]]
}

# Sanitize for shell
sanitize() {
    printf '%q' "$1"
}

# Secure temp directory
SECURE_TMPDIR=$(mktemp -d)
chmod 700 "$SECURE_TMPDIR"
trap 'rm -rf "$SECURE_TMPDIR"' EXIT
```

---

## 🔥 Pro Tips

### 1. Use `set -u` to Catch Unset Variables
```bash
set -u
# rm -rf "$UNDEFINED_VAR/"  # Error instead of rm -rf /
```

### 2. Audit with shellcheck
```bash
shellcheck --severity=warning script.sh
```

### 3. Use `--` to End Options
```bash
rm -- "$filename"  # Safe even if filename starts with -
```

---

## 🛠️ Hands-on Exercise

Audit and fix this script:
1. Validate all inputs
2. Remove command injection risks
3. Handle secrets properly
4. Add proper file permissions
5. Restrict PATH
""",
    "xp_reward": 250,
    "estimated_time": "60 minutes",
    "difficulty": "advanced",
    "order_index": 17,
    "tags": ["bash", "security", "hardening", "validation", "injection"],
}

BASH_NODE_18_PERFORMANCE = {
    "id": "bash-18-performance",
    "title": "Performance Optimization",
    "description": "Write fast scripts that scale",
    "content": """
# Performance Optimization

> *"Bash isn't fast, but smart Bash is fast enough."*

---

## 🎯 Why This Matters

Slow scripts:
- Waste resources
- Delay deployments
- Miss monitoring windows
- Frustrate users

Optimization matters for production scripts.

---

## 🧠 Core Concepts

### Avoid Subshells

```bash
# ❌ Slow: subshell per iteration
for file in *.txt; do
    count=$(wc -l < "$file")
    echo "$file: $count"
done

# ✅ Faster: minimize subshells
while IFS= read -r line; do
    # process
done < <(find . -name "*.txt")
```

### Use Built-ins Over External Commands

```bash
# ❌ Slow: external command
length=$(echo "$string" | wc -c)

# ✅ Fast: built-in
length=${#string}

# ❌ Slow: grep in loop
for item in "${array[@]}"; do
    if echo "$item" | grep -q "pattern"; then
        # ...
    fi
done

# ✅ Fast: built-in matching
for item in "${array[@]}"; do
    if [[ "$item" == *pattern* ]]; then
        # ...
    fi
done
```

### Efficient String Operations

```bash
# ❌ Slow: external tools
basename=$(echo "$path" | sed 's|.*/||')

# ✅ Fast: parameter expansion
basename="${path##*/}"

# ❌ Slow: multiple echoes
echo "line1"
echo "line2"
echo "line3"

# ✅ Fast: single printf
printf '%s\\n' "line1" "line2" "line3"
```

### Parallel Processing

```bash
# Sequential (slow)
for server in "${servers[@]}"; do
    ping -c 1 "$server"
done

# Parallel (fast)
for server in "${servers[@]}"; do
    ping -c 1 "$server" &
done
wait

# With GNU parallel
parallel -j 10 ping -c 1 {} ::: "${servers[@]}"

# xargs parallel
printf '%s\\n' "${servers[@]}" | xargs -P 10 -I {} ping -c 1 {}
```

### Efficient File Processing

```bash
# ❌ Very slow: cat in loop
while read -r line; do
    echo "$line"
done < <(cat hugefile.txt)

# ✅ Better: redirect directly
while IFS= read -r line; do
    echo "$line"
done < hugefile.txt

# ✅ Best: use awk/sed for bulk processing
awk '{print $1}' hugefile.txt
```

### Memory Efficiency

```bash
# ❌ Load entire file into memory
data=$(cat hugefile.txt)

# ✅ Process line by line
while IFS= read -r line; do
    process "$line"
done < hugefile.txt

# ✅ Use streaming tools
cut -d',' -f1 hugefile.csv | sort | uniq -c
```

---

## 💻 Benchmarking

```bash
# Time a command
time expensive_command

# More precise timing
SECONDS=0
expensive_command
echo "Took $SECONDS seconds"

# Compare approaches
hyperfine 'approach1' 'approach2'
```

---

## 🔥 Pro Tips

### 1. Profile Before Optimizing
```bash
# Find slow parts first
PS4='+ $(date "+%s.%N") '
set -x
./script.sh
set +x
```

### 2. Cache Expensive Operations
```bash
# Cache command output
if [[ ! -f "$cache_file" ]] || [[ $(find "$cache_file" -mmin +60) ]]; then
    expensive_command > "$cache_file"
fi
cat "$cache_file"
```

### 3. Use Right Tool for Job
```bash
# For heavy text processing, use awk/python
awk '{sum+=$1} END {print sum}' data.txt  # Fast
# vs
while read n; do ((sum+=n)); done < data.txt  # Slow
```

---

## 🛠️ Hands-on Exercise

Optimize a log processor:
1. Process 1GB log file
2. Extract unique IPs
3. Count occurrences
4. Sort by frequency
5. Compare bash vs awk solutions
""",
    "xp_reward": 225,
    "estimated_time": "55 minutes",
    "difficulty": "advanced",
    "order_index": 18,
    "tags": ["bash", "performance", "optimization", "parallel", "efficiency"],
}

BASH_NODE_19_ORGANIZATION = {
    "id": "bash-19-organization",
    "title": "Script Organization & Libraries",
    "description": "Structure large scripts and build reusable libraries",
    "content": """
# Script Organization & Libraries

> *"A well-organized script is a maintainable script."*

---

## 🎯 Why This Matters

Production scripts:
- Grow over time
- Need maintenance
- Are shared across teams
- Require documentation

Good organization enables all of this.

---

## 🧠 Core Concepts

### Script Template

```bash
#!/usr/bin/env bash
#
# script_name.sh - Brief description
#
# Usage: script_name.sh [OPTIONS] <args>
#
# Options:
#   -h, --help     Show help
#   -v, --verbose  Verbose output
#
# Author: Your Name
# Date: 2025-12-03
# Version: 1.0.0

set -euo pipefail

# Constants
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "$0")"
readonly VERSION="1.0.0"

# Defaults
VERBOSE=false

# Source libraries
source "${SCRIPT_DIR}/lib/logging.sh"
source "${SCRIPT_DIR}/lib/utils.sh"

#######################################
# Show usage information
#######################################
usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS] <args>

Options:
    -h, --help     Show this help
    -v, --verbose  Enable verbose output

Examples:
    $SCRIPT_NAME -v input.txt
EOF
}

#######################################
# Parse command line arguments
#######################################
parse_args() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -h|--help) usage; exit 0 ;;
            -v|--verbose) VERBOSE=true; shift ;;
            --) shift; break ;;
            -*) die "Unknown option: $1" ;;
            *) break ;;
        esac
    done
    ARGS=("$@")
}

#######################################
# Main entry point
#######################################
main() {
    parse_args "$@"
    # Your logic here
}

main "$@"
```

### Library Structure

```
project/
├── bin/
│   ├── deploy.sh
│   ├── backup.sh
│   └── monitor.sh
├── lib/
│   ├── common.sh      # Shared utilities
│   ├── logging.sh     # Log functions
│   ├── config.sh      # Config loading
│   └── validation.sh  # Input validation
├── conf/
│   ├── default.conf
│   └── production.conf
├── tests/
│   ├── test_common.sh
│   └── test_logging.sh
└── README.md
```

### Logging Library

```bash
# lib/logging.sh

readonly LOG_LEVEL_DEBUG=0
readonly LOG_LEVEL_INFO=1
readonly LOG_LEVEL_WARN=2
readonly LOG_LEVEL_ERROR=3

LOG_LEVEL=${LOG_LEVEL:-$LOG_LEVEL_INFO}
LOG_FILE="${LOG_FILE:-/dev/null}"

log() {
    local level=$1; shift
    local msg="$*"
    local ts=$(date '+%Y-%m-%d %H:%M:%S')
    
    echo "[$ts] [$level] $msg" | tee -a "$LOG_FILE" >&2
}

log_debug() { [[ $LOG_LEVEL -le $LOG_LEVEL_DEBUG ]] && log "DEBUG" "$@"; }
log_info()  { [[ $LOG_LEVEL -le $LOG_LEVEL_INFO ]]  && log "INFO" "$@"; }
log_warn()  { [[ $LOG_LEVEL -le $LOG_LEVEL_WARN ]]  && log "WARN" "$@"; }
log_error() { [[ $LOG_LEVEL -le $LOG_LEVEL_ERROR ]] && log "ERROR" "$@"; }

die() {
    log_error "$@"
    exit 1
}
```

### Configuration Management

```bash
# lib/config.sh

load_config() {
    local config_file="${1:?Config file required}"
    
    [[ -f "$config_file" ]] || die "Config not found: $config_file"
    
    # Validate and source
    bash -n "$config_file" || die "Invalid config syntax"
    source "$config_file"
}

# Usage
load_config "${SCRIPT_DIR}/conf/default.conf"
[[ -f "$USER_CONFIG" ]] && load_config "$USER_CONFIG"
```

### Testing Scripts

```bash
# tests/test_logging.sh

source "$(dirname "$0")/../lib/logging.sh"

test_log_info() {
    local output
    output=$(log_info "test message" 2>&1)
    [[ "$output" == *"INFO"*"test message"* ]] || fail "log_info failed"
    pass "log_info works"
}

test_die_exits() {
    (die "test" 2>/dev/null) && fail "die should exit"
    pass "die exits correctly"
}

# Run tests
test_log_info
test_die_exits
```

---

## 💻 Essential Patterns

```bash
# Guard against re-sourcing
[[ -n "${_LOGGING_SH:-}" ]] && return
readonly _LOGGING_SH=1

# Namespace functions
mylib::init() { ... }
mylib::cleanup() { ... }

# Export for subshells
export -f log_info log_error
```

---

## 🔥 Pro Tips

### 1. One Function, One Purpose
```bash
# ✅ Good: focused functions
validate_email() { ... }
send_email() { ... }

# ❌ Bad: doing too much
process_email() { validate && send && log && ... }
```

### 2. Document Everything
```bash
# Function header
#######################################
# Brief description
# Globals:
#   SOME_VAR - description
# Arguments:
#   $1 - first arg
# Outputs:
#   Writes to stdout
# Returns:
#   0 on success, 1 on error
#######################################
```

---

## 🛠️ Hands-on Exercise

Build a script toolkit:
1. Create lib/ with logging, utils, config
2. Build 3 scripts using shared libs
3. Add tests for each library
4. Create README with examples
""",
    "xp_reward": 225,
    "estimated_time": "60 minutes",
    "difficulty": "advanced",
    "order_index": 19,
    "tags": ["bash", "organization", "libraries", "structure", "maintainability"],
}


# ============================================================================
# BLOCK 7: CAPSTONE (Node 20)
# ============================================================================

BASH_NODE_20_AUTOMATION = {
    "id": "bash-20-automation",
    "title": "Real-World Automation Patterns",
    "description": "Production-ready patterns for DevOps automation",
    "content": """
# Real-World Automation Patterns

> *"This is where everything comes together. Welcome to production."*

---

## 🎯 Why This Matters

This final module combines everything:
- All previous concepts working together
- Battle-tested patterns from production
- Templates you'll use daily
- Real DevOps workflows

---

## 🧠 Core Patterns

### 1. Deployment Script

```bash
#!/usr/bin/env bash
set -euo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/lib/common.sh"

# Configuration
readonly APP_NAME="myapp"
readonly DEPLOY_USER="deploy"
readonly SERVERS=("web01" "web02" "web03")
readonly HEALTH_ENDPOINT="/health"
readonly ROLLBACK_LIMIT=3

# State
DEPLOYED_SERVERS=()

cleanup() {
    if [[ ${#DEPLOYED_SERVERS[@]} -gt 0 && ${#DEPLOYED_SERVERS[@]} -lt ${#SERVERS[@]} ]]; then
        log_error "Partial deployment! Rolling back..."
        for server in "${DEPLOYED_SERVERS[@]}"; do
            rollback_server "$server" || true
        done
    fi
}
trap cleanup EXIT

deploy_server() {
    local server=$1
    log_info "Deploying to $server..."
    
    # Remove from load balancer
    lb_remove "$server"
    
    # Wait for connections to drain
    sleep 10
    
    # Deploy
    ssh "${DEPLOY_USER}@${server}" << 'EOF'
        cd /opt/app
        git fetch origin
        git checkout "$VERSION"
        ./scripts/install-deps.sh
        sudo systemctl restart app
EOF
    
    # Health check
    retry 5 check_health "$server" || return 1
    
    # Return to load balancer
    lb_add "$server"
    
    DEPLOYED_SERVERS+=("$server")
    log_info "Deployed to $server successfully"
}

main() {
    local version="${1:?Version required}"
    
    log_info "Starting deployment of $version"
    
    for server in "${SERVERS[@]}"; do
        deploy_server "$server" || die "Failed to deploy to $server"
    done
    
    log_info "Deployment complete!"
}

main "$@"
```

### 2. Log Analyzer

```bash
#!/usr/bin/env bash
set -euo pipefail

# Analyze logs and generate report

readonly LOG_DIR="${1:-/var/log/app}"
readonly OUTPUT="${2:-report.txt}"
readonly DATE=$(date +%Y-%m-%d)

analyze_logs() {
    local log_file=$1
    
    echo "=== Analysis: $log_file ==="
    
    # Error summary
    echo "Errors by type:"
    grep -oE 'ERROR: [^:]+' "$log_file" 2>/dev/null | sort | uniq -c | sort -rn | head -10
    
    # Response times
    echo -e "\\nResponse time stats:"
    grep -oE 'duration=[0-9]+ms' "$log_file" 2>/dev/null | \\
        sed 's/duration=//;s/ms//' | \\
        awk '{sum+=$1; if($1>max)max=$1; count++} END {
            if(count>0) printf "Count: %d, Avg: %.0fms, Max: %dms\\n", count, sum/count, max
        }'
    
    # Top endpoints
    echo -e "\\nTop endpoints:"
    grep -oE 'GET|POST|PUT|DELETE [^ ]+' "$log_file" 2>/dev/null | \\
        sort | uniq -c | sort -rn | head -10
}

main() {
    {
        echo "Log Analysis Report - $DATE"
        echo "================================"
        echo
        
        for log_file in "$LOG_DIR"/*.log; do
            [[ -f "$log_file" ]] || continue
            analyze_logs "$log_file"
            echo
        done
    } > "$OUTPUT"
    
    echo "Report saved to $OUTPUT"
}

main
```

### 3. Backup Script

```bash
#!/usr/bin/env bash
set -euo pipefail

# Configuration
readonly BACKUP_DIR="/backups"
readonly RETENTION_DAYS=30
readonly SOURCES=("/var/www" "/etc/nginx" "/opt/app")
readonly S3_BUCKET="s3://backups/daily"

# Timestamp
readonly TIMESTAMP=$(date +%Y%m%d_%H%M%S)
readonly BACKUP_NAME="backup_${TIMESTAMP}.tar.gz"
readonly BACKUP_PATH="${BACKUP_DIR}/${BACKUP_NAME}"

log() { echo "[$(date '+%H:%M:%S')] $*"; }

create_backup() {
    log "Creating backup..."
    
    tar -czf "$BACKUP_PATH" "${SOURCES[@]}" 2>/dev/null || {
        log "Warning: Some files could not be backed up"
    }
    
    local size=$(du -h "$BACKUP_PATH" | cut -f1)
    log "Backup created: $BACKUP_NAME ($size)"
}

upload_to_s3() {
    log "Uploading to S3..."
    
    if aws s3 cp "$BACKUP_PATH" "${S3_BUCKET}/${BACKUP_NAME}" --quiet; then
        log "Upload complete"
    else
        log "ERROR: Upload failed"
        return 1
    fi
}

cleanup_old() {
    log "Cleaning backups older than $RETENTION_DAYS days..."
    
    find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +"$RETENTION_DAYS" -delete
    
    aws s3 ls "$S3_BUCKET/" | while read -r line; do
        local date_str=$(echo "$line" | awk '{print $1}')
        local file=$(echo "$line" | awk '{print $4}')
        local file_age=$(( ($(date +%s) - $(date -d "$date_str" +%s)) / 86400 ))
        
        if [[ $file_age -gt $RETENTION_DAYS ]]; then
            log "Deleting old backup: $file"
            aws s3 rm "${S3_BUCKET}/${file}" --quiet
        fi
    done
}

main() {
    mkdir -p "$BACKUP_DIR"
    
    create_backup
    upload_to_s3
    cleanup_old
    
    log "Backup complete!"
}

main "$@"
```

### 4. Health Monitor

```bash
#!/usr/bin/env bash
set -euo pipefail

# Configuration
declare -A SERVICES=(
    [web]="http://localhost:80/health"
    [api]="http://localhost:8080/health"
    [db]="pg_isready -h localhost"
    [redis]="redis-cli ping"
)

readonly SLACK_WEBHOOK="${SLACK_WEBHOOK:-}"
readonly CHECK_INTERVAL=60

check_http() {
    local url=$1
    curl -sf --max-time 5 "$url" > /dev/null
}

check_command() {
    local cmd=$1
    eval "$cmd" > /dev/null 2>&1
}

check_service() {
    local name=$1
    local check=$2
    
    if [[ "$check" == http* ]]; then
        check_http "$check"
    else
        check_command "$check"
    fi
}

alert() {
    local service=$1
    local status=$2
    local msg="[$status] Service: $service at $(date)"
    
    echo "$msg"
    
    [[ -n "$SLACK_WEBHOOK" ]] && curl -sf -X POST \\
        -H 'Content-type: application/json' \\
        -d "{\\"text\\": \\"$msg\\"}" \\
        "$SLACK_WEBHOOK" || true
}

monitor() {
    declare -A previous_status
    
    while true; do
        for service in "${!SERVICES[@]}"; do
            if check_service "$service" "${SERVICES[$service]}"; then
                [[ "${previous_status[$service]:-}" == "DOWN" ]] && \\
                    alert "$service" "RECOVERED"
                previous_status[$service]="UP"
            else
                [[ "${previous_status[$service]:-}" != "DOWN" ]] && \\
                    alert "$service" "DOWN"
                previous_status[$service]="DOWN"
            fi
        done
        
        sleep "$CHECK_INTERVAL"
    done
}

main() {
    echo "Starting health monitor..."
    monitor
}

main
```

### 5. Interactive Menu

```bash
#!/usr/bin/env bash

show_menu() {
    clear
    echo "================================"
    echo "   DevOps Toolkit v1.0"
    echo "================================"
    echo "1) Deploy Application"
    echo "2) View Logs"
    echo "3) Check Services"
    echo "4) Backup Database"
    echo "5) System Status"
    echo "q) Quit"
    echo "================================"
    read -rp "Select option: " choice
}

main() {
    while true; do
        show_menu
        case "$choice" in
            1) deploy_app; read -rp "Press Enter..." ;;
            2) view_logs; read -rp "Press Enter..." ;;
            3) check_services; read -rp "Press Enter..." ;;
            4) backup_db; read -rp "Press Enter..." ;;
            5) system_status; read -rp "Press Enter..." ;;
            q|Q) echo "Goodbye!"; exit 0 ;;
            *) echo "Invalid option" ;;
        esac
    done
}

main
```

---

## 🔥 Final Pro Tips

### 1. Always Have a Rollback Plan
### 2. Log Everything Important
### 3. Test in Staging First
### 4. Use Version Control for Scripts
### 5. Document Your Automation

---

## 🏆 Capstone Project

Build a complete deployment pipeline:
1. Pre-flight checks (deps, permissions)
2. Backup current state
3. Deploy with rolling updates
4. Health checks after each server
5. Auto-rollback on failure
6. Slack notifications
7. Deployment summary report

**Congratulations! You've mastered Bash scripting!**
""",
    "xp_reward": 300,
    "estimated_time": "90 minutes",
    "difficulty": "advanced",
    "order_index": 20,
    "tags": ["bash", "automation", "devops", "production", "capstone"],
}


# ============================================================================
# SKILLSMAP DEFINITION
# ============================================================================

def get_bash_skillsmap() -> dict[str, Any]:
    """Return the complete Bash SkillsMap definition."""
    return {
        "id": "bash-scripting",
        "name": "Shell/Bash Scripting",
        "slug": "bash",
        "description": "Master Bash scripting from fundamentals to production automation",
        "icon": "terminal",
        "color": "#4EAA25",  # Bash green
        "estimated_hours": 20,
        "difficulty": "intermediate",
        "prerequisites": ["linux"],
        "tags": ["bash", "shell", "scripting", "automation", "devops"],
        "nodes": [
            # Block 1: Noder 1-3
            BASH_NODE_01_INTRODUCTION,
            BASH_NODE_02_VARIABLES,
            BASH_NODE_03_CONTROL_STRUCTURES,
            # Block 2: Noder 4-6
            BASH_NODE_04_LOOPS,
            BASH_NODE_05_FUNCTIONS,
            BASH_NODE_06_REDIRECTION,
            # Block 3: Noder 7-9
            BASH_NODE_07_HERE_DOCS,
            BASH_NODE_08_STRINGS,
            BASH_NODE_09_ARRAYS,
            # Block 4: Noder 10-12
            BASH_NODE_10_REGEX,
            BASH_NODE_11_ERROR_HANDLING,
            BASH_NODE_12_DEBUGGING,
            # Block 5: Noder 13-15
            BASH_NODE_13_ARGUMENTS,
            BASH_NODE_14_SIGNALS,
            BASH_NODE_15_PROCESS_SUBSTITUTION,
            # Block 6: Noder 16-18
            BASH_NODE_16_CRON,
            BASH_NODE_17_SECURITY,
            BASH_NODE_18_PERFORMANCE,
            # Block 7: Noder 19-20
            BASH_NODE_19_ORGANIZATION,
            BASH_NODE_20_AUTOMATION,
        ],
    }


# Export for seeding
BASH_SKILLSMAP = get_bash_skillsmap()
