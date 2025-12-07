"""
Bash Nodes 6-10: I/O & Text Processing (V2 Format)
==================================================
"""

NODE_BASH_06_INPUT_OUTPUT_V2 = {
    "id": "bash-06-io",
    "title": "Input/Output & Redirection",
    "slug": "bash-io-redirection",
    "description": "Master stdin, stdout, stderr, and redirection operators",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 120,
    "sections": [
        {"type": "intro", "content": {
            "headline": "Input/Output & Redirection",
            "hook": "Data flödar genom dina scripts. Kontrollera flödet och du kontrollerar allt.",
            "learning_objectives": ["Förstå stdin, stdout och stderr", "Använda redirection operators", "Kombinera streams med tee och pipes"],
            "prerequisites": ["Bash Functions"],
            "estimated_time": "35 minuter", "xp_reward": 120
        }},
        {"type": "concepts", "content": {"concepts": [
            {"title": "File Descriptors", "explanation": """**Standard streams:**
- `stdin` (0) - Input
- `stdout` (1) - Normal output
- `stderr` (2) - Error output

```bash
echo "Hello"      # Skriver till stdout
echo "Error" >&2  # Skriver till stderr
read name         # Läser från stdin
```"""},
            {"title": "Output Redirection", "explanation": """```bash
# Skriv till fil (överskriver)
echo "Hello" > file.txt

# Append till fil
echo "World" >> file.txt

# Redirect stderr
command 2> errors.log

# Redirect båda
command > output.log 2>&1

# Kortform för båda
command &> all.log

# Discard output
command > /dev/null 2>&1
```""", "pro_tip": "2>&1 betyder 'skicka stderr till samma ställe som stdout'"},
            {"title": "Input Redirection", "explanation": """```bash
# Läs från fil
while read line; do
    echo "$line"
done < file.txt

# Here-document
cat << EOF
Multi-line
content here
EOF

# Here-string
grep "pattern" <<< "search in this string"
```"""}
        ]}},
        {"type": "practice", "content": {"exercises": [
            {"task": "Redirect output till fil", "instruction": "Skriv 'Hello' till hello.txt", "expected_command": "echo 'Hello' > hello.txt", "hint": "> skapar/överskriver filen"},
            {"task": "Append till fil", "instruction": "Lägg till 'World' i hello.txt", "expected_command": "echo 'World' >> hello.txt", "hint": ">> appendar"},
            {"task": "Discard errors", "instruction": "Kör ls på en fil som inte finns och tysta felet", "expected_command": "ls nonexistent 2>/dev/null", "hint": "2> redirectar stderr"}
        ]}},
        {"type": "quiz", "content": {"questions": {"multiple_choice": [
            {"question": "Vad gör 2>&1?", "options": ["Redirect stdin till fil 1", "Redirect stderr till stdout", "Redirect stdout till fil 2", "Skapar två filer"], "correct": 1, "explanation": "2>&1 skickar stderr (2) till samma destination som stdout (1)."},
            {"question": "Vilken operator appendar till fil?", "options": [">", ">>", ">>>", "->"], "correct": 1, "explanation": ">> appendar. > överskriver filen."}
        ]}}},
        {"type": "challenge", "content": {
            "scenario": "Logga både output och fel separat medan du visar i terminalen",
            "requirements": ["Kör ett kommando", "Visa output i terminalen", "Spara stdout till success.log", "Spara stderr till error.log"],
            "hints": ["tee duplicerar output", "Process substitution med >()"],
            "solution": "command 2> >(tee error.log >&2) | tee success.log"
        }}
    ]
}

NODE_BASH_07_PIPES_V2 = {
    "id": "bash-07-pipes",
    "title": "Pipes & Command Chaining",
    "slug": "bash-pipes",
    "description": "Chain commands together for powerful data processing",
    "difficulty": "intermediate",
    "estimated_minutes": 30,
    "xp_reward": 100,
    "sections": [
        {"type": "intro", "content": {
            "headline": "Pipes & Command Chaining",
            "hook": "Unix-filosofin: små verktyg som gör en sak bra, sammankopplade med pipes.",
            "learning_objectives": ["Använda pipes för dataflöde", "Kedja kommandon med && och ||", "Använda xargs för batch-processing"],
            "prerequisites": ["Bash I/O"], "estimated_time": "30 minuter", "xp_reward": 100
        }},
        {"type": "concepts", "content": {"concepts": [
            {"title": "Basic Pipes", "explanation": """```bash
# Output från ett kommando -> input till nästa
cat file.txt | grep "error" | wc -l

# Vanliga mönster
ps aux | grep nginx
docker ps | awk '{print $1}'
ls -la | sort -k5 -n
```"""},
            {"title": "Command Chaining", "explanation": """```bash
# && - kör nästa OM föregående lyckas
mkdir dir && cd dir && touch file

# || - kör nästa OM föregående misslyckas
command || echo "Command failed"

# ; - kör alltid nästa (oavsett)
command1; command2; command3

# Kombinera
command && echo "Success" || echo "Failed"
```""", "pro_tip": "&& och || är perfekta för one-liners och felhantering"},
            {"title": "xargs", "explanation": """```bash
# Konvertera stdin till argument
find . -name "*.log" | xargs rm

# Med placeholder
echo "a b c" | xargs -I {} echo "Item: {}"

# Parallell execution
find . -name "*.txt" | xargs -P 4 -I {} gzip {}

# Safe med null-separator
find . -name "*.log" -print0 | xargs -0 rm
```""", "common_mistake": "Använd -print0 och xargs -0 för filer med spaces"}
        ]}},
        {"type": "practice", "content": {"exercises": [
            {"task": "Räkna processer", "instruction": "Räkna antal körande processer", "expected_command": "ps aux | wc -l", "hint": "wc -l räknar rader"},
            {"task": "Hitta och ta bort", "instruction": "Hitta alla .tmp filer och ta bort dem", "expected_command": "find . -name '*.tmp' | xargs rm", "hint": "xargs konverterar till argument"}
        ]}},
        {"type": "quiz", "content": {"questions": {"multiple_choice": [
            {"question": "Vad gör command1 && command2?", "options": ["Kör båda parallellt", "Kör command2 bara om command1 lyckas", "Kör command2 bara om command1 misslyckas", "Pipe output"], "correct": 1, "explanation": "&& kör nästa kommando endast om föregående returnerade exit code 0."}
        ]}}}
    ]
}

NODE_BASH_08_TEXT_PROCESSING_V2 = {
    "id": "bash-08-text",
    "title": "Text Processing: grep, sed, awk",
    "slug": "bash-text-processing",
    "description": "Master the holy trinity of text processing",
    "difficulty": "intermediate",
    "estimated_minutes": 45,
    "xp_reward": 150,
    "sections": [
        {"type": "intro", "content": {
            "headline": "Text Processing: grep, sed, awk",
            "hook": "Loggar, config-filer, output - allt är text. Dessa verktyg är dina superkrafter.",
            "learning_objectives": ["Söka med grep och regex", "Transformera text med sed", "Processa strukturerad data med awk"],
            "prerequisites": ["Bash Pipes"], "estimated_time": "45 minuter", "xp_reward": 150
        }},
        {"type": "concepts", "content": {"concepts": [
            {"title": "grep - Search", "explanation": """```bash
grep "pattern" file.txt       # Basic search
grep -i "pattern" file.txt    # Case insensitive
grep -r "pattern" dir/        # Recursive
grep -v "pattern" file.txt    # Invert (exclude)
grep -n "pattern" file.txt    # Show line numbers
grep -c "pattern" file.txt    # Count matches
grep -E "regex" file.txt      # Extended regex
grep -o "pattern" file.txt    # Only matching part
```""", "pro_tip": "grep -E är samma som egrep och ger kraftfullare regex"},
            {"title": "sed - Transform", "explanation": """```bash
# Substitute
sed 's/old/new/' file         # First occurrence per line
sed 's/old/new/g' file        # All occurrences
sed -i 's/old/new/g' file     # In-place edit

# Delete lines
sed '/pattern/d' file         # Delete matching lines
sed '1d' file                 # Delete first line
sed '1,5d' file               # Delete lines 1-5

# Print specific lines
sed -n '5p' file              # Print line 5
sed -n '5,10p' file           # Print lines 5-10
```""", "common_mistake": "På macOS kräver -i en backup extension: sed -i '' 's/old/new/g' file"},
            {"title": "awk - Process", "explanation": """```bash
# Print columns
awk '{print $1}' file          # First column
awk '{print $1, $3}' file      # First and third
awk '{print $NF}' file         # Last column

# With delimiter
awk -F: '{print $1}' /etc/passwd

# Conditions
awk '$3 > 100 {print $1}' file

# Built-in variables
awk '{print NR, $0}' file      # Line number + line
awk 'END {print NR}' file      # Total lines
```""", "pro_tip": "awk är ett komplett programmeringsspråk - du kan göra conditions, loops och funktioner"}
        ]}},
        {"type": "practice", "content": {"exercises": [
            {"task": "Hitta fel i loggar", "instruction": "Sök efter 'ERROR' case-insensitive", "expected_command": "grep -i 'ERROR' /var/log/syslog", "hint": "-i för case insensitive"},
            {"task": "Ersätt text", "instruction": "Byt 'localhost' mot '127.0.0.1' i config", "expected_command": "sed 's/localhost/127.0.0.1/g' config.txt", "hint": "g för global replacement"},
            {"task": "Extrahera kolumn", "instruction": "Visa bara första kolumnen i /etc/passwd", "expected_command": "awk -F: '{print $1}' /etc/passwd", "hint": "-F: sätter delimiter till :"}
        ]}},
        {"type": "quiz", "content": {"questions": {"multiple_choice": [
            {"question": "Vad gör grep -v?", "options": ["Verbose output", "Visar bara matchande", "Inverterar - visar icke-matchande", "Verifierar pattern"], "correct": 2, "explanation": "-v (invert) visar rader som INTE matchar."},
            {"question": "I awk, vad är $NF?", "options": ["Number of fields", "Sista fältet", "New field", "Next file"], "correct": 1, "explanation": "$NF är sista fältet (NF = Number of Fields, $NF = värdet av fält NF)."}
        ]}}}
    ]
}

NODE_BASH_09_REGEX_V2 = {
    "id": "bash-09-regex",
    "title": "Regular Expressions",
    "slug": "bash-regex",
    "description": "Master pattern matching with regular expressions",
    "difficulty": "intermediate",
    "estimated_minutes": 40,
    "xp_reward": 130,
    "sections": [
        {"type": "intro", "content": {
            "headline": "Regular Expressions",
            "hook": "Regex är det kraftfullaste verktyget för textmatchning. Svårt att lära, omöjligt att leva utan.",
            "learning_objectives": ["Förstå regex-syntax", "Använda character classes och quantifiers", "Praktisera med grep, sed och Bash conditionals"],
            "prerequisites": ["Bash Text Processing"], "estimated_time": "40 minuter", "xp_reward": 130
        }},
        {"type": "concepts", "content": {"concepts": [
            {"title": "Basic Patterns", "explanation": """```bash
.       # Matchar ett tecken
^       # Start av rad
$       # Slut på rad
*       # Noll eller fler
+       # En eller fler (extended)
?       # Noll eller en (extended)
\\       # Escape special character
```"""},
            {"title": "Character Classes", "explanation": """```bash
[abc]     # a, b, eller c
[^abc]    # INTE a, b, eller c
[a-z]     # Lowercase letters
[0-9]     # Digits
[A-Za-z]  # All letters

# POSIX classes
[[:alnum:]]   # Alphanumeric
[[:alpha:]]   # Letters
[[:digit:]]   # Digits
[[:space:]]   # Whitespace
```"""},
            {"title": "Praktiska Exempel", "explanation": """```bash
# Email (basic)
grep -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'

# IP-adress
grep -E '([0-9]{1,3}\\.){3}[0-9]{1,3}'

# Datum YYYY-MM-DD
grep -E '[0-9]{4}-[0-9]{2}-[0-9]{2}'

# I Bash conditional
if [[ "$email" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$ ]]; then
    echo "Valid email"
fi
```""", "pro_tip": "Testa dina regex på regex101.com innan du använder dem i scripts"}
        ]}},
        {"type": "quiz", "content": {"questions": {"multiple_choice": [
            {"question": "Vad matchar ^error?", "options": ["error var som helst", "error i början av raden", "rader som slutar med error", "error exakt"], "correct": 1, "explanation": "^ förankrar matchningen i början av raden."}
        ]}}}
    ]
}

NODE_BASH_10_STRING_MANIPULATION_V2 = {
    "id": "bash-10-strings",
    "title": "String Manipulation",
    "slug": "bash-strings",
    "description": "Master Bash parameter expansion for string operations",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 120,
    "sections": [
        {"type": "intro", "content": {
            "headline": "String Manipulation",
            "hook": "Bash har inbyggd stränghantering som är snabbare än att anropa externa kommandon.",
            "learning_objectives": ["Använda parameter expansion", "Substring extraction", "Search and replace patterns"],
            "prerequisites": ["Bash Regex"], "estimated_time": "35 minuter", "xp_reward": 120
        }},
        {"type": "concepts", "content": {"concepts": [
            {"title": "Parameter Expansion Basics", "explanation": """```bash
str="Hello World"

# Längd
echo ${#str}           # 11

# Substring
echo ${str:0:5}        # Hello (start:length)
echo ${str:6}          # World (from position 6)
echo ${str: -5}        # World (last 5, note space!)

# Default values
echo ${var:-default}   # Use default if unset
echo ${var:=default}   # Set AND use default if unset
echo ${var:+alt}       # Use alt if var IS set
echo ${var:?error}     # Error if unset
```""", "pro_tip": "${var:-default} är perfekt för optional config"},
            {"title": "Search & Replace", "explanation": """```bash
file="document.txt.bak"

# Remove pattern
echo ${file#*.}        # txt.bak (remove shortest from start)
echo ${file##*.}       # bak (remove longest from start)
echo ${file%.*}        # document.txt (remove shortest from end)
echo ${file%%.*}       # document (remove longest from end)

# Replace
str="hello hello hello"
echo ${str/hello/hi}   # hi hello hello (first)
echo ${str//hello/hi}  # hi hi hi (all)
```"""},
            {"title": "Case Conversion", "explanation": """```bash
str="Hello World"

echo ${str^^}    # HELLO WORLD (uppercase)
echo ${str,,}    # hello world (lowercase)
echo ${str^}     # Hello world (first char upper)
```"""}
        ]}},
        {"type": "practice", "content": {"exercises": [
            {"task": "Extrahera file extension", "instruction": "Få fram extensionen från 'app.tar.gz'", "expected_command": "f='app.tar.gz'; echo ${f##*.}", "hint": "## tar bort längsta matchningen från start"},
            {"task": "Sätt default", "instruction": "Använd 'production' om ENV är tom", "expected_command": "echo ${ENV:-production}", "hint": ":- ger default utan att sätta variabeln"}
        ]}},
        {"type": "quiz", "content": {"questions": {"multiple_choice": [
            {"question": "Vad ger ${file%.txt}?", "options": ["Tar bort .txt från slutet", "Lägger till .txt", "Kollar om filen slutar med .txt", "Byter ut .txt"], "correct": 0, "explanation": "% tar bort matchande pattern från slutet av strängen."}
        ]}}}
    ]
}
