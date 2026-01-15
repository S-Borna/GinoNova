/**
 * NOD 6: Bash Skriptprogrammering - SCENARIO Questions
 * 20 verklighetstrogna scenariofrågor
 */

import type { Omtenta2Question } from './omtenta-2.0-quiz'

export const SCENARIO_NOD6_QUESTIONS: Omtenta2Question[] = [
    {
        id: 'nod6-s1',
        question: 'Du skriver ett skript och behöver läsa första argumentet som användaren skickar in. Vilken variabel?',
        options: ['$0', '$1', '$@', '$#'],
        correctIndices: [1],
        explanation: '$1 = första arg, $2 = andra, etc. $0 = skriptnamnet, $@ = alla args, $# = antal args.',
        difficulty: 'G',
        category: 'Variabler',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s2',
        question: 'Du vill loopa igenom alla argument till skriptet och processa dem ett i taget. Hur tar du bort första argumentet efter varje iteration?',
        options: ['remove $1', 'shift', 'pop', 'next'],
        correctIndices: [1],
        explanation: 'shift flyttar alla positionsparametrar ett steg vänster. $2 blir $1, $3 blir $2, etc.',
        difficulty: 'VG',
        category: 'Argument',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s3',
        question: 'Du skriver if-sats och vill kolla om en fil existerar. Vilken syntax?',
        options: ['if [ -f /path/file ]', 'if ( exists /path/file )', 'if file.exists(/path/file)', 'if -e /path/file then'],
        correctIndices: [0],
        explanation: '[ -f fil ] testar om fil existerar och är vanlig fil. -e testar bara existens, -d för katalog.',
        difficulty: 'G',
        category: 'Villkor',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s4',
        question: 'Vad gör syntaxen `[ ]` i bash egentligen? Det är ett alias för vilket kommando?',
        options: ['if', 'test', 'check', 'evaluate'],
        correctIndices: [1],
        explanation: '[ ] är en synonym för test-kommandot. [ -f fil ] = test -f fil. [[ ]] är bash-extension med mer features.',
        difficulty: 'VG',
        category: 'Villkor',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s5',
        question: 'Du vill fånga exit-koden från förra kommandot. Vilken variabel?',
        options: ['$!', '$?', '$-', '$_'],
        correctIndices: [1],
        explanation: '$? innehåller exit status från senaste kommando. 0 = success, annat = error.',
        difficulty: 'G',
        category: 'Variabler',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s6',
        question: 'Du vill loopa igenom siffrorna 1-10 i ditt skript. Vilken syntax?',
        options: ['for i = 1 to 10', 'for i in {1..10}; do ... done', 'for (i=1; i<=10; i++)', 'loop 1 10 do ... end'],
        correctIndices: [1],
        explanation: 'for i in {1..10} använder brace expansion. C-style for((i=1;i<=10;i++)) fungerar också i bash.',
        difficulty: 'G',
        category: 'Loopar',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s7',
        question: 'Du vill definiera en funktion i ditt skript. Korrekt syntax?',
        options: ['function backup { ... }', 'backup() { ... }', 'def backup() { ... }', 'Både A och B fungerar'],
        correctIndices: [3],
        explanation: 'Bash accepterar både function name { } och name() { }. Andra formatet är mer portabelt (POSIX).',
        difficulty: 'G',
        category: 'Funktioner',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s8',
        question: 'Du vill att skriptet ska avsluta direkt om något kommando failar. Vilken rad i början?',
        options: ['set -e', 'exit on error', 'strict mode', 'error_exit=true'],
        correctIndices: [0],
        explanation: 'set -e (errexit) avbryter vid första fel. Ofta kombinerat med set -u (undefined vars) och set -o pipefail.',
        difficulty: 'VG',
        category: 'Best Practice',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s9',
        question: 'Du behöver göra aritmetik: räkna ut 5+3 och spara i variabel. Syntax?',
        options: ['result=5+3', 'result=$((5+3))', 'result=$(5+3)', 'result=math(5+3)'],
        correctIndices: [1],
        explanation: '$((...)) är arithmetic expansion. result=5+3 sparar strängen "5+3". $((5+3)) beräknar till 8.',
        difficulty: 'G',
        category: 'Aritmetik',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s10',
        question: 'Du vill läsa user input och spara i variabel NAME. Kommando?',
        options: ['input NAME', 'NAME = readline()', 'read NAME', 'get NAME'],
        correctIndices: [2],
        explanation: 'read NAME väntar på input och sparar i NAME. read -p "Prompt: " NAME visar prompt först.',
        difficulty: 'G',
        category: 'Input',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s11',
        question: 'Du vill hantera flera case i ditt skript baserat på user input. Vilken konstruktion?',
        options: ['switch/case', 'case/esac', 'select/done', 'if/elif/fi'],
        correctIndices: [1],
        explanation: 'case $var in pattern) cmd;; esac är bash\'s switch-statement. Varje case avslutas med ;;',
        difficulty: 'VG',
        category: 'Villkor',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s12',
        question: 'Du vill jämföra två strängar i bash. Korrekt syntax?',
        options: ['if [ $a = $b ]', 'if [ "$a" = "$b" ]', 'if [ $a == $b ]', 'Alla utom A (quotes behövs)'],
        correctIndices: [3],
        explanation: 'Quotes krävs! Utan quotes kraschar scriptet om variabeln är tom. = och == fungerar i [ ].',
        difficulty: 'VG',
        category: 'Villkor',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s13',
        question: 'Vad är skillnaden mellan $VAR och ${VAR}?',
        options: ['Ingen skillnad', '${VAR} är säkrare vid strängkonkatenering', '${} är deprecated', '$VAR är snabbare'],
        correctIndices: [1],
        explanation: '${VAR} är tydligare: ${VAR}text vs $VARtext. ${VAR} stödjer också substitution som ${VAR:-default}.',
        difficulty: 'G',
        category: 'Variabler',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s14',
        question: 'Du vill sätta default-värde om variabel är tom. Syntax?',
        options: ['$VAR || "default"', '${VAR:-default}', '${VAR:=default}', 'Både B och C (men olika)'],
        correctIndices: [3],
        explanation: '${VAR:-default} returnerar default men ändrar inte VAR. ${VAR:=default} sätter också VAR till default.',
        difficulty: 'VG',
        category: 'Variabler',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s15',
        question: 'Du vill skriva ut "Hello World" utan radbrytning. Echo-kommando?',
        options: ['echo "Hello World"', 'echo -n "Hello World"', 'echo -e "Hello World"', 'print "Hello World"'],
        correctIndices: [1],
        explanation: '-n = no newline. Nästa output kommer på samma rad. -e tolkar escape-sekvenser som \\n.',
        difficulty: 'G',
        category: 'Output',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s16',
        question: 'Du vill loopa så länge en fil INTE existerar (vänta på fil). Syntax?',
        options: ['while not [ -f fil ]', 'while [ ! -f fil ]; do ... done', 'until [ -f fil ]; do ... done', 'Både B och C fungerar'],
        correctIndices: [3],
        explanation: '! negerar test. until loopar tills villkoret är sant (motsatsen till while).',
        difficulty: 'VG',
        category: 'Loopar',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s17',
        question: 'Du vill spara output från ett kommando i en variabel. Syntax?',
        options: ['result=$(ls -la)', 'result=`ls -la`', 'result=$[ls -la]', 'Både A och B fungerar'],
        correctIndices: [3],
        explanation: '$() och backticks ` ` gör command substitution. $() är modernare och nestlar bättre.',
        difficulty: 'G',
        category: 'Substitution',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s18',
        question: 'Vad betyder shebang-raden #!/bin/bash i början av skriptet?',
        options: ['En kommentar', 'Anger vilken tolk som ska köra skriptet', 'Importerar bash-bibliotek', 'Aktiverar debug-mode'],
        correctIndices: [1],
        explanation: 'Shebang (#!) anger interpreter. Systemet läser denna och kör /bin/bash script.sh automatiskt.',
        difficulty: 'G',
        category: 'Grunder',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s19',
        question: 'Du vill loopa igenom alla .log filer i en katalog. Syntax?',
        options: ['for f in /var/log/*.log', 'foreach f in /var/log/*.log', 'loop /var/log/*.log as f', 'for f = /var/log/*.log'],
        correctIndices: [0],
        explanation: 'Shell expanderar *.log till alla matchande filer. for f in pattern; do ... done itererar.',
        difficulty: 'G',
        category: 'Loopar',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    },
    {
        id: 'nod6-s20',
        question: 'Du vill returnera värde från funktion och fånga det. Hur?',
        options: ['return värde; x=$(funktion)', 'echo värde; x=$(funktion)', 'funktion returnerar automatiskt', 'set x = funktion()'],
        correctIndices: [1],
        explanation: 'return sätter exit-kod (0-255). För att returnera värden: echo i funktionen, fånga med $().',
        difficulty: 'VG',
        category: 'Funktioner',
        topic: 'nod6-bash-skript',
        type: 'scenario'
    }
]
