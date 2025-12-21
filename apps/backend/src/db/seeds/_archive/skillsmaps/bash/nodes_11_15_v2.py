"""
Bash Nodes 11-15: Advanced Techniques (V2 Format)
=================================================
"""

NODE_BASH_11_PROCESS_MANAGEMENT_V2 = {
    "id": "bash-11-processes",
    "title": "Process Management",
    "slug": "bash-processes",
    "description": "Master background jobs, signals, and process control",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 130,
    "sections": [
        {"type": "intro", "content": {
            "headline": "Process Management",
            "hook": "DevOps handlar om att hantera processer - starta, stoppa, övervaka.",
            "learning_objectives": ["Köra processer i bakgrunden", "Hantera signaler", "Använda traps för cleanup"],
            "prerequisites": ["Bash Strings"], "estimated_time": "35 minuter", "xp_reward": 130
        }},
        {"type": "concepts", "content": {"concepts": [
            {"title": "Background Jobs", "explanation": """```bash
# Starta i bakgrunden
command &

# Se bakgrundsjobb
jobs

# Bring to foreground
fg %1

# Send to background
bg %1

# Wait for background jobs
wait          # Alla
wait $pid     # Specifik
```"""},
            {"title": "Signals", "explanation": """```bash
# Skicka signaler
kill -TERM $pid    # Graceful terminate
kill -KILL $pid    # Force kill (SIGKILL)
kill -HUP $pid     # Reload config
kill -USR1 $pid    # User defined

# Vanliga signaler
SIGTERM (15)  # Default kill
SIGKILL (9)   # Cannot be caught
SIGINT (2)    # Ctrl+C
SIGHUP (1)    # Hangup/reload
```""", "pro_tip": "Använd alltid SIGTERM först, SIGKILL bara som sista utväg"},
            {"title": "Trap - Signal Handling", "explanation": """```bash
#!/usr/bin/env bash

cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/lockfile
    exit 0
}

# Catch signals
trap cleanup SIGTERM SIGINT

# Catch script exit
trap cleanup EXIT

# Your main script here
echo "Running... (Ctrl+C to test)"
while true; do sleep 1; done
```""", "common_mistake": "Glöm inte trap EXIT för cleanup - den körs alltid när scriptet avslutas"}
        ]}},
        {"type": "practice", "content": {"exercises": [
            {"task": "Kör i bakgrunden", "instruction": "Starta sleep 60 i bakgrunden", "expected_command": "sleep 60 &", "hint": "& i slutet kör kommandot i bakgrunden"},
            {"task": "Visa bakgrundsjobb", "instruction": "Lista alla bakgrundsjobb", "expected_command": "jobs", "hint": "jobs visar alla jobb i current shell"}
        ]}},
        {"type": "quiz", "content": {"questions": {"multiple_choice": [
            {"question": "Vilken signal kan INTE fångas av trap?", "options": ["SIGTERM", "SIGINT", "SIGKILL", "SIGHUP"], "correct": 2, "explanation": "SIGKILL (9) kan inte fångas eller ignoreras - det är en garanterad process-kill."}
        ]}}}
    ]
}

NODE_BASH_12_ERROR_HANDLING_V2 = {
    "id": "bash-12-errors",
    "title": "Error Handling & Debugging",
    "slug": "bash-error-handling",
    "description": "Write robust scripts with proper error handling",
    "difficulty": "intermediate",
    "estimated_minutes": 40,
    "xp_reward": 140,
    "sections": [
        {"type": "intro", "content": {
            "headline": "Error Handling & Debugging",
            "hook": "Scripts som bara fungerar i happy path är värdelösa i produktion.",
            "learning_objectives": ["Använda strict mode", "Implementera felhantering", "Debugga effektivt"],
            "prerequisites": ["Bash Processes"], "estimated_time": "40 minuter", "xp_reward": 140
        }},
        {"type": "concepts", "content": {"concepts": [
            {"title": "Strict Mode", "explanation": """```bash
#!/usr/bin/env bash
set -euo pipefail

# set -e: Exit on error
# set -u: Error on undefined variable
# set -o pipefail: Catch errors in pipes

# Alternativt
set -Eeuo pipefail
# -E: Inherit ERR trap in functions
```""", "pro_tip": "ALLTID använd set -euo pipefail i produktionsscripts"},
            {"title": "Exit Codes", "explanation": """```bash
# Check exit code
command
if [[ $? -eq 0 ]]; then
    echo "Success"
fi

# Or inline
command && echo "Success" || echo "Failed"

# Custom exit codes
exit 0   # Success
exit 1   # General error
exit 2   # Misuse of command
exit 126 # Permission denied
exit 127 # Command not found
```"""},
            {"title": "Error Functions", "explanation": """```bash
die() {
    echo "ERROR: $*" >&2
    exit 1
}

warn() {
    echo "WARN: $*" >&2
}

# Usage
[[ -f config.yaml ]] || die "Config not found"
```"""},
            {"title": "Debugging", "explanation": """```bash
# Print commands as executed
bash -x script.sh

# Inside script
set -x  # Enable debug
# ... code ...
set +x  # Disable debug

# Verbose + debug
set -xv

# Custom debug function
debug() {
    [[ "${DEBUG:-0}" == "1" ]] && echo "DEBUG: $*" >&2
}

# Usage: DEBUG=1 ./script.sh
```""", "pro_tip": "Använd DEBUG-variabeln för att enkelt slå på/av debug-output"}
        ]}},
        {"type": "quiz", "content": {"questions": {"multiple_choice": [
            {"question": "Vad gör set -u?", "options": ["Ger error vid odefinierade variabler", "Sätter user", "Undo senaste", "Unlimited resources"], "correct": 0, "explanation": "set -u (nounset) ger error om du försöker använda en variabel som inte är definierad."}
        ]}}}
    ]
}

NODE_BASH_13_SUBSHELLS_V2 = {
    "id": "bash-13-subshells",
    "title": "Subshells & Process Substitution",
    "slug": "bash-subshells",
    "description": "Master advanced process control with subshells",
    "difficulty": "advanced",
    "estimated_minutes": 35,
    "xp_reward": 130,
    "sections": [
        {"type": "intro", "content": {
            "headline": "Subshells & Process Substitution",
            "hook": "Subshells ger dig isolerade miljöer och process substitution ger dig magiska pipes.",
            "learning_objectives": ["Förstå subshells och deras scope", "Använda process substitution", "Undvika vanliga fallgropar"],
            "prerequisites": ["Bash Error Handling"], "estimated_time": "35 minuter", "xp_reward": 130
        }},
        {"type": "concepts", "content": {"concepts": [
            {"title": "Subshells", "explanation": """```bash
# Explicit subshell med ( )
(cd /tmp && ls)    # cd påverkar inte parent shell
pwd                # Fortfarande i original dir

# Pipes skapar subshells!
count=0
cat file | while read line; do
    ((count++))    # Ändras i subshell!
done
echo $count        # 0! (parent ser inte ändringen)

# Lösning: process substitution
while read line; do
    ((count++))
done < <(cat file)
```""", "common_mistake": "Pipes skapar subshells - variabler ändrade i pipelinen syns inte efteråt!"},
            {"title": "Process Substitution", "explanation": """```bash
# <(command) - output som fil
diff <(ls dir1) <(ls dir2)

# >(command) - input som fil
command | tee >(grep ERROR > errors.log)

# Jämför två kommandon
diff <(sort file1) <(sort file2)

# Processa flera inputs
paste <(cut -f1 file) <(cut -f2 file)
```""", "pro_tip": "Process substitution är perfekt för att undvika tempfiler"}
        ]}},
        {"type": "quiz", "content": {"questions": {"multiple_choice": [
            {"question": "Varför ändras inte count utanför: cat f | while read; do ((count++)); done?", "options": ["Syntax error", "while skapar subshell", "Pipe skapar subshell", "count är readonly"], "correct": 2, "explanation": "Pipe skapar en subshell för höger sida - ändringar där syns inte i parent shell."}
        ]}}}
    ]
}

NODE_BASH_14_ARRAYS_ADVANCED_V2 = {
    "id": "bash-14-arrays-advanced",
    "title": "Advanced Arrays & Data Structures",
    "slug": "bash-arrays-advanced",
    "description": "Master complex data handling with arrays",
    "difficulty": "advanced",
    "estimated_minutes": 35,
    "xp_reward": 130,
    "sections": [
        {"type": "intro", "content": {
            "headline": "Advanced Arrays",
            "hook": "Associativa arrays och array-manipulation gör Bash till ett riktigt programmeringsspråk.",
            "learning_objectives": ["Arbeta med associativa arrays", "Array slicing och manipulation", "Simulera data structures"],
            "prerequisites": ["Bash Subshells"], "estimated_time": "35 minuter", "xp_reward": 130
        }},
        {"type": "concepts", "content": {"concepts": [
            {"title": "Associative Arrays (Dictionaries)", "explanation": """```bash
declare -A config

config[host]="localhost"
config[port]="8080"
config[env]="production"

# Access
echo ${config[host]}

# All keys
echo ${!config[@]}

# All values
echo ${config[@]}

# Iterate
for key in "${!config[@]}"; do
    echo "$key: ${config[$key]}"
done
```"""},
            {"title": "Array Operations", "explanation": """```bash
arr=(a b c d e)

# Slice
echo ${arr[@]:1:3}    # b c d (from 1, length 3)

# Append
arr+=(f g)

# Delete element
unset 'arr[2]'

# Length
echo ${#arr[@]}

# Copy array
copy=("${arr[@]}")

# Merge arrays
merged=("${arr1[@]}" "${arr2[@]}")
```"""},
            {"title": "JSON-like Structures", "explanation": """```bash
# Simulated objects with naming convention
declare -A server1 server2

server1[name]="web1"
server1[ip]="10.0.0.1"
server1[port]="80"

server2[name]="web2"
server2[ip]="10.0.0.2"
server2[port]="80"

# Process multiple "objects"
for server in server1 server2; do
    declare -n s="$server"  # nameref
    echo "${s[name]}: ${s[ip]}:${s[port]}"
done
```""", "pro_tip": "declare -n skapar en nameref - en referens till annan variabel"}
        ]}},
        {"type": "quiz", "content": {"questions": {"multiple_choice": [
            {"question": "Hur deklarerar du en associativ array?", "options": ["arr=()", "declare -a arr", "declare -A arr", "assoc arr"], "correct": 2, "explanation": "declare -A skapar associativ array. declare -a skapar indexed array."}
        ]}}}
    ]
}

NODE_BASH_15_GETOPTS_V2 = {
    "id": "bash-15-getopts",
    "title": "Argument Parsing with getopts",
    "slug": "bash-getopts",
    "description": "Build professional CLI tools with proper argument parsing",
    "difficulty": "advanced",
    "estimated_minutes": 35,
    "xp_reward": 130,
    "sections": [
        {"type": "intro", "content": {
            "headline": "Argument Parsing",
            "hook": "Professionella scripts har -h för help och -v för verbose. Det är inte magi - det är getopts.",
            "learning_objectives": ["Parsa short options med getopts", "Hantera long options", "Bygga användarvänliga CLI-tools"],
            "prerequisites": ["Bash Arrays Advanced"], "estimated_time": "35 minuter", "xp_reward": 130
        }},
        {"type": "concepts", "content": {"concepts": [
            {"title": "getopts Basics", "explanation": """```bash
#!/usr/bin/env bash

usage() {
    echo "Usage: $0 [-v] [-f file] [-n count]"
    exit 1
}

verbose=false
file=""
count=1

while getopts "vf:n:h" opt; do
    case $opt in
        v) verbose=true ;;
        f) file="$OPTARG" ;;
        n) count="$OPTARG" ;;
        h) usage ;;
        ?) usage ;;
    esac
done

shift $((OPTIND - 1))  # Remove parsed options
remaining_args="$@"
```""", "pro_tip": "Kolon efter bokstav betyder att optionen tar ett argument"},
            {"title": "Long Options", "explanation": """```bash
# Manual parsing for long options
while [[ $# -gt 0 ]]; do
    case $1 in
        -v|--verbose)
            verbose=true
            shift
            ;;
        -f|--file)
            file="$2"
            shift 2
            ;;
        --file=*)
            file="${1#*=}"
            shift
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
            break
            ;;
    esac
done
```"""}
        ]}},
        {"type": "challenge", "content": {
            "scenario": "Bygg ett deployment-script med argument",
            "requirements": ["-e/--env för environment", "-t/--tag för version", "-d/--dry-run för test", "-h/--help för usage"],
            "hints": ["Kombinera getopts med case för long options", "Validera required arguments"],
            "solution": """#!/usr/bin/env bash
set -euo pipefail

usage() {
    cat << EOF
Usage: $0 -e ENV -t TAG [-d]
  -e, --env     Environment (staging/production)
  -t, --tag     Docker tag
  -d, --dry-run Dry run mode
  -h, --help    Show this help
EOF
    exit 1
}

env="" tag="" dry_run=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -e|--env) env="$2"; shift 2 ;;
        -t|--tag) tag="$2"; shift 2 ;;
        -d|--dry-run) dry_run=true; shift ;;
        -h|--help) usage ;;
        *) echo "Unknown: $1"; usage ;;
    esac
done

[[ -z "$env" ]] && { echo "Missing -e"; usage; }
[[ -z "$tag" ]] && { echo "Missing -t"; usage; }

echo "Deploying $tag to $env (dry_run=$dry_run)"""
        }}
    ]
}
