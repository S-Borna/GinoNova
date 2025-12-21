"""
Bash Node 5: Functions (V2 Format)
==================================
Master function declaration, arguments, and return values
"""

NODE_BASH_05_FUNCTIONS_V2 = {
    "id": "bash-05-functions",
    "title": "Functions",
    "slug": "bash-functions",
    "description": "Master function declaration, arguments, and return values",
    "difficulty": "beginner",
    "estimated_minutes": 30,
    "xp_reward": 100,
    "sections": [
        {
            "type": "intro",
            "content": {
                "headline": "Functions i Bash",
                "hook": "Funktioner är byggstenarna för underhållbar kod. DRY - Don't Repeat Yourself.",
                "learning_objectives": [
                    "Deklarera och anropa funktioner",
                    "Hantera argument och return-värden",
                    "Förstå scope med local-variabler",
                    "Skriva återanvändbara utility-funktioner"
                ],
                "prerequisites": ["Bash Loops"],
                "estimated_time": "30 minuter",
                "xp_reward": 100
            }
        },
        {
            "type": "concepts",
            "content": {
                "concepts": [
                    {
                        "title": "Funktionsdeklaration",
                        "explanation": """```bash
# Standard syntax (rekommenderas)
my_function() {
    echo "Hello from function"
}

# Alternativ syntax
function my_function {
    echo "Hello from function"
}

# Anropa funktionen
my_function
```

**Viktigt:** Funktionen måste definieras INNAN den anropas!""",
                        "pro_tip": "Använd snake_case för funktionsnamn för läsbarhet"
                    },
                    {
                        "title": "Arguments",
                        "explanation": """```bash
greet() {
    local name="$1"      # Första argumentet
    local greeting="$2"  # Andra argumentet

    echo "$greeting, $name!"
}

greet "DevOps" "Hello"  # Output: Hello, DevOps!

# Speciella variabler
show_args() {
    echo "Function: $FUNCNAME"
    echo "Arg count: $#"
    echo "All args: $@"
    echo "All as string: $*"
}
```""",
                        "common_mistake": "Glöm inte att argumenten är positionella ($1, $2...) - det finns inga namngivna parametrar i Bash"
                    },
                    {
                        "title": "Return Values",
                        "explanation": """```bash
# return ger exit status (0-255)
is_even() {
    local num="$1"
    if (( num % 2 == 0 )); then
        return 0  # Success/true
    else
        return 1  # Failure/false
    fi
}

if is_even 4; then
    echo "Even!"
fi

# För att returnera data - använd echo
get_timestamp() {
    date +%s
}

timestamp=$(get_timestamp)
echo "Timestamp: $timestamp"
```""",
                        "pro_tip": "return är för exit status (success/failure). Använd echo/printf för att returnera faktisk data."
                    },
                    {
                        "title": "Local Variables",
                        "explanation": """```bash
# UTAN local - variabeln läcker ut
bad_func() {
    leaked="I escaped!"
}
bad_func
echo "$leaked"  # "I escaped!" - BAD!

# MED local - isolerad till funktionen
good_func() {
    local contained="I stay here"
    echo "$contained"
}
good_func
echo "$contained"  # Tom - som det ska vara
```""",
                        "common_mistake": "ALLTID använd local för variabler i funktioner om de inte avsiktligt ska vara globala"
                    },
                    {
                        "title": "Utility Functions Pattern",
                        "explanation": """```bash
# Logging functions
log_info() {
    echo "[INFO] $(date +%H:%M:%S) $*"
}

log_error() {
    echo "[ERROR] $(date +%H:%M:%S) $*" >&2
}

# Die function - log and exit
die() {
    log_error "$@"
    exit 1
}

# Usage
log_info "Starting deployment"
[[ -f config.yaml ]] || die "Config not found"
```""",
                        "pro_tip": "Skapa ett library med utility-funktioner som du kan sourca i alla dina scripts"
                    }
                ]
            }
        },
        {
            "type": "practice",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa en enkel funktion",
                        "instruction": "Skapa funktionen hello som skriver 'Hello World'",
                        "expected_command": "hello() { echo 'Hello World'; }; hello",
                        "hint": "Semikolon separerar statements på en rad"
                    },
                    {
                        "task": "Funktion med argument",
                        "instruction": "Skapa greet som tar ett namn och hälsar",
                        "expected_command": "greet() { echo \"Hello, $1\"; }; greet DevOps",
                        "hint": "$1 är första argumentet"
                    },
                    {
                        "task": "Returnera data",
                        "instruction": "Skapa get_date som returnerar dagens datum",
                        "expected_command": "get_date() { date +%Y-%m-%d; }; today=$(get_date); echo $today",
                        "hint": "Använd command substitution för att fånga output"
                    }
                ]
            }
        },
        {
            "type": "quiz",
            "content": {
                "questions": {
                    "multiple_choice": [
                        {
                            "question": "Hur får du tredje argumentet i en funktion?",
                            "options": ["$3", "args[3]", "${3}", "$arg3"],
                            "correct": 0,
                            "explanation": "Argument nås via $1, $2, $3 etc. $3 ger tredje argumentet."
                        },
                        {
                            "question": "Vad är rätt sätt att returnera en sträng från en funktion?",
                            "options": [
                                "return 'string'",
                                "echo 'string'",
                                "yield 'string'",
                                "output 'string'"
                            ],
                            "correct": 1,
                            "explanation": "return ger bara exit status (0-255). Använd echo och command substitution för data."
                        },
                        {
                            "question": "Varför ska man använda 'local' i funktioner?",
                            "options": [
                                "Det är snabbare",
                                "Det förhindrar att variabler läcker ut",
                                "Det är obligatoriskt",
                                "Det gör variabler konstanta"
                            ],
                            "correct": 1,
                            "explanation": "local isolerar variabler till funktionen och förhindrar oavsiktlig påverkan på globala variabler."
                        }
                    ]
                }
            }
        },
        {
            "type": "challenge",
            "content": {
                "scenario": "Skapa ett library med deployment-hjälpfunktioner",
                "requirements": [
                    "log_info och log_error funktioner",
                    "die funktion som loggar och exiterar",
                    "check_command som verifierar att ett kommando finns",
                    "Alla ska använda local för variabler"
                ],
                "hints": [
                    "command -v kollar om kommando finns",
                    ">&2 skickar output till stderr",
                    "exit 1 för fel"
                ],
                "solution": """#!/usr/bin/env bash
# deployment_lib.sh

log_info() {
    local msg="$*"
    echo "[INFO] $(date +%H:%M:%S) $msg"
}

log_error() {
    local msg="$*"
    echo "[ERROR] $(date +%H:%M:%S) $msg" >&2
}

die() {
    log_error "$@"
    exit 1
}

check_command() {
    local cmd="$1"
    if ! command -v "$cmd" &>/dev/null; then
        die "Required command not found: $cmd"
    fi
    log_info "Found: $cmd"
}

# Usage
check_command docker
check_command kubectl
log_info "All dependencies satisfied!"""
            }
        }
    ]
}
