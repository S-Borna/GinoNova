// DOE25 Tentaplugg Module - 25 Tasks
// Interfaces

export interface QuizOption {
    text: string;
    correct?: boolean;
    feedback?: string;
}

export interface CompareItem {
    name: string;
    pros: string[];
    cons: string[];
    use_case?: string;
}

export interface ContentBlock {
    type: string;
    title?: string;
    headline?: string;
    explanation?: string;
    code?: string;
    language?: string;
    options?: QuizOption[];
    question?: string;
    hint?: string;
    pro_tip?: string;
    warning?: string;
    warning_level?: string;
    learning_objectives?: string[];
    scenario_title?: string;
    scenario_context?: string;
    scenario_symptoms?: string[];
    scenario_solution?: string;
    challenge_task?: string;
    challenge_commands?: string[];
    expected_output?: string;
    diagram?: string;
    diagram_caption?: string;
    message?: string;
    items?: string[];
    compare_items?: CompareItem[];
    summary_title?: string;
    key_points?: string[];
    next_step?: string;
}

export interface DOE25Task {
    id: string;
    title: string;
    description: string;
    order_index: number;
    estimated_minutes: number;
    content_blocks: ContentBlock[];
}

export interface DOE25Module {
    id: string;
    name: string;
    slug: string;
    description: string;
    difficulty: "beginner" | "intermediate" | "advanced" | "expert";
    estimated_hours: number;
    exam_date: string;
    tasks: DOE25Task[];
}

// ============================================
// DOE25 TENTAPLUGG MODULE - 25 TASKS
// ============================================

export const DOE25_MODULE: DOE25Module = {
    id: "doe25-tenta",
    name: "DOE25 Tentaplugg",
    slug: "doe25-tenta",
    description: "Komplett tentaplugg med 25 tasks: Linux Grunder, Bash Scripting, System Administration & DevOps",
    difficulty: "intermediate",
    estimated_hours: 40,
    exam_date: "2025-01-07T09:30:00",
    tasks: [
        // ============================================
        // MODUL 0: LINUX GRUNDER (2 tasks)
        // ============================================
        {
            id: "doe25-0-1-subnetting",
            title: "0.1 Subnetting & Nätverk",
            description: "Förstå IP-adresser, subnätmasker och nätverksberäkningar",
            order_index: 1,
            estimated_minutes: 45,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🌐 Subnetting & Nätverk",
                    learning_objectives: [
                        "IPv4-adressering och klasser",
                        "Subnätmasker och CIDR-notation",
                        "Beräkna nätverksadress, broadcast och hosts",
                        "Praktiska subnetting-exempel"
                    ]
                },
                {
                    type: "concept",
                    title: "IPv4-adressering",
                    explanation: `En IPv4-adress består av 32 bitar uppdelade i 4 oktetter:

┌─────────────────────────────────────────────────────────────┐
│  192    .    168    .    1      .    100                    │
│  11000000   10101000   00000001   01100100                  │
│  Oktett 1   Oktett 2   Oktett 3   Oktett 4                  │
└─────────────────────────────────────────────────────────────┘

Varje oktett kan vara 0-255 (8 bitar = 2^8 = 256 värden)`
                },
                {
                    type: "concept",
                    title: "IP-klasser (historiskt)",
                    explanation: `┌─────────┬───────────────────┬────────────────┬──────────────┐
│ Klass   │ Första oktett     │ Default mask   │ Nätverk      │
├─────────┼───────────────────┼────────────────┼──────────────┤
│ A       │ 1-126             │ 255.0.0.0      │ Stora        │
│ B       │ 128-191           │ 255.255.0.0    │ Medelstora   │
│ C       │ 192-223           │ 255.255.255.0  │ Små          │
└─────────┴───────────────────┴────────────────┴──────────────┘

OBS: 127.x.x.x är reserverat för loopback (localhost)`
                },
                {
                    type: "concept",
                    title: "CIDR-notation",
                    explanation: `CIDR (Classless Inter-Domain Routing) ersatte klasserna:

┌─────────────────────────────────────────────────────────────┐
│  192.168.1.0/24                                             │
│              └── Antal nätverksbitar (24 av 32)             │
│                                                             │
│  /24 = 255.255.255.0   (24 ettor, 8 nollor)                │
│  /16 = 255.255.0.0     (16 ettor, 16 nollor)               │
│  /8  = 255.0.0.0       (8 ettor, 24 nollor)                │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "concept",
                    title: "Subnätberäkning",
                    explanation: `För 192.168.1.100/24:

┌─────────────────────────────────────────────────────────────┐
│  Nätverksadress:  192.168.1.0    (första i subnätet)       │
│  Broadcast:       192.168.1.255  (sista i subnätet)        │
│  Första host:     192.168.1.1                               │
│  Sista host:      192.168.1.254                             │
│  Antal hosts:     254 (2^8 - 2)                             │
└─────────────────────────────────────────────────────────────┘

Formel: Antal hosts = 2^(32-prefix) - 2
        -2 för nätverksadress och broadcast`
                },
                {
                    type: "code",
                    title: "Praktiska kommandon",
                    language: "bash",
                    code: `# Visa nätverkskonfiguration
ip addr show
ip route show

# Visa subnätinfo
ipcalc 192.168.1.100/24

# Testa nätverksanslutning
ping -c 3 192.168.1.1
traceroute google.com`
                },
                {
                    type: "quiz",
                    question: "Hur många hosts kan finnas i ett /24 nätverk?",
                    options: [
                        { text: "256", correct: false, feedback: "Nej, 2 adresser är reserverade" },
                        { text: "254", correct: true, feedback: "Rätt! 2^8 - 2 = 254 (minus nätverksadress och broadcast)" },
                        { text: "255", correct: false, feedback: "Nej, glöm inte broadcast-adressen" },
                        { text: "252", correct: false, feedback: "Nej, det blir för få" }
                    ],
                    hint: "Tänk på vilka adresser som är reserverade"
                },
                {
                    type: "quiz",
                    question: "Vad är broadcast-adressen för 10.0.0.0/8?",
                    options: [
                        { text: "10.0.0.255", correct: false, feedback: "Nej, /8 har större range" },
                        { text: "10.255.255.255", correct: true, feedback: "Rätt! Alla hostbitar satta till 1" },
                        { text: "10.0.255.255", correct: false, feedback: "Nej, /8 inkluderar mer" },
                        { text: "255.255.255.255", correct: false, feedback: "Nej, det är begränsat broadcast" }
                    ],
                    hint: "/8 betyder att bara första oktetten är nätverksdelen"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Subnetting! 🌐 Nätverksgrunder avklarade."
                }
            ]
        },
        {
            id: "doe25-0-2-filsystem",
            title: "0.2 Linux Filsystem",
            description: "Förstå Linux filsystemhierarkin och viktiga kataloger",
            order_index: 2,
            estimated_minutes: 40,
            content_blocks: [
                {
                    type: "intro",
                    headline: "📁 Linux Filsystem",
                    learning_objectives: [
                        "FHS (Filesystem Hierarchy Standard)",
                        "Viktiga systemkataloger",
                        "Filtyper i Linux",
                        "Navigering och sökvägar"
                    ]
                },
                {
                    type: "concept",
                    title: "Filesystem Hierarchy Standard",
                    explanation: `Linux använder en trädstruktur med / (root) som topp:

┌─────────────────────────────────────────────────────────────┐
│  /                        ← Roten av allt                   │
│  ├── bin/                 ← Grundläggande binärer           │
│  ├── boot/                ← Bootloader, kernel              │
│  ├── dev/                 ← Enheter (devices)               │
│  ├── etc/                 ← Systemkonfiguration             │
│  ├── home/                ← Användarnas hemkataloger        │
│  ├── lib/                 ← Delade bibliotek                │
│  ├── media/               ← Flyttbara media                 │
│  ├── mnt/                 ← Temporära mount points          │
│  ├── opt/                 ← Tredjepartsprogram              │
│  ├── proc/                ← Processinfo (virtuellt)         │
│  ├── root/                ← Roots hemkatalog                │
│  ├── sbin/                ← Systemadmin-binärer             │
│  ├── srv/                 ← Tjänstedata                     │
│  ├── sys/                 ← Systeminfo (virtuellt)          │
│  ├── tmp/                 ← Temporära filer                 │
│  ├── usr/                 ← Användarprogram                 │
│  └── var/                 ← Variabel data (loggar etc)      │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "concept",
                    title: "Viktiga kataloger - detaljer",
                    explanation: `┌─────────────────────────────────────────────────────────────┐
│  /etc/                                                      │
│  ├── passwd          ← Användarinfo                         │
│  ├── shadow          ← Krypterade lösenord                  │
│  ├── group           ← Gruppinfo                            │
│  ├── fstab           ← Filsystem att mounta                 │
│  ├── hosts           ← Lokal DNS                            │
│  ├── ssh/            ← SSH-konfiguration                    │
│  └── systemd/        ← Systemd-tjänster                     │
├─────────────────────────────────────────────────────────────┤
│  /var/                                                      │
│  ├── log/            ← Systemloggar                         │
│  ├── www/            ← Webbserver-filer                     │
│  ├── lib/            ← Variabel programdata                 │
│  └── spool/          ← Köer (mail, print)                   │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "concept",
                    title: "Filtyper i Linux",
                    explanation: `Linux har 7 filtyper (visas med ls -l):

┌──────┬─────────────────┬─────────────────────────────────────┐
│ Typ  │ Namn            │ Beskrivning                         │
├──────┼─────────────────┼─────────────────────────────────────┤
│  -   │ Regular file    │ Vanlig fil                          │
│  d   │ Directory       │ Katalog                             │
│  l   │ Symbolic link   │ Genväg/länk                         │
│  c   │ Character device│ Teckenenhet (terminal)              │
│  b   │ Block device    │ Blockenhet (disk)                   │
│  s   │ Socket          │ Nätverkskommunikation               │
│  p   │ Named pipe      │ FIFO för IPC                        │
└──────┴─────────────────┴─────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Navigeringskommandon",
                    language: "bash",
                    code: `# Absolut vs relativ sökväg
cd /etc/ssh        # Absolut (från root)
cd ../lib          # Relativ (från nuvarande)

# Visa kataloginnehåll
ls -la             # Alla filer, lång format
ls -lh             # Human-readable storlekar
tree -L 2          # Trädvy, 2 nivåer

# Hitta filer
find / -name "*.conf" -type f
locate nginx.conf
which python3

# Diskutrymme
df -h              # Filsystem användning
du -sh /var/log    # Katalogstorlek`
                },
                {
                    type: "quiz",
                    question: "Var lagras systemkonfigurationsfiler i Linux?",
                    options: [
                        { text: "/var", correct: false, feedback: "Nej, /var är för variabel data som loggar" },
                        { text: "/etc", correct: true, feedback: "Rätt! /etc innehåller systemkonfiguration" },
                        { text: "/usr", correct: false, feedback: "Nej, /usr innehåller användarprogram" },
                        { text: "/opt", correct: false, feedback: "Nej, /opt är för tredjepartsprogram" }
                    ],
                    hint: "Tänk 'etcetera' - allt möjligt konfigurationsgrejer"
                },
                {
                    type: "quiz",
                    question: "Vilken katalog innehåller systemloggar?",
                    options: [
                        { text: "/etc/log", correct: false, feedback: "Nej, /etc är för konfiguration" },
                        { text: "/var/log", correct: true, feedback: "Rätt! /var/log innehåller alla systemloggar" },
                        { text: "/log", correct: false, feedback: "Nej, den katalogen finns inte standard" },
                        { text: "/usr/log", correct: false, feedback: "Nej, /usr är för program" }
                    ],
                    hint: "Loggar är variabel data..."
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Linux Filsystem! 📁 MODUL 0 KLAR!"
                }
            ]
        },
        // ============================================
        // MODUL 1: BASH SCRIPTING (11 tasks)
        // ============================================
        {
            id: "doe25-1-1-bash-grunder",
            title: "1.1 Bash Grunder",
            description: "Grundläggande bash-kommandon och skriptstruktur",
            order_index: 3,
            estimated_minutes: 45,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🐚 Bash Grunder",
                    learning_objectives: [
                        "Shebang och skriptstruktur",
                        "Köra och göra skript exekverbara",
                        "Grundläggande I/O (echo, read)",
                        "Exit codes och felhantering"
                    ]
                },
                {
                    type: "concept",
                    title: "Shebang - Skriptets första rad",
                    explanation: `Shebang talar om vilken tolk som ska köra skriptet:

┌─────────────────────────────────────────────────────────────┐
│  #!/bin/bash          ← Använd bash                         │
│  #!/usr/bin/env bash  ← Portabel (hittar bash i PATH)       │
│  #!/bin/sh            ← POSIX shell (mer portabel)          │
│  #!/usr/bin/python3   ← Python-skript                       │
└─────────────────────────────────────────────────────────────┘

VIKTIGT: Shebang MÅSTE vara första raden, inga mellanslag före #`
                },
                {
                    type: "code",
                    title: "Ditt första skript",
                    language: "bash",
                    code: `#!/bin/bash
# mitt_skript.sh - En enkel demo

# Skriv ut text
echo "Hej från mitt skript!"

# Läs input från användaren
read -p "Vad heter du? " namn
echo "Trevligt att träffas, $namn!"

# Exit med statuskod
exit 0`
                },
                {
                    type: "code",
                    title: "Köra skript",
                    language: "bash",
                    code: `# Metod 1: Gör exekverbar och kör
chmod +x mitt_skript.sh
./mitt_skript.sh

# Metod 2: Kör med bash direkt
bash mitt_skript.sh

# Metod 3: Source (kör i nuvarande shell)
source mitt_skript.sh
. mitt_skript.sh`
                },
                {
                    type: "concept",
                    title: "Exit Codes",
                    explanation: `Varje kommando returnerar en exit code:

┌─────────┬─────────────────────────────────────────────────────┐
│ Code    │ Betydelse                                           │
├─────────┼─────────────────────────────────────────────────────┤
│ 0       │ Framgång (allt gick bra)                            │
│ 1       │ Allmänt fel                                         │
│ 2       │ Felaktig användning av kommando                     │
│ 126     │ Kommando finns men är ej körbart                    │
│ 127     │ Kommando hittades inte                              │
│ 128+N   │ Dödad av signal N                                   │
└─────────┴─────────────────────────────────────────────────────┘

Kolla senaste exit code: echo $?`
                },
                {
                    type: "quiz",
                    question: "Vad betyder exit code 0?",
                    options: [
                        { text: "Fel uppstod", correct: false, feedback: "Nej, 0 är bra!" },
                        { text: "Kommandot lyckades", correct: true, feedback: "Rätt! 0 = framgång i Unix" },
                        { text: "Kommandot hittades inte", correct: false, feedback: "Nej, det är 127" },
                        { text: "Skriptet avbröts", correct: false, feedback: "Nej, det är 128+" }
                    ],
                    hint: "I Unix betyder 0 alltid framgång"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Bash Grunder! 🐚"
                }
            ]
        },
        {
            id: "doe25-1-2-variabler",
            title: "1.2 Variabler & Datatyper",
            description: "Variabler, miljövariabler och stränghantering i Bash",
            order_index: 4,
            estimated_minutes: 50,
            content_blocks: [
                {
                    type: "intro",
                    headline: "📦 Variabler & Datatyper",
                    learning_objectives: [
                        "Deklarera och använda variabler",
                        "Miljövariabler vs lokala variabler",
                        "Strängmanipulation",
                        "Arrayer i Bash"
                    ]
                },
                {
                    type: "concept",
                    title: "Variabler i Bash",
                    explanation: `Bash-variabler har inga explicita typer - allt är strängar!

┌─────────────────────────────────────────────────────────────┐
│  REGLER:                                                    │
│  • Inga mellanslag runt =                                   │
│  • Börja med bokstav eller _                                │
│  • Använd $ för att läsa värdet                             │
│  • Använd "quotes" för strängar med mellanslag              │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Variabeldeklaration",
                    language: "bash",
                    code: `#!/bin/bash

# Enkla variabler
namn="Anna"
alder=25
stad="Stockholm"

# Använda variabler
echo "Hej $namn!"
echo "Du är $alder år och bor i $stad"

# Curly braces för tydlighet
echo "\${namn}s ålder är \${alder}"

# Kommandosubstitution
datum=$(date +%Y-%m-%d)
filer=$(ls | wc -l)
echo "Datum: $datum, Antal filer: $filer"`
                },
                {
                    type: "concept",
                    title: "Miljövariabler",
                    explanation: `Miljövariabler ärvs av barnprocesser:

┌─────────────────────────────────────────────────────────────┐
│  Viktiga miljövariabler:                                    │
│  $HOME     - Hemkatalog                                     │
│  $USER     - Användarnamn                                   │
│  $PATH     - Sökvägar för kommandon                         │
│  $PWD      - Nuvarande katalog                              │
│  $SHELL    - Nuvarande shell                                │
│  $?        - Senaste exit code                              │
│  $$        - Nuvarande process ID                           │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Strängmanipulation",
                    language: "bash",
                    code: `#!/bin/bash
str="Hello World"

# Längd
echo \${#str}              # 11

# Substring
echo \${str:0:5}           # Hello
echo \${str:6}             # World

# Ersätt
echo \${str/World/Bash}    # Hello Bash
echo \${str//o/0}          # Hell0 W0rld

# Ta bort mönster
fil="dokument.txt.bak"
echo \${fil%.bak}          # dokument.txt
echo \${fil%%.*}           # dokument`
                },
                {
                    type: "code",
                    title: "Arrayer",
                    language: "bash",
                    code: `#!/bin/bash

# Deklarera array
frukter=("äpple" "banan" "citron")

# Åtkomst
echo \${frukter[0]}        # äpple
echo \${frukter[@]}        # alla element
echo \${#frukter[@]}       # antal element (3)

# Loopa
for frukt in "\${frukter[@]}"; do
    echo "Frukt: $frukt"
done

# Lägg till element
frukter+=("dadel")`
                },
                {
                    type: "quiz",
                    question: "Hur får du längden av variabeln $str?",
                    options: [
                        { text: "len($str)", correct: false, feedback: "Nej, det är Python-syntax" },
                        { text: "\\${#str}", correct: true, feedback: "Rätt! # ger längden" },
                        { text: "$str.length", correct: false, feedback: "Nej, det är annan syntax" },
                        { text: "strlen $str", correct: false, feedback: "Nej, det finns inte i bash" }
                    ],
                    hint: "# används för längd i bash"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Variabler! 📦"
                }
            ]
        },
        {
            id: "doe25-1-3-regex",
            title: "1.3 Reguljära Uttryck (Regex)",
            description: "Mönstermatchning med reguljära uttryck",
            order_index: 5,
            estimated_minutes: 55,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🔍 Reguljära Uttryck",
                    learning_objectives: [
                        "Grundläggande regex-syntax",
                        "Metatecken och kvantifierare",
                        "grep med regex",
                        "Praktiska regex-mönster"
                    ]
                },
                {
                    type: "concept",
                    title: "Regex Grunderna",
                    explanation: `Reguljära uttryck matchar textmönster:

┌─────────┬─────────────────────────────────────────────────────┐
│ Tecken  │ Betydelse                                           │
├─────────┼─────────────────────────────────────────────────────┤
│ .       │ Matchar ETT valfritt tecken                         │
│ *       │ 0 eller fler av föregående                          │
│ +       │ 1 eller fler av föregående                          │
│ ?       │ 0 eller 1 av föregående                             │
│ ^       │ Början av rad                                       │
│ $       │ Slutet av rad                                       │
│ []      │ Teckenklasser [abc] eller [a-z]                     │
│ [^]     │ Negerad teckenklass [^abc]                          │
│ |       │ Alternativ (eller)                                  │
│ ()      │ Gruppering                                          │
└─────────┴─────────────────────────────────────────────────────┘`
                },
                {
                    type: "concept",
                    title: "Kvantifierare",
                    explanation: `┌─────────────┬───────────────────────────────────────────────┐
│ Kvantifierare│ Betydelse                                     │
├─────────────┼───────────────────────────────────────────────┤
│ {n}         │ Exakt n gånger                                 │
│ {n,}        │ n eller fler gånger                            │
│ {n,m}       │ Mellan n och m gånger                          │
│ *           │ Samma som {0,}                                 │
│ +           │ Samma som {1,}                                 │
│ ?           │ Samma som {0,1}                                │
└─────────────┴───────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "grep med regex",
                    language: "bash",
                    code: `# Grundläggande grep
grep "error" /var/log/syslog

# Extended regex (-E)
grep -E "error|warning" logfil.txt

# Case insensitive (-i)
grep -i "ERROR" logfil.txt

# Visa radnummer (-n)
grep -n "pattern" fil.txt

# Invertera matchning (-v)
grep -v "^#" config.conf   # Exkludera kommentarer

# Endast filnamn (-l)
grep -l "TODO" *.py`
                },
                {
                    type: "code",
                    title: "Praktiska regex-exempel",
                    language: "bash",
                    code: `# Matcha IP-adresser
grep -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" access.log

# Matcha e-postadresser
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" fil.txt

# Matcha datum (YYYY-MM-DD)
grep -E "[0-9]{4}-[0-9]{2}-[0-9]{2}" logg.txt

# Rader som börjar med siffra
grep "^[0-9]" fil.txt

# Rader som slutar med punkt
grep "\.$" fil.txt

# Tomma rader
grep "^$" fil.txt`
                },
                {
                    type: "quiz",
                    question: "Vad matchar regex-mönstret ^#?",
                    options: [
                        { text: "Rader som innehåller #", correct: false, feedback: "Nej, ^ betyder början" },
                        { text: "Rader som börjar med #", correct: true, feedback: "Rätt! ^ = radstart" },
                        { text: "Rader som slutar med #", correct: false, feedback: "Nej, $ är för radslut" },
                        { text: "Alla #-tecken", correct: false, feedback: "Nej, ^ begränsar till start" }
                    ],
                    hint: "^ betyder början av raden"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Regex! 🔍"
                }
            ]
        },
        {
            id: "doe25-1-4-sed",
            title: "1.4 sed - Stream Editor",
            description: "Textmanipulation med sed",
            order_index: 6,
            estimated_minutes: 50,
            content_blocks: [
                {
                    type: "intro",
                    headline: "✂️ sed - Stream Editor",
                    learning_objectives: [
                        "Grundläggande sed-syntax",
                        "Sök och ersätt",
                        "Radera och infoga rader",
                        "In-place editing"
                    ]
                },
                {
                    type: "concept",
                    title: "sed Syntax",
                    explanation: `sed processar text rad för rad:

┌─────────────────────────────────────────────────────────────┐
│  sed [OPTIONS] 'COMMAND' file                               │
│                                                             │
│  Vanliga options:                                           │
│  -i       In-place (ändra filen direkt)                     │
│  -n       Suppress automatic printing                       │
│  -e       Flera kommandon                                   │
│  -r/-E    Extended regex                                    │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Sök och ersätt",
                    language: "bash",
                    code: `# Grundläggande ersättning
sed 's/gammal/ny/' fil.txt           # Första på varje rad
sed 's/gammal/ny/g' fil.txt          # Alla förekomster
sed 's/gammal/ny/gi' fil.txt         # Case insensitive

# In-place editing (ändra filen)
sed -i 's/fel/rätt/g' fil.txt
sed -i.bak 's/fel/rätt/g' fil.txt    # Med backup

# Delimiter kan vara annat än /
sed 's|/usr/local|/opt|g' fil.txt
sed 's#http://#https://#g' fil.txt`
                },
                {
                    type: "code",
                    title: "Radera och visa rader",
                    language: "bash",
                    code: `# Radera rader
sed '/pattern/d' fil.txt             # Rader med pattern
sed '5d' fil.txt                     # Rad 5
sed '1,10d' fil.txt                  # Rad 1-10
sed '/^#/d' fil.txt                  # Kommentarer
sed '/^$/d' fil.txt                  # Tomma rader

# Visa specifika rader
sed -n '5p' fil.txt                  # Rad 5
sed -n '1,10p' fil.txt               # Rad 1-10
sed -n '/error/p' fil.txt            # Rader med error`
                },
                {
                    type: "code",
                    title: "Avancerade exempel",
                    language: "bash",
                    code: `# Infoga text
sed '1i\\Första raden' fil.txt       # Före rad 1
sed '$a\\Sista raden' fil.txt        # Efter sista

# Flera kommandon
sed -e 's/foo/bar/g' -e 's/baz/qux/g' fil.txt

# Adressering
sed '10,20s/old/new/g' fil.txt       # Rad 10-20
sed '/START/,/END/d' fil.txt         # Mellan mönster

# Gruppering och backreference
sed 's/\\(.*\\):\\(.*\\)/\\2:\\1/' fil.txt # Byt ordning`
                },
                {
                    type: "quiz",
                    question: "Vad gör sed 's/foo/bar/g' fil.txt?",
                    options: [
                        { text: "Ersätter första foo med bar", correct: false, feedback: "Nej, g gör alla" },
                        { text: "Ersätter alla foo med bar", correct: true, feedback: "Rätt! g = global" },
                        { text: "Raderar foo", correct: false, feedback: "Nej, s är för substitution" },
                        { text: "Söker efter foo", correct: false, feedback: "Nej, den ersätter" }
                    ],
                    hint: "g står för global"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat sed! ✂️"
                }
            ]
        },
        {
            id: "doe25-1-5-awk",
            title: "1.5 awk - Textbearbetning",
            description: "Kolumnbaserad textbearbetning med awk",
            order_index: 7,
            estimated_minutes: 55,
            content_blocks: [
                {
                    type: "intro",
                    headline: "📊 awk - Textbearbetning",
                    learning_objectives: [
                        "awk grundsyntax",
                        "Fält och kolumner",
                        "Mönstermatchning",
                        "Inbyggda variabler"
                    ]
                },
                {
                    type: "concept",
                    title: "awk Syntax",
                    explanation: `awk processar text kolumnvis:

┌─────────────────────────────────────────────────────────────┐
│  awk 'pattern { action }' file                              │
│                                                             │
│  Fält (kolumner):                                           │
│  $0  - Hela raden                                           │
│  $1  - Första fältet                                        │
│  $2  - Andra fältet                                         │
│  $NF - Sista fältet                                         │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Grundläggande awk",
                    language: "bash",
                    code: `# Skriv ut specifika kolumner
awk '{print $1}' fil.txt             # Första kolumnen
awk '{print $1, $3}' fil.txt         # Kolumn 1 och 3
awk '{print $NF}' fil.txt            # Sista kolumnen

# Annan delimiter (-F)
awk -F: '{print $1}' /etc/passwd     # Användarnamn
awk -F, '{print $2}' data.csv        # CSV kolumn 2

# Formaterad output
awk '{printf "%-10s %s\\n", $1, $2}' fil.txt`
                },
                {
                    type: "concept",
                    title: "Inbyggda variabler",
                    explanation: `┌─────────┬─────────────────────────────────────────────────────┐
│ Variabel│ Betydelse                                           │
├─────────┼─────────────────────────────────────────────────────┤
│ NR      │ Radnummer (Number of Record)                        │
│ NF      │ Antal fält på raden (Number of Fields)              │
│ FS      │ Fältseparator (Field Separator)                     │
│ OFS     │ Output field separator                              │
│ RS      │ Record separator (radbrytning)                      │
│ FILENAME│ Nuvarande filnamn                                   │
└─────────┴─────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Mönster och villkor",
                    language: "bash",
                    code: `# Med mönster
awk '/error/ {print}' logg.txt       # Rader med error
awk '$3 > 100 {print $1}' data.txt   # Villkor på kolumn

# BEGIN och END
awk 'BEGIN {print "Start"} {print} END {print "Slut"}' fil.txt

# Summera kolumn
awk '{sum += $1} END {print sum}' numbers.txt

# Räkna rader
awk 'END {print NR}' fil.txt

# Unika värden
awk '!seen[$1]++' fil.txt`
                },
                {
                    type: "code",
                    title: "Praktiska exempel",
                    language: "bash",
                    code: `# Analysera /etc/passwd
awk -F: '$3 >= 1000 {print $1}' /etc/passwd   # Vanliga users

# Diskutrymme per filsystem
df -h | awk 'NR>1 {print $5, $6}'

# Processer per användare
ps aux | awk '{count[$1]++} END {for (u in count) print u, count[u]}'

# Logganalys - requests per IP
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head`
                },
                {
                    type: "quiz",
                    question: "Vad skriver awk '{print $NF}' ut?",
                    options: [
                        { text: "Första fältet", correct: false, feedback: "Nej, det är $1" },
                        { text: "Sista fältet", correct: true, feedback: "Rätt! NF = Number of Fields" },
                        { text: "Antal fält", correct: false, feedback: "Nej, då skulle det vara print NF" },
                        { text: "Hela raden", correct: false, feedback: "Nej, det är $0" }
                    ],
                    hint: "NF står för Number of Fields"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat awk! 📊"
                }
            ]
        },
        {
            id: "doe25-1-6-villkor",
            title: "1.6 Villkor (if/else)",
            description: "Villkorssatser och test-kommandon i Bash",
            order_index: 8,
            estimated_minutes: 45,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🔀 Villkor (if/else)",
                    learning_objectives: [
                        "if/elif/else syntax",
                        "test-kommandot och [ ]",
                        "Strängjämförelser",
                        "Numeriska jämförelser",
                        "Filjämförelser"
                    ]
                },
                {
                    type: "concept",
                    title: "if/else Syntax",
                    explanation: `Grundläggande villkorsstruktur:

┌─────────────────────────────────────────────────────────────┐
│  if [ villkor ]; then                                       │
│      # kod om sant                                          │
│  elif [ annat_villkor ]; then                               │
│      # kod om annat sant                                    │
│  else                                                       │
│      # kod om falskt                                        │
│  fi                                                         │
└─────────────────────────────────────────────────────────────┘

VIKTIGT: Mellanslag krävs inuti [ ] !`
                },
                {
                    type: "concept",
                    title: "Jämförelseoperatorer",
                    explanation: `┌──────────────────────────────────────────────────────────────┐
│  STRÄNGAR:                                                   │
│  =, ==    Lika med         [ "$a" = "$b" ]                   │
│  !=      Inte lika         [ "$a" != "$b" ]                  │
│  -z      Tom sträng        [ -z "$str" ]                     │
│  -n      Ej tom            [ -n "$str" ]                     │
├──────────────────────────────────────────────────────────────┤
│  NUMMER:                                                     │
│  -eq     Equal             [ $a -eq $b ]                     │
│  -ne     Not equal         [ $a -ne $b ]                     │
│  -lt     Less than         [ $a -lt $b ]                     │
│  -le     Less or equal     [ $a -le $b ]                     │
│  -gt     Greater than      [ $a -gt $b ]                     │
│  -ge     Greater or equal  [ $a -ge $b ]                     │
└──────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "concept",
                    title: "Filtest",
                    explanation: `┌─────────┬─────────────────────────────────────────────────────┐
│ Test    │ Betydelse                                           │
├─────────┼─────────────────────────────────────────────────────┤
│ -e      │ Filen existerar                                     │
│ -f      │ Är en vanlig fil                                    │
│ -d      │ Är en katalog                                       │
│ -r      │ Är läsbar                                           │
│ -w      │ Är skrivbar                                         │
│ -x      │ Är exekverbar                                       │
│ -s      │ Har storlek > 0                                     │
│ -L      │ Är symbolisk länk                                   │
└─────────┴─────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Praktiska exempel",
                    language: "bash",
                    code: `#!/bin/bash

# Kontrollera fil
if [ -f "/etc/passwd" ]; then
    echo "Filen existerar"
else
    echo "Filen finns inte"
fi

# Numerisk jämförelse
age=25
if [ $age -ge 18 ]; then
    echo "Vuxen"
else
    echo "Minderårig"
fi

# Strängjämförelse
read -p "Ja eller Nej? " svar
if [ "$svar" = "ja" ]; then
    echo "Du svarade ja"
fi

# Kombinera villkor
if [ -f "$fil" ] && [ -r "$fil" ]; then
    echo "Fil finns och är läsbar"
fi`
                },
                {
                    type: "quiz",
                    question: "Hur testar du om variabeln $x är större än 10?",
                    options: [
                        { text: "[ $x > 10 ]", correct: false, feedback: "Nej, > är redirect i shell" },
                        { text: "[ $x -gt 10 ]", correct: true, feedback: "Rätt! -gt = greater than" },
                        { text: "[ $x greater 10 ]", correct: false, feedback: "Nej, fel syntax" },
                        { text: "if $x > 10", correct: false, feedback: "Nej, helt fel syntax" }
                    ],
                    hint: "-gt står för greater than"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Villkor! 🔀"
                }
            ]
        },
        {
            id: "doe25-1-7-interaktiva",
            title: "1.7 Interaktiva Skript",
            description: "Användarinput och menysystem",
            order_index: 9,
            estimated_minutes: 40,
            content_blocks: [
                {
                    type: "intro",
                    headline: "💬 Interaktiva Skript",
                    learning_objectives: [
                        "read-kommandot",
                        "select för menyer",
                        "case-satser",
                        "Användarvalidering"
                    ]
                },
                {
                    type: "code",
                    title: "read - Läsa input",
                    language: "bash",
                    code: `#!/bin/bash

# Enkel input
read -p "Ditt namn: " namn
echo "Hej $namn!"

# Med timeout
read -t 10 -p "Svara inom 10 sek: " svar

# Dold input (lösenord)
read -s -p "Lösenord: " password
echo  # Ny rad efter dold input

# Läs till array
read -a ord -p "Skriv ord: "
echo "Första ordet: \${ord[0]}"`
                },
                {
                    type: "code",
                    title: "select - Menyval",
                    language: "bash",
                    code: `#!/bin/bash

echo "Välj en frukt:"
select frukt in "Äpple" "Banan" "Citron" "Avsluta"; do
    case $frukt in
        "Äpple")
            echo "Du valde äpple"
            ;;
        "Banan")
            echo "Du valde banan"
            ;;
        "Citron")
            echo "Du valde citron"
            ;;
        "Avsluta")
            echo "Hejdå!"
            break
            ;;
        *)
            echo "Ogiltigt val"
            ;;
    esac
done`
                },
                {
                    type: "code",
                    title: "case - Mönstermatchning",
                    language: "bash",
                    code: `#!/bin/bash

read -p "Ange kommando: " cmd

case $cmd in
    start|begin)
        echo "Startar..."
        ;;
    stop|end)
        echo "Stoppar..."
        ;;
    status)
        echo "Visar status..."
        ;;
    *)
        echo "Okänt kommando: $cmd"
        echo "Använd: start|stop|status"
        exit 1
        ;;
esac`
                },
                {
                    type: "quiz",
                    question: "Hur läser du lösenord utan att visa det?",
                    options: [
                        { text: "read -p password", correct: false, feedback: "Nej, -p är för prompt" },
                        { text: "read -s password", correct: true, feedback: "Rätt! -s = silent/secret" },
                        { text: "read --hidden password", correct: false, feedback: "Nej, den flaggan finns inte" },
                        { text: "password = input()", correct: false, feedback: "Nej, det är Python" }
                    ],
                    hint: "-s gömmer input"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Interaktiva Skript! 💬"
                }
            ]
        },
        {
            id: "doe25-1-8-loopar",
            title: "1.8 Loopar (for/while)",
            description: "Iteration med for och while-loopar",
            order_index: 10,
            estimated_minutes: 50,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🔄 Loopar",
                    learning_objectives: [
                        "for-loopar",
                        "while-loopar",
                        "until-loopar",
                        "break och continue"
                    ]
                },
                {
                    type: "code",
                    title: "for-loopar",
                    language: "bash",
                    code: `#!/bin/bash

# Lista
for frukt in äpple banan citron; do
    echo "Frukt: $frukt"
done

# Range
for i in {1..5}; do
    echo "Nummer: $i"
done

# Med steg
for i in {0..10..2}; do
    echo "Jämnt: $i"
done

# C-style
for ((i=0; i<5; i++)); do
    echo "Index: $i"
done

# Filer i katalog
for fil in *.txt; do
    echo "Bearbetar: $fil"
done`
                },
                {
                    type: "code",
                    title: "while-loopar",
                    language: "bash",
                    code: `#!/bin/bash

# Enkel while
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

# Läs fil rad för rad
while IFS= read -r line; do
    echo "Rad: $line"
done < fil.txt

# Oändlig loop med break
while true; do
    read -p "Kommando (q=quit): " cmd
    [ "$cmd" = "q" ] && break
    echo "Du skrev: $cmd"
done`
                },
                {
                    type: "code",
                    title: "until och kontroll",
                    language: "bash",
                    code: `#!/bin/bash

# until - kör tills villkoret är sant
count=1
until [ $count -gt 5 ]; do
    echo "Count: $count"
    ((count++))
done

# break - avbryt loop
for i in {1..10}; do
    [ $i -eq 5 ] && break
    echo $i
done

# continue - hoppa till nästa iteration
for i in {1..5}; do
    [ $i -eq 3 ] && continue
    echo $i    # Skriver 1 2 4 5
done`
                },
                {
                    type: "quiz",
                    question: "Hur loopar du genom filer med .log-extension?",
                    options: [
                        { text: "for f in *.log; do", correct: true, feedback: "Rätt! Glob-mönster fungerar i for" },
                        { text: "foreach *.log", correct: false, feedback: "Nej, det är annan syntax" },
                        { text: "while *.log; do", correct: false, feedback: "Nej, while tar villkor" },
                        { text: "loop files *.log", correct: false, feedback: "Nej, det finns inte" }
                    ],
                    hint: "for med glob-mönster"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Loopar! 🔄"
                }
            ]
        },
        {
            id: "doe25-1-9-parametrar",
            title: "1.9 Skriptparametrar",
            description: "Hantera argument och options i skript",
            order_index: 11,
            estimated_minutes: 45,
            content_blocks: [
                {
                    type: "intro",
                    headline: "📥 Skriptparametrar",
                    learning_objectives: [
                        "Positionsparametrar ($1, $2...)",
                        "Specialvariabler ($#, $@, $*)",
                        "shift-kommandot",
                        "getopts för flaggor"
                    ]
                },
                {
                    type: "concept",
                    title: "Positionsparametrar",
                    explanation: `┌─────────┬─────────────────────────────────────────────────────┐
│ Variabel│ Betydelse                                           │
├─────────┼─────────────────────────────────────────────────────┤
│ $0      │ Skriptets namn                                      │
│ $1-$9   │ Argument 1-9                                        │
│ \${10}   │ Argument 10+                                        │
│ $#      │ Antal argument                                      │
│ $@      │ Alla argument (separata)                            │
│ $*      │ Alla argument (en sträng)                           │
│ $?      │ Exit code från förra kommandot                      │
│ $$      │ Skriptets PID                                       │
└─────────┴─────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Grundläggande parametrar",
                    language: "bash",
                    code: `#!/bin/bash
# Kör: ./script.sh arg1 arg2 arg3

echo "Skript: $0"
echo "Första arg: $1"
echo "Andra arg: $2"
echo "Antal args: $#"
echo "Alla args: $@"

# Loopa genom alla
for arg in "$@"; do
    echo "Argument: $arg"
done

# Kontrollera antal
if [ $# -lt 2 ]; then
    echo "Usage: $0 <arg1> <arg2>"
    exit 1
fi`
                },
                {
                    type: "code",
                    title: "getopts för flaggor",
                    language: "bash",
                    code: `#!/bin/bash
# Kör: ./script.sh -v -f filnamn -n 5

verbose=false
filename=""
count=1

while getopts "vf:n:" opt; do
    case $opt in
        v) verbose=true ;;
        f) filename="$OPTARG" ;;
        n) count="$OPTARG" ;;
        ?) echo "Usage: $0 [-v] [-f file] [-n num]"
           exit 1 ;;
    esac
done

echo "Verbose: $verbose"
echo "File: $filename"
echo "Count: $count"`
                },
                {
                    type: "quiz",
                    question: "Vad innehåller $# i ett skript?",
                    options: [
                        { text: "Skriptets namn", correct: false, feedback: "Nej, det är $0" },
                        { text: "Antal argument", correct: true, feedback: "Rätt! # = antal" },
                        { text: "Alla argument", correct: false, feedback: "Nej, det är $@ eller $*" },
                        { text: "Exit code", correct: false, feedback: "Nej, det är $?" }
                    ],
                    hint: "# brukar betyda antal/nummer"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Skriptparametrar! 📥"
                }
            ]
        },
        {
            id: "doe25-1-10-funktioner",
            title: "1.10 Funktioner",
            description: "Återanvändbar kod med funktioner",
            order_index: 12,
            estimated_minutes: 45,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🔧 Funktioner",
                    learning_objectives: [
                        "Definiera funktioner",
                        "Parametrar och returvärden",
                        "Lokala variabler",
                        "Rekursion"
                    ]
                },
                {
                    type: "code",
                    title: "Definiera funktioner",
                    language: "bash",
                    code: `#!/bin/bash

# Syntax 1
function hello() {
    echo "Hej från funktion!"
}

# Syntax 2 (POSIX)
goodbye() {
    echo "Hejdå!"
}

# Anropa
hello
goodbye`
                },
                {
                    type: "code",
                    title: "Parametrar och return",
                    language: "bash",
                    code: `#!/bin/bash

# Funktion med parametrar
greet() {
    local name="$1"    # Lokal variabel
    local age="$2"
    echo "Hej $name, du är $age år"
}

# Anropa med argument
greet "Anna" 25

# Return value (0-255)
is_even() {
    if [ $(($1 % 2)) -eq 0 ]; then
        return 0   # true
    else
        return 1   # false
    fi
}

if is_even 4; then
    echo "4 är jämnt"
fi`
                },
                {
                    type: "code",
                    title: "Returnera data",
                    language: "bash",
                    code: `#!/bin/bash

# Returnera via echo (capture med $())
get_date() {
    date +%Y-%m-%d
}
today=$(get_date)
echo "Idag: $today"

# Returnera via global variabel
calculate() {
    result=$(($1 + $2))
}
calculate 5 3
echo "Summa: $result"`
                },
                {
                    type: "quiz",
                    question: "Hur gör du en variabel lokal i en funktion?",
                    options: [
                        { text: "var name=value", correct: false, feedback: "Nej, det är globalt" },
                        { text: "local name=value", correct: true, feedback: "Rätt! local begränsar scope" },
                        { text: "private name=value", correct: false, feedback: "Nej, finns inte i bash" },
                        { text: "my name=value", correct: false, feedback: "Nej, det är Perl" }
                    ],
                    hint: "Nyckelordet är 'local'"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Funktioner! 🔧"
                }
            ]
        },
        {
            id: "doe25-1-11-signals",
            title: "1.11 Signaler & Traps",
            description: "Hantera signaler och cleanup",
            order_index: 13,
            estimated_minutes: 40,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🚨 Signaler & Traps",
                    learning_objectives: [
                        "Vanliga Unix-signaler",
                        "trap-kommandot",
                        "Cleanup vid avslut",
                        "Hantera Ctrl+C"
                    ]
                },
                {
                    type: "concept",
                    title: "Vanliga signaler",
                    explanation: `┌─────────┬─────────┬───────────────────────────────────────────┐
│ Signal  │ Nummer  │ Beskrivning                               │
├─────────┼─────────┼───────────────────────────────────────────┤
│ SIGHUP  │ 1       │ Hangup (terminal stängd)                  │
│ SIGINT  │ 2       │ Interrupt (Ctrl+C)                        │
│ SIGQUIT │ 3       │ Quit (Ctrl+\\)                             │
│ SIGKILL │ 9       │ Kill (kan ej fångas)                      │
│ SIGTERM │ 15      │ Terminate (default för kill)              │
│ SIGSTOP │ 19      │ Stop (kan ej fångas)                      │
└─────────┴─────────┴───────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "trap - Fånga signaler",
                    language: "bash",
                    code: `#!/bin/bash

# Cleanup-funktion
cleanup() {
    echo "Städar upp..."
    rm -f /tmp/myapp_*.tmp
    exit 0
}

# Fånga signaler
trap cleanup SIGINT SIGTERM EXIT

# Skapa tempfil
tmpfile=$(mktemp /tmp/myapp_XXXXXX.tmp)
echo "Tempfil: $tmpfile"

# Huvudloop
echo "Tryck Ctrl+C för att avsluta..."
while true; do
    sleep 1
done`
                },
                {
                    type: "code",
                    title: "Praktiska trap-exempel",
                    language: "bash",
                    code: `#!/bin/bash

# Ignorera Ctrl+C
trap '' SIGINT
echo "Ctrl+C ignoreras..."

# Återställ default
trap - SIGINT

# Trap på error
trap 'echo "Fel på rad $LINENO"' ERR

# Cleanup vid alla exits
trap 'rm -f "$lockfile"' EXIT
lockfile="/var/run/myapp.lock"`
                },
                {
                    type: "quiz",
                    question: "Vilken signal skickas vid Ctrl+C?",
                    options: [
                        { text: "SIGKILL", correct: false, feedback: "Nej, SIGKILL är signal 9" },
                        { text: "SIGTERM", correct: false, feedback: "Nej, SIGTERM är default för kill" },
                        { text: "SIGINT", correct: true, feedback: "Rätt! INT = Interrupt" },
                        { text: "SIGHUP", correct: false, feedback: "Nej, HUP är hangup" }
                    ],
                    hint: "INT = Interrupt"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Signaler! 🚨 MODUL 1 KLAR!"
                }
            ]
        },
        // ============================================
        // MODUL 2: LINUX SYSTEM ADMINISTRATION (8 tasks)
        // ============================================
        {
            id: "doe25-2-1-users",
            title: "2.1 Användarhantering",
            description: "Skapa och hantera användare och grupper",
            order_index: 14,
            estimated_minutes: 50,
            content_blocks: [
                {
                    type: "intro",
                    headline: "👤 Användarhantering",
                    learning_objectives: [
                        "Skapa och ta bort användare",
                        "Gruppadministration",
                        "passwd, shadow och group-filer",
                        "sudo-konfiguration"
                    ]
                },
                {
                    type: "concept",
                    title: "Viktiga filer",
                    explanation: `┌─────────────────────────────────────────────────────────────┐
│  /etc/passwd   - Användarinfo (alla kan läsa)               │
│  Format: user:x:UID:GID:GECOS:home:shell                    │
│                                                             │
│  /etc/shadow   - Lösenord (endast root)                     │
│  Format: user:hash:lastchg:min:max:warn:inactive:expire     │
│                                                             │
│  /etc/group    - Gruppinfo                                  │
│  Format: group:x:GID:members                                │
│                                                             │
│  /etc/sudoers  - sudo-behörigheter                          │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Användarkommandon",
                    language: "bash",
                    code: `# Skapa användare
sudo useradd -m -s /bin/bash anna    # Med hemkatalog
sudo useradd -m -G sudo,docker bob   # Med grupper

# Sätt lösenord
sudo passwd anna

# Ändra användare
sudo usermod -aG docker anna         # Lägg till i grupp
sudo usermod -s /bin/zsh anna        # Ändra shell

# Ta bort användare
sudo userdel anna                    # Behåll hemkatalog
sudo userdel -r anna                 # Ta bort allt

# Visa info
id anna
groups anna
getent passwd anna`
                },
                {
                    type: "code",
                    title: "Grupphantering",
                    language: "bash",
                    code: `# Skapa grupp
sudo groupadd developers

# Lägg till användare i grupp
sudo usermod -aG developers anna

# Ta bort från grupp
sudo gpasswd -d anna developers

# Ta bort grupp
sudo groupdel developers

# Visa grupper
groups
cat /etc/group | grep developers`
                },
                {
                    type: "quiz",
                    question: "Var lagras krypterade lösenord?",
                    options: [
                        { text: "/etc/passwd", correct: false, feedback: "Nej, där finns bara x" },
                        { text: "/etc/shadow", correct: true, feedback: "Rätt! shadow är skyddad" },
                        { text: "/etc/security", correct: false, feedback: "Nej, fel katalog" },
                        { text: "/home/user/.password", correct: false, feedback: "Nej, finns inte" }
                    ],
                    hint: "shadow = skugga (dolt)"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Användarhantering! 👤"
                }
            ]
        },
        {
            id: "doe25-2-2-permissions",
            title: "2.2 Filrättigheter",
            description: "Behörigheter, chmod och chown",
            order_index: 15,
            estimated_minutes: 55,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🔐 Filrättigheter",
                    learning_objectives: [
                        "rwx-systemet",
                        "chmod (symbolisk och numerisk)",
                        "chown och chgrp",
                        "Speciella bitar (SUID, SGID, sticky)"
                    ]
                },
                {
                    type: "concept",
                    title: "Rättighetssystemet",
                    explanation: `Linux använder rwx för tre kategorier:

┌─────────────────────────────────────────────────────────────┐
│  -rwxr-xr-x  1 anna developers 4096 Jan 1 file.txt         │
│  │└┬┘└┬┘└┬┘                                                 │
│  │ │  │  └── Others (alla andra)                            │
│  │ │  └───── Group (gruppmedlemmar)                         │
│  │ └──────── User/Owner (ägaren)                            │
│  └────────── Filtyp (- = fil, d = katalog)                  │
├─────────────────────────────────────────────────────────────┤
│  r = read (4)    - Läsa fil / lista katalog                 │
│  w = write (2)   - Ändra fil / skapa i katalog              │
│  x = execute (1) - Köra fil / gå in i katalog               │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "chmod - Ändra rättigheter",
                    language: "bash",
                    code: `# Numeriskt (oktalt)
chmod 755 script.sh      # rwxr-xr-x
chmod 644 config.txt     # rw-r--r--
chmod 700 privat/        # rwx------

# Symboliskt
chmod u+x script.sh      # Ge user execute
chmod g-w fil.txt        # Ta bort group write
chmod o=r fil.txt        # Sätt others till read
chmod a+r fil.txt        # Alla får read

# Rekursivt
chmod -R 755 katalog/`
                },
                {
                    type: "code",
                    title: "chown/chgrp - Ändra ägare",
                    language: "bash",
                    code: `# Ändra ägare
sudo chown anna fil.txt
sudo chown anna:developers fil.txt   # Ägare och grupp

# Ändra grupp
sudo chgrp developers fil.txt

# Rekursivt
sudo chown -R www-data:www-data /var/www/`
                },
                {
                    type: "concept",
                    title: "Speciella bitar",
                    explanation: `┌─────────┬─────────┬───────────────────────────────────────────┐
│ Bit     │ Nummer  │ Effekt                                    │
├─────────┼─────────┼───────────────────────────────────────────┤
│ SUID    │ 4000    │ Kör som filens ägare                      │
│ SGID    │ 2000    │ Kör som filens grupp / ärv grupp          │
│ Sticky  │ 1000    │ Endast ägare kan radera (t.ex. /tmp)      │
└─────────┴─────────┴───────────────────────────────────────────┘

chmod 4755 fil      # SUID + rwxr-xr-x
chmod 2755 katalog  # SGID
chmod 1777 /tmp     # Sticky + rwxrwxrwx`
                },
                {
                    type: "quiz",
                    question: "Vad betyder chmod 644?",
                    options: [
                        { text: "rwxrwxrwx", correct: false, feedback: "Nej, det är 777" },
                        { text: "rw-r--r--", correct: true, feedback: "Rätt! 6=rw, 4=r, 4=r" },
                        { text: "rwxr-xr-x", correct: false, feedback: "Nej, det är 755" },
                        { text: "rw-rw-rw-", correct: false, feedback: "Nej, det är 666" }
                    ],
                    hint: "6=4+2=r+w, 4=r"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Filrättigheter! 🔐"
                }
            ]
        },
        {
            id: "doe25-2-3-ssh",
            title: "2.3 SSH & Säkerhet",
            description: "SSH-konfiguration och nyckelautentisering",
            order_index: 16,
            estimated_minutes: 50,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🔑 SSH & Säkerhet",
                    learning_objectives: [
                        "SSH-nyckelpar",
                        "SSH-konfiguration",
                        "sshd_config säkerhet",
                        "SSH tunnlar"
                    ]
                },
                {
                    type: "code",
                    title: "SSH-nycklar",
                    language: "bash",
                    code: `# Generera nyckelpar
ssh-keygen -t ed25519 -C "email@example.com"
ssh-keygen -t rsa -b 4096 -C "email@example.com"

# Kopiera publik nyckel till server
ssh-copy-id user@server
# Eller manuellt:
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys

# SSH-agent
eval $(ssh-agent)
ssh-add ~/.ssh/id_ed25519`
                },
                {
                    type: "concept",
                    title: "SSH-filer",
                    explanation: `┌─────────────────────────────────────────────────────────────┐
│  ~/.ssh/                                                    │
│  ├── id_ed25519        ← Privat nyckel (SKYDDA!)            │
│  ├── id_ed25519.pub    ← Publik nyckel (dela ut)            │
│  ├── authorized_keys   ← Tillåtna publika nycklar           │
│  ├── known_hosts       ← Kända servrar                      │
│  └── config            ← Klientkonfiguration                │
│                                                             │
│  /etc/ssh/                                                  │
│  └── sshd_config       ← Serverkonfiguration                │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Säkra sshd_config",
                    language: "bash",
                    code: `# /etc/ssh/sshd_config

# Stäng av root-login
PermitRootLogin no

# Bara nyckelautentisering
PasswordAuthentication no
PubkeyAuthentication yes

# Begränsa användare
AllowUsers anna bob
AllowGroups sshusers

# Ändra port (security through obscurity)
Port 2222

# Starta om efter ändringar
sudo systemctl restart sshd`
                },
                {
                    type: "code",
                    title: "SSH tunnlar",
                    language: "bash",
                    code: `# Lokal tunnel (local port forwarding)
# Nå remote:3306 via localhost:3307
ssh -L 3307:localhost:3306 user@server

# Remote tunnel (remote port forwarding)
# Exponera lokal port på remote server
ssh -R 8080:localhost:80 user@server

# SOCKS proxy
ssh -D 1080 user@server`
                },
                {
                    type: "quiz",
                    question: "Vilken fil innehåller tillåtna publika nycklar?",
                    options: [
                        { text: "~/.ssh/id_rsa.pub", correct: false, feedback: "Nej, det är din publik nyckel" },
                        { text: "~/.ssh/authorized_keys", correct: true, feedback: "Rätt!" },
                        { text: "~/.ssh/known_hosts", correct: false, feedback: "Nej, det är kända servrar" },
                        { text: "/etc/ssh/sshd_config", correct: false, feedback: "Nej, det är serverkonfig" }
                    ],
                    hint: "authorized = tillåtna"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat SSH! 🔑"
                }
            ]
        },
        {
            id: "doe25-2-4-ufw",
            title: "2.4 UFW Brandvägg",
            description: "Enkel brandväggskonfiguration med UFW",
            order_index: 17,
            estimated_minutes: 40,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🛡️ UFW Brandvägg",
                    learning_objectives: [
                        "UFW grundläggande användning",
                        "Tillåta och blockera portar",
                        "Applikationsprofiler",
                        "Loggning"
                    ]
                },
                {
                    type: "concept",
                    title: "UFW - Uncomplicated Firewall",
                    explanation: `UFW är ett användarvänligt gränssnitt till iptables:

┌─────────────────────────────────────────────────────────────┐
│  UFW är DEFAULT på Ubuntu/Debian                            │
│  Förenklar brandväggsregler betydligt                       │
│  Arbetar med INPUT/OUTPUT/FORWARD chains                    │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Grundläggande UFW",
                    language: "bash",
                    code: `# Status
sudo ufw status
sudo ufw status verbose

# Aktivera/avaktivera
sudo ufw enable
sudo ufw disable

# Default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Tillåt port
sudo ufw allow 22              # SSH
sudo ufw allow 80/tcp          # HTTP
sudo ufw allow 443/tcp         # HTTPS

# Blockera
sudo ufw deny 23               # Telnet`
                },
                {
                    type: "code",
                    title: "Avancerade regler",
                    language: "bash",
                    code: `# Tillåt från specifik IP
sudo ufw allow from 192.168.1.100
sudo ufw allow from 192.168.1.0/24 to any port 22

# Begränsa (rate limiting)
sudo ufw limit ssh             # Max 6 conn/30s

# Applikationsprofiler
sudo ufw app list
sudo ufw allow 'Nginx Full'
sudo ufw allow 'OpenSSH'

# Ta bort regel
sudo ufw delete allow 80
sudo ufw status numbered
sudo ufw delete 3`
                },
                {
                    type: "quiz",
                    question: "Hur tillåter du SSH med UFW?",
                    options: [
                        { text: "ufw open 22", correct: false, feedback: "Nej, fel syntax" },
                        { text: "ufw allow 22", correct: true, feedback: "Rätt!" },
                        { text: "ufw permit ssh", correct: false, feedback: "Nej, fel syntax" },
                        { text: "ufw enable ssh", correct: false, feedback: "Nej, enable aktiverar UFW" }
                    ],
                    hint: "allow = tillåt"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat UFW! 🛡️"
                }
            ]
        },
        {
            id: "doe25-2-5-firewalld",
            title: "2.5 Firewalld",
            description: "Brandvägg för RHEL/CentOS med zoner",
            order_index: 18,
            estimated_minutes: 45,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🔥 Firewalld",
                    learning_objectives: [
                        "Zoner och tjänster",
                        "firewall-cmd kommandon",
                        "Permanenta vs runtime regler",
                        "Rich rules"
                    ]
                },
                {
                    type: "concept",
                    title: "Firewalld zoner",
                    explanation: `Firewalld använder zoner för olika säkerhetsnivåer:

┌─────────────────────────────────────────────────────────────┐
│  drop      - Droppa allt, ingen respons                     │
│  block     - Reject med ICMP prohibited                     │
│  public    - Opålitligt (default för nya interfaces)        │
│  external  - För NAT/masquerading                           │
│  dmz       - Demilitariserad zon                            │
│  work      - Arbetsdatorer                                  │
│  home      - Hemdatorer                                     │
│  internal  - Interna nät                                    │
│  trusted   - Tillåt allt                                    │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "firewall-cmd grunderna",
                    language: "bash",
                    code: `# Status
sudo firewall-cmd --state
sudo firewall-cmd --list-all

# Zoner
sudo firewall-cmd --get-zones
sudo firewall-cmd --get-default-zone
sudo firewall-cmd --get-active-zones

# Lista tjänster
sudo firewall-cmd --get-services
sudo firewall-cmd --list-services`
                },
                {
                    type: "code",
                    title: "Hantera regler",
                    language: "bash",
                    code: `# Tillåt tjänst (runtime)
sudo firewall-cmd --add-service=http

# Permanent (överlevener reboot)
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload

# Tillåt port
sudo firewall-cmd --permanent --add-port=8080/tcp

# Ta bort
sudo firewall-cmd --permanent --remove-service=http

# Ändra zon för interface
sudo firewall-cmd --zone=trusted --change-interface=eth1`
                },
                {
                    type: "quiz",
                    question: "Hur gör du en firewalld-regel permanent?",
                    options: [
                        { text: "--save", correct: false, feedback: "Nej, det finns inte" },
                        { text: "--permanent", correct: true, feedback: "Rätt! Och glöm inte --reload" },
                        { text: "--persist", correct: false, feedback: "Nej, fel flagga" },
                        { text: "firewall-cmd save", correct: false, feedback: "Nej, fel syntax" }
                    ],
                    hint: "permanent = beständig"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Firewalld! 🔥"
                }
            ]
        },
        {
            id: "doe25-2-6-lagring",
            title: "2.6 Lagring & Filsystem",
            description: "Partitioner, LVM och montering",
            order_index: 19,
            estimated_minutes: 55,
            content_blocks: [
                {
                    type: "intro",
                    headline: "💾 Lagring & Filsystem",
                    learning_objectives: [
                        "Partitionering (fdisk, parted)",
                        "Filsystem (ext4, xfs)",
                        "Montering och fstab",
                        "LVM grunderna"
                    ]
                },
                {
                    type: "concept",
                    title: "Lagringsstack",
                    explanation: `┌─────────────────────────────────────────────────────────────┐
│  Applikation                                                │
│       ↓                                                     │
│  Filsystem (ext4, xfs, btrfs)                              │
│       ↓                                                     │
│  LVM (valfritt) - Logical Volume Manager                    │
│       ↓                                                     │
│  Partition (/dev/sda1, /dev/nvme0n1p1)                     │
│       ↓                                                     │
│  Disk (/dev/sda, /dev/nvme0n1)                             │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Diskhantering",
                    language: "bash",
                    code: `# Lista diskar och partitioner
lsblk
fdisk -l
blkid

# Partitionera (interaktivt)
sudo fdisk /dev/sdb
# n = ny partition
# p = primär
# w = skriv och avsluta

# Skapa filsystem
sudo mkfs.ext4 /dev/sdb1
sudo mkfs.xfs /dev/sdb2`
                },
                {
                    type: "code",
                    title: "Montering",
                    language: "bash",
                    code: `# Manuell montering
sudo mount /dev/sdb1 /mnt/data
sudo mount -t ext4 /dev/sdb1 /mnt/data

# Avmontera
sudo umount /mnt/data

# Visa monterade
mount | grep sdb
df -h

# Permanent i /etc/fstab
# <device>     <mount>   <type>  <options>  <dump> <pass>
/dev/sdb1      /data     ext4    defaults   0      2
UUID=xxx-xxx   /backup   xfs     defaults   0      2`
                },
                {
                    type: "code",
                    title: "LVM grunderna",
                    language: "bash",
                    code: `# Physical Volume
sudo pvcreate /dev/sdb /dev/sdc
sudo pvs

# Volume Group
sudo vgcreate vg_data /dev/sdb /dev/sdc
sudo vgs

# Logical Volume
sudo lvcreate -L 10G -n lv_mysql vg_data
sudo lvcreate -l 100%FREE -n lv_www vg_data
sudo lvs

# Skapa filsystem och mounta
sudo mkfs.ext4 /dev/vg_data/lv_mysql
sudo mount /dev/vg_data/lv_mysql /var/lib/mysql`
                },
                {
                    type: "quiz",
                    question: "Var konfigureras automatisk montering vid boot?",
                    options: [
                        { text: "/etc/mount", correct: false, feedback: "Nej, finns inte" },
                        { text: "/etc/fstab", correct: true, feedback: "Rätt! fstab = file system table" },
                        { text: "/etc/disks", correct: false, feedback: "Nej, finns inte" },
                        { text: "/boot/mount.conf", correct: false, feedback: "Nej, finns inte" }
                    ],
                    hint: "fstab = file system table"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Lagring! 💾"
                }
            ]
        },
        {
            id: "doe25-2-7-backup",
            title: "2.7 Backup & Återställning",
            description: "rsync, tar och backupstrategier",
            order_index: 20,
            estimated_minutes: 45,
            content_blocks: [
                {
                    type: "intro",
                    headline: "📦 Backup & Återställning",
                    learning_objectives: [
                        "tar för arkivering",
                        "rsync för synkronisering",
                        "Backupstrategier",
                        "Automatisering med cron"
                    ]
                },
                {
                    type: "code",
                    title: "tar - Arkivering",
                    language: "bash",
                    code: `# Skapa arkiv
tar -cvf backup.tar /path/to/dir          # Utan komprimering
tar -czvf backup.tar.gz /path/to/dir      # gzip
tar -cjvf backup.tar.bz2 /path/to/dir     # bzip2

# Extrahera
tar -xvf backup.tar
tar -xzvf backup.tar.gz -C /destination

# Lista innehåll
tar -tvf backup.tar.gz

# Exkludera
tar -czvf backup.tar.gz --exclude='*.log' /path`
                },
                {
                    type: "code",
                    title: "rsync - Synkronisering",
                    language: "bash",
                    code: `# Lokal synk
rsync -av /source/ /destination/

# Remote via SSH
rsync -avz /local/path/ user@server:/remote/path/
rsync -avz user@server:/remote/ /local/

# Viktiga flaggor
# -a = archive (behåll permissions, symlinks etc)
# -v = verbose
# -z = komprimera under överföring
# --delete = ta bort filer som inte finns i source
# --dry-run = testa utan att göra ändringar

rsync -avz --delete --dry-run /source/ /dest/`
                },
                {
                    type: "concept",
                    title: "Backupstrategier",
                    explanation: `┌─────────────────────────────────────────────────────────────┐
│  3-2-1 REGELN:                                              │
│  • 3 kopior av data                                         │
│  • 2 olika mediatyper                                       │
│  • 1 offsite (annan plats)                                  │
├─────────────────────────────────────────────────────────────┤
│  TYPER:                                                     │
│  • Full     - Allt varje gång                               │
│  • Incremental - Bara ändrat sedan förra backup             │
│  • Differential - Ändrat sedan senaste FULLA backup         │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Automatiserad backup",
                    language: "bash",
                    code: `#!/bin/bash
# backup.sh

DATE=$(date +%Y%m%d)
BACKUP_DIR="/backup"
SOURCE="/var/www"

# Skapa daterad backup
tar -czvf "$BACKUP_DIR/www_$DATE.tar.gz" "$SOURCE"

# Ta bort backups äldre än 7 dagar
find "$BACKUP_DIR" -name "www_*.tar.gz" -mtime +7 -delete

# Cron: 0 2 * * * /path/to/backup.sh`
                },
                {
                    type: "quiz",
                    question: "Vad gör rsync --delete?",
                    options: [
                        { text: "Raderar källfiler", correct: false, feedback: "Nej, det vore farligt!" },
                        { text: "Raderar filer i mål som inte finns i källa", correct: true, feedback: "Rätt! Gör målet identiskt med källan" },
                        { text: "Raderar rsync-cachen", correct: false, feedback: "Nej, det finns ingen sådan" },
                        { text: "Avbryter synkroniseringen", correct: false, feedback: "Nej, fel" }
                    ],
                    hint: "Synkroniserar = gör identiska"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Backup! 📦"
                }
            ]
        },
        {
            id: "doe25-2-8-systemd",
            title: "2.8 Systemd & Tjänster",
            description: "Tjänstehantering med systemd",
            order_index: 21,
            estimated_minutes: 50,
            content_blocks: [
                {
                    type: "intro",
                    headline: "⚙️ Systemd & Tjänster",
                    learning_objectives: [
                        "systemctl kommandon",
                        "Tjänstestatus och loggar",
                        "Skapa egna unit-filer",
                        "Targets och runlevels"
                    ]
                },
                {
                    type: "code",
                    title: "systemctl grunderna",
                    language: "bash",
                    code: `# Starta/stoppa/restarta
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx      # Ladda om config

# Status
systemctl status nginx
systemctl is-active nginx
systemctl is-enabled nginx

# Aktivera/avaktivera vid boot
sudo systemctl enable nginx
sudo systemctl disable nginx
sudo systemctl enable --now nginx  # Enable + start`
                },
                {
                    type: "code",
                    title: "Loggar med journalctl",
                    language: "bash",
                    code: `# Loggar för tjänst
journalctl -u nginx
journalctl -u nginx -f           # Följ (tail -f)
journalctl -u nginx --since today
journalctl -u nginx -n 50        # Senaste 50 rader

# Systemloggar
journalctl -b                    # Sedan boot
journalctl -p err                # Bara errors
journalctl --disk-usage          # Loggstorlek`
                },
                {
                    type: "concept",
                    title: "Unit-fil struktur",
                    explanation: `Unit-filer ligger i /etc/systemd/system/:

┌─────────────────────────────────────────────────────────────┐
│  [Unit]                                                     │
│  Description=Min Applikation                                │
│  After=network.target                                       │
│                                                             │
│  [Service]                                                  │
│  Type=simple                                                │
│  User=www-data                                              │
│  WorkingDirectory=/app                                      │
│  ExecStart=/app/start.sh                                    │
│  Restart=always                                             │
│                                                             │
│  [Install]                                                  │
│  WantedBy=multi-user.target                                 │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Skapa egen tjänst",
                    language: "bash",
                    code: `# /etc/systemd/system/myapp.service
[Unit]
Description=My Node App
After=network.target

[Service]
Type=simple
User=node
WorkingDirectory=/var/www/myapp
ExecStart=/usr/bin/node server.js
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target

# Aktivera
sudo systemctl daemon-reload
sudo systemctl enable --now myapp`
                },
                {
                    type: "quiz",
                    question: "Hur laddar du om systemd efter ändring i unit-fil?",
                    options: [
                        { text: "systemctl restart", correct: false, feedback: "Nej, det startar om tjänsten" },
                        { text: "systemctl daemon-reload", correct: true, feedback: "Rätt! Laddar om konfigurationen" },
                        { text: "systemctl reload-config", correct: false, feedback: "Nej, finns inte" },
                        { text: "service reload", correct: false, feedback: "Nej, gammalt system" }
                    ],
                    hint: "daemon-reload läser om unit-filer"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Systemd! ⚙️ MODUL 2 KLAR!"
                }
            ]
        },
        // ============================================
        // MODUL 3: DEVOPS (4 tasks)
        // ============================================
        {
            id: "doe25-3-1-docker-grunder",
            title: "3.1 Docker Grunder",
            description: "Containers och grundläggande Docker-kommandon",
            order_index: 22,
            estimated_minutes: 55,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🐳 Docker Grunder",
                    learning_objectives: [
                        "Containers vs VMs",
                        "docker run och livscykel",
                        "Hantera containers",
                        "Volymer och nätverk"
                    ]
                },
                {
                    type: "concept",
                    title: "Containers vs VMs",
                    explanation: `┌─────────────────────────────────────────────────────────────┐
│  VM:                        Container:                      │
│  ┌─────────┬─────────┐     ┌─────────┬─────────┐           │
│  │  App A  │  App B  │     │  App A  │  App B  │           │
│  ├─────────┼─────────┤     ├─────────┴─────────┤           │
│  │ Guest OS│ Guest OS│     │   Container Engine │           │
│  ├─────────┴─────────┤     ├───────────────────┤           │
│  │    Hypervisor     │     │    Host OS         │           │
│  ├───────────────────┤     ├───────────────────┤           │
│  │    Hardware       │     │    Hardware        │           │
│  └───────────────────┘     └───────────────────┘           │
│                                                             │
│  • Tyngre, GB-storlek       • Lättare, MB-storlek          │
│  • Minuter att starta       • Sekunder att starta          │
│  • Full isolering           • Delar kernel                  │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "docker run",
                    language: "bash",
                    code: `# Kör container
docker run hello-world
docker run -it ubuntu bash           # Interaktiv
docker run -d nginx                  # Bakgrund (detached)
docker run -d -p 8080:80 nginx       # Port mapping
docker run -d --name web nginx       # Namnge

# Med volymer
docker run -v /host/path:/container/path nginx
docker run -v myvolume:/data nginx

# Med miljövariabler
docker run -e MYSQL_ROOT_PASSWORD=secret mysql`
                },
                {
                    type: "code",
                    title: "Hantera containers",
                    language: "bash",
                    code: `# Lista
docker ps                    # Körande
docker ps -a                 # Alla

# Starta/stoppa
docker start container_name
docker stop container_name
docker restart container_name

# Ta bort
docker rm container_name
docker rm -f container_name  # Force

# Loggar
docker logs container_name
docker logs -f container_name  # Följ

# Exec - kör kommando i container
docker exec -it container_name bash`
                },
                {
                    type: "quiz",
                    question: "Vad gör docker run -d?",
                    options: [
                        { text: "Raderar containern", correct: false, feedback: "Nej, -d = detached" },
                        { text: "Kör i bakgrunden (detached)", correct: true, feedback: "Rätt! Detached mode" },
                        { text: "Debug mode", correct: false, feedback: "Nej, finns inte" },
                        { text: "Duplicerar containern", correct: false, feedback: "Nej, fel" }
                    ],
                    hint: "d = detached = bakgrund"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Docker Grunder! 🐳"
                }
            ]
        },
        {
            id: "doe25-3-2-docker-images",
            title: "3.2 Docker Images",
            description: "Bygga och hantera Docker images med Dockerfile",
            order_index: 23,
            estimated_minutes: 50,
            content_blocks: [
                {
                    type: "intro",
                    headline: "📦 Docker Images",
                    learning_objectives: [
                        "Dockerfile syntax",
                        "Bygga images",
                        "Lager och caching",
                        "Registry och push/pull"
                    ]
                },
                {
                    type: "concept",
                    title: "Dockerfile instruktioner",
                    explanation: `┌─────────────┬───────────────────────────────────────────────┐
│ Instruktion │ Beskrivning                                   │
├─────────────┼───────────────────────────────────────────────┤
│ FROM        │ Basimage                                      │
│ RUN         │ Kör kommando vid build                        │
│ COPY        │ Kopiera filer från host                       │
│ ADD         │ Som COPY + URL + tar-extraktion               │
│ WORKDIR     │ Sätt arbetskatalog                            │
│ ENV         │ Miljövariabel                                 │
│ EXPOSE      │ Dokumentera port                              │
│ CMD         │ Default kommando vid run                      │
│ ENTRYPOINT  │ Huvudkommando (CMD blir argument)             │
└─────────────┴───────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Exempel Dockerfile",
                    language: "dockerfile",
                    code: `# Node.js app
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]

# Python app
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]`
                },
                {
                    type: "code",
                    title: "Bygga och hantera images",
                    language: "bash",
                    code: `# Bygg image
docker build -t myapp .
docker build -t myapp:1.0 .
docker build -f Dockerfile.prod -t myapp:prod .

# Lista images
docker images
docker image ls

# Ta bort
docker rmi myapp
docker image prune           # Ta bort oanvända

# Push till registry
docker tag myapp:1.0 username/myapp:1.0
docker push username/myapp:1.0
docker pull username/myapp:1.0`
                },
                {
                    type: "quiz",
                    question: "Vilken instruktion sätter default-kommandot?",
                    options: [
                        { text: "RUN", correct: false, feedback: "Nej, RUN kör vid build" },
                        { text: "CMD", correct: true, feedback: "Rätt! CMD är default vid run" },
                        { text: "EXEC", correct: false, feedback: "Nej, finns inte" },
                        { text: "START", correct: false, feedback: "Nej, finns inte" }
                    ],
                    hint: "CMD = command"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Docker Images! 📦"
                }
            ]
        },
        {
            id: "doe25-3-3-docker-compose",
            title: "3.3 Docker Compose",
            description: "Multi-container applikationer med docker-compose",
            order_index: 24,
            estimated_minutes: 50,
            content_blocks: [
                {
                    type: "intro",
                    headline: "🎼 Docker Compose",
                    learning_objectives: [
                        "docker-compose.yml syntax",
                        "Services, networks, volumes",
                        "Compose kommandon",
                        "Miljövariabler och overrides"
                    ]
                },
                {
                    type: "code",
                    title: "docker-compose.yml exempel",
                    language: "yaml",
                    code: `version: '3.8'

services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://db:5432/app
    depends_on:
      - db
    volumes:
      - ./src:/app/src

  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=secret
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:`
                },
                {
                    type: "code",
                    title: "docker-compose kommandon",
                    language: "bash",
                    code: `# Starta alla tjänster
docker-compose up
docker-compose up -d            # Detached
docker-compose up --build       # Bygg om images

# Stoppa
docker-compose down
docker-compose down -v          # Ta bort volymer också

# Status
docker-compose ps
docker-compose logs
docker-compose logs -f web      # Följ specifik tjänst

# Skala
docker-compose up -d --scale web=3

# Exec
docker-compose exec web bash`
                },
                {
                    type: "concept",
                    title: "Avancerade features",
                    explanation: `┌─────────────────────────────────────────────────────────────┐
│  depends_on    - Startordning                               │
│  networks      - Isolera tjänster                           │
│  volumes       - Persistens och delning                     │
│  healthcheck   - Kontrollera tjänstehälsa                   │
│  restart       - always/unless-stopped/on-failure           │
│  profiles      - Gruppera tjänster                          │
└─────────────────────────────────────────────────────────────┘`
                },
                {
                    type: "code",
                    title: "Med .env fil",
                    language: "bash",
                    code: `# .env
POSTGRES_PASSWORD=supersecret
APP_PORT=3000

# docker-compose.yml använder automatiskt
services:
  web:
    ports:
      - "\${APP_PORT}:3000"
  db:
    environment:
      - POSTGRES_PASSWORD=\${POSTGRES_PASSWORD}`
                },
                {
                    type: "quiz",
                    question: "Hur startar du compose i bakgrunden?",
                    options: [
                        { text: "docker-compose start", correct: false, feedback: "Nej, start är för stoppade containers" },
                        { text: "docker-compose up -d", correct: true, feedback: "Rätt! -d = detached" },
                        { text: "docker-compose run", correct: false, feedback: "Nej, run kör engångskommando" },
                        { text: "docker-compose background", correct: false, feedback: "Nej, finns inte" }
                    ],
                    hint: "-d fungerar som i docker run"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Docker Compose! 🎼"
                }
            ]
        },
        {
            id: "doe25-3-4-git",
            title: "3.4 Git Versionshantering",
            description: "Git workflow och kommandon för DevOps",
            order_index: 25,
            estimated_minutes: 55,
            content_blocks: [
                {
                    type: "intro",
                    headline: "📚 Git Versionshantering",
                    learning_objectives: [
                        "Git grundkommandon",
                        "Branching och merging",
                        "Remote repositories",
                        "Git workflow"
                    ]
                },
                {
                    type: "code",
                    title: "Git grunderna",
                    language: "bash",
                    code: `# Konfigurera
git config --global user.name "Ditt Namn"
git config --global user.email "din@email.com"

# Initiera/klona
git init
git clone https://github.com/user/repo.git

# Status och diff
git status
git diff
git diff --staged

# Stage och commit
git add file.txt
git add .
git commit -m "Beskrivning"
git commit -am "Stage och commit"`
                },
                {
                    type: "code",
                    title: "Branching",
                    language: "bash",
                    code: `# Lista branches
git branch
git branch -a                    # Inkl. remote

# Skapa och byta
git branch feature-x
git checkout feature-x
git checkout -b feature-y        # Skapa + byta
git switch -c feature-z          # Nyare syntax

# Merge
git checkout main
git merge feature-x

# Ta bort branch
git branch -d feature-x
git branch -D feature-x          # Force`
                },
                {
                    type: "code",
                    title: "Remote och sync",
                    language: "bash",
                    code: `# Remote
git remote add origin git@github.com:user/repo.git
git remote -v

# Push/Pull
git push origin main
git push -u origin main          # Sätt upstream
git pull origin main
git fetch origin

# Hantera konflikter
git merge feature
# (fixa konflikter i filer)
git add .
git commit -m "Resolve conflicts"`
                },
                {
                    type: "concept",
                    title: "Git workflow",
                    explanation: `┌─────────────────────────────────────────────────────────────┐
│  WORKING DIR  →  STAGING  →  LOCAL REPO  →  REMOTE         │
│       │             │            │              │           │
│    git add       git commit   git push                      │
│       ←             ←            ←                          │
│    git checkout  git reset   git pull/fetch                 │
└─────────────────────────────────────────────────────────────┘

Feature Branch Workflow:
1. git checkout -b feature-x
2. (gör ändringar, commit)
3. git push origin feature-x
4. (skapa Pull Request)
5. (code review)
6. git merge till main`
                },
                {
                    type: "code",
                    title: "Användbart",
                    language: "bash",
                    code: `# Ångra
git checkout -- file.txt         # Kasta ändringar
git reset HEAD file.txt          # Unstage
git reset --hard HEAD~1          # Ta bort senaste commit

# Stash
git stash
git stash pop
git stash list

# Log
git log --oneline
git log --graph --oneline --all
git blame file.txt`
                },
                {
                    type: "quiz",
                    question: "Hur skapar du en ny branch och byter till den?",
                    options: [
                        { text: "git branch new && git checkout new", correct: false, feedback: "Fungerar men finns kortare" },
                        { text: "git checkout -b new", correct: true, feedback: "Rätt! -b skapar och byter" },
                        { text: "git new-branch", correct: false, feedback: "Nej, finns inte" },
                        { text: "git create new", correct: false, feedback: "Nej, finns inte" }
                    ],
                    hint: "-b = branch"
                },
                {
                    type: "checkpoint",
                    message: "Du har klarat Git! 📚 MODUL 3 KLAR! 🎉 ALLA 25 TASKS AVKLARADE!"
                }
            ]
        }
    ]
};

// Export individual tasks for easy access
export const DOE25_TASKS = DOE25_MODULE.tasks;

// Slug to ID mapping (backend slugs -> frontend IDs)
const SLUG_TO_ID: Record<string, string> = {
    "subnetting-natverk": "doe25-0-1-subnetting",
    "filsystem-navigation": "doe25-0-2-filesystem",
    "anvandare-grupper": "doe25-1-1-users-groups",
    "filratigheter": "doe25-1-2-permissions",
    "ssh-hardening": "doe25-1-3-ssh-hardening",
    "ufw-brandvagg": "doe25-1-4-ufw",
    "firewalld": "doe25-1-5-firewalld",
    "lagring-lvm": "doe25-1-6-storage",
    "backup-tar": "doe25-1-7-backup",
    "systemd-services": "doe25-1-8-systemd",
    "bash-grunder": "doe25-2-1-bash-basics",
    "variabler-input": "doe25-2-2-variables",
    "kontrollstrukturer": "doe25-2-3-control",
    "funktioner-felhantering": "doe25-2-4-functions",
    "textbearbetning": "doe25-2-5-text-processing",
    "automation-cron": "doe25-2-6-automation",
    "docker-grunder": "doe25-3-1-docker-basics",
    "docker-images": "doe25-3-2-docker-images",
    "docker-compose": "doe25-3-3-docker-compose",
    "git-basics": "doe25-3-4-git-basics",
};

// Get task by ID or slug
export const getTaskById = (idOrSlug: string) => {
    // First try direct ID match
    let task = DOE25_TASKS.find(t => t.id === idOrSlug);
    if (task) return task;
    
    // Try slug lookup
    const mappedId = SLUG_TO_ID[idOrSlug];
    if (mappedId) {
        return DOE25_TASKS.find(t => t.id === mappedId);
    }
    
    return undefined;
};

// Get task by order index
export const getTaskByOrder = (order: number) => DOE25_TASKS.find(t => t.order_index === order);
