"""
Bash Studyflow Data
Flashcards och Multiple Choice för Bash Scripting
"""

BASH_MODULE = {
    "slug": "bash",
    "title": "Bash Scripting",
    "description": "Shell scripting och automation",
    "icon": "Terminal",
    "topics": [
        {
            "id": "bash-basics",
            "title": "Bash Basics",
            "flashcards": [
                {"front": "Hur börjar ett bash-script?", "back": "#!/bin/bash (shebang)"},
                {"front": "Hur kör man ett script?", "back": "chmod +x script.sh && ./script.sh"},
                {"front": "Hur skriver man ut text?", "back": "echo 'text' eller printf 'text'"},
                {"front": "Hur kommenterar man i bash?", "back": "# för enkelrad, : ' text ' för multirad"},
                {"front": "Vad är exit code 0?", "back": "Framgång - kommandot lyckades"},
            ],
            "multiple_choice": [
                {
                    "question": "Vad kallas första raden #!/bin/bash?",
                    "options": ["Header", "Shebang", "Comment", "Import"],
                    "correct": 1,
                    "explanation": "Shebang (#!) talar om vilken interpretator som ska köra scriptet."
                },
                {
                    "question": "Vad betyder exit code 0?",
                    "options": ["Fel", "Framgång", "Varning", "Timeout"],
                    "correct": 1,
                    "explanation": "Exit code 0 betyder att kommandot kördes utan fel."
                },
            ]
        },
        {
            "id": "bash-variables",
            "title": "Variables",
            "flashcards": [
                {"front": "Hur skapar man en variabel?", "back": "NAME='value' (utan mellanslag)"},
                {"front": "Hur använder man en variabel?", "back": "$NAME eller ${NAME}"},
                {"front": "Vad är $1, $2, $3?", "back": "Positionsparametrar (argument till script)"},
                {"front": "Vad är $#?", "back": "Antal argument"},
                {"front": "Vad är $@?", "back": "Alla argument som lista"},
                {"front": "Vad är $??", "back": "Exit code från förra kommandot"},
            ],
            "multiple_choice": [
                {
                    "question": "Hur refererar man till en variabel?",
                    "options": ["NAME", "$NAME", "%NAME%", "@NAME"],
                    "correct": 1,
                    "explanation": "I bash används $ framför variabelnamnet för att få värdet."
                },
                {
                    "question": "Vad innehåller $0?",
                    "options": ["Första argumentet", "Scriptets namn", "Exit code", "Process ID"],
                    "correct": 1,
                    "explanation": "$0 innehåller namnet på scriptet som körs."
                },
            ]
        },
        {
            "id": "bash-conditionals",
            "title": "Conditionals (if/else)",
            "flashcards": [
                {"front": "Syntax för if-sats?", "back": "if [ condition ]; then ... fi"},
                {"front": "Vad testar -f?", "back": "Om filen finns och är en vanlig fil"},
                {"front": "Vad testar -d?", "back": "Om katalogen finns"},
                {"front": "Vad testar -z?", "back": "Om strängen är tom"},
                {"front": "Vad testar -eq?", "back": "Om två tal är lika (equal)"},
            ],
            "multiple_choice": [
                {
                    "question": "Hur avslutas en if-sats i bash?",
                    "options": ["end", "endif", "fi", "}"],
                    "correct": 2,
                    "explanation": "fi (if baklänges) avslutar if-satser i bash."
                },
                {
                    "question": "Vad testar [ -f /etc/passwd ]?",
                    "options": ["Om filen är körbar", "Om filen finns", "Om filen är tom", "Om filen är en katalog"],
                    "correct": 1,
                    "explanation": "-f testar om path är en existerande fil."
                },
            ]
        },
        {
            "id": "bash-loops",
            "title": "Loops",
            "flashcards": [
                {"front": "For-loop syntax?", "back": "for i in 1 2 3; do ... done"},
                {"front": "While-loop syntax?", "back": "while [ condition ]; do ... done"},
                {"front": "Hur loopar man över filer?", "back": "for f in *.txt; do ... done"},
                {"front": "Hur bryter man en loop?", "back": "break"},
                {"front": "Hur hoppar man till nästa iteration?", "back": "continue"},
            ],
            "multiple_choice": [
                {
                    "question": "Hur avslutas en loop i bash?",
                    "options": ["end", "endfor", "done", "}"],
                    "correct": 2,
                    "explanation": "done avslutar for och while-loopar i bash."
                },
                {
                    "question": "Vad gör 'break' i en loop?",
                    "options": ["Pausar loopen", "Avslutar loopen", "Startar om loopen", "Hoppar över iteration"],
                    "correct": 1,
                    "explanation": "break avslutar loopen omedelbart."
                },
            ]
        },
        {
            "id": "bash-functions",
            "title": "Functions",
            "flashcards": [
                {"front": "Hur definierar man en funktion?", "back": "function_name() { ... }"},
                {"front": "Hur anropar man en funktion?", "back": "function_name arg1 arg2"},
                {"front": "Hur returnerar man värde?", "back": "return 0 (exit code) eller echo för output"},
                {"front": "Vad är $1 i en funktion?", "back": "Första argumentet till funktionen"},
                {"front": "Hur gör man variabel lokal?", "back": "local varname='value'"},
            ],
            "multiple_choice": [
                {
                    "question": "Hur definierar man en funktion i bash?",
                    "options": ["def name():", "function name {}", "name() {}", "func name()"],
                    "correct": 2,
                    "explanation": "name() { commands; } är standardsyntax för bash-funktioner."
                },
                {
                    "question": "Vad gör 'local' i en funktion?",
                    "options": ["Exporterar variabeln", "Gör variabeln global", "Begränsar scope till funktionen", "Tar bort variabeln"],
                    "correct": 2,
                    "explanation": "local begränsar variabelns scope till funktionen."
                },
            ]
        },
        {
            "id": "bash-arrays",
            "title": "Arrays",
            "flashcards": [
                {"front": "Hur skapar man en array?", "back": "arr=(val1 val2 val3)"},
                {"front": "Hur får man första elementet?", "back": "${arr[0]}"},
                {"front": "Hur får man alla element?", "back": "${arr[@]}"},
                {"front": "Hur får man array-längd?", "back": "${#arr[@]}"},
                {"front": "Hur lägger man till element?", "back": "arr+=(newval)"},
            ],
            "multiple_choice": [
                {
                    "question": "Hur får man första elementet i array?",
                    "options": ["$arr[0]", "${arr[0]}", "arr(0)", "$arr.0"],
                    "correct": 1,
                    "explanation": "${arr[0]} med curly braces krävs för array-access."
                },
                {
                    "question": "Vad ger ${#arr[@]}?",
                    "options": ["Första elementet", "Sista elementet", "Antal element", "Alla element"],
                    "correct": 2,
                    "explanation": "# framför ger längden/antal element i arrayen."
                },
            ]
        },
        {
            "id": "bash-text-processing",
            "title": "Text Processing",
            "flashcards": [
                {"front": "Vad gör grep?", "back": "Söker efter mönster i text"},
                {"front": "Vad gör sed?", "back": "Stream editor - ersätter text"},
                {"front": "Vad gör awk?", "back": "Kraftfullt verktyg för textbearbetning"},
                {"front": "Vad gör cut?", "back": "Klipper ut kolumner från text"},
                {"front": "Vad gör sort?", "back": "Sorterar rader"},
            ],
            "multiple_choice": [
                {
                    "question": "Vilket kommando söker efter mönster i filer?",
                    "options": ["find", "grep", "search", "locate"],
                    "correct": 1,
                    "explanation": "grep (Global Regular Expression Print) söker efter mönster."
                },
                {
                    "question": "Vad gör 'sed s/old/new/g'?",
                    "options": ["Söker efter old", "Ersätter old med new", "Tar bort old", "Lägger till new"],
                    "correct": 1,
                    "explanation": "sed s/old/new/g ersätter alla förekomster av old med new."
                },
            ]
        },
    ]
}
