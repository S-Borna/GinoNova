/**
 * DOE25 Tentaplugg - Flashcards
 * 10 flashcards per task för snabb repetition
 * Fokus på kommandon, koncept och vanliga frågor på tentan
 */

export interface Flashcard {
    id: string
    front: string
    back: string
    category: string
    difficulty: 'G' | 'VG'
}

export interface TaskFlashcardSet {
    taskId: string
    taskTitle: string
    flashcards: Flashcard[]
}

// =============================================================================
// TASK 1: SUBNETTING & NÄTVERK
// =============================================================================

const TASK_1_FLASHCARDS: Flashcard[] = [
    { id: 'f1-1', front: 'Hur många bitar är en IPv4-adress?', back: '32 bitar (4 oktetter × 8 bitar)', category: 'IPv4', difficulty: 'G' },
    { id: 'f1-2', front: 'Vad betyder /24 i CIDR-notation?', back: '24 nätverksbitar = 255.255.255.0 = 254 hosts', category: 'CIDR', difficulty: 'G' },
    { id: 'f1-3', front: 'Formel för antal hosts?', back: '2^(32-prefix) - 2\n(minus nätverksadress och broadcast)', category: 'Beräkning', difficulty: 'G' },
    { id: 'f1-4', front: 'Vilken IP-range är loopback?', back: '127.0.0.0/8\n(127.0.0.1 = localhost)', category: 'Reserverat', difficulty: 'G' },
    { id: 'f1-5', front: 'Kommando för att visa nätverksconfig?', back: 'ip addr show\n(eller ip a)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f1-6', front: 'Vad är broadcast-adressen för 192.168.1.0/24?', back: '192.168.1.255\n(alla hostbitar = 1)', category: 'Beräkning', difficulty: 'G' },
    { id: 'f1-7', front: 'Privata IP-ranges (RFC 1918)?', back: '10.0.0.0/8\n172.16.0.0/12\n192.168.0.0/16', category: 'Reserverat', difficulty: 'VG' },
    { id: 'f1-8', front: 'Hur många hosts i /30?', back: '2 hosts\n(2^2 - 2 = 2, används för punkt-till-punkt)', category: 'Beräkning', difficulty: 'VG' },
    { id: 'f1-9', front: 'Vad gör traceroute?', back: 'Visar alla hopp (routrar) på vägen till en destination', category: 'Kommandon', difficulty: 'G' },
    { id: 'f1-10', front: 'Dela 192.168.1.0/24 i 4 subnät - vilken prefix?', back: '/26\n(4 subnät = 2^2 = 2 extra bitar, /24+2=/26)', category: 'Beräkning', difficulty: 'VG' }
]

// =============================================================================
// TASK 2: LINUX FILSYSTEM
// =============================================================================

const TASK_2_FLASHCARDS: Flashcard[] = [
    { id: 'f2-1', front: 'Var lagras systemkonfiguration?', back: '/etc\n(Editable Text Config)', category: 'FHS', difficulty: 'G' },
    { id: 'f2-2', front: 'Var finns systemloggar?', back: '/var/log', category: 'FHS', difficulty: 'G' },
    { id: 'f2-3', front: 'Var finns användarnas hemkataloger?', back: '/home\n(/root för root-användaren)', category: 'FHS', difficulty: 'G' },
    { id: 'f2-4', front: 'Vad innehåller /etc/fstab?', back: 'Filsystem som monteras vid boot\n(File System Table)', category: 'Konfiguration', difficulty: 'VG' },
    { id: 'f2-5', front: 'Skillnad hård länk vs symbolisk länk?', back: 'Hård: delar inode, bryts ej\nSymbolisk: pekar på namn, bryts om original tas bort', category: 'Filtyper', difficulty: 'VG' },
    { id: 'f2-6', front: 'Vad är /dev/null?', back: 'Svart hål - slänger all data som skrivs dit\nAnvänds för att tysta output', category: 'Devices', difficulty: 'G' },
    { id: 'f2-7', front: 'Kommando för att visa diskutrymme per katalog?', back: 'du -sh /katalog\n(-s = summary, -h = human readable)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f2-8', front: 'Var installeras tredjepartsprogram?', back: '/opt eller /usr/local', category: 'FHS', difficulty: 'VG' },
    { id: 'f2-9', front: 'Vad gör sticky bit på /tmp?', back: 'Bara filägaren kan ta bort sin fil\n(chmod +t, visas som t i rwxrwxrwt)', category: 'Rättigheter', difficulty: 'VG' },
    { id: 'f2-10', front: 'Vad är inode?', back: 'Metadata om filen (rättigheter, storlek, etc.)\nFilnamn lagras separat i katalogen', category: 'Koncept', difficulty: 'VG' }
]

// =============================================================================
// TASK 3: BASH GRUNDER
// =============================================================================

const TASK_3_FLASHCARDS: Flashcard[] = [
    { id: 'f3-1', front: 'Vad är shebang?', back: '#!/bin/bash\nFörsta raden, talar om vilken tolk som ska köra skriptet', category: 'Syntax', difficulty: 'G' },
    { id: 'f3-2', front: 'Hur gör du ett skript exekverbart?', back: 'chmod +x script.sh', category: 'Kommandon', difficulty: 'G' },
    { id: 'f3-3', front: 'Vad returnerar $?', back: 'Exit code från senaste kommandot\n(0 = success, annat = error)', category: 'Variabler', difficulty: 'G' },
    { id: 'f3-4', front: 'Skillnad > vs >>?', back: '> = skriver över filen\n>> = lägger till i slutet', category: 'Redirection', difficulty: 'G' },
    { id: 'f3-5', front: 'Vad gör 2>&1?', back: 'Redirectar stderr (2) till samma ställe som stdout (1)', category: 'Redirection', difficulty: 'VG' },
    { id: 'f3-6', front: 'Vad gör &> fil?', back: 'Redirectar BÅDE stdout OCH stderr till fil', category: 'Redirection', difficulty: 'VG' },
    { id: 'f3-7', front: 'Vad gör set -e?', back: 'Avbryt skriptet vid första fel\n(exit vid icke-noll exit code)', category: 'Best practices', difficulty: 'VG' },
    { id: 'f3-8', front: 'Vad gör set -x?', back: 'Debug mode - skriver ut varje kommando innan det körs', category: 'Debug', difficulty: 'VG' },
    { id: 'f3-9', front: 'Vad gör tee?', back: 'Skriver till fil OCH stdout samtidigt\nEx: cmd | tee logfil', category: 'Kommandon', difficulty: 'VG' },
    { id: 'f3-10', front: 'Portabel shebang?', back: '#!/usr/bin/env bash\n(hittar bash i PATH)', category: 'Best practices', difficulty: 'G' }
]

// =============================================================================
// TASK 4: VARIABLER & DATATYPER
// =============================================================================

const TASK_4_FLASHCARDS: Flashcard[] = [
    { id: 'f4-1', front: 'Syntax för att tilldela variabel?', back: 'var=värde\n(INGA mellanslag runt =)', category: 'Syntax', difficulty: 'G' },
    { id: 'f4-2', front: 'Hur läser du en variabel?', back: '$var eller ${var}', category: 'Syntax', difficulty: 'G' },
    { id: 'f4-3', front: 'Skillnad \' och \"?', back: '\' = literal, ingen expansion\n\" = expanderar variabler', category: 'Citering', difficulty: 'G' },
    { id: 'f4-4', front: 'Hur exporterar du miljövariabel?', back: 'export VAR=värde', category: 'Miljövariabler', difficulty: 'G' },
    { id: 'f4-5', front: 'Vad gör ${var:-default}?', back: 'Returnerar default om var är tom/odefinierad', category: 'Expansion', difficulty: 'VG' },
    { id: 'f4-6', front: 'Hur får du längden på en sträng?', back: '${#var}', category: 'Stränghantering', difficulty: 'VG' },
    { id: 'f4-7', front: 'Hur gör du substring?', back: '${var:start:längd}\nEx: ${var:0:5} = första 5 tecken', category: 'Stränghantering', difficulty: 'VG' },
    { id: 'f4-8', front: 'Ersätt i sträng?', back: '${var/sök/ersätt} = första\n${var//sök/ersätt} = alla', category: 'Stränghantering', difficulty: 'VG' },
    { id: 'f4-9', front: 'Vad gör command substitution $()?', back: 'Fångar output från kommando\nEx: datum=$(date)', category: 'Expansion', difficulty: 'G' },
    { id: 'f4-10', front: 'Aritmetik i bash?', back: '$((uttryck))\nEx: sum=$((a + b))', category: 'Aritmetik', difficulty: 'G' }
]

// =============================================================================
// TASK 5: REGEX
// =============================================================================

const TASK_5_FLASHCARDS: Flashcard[] = [
    { id: 'f5-1', front: 'Vad matchar ^?', back: 'Början av rad', category: 'Ankare', difficulty: 'G' },
    { id: 'f5-2', front: 'Vad matchar $?', back: 'Slut på rad', category: 'Ankare', difficulty: 'G' },
    { id: 'f5-3', front: 'Vad matchar . (punkt)?', back: 'ETT valfritt tecken (utom newline)', category: 'Wildcards', difficulty: 'G' },
    { id: 'f5-4', front: 'Vad matchar .*?', back: 'Noll eller fler av vad som helst', category: 'Kvantifierare', difficulty: 'G' },
    { id: 'f5-5', front: 'Skillnad * + ??', back: '* = 0 eller fler\n+ = 1 eller fler\n? = 0 eller 1', category: 'Kvantifierare', difficulty: 'VG' },
    { id: 'f5-6', front: 'Vad matchar [a-z]?', back: 'ETT tecken a-z (lowercase)', category: 'Character class', difficulty: 'G' },
    { id: 'f5-7', front: 'Vad matchar [^abc]?', back: 'ETT tecken som INTE är a, b eller c', category: 'Character class', difficulty: 'VG' },
    { id: 'f5-8', front: 'Extended regex i grep?', back: 'grep -E\n(stödjer + ? | () utan escape)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f5-9', front: 'Matcha literal punkt?', back: '\\.\n(escape med backslash)', category: 'Escape', difficulty: 'G' },
    { id: 'f5-10', front: 'Alternation (OR)?', back: 'cat|dog matchar "cat" eller "dog"', category: 'Mönster', difficulty: 'VG' }
]

// =============================================================================
// TASK 6: SED
// =============================================================================

const TASK_6_FLASHCARDS: Flashcard[] = [
    { id: 'f6-1', front: 'sed ersätt-syntax?', back: 's/sök/ersätt/flaggor\nEx: s/old/new/g', category: 'Syntax', difficulty: 'G' },
    { id: 'f6-2', front: 'Vad gör g-flaggan?', back: 'Global - ersätt ALLA träffar per rad\n(utan g = bara första)', category: 'Flaggor', difficulty: 'G' },
    { id: 'f6-3', front: 'Vad gör sed -i?', back: 'In-place - ändrar filen direkt', category: 'Flaggor', difficulty: 'G' },
    { id: 'f6-4', front: 'Ta bort rader med mönster?', back: 'sed \'/mönster/d\' fil', category: 'Radering', difficulty: 'G' },
    { id: 'f6-5', front: 'Skriv ut specifik rad?', back: 'sed -n \'5p\' fil\n(-n = suppress, p = print)', category: 'Utskrift', difficulty: 'VG' },
    { id: 'f6-6', front: 'Ersätt endast rad 3?', back: 'sed \'3s/old/new/\' fil', category: 'Adressering', difficulty: 'VG' },
    { id: 'f6-7', front: 'Ersätt rad 1-5?', back: 'sed \'1,5s/old/new/\' fil', category: 'Adressering', difficulty: 'VG' },
    { id: 'f6-8', front: 'Annan avgränsare än /?', back: 's#old#new#g eller s|old|new|g\n(bra för sökvägar)', category: 'Tips', difficulty: 'VG' },
    { id: 'f6-9', front: 'Backreference i sed?', back: '\\1 refererar till första ()\nEx: s/\\(word\\)/[\\1]/g', category: 'Avancerat', difficulty: 'VG' },
    { id: 'f6-10', front: 'Ta bort tomma rader?', back: 'sed \'/^$/d\' fil', category: 'Vanliga', difficulty: 'G' }
]

// =============================================================================
// TASK 7: AWK
// =============================================================================

const TASK_7_FLASHCARDS: Flashcard[] = [
    { id: 'f7-1', front: 'Vad är $0 i awk?', back: 'Hela raden', category: 'Variabler', difficulty: 'G' },
    { id: 'f7-2', front: 'Vad är $1, $2 etc?', back: 'Kolumn 1, 2 etc (space-separerade)', category: 'Variabler', difficulty: 'G' },
    { id: 'f7-3', front: 'Vad är $NF?', back: 'Sista kolumnen', category: 'Variabler', difficulty: 'G' },
    { id: 'f7-4', front: 'Vad är NR?', back: 'Radnummer (Number of Record)', category: 'Variabler', difficulty: 'G' },
    { id: 'f7-5', front: 'Ändra fältavgränsare?', back: 'awk -F:\nEx: awk -F: \'{print $1}\' /etc/passwd', category: 'Flaggor', difficulty: 'G' },
    { id: 'f7-6', front: 'Villkor i awk?', back: 'awk \'$3 > 100 {print $1}\'', category: 'Villkor', difficulty: 'VG' },
    { id: 'f7-7', front: 'Summera kolumn?', back: 'awk \'{sum += $1} END {print sum}\'', category: 'Beräkning', difficulty: 'VG' },
    { id: 'f7-8', front: 'BEGIN och END?', back: 'BEGIN körs före första raden\nEND körs efter sista', category: 'Block', difficulty: 'VG' },
    { id: 'f7-9', front: 'Skriv ut rad 5-10?', back: 'awk \'NR>=5 && NR<=10\'', category: 'Villkor', difficulty: 'VG' },
    { id: 'f7-10', front: 'Lista alla användarnamn?', back: 'awk -F: \'{print $1}\' /etc/passwd', category: 'Vanliga', difficulty: 'G' }
]

// =============================================================================
// TASK 8: VILLKOR (if/else)
// =============================================================================

const TASK_8_FLASHCARDS: Flashcard[] = [
    { id: 'f8-1', front: 'if-syntax i bash?', back: 'if [ villkor ]; then\n  ...\nfi', category: 'Syntax', difficulty: 'G' },
    { id: 'f8-2', front: 'Numerisk jämförelse?', back: '-eq -ne -lt -le -gt -ge', category: 'Operatorer', difficulty: 'G' },
    { id: 'f8-3', front: 'Strängjämförelse?', back: '= !=\n(eller == i [[ ]])', category: 'Operatorer', difficulty: 'G' },
    { id: 'f8-4', front: 'Kolla om fil finns?', back: '[ -f filnamn ]', category: 'Tester', difficulty: 'G' },
    { id: 'f8-5', front: 'Kolla om katalog finns?', back: '[ -d katalog ]', category: 'Tester', difficulty: 'G' },
    { id: 'f8-6', front: 'Skillnad [ ] och [[ ]]?', back: '[[ ]] är modernare\nStödjer && || och regex', category: 'Syntax', difficulty: 'VG' },
    { id: 'f8-7', front: 'AND i test?', back: '[ $a -eq 1 ] && [ $b -eq 2 ]\neller [[ $a -eq 1 && $b -eq 2 ]]', category: 'Logik', difficulty: 'VG' },
    { id: 'f8-8', front: 'Kolla om sträng är tom?', back: '[ -z "$var" ]\n(zero length)', category: 'Tester', difficulty: 'G' },
    { id: 'f8-9', front: 'Kolla om sträng inte är tom?', back: '[ -n "$var" ]\n(non-zero)', category: 'Tester', difficulty: 'G' },
    { id: 'f8-10', front: 'case-syntax?', back: 'case $var in\n  pattern) cmd ;;\n  *) default ;;\nesac', category: 'Syntax', difficulty: 'VG' }
]

// =============================================================================
// TASK 9: INTERAKTIVA SKRIPT
// =============================================================================

const TASK_9_FLASHCARDS: Flashcard[] = [
    { id: 'f9-1', front: 'Läs input från användaren?', back: 'read variabel', category: 'Input', difficulty: 'G' },
    { id: 'f9-2', front: 'Läs med prompt?', back: 'read -p "Fråga: " var', category: 'Input', difficulty: 'G' },
    { id: 'f9-3', front: 'Dold input (lösenord)?', back: 'read -s variabel\n(silent/secret)', category: 'Input', difficulty: 'G' },
    { id: 'f9-4', front: 'Timeout på input?', back: 'read -t 5 var\n(5 sekunder)', category: 'Input', difficulty: 'VG' },
    { id: 'f9-5', front: 'Skapa numrerad meny?', back: 'select val in alt1 alt2; do\n  ...\ndone', category: 'Meny', difficulty: 'VG' },
    { id: 'f9-6', front: 'Validera numerisk input?', back: '[[ $var =~ ^[0-9]+$ ]]', category: 'Validering', difficulty: 'VG' },
    { id: 'f9-7', front: 'Läs in hela raden med mellanslag?', back: 'read -r line\n(-r = raw, no backslash escape)', category: 'Input', difficulty: 'VG' },
    { id: 'f9-8', front: 'Ge variabel defaultvärde?', back: 'read -p "Port [8080]: " port\nport=${port:-8080}', category: 'Tips', difficulty: 'VG' },
    { id: 'f9-9', front: 'Fråga ja/nej?', back: 'read -p "Continue? [y/n] " svar\n[[ $svar =~ ^[Yy] ]]', category: 'Vanliga', difficulty: 'G' },
    { id: 'f9-10', front: 'PS3-variabel i select?', back: 'PS3="Välj ett alternativ: "\n(ändrar select-prompten)', category: 'Meny', difficulty: 'VG' }
]

// =============================================================================
// TASK 10: LOOPAR
// =============================================================================

const TASK_10_FLASHCARDS: Flashcard[] = [
    { id: 'f10-1', front: 'for-loop syntax?', back: 'for var in lista; do\n  ...\ndone', category: 'Syntax', difficulty: 'G' },
    { id: 'f10-2', front: 'Loop genom filer?', back: 'for fil in *.txt; do\n  echo "$fil"\ndone', category: 'Vanliga', difficulty: 'G' },
    { id: 'f10-3', front: 'Range i for?', back: 'for i in {1..10}; do', category: 'Syntax', difficulty: 'G' },
    { id: 'f10-4', front: 'C-style for?', back: 'for ((i=0; i<10; i++)); do', category: 'Syntax', difficulty: 'VG' },
    { id: 'f10-5', front: 'while-syntax?', back: 'while [ villkor ]; do\n  ...\ndone', category: 'Syntax', difficulty: 'G' },
    { id: 'f10-6', front: 'Läs fil rad för rad?', back: 'while IFS= read -r line; do\n  ...\ndone < fil', category: 'Vanliga', difficulty: 'VG' },
    { id: 'f10-7', front: 'Skillnad while vs until?', back: 'while: kör medan sant\nuntil: kör tills sant', category: 'Koncept', difficulty: 'VG' },
    { id: 'f10-8', front: 'Avbryt loop?', back: 'break', category: 'Kontroll', difficulty: 'G' },
    { id: 'f10-9', front: 'Hoppa till nästa iteration?', back: 'continue', category: 'Kontroll', difficulty: 'G' },
    { id: 'f10-10', front: 'Oändlig loop?', back: 'while true; do\n  ...\ndone', category: 'Syntax', difficulty: 'G' }
]

// =============================================================================
// TASK 11: SKRIPTPARAMETRAR
// =============================================================================

const TASK_11_FLASHCARDS: Flashcard[] = [
    { id: 'f11-1', front: 'Vad är $1, $2, $3...?', back: 'Positionsparametrar (argument 1, 2, 3...)', category: 'Variabler', difficulty: 'G' },
    { id: 'f11-2', front: 'Vad är $0?', back: 'Skriptets namn', category: 'Variabler', difficulty: 'G' },
    { id: 'f11-3', front: 'Vad är $#?', back: 'Antal argument', category: 'Variabler', difficulty: 'G' },
    { id: 'f11-4', front: 'Vad är $@?', back: 'Alla argument (separat)', category: 'Variabler', difficulty: 'G' },
    { id: 'f11-5', front: 'Skillnad $@ vs $*?', back: '"$@" = separata argument\n"$*" = ett argument', category: 'Variabler', difficulty: 'VG' },
    { id: 'f11-6', front: 'Vad gör shift?', back: 'Skiftar parametrar: $2→$1, $3→$2...', category: 'Kommandon', difficulty: 'VG' },
    { id: 'f11-7', front: 'getopts syntax?', back: 'while getopts "ab:" opt; do\n  case $opt in...', category: 'Flaggor', difficulty: 'VG' },
    { id: 'f11-8', front: 'Vad betyder : efter bokstav i getopts?', back: 'Flaggan tar argument\nEx: "a:b" = -a TAR arg, -b tar inte', category: 'Flaggor', difficulty: 'VG' },
    { id: 'f11-9', front: 'OPTARG i getopts?', back: 'Innehåller argumentet till flaggan', category: 'Flaggor', difficulty: 'VG' },
    { id: 'f11-10', front: 'Validera antal argument?', back: 'if [ $# -lt 2 ]; then\n  echo "Usage: ..."\n  exit 1\nfi', category: 'Validering', difficulty: 'G' }
]

// =============================================================================
// TASK 12: FUNKTIONER
// =============================================================================

const TASK_12_FLASHCARDS: Flashcard[] = [
    { id: 'f12-1', front: 'Funktions-syntax?', back: 'func_name() {\n  ...\n}\neller function func_name { }', category: 'Syntax', difficulty: 'G' },
    { id: 'f12-2', front: 'Argument till funktion?', back: '$1, $2, $@ (samma som skript)', category: 'Argument', difficulty: 'G' },
    { id: 'f12-3', front: 'Returnera värde?', back: 'return N (exit code 0-255)\nAnvänd echo för text!', category: 'Return', difficulty: 'G' },
    { id: 'f12-4', front: 'Fånga funktions output?', back: 'result=$(min_funktion)', category: 'Return', difficulty: 'G' },
    { id: 'f12-5', front: 'Lokal variabel?', back: 'local var=värde\n(synlig bara i funktionen)', category: 'Scope', difficulty: 'VG' },
    { id: 'f12-6', front: 'Utan local - vad händer?', back: 'Variabeln blir global!', category: 'Scope', difficulty: 'VG' },
    { id: 'f12-7', front: 'Kolla funktions exit code?', back: 'min_funktion\nif [ $? -eq 0 ]; then', category: 'Kontroll', difficulty: 'G' },
    { id: 'f12-8', front: 'Var måste funktioner definieras?', back: 'FÖRE de anropas i skriptet', category: 'Viktigt', difficulty: 'G' },
    { id: 'f12-9', front: 'Rekursiv funktion möjligt?', back: 'Ja, funktioner kan anropa sig själva', category: 'Avancerat', difficulty: 'VG' },
    { id: 'f12-10', front: 'Ändra global variabel från funktion?', back: 'global_var="nytt värde"\n(utan local)', category: 'Scope', difficulty: 'VG' }
]

// =============================================================================
// TASK 13: SIGNALER & TRAP
// =============================================================================

const TASK_13_FLASHCARDS: Flashcard[] = [
    { id: 'f13-1', front: 'Vad är SIGINT?', back: 'Ctrl+C (Interrupt)', category: 'Signaler', difficulty: 'G' },
    { id: 'f13-2', front: 'Vad är SIGTERM?', back: 'kill-kommandot (Terminate)', category: 'Signaler', difficulty: 'G' },
    { id: 'f13-3', front: 'Vad är SIGKILL?', back: 'kill -9 (kan EJ fångas!)', category: 'Signaler', difficulty: 'G' },
    { id: 'f13-4', front: 'trap-syntax?', back: 'trap \'kommando\' SIGNAL\nEx: trap \'cleanup\' EXIT', category: 'Syntax', difficulty: 'G' },
    { id: 'f13-5', front: 'Ignorera signal?', back: 'trap \'\' SIGINT\n(tom sträng)', category: 'Trap', difficulty: 'VG' },
    { id: 'f13-6', front: 'Återställ default?', back: 'trap - SIGNAL', category: 'Trap', difficulty: 'VG' },
    { id: 'f13-7', front: 'Cleanup vid avslut?', back: 'trap \'rm -f $tmpfile\' EXIT\n(EXIT körs alltid)', category: 'Best practices', difficulty: 'G' },
    { id: 'f13-8', front: 'Lista alla signaler?', back: 'kill -l', category: 'Kommandon', difficulty: 'G' },
    { id: 'f13-9', front: 'Skicka signal till process?', back: 'kill -SIGNAL PID\nEx: kill -TERM 1234', category: 'Kommandon', difficulty: 'G' },
    { id: 'f13-10', front: 'SIGHUP traditionell användning?', back: 'Ladda om konfiguration\n(Hangup)', category: 'Signaler', difficulty: 'VG' }
]

// =============================================================================
// TASK 14: ANVÄNDARHANTERING
// =============================================================================

const TASK_14_FLASHCARDS: Flashcard[] = [
    { id: 'f14-1', front: 'Skapa användare?', back: 'useradd -m username\n(-m skapar hemkatalog)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f14-2', front: 'Sätt lösenord?', back: 'passwd username', category: 'Kommandon', difficulty: 'G' },
    { id: 'f14-3', front: 'Lägg till i grupp?', back: 'usermod -aG gruppnamn user\n(-a = append)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f14-4', front: 'Ta bort användare?', back: 'userdel -r username\n(-r tar bort hemkatalog)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f14-5', front: 'Var finns användarinfo?', back: '/etc/passwd', category: 'Filer', difficulty: 'G' },
    { id: 'f14-6', front: 'Var finns lösenord (krypterade)?', back: '/etc/shadow', category: 'Filer', difficulty: 'G' },
    { id: 'f14-7', front: 'Var finns gruppinfo?', back: '/etc/group', category: 'Filer', difficulty: 'G' },
    { id: 'f14-8', front: 'Visa användarens grupper?', back: 'id username\neller groups username', category: 'Kommandon', difficulty: 'G' },
    { id: 'f14-9', front: 'Skapa grupp?', back: 'groupadd gruppnamn', category: 'Kommandon', difficulty: 'G' },
    { id: 'f14-10', front: 'Ändra primärgrupp?', back: 'usermod -g gruppnamn user', category: 'Kommandon', difficulty: 'VG' }
]

// =============================================================================
// TASK 15: FILRÄTTIGHETER
// =============================================================================

const TASK_15_FLASHCARDS: Flashcard[] = [
    { id: 'f15-1', front: 'rwx i siffror?', back: 'r=4, w=2, x=1\n(rwx = 4+2+1 = 7)', category: 'Grunder', difficulty: 'G' },
    { id: 'f15-2', front: 'Vad betyder 755?', back: 'rwxr-xr-x\n(ägare full, andra kör/läs)', category: 'Grunder', difficulty: 'G' },
    { id: 'f15-3', front: 'Vad betyder 644?', back: 'rw-r--r--\n(standard för filer)', category: 'Grunder', difficulty: 'G' },
    { id: 'f15-4', front: 'Ändra rättigheter?', back: 'chmod 755 fil\neller chmod u+x fil', category: 'Kommandon', difficulty: 'G' },
    { id: 'f15-5', front: 'Ändra ägare?', back: 'chown user:grupp fil', category: 'Kommandon', difficulty: 'G' },
    { id: 'f15-6', front: 'Vad är SUID?', back: 'Kör med filens ägares rättigheter\n(chmod 4755, s i owner x)', category: 'Special', difficulty: 'VG' },
    { id: 'f15-7', front: 'Vad är SGID?', back: 'Kör med filens grupps rättigheter\n(chmod 2755, s i group x)', category: 'Special', difficulty: 'VG' },
    { id: 'f15-8', front: 'Vad är sticky bit?', back: 'Bara ägaren kan ta bort filen\n(chmod 1777, t i other x)', category: 'Special', difficulty: 'VG' },
    { id: 'f15-9', front: 'Rekursiv chmod?', back: 'chmod -R 755 katalog', category: 'Kommandon', difficulty: 'G' },
    { id: 'f15-10', front: 'Visa rättigheter?', back: 'ls -l fil', category: 'Kommandon', difficulty: 'G' }
]

// =============================================================================
// TASK 16: SSH
// =============================================================================

const TASK_16_FLASHCARDS: Flashcard[] = [
    { id: 'f16-1', front: 'Generera SSH-nyckel?', back: 'ssh-keygen -t ed25519\n(eller -t rsa -b 4096)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f16-2', front: 'Kopiera nyckel till server?', back: 'ssh-copy-id user@server', category: 'Kommandon', difficulty: 'G' },
    { id: 'f16-3', front: 'Var ligger privat nyckel?', back: '~/.ssh/id_ed25519\n(eller id_rsa)', category: 'Filer', difficulty: 'G' },
    { id: 'f16-4', front: 'Var ligger publik nyckel?', back: '~/.ssh/id_ed25519.pub', category: 'Filer', difficulty: 'G' },
    { id: 'f16-5', front: 'Rätt rättigheter privat nyckel?', back: '600 (chmod 600 id_ed25519)', category: 'Säkerhet', difficulty: 'G' },
    { id: 'f16-6', front: 'Serverns SSH-config?', back: '/etc/ssh/sshd_config', category: 'Filer', difficulty: 'G' },
    { id: 'f16-7', front: 'Stäng av root-login?', back: 'PermitRootLogin no\n(i sshd_config)', category: 'Säkerhet', difficulty: 'G' },
    { id: 'f16-8', front: 'authorized_keys?', back: 'Serverns lista på godkända publika nycklar\n~/.ssh/authorized_keys', category: 'Filer', difficulty: 'VG' },
    { id: 'f16-9', front: 'Debug SSH-anslutning?', back: 'ssh -v user@server\n(-vv eller -vvv för mer)', category: 'Debug', difficulty: 'VG' },
    { id: 'f16-10', front: 'SSH config för genvägar?', back: '~/.ssh/config\nHost alias\n  HostName server\n  User user', category: 'Tips', difficulty: 'VG' }
]

// =============================================================================
// TASK 17: UFW
// =============================================================================

const TASK_17_FLASHCARDS: Flashcard[] = [
    { id: 'f17-1', front: 'Vad är UFW?', back: 'Uncomplicated Firewall\n(frontend för iptables)', category: 'Koncept', difficulty: 'G' },
    { id: 'f17-2', front: 'Aktivera UFW?', back: 'ufw enable', category: 'Kommandon', difficulty: 'G' },
    { id: 'f17-3', front: 'Tillåt SSH?', back: 'ufw allow ssh\neller ufw allow 22', category: 'Kommandon', difficulty: 'G' },
    { id: 'f17-4', front: 'Visa regler?', back: 'ufw status\n(eller ufw status verbose)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f17-5', front: 'Neka port?', back: 'ufw deny 23', category: 'Kommandon', difficulty: 'G' },
    { id: 'f17-6', front: 'Ta bort regel?', back: 'ufw delete allow 22\neller ufw delete 3 (radnummer)', category: 'Kommandon', difficulty: 'VG' },
    { id: 'f17-7', front: 'Default policy?', back: 'ufw default deny incoming\nufw default allow outgoing', category: 'Best practices', difficulty: 'G' },
    { id: 'f17-8', front: 'Tillåt från specifik IP?', back: 'ufw allow from 192.168.1.100', category: 'Regler', difficulty: 'VG' },
    { id: 'f17-9', front: 'Tillåt port range?', back: 'ufw allow 6000:6007/tcp', category: 'Regler', difficulty: 'VG' },
    { id: 'f17-10', front: 'VIKTIGT före enable?', back: 'ufw allow ssh FÖRST!\n(annars låser du ute dig själv)', category: 'Varning', difficulty: 'G' }
]

// =============================================================================
// TASK 18: FIREWALLD
// =============================================================================

const TASK_18_FLASHCARDS: Flashcard[] = [
    { id: 'f18-1', front: 'Var används firewalld?', back: 'RHEL/CentOS/Fedora\n(Ubuntu använder UFW)', category: 'Koncept', difficulty: 'G' },
    { id: 'f18-2', front: 'Tillåt HTTP permanent?', back: 'firewall-cmd --permanent --add-service=http\nfirewall-cmd --reload', category: 'Kommandon', difficulty: 'G' },
    { id: 'f18-3', front: 'Varför --permanent?', back: 'Utan det försvinner regeln vid omstart', category: 'Viktigt', difficulty: 'G' },
    { id: 'f18-4', front: 'Lista regler?', back: 'firewall-cmd --list-all', category: 'Kommandon', difficulty: 'G' },
    { id: 'f18-5', front: 'Vad är zoner?', back: 'Grupper av regler\n(public, trusted, drop...)', category: 'Koncept', difficulty: 'VG' },
    { id: 'f18-6', front: 'Lägg till port?', back: 'firewall-cmd --permanent --add-port=8080/tcp', category: 'Kommandon', difficulty: 'G' },
    { id: 'f18-7', front: 'Ta bort service?', back: 'firewall-cmd --permanent --remove-service=http', category: 'Kommandon', difficulty: 'VG' },
    { id: 'f18-8', front: 'Ladda om regler?', back: 'firewall-cmd --reload', category: 'Kommandon', difficulty: 'G' },
    { id: 'f18-9', front: 'Default zon?', back: 'firewall-cmd --get-default-zone\n(oftast public)', category: 'Kommandon', difficulty: 'VG' },
    { id: 'f18-10', front: 'Ändra zon för interface?', back: 'firewall-cmd --zone=trusted --change-interface=eth1', category: 'Avancerat', difficulty: 'VG' }
]

// =============================================================================
// TASK 19: LAGRING & LVM
// =============================================================================

const TASK_19_FLASHCARDS: Flashcard[] = [
    { id: 'f19-1', front: 'Lista blockenheter?', back: 'lsblk', category: 'Kommandon', difficulty: 'G' },
    { id: 'f19-2', front: 'Formatera partition?', back: 'mkfs.ext4 /dev/sdb1', category: 'Kommandon', difficulty: 'G' },
    { id: 'f19-3', front: 'Montera disk?', back: 'mount /dev/sdb1 /mnt/data', category: 'Kommandon', difficulty: 'G' },
    { id: 'f19-4', front: 'Permanent montering?', back: 'Lägg till rad i /etc/fstab', category: 'Konfiguration', difficulty: 'G' },
    { id: 'f19-5', front: 'LVM komponenter?', back: 'PV → VG → LV\n(Physical → Volume Group → Logical)', category: 'LVM', difficulty: 'VG' },
    { id: 'f19-6', front: 'Skapa physical volume?', back: 'pvcreate /dev/sdb', category: 'LVM', difficulty: 'VG' },
    { id: 'f19-7', front: 'Skapa volume group?', back: 'vgcreate myvg /dev/sdb /dev/sdc', category: 'LVM', difficulty: 'VG' },
    { id: 'f19-8', front: 'Skapa logical volume?', back: 'lvcreate -L 10G -n mylv myvg', category: 'LVM', difficulty: 'VG' },
    { id: 'f19-9', front: 'Utöka LV?', back: 'lvextend -L +5G /dev/myvg/mylv\nresize2fs /dev/myvg/mylv', category: 'LVM', difficulty: 'VG' },
    { id: 'f19-10', front: 'Visa diskutrymme?', back: 'df -h', category: 'Kommandon', difficulty: 'G' }
]

// =============================================================================
// TASK 20: BACKUP
// =============================================================================

const TASK_20_FLASHCARDS: Flashcard[] = [
    { id: 'f20-1', front: 'Skapa tar-arkiv?', back: 'tar cvf arkiv.tar katalog/', category: 'tar', difficulty: 'G' },
    { id: 'f20-2', front: 'Skapa gzippat arkiv?', back: 'tar czvf arkiv.tar.gz katalog/', category: 'tar', difficulty: 'G' },
    { id: 'f20-3', front: 'Extrahera arkiv?', back: 'tar xzvf arkiv.tar.gz', category: 'tar', difficulty: 'G' },
    { id: 'f20-4', front: 'tar-flaggor c x v f z?', back: 'c=create x=extract v=verbose\nf=file z=gzip', category: 'tar', difficulty: 'G' },
    { id: 'f20-5', front: 'rsync grundkommando?', back: 'rsync -avz källa/ mål/', category: 'rsync', difficulty: 'G' },
    { id: 'f20-6', front: 'rsync -a betyder?', back: 'Archive mode\n(bevarar rättigheter, timestamps, etc)', category: 'rsync', difficulty: 'G' },
    { id: 'f20-7', front: 'rsync --delete?', back: 'Ta bort filer i mål som inte finns i källa', category: 'rsync', difficulty: 'VG' },
    { id: 'f20-8', front: 'rsync till remote?', back: 'rsync -avz katalog/ user@server:/backup/', category: 'rsync', difficulty: 'VG' },
    { id: 'f20-9', front: 'Lista innehåll i tar?', back: 'tar tvf arkiv.tar\n(t = list)', category: 'tar', difficulty: 'G' },
    { id: 'f20-10', front: 'Trailing slash i rsync?', back: 'källa/ = innehållet\nkälla = hela katalogen', category: 'rsync', difficulty: 'VG' }
]

// =============================================================================
// TASK 21: SYSTEMD
// =============================================================================

const TASK_21_FLASHCARDS: Flashcard[] = [
    { id: 'f21-1', front: 'Starta tjänst?', back: 'systemctl start tjänst', category: 'Kommandon', difficulty: 'G' },
    { id: 'f21-2', front: 'Stoppa tjänst?', back: 'systemctl stop tjänst', category: 'Kommandon', difficulty: 'G' },
    { id: 'f21-3', front: 'Starta vid boot?', back: 'systemctl enable tjänst', category: 'Kommandon', difficulty: 'G' },
    { id: 'f21-4', front: 'Visa status?', back: 'systemctl status tjänst', category: 'Kommandon', difficulty: 'G' },
    { id: 'f21-5', front: 'Ladda om config?', back: 'systemctl reload tjänst\n(eller restart)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f21-6', front: 'Efter ändring i .service-fil?', back: 'systemctl daemon-reload', category: 'Viktigt', difficulty: 'G' },
    { id: 'f21-7', front: 'Visa loggar?', back: 'journalctl -u tjänst', category: 'Kommandon', difficulty: 'G' },
    { id: 'f21-8', front: 'Följ loggar live?', back: 'journalctl -u tjänst -f', category: 'Kommandon', difficulty: 'G' },
    { id: 'f21-9', front: 'Var finns unit-filer?', back: '/etc/systemd/system/\n(användar-skapade)\n/usr/lib/systemd/system/\n(paket)', category: 'Filer', difficulty: 'VG' },
    { id: 'f21-10', front: 'Lista alla tjänster?', back: 'systemctl list-units --type=service', category: 'Kommandon', difficulty: 'VG' }
]

// =============================================================================
// TASK 22: DOCKER GRUNDER
// =============================================================================

const TASK_22_FLASHCARDS: Flashcard[] = [
    { id: 'f22-1', front: 'Kör container?', back: 'docker run image', category: 'Kommandon', difficulty: 'G' },
    { id: 'f22-2', front: 'Kör i bakgrunden?', back: 'docker run -d image\n(-d = detached)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f22-3', front: 'Lista körande containers?', back: 'docker ps\n(docker ps -a för alla)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f22-4', front: 'Stoppa container?', back: 'docker stop container_id', category: 'Kommandon', difficulty: 'G' },
    { id: 'f22-5', front: 'Visa loggar?', back: 'docker logs container_id', category: 'Kommandon', difficulty: 'G' },
    { id: 'f22-6', front: 'Öppna shell i container?', back: 'docker exec -it container bash\n(-it = interactive + tty)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f22-7', front: 'Port-mapping?', back: '-p host:container\nEx: -p 8080:80', category: 'Nätverk', difficulty: 'G' },
    { id: 'f22-8', front: 'Volym-mount?', back: '-v /host/path:/container/path', category: 'Volymer', difficulty: 'VG' },
    { id: 'f22-9', front: 'Auto-restart?', back: '--restart=always', category: 'Konfiguration', difficulty: 'VG' },
    { id: 'f22-10', front: 'Ta bort container?', back: 'docker rm container_id\n(docker rm -f för tvinga)', category: 'Kommandon', difficulty: 'G' }
]

// =============================================================================
// TASK 23: DOCKER IMAGES
// =============================================================================

const TASK_23_FLASHCARDS: Flashcard[] = [
    { id: 'f23-1', front: 'Bygg image?', back: 'docker build -t namn .\n(-t = tag/namn)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f23-2', front: 'Dockerfile första rad?', back: 'FROM basimage\nEx: FROM ubuntu:22.04', category: 'Dockerfile', difficulty: 'G' },
    { id: 'f23-3', front: 'Köra kommandon i build?', back: 'RUN apt update && apt install -y nginx', category: 'Dockerfile', difficulty: 'G' },
    { id: 'f23-4', front: 'Kopiera filer?', back: 'COPY källa mål\nEx: COPY . /app', category: 'Dockerfile', difficulty: 'G' },
    { id: 'f23-5', front: 'Startkommando?', back: 'CMD ["nginx", "-g", "daemon off;"]', category: 'Dockerfile', difficulty: 'G' },
    { id: 'f23-6', front: 'Sätt working directory?', back: 'WORKDIR /app', category: 'Dockerfile', difficulty: 'G' },
    { id: 'f23-7', front: 'Lista images?', back: 'docker images', category: 'Kommandon', difficulty: 'G' },
    { id: 'f23-8', front: 'Ta bort image?', back: 'docker rmi image_id', category: 'Kommandon', difficulty: 'G' },
    { id: 'f23-9', front: 'Multi-stage build?', back: 'FROM node AS builder\n...\nFROM nginx\nCOPY --from=builder', category: 'Avancerat', difficulty: 'VG' },
    { id: 'f23-10', front: '.dockerignore?', back: 'Exkludera filer från COPY\n(som .gitignore)', category: 'Best practices', difficulty: 'VG' }
]

// =============================================================================
// TASK 24: DOCKER COMPOSE
// =============================================================================

const TASK_24_FLASHCARDS: Flashcard[] = [
    { id: 'f24-1', front: 'Starta alla services?', back: 'docker-compose up\n(docker-compose up -d för bakgrund)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f24-2', front: 'Stoppa allt?', back: 'docker-compose down', category: 'Kommandon', difficulty: 'G' },
    { id: 'f24-3', front: 'Visa loggar?', back: 'docker-compose logs\n(-f för att följa)', category: 'Kommandon', difficulty: 'G' },
    { id: 'f24-4', front: 'Bygg och starta?', back: 'docker-compose up --build', category: 'Kommandon', difficulty: 'G' },
    { id: 'f24-5', front: 'Compose-fil format?', back: 'docker-compose.yml\n(YAML-format)', category: 'Konfiguration', difficulty: 'G' },
    { id: 'f24-6', front: 'Definiera service?', back: 'services:\n  web:\n    image: nginx', category: 'Syntax', difficulty: 'G' },
    { id: 'f24-7', front: 'Definiera volym?', back: 'volumes:\n  - ./data:/app/data', category: 'Syntax', difficulty: 'G' },
    { id: 'f24-8', front: 'Miljövariabler?', back: 'environment:\n  - DB_HOST=db', category: 'Syntax', difficulty: 'G' },
    { id: 'f24-9', front: 'Beroende mellan services?', back: 'depends_on:\n  - db', category: 'Syntax', difficulty: 'VG' },
    { id: 'f24-10', front: 'Stoppa + ta bort volymer?', back: 'docker-compose down -v', category: 'Kommandon', difficulty: 'VG' }
]

// =============================================================================
// TASK 25: GIT
// =============================================================================

const TASK_25_FLASHCARDS: Flashcard[] = [
    { id: 'f25-1', front: 'Initiera repo?', back: 'git init', category: 'Grundläggande', difficulty: 'G' },
    { id: 'f25-2', front: 'Klona repo?', back: 'git clone URL', category: 'Grundläggande', difficulty: 'G' },
    { id: 'f25-3', front: 'Stagea ändringar?', back: 'git add fil\ngit add -A (alla)', category: 'Grundläggande', difficulty: 'G' },
    { id: 'f25-4', front: 'Commita?', back: 'git commit -m "meddelande"', category: 'Grundläggande', difficulty: 'G' },
    { id: 'f25-5', front: 'Skapa branch?', back: 'git checkout -b branch\neller git branch branch', category: 'Branches', difficulty: 'G' },
    { id: 'f25-6', front: 'Byta branch?', back: 'git checkout branch\neller git switch branch', category: 'Branches', difficulty: 'G' },
    { id: 'f25-7', front: 'Merga branch?', back: 'git merge branch', category: 'Branches', difficulty: 'G' },
    { id: 'f25-8', front: 'Pusha till remote?', back: 'git push origin branch', category: 'Remote', difficulty: 'G' },
    { id: 'f25-9', front: 'Hämta + merga?', back: 'git pull\n(= git fetch + git merge)', category: 'Remote', difficulty: 'G' },
    { id: 'f25-10', front: 'Spara ändringar temporärt?', back: 'git stash\ngit stash pop (återställ)', category: 'Avancerat', difficulty: 'VG' }
]

// =============================================================================
// EXPORT
// =============================================================================

export const DOE25_FLASHCARDS: TaskFlashcardSet[] = [
    { taskId: 'doe25-0-1-subnetting', taskTitle: '0.1 Subnetting & Nätverk', flashcards: TASK_1_FLASHCARDS },
    { taskId: 'doe25-0-2-filsystem', taskTitle: '0.2 Linux Filsystem', flashcards: TASK_2_FLASHCARDS },
    { taskId: 'doe25-1-1-bash-grunder', taskTitle: '1.1 Bash Grunder', flashcards: TASK_3_FLASHCARDS },
    { taskId: 'doe25-1-2-variabler', taskTitle: '1.2 Variabler & Datatyper', flashcards: TASK_4_FLASHCARDS },
    { taskId: 'doe25-1-3-regex', taskTitle: '1.3 Reguljära Uttryck (Regex)', flashcards: TASK_5_FLASHCARDS },
    { taskId: 'doe25-1-4-sed', taskTitle: '1.4 sed - Stream Editor', flashcards: TASK_6_FLASHCARDS },
    { taskId: 'doe25-1-5-awk', taskTitle: '1.5 awk - Textbearbetning', flashcards: TASK_7_FLASHCARDS },
    { taskId: 'doe25-1-6-villkor', taskTitle: '1.6 Villkor (if/else)', flashcards: TASK_8_FLASHCARDS },
    { taskId: 'doe25-1-7-interaktiva', taskTitle: '1.7 Interaktiva Skript', flashcards: TASK_9_FLASHCARDS },
    { taskId: 'doe25-1-8-loopar', taskTitle: '1.8 Loopar (for/while)', flashcards: TASK_10_FLASHCARDS },
    { taskId: 'doe25-1-9-parametrar', taskTitle: '1.9 Skriptparametrar', flashcards: TASK_11_FLASHCARDS },
    { taskId: 'doe25-1-10-funktioner', taskTitle: '1.10 Funktioner', flashcards: TASK_12_FLASHCARDS },
    { taskId: 'doe25-1-11-signals', taskTitle: '1.11 Signaler & Trap', flashcards: TASK_13_FLASHCARDS },
    { taskId: 'doe25-2-1-users', taskTitle: '2.1 Användarhantering', flashcards: TASK_14_FLASHCARDS },
    { taskId: 'doe25-2-2-permissions', taskTitle: '2.2 Rättigheter & ACL', flashcards: TASK_15_FLASHCARDS },
    { taskId: 'doe25-2-3-ssh', taskTitle: '2.3 SSH', flashcards: TASK_16_FLASHCARDS },
    { taskId: 'doe25-2-4-ufw', taskTitle: '2.4 UFW Firewall', flashcards: TASK_17_FLASHCARDS },
    { taskId: 'doe25-2-5-firewalld', taskTitle: '2.5 Firewalld', flashcards: TASK_18_FLASHCARDS },
    { taskId: 'doe25-2-6-lagring', taskTitle: '2.6 Lagring & LVM', flashcards: TASK_19_FLASHCARDS },
    { taskId: 'doe25-2-7-backup', taskTitle: '2.7 Backup', flashcards: TASK_20_FLASHCARDS },
    { taskId: 'doe25-2-8-systemd', taskTitle: '2.8 Systemd', flashcards: TASK_21_FLASHCARDS },
    { taskId: 'doe25-3-1-docker-grunder', taskTitle: '3.1 Docker Grunder', flashcards: TASK_22_FLASHCARDS },
    { taskId: 'doe25-3-2-docker-images', taskTitle: '3.2 Docker Images', flashcards: TASK_23_FLASHCARDS },
    { taskId: 'doe25-3-3-docker-compose', taskTitle: '3.3 Docker Compose', flashcards: TASK_24_FLASHCARDS },
    { taskId: 'doe25-3-4-git', taskTitle: '3.4 Git', flashcards: TASK_25_FLASHCARDS }
]

// Helper functions
export function getFlashcardsForTask(taskId: string): Flashcard[] {
    const set = DOE25_FLASHCARDS.find(s => s.taskId === taskId)
    return set?.flashcards || []
}

export function getAllDOE25Flashcards(): Flashcard[] {
    return DOE25_FLASHCARDS.flatMap(s => s.flashcards)
}

export function getFlashcardsByDifficulty(difficulty: 'G' | 'VG'): Flashcard[] {
    return getAllDOE25Flashcards().filter(f => f.difficulty === difficulty)
}
