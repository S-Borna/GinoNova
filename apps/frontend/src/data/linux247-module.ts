/**
 * Linux 24/7 Module - Premium Learning Content
 * 20 tasks from basics to advanced Linux system administration
 */

export interface ContentBlock {
    type: 'intro' | 'concept' | 'code' | 'quiz' | 'checkpoint' | 'tip' | 'warning' | 'common_mistake' | 'mnemonic' | 'cheat_sheet'
    title?: string
    content?: string
    code?: string
    language?: string
    question?: string
    options?: string[]
    correctIndex?: number
    explanation?: string
    objectives?: string[]
    diagram?: string
    // New pedagogical fields
    wrong?: string
    right?: string
    concept?: string
    trick?: string
    example?: string
    commands?: { cmd: string; desc: string }[]
}

export interface Linux247Task {
    id: string
    order: number
    title: string
    slug: string
    description: string
    difficulty: 'easy' | 'medium' | 'hard'
    estimatedMinutes: number
    xpReward: number
    category: string
    icon: string
    content_blocks: ContentBlock[]
}

export interface Linux247Module {
    id: string
    slug: string
    title: string
    description: string
    icon: string
    totalTasks: number
    estimatedHours: number
    tasks: Linux247Task[]
}

export const LINUX247_MODULE: Linux247Module = {
    id: 'linux-247',
    slug: 'linux-247',
    title: 'Linux 24/7',
    description: 'Komplett Linux för DevOps - från grunden till produktion',
    icon: 'terminal',
    totalTasks: 20,
    estimatedHours: 40,
    tasks: [
        // ========================================================================
        // TASK 1: File System Essentials
        // ========================================================================
        {
            id: 'linux247-1-filesystem',
            order: 1,
            title: 'File System Essentials',
            slug: 'file-system-essentials',
            description: 'Navigera, kopiera, flytta och hantera filer i Linux',
            difficulty: 'easy',
            estimatedMinutes: 45,
            xpReward: 100,
            category: 'Grundläggande',
            icon: '📁',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Navigera i filsystemet med cd, pwd och ls',
                        'Kopiera och flytta filer med cp och mv',
                        'Ta bort filer säkert med rm',
                        'Hitta filer med find och which',
                        'Förstå Linux filsystemets struktur'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Varför viktigt för DevOps?',
                    content: 'Som DevOps-ingenjör arbetar du konstant med filer. Konfigurationsfiler i /etc, loggar i /var/log, scripts i /opt eller /home, och applikationer i /var/www. Dessa kommandon använder du flera gånger per dag.',
                    diagram: 'file-tree'
                },
                {
                    type: 'concept',
                    title: 'Navigation - De viktiga kommandona',
                    content: '**cd** (change directory) - Byt katalog\n**pwd** (print working directory) - Visa var du är\n**ls** (list) - Lista innehåll'
                },
                {
                    type: 'code',
                    title: 'cd - Byt katalog',
                    language: 'bash',
                    code: `# Gå till specifik katalog
cd /var/log

# Gå upp en nivå
cd ..

# Gå till hemkatalogen
cd ~

# ⭐ PRO-TIPS: Tillbaka till förra katalogen
cd -`
                },
                {
                    type: 'code',
                    title: 'ls - Lista filer (MEMORERA DETTA!)',
                    language: 'bash',
                    code: `# Enkel lista
ls

# Lång lista med detaljer
ls -l

# Inkludera dolda filer
ls -la

# ⭐ FAVORITEN - Human-readable med allt
ls -lah

# Sorterat efter tid (nyaste först)
ls -lht`
                },
                {
                    type: 'quiz',
                    question: 'Vilket kommando visar ALLA filer (inkl. dolda) med human-readable storlekar?',
                    options: ['ls -l', 'ls -la', 'ls -lah', 'ls -h'],
                    correctIndex: 2,
                    explanation: 'ls -lah kombinerar: -l (lång lista), -a (alla filer inkl. dolda), -h (human-readable storlekar som KB, MB, GB)'
                },
                {
                    type: 'concept',
                    title: 'Filoperationer',
                    content: '**cp** (copy) - Kopiera filer\n**mv** (move) - Flytta eller byt namn\n**rm** (remove) - Ta bort filer\n**mkdir** (make directory) - Skapa kataloger'
                },
                {
                    type: 'code',
                    title: 'cp - Kopiera filer',
                    language: 'bash',
                    code: `# Kopiera fil
cp fil.txt kopia.txt

# ⭐ VIKTIGT: -r för kataloger (rekursivt)
cp -r katalog/ backup/

# DevOps-mönster: Backup innan ändring
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak.$(date +%Y%m%d)`
                },
                {
                    type: 'code',
                    title: 'rm - Ta bort (FÖRSIKTIGT!)',
                    language: 'bash',
                    code: `# Ta bort fil
rm fil.txt

# Ta bort katalog rekursivt
rm -r katalog/

# ⚠️ FARLIGT - Force delete (dubbelkolla!)
rm -rf katalog/

# Säkrare: Interaktiv (frågar först)
rm -i fil.txt`
                },
                {
                    type: 'warning',
                    title: 'VARNING: rm -rf',
                    content: 'rm -rf tar bort ALLT utan att fråga. Dubbelkolla ALLTID sökvägen innan du kör detta kommando. Ett misstag kan radera hela systemet!'
                },
                {
                    type: 'code',
                    title: 'find - Sök efter filer',
                    language: 'bash',
                    code: `# Hitta .log-filer
find /var/log -name "*.log"

# Hitta stora filer (>100MB)
find . -type f -size +100M

# Hitta nyligen ändrade filer (senaste 7 dagarna)
find /etc -mtime -7

# ⭐ PRO: Hitta och ta bort gamla temp-filer
find /tmp -type f -mtime +30 -delete`
                },
                {
                    type: 'quiz',
                    question: 'Du ska kopiera hela katalogen "projekt" till "backup". Vilket kommando är korrekt?',
                    options: ['cp projekt backup', 'cp -r projekt/ backup/', 'mv projekt backup', 'copy projekt backup'],
                    correctIndex: 1,
                    explanation: 'cp -r behövs för att kopiera kataloger rekursivt. Utan -r kopieras bara filer, inte underkataloger.'
                },
                {
                    type: 'tip',
                    title: 'DevOps Pro-Tips',
                    content: '1. Gör ALLTID backup innan du ändrar config-filer\n2. Använd ls -la innan rm för att verifiera\n3. Lär dig tab-completion - det sparar tid och förhindrar stavfel'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'rm -rf katalog (utan att verifiera först)',
                    right: 'ls katalog/ && rm -rf katalog',
                    explanation: 'Dubbelkolla ALLTID med ls innan rm -rf. Ett misstag kan radera allt!'
                },
                {
                    type: 'mnemonic',
                    title: '🧠 Minnesregel',
                    concept: 'Navigering',
                    trick: 'cd = Change Dir, pwd = Print Working Dir, ls = List',
                    example: 'cd ~ går hem, cd - går tillbaka, cd .. går upp'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Snabbkoll',
                    commands: [
                        { cmd: 'ls -lah', desc: 'Lista allt, human-readable' },
                        { cmd: 'cp -r katalog/', desc: 'Kopiera rekursivt' },
                        { cmd: 'rm -i fil', desc: 'Ta bort med bekräftelse' },
                        { cmd: 'find . -name "*.log"', desc: 'Sök filer' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: File System Essentials',
                    content: 'Du kan nu navigera i Linux filsystemet, kopiera/flytta/ta bort filer, och hitta filer med find. Dessa kommandon är grunden för allt DevOps-arbete!'
                }
            ]
        },

        // ========================================================================
        // TASK 2: Text Processing & Search
        // ========================================================================
        {
            id: 'linux247-2-text',
            order: 2,
            title: 'Text Processing & Search',
            slug: 'text-processing',
            description: 'Visa, sök och manipulera textfiler effektivt',
            difficulty: 'easy',
            estimatedMinutes: 50,
            xpReward: 120,
            category: 'Grundläggande',
            icon: '📝',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Visa filinnehåll med cat, less och head/tail',
                        'Söka i filer med grep och dess flaggor',
                        'Kombinera kommandon med pipes (|)',
                        'Räkna rader/ord med wc',
                        'Sortera och filtrera data'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Varför texthantering är kritiskt',
                    content: 'I Linux är ALLT filer - konfiguration, loggar, data. Som DevOps läser du loggar, söker efter fel, och filtrerar data dagligen. Att behärska grep och pipes gör dig 10x snabbare.',
                    diagram: 'pipe-flow'
                },
                {
                    type: 'code',
                    title: 'Visa filer - cat, less, head, tail',
                    language: 'bash',
                    code: `# Visa hela filen
cat fil.txt

# Visa med radnummer
cat -n fil.txt

# ⭐ less - Bläddra i stora filer (q för avsluta)
less /var/log/syslog

# Första 10 raderna
head fil.txt
head -20 fil.txt    # Första 20

# Sista 10 raderna
tail fil.txt

# ⭐ SUPERVIKTIGT: Följ logg i realtid
tail -f /var/log/nginx/access.log`
                },
                {
                    type: 'quiz',
                    question: 'Du vill se nya loggmeddelanden i realtid. Vilket kommando använder du?',
                    options: ['cat -f logfil', 'tail -f logfil', 'less -f logfil', 'watch logfil'],
                    correctIndex: 1,
                    explanation: 'tail -f "följer" filen och visar nya rader när de läggs till. Perfekt för att övervaka loggar i realtid!'
                },
                {
                    type: 'concept',
                    title: 'grep - Din bästa vän',
                    content: 'grep (Global Regular Expression Print) söker efter mönster i filer. Det är det mest använda kommandot för att hitta information i loggar och konfigurationsfiler.'
                },
                {
                    type: 'code',
                    title: 'grep - Sök i filer',
                    language: 'bash',
                    code: `# Enkel sökning
grep "error" /var/log/syslog

# Case-insensitive (-i)
grep -i "ERROR" logfil.txt

# Visa radnummer (-n)
grep -n "failed" /var/log/auth.log

# Rekursiv sökning i alla filer (-r)
grep -r "password" /etc/

# ⭐ KOMBINERA FLAGGOR
grep -rni "connection refused" /var/log/

# Invertera - visa rader som INTE matchar (-v)
grep -v "^#" /etc/ssh/sshd_config  # Ignorera kommentarer`
                },
                {
                    type: 'code',
                    title: 'Pipes - Kombinera kommandon',
                    language: 'bash',
                    code: `# Sök i output från annat kommando
cat /var/log/syslog | grep "error"

# Räkna antal fel
grep "error" /var/log/syslog | wc -l

# ⭐ PRAKTISKT: Hitta de 10 vanligaste felen
grep "error" /var/log/syslog | sort | uniq -c | sort -rn | head -10

# Filtrera och visa specifika kolumner
ps aux | grep nginx | awk '{print $2, $11}'`
                },
                {
                    type: 'quiz',
                    question: 'Vad gör kommandot: grep -rni "error" /var/log/',
                    options: [
                        'Söker "error" endast i en fil',
                        'Söker rekursivt, case-insensitive, med radnummer',
                        'Tar bort rader med "error"',
                        'Räknar antal "error"'
                    ],
                    correctIndex: 1,
                    explanation: '-r = rekursivt (alla filer), -n = visa radnummer, -i = case-insensitive. Perfekt för att hitta fel i loggar!'
                },
                {
                    type: 'code',
                    title: 'wc, sort, uniq - Analysera data',
                    language: 'bash',
                    code: `# Räkna rader, ord, tecken
wc fil.txt
wc -l fil.txt      # Endast rader

# Sortera
sort fil.txt
sort -n numbers.txt    # Numerisk sortering
sort -r fil.txt        # Omvänd ordning

# Unika rader (kräver sorterad input!)
sort fil.txt | uniq
sort fil.txt | uniq -c   # Med antal`
                },
                {
                    type: 'tip',
                    title: 'DevOps Pro-Tips: Log Analysis',
                    content: '**Snabb felanalys:**\n```bash\ngrep -i error /var/log/syslog | tail -50\n```\n\n**Räkna unika IP-adresser:**\n```bash\nawk \'{print $1}\' access.log | sort | uniq -c | sort -rn | head\n```'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'grep "error" fil (missar ERROR, Error, etc.)',
                    right: 'grep -i "error" fil (-i = case insensitive)',
                    explanation: 'Loggmeddelanden kan ha olika case. Använd alltid -i för säkrare sökning.'
                },
                {
                    type: 'mnemonic',
                    title: '🧠 Minnesregel',
                    concept: 'grep-flaggor',
                    trick: '-i = Ignore case, -r = Recursive, -n = Number, -v = inVert',
                    example: 'grep -rni "error" /var/log/ = sök rekursivt, case-insensitive, med radnummer'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Snabbkoll',
                    commands: [
                        { cmd: 'tail -f logfil', desc: 'Följ logg live' },
                        { cmd: 'grep -rni "text" .', desc: 'Sök rekursivt' },
                        { cmd: 'cat fil | sort | uniq', desc: 'Unika rader' },
                        { cmd: 'wc -l fil', desc: 'Räkna rader' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Text Processing',
                    content: 'Du behärskar nu grunderna i texthantering! grep, pipes, och tail -f är dina nya bästa vänner för att analysera loggar och hitta problem snabbt.'
                }
            ]
        },

        // ========================================================================
        // TASK 3: Process Management
        // ========================================================================
        {
            id: 'linux247-3-processes',
            order: 3,
            title: 'Process Management',
            slug: 'process-management',
            description: 'Hantera processer, övervaka systemet och felsök',
            difficulty: 'easy',
            estimatedMinutes: 45,
            xpReward: 110,
            category: 'Grundläggande',
            icon: '⚙️',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Lista processer med ps och top/htop',
                        'Avsluta processer med kill och pkill',
                        'Köra processer i bakgrunden',
                        'Förstå process-states och PID',
                        'Övervaka systemresurser'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Processer i Linux',
                    content: 'En process är ett körande program. Varje process har ett unikt Process ID (PID). Som DevOps måste du kunna hitta problematiska processer, avsluta dem, och övervaka resurser.',
                    diagram: 'process-tree'
                },
                {
                    type: 'code',
                    title: 'ps - Lista processer',
                    language: 'bash',
                    code: `# Visa dina processer
ps

# ⭐ VIKTIGAST: Alla processer med detaljer
ps aux

# Hitta specifik process
ps aux | grep nginx

# Trädvy (visa parent-child)
ps auxf

# Endast PID för en process
pgrep nginx`
                },
                {
                    type: 'quiz',
                    question: 'Du vill se alla körande processer på systemet. Vilket kommando?',
                    options: ['ps', 'ps -a', 'ps aux', 'ps --all'],
                    correctIndex: 2,
                    explanation: 'ps aux visar ALLA processer för ALLA användare med detaljerad info (CPU%, MEM%, kommando etc.)'
                },
                {
                    type: 'code',
                    title: 'top / htop - Realtidsövervakning',
                    language: 'bash',
                    code: `# Grundläggande övervakning
top

# ⭐ BÄTTRE: htop (installera med apt install htop)
htop

# Tangenter i top/htop:
# q = avsluta
# k = kill process
# M = sortera efter minne
# P = sortera efter CPU
# / = sök`
                },
                {
                    type: 'code',
                    title: 'kill - Avsluta processer',
                    language: 'bash',
                    code: `# Avsluta med PID (SIGTERM - snällt)
kill 1234

# Tvinga avslut (SIGKILL - hårt)
kill -9 1234

# ⭐ ENKLARE: Avsluta via namn
pkill nginx

# Avsluta ALLA med namn
killall nginx

# Skicka HUP-signal (reload config)
kill -HUP $(pgrep nginx)`
                },
                {
                    type: 'warning',
                    title: 'kill -9 vs kill',
                    content: 'kill (SIGTERM) ger processen chans att städa upp. kill -9 (SIGKILL) avslutar omedelbart utan cleanup. Använd -9 endast om vanlig kill inte fungerar!'
                },
                {
                    type: 'quiz',
                    question: 'Nginx svarar inte. Du vill avsluta och låta den städa upp. Vad kör du först?',
                    options: ['kill -9 $(pgrep nginx)', 'pkill nginx', 'killall -9 nginx', 'rm nginx'],
                    correctIndex: 1,
                    explanation: 'pkill nginx skickar SIGTERM vilket ger nginx chans att stänga connections och spara state innan den avslutas.'
                },
                {
                    type: 'code',
                    title: 'Bakgrundsprocesser',
                    language: 'bash',
                    code: `# Kör i bakgrunden med &
./long_script.sh &

# Se bakgrundsjobb
jobs

# Ta fram till förgrunden
fg %1

# Pausa körande process: Ctrl+Z
# Fortsätt i bakgrunden:
bg

# ⭐ Kör kommando som överlever logout
nohup ./script.sh &`
                },
                {
                    type: 'tip',
                    title: 'DevOps Pro-Tips',
                    content: '**Hitta vad som äter CPU:**\n```bash\nps aux --sort=-%cpu | head -10\n```\n\n**Hitta vad som äter RAM:**\n```bash\nps aux --sort=-%mem | head -10\n```'
                },
                {
                    type: 'checkpoint',
                    title: 'Checkpoint: Process Management',
                    content: 'Du kan nu övervaka systemet, hitta problematiska processer, och hantera dem effektivt. ps aux och htop är dina go-to verktyg!'
                }
            ]
        },

        // ========================================================================
        // TASK 4: System Information & Monitoring
        // ========================================================================
        {
            id: 'linux247-4-sysinfo',
            order: 4,
            title: 'System Information & Monitoring',
            slug: 'system-info',
            description: 'Samla systeminformation och övervaka prestanda',
            difficulty: 'easy',
            estimatedMinutes: 40,
            xpReward: 100,
            category: 'Grundläggande',
            icon: '📊',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Visa systeminfo med uname och hostnamectl',
                        'Kontrollera disk med df och du',
                        'Övervaka minne med free',
                        'Se nätverkskonfiguration',
                        'Förstå system-metrics'
                    ]
                },
                {
                    type: 'code',
                    title: 'Systeminformation',
                    language: 'bash',
                    code: `# Kernel och OS
uname -a

# ⭐ Detaljerad systeminfo
hostnamectl

# CPU-info
lscpu
cat /proc/cpuinfo | grep "model name" | head -1

# Minne
cat /proc/meminfo | head -5`
                },
                {
                    type: 'code',
                    title: 'df - Diskutrymme',
                    language: 'bash',
                    code: `# ⭐ Human-readable diskutrymme
df -h

# Endast lokala filsystem
df -h --local

# Specifik mount
df -h /var

# Visa filsystemtyp
df -Th`
                },
                {
                    type: 'quiz',
                    question: 'Disken är full. Vilket kommando ger snabbast överblick?',
                    options: ['du -sh /', 'df -h', 'ls -la /', 'free -h'],
                    correctIndex: 1,
                    explanation: 'df -h visar snabbt hur mycket utrymme som används på varje partition. du tar längre tid då det räknar allt.'
                },
                {
                    type: 'code',
                    title: 'du - Katalogstorlekar',
                    language: 'bash',
                    code: `# Storlek på katalog
du -sh /var/log

# Top 10 största kataloger
du -h /var | sort -rh | head -10

# ⭐ PRO: Hitta var disken fylls
du -h --max-depth=1 / 2>/dev/null | sort -rh | head -20`
                },
                {
                    type: 'code',
                    title: 'free - Minnesanvändning',
                    language: 'bash',
                    code: `# ⭐ Human-readable minne
free -h

# Output:
#               total   used   free   shared  buff/cache  available
# Mem:           16Gi   4.2Gi  8.1Gi   512Mi      3.7Gi      11Gi
# Swap:          2.0Gi  0B     2.0Gi

# OBS: "available" är det viktiga, inte "free"!`
                },
                {
                    type: 'concept',
                    title: 'Förstå free output',
                    content: '**total**: Totalt RAM\n**used**: Aktivt använt minne\n**free**: Helt oanvänt (oftast lågt)\n**buff/cache**: Minne för disk-cache\n**available**: ⭐ Det som faktiskt kan användas! Cache frigörs vid behov.'
                },
                {
                    type: 'code',
                    title: 'Nätverksinformation',
                    language: 'bash',
                    code: `# IP-adresser
ip a

# Äldre variant (fortfarande vanlig)
ifconfig

# Routing-tabell
ip route

# DNS-servers
cat /etc/resolv.conf

# ⭐ Lyssnade portar
ss -tuln
# eller
netstat -tuln`
                },
                {
                    type: 'quiz',
                    question: 'Du behöver se vilka portar som lyssnar på servern. Vad kör du?',
                    options: ['ps aux', 'netstat -tuln', 'df -h', 'free -h'],
                    correctIndex: 1,
                    explanation: 'netstat -tuln (eller ss -tuln) visar alla TCP/UDP-portar som lyssnar. -t=TCP, -u=UDP, -l=listening, -n=numeriskt'
                },
                {
                    type: 'tip',
                    title: 'One-liner Dashboard',
                    content: '```bash\necho "=== SYSTEM ===" && uname -n && echo "=== DISK ===" && df -h / && echo "=== MEM ===" && free -h && echo "=== LOAD ===" && uptime\n```'
                },
                {
                    type: 'checkpoint',
                    title: 'Checkpoint: System Monitoring',
                    content: 'Du kan nu snabbt diagnostisera ett system: kontrollera disk (df -h), minne (free -h), nätverk (ip a, ss -tuln), och systeminformation!'
                }
            ]
        },

        // ========================================================================
        // TASK 5: Log Management
        // ========================================================================
        {
            id: 'linux247-5-logs',
            order: 5,
            title: 'Log Management',
            slug: 'log-management',
            description: 'Förstå, läsa och analysera systemloggar',
            difficulty: 'easy',
            estimatedMinutes: 45,
            xpReward: 110,
            category: 'Grundläggande',
            icon: '📋',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Förstå Linux logg-struktur (/var/log)',
                        'Läsa journalctl för systemd-loggar',
                        'Analysera auth.log för säkerhet',
                        'Söka effektivt i loggar',
                        'Hantera loggrotation'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Linux Loggar',
                    content: 'Loggar är din bästa vän vid felsökning. Nästan alla Linux-system loggar till /var/log. Moderna system med systemd använder journalctl för centraliserad logging.',
                    diagram: 'log-flow'
                },
                {
                    type: 'code',
                    title: 'Viktiga loggfiler',
                    language: 'bash',
                    code: `# Systemloggar
/var/log/syslog        # Generella systemloggar (Debian/Ubuntu)
/var/log/messages      # Generella systemloggar (RHEL/CentOS)

# Säkerhet & autentisering
/var/log/auth.log      # SSH-logins, sudo, etc.

# Applikationer
/var/log/nginx/        # Nginx access + error logs
/var/log/apache2/      # Apache logs
/var/log/mysql/        # MySQL logs

# Boot & kernel
/var/log/kern.log      # Kernel messages
/var/log/dmesg         # Boot messages`
                },
                {
                    type: 'code',
                    title: 'journalctl - Systemd-loggar',
                    language: 'bash',
                    code: `# Alla loggar
journalctl

# ⭐ Följ i realtid
journalctl -f

# Loggar för specifik service
journalctl -u nginx
journalctl -u ssh

# Endast fel
journalctl -p err

# Sedan boot
journalctl -b

# Senaste timmen
journalctl --since "1 hour ago"

# Kombinera!
journalctl -u nginx --since "1 hour ago" -p err`
                },
                {
                    type: 'quiz',
                    question: 'Du vill se nginx-fel i realtid. Vilket kommando?',
                    options: [
                        'tail -f /var/log/nginx/error.log',
                        'journalctl -u nginx -f',
                        'Båda fungerar!',
                        'cat /var/log/nginx/error.log'
                    ],
                    correctIndex: 2,
                    explanation: 'Både tail -f och journalctl -f fungerar! tail -f är för filer, journalctl -f för systemd-services.'
                },
                {
                    type: 'code',
                    title: 'Praktisk logganalys',
                    language: 'bash',
                    code: `# Senaste SSH-inloggningar
grep "Accepted" /var/log/auth.log | tail -20

# Misslyckade inloggningsförsök
grep "Failed password" /var/log/auth.log

# ⭐ Top 10 IP-adresser som försökt logga in
grep "Failed password" /var/log/auth.log | \\
  awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head -10

# Räkna 404-fel i nginx
grep " 404 " /var/log/nginx/access.log | wc -l`
                },
                {
                    type: 'code',
                    title: 'Loggrotation',
                    language: 'bash',
                    code: `# Logrotate konfiguration
cat /etc/logrotate.conf
ls /etc/logrotate.d/

# Exempel: nginx logrotation
cat /etc/logrotate.d/nginx

# Manuell rotation (testa config)
logrotate -d /etc/logrotate.conf

# Tvinga rotation
logrotate -f /etc/logrotate.conf`
                },
                {
                    type: 'tip',
                    title: 'Quick Troubleshooting Cheat Sheet',
                    content: '**Service startar inte:**\n```bash\njournalctl -u servicename -n 50 --no-pager\n```\n\n**Senaste systemfel:**\n```bash\njournalctl -p err --since "10 min ago"\n```\n\n**Disk full? Hitta stora loggar:**\n```bash\ndu -sh /var/log/* | sort -rh | head -10\n```'
                },
                {
                    type: 'checkpoint',
                    title: 'Checkpoint: Log Management',
                    content: 'Du kan nu navigera Linux loggsystemet, använda journalctl effektivt, och analysera loggar för felsökning. Detta är en av de viktigaste DevOps-skills!'
                }
            ]
        },

        // ========================================================================
        // TASK 6-20: Placeholder - will be added in next parts
        // ========================================================================
        {
            id: 'linux247-6-ssh',
            order: 6,
            title: 'SSH & Remote Access',
            slug: 'ssh-remote-access',
            description: 'Säker fjärråtkomst och SSH-nyckelhantering',
            difficulty: 'medium',
            estimatedMinutes: 50,
            xpReward: 130,
            category: 'Nätverk',
            icon: '🔐',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Ansluta till servrar med SSH',
                        'Skapa och hantera SSH-nycklar',
                        'Konfigurera SSH-klient (~/.ssh/config)',
                        'Förstå SSH-säkerhet',
                        'Använda SCP och rsync för filöverföring'
                    ]
                },
                {
                    type: 'concept',
                    title: 'SSH - Secure Shell',
                    content: 'SSH är standarden för säker fjärråtkomst till Linux-servrar. Istället för lösenord använder proffs SSH-nycklar för autentisering - säkrare och bekvämare.',
                    diagram: 'ssh-flow'
                },
                {
                    type: 'code',
                    title: 'Grundläggande SSH',
                    language: 'bash',
                    code: `# Anslut till server
ssh user@server.com

# Specifik port
ssh -p 2222 user@server.com

# Kör kommando direkt
ssh user@server "uptime && df -h"`
                },
                {
                    type: 'code',
                    title: 'SSH-nycklar (VIKTIGT!)',
                    language: 'bash',
                    code: `# ⭐ Skapa SSH-nyckelpar
ssh-keygen -t ed25519 -C "din.email@example.com"

# Kopiera publik nyckel till server
ssh-copy-id user@server.com

# Eller manuellt:
cat ~/.ssh/id_ed25519.pub | ssh user@server "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"`
                },
                {
                    type: 'quiz',
                    question: 'Vilken fil innehåller din PRIVATA SSH-nyckel som ALDRIG ska delas?',
                    options: ['~/.ssh/id_ed25519.pub', '~/.ssh/id_ed25519', '~/.ssh/authorized_keys', '~/.ssh/known_hosts'],
                    correctIndex: 1,
                    explanation: 'id_ed25519 (utan .pub) är din privata nyckel. Den publika (.pub) kopieras till servrar, men den privata stannar på din maskin!'
                },
                {
                    type: 'code',
                    title: 'SSH Config - Gör livet enklare',
                    language: 'bash',
                    code: `# ~/.ssh/config
Host prod
    HostName prod.example.com
    User deploy
    Port 22
    IdentityFile ~/.ssh/prod_key

Host staging
    HostName staging.example.com
    User deploy
    Port 2222

# Nu kan du köra:
ssh prod
ssh staging`
                },
                {
                    type: 'code',
                    title: 'Filöverföring - SCP & rsync',
                    language: 'bash',
                    code: `# SCP - Kopiera filer
scp fil.txt user@server:/path/
scp -r katalog/ user@server:/path/

# ⭐ rsync - Smartare synkronisering
rsync -avz katalog/ user@server:/path/
# -a = archive (behåll permissions)
# -v = verbose
# -z = compress

# Synka och ta bort borttagna filer
rsync -avz --delete src/ user@server:/dest/`
                },
                {
                    type: 'checkpoint',
                    title: 'Checkpoint: SSH & Remote Access',
                    content: 'Du kan nu ansluta säkert till servrar, skapa SSH-nycklar, och överföra filer. SSH-config gör ditt liv mycket enklare!'
                }
            ]
        },

        {
            id: 'linux247-7-firewall',
            order: 7,
            title: 'Firewall Essentials',
            slug: 'firewall-essentials',
            description: 'Konfigurera brandvägg med ufw och iptables',
            difficulty: 'medium',
            estimatedMinutes: 45,
            xpReward: 120,
            category: 'Säkerhet',
            icon: '🛡️',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Förstå varför brandväggar är kritiska',
                        'Konfigurera ufw (Uncomplicated Firewall)',
                        'Öppna och stänga portar säkert',
                        'Skapa regler för specifika IP-adresser',
                        'Grundläggande iptables-förståelse'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Varför brandvägg?',
                    content: 'En brandvägg är din första försvarslinje. Den kontrollerar vilken trafik som får komma in och ut. Utan brandvägg är alla portar öppna för attacker. Som DevOps måste du kunna öppna rätt portar (HTTP/HTTPS/SSH) och blockera allt annat.'
                },
                {
                    type: 'code',
                    title: 'ufw - Enkel brandvägg',
                    language: 'bash',
                    code: `# Kontrollera status
ufw status
ufw status verbose

# ⭐ Aktivera brandväggen
sudo ufw enable

# Inaktivera (försiktigt!)
sudo ufw disable

# Återställ till default
sudo ufw reset`
                },
                {
                    type: 'warning',
                    title: 'VARNING: SSH-regeln först!',
                    content: 'Om du aktiverar ufw utan att först tillåta SSH (port 22) kan du LÅSA UTE DIG SJÄLV från servern! Alltid: sudo ufw allow ssh INNAN ufw enable'
                },
                {
                    type: 'code',
                    title: 'Öppna portar',
                    language: 'bash',
                    code: `# ⭐ VIKTIGT: Tillåt SSH först!
sudo ufw allow ssh
# eller
sudo ufw allow 22

# Tillåt HTTP och HTTPS
sudo ufw allow 80
sudo ufw allow 443
# eller enklare:
sudo ufw allow http
sudo ufw allow https

# Tillåt specifik port
sudo ufw allow 3000

# Tillåt port-range
sudo ufw allow 8000:8010/tcp`
                },
                {
                    type: 'quiz',
                    question: 'Du ska aktivera ufw på en fjärrserver. Vad gör du FÖRST?',
                    options: ['sudo ufw enable', 'sudo ufw allow ssh', 'sudo ufw deny all', 'sudo ufw reset'],
                    correctIndex: 1,
                    explanation: 'ALLTID tillåt SSH först! Om du kör "ufw enable" utan SSH-regel låser du ut dig själv från servern.'
                },
                {
                    type: 'code',
                    title: 'Blockera och ta bort regler',
                    language: 'bash',
                    code: `# Blockera port
sudo ufw deny 23

# Ta bort regel
sudo ufw delete allow 80

# Visa numrerade regler
sudo ufw status numbered

# Ta bort regel via nummer
sudo ufw delete 3`
                },
                {
                    type: 'code',
                    title: 'Avancerade regler',
                    language: 'bash',
                    code: `# Tillåt från specifik IP
sudo ufw allow from 192.168.1.100

# Tillåt från IP till specifik port
sudo ufw allow from 10.0.0.0/24 to any port 22

# Tillåt från subnät
sudo ufw allow from 192.168.1.0/24

# ⭐ PRAKTISKT: Endast SSH från kontoret
sudo ufw allow from 203.0.113.0/24 to any port 22`
                },
                {
                    type: 'quiz',
                    question: 'Hur tillåter du SSH endast från IP 10.0.0.5?',
                    options: [
                        'ufw allow ssh from 10.0.0.5',
                        'ufw allow from 10.0.0.5 to any port 22',
                        'ufw allow 22 from 10.0.0.5',
                        'ufw allow 10.0.0.5:22'
                    ],
                    correctIndex: 1,
                    explanation: 'Syntaxen är "from [IP] to any port [PORT]". Detta begränsar SSH till endast den specifika IP-adressen.'
                },
                {
                    type: 'code',
                    title: 'Default policies',
                    language: 'bash',
                    code: `# Se default policies
sudo ufw status verbose

# ⭐ Rekommenderad setup för server:
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Sedan öppna det du behöver:
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https`
                },
                {
                    type: 'tip',
                    title: 'DevOps Best Practice',
                    content: '**Minimal-access-principen:**\n1. Blockera allt inkommande som default\n2. Öppna ENDAST de portar som behövs\n3. Begränsa SSH till specifika IP-adresser om möjligt\n4. Dokumentera varje öppen port och varför'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'sudo ufw enable (utan att först tillåta SSH)',
                    right: 'sudo ufw allow ssh && sudo ufw enable',
                    explanation: 'Aktivera ALDRIG brandväggen utan att först säkerställa att du kan logga in!'
                },
                {
                    type: 'mnemonic',
                    title: '🧠 Minnesregel',
                    concept: 'ufw-ordning',
                    trick: 'SSH → Enable → HTTP → HTTPS (SEHH)',
                    example: 'Först SSH (22), sedan enable, sedan webbtrafik'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 ufw Snabbkoll',
                    commands: [
                        { cmd: 'ufw allow ssh', desc: 'Tillåt SSH (port 22)' },
                        { cmd: 'ufw allow 80,443/tcp', desc: 'Tillåt HTTP+HTTPS' },
                        { cmd: 'ufw status numbered', desc: 'Visa regler med nummer' },
                        { cmd: 'ufw delete 3', desc: 'Ta bort regel #3' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Firewall Essentials',
                    content: 'Du kan nu säkra servrar med ufw! Kom ihåg: SSH först, sedan enable, och öppna bara det som behövs.'
                }
            ]
        },

        {
            id: 'linux247-8-network',
            order: 8,
            title: 'Network Basics',
            slug: 'network-basics',
            description: 'Nätverkskonfiguration och felsökning',
            difficulty: 'medium',
            estimatedMinutes: 50,
            xpReward: 130,
            category: 'Nätverk',
            icon: '🌐',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Visa nätverkskonfiguration med ip och ifconfig',
                        'Felsöka nätverk med ping, traceroute, dig',
                        'Förstå DNS-uppslagning',
                        'Använda curl och wget för HTTP-tester',
                        'Diagnostisera nätverksproblem systematiskt'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Nätverksdiagnostik i DevOps',
                    content: 'När en service inte svarar är nätverket ofta boven. Kan du pinga servern? Är DNS rätt? Är porten öppen? Dessa verktyg hjälper dig hitta problemet snabbt.'
                },
                {
                    type: 'code',
                    title: 'ip - Modern nätverksinfo',
                    language: 'bash',
                    code: `# ⭐ Visa alla interface och IP-adresser
ip a
ip addr show

# Visa specifikt interface
ip a show eth0

# Visa routing-tabell
ip route
ip r

# Visa endast IPv4
ip -4 a`
                },
                {
                    type: 'code',
                    title: 'ping - Testa anslutning',
                    language: 'bash',
                    code: `# Pinga server (Ctrl+C för att stoppa)
ping google.com

# Pinga med begränsat antal
ping -c 4 google.com

# Pinga med intervall (snabbare)
ping -i 0.5 -c 10 server.com

# ⭐ PRO: Testa om server svarar
ping -c 1 -W 2 server.com && echo "UP" || echo "DOWN"`
                },
                {
                    type: 'quiz',
                    question: 'Du kan inte nå en webbserver. Vad testar du FÖRST?',
                    options: ['curl http://server', 'ping server', 'dig server', 'traceroute server'],
                    correctIndex: 1,
                    explanation: 'Börja med ping för att se om servern överhuvudtaget är nåbar. Om ping fungerar men inte HTTP, är problemet tjänsten, inte nätverket.'
                },
                {
                    type: 'code',
                    title: 'traceroute - Spåra vägen',
                    language: 'bash',
                    code: `# Visa vägen till destination
traceroute google.com

# Snabbare (färre försök)
traceroute -q 1 google.com

# Med IP (skippa DNS)
traceroute -n google.com

# ⭐ Windows-variant: tracert
# Linux: mtr för interaktiv traceroute
mtr google.com`
                },
                {
                    type: 'code',
                    title: 'DNS - dig och nslookup',
                    language: 'bash',
                    code: `# ⭐ dig - Detaljerad DNS-info
dig example.com

# Endast svaret
dig +short example.com

# Specifik DNS-server
dig @8.8.8.8 example.com

# Olika record-typer
dig example.com MX      # Mail servers
dig example.com NS      # Nameservers
dig example.com TXT     # TXT records

# nslookup (äldre, men fortfarande vanlig)
nslookup example.com`
                },
                {
                    type: 'quiz',
                    question: 'DNS ger fel IP. Hur testar du med Googles DNS istället?',
                    options: ['dig google example.com', 'dig @8.8.8.8 example.com', 'nslookup -google example.com', 'dns 8.8.8.8 example.com'],
                    correctIndex: 1,
                    explanation: 'dig @[dns-server] domain - @ anger vilken DNS-server som ska användas. 8.8.8.8 är Googles publika DNS.'
                },
                {
                    type: 'code',
                    title: 'curl - HTTP-tester',
                    language: 'bash',
                    code: `# Hämta webbsida
curl http://example.com

# ⭐ Visa headers + body
curl -i http://example.com

# Endast headers
curl -I http://example.com

# Följ redirects
curl -L http://example.com

# POST med data
curl -X POST -d "name=test" http://api.com/endpoint

# POST med JSON
curl -X POST -H "Content-Type: application/json" \\
  -d '{"name":"test"}' http://api.com/endpoint

# ⭐ DEBUG: Visa allt (request + response)
curl -v http://example.com`
                },
                {
                    type: 'code',
                    title: 'wget - Ladda ner filer',
                    language: 'bash',
                    code: `# Ladda ner fil
wget http://example.com/file.tar.gz

# Spara med annat namn
wget -O myfile.tar.gz http://example.com/file.tar.gz

# Fortsätt avbruten nedladdning
wget -c http://example.com/largefile.iso

# Tyst läge (scripts)
wget -q http://example.com/file.tar.gz`
                },
                {
                    type: 'code',
                    title: 'ss/netstat - Nätverksanslutningar',
                    language: 'bash',
                    code: `# ⭐ Visa lyssnade portar
ss -tuln
netstat -tuln

# Visa alla anslutningar
ss -ta

# Visa med processnamn
ss -tulnp

# Hitta vad som lyssnar på port 80
ss -tlnp | grep :80`
                },
                {
                    type: 'tip',
                    title: 'Felsökningsworkflow',
                    content: '**När en tjänst inte svarar:**\n1. `ping server` - Är servern nåbar?\n2. `dig server` - Är DNS rätt?\n3. `ss -tlnp | grep :PORT` - Lyssnar tjänsten?\n4. `curl -v http://server:port` - Vad svarar den?'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'curl http://server (utan att kolla om servern är nåbar)',
                    right: 'ping server först, sedan curl',
                    explanation: 'Testa nätverket först (ping), sedan tjänsten (curl). Det sparar tid vid felsökning.'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Nätverks-snabbkoll',
                    commands: [
                        { cmd: 'ip a', desc: 'Visa IP-adresser' },
                        { cmd: 'ping -c 4 host', desc: 'Testa anslutning' },
                        { cmd: 'dig +short domain', desc: 'DNS-lookup' },
                        { cmd: 'curl -I url', desc: 'HTTP headers' },
                        { cmd: 'ss -tuln', desc: 'Lyssnade portar' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Network Basics',
                    content: 'Du kan nu diagnostisera nätverksproblem! ping, dig, curl och ss är dina go-to verktyg för att hitta var problemet ligger.'
                }
            ]
        },

        {
            id: 'linux247-9-packages',
            order: 9,
            title: 'Package Management',
            slug: 'package-management',
            description: 'Installera och hantera programpaket',
            difficulty: 'easy',
            estimatedMinutes: 40,
            xpReward: 100,
            category: 'System',
            icon: '📦',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Installera och ta bort paket med apt',
                        'Uppdatera system säkert',
                        'Söka efter paket',
                        'Förstå repositories',
                        'Grundläggande yum/dnf för Red Hat-system'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Pakethantering i Linux',
                    content: 'Linux använder pakethanterare för att installera mjukvara. Ubuntu/Debian använder apt, Red Hat/CentOS använder yum/dnf. Som DevOps installerar du nginx, docker, och andra verktyg dagligen.'
                },
                {
                    type: 'code',
                    title: 'apt - Grundläggande (Ubuntu/Debian)',
                    language: 'bash',
                    code: `# ⭐ STEG 1: Uppdatera paketlistan ALLTID först!
sudo apt update

# Installera paket
sudo apt install nginx

# Installera utan att fråga
sudo apt install -y nginx

# Ta bort paket
sudo apt remove nginx

# Ta bort paket + config-filer
sudo apt purge nginx

# ⭐ Städa bort oanvända dependencies
sudo apt autoremove`
                },
                {
                    type: 'warning',
                    title: 'apt update vs apt upgrade',
                    content: 'apt update - Uppdaterar LISTAN över tillgängliga paket\napt upgrade - Uppgraderar INSTALLERADE paket till nyare versioner\n\nKör alltid update INNAN upgrade!'
                },
                {
                    type: 'code',
                    title: 'Uppgradera system',
                    language: 'bash',
                    code: `# ⭐ Säker uppgradering (rekommenderat)
sudo apt update
sudo apt upgrade -y

# Full uppgradering (kan ta bort paket)
sudo apt full-upgrade

# Kontrollera vad som kommer uppgraderas
apt list --upgradable

# ⭐ One-liner för uppdatering
sudo apt update && sudo apt upgrade -y`
                },
                {
                    type: 'quiz',
                    question: 'Du ska installera nginx på en ny server. Vad gör du FÖRST?',
                    options: ['apt install nginx', 'apt upgrade', 'apt update', 'apt search nginx'],
                    correctIndex: 2,
                    explanation: 'Alltid "apt update" först! Detta uppdaterar paketlistan så apt vet vilka versioner som finns tillgängliga.'
                },
                {
                    type: 'code',
                    title: 'Söka och visa info',
                    language: 'bash',
                    code: `# Sök efter paket
apt search nginx

# Visa paketinfo
apt show nginx

# Lista installerade paket
apt list --installed

# Kolla om paket är installerat
apt list --installed | grep nginx
# eller
dpkg -l | grep nginx`
                },
                {
                    type: 'code',
                    title: 'yum/dnf - Red Hat/CentOS/Fedora',
                    language: 'bash',
                    code: `# dnf är nyare, yum fungerar fortfarande

# Installera
sudo dnf install nginx
sudo yum install nginx

# Uppdatera
sudo dnf update

# Ta bort
sudo dnf remove nginx

# Sök
dnf search nginx

# Info
dnf info nginx`
                },
                {
                    type: 'quiz',
                    question: 'Vilket kommando tar bort nginx OCH dess config-filer på Ubuntu?',
                    options: ['apt remove nginx', 'apt purge nginx', 'apt delete nginx', 'apt uninstall nginx'],
                    correctIndex: 1,
                    explanation: 'apt purge tar bort paketet OCH alla konfigurationsfiler. apt remove behåller config-filerna.'
                },
                {
                    type: 'code',
                    title: 'Praktiska mönster',
                    language: 'bash',
                    code: `# ⭐ Installera flera paket
sudo apt install -y nginx git curl htop

# Kolla vilken version som är installerad
apt policy nginx

# Installera specifik version
sudo apt install nginx=1.18.0-0ubuntu1

# ⭐ DevOps-mönster: Setup-script
#!/bin/bash
apt update
apt install -y nginx git docker.io
systemctl enable nginx docker`
                },
                {
                    type: 'tip',
                    title: 'DevOps Pro-Tips',
                    content: '**I scripts:**\n- Använd `-y` för att inte fastna på frågor\n- Kör alltid `update` först\n- Dokumentera vilka paket som behövs i en README\n\n**Säkerhet:**\n- Uppdatera regelbundet: `apt update && apt upgrade -y`\n- Kör detta som cron-jobb på staging-miljöer'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'apt install paket (utan apt update först)',
                    right: 'apt update && apt install paket',
                    explanation: 'Utan update kan apt försöka installera gamla versioner som inte längre finns.'
                },
                {
                    type: 'mnemonic',
                    title: '🧠 Minnesregel',
                    concept: 'apt-flödet',
                    trick: 'Update → Upgrade → Install (UUI)',
                    example: 'apt update, apt upgrade, apt install nginx'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 apt Snabbkoll',
                    commands: [
                        { cmd: 'apt update', desc: 'Uppdatera paketlistan' },
                        { cmd: 'apt upgrade -y', desc: 'Uppgradera alla paket' },
                        { cmd: 'apt install -y pkg', desc: 'Installera paket' },
                        { cmd: 'apt purge pkg', desc: 'Ta bort + config' },
                        { cmd: 'apt autoremove', desc: 'Städa dependencies' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Package Management',
                    content: 'Du kan nu installera, uppdatera och ta bort paket! Kom ihåg: alltid "apt update" först.'
                }
            ]
        },

        {
            id: 'linux247-10-systemd',
            order: 10,
            title: 'System Services & systemd',
            slug: 'systemd-services',
            description: 'Hantera tjänster med systemctl',
            difficulty: 'medium',
            estimatedMinutes: 50,
            xpReward: 140,
            category: 'System',
            icon: '🔧',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Hantera tjänster med systemctl',
                        'Starta, stoppa och restarta services',
                        'Aktivera services vid boot',
                        'Felsöka med journalctl',
                        'Förstå service units'
                    ]
                },
                {
                    type: 'concept',
                    title: 'systemd - Hjärtat i moderna Linux',
                    content: 'systemd är init-systemet som startar och hanterar alla tjänster (nginx, docker, ssh, etc.). systemctl är kommandot för att styra dessa tjänster. Som DevOps använder du detta KONSTANT.'
                },
                {
                    type: 'code',
                    title: 'systemctl - Grundläggande',
                    language: 'bash',
                    code: `# ⭐ Visa status för en tjänst
systemctl status nginx

# Starta tjänst
sudo systemctl start nginx

# Stoppa tjänst
sudo systemctl stop nginx

# ⭐ Restarta (stoppa + starta)
sudo systemctl restart nginx

# Reload config utan att stoppa
sudo systemctl reload nginx`
                },
                {
                    type: 'quiz',
                    question: 'Du har ändrat nginx.conf. Hur laddar du om utan att tappa anslutningar?',
                    options: ['systemctl restart nginx', 'systemctl reload nginx', 'systemctl stop nginx && start nginx', 'nginx -reload'],
                    correctIndex: 1,
                    explanation: 'reload laddar om konfigurationen utan att stoppa tjänsten. restart stoppar och startar, vilket kan tappa anslutningar.'
                },
                {
                    type: 'code',
                    title: 'Enable/Disable - Autostart vid boot',
                    language: 'bash',
                    code: `# ⭐ Starta automatiskt vid boot
sudo systemctl enable nginx

# Inaktivera autostart
sudo systemctl disable nginx

# Enable + starta direkt
sudo systemctl enable --now nginx

# Kolla om enabled
systemctl is-enabled nginx`
                },
                {
                    type: 'warning',
                    title: 'enable ≠ start',
                    content: 'enable = startar vid BOOT\nstart = startar NU\n\nOm du vill ha båda: systemctl enable --now nginx'
                },
                {
                    type: 'code',
                    title: 'Visa och lista tjänster',
                    language: 'bash',
                    code: `# ⭐ Lista alla aktiva tjänster
systemctl list-units --type=service

# Lista alla tjänster (inkl inaktiva)
systemctl list-units --type=service --all

# Lista enabled services
systemctl list-unit-files --type=service | grep enabled

# Kolla om tjänst körs
systemctl is-active nginx`
                },
                {
                    type: 'code',
                    title: 'journalctl - Loggar för tjänster',
                    language: 'bash',
                    code: `# ⭐ Loggar för specifik tjänst
journalctl -u nginx

# Senaste loggarna
journalctl -u nginx -n 50

# Följ i realtid
journalctl -u nginx -f

# Sedan senaste boot
journalctl -u nginx -b

# ⭐ Endast fel
journalctl -u nginx -p err

# Senaste timmen
journalctl -u nginx --since "1 hour ago"`
                },
                {
                    type: 'quiz',
                    question: 'nginx startar inte. Vad kör du för att se varför?',
                    options: ['cat /var/log/nginx/error.log', 'journalctl -u nginx', 'systemctl status nginx', 'Alla fungerar!'],
                    correctIndex: 3,
                    explanation: 'Alla tre ger användbar info! systemctl status ger snabb överblick, journalctl ger detaljerade loggar, och nginx error.log har applikationsloggar.'
                },
                {
                    type: 'code',
                    title: 'Felsökning - Vanliga kommandon',
                    language: 'bash',
                    code: `# ⭐ STEG 1: Kolla status
systemctl status nginx

# STEG 2: Kolla loggar
journalctl -u nginx -n 50 --no-pager

# STEG 3: Testa config (nginx-specifikt)
nginx -t

# STEG 4: Försök starta igen
sudo systemctl start nginx

# PRO: Reload systemd om unit-fil ändrats
sudo systemctl daemon-reload`
                },
                {
                    type: 'tip',
                    title: 'DevOps Felsökningsworkflow',
                    content: '**Service startar inte?**\n1. `systemctl status service` - Snabb överblick\n2. `journalctl -u service -n 50` - Detaljerade loggar\n3. Fixa problemet (oftast config-fel)\n4. `systemctl daemon-reload` (om unit ändrats)\n5. `systemctl restart service`'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'systemctl start nginx (och förvänta sig att det startar vid boot)',
                    right: 'systemctl enable --now nginx',
                    explanation: 'start startar bara NU. enable gör att den startar vid BOOT. Använd --now för båda.'
                },
                {
                    type: 'mnemonic',
                    title: '🧠 Minnesregel',
                    concept: 'systemctl-kommandon',
                    trick: 'SSRE: Status, Start, Restart, Enable',
                    example: 'Börja med status för att se läget, sedan start/restart, och enable för autostart'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 systemctl Snabbkoll',
                    commands: [
                        { cmd: 'systemctl status svc', desc: 'Visa status' },
                        { cmd: 'systemctl restart svc', desc: 'Starta om' },
                        { cmd: 'systemctl enable --now svc', desc: 'Enable + start' },
                        { cmd: 'journalctl -u svc -f', desc: 'Följ loggar live' },
                        { cmd: 'systemctl daemon-reload', desc: 'Ladda om unit-filer' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: systemd Services',
                    content: 'Du kan nu hantera tjänster som ett proffs! systemctl och journalctl är dina viktigaste verktyg för service management.'
                }
            ]
        },

        {
            id: 'linux247-11-permissions',
            order: 11,
            title: 'File Permissions & Security',
            slug: 'file-permissions',
            description: 'Linux rättigheter och säkerhet',
            difficulty: 'medium',
            estimatedMinutes: 45,
            xpReward: 120,
            category: 'Säkerhet',
            icon: '🔒',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Läsa och förstå filrättigheter (rwx)',
                        'Ändra rättigheter med chmod',
                        'Ändra ägare med chown',
                        'Förstå numerisk notation (755, 644)',
                        'Grundläggande om SUID/SGID'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Varför rättigheter är kritiska',
                    content: 'Filrättigheter skyddar ditt system. Fel rättigheter = säkerhetshål eller tjänster som inte fungerar. Som DevOps måste du förstå rwx och kunna sätta rätt rättigheter på config-filer, scripts och webbkataloger.'
                },
                {
                    type: 'code',
                    title: 'Läsa rättigheter - ls -l',
                    language: 'bash',
                    code: `ls -l fil.txt
# -rw-r--r-- 1 user group 1234 Jan 1 12:00 fil.txt

# Första tecknet: filtyp
# - = vanlig fil
# d = katalog
# l = symbolisk länk

# Sedan 3 grupper om 3 tecken:
# rwx = user (ägare)
# r-x = group
# r-- = others

# r = read (läsa)
# w = write (skriva)
# x = execute (köra)`
                },
                {
                    type: 'quiz',
                    question: 'Vad betyder rättigheterna -rwxr-x--- ?',
                    options: [
                        'Alla kan göra allt',
                        'User: alla, Group: läsa+köra, Others: inget',
                        'User: läsa, Group: alla, Others: köra',
                        'Endast user kan läsa'
                    ],
                    correctIndex: 1,
                    explanation: 'rwx för user (alla rättigheter), r-x för group (läsa+köra), --- för others (inga rättigheter)'
                },
                {
                    type: 'code',
                    title: 'chmod - Symbolisk notation',
                    language: 'bash',
                    code: `# Lägg till rättighet
chmod +x script.sh        # Alla får köra
chmod u+x script.sh       # User får köra
chmod g+w fil.txt         # Group får skriva

# Ta bort rättighet
chmod -w fil.txt          # Ta bort skrivrätt för alla
chmod o-rwx fil.txt       # Others får inget

# Sätt exakt
chmod u=rwx,g=rx,o= fil.txt

# ⭐ Vanligt för scripts
chmod +x script.sh`
                },
                {
                    type: 'code',
                    title: 'chmod - Numerisk notation (VIKTIGT!)',
                    language: 'bash',
                    code: `# Siffror: r=4, w=2, x=1
# Summera för varje grupp: user, group, others

# 755 = rwxr-xr-x (user: 7, group: 5, others: 5)
chmod 755 script.sh

# 644 = rw-r--r-- (vanligt för filer)
chmod 644 config.txt

# ⭐ VANLIGA MÖNSTER:
chmod 755 script.sh      # Körbart script
chmod 644 config.txt     # Config-fil
chmod 600 id_rsa         # SSH privat nyckel
chmod 700 .ssh/          # SSH-katalog`
                },
                {
                    type: 'quiz',
                    question: 'Vilka rättigheter ger chmod 644?',
                    options: ['rwxr--r--', 'rw-r--r--', 'rw-rw-r--', 'r--r--r--'],
                    correctIndex: 1,
                    explanation: '6=rw- (4+2), 4=r-- (4), 4=r-- (4). Alltså: user kan läsa+skriva, group och others kan endast läsa.'
                },
                {
                    type: 'code',
                    title: 'chown - Ändra ägare',
                    language: 'bash',
                    code: `# Ändra user
sudo chown nginx fil.txt

# Ändra user och group
sudo chown nginx:www-data fil.txt

# Endast group
sudo chown :www-data fil.txt

# ⭐ Rekursivt för katalog
sudo chown -R www-data:www-data /var/www/html/`
                },
                {
                    type: 'code',
                    title: 'Praktiska exempel',
                    language: 'bash',
                    code: `# ⭐ SSH-nycklar (MÅSTE vara rätt!)
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub

# Webbkatalog
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html

# Script körbart
chmod +x deploy.sh

# ⭐ Säker config-fil
chmod 600 .env
chmod 640 /etc/myapp/config.yml`
                },
                {
                    type: 'warning',
                    title: 'ALDRIG chmod 777!',
                    content: '777 ger ALLA full tillgång - detta är en säkerhetsrisk! Om du behöver 777 för att något ska fungera, är det ett tecken på att något annat är fel (oftast ägare/group).'
                },
                {
                    type: 'tip',
                    title: 'Snabbguide: Vanliga rättigheter',
                    content: '**755** - Kataloger, scripts (rwxr-xr-x)\n**644** - Vanliga filer (rw-r--r--)\n**600** - Känsliga filer (rw-------)\n**700** - Privata kataloger (rwx------)'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'chmod 777 fil (för att det "fungerar")',
                    right: 'chown rätt-user:rätt-group fil && chmod 755 fil',
                    explanation: 'Fixa ägare/grupp istället för att ge alla full tillgång!'
                },
                {
                    type: 'mnemonic',
                    title: '🧠 Minnesregel',
                    concept: 'rwx-siffror',
                    trick: 'r=4, w=2, x=1 (421) - Summera!',
                    example: '7=rwx (4+2+1), 5=r-x (4+1), 4=r-- (4)'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Permissions Snabbkoll',
                    commands: [
                        { cmd: 'chmod 755 script.sh', desc: 'Körbart script' },
                        { cmd: 'chmod 644 file.txt', desc: 'Vanlig fil' },
                        { cmd: 'chmod 600 .env', desc: 'Känslig fil' },
                        { cmd: 'chown -R user:group dir/', desc: 'Ändra ägare rekursivt' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: File Permissions',
                    content: 'Du förstår nu Linux rättigheter! Kom ihåg: 755 för scripts/kataloger, 644 för filer, 600 för känsligt. Och ALDRIG 777!'
                }
            ]
        },

        {
            id: 'linux247-12-compression',
            order: 12,
            title: 'Compression & Archives',
            slug: 'compression-archives',
            description: 'Komprimera och packa filer',
            difficulty: 'easy',
            estimatedMinutes: 35,
            xpReward: 90,
            category: 'Grundläggande',
            icon: '🗜️',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Skapa och packa upp tar-arkiv',
                        'Komprimera med gzip och bzip2',
                        'Använda tar.gz och tar.bz2',
                        'Arbeta med zip-filer',
                        'Vanliga DevOps-mönster för backup'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Arkivering i DevOps',
                    content: 'tar (tape archive) skapar arkiv av flera filer. gzip komprimerar. Tillsammans = .tar.gz, det vanligaste formatet i Linux. Som DevOps använder du detta för backup, deploy och distribution.'
                },
                {
                    type: 'code',
                    title: 'tar - Grundläggande',
                    language: 'bash',
                    code: `# ⭐ SKAPA arkiv (c = create)
tar -cvf arkiv.tar katalog/
# c = create
# v = verbose (visa filer)
# f = file (ange filnamn)

# PACKA UPP (x = extract)
tar -xvf arkiv.tar

# ⭐ Packa upp till specifik katalog
tar -xvf arkiv.tar -C /destination/

# Lista innehåll (t = list)
tar -tvf arkiv.tar`
                },
                {
                    type: 'code',
                    title: 'tar.gz - Komprimerat arkiv',
                    language: 'bash',
                    code: `# ⭐ SKAPA .tar.gz (vanligast!)
tar -czvf arkiv.tar.gz katalog/
# z = gzip compression

# PACKA UPP .tar.gz
tar -xzvf arkiv.tar.gz

# ⭐ PRO-TIP: tar detekterar komprimering!
tar -xvf arkiv.tar.gz  # Fungerar utan z!

# Skapa .tar.bz2 (bättre komprimering)
tar -cjvf arkiv.tar.bz2 katalog/`
                },
                {
                    type: 'quiz',
                    question: 'Hur packar du upp backup.tar.gz till /restore/?',
                    options: [
                        'tar -xvf backup.tar.gz /restore/',
                        'tar -xzvf backup.tar.gz -C /restore/',
                        'unzip backup.tar.gz -d /restore/',
                        'gunzip backup.tar.gz /restore/'
                    ],
                    correctIndex: 1,
                    explanation: '-C anger destination-katalogen. -x extraherar, -z hanterar gzip, -v visar progress, -f anger filen.'
                },
                {
                    type: 'code',
                    title: 'gzip - Komprimera enskilda filer',
                    language: 'bash',
                    code: `# Komprimera fil (ersätter originalet!)
gzip fil.txt
# Resultat: fil.txt.gz

# Packa upp
gunzip fil.txt.gz
# eller
gzip -d fil.txt.gz

# Behåll originalet
gzip -k fil.txt

# Visa utan att packa upp
zcat fil.txt.gz
zless fil.txt.gz`
                },
                {
                    type: 'code',
                    title: 'zip - Windows-kompatibelt',
                    language: 'bash',
                    code: `# Skapa zip
zip arkiv.zip fil1.txt fil2.txt

# Zip med katalog (rekursivt)
zip -r arkiv.zip katalog/

# Packa upp
unzip arkiv.zip

# Packa upp till specifik katalog
unzip arkiv.zip -d /destination/

# Lista innehåll
unzip -l arkiv.zip`
                },
                {
                    type: 'quiz',
                    question: 'Vilket kommando skapar backup.tar.gz av /var/www?',
                    options: [
                        'tar -xzvf backup.tar.gz /var/www',
                        'tar -czvf backup.tar.gz /var/www',
                        'gzip -r /var/www > backup.tar.gz',
                        'zip -r backup.tar.gz /var/www'
                    ],
                    correctIndex: 1,
                    explanation: '-c = create (skapa), -z = gzip, -v = verbose, -f = filename. -x är för extract (packa upp).'
                },
                {
                    type: 'code',
                    title: 'Praktiska DevOps-mönster',
                    language: 'bash',
                    code: `# ⭐ Backup med datum
tar -czvf backup_$(date +%Y%m%d).tar.gz /var/www/

# Backup exkludera vissa filer
tar --exclude='*.log' --exclude='node_modules' \\
    -czvf backup.tar.gz projekt/

# ⭐ Snabb deploy-paket
tar -czvf release-v1.2.3.tar.gz \\
    --exclude='.git' \\
    --exclude='node_modules' \\
    --exclude='.env' \\
    .

# Packa upp och överskriva
tar -xzvf backup.tar.gz -C / --overwrite`
                },
                {
                    type: 'tip',
                    title: 'Minnesregel: tar-flaggor',
                    content: '**c** = Create (skapa)\n**x** = eXtract (packa upp)\n**t** = lisT (visa innehåll)\n**z** = gZip\n**v** = Verbose\n**f** = File (måste vara sist!)'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'tar -czvf katalog/ arkiv.tar.gz (fel ordning)',
                    right: 'tar -czvf arkiv.tar.gz katalog/',
                    explanation: 'Arkivnamnet kommer direkt efter -f. Ordningen är viktig!'
                },
                {
                    type: 'mnemonic',
                    title: '🧠 Minnesregel',
                    concept: 'tar create vs extract',
                    trick: 'Create = czvf, eXtract = xzvf',
                    example: 'tar -czvf (skapa), tar -xzvf (packa upp)'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Arkiv Snabbkoll',
                    commands: [
                        { cmd: 'tar -czvf arkiv.tar.gz dir/', desc: 'Skapa .tar.gz' },
                        { cmd: 'tar -xzvf arkiv.tar.gz', desc: 'Packa upp .tar.gz' },
                        { cmd: 'tar -xzvf fil.tar.gz -C /dest/', desc: 'Packa upp till katalog' },
                        { cmd: 'tar -tvf arkiv.tar.gz', desc: 'Lista innehåll' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Compression & Archives',
                    content: 'Du kan nu skapa och packa upp arkiv! tar -czvf för att skapa, tar -xzvf för att packa upp. Det är allt du behöver!'
                }
            ]
        },

        {
            id: 'linux247-13-environment',
            order: 13,
            title: 'Environment & Variables',
            slug: 'environment-variables',
            description: 'Miljövariabler och konfiguration',
            difficulty: 'medium',
            estimatedMinutes: 40,
            xpReward: 110,
            category: 'System',
            icon: '🌍',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Förstå vad miljövariabler är',
                        'Sätta och exportera variabler',
                        'Förstå PATH-variabeln',
                        'Göra variabler persistenta (.bashrc)',
                        'Arbeta med .env-filer'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Miljövariabler i DevOps',
                    content: 'Miljövariabler lagrar konfiguration utanför koden. API-nycklar, databasanslutningar, och featureflaggor sätts som miljövariabler. Detta är 12-factor app principen - config hör inte hemma i koden!'
                },
                {
                    type: 'code',
                    title: 'Visa miljövariabler',
                    language: 'bash',
                    code: `# Visa alla miljövariabler
env
printenv

# Visa specifik variabel
echo $HOME
echo $USER
echo $PATH

# Eller med printenv
printenv HOME`
                },
                {
                    type: 'code',
                    title: 'Sätta variabler',
                    language: 'bash',
                    code: `# Sätt variabel (endast i denna shell)
MY_VAR="hello"
echo $MY_VAR

# ⭐ Export - gör tillgänglig för child-processer
export MY_VAR="hello"
export DATABASE_URL="postgres://localhost:5432/mydb"

# Sätt och exportera på en rad
export API_KEY="secret123"

# Ta bort variabel
unset MY_VAR`
                },
                {
                    type: 'quiz',
                    question: 'Du sätter MY_VAR="test" och kör ett script. Varför ser inte scriptet variabeln?',
                    options: [
                        'Variabeln har fel namn',
                        'Du måste använda export',
                        'Scripts kan inte läsa variabler',
                        'Du måste starta om terminalen'
                    ],
                    correctIndex: 1,
                    explanation: 'Utan export är variabeln lokal till din shell. Child-processer (scripts) ser inte den. Använd: export MY_VAR="test"'
                },
                {
                    type: 'code',
                    title: 'PATH - Var kommandon finns',
                    language: 'bash',
                    code: `# Visa PATH
echo $PATH
# /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

# ⭐ Lägg till katalog till PATH
export PATH="$PATH:/home/user/scripts"

# Lägg till först (högre prioritet)
export PATH="/opt/myapp/bin:$PATH"

# Hitta var ett kommando finns
which python
which nginx`
                },
                {
                    type: 'code',
                    title: 'Persistenta variabler - .bashrc',
                    language: 'bash',
                    code: `# ⭐ Lägg till i ~/.bashrc för permanent effekt
echo 'export MY_VAR="permanent"' >> ~/.bashrc

# Ladda om .bashrc
source ~/.bashrc
# eller
. ~/.bashrc

# Olika filer för olika syften:
# ~/.bashrc     - Interaktiva shells
# ~/.profile    - Login shells
# ~/.bash_profile - Login shells (om finns)
# /etc/environment - Systemvida variabler`
                },
                {
                    type: 'quiz',
                    question: 'Du lägger till en export i .bashrc. Varför syns den inte direkt?',
                    options: [
                        '.bashrc är fel fil',
                        'Du måste köra source ~/.bashrc',
                        'Variabeln är ogiltig',
                        'Du har inte sudo-rättigheter'
                    ],
                    correctIndex: 1,
                    explanation: '.bashrc laddas vid ny shell-session. För att ladda ändringar direkt: source ~/.bashrc'
                },
                {
                    type: 'code',
                    title: '.env-filer (DevOps-standard)',
                    language: 'bash',
                    code: `# Skapa .env-fil
cat > .env << 'EOF'
DATABASE_URL=postgres://localhost:5432/mydb
API_KEY=secret123
DEBUG=true
EOF

# ⭐ Ladda .env-fil
export $(cat .env | xargs)

# Eller med source (kräver export i filen)
set -a
source .env
set +a

# I scripts:
if [ -f .env ]; then
    export $(cat .env | xargs)
fi`
                },
                {
                    type: 'code',
                    title: 'Praktiska mönster',
                    language: 'bash',
                    code: `# ⭐ Kör kommando med temporär variabel
DATABASE_URL="test-db" ./migrate.sh

# Visa om variabel finns
if [ -z "$API_KEY" ]; then
    echo "API_KEY saknas!"
    exit 1
fi

# Default-värde om variabel saknas
PORT=\${PORT:-3000}

# Docker: skicka miljövariabler
docker run -e DATABASE_URL -e API_KEY myapp`
                },
                {
                    type: 'warning',
                    title: 'SÄKERHET: .env-filer',
                    content: 'Lägg ALDRIG .env i git! Lägg till .env i .gitignore. Använd .env.example för att dokumentera vilka variabler som behövs.'
                },
                {
                    type: 'tip',
                    title: 'DevOps Best Practice',
                    content: '**12-Factor App:**\n- Ingen config i koden\n- Alla secrets som miljövariabler\n- .env för lokal utveckling\n- Secrets management (Vault, AWS Secrets) i produktion'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'MY_VAR="test" (och förvänta sig att script ser det)',
                    right: 'export MY_VAR="test"',
                    explanation: 'Utan export är variabeln lokal. Child-processer ärver endast exporterade variabler.'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Miljövariabler Snabbkoll',
                    commands: [
                        { cmd: 'export VAR="value"', desc: 'Sätt och exportera' },
                        { cmd: 'source ~/.bashrc', desc: 'Ladda om config' },
                        { cmd: 'echo $VAR', desc: 'Visa variabel' },
                        { cmd: 'export $(cat .env | xargs)', desc: 'Ladda .env' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Environment Variables',
                    content: 'Du förstår nu miljövariabler! export gör variabler tillgängliga, .bashrc gör dem permanenta, och .env-filer är DevOps-standard.'
                }
            ]
        },

        {
            id: 'linux247-14-disk',
            order: 14,
            title: 'Disk Management',
            slug: 'disk-management',
            description: 'Hantera diskar och partitioner',
            difficulty: 'hard',
            estimatedMinutes: 55,
            xpReward: 150,
            category: 'System',
            icon: '💿',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Visa diskar och partitioner med lsblk',
                        'Förstå Linux disk-namngivning',
                        'Montera och avmontera filsystem',
                        'Konfigurera /etc/fstab för automontering',
                        'Grundläggande partitionering'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Diskar i Linux',
                    content: 'Linux ser diskar som filer i /dev. sda = första SATA/SCSI-disken, sda1 = första partitionen. nvme0n1 = första NVMe-SSD. Som DevOps behöver du kunna lägga till extra diskar och montera dem korrekt.'
                },
                {
                    type: 'code',
                    title: 'lsblk - Lista block devices',
                    language: 'bash',
                    code: `# ⭐ Visa alla diskar och partitioner
lsblk

# Med filsystemtyp
lsblk -f

# Exempel output:
# NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
# sda      8:0    0   50G  0 disk
# ├─sda1   8:1    0   49G  0 part /
# └─sda2   8:2    0    1G  0 part [SWAP]
# sdb      8:16   0  100G  0 disk
# └─sdb1   8:17   0  100G  0 part /data`
                },
                {
                    type: 'code',
                    title: 'df och du - Diskutrymme',
                    language: 'bash',
                    code: `# ⭐ Visa ledigt utrymme per partition
df -h

# Visa filsystemtyp
df -Th

# Visa användning för katalog
du -sh /var/log

# ⭐ Hitta vad som tar plats
du -h --max-depth=1 / 2>/dev/null | sort -rh | head -20`
                },
                {
                    type: 'quiz',
                    question: 'Disken är 95% full. Vilket kommando hittar snabbast vad som tar plats?',
                    options: [
                        'ls -la /',
                        'df -h',
                        'du -h --max-depth=1 / | sort -rh | head',
                        'find / -size +100M'
                    ],
                    correctIndex: 2,
                    explanation: 'du med --max-depth=1 visar storleken på kataloger i /, sorterat visar det de största först. df visar bara att disken är full, inte var.'
                },
                {
                    type: 'code',
                    title: 'mount - Montera filsystem',
                    language: 'bash',
                    code: `# Visa monterade filsystem
mount
mount | grep sda

# ⭐ Montera partition
sudo mount /dev/sdb1 /mnt/data

# Montera med specifik typ
sudo mount -t ext4 /dev/sdb1 /mnt/data

# Avmontera
sudo umount /mnt/data
# eller
sudo umount /dev/sdb1`
                },
                {
                    type: 'warning',
                    title: 'VARNING: umount',
                    content: 'Du kan inte avmontera ett filsystem som är i användning (filer öppna, terminal i katalogen). Byt katalog först eller använd lsof för att hitta vad som blockerar.'
                },
                {
                    type: 'code',
                    title: '/etc/fstab - Automontering',
                    language: 'bash',
                    code: `# Visa fstab
cat /etc/fstab

# Format:
# <device>  <mount>  <type>  <options>  <dump>  <pass>

# Exempel:
# /dev/sdb1  /data  ext4  defaults  0  2

# ⭐ Lägg till ny disk (editera fstab)
sudo nano /etc/fstab
# Lägg till:
# /dev/sdb1  /mnt/data  ext4  defaults  0  2

# Testa fstab utan omstart
sudo mount -a`
                },
                {
                    type: 'quiz',
                    question: 'Du har lagt till en rad i /etc/fstab. Hur testar du utan omstart?',
                    options: ['reboot', 'mount -a', 'systemctl reload fstab', 'fstab --test'],
                    correctIndex: 1,
                    explanation: 'mount -a monterar alla filsystem i fstab som inte redan är monterade. Perfekt för att testa nya rader utan omstart.'
                },
                {
                    type: 'code',
                    title: 'Skapa filsystem (formatera)',
                    language: 'bash',
                    code: `# ⚠️ VARNING: Detta raderar all data!

# Skapa ext4 filsystem
sudo mkfs.ext4 /dev/sdb1

# Skapa xfs filsystem
sudo mkfs.xfs /dev/sdb1

# ⭐ Komplett flöde för ny disk:
# 1. Identifiera disken
lsblk

# 2. Partitionera (om ny disk)
sudo fdisk /dev/sdb

# 3. Skapa filsystem
sudo mkfs.ext4 /dev/sdb1

# 4. Skapa mount point
sudo mkdir -p /mnt/data

# 5. Montera
sudo mount /dev/sdb1 /mnt/data

# 6. Lägg till i fstab för autostart`
                },
                {
                    type: 'code',
                    title: 'Praktiska scenario',
                    language: 'bash',
                    code: `# ⭐ Disk full? Hitta stora filer
find / -type f -size +100M 2>/dev/null | head -20

# Hitta stora loggar
find /var/log -type f -size +50M

# Rensa vanliga space-hogs
sudo journalctl --vacuum-size=100M
sudo apt clean
sudo rm -rf /tmp/*

# Kolla inode-användning (många små filer)
df -i`
                },
                {
                    type: 'tip',
                    title: 'DevOps Disk-workflow',
                    content: '**Ny disk i molnet:**\n1. Attach disk i konsolen\n2. `lsblk` - hitta nya disken\n3. `mkfs.ext4 /dev/xvdf`\n4. `mkdir /data && mount /dev/xvdf /data`\n5. Lägg till i `/etc/fstab`'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'Editera fstab med fel device (t.ex. sda istället för sdb)',
                    right: 'Dubbelkolla med lsblk INNAN du editerar fstab',
                    explanation: 'Fel i fstab kan göra systemet obootbart! Verifiera alltid disk-namnet med lsblk.'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Disk Snabbkoll',
                    commands: [
                        { cmd: 'lsblk', desc: 'Lista diskar' },
                        { cmd: 'df -h', desc: 'Visa ledigt utrymme' },
                        { cmd: 'du -sh /path', desc: 'Katalogstorlek' },
                        { cmd: 'mount /dev/sdb1 /mnt', desc: 'Montera disk' },
                        { cmd: 'mount -a', desc: 'Montera alla i fstab' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Disk Management',
                    content: 'Du kan nu hantera diskar! lsblk för att se, df -h för utrymme, mount för att koppla, och fstab för autostart.'
                }
            ]
        },

        {
            id: 'linux247-15-reference',
            order: 15,
            title: 'Quick Reference & Workflows',
            slug: 'quick-reference',
            description: 'Snabbreferens och arbetsflöden',
            difficulty: 'easy',
            estimatedMinutes: 30,
            xpReward: 80,
            category: 'Reference',
            icon: '📚',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Sammanfatta de viktigaste kommandona',
                        'Felsökningsworkflows för vanliga problem',
                        'One-liners som sparar tid',
                        'Cheat sheets för tentaplugg'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Snabbreferens för DevOps',
                    content: 'Denna task samlar de viktigaste kommandona och workflows du behöver. Perfekt för tentaplugg och som snabbreferens i arbetet.'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Filsystem & Navigation',
                    commands: [
                        { cmd: 'pwd', desc: 'Visa nuvarande katalog' },
                        { cmd: 'ls -lah', desc: 'Lista allt, human-readable' },
                        { cmd: 'cd -', desc: 'Gå till förra katalogen' },
                        { cmd: 'cp -r src/ dest/', desc: 'Kopiera rekursivt' },
                        { cmd: 'rm -rf dir/', desc: 'Ta bort katalog (FARLIGT!)' },
                        { cmd: 'find . -name "*.log"', desc: 'Hitta filer' }
                    ]
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Text & Sökning',
                    commands: [
                        { cmd: 'cat fil.txt', desc: 'Visa fil' },
                        { cmd: 'tail -f logfil', desc: 'Följ logg live' },
                        { cmd: 'grep -rni "text" .', desc: 'Sök rekursivt' },
                        { cmd: 'grep -v "^#" fil', desc: 'Ignorera kommentarer' },
                        { cmd: 'wc -l fil', desc: 'Räkna rader' },
                        { cmd: 'sort | uniq -c', desc: 'Räkna unika' }
                    ]
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Processer & System',
                    commands: [
                        { cmd: 'ps aux', desc: 'Alla processer' },
                        { cmd: 'ps aux | grep nginx', desc: 'Hitta process' },
                        { cmd: 'kill -9 PID', desc: 'Tvinga avsluta' },
                        { cmd: 'pkill processnamn', desc: 'Avsluta via namn' },
                        { cmd: 'htop', desc: 'Interaktiv processvy' },
                        { cmd: 'free -h', desc: 'Minnesanvändning' },
                        { cmd: 'df -h', desc: 'Diskutrymme' }
                    ]
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Services (systemd)',
                    commands: [
                        { cmd: 'systemctl status svc', desc: 'Visa status' },
                        { cmd: 'systemctl start svc', desc: 'Starta' },
                        { cmd: 'systemctl restart svc', desc: 'Starta om' },
                        { cmd: 'systemctl enable --now svc', desc: 'Enable + start' },
                        { cmd: 'journalctl -u svc -f', desc: 'Följ loggar' },
                        { cmd: 'journalctl -p err', desc: 'Endast fel' }
                    ]
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Nätverk',
                    commands: [
                        { cmd: 'ip a', desc: 'Visa IP-adresser' },
                        { cmd: 'ping -c 4 host', desc: 'Testa anslutning' },
                        { cmd: 'ss -tuln', desc: 'Lyssnade portar' },
                        { cmd: 'curl -I url', desc: 'HTTP headers' },
                        { cmd: 'dig +short domain', desc: 'DNS lookup' }
                    ]
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Brandvägg (ufw)',
                    commands: [
                        { cmd: 'ufw status', desc: 'Visa status' },
                        { cmd: 'ufw allow ssh', desc: 'Tillåt SSH' },
                        { cmd: 'ufw allow 80,443/tcp', desc: 'Tillåt HTTP/S' },
                        { cmd: 'ufw enable', desc: 'Aktivera' },
                        { cmd: 'ufw delete allow 80', desc: 'Ta bort regel' }
                    ]
                },
                {
                    type: 'code',
                    title: '⭐ WORKFLOW: Service startar inte',
                    language: 'bash',
                    code: `# 1. Kolla status
systemctl status nginx

# 2. Se loggar
journalctl -u nginx -n 50 --no-pager

# 3. Testa config (nginx-specifikt)
nginx -t

# 4. Fixa problemet (oftast config-fel)

# 5. Starta om
sudo systemctl restart nginx`
                },
                {
                    type: 'code',
                    title: '⭐ WORKFLOW: Disk full',
                    language: 'bash',
                    code: `# 1. Se vad som är fullt
df -h

# 2. Hitta stora kataloger
du -h --max-depth=1 / 2>/dev/null | sort -rh | head

# 3. Vanliga bov: loggar
du -sh /var/log/*

# 4. Städa
sudo journalctl --vacuum-size=100M
sudo apt clean
sudo rm -rf /tmp/*`
                },
                {
                    type: 'code',
                    title: '⭐ WORKFLOW: Kan inte nå server',
                    language: 'bash',
                    code: `# 1. Pinga servern
ping -c 4 server.com

# 2. Kolla DNS
dig +short server.com

# 3. Kolla om port är öppen
nc -zv server.com 80

# 4. Testa HTTP
curl -I http://server.com

# 5. Kolla lokalt om tjänsten lyssnar
ss -tuln | grep :80`
                },
                {
                    type: 'code',
                    title: '⭐ WORKFLOW: Setup ny server',
                    language: 'bash',
                    code: `# 1. Uppdatera system
sudo apt update && sudo apt upgrade -y

# 2. Installera basics
sudo apt install -y vim htop curl git

# 3. Konfigurera brandvägg
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable

# 4. Skapa deploy-user
sudo useradd -m -s /bin/bash deploy
sudo usermod -aG sudo deploy`
                },
                {
                    type: 'tip',
                    title: 'DevOps One-Liners',
                    content: '**Senaste modifierade filer:**\n`find . -type f -mtime -1`\n\n**Räkna unika IP i logg:**\n`awk \'{print $1}\' access.log | sort | uniq -c | sort -rn | head`\n\n**Kolla memory-hogs:**\n`ps aux --sort=-%mem | head -10`'
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Quick Reference',
                    content: 'Du har nu en komplett snabbreferens! Använd dessa workflows för felsökning och dessa cheat sheets för tentaplugg.'
                }
            ]
        },

        {
            id: 'linux247-16-productivity',
            order: 16,
            title: 'Terminal Productivity',
            slug: 'terminal-productivity',
            description: 'Bli effektiv i terminalen',
            difficulty: 'medium',
            estimatedMinutes: 45,
            xpReward: 120,
            category: 'Produktivitet',
            icon: '⚡',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Använda keyboard shortcuts för snabbhet',
                        'Utnyttja command history effektivt',
                        'Skapa aliases för vanliga kommandon',
                        'Grundläggande tmux för sessioner',
                        'Bli 10x snabbare i terminalen'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Varför produktivitet spelar roll',
                    content: 'Som DevOps lever du i terminalen. Skillnaden mellan en nybörjare och ett proffs är inte vad de kan, utan hur snabbt de gör det. Dessa tricks sparar timmar varje vecka.'
                },
                {
                    type: 'code',
                    title: '⚡ Keyboard Shortcuts (MEMORERA!)',
                    language: 'bash',
                    code: `# NAVIGATION
Ctrl+A      # Gå till radens början
Ctrl+E      # Gå till radens slut
Ctrl+U      # Radera allt före cursor
Ctrl+K      # Radera allt efter cursor
Ctrl+W      # Radera ord bakåt
Ctrl+Y      # Klistra in raderat

# ⭐ SUPERANVÄNDBARA
Ctrl+R      # Sök i history (VIKTIG!)
Ctrl+L      # Rensa skärmen (= clear)
Ctrl+C      # Avbryt körande kommando
Ctrl+Z      # Pausa process (fg för fortsätt)
Ctrl+D      # Logga ut / EOF`
                },
                {
                    type: 'quiz',
                    question: 'Du vill hitta ett kommando du körde igår. Snabbaste sättet?',
                    options: ['history | grep kommando', 'Ctrl+R och börja skriva', 'Pil upp många gånger', 'cat ~/.bash_history'],
                    correctIndex: 1,
                    explanation: 'Ctrl+R startar reverse search. Börja skriva och bash hittar senaste matchningen. Tryck Ctrl+R igen för äldre matchningar.'
                },
                {
                    type: 'code',
                    title: 'History - Ditt minne',
                    language: 'bash',
                    code: `# Visa history
history
history 20      # Senaste 20

# ⭐ Kör tidigare kommando
!!              # Kör senaste kommando
!$              # Senaste argumentet
sudo !!         # Kör senaste med sudo

# Kör kommando #123 från history
!123

# Sök
history | grep ssh

# ⭐ CTRL+R - Interaktiv sökning
# Tryck Ctrl+R, börja skriv, Enter för att köra`
                },
                {
                    type: 'code',
                    title: 'Aliases - Dina genvägar',
                    language: 'bash',
                    code: `# Skapa alias (temporärt)
alias ll='ls -lah'
alias gs='git status'
alias dc='docker-compose'

# ⭐ Gör permanent - lägg i ~/.bashrc
echo "alias ll='ls -lah'" >> ~/.bashrc
echo "alias gs='git status'" >> ~/.bashrc
echo "alias update='sudo apt update && sudo apt upgrade -y'" >> ~/.bashrc

# Ladda om
source ~/.bashrc

# Visa alla aliases
alias`
                },
                {
                    type: 'quiz',
                    question: 'Du skapar alias gs="git status". Var lägger du det för att det ska finnas efter omstart?',
                    options: ['/etc/aliases', '~/.bashrc', '/etc/bash.bashrc', '~/.bash_aliases eller ~/.bashrc'],
                    correctIndex: 3,
                    explanation: 'Båda fungerar! ~/.bash_aliases är dedikerad för aliases, ~/.bashrc är mer generell. Ubuntu laddar ~/.bash_aliases automatiskt om den finns.'
                },
                {
                    type: 'code',
                    title: 'Tab Completion - Skriv mindre!',
                    language: 'bash',
                    code: `# ⭐ TAB = Autocomplete
cd /etc/ng<TAB>     # → /etc/nginx/
cat /var/log/sy<TAB>  # → /var/log/syslog

# Dubbel-TAB = Visa alternativ
cd /etc/<TAB><TAB>    # Visar alla kataloger

# Fungerar även för:
# - Kommandon
# - Filnamn
# - Git branches
# - SSH hosts (om konfigurerade)`
                },
                {
                    type: 'code',
                    title: 'tmux - Terminal multiplexer',
                    language: 'bash',
                    code: `# Installera
sudo apt install -y tmux

# Starta ny session
tmux
tmux new -s mysession

# ⭐ Detacha (lämna körande)
Ctrl+B, D

# Lista sessioner
tmux ls

# Återanslut
tmux attach
tmux attach -t mysession

# Döda session
tmux kill-session -t mysession

# ⭐ VIKTIGT: Processer i tmux överlever logout!`
                },
                {
                    type: 'code',
                    title: 'Praktiska produktivitetstips',
                    language: 'bash',
                    code: `# ⭐ Kör senaste kommando med sudo
sudo !!

# Upprepa argument
mkdir /var/www/myapp
cd !$    # = cd /var/www/myapp

# ⭐ Byt ut text i senaste kommando
^fel^rätt
# Exempel: cat /etc/nignx/nginx.conf
# ^nignx^nginx
# → cat /etc/nginx/nginx.conf

# Kör kommando i bakgrunden
./long-script.sh &

# Se senaste exitkod
echo $?`
                },
                {
                    type: 'tip',
                    title: 'DevOps Pro-Tips',
                    content: '**Mina favorit-aliases:**\n```bash\nalias ll="ls -lah"\nalias gs="git status"\nalias gp="git pull"\nalias dc="docker-compose"\nalias k="kubectl"\nalias tf="terraform"\n```\n\nLägg dessa i ~/.bashrc och njut!'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'Skriva långa kommandon om och om igen',
                    right: 'Använd Ctrl+R, aliases och tab completion',
                    explanation: 'Varje sekund räknas. Lär dig shortcuts så sparar du timmar varje vecka!'
                },
                {
                    type: 'mnemonic',
                    title: '🧠 Minnesregel',
                    concept: 'Bash-shortcuts',
                    trick: 'Ctrl+R = Reverse search, Ctrl+A/E = start/End',
                    example: 'Ctrl+R för att hitta gammalt kommando, Ctrl+A för att gå till början'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Produktivitet Snabbkoll',
                    commands: [
                        { cmd: 'Ctrl+R', desc: 'Sök i history' },
                        { cmd: '!!', desc: 'Kör senaste kommando' },
                        { cmd: 'sudo !!', desc: 'Senaste med sudo' },
                        { cmd: 'alias ll="ls -lah"', desc: 'Skapa alias' },
                        { cmd: 'tmux / Ctrl+B,D', desc: 'Ny session / detach' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Terminal Productivity',
                    content: 'Du har nu verktygen för att bli snabb! Ctrl+R för history, aliases för genvägar, och tmux för sessioner. Öva tills det blir muskelminne!'
                }
            ]
        },

        {
            id: 'linux247-17-users',
            order: 17,
            title: 'User & Group Management',
            slug: 'user-management',
            description: 'Hantera användare och grupper',
            difficulty: 'medium',
            estimatedMinutes: 45,
            xpReward: 120,
            category: 'Säkerhet',
            icon: '👥',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Skapa och ta bort användare',
                        'Hantera grupper',
                        'Ge sudo-rättigheter',
                        'Förstå /etc/passwd och /etc/shadow',
                        'Hantera lösenord'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Användare i Linux',
                    content: 'Varje process körs som en användare. Root har alla rättigheter, vanliga användare har begränsade. Som DevOps skapar du ofta deploy-användare, service-konton och hanterar sudo-access.'
                },
                {
                    type: 'code',
                    title: 'Skapa användare',
                    language: 'bash',
                    code: `# ⭐ Skapa användare med hemkatalog
sudo useradd -m username
sudo useradd -m -s /bin/bash deploy

# Sätt lösenord
sudo passwd username

# ⭐ One-liner: Skapa + hemkatalog + shell + lösenord
sudo useradd -m -s /bin/bash newuser
sudo passwd newuser

# Skapa utan login-möjlighet (för services)
sudo useradd -r -s /usr/sbin/nologin serviceuser`
                },
                {
                    type: 'quiz',
                    question: 'Du skapar användare "deploy" men kan inte logga in. Vad glömde du troligen?',
                    options: ['-m för hemkatalog', '-s /bin/bash för shell', 'sudo passwd deploy', 'Alla tre kan vara orsaken!'],
                    correctIndex: 3,
                    explanation: 'Utan -m finns ingen hemkatalog, utan -s kan shell vara /usr/sbin/nologin, och utan passwd finns inget lösenord. Alla tre behövs för en komplett användare!'
                },
                {
                    type: 'code',
                    title: 'Modifiera och ta bort användare',
                    language: 'bash',
                    code: `# Ändra shell
sudo usermod -s /bin/bash username

# Lägg till i grupp
sudo usermod -aG sudo username
sudo usermod -aG docker username

# ⭐ Lås användare (inaktivera)
sudo usermod -L username

# Lås upp
sudo usermod -U username

# Ta bort användare
sudo userdel username

# Ta bort användare + hemkatalog
sudo userdel -r username`
                },
                {
                    type: 'warning',
                    title: 'usermod -G vs -aG',
                    content: '-G ERSÄTTER alla grupper\n-aG LÄGGER TILL till befintliga grupper\n\nAnvänd ALLTID -aG om du inte vill ta bort användaren från alla andra grupper!'
                },
                {
                    type: 'code',
                    title: 'Grupper',
                    language: 'bash',
                    code: `# Visa vilka grupper user tillhör
groups username
id username

# Skapa grupp
sudo groupadd developers

# ⭐ Lägg till user i grupp
sudo usermod -aG developers username

# Ta bort user från grupp
sudo gpasswd -d username developers

# Ta bort grupp
sudo groupdel developers

# Lista alla grupper
cat /etc/group`
                },
                {
                    type: 'quiz',
                    question: 'Hur ger du användare "deploy" sudo-rättigheter?',
                    options: [
                        'sudo adduser deploy',
                        'usermod -aG sudo deploy',
                        'passwd deploy sudo',
                        'chmod +s deploy'
                    ],
                    correctIndex: 1,
                    explanation: 'Gruppen "sudo" har sudo-rättigheter på Ubuntu/Debian. usermod -aG sudo lägger till användaren i denna grupp.'
                },
                {
                    type: 'code',
                    title: 'Sudo-konfiguration',
                    language: 'bash',
                    code: `# ⭐ Lägg till i sudo-grupp (Ubuntu/Debian)
sudo usermod -aG sudo username

# På Red Hat/CentOS: wheel-gruppen
sudo usermod -aG wheel username

# Editera sudoers säkert
sudo visudo

# Ge specifik användare sudo utan lösenord
# Lägg till i /etc/sudoers:
# deploy ALL=(ALL) NOPASSWD: ALL

# ⭐ Bättre: Skapa fil i /etc/sudoers.d/
echo "deploy ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/deploy`
                },
                {
                    type: 'code',
                    title: 'Viktiga filer',
                    language: 'bash',
                    code: `# ⭐ /etc/passwd - Användarinfo
cat /etc/passwd
# username:x:1000:1000:Full Name:/home/username:/bin/bash
# user:lösenord:UID:GID:kommentar:hem:shell

# /etc/shadow - Lösenord (krypterade)
sudo cat /etc/shadow

# /etc/group - Grupper
cat /etc/group
# sudo:x:27:user1,user2

# ⭐ Visa info om användare
id username
getent passwd username`
                },
                {
                    type: 'code',
                    title: 'Praktiska DevOps-mönster',
                    language: 'bash',
                    code: `# ⭐ Skapa deploy-user för automation
sudo useradd -m -s /bin/bash deploy
sudo usermod -aG sudo deploy
echo "deploy ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/deploy

# Sätt upp SSH-nyckel för deploy
sudo mkdir -p /home/deploy/.ssh
sudo cp ~/.ssh/authorized_keys /home/deploy/.ssh/
sudo chown -R deploy:deploy /home/deploy/.ssh
sudo chmod 700 /home/deploy/.ssh
sudo chmod 600 /home/deploy/.ssh/authorized_keys

# Skapa service-användare (utan login)
sudo useradd -r -s /usr/sbin/nologin appuser`
                },
                {
                    type: 'tip',
                    title: 'Best Practice: Användare',
                    content: '**Principer:**\n- En användare per person/service\n- Ge minimala rättigheter\n- Använd grupper för gemensamma rättigheter\n- Undvik att köra services som root\n- Dokumentera varför användare finns'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'usermod -G sudo user (tar bort från alla andra grupper!)',
                    right: 'usermod -aG sudo user',
                    explanation: 'Utan -a (append) ersätts alla grupper! Användaren förlorar tillgång till docker, etc.'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Användare Snabbkoll',
                    commands: [
                        { cmd: 'useradd -m -s /bin/bash user', desc: 'Skapa användare' },
                        { cmd: 'passwd user', desc: 'Sätt lösenord' },
                        { cmd: 'usermod -aG sudo user', desc: 'Ge sudo-rättigheter' },
                        { cmd: 'id user', desc: 'Visa info' },
                        { cmd: 'userdel -r user', desc: 'Ta bort + hemkatalog' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: User Management',
                    content: 'Du kan nu hantera användare! useradd skapar, usermod -aG lägger till i grupp, och sudo-gruppen ger administratörsrättigheter.'
                }
            ]
        },

        {
            id: 'linux247-18-cron',
            order: 18,
            title: 'Cron Jobs & Scheduling',
            slug: 'cron-scheduling',
            description: 'Schemalägg uppgifter automatiskt',
            difficulty: 'medium',
            estimatedMinutes: 40,
            xpReward: 110,
            category: 'Automation',
            icon: '⏰',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Förstå cron-syntaxen',
                        'Skapa och hantera cron jobs',
                        'Vanliga schemaläggningar',
                        'Felsöka cron-problem',
                        'Grundläggande systemd timers'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Varför cron?',
                    content: 'Cron kör uppgifter automatiskt på schema - backup varje natt, logrotation varje vecka, cleanup-scripts varje timme. Som DevOps använder du cron för allt som ska köras regelbundet utan manuell insats.'
                },
                {
                    type: 'code',
                    title: 'Cron-syntaxen (MEMORERA!)',
                    language: 'bash',
                    code: `# ┌───────────── minut (0-59)
# │ ┌─────────── timme (0-23)
# │ │ ┌───────── dag i månaden (1-31)
# │ │ │ ┌─────── månad (1-12)
# │ │ │ │ ┌───── veckodag (0-7, 0=söndag)
# │ │ │ │ │
# * * * * * kommando

# Exempel:
# 30 2 * * *     # 02:30 varje dag
# 0 * * * *      # Varje hel timme
# */5 * * * *    # Var 5:e minut
# 0 0 * * 0      # Midnatt varje söndag`
                },
                {
                    type: 'quiz',
                    question: 'Vad betyder cron-uttrycket: 0 3 * * 1',
                    options: [
                        'Kl 03:00 den 1:a varje månad',
                        'Kl 03:00 varje måndag',
                        'Var 3:e timme på måndagar',
                        'Den 3:e minuten varje timme'
                    ],
                    correctIndex: 1,
                    explanation: 'minut=0, timme=3, dag=*, månad=*, veckodag=1 (måndag). Alltså: kl 03:00 varje måndag.'
                },
                {
                    type: 'code',
                    title: 'Crontab - Hantera jobb',
                    language: 'bash',
                    code: `# ⭐ Editera din crontab
crontab -e

# Lista dina cron jobs
crontab -l

# Ta bort alla dina cron jobs
crontab -r

# Editera annan användares crontab
sudo crontab -u deploy -e

# Lista root's crontab
sudo crontab -l`
                },
                {
                    type: 'code',
                    title: 'Vanliga exempel',
                    language: 'bash',
                    code: `# ⭐ Backup varje natt kl 02:00
0 2 * * * /scripts/backup.sh

# Loggrotation varje söndag kl 04:00
0 4 * * 0 /scripts/rotate-logs.sh

# Hälsokontroll var 5:e minut
*/5 * * * * /scripts/health-check.sh

# Månadsrapport första dagen kl 06:00
0 6 1 * * /scripts/monthly-report.sh

# ⭐ Vardagar kl 09:00
0 9 * * 1-5 /scripts/workday-task.sh`
                },
                {
                    type: 'code',
                    title: 'System cron-kataloger',
                    language: 'bash',
                    code: `# Fördefinierade scheman (lägg scripts här)
/etc/cron.hourly/    # Körs varje timme
/etc/cron.daily/     # Körs dagligen
/etc/cron.weekly/    # Körs varje vecka
/etc/cron.monthly/   # Körs varje månad

# ⭐ Exempel: Daglig backup
sudo cp backup.sh /etc/cron.daily/
sudo chmod +x /etc/cron.daily/backup.sh

# System crontab (editera försiktigt!)
cat /etc/crontab`
                },
                {
                    type: 'quiz',
                    question: 'Du vill köra ett script varje timme. Enklaste sättet?',
                    options: [
                        'Editera crontab med "0 * * * *"',
                        'Lägg scriptet i /etc/cron.hourly/',
                        'Båda fungerar!',
                        'Skapa systemd timer'
                    ],
                    correctIndex: 2,
                    explanation: 'Både crontab och /etc/cron.hourly/ fungerar! cron.hourly är enklare för enkla scripts, crontab ger mer kontroll.'
                },
                {
                    type: 'code',
                    title: 'Felsökning av cron',
                    language: 'bash',
                    code: `# ⭐ Logga output till fil
0 2 * * * /scripts/backup.sh >> /var/log/backup.log 2>&1

# Se cron-loggar
grep CRON /var/log/syslog

# Vanliga problem:
# 1. PATH - cron har minimal PATH
# 2. Permissions - script måste vara körbart
# 3. Absoluta paths - använd alltid fulla sökvägar

# ⭐ Best practice: Sätt PATH i crontab
PATH=/usr/local/bin:/usr/bin:/bin
0 2 * * * backup.sh`
                },
                {
                    type: 'warning',
                    title: 'Vanliga cron-fällor',
                    content: '**1. PATH**: Cron har minimal PATH - använd absoluta sökvägar!\n**2. Tyst fail**: Utan logging ser du inte fel\n**3. % tecken**: % är special i cron - escape med \\\n**4. Email**: Cron mailar output - kan fylla disk!'
                },
                {
                    type: 'code',
                    title: 'Komplett exempel',
                    language: 'bash',
                    code: `# ⭐ Professionell crontab setup
# crontab -e

# Sätt PATH
PATH=/usr/local/bin:/usr/bin:/bin

# Ingen email-output
MAILTO=""

# Backup varje natt, logga till fil
0 2 * * * /home/deploy/scripts/backup.sh >> /var/log/backup.log 2>&1

# Health check var 5:e minut
*/5 * * * * /home/deploy/scripts/healthcheck.sh >> /var/log/health.log 2>&1

# Cleanup varje söndag
0 3 * * 0 /home/deploy/scripts/cleanup.sh >> /var/log/cleanup.log 2>&1`
                },
                {
                    type: 'tip',
                    title: 'Crontab Generator',
                    content: 'Använd https://crontab.guru för att testa och förstå cron-uttryck! Skriv in uttrycket och se när det körs.'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: '0 2 * * * backup.sh (relativ path)',
                    right: '0 2 * * * /full/path/to/backup.sh',
                    explanation: 'Cron har annan PATH än din shell. Använd ALLTID absoluta sökvägar!'
                },
                {
                    type: 'mnemonic',
                    title: '🧠 Minnesregel',
                    concept: 'Cron-fält',
                    trick: 'Minut Timme Dag Månad Veckodag (MTDMV)',
                    example: '30 2 * * 1 = 02:30 varje måndag'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Cron Snabbkoll',
                    commands: [
                        { cmd: 'crontab -e', desc: 'Editera crontab' },
                        { cmd: 'crontab -l', desc: 'Lista cron jobs' },
                        { cmd: '*/5 * * * *', desc: 'Var 5:e minut' },
                        { cmd: '0 2 * * *', desc: 'Kl 02:00 dagligen' },
                        { cmd: '0 0 * * 0', desc: 'Midnatt söndagar' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Cron Jobs',
                    content: 'Du kan nu schemalägga uppgifter! crontab -e för att editera, och kom ihåg: absoluta paths och logga output!'
                }
            ]
        },

        {
            id: 'linux247-19-scripting',
            order: 19,
            title: 'Shell Scripting Fundamentals',
            slug: 'shell-scripting',
            description: 'Grundläggande Bash-scripting',
            difficulty: 'hard',
            estimatedMinutes: 60,
            xpReward: 160,
            category: 'Automation',
            icon: '📜',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Skapa och köra bash-scripts',
                        'Använda variabler och argument',
                        'Villkor med if/else',
                        'Loopar med for och while',
                        'Skapa återanvändbara funktioner'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Varför scripting?',
                    content: 'Scripts automatiserar repetitiva uppgifter. Deploy-scripts, backup-scripts, health-checks - allt som du gör mer än en gång bör vara ett script. Som DevOps är scripting en av dina viktigaste skills.'
                },
                {
                    type: 'code',
                    title: 'Grundläggande struktur',
                    language: 'bash',
                    code: `#!/bin/bash
# ⭐ Shebang - talar om vilken tolk som ska användas

# Kommentar
echo "Hello, DevOps!"

# Gör scriptet körbart:
# chmod +x script.sh

# Kör scriptet:
# ./script.sh
# eller
# bash script.sh`
                },
                {
                    type: 'code',
                    title: 'Variabler',
                    language: 'bash',
                    code: `#!/bin/bash

# ⭐ Sätta variabler (INGET mellanslag runt =)
NAME="DevOps"
COUNT=10
TODAY=$(date +%Y-%m-%d)

# Använda variabler
echo "Hello, $NAME"
echo "Today is $TODAY"

# ⭐ Curly braces för tydlighet
echo "\${NAME}_backup"   # DevOps_backup

# Environment variables
echo "User: $USER"
echo "Home: $HOME"`
                },
                {
                    type: 'quiz',
                    question: 'Varför fungerar inte: NAME = "test"?',
                    options: [
                        'NAME är reserverat',
                        'Mellanslag runt = är inte tillåtet',
                        'Citattecken behövs inte',
                        'Bör vara name istället för NAME'
                    ],
                    correctIndex: 1,
                    explanation: 'I bash får det INTE finnas mellanslag runt =. Korrekt: NAME="test"'
                },
                {
                    type: 'code',
                    title: 'Script-argument',
                    language: 'bash',
                    code: `#!/bin/bash
# ⭐ Argument nås via $1, $2, etc.

echo "Script name: $0"
echo "First arg: $1"
echo "Second arg: $2"
echo "All args: $@"
echo "Number of args: $#"

# Exempel: ./deploy.sh prod v1.2.3
# $1 = prod
# $2 = v1.2.3

# ⭐ Kolla om argument saknas
if [ -z "$1" ]; then
    echo "Usage: $0 <environment>"
    exit 1
fi`
                },
                {
                    type: 'code',
                    title: 'if/else - Villkor',
                    language: 'bash',
                    code: `#!/bin/bash

# ⭐ Grundläggande if
if [ "$1" == "prod" ]; then
    echo "Deploying to production"
fi

# if/else
if [ -f "/etc/nginx/nginx.conf" ]; then
    echo "Nginx config exists"
else
    echo "Nginx config NOT found"
fi

# if/elif/else
if [ "$ENV" == "prod" ]; then
    echo "Production"
elif [ "$ENV" == "staging" ]; then
    echo "Staging"
else
    echo "Development"
fi`
                },
                {
                    type: 'code',
                    title: 'Test-operatorer',
                    language: 'bash',
                    code: `# ⭐ Filer
[ -f fil ]     # Fil finns
[ -d dir ]     # Katalog finns
[ -x fil ]     # Fil är körbar
[ -r fil ]     # Fil är läsbar

# Strängar
[ -z "$var" ]  # Sträng är tom
[ -n "$var" ]  # Sträng är INTE tom
[ "$a" == "$b" ]  # Strängar är lika

# ⭐ Tal (numerisk jämförelse)
[ "$a" -eq "$b" ]  # equal (lika)
[ "$a" -ne "$b" ]  # not equal
[ "$a" -gt "$b" ]  # greater than
[ "$a" -lt "$b" ]  # less than

# Kombinera
[ -f fil ] && [ -r fil ]  # Finns OCH läsbar`
                },
                {
                    type: 'quiz',
                    question: 'Hur kollar du om variabeln $ENV är tom?',
                    options: ['if [ $ENV == "" ]', 'if [ -z "$ENV" ]', 'if [ empty $ENV ]', 'if [ $ENV -eq 0 ]'],
                    correctIndex: 1,
                    explanation: '-z testar om strängen är tom (zero length). Kom ihåg citattecken runt variabeln!'
                },
                {
                    type: 'code',
                    title: 'for-loop',
                    language: 'bash',
                    code: `#!/bin/bash

# ⭐ Loopa över lista
for server in web1 web2 web3; do
    echo "Deploying to $server"
    ssh $server "systemctl restart nginx"
done

# Loopa över filer
for file in *.log; do
    echo "Processing $file"
done

# ⭐ Loopa med sekvens
for i in {1..5}; do
    echo "Iteration $i"
done

# C-style loop
for ((i=0; i<10; i++)); do
    echo "Count: $i"
done`
                },
                {
                    type: 'code',
                    title: 'while-loop',
                    language: 'bash',
                    code: `#!/bin/bash

# ⭐ while-loop
COUNT=0
while [ $COUNT -lt 5 ]; do
    echo "Count: $COUNT"
    COUNT=$((COUNT + 1))
done

# Läs fil rad för rad
while read line; do
    echo "Line: $line"
done < servers.txt

# ⭐ Vänta tills service är uppe
while ! curl -s http://localhost:8080/health > /dev/null; do
    echo "Waiting for service..."
    sleep 2
done
echo "Service is up!"`
                },
                {
                    type: 'code',
                    title: 'Funktioner',
                    language: 'bash',
                    code: `#!/bin/bash

# ⭐ Definiera funktion
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Funktion med argument
deploy() {
    local ENV=$1
    local VERSION=$2
    log "Deploying $VERSION to $ENV"
    # Deploy-logik här
}

# ⭐ Anropa funktioner
log "Starting deployment"
deploy "prod" "v1.2.3"
log "Done"`
                },
                {
                    type: 'code',
                    title: 'Komplett deploy-script',
                    language: 'bash',
                    code: `#!/bin/bash
set -e  # Avbryt vid fel

# ⭐ Variabler
ENV=\${1:-staging}  # Default till staging
APP_DIR="/var/www/app"

# Funktioner
log() { echo "[$(date '+%H:%M:%S')] $1"; }

check_requirements() {
    if ! command -v git &> /dev/null; then
        log "ERROR: git not found"
        exit 1
    fi
}

deploy() {
    log "Deploying to $ENV..."
    cd $APP_DIR
    git pull origin main
    systemctl restart app
    log "Deploy complete!"
}

# ⭐ Main
log "Starting deploy to $ENV"
check_requirements
deploy
log "All done!"`
                },
                {
                    type: 'warning',
                    title: 'set -e',
                    content: 'Lägg "set -e" i början av scripts! Detta gör att scriptet avbryts om något kommando misslyckas. Utan detta fortsätter scriptet även efter fel.'
                },
                {
                    type: 'tip',
                    title: 'DevOps Script Best Practices',
                    content: '**1.** Börja med `set -e` (avbryt vid fel)\n**2.** Validera input/argument\n**3.** Använd funktioner för återanvändning\n**4.** Logga vad som händer\n**5.** Testa i staging först!'
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'if [ $VAR == "test" ] (variabel utan quotes)',
                    right: 'if [ "$VAR" == "test" ]',
                    explanation: 'Om VAR är tom blir det syntaxfel. Använd ALLTID quotes runt variabler i tester!'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Scripting Snabbkoll',
                    commands: [
                        { cmd: '#!/bin/bash', desc: 'Shebang (första raden)' },
                        { cmd: 'set -e', desc: 'Avbryt vid fel' },
                        { cmd: '[ -f fil ]', desc: 'Fil finns' },
                        { cmd: '[ -z "$var" ]', desc: 'Variabel tom' },
                        { cmd: 'for x in a b c; do', desc: 'For-loop' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Shell Scripting',
                    content: 'Du kan nu skriva bash-scripts! Variabler, villkor, loopar och funktioner. Börja automatisera dina repetitiva uppgifter!'
                }
            ]
        },

        {
            id: 'linux247-20-troubleshooting',
            order: 20,
            title: 'Troubleshooting & Debugging',
            slug: 'troubleshooting',
            description: 'Systematisk felsökning',
            difficulty: 'hard',
            estimatedMinutes: 55,
            xpReward: 150,
            category: 'Avancerat',
            icon: '🔍',
            content_blocks: [
                {
                    type: 'intro',
                    title: 'Lärandemål',
                    objectives: [
                        'Systematisk felsökningsmetodik',
                        'Diagnostisera vanliga problem',
                        'Använda debug-verktyg',
                        'Analysera performance-problem',
                        'Bygga mental modell för felsökning'
                    ]
                },
                {
                    type: 'concept',
                    title: 'Felsökningsmentalitet',
                    content: 'Felsökning är en systematisk process, inte gissning. Samla data, forma hypotes, testa, upprepa. De bästa DevOps-ingenjörerna är metodiska - de vet VAR de ska titta och i vilken ORDNING.'
                },
                {
                    type: 'code',
                    title: '⭐ WORKFLOW: Tjänst svarar inte',
                    language: 'bash',
                    code: `# 1. Är processen igång?
systemctl status nginx
ps aux | grep nginx

# 2. Lyssnar den på rätt port?
ss -tuln | grep :80

# 3. Vad säger loggarna?
journalctl -u nginx -n 50 --no-pager
tail -50 /var/log/nginx/error.log

# 4. Är det brandväggen?
ufw status
iptables -L -n

# 5. Kan du nå lokalt?
curl -I http://localhost

# 6. DNS korrekt?
dig +short yourserver.com`
                },
                {
                    type: 'code',
                    title: '⭐ WORKFLOW: Server är långsam',
                    language: 'bash',
                    code: `# 1. Vad är load?
uptime
# load > antal CPU-kärnor = problem

# 2. CPU-användning?
top -c
# eller htop

# 3. Minne?
free -h
# Kolla "available", inte "free"

# 4. Disk I/O?
iostat -x 2 5
# %util > 80% = disk bottleneck

# 5. Vilken process äter resurser?
ps aux --sort=-%cpu | head -10
ps aux --sort=-%mem | head -10

# 6. Nätverks-I/O?
iftop
# eller
nethogs`
                },
                {
                    type: 'quiz',
                    question: 'Server är långsam. uptime visar "load average: 12.5, 10.2, 8.5" på 4-kärnig CPU. Vad betyder det?',
                    options: [
                        'Allt är bra, under 20',
                        'Svår överbelastning - load > CPU-kärnor',
                        'Minnet är fullt',
                        'Disken är full'
                    ],
                    correctIndex: 1,
                    explanation: 'Load average > antal CPU-kärnor = kö. 12.5 på 4 kärnor betyder ~3x överbelastning. Något köar och väntar på CPU.'
                },
                {
                    type: 'code',
                    title: '⭐ WORKFLOW: Disk full',
                    language: 'bash',
                    code: `# 1. Vilken partition är full?
df -h

# 2. Hitta stora kataloger
du -h --max-depth=1 / 2>/dev/null | sort -rh | head

# 3. Vanliga bovar
du -sh /var/log/*
du -sh /tmp/*

# 4. Hitta stora filer
find / -type f -size +100M 2>/dev/null

# 5. Städa
sudo journalctl --vacuum-size=100M
sudo apt clean
sudo rm -rf /tmp/*
# Rotera/ta bort gamla loggar

# 6. Kolla inode (många små filer)
df -i`
                },
                {
                    type: 'code',
                    title: '⭐ WORKFLOW: Kan inte ansluta till server',
                    language: 'bash',
                    code: `# 1. Ping
ping -c 4 server.com

# 2. DNS fungerar?
dig +short server.com
nslookup server.com

# 3. Traceroute - var fastnar det?
traceroute server.com

# 4. Port öppen?
nc -zv server.com 22
nc -zv server.com 80

# 5. Från servern - lyssnar tjänsten?
ss -tuln | grep :80

# 6. Brandvägg?
sudo ufw status
sudo iptables -L -n`
                },
                {
                    type: 'code',
                    title: '⭐ WORKFLOW: OOM (Out of Memory)',
                    language: 'bash',
                    code: `# 1. Kolla dmesg för OOM killer
dmesg | grep -i "out of memory"
dmesg | grep -i "killed process"

# 2. Nuvarande minnesanvändning
free -h
cat /proc/meminfo

# 3. Vilka processer äter minne?
ps aux --sort=-%mem | head -10

# 4. Swap-användning
swapon --show

# 5. Kortsiktig fix - döda minneshog
kill $(pgrep -f processnamn)

# 6. Långsiktig - analysera med:
top -o %MEM`
                },
                {
                    type: 'code',
                    title: 'Debug-verktyg',
                    language: 'bash',
                    code: `# ⭐ strace - Spåra system calls
strace -p PID
strace -f ./program

# lsof - Lista öppna filer
lsof -p PID
lsof -i :80    # Vem lyssnar på port 80

# tcpdump - Nätverkstrafik
sudo tcpdump -i eth0 port 80
sudo tcpdump -i any host 192.168.1.1

# ⭐ dmesg - Kernel-meddelanden
dmesg | tail -50
dmesg -T | grep -i error`
                },
                {
                    type: 'quiz',
                    question: 'En process hänger sig. Hur ser du vad den försöker göra?',
                    options: ['ps aux', 'top', 'strace -p PID', 'lsof -p PID'],
                    correctIndex: 2,
                    explanation: 'strace visar vilka system calls processen gör i realtid. Du kan se om den väntar på I/O, nätverk, etc.'
                },
                {
                    type: 'code',
                    title: 'Loggar - Din guldgruva',
                    language: 'bash',
                    code: `# ⭐ Systemloggar
journalctl -xe                      # Senaste med förklaringar
journalctl -u nginx --since "1h"    # Senaste timmen
journalctl -p err -b                # Endast fel sedan boot

# Var loggar finns
/var/log/syslog          # System (Ubuntu)
/var/log/messages        # System (RHEL)
/var/log/auth.log        # SSH, sudo
/var/log/nginx/          # Nginx
/var/log/apache2/        # Apache

# ⭐ Sök efter fel
grep -i error /var/log/syslog | tail -50
grep -i fail /var/log/auth.log | tail -20`
                },
                {
                    type: 'tip',
                    title: 'Felsökningens 5 steg',
                    content: '**1. Reproducera** - Kan du få felet att uppstå igen?\n**2. Samla data** - Loggar, metrics, status\n**3. Hypotes** - Vad kan vara fel?\n**4. Testa** - Verifiera hypotesen\n**5. Fixa & dokumentera** - Lös och skriv ner'
                },
                {
                    type: 'code',
                    title: 'Quick Health Check Script',
                    language: 'bash',
                    code: `#!/bin/bash
echo "=== SYSTEM HEALTH CHECK ==="
echo "Hostname: $(hostname)"
echo "Uptime: $(uptime -p)"
echo ""
echo "=== LOAD ==="
uptime
echo ""
echo "=== MEMORY ==="
free -h
echo ""
echo "=== DISK ==="
df -h | grep -v tmpfs
echo ""
echo "=== TOP PROCESSES (CPU) ==="
ps aux --sort=-%cpu | head -5
echo ""
echo "=== RECENT ERRORS ==="
journalctl -p err --since "1h ago" --no-pager | tail -10`
                },
                {
                    type: 'common_mistake',
                    title: '⚠️ Vanligt misstag',
                    wrong: 'Gissa och prova slumpmässiga lösningar',
                    right: 'Samla data först, forma hypotes, testa systematiskt',
                    explanation: 'Slumpmässig felsökning tar längre tid och kan göra saken värre. Var metodisk!'
                },
                {
                    type: 'cheat_sheet',
                    title: '📋 Felsökning Snabbkoll',
                    commands: [
                        { cmd: 'systemctl status svc', desc: 'Tjänststatus' },
                        { cmd: 'journalctl -xe', desc: 'Senaste loggar med förklaring' },
                        { cmd: 'ss -tuln', desc: 'Lyssnade portar' },
                        { cmd: 'ps aux --sort=-%cpu', desc: 'CPU-hungriga processer' },
                        { cmd: 'df -h && free -h', desc: 'Disk + minne snabbkoll' }
                    ]
                },
                {
                    type: 'checkpoint',
                    title: '🎉 Checkpoint: Troubleshooting',
                    content: 'Du har nu en systematisk approach till felsökning! Samla data, forma hypotes, testa. Med dessa verktyg kan du diagnostisera de flesta Linux-problem.'
                }
            ]
        }
    ]
}

// Helper functions
export function getLinux247TaskById(taskId: string): Linux247Task | undefined {
    return LINUX247_MODULE.tasks.find(t => t.id === taskId || t.slug === taskId)
}

export function getLinux247TaskByOrder(order: number): Linux247Task | undefined {
    return LINUX247_MODULE.tasks.find(t => t.order === order)
}

export function getLinux247TaskBySlug(slug: string): Linux247Task | undefined {
    return LINUX247_MODULE.tasks.find(t => t.slug === slug)
}

export function getAllLinux247Tasks(): Linux247Task[] {
    return LINUX247_MODULE.tasks
}

// Group tasks by category
export function getLinux247TasksByCategory(): Record<string, Linux247Task[]> {
    const grouped: Record<string, Linux247Task[]> = {}
    for (const task of LINUX247_MODULE.tasks) {
        if (!grouped[task.category]) {
            grouped[task.category] = []
        }
        grouped[task.category].push(task)
    }
    return grouped
}
